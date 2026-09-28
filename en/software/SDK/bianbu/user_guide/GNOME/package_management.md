---
title: "Package Management"
lang: en
category: "Software/SDK/Bianbu/Bianbu User Guide/GNOME"
source_page: https://www.spacemit.com/community/document/info?nodepath=software/SDK/bianbu/user_guide/GNOME/package_management.md&lang=en
source_file: https://cdn-resource.spacemit.com/software/SDK/bianbu/docs-bianbu/en/user_guide/GNOME/package_management.md
updated: "2026-06-05 11:22:37"
---
# Package Management

## Overview

- **Packages**
Bianbu software packages follow the Debian package standards and are managed using `apt`.

- **Repositories**
Bianbu provides the following official APT package repositories:
  - **Bianbu 1.0**  (End of Life) : [http://archive.spacemit.com/bianbu-ports/](http://archive.spacemit.com/bianbu-ports/)
  - **Bianbu 2.0 & 3.0** : [http://archive.spacemit.com/bianbu/](http://archive.spacemit.com/bianbu/)

## Update Package

To refresh the local package, run the following command in the terminal:

```shell
apt-get update
```

## Install or Update a Package

To install or upgrade a specific package — for example,  `hello` — run the following command:

```shell
apt-get install hello
```

## Remove a Package

To uninstall a package while preserving its configuration files — for example, `hello`, run the following command:

```shell
apt-get remove hello
```

To completely remove a package along with its configuration files, run the following command:

```shell
apt-get purge hello
```
