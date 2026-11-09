---
title: "NVIDIA open-source tools reduce 5G simulation times to minutes"
date: 2026-11-09T07:46:11-08:00
summary: "CTTC researchers used NVIDIA Aerial to cut 5G network simulation times from three hours to 10 to 20 minutes."
tags: ["5g", "6g", "simulation", "open-source"]
source_type: press
sources:
  - "https://blogs.nvidia.com/blog/telco-open-source-tools-research-6g-networks/"
---

[NVIDIA](https://blogs.nvidia.com/blog/telco-open-source-tools-research-6g-networks/) open-sourced its Aerial wireless software and Sionna physical-layer simulator last year, and researchers at the Centre Tecnològic de Telecomunicacions de Catalunya (CTTC) have now integrated GPU-accelerated radio channel models that cut 5G network simulation times from approximately three hours to 10 to 20 minutes.

The integration brings NVIDIA Aerial CUDA-Accelerated RAN (ACAR) into CTTC’s open source 5G-LENA network simulator. ACAR provides GPU-accelerated calculations of how wireless signals travel between antennas and devices, accounting for reflections, scattering, and path loss. These channel models grow increasingly demanding as simulated networks add more nodes and mobility patterns, requiring recalculation for every transmission and movement. By executing these calculations on GPUs instead of traditional CPU-based methods, CTTC preserved the expected statistical behavior and network performance while reducing runtime. The early evaluation maintained accuracy across diverse scenarios.

For network operators and equipment designers, shorter simulation cycles translate directly to faster validation of radio resource management algorithms, beamforming strategies, and interference mitigation before committing to costly hardware builds and field trials. Teams can compare more design alternatives, stress-test edge cases with hundreds of contending devices, and refine parameters without waiting hours for batch results. This compression of the simulation-to-real pipeline helps evaluate 6G proposals thoroughly without stretching development timelines or inflating research and development budgets. Faster iteration means fewer surprises after deployment, reducing the risk of discovering coverage holes or capacity limits when baseband units and antennas are already installed and operational. The tools are available on GitHub as open source projects, allowing other research groups to replicate the CTTC integration or adapt the GPU acceleration for their own network simulators.
