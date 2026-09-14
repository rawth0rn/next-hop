---
title: "Cilium 1.20 Adds ENI IPv6 Support on AWS"
date: 2026-09-14T07:45:55-07:00
summary: "Cilium 1.20 graduates ENI IPAM IPv6 support to beta, enabling dual-stack pods with VPC-routable addresses on AWS."
tags: ["cilium", "ipv6", "eni", "kubernetes"]
source_type: engineering
sources:
  - "https://www.cncf.io/blog/2026/09/14/cilium-1-20-gateway-api-externalauth-tcproute-udproute-eni-ipam-for-ipv6-and-more/"
---

Cilium 1.20 graduates ENI IPAM IPv6 support to beta, closing a feature gap that had persisted for four years since the initial request. The release, detailed in a [CNCF blog post](https://www.cncf.io/blog/2026/09/14/cilium-1-20-gateway-api-externalauth-tcproute-udproute-eni-ipam-for-ipv6-and-more/), enables pods on AWS Elastic Kubernetes Service (EKS) to receive routable IPv6 addresses directly from the Virtual Private Cloud (VPC) through the same Elastic Network Interface (ENI) mechanism that already handles IPv4.

ENI IP Address Management (IPAM) mode is the AWS-specific approach that allocates real VPC addresses to pods instead of using overlay networking. The IPv6 implementation uses Prefix Delegation to attach a /80 IPv6 prefix to each node’s ENI. The Cilium agent then assigns individual addresses from that prefix to pods. This approach mirrors the IPv4 implementation and maintains the same performance characteristics and operational model.

The configuration is straightforward. You enable ENI mode, enable IPv6, and set the IPAM mode to ENI. The YAML looks like this:

ipam:
  mode: eni
eni:
  enabled: true
ipv6:
  enabled: true

Once applied, pods boot with dual-stack addressing. The example output shows the result:

NAME                              IPS
dualstack-demo-7f8876746b-5xvnk   192.168.128.71,2a05:d01c:38d:4c02:909e::e771
dualstack-demo-7f8876746b-8lj6z   192.168.177.118,2a05:d01c:38d:4c00:1cf5::57d1

The IPv6 address from the first pod comes directly from the /80 prefix delegated to that node’s ENI, which you can verify in the AWS console. You will see the prefix attached to the worker node’s network interface.

Datadog engineers built this feature. Their contribution is significant because it finally delivers feature parity across IPv4 and IPv6 for ENI mode. As the maintainers note, it even renders a footnote in Chapter 4 of Cilium: Up and Running obsolete, though they express mild disappointment at the book aging so quickly after publication.

For practitioners running EKS clusters, this beta feature means you can adopt IPv6 without sacrificing the benefits of ENI mode. Pods get real, VPC-routable addresses in both families. The operator handles Prefix Delegation automatically. You avoid the operational complexity of maintaining separate networking paths for IPv4 and IPv6. The feature also sets the stage for IPv6-only clusters in the future, though that remains a separate discussion.

The beta status means you should test thoroughly before production deployment, but the implementation is complete enough for serious evaluation. The four-year development timeline suggests the feature was not rushed. Check the documentation for current limitations and upgrade considerations. You should also verify that your AWS VPC and subnet configurations support IPv6 Prefix Delegation before enabling this feature.
