---
title: "Cilium 1.20 graduates Multi Pool IPAM to stable"
date: 2026-08-08T15:07:04-07:00
summary: "Cilium 1.20 promotes Multi Pool IPAM from beta to stable for production Kubernetes clusters."
tags: ["cilium", "kubernetes", "ipam"]
source_type: engineering
sources:
  - "https://isovalent.com/blog/post/cilium-1-20/?utm_medium=referral&utm_campaign=cilium-blog"
---

Cilium 1.20 [graduates Multi Pool IP Address Management (IPAM) to stable status](https://isovalent.com/blog/post/cilium-1-20/?utm_medium=referral&utm_campaign=cilium-blog), moving the feature from beta to production-ready for Kubernetes clusters.

Multi Pool IPAM allows operators to define multiple distinct IP address pools within a single cluster. This lets you segregate pod addressing by workload type, node pool, or failure domain. For example, you can allocate one Classless Inter-Domain Routing (CIDR) block for general workloads and another for database or storage traffic that requires specific network segmentation or firewall rules. The stable designation means the API is now frozen and covered by long-term support guarantees, removing the deprecation risk and breaking change potential that accompanies beta features.

For network operators, this solves IP exhaustion problems that occur when a single large CIDR fills up during cluster growth. Instead of renumbering or expanding a monolithic prefix, you add new pools and assign them to specific node groups or namespaces. The allocation logic respects pool boundaries during pod scheduling, ensuring workloads land on nodes with available addresses from the correct range. This maps cleanly to existing network security zones and simplifies compliance with segmentation policies. The feature also supports distinct pools for different availability zones, preventing address starvation in one zone from affecting others. You can define pools statically or through Cilium's operator automation, depending on your infrastructure tooling.

Moving from beta to stable indicates the feature is ready for production workloads without the caveats of experimental code. Operators who previously tested Multi Pool IPAM can now deploy it with standard support guarantees. This is particularly valuable in regulated environments where network segmentation is mandatory and API stability is required for audit trails.

The release also introduces ENI IPAM for IPv6, Gateway API ExternalAuth, and TCPRoute/UDPRoute support. However, the stabilization of Multi Pool IPAM addresses immediate production readiness concerns for large-scale deployments.
