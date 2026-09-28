---
title: "SpacemiT Cloud Platform User Guide"
lang: en
category: "Cloud/User Guide"
source_page: https://www.spacemit.com/community/document/info?nodepath=cloud/userguide/cloud_user_guide.md&lang=en
source_file: https://cdn-resource.spacemit.com/cloud/userguide/docs-cloud/en/cloud_user_guide.md
updated: "2026-05-13 17:47:45"
---
# SpacemiT Cloud Platform User Guide

This document serves as the official user guide for the SpacemiT Cloud Platform. It is intended for new platform users and developers, and provides a systematic introduction to account registration, instance provisioning, remote access, platform applications, local connectivity, API usage, and development examples. This guide helps users efficiently complete environment setup, resource configuration, and application development.

## 1. Document Overview

### 1.1 Scope

This document applies to common usage scenarios of the SpacemiT Cloud Platform, including but not limited to:

- Platform registration and login
- Cloud instance provisioning and management
- Remote access to instances through web-based or local tools
- Use of built-in platform applications and development environments
- Secondary development through instance-exposed APIs

### 1.2 Platform Access URL

Platform URL: [https://gdriscv.com](https://gdriscv.com)

## 2. Registration and Sign-In

### 2.1 Register an Account

After accessing the official platform website, click **Sign Up Now** on the homepage to enter the registration process.

<img src="../../../_assets/docs-cloud/static/register.png" alt="" width="600">

The platform currently supports the following registration methods:

- Mobile phone number registration (currently supports mainland China mobile numbers only)
- Email registration

#### Mobile Phone Registration

<img src="../../../_assets/docs-cloud/static/reg_phone.png" alt="" width="600">

#### Email Registration

<img src="../../../_assets/docs-cloud/static/reg_email.png" alt="" width="600">

### 2.2 Platform Login

After registration is completed, click **Login Now** to enter the login page.

The platform supports the following login methods:

- SMS verification login
- Password login

<img src="../../../_assets/docs-cloud/static/login.png" alt="" width="600">

After successful login, the system enters the main platform interface.

<img src="../../../_assets/docs-cloud/static/main.png" alt="" width="800">

## 3. Instance Provisioning

In the platform main interface, under **My Instances**:

- For users without instances, click **Apply New** to launch the instance creation page.
  <img src="../../../_assets/docs-cloud/static/instancex00.png" alt="" width="800">
s
- For users with existing instances, click **Apply New Instance** to launch the instance creation page.
  <img src="../../../_assets/docs-cloud/static/instancex01.png" alt="" width="800">

The following figure shows the instance creation page.
<img src="../../../_assets/docs-cloud/static/instance.png" alt="" width="800">

### 3.1 Select Instance Type

The platform provides multiple instance creation methods. Users may select an appropriate instance type according to development requirements, workload requirements, and target application scenarios.

#### 3.1.1 Create from Operating System Image

Supported operating system images include:

- Bianbu
- Deepin
- OpenHarmony
- openKylin

<img src="../../../_assets/docs-cloud/static/instance_os.png" alt="" width="800">

#### 3.1.2 Create from Quick Application Template

Supported quick application templates include:

- Tongyi Qwen large language model
- DeepSeek large language model
- JupyterLab online Python development environment

<img src="../../../_assets/docs-cloud/static/instance_app.png" alt="" width="800">

#### 3.1.3 Create from RISC-V Heterogeneous Computing Cluster

This instance type is suitable for development, validation, and computing tasks requiring access to RISC-V heterogeneous computing resources.

<img src="../../../_assets/docs-cloud/static/instance_riscv.png" alt="" width="800">

### 3.2 Configure Instance Name

Enter the instance name and select the relevant agreements before submitting the request.

<img src="../../../_assets/docs-cloud/static/instance2.png" alt="" width="600">

### 3.3 Select Instance Duration

<img src="../../../_assets/docs-cloud/static/instance_time.png" alt="" width="400">

- Non-member users: 48 hours, 7 days, or 1 month
- Member users: Up to 3 months

### 3.4 Create Instance

After configuration is completed, click **Get Start** to create the instance.

<img src="../../../_assets/docs-cloud/static/instance_start.png" alt="" width="600">

## 4. Remote Instance Access

After an instance is successfully created, provisioned instance resources under the current account can be viewed.

<img src="../../../_assets/docs-cloud/static/myinstance.png" alt="" width="600">

Click an instance card to view instance specification and available functions.

<img src="../../../_assets/docs-cloud/static/myinstance2.png" alt="" width="600">

### 4.1 Command-Line Access

Click **Start Remote Access**

<img src="../../../_assets/docs-cloud/static/remote_start.png" alt="" width="400">

The terminal workspace is displayed.

<img src="../../../_assets/docs-cloud/static/instance_remote.png" alt="" width="800">

The command-line interface supports:

- Multi-session management
- Split-screen operation

<img src="../../../_assets/docs-cloud/static/instance_remote2.png" alt="" width="800">

After use, click the **Exit** icon in the upper-right corner to return to the main platform interface.

<img src="../../../_assets/docs-cloud/static/instance_remote3.png" alt="" width="800">

### 4.2 Serial Port Debugging

In the workspace, click the **Serial Debug** button to enter the serial terminal interface.

<img src="../../../_assets/docs-cloud/static/instance_serial.png" alt="" width="800">

### 4.3 File Management and Online Editing

In the upper-left corner of the workspace, click **File** to open the file tree or file tree management.

<img src="../../../_assets/docs-cloud/static/instance_file.png" alt="" width="800">

Right-click a directory or file in the file tree to perform the following operations:

- Refresh
- Delete File
- Create Folder
- Upload File
- Download File

<img src="../../../_assets/docs-cloud/static/instance_file2.png" alt="" width="800">

<img src="../../../_assets/docs-cloud/static/instance_file3.png" alt="" width="800">

Double-click a file (such as `.profile`) to edit it directly in the browser.

<img src="../../../_assets/docs-cloud/static/instance_file4.png" alt="" width="800">

After editing is complete, click the **Save** icon in the upper-right corner to submit the changes.

<img src="../../../_assets/docs-cloud/static/instance_file5.png" alt="" width="800">

### 4.4 Remote Desktop

Click **Remote Desktop** at the top of the workspace to enable or disable graphical remote desktop mode.

> Note: If this button is not clickable, switch back to the Terminal or Serial Debug first.

<img src="../../../_assets/docs-cloud/static/remote_desk00.png" alt="" width="800">

<img src="../../../_assets/docs-cloud/static/remote_desk01.png" alt="" width="800">

Remote desktop supports the following functions:

- Window resizing
- Full-screen display

### 4.5 Instance Restart

Click **Control** in the top bar to perform the following management operations:

- Power reboot
- System reboot

<img src="../../../_assets/docs-cloud/static/instance_reboot.png" alt="" width="800">

### 4.6 Instance Flashing

Click **Flash** in the top bar of the workspace to perform the following operations:

- Open the flashing panel
- Close the flashing panel
- Select a target image from the image list on the right and click the **Flash** icon

<img src="../../../_assets/docs-cloud/static/instance_flash.png" alt="" width="800">

> Flashing operations may affect the current instance environment and data. Back up important data before performing flashing operations.

## 5. Built-In Platform Applications

### 5.1 code-server

In the top toolbar of the workspace, click **Applications → code-server**:

- **Open**: Launch the Code Server online IDE
- **Close**: Stop Code Server

<img src="../../../_assets/docs-cloud/static/code_server.png" alt="" width="800">

#### Install Python Extension

Search for `python` in the extension panel on the left. After the extension is installed, online Python development is available.

<img src="../../../_assets/docs-cloud/static/python00.png" alt="" width="800">

<img src="../../../_assets/docs-cloud/static/python01.png" alt="" width="800">

### 5.2 JupyterLab

In the top toolbar of the workspace, click **Applications → JupyterLab**:

- **Open**: Launch JupyterLab
- **Close**: Exit JupyterLab

**Note:** JupyterLab is available only in instances created from the JupyterLab quick application template. Other operating system images and AI images do not provide this application by default.

<img src="../../../_assets/docs-cloud/static/jupyterlab.png" alt="" width="800">

### 5.3 Tongyi Qwen Large Model Application

In the top toolbar of the workspace, click **Applications → qwen-ai**:

- **Open**: Launch the Qwen application
- **Close**: Exit the Qwen application

<img src="../../../_assets/docs-cloud/static/qwen00.png" alt="" width="800">

The related AI functions can also be accessed quickly through the **AI** icon on the right.

<img src="../../../_assets/docs-cloud/static/ai.png" alt="" width="800">

### 5.4 Deepseek Large Model Application

In the top toolbar of the workspace, click **Applications → deepseek-ai**:

- **Open**: Launch the DeepSeek application
- **Close**: Exit the DeepSeek application

<img src="../../../_assets/docs-cloud/static/deepseek.png" alt="" width="800">

Quick access through the **AI** icon on the right side is also supported.

## 6. Account Management

### 6.1 Modify Personal Information

Click the user icon in the upper-right corner of the system page to enter the account management center.

<img src="../../../_assets/docs-cloud/static/user00.png" alt="" width="800">

On the account settings page, click **Edit Profile**.

<img src="../../../_assets/docs-cloud/static/user01.png" alt="" width="800">

The following account information is currently supported:

- Username
- Password
- Mobile phone number
- Email address

<img src="../../../_assets/docs-cloud/static/user02.png" alt="" width="500">

The following example shows the mobile phone number modification page:

<img src="../../../_assets/docs-cloud/static/user03.png" alt="" width="500">

After saving, click Return to System to return to the account management interface.

### 6.2 Message Center

In the account management interface, click the **Message Center** tab on the left to view platform notifications centrally.

<img src="../../../_assets/docs-cloud/static/info.png" alt="" width="800">

### 6.3 Instance Sharing

In the account management interface, click the **Instance Sharing** tab on the left to share personal instance resources with other users.

<img src="../../../_assets/docs-cloud/static/instance_share.png" alt="" width="800">

### 6.4 API Key Management

In the account management interface, click the **API Key** tab on the left to manage API keys.

API keys are primarily used to access APIs exposed by instances remotely.

<img src="../../../_assets/docs-cloud/static/apikey.png" alt="" width="800">

### 6.5 Alert Information

In the account management interface, click the **Instance Warning** tab on the left to view instance-related alert status information.

<img src="../../../_assets/docs-cloud/static/notices.png" alt="" width="800">

## 7. Local Instance Connection

### 7.1 Direct SSH Connection

The platform supports direct connection to instances through a local SSH client. Before establishing a direct SSH connection, TLS tunneling must be enabled. Stunnel is recommended.

#### 7.1.1 Install Stunnel Client

- Windows: [https://www.stunnel.org/downloads/stunnel-latest-win64-installer.exe](https://www.stunnel.org/downloads/stunnel-latest-win64-installer.exe)
- Ubuntu/Debian:

  ```bash
  sudo apt install stunnel4
  ```

- CentOS/RHEL:

  ```bash
  sudo yum install stunnel
  ```

#### 7.1.2 Obtain Stunnel Configuration

In the console, click the target instance card.

<img src="../../../_assets/docs-cloud/static/instance00.png" alt="" width="800">

Click **Local Connection** to open the page containing connection information and operating instructions.

<img src="../../../_assets/docs-cloud/static/local_connect.png" alt="" width="600">

Copy the configuration information shown on the page into the Stunnel client configuration file, then start or reload the Stunnel service.

<img src="../../../_assets/docs-cloud/static/config.png" alt="" width="600">

On Linux systems, the generated Stunnel configuration file can be used directly to start the service.

<img src="../../../_assets/docs-cloud/static/linux_stunnel.png" alt="" width="800">

#### 7.1.3 Connect Through the Command Line

Example command:

```bash
ssh -p 2222 root@localhost
```

<img src="../../../_assets/docs-cloud/static/cmd.png" alt="" width="600">

#### 7.1.4 Connect Through MobaXterm

<img src="../../../_assets/docs-cloud/static/moba00.png" alt="" width="800">

When using MobaXterm, the SSH protocol version must be explicitly specified as **SSHv2**.

Procedure:

1. Select the **Advanced SSH settings** tab.
2. Click **Expert SSH settings**.
3. Set **SSH protocol version** to **SSHv2**.
4. Click **OK** to complete the connection.

<img src="../../../_assets/docs-cloud/static/sshv2.png" alt="" width="600">

#### 7.1.5 Obtain User Password

<img src="../../../_assets/docs-cloud/static/password00.png" alt="" width="800">

The user password can be found at the bottom of the **Connection Information** page.

<img src="../../../_assets/docs-cloud/static/password01.png" alt="" width="600">

### 7.2 Direct VNC Connection

Direct VNC connection is similar to direct SSH connection. Before the connection is established, the Stunnel configuration must also be completed first.

Using MobaXterm as an example:

1. Complete the Stunnel configuration.
2. Click **Session** on the left.
3. Select **VNC**.
4. Enter `localhost` for the address.
5. Enter `5901` for the port.
6. Click **OK** to establish the connection.

If a password is required, refer to **User Password** section in the previous section.

<img src="../../../_assets/docs-cloud/static/vnc.png" alt="" width="800">

Example interface after successful connection:

![](../../../_assets/docs-cloud/static/remote_connected.png)

## 8. API Calls

### 8.1 Ollama API Calls

Currently, only the following instance types are supported:

- Tongyi Qwen large model instances
- DeepSeek large model instances

After entering the instance workspace, refer to [4.1 Command-Line Access](cloud_user_guide.md#41-command-line-access), then click the **API Calling** button on the right to access the configuration page.

<img src="../../../_assets/docs-cloud/static/api00.png" alt="" width="800">

<img src="../../../_assets/docs-cloud/static/api01.png" alt="" width="800">

After configuring the request headers, the Ollama API can be invoked using the URL provided on the page.

<img src="../../../_assets/docs-cloud/static/api02.png" alt="" width="800">

<img src="../../../_assets/docs-cloud/static/api03.png" alt="" width="800">

### 8.2 Custom API Calls

Instances support deployment and external access for custom services through port `18080`.

For example, a Python HTTP service can be run inside the instance:

<img src="../../../_assets/docs-cloud/static/python_http.png" alt="" width="600">

GET or POST requests can then be sent using Postman, where `DeviceID` is the instance device ID.

<img src="../../../_assets/docs-cloud/static/postman.png" alt="" width="800">

For API keys, refer to [6.4 API Key Management](cloud_user_guide.md#64-api-key-management).

<img src="../../../_assets/docs-cloud/static/apikey.png" alt="" width="800">

The request URL format is as follows:

```text
https://gdriscv.com/api/remote/{deviceId}
```

<img src="../../../_assets/docs-cloud/static/address00.png" alt="" width="800">

<img src="../../../_assets/docs-cloud/static/address01.png" alt="" width="800">

## 9. Development Examples

This chapter provides representative development examples to help users quickly understand the platform capabilities and development workflow for RISC-V and AI applications.

### 9.1 RISC-V Assembly and Vector Development

#### 9.1.1 RVV Programming

RVV (RISC-V Vector) is designed for high-performance vector computing scenarios. Compared with ARM NEON / SVE, RVV provides greater flexibility in vector-length configuration and hardware adaptability.

The following table provides a brief comparison between RVV and ARM SVE:

| Feature | SVE (ARM) | RVV (RISC-V) |
| --- | --- | --- |
| Instruction set architecture | ARM v8/v9 extension | Official RISC-V vector extension (V extension) |
| Design philosophy | Prioritizes hardware transparency and code compatibility | Prioritizes flexibility and configurability, allowing hardware customization |
| Register structure | Independent predicate registers (P0-P15) + Z registers | Vector registers can also be used as mask registers, configurable vector registers |
| Minimum implementation requirement | Must support 128-bit vectors | No fixed minimum length, scalable from 128 bits |
| Programming model | Emphasizes compiler-driven optimization | Better suited to manual optimization based on hardware characteristics |
| Data type support | Supports FP32/FP64, INT8/16/32/64, etc. | Supports FP16/32/64, INT8/16/32/64, etc. |
| Memory Access Pattern | Supports complex addressing | Emphasizes explicit memory operations |
| Application scenarios | High-performance computing in the ARM ecosystem (servers, supercomputers) | Customized RISC-V scenarios (AIoT, edge computing) |

Core code example:

```c
void vector_add_rvv(int32_t* vec1, int32_t* vec2, int32_t* result, size_t size) {
    // Set vector length
    size_t v1;

    for (size_t i = 0; i < size; i += v1) {
        // Set the vector length dynamically. If __riscv_vsetvlmax_e32m4() > size - i,
        // the length is set to size - i; otherwise, it is set to __riscv_vsetvlmax_e32m4().
        v1 = __riscv_vsetvl_e32m4(size - i);

        vint32m4_t v1 = __riscv_vle32_v_i32m4(&vec1[i], v1);  // Load vec1
        vint32m4_t v2 = __riscv_vle32_v_i32m4(&vec2[i], v1);  // Load vec2
        vint32m4_t vresult = __riscv_vadd_vv_i32m4(v1, v2, v1);  // Vector addition
        __riscv_vse32_v_i32m4(&result[i], vresult, v1);  // Store result
    }
}
```

Inside the cloud instance, code can be edited through Code Server and compiled and validated by using `gcc`.

<img src="../../../_assets/docs-cloud/static/rvv00.png" alt="" width="800">

<img src="../../../_assets/docs-cloud/static/rvv01.png" alt="" width="600">

#### 9.1.2 RISC-V AI Instruction Programming

K1 is an 8-core RISC-V AI CPU. Based on the open-source RISC-V instruction set, K1 adds general-purpose AI computing capability and can provide approximately 50 KDMIPS of CPU compute power and 2.0 TOPS of AI compute power.

The chip supports the RISC-V Vector 1.0 standard and provides 256-bit vector compute bandwidth, enabling strong SIMD parallel processing capability for high-performance AI computing.

<img src="../../../_assets/docs-cloud/static/ai-cpu.png" alt="" width="800">

Core example code:

<img src="../../../_assets/docs-cloud/static/demo00.png" alt="" width="800">

Example of editing and compiling through Code Server:

<img src="../../../_assets/docs-cloud/static/demo01.png" alt="" width="800">

Execution result:

<img src="../../../_assets/docs-cloud/static/demo03.png" alt="" width="500">

#### 9.1.3 Convolution Optimization Example

Convolutional neural networks (CNNs) are widely used in image classification, object detection, and image segmentation tasks. Through local perception and parameter sharing, convolution operations effectively reduce model parameter size and improve inference efficiency.

The following is a 1×3 convolution optimization example:

<img src="../../../_assets/docs-cloud/static/cnn00.png" alt="" width="800">

The editing interface in the cloud instance is shown below:

<img src="../../../_assets/docs-cloud/static/cnn01.png" alt="" width="800">

Execution result:

<img src="../../../_assets/docs-cloud/static/cnn02.png" alt="" width="500">

### 9.2 AI Development Examples

#### 9.2.1 YOLOv8 Pose Estimation

YOLOv8-pose is a human pose estimation model based on YOLOv8. It detects human targets and outputs keypoint locations, making it suitable for action recognition, motion analysis, and human-computer interaction scenarios.

This example demonstrates the basic workflow for pose estimation development in a RISC-V AI computing environment.

##### Step 1: Download the Code

```bash
git clone https://gitee.com/bianbu/spacemit-demo.git
```

##### Step 2: Download the Model

```bash
cd spacemit-demo/examples/CV/yolov8-pose/model
sh download_model.sh
```

After the model download is complete, the following files are available:

- FP32 model: `yolov8n-pose.onnx`
- INT8 model: `yolov8n-pose.q.onnx`

##### Step 3: Create an Environment and Install Dependencies

```bash
python3 -m venv <env>
source <env>/bin/activate
pip install -r requirements.txt --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple
```

##### Step 4: Edit the Code

Open Code Server in the cloud instance and edit the relevant code.

<img src="../../../_assets/docs-cloud/static/yolov8_00.png" alt="" width="800">

##### Step 5: Run the Example

```bash
python test_yolov8_pose.py
```

Example execution result:

<img src="../../../_assets/docs-cloud/static/yolov8_01.png" alt="" width="800">

#### 9.2.2 YOLOv5-face Face Detection

YOLOv5-face is a real-time detection model optimized for face detection scenarios. It is suitable for use cases such as face recognition, security monitoring, and expression analysis.

This example demonstrates the basic workflow for deploying and running a face detection task in a RISC-V AI environment.

##### Step 1: Download the Example Code and Model

```bash
git clone https://gitee.com/bianbu/spacemit-demo.git
cd spacemit-demo/examples/CV/yolov5-face/model
sh download_model.sh
```

##### Step 2: Create an Environment and Install Dependencies

```
python3 -m venv name(virtual environment name) 
source name/bin/activate 
pip install -r requirements.txt --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple
```

##### Step 3: Edit and Run

Open and edit `test_yolov5-face.py` in Code Server.

<img src="../../../_assets/docs-cloud/static/yolov5_00.png" alt="" width="800">

Example execution result:

<img src="../../../_assets/docs-cloud/static/yolov5_01.png" alt="" width="800">

### 9.3 OCR Recognition Example

This example describes OCR capability based on OpenCV, deeply optimized for the K1 RISC-V platform.

#### Step 1: Download the Example Code

```bash
git clone https://gitee.com/bianbu/spacemit-demo.git
```

#### Step 2: Download the Model and Test Data

Run the model download script:

```bash
cd spacemit-demo/examples/CV/ocr/model
sh download_model.sh
```

Run the test data download script:

```bash
cd data
sh download_data.sh
```

#### Step 3: Create an Environment and Install Dependencies

```
python3 -m venv name(virtual environment name) 
source name/bin/activate 
pip install -r requirements.txt --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple
```

#### Step 4: Edit and Run

Edit `test_ocr.py` through Code Server in the cloud instance.

<img src="../../../_assets/docs-cloud/static/ocr00.png" alt="" width="800">

After execution is complete, the recognition results can be viewed in the log output.

<img src="../../../_assets/docs-cloud/static/ocr01.png" alt="" width="800">

### 9.4 OpenHarmony Debugging

#### 9.4.1 Apply for an Online Instance and Connect Remotely

After applying for an OpenHarmony online instance, application development and debugging can be performed through the remote desktop.

<img src="../../../_assets/docs-cloud/static/oh00.png" alt="" width="800">

#### 9.4.2 View System Logs (hilog)

Run the following command in the remote environment to view system logs in real time:

```bash
hilog
```

<img src="../../../_assets/docs-cloud/static/oh01.png" alt="" width="800">

#### 9.4.3 Application File Management

The tool area in the lower-right corner of the remote desktop supports the following file management operations:

- Upload
- Install
- Delete
- View

<img src="../../../_assets/docs-cloud/static/oh02.png" alt="" width="800">

#### 9.4.4 Uninstall an Application

In the remote desktop, select the target application icon and **press and hold the left mouse button** until the uninstall option appears, then perform the uninstall operation.

<img src="../../../_assets/docs-cloud/static/oh03.png" alt="l" width="800">

#### 9.4.5 Install an Application

Click the **Install** button in the tool area, then select the application package to complete the installation.

<img src="../../../_assets/docs-cloud/static/oh04.png" alt="" width="400">

#### 9.4.6 View Installation Logs

During installation, the following command can be used to view installation-related logs:

```bash
hilog | grep bm
```

If `bm output` appears in the log, the application is generally considered to have been installed successfully.

<img src="../../../_assets/docs-cloud/static/oh05.png" alt="" width="800">

#### 9.4.7 View Application Runtime Logs

```bash
hilog | grep "xxx"
```

Example:

```bash
hilog | grep "VideoPlay"
```

<img src="../../../_assets/docs-cloud/static/oh06.png" alt="" width="800">

#### 9.4.8 Future Expansion Directions

- Large model development: Ollama and MCP development capability (to be added)
- GUI development: Qt and Electron development capability based on the RISC-V online environment (to be added)
