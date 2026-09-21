---
title: "GeoRIS Geofences Indoor 5G Using Reconfigurable Intelligent Surfaces"
date: 2026-09-21T07:29:07-07:00
summary: "A preprint on arXiv proposes using reconfigurable intelligent surfaces to dynamically block or allow outdoor-to-indoor 5G signals."
tags: ["ris", "geofencing", "5g", "wireless"]
source_type: research
sources:
  - "https://arxiv.org/abs/2609.21077"
---

Researchers posted [GeoRIS: Geofencing With Reconfigurable Intelligent Surfaces](https://arxiv.org/abs/2609.21077) to arXiv cs.NI, a preprint that proposes using reconfigurable intelligent surfaces (RIS) to enforce geofencing in outdoor-to-indoor wireless scenarios. The work targets 5G enhanced mobile broadband (eMBB) links and shows how these surfaces can define whether indoor spaces get service at all.

GeoRIS is a controller that adjusts the radio environment by manipulating beam management procedures. It steers alignment for directional transmission links between an outdoor base station and indoor users. The design does not require control over the outdoor base station, and it can function with or without channel state information (CSI). That matters because operators often cannot access macro network settings or maintain perfect CSI in busy indoor settings. By tuning the RIS, the controller either extends a signal into a building or scatters it to the point that the link no longer meets 5G eMBB requirements.

The authors evaluate GeoRIS through simulations based on Third Generation Partnership Project (3GPP) network models. They find that the same RIS hardware can play opposing roles. In one mode, the surface helps the indoor area act as a strongly covered area. In another, it turns that same space into an out-of-service area. Their simulations show the system changing an indoor space from a strongly covered area to an out-of-service area, and vice versa. In the covered state, the network supports eMBB services in approximately 90 percent of the area. In the out-of-service state, it inhibits eMBB services in approximately 90 percent of the area.

For network operators and facility managers, this means a physical, software-defined perimeter for indoor wireless access. Instead of negotiating with the outdoor carrier to adjust base station power or beam patterns, staff can install an indoor RIS and toggle coverage as needed. The ability to work without CSI also lowers deployment complexity. Use cases include creating temporary dead zones for security or energy reasons, or keeping Internet of Things (IoT) traffic inside a defined boundary without relying solely on higher-layer policies.

The paper is a preprint and has not yet passed peer review. If the simulation results hold up in live deployments, GeoRIS could offer a practical addition to indoor 5G toolkits.
