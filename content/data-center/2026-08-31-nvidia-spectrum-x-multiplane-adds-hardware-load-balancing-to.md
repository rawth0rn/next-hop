---
title: "NVIDIA Spectrum-X Multiplane Adds Hardware Load Balancing to SuperNICs"
date: 2026-08-31T07:33:43-07:00
summary: "Spectrum-X Multiplane technology isolates link failures to individual planes using hardware load balancing in the SuperNIC."
tags: ["spectrum-x", "multiplane", "congestion-control", "ai-networking"]
source_type: engineering
sources:
  - "https://developer.nvidia.com/blog/giga-scale-ai-ethernet-evolution-spectrum-x-ethernet-rewrites-rules/"
---

NVIDIA [published](https://developer.nvidia.com/blog/giga-scale-ai-ethernet-evolution-spectrum-x-ethernet-rewrites-rules/) architectural details for Spectrum-X Multiplane technology, a hardware-accelerated load balancing mechanism for network interface cards (NICs) deployed in AI clusters. The system addresses a fundamental flaw in standard multiplane Ethernet designs that handle AI training traffic.

Traditional multiplane topologies split a host's bandwidth, such as 800 gigabits per second, into multiple lower-speed planes, such as four at 200 gigabits per second each. Standard approaches use oblivious packet spraying, distributing traffic sequentially across planes without visibility into individual plane health. When a single fiber link degrades or flaps, the degraded plane slows, yet oblivious spraying continues to send traffic to it. This forces the entire network to bottleneck at the speed of the slowest plane.

Spectrum-X Multiplane technology implements a Plane Load Balancer (PLB) directly in SuperNIC silicon. The PLB makes the multiplane architecture transparent to applications, exposing a single unified Remote Direct Memory Access over Converged Ethernet (RoCE) device to the operating system while handling all distribution in hardware.

The PLB operates via a two-stage hierarchical selection process. For every destination GPU, the SuperNIC maintains independent Congestion Control (CC) contexts for each physical plane, monitoring Round Trip Time (RTT) probes and processing Congestion Notification Packets (CNPs) to calculate real-time rate allowances. Before transmission, the NIC filters out any planes experiencing end-to-end congestion or link failure. From the remaining healthy planes, the hardware selects the plane with the shallowest local egress queue.

This isolation prevents faults from propagating across planes. In a validation scenario with a 20 percent switch-to-switch connectivity failure on one plane of an eight-plane network, traditional Ethernet multiplane designs collapsed the entire fabric to 80 percent capacity. Spectrum-X Multiplane isolated the failure, maintaining seven planes at 100 percent capacity and only the degraded plane at 80 percent, delivering 1.2 times higher All-to-All collective bandwidth during the failure.

The hardware also provides multi-tenant isolation. In a DeepSeek-V3 large language model training simulation, traditional Ethernet step times inflated from 735 milliseconds to 1.18 seconds when background traffic was introduced, while Spectrum-X maintained stable 668 millisecond step times under both standalone and congested conditions.
