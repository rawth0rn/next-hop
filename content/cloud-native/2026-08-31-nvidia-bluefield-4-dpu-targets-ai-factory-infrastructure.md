---
title: "NVIDIA BlueField-4 DPU Targets AI Factory Infrastructure"
date: 2026-08-31T07:37:54-07:00
summary: "NVIDIA BlueField-4 DPU accelerates north-south infrastructure for agentic AI factories."
tags: ["dpu", "ai-networking", "infrastructure", "bluefield"]
source_type: engineering
sources:
  - "https://developer.nvidia.com/blog/nvidia-bluefield-4-powers-new-scale-in-network-infrastructure-for-agentic-ai-factories/"
---

NVIDIA [announced](https://developer.nvidia.com/blog/nvidia-bluefield-4-powers-new-scale-in-network-infrastructure-for-agentic-ai-factories/) BlueField-4 as the data processing unit (DPU) powering Scale-In network infrastructure, a new domain for securing and managing north-south traffic into agentic AI factories.

Scale-In represents the fifth pillar of NVIDIA AI networking, complementing Scale-Up GPU interconnects, Scale-Out server fabrics, Scale-Across data center links, and Context Memory storage. While traditional cloud infrastructure relied on software-defined networking running on host central processing units (CPUs), agentic AI factories require dedicated acceleration to handle multi-terabit access paths without consuming compute resources meant for AI workloads.

BlueField-4 provides host-independent processing that sits outside the tenant host domain. It combines programmable control-plane logic with inline data-path engines that enforce policies locally without returning work to the CPU. In the Vera Rubin NVL72 platform, ConnectX-9 SuperNICs carry tenant workload traffic over the Scale-Out network while BlueField-4 manages infrastructure services including security policy, telemetry, and storage access. BlueField Astra extends this control into the east-west fabric, synchronizing encryption and isolation policies across both network domains.

The DPU offers 4x the memory bandwidth and 2x the network bandwidth of BlueField-3, supporting more concurrent services and larger policy datasets. NVIDIA DOCA provides the software layer, with containerized microservices for networking, security, and telemetry running directly on the DPU. Spectrum-X Ethernet connects the Scale-In fabric to external storage and data sources.

For network operators, Scale-In moves security enforcement and infrastructure management into silicon that tenants cannot bypass or disable. This architecture prevents infrastructure services from becoming bottlenecks as AI compute scales, while preserving host CPU cycles for AI workloads. Operators gain consistent control over access, data movement, and tenant isolation across both north-south entry points and east-west server traffic without routing all flows through a single chokepoint.
