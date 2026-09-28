---
title: "K3 CoM260 Kit 简介"
lang: zh
category: "硬件/生态硬件/K3 CoM260 Kit"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/eco/k3_com260/root_overview.md&lang=zh
source_file: https://cdn-resource.spacemit.com/hardware/eco/docs-product/zh/k3_com260/root_overview.md
updated: "2026-06-18 09:39:34"
---
# K3 CoM260 Kit 简介

**[PDF 版本](https://cdn-resource.spacemit.com/file/product/K3/K3-CoM260_brief_zh.pdf)**

**RISC-V 机器人全功能开发套装**

SpacemiT K3-CoM260 开发者套件将 8 核通用 CPU 与 8 核 AI CPU 集成于紧凑的核心模组与参考载板中，提供高达 60 TOPS 的 AI 算力与 130 KDMIPS 的通用计算能力，可流畅运行 300 亿参数级大模型，是一套面向端侧 AI 的完整开发与验证平台。该套件基于 RISC-V 架构，支持主流 AI 模型部署并遵循标准 CPU 编程范式，实现 AI 算法的零成本迁移，同时在硬件层面兼容 Orin Nano，适用于 AI 一体机、服务机器人及端侧自主智能体的工程化落地。

## 特性

- **高性能端侧 AI**
  60 TOPS 通用 AI 算力，支持 30B 级大模型流畅推理与多路并发应用

- **CPU + AI CPU 架构**
  通用 CPU 与 AI CPU 协同设计，兼顾系统计算与高性能推理需求

- **模组化设计**
  核心模组 + 通用载板形态，兼容 K3-CoM260 全系列，便于快速集成

- **开发者友好**
  遵循标准 CPU 编程范式，实现 AI 算法与系统软件的零成本迁移

- **RISC-V 前沿架构**
  全球首款支持 RVA23 标准的紧凑型 RISC-V 边缘计算平台

- **丰富标准接口**
  提供完善的高速 IO 与扩展接口，满足摄像头、传感器与外设接入

- **机器人系统安全**
  支持 OP-TEE 安全操作系统，芯片集成硬件安全引擎

- **工程化支持**
  支持定制软件、载板设计与整机工程化，加速产品落地

## 产品规格

|模块 | 描述 |
|:------|:------|
| 芯片 | SpacemiT K3 RISC-V AI 芯片 |
| CPU | 8 核 X100™ 64 位 RISC-V CPU<br>- 2 Clusters x 4 Cores/Cluster，每个 Cluster 拥有 4MB L2 共享缓存，并可跨 Cluster 访问<br>- 每个 X100 核具有 64KB I-Cache、64KB D-Cache<br>- 支持 RVA23 profile 标准<br>- 支持 RVV1.0，VLEN：256bit |
| AI 性能 | 8 核 A100™ AI 核心，提供 60 TOPS AI 算力<br>- 2 Clusters x 4 Cores/Cluster，每个 Cluster 内拥有 1MB L2 共享缓存和 1.5MB 专用加速缓存（TCM），并可跨 Cluster 访问<br>- 每个 A100 核具有 32KB I-Cache、32KB D-Cache<br>- 支持 RVV1.0，VLEN：1024bit |
| 硬件安全引擎 | 支持国际通用密码算法及中国商用密码算法 <br> - 哈希算法：SHA1 / SHA224 / SHA256、SM3 <br> - 对称加密算法：AES-128/192/256、SM4 <br> - 非对称加密算法：RSA-1024/2048/4096、ECC-128/256、512、SM2 |
| 安全系统方案 | 支持基于 HW-RoT 的 Secure Boot <br> 支持 RISC-V 架构（PMP/IOPMP 隔离机制）的 TEE 可信计算 <br> 支持 OP-TEE 安全操作系统 |
| GPU | 集成 3D-GPU，支持 Vulkan、OpenCL、OpenGLES |
| 内存 | 8GB/16GB/32GB 64 位 LPDDR5、6400MT/s |
| 存储 | 支持内部 UFS、SD 卡插槽及外置 NVMe |
| 视频编码 | 4K60（H.264/H.265） |
| 视频解码 | 1 x 4K120 (H.264/H.265/VP9)<br>2 x 4K60 (H.264/H.265/VP9)<br>8 x 1080p60 (H.264/H.265/VP9)<br>16 x 1080p30 (H.264/H.265/VP9) |
| 功耗 | 18W ~ 35W |

**参考载板**

|模块 | 描述 |
|:------|:------|
| 摄像头接口 | 2 x MIPI CSI-1.1 22 针摄像头连接器 |
| PCIe 接口 | M.2 Key M 插槽（支持 PCIe Gen3 ×4）<br>M.2 Key M 插槽（支持 PCIe Gen3 ×1）<br>M.2 Key E 插槽 |
| USB 接口 | USB Type-A 接口：4 × USB 3.0<br>USB Type-C 接口 |
| 网络接口 | 1 x 千兆以太网接口 |
| 显示接口 | 1 x DP 1.2 接口<br>1 x MIPI DSI-1.2 30 针显示屏连接器 |
| 其他 I/O 接口 | 40 针扩展接口（支持 UART、SPI、I2S、I2C、GPIO）<br>12 针按钮接口<br>4 针风扇接口<br>直流电源接口 |
| 机械尺寸 | 103mm x 90.5mm x 35mm (高度包含脚垫、载板、模块及散热方案) |

## 合作与采购咨询

- **商务电话**：0571-89000775
- **商务邮箱**：[business@spacemit.com](mailto:business@spacemit.com)