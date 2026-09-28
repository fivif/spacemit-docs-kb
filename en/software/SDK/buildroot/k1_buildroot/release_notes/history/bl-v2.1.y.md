---
title: "Buildroot 2.1 Release Notes [End of Life]"
lang: en
category: "Software/SDK/Buildroot/K1 Buildroot/Release Notes/Release History"
source_page: https://www.spacemit.com/community/document/info?nodepath=software/SDK/buildroot/k1_buildroot/release_notes/history/bl-v2.1.y.md&lang=en
source_file: https://cdn-resource.spacemit.com/software/SDK/buildroot/docs-buildroot/en/k1_buildroot/release_notes/history/bl-v2.1.y.md
updated: "2026-03-17 15:20:39"
---
# Buildroot 2.1 Release Notes [End of Life]

Buildroot 2.1 will reach end of maintenance on July 31, 2025. We recommend using version 2.2 or later. If you have any questions, please contact us.

## v2.1 release note

Release date: 2025-1-20

Compared to 2.0, 2.1 fixes several issues and provides a new kernel branch k1-bl-v2.1.y (based on 6.6.63), including every modification.

### Major Updates

- Upgraded kernel to 6.6.63
- Added support for hardware random number generator
- Added support for suspend to disk
- Fixed the issue where PCIe memory allocation failed when booting the kernel via EFI
- Fixed the issue of husb239 interrupt loss
- Fixed the issue where husb239 could not enter suspend mode
- Fixed occasional errors in i2c
- Fixed PWM clock configuration errors
- Fixed system crash caused by repeated TCM release
