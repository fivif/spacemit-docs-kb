---
title: "K3 CoM260 Kit Brief"
lang: en
category: "Hardware/Ecosystem Hardware/K3 CoM260 Kit"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/eco/k3_com260/root_overview.md&lang=en
source_file: https://cdn-resource.spacemit.com/hardware/eco/docs-product/en/k3_com260/root_overview.md
updated: "2026-06-18 09:39:32"
---
# K3 CoM260 Kit Brief

**[PDF Version](https://cdn-resource.spacemit.com/file/product/K3/K3-CoM260_brief_en.pdf)**

**A Full-Stack RISC-V Robotics Development Kit**

The SpacemiT K3-CoM260 Developer Kit integrates an 8-core general-purpose CPU and an 8-core AI CPU into a compact compute module and reference carrier board. It delivers up to 60 TOPS of AI performance and 130 KDMIPS of general computing power, enabling smooth execution of 30B large models.

Built on the RISC-V architecture, the kit supports mainstream AI model deployment while following standard CPU programming paradigms, allowing seamless, zero-cost migration of AI algorithms. With hardware compatibility aligned with Orin Nano, it serves as a complete platform for edge AI development and validation, ideal for AI appliances, service robots, and autonomous edge agents.

## Key Features

- **High-Performance Edge AI**
  Up to 60 TOPS AI compute, supporting smooth inference of 30B models and multi-stream concurrent workloads

- **CPU + AI CPU Architecture**
  Co-designed general-purpose CPU and AI CPU to balance system computing and high-performance AI inference

- **Modular Design**
  Compute module + carrier board form factor, compatible with the full K3-CoM260 series for easy integration

- **Developer-Friendly**
  Standard CPU programming model enables zero-cost migration of AI algorithms and system software

- **Advanced RISC-V Architecture**
  The world’s first compact RISC-V edge computing platform supporting the RVA23 profile

- **Rich Standard Interfaces**
  Comprehensive high-speed I/O and expansion interfaces for cameras, sensors, and peripherals

- **Robotics-Grade Security**
  Integrated hardware security engine with OP-TEE support for trusted execution and secure system deployment

- **Engineering-Ready Support**
  Supports customized software, carrier board design, and full system integration to accelerate product deployment

## Specifications

|Module | Description |
|:------|:------|
| Chip | SpacemiT K3 RISC-V AI CPU |
| CPU | 8 x X100™ 64-bit RISC-V CPU cores<br>- 2 clusters x 4 cores per cluster, each cluster includes 4 MB shared L2 cache, with cross-cluster access<br>- Each X100 core includes 64 KB I-cache and 64 KB D-cache<br>- Compliant with the RVA23 profile<br>- Supports RVV 1.0, VLEN: 256 bits |
| AI Performance | 8 x A100™ AI CPU cores, delivering 60 TOPS<br>- 2 clusters x 4 cores per cluster, each cluster includes 1 MB shared L2 cache and 1.5 MB TCM (Tightly Coupled Memory), with cross-cluster access<br>- Each A100 core includes 32 KB I-cache and 32 KB D-cache<br>- Supports RVV 1.0, VLEN: 1024 bits |
| Hardware Security Engine | Supports international and Chinese commercial cryptographic algorithms <br> - Hash: SHA1 / SHA224 / SHA256, SM3 <br> - Symmetric encryption: AES-128/192/256, SM4 <br> - Asymmetric encryption: RSA-1024/2048/4096, ECC-128/256/512, SM2 |
| Security System | HW-RoT-based Secure Boot <br> Trusted Execution Environment (TEE) with RISC-V PMP/IOPMP isolation mechanisms <br> Supports the OP-TEE OS |
| GPU | Integrated 3D GPU, with support for Vulkan, OpenCL, and OpenGL ES |
| Memory | 8GB/16GB/32GB 64-bit LPDDR5, 6400MT/s |
| Storage | Supports internal UFS, SD card slot, and external NVMe |
| Video Encoding | 4K60 (H.264/H.265) |
| Video Decoding | 1x 4K120 (H.264/H.265/VP9)<br>2x 4K60 (H.264/H.265/VP9)<br>8x 1080p60 (H.264/H.265/VP9)<br>16x 1080p30 (H.264/H.265/VP9) |
| Power Consumption | 18W–25W |

**Reference Carrier Board**

|Module | Description |
|:------|:------|
| Camera | 2 x MIPI CSI-1.1, 22-pin camera connectors |
| PCIe   | M.2 Key M slot (PCIe Gen3 ×4)<br>M.2 Key M slot (PCIe Gen3 ×1)<br>M.2 Key E slot |
| USB    | 4 x USB 3.0 Type-A<br>1 x USB Type-C |
| Networking | 1 x GbE connector |
| Display | 1 x DP 1.2 connector<br>1 x MIPI DSI-1.2 30-pin display connector |
| Other I/O | 40-pin expansion header (UART, SPI, I2S, I2C, GPIO)<br>12-pin button header<br>4-pin fan header<br>DC power jack |
| Mechanical | 103mm x 90.5mm x 34.77mm (Height includes feet, carrier board, module, and thermal solution) |

## Business Cooperation & Purchase

- **Phone**: 0571-89000775
- **Email**: [business@spacemit.com](mailto:business@spacemit.com)
