---
title: "Meta Shows MetaRoCE Adapter for Million-GPU Clusters at OCP Summit"
date: 2026-11-16T07:30:52-08:00
summary: "Meta displayed a network adapter running its MetaRoCE protocol for scaling RDMA to million-GPU clusters using commodity Ethernet."
tags: ["metaroce", "rdma", "ocp", "ethernet"]
source_type: press
sources:
  - "https://www.servethehome.com/this-is-the-meta-metaroce-network-adapter/"
---

Meta [displayed its MetaRoCE network adapter](https://www.servethehome.com/this-is-the-meta-metaroce-network-adapter/) at the Open Compute Project (OCP) Summit 2026. The card is Meta’s attempt to scale Remote Direct Memory Access (RDMA) transport to clusters of one million GPUs while keeping the underlying hardware entirely commodity.

The adapter follows the OCP Network Interface Card (NIC) 3.0 specification with a Small Form Factor (SFF) pull tab design. Meta says the protocol runs on standard Ethernet using Explicit Congestion Notification (ECN) and Equal-Cost Multi-Path (ECMP) and does not require specialized switching hardware. This means operators can deploy it across existing data center fabrics without forklift upgrades.

Key features include per-path reliability and congestion control, plus Receiver rate hints (RCN) for fast incast convergence. The implementation tolerates packet loss and reordering, and a single Queue Pair (QP) can carry multiple streams across multiple network paths simultaneously. This packet spraying approach keeps links utilized even when individual paths drop packets or arrive out of sequence. The design specifically targets incast scenarios common in synchronized training workloads where many GPUs send data to a single destination simultaneously.

Before the summit, Meta demonstrated the stack running on AMD Pensando NICs. Because those cards are programmable, Meta could implement the protocol without waiting for dedicated MetaRoCE silicon. That programmability lets Meta source hardware from multiple vendors rather than locking into a single supply chain. The ability to run on existing programmable NICs lowers the barrier to testing the transport in production environments.

For data center operators, the practical benefit is extending RDMA to training clusters without building a separate lossless network. Traditional RDMA over Ethernet often requires lossless fabrics and complex congestion management to prevent drops. MetaRoCE accepts packet loss and out-of-order delivery as normal, which matches the behavior of large ECMP fabrics built from commodity switches.

Meta has not announced general availability or pricing for the adapter. If the protocol reaches production, it could reduce dependency on specialized RDMA hardware while pushing the upper limits of GPU cluster scale.
