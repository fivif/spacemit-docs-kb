---
title: "Cluster Server RV2768 Brief"
lang: en
category: "Hardware/Ecosystem Hardware/Cluster Server RV2768"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/eco/k3_rv2768/root_overview.md&lang=en
source_file: https://cdn-resource.spacemit.com/hardware/eco/docs-product/en/k3_rv2768/root_overview.md
updated: "2026-08-04 16:28:36"
---
# Cluster Server RV2768 Brief

**[PDF Version](https://cdn-resource.spacemit.com/file/product/K3/k3-rv2768_brief_en.pdf)**

**768-Core Native RISC-V AI Compute Cluster**

The Cluster Server RV2768 is a RISC-V-based cluster server in a 2U, 19-inch rack form factor, integrating up to 48 SpacemiT K3 processors and compliant with the RVA23 profile defined by RISC-V International.

RVA23 targets general-purpose application processors, requiring support for Vector and Hypervisor extensions, and represents a modern performance standard for AI and high-performance workloads. The system delivers 768 native RISC-V cores, making it well-suited for running large numbers of AI agents and applications while handling compute-intensive data processing tasks.

With a multi-node cluster architecture and full hardware virtualization, the server allows multiple users to run independent computing environments simultaneously without interference, providing hardware-level isolation between users. Leveraging vector extensions, it delivers up to 2880 TOPS of AI compute and supports up to 1536 GB of memory, enabling concurrent AI inference workloads.

## Key Features

- **Reliable & Serviceable**
  - Independent maintenance, remote access, debugging, and upgrade per compute node
  - Front I/O design for simplified servicing and improved thermal efficiency (no rear cabling)
  - Rear “N+1” redundant fan design
- **Flexible Compute Scaling**
  - 2U chassis supporting up to 48 compute nodes (384 CPU cores + 384 AI cores)
  - External switch connectivity to any node via independent, non-blocking channels
- **Intelligent Management**
  - PXE boot support for diskless startup via network
  - Integrated Layer 3 management switch supporting VLAN segmentation, dynamic routing, and link aggregation
  - Built-in BMC for system monitoring, thermal control, and compute module management
- **Standards-Compliant Architecture**
  - RVA23 profile support, meeting instruction set requirements for high-end Linux distributions over the next five years and beyond
  - Full hardware virtualization across CPU, memory, interrupts, and I/O
  - 1024-bit wide parallel AI compute for efficient integration with mainstream AI ecosystems

## Specifications

| Module | Item | Description |
| :--- | :--- | :--- |
| **Physical** | Form Factor | 2U rackmount |
| | Dimensions | 87.4 mm × 447.6 mm × 816.8 mm |
| | Compute Modules | Up to 24 modules, each with 2 K3 nodes, independently serviceable |
| | Compute Nodes | Up to 48 physically isolated nodes, each independently manageable and maintainable |
| **Compute Node** | CPU Cores | 8 × X100 cores per K3, SPECint2006 > 9.0/GHz, up to 2.4 GHz |
| | AI Cores | 8 × A100 cores per node, 60 TOPS @INT4 |
| | RAM | LPDDR5, 8 / 16 / 32 GB options, up to 6400 MT/s |
| | ROM | NVMe SSD (PCIe 3.0 x4), 64 / 128 / 256 GB, optional UFS |
| | Networking | 1GE port for internal management network, 10GE port for external connectivity |
| | Features | PXE boot, remote access, debugging, and upgrade |
| **Switch System** | External Ports | 2 × 10GbE SFP+ and 48 × 10GbE SFP+ |
| | Topology | Network connectivity between compute node interfaces, sideband management ports, and external ports |
| **System (Chassis)** | Power | 2000 W / 3000 W PSU (Platinum/Titanium), hot-swappable, 1+1 redundancy |
| | Cooling | 4 fans |
| | Installation | L-type rail support |
| **Management** | System Management | Unified multi-node module management and integrated switch management, with a dedicated front GE management port for full fault monitoring and operations |
| | Node Management | Power control, reset, firmware configuration, serial debug, and remote console |
| **Software** | OS | Optional pre-installed mainstream Linux distributions |
| | Software Platform | Cluster management, distributed computing, AI agent clusters |
| **Operating Conditions** | Temperature | 5°C–40°C (41°F–104°F), ASHRAE A1/A2/A3 compliant |
| | Humidity | 8%–90% |

## Business Cooperation & Purchase

- **Phone**: 0571-89000775
- **Email**: [business@spacemit.com](mailto:business@spacemit.com)
