---
title: "基于 K1 AI CPU 大模型部署落地"
lang: zh
category: "比赛/高校竞赛教程/AI 大模型开发文档及案例集"
source_page: https://www.spacemit.com/community/document/info?nodepath=competition/%E7%AB%9E%E8%B5%9B%E6%95%99%E7%A8%8B/02_AI_%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%BC%80%E5%8F%91%E6%96%87%E6%A1%A3%E5%8F%8A%E6%A1%88%E4%BE%8B%E9%9B%86/01_%E5%9F%BA%E4%BA%8EK1_AI_CPU%E7%9A%84%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%83%A8%E7%BD%B2%E8%90%BD%E5%9C%B0.md&lang=zh
source_file: https://cdn-resource.spacemit.com/competition/docs-events/zh/竞赛教程/02_AI_大模型开发文档及案例集/01_基于K1_AI_CPU的大模型部署落地.md
updated: "2026-06-10 14:57:14"
---

# 基于 K1 AI CPU 大模型部署落地

## 1. 简介

本赛题要求基于进迭开源的 Llama.cpp 进行部署。本工程在此基础上，额外增加了对进迭时空 AI 扩展指令的支持，并针对 K1 芯片进行了多项优化。优化主要集中在张量计算引擎 GGML，其余均保持与 Llama.cpp 源码一致。

整体架构如下图所示。

![](../../../../_assets/docs-events/竞赛教程/02_AI_大模型开发文档及案例集/images/blockdiagram.png)

## 2. 编译使用

### 2.1  交叉编译

从进迭时空代码仓库拉取代码，切换到进迭时空开发分支，并使用脚本编译即可。详细编译流程如下：

``` shell
# clone 代码
git clone git@github.com:ggml-org/llama.cpp.git

# 编译
参考docs/build-riscv64-spacemit.md，进行工程编译
```

编译完以后，工具和库会被安装到build/installed。其结构如下：

![](../../../../_assets/docs-events/竞赛教程/02_AI_大模型开发文档及案例集/images/structure.png)

### 2.2 关键工具介绍 
| 功能       | 名字           |
|------------|----------------|
| 量化工具   | llama-quantize |
| benchmark工具 | llama-bench |

量化工具使用说明：

![](../../../../_assets/docs-events/竞赛教程/02_AI_大模型开发文档及案例集/images/help.png)

量化支持类型：

![](../../../../_assets/docs-events/竞赛教程/02_AI_大模型开发文档及案例集/images/types.png)
