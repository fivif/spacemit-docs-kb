---
title: "K1 MUSE Pi 用户使用指南"
lang: zh
category: "硬件/生态硬件/K1 MUSE Pi"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/eco/k1_muse_pi/pi_user_guide.md&lang=zh
source_file: https://cdn-resource.spacemit.com/hardware/eco/docs-product/zh/k1_muse_pi/pi_user_guide.md
updated: "2026-03-31 17:53:53"
---

# K1 MUSE Pi 用户使用指南

## 产品简介

**K1 MUSE Pi** 是进迭时空生态产品开发板系列，第一代搭载了进迭时空八核 RISC-V 高性能处理器 M1，核内融合 2.0Tops 通用 AI 算力，可支持所有 AI 模型算法的快速部署。

**K1 MUSE Pi** 充分展现了 M1 的方案和接口扩展性，设计引出了 M1 芯片原生的 HDMI、双网口、USB3.0、USB2.0、双 PCle2.1 等接口，可适配进迭自研 BianbuOS、BianbuNAS、OpenHarmony、OpenKylin、Deepin 等操作系统，可快速用于行业控制、NAS、机器视觉、网关等产品形态评估和孵化。

## 产品规格

<table>
<tbody>
<tr>
<td><strong>处理器</strong></td>
<td>SpacemiT M1，8核64位RISC-V处理器, 融合2.0 TOPS AI算力</td>
</tr>
<tr>
<td><strong>显示</strong></td>
<td>HDMI Type-A接口，最高支持1080P@60Hz<br/>4lane MIPI DSI FPC接口，最高支持1080P@60Hz</td>
</tr>
<tr>
<td><strong>内存</strong></td>
<td>LPDDR4X，2400MT/s速率，可选配8GB/16GB容量</td>
</tr>
<tr>
<td><strong>本地存储</strong></td>
<td>eMMC 5.1，可选配32GB/64GB容量</td>
</tr>
<tr>
<td><strong>扩展存储</strong></td>
<td>2*M.2 2280 M-Key连接器，可装配 NVMe SSD<br/>TF卡接口，支持UHS-Ⅱ模式存储卡</td>
</tr>
<tr>
<td><strong>无线通讯</strong></td>
<td>支持Wi-Fi6＆BT5.2</td>
</tr>
<tr>
<td><strong>有线网络</strong></td>
<td>支持2路以太网，RJ45接口，1000M/100M自适应</td>
</tr>
<tr>
<td><strong>音频接口</strong></td>
<td>3.5mm音频耳麦接口</td>
</tr>
<tr>
<td><strong>USB接口</strong><br/></td>
<td>1路USB3.0和1路USB2.0 Type-A host接口<br/>1路USB2.0 Type-C OTG接口，支持12V 3A PD供电</td>
</tr>
<tr>
<td><strong>调试接口</strong></td>
<td>26Pin标准GPIO接口，附带3个侧边按键，用于硬件复位、开关机和烧录升级</td>
</tr>
<tr>
<td><strong>MIPI接口</strong></td>
<td>1路 4lane MIPI DSl <br/>2路 4lane MIPI CSl，支持“4+4”或“4+2+2”组合链路</td>
</tr>
<tr>
<td><strong>外观形态</strong></td>
<td>单板计算机，可选装透明亚克力外壳，尺寸为129.45*80mm</td>
</tr>
<tr>
<td><strong>操作系统</strong></td>
<td>支持Bianbu Desktop、Bianbu NAS、Ubuntu、openKylin、deepin、Fedora等操作系统</td>
</tr>
<tr>
<td><strong>电源输入</strong></td>
<td>支持USB PD3.0供电</td>
</tr>
<tr>
<td><strong>可靠性</strong></td>
<td>外设接口ESD可防护接触±4kV，空气±8kV<br/>可选消费级-20°C~70°C或工业级-40°C~85°C</td>
</tr>
</tbody>
</table>

## 系统概述

### K1 芯片概述

K1 是一款高性能、超低功耗的 SOC，集成了 8 核 RISC-V CPU 内核和 SpacemiT® 道一 ™AI 计算能力。K1 具有以下特点：

- 集成 SpacemiT® 自主创新 X60™RISC-V 处理器核，遵循 RISC-V 64GCVB 体系结构和 RVA22 标准。
- 通过探索 RISC-V 定制指令扩展 2.OTOPS AI 算力，实现 CPU AI 融合算力，支持 TensorFlowLite、TensorFlow、ONNX RunTime 等主流 AI 推理框架
- 通过实现不同电源的划分，以及不同层级的功率状态。实现超低功耗，使 K1 更具竞争力和领先优势。
- 支持全功能界面，丰富更具创新性的应用程序和产品。
- 兼容主流操作系统，满足各种应用场景的需求。
- 符合工业级可靠性标准。

**框图**

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/Hs4Sbm1KOoe6cRx2J4DcJS9Dngf.png)

### K1 MUSE Pi 参考方案框图
   3.1 参考方案框图
   K1 MUSE Pi 系统采用 K1 的芯片，P1 PMIC+ 外挂 DCDC 的供电方案；DRAM 采用 LPDDR4X、eMMC5.1；包括 2xPCIe2.0 2lane M.2 KEY M、USB2.0 TYPEA、USB3.0 TYPEA、WIFI/BT、TF Card、HDMI TX、MIPI DSI、MIPI CSI、TYPEC、2xRJ45 等外设接口，集成了一个稳定的可量产化的方案。参考方案框图如下：
   ![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/PDgvb49SsoQV1HxPi8zcF25Jn5f.jpg)

### 功能概述

K1 MUSE Pi 包含的功能如下：

- TYPEC：一路 USB2.0 DEVICE TYPEC 接口，兼容系统固件升级通道及 PD3.0 12V/3A 供电通道
- Audio Interface：外挂顺芯 ES8326B 方案，支持立体声喇叭、耳机输出声音、双 MIC 录音
- HDMI1.4 OUT：一路 HDMI1.4 OUT TYPEA 接口，最大可支持 1920x1080@60Hz 输出
- MIPI DSI/TP：通过 31pin 座子，一路 4lane MIPI DSI 信号支持 LCD 屏、一路 I2C 信号支持 CTP 屏。可通过配套屏转接小板实现显示、触摸功能。
- MIPI CSI：通过 60 pin 高速座子，两路 4lane MIPI CSI 信号分别支持 16M 与 8M 摄像头；可通过座子对应线序设计小板匹配特定摄像头模组。实现拍摄录像功能。
- 26pin 双排插针：兼容树莓派标准 26pin 双排插针，支持 I2C、UART、SPI、JTAG 和 GPIO 调试
- TF 卡座：支持高速 TF 卡
- SDIO WIFI：WIFI 型号为 RTL8852BS，外置 SMA 天线，支持无线上网功能
- Ethernet：支持两路 RJ45 接口 10/100/1000M 以太网
- PCIe2.1 2lane Interface：两路标准 M.2 KEY M 接口，用于扩展 PCIe 设备
- USB2.0 TYPEA：单通道 USB2.0 TYPEA 接口，用于扩展 USB 设备
- USB3.0 TYPEA：单通道 USB3.0 TYPEA 接口，用于扩展 USB 设备
- UART Debug：用户调试查看 LOG 信息使用；支持 3 pin 单排插针（J25）调试 X60；支持 26pin 双排插针 pin6、8、10 调试 RCPU
- JTAG：支持 26pin 双排插针 pin7、11、13、15 调试 PRI JTAG。支持通过配套的 TF 卡转接子板调试 SEC2 JTAG
- System Key：包含 Reset、PWRON、DownLoad（FEL）按键
- SWITCH：支持启动介质选择

### 功能接口

<table>
<tbody>
<tr>
<td><strong>功能</strong></td>
<td><strong>是否可用</strong></td>
</tr>
<tr>
<td>LPDDR4x (4GB)</td>
<td>YES</td>
</tr>
<tr>
<td>eMMC (16GB)</td>
<td>YES</td>
</tr>
<tr>
<td>SPI FLASH</td>
<td>默认未贴</td>
</tr>
<tr>
<td>TYPEC 12V Input</td>
<td>YES</td>
</tr>
<tr>
<td>Audio (SPK、MIC、Earphone)</td>
<td>YES</td>
</tr>
<tr>
<td>HDMI1.4 OUT</td>
<td>YES</td>
</tr>
<tr>
<td>MIPI DSI/TP</td>
<td>YES</td>
</tr>
<tr>
<td>MIPI CSI</td>
<td>YES</td>
</tr>
<tr>
<td>TF卡</td>
<td>YES</td>
</tr>
<tr>
<td>SDIO WIFI&BT</td>
<td>YES</td>
</tr>
<tr>
<td>千兆网口10M/100M/1000M (2Port)</td>
<td>YES</td>
</tr>
<tr>
<td>PCIe2.0 2lane Interface (2Port)</td>
<td>YES</td>
</tr>
<tr>
<td>USB2.0 TYPEA</td>
<td>YES</td>
</tr>
<tr>
<td>USB3.0 TYPEA</td>
<td>YES</td>
</tr>
<tr>
<td>UART Debug (3pin+26pin)</td>
<td>YES</td>
</tr>
<tr>
<td>JTAG (26pin)</td>
<td>YES</td>
</tr>
<tr>
<td>System Key</td>
<td>YES</td>
</tr>
</tbody>
</table>

## 硬件介绍

### 实物图

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/UU0LbjG4JoIH2oxR6plcpVKanLr.png)

### 电源框图

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/DgJcbZGhDo4FQTxbAOFcP2oGnqb.png)

### Boot Download Sel&JTAG Sel

SEC2 JTAG 配置电路：K1 SEC2 JTAG 与 MMC1（TF CARD）接口复用，当 JTAG_SEL 拉高，MMC1_CMD 拉低，即可配置为 SEC2 JTAG 调试 X60 CPU
![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/SbuCbsWobovVuexwSK2c55j9nKb.png)

<table>
<tbody>
<tr>
<td>TF卡信号名称</td>
<td>复用JTAG信号</td>
</tr>
<tr>
<td>MMC1_CLK</td>
<td>SEC2_TCK</td>
</tr>
<tr>
<td>MMC1_DATA0</td>
<td>SEC2_TRSTn</td>
</tr>
<tr>
<td>MMC1_DATA1</td>
<td>SEC2_TDO</td>
</tr>
<tr>
<td>MMC1_DATA2</td>
<td>SEC2_TDI</td>
</tr>
<tr>
<td>MMC1_DATA3</td>
<td>SEC2_TMS</td>
</tr>
</tbody>
</table>

Boot Download Sel 配置电路：K1 支持配置 strap pin 选择启动介质。通过拨码开关即可配置，下表为设备启动介质与拨码开关的匹配关系。
![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/I21ub38Y1ozWMpxcrE0c3E0qnUG.png)

<table>
<tbody>
<tr>
<td><strong>开关1</strong></td>
<td><strong>开关2</strong></td>
<td><strong>启动顺序</strong></td>
<td><strong>备注</strong></td>
</tr>
<tr>
<td>OFF</td>
<td>OFF</td>
<td>TF Card-&gt;EMMC<br/></td>
<td>出厂默认配置</td>
</tr>
<tr>
<td>ON</td>
<td>OFF</td>
<td>TF Card-&gt;SPI NOR</td>
<td>SPI NOR默认加载SSD内核</td>
</tr>
</tbody>
</table>

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/VNaNbxVTcoSC5lx5EHQc5dj6n5e.png)
需要注意的是，当设备插入了写入固件的 TF Card，无论拨码开关在何种配置下，设备都会从 TF Card 启动。
当使用拨码开关配置了设备启动路径，刷机时固件会默认刷到该种启动路径下。例如，当拨码开关配置从 SPI NOR 启动时，刷机时固件默认会刷到 SPI NOR 和 SSD，其中需要注意的是，SSD 需要配置在 M.2 一号槽位。
![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/UqEKb1cV5o12upxaUNqcscPOnDd.jpg)

### I2C 地址

开发板预留丰富的外围接口，用户调试 I2C 外设会涉及到 I2C 通道复用情况，下图为现有的开发板器件对应的 I2C 地址和上拉电源，避免地址冲突和电平不匹配。

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/AqcrbA605oR6h3xaK53cLbDinzN.png)

## 模块简述

### 电源输入

MUSE Pi 仅提供一种电源输入方式：Type-C 输入，需使用支持 PD3.0 的适配器，输入电压默认调节为 12V。通过前端降压变换器（buck）电源后，得到电源 VCC5V0\_SYS 与 VCC4V0，分别给外挂 DCDC 和 PMIC 供电，输出不同电压供系统使用。M.2 座 3.3V 供电电流较大，由适配器输入电源通过前端降压变换器（buck）输出得到。

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/ZCKnbt81go9wZPx87iucVS42nTI.png)

### 存储器

eMMC：开发板上存储类型为 eMMC FLASH，默认使用的容量 16GB

SPI Flash：开发板预留 SPI 器件位置

DDR：开发板 DDR 使用一片 4GB LPDDR4X

EEPROM：开发板支持 EEPROM 存储板卡信息

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/EiwZbgt2GoMZucxbSQDc8VkGnfE.png)

### 按键输入

MUSE Pi 支持电源开关按键、烧录按键和复位按键

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/J4l2btpWIoLdrrxDgCyc5F9gnTc.png)

### MIPI CSI 高速连接器

MUSE Pi 不固定支持某一摄像头模组，高速连接器包含两组 4lane 信号，可根据高速连接器对应线序自行设计小板来匹配特定模组，实现 4lane+4lane 或 4lane+2lane+2lane 的摄像头组合

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/Inq7b3oXeox6HfxlHOOcqshwn3g.png)

60pin 高速连接器接口线序如下：

<table>
<tbody>
<tr>
<td>pin</td>
<td>信号名称</td>
<td>信号名称</td>
<td>pin</td>
</tr>
<tr>
<td>1</td>
<td>GND</td>
<td>(悬空)</td>
<td>60</td>
</tr>
<tr>
<td>2</td>
<td>MIPI_CSI_DN0</td>
<td>(悬空)</td>
<td>59</td>
</tr>
<tr>
<td>3</td>
<td>MIPI_CSI_DP0</td>
<td>(悬空)</td>
<td>58</td>
</tr>
<tr>
<td>4</td>
<td>GND</td>
<td>(悬空)</td>
<td>57</td>
</tr>
<tr>
<td>5</td>
<td>MIPI_CSI1_DN1</td>
<td>(悬空)</td>
<td>56</td>
</tr>
<tr>
<td>6</td>
<td>MIPI_CSI1_DP1</td>
<td>(悬空)</td>
<td>55</td>
</tr>
<tr>
<td>7</td>
<td>GND</td>
<td>(悬空)</td>
<td>54</td>
</tr>
<tr>
<td>8</td>
<td>MIPI_CSI1_DN2</td>
<td>(悬空)</td>
<td>53</td>
</tr>
<tr>
<td>9</td>
<td>MIPI_CSI1_DP2</td>
<td>(悬空)</td>
<td>52</td>
</tr>
<tr>
<td>10</td>
<td>GND</td>
<td>(悬空)</td>
<td>51</td>
</tr>
<tr>
<td>11</td>
<td>MIPI_CSI1_DN3</td>
<td>GND</td>
<td>50</td>
</tr>
<tr>
<td>12</td>
<td>MIPI_CSI1_DP3</td>
<td>MIPI_CSI3_DN0</td>
<td>49</td>
</tr>
<tr>
<td>13</td>
<td>GND</td>
<td>MIPI_CSI3_DP0</td>
<td>48</td>
</tr>
<tr>
<td>14</td>
<td>MIPI_CSI1_CLKN</td>
<td>GND</td>
<td>47</td>
</tr>
<tr>
<td>15</td>
<td>MIPI_CSI1_CLKP</td>
<td>MIPI_CSI3_DN1</td>
<td>46</td>
</tr>
<tr>
<td>16</td>
<td>GND</td>
<td>MIPI_CSI3_DP1</td>
<td>45</td>
</tr>
<tr>
<td>17</td>
<td>CAMERA0_RST</td>
<td>GND</td>
<td>44</td>
</tr>
<tr>
<td>18</td>
<td>CAMERA0_PDN</td>
<td>MIPI_CSI3_DN2</td>
<td>43</td>
</tr>
<tr>
<td>19</td>
<td>GND</td>
<td>MIPI_CSI3_DP2</td>
<td>42</td>
</tr>
<tr>
<td>20</td>
<td>CAM_MCLK0</td>
<td>GND</td>
<td>41</td>
</tr>
<tr>
<td>21</td>
<td>GND</td>
<td>MIPI_CSI3_DN3</td>
<td>40</td>
</tr>
<tr>
<td>22</td>
<td>CAM_I2C0_SDA</td>
<td>MIPI_CSI3_DP3</td>
<td>39</td>
</tr>
<tr>
<td>23</td>
<td>CAM_I2C0_SCL</td>
<td>GND</td>
<td>38</td>
</tr>
<tr>
<td>24</td>
<td>GND</td>
<td>MIPI_CSI3_CLKN</td>
<td>37</td>
</tr>
<tr>
<td>25</td>
<td>GND</td>
<td>MIPI_CSI3_CLKP</td>
<td>36</td>
</tr>
<tr>
<td>26</td>
<td>CSI_DVDD12</td>
<td>GND</td>
<td>35</td>
</tr>
<tr>
<td>27</td>
<td>CSI_VCCI018</td>
<td>MIPI_CSI2_CLKN</td>
<td>34</td>
</tr>
<tr>
<td>28</td>
<td>CSI_AVDD28</td>
<td>MIPI_CSI2_CLKP</td>
<td>33</td>
</tr>
<tr>
<td>29</td>
<td>CSI_AFVCC28</td>
<td>GND</td>
<td>32</td>
</tr>
<tr>
<td>30</td>
<td>CAMERA1_PDN</td>
<td>CAMERA1_RST</td>
<td>31</td>
</tr>
</tbody>
</table>

### MIPI DSI 屏连接座

开发板支持 1080P 屏（JL-M101N013-P12WU-M402632），屏座接口型号为 FH35C-31S-0.3SHW(50)

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/PHNWbm0A7ofQaBxJgeIcC6TwnRd.png)

屏接口顺序

<table>
<tbody>
<tr>
<td>pin</td>
<td>信号名称</td>
<td>信号名称</td>
<td>pin</td>
</tr>
<tr>
<td>1</td>
<td>MIPI_DSI1_LANE0_DN</td>
<td>MIPI_DSI1_LANE0_DP</td>
<td>2</td>
</tr>
<tr>
<td>3</td>
<td>GND</td>
<td>MIPI_DSI1_LANE1_DN</td>
<td>4</td>
</tr>
<tr>
<td>5</td>
<td>MIPI_DSI1_LANE1_DP</td>
<td>GND</td>
<td>6</td>
</tr>
<tr>
<td>7</td>
<td>MIPI_DSI1_CLK_N</td>
<td>MIPI_DSI1_CLK_P</td>
<td>8</td>
</tr>
<tr>
<td>9</td>
<td>GND</td>
<td>MIPI_DSI1_LANE2_DN</td>
<td>10</td>
</tr>
<tr>
<td>11</td>
<td>MIPI_DSI1_LANE2_DP</td>
<td>GND</td>
<td>12</td>
</tr>
<tr>
<td>13</td>
<td>MIPI_DSI1_LANE3_DN</td>
<td>MIPI_DSI1_LANE3_DP</td>
<td>14</td>
</tr>
<tr>
<td>15</td>
<td>GND</td>
<td>MIPI_LCD_ADC_1V8</td>
<td>16</td>
</tr>
<tr>
<td>17</td>
<td>LCD_PWR_EN_1V8</td>
<td>LCD_RST_1V8</td>
<td>18</td>
</tr>
<tr>
<td>19</td>
<td>LCD_BL_EN_1V8</td>
<td>LCD_BL_PWM_1V8</td>
<td>20</td>
</tr>
<tr>
<td>21</td>
<td>GND</td>
<td>TP_INT_1V8</td>
<td>22</td>
</tr>
<tr>
<td>23</td>
<td>TP_RST_1V8</td>
<td>AP_12C6_SCL</td>
<td>24</td>
</tr>
<tr>
<td>25</td>
<td>AP_12C6_SDA</td>
<td>LCD_VCC18</td>
<td>26</td>
</tr>
<tr>
<td>27</td>
<td>GND</td>
<td>GND</td>
<td>28</td>
</tr>
<tr>
<td>29</td>
<td>LCD_VCC5V0</td>
<td>LCD_VCC5V0</td>
<td>30</td>
</tr>
<tr>
<td>31</td>
<td>LCD_VCC5V0</td>
<td>GND</td>
<td>32</td>
</tr>
<tr>
<td>33</td>
<td>GND</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/OOucbXhbQoFVuLxdLdncYDJBnWe.png)

### Type-C 连接器

开发板 Type-C 连接器，支持 USB2.0 DEVICE，内置调压芯片支持 PD3.0 协议调压到 12V 给 MUSE Pi 供电

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/M6awbbwv8o1WkZxzO4pc9kgOnwh.png)

### HDMI 输出接口

开发板支持一路 HDMI 标准 A 输出接口，最大支持 HDMI1.4，最大可支持 1080p 60fps 视频输出

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/Ix06beoV0oTRxUx4rOncNF8Jn4T.png)

### USB 接口

开发板提供一个 USB2.0 接口和一个 USB3.0 接口，方便开发者接入 USB 设备

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/DxyKbIRC7oUqjQxlot7c500mnWf.png)

### RJ45 接口

开发板支持 2 个 RJ45 千兆网接口

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/YP1Eb994son3axxSgn3cbE82n4c.png)

### wifi/BT 模组

开发板支持 wifi/BT 模组，支持无线上网和蓝牙功能

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/MgUDbMudYoZ3zDxzz7ac3uTnnJf.png)

### 26pin 接口

开发板支持 26pin 双排插针，线序如下：

PS: **粗体**为当前默认功能，若要使用其他功能需要自行配置

<table>
<tbody>
<tr>
<td>pin</td>
<td>管脚定义</td>
<td>信号名称</td>
<td>pin</td>
</tr>
<tr>
<td>1</td>
<td>VCC3V3_SYS</td>
<td>VCC5V0_OUT</td>
<td>2</td>
</tr>
<tr>
<td>3</td>
<td><strong>AP_I2C4_SDA_3V3</strong><br/>{GPIO[52] / R_SPI_RXD / R_UART1_RXD / R_PWM7}</td>
<td>VCC5V0_OUT</td>
<td>4</td>
</tr>
<tr>
<td>5</td>
<td><strong>AP_I2C4_SCL_3V3</strong><br/>{R_SPI_TXD / R_UART1_TXD / R_PWM6}</td>
<td>GND<br/></td>
<td>6</td>
</tr>
<tr>
<td>7</td>
<td><strong>PRI_TDI</strong><br/>{GPI0_70_3V3 / AP_I2C2_SCL_3V3 / UART5_TXD}</td>
<td><strong>R_UART0_TXD_3V3</strong><br/>{GPIO[47] / R_CAN_TX0 / R_PWM8 / AP_I2C3_SCL}</td>
<td>8</td>
</tr>
<tr>
<td>9</td>
<td>GND</td>
<td><strong>R_UART0_RXD_3V3</strong><br/>{GPIO[48] / R_CAN_RX0 / R_IR_RX / AP_I2C3_SDA / KP_MKOUT[2]}</td>
<td>10</td>
</tr>
<tr>
<td>11</td>
<td><strong>GPIO_71_3V3</strong><br/>{PRI_TMS / AP_I2C2_SDA_3V3 / UART5_RXD}</td>
<td><strong>GPI0_74_3V3</strong><br/>{R_PWM9 / PCIe2_WAKEN}</td>
<td>12<br/></td>
</tr>
<tr>
<td>13</td>
<td><strong>GPI0_72_3V3</strong><br/>{PRI_TCK / UART9_TXD / UART5_CTS_N}</td>
<td>GND</td>
<td>14</td>
</tr>
<tr>
<td>15</td>
<td><strong>GPI0_73_3V3</strong><br/>{PRI_TDO / UART9_RXD / UART5_RTS_N}</td>
<td><strong>GPIO_91_3V3</strong><br/>{MN_CLK2 / DSI_TE / R_I2C0_SCL}</td>
<td>16</td>
</tr>
<tr>
<td>17</td>
<td>VCC3V3_SYS</td>
<td><strong>GPIO_92_3V3</strong><br/>{MN_CLK / PWM7 / R_I2C0_SDA}</td>
<td>18</td>
</tr>
<tr>
<td>19</td>
<td><strong>SPI3_MOSI_3V3</strong><br/>{GPIO[77] / SPI2_MOSI / AP_I2C3_SCL / UART8_CTS_N / R_PWM0 / KP_MKOUT[2] / AP_CW[14]}</td>
<td>GND</td>
<td>20<br/></td>
</tr>
<tr>
<td>21</td>
<td><strong>SPI3_MISO_3V3</strong><br/>{GPIO[78] / SPI2_MISO / AP_I2C3_SDA / UART8_RTS_N / R_PWM1 / KP_MKIN[3] / AP_CW[15]}</td>
<td><strong>GPIO_49_3V3</strong><br/>{R_SPI_SCLK / R_UART1_CTS_N / R_PWM4 / R_I2C0_SCL / KP_MKIN[3]}</td>
<td>22</td>
</tr>
<tr>
<td>23</td>
<td><strong>SPI3_SCLK_3V3</strong><br/>{GPIO[75] / SPI2_SCLK / CAN_TX0 / UART8_TXD / AP_I2C4_SCL / AP_CW[12]}</td>
<td><strong>SPI3_CS_3V3</strong><br/>{GPIO[76] / SPI2_CS / CAN_RX0 / UART8_RXD / AP_I2C4_SDA / AP_CW[13]}</td>
<td>24</td>
</tr>
<tr>
<td>25</td>
<td>GND</td>
<td><strong>GPIO_50_3V3</strong><br/>{R_SPI_FRM / R_UART1_RTS_N / R_PWM5 / R_I2C0_SDA / KP_MKOUT[3]}</td>
<td>26</td>
</tr>
</tbody>
</table>

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/OTq5bmXsKoL0yvxeFEecRjO9nAl.png)

### JTAG 调试接口

开发板在 26pin 接口中预留 Primary JTAG 调试通道，线序如下

<table>
<tbody>
<tr>
<td>26pin</td>
<td>网络名称</td>
<td>JTAG信号名称</td>
</tr>
<tr>
<td>7</td>
<td>GPI0_70_3V3</td>
<td>PRI_TDI</td>
</tr>
<tr>
<td>11</td>
<td>GPIO_71_3V3</td>
<td>PRI_TMS</td>
</tr>
<tr>
<td>13</td>
<td>GPI0_72_3V3</td>
<td>PRI_TCK</td>
</tr>
<tr>
<td>15</td>
<td>GPI0_73_3V3</td>
<td>PRI_TDO</td>
</tr>
</tbody>
</table>

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/K58IbYfwPofrL3xxCMHcTElSnOb.png)

### UART 调试接口

开发板设计 3pin 单排插针，支持 UART0（GPIO68-TX，GPIO69-RX）调试接口，主控端线序从左到右 TX，RX，GND

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/QapBb4Grzo6MSBxMeG0cytWwnjf.png)

### 音频接口

开发板预留 2 个 speaker 接口，支持 3.5mm 耳机座

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/IGZdb9qjCojDYmx58EBczsM2nGc.png)

### TF 卡接口（无弹片）

开发板支持 TF 卡，方便开发者接入 TF 卡设备。同时支持 debug 扩展卡，用于 UART0 或 JTAG 调试

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/OysebDRv2oC1i8xYLHQc5IiGnSe.png)

### M.2 KEY M 接口

开发板支持 M.2KEYM 接口，方便开发者接入 SSD 以及其他 M.2KEYM 设备，同时支持连接 JMB582 扩展卡转 SATA

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/NM1ObtE7Po2BPyxKq6RcfNOZncc.png)

## 初次设置

### 使用前准备

MUSE Pi 是开发板形态产品，因此您需要连接必要的外设来使用它

**电源适配器**

MUSE Pi 采用 USB-PD3.0 协议 Type-C 接口供电/充电，您可以使用任何提供正确电源模式的通过相关质量认证的 Type-C 电源适配器，建议电源适配器最大功率不低于 30W。

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/TKpAbIk80oOdqKx2hWbcEUjynvd.jpg)

**键盘＆鼠标：**

您可以使用 MUSE Pi 上的任一 USB-A 端口连接有线键盘/鼠标或 USB 接收器，以及通过蓝牙的方式连接键鼠。

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/GcuAbV3Veoff4JxnF9jcXNLSnyb.jpg)

**显示器：**

MUSE Pi 需要通过外置显示器将画面显示出来。MUSE Pi 支持 HDMI 和 MIPI DSI 视频接口，因此您可以连接或同时连接带有 HDMI 或者 MIPI DSI 视频接口的显示器。

请注意，若要通过 MIPI DSI 视频接口输出画面，请在开机前就将 MIPI DSI 视频线连接好显示器和 MUSE Pi，MUSE Pi 的 MIPI DSI 视频接口不支持热插拔。

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/MJUObpLssoPZM0xcmdZcX92Inve.jpg)

**音频：**

MUSE Pi 可以通过 HDMI 信号在显示器上进行音频的输出。

除此之外，您还可以使用机身侧 I/O 的 3.5mm 耳麦孔来连接音频外设。

您可以通过声卡设置，切换音频孔声卡（ES8326）或 HDMI 声卡。

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/C7MWbYgtVoA7Rnx323WcgH7qntg.jpg)

**网络连接：**

MUSE Pi 支持有线 RJ45 网口，您可以通过 RJ45 网口直接与网线连接，如连接单根网线，两个网口可任选其一。

MUSE Pi 支持无线 WiFi 和蓝牙的连接，如需增强信号，可以安装天线。

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/Fphyb7cg0oICmbx6jAvcWtL7nVe.jpg)

### 开始启动

**提前连接您的所需要的外设，并按下启动按钮：**

将设备通过视频连接线连接到显示器，同时连接上键盘和鼠标。

最后连接上电源线，并通电即可开机。（首次通电即开机，若软件关机后，需短按电源按钮 1S 即可开机），开发板运行后，红色的电源指示灯会亮起。

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/ZA9gbmazLoHDyYxE9UKcdGo1nle.jpg)

### 首次启动时配置

您的 MUSE Pi 会预装进迭时空 Bianbu desktop 操作系统，将在首次启动时运行配置向导。您需要显示器、键盘、鼠标来浏览向导。

**系统语言：**

此页面帮助您配置系统的语言，默认显示 English 和中文，如需更多语言，可点击下方三个点，弹出更多选项。

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/EHycbxUnCo6t7MxkYjucK6fFnRb.png)

**输入法：**

此页面帮助您配置系统的键盘布局和输入法

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/AMvNbbdRBoaxtzxUiRJcTydnnSh.png)

**无线上网：**

此页面帮助您连接到 WiFi 网络，从列表中选择您的网络并进行连接；如暂未有合适 WiFi 网络，可在左上角选择跳过该设置

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/VRxkbkGnjo25KexMtbjc8qFMnJb.png)

**位置服务：**

此页面可选择是否打开位置服务，如打开位置服务可便捷您的使用体验，但相应的可能会带来位置隐私泄露的风险

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/FMLxbzlVlo2HYixvSD9cGPmLn3i.png)

**时区：**

此页面帮助配置您所在时区信息，联网状态下系统能够自动同步相应时区时间，可以搜索城市来添加设置

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/EoDibot8HoJJcQx6YebctOdhnae.png)

**设置您的用户名和密码：**

该页面帮助您设置用户名和密码，请牢记您的密码

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/RJHvb3W74oc1a4xnoahcZovinte.png)

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/UwiNbhcmfonYzdxBwYfc38hcnxg.png)

**配置完成**

配置完成，点击“开始使用 Bianbu”吧，后可进入桌面

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/ANTIbhchEoc246xlJAoculU8nuc.png)

## 刷入固件

### 进入刷机模式

- 设备未上电，处于关机状态时

1）按住“DOWNLOAD（FDL）按键”不松开

2）插上电源线

3）松开“DOWNLOAD（FDL）按键”

4）插上 USB 数据线到刷机 USB 连接器，通过进迭时空官方刷机工具 Titan 或者 fastboot 命令即可进行刷机操作

- 设备已上电，处于开机状态时

1）按住 FDL 按键不松开

2）短按 Reset 键

3）松开 FDL 按键

4）插上 USB 数据线到刷机 USB 连接器，通过进迭时空官方刷机工具 Titan 或者 fastboot 命令即可进行刷机操作

**注意：**请使用 USB 数据线刷机

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/CrVUbq9c0oABJ6xKFUZct510nqh.png)

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/IOK1bGhMWoJshdx0zKocr6psnsg.png)

### 固件下载和安装

### Bianbu

**Bianbu 简介：**

Bianbu 是进迭时空针对 RISC-V 架构的处理器做了深度优化的操作系统，MUSEBook 适用于并出厂预装 Bianbu Desktop 版本。同时 MUSE Pi 适用于 Bianbu NAS 版本。

**Bianbu 网站：**

如需获取更多 Bianbu 相关信息，详见：[简介 | Bianbu | 进迭时空开发者社区](https://bianbu.spacemit.com/)

**Bianbu desktop/NAS 固件下载地址：**

[Index of /image/k1/version/bianbu](https://archive.spacemit.com/image/k1/version/bianbu/)

其中含有 NAS 字样的固件包，为 Bianbu NAS 的固件

## 串口调试

### 接口连接：

上位机经 USB 转 TTL 设备与 MUSE Pi 主板接口的 TX、RX、GND 正常连接。接口信号如图：

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/IFdZbWTHgok9OGxDCe9cONGAntb.png)

### Windows 调试：

以“MobaXterm”为例：

首先，请正确连接硬件串口，并确认在设备管理器的端口中有 COM 口的显示，如图：

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/RK7wbPdAQo9jK5x3lf4c5Xgon1f.png)

打开“MobaXterm”软件，选择“Sessions”——“New Session”，在弹出的对话框中，选择“Serial”，"Serial port"选择上图中识别到的对应 COM 口，**“Speed”速率选择“115200”**，最后点击“OK”，即可进入打印页面

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/LUQlb4oNIoZFuBxeDxVcBBVHnJe.png)

![](https://cdn-resource.spacemit.com/eco/docs-product/zh/k1_muse_pi/static/RZ7pbCq29ockQaxrUhdcFJyonsc.png)

## 注意事项

K1 MUSE_PI 适用于实验室或者工程环境，开始操作前，请先阅读以下注意事项：

1. 任何情况下不可对屏幕接口、CSI 接口及扩展板进行热插拔操作。
2. 拆封开发板包装和安装前，为避免静电释放（ESD）对开发板硬件造成损伤，请采取必要防静电措施。
3. 持开发板时请拿开发板边沿，不要触碰到开发板上的外露金属部分，以免静电对开发板元器件造成损坏。
4. 请将开发板放置于干燥的平面上，以保证它们远离热源、电磁干扰源与辐射源、电磁辐射敏感设备（如：医疗设备）等。
