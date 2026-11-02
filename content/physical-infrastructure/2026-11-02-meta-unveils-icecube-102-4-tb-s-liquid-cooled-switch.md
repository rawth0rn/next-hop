---
title: "Meta Unveils IceCube 102.4 Tb/s Liquid-Cooled Switch"
date: 2026-11-02T07:47:50-08:00
summary: "Meta unveils its first liquid-cooled 102.4 Tb/s switch blade for AI clusters."
tags: ["liquid-cooling", "800g-ethernet", "open-compute", "fboss"]
source_type: engineering
sources:
  - "https://engineering.fb.com/2026/10/26/open-source/ocp-summit-2026-meta-networking-talks/"
---

Meta [unveiled IceCube](https://engineering.fb.com/2026/10/26/open-source/ocp-summit-2026-meta-networking-talks/), its first liquid-cooled network switch, at the 2026 Open Compute Project (OCP) Global Summit.

The switch delivers 102.4 Tb/s of non-blocking capacity across 128 ports of 800 Gb/s Ethernet. Meta offers two variants: one built around the Broadcom Tomahawk 6C and another using the NVIDIA Spectrum-6 application-specific integrated circuit (ASIC). Both fit into IcePack, Meta's liquid-cooled rack architecture, as 2OU (two open rack units) blades that use hybrid liquid and air cooling. The design is physical layer (PHY)-less, meaning it eliminates the retimer chips typically found between the ASIC and the optical modules, reducing power and latency.

The hardware runs FBOSS, Meta's network operating system. This extends Meta's existing software stack from previous generations directly onto the new 102.4 Tb/s silicon.

AI training clusters are pushing power density beyond what air-cooled switches can sustain. The 102.4 Tb/s generation of switching silicon generates heat densities that require liquid cooling to operate reliably at scale. By moving to a liquid-cooled rack design with hybrid cooling for the switch itself, Meta can deploy these high-capacity blades in its gigawatt-scale Prometheus cluster without hitting thermal limits.

The PHY-less design also cuts component count and power draw. At fleet scale, removing retimers from every 800 Gb/s link translates to measurable power savings and reduced failure points. The choice to support both Broadcom and NVIDIA ASICs under the same FBOSS stack gives Meta supply chain flexibility and avoids single-vendor lock-in for its scale-out fabric.

Meta contributed the IceCube design to OCP, continuing its push for open hardware in AI infrastructure.
