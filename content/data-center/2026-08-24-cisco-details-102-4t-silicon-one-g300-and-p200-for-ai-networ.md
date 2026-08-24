---
title: "Cisco Details 102.4T Silicon One G300 and P200 for AI Networks"
date: 2026-08-24T07:41:36-07:00
summary: "Cisco outlined availability for its 102.4 Tb/s Silicon One G300 and 51.2 Tb/s P200 chips targeting AI cluster scale-out and scale-across networking."
tags: ["ethernet", "switching", "ai-networking", "silicon-one"]
source_type: press
sources:
  - "https://www.datacenterknowledge.com/networking/ai-data-center-networking-scaling-up-out-and-across-with-102-4t-ethernet"
---

[Cisco detailed availability timelines for its Silicon One G300 and P200 networking chips](https://www.datacenterknowledge.com/networking/ai-data-center-networking-scaling-up-out-and-across-with-102-4t-ethernet) at its Cisco Live event in June, with broad shipment expected before the end of 2026. The new application-specific integrated circuits (ASICs) target the bottleneck of network silicon in large artificial intelligence (AI) clusters, offering high-density Ethernet switching for both intra-data center scale-out and inter-data center scale-across connectivity.

The Silicon One G300 addresses scale-out fabrics within the data center. It delivers 102.4 Tb/s of aggregate bandwidth via 512 lanes operating at 200 Gb/s per lane, exposing a large number of high-speed channels. The chip integrates real-time telemetry, identity-aware forwarding, and traffic visibility. According to Cisco, the G300 emphasizes congestion avoidance and burst tolerance, redirecting packets instantaneously to prevent delays and maintain GPU utilization across racks of accelerators. The company positions this chip for large-cluster environments spanning training, inference, and real-time agentic workloads.

For scale-across scenarios connecting multiple sites over optical networks, the Silicon One P200 provides 51.2 Tb/s via 512 links at 100 Gb/s. It pairs with external high-bandwidth memory (HBM) to provide deep buffering for wide-area links, allowing optical fiber to operate close to capacity for long periods while minimizing perceived latency. Select customers have early access now, with 28.8 Tb/s switches featuring the P200 slated for the third quarter of 2026 and 51.2 Tb/s models due before year end.

Both chips face competition from Broadcom's Tomahawk 6 and Nvidia's Spectrum-6, which also target 102.4 Tb/s for AI networking.

For practitioners running AI infrastructure, the network determines cluster efficiency. Without predictable bandwidth and low latency, GPU investments become stranded resources. The G300 and P200 acknowledge that AI networking requires purpose-built silicon with deeper buffering and richer telemetry, not incremental upgrades. High-density switches using these chips incorporate liquid cooling via cold plates mounted to the chips, with Cisco offering configurations ranging from full liquid cooling to air cooled depending on customer requirements.
