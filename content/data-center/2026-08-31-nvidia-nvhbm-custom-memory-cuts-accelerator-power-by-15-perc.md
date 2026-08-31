---
title: "NVIDIA NVHBM Custom Memory Cuts Accelerator Power by 15 Percent"
date: 2026-08-31T07:31:19-07:00
summary: "NVIDIA NVHBM custom memory delivers up to 30 percent more bandwidth with 15 percent lower power for AI accelerators."
tags: ["hbm", "ai-accelerators", "nvlink", "power-efficiency"]
source_type: engineering
sources:
  - "https://developer.nvidia.com/blog/nvidia-nvlink-fusion-brings-nvhbm-to-next-generation-ai-infrastructure/"
---

NVIDIA introduced NVHBM, a custom high-bandwidth memory (HBM) base-die technology designed for custom AI accelerators (XPUs), as part of its NVLink Fusion platform ([NVIDIA Developer Blog](https://developer.nvidia.com/blog/nvidia-nvlink-fusion-brings-nvhbm-to-next-generation-ai-infrastructure/)).

NVHBM integrates the memory controller into the 3D HBM stack and uses a custom physical interface (PHY). Compared with the JEDEC HBM4e standard, this design reduces PHY and support area by up to 67 percent. The narrower interface simplifies interposer routing, reclaiming up to 80 percent more usable silicon across the layout. This allows the central compute die to expand, providing up to a 30 percent increase in available main-die silicon for compute or other features within a fixed package footprint.

The memory delivers up to 30 percent more bandwidth per stack than standard HBM4e while consuming 15 percent less power. Higher bandwidth keeps compute engines fed during bandwidth-intensive phases of training and inference, improving accelerator utilization. Lower power creates thermal headroom for higher sustained utilization or additional compute logic.

For practitioners building AI infrastructure, the power savings translate directly into rack-scale density. In a hypothetical 1-gigawatt data center deploying 2,000W XPUs, the 15 percent power reduction could enable up to 15,000 additional accelerators in the same power envelope. The area savings let hyperscalers add workload-specific capabilities, such as specialized engines for inference serving or multimodal pipelines, without growing the package size.

NVHBM connects to the NVLink Fusion chiplet, which bridges custom XPUs into the sixth-generation NVLink scale-up fabric. This lets operators deploy semi-custom accelerators alongside standard GPUs within the same rack-scale domain, using shared networking and software stacks. The combined improvements translate into a 30 percent overall end-to-end performance increase per XPU, according to NVIDIA.
