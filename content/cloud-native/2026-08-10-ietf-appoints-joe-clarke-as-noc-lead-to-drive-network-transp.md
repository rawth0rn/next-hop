---
title: "IETF appoints Joe Clarke as NOC Lead to drive network transparency"
date: 2026-08-10T07:23:08-07:00
summary: "Joe Clarke appointed IETF NOC Lead, prioritizing real-time network dashboards and operational transparency."
tags: ["ietf", "noc", "observability", "automation"]
source_type: research
sources:
  - "http://www.ietf.org/blog/meet-our-new-ietf-noc-lead/"
---

[Joe Clarke has been appointed](http://www.ietf.org/blog/meet-our-new-ietf-noc-lead/) as the new Internet Engineering Task Force (IETF) Network Operations Center (NOC) Lead. His appointment marks a return to volunteer management for the team that builds and operates the network supporting IETF meetings. Clarke previously co-chaired the Operations and Management Area Working Group (opsawg) and served as a reviewer for the Operations (OPS) Directorate.

Clarke outlined immediate priorities starting with IETF 127 in San Francisco. The first is expanding network transparency through a dashboard landing page unveiled at IETF 126 in Vienna. The dashboard displays real-time statistics including general network metrics and current user counts. The team recently added Explicit Congestion Notification (ECN) monitoring after a community request. The underlying infrastructure runs IPv6 Mostly (Request for Comments (RFC) 8925) on the main service set identifier (SSID) alongside WiFi 7 access points. The NOC also maintains production deployments of Resource Public Key Infrastructure (RPKI) per RFC 8210 and DNS-Based Authentication of Named Entities (DANE) per RFC 6698, plus filtering per Best Current Practice (BCP) 38. Clarke noted the network sits in the critical path for meeting success, meaning failures directly impact the organization’s ability to function. The team fosters experiments on technologies such as Media Access Control (MAC) address randomization from the madinas Working Group and brings findings back to the IETF through documents or working group discussions.

For operators running cloud-native infrastructure, the IETF NOC functions as a high-stakes production environment supporting thousands of users with minimal tolerance for failure. Clarke’s emphasis on real-time dashboards offers a practical model for observability that practitioners can adapt to data center and cloud operations. The deployment of IPv6 Mostly and WiFi 7 at conference scale provides empirical performance data under realistic load conditions. The team is also experimenting with an AI agent to assist with meeting network deployments, signaling potential automation patterns for future operational workflows. Clarke is recruiting volunteers to build a talent pipeline, ensuring redundancy and fresh perspectives for the long term health of the operation.
