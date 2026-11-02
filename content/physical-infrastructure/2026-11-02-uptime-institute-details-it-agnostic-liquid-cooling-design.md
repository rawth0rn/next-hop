---
title: "Uptime Institute details IT-agnostic liquid cooling design"
date: 2026-11-02T07:50:00-08:00
summary: "Uptime Institute publishes guidance on designing shared direct liquid cooling infrastructure for multi-vendor environments."
tags: ["liquid-cooling", "data-center", "ai-infrastructure", "cooling-systems"]
source_type: research
sources:
  - "https://journal.uptimeinstitute.com/it-agnostic-dlc-systems-key-considerations/"
---

Uptime Institute published ["IT-agnostic DLC systems: key considerations"](https://journal.uptimeinstitute.com/it-agnostic-dlc-systems-key-considerations/) in its journal, providing guidance on designing direct liquid cooling (DLC) infrastructure that supports hardware from multiple vendors within a single shared secondary fluid network (SFN). The report addresses the fragmentation in DLC specifications that currently forces operators into vendor-specific silos.

Material compatibility and coolant quality stand out as immediate technical barriers. While high-quality water coolants such as propylene-glycol mix (PG25) or deionized water work technically with wetted components across major IT vendors, each requires correct additive packages to inhibit corrosion and biological growth. Operators must maintain updated wetted material lists with all vendors and consult Open Compute Project (OCP) guidelines. Commissioning requires strict hygiene protocols, including testing for turbidity and pH against retained factory samples before connecting new equipment to the SFN.

Filtration follows the 25 micron industry standard, usually implemented via full-flow filters in coolant distribution units (CDUs). For multi-megawatt networks, side-stream filtration helps protect CDU filters and maintain fluid quality.

Physical design must accommodate heterogeneous rack configurations. Row-level SFN headers need densely spaced connection points to support varying manifold positions and rack widths. For high-density AI computing, DN65/2.5-inch rack connections are recommended as a minimum, with fluid velocity limited to 2 meters per second to prevent erosion. Adjustable or automated valves enable flow modulation to balance cooling across racks with differing power densities and pressure drops.

An IT-agnostic approach matters because it prevents commercial lock-in and reduces operational complexity as facilities cycle through multiple hardware generations. Shared infrastructure eliminates the need to rebuild cooling systems for each IT refresh, critical for scaling AI compute where densities vary widely. The guidance also notes that achieving concurrent maintainability often requires dividing headers into sections with isolation valves, as not all IT racks ship with redundant manifolds.

The report draws on operator briefings and input from Vertiv and Schneider Electric.
