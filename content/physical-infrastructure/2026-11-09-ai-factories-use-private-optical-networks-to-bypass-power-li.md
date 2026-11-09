---
title: "AI factories use private optical networks to bypass power limits"
date: 2026-11-09T08:05:15-08:00
summary: "RIPE Labs analysis shows AI factories distribute compute across campuses using private optical networks due to power constraints."
tags: ["ai-factories", "optical-networks", "power-constraints", "dci"]
source_type: research
sources:
  - "https://labs.ripe.net/author/armanobosyan/the-internets-new-factories/"
---

The RIPE Labs article [The Internet's New Factories](https://labs.ripe.net/author/armanobosyan/the-internets-new-factories/) examines how power constraints are reshaping AI factory locations and forcing operators to build dedicated optical wide-area networks between distributed campuses.

The article describes AI factories as unified systems where accelerators, storage, and data pipelines operate across multiple network layers. Unlike conventional data centres that scale vertically within a single facility, AI factories distribute compute across metropolitan regions because individual campuses face hard limits on available electricity. The International Energy Agency cites conventional facilities at 10 to 25 megawatts (MW) while hyperscale AI projects exceed 100 MW and reach gigawatt scale. Microsoft connects its Fairwater sites in Wisconsin and Atlanta through a dedicated optical AI wide-area network, while Meta has spread infrastructure across wider metropolitan areas to overcome power and space constraints. Google locates data centres near energy sources and pools compute across campuses privately, noting that moving electricity is harder than moving data over fibre.

For network operators, this shift changes what infrastructure gets built and where demand appears. Public Internet traffic graphs show little of this activity because checkpoint bursts, model replicas, and distributed workloads travel over dark fibre and dedicated wavelengths between campuses rather than through transit providers. Public traffic measurements show AI flows remain modest compared to private fabric volumes. Fibre and data-centre interconnection providers now field requests for private capacity with specific delivery dates tied to construction phases, diverse site entrances, and restoration commitments. Operators must plan for checkpoint sizes and failure recovery timelines rather than simply provisioning average bandwidth.

The analysis suggests operators should prepare for automated request loads at the edge while recognizing that the largest AI transfers will remain invisible to public routing tables.
