---
title: "Bianbu V1.0 更新说明 [已停服]"
lang: zh
category: "软件/SDK 与系统构建/Bianbu/更新说明/历史版本"
source_page: https://www.spacemit.com/community/document/info?nodepath=software/SDK/bianbu/release_notes/history/bianbu_1.0.md&lang=zh
source_file: https://cdn-resource.spacemit.com/software/SDK/bianbu/docs-bianbu/zh/release_notes/history/bianbu_1.0.md
updated: "2026-02-04 14:24:24"
---
# Bianbu V1.0 更新说明 [已停服]

## Bianbu V1.0 停服公告（End of Life）

Bianbu V1.0 基于 **Ubuntu 23.10** 构建。由于 Ubuntu 社区已停止对 23.10 版本的维护与安全更新，Bianbu V1.0 已不再具备持续维护的基础条件。

进迭时空已基于 **Ubuntu 24.04 LTS**，并结合 RISC-V 架构进行深度优化，推出新一代系统 **Bianbu V2.x**。为统一版本规划、保障系统安全性与长期可维护性，现正式宣布：

**Bianbu V1.0 进入生命周期终止（End of Life，EOL）状态。**

### 生命周期支持信息

| 版本        | 停止支持日期 | 延长生命周期支持（ELS） |
|-------------|--------------|--------------------------|
| Bianbu 1.x.x | 2024/12/31   | 不提供                   |

### 用户迁移建议

为获得持续的功能更新、安全补丁及更完善的 RISC-V 平台支持，**建议用户尽快升级至 Bianbu V2.x 系列版本**。  
具体升级方式请参考文档：**[用户指南 — 系统升级](../../../../../../en/software/SDK/bianbu/zh/user_guide/GNOME/upgrade.md)**。

## V1.0 更新说明

发布日期：2024-5-30

Buildroot版本：[v1.0](../../../buildroot/release_notes/history/bl-v1.0.y.md)

### 主要组件

#### 应用

- GNOME 45.0
- Chromium 122
- Nautilus
- Shotwell
- LibreOffice
- mpv
- Rhythmbox
- docker.io 24.0.5

#### 应用框架

- Electron 29.3.1
- QT 5.15.10
- GTK 4.12.2

#### 多媒体框架

- FFmpeg 6.0 (with Hardware Accelerated)
- GStreamer 1.22.5 (with Hardware Accelerated)
- PipeWire 0.3.79

#### 推理框架

- onnxruntime 1.15.1 (with Hardware Accelerated)

#### 运行时

- Python 3.11.6
- OpenJDK 17 (default)
- Node.js

#### 库

- OpenCV 4.6.0
- OpenSSL 3.0.10
- MPP，进迭时空多媒体处理平台，提供 C API 和 sample
- Mesa 3D 22.3.5

### 已知问题

- 长时间挂起后无法唤醒

## V1.0.3

发布日期：2024-6-19

Buildroot版本：[v1.0.3](../../../buildroot/release_notes/history/bl-v1.0.y.md)

### 主要更新

- 修复长时间挂起后无法唤醒
- 修复XFCE桌面卡顿的问题
- 修复文件浏览器属性对话框crash的问题
- 修复Chromium中文重复输入的问题

## V1.0.5

发布日期：2024-6-26

Buildroot版本：[v1.0.5](../../../buildroot/release_notes/history/bl-v1.0.y.md)

### 主要更新

- 修复LibreOffice打开word或excel、保存文件低概率闪退的问题
- 修复茄子相机在系统休眠唤醒后无响应的问题

## V1.0.7

发布日期：2024-7-11

Buildroot版本：[v1.0.7](../../../buildroot/release_notes/history/bl-v1.0.y.md)

## V1.0.8

发布日期：2024-7-16

Buildroot版本：[v1.0.8](../../../buildroot/release_notes/history/bl-v1.0.y.md)

## V1.0.9

发布日期：2024-7-20

Buildroot版本：[v1.0.9](../../../buildroot/release_notes/history/bl-v1.0.y.md)

## V1.0.11

发布日期：2024-8-1

Buildroot版本：[v1.0.11](../../../buildroot/release_notes/history/bl-v1.0.y.md)

## V1.0.12

发布日期：2024-8-2

Buildroot版本：[v1.0.12](../../../buildroot/release_notes/history/bl-v1.0.y.md)

### 主要更新

- 修复目标检测和姿态跟踪无法打开的问题

## V1.0.13

发布日期：2024-8-16

Buildroot版本：[v1.0.13](../../../buildroot/release_notes/history/bl-v1.0.y.md)

### 主要更新

- 支持开关机动画
- 支持安装`llm-client`大语言模型客户端
- 支持安装`box64`
- 完善universe组件
- 修复版本号错误，反复在线升级的问题

## V1.0.14

发布日期：2024-8-31

Buildroot版本：[v1.0.14](../../../buildroot/release_notes/history/bl-v1.0.y.md)

### 主要更新

- 修复HDMI作为主屏时，没接导致串口无法登录的问题
- 修复ssh不支持压缩的问题

## V1.0.15

发布日期：2024-9-7

Buildroot版本：[v1.0.15](../../../buildroot/release_notes/history/bl-v1.0.y.md)

### 主要更新

- 修复spacemit-uart-bt软件包版本过低的问题
- 支持升级到Bianbu 2.0（开发中的版本）
