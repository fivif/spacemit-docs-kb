---
title: "ESOS Development Guide"
lang: en
category: "Software/SDK/Buildroot/K3 Buildroot/ESOS Development Guides"
source_page: https://www.spacemit.com/community/document/info?nodepath=software/SDK/buildroot/k3_buildroot/esos/esos_dev_guide.md&lang=en
source_file: https://cdn-resource.spacemit.com/software/SDK/buildroot/docs-buildroot/en/k3_buildroot/esos/esos_dev_guide.md
updated: "2026-06-08 10:19:47"
---
# ESOS Development Guide

The ESOS system is built on RT-Thread and runs on the RCPU. Its functionality is divided into the following two areas:

1. Works with the main CPU cluster to handle power and energy management, such as dynamic frequency and voltage scaling, power-switch control, system reboot, and system suspend/resume.
2. Works with the main CPU cluster to handle real-time tasks, such as motor control and relay switching.

## ESOS Directory Structure

### SDK Root Directory Structure
```
|-- bsp-src
|   |-- linux-6.18
|   |-- opensbi
|   `-- uboot-2022.10
|-- buildroot
|-- buildroot-ext
|-- Makefile
|-- package-src
|   |-- esos
`-- scripts
    |-- build-muse-boot-plt.sh
    |-- build-plt-stability.sh
    |-- check-config.sh
    |-- check-dl-update.py
    |-- Dockerfile
    |-- envsetup.sh
    |-- gen_imgcfg.py
    |-- LICENSE
    |-- Makefile
    `-- ubuntu.mirror

```
### ESOS Internal Directory Structure
```.
|-- AUTHORS
|-- bsp
|   |-- spacemit
|-- build.sh
|-- build_top.sh
|-- ChangeLog.md
|-- components
|-- debian
|-- documentation
|-- esos_rt24.its
|-- esos_rt24_sign.its
|-- examples
|-- include
|-- Jenkinsfile
|-- Kconfig
|-- libcpu
|   |-- risc-v
|-- LICENSE
|-- null.spacemit
|-- README.md
|-- README_zh.md
|-- src
`-- tools

```

## Building ESOS

### Building from the Top-Level SDK
```
# Build ESOS. By default, this builds all rt24 cores.
make esos

# Clean the build output.
make esos-dirclean

# Reconfigure and rebuild. Note: this is not `make esos-rebuild`.
make esos-reconfigure

```

### Building and Configuring ESOS Separately

For ESOS source changes or `menuconfig` updates, enter the ESOS source directory and select the target core:
```
./build.sh config
INFO: prepare to config esos sdk ...
All valid soc chips:
        0: n308
        1: rt24
Please select a chip:1
All valid boards:
        0: os0_rcpu
        1: os1_rcpu
Please select a board:0

INFO: target configuration is as follows:
INFO: -------------------------------------------------------------------------
export TARGET_CHIP=rt24
export TARGET_BOARD=os0_rcpu
export TARGET_DEFCONFIG=rt24_os0_rcpu_defconfig
export TARGET_ENTRY_POINT=0x100200000
INFO: -------------------------------------------------------------------------

```
After the target core is selected, the graphical `menuconfig` interface can be launched. Once configuration is complete, the updated settings are saved to `bsp/spacemit/platform/rt24/osX_rcpu/rt24_osX_rcpu_defconfig`.

```
./build.sh menuconfig

```
After the changes are complete, run the following command to generate the core `.elf` file:

```
./build.sh

```
To generate `esos.itb`, return to the parent directory and run the following command:

```
cd buildroot-k3
make esos-reconfigure

```