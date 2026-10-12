---
title: "NVIDIA Open Sources DOCA GPUNetIO for GPU-Driven Networking"
date: 2026-10-12T07:29:13-07:00
summary: "NVIDIA open-sourced DOCA GPUNetIO to unify GPU-initiated networking and remove the CPU from the data path."
tags: ["gpunetio", "gpu", "rdma", "cuda"]
source_type: engineering
sources:
  - "https://developer.nvidia.com/blog/doca-gpunetio-gda-ki-unified-gpu-networking/"
---

NVIDIA has open-sourced [DOCA GPUNetIO](https://developer.nvidia.com/blog/doca-gpunetio-gda-ki-unified-gpu-networking/) and unified its GPU-initiated networking stack, giving CUDA kernels direct control over Ethernet and Remote Direct Memory Access (RDMA) operations without CPU involvement in the data path.

DOCA GPUNetIO is a GPU-centric networking SDK that treats packet processing and data movement as first-class GPU operations. It combines GPUDirect RDMA, GPUDirect Async Kernel-Initiated (GDA-KI), and GDRCopy so CUDA kernels can post Work Queue Entries (WQEs), ring network interface card (NIC) doorbells, and poll Completion Queue Entries (CQEs) directly. The control path still runs on the host CPU to initialize devices and create transport objects via DOCA Verbs or DOCA Ethernet, but these objects are exported to GPU memory as descriptors. Once the setup completes, the data path runs entirely on the GPU, eliminating the latency and overhead of CPU-mediated transactions.

The release matters because it consolidates what had been fragmented. Before this unification, libraries such as NCCL, NVSHMEM, UCX/NIXL, and DeepEP each maintained their own separate GDA-KI implementations for GPU-initiated RDMA. Now they converge on a single GPUNetIO foundation. NVIDIA ships two variants: a full DOCA SDK version supporting Verbs, Ethernet, DMA, and Comm Channel, and a lighter open-source implementation focused on RDMA Verbs. The open-source version can detect the SDK at runtime and call advanced features when available, or fall back to its own implementation when the SDK is absent.

For operators running distributed AI training or real-time inference, this means less duplicated code across the software stack, faster propagation of optimizations and bug fixes, and a stable target for integration. Instead of debugging multiple slightly different RDMA paths, practitioners now get one hardened GDA-KI implementation shared by the ecosystem. The unified model also simplifies performance tuning, since optimizations made for one framework become immediately available to all others using the same base.
