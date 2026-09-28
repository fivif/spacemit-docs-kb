---
title: "Support & Service"
lang: en
category: "Hardware/Ecosystem Hardware"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/eco/service.md&lang=en
source_file: https://cdn-resource.spacemit.com/hardware/eco/docs-product/en/service.md
updated: "2026-03-31 17:49:51"
---

# Support & Service

## After-Sales Notes

- Before purchasing any product in the MUSE ecosystem, please carefully review the product specifications. MUSE ecosystem products are development-class devices and may not meet all requirements related to specific functions, use cases, or system/software compatibility. These products are not eligible for the “7-day no-reason return” service. Free warranty service is provided only for hardware defects covered within the warranty period.
- After purchase, please keep all related proof of purchase and invoices for future maintenance and service needs.
- Each product includes a limited free warranty starting from the date of purchase. For specific warranty durations, refer to the product’s warranty documentation or the information published on the official website.
- During the warranty period, if the product experiences a non-man-made hardware failure, the user must provide a written description of the issue, and send the warranty card and proof of purchase to the designated address (consult the seller for details). After the seller confirms that the issue is a product quality defect and meets warranty conditions, the return shipping cost will be covered by the seller. If the seller determines the issue is not a product quality defect (e.g., due to flashing unofficial firmware, missing or mismatched EEPROM data, etc.) or does not meet warranty conditions, the return shipping cost will be borne by the buyer.
- For out-of-warranty failures or damages caused by human factors, users may request paid repair services.
- For failures caused by unauthorized disassembly or modification, warranty service will not be provided. Paid repair service is available, and the user must cover all related repair and shipping costs.

## Product Warranty Policy

<table>
  <tbody>
    <tr>
      <td><strong>Product</strong></td>
      <td><strong>Policy</strong></td>
      <td><strong>Remarks</strong></td>
    </tr>
    <tr>
      <td>MUSE Book</td>
      <td>One-year free warranty for non-man-made hardware damage, starting from the date of purchase.</td>
      <td>No warranty after disassembly; no free warranty for issues caused by flashing unofficial software.</td>
    </tr>
    <tr>
      <td>MUSE Box</td>
      <td>Half-year free warranty for non-man-made hardware damage, starting from the date of purchase.</td>
      <td>No warranty after disassembly/modification; no free warranty for issues caused by flashing unofficial software.</td>
    </tr>
    <tr>
      <td>MUSE Pi</td>
      <td>Half-year free warranty for non-man-made hardware damage, starting from the date of purchase.</td>
      <td>No warranty after disassembly/modification; no free warranty for issues caused by flashing unofficial software.</td>
    </tr>
  </tbody>
</table>

## Safety Precautions

To ensure safe use of the product:

- Please read and fully understand the user manual and safety instructions before using the product.
- Only use the original power adapter or a compatible adapter that meets quality requirements to avoid power-related issues.
- Do not use the product in humid, dusty, flammable, or high-temperature environments to prevent malfunction or safety risks.
- Avoid strong impact or dropping the product to prevent internal component damage.
- Keep the product clean and dry. Prevent liquids or foreign objects from entering the device to avoid failures or safety hazards.
- Ensure the power plug is properly connected during use. Avoid loose connections or short circuits.
- Do not disassemble or modify the device without authorization, as this may affect performance, create safety risks, and void the warranty.
- Perform regular maintenance to ensure the product operates safely and reliably.
- If the product will not be used for a long period or during thunderstorms, please power it off or unplug it for safety.
- If any abnormal behavior or malfunction is detected, stop using the product immediately and contact the seller for support.
- Do not erase the EEPROM built-in information (if applicable); otherwise, warranty service cannot be provided.
- Always download and use officially authorized systems and software. Repairs caused by non-hardware issues will not be covered under warranty.

## FAQ

### System & Usage

#### Q1: What should I do if I encounter application errors or mouse lag after the first boot?

**A**:
After the initial boot setup, some system configurations may not be fully applied yet. We recommend **restarting the device once**. The system should function normally after the reboot.

#### Q2: How do I reset my password if I forget it?

**A**:

1. Connect the MUSE Book to a host computer (e.g., PC) using a serial cable.
2. Open a serial communication software on the host computer and log in with the administrator account:
    - Username: `root`
    - Password: `bianbu`
3. After logging in, execute one of the following commands based on your needs:
    - If you want to **keep the user's data**:

        ```bash
        userdel username
        ```

    - If you do **not** want to keep the user's data:

        ```bash
        userdel -r username
        ```

    *(Replace `username` with the actual username of the account whose password you forgot.)*
4. Restart the device. You will be able to enter the setup interface again to create a new username and password.

### System Support

#### Q3: Which operating systems are supported by MUSE series products?

**A**:
The following operating systems are currently adapted:

- Bianbu Desktop (Pre-installed)
- Bian Linux
- Deepin
- OpenKylin
- OpenHarmony

Adaptation for more operating systems is ongoing. Please follow the official announcements from SpacemiT for the latest updates.

#### Q4: Do MUSE series products support the Windows operating system?

**A**:
Windows is currently **not supported**. The MUSE Book comes pre-installed with **Bianbu Desktop**, a deeply optimized Ubuntu-based distribution. It includes essential software like LibreOffice, a web browser, and media viewers for an out-of-the-box experience. Users can also install additional applications through the Bianbu software repository.

### Firmware & Drivers

#### Q5: Can I flash the firmware on MUSE series products myself?

**A**:
Yes. Users can flash the firmware using command-line tools or the Titan Tool. Please refer to the corresponding product's **User Guide** for detailed instructions.

#### Q6: Where can I download the serial cable driver for MUSE Pi?

**A**:
Driver download link:
[https://www.ftdichip.cn/Drivers/D2XX.htm](https://www.ftdichip.cn/Drivers/D2XX.htm)