---
title: "AWS NLB listener rules route IPv4 and IPv6 by source IP type"
date: 2026-08-08T15:10:25-07:00
summary: "AWS Network Load Balancer now routes IPv4 and IPv6 clients to matching target groups with listener rules, preserving source IP without translation."
tags: ["aws", "load-balancer", "ipv6", "dual-stack"]
source_type: engineering
sources:
  - "https://aws.amazon.com/blogs/networking-and-content-delivery/consolidate-dual-stack-architectures-with-listener-rules-for-network-load-balancer/"
---

AWS announced [listener rules for Network Load Balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/consolidate-dual-stack-architectures-with-listener-rules-for-network-load-balancer/) that route connections based on source IP address type, letting a single dual-stack NLB send IPv4 clients to IPv4 targets and IPv6 clients to IPv6 targets without protocol translation.

Before this launch, a dual-stack NLB listener could only forward to target groups of one IP address family. If IPv6 clients reached IPv4 targets, the load balancer translated the connection and the target saw the load balancer's address, not the original client IP. Workarounds were to run two separate NLBs or enable Proxy Protocol version 2 and parse its headers on every target.

Listener rules evaluate the source IP address type at Layer 3 and forward matching traffic to a target group of the same family. Rules run in priority order, with lower numbers evaluated first. Traffic that matches no rule falls through to the listener's default action. A typical configuration uses two rules: one for IPv4 sources to an IPv4 target group, and one for IPv6 sources to an IPv6 target group.

The feature requires a dual-stack NLB with IPv6 CIDR blocks on the VPC and subnets. You create separate target groups for each address family, then add rules via the AWS CLI version 2.35.24 or newer, or through the console. Rules support TCP, UDP, and TLS listeners, and you can use weighted target groups for gradual migrations.

Running one NLB instead of two cuts hourly and LCU charges in half for the front-end tier. It also eliminates the need to deploy and maintain Proxy Protocol parsing across the fleet. Security groups, network ACLs, and VPC Flow Logs now show the actual client IP for both IPv4 and IPv6 connections, which satisfies compliance requirements that depend on end-to-end source IP preservation.

For teams running separate IPv4 and IPv6 NLBs, migration is straightforward. Create a dual-stack NLB with the two rules, validate the traffic split using per-target-group CloudWatch metrics, then update DNS to point both A and AAAA records at the consolidated NLB. After connections drain, decommission the old load balancers.

The feature works with existing NLB capabilities including cross-zone load balancing, sticky sessions, and TLS termination. Two separate NLBs still provide fault isolation per address family, so evaluate availability requirements before consolidating.
