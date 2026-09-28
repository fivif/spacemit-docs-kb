---
title: "K3 Shelf Array Server Brief"
lang: en
category: "Hardware/Ecosystem Hardware/K3 Shelf N10/N48"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/eco/k3_shelf/root_overview.md&lang=en
source_file: https://cdn-resource.spacemit.com/hardware/eco/docs-product/en/k3_shelf/root_overview.md
updated: "2026-07-23 17:54:50"
---
# K3 Shelf Array Server Brief

**[PDF Version](https://cdn-resource.spacemit.com/file/product/K3/k3-shelf_brief_en.pdf)**

**K3 Shelf Native RISC-V Build Cluster Server**

SpacemiT K3 Shelf is available in two high-density rack server models, N10 and N48, powered by the self-developed K3 AI CPU based on the RVA23 Profile. Each compute node features an 8-core X100 RISC-V CPU running at up to 2.4 GHz, delivering up to 60 TOPS of AI performance.

Built on a native RISC-V architecture, K3 Shelf supports mainstream build systems such as Koji and Open Build Service (OBS). Native compilation delivers over 10× the performance of QEMU emulation on x86, significantly reducing build times for operating systems, firmware, and open-source software.

With a typical power consumption of just 15–25 W per node, K3 Shelf reduces power usage by up to 60% compared with conventional x86 servers. Equipped with four 10GbE ports, a full BMC management system, remote serial console, and cloud debugging, it is an ideal platform for RISC-V software validation, distributed source code builds, on-premises LLM deployment, and edge computing.

## Key Features

- **10/48 K3 compute nodes**

  Each K3 node features an 8-core X100 RISC-V CPU at up to 2.4 GHz and an 8-core A100 AI CPU, delivering up to 60 TOPS.

- **Mainstream Linux Build System Support**
  
  Supports Koji and Open Build Service (OBS), with native compilation over 10× faster than QEMU on x86.

- **RISC-V Software Compatibility Testing**
  
  The industry's first mass-produced RVA23 Profile array server for validating Linux distributions, open-source software, and AI frameworks.

- **Remote RISC-V Cloud Debugging**

  Supports remote flashing, serial console, SSH, Web IDE, and remote desktop for an out-of-the-box cloud development environment.

- **Exceptional Energy Efficiency**

  Twelve K3 nodes match the build performance of a mid-range x86 workstation while consuming just 15–25 W per node, cutting power costs by up to 60%.

- **Equipped with 4 × 10GbE ports**

  Features 4×10GbE (SFP+) ports and a dedicated MGMT port for high-speed networking and BMC management.

- **Integrated BMC Management**

  Provides real-time monitoring, configuration, hardware management, diagnostics, firmware updates, and open APIs for software development.

- **Broad Application Scenarios**

  Ideal for AI computing, edge AI, on-premises LLM deployment, smart cities, healthcare, industrial AI, and intelligent security.

## Specifications (N10)

| Module | Item | Description |
| :--- | :--- | :--- |
| **Technical Specifications** | Form Factor | 1U rack-mounted AI computing server |
| | Architecture | RISC-V architecture |
| | Nodes | 10 distributed compute nodes + 1 control node |
| | Compute Node | 8-core 64-bit X100 processor, up to 2.4 GHz, with an 8-core AI CPU supporting 1024-bit RVV 1.0 vector computing |
| | Video Encoding | H.265/H.264: 1 × 4K@60fps, 8 × 1080p@30fps |
| | Video Decoding | 4K@120fps [H.264/H.265/VP9]/JPEG(MPEG4/MPEG2), 16 × 1080p@30fps |
| | Control Node | 8-core 64-bit X100 processor running at up to 2.4 GHz, paired with an 8-core A100 AI CPU delivering up to 60 TOPS |
| | AI Performance | 600 TOPS (60 TOPS × 10, INT4) |
| | Memory | 16 GB LPDDR5 × 10 (16 GB / 32 GB options) |
| | Storage | 128 GB UFS × 10 (16/32/64/128/256 GB options) |
| | Storage Expansion | Optional M.2 2280 PCIe NVMe SSD × 10 and one 3.5"/2.5" SATA 3.0 SSD with hot-swap support. The BMC provides direct storage management, while compute nodes can access the drive through BMC network sharing. |
| | Power Supply | 550 W AC power supply (90–264 VAC, 47–63 Hz), non-hot-swappable |
| | Cooling | 6 high-speed cooling fans |
| **Physical Specifications** | Dimensions | 440.5 × 494.0 × 44.4 mm (L × W × H) |
| | Weight (Fully Configured) | Net weight: 8.1 kg; Shipping weight: 10.3 kg |
| | Environmental | Operating: 0℃ - 35℃; Storage: -40℃ - 60℃; Humidity: 5% - 80%RH (non-condensing) |
| **Software** | BMC | Integrated web-based BMC management system supporting monitoring, configuration, alarms, remote management, virtual media, CLI, and Redfish APIs for software development. |
| | LLMs | Supports on-premises deployment of full-parameter Transformer-based LLMs, including DeepSeek-R1, Gemma, Llama, ChatGLM, Qwen, Phi, and more. |
| | Deep Learning | Supports CNN, RNN, LSTM, and other neural networks, together with TensorFlow, PyTorch, PaddlePaddle, ONNX, Caffe, custom operators, and Docker containerization. |
| **Interfaces** | Networking | 4 × 10GbE (SFP+) ports, 1 × Gigabit Ethernet (RJ45, MGMT for BMC) |
| | Console | 1 × Console (RJ45, BMC debug port, 115200 bps) |
| | Display | 1 × HDMI (up to 1080p, BMC display output) |
| | USB | 2 × USB 3.0 (supports USB OTG for BMC firmware upgrade) |
| | Buttons | 1 × Reset, 1 × Power, 1 × BMC Reset |
| | Other Interfaces | 1 × RS232 (DB9, 115200 bps), 1 × RS485 (DB9, 115200 bps) |

## Specifications (N48)

| Module | Item | Description |
| :--- | :--- | :--- |
| **Technical Specifications** | Form Factor | 2U rack-mounted AI computing server |
| | Architecture | RISC-V architecture |
| | Nodes | 48 distributed compute nodes + 1 control node |
| | Compute Node | 8-core 64-bit X100 processor, up to 2.4 GHz, with an 8-core AI CPU supporting 1024-bit RVV 1.0 vector computing |
| | Video Encoding | H.265/H.264: 1 × 4K@60fps, 8 × 1080p@30fps |
| | Video Decoding | 4K@120fps [H.264/H.265/VP9]/JPEG(MPEG4/MPEG2), 16 × 1080p@30fps |
| | Control Node | 8-core 64-bit X100 processor running at up to 2.4 GHz, paired with an 8-core A100 AI CPU delivering up to 60 TOPS |
| | AI Performance | 2880 TOPS (60 TOPS × 48, INT4) |
| | Memory | 16 GB LPDDR5 × 48 (16 GB / 32 GB options) |
| | Storage | 128 GB UFS × 48 (16/32/64/128/256 GB options) |
| | Storage Expansion | Optional M.2 2280 PCIe NVMe SSD × 48 |
| | Power Supply | Dual redundant AC power supplies (hot-swappable) |
| | Screen | 1 × touchscreen display |
| | Cooling | 12 high-speed cooling fans |
| **Physical Specifications** | Dimensions | 724.0 × 430.0 × 88.8 mm (L × W × H) |
| | Weight (Fully Configured) | Net weight: 23.1 kg; Shipping weight: 25.3 kg |
| | Environmental | Operating: 0℃ - 35℃; Storage: -40℃ - 60℃; Humidity: 5% - 80%RH (non-condensing) |
| **Software** | BMC | Integrated web-based BMC management system supporting monitoring, configuration, alarms, remote management, virtual media, CLI, and Redfish APIs for software development. |
| | LLMs | Supports on-premises deployment of full-parameter Transformer-based LLMs, including DeepSeek-R1, Gemma, Llama, ChatGLM, Qwen, Phi, and more. |
| | Deep Learning | Supports CNN, RNN, LSTM, and other neural networks, together with TensorFlow, PyTorch, PaddlePaddle, ONNX, Caffe, custom operators, and Docker containerization. |
| **Interfaces** | Networking | 2 × 10GbE (SFP+), 2 × Gigabit Ethernet (RJ45), and 1 × Gigabit Ethernet (RJ45, MGMT for BMC) |
| | Console | 1 × Console (RJ45, BMC debug port, 115200 bps) |
| | Display output | 1 × VGA (up to 1080p, BMC display output) |
| | USB | 2 × USB 3.0 (supports USB OTG for BMC firmware upgrade) |
| | Buttons | 1 × Reset, 1 × UID, 1 × Power button |

## Business Cooperation & Purchase

- **Phone**: 0571-89000775
- **Email**: [business@spacemit.com](mailto:business@spacemit.com)
