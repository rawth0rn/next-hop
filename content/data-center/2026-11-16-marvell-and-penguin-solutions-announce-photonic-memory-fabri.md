---
title: "Marvell and Penguin Solutions announce photonic memory fabric for AI clusters"
date: 2026-11-16T07:14:49-08:00
summary: "Marvell and Penguin Solutions announced a photonic fabric that pools 16 TB of DRAM and half a terabyte of HBM across 16 systems."
tags: ["photonics", "memory", "ai-infrastructure"]
source_type: press
sources:
  - "https://www.theregister.com/systems/2026/11/16/marvell-and-penguin-solutions-aim-to-end-the-rampocalypse-with-photonic-memory-fabric/5309921"
---

Marvell and Penguin Solutions announced a photonic memory fabric that lets up to 16 systems share 16 TB of DRAM and half a terabyte of high bandwidth memory (HBM) across a pooled optical interconnect, [according to The Register](https://www.theregister.com/systems/2026/11/16/marvell-and-penguin-solutions-aim-to-end-the-rampocalypse-with-photonic-memory-fabric/5309921).

The architecture extends memory buses beyond individual server boundaries using photonic links. Each appliance retains local memory, but the fabric presents the aggregated pool as a unified address space accessible by all connected hosts. This allows workloads to allocate DRAM and HBM dynamically rather than binding capacity permanently to specific CPUs or GPUs. The design targets AI training clusters where memory capacity, not compute, often limits throughput. Current GPU servers frequently stall while waiting for data transfers from host memory or SSDs, and the working sets for large language models exceed the HBM capacity of individual accelerators.

For operators, pooled memory addresses the fragmentation that strands expensive HBM and DRAM when individual nodes underutilize their allocations. Instead of overprovisioning every server to meet peak requirements, a cluster can share resources across the fabric, improving utilization rates and deferring hardware purchases. The optical layer provides the bandwidth necessary to maintain coherence across chassis, though latency will exceed local memory access. The announcement specifies support for up to 16 systems, suggesting initial deployment will focus on rack-scale integration rather than datacenter-wide pooling.

The technology enters a market where AI infrastructure spending concentrates on GPUs while memory bottlenecks throttle actual throughput. By decoupling memory capacity from individual compute nodes, the fabric offers a path to higher aggregate utilization without requiring application-level changes to memory semantics. Operators should evaluate whether the latency trade-offs suit their specific workloads and whether their orchestration stacks can exploit dynamic memory allocation across the pool.
