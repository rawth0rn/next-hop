---
title: "AWS Ships Cloud WAN Flow Logs for Global Traffic Monitoring"
date: 2026-11-16T07:36:02-08:00
summary: "AWS Cloud WAN Flow Logs capture flow records at the core network, edge, and attachment levels, enabling global traffic analysis without per-VPC correlation."
tags: ["cloud-wan", "flow-logs", "network-monitoring", "aws"]
source_type: engineering
sources:
  - "https://aws.amazon.com/blogs/networking-and-content-delivery/monitoring-global-traffic-with-aws-cloud-wan-flow-logs/"
---

AWS shipped [AWS Cloud WAN Flow Logs](https://aws.amazon.com/blogs/networking-and-content-delivery/monitoring-global-traffic-with-aws-cloud-wan-flow-logs/), a feature that captures flow records at the core network, edge, and attachment scopes. Until now, operators who wanted visibility into global traffic had to enable Amazon VPC Flow Logs in every Virtual Private Cloud and correlate the records manually. Traffic between hybrid attachments, including AWS Direct Connect, AWS Site-to-Site VPN, and Connect attachments, never traversed a VPC, so VPC Flow Logs could not capture it.

You create flow logs at one of three scopes. A core network scope captures all traffic crossing the core network. An edge scope captures flows through attachments in a specific AWS Region. An attachment scope captures flows for a single attachment. Each record includes the source and destination Region, segment, and attachment identifier. The default format delivers 42 space-separated fields, though you can specify a custom format to capture only the AWS Cloud WAN context fields you need. You can publish logs to Amazon CloudWatch Logs, Amazon Simple Storage Service, or Amazon Data Firehose, then analyze them with Amazon Athena or CloudWatch Logs Insights.

The records expose details that VPC Flow Logs cannot. They show which inspection attachment a flow passed through when using service insertion. With 1:1 network address translation (NAT), the logs include both the original and translated addresses. When AWS Cloud WAN drops a packet, the record states why, distinguishing between no-route, blackhole, and time to live (TTL) expired drops.

For operators, this removes the operational burden of managing and correlating dozens or hundreds of VPC Flow Logs across accounts and Regions. You gain visibility into traffic between on-premises sites and cloud resources that bypass VPCs entirely, including Direct Connect and VPN attachments. The drop reasons let you pinpoint routing issues without guessing, showing exactly where traffic hits a blackhole or exceeds its TTL. You manage all flow logs from the AWS Cloud WAN home Region, us-west-2 for commercial partitions, and records typically arrive within about ten minutes after the initial provisioning delay.
