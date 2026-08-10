---
title: "NTT Docomo and Samsung validate individual-level AI-RAN optimization"
date: 2026-08-10T07:25:39-07:00
summary: "NTT Docomo and Samsung validated AI-RAN technology to optimize individual user experience and reduce service issues."
tags: ["ai-ran", "6g", "mobile-networks", "ran"]
source_type: press
sources:
  - "https://www.mobileworldlive.com/network-tech/samsung-ntt-add-a-personal-touch-to-ai-ran-tests/"
---

NTT Docomo and Samsung Electronics [validated AI-RAN technology](https://www.mobileworldlive.com/network-tech/samsung-ntt-add-a-personal-touch-to-ai-ran-tests/) that optimizes user experience at an individual level to cut service issues. The companies asserted the work represents an important step toward predictive architecture expected to be prevalent in sixth generation (6G) standards.

The tests examined how artificial intelligence applied to the Radio Access Network (RAN) can move beyond cell-wide optimization to target specific user devices. Rather than managing spectrum and power based on aggregate demand across a coverage area, the approach models individual channel conditions and service requirements. This granularity aims to prevent service issues before they affect the user by predicting degradation at the device level. The architecture shifts RAN control from reactive macro adjustments to proactive, per-user resource allocation. Such fine-grained management represents a departure from current massive MIMO techniques that optimize for groups of users within beamforming sectors.

For network operators, individual-level optimization introduces new operational requirements. Current RAN management tools aggregate metrics across sectors and cells to identify congestion or interference. A predictive architecture requires streaming telemetry from each user equipment to inference engines at the edge, changing where compute is placed and how faults are traced. When service issues occur, remediation must distinguish between systemic radio problems and specific user contexts, complicating troubleshooting workflows. The validation suggests 6G RAN planning must account for AI inference latency and training data governance at the access layer, not just in core analytics platforms. Engineers will need to integrate per-user prediction models with existing fault management systems.

The partners did not disclose commercial deployment timelines or specific performance metrics from the validation.
