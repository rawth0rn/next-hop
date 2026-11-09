---
title: "AWS documents mTLS over QUIC using NLB passthrough and EKS"
date: 2026-11-09T07:50:41-08:00
summary: "AWS published a pattern for terminating mutual TLS on EKS pods behind a Network Load Balancer forwarding QUIC traffic."
tags: ["quic", "mtls", "eks", "nlb"]
source_type: engineering
sources:
  - "https://aws.amazon.com/blogs/networking-and-content-delivery/securing-autonomous-fleet-communications-at-scale-with-mtls-over-quic-using-network-load-balancer-passthrough/"
---

AWS published a [reference implementation](https://aws.amazon.com/blogs/networking-and-content-delivery/securing-autonomous-fleet-communications-at-scale-with-mtls-over-quic-using-network-load-balancer-passthrough/) for terminating mutual transport layer security (mTLS) over QUIC on Amazon Elastic Kubernetes Service (EKS) behind a Network Load Balancer in passthrough mode, targeting latency-sensitive autonomous fleets that operate across cellular networks.

The architecture forwards QUIC packets through the Network Load Balancer without terminating transport layer security, allowing backend pods running on EKS to handle the full mutual transport layer security exchange including client certificate verification. The AWS Load Balancer Controller provisions the Network Load Balancer and target group, then injects a unique Server ID into each pod via the AWS_LBC_QUIC_SERVER_ID environment variable. The QUIC server implementation, using quic-go, reads this variable and places the decoded 8-byte value at bytes 1 through 8 of every Connection ID it generates. Because the Network Load Balancer routes packets based on this Connection ID, sessions persist through cellular handoffs that change client IP addresses, avoiding the reconnects that transmission control protocol would require.

For fleets such as Zipline's delivery drones, which stream telemetry across multiple continents through constantly changing cellular networks, transmission control protocol forces a reconnect and transport layer security renegotiation during every cell tower handoff, adding latency to critical communications. Shared-secret authentication schemes present operational challenges when managing unique credentials across thousands of devices, and fleet-wide shared credentials create security risks. This pattern replaces shared secrets with mutual transport layer security certificates issued through AWS Private Certificate Authority, giving each device a cryptographic identity that operators can revoke individually without rotating credentials across the entire fleet, while QUIC's Connection ID maintains transport continuity during network transitions.

The deployment uses standard Kubernetes workflows with the AWS Load Balancer Controller, requiring only namespace labels, pod annotations for Server ID injection, and Service annotations to create a TCP_QUIC listener on port 443 that handles both user datagram protocol traffic and transmission control protocol health checks.
