---
title: "NetMon Hybrid Monitoring Detects 5G Core Faults in Seconds"
date: 2026-09-14T07:48:21-07:00
summary: "Researchers propose NetMon, a hybrid eBPF and active probing system for early fault detection in Kubernetes-based 5G cores."
tags: ["ebpf", "5g", "kubernetes", "monitoring"]
source_type: research
sources:
  - "https://arxiv.org/abs/2609.12649"
---

Researchers published a [preprint on arXiv](https://arxiv.org/abs/2609.12649) describing NetMon, a hybrid monitoring system designed for Kubernetes-based 5G packet core deployments. The paper, "Hybrid Monitoring for Early Fault Detection in Cloud-Native 5G Systems," presents evaluation results from Ericsson Access and Mobility Management Function (AMF) clusters running production traffic patterns. The work targets the specific observability gaps in cloud-native 5G infrastructure.

NetMon combines extended Berkeley Packet Filter (eBPF) based passive kernel-level observation with active TCP probing and centralized correlation. The eBPF component instruments the kernel to observe traffic without modifying application code, capturing granular telemetry on latency and packet loss from the network stack directly. Active probes run synthetic TCP transactions to verify path health even when user plane traffic is absent or routes are idle. A central analyzer ingests both data streams to correlate events and attribute faults to specific pods, nodes, or network segments with second-level granularity, distinguishing between application and network issues.

The evaluation demonstrates detection of degradation as subtle as 10ms added latency or 5 packet loss within seconds of onset. Standard Kubernetes health checks only report binary up or down states, which misses partial degradation like intermittent packet loss or latency spikes that precede hard failures. Scrape-based metrics systems typically batch data in thirty-second or one-minute intervals, introducing detection delays measured in tens of seconds. Purely passive monitoring cannot confirm whether idle backup paths are functional or degraded. NetMon addresses these gaps by maintaining continuous visibility into both active traffic flows and standby infrastructure components without modifying the 5G core applications.

The system sustains this detection capability under application loads up to 50 simulated User Equipment (UE). Resource overhead remains low at 34 millicores CPU and 45 MiB memory per pod. This footprint suggests operators could deploy NetMon as a sidecar or daemonset without impacting the monitored workload performance or requiring additional hardware nodes.

For teams operating cloud-native 5G infrastructure, the approach offers a method to catch network degradation before it affects subscriber service quality. The hybrid architecture provides the component-level localization necessary to reduce mean time to resolution during incidents.
