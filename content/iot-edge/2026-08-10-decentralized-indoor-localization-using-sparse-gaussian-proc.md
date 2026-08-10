---
title: "Decentralized Indoor Localization Using Sparse Gaussian Processes on IoT Devices"
date: 2026-08-10T07:08:00-07:00
summary: "A sparse Gaussian process model enables real-time localization training directly on IoT devices."
tags: ["localization", "edge-computing", "gaussian-process", "iot"]
source_type: research
sources:
  - "https://arxiv.org/abs/2409.00078"
---

Researchers posted a [preprint](https://arxiv.org/abs/2409.00078) to arXiv describing a decentralized indoor localization framework that runs Sparse Gaussian Process with Reduced-dimensional Inputs (SGP-RI) directly on Internet of Things (IoT) devices for smaller service areas.

The framework moves localization from centralized servers covering multistory buildings to individual IoT devices responsible for smaller zones. Each device runs an SGP-RI model, a sparse approximation of the standard Gaussian Process (GP) that reduces input dimensionality to fit within memory and compute constraints typical of edge hardware. This architecture enables real-time sensing and model retraining directly on the device. When the indoor electromagnetic environment shifts due to furniture moves, construction, or seasonal humidity changes, the device updates its local model immediately without waiting for a central server to aggregate fingerprints from across the entire deployment and retrain a global model.

The authors tested the approach using both a multibuilding, multifloor static database and a single-building, single-floor dynamic database. The SGP-RI model trained on less than half the samples achieved localization accuracy comparable to a standard GP trained on the full dataset. This indicates the sparse approximation preserves precision while reducing memory and processing requirements.

For network operators, the shift addresses two operational pain points. Centralized systems require expensive updates to fingerprint databases and global model retraining to adapt to time-varying indoor electromagnetic environments. They also concentrate risk, as a breach of the central server exposes the entire deployment. Running SGP-RI at the edge reduces update latency, limits the blast radius of compromised credentials, and cuts the storage and transmission overhead for initial site surveys due to the reduced training sample requirement. The approach trades centralized scale for local adaptability.

The work remains a preprint on arXiv and has not yet undergone peer review.
