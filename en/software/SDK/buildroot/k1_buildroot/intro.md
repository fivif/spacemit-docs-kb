---
title: "Introduction"
lang: en
category: "Software/SDK/Buildroot/K1 Buildroot"
source_page: https://www.spacemit.com/community/document/info?nodepath=software/SDK/buildroot/k1_buildroot/intro.md&lang=en
source_file: https://cdn-resource.spacemit.com/software/SDK/buildroot/docs-buildroot/en/k1_buildroot/intro.md
updated: "2026-06-08 10:18:37"
---
# Introduction

The Linux SDK built with Buildroot, adapted for SpacemiT K series chips. It consists of the supervisor program interface (OpenSBI), bootloader (U-Boot/UEFI), Linux kernel, root file system (containing various middleware and libraries), and examples. Its goal is to provide processor Linux support for customers and enable the development of drivers and applications.

## System Architecture

![](https://cdn-resource.spacemit.com/buildroot/docs-buildroot/en/k1_buildroot/static/bianbu-linux-arch.png)

## Main components

The following are the components of SDK:

- OpenSBI
- U-Boot
- Linux Kernel
- Buildroot
- onnxruntime (with Hardware Accelerated)
- ai-support: AI demo
- img-gpu-powervr: GPU DDK
- mesa3d
- QT 5.15 (with GPU enabled)
- k1x-vpu-firmware: Video Process Unit firmware
- k1x-vpu-test: Video Process Unit test program
- k1x-jpu: JPEG Process Unit API
- k1x-cam: CMOS Sensor and ISP API
- mpp: Media Process Platform
- FFmpeg (with Hardware Accelerated)
- GStreamer (with Hardware Accelerated)
- v2d-test: 2D Unit test program
- factorytest: factory test app

More is coming.

## Quick start guide

- [Image](image.md)
- [Source](source.md)
- [Tools](../tools.md)

## Release notes

- [Release notes](release_notes/index.md)
