---
title: "进迭云平台使用指南"
lang: zh
category: "云/使用手册"
source_page: https://www.spacemit.com/community/document/info?nodepath=cloud/userguide/cloud_user_guide.md&lang=zh
source_file: https://cdn-resource.spacemit.com/cloud/userguide/docs-cloud/zh/cloud_user_guide.md
updated: "2026-09-11 14:23:44"
---
# 进迭云平台使用指南

本文档为进迭云平台官方使用说明，面向平台新用户及开发者，系统介绍账号注册、实例申请、远程连接、平台应用、本地接入、API 调用及开发示例等内容，帮助用户高效完成环境准备、资源接入与业务开发。

## 1. 文档说明

### 1.1 适用范围

本文档适用于进迭云平台的常见使用场景，包括但不限于：

- 注册与登录平台
- 申请并管理云实例
- 通过网页或本地工具远程连接实例
- 使用平台内置应用与开发环境
- 调用实例开放接口进行二次开发

### 1.2 平台访问地址

平台访问地址：[https://gdriscv.com](https://gdriscv.com)

## 2. 注册与登录

### 2.1 注册账号

访问平台官网后，点击首页 **立刻注册** 进入注册流程。

<img src="../../../_assets/docs-cloud/static/register.png" alt="" width="600">

当前平台支持以下注册方式：

- 手机号注册（现仅支持中国国内手机号）
- 邮箱注册

#### 手机号注册

<img src="../../../_assets/docs-cloud/static/reg_phone.png" alt="" width="600">

#### 邮箱注册

<img src="../../../_assets/docs-cloud/static/reg_email.png" alt="" width="600">

### 2.2 登录平台

注册完成后，点击 **立即登录** 进入登录页面。

平台支持以下登录方式：

- 短信登录
- 密码登录

<img src="../../../_assets/docs-cloud/static/login.png" alt="登录页面" width="600">

登录成功后，系统将进入平台主界面。

<img src="../../../_assets/docs-cloud/static/main.png" alt="平台主界面" width="800">

## 3. 申请实例

在平台主界面，**我的示例** 里

- 如果没有实例，点击 **申请实例**，即可进入实例创建页面。
  <img src="../../../_assets/docs-cloud/static/instancex00.png" alt="" width="800">

- 如果已有实例，可点击 **申请新的实例**，即可进入实例创建页面。
  <img src="../../../_assets/docs-cloud/static/instancex01.png" alt="" width="800">

实例创建页面示例如下。
<img src="../../../_assets/docs-cloud/static/instance.png" alt="申请实例页面" width="800">

### 3.1 选择实例类型

平台提供多种实例创建方式，用户可根据业务目标、开发环境及算力需求选择合适的实例类型。

#### 3.1.1 基于操作系统镜像创建

支持的操作系统镜像包括：

- Bianbu
- Deepin
- OpenHarmony
- openKylin

<img src="../../../_assets/docs-cloud/static/instance_os.png" alt="操作系统镜像列表" width="800">

#### 3.1.2 基于快应用模板创建

支持的快应用模板包括：

- 通义 Qwen 大模型
- Deepseek 大模型
- 在线 Python 开发环境 JupyterLab

<img src="../../../_assets/docs-cloud/static/instance_app.png" alt="" width="800">

#### 3.1.3 基于 RISC-V 算力融合集群创建

该类型适用于需要调用 RISC-V 异构算力资源的开发、验证与计算任务。

<img src="../../../_assets/docs-cloud/static/instance_riscv.png" alt="" width="800">

### 3.2 设置实例名称

输入实例名称，并勾选相关协议后提交申请。

<img src="../../../_assets/docs-cloud/static/instance2.png" alt="" width="600">

### 3.3 选择实例使用时长

<img src="../../../_assets/docs-cloud/static/instance_time.png" alt="" width="400">

- **非会员用户**：可选 48 小时、7 天、1 个月
- **会员用户**：最长可选 3 个月

### 3.4 创建实例

完成配置后，可点击 **开始使用** 完成创建实例

<img src="../../../_assets/docs-cloud/static/instance_start.png" alt="" width="600">

## 4. 远程使用实例

实例创建成功后，可在控制台查看当前账号下已开通的实例资源。

<img src="../../../_assets/docs-cloud/static/myinstance.png" alt="" width="600">

点击实例卡片，可查看实例详情、运行状态及可用功能入口。

<img src="../../../_assets/docs-cloud/static/myinstance2.png" alt="" width="600">

### 4.1 命令行访问

点击 **开始远程**

<img src="../../../_assets/docs-cloud/static/remote_start.png" alt="" width="400">

进入实例命令行工作台

<img src="../../../_assets/docs-cloud/static/instance_remote.png" alt="远程命令行界面" width="800">

命令行界面支持：

- 多会话管理
- 分屏操作

<img src="../../../_assets/docs-cloud/static/instance_remote2.png" alt="" width="800">

使用完成后，点击右上角 **退出** 图标返回平台主界面。

<img src="../../../_assets/docs-cloud/static/instance_remote3.png" alt="" width="800">

### 4.2 串口调试

在工作台点击 **串口调试** 按钮，可进入串口终端界面。

<img src="../../../_assets/docs-cloud/static/instance_serial.png" alt="" width="800">

### 4.3 文件管理与在线编辑

在工作台左上角点击 **文件**，可打开文件树或文件管理视图。

<img src="../../../_assets/docs-cloud/static/instance_file.png" alt="" width="800">

在文件树中右键目录或文件，可执行以下操作：

- 上传
- 下载
- 刷新
- 新建文件
- 新建目录

<img src="../../../_assets/docs-cloud/static/instance_file2.png" alt="" width="800">

<img src="../../../_assets/docs-cloud/static/instance_file3.png" alt="" width="800">

双击文件（如 `.profile`）后，可直接进行在线编辑。

<img src="../../../_assets/docs-cloud/static/instance_file4.png" alt="" width="800">

编辑完成后，点击右上角 **保存** 图标以提交修改。

<img src="../../../_assets/docs-cloud/static/instance_file5.png" alt="" width="800">

### 4.4 远程桌面

在工作台顶部点击 **远程桌面**，可开启或关闭图形化远程桌面模式。

若该按钮处于禁用状态，请先切换回 Terminal 或串口界面。

<img src="../../../_assets/docs-cloud/static/remote_desk00.png" alt="" width="800">

<img src="../../../_assets/docs-cloud/static/remote_desk01.png" alt="" width="800">

远程桌面支持以下功能：

- 尺寸调整
- 全屏显示

### 4.5 实例重启

点击顶部 **控制** 选项后，可执行以下管理操作：

- 电源重启
- 系统重启

<img src="../../../_assets/docs-cloud/static/instance_reboot.png" alt="" width="800">

### 4.6 实例刷机

在工作台顶栏点击 **刷机**，可执行以下操作：

- 打开刷机面板
- 关闭刷机面板
- 在右侧镜像列表中选择目标镜像并点击 **烧写** 图标

<img src="../../../_assets/docs-cloud/static/instance_flash.png" alt="实例刷机界面" width="800">

> 刷机操作通常会影响实例当前环境与数据，建议提前完成重要数据备份。

## 5. 平台内置应用

### 5.1 Code Server

在工作台顶部点击 **应用 → code-server**：

- **打开**：启动 Code Server 在线 IDE
- **关闭**：停止 Code Server

<img src="../../../_assets/docs-cloud/static/code_server.png" alt="" width="800">

#### 安装 Python 插件

在左侧扩展面板中搜索 `python`，安装对应插件后即可使用在线 Python 开发能力。

<img src="../../../_assets/docs-cloud/static/python00.png" alt="" width="800">

<img src="../../../_assets/docs-cloud/static/python01.png" alt="" width="800">

### 5.2 JupyterLab

在工作台顶部点击 **应用 → JupyterLab**：

- **打开**：进入 JupyterLab
- **关闭**：退出 JupyterLab

**说明：** JupyterLab 仅在快应用模板中的 JupyterLab 实例可用，其他操作系统镜像和 AI 镜像默认不提供该应用。

<img src="../../../_assets/docs-cloud/static/jupyterlab.png" alt="JupyterLab 应用" width="800">

### 5.3 通义 Qwen 大模型应用

在工作台顶部点击 **应用 → qwen-ai**：

- **打开**：进入 Qwen 应用
- **关闭**：退出 Qwen 应用

<img src="../../../_assets/docs-cloud/static/qwen00.png" alt="Qwen 应用" width="800">

也可通过右侧 **AI** 图标快速进入相关能力入口。

<img src="../../../_assets/docs-cloud/static/ai.png" alt="AI 快捷入口" width="800">

### 5.4 Deepseek 大模型应用

在工作台顶部点击 **应用 → deepseek-ai**：

- **打开**：进入 Deepseek 应用
- **关闭**：退出 Deepseek 应用

<img src="../../../_assets/docs-cloud/static/deepseek.png" alt="账户管理入口" width="800">

同样支持通过右侧 **AI** 图标快速访问。

## 6. 账户管理

### 6.1 修改个人信息

在系统控制台页面，点击右上角 **用户图标**，进入 **账户管理界面**。

<img src="../../../_assets/docs-cloud/static/user00.png" alt="账户管理界面" width="800">

在账户设置页面点击 **“编辑个人信息”**。

<img src="../../../_assets/docs-cloud/static/user01.png" alt="编辑个人信息入口" width="800">

当前支持维护以下账户信息：

- 用户名
- 密码
- 手机号
- 邮箱

<img src="../../../_assets/docs-cloud/static/user02.png" alt="个人信息修改页面" width="500">

以下示例展示了手机号修改页面：

<img src="../../../_assets/docs-cloud/static/user03.png" alt="修改手机号示例" width="500">

保存完成后，点击 **返回系统** 即可返回账户管理界面。

### 6.2 消息中心

在账户管理界面点击左侧 **消息中心** 页签，可统一查看平台消息通知。

<img src="../../../_assets/docs-cloud/static/info.png" alt="消息中心" width="800">

### 6.3 实例共享

在账户管理界面点击左侧 **实例共享** 页签，可将个人实例资源共享给其他用户。

<img src="../../../_assets/docs-cloud/static/instance_share.png" alt="实例共享" width="800">

### 6.4 API Key 管理

在账户管理界面点击左侧 **API Key** 页签，可进行 API Key 管理。

API Key 主要用于远程调用实例提供的 API 接口。

<img src="../../../_assets/docs-cloud/static/apikey.png" alt="API Key 管理" width="800">

### 6.5 告警信息

在账户管理界面点击左侧 **告警信息** 页签，可查看实例相关告警状态。

<img src="../../../_assets/docs-cloud/static/notices.png" alt="告警信息" width="800">

## 7. 本地连接实例

### 7.1 SSH 直连

平台支持通过本地 SSH 客户端直连实例。进行 SSH 直连前，需要先启用 **TLS 隧道**，推荐使用 Stunnel。

#### 7.1.1 安装 Stunnel 客户端

- Windows： [https://www.stunnel.org/downloads/stunnel-latest-win64-installer.exe](https://www.stunnel.org/downloads/stunnel-latest-win64-installer.exe)
- Ubuntu/Debian：

  ```bash
  sudo apt install stunnel4
  ```

- CentOS/RHEL：

  ```bash
  sudo yum install stunnel
  ```

#### 7.1.2 获取 Stunnel 配置

在控制台点击目标实例卡片。

<img src="../../../_assets/docs-cloud/static/instance00.png" alt="实例卡片" width="800">

点击 **本地连接**，弹出连接信息与操作说明页面。

<img src="../../../_assets/docs-cloud/static/local_connect.png" alt="本地连接说明" width="600">

将页面中的配置信息复制至 Stunnel 客户端配置文件，并启动或重新加载 Stunnel 服务。

<img src="../../../_assets/docs-cloud/static/config.png" alt="Stunnel 配置示例" width="600">

Linux 环境下可直接使用对应 Stunnel 配置文件启动服务。

<img src="../../../_assets/docs-cloud/static/linux_stunnel.png" alt="Linux 启动 Stunnel" width="800">

#### 7.1.3 通过命令行连接

示例命令如下：

```bash
ssh -p 2222 root@localhost
```

<img src="../../../_assets/docs-cloud/static/cmd.png" alt="SSH 命令行连接" width="600">

#### 7.1.4 通过 MobaXterm 连接

<img src="../../../_assets/docs-cloud/static/moba00.png" alt="MobaXterm SSH 配置" width="800">

使用 MobaXterm 连接时，需明确指定 SSH 协议版本为 **SSHv2**。

操作步骤如下：

1. 选择 **Advanced SSH settings** 标签。
2. 点击 **Expert SSH settings**。
3. 将 **SSH protocol version** 设置为 **SSHv2**。
4. 点击 **OK** 完成连接。

<img src="../../../_assets/docs-cloud/static/sshv2.png" alt="设置 SSHv2" width="600">

#### 7.1.5 获取用户密码

<img src="../../../_assets/docs-cloud/static/password00.png" alt="连接信息页面" width="800">

用户密码可在 **连接信息** 页面末尾获取。

<img src="../../../_assets/docs-cloud/static/password01.png" alt="用户密码位置" width="600">

### 7.2 VNC 直连

VNC 直连与 SSH 直连类似，建立连接前同样需要先完成 Stunnel 配置。

以 MobaXterm 为例：

1. 完成 Stunnel 配置。
2. 点击左侧 **Session**。
3. 选择 **VNC**。
4. 地址填写 `localhost`。
5. 端口填写 `5901`。
6. 点击 **OK** 建立连接。

如需输入密码，请参考上一节中 **用户密码** 的说明。

<img src="../../../_assets/docs-cloud/static/vnc.png" alt="VNC 连接配置" width="800">

连接成功后界面示例如下：

![](../../../_assets/docs-cloud/static/remote_connected.png)

## 8. API 调用

### 8.1 Ollama 接口调用

当前该能力仅支持以下实例类型：

- 通义 Qwen 大模型实例
- Deepseek 大模型实例

进入实例工作台后，参考 [4.1 命令行访问](cloud_user_guide.md#41-命令行访问)，点击右侧 **“API 调用”** 按钮，打开配置页面。

<img src="../../../_assets/docs-cloud/static/api00.png" alt="API 调用入口" width="800">

<img src="../../../_assets/docs-cloud/static/api01.png" alt="API 配置页面" width="800">

完成请求头配置后，即可通过页面提供的 URL 调用 Ollama 接口。

<img src="../../../_assets/docs-cloud/static/api02.png" alt="API 请求头配置" width="800">

<img src="../../../_assets/docs-cloud/static/api03.png" alt="API 调用示例" width="800">

### 8.2 自定义接口调用

实例支持通过指定端口 `18080` 部署并对外访问自定义服务。

例如，可在实例中运行 Python HTTP 服务：

<img src="../../../_assets/docs-cloud/static/python_http.png" alt="Python HTTP 服务示例" width="600">

随后可使用 Postman 发送 GET 或 POST 请求，其中 `deviceId` 为实例设备 ID。

<img src="../../../_assets/docs-cloud/static/postman.png" alt="Postman 调用示例" width="800">

API Key 可参考 [6.4 API Key 管理](cloud_user_guide.md#64-api-key-管理) 获取。

<img src="../../../_assets/docs-cloud/static/apikey.png" alt="API Key 获取页面" width="800">

请求地址格式如下：

```text
https://gdriscv.com/api/remote/{deviceId}
```

<img src="../../../_assets/docs-cloud/static/address00.png" alt="请求地址示例1" width="800">

<img src="../../../_assets/docs-cloud/static/address01.png" alt="请求地址示例2" width="800">

## 9. 开发示例

本章提供典型开发场景示例，帮助用户快速理解平台在 RISC-V 与 AI 开发方向上的使用方式与能力边界。

### 9.1 RISC-V 汇编与向量开发

#### 9.1.1 RVV 编程

RVV（RISC-V Vector）扩展面向高性能向量计算场景。相较于 ARM NEON / SVE，RVV 在向量长度配置与硬件适配性方面具备更高灵活性。

下表给出了 RVV 与 ARM SVE 的简要对比：

| 特性 | SVE (ARM) | RVV (RISC-V) |
| --- | --- | --- |
| 指令集架构 | ARM v8/v9 的扩展 | RISC-V 官方矢量扩展（V 扩展） |
| 设计哲学 | 硬件透明性优先，强调代码兼容性 | 灵活性与可配置性优先，允许硬件定制 |
| 寄存器结构 | 独立谓词寄存器（P0-P15）+ Z 寄存器 | 通用寄存器复用为掩码，矢量寄存器可配置 |
| 最小实现要求 | 必须支持 128 位矢量 | 无固定最小长度，可从 128 位扩展 |
| 编程模型 | 强调编译器自动优化 | 更适合结合硬件特性进行手动优化 |
| 数据类型支持 | 支持 FP32/FP64、INT8/16/32/64 等 | 支持 FP16/32/64、INT8/16/32/64 等 |
| 内存访问模式 | 支持复杂寻址 | 更强调显式内存操作 |
| 应用场景 | ARM 生态的高性能计算（服务器、超算） | RISC-V 定制化场景（AIoT、边缘计算） |

核心代码示例如下：

```c
void vector_add_rvv(int32_t* vec1, int32_t* vec2, int32_t* result, size_t size) {
    // 设置向量长度
    size_t v1;

    for (size_t i = 0; i < size; i += v1) {
        // 动态设置向量长度，如果__riscv_vsetvlmax_e32m4()>size-i，长度会被设置为size-i，否则会被设置为__riscv_vsetvlmax_e32m4()
        v1 = __riscv_vsetvl_e32m4(size - i);

        vint32m4_t v1 = __riscv_vle32_v_i32m4(&vec1[i], v1);  // 加载 vec1
        vint32m4_t v2 = __riscv_vle32_v_i32m4(&vec2[i], v1);  // 加载 vec2
        vint32m4_t vresult = __riscv_vadd_vv_i32m4(v1, v2, v1);  // 向量加法
        __riscv_vse32_v_i32m4(&result[i], vresult, v1);  // 存储结果
    }
}
```

在云实例中，可通过 Code Server 编辑代码，并使用 `gcc` 完成编译与运行验证。

<img src="../../../_assets/docs-cloud/static/rvv00.png" alt="RVV 代码编辑" width="800">

<img src="../../../_assets/docs-cloud/static/rvv01.png" alt="RVV 运行结果" width="600">

#### 9.1.2 RISC-V AI 指令编程

K1 是一款 8 核 RISC-V AI CPU。在 RISC-V 开源指令集基础上，K1 增加了通用 AI 计算能力，可提供约 50 KDMIPS CPU 算力和 2.0 TOPS AI 算力。

该芯片支持 RISC-V Vector 1.0 标准，具备 256-bit 向量计算带宽，可为高性能 AI 计算提供较强的 SIMD 并行处理能力。

<img src="../../../_assets/docs-cloud/static/ai-cpu.png" alt="K1 AI CPU" width="800">

核心示例代码：

<img src="../../../_assets/docs-cloud/static/demo00.png" alt="AI 指令示例代码" width="800">

通过 Code Server 编辑与编译示例：

<img src="../../../_assets/docs-cloud/static/demo01.png" alt="AI 指令编译示例" width="800">

运行结果：

<img src="../../../_assets/docs-cloud/static/demo03.png" alt="AI 指令运行结果" width="500">

#### 9.1.3 卷积优化示例

卷积神经网络（CNN）广泛用于图像分类、目标检测和图像分割等任务。卷积操作通过局部感知和参数共享机制，有效降低模型参数规模并提升推理效率。

以下为 1×3 卷积优化示例：

<img src="../../../_assets/docs-cloud/static/cnn00.png" alt="卷积核心代码" width="800">

在云实例中的编辑界面如下：

<img src="../../../_assets/docs-cloud/static/cnn01.png" alt="卷积示例编辑界面" width="800">

运行结果如下：

<img src="../../../_assets/docs-cloud/static/cnn02.png" alt="卷积运行结果" width="500">

### 9.2 AI 开发示例

#### 9.2.1 YOLOv8 姿态识别

YOLOv8-pose 是基于 YOLOv8 的人体姿态估计模型，可对人体目标进行检测并输出关键点位置，适用于动作识别、运动分析、人机交互等场景。

本示例展示在 RISC-V AI 算力环境下完成姿态识别开发的基础流程。

##### 步骤 1：下载代码

```bash
git clone https://gitee.com/bianbu/spacemit-demo.git
```

##### 步骤 2：下载模型

```bash
cd spacemit-demo/examples/CV/yolov8-pose/model
sh download_model.sh
```

模型下载完成后将获得：

- FP32 模型：`yolov8n-pose.onnx`
- INT8 模型：`yolov8n-pose.q.onnx`

##### 步骤 3：创建环境并安装依赖

```bash
python3 -m venv <env>
source <env>/bin/activate
pip install -r requirements.txt --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple
```

##### 步骤 4：编辑代码

在云实例中打开 Code Server，并编辑相关代码。

<img src="../../../_assets/docs-cloud/static/yolov8_00.png" alt="YOLOv8 编辑界面" width="800">

##### 步骤 5：运行示例

```bash
python test_yolov8_pose.py
```

运行结果示例：

<img src="../../../_assets/docs-cloud/static/yolov8_01.png" alt="YOLOv8 运行结果" width="800">

#### 9.2.2 YOLOv5-face 人脸检测

YOLOv5-face 是针对人脸检测场景优化的实时检测模型，适用于人脸识别、安防监控、表情分析等场景。

本示例展示在 RISC-V AI 环境中部署并运行人脸检测任务的基础流程。

##### 步骤 1：下载示例代码与模型

```bash
git clone https://gitee.com/bianbu/spacemit-demo.git
cd spacemit-demo/examples/CV/yolov5-face/model
sh download_model.sh
```

##### 步骤 2：创建环境并安装依赖

```
python3 -m venv name(虚拟环境名) 
source name/bin/activate 
pip install -r requirements.txt --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple
```

##### 步骤 3：编辑与运行

在 Code Server 中打开并编辑 `test_yolov5-face.py`。

<img src="../../../_assets/docs-cloud/static/yolov5_00.png" alt="YOLOv5-face 编辑界面" width="800">

运行结果示例：

<img src="../../../_assets/docs-cloud/static/yolov5_01.png" alt="YOLOv5-face 运行结果" width="800">

### 9.3 OCR 识别示例

本示例基于 K1 RISC-V 平台深度优化的 OpenCV OCR 能力进行说明。

#### 步骤 1：下载示例代码

```bash
git clone https://gitee.com/bianbu/spacemit-demo.git
```

#### 步骤 2：下载模型与测试数据

执行模型下载脚本：

```bash
cd spacemit-demo/examples/CV/ocr/model
sh download_model.sh
```

执行测试数据下载脚本：

```bash
cd data
sh download_data.sh
```

#### 步骤 3：创建环境并安装依赖

```
python3 -m venv name(虚拟环境名) 
source name/bin/activate 
pip install -r requirements.txt --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple
```

#### 步骤 4：编辑并运行

在云实例中通过 Code Server 编辑 `test_ocr.py`。

<img src="../../../_assets/docs-cloud/static/ocr00.png" alt="OCR 编辑界面" width="800">

运行完成后，可从日志输出中查看识别结果。

<img src="../../../_assets/docs-cloud/static/ocr01.png" alt="OCR 运行结果" width="800">

### 9.4 OpenHarmony 调试

#### 9.4.1 申请在线实例并远程连接

申请 OpenHarmony 在线实例后，可通过远程桌面开展应用开发与调试工作。

<img src="../../../_assets/docs-cloud/static/oh00.png" alt="OpenHarmony 远程桌面" width="800">

#### 9.4.2 查看系统日志（hilog）

在远程环境中执行以下命令，可实时查看系统日志：

```bash
hilog
```

<img src="../../../_assets/docs-cloud/static/oh01.png" alt="hilog 日志查看" width="800">

#### 9.4.3 应用文件管理

在远程桌面右下角的工具区域，可执行以下文件管理操作：

- 上传
- 安装
- 删除
- 查看

<img src="../../../_assets/docs-cloud/static/oh02.png" alt="OpenHarmony 文件工具区" width="800">

#### 9.4.4 卸载应用

在远程桌面中选中目标应用图标，**鼠标左键长按**，待出现卸载选项后执行卸载操作。

<img src="../../../_assets/docs-cloud/static/oh03.png" alt="OpenHarmony 应用卸载" width="800">

#### 9.4.5 安装应用

点击工具区中的 **安装** 按钮，选择待安装应用包后即可完成安装。

<img src="../../../_assets/docs-cloud/static/oh04.png" alt="OpenHarmony 应用安装" width="400">

#### 9.4.6 查看安装日志

安装过程中，可通过以下命令查看安装相关日志：

```bash
hilog | grep bm
```

若日志中出现 `bm output`，通常表示应用已安装成功。

<img src="../../../_assets/docs-cloud/static/oh05.png" alt="安装日志查看" width="800">

#### 9.4.7 查看应用运行日志

```bash
hilog | grep "xxx"
```

示例：

```bash
hilog | grep "VideoPlay"
```

<img src="../../../_assets/docs-cloud/static/oh06.png" alt="应用运行日志" width="800">

#### 9.4.8 后续扩展方向

- 大模型开发：Ollama 与 MCP 开发能力（待补充）
- GUI 开发：基于 RISC-V 在线环境的 Qt、Electron 开发能力（待补充）
