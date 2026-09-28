---
title: "Applications and Software Management"
lang: en
category: "Software/SDK/Bianbu/Bianbu User Guide/LXQt"
source_page: https://www.spacemit.com/community/document/info?nodepath=software/SDK/bianbu/user_guide/LXQt/software_management.md&lang=en
source_file: https://cdn-resource.spacemit.com/software/SDK/bianbu/docs-bianbu/en/user_guide/LXQt/software_management.md
updated: "2026-05-15 09:02:41"
---
# Applications and Software Management

This section introduces the commonly preinstalled applications in Bianbu LXQt and explains how to manage software using the APT package manager.

## Common Applications Overview

| Application | Package Name | Icon | Description |
|------------|--------------|------|-------------|
| Web Browser | chromium-browser-stable | ![chromium-browser](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/chromium-browser.svg) | Open-source web browser based on Chromium |
| TigerVNC Viewer | tigervnc-viewer | ![tigervnc](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/tigervnc.svg) | VNC remote desktop client |
| LibreOffice | libreoffice | ![LibreOffice](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/libreoffice.svg) | LibreOffice launcher (office suite entry point) |
| LibreOffice Calc | libreoffice-calc | ![libreoffice-calc](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/libreoffice-calc.svg) | Spreadsheet editor |
| LibreOffice Draw | libreoffice-draw | ![libreoffice-draw](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/libreoffice-draw.svg) | Vector drawing and flowchart tool |
| LibreOffice Impress | libreoffice-impress | ![libreoffice-impress](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/libreoffice-impress.svg) | Presentation editor |
| LibreOffice Math | libreoffice-math | ![libreoffice-math](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/libreoffice-math.svg) | Formula editor |
| LibreOffice Writer | libreoffice-writer | ![libreoffice-writer](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/libreoffice-writer.svg) | Document and word processor |
| Okular | okular | ![okular](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/okular.svg) | Multi-format document viewer (PDF, EPUB, DjVu, etc.) |
| Skanlite | skanlite | ![org.kde.skanlite](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/org.kde.skanlite.svg) | Lightweight image scanning utility |
| 2048-Qt | 2048-qt | ![2048-qt](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/2048-qt.svg) | Classic 2048 puzzle game (Qt version) |
| Audacious | audacious | ![audacious](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/audacious.svg) | Lightweight audio player with plugin support |
| Cheese | cheese | ![cheese](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/cheese.svg) | Webcam photo and video capture tool |
| FeatherPad | featherpad | ![featherpad](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/featherpad.svg) | Lightweight plain-text editor with tabs |
| LXImage-Qt | lximage-qt | ![lximage-qt](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/lximage-qt.svg) | Default LXQt image viewer |
| mpv | mpv | ![mpv](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/mpv.svg) | High-performance media player with hardware acceleration |
| PulseAudio Volume Control | pavucontrol-qt | ![multimedia-volume-control](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/multimedia-volume-control.svg) | Audio device and volume management (Qt) |
| Fcitx 5 | fcitx | ![fcitx5](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/fcitx.svg) | Next-generation input method framework |
| QTerminal | qterminal | ![utilities-terminal](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/utilities-terminal.svg) | Lightweight multi-tab terminal emulator |
| Drop-down QTerminal | qterminal | ![utilities-terminal](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/utilities-terminal.svg) | Quake-style drop-down terminal |
| qps | qps | ![qps](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/qps.svg) | Qt-based process viewer and manager |
| Disks | gnome-disk-utility | ![org.gnome.DiskUtility](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/org.gnome.DiskUtility.svg) | Disk and partition management utility |
| KCalc | kcalc | ![accessories-calculator](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/accessories-calculator.svg) | Scientific calculator |
| LXQt Archiver | lxqt-archiver | ![lxqt-archiver](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/lxqt-archiver.svg) | Archive compression and extraction tool |
| PCManFM-Qt | pcmanfm-qt | ![pcmanfm-qt](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/pcmanfm-qt.svg) | Default LXQt file manager |
| QtPass | qtpass | ![qtpass-icon](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/qtpass-icon.svg) | Password manager based on pass and GPG |
| Vim | vim-common | ![gvim](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/gvim.svg) | Highly configurable text editor |
| nobleNote | noblenote | ![noblenote](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/noblenote.svg) | Lightweight notes and checklist application |
| Keyboard Layout Viewer | fcitx5-config-qt | ![input-keyboard](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/input-keyboard.svg) | View and switch keyboard layouts |

## Package Management with APT

`APT` (Advanced Package Tool) is the default package manager used by the system. It is widely used in **Debian** and Debian-based distributions to manage software packages.

APT provides the following core functions:

- **Install software**  
  Download and install packages from official repositories.

- **Update the system**  
  Refresh package indexes and upgrade installed packages.

- **Remove software**  
  Uninstall packages and clean up unused dependencies.

- **Dependency management**  
  Automatically resolves package dependencies and prevents conflicts.

The following image shows the built-in help information for the `apt` command.  
For full command usage and options, refer to [the Debian official manual](https://manpages.debian.org/bookworm/apt/apt-get.8.en.html).

![APT help output](../../../../../../_assets/docs-bianbu/user_guide/LXQt/static/aptHelp.png)
