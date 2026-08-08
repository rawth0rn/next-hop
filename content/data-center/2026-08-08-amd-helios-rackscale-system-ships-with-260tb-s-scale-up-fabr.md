---
title: "AMD Helios Rackscale System Ships with 260TB/s Scale-Up Fabric"
date: 2026-08-08T15:03:36-07:00
summary: "AMD's 72-GPU Helios rack entered production with 260TB/s scale-up fabric and 1.7PB/s aggregate memory bandwidth."
tags: ["amd", "helios", "rackscale", "gpu-interconnect"]
source_type: press
sources:
  - "https://www.servethehome.com/amd-helios-architecture-deep-dive-amd-broadcom-hardware-combined/"
---

[ServeTheHome](https://www.servethehome.com/amd-helios-architecture-deep-dive-amd-broadcom-hardware-combined/) reports that AMD entered production with its Helios rackscale architecture, revealing full specifications for the 72-GPU system that clusters EPYC processors, Instinct accelerators, and Pensando network interface cards (NICs) and data processing units (DPUs) into a single coherent unit designed for AI workloads.

The Helios rack combines AMD EPYC 9006 "Venice" processors with Instinct MI455X GPUs to create a unified computing appliance. The system scales to 72 GPUs offering 2.9 EFLOPS of peak MXFP4 compute performance. Each GPU carries 432GB of High Bandwidth Memory 4 (HBM4), yielding 31TB total memory capacity across the rack with aggregate bandwidth reaching 1.7PB per second.

Notably, the per-GPU memory bandwidth runs 21% higher than AMD originally projected, which addresses one of the persistent bottlenecks in AI inference workloads. Networking hardware distinguishes between scale-up and scale-out domains. The scale-up fabric provides 260TB per second of cumulative bandwidth between nodes within the same Helios rack, enabling the GPUs to function as a single coherent machine for training runs.

For connecting multiple Helios racks, the scale-out links offer 43TB per second of bandwidth. This dual-fabric approach reflects the architecture of modern AI training clusters, where intra-rack communication demands far exceed inter-rack requirements.

For operators building AI infrastructure, the production readiness matters because rackscale systems have become the default unit of deployment for large language model training and inference. The bandwidth figures, particularly the 1.7PB per second aggregate memory bandwidth and the 260TB per second scale-up fabric, define the performance boundaries for workloads that span dozens of accelerators. The 21% memory bandwidth improvement over initial projections directly impacts inference latency and throughput without requiring hardware revisions.

The Helios architecture demonstrates how processor, GPU, and DPU integration changes the procurement and operational model for AI clusters, moving from server-centric to rack-centric deployment.
