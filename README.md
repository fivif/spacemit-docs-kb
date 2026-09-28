# 进迭时空（SpacemiT）文档知识库

进迭时空官方文档中心的完整离线镜像，**Markdown 源文件 + 本地化图片 + 可检索索引**。

- 来源：<https://www.spacemit.com/community/document>
- 文档总数：**1495 篇**（中文 805 · 英文 690）
- 正文格式：官方 Markdown 源文件（非 HTML 抠取）
- 抓取脚本：`_tools/crawl_spacemit_docs.py`（可重复执行，增量更新）

## 为什么用这个仓库

官方文档中心是 SPA，正文从 `cdn-resource.spacemit.com` 动态加载。本仓库直接抓取官方 Markdown 源文件，保留原始结构，并把图片本地化——断网、离线、喂 LLM 都能用。

## 目录结构

```
.
├── INDEX.md                 总索引：分类树 + 每篇文档链接 + 字数
├── README.md
├── zh/                      中文文档 805 篇（保持官方目录结构）
├── en/                      英文文档 690 篇
├── _assets/                 文档引用图片（按官方资源仓库镜像）
├── _meta/
│   ├── manifest.json        每篇元数据：标题/来源/更新时间/字数/章节锚点/sha256
│   ├── searchindex.jsonl    轻量检索索引（一行一篇，可直接喂检索）
│   └── stats.json           抓取统计与失败清单
└── _tools/
    ├── crawl_spacemit_docs.py   全量抓取 / 更新
    └── refetch_missing.py       缺失图片补抓 + 改写引用
```

中文文档含 8 大类：硬件 / 软件 / AI / 云 / 工具 / 比赛 / 教程 / 技术服务。

## 每篇文档的格式

正文头部带 front-matter，便于批量解析：

```yaml
---
title: "K3 数据手册"
lang: zh
category: "硬件/K 系列 AI CPU 芯片/K3/芯片产品文档"
source_page: https://www.spacemit.com/community/document/info?nodepath=...&lang=zh
source_file: https://cdn-resource.spacemit.com/hardware/docs-chip/zh/...
updated: "2026-08-27 14:43:33"
---
```

图片引用与站内跳转均已改写为**本地相对路径**，克隆后直接可读。

## 数据来源与抓取方式

| 用途 | 接口 |
|---|---|
| 文档树 | `https://www.spacemit.com/api-server/document/get-doc-tree?language=zh\|en` |
| 正文 | `https://cdn-resource.spacemit.com/<group>/<repo>/<lang>/<path>.md` |
| 兜底 | GitHub raw（`spacemit-com/docs-*`） |

均为官方公开接口，无需鉴权。

## 使用方式

### 检索

`_meta/searchindex.jsonl` 每行一篇，含标题、分类与全部章节标题：

```json
{"id": "zh/hardware/key_stone/k3/index.md", "lang": "zh", "title": "K3", "category": "...", "headings": ["产品简介", "数据手册"]}
```

### 更新

```bash
# 全量重新抓取（会覆盖本地改动）
python _tools/crawl_spacemit_docs.py --out . --langs zh,en --workers 16

# 只补失败图片并就地改写 Markdown 引用
python _tools/refetch_missing.py --kb . --apply
```

仅依赖 Python 3.9+ 标准库，无第三方包。

## 抓取统计

| 项目 | 数值 |
|---|---|
| 文档 | 1495 篇（正文完整率 1494/1495） |
| 图片引用 | 4419 处 |
| 图片文件 | 2838 个（按内容去重，中英共用） |
| 正文体积 | 18.6 MB |

### 已知缺失

- `courses/Linux/02_Linux_应用开发学习/code/readme.md` —— 上游本身是 0 字节空文件。
- 43 张配图在官方 CDN 与 GitHub 仓库中均不存在（OpenHarmony、K3 英文手册居多）。这些图在**官网页面上同样不显示**，属上游缺图。清单见 `_meta/stats.json` 的 `failures.images`。

## 版权

文档内容版权归**进迭时空（SpacemiT）**所有，本仓库仅为便于检索与离线阅读的镜像，请以[官方文档中心](https://www.spacemit.com/community/document)为准。
