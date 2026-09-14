---
title: "eBPF/XDP-Based NIDS Architecture Trade-offs for DDoS Detection"
date: 2026-09-14T07:49:47-07:00
summary: "Research compares monolithic, Kafka, and gRPC architectures for an embedded DDoS detection system using eBPF/XDP on Raspberry Pi 5."
tags: ["ebpf", "xdp", "nids", "microservices"]
source_type: research
sources:
  - "https://arxiv.org/abs/2609.12605"
---

A preprint titled [A Feature-Rich Embedded NIDS with eBPF/XDP: Detector and Architecture Trade-offs](https://arxiv.org/abs/2609.12605) presents a Network Intrusion Detection System (NIDS) for Distributed Denial-of-Service (DDoS) detection that integrates eBPF/XDP packet filtering with three distinct software architectures, measuring the trade-offs between detection accuracy and transport overhead on resource-constrained hardware.

The paper, submitted to arXiv cs.NI and developed with Ericsson, describes a system that uses GoFlowMeter (an open-source Go implementation of CICFlowMeter) to extract flow features from network traffic. Detection relies on an Isolation Forest algorithm trained on these features, improving upon a statistical baseline by flagging low-volume attack windows that the baseline misses. The system leverages extended Berkeley Packet Filter (eBPF) and Express Data Path (XDP) to filter traffic at the kernel level.

The researchers compared three deployment patterns on a Raspberry Pi 5 testbed replaying the CIC-DDoS2019 dataset: a monolithic application, a Kafka-based microservice pipeline, and a Google Remote Procedure Call (gRPC)-based microservice architecture.

Detection quality depends mainly on the choice of detector rather than the transport mechanism. The Isolation Forest achieved a 0.965 F1 score in the monolithic variant. However, architecture choice introduces measurable latency. The gRPC-based approach reached nearly the same accuracy as the monolithic version while adding less than 2 milliseconds of transport time per window. In contrast, the asynchronous Kafka pipeline reduced accuracy by roughly nine percentage points and added approximately 27 milliseconds of latency.

These results clarify the overhead costs when deploying kernel-level packet processing on edge hardware. For operators running DDoS defense on constrained devices, gRPC offers a middle ground between the simplicity of monolithic deployment and the decoupling of message queues, without the latency penalty of Kafka.
