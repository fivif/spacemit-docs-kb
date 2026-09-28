---
title: "Cluster Server RV2768 Redfish API Reference"
lang: en
category: "Hardware/Ecosystem Hardware/Cluster Server RV2768"
source_page: https://www.spacemit.com/community/document/info?nodepath=hardware/eco/k3_rv2768/rv2768_redfish.md&lang=en
source_file: https://cdn-resource.spacemit.com/hardware/eco/docs-product/en/k3_rv2768/rv2768_redfish.md
updated: "2026-08-04 16:29:03"
---
# Cluster Server RV2768 Redfish API Reference

## Overview

The Cluster Server RV2768 BMC manages up to 48 compute modules. Each compute module is identified by a system identifier (`systemName`) in the `sub<X>-<Y>` format. This document describes Redfish APIs for module power management, fan control, firmware updates, processor inventory.

## System Naming Conventions

Both API sets use the same systemName format: `sub<X>-<Y>`, where X ranges from 0 to 23 and Y ranges from 0 to 1.

| systemName | hostId |
|---|---|
| `system` | 48 (Global) |
| `sub0-0` | 0 |
| `sub0-1` | 1 |
| `sub1-0` | 2 |
| `sub1-1` | 3 |
| ... | ... |
| `sub23-0` | 46 |
| `sub23-1` | 47 |

**hostId Formula**: `hostId = X * 2 + Y`

## 1. Power Control APIs

### 1.1 Power and Reset Operations

**POST** `/redfish/v1/Systems/{systemName}/Actions/ComputerSystem.Reset/`

Performs a power-state transition on the specified compute module.

**Request Headers**

```text
Content-Type: application/json
```

**Path Parameters**

| Parameter | Type | Description |
|---|---|---|
| `systemName` | string | System name in the format `sub<group>-<index>` or `system` |

**Request Body**

```json
{
    "ResetType": "<reset_type>"
}
```

**ResetType Parameter Descriptions**

| ResetType | Description | D-Bus Command | Target |
|---|---|---|---|
| `ForceOn` | Force power-on | `xyz.openbmc_project.State.Host.Transition.On` | Host |
| `ForceOff` | Force power-off | `xyz.openbmc_project.State.Chassis.Transition.Off` | Chassis |
| `ForceRestart` | Force restart | `xyz.openbmc_project.State.Host.Transition.ForceWarmReboot` | Host |
| `PowerCycle` | Power cycle (restart) | `xyz.openbmc_project.State.Host.Transition.Reboot` | Host |

**Response**

Returns HTTP 204 No Content on success.

**Example: Power off module 1 (sub0-0)**

```bash
curl -k -u root:0penBmc -X POST \
  https://<bmc-ip>/redfish/v1/Systems/sub0-0/Actions/ComputerSystem.Reset/ \
  -H "Content-Type: application/json" \
  -d '{"ResetType": "GracefulShutdown"}'
```

**Example: Restart module 4 (sub1-1)**

```bash
curl -k -u root:0penBmc -X POST \
  https://<bmc-ip>/redfish/v1/Systems/sub1-1/Actions/ComputerSystem.Reset/ \
  -H "Content-Type: application/json" \
  -d '{"ResetType": "GracefulRestart"}'
```

**Example: Force power-off of the global system**

```bash
curl -k -u root:0penBmc -X POST \
  https://<bmc-ip>/redfish/v1/Systems/system/Actions/ComputerSystem.Reset/ \
  -H "Content-Type: application/json" \
  -d '{"ResetType": "ForceOff"}'
```

### 1.2 Query Supported Reset Operations

**GET** `/redfish/v1/Systems/{systemName}/ResetActionInfo/`

Returns all ResetType enumeration values supported by the system.

**Response Example**

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

### 1.3 Query the Status of a Single Node

**GET** `/redfish/v1/Systems/{systemName}`

**Response Example**

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

**Path Parameters**

| Parameter | Type | Description |
|---|---|---|
| `systemName` | string | Format `sub<X>-<Y>`, with values from `sub0-0` to `sub23-1` |

**PowerState Mapping**

| Property | Description |
|---|---|
| PowerState | Node power state |
| ACPowerState | Node AC power state |

**Test Commands**

```bash
# Query host0 status
curl -k -H "X-Auth-Token: $token" https://${bmc_ip}/redfish/v1/Systems/sub0-0

# Query host47 status
curl -k -H "X-Auth-Token: $token" https://${bmc_ip}/redfish/v1/Systems/sub23-1

# Query overall system status
curl -k -H "X-Auth-Token: $token" https://${bmc_ip}/redfish/v1/Systems/system

# Query the status of all modules
for i in {0..23}; do
  for j in {0..1}; do
    curl -k -H "X-Auth-Token: $token" https://${bmc_ip}/redfish/v1/Systems/sub${i}-${j}
  done
done
```

### 1.4 Batch Power Control for All Modules

**POST** `/redfish/v1/Chassis/bmc/Actions/Oem/Spacemit/AllNodesPower`

**Request Body**

```json
{
  "PowerState": "On"
}
```

**Response Example**

```json
{
    "Message": "All modules power On command sent successfully",
    "PowerState": "On"
}
```

### 1.5 Query the Overall Power State of All Modules

**GET** `/redfish/v1/Chassis/bmc/Oem/Spacemit/NodesPowerState`

**Response Example**

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

### 1.6 Power a Single Module On or Off

**POST** `/redfish/v1/Systems/sub0-0/Actions/ComputerSystem.Reset`

**Request Body**

Power-off operation for a single module:

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

Power-on operation for a single module:

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

**Response**

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

## 2. CPU Asset Information APIs

### 2.1 Get the Processor List

**GET** `/redfish/v1/Systems/{systemName}/Processors/`

Gets the processor collection for the specified module.

**Path Parameters**

| Parameter | Type | Description |
|---|---|---|
| `systemName` | string | Format `sub<X>-<Y>`, with values from `sub0-0` to `sub23-1` |

**Response Example**

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

**Example**

```bash
curl -k -u root:0penBmc \
  https://<bmc-ip>/redfish/v1/Systems/sub0-0/Processors/
```

### 2.2 Get Detailed Processor Information

**GET** `/redfish/v1/Systems/{systemName}/Processors/{processorId}`

Gets detailed processor inventory information for the specified compute module.

**Path Parameters**

| Parameter | Type | Description |
|---|---|---|
| `systemName` | string | Format `sub<X>-<Y>` (range `sub0-0` to `sub23-1`) |
| `processorId` | string | Processor ID, fixed at `cpu0` |

**Response Field Descriptions**

| Field | Type | Source Interface | Description |
|---|---|---|---|
| `@odata.id` | string | — | Resource path |
| `@odata.type` | string | — | `#Processor.v1_18_0.Processor` |
| `Id` | string | `xyz.openbmc_project.Inventory.Item.Cpu` | Processor ID |
| `Name` | string | — | Fixed as `"Processor"` |
| `ProcessorType` | string | — | Fixed as `"CPU"` |
| `Status.State` | string | `xyz.openbmc_project.Inventory.Item.Cpu` | `Enabled` / `Absent` |
| `Status.Health` | string | `xyz.openbmc_project.Inventory.Item.Cpu` | `OK` / `Critical` |
| `TotalCores` | integer | `xyz.openbmc_project.Inventory.Item.Cpu` | Total core count |
| `MaxSpeedMHz` | integer | `xyz.openbmc_project.Inventory.Item.Cpu` | Maximum frequency (MHz) |
| `Model` | string | `xyz.openbmc_project.Inventory.Decorator.Asset` | Model |
| `SerialNumber` | string | `xyz.openbmc_project.Inventory.Decorator.Asset` | Serial number |
| `ProcessorId.EffectiveFamily` | string | `xyz.openbmc_project.Inventory.Item.Cpu` | Effective family |
| `ProcessorId.Step` | string | `xyz.openbmc_project.Inventory.Item.Cpu` | Stepping |
| `DiskSizeGB` | integer | `xyz.openbmc_project.Inventory.Item.Cpu` | Disk size mounted on the root node |
| `RamSizeMB` | integer | `xyz.openbmc_project.Inventory.Item.Cpu` | RAM size |

**Response Example (CPU Present)**

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

**Response Example (CPU Absent / Module Offline)**

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

**Example: Get CPU information for module 0 (`sub0-0`)**

```bash
curl -k -u root:0penBmc \
  https://<bmc-ip>/redfish/v1/Systems/sub0-0/Processors/cpu0
```

**Example: Get CPU information for module 44 (`sub22-0`)**

```bash
curl -k -u root:0penBmc \
  https://<bmc-ip>/redfish/v1/Systems/sub22-0/Processors/cpu0
```

## 3. Fan Mode Control APIs (OEM)

### 3.1 Query the Current Fan Mode

**GET** `/redfish/v1/Managers/bmc/Oem/Spacemit/FanMode`

**Response Example**

```json
{
    "@odata.type": "#OemSpacemit.FanMode",
    "@odata.id": "/redfish/v1/Managers/bmc/Oem/Spacemit/FanMode",
    "Mode": "Auto"
}
```

**Example**

```bash
curl -k -u root:0penBmc \
  https://<bmc-ip>/redfish/v1/Managers/bmc/Oem/Spacemit/FanMode
```

### 3.2 Set the Fan Mode

**PATCH** `/redfish/v1/Managers/bmc/Oem/Spacemit/FanMode`

**Request Body**

```json
{
    "Mode": "Auto"
}
```

**Mode Parameter Descriptions**

| Mode | Description | Behavior |
|---|---|---|
| `Auto` | Automatic speed control | Sets `Manual=false`; phosphor-pid-control (swampd) manages fan speed automatically |
| `Manual` | Fixed manual speed | Sets `Manual=true`; fan speed can be set through the Redfish API |

**Response**

Returns HTTP 200 OK on success.

**Example: Switch to manual mode**

```bash
curl -k -u root:0penBmc -X PATCH \
  https://<bmc-ip>/redfish/v1/Managers/bmc/Oem/Spacemit/FanMode \
  -H "Content-Type: application/json" \
  -d '{"Mode": "Manual"}'
```

**Example: Switch to automatic mode**

```bash
curl -k -u root:0penBmc -X PATCH \
  https://<bmc-ip>/redfish/v1/Managers/bmc/Oem/Spacemit/FanMode \
  -H "Content-Type: application/json" \
  -d '{"Mode": "Auto"}'
```

## 4. Fan Speed Control APIs (OEM)

### 4.1 Query the Current Fan Speed

**GET** `/redfish/v1/Chassis/bmc/Oem/Spacemit/FanSpeeds`

**Response Example**

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

**Example**

```bash
curl -k -u root:0penBmc \
  https://<bmc-ip>/redfish/v1/Chassis/bmc/Oem/Spacemit/FanSpeeds
```

### 4.2 Set the Fan Speed

**PATCH** `/redfish/v1/Chassis/bmc/Oem/Spacemit/FanSpeeds`

**Request Body**

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

Multiple fans can be set in a single request. There is no need to include all fans; only the specified fans will be configured.

**Parameter Descriptions**

| Parameter | Type | Description |
|---|---|---|
| `FanName` | string | Fan name; allowable values: pwm1 to pwm4 |
| `SpeedPercent` | number | Duty-cycle percentage, range 0–100 |

**Response**

Returns HTTP 200 OK on success.

**Example: Set fan1 and fan2 to 50% speed**

Each PWM channel controls one dual-rotor fan and corresponds to two speed telemetry signals:

- `pwm1`: fan1, fan2
- `pwm2`: fan3, fan4
- `pwm3`: fan5, fan6
- `pwm4`: fan7, fan8

```bash
curl -k -u root:0penBmc -X PATCH \
  https://<bmc-ip>/redfish/v1/Chassis/bmc/Oem/Spacemit/FanSpeeds \
  -H "Content-Type: application/json" \
  -d '{"FanSpeeds": [{"FanName": "pwm1", "SpeedPercent": 50}]}'
```

**Example: Set multiple fans simultaneously**

```bash
curl -k -u root:0penBmc -X PATCH \
  https://<bmc-ip>/redfish/v1/Chassis/bmc/Oem/Spacemit/FanSpeeds \
  -H "Content-Type: application/json" \
  -d '{"FanSpeeds": [{"FanName": "pwm1", "SpeedPercent": 30}, {"FanName": "pwm2", "SpeedPercent": 60}, {"FanName": "pwm3", "SpeedPercent": 100}]}'
```

> **Note**: Before setting fan speed, switch the mode to Manual through the FanMode API. Otherwise, phosphor-pid-control overrides manually set speed values in Auto mode.

## 5. Firmware Update Mode APIs (OEM)

### 5.1 Discover Supported Module Firmware Update APIs

**GET** `/redfish/v1/UpdateService/`

In the returned JSON, the `Actions.Oem.Spacemit` field contains the update action for all 48 modules.

**Response Example (Partial)**

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

**Example**

```bash
curl -k -u root:0penBmc \
  https://<bmc-ip>/redfish/v1/UpdateService/
```

### 5.2 Perform a Module Firmware Update

**POST** `/redfish/v1/UpdateService/Actions/Oem/Spacemit/<subX-Y>/UpdateService.Update`

Performs a firmware update on the specified module.

**Path Parameters**

| Parameter | Type | Description |
|---|---|---|
| `subX-Y` | string | Module identifier in the format `sub<X>-<Y>`, where X=0-23 and Y=0-1 |

**Module Number Mapping**

| subX-Y | Module Number | I2C Address Parameter | Bitmask Parameter |
|---|---|---|---|
| `sub0-0` | 1 | 0x80 | 0xfe (bit 0 cleared) |
| `sub0-1` | 2 | 0x80 | 0xfd (bit 1 cleared) |
| `sub1-0` | 3 | 0x80 | 0xfb (bit 2 cleared) |
| `sub1-1` | 4 | 0x80 | 0xf7 (bit 3 cleared) |
| `sub2-0` | 5 | 0x80 | 0xef (bit 4 cleared) |
| `sub2-1` | 6 | 0x80 | 0xdf (bit 5 cleared) |
| `sub3-0` | 7 | 0x80 | 0xbf (bit 6 cleared) |
| `sub3-1` | 8 | 0x80 | 0x7f (bit 7 cleared) |
| `sub4-0` | 9 | 0x81 | 0xfe (bit 0 cleared) |
| `sub4-1` | 10 | 0x81 | 0xfd (bit 1 cleared) |
| ... | ... | ... | ... |
| `sub23-0` | 47 | 0x85 | 0xfd (bit 1 cleared) |
| `sub23-1` | 48 | 0x85 | 0x7f (bit 7 cleared) |

**Request Body**

No request body is required (the method is POST, but no JSON payload is needed).

**Response**

Returns HTTP 200 OK with operation status information on success.

**Response Example**

```json
{
    "Status": 0,
    "Message": "firmware upgrade initiated for module 1 (sub0-0)"
}
```

The `Status` field is the `int32_t` status code returned by the D-Bus method.

**Example: Perform a firmware update on module 1 (sub0-0)**

```bash
curl -k -u root:0penBmc -X POST \
  https://<bmc-ip>/redfish/v1/UpdateService/Actions/Oem/Spacemit/sub0-0/UpdateService.Update
```

**Example: Perform a firmware update on module 10 (sub4-1)**

```bash
curl -k -u root:0penBmc -X POST \
  https://<bmc-ip>/redfish/v1/UpdateService/Actions/Oem/Spacemit/sub4-1/UpdateService.Update
```

**Example: Perform a firmware update on module 48 (sub23-1)**

```bash
curl -k -u root:0penBmc -X POST \
  https://<bmc-ip>/redfish/v1/UpdateService/Actions/Oem/Spacemit/sub23-1/UpdateService.Update
```

**Error Response**

If the provided `subX-Y` format is invalid or out of range (X > 23 or Y > 1), a 404 error is returned:

```json
{
    "error": {
        "code": "Base.1.8.1.ResourceNotFound",
        "message": "The requested resource of type UpdateService named sub99-0 was not found."
    }
}
```

## 6. Query Module Presence

**GET** `/redfish/v1/Chassis/bmc/Oem/Spacemit/BoardPresence`

**Response**

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

## 7. Network Protocol

### 7.1 Query the Network Protocol

**GET** `/redfish/v1/Managers/bmc/NetworkProtocol`

**Response**

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

### 7.2 Configure the NTP Server

**PATCH** `/redfish/v1/Managers/bmc/NetworkProtocol`

**Request Body**

```json
{
    "NTP": {
        "ProtocolEnabled": true,
        "NTPServers": ["10.0.26.11", "10.0.26.12"]
    }
}
```

**Response**

```
204 No Content
```

## 8. Module ID and systemName Mapping

The two API sets use a unified mapping, as shown below:

| moduleId | systemName | hostId | Cluster ID |
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

## 9. Error Responses

| HTTP Status Code | Description |
|---|---|
| 204 | Operation successful (Reset API) |
| 400 | Invalid request parameters (for example, an invalid ResetType) |
| 404 | Resource not found (invalid systemName format or nonexistent module) |
| 500 | Internal error (D-Bus communication failure) |

**404 Response Example**

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