---
title: "Ordered Chaos paper offers adaptive multipath load balancing with fast loss detection"
date: 2026-11-02T07:43:42-08:00
summary: "ArXiv preprint Ordered Chaos combines subflow spraying with precise loss detection to improve datacenter fabric performance."
tags: ["load-balancing", "datacenter", "transport-protocols", "congestion-control"]
source_type: research
sources:
  - "https://arxiv.org/abs/2610.41707"
---

Researchers posted [Ordered Chaos: Towards Adaptive Multipath Load Balancing with Precise Fast Loss Detection](https://arxiv.org/abs/2610.41707) to arXiv cs.NI on 2 November 2026. The preprint targets the tension between order-preserving routing and packet spraying in best-effort datacenter fabrics.

Current schemes force a choice. Equal-Cost Multipath (ECMP) keeps packets in order, which preserves the loss signals that Transmission Control Protocol (TCP) needs for fast recovery. However, ECMP hashes flows to fixed paths, so it cannot shift traffic away from hotspots quickly. Packet spraying spreads load evenly across all available paths, but it destroys ordering and makes it impossible to tell whether a gap in the sequence is loss, reordering, or merely delay. Network stacks then wait for timeouts, adding latency.

Ordered Chaos splits the difference with Reactive Subflow Spraying (RSS) and Precise Fast Loss Detection (PFLD). RSS divides each flow into subflows, each routed independently while keeping packets inside a subflow ordered. This retains enough structure for the receiver to detect loss quickly. PFLD sends lightweight probes alongside data packets. When a gap appears, the receiver uses probe timing to distinguish congestion drops from corruption, tail drops, or retransmissions within one round-trip time (RTT).

The authors tested the design in simulation, on AI and high-performance computing (HPC) workloads, and on a data processing unit (DPU) prototype. RSS plus PFLD cut tail flow completion time by up to three times, removed up to 99 percent of timeout-based recoveries, and sped up collective and training communication by up to 35 percent.

For operators, the benefit is concrete. Datacenter fabrics running RDMA over Converged Ethernet version 2 (RoCEv2) or TCP can adopt the end-host logic without changing switches. Reducing tail latency and eliminating timeouts improves throughput for storage replication and distributed training jobs that currently stall when ECMP hashes collide or when spraying triggers spurious retransmissions.
