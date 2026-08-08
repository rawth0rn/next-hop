---
title: "NVIDIA Ships Sixth Generation NVLink for AI Factories"
date: 2026-08-08T15:19:41-07:00
summary: "NVIDIA released sixth generation NVLink specifications for the Vera Rubin NVL72 platform."
tags: ["nvlink", "ai-factories", "gpu-interconnects", "scale-up-networking"]
source_type: engineering
sources:
  - "https://developer.nvidia.com/blog/nvidia-nvlink-the-scale-up-network-for-ai-factories/"
---

NVIDIA [published specifications](https://developer.nvidia.com/blog/nvidia-nvlink-the-scale-up-network-for-ai-factories/) for sixth generation NVLink, the NVLink 6 Switch and interconnect fabric designed for the Vera Rubin NVL72 platform.

The NVLink 6 Switch provides 3.6 TB/s of bidirectional GPU-to-GPU bandwidth per accelerator and 260 TB/s of aggregate bandwidth across a 72-GPU domain. End-to-end latency is 3X lower than off-the-shelf Ethernet alternatives, while packet rates are 10X higher. The architecture forms a single all-to-all topology through NVLink Switch trays and a spine of 5,000 cables, allowing any GPU to communicate with any other GPU with uniform latency and bandwidth. Each switch tray incorporates four NVLink 6 switch chips delivering 28.8 TB/s of total tray bandwidth and 14.4 TFLOPS of FP8 in-network compute for accelerating collective operations including all-reduce, reduce, and broadcast.

The sixth generation introduces intelligent resiliency features designed for continuous AI factory operation. Hot-swappable switch trays, dynamic traffic rerouting, and in-service software updates allow technicians to service components without taking entire racks offline. Control plane resilience, support for partially populated racks, and fine-grained link telemetry provide fault isolation and monitoring capabilities. These features address the operational reality of densely packed infrastructure where individual rack values are high and downtime disrupts model training and inference pipelines.

For practitioners operating AI infrastructure, the scale-up fabric determines whether mixture-of-experts (MoE) models achieve performance gains or stall on communication overhead. Modern inference with expert parallelism requires intensive all-to-all GPU communication; tokens must dispatch to selected experts, process, and gather with minimal latency. A low-bandwidth or high-latency fabric erases the benefits of parallel processing. NVLink 6 optimizes tokens per watt and per dollar by keeping GPUs fed with data, while resiliency features ensure that hardware maintenance does not become a bottleneck in continuous production environments.
