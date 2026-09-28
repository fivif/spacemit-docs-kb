---
title: "K3 Shelf 阵列服务器简介"
lang: zh
category: "硬件/生态硬件/K3 Shelf N10/N48"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/eco/k3_shelf/root_overview.md&lang=zh
source_file: https://cdn-resource.spacemit.com/hardware/eco/docs-product/zh/k3_shelf/root_overview.md
updated: "2026-07-23 17:55:07"
---
# K3 Shelf 阵列服务器简介

**[PDF 版本](https://cdn-resource.spacemit.com/file/product/K3/k3-shelf_brief_zh.pdf)**

**原生 RISC-V 编译集群服务器 K3 Shelf**

进迭时空 K3 SHELF 分为 N10、N48 两款高密度机架服务器，基于自研 RVA23 架构 K3 芯片打造，单节点 8 核 X100 主频 2.4 GHz、60 TOPS 算力。依托原生 RISC-V 硬件架构，可配合 Koji、Open Build Server 等构建系统，原生编译性能远超 X86 平台 QEMU 仿真，效率提升 10 倍 +，极大缩减系统、固件与开源项目编译周期。整机单节点功耗仅 15-25 W，相较传统 X86 服务器省电 60%，配置四万兆网口 + 全套 BMC 管理，集成远程串口、云端调试功能，是 RISC-V 软件测试、源码编译集群、本地大模型部署、边缘计算的优选硬件。

## 特性

- **10 个/48 个 K3 计算节点**
   服务器内置多个 K3 计算节点，每个节点搭载 8 核 X100 RISC-V CPU（最高主频 2.4 GHz）和 8 核 A100 AI CPU，可提供高达 60 TOPS AI 算力

- **主流 Linux 发行版构建系统支持**
   支持 Open Build Server、Koji 等主流构建系统，原生编译性能相比 X86 QEMU 提升 10 倍以上

- **支持 RISC-V 软件兼容性测试**
   业界首款 RVA23 Profile 量产阵列服务器，支持主流 Linux 发行版、开源软件、AI 框架的兼容性测试

- **远程 RISC-V 云调试功能**
   配合云平台，支持远程自动刷机、远程串口调试、远程 SSH、WEB IDE、远程桌面实现开箱即用的云调试环境

- **极致能效比，绿色算力**
   12 个 K3 相当于一台中端 X86 工作站，单节点 15-25 W，2U 服务器 12 个节点总功耗仅 150-300 W，相比 X86 服务器节省 60% 电费

- **拥有 4 个万兆网口**
   拥有 4 个万兆网口（SFP+）、1 个 MGMT（BMC 管理网络接口），让网络通讯拥有更高的速率

- **配套 BMC 管理系统**
   配套 BMC 智能管理系统，轻松完成实时监控、软件配置、硬件管理、故障排除、系统升级，并可提供二次开发

- **广泛的应用场景**
   广泛适用于智算服务器、边缘计算、大模型本地化、智慧城市、智慧医疗、智慧工业、智能安防等类型产品和领域

## 产品规格（N10）

| 模块 | 项目 | 描述 |
| :--- | :--- | :--- |
| **技术规格** | 服务器形态 | 1U 机架式算力服务器 |
| | 构架 | RISC-V 架构 |
| | 节点数 | 10 个分布式计算点 + 1 个控制节点 |
| | 计算节点 | 八核 64 位处理器 X100，最高主频 2.4 GHz + 八核 AI 核支持 1024 bit 的 RVV 1.0 并行计算 |
| | 视频编码 | H.265/H.264：1 × 4K@60fps、8 × 1080P@30fps |
| | 视频解码 | 4K@120fps [H.264/H.265/VP9]/JPEG(MPEG4/MPEG2)、16 × 1080P@30fps |
| | 控制节点 | 八核 64 位处理器 X100，最高主频 2.4 GHz，八核 A100 可提供 60 TOPS AI 算力 |
| | AI 算力 | 600 TOPS（60 TOPS × 10，INT4） |
| | 内存 | 16 GB LPDDR5 × 10（16/32 GB） |
| | 存储 | 128 GB UFS × 10（16/32/64/128/256 GB） |
| | 扩展存储 | M.2 2280 PCIe NVMe SSD × 48（选配）、3.5 英寸/2.5 英寸 SATA 3.0 SSD 硬盘 × 1（支持热插拔；BMC 可直接操作硬盘，计算子节点可通过 BMC 提供的网络共享方式，间接访问硬盘） |
| | 电源 | 550 W AC 电源（输入：90 V AC～264 V AC，47 Hz～63 Hz，BA；不支持热插拔） |
| | 风扇模组 | 6 个高速散热风扇 |
| **物理规格** | 尺寸 | 440.5 mm（长）× 494.0 mm（宽）× 44.4 mm（高） |
| | 满配重量 | 服务器净重：8.1 kg，带包装总重：10.3 kg |
| | 环境 | 工作温度：0℃ - 35℃，存储温度：-40℃ - 60℃，工作湿度：5% - 80%RH（无凝露） |
| **软件参数** | BMC | 集成基于 Web 管理界面的 BMC 管理系统，支持监控、配置、告警、远程运维及虚拟媒体管理等功能，提供 CLI 命令行和 Redfish 等工具，便于二次开发 |
| | 大语言模型 | 支持 Transformer 架构下超大规模参数模型的私有化部署，如 Deepseek-R1 系列、Gemma 系列、Llama 系列、ChatGLM 系列、Qwen 系列、Phi 系列等大语言模型 |
| | 深度学习 | 支持 CNN、RNN、LSTM 等传统网络结构，支持多种深度学习框架，包括 TensorFlow、PyTorch、PaddlePaddle、ONNX、Caffe 等；支持自定义算子开发、Docker 容器化管理技术 |
| **接口参数** | 网络 | 4 × 10 Gbps 光网（SFP+）、1 × 千兆以太网（RJ45，MGMT 用作 BMC 管理网络） |
| | Console | 1 × Console（RJ45，BMC 调试串口，波特率 115200） |
| | 显示 | 1 × HDMI（最高分辨率 1080P，BMC 管理显示） |
| | USB | 2 × USB 3.0（下限 USB 为 USB 3.0 OTG，可使用 U 盘对 BMC 进行 OTG 升级） |
| | 按键 | 1 × 复位键、1 × 电源键、1 × 重启 BMC 键 |
| | 其他接口 | 1 × RS232（DB9，波特率为 115200）、1 × RS485（DB9，波特率为 115200） |

## 产品规格（N48）

| 模块 | 项目 | 描述 |
| :--- | :--- | :--- |
| **技术规格** | 服务器形态 | 2U 机架式算力服务器 |
| | 构架 | RISC-V 架构 |
| | 节点数 | 48 个分布式计算点 + 1 个控制节点 |
| | 计算节点 | 八核 64 位处理器 X100，最高主频 2.4 GHz + 八核 AI 核支持 1024 bit 的 RVV 1.0 并行计算 |
| | 视频编码 | H.265/H.264：1 × 4K@60fps、8 × 1080P@30fps |
| | 视频解码 | 4K@120fps [H.264/H.265/VP9]/JPEG(MPEG4/MPEG2)、16 × 1080P@30fps |
| | 控制节点 | 八核 64 位处理器 X100，最高主频 2.4 GHz，八核 A100 可提供 60 TOPS AI 算力 |
| | AI 算力 | 2880 TOPS（60 TOPS × 48，INT4） |
| | 内存 | 16 GB LPDDR5 × 48（16/32 GB） |
| | 存储 | 128 GB UFS × 48（16/32/64/128/256 GB） |
| | 扩展存储 | M.2 2280 PCIe NVMe SSD × 48（选配） |
| | 电源 | 2 个 AC 冗余电源（支持热插拔） |
| | 屏幕 | 1 个触摸显示屏 |
| | 风扇模组 | 12 个高速散热风扇 |
| **物理规格** | 尺寸 | 724.0 mm（长）× 430.0 mm（宽）× 88.8 mm（高） |
| | 满配重量 | 服务器净重：23.1 kg，带包装总重：25.3 kg |
| | 环境 | 工作温度：0℃ - 35℃，存储温度：-40℃ - 60℃，工作湿度：5% - 80%RH（无凝露） |
| **软件参数** | BMC | 集成基于 Web 管理界面的 BMC 管理系统，支持监控、配置、告警、远程运维及虚拟媒体管理等功能，提供 CLI 命令行和 Redfish 等工具，便于二次开发 |
| | 大语言模型 | 支持 Transformer 架构下超大规模参数模型的私有化部署，如 Deepseek-R1 系列、Gemma 系列、Llama 系列、ChatGLM 系列、Qwen 系列、Phi 系列等大语言模型 |
| | 深度学习 | 支持 CNN、RNN、LSTM 等传统网络结构，支持多种深度学习框架，包括 TensorFlow、PyTorch、PaddlePaddle、ONNX、Caffe 等；支持自定义算子开发、Docker 容器化管理技术 |
| **接口参数** | 网络 | 2 × 10 Gbps 万兆网（SFP+）、2 × 千兆以太网（RJ45）、1 × 千兆以太网（RJ45，MGMT 用作 BMC 管理网络） |
| | Console | 1 × Console（RJ45，BMC 调试串口，波特率 115200） |
| | 显示 | 1 × VGA（最高分辨率 1080P，BMC 管理显示） |
| | USB | 2 × USB 3.0（下限 USB 为 USB 3.0 OTG，可使用 U 盘对 BMC 进行 OTG 升级） |
| | 按键 | 1 × 复位键、1 × UID 按键、1 × 电源键 |

## 合作与采购咨询

- **商务电话**：0571-89000775
- **商务邮箱**：[business@spacemit.com](mailto:business@spacemit.com)