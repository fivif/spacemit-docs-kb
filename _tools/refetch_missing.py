#!/usr/bin/env python3
"""补抓：对 _meta/stats.json 里失败的图片逐级回退取回，并就地重写 Markdown 引用。

回退顺序：CDN 原样 -> 中英目录互换 -> GitHub raw。
命中后写入 _assets/ 并把正文里残留的远程 URL 替换为本地相对路径。

用法（在知识库目录下）：
  python _tools/refetch_missing.py --kb .            # 只诊断
  python _tools/refetch_missing.py --kb . --apply    # 诊断并写回
"""

from __future__ import annotations

import argparse
import json
import os
import posixpath
import re
import ssl
import sys
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/153.0.0.0 Safari/537.36"
SAFE_URL_CHARS = "%/:?&=#@+,;$!*'()[]~"
ILLEGAL_PATH_CHARS = re.compile(r'[<>:"|?*\x00-\x1f]')
LANG_SEGS = ("zh", "en")
ctx = ssl.create_default_context()


def safe_relpath(path: str) -> str:
    parts = []
    for seg in path.split("/"):
        seg = ILLEGAL_PATH_CHARS.sub("_", seg).strip().rstrip(".")
        if seg and seg not in (".", ".."):
            parts.append(seg)
    return "/".join(parts)


def local_asset_relpath(url: str) -> str:
    parts = [p for p in urllib.parse.unquote(urllib.parse.urlsplit(url).path).split("/") if p]
    if not parts:
        return "asset"
    repo_idx = next((i for i, p in enumerate(parts) if p.startswith("docs-")), None)
    if repo_idx is not None:
        repo, rest = parts[repo_idx], parts[repo_idx + 1 :]
    else:
        lang_idx = next((i for i, p in enumerate(parts) if p in LANG_SEGS and i > 0), None)
        if lang_idx is not None:
            repo, rest = parts[lang_idx - 1], parts[lang_idx + 1 :]
        else:
            repo, rest = parts[0], parts[1:]
    if rest and rest[0] in LANG_SEGS:
        rest = rest[1:]
    return safe_relpath(posixpath.join(repo, *rest)) if rest else safe_relpath(repo)


def fetch(url: str) -> bytes:
    req = urllib.request.Request(
        urllib.parse.quote(url, safe=SAFE_URL_CHARS),
        headers={"User-Agent": USER_AGENT, "Referer": "https://www.spacemit.com/community/document"},
    )
    with urllib.request.urlopen(req, timeout=15, context=ctx) as r:
        return r.read()


def gh_raw_candidates(url: str):
    """CDN 路径 -> GitHub raw 候选（main / master 分支都试）。"""
    parts = urllib.parse.unquote(urllib.parse.urlsplit(url).path).strip("/").split("/")
    for i, seg in enumerate(parts):
        if seg.startswith("docs-"):
            tail = "/".join(parts[i + 1 :])
            return [
                f"https://raw.githubusercontent.com/spacemit-com/{seg}/main/{tail}",
                f"https://raw.githubusercontent.com/spacemit-com/{seg}/master/{tail}",
            ]
    return []


def try_variants(url: str):
    """按优先级尝试，返回 (数据, 实际命中URL) 或 (None, 错误)。"""
    last = "unknown"
    candidates = [url]
    if "/en/" in url:
        candidates.append(url.replace("/en/", "/zh/"))
    elif "/zh/" in url:
        candidates.append(url.replace("/zh/", "/en/"))
    candidates += gh_raw_candidates(url)
    for cand in candidates:
        try:
            return fetch(cand), cand
        except Exception as exc:  # noqa: BLE001
            last = f"{type(exc).__name__}: {exc}"
    return None, last


def run_probe(url: str, idx: int, total: int):
    data, info = try_variants(url)
    status = "OK" if data else "MISS"
    tag = ""
    if data:
        tag = "cdn" if info == url else ("github" if "githubusercontent" in info else "langswap")
    print(f"  [{idx}/{total}] {status:4s} {tag:9s} {url.split('cdn-resource.spacemit.com/')[-1]}", flush=True)
    return url, data, info


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", default=".", help="知识库目录")
    ap.add_argument("--apply", action="store_true", help="把取回的图写盘并改写 Markdown")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    kb = os.path.abspath(args.kb)
    stats_path = os.path.join(kb, "_meta", "stats.json")
    if not os.path.exists(stats_path):
        print(f"找不到 {stats_path}", file=sys.stderr)
        return 2
    stats = json.load(open(stats_path, encoding="utf-8"))
    fails = list(stats["failures"]["images"])
    print(f"待处理失败图片：{len(fails)}", flush=True)

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = [ex.submit(run_probe, u, i + 1, len(fails)) for i, u in enumerate(fails)]
        results = [f.result() for f in futures]

    recovered = [(u, data, used) for u, data, used in results if data]
    lost = [(u, err) for u, data, err in results if not data]
    print(f"\n可恢复 {len(recovered)} / 彻底缺失 {len(lost)}", flush=True)
    for u, _, used in recovered[:15]:
        tag = "CDN" if used == u else ("GitHub" if "githubusercontent" in used else "语言互换")
        print(f"  [{tag}] {u.split('cdn-resource.spacemit.com/')[-1]}")

    if not args.apply:
        print("\n（仅诊断。加 --apply 写回）")
        return 0

    # 写图片 + 记录 URL 映射
    url_map = {}
    for url, data, used in recovered:
        rel = posixpath.join("_assets", safe_relpath(local_asset_relpath(url)))
        dest = os.path.join(kb, rel.replace("/", os.sep))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as fh:
            fh.write(data)
        url_map[url] = rel

    # 就地改写所有 Markdown 里残留的这些远程 URL
    patterns = {}
    for url, rel in url_map.items():
        patterns[url] = rel
        enc = urllib.parse.quote(url, safe=SAFE_URL_CHARS)
        if enc != url:
            patterns[enc] = urllib.parse.quote(rel, safe="/")

    changed_files = 0
    changed_refs = 0
    for lang in LANG_SEGS:
        root = os.path.join(kb, lang)
        for dirpath, _, files in os.walk(root):
            for fn in files:
                if not fn.endswith(".md"):
                    continue
                fp = os.path.join(dirpath, fn)
                with open(fp, encoding="utf-8") as fh:
                    text = fh.read()
                orig = text
                doc_rel = posixpath.join(*os.path.relpath(fp, kb).split(os.sep))
                for remote, local in patterns.items():
                    if remote in text:
                        target = posixpath.relpath(local, posixpath.dirname(doc_rel) or ".")
                        n = text.count(remote)
                        text = text.replace(remote, target)
                        changed_refs += n
                if text != orig:
                    with open(fp, "w", encoding="utf-8", newline="\n") as fh:
                        fh.write(text)
                    changed_files += 1

    # 更新 stats
    stats["failures"]["images"] = {u: e for u, e in lost}
    stats["refetch"] = {
        "recovered": len(recovered),
        "still_missing": len(lost),
        "md_files_updated": changed_files,
        "refs_replaced": changed_refs,
    }
    with open(stats_path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(stats, fh, ensure_ascii=False, indent=1)

    print(f"\n写回完成：新增/覆盖图片 {len(url_map)} 张，改写 {changed_files} 个 md，替换 {changed_refs} 处引用")
    print(f"仍缺失：{len(lost)}（上游确实没有）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
