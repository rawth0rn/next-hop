---
title: "AWS Client VPN adds device posture assessment with Cedar policies"
date: 2026-11-09T07:48:16-08:00
summary: "AWS Client VPN now enforces device health policies written in Cedar continuously throughout sessions."
tags: ["aws", "vpn", "cedar", "device-posture"]
source_type: engineering
sources:
  - "https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-device-posture-assessment-for-aws-client-vpn/"
---

AWS Client VPN [added device posture assessment](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-device-posture-assessment-for-aws-client-vpn/), letting operators write Cedar policies that grant tunnel access only to devices meeting health requirements. The feature evaluates these policies at connection time and re-evaluates them approximately every five minutes for the life of the session.

Device trust providers supply signed tokens containing compliance attributes. At launch, supported providers are CrowdStrike on Windows and macOS, Jamf on macOS, and JumpCloud on Windows, macOS, and Ubuntu. You register a provider on the Client VPN endpoint with the new device-posture-options parameter, available on both create-client-vpn-endpoint and modify-client-vpn-endpoint. You then write a Cedar policy that references both device attributes and user identity. The AWS VPN Client reads the token from the provider's local agent and sends it with the connection request. Client VPN verifies the signature and tenant match before evaluating the policy. The client sends refreshed tokens periodically, and if a device falls out of compliance, the session disconnects at the next evaluation. Shadow mode lets you test policies against live traffic without blocking connections, logging decisions to Amazon CloudWatch until you are ready to enforce.

For operators, this replaces the previous pattern of using AWS Lambda functions in client connect handlers to check device state once at connect time. Continuous evaluation closes the gap between initial connection and session lifetime, stopping traffic from compromised or unmanaged devices without waiting for a manual sweep. If the provider agent stops or becomes unreachable, Client VPN retains the last attributes for up to 15 minutes before re-evaluating the policy without device claims. Because Cedar policies coexist with existing authorization rules, you can migrate checks gradually rather than rewriting access controls all at once. The feature requires AWS VPN Client version 6.2.0 or later and incurs no additional charge beyond standard Client VPN pricing.
