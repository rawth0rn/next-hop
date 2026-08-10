---
title: "Coherent pluggables and quantum link control advance data center interconnect"
date: 2026-08-10T07:17:56-07:00
summary: "Data center interconnect sees 800G pluggable adoption and quantum link rate-fidelity advances"
tags: ["optical", "quantum", "dci", "networking"]
source_type: roundup
sources:
  - "https://www.datacenterdynamics.com/en/opinions/building-cost-effective-networks-for-the-ai-era-data-center-interconnect-and-scale-across-networking/"
  - "https://arxiv.org/abs/2608.07163"
---

[Data Center Dynamics](https://www.datacenterdynamics.com/en/opinions/building-cost-effective-networks-for-the-ai-era-data-center-interconnect-and-scale-across-networking/) published guidance on cost-effective AI-era network designs using coherent pluggables, while researchers posted a preprint on [arXiv](https://arxiv.org/abs/2608.07163) demonstrating adaptive rate-fidelity control for quantum links over deployed fiber.

The Data Center Dynamics analysis identifies three innovations reshaping data center interconnect (DCI) and scale-across networking: coherent pluggables, multi-scale open optical line systems, and AI-enabled network automation. Coherent pluggables have moved from metro DCI to mainstream use in AI and cloud interconnects. The transition from 400G ZR/ZR+ to 800G ZR/ZR+ extends pluggable economics to higher-capacity applications while reducing power consumption and footprint per bit. These devices integrate directly into routers and switches, simplifying operations compared to traditional transponder-based architectures.

The arXiv preprint, "Rate-Fidelity Control for Wide-Area Quantum Links," proposes a software-based control protocol for quantum networks. The system dynamically adjusts source pump power and polarization compensation to maximize entanglement distribution rates while maintaining minimum fidelity constraints. Using trace-driven simulations based on a 64 km deployed fiber, the authors show their adaptive controller improves mean distribution rates by 14% over optimized static policies during a 24-hour period, without requiring offline policy optimization or additional quantum hardware.

For network operators, 800G coherent pluggables offer a path to scale AI backend networks without the space and power penalties of discrete optical transport gear. The shift to pluggable optics in DCI reduces complexity and cost per bit as clusters grow beyond single data center boundaries. Meanwhile, the quantum link research addresses a physical layer challenge that could affect future quantum data center interconnects. While quantum networking remains experimental, the demonstration that software control can stabilize fidelity over deployed fiber suggests operational models for eventual production quantum links may resemble classical optical control planes more closely than current fixed-policy hardware approaches.
