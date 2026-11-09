---
title: "REGULUS edge AI SoC delivers 10 TOPS at under 3W for Physical AI"
date: 2026-11-09T07:38:36-08:00
summary: "Mobilint's REGULUS SoC brings Ceva's NeuPro-Nano NPU to production, delivering 10 TOPS under 3W for power-constrained edge devices."
tags: ["edge-ai", "physical-ai", "embedded-systems", "npus"]
source_type: press
sources:
  - "https://iot-now.com/2026/11/03/159158-ceva-mobilint-physical-ai-regulus-edge-ai-soc/"
---

[Mobilint](https://iot-now.com/2026/11/03/159158-ceva-mobilint-physical-ai-regulus-edge-ai-soc/) has shipped the REGULUS edge AI System-on-Chip (SoC), marking the first production deployment of Ceva's NeuPro Neural Processing Unit (NPU) family. The device integrates Ceva's SensPro AI Digital Signal Processor (DSP) alongside the NeuPro-Nano NPN32 NPU within Mobilint's highly integrated processing architecture.

REGULUS delivers 10 TOPS of AI performance while consuming under 3W. It supports up to 8GB of memory. The multi-engine design assigns sensing and signal-processing workloads to the programmable SensPro core, while the NeuPro-Nano handles neural inference for always-on use cases. This heterogeneous architecture allows different workloads to run on the engine best suited to the task. SensPro provides flexible programmability for sensor fusion and preprocessing, while NeuPro-Nano offers dedicated efficiency for inference tasks. The split reduces power consumption compared to running all workloads on a single processing type, extending battery life in portable deployments.

The combination enables the chip to function as a standalone processor for on-device AI in power-constrained and space-constrained environments. The SoC targets Physical AI applications including robotics, drones, machine vision, smart cameras, and Internet of Things (IoT) devices. These systems must sense, interpret, and respond to surroundings in real time without relying on cloud connectivity. Local processing eliminates the need to shuttle sensor data to remote servers for initial analysis.

REGULUS is already powering commercial hardware. Mobilint's MLD-R1 AI USB accelerator, which adds on-device AI to existing systems, began shipping after its preview at COMPUTEX 2026. The accelerator supports computer vision, video analytics, and generative AI workloads across smart factories, security, medical devices, and digital signage. It offers compatibility with standard frameworks including PyTorch, ONNX, Hugging Face, TensorFlow, TFLite, and Keras.

For network operators and system architects, the chip offers a deployable option for edge AI that operates independently of cloud connectivity and high-power server hardware. The 10 TOPS performance within a 3W envelope suits battery-operated and thermally limited installations where real-time local inference is mandatory. The availability of the MLD-R1 USB accelerator provides an immediate integration path for existing equipment that requires AI acceleration without system redesign.
