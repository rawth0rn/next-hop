---
title: "INC-SRv6 repurposes SRv6 headers for UAV mesh failover"
date: 2026-11-16T07:27:04-08:00
summary: "Researchers propose using the SRv6 Segments Left pointer to enable distributed route learning and fast failover in dynamic UAV networks without control plane flooding."
tags: ["srv6", "uav-networks", "segment-routing", "mesh-networks"]
source_type: research
sources:
  - "https://arxiv.org/abs/2611.17659"
---

Researchers posted INC-SRv6: In-Network Route Exploration and Fast Failover Using Segment Routing Headers in Dynamic UAV Networks to [arXiv](https://arxiv.org/abs/2611.17659) as a preprint. The paper proposes a routing mechanism that repurposes the IPv6 Segment Routing Header (SRH) to enable in-network route exploration and fast failover for dynamic unmanned aerial vehicle (UAV) networks.

The mechanism treats the SRH Segments Left (SL) pointer as a dynamic partition rather than a simple countdown. Slots ahead of the active SL pointer record hop-by-hop next-hop information as the packet traverses the network. The suffix behind SL serves simultaneously as an in-band multi-destination reachability vector. Transit routers extract distance-weighted updates from arriving suffixes and gate admission through single-pass confidence checks with bounded binary probing. When links fail, routers deterministically advance or reverse the SL pointer to restore pre-transmission SRH state for local failover. This allows the network to repair multi-hop paths without flooding the control plane.

Simulations across 200-node 3D UAV networks with high-speed flight and repeated 20% relay outages show packet delivery of 92.12% versus 89.12% for reactive routing. The 95th-percentile tail delay drops from 121.26 ms to 8.84 ms. Control traffic falls by 35.8%, with a 4-byte compact uSID stride model cutting SRv6 control bytes by over 52%. The improvement comes from localizing recovery decisions to individual routers rather than waiting for centralized convergence or full route recomputation.

For operators building airborne mesh networks, INC-SRv6 offers a way to handle rapid link turnover under high-speed flight without burdening the control plane. The approach uses existing SRv6 header fields rather than introducing new protocols, potentially simplifying deployment on standard IPv6 forwarding hardware. The compact 4-byte uSID stride model also reduces header overhead compared to standard SRv6 implementations, saving bandwidth over lossy aerial links. This matters for time-sensitive payloads requiring guaranteed delivery and latency quality of service under constantly changing topology.
