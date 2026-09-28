---
title: "Cluster Server RV2768 Redfish 接口说明"
lang: zh
category: "硬件/生态硬件/Cluster Server RV2768"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/eco/k3_rv2768/rv2768_redfish.md&lang=zh
source_file: https://cdn-resource.spacemit.com/hardware/eco/docs-product/zh/k3_rv2768/rv2768_redfish.md
updated: "2026-08-04 16:31:50"
---
# Cluster Server RV2768 Redfish 接口说明

## 概述

Cluster Server RV2768 BMC 支持 48 个计算模块，每个模块通过 `sub<X>-<Y>` 格式的 systemName 标识。本文档描述电源控制、风扇控制、进入模块固件升级模式和 CPU 资产信息相关的 Redfish 接口。

## 系统命名规则

两套接口统一使用相同的 systemName 格式：`sub<X>-<Y>`，其中 X 取值范围 0~23，Y 的取值范围 0~1。

| systemName | hostId |
|---|---|
| `system` | 48（全局） |
| `sub0-0` | 0 |
| `sub0-1` | 1 |
| `sub1-0` | 2 |
| `sub1-1` | 3 |
| ... | ... |
| `sub23-0` | 46 |
| `sub23-1` | 47 |

**hostId 计算公式**：`hostId = X * 2 + Y`

## 1. 电源控制接口

### 1.1 执行开关机和复位操作

**POST** `/redfish/v1/Systems/{systemName}/Actions/ComputerSystem.Reset/`

对指定模块执行电源状态转换。

**请求头**

```text
Content-Type: application/json
```

**路径参数**

| 参数 | 类型 | 说明 |
|---|---|---|
| `systemName` | string | 系统名称，格式 `sub<group>-<index>` 或 `system` |

**请求体**

```json
{
    "ResetType": "<reset_type>"
}
```

**ResetType 参数说明**

| ResetType | 说明 | D-Bus 命令 | 操作对象 |
|---|---|---|---|
| `ForceOn` | 强制开机 | `xyz.openbmc_project.State.Host.Transition.On` | Host |
| `ForceOff` | 强制关机 | `xyz.openbmc_project.State.Chassis.Transition.Off` | Chassis |
| `ForceRestart` | 强制重启 | `xyz.openbmc_project.State.Host.Transition.ForceWarmReboot` | Host |
| `PowerCycle` | 电源循环（重启） | `xyz.openbmc_project.State.Host.Transition.Reboot` | Host |

**响应**

成功时返回 HTTP 204 No Content。

**示例：关闭模块 1（sub0-0）**

```bash
curl -k -u root:0penBmc -X POST \
  https://<bmc-ip>/redfish/v1/Systems/sub0-0/Actions/ComputerSystem.Reset/ \
  -H "Content-Type: application/json" \
  -d '{"ResetType": "GracefulShutdown"}'
```

**示例：重启模块 4（sub1-1）**

```bash
curl -k -u root:0penBmc -X POST \
  https://<bmc-ip>/redfish/v1/Systems/sub1-1/Actions/ComputerSystem.Reset/ \
  -H "Content-Type: application/json" \
  -d '{"ResetType": "GracefulRestart"}'
```

**示例：强制关闭全局系统**

```bash
curl -k -u root:0penBmc -X POST \
  https://<bmc-ip>/redfish/v1/Systems/system/Actions/ComputerSystem.Reset/ \
  -H "Content-Type: application/json" \
  -d '{"ResetType": "ForceOff"}'
```

### 1.2 查询支持的 Reset 操作

**GET** `/redfish/v1/Systems/{systemName}/ResetActionInfo/`

返回该系统支持的所有 ResetType 枚举值。

**响应示例**

```json
{
    "@odata.id": "/redfish/v1/Systems/sub0-0/ResetActionInfo",
    "@odata.type": "#ActionInfo.v1_1_2.ActionInfo",
    "Id": "ResetActionInfo",
    "Name": "Reset Action Info",
    "Parameters": [
        {
            "Name": "ResetType",
            "Required": true,
            "DataType": "String",
            "AllowableValues": [
                "On",
                "ForceOff",
                "ForceRestart",
                "GracefulShutdown",
                "GracefulRestart",
                "PowerCycle",
                "Nmi"
            ]
        }
    ]
}
```

### 1.3 查询单个节点状态

**GET** `/redfish/v1/Systems/{systemName}`

**响应示例**

```json
{
    "@odata.id": "/redfish/v1/Systems/sub0-0",
    "@odata.type": "#ComputerSystem.v1_22_0.ComputerSystem",
    "Actions": {
        "#ComputerSystem.Reset": {
            "@Redfish.ActionInfo": "/redfish/v1/Systems/sub0-0/ResetActionInfo",
            "target": "/redfish/v1/Systems/sub0-0/Actions/ComputerSystem.Reset"
        }
    },
    "Description": "K3 Compute Module",
    "Id": "sub0-0",
    "Links": {
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/bmc"
            }
        ]
    },
    "Name": "sub0-0",
    "Oem": {
        "Spacemit": {
            "ACPowerState": "On"
        }
    },
    "PowerState": "On",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "SystemType": "Physical"
}
```

**路径参数**

| 参数 | 类型 | 说明 |
|---|---|---|
| `systemName` | string | 格式 `sub<X>-<Y>`，X,Y（范围 `sub0-0` ~ `sub23-1`） |

**PowerState 状态映射**

| 属性 | 说明 |
|---|---|
| PowerState | 节点的开关机状态 |
| ACPowerState | 节点的上下电状态 |

**测试方法**

```bash
# 查询 host0 状态
curl -k -H "X-Auth-Token: $token" https://${bmc_ip}/redfish/v1/Systems/sub0-0

# 查询 host47 状态
curl -k -H "X-Auth-Token: $token" https://${bmc_ip}/redfish/v1/Systems/sub23-1

# 查询整机状态
curl -k -H "X-Auth-Token: $token" https://${bmc_ip}/redfish/v1/Systems/system

# 查询所有模块状态
for i in {0..23}; do
  for j in {0..1}; do
    curl -k -H "X-Auth-Token: $token" https://${bmc_ip}/redfish/v1/Systems/sub${i}-${j}
  done
done
```

### 1.4 所有模组批量上下电控制

**POST** `/redfish/v1/Chassis/bmc/Actions/Oem/Spacemit/AllNodesPower`

**请求体**

```json
{
  "PowerState": "On"
}
```

**响应示例**

```json
{
    "Message": "All modules power On command sent successfully",
    "PowerState": "On"
}
```

### 1.5 所有模组整体上下电状态查询

**GET** `/redfish/v1/Chassis/bmc/Oem/Spacemit/NodesPowerState`

**响应示例**

```json
{
    "@odata.id": "/redfish/v1/Chassis/bmc/Oem/Spacemit/NodesPowerState",
    "@odata.type": "#OemSpacemit.NodesPowerState",
    "Name": "K3 Nodes Power State",
    "PowerState": "On",
    "RegisterValues": [
        "0x03",
        "0x00",
        "0x00",
        "0x00",
        "0x00",
        "0x00"
    ]
}
```

### 1.6 执行单个模块上下电操作

**POST** `/redfish/v1/Systems/sub0-0/Actions/ComputerSystem.Reset`

**请求体**

单个模块下电操作：

```json
{
    "ResetType": "ForceOff",
    "Oem": {
      "Cluster-BMC": {
        "PowerOffAC": true
      }
    }
}
```

单个模块上电操作：

```json
{
    "ResetType": "ForceOn",
    "Oem": {
      "Cluster-BMC": {
        "PowerOnAC": true
      }
    }
}
```

**响应**

```json
{
    "@Message.ExtendedInfo": [
        {
            "@odata.type": "#Message.v1_1_1.Message",
            "Message": "The request completed successfully.",
            "MessageArgs": [],
            "MessageId": "Base.1.16.0.Success",
            "MessageSeverity": "OK",
            "Resolution": "None"
        }
    ]
}
```

## 2. CPU 资产信息接口

### 2.1 获取处理器列表

**GET** `/redfish/v1/Systems/{systemName}/Processors/`

获取指定模块下的处理器集合。

**路径参数**

| 参数 | 类型 | 说明 |
|---|---|---|
| `systemName` | string | 格式 `sub<X>-<Y>`，X,Y（范围 `sub0-0` ~ `sub23-1`） |

**响应示例**

```json
{
    "@odata.id": "/redfish/v1/Systems/sub0-0/Processors",
    "@odata.type": "#ProcessorCollection.ProcessorCollection",
    "Name": "Processor Collection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/sub0-0/Processors/cpu0"
        }
    ],
    "Members@odata.count": 1
}
```

**示例**

```bash
curl -k -u root:0penBmc \
  https://<bmc-ip>/redfish/v1/Systems/sub0-0/Processors/
```

### 2.2 获取处理器详细信息

**GET** `/redfish/v1/Systems/{systemName}/Processors/{processorId}`

获取指定模块的 CPU 详细资产信息。

**路径参数**

| 参数 | 类型 | 说明 |
|---|---|---|
| `systemName` | string | 格式 `sub<X>-<Y>`（范围 `sub0-0` ~ `sub23-1`） |
| `processorId` | string | 处理器 ID，固定为 `cpu0` |

**响应字段说明**

| 字段 | 类型 | 来源接口 | 说明 |
|---|---|---|---|
| `@odata.id` | string | — | 资源路径 |
| `@odata.type` | string | — | `#Processor.v1_18_0.Processor` |
| `Id` | string | `xyz.openbmc_project.Inventory.Item.Cpu` | 处理器 ID |
| `Name` | string | — | 固定为 `"Processor"` |
| `ProcessorType` | string | — | 固定为 `"CPU"` |
| `Status.State` | string | `xyz.openbmc_project.Inventory.Item.Cpu` | `Enabled` / `Absent` |
| `Status.Health` | string | `xyz.openbmc_project.Inventory.Item.Cpu` | `OK` / `Critical` |
| `TotalCores` | integer | `xyz.openbmc_project.Inventory.Item.Cpu` | 总核心数 |
| `MaxSpeedMHz` | integer | `xyz.openbmc_project.Inventory.Item.Cpu` | 最大频率（MHz） |
| `Model` | string | `xyz.openbmc_project.Inventory.Decorator.Asset` | 型号 |
| `SerialNumber` | string | `xyz.openbmc_project.Inventory.Decorator.Asset` | 序列号 |
| `ProcessorId.EffectiveFamily` | string | `xyz.openbmc_project.Inventory.Item.Cpu` | 有效家族 |
| `ProcessorId.Step` | string | `xyz.openbmc_project.Inventory.Item.Cpu` | 步进 |
| `DiskSizeGB` | integer | `xyz.openbmc_project.Inventory.Item.Cpu` | 根节点所挂载的磁盘大小 |
| `RamSizeMB` | integer | `xyz.openbmc_project.Inventory.Item.Cpu` | RAM 大小 |

**响应示例（CPU 存在）**

```json
{
    "@odata.id": "/redfish/v1/Systems/sub0-0/Processors/cpu0",
    "@odata.type": "#Processor.v1_18_0.Processor",
    "Id": "cpu0",
    "MaxSpeedMHz": 0,
    "Model": "SpacemiT K3 BS01DCMA",
    "Name": "Processor",
    "Oem": {
        "Spacemit": {
            "DiskSizeGB": 0,
            "RamSizeMB": 15969
        }
    },
    "ProcessorId": {
        "EffectiveFamily": "0x0000",
        "Step": "0x0000"
    },
    "ProcessorType": "CPU",
    "SerialNumber": "03021551201A6001",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 16
}
```

**响应示例（CPU 不存在 / 模块离线）**

```json
{
    "@odata.id": "/redfish/v1/Systems/sub1-0/Processors/cpu0",
    "@odata.type": "#Processor.v1_18_0.Processor",
    "Id": "cpu0",
    "MaxSpeedMHz": 0,
    "Name": "Processor",
    "Oem": {
        "Spacemit": {
            "DiskSizeGB": 0,
            "RamSizeMB": 0
        }
    },
    "ProcessorId": {
        "EffectiveFamily": "0x0000",
        "Step": "0x0000"
    },
    "ProcessorType": "CPU",
    "Status": {
        "Health": "Critical",
        "State": "Absent"
    },
    "TotalCores": 0
}
```

**示例：获取模块 0（`sub0-0`）的 CPU 信息**

```bash
curl -k -u root:0penBmc \
  https://<bmc-ip>/redfish/v1/Systems/sub0-0/Processors/cpu0
```

**示例：获取模块 44（`sub22-0`）的 CPU 信息**

```bash
curl -k -u root:0penBmc \
  https://<bmc-ip>/redfish/v1/Systems/sub22-0/Processors/cpu0
```

## 3. 风扇模式控制接口（OEM）

### 3.1 查询当前风扇模式

**GET** `/redfish/v1/Managers/bmc/Oem/Spacemit/FanMode`

**响应示例**

```json
{
    "@odata.type": "#OemSpacemit.FanMode",
    "@odata.id": "/redfish/v1/Managers/bmc/Oem/Spacemit/FanMode",
    "Mode": "Auto"
}
```

**示例**

```bash
curl -k -u root:0penBmc \
  https://<bmc-ip>/redfish/v1/Managers/bmc/Oem/Spacemit/FanMode
```

### 3.2 设置风扇模式

**PATCH** `/redfish/v1/Managers/bmc/Oem/Spacemit/FanMode`

**请求体**

```json
{
    "Mode": "Auto"
}
```

**Mode 参数说明**

| Mode | 说明 | 行为 |
|---|---|---|
| `Auto` | 自动调速 | 设置 `Manual=false`，由 phosphor-pid-control（swampd）自动管理风扇转速 |
| `Manual` | 手动固定转速 | 设置 `Manual=true`，可以通过 redfish 接口设置风扇转速 |

**响应**

成功时返回 HTTP 200 OK。

**示例：切换到手动模式**

```bash
curl -k -u root:0penBmc -X PATCH \
  https://<bmc-ip>/redfish/v1/Managers/bmc/Oem/Spacemit/FanMode \
  -H "Content-Type: application/json" \
  -d '{"Mode": "Manual"}'
```

**示例：切换到自动模式**

```bash
curl -k -u root:0penBmc -X PATCH \
  https://<bmc-ip>/redfish/v1/Managers/bmc/Oem/Spacemit/FanMode \
  -H "Content-Type: application/json" \
  -d '{"Mode": "Auto"}'
```

## 4. 风扇转速控制接口（OEM）

### 4.1 查询当前风扇转速

**GET** `/redfish/v1/Chassis/bmc/Oem/Spacemit/FanSpeeds`

**响应示例**

```json
{
    "@odata.id": "/redfish/v1/Chassis/bmc/Oem/Spacemit/FanSpeeds",
    "@odata.type": "#OemSpacemit.FanSpeeds",
    "FanSpeeds": [
        {
            "FanName": "fan1",
            "Speed": 9098.0
        },
        {
            "FanName": "fan2",
            "Speed": 8745.0
        },
        {
            "FanName": "fan3",
            "Speed": 9098.0
        },
        {
            "FanName": "fan4",
            "Speed": 8732.0
        },
        {
            "FanName": "fan5",
            "Speed": 9112.0
        },
        {
            "FanName": "fan6",
            "Speed": 8719.0
        },
        {
            "FanName": "fan7",
            "Speed": 9140.0
        },
        {
            "FanName": "fan8",
            "Speed": 8732.0
        }
    ],
    "Name": "Fan Speed Control"
}
```

**示例**

```bash
curl -k -u root:0penBmc \
  https://<bmc-ip>/redfish/v1/Chassis/bmc/Oem/Spacemit/FanSpeeds
```

### 4.2 设置风扇转速

**PATCH** `/redfish/v1/Chassis/bmc/Oem/Spacemit/FanSpeeds`

**请求体**

```json
{
  "FanSpeeds": [
    { "FanName": "pwm1", "SpeedPercent": 30.0 },
    { "FanName": "pwm2", "SpeedPercent": 40.0 },
    { "FanName": "pwm3", "SpeedPercent": 50.0 },
    { "FanName": "pwm4", "SpeedPercent": 60.0 }
  ]
}
```

支持一次设置一个或多个风扇，无需包含所有 8 个。

**参数说明**

| 参数 | 类型 | 说明 |
|---|---|---|
| `FanName` | string | 风扇名称，可选值：pwm1 ~ pwm4 |
| `SpeedPercent` | number | 占空比百分比，范围 0–100 |

**响应**

成功时返回 HTTP 200 OK。

**示例：设置 fan1 和 fan2 为 50% 转速**

每个 PWM 通道控制一个双转子风扇，并对应两路转速遥测信号：

- `pwm1`：fan1、fan2
- `pwm2`：fan3、fan4
- `pwm3`：fan5、fan6
- `pwm4`：fan7、fan8

```bash
curl -k -u root:0penBmc -X PATCH \
  https://<bmc-ip>/redfish/v1/Chassis/bmc/Oem/Spacemit/FanSpeeds \
  -H "Content-Type: application/json" \
  -d '{"FanSpeeds": [{"FanName": "pwm1", "SpeedPercent": 50}]}'
```

**示例：同时设置多个风扇**

```bash
curl -k -u root:0penBmc -X PATCH \
  https://<bmc-ip>/redfish/v1/Chassis/bmc/Oem/Spacemit/FanSpeeds \
  -H "Content-Type: application/json" \
  -d '{"FanSpeeds": [{"FanName": "pwm1", "SpeedPercent": 30}, {"FanName": "pwm2", "SpeedPercent": 60}, {"FanName": "pwm3", "SpeedPercent": 100}]}'
```

> **注意**：设置风扇转速前应先通过 FanMode 接口将模式切换为 Manual，否则 Auto 模式下 phosphor-pid-control 会覆盖手动设置的转速值。

## 5. 固件升级模式接口（OEM）

### 5.1 发现支持的模块固件升级接口

**GET** `/redfish/v1/UpdateService/`

在返回的 JSON 中，`Actions.Oem.Spacemit` 字段包含所有 48 个模块的升级 Action。

**响应示例（部分）**

```json
{
    "@odata.type": "#UpdateService.v1_11_1.UpdateService",
    "@odata.id": "/redfish/v1/UpdateService",
    "Actions": {
        "#UpdateService.SimpleUpdate": {
            "target": "/redfish/v1/UpdateService/Actions/UpdateService.SimpleUpdate"
        },
        "Oem": {
            "Spacemit": {
                "#Spacemit.sub0-0.UpdateService.Update": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Spacemit/sub0-0/UpdateService.Update",
                    "@Redfish.ActionInfo": "/redfish/v1/UpdateService/Oem/Spacemit/sub0-0/UpdateActionInfo"
                },
                "#Spacemit.sub0-1.UpdateService.Update": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Spacemit/sub0-1/UpdateService.Update",
                    "@Redfish.ActionInfo": "/redfish/v1/UpdateService/Oem/Spacemit/sub0-1/UpdateActionInfo"
                },
                "#Spacemit.sub23-1.UpdateService.Update": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Spacemit/sub23-1/UpdateService.Update",
                    "@Redfish.ActionInfo": "/redfish/v1/UpdateService/Oem/Spacemit/sub23-1/UpdateActionInfo"
                }
            }
        }
    }
}
```

**示例**

```bash
curl -k -u root:0penBmc \
  https://<bmc-ip>/redfish/v1/UpdateService/
```

### 5.2 执行模块固件升级

**POST** `/redfish/v1/UpdateService/Actions/Oem/Spacemit/<subX-Y>/UpdateService.Update`

对指定的模块执行固件升级操作。

**路径参数**

| 参数 | 类型 | 说明 |
|---|---|---|
| `subX-Y` | string | 模块标识，格式 `sub<X>-<Y>`，其中 X=0-23，Y=0-1 |

**模块编号映射**

| subX-Y | 模块号 | I2C 地址参数 | 位掩码参数 |
|---|---|---|---|
| `sub0-0` | 1 | 0x80 | 0xfe (bit 0 清零) |
| `sub0-1` | 2 | 0x80 | 0xfd (bit 1 清零) |
| `sub1-0` | 3 | 0x80 | 0xfb (bit 2 清零) |
| `sub1-1` | 4 | 0x80 | 0xf7 (bit 3 清零) |
| `sub2-0` | 5 | 0x80 | 0xef (bit 4 清零) |
| `sub2-1` | 6 | 0x80 | 0xdf (bit 5 清零) |
| `sub3-0` | 7 | 0x80 | 0xbf (bit 6 清零) |
| `sub3-1` | 8 | 0x80 | 0x7f (bit 7 清零) |
| `sub4-0` | 9 | 0x81 | 0xfe (bit 0 清零) |
| `sub4-1` | 10 | 0x81 | 0xfd (bit 1 清零) |
| ... | ... | ... | ... |
| `sub23-0` | 47 | 0x85 | 0xfd (bit 1 清零) |
| `sub23-1` | 48 | 0x85 | 0x7f (bit 7 清零) |

**请求体**

无需请求体（POST 方法，但不需要 JSON payload）。

**响应**

成功时返回 HTTP 200 OK，包含操作状态信息。

**响应示例**

```json
{
    "Status": 0,
    "Message": "firmware upgrade initiated for module 1 (sub0-0)"
}
```

`Status` 字段为 D-Bus 方法返回的 `int32_t` 状态码。

**示例：升级模块 1（sub0-0）**

```bash
curl -k -u root:0penBmc -X POST \
  https://<bmc-ip>/redfish/v1/UpdateService/Actions/Oem/Spacemit/sub0-0/UpdateService.Update
```

**示例：升级模块 10（sub4-1）**

```bash
curl -k -u root:0penBmc -X POST \
  https://<bmc-ip>/redfish/v1/UpdateService/Actions/Oem/Spacemit/sub4-1/UpdateService.Update
```

**示例：升级模块 48（sub23-1）**

```bash
curl -k -u root:0penBmc -X POST \
  https://<bmc-ip>/redfish/v1/UpdateService/Actions/Oem/Spacemit/sub23-1/UpdateService.Update
```

**错误响应**

如果提供的 `subX-Y` 格式不正确或超出范围（X > 23 或 Y > 1），将返回 404 错误：

```json
{
    "error": {
        "code": "Base.1.8.1.ResourceNotFound",
        "message": "The requested resource of type UpdateService named sub99-0 was not found."
    }
}
```

## 6. 模组在位信息查询

**GET** `/redfish/v1/Chassis/bmc/Oem/Spacemit/BoardPresence`

**响应**

```json
{
    "@odata.id": "/redfish/v1/Chassis/bmc/Oem/Spacemit/BoardPresence",
    "@odata.type": "#OemSpacemit.BoardPresence",
    "Clusters": [
        { "Id": "sub0", "Present": true },
        { "Id": "sub1", "Present": false },
        { "Id": "sub2", "Present": false },
        { "Id": "sub3", "Present": false },
        { "Id": "sub4", "Present": false },
        { "Id": "sub5", "Present": false },
        { "Id": "sub6", "Present": false },
        { "Id": "sub7", "Present": false },
        { "Id": "sub8", "Present": false },
        { "Id": "sub9", "Present": false },
        { "Id": "sub10", "Present": false },
        { "Id": "sub11", "Present": false },
        { "Id": "sub12", "Present": false },
        { "Id": "sub13", "Present": false },
        { "Id": "sub14", "Present": false },
        { "Id": "sub15", "Present": false },
        { "Id": "sub16", "Present": false },
        { "Id": "sub17", "Present": false },
        { "Id": "sub18", "Present": false },
        { "Id": "sub19", "Present": false },
        { "Id": "sub20", "Present": false },
        { "Id": "sub21", "Present": false },
        { "Id": "sub22", "Present": false },
        { "Id": "sub23", "Present": false }
    ],
    "Name": "K3 Board Presence"
}
```

## 7. 网络协议

### 7.1 查询网络协议

**GET** `/redfish/v1/Managers/bmc/NetworkProtocol`

**响应**

```json
{
    "@odata.id": "/redfish/v1/Managers/bmc/NetworkProtocol",
    "@odata.type": "#ManagerNetworkProtocol.v1_5_0.ManagerNetworkProtocol",
    "Description": "Manager Network Service",
    "FQDN": "k3",
    "HTTP": {
        "Port": null,
        "ProtocolEnabled": false
    },
    "HTTPS": {
        "Certificates": {
            "@odata.id": "/redfish/v1/Managers/bmc/NetworkProtocol/HTTPS/Certificates"
        },
        "Port": 443,
        "ProtocolEnabled": true
    },
    "HostName": "k3",
    "IPMI": {
        "Port": 623,
        "ProtocolEnabled": true
    },
    "Id": "NetworkProtocol",
    "NTP": {
        "NTPServers": [
            "10.0.26.11",
            "10.0.26.12"
        ],
        "ProtocolEnabled": true
    },
    "Name": "Manager Network Protocol",
    "SSH": {
        "Port": 22,
        "ProtocolEnabled": true
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

### 7.2 设置 NTP Server

**PATCH** `/redfish/v1/Managers/bmc/NetworkProtocol`

**请求体**

```json
{
    "NTP": {
        "ProtocolEnabled": true,
        "NTPServers": ["10.0.26.11", "10.0.26.12"]
    }
}
```

**响应**

```
204 No Content
```

## 8. 模块 ID 与 systemName 对照表

两套接口统一，完整对照如下：

| moduleId（模块 Id） | systemName | hostId | 模组 Id |
|---|---|---|---|
| 1 | sub0-0 | 0 | sub0 |
| 2 | sub0-1 | 1 | sub0 |
| 3 | sub1-0 | 2 | sub1 |
| 4 | sub1-1 | 3 | sub1 |
| ... | ... | ... |  |
| 45 | sub22-0 | 44 | sub22 |
| 46 | sub22-1 | 45 | sub22 |
| 47 | sub23-0 | 46 | sub23 |
| 48 | sub23-1 | 47 | sub23 |
| — | system | 48 | — |

## 9. 错误响应

| HTTP 状态码 | 说明 |
|---|---|
| 204 | 操作成功（Reset 接口） |
| 400 | 请求参数错误（如 ResetType 不合法） |
| 404 | 资源不存在（systemName 格式错误或模块不存在） |
| 500 | 内部错误（D-Bus 通信失败） |

**404 响应示例**

```json
{
    "error": {
        "code": "Base.1.8.1.ResourceNotFound",
        "message": "The requested resource of type ComputerSystem named sub99-0 was not found.",
        "@Message.ExtendedInfo": [
            {
                "@odata.type": "#Message.v1_1_1.Message",
                "MessageId": "Base.1.8.1.ResourceNotFound",
                "Message": "The requested resource of type ComputerSystem named sub99-0 was not found.",
                "MessageArgs": ["ComputerSystem", "sub99-0"],
                "Severity": "Critical",
                "Resolution": "Provide a valid resource identifier and resubmit the request."
            }
        ]
    }
}
```