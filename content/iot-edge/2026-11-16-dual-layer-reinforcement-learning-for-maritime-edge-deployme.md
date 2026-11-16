---
title: "Dual-Layer Reinforcement Learning for Maritime Edge Deployment"
date: 2026-11-16T07:28:21-08:00
summary: "Researchers propose a dual-layer reinforcement learning framework to optimize unmanned surface vehicle deployment for maritime edge computing."
tags: ["edge-computing", "maritime-networks", "reinforcement-learning", "usv"]
source_type: research
sources:
  - "https://arxiv.org/abs/2611.17779"
---

A preprint on [arXiv](https://arxiv.org/abs/2611.17779) proposes a Dual-Layer Reinforcement Learning (DLRL) framework to optimize deployment of Unmanned Surface Vehicles (USVs) for mobile edge computing in maritime wireless networks.

The paper addresses resource management in Internet of Vessels (IoV) environments where USVs act as mobile edge nodes. These vessels provide computation and storage services to maritime users, complementing distant cloud infrastructure. The researchers formulate the optimization as a mixed-integer nonlinear program that minimizes expected response time by jointly optimizing USV positions and computation offloading decisions. Solving this problem directly is difficult because it combines continuous spatial variables with discrete assignment variables.

The DLRL framework splits the optimization across two layers to handle this complexity. In the outer layer, a Deep Deterministic Policy Gradient (DDPG) algorithm determines the continuous spatial deployment of USVs. In the inner layer, a Q-learning algorithm makes discrete decisions about which computation tasks to offload to the edge versus process locally on user devices. This architecture separates the physical positioning problem from the logical resource allocation problem while allowing them to converge on a coordinated solution.

For network operators, maritime edge computing presents unique deployment challenges. Ships and offshore platforms move constantly, requiring compute nodes to relocate rather than remain at fixed base stations. Joint optimization of where to place mobile infrastructure and how to route computation has been computationally expensive to solve in real time. The proposed approach offers a near-optimal solution that converges faster than direct methods, which matters when vessels drift and channel conditions change. The numerical results demonstrate the method outperforms existing algorithms that handle only continuous or only discrete variables, suggesting practical latency reductions for maritime applications.

The paper is available as a preprint on arXiv.
