---
title: "K1 MUSE Pi Pro User Guide"
lang: en
category: "Hardware/Ecosystem Hardware/K1 MUSE Pi Pro"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/eco/k1_muse_pi_pro/pi_pro_user_guide.md&lang=en
source_file: https://cdn-resource.spacemit.com/hardware/eco/docs-product/en/k1_muse_pi_pro/pi_pro_user_guide.md
updated: "2026-08-26 11:24:01"
---

# K1 MUSE Pi Pro User Guide

## 1. Introduction

**MUSE Pi Pro** is a single-board computer integrating a RISC-V 8-core processor, onboard storage, general-purpose interface components and expansion ports onto a single PCB. It supports UEFI boot, multiple operating systems and versatile applications, making it a complete standalone computing system.

MUSE Pi Pro comes in a compact 1.8-inch board form factor, designed to deliver efficient computing performance under low-power, space-constrained scenarios. It is especially suitable for large language model applications, robotics, education & research and IoT devices, providing essential computing power and extensive interface expansion for the new era of AI.

## 2. Hardware

### 2.1 On-Board Resources Overview

![MUSE Pi Pro Board](../../../../_assets/docs-product/k1_muse_pi_pro/static/pi_pro_board.png)

> **Note:** Board appearance may vary slightly between hardware revisions.

### 2.2 Indicators and Buttons

#### LED Indicators

| LED   | Description       |
| ------ | -------- |
| **STAT (System Status)** | - **Off:** No power or hardware fault<br>- **Solid green:** System booted and running normally<br>- **Solid green for 3s → 1 blink:** Boot error (SPI Flash content or communication failure)<br>- **Solid green for 3s → 2 blinks:** External RAM error (DDR communication failure or memory damage)<br>- **Solid green for 3s → 3 blinks:** Kernel error (invalid image or storage corruption)<br>- **Solid green for 3s → 4 blinks:** GRUB/bootloader error (invalid or incompatible boot content) |

#### Buttons

| Button   | Description    |
| ---------- | -------- |
| **PWR (Power Button)**      | - **Shutdown → 1s press:** Power on<br>- **Standby → 1s press:** Wake up<br>- **Normal operation → 3s press:** Forced power-off |
| **RST (Reset Button)**      | - **Short press:** System reset (cold reboot)                                                                                   |
| **FDL (Firmware Download)** | - **Hold while powering on / resetting:** Enter firmware flashing mode                                                          |

![Buttons](../../../../_assets/docs-product/k1_muse_pi_pro/static/JT6LbmgB9ogTOPx2PkjcNhfsnjf.png)

### 2.3 Interface Description

#### Power & Firmware Download Port (PWR)

- Connector type: **USB Type-C**
- Supports **USB-PD** power profiles: 5V/3A, 9V/3A, 12V/3A
- In firmware download mode, the port functions as both **power input** and **USB Device**, allowing the host PC to detect the board and perform flashing operations.

> **Important:**
>
> - A USB cable with **data lines** is required. Charge-only cables are not supported for flashing.
> - To ensure reliable system upgrade, use a USB power source capable of **≥10W**.

![Type-C](../../../../_assets/docs-product/k1_muse_pi_pro/static/XLvWbnBe6oKzrpxa5Uzc9mKnnKg.png)

#### M.2 M-Key Storage Expansion

- Connector: **M.2 (Key-M), height 3.2 mm**
- Supports **NVMe protocol**, 2230 form-factor SSDs
- PCIe 2.0 ×2 bandwidth

> **Important:** Hot-plug is **not supported**. Install or remove SSDs only when power is off.

![M.2](../../../../_assets/docs-product/k1_muse_pi_pro/static/Nm3XbpoC3om51AxAusDcRslOnXG.png)

#### HDMI Display Output

- Connector type: **HDMI Type-A**
- Used for UEFI boot configuration display
- Desktop OS display supports **1080p @ 60Hz**
- Hot-plug supported

#### MIPI DSI Display Interface (DISPLAY)

- Connector: **15-pin, 1.0 mm FFC**
- **MIPI DSI 2-lane**, includes I²C control channel and touch support
- When only a MIPI panel is connected → it becomes the **primary display**
- When both MIPI and HDMI displays are connected → MIPI is the **default primary display**; HDMI acts as extended display
  (primary display can be changed in OS settings)

> **Important:** Hot-plug for MIPI devices is **not supported**.

![DISPLAY](../../../../_assets/docs-product/k1_muse_pi_pro/static/Lxfobq9KFojMdVxzOQvc6AeTnAi.png)

#### Camera Interface CAMERA0

- Connector: **22-pin, 0.5 mm FFC**
- Compatible camera modules listed in:
  **[K1 AVL](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_Key_Parts_AVL-V2.6-20251119.xlsm) – Key Component List**

![CAMERA0](../../../../_assets/docs-product/k1_muse_pi_pro/static/LLVibDZlAoUzoZxphA2c9sAdnKf.png)

> **Note:** For MIPI camera connection instructions and troubleshooting, see [MIPI Camera Usage and FAQ](../../../software/SDK/bianbu/user_guide/LXQt/Camera_FAQ.md).

#### Camera Interface CAMERA1

- Connector: **15-pin, 1.0 mm FFC**
- Compatible camera modules listed in the **[K1 AVL](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_Key_Parts_AVL-V2.6-20251119.xlsm)**

![CAMERA1](../../../../_assets/docs-product/k1_muse_pi_pro/static/L0jUbUjaCoOXkCxTtIDcK1Oanng.png)

#### Audio Interface (AUDIO)

- Standard **3.5 mm TRRS audio jack**
- Backed by **ES8326** audio codec
- Selectable in the system audio settings for playback/recording tests

#### 1G Ethernet Port (1G ETH)

- Connector: **RJ45 with LED indicators**
- Supports **1000M/100M**, auto-negotiation

**Green LED (LINK SPEED):**

1. Solid green → Link established at highest supported speed
2. Off → Link established but not at top speed
3. Off when no link is established

**Yellow LED (ACTIVE):**

1. Off → No data traffic
2. Blinking → Active data transfer (faster blinking = higher traffic)
3. Off when no link is established

#### USB3 Host Interface

- Connector: **USB Type-A**
- Supports **USB 3.0 Host**
- Compatible with multiple devices simultaneously (keyboard, mouse, drive, USB camera, compute stick, etc.)
- Device compatibility list: **[K1 AVL](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K1/K1_Key_Parts_AVL-V2.6-20251119.xlsm)**

#### miniPCIe Expansion Slot

- Connector: **miniPCIe, height 9.9 mm**
- Supports **USB 2.0** and **PCIe 2.0 ×1**
- Compatible with standard full-size miniPCIe modules (4G/5G, wireless, network cards)

> **Important:** Hot-plug is **not supported**.

![miniPCIe](../../../../_assets/docs-product/k1_muse_pi_pro/static/FCjqb2RjPohLX4xvekbcoUsNnMg.png)

#### GPIO Header

- Connector: **2×20, 2.54 mm pitch**
- **PIN2 / PIN4:** 5V output (up to 1A) for fans or expansion boards
- **PIN6 / PIN8 / PIN10:** GND / debugUART_TX / debugUART_RX
- For more details about GPIO usage, visit the document **[GPIO](../../../software/SDK/buildroot/k1_buildroot/device/peripheral_driver/02-GPIO.md)**
- For more about extended IO definition, visit the document **[MUSE Pi/MUSE Pi Pro Expansion I/O Definitions](../../../software/SDK/bianbu/user_guide/LXQt/MUSEPi_and_MUSEPiPro_expansion_IO_pinout.md)**
- GPIO voltage domain: **3.3V**, supports multi-function pinmux

![GPIO](../../../../_assets/docs-product/k1_muse_pi_pro/static/CRNsbxdgGodPOsxIdqAcGEyJnqb.png)

### 2.4 Product Specifications

| Module | Description  |
| --- | --- |
| Processor | SpacemiT M1, 8-core 64-bit RISC-V processor with 2.0 TOPS AI power |
| Display | - HDMI 1.4 (up to 1080P@60Hz)<br>- 2-lane MIPI DSI FPC (up to 1080P@60Hz) |
| Memory | LPDDR4X @ 2400MT/s, 8GB / 16GB options |
| Local Storage | eMMC 5.1, 64GB / 128GB options |
| Storage Expansion | - M.2 M-Key connector, 2230 size NVMe SSD <br>- MicroSD slot, supports UHS-II |
| Wireless | Onboard Wi-Fi 6 and Bluetooth 5.2, supports dual wireless via M.2/mPCIe |
| Network Port | 1 x Ethernet port, RJ45 connector, 1000M/100M auto-sensing |
| Audio | 3.5mm audio jack |
| USB | 4× USB 3.0 Type-A (host), 1× USB 2.0 Type-C (device/OTG) |
| Debug | UART TTL debug port + 3 buttons: reset / power / flash |
| I/O Expansion | - Standard M.2 M-Key slot (2230, supports SSD, PCIe-to-SATA, PCIe comm boards, etc.)<br>- Full-size miniPCIe slot (supports 4G/5G, PCIe wireless/network modules)<br>- 40-pin standard GPIO interface |
| MIPI Interfaces | - 1 x 2-lane MIPI DSI FPC 15-pin interface<br>- 1 x 4-lane MIPI CSI FPC 22-pin interface, 1 x 2-lane MIPI CSI FPC 15-pin interface |
| Form Factor | Single-board computer, FEMTO-ITX dimensions, 85x56mm (credit card size) |
| OS | Bianbu Desktop, Ubuntu, OpenKylin, Deepin, Fedora and other OSs |
| Power | USB-PD: 5V/9V/12V @ 3A |
| Reliability | - ESD: ±4kV contact / ±8kV air, CE/FCC compliant<br>- Available in consumer-grade (-20°C to 70°C) or industrial-grade (-40°C to 85°C) versions |
| Structure | - Optional passive or active cooling heat sinks<br>- Optional metal chassis or acrylic case<br>- Optional touch screen or industrial terminal configurations |

### 2.5 Block Diagram

![Block Diagram](../../../../_assets/docs-product/k1_muse_pi_pro/static/QVGAbS5pEou7W9xYwn4cNaKFnsb.png)

## 3. Quick Start

### 3.1 Preparation

Since MUSE Pi Pro is a single-board computer, some peripherals are needed for working with it, in particular:

- A power supply
- A display
- An HDMI cable
- A keyboard
- A mouse

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/EpmwbwKeSofjCIxP91pcBHq4nCh.png)

### 3.2 Start Up

Once all necessary peripherals are connected, simply power on MUSE Pi Pro to start up.

After powering on at the first time, MUSE Pi Pro needs some configurations as described in the following section.

### 3.3 Configuring MUSE Pi Pro At The First Boot

MUSE Pi Pro supports UEFI boot and configuration. After powering on, the boot medium can be selected and the computer setup can be personalized.

Within 3 seconds of powering on, press the **F2 key** to enter the UEFI setup interface.

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/UzeVbTmnCowOmExaIswcyc1qnmf.png)

#### UEFI Configuration Guide

The following functions are available:

- **Boot Manager Menu**
  Enter the Boot Manager menu, then use the **↑ **and** ↓ keys** to select the boot medium among

  - EMMC storage
  - SSD
  - USB drive
  - SD card

   It is also possible to enter the UEFI shell command line interface.

  ![](../../../../_assets/docs-product/k1_muse_pi_pro/static/DussbQopfo5C9RximKGcgFAenUc.png)
  
- **Boot Maintenance Manager Menu**
  Enter the Boot Maintenance Manager menu, then select "**Boot Options**," then choose "**Change Boot Order**" to set the boot medium priority. Use **+** and **- keys** to adjust the boot order.
  After pressing the **Enter key**, select "**Commit Changes and Exit**" to apply the changes and exit, returning to the main menu. Press the **F10 key** to save the settings.
  ![](../../../../_assets/docs-product/k1_muse_pi_pro/static/G983bN6RMonWDXxmz09cksH4nDb.png)

- **UEFI Interactive Shell**
  MUSE Pi Pro supports UEFI Interactive Shell V2.2.
  Upon first entering the UEFI Interactive Shell, all detected storage devices will be displayed.
  After pressing any key (except **Esc**) or waiting 5 seconds, the EFI Shell will be ready to execute commands.
  Type "**help**" to display the supported commands and related help information.
  ![](../../../../_assets/docs-product/k1_muse_pi_pro/static/Unf4bd8KIoIzihx4ehKcJr5Gngc.png)

Open source **UEFI** firmware repository for **Bianbu Linux**:
 - [edk2](https://gitee.com/bianbu-linux/edk2)
 - [edk2-platforms](https://gitee.com/bianbu-linux/edk2-platforms)

Refer to [UEFI firmware development for MUSE Pi Pro](https://mp.weixin.qq.com/s/s7S3pQesObrmAF_56Cq9Lg) for more details.

#### Bianbu Desktop OS Configuration Guide

If the **F2 key** is not pressed within 3 seconds after powering on the MUSE Pi Pro, by default it will boot from the onboard storage medium and launch the pre-installed Bianbu Desktop operating system.

A configuration wizard will be run upon first startup that includes the following steps.

1. System Language

   Choose the system language. English and Chinese are displayed by default. If need more language options, just click the three dots below to show them.

   ![](../../../../_assets/docs-product/k1_muse_pi_pro/static/JRoobRffJofXQ8x5JxZc3EUpn1g.png)

2. Input Method

   Configure the MUSE Pi Pro’s keyboard layout and input method.

   ![](../../../../_assets/docs-product/k1_muse_pi_pro/static/MoIfbrH7jow5khxznDNcUXdyn5e.png)

3. Wireless Internet Connection

   Select a valid Wi-Fi network from the list and connect it. If there is no suitable Wi-Fi network, skip this setting by clicking on the upper right corner.

   ![](../../../../_assets/docs-product/k1_muse_pi_pro/static/JOgPbIWJwoWAHQxluzhcqFkGnSf.png)

4. Location Services

   Turning on location services can facilitate the usage experience, but it may also bring risks of location privacy leakage. Please be aware and careful!

   ![](../../../../_assets/docs-product/k1_muse_pi_pro/static/Lj8mbqTqzoFPeWxmsDRcyEI5nXb.png)

5. Time Zone

   Configure user time zone information. While online (i.e. Wi-Fi connected), the system can automatically synchronize the corresponding time zone, then user can search for cities to add settings.

   ![](../../../../_assets/docs-product/k1_muse_pi_pro/static/P9y8bMbz2oKURNxIbMPcAB13nlc.png)

6. Username & Password Account

   Set username and password

   ![](../../../../_assets/docs-product/k1_muse_pi_pro/static/Xnq4b4GIFoFDUmxoTv8cYjDdnZb.png)

   ![](../../../../_assets/docs-product/k1_muse_pi_pro/static/G8R3bsqhcosIAYxrP8oc8FBGn4d.png)

7. Configuration completed

   When the configuration is completed, click "Start using Bianbu" thus MUSE Pi Pro will enter the desktop of Bianbu OS.

   ![](../../../../_assets/docs-product/k1_muse_pi_pro/static/AjGmbBkM2o8culxW4BmcWJw1nFg.png)

## 4. Firmware Flashing & Serial Port Debugging

### 4.1 Flashing Process

#### Via USB Type-C Cable

- When the device is powered off,

  - Press and hold the **Firmware Download (FDL)** button without releasing it
  - Connect the USB Type-C cable to the device and the host computer, which also supplies power to turn on the device itself
  - Release the **Firmware Download (FDL)** button
  - Use

    - Either the official **Titan Flasher** tool provided by **SpacemiT** as per description in the [Flashing Tool User Manual](../../../tools/user_guide/flasher_user_guide.md)
    - Or the **fastboot** command

    to proceed with the firmware flashing operation
- When the device is powered on and connected to the USB Type-C cable for power,

  - Press and hold the **Firmware Download (FDL)** button without releasing it
  - Press shortly the **Reset (RST)** button
  - Release the **Firmware Download (FDL)** button
  - Use

    - Either the official **Titan Flasher** tool provided by **SpacemiT** as per description in the [Flashing Tool User Manual](../../../tools/user_guide/flasher_user_guide.md)
    - Or the **fastboot** command

    to proceed with the firmware flashing operation

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/RoFhbwRnEodBcAxCeQfcpArdnLb.png)

### 4.2 Serial Port Debugging

#### Interface Connection

The host computer is normally connected to the TX, RX and GND of the MUSE Pi via the USB to TTL device. The signal interface connection is shown below.

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/Q0H1bvBILoAzVwxGIudczWwLn0g.png)

#### Debugging Under Windows OS

Let’s take the “**MobaXterm**” software tool as example.

Firstly, please connect the hardware serial port correctly and confirm that there is a COM port displayed in the port list of the device manager, as shown below.

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/E1p9bnV5voQcKbxQrvncVFnLn3b.png)

Open the “MobaXterm” software tool then select “Sessions” - “New Session” (1) in the screen appearing. In the pop-up dialog box appearing,

- Select “Serial” (2)
- Select the corresponding COM port identified above for “Serial port” (3)
- Select “115200” for “Speed” (4)
- Click “OK” (5)

as shown below.

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/FPsyb2sIMoIdMtxUFHvcysLinq9.png)

Thus the print page will be entered as shown below.

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/OOH8bf04ZoFZ9sxt4JDc7Qown9b.png)

## 5. Precautions

The MUSE Pi Pro is designed for home, office, and industrial environments. Before operation, please read the following precautions:

1. Do not hot-plug the display interface, CSI interface, or any expansion board under any circumstances.

2. Before unboxing and installing the single-board computer, take appropriate electrostatic discharge (ESD) protection measures to prevent hardware damage.

3. When handling the single-board computer, hold it by the edges. Avoid touching any exposed metal components to prevent potential ESD damage to onboard devices.

4. Place the board on a dry, flat surface, ensuring it is kept away from heat sources, electromagnetic interference (EMI), radiation sources, and EMI-sensitive equipment (e.g., medical devices).

5. Ensure proper ventilation. For continuous full-load operation of 72 hours or longer, install the original heatsink or apply sufficient and effective cooling measures.

## 6. Open-Source Resources

**Structure Drawing:**

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/AuLqbhcMOo206mxtvVfcwR6Nnje.png)

## 7. Appendix — Interface Pin Assignments

### 7.1 MIPI CSI High-Speed Connectors

The MUSE Pi Pro is equipped with one 4-lane MIPI CSI (FPC 22-pin) interface and one 2-lane MIPI CSI (FPC 15-pin) interface.

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/AsqcbGXvaoYKR1xx014cLMQrnmb.png)

**15-Pin High-Speed Connector Pin Assignment**：

| pin | Signal Name |
|-----|----------|
| 1 | GND |
| 2 | MIPI_CSI3_DN0 |
| 3 | MIPI_CSI3_DP0 |
| 4 | GND |
| 5 | MIPI_CSI3_DN1 |
| 6 | MIPI_CSI3_DP1 |
| 7 | GND |
| 8 | MIPI_CSI3_CLKN |
| 9 | MIPI_CSI3_CLKP |
| 10 | GND |
| 11 | CAMERA1_PDN |
| 12 | CAM_MCLK1 |
| 13 | CAM_I2C1_SCL_3V3 |
| 14 | CAM_I2C1_SDA_3V3 |
| 15 | CSI_VCC33 |

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/SJEJbRHcBoDjRxx4tCZcU724npc.png)

**22-Pin High-Speed Connector Pin Assignment**：

| pin | Signal Name |
|-----|----------|
| 1 | GND |
| 2 | MIPI_CSI1_DN0 |
| 3 | MIPI_CSI1_DP0 |
| 4 | GND |
| 5 | MIPI_CSI1_DN1 |
| 6 | MIPI_CSI1_DP1 |
| 7 | GND |
| 8 | MIPI_CSI1_CLKN |
| 9 | MIPI_CSI1_CLKP |
| 10 | GND |
| 11 | MIPI_CSI1_DN2 |
| 12 | MIPI_CSI1_DP2 |
| 13 | GND |
| 14 | MIPI_CSI1_DN3 |
| 15 | MIPI_CSI1_DP3 |
| 16 | GND |
| 17 | CAMERA0_PDN |
| 18 | CAM_MCLK0 |
| 19 | GND |
| 20 | CAM_I2C0_SCL_1833 |
| 21 | CAM_I2C0_SDA_1833 |
| 22 | CSI_VCC33 |

### 7.2 MIPI DSI Display Connector

The MUSE Pi Pro includes one 2-lane MIPI DSI FPC 15-pin interface.

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/M1jLbBDcIomrEYx2whIcbUowncN.png)

**MIPI DSI FPC 15-Pin High-Speed Connector Pin Assignment**：

| pin | Signal Name |
|-----|----------|
| 1 | GND |
| 2 | MIPI_DSI1_LANE1_DN |
| 3 | MIPI_DSI1_LANE1_DP |
| 4 | GND |
| 5 | MIPI_DSI1_CLK_N |
| 6 | MIPI_DSI1_CLK_P |
| 7 | GND |
| 8 | MIPI_DSI1_LANE0_DN |
| 9 | MIPI_DSI1_LANE0_DP |
| 10 | GND |
| 11 | AP_I2C5_SCL_3V3 |
| 12 | AP_I2C5_SDA_3V3 |
| 13 | GND |
| 14 | LCD_VCC33 |
| 15 | LCD_VCC33 |

### 7.3 40pin Header

The development board supports a 40-pin dual-row header. The pin assignments are as follows:

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/GPLWbgRYCoATDqxWtWOcDy49nTe.png)

| pin | Signal Name | Signal Name | pin |
|-----|----------|----------|-----|
| 1 | VCC3V3_SYS | VCC5V0_OUT | 2 |
| 3 | AP_I2C4_SDA_3V3 | VCC5V0_OUT | 4 |
| 5 | AP_I2C4_SCL_3V3 | GND | 6 |
| 7 | GPIO_70_3V3 | UART0_TXD_3V3 | 8 |
| 9 | GND | UART0_RXD_3V3 | 10 |
| 11 | GPIO_71_3V3 | GPI0_74_3V3 | 12 |
| 13 | GPIO_72_3V3 | GND | 14 |
| 15 | GPIO_73_3V3 | GPIO_91_3V3 | 16 |
| 17 | VCC3V3_SYS | GPIO_92_3V3 | 18 |
| 19 | SPI3_MOSI_3V3 | GND | 20 |
| 21 | SPI3_MISO_3V3 | GPIO_49_3V3 | 22 |
| 23 | SPI3_SCLK_3V3 | SPI3_CS_3V3 | 24 |
| 25 | GND | GPIO_50_3V3 | 26 |
| 27 | AP_I2C3_SDA_3V3 | AP_I2C3_SCL_3V3 | 28 |
| 29 | GPIO_51_3V3 | GND | 30 |
| 31 | GPIO_52_3V3 | GPIO_34_3V3 | 32 |
| 33 | GPIO_47_3V3 | GND | 34 |
| 35 | GPIO_48_3V3 | GPIO_35_3V3 | 36 |
| 37 | GPIO_33_3V3 | GPIO_46_3V3 | 38 |
| 39 | GND | GPIO_37_3V3 | 40 |

### 7.4 UART Debug Interface

The board provides UART debugging via Pin 6, 8, and 10 of the 40-pin header for X60 debugging.
On the host controller side, the pin order from top to bottom is:
GND → RX → TX

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/Q0H1bvBILoAzVwxGIudczWwLn0g.png)

### 7.5 JTAG Debug Interface

The development board reserves a Primary JTAG debug channel on the 40-pin header with the following pin assignments:

| 40pin | Net Name        | JTAG Signal Name |
|-------|-----------------|------------------|
| 7     | GPIO_70_3V3     | PRI_TDI          |
| 11    | GPIO_71_3V3     | PRI_TMS          |
| 13    | GPIO_72_3V3     | PRI_TCK          |
| 15    | GPIO_73_3V3     | PRI_TDO          |

![](../../../../_assets/docs-product/k1_muse_pi_pro/static/pi_pro_jtag.png)

## 8. Frequently Asked Questions (FAQ)

For issues with firmware flashing, power supply, or Wi-Fi connections, refer to the [K1 FAQ](../../../software/SDK/bianbu/user_guide/LXQt/K1_FAQ.md).