---
title: "SpaceMITExecutionProvider加速算子"
lang: zh
category: "AI/计算软件栈/AI 计算软件栈列表"
source_page: https://www.spacemit.com/community/document/info?nodepath=ai/compute_stack/ai_compute_stack/onnxruntime_ep_ops.md&lang=zh
source_file: https://cdn-resource.spacemit.com/ai/docs-ai/zh/compute_stack/ai_compute_stack/onnxruntime_ep_ops.md
updated: "2026-08-11 09:20:36"
---

# SpaceMITExecutionProvider加速算子

>+ 本章节罗列SpaceMITExecutionProvider支持的加速算子及其在capability判定阶段的限制
>+ [ONNX-OP描述参考](https://onnx.ai/onnx/operators/index.html)
>+ [ONNX-Contrib-OP描述参考](https://github.com/microsoft/onnxruntime/blob/main/docs/ContribOperators.md)

- [SpaceMITExecutionProvider加速算子](onnxruntime_ep_ops.md#spacemitexecutionprovider加速算子)
  - [Dense](onnxruntime_ep_ops.md#dense)
    - [**Conv**](onnxruntime_ep_ops.md#conv)
    - [**ConvTranspose**](onnxruntime_ep_ops.md#convtranspose)
    - [**Gemm**](onnxruntime_ep_ops.md#gemm)
    - [**MatMul**](onnxruntime_ep_ops.md#matmul)
  - [QDQ](onnxruntime_ep_ops.md#qdq)
    - [**DynamicQuantizeMatMul**](onnxruntime_ep_ops.md#dynamicquantizematmul)
    - [**MatMulInteger**](onnxruntime_ep_ops.md#matmulinteger)
    - [**DynamicQuantizeLinear**](onnxruntime_ep_ops.md#dynamicquantizelinear)
    - [**QuantizeLinear**](onnxruntime_ep_ops.md#quantizelinear)
    - [**DequantizeLinear**](onnxruntime_ep_ops.md#dequantizelinear)
  - [Pool](onnxruntime_ep_ops.md#pool)
    - [**AveragePool**](onnxruntime_ep_ops.md#averagepool)
    - [**GlobalAveragePool**](onnxruntime_ep_ops.md#globalaveragepool)
    - [**MaxPool**](onnxruntime_ep_ops.md#maxpool)
    - [**GlobalMaxPool**](onnxruntime_ep_ops.md#globalmaxpool)
  - [Reduce](onnxruntime_ep_ops.md#reduce)
    - [**ReduceMean**](onnxruntime_ep_ops.md#reducemean)
    - [**ReduceMax**](onnxruntime_ep_ops.md#reducemax)
    - [**ReduceSum**](onnxruntime_ep_ops.md#reducesum)
    - [**ArgMax**](onnxruntime_ep_ops.md#argmax)
    - [**ArgMin**](onnxruntime_ep_ops.md#argmax)
  - [Math](onnxruntime_ep_ops.md#math)
    - [**Add**](onnxruntime_ep_ops.md#add)
    - [**Sub**](onnxruntime_ep_ops.md#sub)
    - [**Sum**](onnxruntime_ep_ops.md#sum)
    - [**Mul**](onnxruntime_ep_ops.md#mul)
    - [**Div**](onnxruntime_ep_ops.md#div)
    - [**Pow**](onnxruntime_ep_ops.md#pow)
    - [**Sqrt**](onnxruntime_ep_ops.md#sqrt)
    - [**Abs**](onnxruntime_ep_ops.md#abs)
    - [**Neg**](onnxruntime_ep_ops.md#neg)
    - [**Log**](onnxruntime_ep_ops.md#log)
    - [**Reciprocal**](onnxruntime_ep_ops.md#reciprocal)
    - [**Sin**](onnxruntime_ep_ops.md#sin)
    - [**Cos**](onnxruntime_ep_ops.md#cos)
    - [**Tan**](onnxruntime_ep_ops.md#tan)
    - [**Sinh**](onnxruntime_ep_ops.md#sinh)
    - [**Cosh**](onnxruntime_ep_ops.md#cosh)
    - [**Floor**](onnxruntime_ep_ops.md#floor)
    - [**Ceil**](onnxruntime_ep_ops.md#ceil)
  - [Activation](onnxruntime_ep_ops.md#activation)
    - [**Sigmoid**](onnxruntime_ep_ops.md#sigmoid)
    - [**Swish**](onnxruntime_ep_ops.md#swish)
    - [**HardSigmoid**](onnxruntime_ep_ops.md#hardsigmoid)
    - [**HardSwish**](onnxruntime_ep_ops.md#hardswish)
    - [**Tanh**](onnxruntime_ep_ops.md#tanh)
    - [**LeakyRelu**](onnxruntime_ep_ops.md#leakyrelu)
    - [**Clip**](onnxruntime_ep_ops.md#clip)
    - [**Relu**](onnxruntime_ep_ops.md#relu)
    - [**PRelu**](onnxruntime_ep_ops.md#prelu)
    - [**Elu**](onnxruntime_ep_ops.md#elu)
    - [**Gelu**](onnxruntime_ep_ops.md#gelu)
    - [**Celu**](onnxruntime_ep_ops.md#celu)
    - [**Selu**](onnxruntime_ep_ops.md#selu)
    - [**Softplus**](onnxruntime_ep_ops.md#softplus)
    - [**Softsign**](onnxruntime_ep_ops.md#softsign)
    - [**Erf**](onnxruntime_ep_ops.md#erf)
    - [**Softmax**](onnxruntime_ep_ops.md#softmax)
    - [**LogSoftmax**](onnxruntime_ep_ops.md#logsoftmax)
  - [Tensor](onnxruntime_ep_ops.md#tensor)
    - [**Cast**](onnxruntime_ep_ops.md#cast)
    - [**Concat**](onnxruntime_ep_ops.md#concat)
    - [**Split**](onnxruntime_ep_ops.md#split)
    - [**Transpose**](onnxruntime_ep_ops.md#transpose)
    - [**Unsqueeze**](onnxruntime_ep_ops.md#unsqueeze)
    - [**Squeeze**](onnxruntime_ep_ops.md#squeeze)
    - [**Reshape**](onnxruntime_ep_ops.md#reshape)
    - [**Flatten**](onnxruntime_ep_ops.md#flatten)
    - [**Gather**](onnxruntime_ep_ops.md#gather)
    - [**GatherND**](onnxruntime_ep_ops.md#gathernd)
    - [**ScatterND**](onnxruntime_ep_ops.md#scatternd)
    - [**Slice**](onnxruntime_ep_ops.md#slice)
    - [**Resize**](onnxruntime_ep_ops.md#resize)
    - [**Where**](onnxruntime_ep_ops.md#where)
    - [**Pad**](onnxruntime_ep_ops.md#pad)
    - [**Tile**](onnxruntime_ep_ops.md#tile)
    - [**GridSample**](onnxruntime_ep_ops.md#gridsample)
  - [Norm](onnxruntime_ep_ops.md#norm)
    - [**LayerNormalization**](onnxruntime_ep_ops.md#layernormalization)
    - [**InstanceNormalization**](onnxruntime_ep_ops.md#instancenormalization)
    - [**BatchNormalization**](onnxruntime_ep_ops.md#batchnormalization)
    - [**RMSNormalization**](onnxruntime_ep_ops.md#rmsnormalization)
    - [**GroupNormalization**](onnxruntime_ep_ops.md#groupnormalization)
  - [Compare](onnxruntime_ep_ops.md#compare)
    - [**Equal**](onnxruntime_ep_ops.md#equal)
    - [**Greater**](onnxruntime_ep_ops.md#greater)
    - [**GreaterOrEqual**](onnxruntime_ep_ops.md#greaterorequal)
    - [**Less**](onnxruntime_ep_ops.md#less)
    - [**LessOrEqual**](onnxruntime_ep_ops.md#lessorequal)
  - [Transformer](onnxruntime_ep_ops.md#transformer)
    - [**RotaryEmbedding**](onnxruntime_ep_ops.md#rotaryembeding)
    - [**Attention**](onnxruntime_ep_ops.md#attention)
  - [Custom operator](onnxruntime_ep_ops.md#customop)
    - [**YoloDecode**](onnxruntime_ep_ops.md#yolodecode)

## Dense
### **Conv**
>+ Domain: ai.onnx
>+ Opset: 11
>+ Attributes: kernel_shape需存在；W需为常量，或由无上游输入边的DequantizeLinear节点提供
>+ Type: T：tensor(float) | tensor(float16)
>+ Notes: kernel_shape维度数不超过3，支持1D、2D、3D

### **ConvTranspose**
>+ Domain: ai.onnx
>+ Opset: 11
>+ Attributes: kernel_shape需存在；W需为常量，或由无上游输入边的DequantizeLinear节点提供
>+ Type: T：tensor(float) | tensor(float16)
>+ Notes: kernel_shape维度数不超过2，支持1D、2D

### **Gemm**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes: transA==0，alpha==1.0，beta==1.0
>+ Type: T：tensor(float) | tensor(float16)
>+ Notes: 支持QDQ量化格式，A非对称pertensor，B对称perchannel，当B为非常量时，B需为非对称pertensor

### **MatMul**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes: 无额外属性限制
>+ Type: T：tensor(float) | tensor(float16)
>+ Notes: 支持QDQ量化格式，A非对称pertensor，B对称perchannel，当B为非常量时，B需为非对称pertensor

## QDQ
### **DynamicQuantizeMatMul**
>+ Domain: com.microsoft
>+ Opset: 1（参考ONNX-Contrib）
>+ Attributes:
>+ Type: T1：tensor(float)
>+ Type: T2：tensor(float)

### **MatMulInteger**
>+ Domain: ai.onnx
>+ Opset: 10
>+ Attributes:
>+ Type: T1：tensor(int8) | tensor(uint8)
>+ Type: T2：tensor(int32)

### **DynamicQuantizeLinear**
>+ Domain: ai.onnx
>+ Opset: 11
>+ Attributes:
>+ Type: T1：tensor(float)
>+ Type: T2：tensor(int8) | tensor(uint8)

### **QuantizeLinear**
>+ Domain: ai.onnx
>+ Opset: 19
>+ Attributes:
>+ Type: T1：tensor(float)
>+ Type: T2：tensor(int8) | tensor(uint8)

### **DequantizeLinear**
>+ Domain: ai.onnx
>+ Opset: 19
>+ Attributes:
>+ Type: T1：tensor(int8) | tensor(uint8) | tensor(int32)
>+ Type: T2：tensor(float)

## Pool
### **AveragePool**
>+ Domain: ai.onnx
>+ Opset: 22
>+ Attributes: 若count_include_pad!=1，则pads必须全为0；若存在kernel_shape，其维度数不超过2
>+ Type: T：tensor(float) | tensor(float16)

### **GlobalAveragePool**
>+ Domain: ai.onnx
>+ Opset: 1
>+ Attributes: 若存在kernel_shape，其维度数不超过2
>+ Type: T：tensor(float) | tensor(float16)

### **MaxPool**
>+ Domain: ai.onnx
>+ Opset: 12
>+ Attributes: 若存在kernel_shape，其维度数不超过2
>+ Type: T：tensor(float) | tensor(float16)

### **GlobalMaxPool**
>+ Domain: ai.onnx
>+ Opset: 1
>+ Attributes: 若存在kernel_shape，其维度数不超过2
>+ Type: T：tensor(float) | tensor(float16)

## Reduce
### **ReduceMean**
>+ Domain: ai.onnx
>+ Opset: 18
>+ Attributes: 除第一个输入外，其余输入需为常量initializer
>+ Type: T：tensor(float) | tensor(float16)

### **ReduceMax**
>+ Domain: ai.onnx
>+ Opset: 20
>+ Attributes: 除第一个输入外，其余输入需为常量initializer
>+ Type: T：tensor(float) | tensor(float16)

### **ReduceSum**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes: 除第一个输入外，其余输入需为常量initializer
>+ Type: T：tensor(float) | tensor(float16)

### **ArgMax**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T1：tensor(float) | tensor(float16) | tensor(int8)
>+ Type: T2：tensor(int64)

### **ArgMin**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T1：tensor(float) | tensor(float16) | tensor(int8)
>+ Type: T2：tensor(int64)


## Math
### **Add**
>+ Domain: ai.onnx
>+ Opset: 14
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Sub**
>+ Domain: ai.onnx
>+ Opset: 14
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Sum**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Mul**
>+ Domain: ai.onnx
>+ Opset: 14
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Div**
>+ Domain: ai.onnx
>+ Opset: 14
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Pow**
>+ Domain: ai.onnx
>+ Opset: 14
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Sqrt**
>+ Domain: ai.onnx
>+ Opset: 14
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Abs**
>+ Domain: ai.onnx
>+ Opset: 14
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Neg**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Log**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Reciprocal**
>+ Domain: ai.onnx
>+ Opset: 14
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Sin**
>+ Domain: ai.onnx
>+ Opset: 7
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Cos**
>+ Domain: ai.onnx
>+ Opset: 7
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Tan**
>+ Domain: ai.onnx
>+ Opset: 7
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Sinh**
>+ Domain: ai.onnx
>+ Opset: 9
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Cosh**
>+ Domain: ai.onnx
>+ Opset: 9
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Floor**
>+ Domain: ai.onnx
>+ Opset: 6
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Ceil**
>+ Domain: ai.onnx
>+ Opset: 6
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

## Activation
### **Sigmoid**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Swish**
>+ Domain: ai.onnx
>+ Opset: 24
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **HardSigmoid**
>+ Domain: ai.onnx
>+ Opset: 22
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **HardSwish**
>+ Domain: ai.onnx
>+ Opset: 22
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Tanh**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **LeakyRelu**
>+ Domain: ai.onnx
>+ Opset: 16
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Clip**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Relu**
>+ Domain: ai.onnx
>+ Opset: 14
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **PRelu**
>+ Domain: ai.onnx
>+ Opset: 9
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Elu**
>+ Domain: ai.onnx
>+ Opset: 22
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Gelu**
>+ Domain: ai.onnx
>+ Opset: 20
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Celu**
>+ Domain: ai.onnx
>+ Opset: 12
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Selu**
>+ Domain: ai.onnx
>+ Opset: 6
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Softplus**
>+ Domain: ai.onnx
>+ Opset: 1
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Softsign**
>+ Domain: ai.onnx
>+ Opset: 1
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Erf**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Softmax**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **LogSoftmax**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

## Tensor
### **Cast**
>+ Domain: ai.onnx
>+ Opset: 24
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)

### **Concat**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)

### **Split**
>+ Domain: ai.onnx
>+ Opset: 18
>+ Attributes: 除第一个输入外，其余输入需为常量initializer
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)

### **Transpose**
>+ Domain: ai.onnx
>+ Opset: 24
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16) | tensor(int8)

### **Unsqueeze**
>+ Domain: ai.onnx
>+ Opset: 24
>+ Attributes: axes输入需为常量initializer
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)

### **Squeeze**
>+ Domain: ai.onnx
>+ Opset: 24
>+ Attributes: axes输入需为常量initializer
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)

### **Reshape**
>+ Domain: ai.onnx
>+ Opset: 24
>+ Attributes: shape输入需为常量initializer
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)

### **Flatten**
>+ Domain: ai.onnx
>+ Opset: 24
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)

### **Gather**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)

### **GatherND**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)

### **ScatterND**
>+ Domain: ai.onnx
>+ Opset: 16
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)

### **Slice**
>+ Domain: ai.onnx
>+ Opset: 13
>+ Attributes: 除第一个输入外，其余输入需为常量initializer；仅支持opset >= 10
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)

### **Resize**
>+ Domain: ai.onnx
>+ Opset: 19
>+ Attributes: coordinate_transformation_mode仅支持asymmetric、half_pixel；mode仅支持nearest、linear
>+ Type: T：tensor(float) | tensor(float16) | tensor(int8)

### **Where**
>+ Domain: ai.onnx
>+ Opset: 9
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)

### **Pad**
>+ Domain: ai.onnx
>+ Opset: 21
>+ Attributes: pads输入需为常量initializer
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(int8) | tensor(uint8)

### **Tile**
>+ Domain: ai.onnx
>+ Opset: 6
>+ Attributes: repeats输入需为常量initializer
>+ Type: T：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)

### **GridSample**
>+ Domain: ai.onnx
>+ Opset: 16
>+ Attributes: mode仅支持bilinear、nearest；padding_mode仅支持zeros、border
>+ Type: T1：tensor(float) | tensor(float16)

## Norm
### **LayerNormalization**
>+ Domain: ai.onnx
>+ Opset: 17
>+ Attributes: capability阶段无额外常量限制
>+ Type: T：tensor(float) | tensor(float16)

### **InstanceNormalization**
>+ Domain: ai.onnx
>+ Opset: 6
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **BatchNormalization**
>+ Domain: ai.onnx
>+ Opset: 15
>+ Attributes: capability阶段无额外常量限制
>+ Type: T：tensor(float) | tensor(float16)

### **RMSNormalization**
>+ Domain: ai.onnx
>+ Opset: 23
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **GroupNormalization**
>+ Domain: ai.onnx
>+ Opset: 21
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

## Compare
### **Equal**
>+ Domain: ai.onnx
>+ Opset: 11
>+ Attributes:
>+ Type: T1：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)
>+ Type: T2：tensor(uint8) | tensor(bool)

### **Greater**
>+ Domain: ai.onnx
>+ Opset: 9
>+ Attributes:
>+ Type: T1：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)
>+ Type: T2：tensor(uint8) | tensor(bool)

### **GreaterOrEqual**
>+ Domain: ai.onnx
>+ Opset: 12
>+ Attributes:
>+ Type: T1：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)
>+ Type: T2：tensor(uint8) | tensor(bool)

### **Less**
>+ Domain: ai.onnx
>+ Opset: 9
>+ Attributes:
>+ Type: T1：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)
>+ Type: T2：tensor(uint8) | tensor(bool)

### **LessOrEqual**
>+ Domain: ai.onnx
>+ Opset: 12
>+ Attributes:
>+ Type: T1：tensor(float) | tensor(float16) | tensor(int32) | tensor(uint32) | tensor(int8) | tensor(uint8) | tensor(bool)
>+ Type: T2：tensor(uint8) | tensor(bool)

## Transformer
### **RotaryEmbedding**
>+ Domain: ai.onnx
>+ Opset: 23
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

### **Attention**
>+ Domain: ai.onnx
>+ Opset: 23
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)

## Contrib Function operator
### **YoloDecode**
>+ Domain: spacemit_functions.YoloDecode
>+ Opset: 
>+ Attributes:
>+ Type: T：tensor(float) | tensor(float16)
