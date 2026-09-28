---
title: "K1 RISC-V 集群服务器简介"
lang: zh
category: "硬件/生态硬件/K1 RISC-V 集群服务器"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/eco/k1_muse_shelf/root_overview.md&lang=zh
source_file: https://cdn-resource.spacemit.com/hardware/eco/docs-product/zh/k1_muse_shelf/root_overview.md
updated: "2026-05-09 18:09:22"
---

# K1 RISC-V 集群服务器简介

**[PDF 版本](https://cdn-resource.spacemit.com/file/product/K1/MUSE_shelf_brief_zh.pdf)**

**为全球开发者开放的 RISC-V 云算力**

**MUSE Shelf** 是专为开发者群体设计的 RISC-V 开发服务器，具有全面计算、高效运维、高速互联、智能管理的特点；应用平台采用进迭云平台服务，提供高可用、强拓展、高性能的分布式云平台，提供基于 RISC-V 平台的应用开发或适配。

**MUSE Shelf** 旨在为全球开发者提供 RISC-V 计算实例，支持远程桌面、远程编译、一键刷机、一键应用安装等功能，让开发者可以随时随地地使用 RISC-V 算力并进行创意开发。

## 特性

- **高密度 RISC-V 计算集群**
  集成 80 颗进迭时空 RISC-V 八核处理器，提供面向开发与验证场景的大规模并行算力。

- **模组化刀片式架构**
  采用 2 / 4 刀片设计，支持灵活部署、快速维护与按需扩展。

- **标准化服务器形态**
  基于 2U 标准服务器框架设计，便于机房集成与规模化运维部署。

- **多方式开发调试支持**
  支持 SSH、UART、ADB 等调试方式，满足不同开发阶段的调试需求。

- **远程开发与交互能力**
  支持远程文件上传下载、VNC / RDP 投屏，实现完整的远程开发体验。

- **远程刷机与系统管理**
  支持远程 Fastboot 刷机及上下电控制，提升设备管理与系统迭代效率。

## 产品规格

| 模块 | 项目 | 描述  |
| :--- | :--- | :--- |
| **阵列机箱** | BMC | AC50-BMCS-SRV-RISCV-2.1.4 |
| | 云服务 | 进迭云平台 |
| | 形态 | 2U 机架式（4 刀片式） |
| | CPU 板卡数量 | 每刀片 20 路 CPU 板卡，共 4 刀片、80 路 K1 SOM 板卡 |
| **K1-SoM** | CPU | K1（8 核 RISC-V AI CPU，提供 50K DMIPS CPU 算力和 2.0 TOPS AI 算力） |
| | DRAM 容量 | 8 GB / 16 GB |
| | Flash 容量 | 64 GB / 128 GB |
| | 接口 | GbE / USB Device / UART |
| | 尺寸 | 47.10 mm × 64.10 mm |
| | PCB | 6 层通孔 |
| **交换系统** | 网络 | 每刀片 2 × 25 Gb SFP28 光口，共 4 个刀片、8 个光口，各刀片网络完全独立 |
| **电源** | 电源输入 | 1200 W 白金电源模块，支持热插拔，1 + 1 冗余备份 |
| **工作条件** | 工作温度 | 5 ℃ ~ 35 ℃ |
| | 工作湿度 | 40% ~ 60% |

## 合作与采购咨询

- **商务电话**：0571-89000775
- **商务邮箱**：[business@spacemit.com](mailto:business@spacemit.com)
- **产品购买**：[K1 MUSE Shelf（官方购买链接）](https://item.taobao.com/item.htm?id=807037514272)