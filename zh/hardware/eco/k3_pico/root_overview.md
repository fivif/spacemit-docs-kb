---
title: "K3 Pico-ITX 简介"
lang: zh
category: "硬件/生态硬件/K3 Pico-ITX"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/eco/k3_pico/root_overview.md&lang=zh
source_file: https://cdn-resource.spacemit.com/hardware/eco/docs-product/zh/k3_pico/root_overview.md
updated: "2026-05-11 18:51:09"
---

# K3 Pico-ITX 简介

**[PDF 版本](https://cdn-resource.spacemit.com/file/product/K3/K3-Pico-ITX_brief_zh.pdf)**

**极致集成度的迷你 AI 计算机**

K3 Pico-ITX 为 60TOPS 算力的单板计算机，8 计算核和 8 智算核统一内存架构，板载 UFS 高速硬盘和万兆网络光通讯接口，充分释放算力性能，提高科学计算、人工智能等应用处理效率。

K3 Pico-ITX 为 2.5" Pico-ITX plus 尺寸，满足各行业紧凑型场景应用。单板支持双 M.2 扩展槽位，具备实时运动控制和系统管理接口。凭借其丰富的接口扩展性与工业架构式设计，可支持行业解决方案提供商开展快速评估与系统集成工作，推动产品商业化落地进程。

## 特性

- **智算一体**
  - 符合 RVA23 标准的 8 核处理器 K3，60TOPS 通用 AI 算力，支持 IME 扩展和完整虚拟化
  - 计算核和智算核统一内存架构，支持 300 亿参数模型部署
  
- **到手即用**
  - 板载 UFS 本地存储，比行业板载 eMMC 提升 3.4 倍速率
  - 全功能 Type-C 接口，支持 65W PD 协议供电和 4K DP 显示，仅需一根线缆，即刻点亮算力
  
- **灵活扩展**
  - M.2 B-Key 和 M-Key 双扩展槽位，其中 M-Key 采用 4 lane PCIe Gen3，可扩展全链路 NVMe SSD
  - 板载万兆 PCIe 以太网，支持 10G-BASE-R 光纤接口，实现低延迟、高吞吐的数据传输，支持集群化部署
  
- **快速集成**
  - 板载行业应用高清屏幕 eDP 接口，支持屏显产品系统集成
  - 实时核 RT24 直出的柔性扩展 IO 插槽，支持 EtherCAT、CAN-FD 等接口，满足微秒级运动控制和机器人等应用
  - MUSE 系列架构设计，冷热分层，最佳 CPU 算力性能释放

## 产品规格

| 模块 | 描述 |
| :--- | :--- |
| 处理器 | SpacemiT K3，8 核 2.4GHz，融合 60TOPS AI 算力，符合 RVA23 标准，支持 IME 向量扩展和完整虚拟化 |
| 显示 | DP Type-C 接口，最高支持 4K 3840 × 2160 分辨率，60Hz 刷新率<br>40PIN EDP 接口，最高支持 2.5K 2560 × 1600 分辨率，90Hz 刷新率 |
| 内存 | 双通道 2 × 32bit LPDDR5，6400MT/s 速率，可选 16GB/32GB 容量 |
| 本地存储 | UFS2.2，可选 128GB/256GB 容量 |
| 存储扩展 | M.2 M-Key 连接器，可装配 2280 尺寸 NVMe SSD，PCIe Gen3 x4 信号链路 |
| 高速扩展 | M.2 B-Key 连接器，可装配 2242/3042 尺寸扩展卡，PCIe Gen3 x2 及 USB 信号* |
| 实时扩展 | FPC 连接器，支持 EtherCAT、5 路 CAN-FD、SPI、I2C 和 UART 等实时信号扩展 |
| 无线通讯 | 板载 PCIe Wi-Fi 6 + BT5.2 模组，符合 802.11a/b/g/n/ac/ax 标准，双天线双频率 |
| 有线网络 | 支持一路以太网，RJ45 接口，1000M/100M 自适应速率 |
| 光纤网络 | 支持万兆以太网，SFP+ 接口，支持 10G BASE-R 和 10G BASE-X，支持 QinQ，MSI-X，WOL 等网络特性 |
| 音频接口 | 板载 CODEC 电路，支持音频输入输出板内接口 |
| USB 接口 | 2 路 USB 3.2 Gen1 Type-C 接口，其中一路为全功能，一路为 OTG；<br>4 路 USB 2.0 Type-A Host 接口； |
| 调试接口 | 支持 UART 和 JTAG 接口，附带 3 个侧边按键，用于开关机，复位和固件烧写升级 |
| 管理系统 | 板载 EC 管理系统，支持电源管理、智能散热策略和系统状态管理，板内支持 I2C/UART/GPIO 扩展接口 |
| 外观形态 | 100 mm × 86 mm，单板计算机 Pico-ITX Plus 尺寸，约为 2.5 寸硬盘大小 |
| 操作系统 | 预装 Bianbu 3.0，支持 Ubuntu 26.04、OpenHarmony 6.0、OpenKylin、Deepin、Fedora 等操作系统 |
| 电源输入 | 支持 Type-C 口 USB-PD 协议，额定输入 65W 功率，板上 ATX 2PIN 电源输入端支持 12V@7A 供电 |
| 可靠性 | 单板形态外设接口 ESD 可防护接触 ±4kV，空气 ±8kV；<br>整机形态 ESD 可防护接触 ±6kV，空气 ±12kV；<br>满足 CCC、CE、FCC 等电磁兼容认证标准，可选消费级 -20℃～70℃ 或工业级 -40℃～85℃ |
| 时钟 | 板载 RTC 时钟电源接口，支持安装电池，满足 G3 状态供电 |
| 结构 | 可选配单板或配带风冷风扇的散热器套装<br>可选配单板或自研全金属工业机箱<br>可选配实时扩展板、触摸屏或工业接线端子多种配置 |

> **注：** M.2 B-Key 插槽安装 PCIe 设备时，B-Key 的 2 lane PCIe 与 M-Key 复用，M.2 M-Key 插槽为 PCIe Gen3 x2 信号链路。

## 框图

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/static/k3_pico_bd.png)

## 可选配部件

| 类别 | 名称 | 描述 | 与主板的接口 |
| :--- | :--- | :--- | :--- |
| **外设部件** | 固态硬盘 | 980 NVMe™ M.2 固态硬盘，PCIe Gen 3.0 x4，<br>NVMe 1.4，顺序读取高达 3,500 MB/s，顺序写入达 3,000 MB/s | M.2 M-Key 2280 |
| | 固态硬盘 | B+M NVMe SSD 128GB 硬盘 | M.2 B-Key 2242 |
| | 4G 模组 | EM05 | M.2 B-Key 3042 |
| | SATA 扩展卡 | PCIe 转 5 × SATA 接口 | M.2 M-Key 2280 |
| | 扩展坞 | 扩展坞 Type-C 转 HD 高清 4K 投屏 PD 充电 USB3.0 平板笔记本 3 合 1 | 全功能 Type-C |
| | 超清屏 | 16 寸 2.5K 90Hz 2560 x 1600 LCD | EDP 40PIN |
| | 实时控制扩展板 | 19V 输入，5 路 CAN-FD，EtherCAT，RS232 和 RS485 等 IO，工业级隔离防护 | FPC |
| **结构配件** | 嵌入风扇式散热器 | 自研铝制 | FAN |
| | 金属机箱 | 120 × 120 × 48 mm 自研金属机箱 | BTN |

## 合作与采购咨询


- **商务电话**：0571-89000775
- **商务邮箱**：[business@spacemit.com](mailto:business@spacemit.com)