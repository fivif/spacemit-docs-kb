#!/usr/bin/env python3
"""进迭时空（SpacemiT）官方文档知识库抓取工具。

数据来源（官方公开接口，无需登录）：
  1) 文档树：https://www.spacemit.com/api-server/document/get-doc-tree?language=zh|en
  2) 正文：  https://cdn-resource.spacemit.com/<group>/<repo>/<lang>/<path>.md
  3) 兜底：  上述地址缺漏时回落到 GitHub raw（spacemit-com/docs-*）

产物：
  <out>/zh/**.md   中文文档（保持官方目录结构 + front-matter）
  <out>/en/**.md   英文文档
  <out>/_assets/** 文档引用图片（按资源仓库镜像，中英共用同一份，跨文档去重）
  <out>/INDEX.md   总索引（分类树 + 每篇链接 + 字数）
  <out>/_meta/manifest.json      每篇元数据（标题/来源/更新时间/字数/章节/sha256）
  <out>/_meta/searchindex.jsonl  检索用轻量索引（一行一篇）
  <out>/_meta/stats.json         抓取统计与失败清单

用法：
  python _tools/crawl_spacemit_docs.py --out . --langs zh,en --workers 16
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import posixpath
import re
import ssl
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field

TREE_API = "https://www.spacemit.com/api-server/document/get-doc-tree?language={lang}"
DOC_PAGE = "https://www.spacemit.com/community/document/info?nodepath={path}&lang={lang}"
CDN_ROOT = "https://cdn-resource.spacemit.com"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
)
SAFE_URL_CHARS = "%/:?&=#@+,;$!*'()[]~"
ILLEGAL_PATH_CHARS = re.compile(r'[<>:"|?*\x00-\x1f]')
LANG_SEGS = ("zh", "en")
IMG_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".avif"}
IMG_MD_RE = re.compile(r'!\[([^\]]*)\]\(\s*([^)\s]+)(\s+"[^"]*")?\s*\)')
IMG_HTML_RE = re.compile(r'(<img\b[^>]*?\bsrc=")([^"]+)(")', re.IGNORECASE)
LINK_MD_RE = re.compile(r'(?<!!)\[([^\]]*)\]\(\s*([^)\s]+)(\s+"[^"]*")?\s*\)')
LINK_HTML_RE = re.compile(r'(<a\b[^>]*?\bhref=")([^"]+)(")', re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #
class Fetcher:
    """带重试与兜底策略的并发 HTTP 客户端。"""

    def __init__(self, workers: int = 16, retries: int = 4, timeout: int = 60):
        self.workers = workers
        self.retries = retries
        self.timeout = timeout
        self.ctx = ssl.create_default_context()
        self.lock = threading.Lock()
        self.stats = {"bytes": 0, "requests": 0, "retries": 0, "fallbacks": 0}

    @staticmethod
    def _encode(url: str) -> str:
        return urllib.parse.quote(url, safe=SAFE_URL_CHARS)

    def get(self, url: str) -> bytes:
        last: Exception | None = None
        for attempt in range(self.retries):
            try:
                req = urllib.request.Request(
                    self._encode(url),
                    headers={
                        "User-Agent": USER_AGENT,
                        "Referer": "https://www.spacemit.com/community/document",
                    },
                )
                with urllib.request.urlopen(req, timeout=self.timeout, context=self.ctx) as resp:
                    data = resp.read()
                with self.lock:
                    self.stats["requests"] += 1
                    self.stats["bytes"] += len(data)
                return data
            except urllib.error.HTTPError as exc:
                last = exc
                if exc.code in (403, 404, 410):  # 不存在，不重试
                    break
                with self.lock:
                    self.stats["retries"] += 1
                time.sleep(min(1.5 * (2**attempt), 15))
            except Exception as exc:  # noqa: BLE001
                last = exc
                with self.lock:
                    self.stats["retries"] += 1
                time.sleep(min(1.5 * (2**attempt), 15))
        raise last  # type: ignore[misc]

    def get_text(self, url: str) -> str:
        return self.get(url).decode("utf-8-sig", "replace")

    def get_doc_text(self, cdn: str, gh: str) -> tuple[str, str]:
        """取文档正文，CDN 缺漏时回落 GitHub raw。返回 (正文, 实际来源)。"""
        try:
            return self.get_text(cdn), "cdn"
        except Exception as exc:  # noqa: BLE001
            if not gh:
                raise
            raw = gh.replace("https://github.com/", "https://raw.githubusercontent.com/").replace("/blob/", "/")
            try:
                text = self.get_text(raw)
            except Exception:  # noqa: BLE001
                raise exc from None
            with self.lock:
                self.stats["fallbacks"] += 1
            return text, "github"

    def get_image(self, url: str) -> tuple[bytes, str]:
        """取图片；CDN 404 时尝试中英目录互换（站内部分链接语言段写错）。"""
        try:
            return self.get(url), url
        except Exception as exc:  # noqa: BLE001
            alt = url.replace("/zh/", "/en/") if "/zh/" in url else url.replace("/en/", "/zh/")
            if alt == url:
                raise
            try:
                data = self.get(alt)
            except Exception:  # noqa: BLE001
                raise exc from None
            with self.lock:
                self.stats["fallbacks"] += 1
            return data, alt

    def map(self, fn, items, desc: str):
        """并发执行 fn(item)，返回 ({item: 结果}, {item: 错误})。item 必须可哈希。"""
        results: dict = {}
        errors: dict = {}
        total = len(items)
        done = 0
        t0 = time.time()
        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            futures = {pool.submit(fn, it): it for it in items}
            for fut in as_completed(futures):
                item = futures[fut]
                done += 1
                try:
                    results[item] = fut.result()
                except Exception as exc:  # noqa: BLE001
                    errors[item] = f"{type(exc).__name__}: {exc}"
                if done % 50 == 0 or done == total:
                    rate = done / max(time.time() - t0, 1e-6)
                    print(f"  {desc}: {done}/{total} ({rate:.1f}/s, 失败 {len(errors)})", flush=True)
        return results, errors


# --------------------------------------------------------------------------- #
# 路径映射
# --------------------------------------------------------------------------- #
def safe_relpath(path: str) -> str:
    """转成各平台都合法的相对路径。"""
    parts = []
    for seg in path.split("/"):
        seg = ILLEGAL_PATH_CHARS.sub("_", seg).strip().rstrip(".")
        if seg and seg not in (".", ".."):
            parts.append(seg)
    return "/".join(parts)


def local_asset_relpath(url: str) -> str:
    """CDN 资源 URL -> _assets 下的镜像路径。

    以 `docs-*` 资源仓库段为根，去掉紧随其后的语言段，使中英文共用同一张图
    （CDN 上同一仓库 zh/en 目录内容大量重复）。
    """
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
    rel = safe_relpath(posixpath.join(repo, *rest)) if rest else safe_relpath(repo)
    # 拆掉不要的段名（只保留真实文件名前的目录）
    return rel


def asset_flat_name(url: str) -> str:
    """去掉语言段后的仓库内相对路径，用于内容一致性去重。"""
    return local_asset_relpath(url)


def doc_cdn_dir(cdn: str) -> str:
    """文档自身 CDN URL 的目录部分，相对图片引用以此为基准。"""
    return posixpath.dirname(cdn)


def rel_link(from_file: str, to_file: str) -> str:
    return posixpath.relpath(to_file, posixpath.dirname(from_file) or ".")


@dataclass
class Doc:
    lang: str
    path: str
    title: str
    name_path: str
    cdn: str
    update_time: str
    gh: str = field(default="")
    text: str = field(default="")
    source_used: str = field(default="cdn")


# --------------------------------------------------------------------------- #
# Markdown 处理
# --------------------------------------------------------------------------- #
def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :].lstrip("\n")
    return text


def first_heading(text: str) -> str:
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            return re.sub(r"[`*_]", "", m.group(2)).strip()
    return ""


def anchor_of(title: str) -> str:
    a = re.sub(r"[^\w\u4e00-\u9fff\- ]+", "", title.lower(), flags=re.UNICODE).strip()
    return a.replace(" ", "-") or "section"


def iter_markdown_headings(body: str):
    seen: dict = {}
    for line in body.splitlines():
        m = HEADING_RE.match(line)
        if not m:
            continue
        level = len(m.group(1))
        title = re.sub(r"`([^`]*)`", r"\1", m.group(2))
        title = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", title)
        title = re.sub(r"<[^>]+>", "", title).strip()
        anchor = anchor_of(title)
        n = seen.get(anchor, 0)
        seen[anchor] = n + 1
        yield level, title, anchor if n == 0 else f"{anchor}-{n}"


def resolve_asset_url(url: str, base_dir: str):
    """图片引用 -> 绝对 CDN URL。

    `base_dir` 是该文档**自身 CDN URL 的目录**，不能用文档树里的 `path`：
    后者缺少 `docs-*` 仓库段与语言段（courses/... 实际在 courses/docs-courses/zh/...），
    用它拼相对路径会得到 404。
    """
    if url.startswith("data:"):
        return None
    if url.startswith("http"):
        return url
    rel = url.split("#")[0].strip()
    if not rel:
        return None
    if rel.startswith("/"):
        return CDN_ROOT + rel
    return posixpath.normpath(posixpath.join(base_dir, rel))


def rewrite_doc(doc: Doc, asset_paths: dict):
    """重写正文中的图片与站内跳转，返回 (正文, 未解析引用列表)。"""
    body = strip_front_matter(doc.text)
    doc_rel = posixpath.join(doc.lang, doc.path)
    base_dir = doc_cdn_dir(doc.cdn)
    unresolved: list = []

    def asset_link(url: str):
        local = asset_paths.get(url)
        return rel_link(doc_rel, local) if local else None

    def sub_img(m: re.Match) -> str:
        alt, url, title = m.group(1), m.group(2), m.group(3) or ""
        if url.startswith("data:"):
            return m.group(0)
        repl = asset_link(resolve_asset_url(url, base_dir) or "")
        if repl is None:
            unresolved.append(url)
            return m.group(0)
        return f"![{alt}]({repl}{title})"

    def sub_img_html(m: re.Match) -> str:
        repl = asset_link(resolve_asset_url(m.group(2), base_dir) or "")
        if repl is None:
            unresolved.append(m.group(2))
            return m.group(0)
        return f"{m.group(1)}{repl}{m.group(3)}"

    def doc_target(url: str):
        """站内文档跳转 -> 本地相对链接。"""
        path = urllib.parse.urlsplit(url).path if url.startswith("http") else url
        if not path.startswith("/community/document"):
            return None
        q = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)
        nodepath = (q.get("nodepath") or [""])[0]
        if not nodepath:
            return None
        lang = (q.get("lang") or [doc.lang])[0]
        anchor = (q.get("anchor") or [""])[0]
        target = posixpath.join(lang, safe_relpath(urllib.parse.unquote(nodepath)))
        return rel_link(doc_rel, target) + (f"#{anchor}" if anchor else "")

    def sub_link(m: re.Match) -> str:
        repl = doc_target(m.group(2))
        return m.group(0) if repl is None else f"[{m.group(1)}]({repl}{m.group(3) or ''})"

    def sub_link_html(m: re.Match) -> str:
        repl = doc_target(m.group(2))
        return m.group(0) if repl is None else f"{m.group(1)}{repl}{m.group(3)}"

    body = IMG_MD_RE.sub(sub_img, body)
    body = IMG_HTML_RE.sub(sub_img_html, body)
    body = LINK_MD_RE.sub(sub_link, body)
    body = LINK_HTML_RE.sub(sub_link_html, body)
    return body, unresolved


def find_asset_urls(text: str, base_dir: str) -> set:
    """收集一篇文档引用的远程图片 URL。"""
    body = strip_front_matter(text)
    raw = {m.group(2) for m in IMG_MD_RE.finditer(body)}
    raw |= {m.group(2) for m in IMG_HTML_RE.finditer(body)}
    raw |= set(re.findall(r"(?:image|logo|cover)['\"]?\s*:\s*['\"]?(\S+)", body))
    out = set()
    for url in raw:
        url = url.strip().strip("\"'")
        if url.startswith("data:"):
            continue
        resolved = resolve_asset_url(url, base_dir)
        if resolved and "spacemit.com" in resolved:
            out.add(resolved)
    return {u for u in out if posixpath.splitext(urllib.parse.urlsplit(u).path)[1].lower() in IMG_EXTS}


# --------------------------------------------------------------------------- #
# 索引生成
# --------------------------------------------------------------------------- #
def build_index(langs, trees, manifest) -> str:
    lang_titles = {"zh": "中文文档", "en": "English Docs"}
    lines = [
        "# 进迭时空（SpacemiT）文档知识库",
        "",
        f"- 文档总数：**{len(manifest)}** 篇"
        f"（中文 {sum(1 for m in manifest if m['lang'] == 'zh')} · "
        f"英文 {sum(1 for m in manifest if m['lang'] == 'en')}）",
        f"- 抓取时间：{time.strftime('%Y-%m-%d %H:%M:%S')}",
        "- 来源：https://www.spacemit.com/community/document （进迭时空官方文档中心）",
        "- 正文为官方 Markdown 源文件；图片本地化到 `_assets/`；站内跳转已改写为本地相对路径。",
        "- 中文 8 大类：硬件 / 软件 / AI / 云 / 工具 / 比赛 / 教程 / 技术服务。",
        "",
    ]
    for lang in langs:
        lines += [f"## {lang_titles.get(lang, lang)}", ""]
        by_path = {m["path"]: m for m in manifest if m["lang"] == lang}

        def walk(nodes, depth):
            for node in nodes:
                if node.get("isDirectory"):
                    if depth <= 3:
                        lines.append(f"{'  ' * (depth - 1)}- **{node['name']}**")
                    walk(node.get("children") or [], depth + 1)
                else:
                    meta = by_path.get(node["path"])
                    if not meta or not node["docName"].lower().endswith(".md"):
                        continue
                    label = node.get("name") or meta["title"] or node["docName"]
                    href = urllib.parse.quote(meta["local"], safe="/")
                    lines.append(f"{'  ' * (depth - 1)}- [{label}]({href}) <sub>{meta['words']} 字</sub>")

        walk(trees[lang], 1)
        lines.append("")
    lines += [
        "## 配套文件",
        "",
        "- `_meta/manifest.json`：每篇文档的标题、来源、更新时间、字数、章节、sha256",
        "- `_meta/searchindex.jsonl`：标题 + 章节级轻量索引（一行一篇，可直接喂检索）",
        "- `_meta/stats.json`：抓取统计与失败清单",
        "- `_tools/crawl_spacemit_docs.py`：抓取/更新脚本，可重复执行",
        "",
        "重跑更新：`python _tools/crawl_spacemit_docs.py --out . --langs zh,en`",
        "",
    ]
    return "\n".join(lines)


def collect_docs(tree):
    docs = []

    def walk(nodes):
        for node in nodes:
            if node.get("isDirectory"):
                walk(node.get("children") or [])
            elif node.get("docName", "").lower().endswith(".md") and node.get("storgeAddress"):
                docs.append(node)

    walk(tree)
    return docs


# --------------------------------------------------------------------------- #
# 主流程
# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description="抓取进迭时空官方文档为 Markdown 知识库")
    ap.add_argument("--out", required=True, help="输出目录（知识库根目录）")
    ap.add_argument("--langs", default="zh,en", help="语言，逗号分隔，默认 zh,en")
    ap.add_argument("--workers", type=int, default=16, help="并发数，默认 16")
    ap.add_argument("--no-images", action="store_true", help="不下载图片")
    args = ap.parse_args()

    out_dir = os.path.abspath(args.out)
    langs = [x.strip() for x in args.langs.split(",") if x.strip()]
    fetcher = Fetcher(workers=args.workers)
    t0 = time.time()

    print("[1/5] 拉取文档树", flush=True)
    trees = {}
    for lang in langs:
        payload = json.loads(fetcher.get_text(TREE_API.format(lang=lang)))
        if payload.get("code") != 20000:
            print(f"  ! {lang} 接口异常：{payload.get('message')}", file=sys.stderr)
            return 2
        trees[lang] = payload.get("data") or []

    docs: list[Doc] = []
    seen_paths: set = set()
    for lang in langs:
        nodes = collect_docs(trees[lang])
        print(f"  {lang}: {len(nodes)} 篇 Markdown", flush=True)
        for n in nodes:
            key = (lang, n["path"])
            if key in seen_paths:
                continue
            seen_paths.add(key)
            docs.append(
                Doc(
                    lang=lang,
                    path=safe_relpath(n["path"]),
                    title=n.get("name") or "",
                    name_path=n.get("namePath") or "",
                    cdn=n["storgeAddress"],
                    update_time=n.get("updateTime") or "",
                    gh=n.get("url") or "",
                )
            )

    print(f"[2/5] 下载正文（{len(docs)} 篇，{args.workers} 并发）", flush=True)
    by_url = {d.cdn: d for d in docs}
    text_map, text_err = fetcher.map(
        lambda u: fetcher.get_doc_text(u, by_url[u].gh), list(by_url), "正文"
    )
    for url, d in by_url.items():
        got = text_map.get(url)
        if got:
            d.text, d.source_used = got
    failed_docs = [d for d in docs if not d.text]
    docs = [d for d in docs if d.text]
    print(f"  成功 {len(docs)} 篇（其中 GitHub 兜底 "
          f"{sum(1 for d in docs if d.source_used == 'github')} 篇），失败 {len(failed_docs)} 篇", flush=True)

    print("[3/5] 解析并下载图片", flush=True)
    asset_urls: set = set()
    for d in docs:
        asset_urls |= find_asset_urls(d.text, doc_cdn_dir(d.cdn))
    print(f"  引用图片：{len(asset_urls)} 个唯一 URL", flush=True)

    asset_paths: dict = {}   # URL -> _assets 下相对路径
    local_owner: dict = {}   # 本地路径 -> 已写入的 URL（同图不同语言变体只存一份）
    img_err: dict = {}
    img_fixed: dict = {}
    if asset_urls and not args.no_images:
        url_to_rel = {u: posixpath.join("_assets", local_asset_relpath(u)) for u in asset_urls}
        payloads, img_err = fetcher.map(lambda u: fetcher.get_image(u), sorted(asset_urls), "图片")
        for url, (data, used_url) in payloads.items():
            rel = url_to_rel[url]
            if rel not in local_owner:
                dest = os.path.join(out_dir, rel.replace("/", os.sep))
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as fh:
                    fh.write(data)
                local_owner[rel] = url
            asset_paths[url] = rel
            if used_url != url:
                img_fixed[url] = used_url
    else:
        print("  （跳过图片下载）", flush=True)

    print("[4/5] 写入 Markdown", flush=True)
    manifest = []
    unresolved_all: dict = {}
    for d in docs:
        body, unresolved = rewrite_doc(d, asset_paths)
        if unresolved:
            unresolved_all[d.path] = sorted(set(unresolved))
        title = first_heading(body) or d.title or posixpath.basename(d.path)
        headings = list(iter_markdown_headings(body))
        rel = posixpath.join(d.lang, d.path)
        category = d.name_path.rsplit("/", 1)[0] if "/" in d.name_path else ""
        fm = [
            "---",
            f"title: {json.dumps(title, ensure_ascii=False)}",
            f"lang: {d.lang}",
            f"category: {json.dumps(category, ensure_ascii=False)}",
            f"source_page: {DOC_PAGE.format(path=urllib.parse.quote(d.path, safe='/'), lang=d.lang)}",
            f"source_file: {d.cdn}",
            f"updated: {json.dumps(d.update_time, ensure_ascii=False)}",
            "---",
            "",
        ]
        dest = os.path.join(out_dir, rel.replace("/", os.sep))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(fm) + body)
        manifest.append(
            {
                "lang": d.lang,
                "path": d.path,
                "local": rel,
                "title": title,
                "category": category,
                "words": len(re.sub(r"\s+", "", body)),
                "headings": [{"level": lv, "title": t, "anchor": a} for lv, t, a in headings],
                "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
                "updated": d.update_time,
                "source": d.cdn,
                "source_used": d.source_used,
            }
        )

    print("[5/5] 生成索引与元数据", flush=True)
    meta_dir = os.path.join(out_dir, "_meta")
    os.makedirs(meta_dir, exist_ok=True)
    manifest.sort(key=lambda m: (m["lang"], m["local"]))
    with open(os.path.join(meta_dir, "manifest.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(meta_dir, "searchindex.jsonl"), "w", encoding="utf-8", newline="\n") as fh:
        for m in manifest:
            fh.write(
                json.dumps(
                    {
                        "id": m["local"],
                        "lang": m["lang"],
                        "title": m["title"],
                        "category": m["category"],
                        "headings": [h["title"] for h in m["headings"]],
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
    with open(os.path.join(out_dir, "INDEX.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(build_index(langs, trees, manifest))

    stats = {
        "crawled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "elapsed_sec": round(time.time() - t0, 1),
        "out_dir": out_dir,
        "docs_total": len(manifest),
        "docs_by_lang": {lang: sum(1 for m in manifest if m["lang"] == lang) for lang in langs},
        "assets_total": len(asset_paths),
        "assets_files": len(local_owner),
        "http": fetcher.stats,
        "failures": {
            "docs": {d.path: text_err.get(d.cdn, "empty body") for d in failed_docs},
            "images": {u: e for u, e in img_err.items()},
            "unresolved_refs": unresolved_all,
        },
        "image_lang_fixed": img_fixed,
    }
    with open(os.path.join(meta_dir, "stats.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(stats, fh, ensure_ascii=False, indent=1)

    print(
        f"完成：{len(manifest)} 篇 Markdown，{len(local_owner)} 张图片"
        f"（引用 {len(asset_paths)} 处），失败 文档{len(failed_docs)}/图片{len(img_err)}，"
        f"耗时 {stats['elapsed_sec']}s"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
