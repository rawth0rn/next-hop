---
title: "AWS PrivateLink adds tunnel endpoints for CIDR-based access"
date: 2026-11-09T07:49:13-08:00
summary: "AWS PrivateLink now supports accessing entire CIDR ranges through GENEVE-encapsulated tunnel endpoints."
tags: ["aws", "privatelink", "geneve", "vpc"]
source_type: engineering
sources:
  - "https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-tunnel-endpoints-for-private-access-to-network-segments/"
---

AWS PrivateLink [introduced tunnel endpoints](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-tunnel-endpoints-for-private-access-to-network-segments/) for private access to network segments, allowing vendors to reach entire Classless Inter-Domain Routing (CIDR) ranges in customer Virtual Private Clouds (VPCs) without enumerating individual resources.

Previously, AWS PrivateLink resource configurations identified single resources by IP address, domain name, or Amazon Resource Name (ARN). Providers had to create a configuration for each resource they wanted to share. The new CIDR-type resource configuration represents a network segment as one or more IPv4 or IPv6 ranges. Providers attach these to a resource gateway and share them through AWS Resource Access Manager (AWS RAM). Consumers create a tunnel endpoint in their VPC and configure a GENEVE device (RFC 8926) in a network namespace. The device encapsulates packets destined for the shared ranges and sends them to the tunnel endpoint on UDP port 6081. The endpoint removes the GENEVE header, translates the source address to the resource gateway, and forwards the packet into the provider VPC. Because the provider addresses exist only inside the tunnel, consumer and provider VPCs can use overlapping CIDR blocks.

This change matters for security scanning and analytics workloads that must reach resources customers create after the initial setup. A security scanner can now access every host in shared subnets, including hosts launched since the last scan, without requiring the customer to update the resource configuration. The tunnel also carries DNS queries to the provider's resolver at 169.254.168.253, allowing consumers to resolve names in the provider's Amazon Route 53 private hosted zones. This solves naming conflicts when one consumer VPC serves multiple providers.

There are constraints. Application traffic must use TCP. DNS is the only supported UDP traffic, and ICMP is not supported. Connections must initiate from the consumer side. The tunnel endpoint and resource gateway must share at least one Availability Zone. IP fragments are dropped.
