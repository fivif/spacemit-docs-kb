---
title: "Introduction"
lang: en
category: "Software/SDK/Buildroot/K3 Buildroot"
source_page: https://www.spacemit.com/community/document/info?nodepath=software/SDK/buildroot/k3_buildroot/intro.md&lang=en
source_file: https://cdn-resource.spacemit.com/software/SDK/buildroot/docs-buildroot/en/k3_buildroot/intro.md
updated: "2026-06-08 10:20:01"
---
# Introduction

The Linux SDK built with Buildroot, adapted for SpacemiT K series chips. It consists of the supervisor program interface (OpenSBI), bootloader (U-Boot/UEFI), Linux kernel, root file system (containing various middleware and libraries), and examples. Its goal is to provide processor Linux support for customers and enable the development of drivers and applications.

## System Architecture

![](../../../../../_assets/docs-buildroot/k3_buildroot/static/bianbu-linux-arch.png)

## Main Components

The following are the components of SDK:

- OpenSBI
- U-Boot
- Linux Kernel
- Buildroot
- esos: Real-Time Operating System
- img-gpu-powervr: GPU DDK
- mesa3d
- k3x-vpu-firmware: Video Process Unit firmware
- k3x-vpu-test: Video Process Unit test program
- k3x-cam: CSI Unit test program
- mpp: Media Process Platform
- FFmpeg (with Hardware Accelerated)
- GStreamer (with Hardware Accelerated)
- v2d-test: 2D Unit test program
- factorytest: factory test app

More is coming.

## Quick Start Guide

- [Image](image.md)
- [Source](source.md)
- [Tools](../tools.md)

## Release Notes

- [Release notes](release_notes/index.md)