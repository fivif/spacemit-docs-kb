---
title: "SpacemiT AI 助手"
lang: zh
category: "工具/SpacemiT Studio/用户指南"
source_page: https://www.spacemit.com/community/document/info?nodepath=tools/studio/user_guide/ai.md&lang=zh
source_file: https://cdn-resource.spacemit.com/tools/docs-tool/zh/studio/user_guide/ai.md
updated: "2026-08-24 09:53:22"
---
# SpacemiT AI 助手

> 注：持续开发中...


## 概述

**SpacemiT AI 助手**是集成于 SpacemiT Studio 中的对话式 AI 开发助手，基于进迭时空文档与预置技能库，支持代码辅助、问题排查与端侧 AI 应用开发。

![](https://cdn-resource.spacemit.com/tools/docs-tool/zh/studio/static/ai.png)

> 注意：安装驱动后才能使用 AI 助手，否则会报错。

## 顶部工具栏

![](https://cdn-resource.spacemit.com/tools/docs-tool/zh/studio/static/ai_00.png)

AI 助手面板顶部工具栏从左到右依次为：

- **[技能管理](ai.md#技能管理)**：管理已安装的 AI 技能（Skill），可启用、禁用或添加新技能
- **新建会话**：创建一个全新的对话会话
- **会话记录**：查看历史会话列表，可切换回之前的对话
- **清空对话**：清除当前会话中的所有消息
- **收起面板**：隐藏 AI 助手面板

## 技能管理

![](https://cdn-resource.spacemit.com/tools/docs-tool/zh/studio/static/ai_01.png)

技能（Skill）是 AI 助手的功能扩展模块，每个技能对应特定的知识库或任务能力。技能管理界面提供以下功能：

- **技能列表**：显示已安装的技能，包括技能名称和描述
- **启用/禁用**：每个技能右侧有开关，可按需开启或关闭
- **搜索**：顶部搜索框可按名称快速筛选技能

### 技能商店

![](https://cdn-resource.spacemit.com/tools/docs-tool/zh/studio/static/ai_02.png)

点击**技能商店**后打开可用技能列表，以可安装的技能卡片形式展示。每张卡片显示技能名称、版本、标签、描述及 **添加到本地** 按钮，支持按分类筛选和关键词搜索。

技能商店中的示例技能包括 **烧录助手**、**设备诊断专家**、**文件管理器** 和 **性能监控**。

### 新建技能

![](https://cdn-resource.spacemit.com/tools/docs-tool/zh/studio/static/ai_03.png)

点击**新建技能**后弹出创建表单，可填写以下信息：

- **名称**：技能的唯一标识符。
- **描述**：技能的功能说明。
- **系统提示词**：定义技能人格、行为和响应风格的系统提示词。
- **工具权限**：选择 **所有工具** 可授予技能访问所有可用工具的权限，或选择 **白名单** 将其限制为指定工具子集。

填写完成后点击**保存**创建自定义技能，或点击**取消**放弃创建。