---
title: "16.9 Time-Out Monitor"
lang: en
category: "Hardware/K Series AI CPU Chips/K3/Chip Product Documentation/User Manual/16. System Peripherals"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/key_stone/k3/k3_docs/k3_usermanual/16_peripherals/timeout_monitor.md&lang=en
source_file: https://cdn-resource.spacemit.com/hardware/docs-chip/en/key_stone/k3/k3_docs/k3_usermanual/16_peripherals/timeout_monitor.md
updated: "2026-04-30 15:37:33"
---
# 16.9 Time-Out Monitor

## 16.9.1 Overview

The Time-Out Monitor (TOM) is an AXI bus event detection module designed to monitor AXI transactions and identify timeout conditions that may occur during data transfers between system components.

## 16.9.2 Features

- Configurable timeout threshold for flexible detection of stalled transactions  
- Programmable auto-response behavior when a timeout event is detected  
- Debug support: the address and ID of the first timed-out transaction are captured for analysis  
- Configurable AW/ARREADY signal monitoring to ensure bus transaction reliability  
