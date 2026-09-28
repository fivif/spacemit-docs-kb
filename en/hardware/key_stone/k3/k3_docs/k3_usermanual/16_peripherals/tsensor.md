---
title: "16.4 Temperature Sensor"
lang: en
category: "Hardware/K Series AI CPU Chips/K3/Chip Product Documentation/User Manual/16. System Peripherals"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/key_stone/k3/k3_docs/k3_usermanual/16_peripherals/tsensor.md&lang=en
source_file: https://cdn-resource.spacemit.com/hardware/docs-chip/en/key_stone/k3/k3_docs/k3_usermanual/16_peripherals/tsensor.md
updated: "2026-04-30 15:37:35"
---
# 16.4 Temperature Sensor

## 16.4.1 Overview

The K3 integrates one Temperature Sensor (TSEN) module featuring 7 temperature measurement points. It is designed to monitor thermal conditions across various on-chip locations, providing real-time temperature data that enables the system to perform dynamic thermal management and protection operations.

## 16.4.2 Features

- Support for system restart temperature threshold configuration  
- Provides 7 independent temperature measurement points as follows:
  - Top sensor
  - VPU sensor
  - GPU sensor
  - Cluster 0 sensor
  - Cluster 1 sensor
  - Cluster 2 sensor
  - Cluster 3 sensor
- 12-bit temperature sampling accuracy for precise thermal monitoring  