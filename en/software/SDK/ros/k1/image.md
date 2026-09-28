---
title: "Images"
lang: en
category: "Software/SDK/ROS 2/K1"
source_page: https://www.spacemit.com/community/document/info?nodepath=software/SDK/ros/k1/image.md&lang=en
source_file: https://cdn-resource.spacemit.com/software/SDK/ros/docs-ros/en/k1/image.md
updated: "2026-05-08 18:23:55"
---
# Images

ROS2_LXQT currently provides two image formats:

- **SD card raw image**

  Files in this format end with `*.img.zip`. They can be written to an SD card using [balenaEtcher](https://etcher.balena.io/), or extracted and flashed using the `dd` command.

- **Custom image**

  Files in this format end with `.zip`. They can be flashed using Titan Flasher, or extracted and flashed using `fastboot`.

**Default credentials:**
- Root user password: `bianbu`
- Default Bianbu user password: `bianbu`

## Download

Link: [ROS2_LXQT Image](https://archive.spacemit.com/ros2/bianbu-ros-images/v1.5/ROS2_LXQT-v1.5rc3-20251107.zip)

## Flashing

For flashing with Titan Flasher, see the [Flashing Tool User Manual](../../../../tools/user_guide/flasher_user_guide.md).
