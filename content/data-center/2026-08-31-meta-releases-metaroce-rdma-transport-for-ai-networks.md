---
title: "Meta Releases MetaRoCE RDMA Transport for AI Networks"
date: 2026-08-31T07:26:11-07:00
summary: "Meta open-sources MetaRoCE, a new RDMA transport built for AI-scale Ethernet networks."
tags: ["rdma", "ai-networking", "open-source", "metaroce"]
source_type: engineering
sources:
  - "https://engineering.fb.com/2026/08/24/networking-traffic/metaroce-rdma-transport-ai-ethernet/"
---

Meta is releasing [MetaRoCE](https://engineering.fb.com/2026/08/24/networking-traffic/metaroce-rdma-transport-ai-ethernet/), a clean-sheet Remote Direct Memory Access (RDMA) transport protocol purpose-built for AI workloads on commodity Ethernet, through the Open Compute Project (OCP). The specification, reference software implementation, and compliance test suite will be available for vendors to build interoperable hardware.

Traditional RoCE expects ordered packet delivery and relies on Priority Flow Control (PFC) to achieve losslessness. MetaRoCE moves intelligence to the endpoint, treating out-of-order arrival as the normal case. Every packet carries its own destination address, allowing data to be written directly to final memory locations without reorder buffers or head-of-line blocking. The protocol sprays packets across many fine-grained logical paths, each with independent telemetry including per-path round-trip time, Explicit Congestion Notification (ECN) state, and utilization.

Loss tolerance is built into the design. MetaRoCE does not require PFC or pause frames. Each path maintains its own ordered sequence and 256-bit selective acknowledgment bitvector, so a gap triggers retransmission of exactly the missing packet on the path that lost it. Congestion control combines conventional ECN-based sender-driven Additive Increase Multiplicative Decrease (AIMD) with receiver-driven fair-share rate hints, keeping per-path windows that allow the transport to distinguish congestion from failure. A single connection can carry many independent ordered streams above while managing many paths below, stopping connection state from growing with workload parallelism.

Meta validated MetaRoCE on AMD Pensando programmable Network Interface Cards (NICs) in a 64-node GPU cluster. Under packet loss conditions that would degrade RoCEv2, MetaRoCE maintains approximately 86 percent throughput at 1 percent packet loss and continues delivering useful bandwidth even at 10 percent loss rates. Multiplane testing across four and eight planes with up to 4,000 concurrent connections showed linear throughput scaling with plane count, and simulated plane failures demonstrated graceful autonomous recovery without application involvement.

For network operators building AI infrastructure, MetaRoCE matters because it runs on existing Ethernet fabrics requiring only ECN marking and Equal-Cost Multi-Path (ECMP), no proprietary switch features. The transport performs better in ideal conditions and degrades gracefully when things go wrong, reducing the operational burden of managing lossless networks at million-GPU scale. By open-sourcing the complete stack, Meta enables a multi-vendor ecosystem around a unified standard, accelerating hardware innovation without vendor lock-in.

Meta will release the specification, Data Plane Development Kit (DPDK)-optimized software reference implementation, and production compliance framework at the October 2026 OCP Global Summit.
