---
title: "DT-STABLE Framework Manages LEO Interference Using Digital Twins"
date: 2026-10-26T07:26:48-07:00
summary: "Researchers propose a digital twin framework for managing interference between terrestrial and satellite networks in Open RAN environments."
tags: ["o-ran", "digital-twins", "satellite", "interference"]
source_type: research
sources:
  - "https://arxiv.org/abs/2610.32827"
---

Researchers posted a [preprint](https://arxiv.org/abs/2610.32827) to arXiv describing DT-STABLE, a framework that couples digital twins with Open RAN (O-RAN) interfaces to manage interference between terrestrial networks (TNs) and non-terrestrial networks (NTNs) using low-Earth orbit (LEO) satellites. The paper, "Multi-Timescale Context-Aware Radio Resource Optimization for Harmonious NTN-TN Coexistence: A Digital Twin and Open RAN Enabled Framework", addresses aggregate interference from terrestrial downlink transmissions at satellite receivers.

The framework uses site-specific data to build a digital twin that estimates interference at LEO satellites, enabling proactive radio resource management without exhaustive real-time measurements. The authors formulate the optimization as joint beam activation and user association under constraints including RF chain limits, load balancing, and aggregate satellite interference limits. They prove this problem is NP-hard and develop a digital twin-guided scheduling algorithm to solve it efficiently.

The architecture operates across multiple timescales. Short-timescale radio resource adaptation runs continuously, while mid- and long-timescale digital twin updates occur periodically through standardized O-RAN interfaces. This separation allows the system to react quickly to channel variations while keeping computationally intensive optimization offline.

For operators running 28 GHz networks, the simulations show concrete operational benefits. The framework achieves 89.63 percent interference-to-noise ratio (INR) satisfaction with a mean sum rate of 210.96 bps/Hz. When satellite protection is prioritized, INR satisfaction approaches nearly 100 percent. The digital twin approach reduces beam measurement overhead by 99.71 percent compared to exhaustive sweeping and achieves up to 33.1 times lower runtime than exact optimization using Gurobi.

This matters for practitioners because it offers a path to integrate LEO satellite services without building separate spectrum silos. The O-RAN integration means the framework can interface with existing disaggregated radio access networks through standardized interfaces. The reduced measurement overhead addresses the computational cost of managing interference in dense millimeter-wave deployments, while the multi-timescale approach aligns with how operators already separate real-time scheduling from slower configuration updates.
