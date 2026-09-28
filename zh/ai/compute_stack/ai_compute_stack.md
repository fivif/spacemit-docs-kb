---
title: "AI 计算软件栈"
lang: zh
category: "AI/计算软件栈"
source_page: https://www.spacemit.com/community/document/info?nodepath=ai/compute_stack/ai_compute_stack.md&lang=zh
source_file: https://cdn-resource.spacemit.com/ai/docs-ai/zh/compute_stack/ai_compute_stack.md
updated: "2026-06-04 08:40:37"
---

# AI 计算软件栈

## 软件栈框架

![AI软件栈图](../../../_assets/docs-ai/compute_stack/images/ai_compute_stack.png)

## 多层级交付

进迭时空AI计算软件栈提供多层级交付产物，以满足AI生态上的多类用户多样化的需求

### 端到端模型推理

* [OnnxRuntime](ai_compute_stack/onnxruntime.md)
  > 基于ONNXRuntime的SpacemiT推理引擎，通过使用`SpaceMITExecutionProvider`获得极致推理性能

* [XSlim](ai_compute_stack/xslim.md)
  > 模型量化精简工具链，支持多种量化格式与量化调优策略

* [Llama.cpp](ai_compute_stack/llama.cpp.md)
  > 轻量大模型推理引擎，完全开源并同步社区

* [vLLM](ai_compute_stack/vllm.md)
  > 热门的高性能大语言模型推理与服务框架，支持原生部署大模型

### AI算子加速库

* TBD

### AI编程语言

* [Triton](ai_compute_stack/triton.md)
  > 提供Python交互的高性能AI算子编程体验

### 示例

* [QuickStart](ai_compute_stack/quick_start.md)
* [ModelZoo](ai_compute_stack/modelzoo.md)
