---
title: "K3 Pico-ITX Brief"
lang: en
category: "Hardware/Ecosystem Hardware/K3 Pico-ITX"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/eco/k3_pico/root_overview.md&lang=en
source_file: https://cdn-resource.spacemit.com/hardware/eco/docs-product/en/k3_pico/root_overview.md
updated: "2026-06-10 18:01:29"
---

# K3 Pico-ITX Brief

**[PDF Version](https://cdn-resource.spacemit.com/file/product/K3/K3-Pico-ITX_brief_en.pdf)**

**Ultra-High Integration Mini AI Computer**

The K3 Pico-ITX is a single-board computer delivering up to 60 TOPS of AI performance. It features a unified memory architecture with 8 CPU cores and 8 AI acceleration cores, along with onboard high-speed UFS storage and a 10Gb optical networking interface. This design maximizes computing capability and improves efficiency for applications such as scientific computing and AI.

Built in a 2.5-inch Pico-ITX Plus form factor, the K3 Pico-ITX is optimized for space-constrained deployments. The board supports dual M.2 expansion slots and provides interfaces for real-time motion control and system management.

With rich I/O expandability and an industrial-grade architecture, the K3 Pico-ITX enables rapid evaluation and system integration, accelerating time to market.

## Key Features

- **Unified AI Compute**
  - 8-core K3 processor compliant with the RVA23 profile, delivering 60 TOPS of AI performance with IME extension support and full virtualization
  - Unified memory architecture across compute and AI cores, enabling deployment of 30B models

- **Ready Out of the Box**
  - Onboard UFS storage, offering speeds up to 3.4× faster than typical eMMC solutions
  - Full-featured USB Type-C with 65 W PD and 4K DP—power and display in one cable

- **Flexible Expansion**
  - Dual M.2 slots (B-Key and M-Key), with M-Key supporting 4-lane PCIe Gen3 for full-bandwidth NVMe SSD expansion
  - Integrated 10GbE over PCIe with support for 10GBASE-R optical interface, enabling low-latency, high-throughput data transfer and scalable clustering

- **Rapid Integration**
  - Onboard eDP interface for HD displays, simplifying display system integration
  - Flexible expansion I/O powered by the RT24 real-time core, supporting EtherCAT, 5 × CAN-FD, and other interfaces for microsecond-level motion control and robotics
  - MUSE architecture with thermal and workload partitioning, ensuring optimal CPU performance and efficiency

## Specifications

| Module | Description |
| :----- | :---------- |
| Processor | SpacemiT K3, 8 cores @2.4 GHz, 60 TOPS AI performance, RVA23 compliant, supports IME vector extensions and full virtualization |
| Display   | DP Type-C: up to 4K (3840 × 2160) @ 60 Hz<br>40-pin eDP: up to 2.5K (2560 × 1600) @ 90 Hz                                     |
| Memory    | Dual-channel 2 × 32-bit LPDDR5 6400 MT/s, 16 GB / 32 GB options                                                              |
| Local Storage | UFS 2.2, 128 GB / 256 GB options                                                                                       |
| Storage Expansion | M.2 M-Key (PCIe Gen3 ×4), supports 2280 NVMe SSD                                                          |
| HS Expansion | M.2 B-Key (PCIe Gen3 ×2 + USB), supports 2242/3042 cards                                                     |
| Real-Time Expansion | FPC connector for EtherCAT, 5 × CAN-FD, SPI, I²C, UART, etc.                                                         |
| Wireless | Onboard Wi-Fi 6 + BT 5.2, dual-band, dual-antenna, 802.11 a/b/g/n/ac/ax compliant                            |
| Wired Network | 1 × RJ45 Ethernet, 10/100/1000 Mbps adaptive                                                                          |
| Optical Network | 10GbE SFP+ port, supports 10GBASE-R / 10GBASE-X, QinQ, MSI-X, WOL, and clustering                            |
| Audio     | Onboard CODEC, internal audio input/output                                                                               |
| USB       | 2 × USB 3.2 Gen1 Type-C (1 full-featured, one OTG)<br>4 × USB 2.0 Type-A Host                                          |
| Debug     | UART, JTAG, and 3 side buttons for power, reset, and firmware update                                                      |
| System Management | Onboard EC controller for power, thermal, and system status; includes I²C/UART/GPIO expansion                    |
| Form Factor | 100 × 86 mm, Pico-ITX Plus single-board computer, approx. size of a 2.5" drive                                         |
| OS        | Pre-installed Bianbu 3.0; supports Ubuntu 26.04, OpenHarmony 6.0, OpenKylin, Deepin, Fedora, etc.                           |
| Power Input | Type-C USB-PD (65 W) or ATX 2-pin 12 V @ 7 A                                                                        |
| Reliability | ESD protection: board: ±4 kV (contact), ±8 kV (air); system: ±6 kV (contact), ±12 kV (air)<br>Compliant with CCC, CE, and FCC; operating temp: -20 °C ～ 70 °C (consumer) / -40 °C ～ 85 °C (industrial) |
| Clock     | Onboard RTC with battery interface, supports G3 state                                                                      |
| Structure | Optional single-board or fan-cooled heatsink assembly<br>Optional single-board or fully-metal industrial chassis<br>Optional real-time board, touchscreen, terminal blocks |

> **Note:** The M.2 B-Key PCIe ×2 lanes are shared with the M-Key slot; when both are populated, the M.2 M-Key operates at PCIe Gen3 ×2.

## Block Diagram

![](https://cdn-resource.spacemit.com/eco/docs-product/en/static/k3_pico_bd.png)

## Optional Components

| Category             | Name                     | Description   | Interface               |
|:----------------------|:--------------------------|:---------------|:-------------------------|
| **Peripheral**           | SSD                      | 980 NVMe™ M.2 SSD, PCIe Gen 3.0 ×4, NVMe 1.4, <br>sequential read up to 3,500 MB/s, <br>sequential write up to 3,000 MB/s | M.2 M-Key 2280          |
|            | SSD                      | B+M NVMe SSD 128 GB | M.2 B-Key 2242          |
|            | 4G Module                | EM05 | M.2 B-Key 3042          |
|            | SATA Expansion Card      | PCIe to 5 × SATA interface | M.2 M-Key 2280          |
|            | Docking Station          | Type-C dock for HD 4K display, PD charging, <br>USB 3.0 for tablets/laptops (3-in-1)                        | Full-featured Type-C    |
|            | Ultra HD Display         | 16" 2.5K LCD, 90 Hz, 2560 × 1600 | 40-pin eDP              |
|            | Real-time Control Expansion Board | 19 V input, 5 × CAN-FD, EtherCAT, RS232 & RS485 I/O, <br>industrial-grade isolation protection         | FPC                     |
| **Structural Accessory** | Embedded Fan Heatsink    | Custom aluminum design    | FAN                     |
| | Metal Chassis            | 120 × 120 × 48 mm self-developed metal chassis                                                           | BTN                     |

## Business Cooperation & Purchase


- **Phone**: 0571-89000775
- **Email**: [business@spacemit.com](mailto:business@spacemit.com)
