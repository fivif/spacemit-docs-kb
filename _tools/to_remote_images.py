#!/usr/bin/env python3
"""把正文里的本地图片引用（_assets/...）还原为官方 CDN 绝对地址。

用途：仓库想保持轻量、不提交 1.9 GB 图片，但又要让 Markdown 在 GitHub 上正常显示。
图片引用还原后可直接由 CDN 提供（已验证 CDN 允许热链，GitHub camo 可正常抓取）。

还原依据：每篇文档的 front-matter `source_file` 给出该文档的真实 CDN 地址，
据此取得 group / repo / lang 三段；本地 `_assets/<repo>/<rest>` 中的 <rest>
拼回 <group>/<repo>/<lang>/<rest> 即为原始 URL。

用法：
  python _tools/to_remote_images.py --kb .            # 预演，只统计不写
  python _tools/to_remote_images.py --kb . --apply    # 实际改写
"""

from __future__ import annotations

import argparse
import collections
import os
import posixpath
import re
import sys
import urllib.parse

CDN_ROOT = "https://cdn-resource.spacemit.com"
ARCHIVE_ROOT = "https://archive.spacemit.com"
SAFE_URL_CHARS = "%/:?&=#@+,;$!*'()[]~"
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
IMG_REF_RE = re.compile(r'(!\[[^\]]*\]\()([^)\s]+)((?:\s+"[^"]*")?\))')
IMG_SRC_RE = re.compile(r'(<img\b[^>]*?\bsrc=")([^"]+)(")', re.IGNORECASE)
LANG_SEGS = ("zh", "en")


def parse_front_matter(text: str) -> dict:
    m = FM_RE.match(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm


def split_cdn(url: str):
    """CDN 文档地址 -> (group, repo, lang)"""
    parts = [p for p in urllib.parse.unquote(urllib.parse.urlsplit(url).path).split("/") if p]
    repo_idx = next((i for i, p in enumerate(parts) if p.startswith("docs-")), None)
    if repo_idx is None or repo_idx == 0:
        return None
    group, repo = parts[repo_idx - 1], parts[repo_idx]
    lang = parts[repo_idx + 1] if len(parts) > repo_idx + 1 and parts[repo_idx + 1] in LANG_SEGS else "zh"
    return group, repo, lang


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", default=".", help="知识库目录")
    ap.add_argument("--apply", action="store_true", help="实际写回")
    args = ap.parse_args()

    kb = os.path.abspath(args.kb)
    stats = collections.Counter()
    cross_repo: list = []
    samples: list = []

    for lang in LANG_SEGS:
        root = os.path.join(kb, lang)
        if not os.path.isdir(root):
            continue
        for dirpath, _, files in os.walk(root):
            for fn in files:
                if not fn.endswith(".md"):
                    continue
                fp = os.path.join(dirpath, fn)
                with open(fp, encoding="utf-8") as fh:
                    text = fh.read()
                fm = parse_front_matter(text)
                src = fm.get("source_file", "")
                info = split_cdn(src) if src else None
                if not info:
                    stats["no_source_file"] += 1
                    continue
                group, repo, doc_lang = info
                doc_rel = posixpath.join(*os.path.relpath(fp, kb).split(os.sep))
                doc_dir = posixpath.dirname(doc_rel)

                def to_remote(local_ref: str):
                    """本地 _assets 引用 -> 原始 CDN 绝对地址；非本地引用返回 None。"""
                    if local_ref.startswith(("http://", "https://", "data:")):
                        return None
                    target = posixpath.normpath(posixpath.join(doc_dir, urllib.parse.unquote(local_ref.split("#")[0])))
                    if not target.startswith("_assets/"):
                        return None
                    rest = target[len("_assets/") :]
                    parts = rest.split("/", 1)
                    ref_repo = parts[0]
                    tail = parts[1] if len(parts) > 1 else ""
                    if not tail:
                        return None
                    # 1) /file/... 类公共附件
                    if ref_repo == "file":
                        return f"{CDN_ROOT}/file/{tail}"
                    # 2) ros2 演示视频实际托管在 archive 域，不在 cdn-resource
                    if ref_repo == "ros2":
                        return f"{ARCHIVE_ROOT}/ros2/{tail}"
                    if ref_repo != repo:
                        cross_repo.append((doc_rel, ref_repo, repo, local_ref))
                    # 3) 常规图片：文档自身 group + 资源仓库段 + 文档语言段
                    return f"{CDN_ROOT}/{group}/{ref_repo}/{doc_lang}/{tail}"

                new = text
                for m in IMG_REF_RE.finditer(text):
                    url = to_remote(m.group(2))
                    if url:
                        stats["md_image_rewritten"] += 1
                        if len(samples) < 5:
                            samples.append((doc_rel, m.group(2), url))
                        new = new.replace(m.group(0), f"{m.group(1)}{urllib.parse.quote(url, safe=SAFE_URL_CHARS)}{m.group(3)}")
                for m in IMG_SRC_RE.finditer(text):
                    url = to_remote(m.group(2))
                    if url:
                        stats["html_image_rewritten"] += 1
                        new = new.replace(m.group(0), f"{m.group(1)}{urllib.parse.quote(url, safe=SAFE_URL_CHARS)}{m.group(3)}")

                if new != text:
                    stats["md_files_changed"] += 1
                    if args.apply:
                        with open(fp, "w", encoding="utf-8", newline="\n") as fh:
                            fh.write(new)

    print("=== 统计 ===")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print(f"  跨仓库引用（可能拼错）: {len(cross_repo)}")
    for row in cross_repo[:8]:
        print("    ", row)
    if samples:
        print("=== 样例 ===")
        for doc, old, new in samples:
            print(f"  {doc}\n    {old}\n -> {new}")
    if not args.apply:
        print("\n（预演模式，未写盘。加 --apply 实际改写）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
