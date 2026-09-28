---
title: "System Tools"
lang: en
category: "Tools/SpacemiT Studio/User Guide/Development Tools"
source_page: https://www.spacemit.com/community/document/info?nodepath=tools/studio/user_guide/dev_tools/system_tools.md&lang=en
source_file: https://cdn-resource.spacemit.com/tools/docs-tool/en/studio/user_guide/dev_tools/system_tools.md
updated: "2026-08-24 08:56:24"
---
# System Tools

## System Preconfiguration

A headless initialization tool that presets system parameters before the device's first boot. Basic configuration can be completed without a monitor or keyboard.

### Procedure

1. Go to **Development Tools → System Preconfiguration**.

   ![System Preconfiguration entry](https://cdn-resource.spacemit.com/tools/docs-tool/en/studio/static/systool_preconfig_00.png)

2. Specify the configuration fields to preset:

   ![System Preconfiguration fields](https://cdn-resource.spacemit.com/tools/docs-tool/en/studio/static/systool_preconfig_01.png)

   - **Username / Password**: Sets the system login credentials.
   - **Hostname**: A custom device name. If left blank, the hostname is generated automatically.
   - **Language / Timezone**: The system display language and timezone. The timezone defaults to UTC.
   - **WiFi**: Optional. Enter the SSID and password (WPA/WPA2-PSK supported) to connect automatically on first boot.
   - **Logo Configuration**: Upload a logo image to display during device boot. Only BMP format is supported, with 8/24/32-bit color depth and a maximum size of 1MB.

3. Click **Push and Run**. The configuration is written to the connected device and applied automatically on first boot.

## Port Forwarding

Maps a device port to the local machine, enabling access to services running on the device from a local browser or tool.

### Use Cases

- Accessing web services on the device (such as HTTP/HTTPS applications)
- Debugging development services on the device, such as Node.js or Flask
- Connecting to services on the device, such as Jupyter, MySQL, or Redis

### Port Forwarding Procedure

1. Ensure the device is connected and appears in the **Current Device** panel.
2. Go to **Development Tools → Port Forward**.

   ![Port Forwarding entry](https://cdn-resource.spacemit.com/tools/docs-tool/en/studio/static/systool_mapping_00.png)

3. Fill in the forwarding rule in the **New Forward** panel:

   ![New Forward panel](https://cdn-resource.spacemit.com/tools/docs-tool/en/studio/static/systool_mapping_01.png)

    - **Remote Port**: The device port number to forward (for example, 8080).
    - **Local Port**: The local port number to map. If left blank, a port is assigned automatically.
       Common ports can also be selected using shortcut tags: HTTP (80), HTTPS (443), SSH (22), Node.js (3000), Flask (5000), Jupyter (8888), MySQL (3306), and Redis (6379).

4. Click **Create Forward**.

   ![Create Forward](https://cdn-resource.spacemit.com/tools/docs-tool/en/studio/static/systool_mapping_02.png)

5. After the forward is created, it appears in the **Active Forwards** list on the right. Access the device service at `localhost:<local port>`.

   ![Active Forwards list](https://cdn-resource.spacemit.com/tools/docs-tool/en/studio/static/systool_mapping_03.png)

## Serial Connection

Enables command-line interaction and system debugging through a serial connection to the device.

### Serial Connection Use Cases

- Viewing device boot logs and performing system debugging
- Controlling the device in environments without network access
- Bootloader interaction and low-level system configuration
- Embedded development and driver debugging

### Serial Connection Procedure

1. Ensure the device is connected to the computer over a serial connection.
2. Go to **Development Tools → Serial Connection**.

   ![Serial Connection entry](https://cdn-resource.spacemit.com/tools/docs-tool/en/studio/static/systool_serial_00.png)

3. Configure the serial parameters:

   ![Configure serial parameters](https://cdn-resource.spacemit.com/tools/docs-tool/en/studio/static/systool_serial_01.png)

   - **Serial Port**: Select the serial port corresponding to the device (for example, COM3 or /dev/ttyUSB0).
   - **Baud Rate**: Sets the communication speed. The common value is 115200.

4. Click **Connect**. After the connection is established, interact with the device through the terminal window.
