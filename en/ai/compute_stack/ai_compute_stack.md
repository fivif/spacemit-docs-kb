---
title: "AI Compute Software Stack"
lang: en
category: "AI/Compute Software Stack"
source_page: https://www.spacemit.com/community/document/info?nodepath=ai/compute_stack/ai_compute_stack.md&lang=en
source_file: https://cdn-resource.spacemit.com/ai/docs-ai/en/compute_stack/ai_compute_stack.md
updated: "2026-05-28 16:40:09"
---

# AI Compute Software Stack

## Software Stack Architecture

![AI Software Stack](../../../_assets/docs-ai/compute_stack/images/ai_compute_stack.png)

## Multi-Level Delivery

The SpacemiT AI compute software stack provides **multi-level deliverables** to address the diverse needs of different users across the AI ecosystem.

### End-to-End Model Inference

- [OnnxRuntime](ai_compute_stack/onnxruntime.md)  
  > A SpacemiT inference engine based on ONNX Runtime. By leveraging the `SpaceMITExecutionProvider`, it delivers optimized inference performance.

- [XSlim](ai_compute_stack/xslim.md)  
  > A model quantization and compression toolchain that supports multiple quantization formats and tuning strategies.

- [Llama.cpp](ai_compute_stack/llama.cpp.md)  
  > A lightweight large-model inference engine that is fully open-source and kept in sync with the upstream community.

- [vLLM](ai_compute_stack/vllm.md)  
  > A popular high-performance framework for large language model inference and serving, supporting native deployment of LLMs.

### AI Operator Acceleration Libraries

> TBD

### AI Programming Languages

- [Triton](ai_compute_stack/triton.md)  
  > Provides a high-performance AI operator programming experience with a Python-based interface.

### Examples

- [QuickStart](ai_compute_stack/quick_start.md)
- [ModelZoo](ai_compute_stack/modelzoo.md)

