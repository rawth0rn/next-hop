---
title: "AWS adds cross-account canary routing with VPC Lattice and API Gateway"
date: 2026-10-12T07:25:59-07:00
summary: "AWS combines API Gateway canary releases with VPC Lattice to route precise traffic slices across accounts during microservice migrations."
tags: ["aws", "vpc-lattice", "api-gateway", "canary"]
source_type: engineering
sources:
  - "https://aws.amazon.com/blogs/networking-and-content-delivery/cross-account-canary-routing-with-amazon-vpc-lattice-and-amazon-api-gateway/"
---

AWS introduced cross-account canary routing that combines Amazon API Gateway canary releases with Amazon VPC Lattice service networking to shift precise traffic slices across AWS accounts during microservice migrations [source](https://aws.amazon.com/blogs/networking-and-content-delivery/cross-account-canary-routing-with-amazon-vpc-lattice-and-amazon-api-gateway/). The pattern addresses a gap in the strangler fig migration approach where teams place each new microservice in its own account for isolation but lack fine-grained traffic control across account boundaries.

The architecture rests on three layers. First, a central API Gateway in one account serves as the public entry point and owns the canary routing decision. The gateway uses its native stage canary feature to split traffic, for example sending 90 percent of requests to a monolith and 10 percent to a new payments service. Second, a forwarder Lambda function bridges API Gateway to VPC Lattice. API Gateway cannot invoke VPC Lattice endpoints directly because Lattice endpoints are only reachable from VPCs associated with the service network. The Lambda function reads a stage variable set by the canary decision and forwards the request to the corresponding Lattice service DNS name. Third, VPC Lattice provides the cross-account connectivity. Workload accounts share a Lattice service network, making services discoverable by managed DNS names without VPC peering or transit gateways.

A request flows through these layers in sequence. The client hits the public API Gateway endpoint. The gateway makes the per-request canary decision and sets a stage variable identifying the target service. It then invokes the forwarder Lambda, which runs in a VPC attached to the shared service network. The Lambda forwards the request to the appropriate Lattice service based on the stage variable. The split percentage lives entirely in the API Gateway stage configuration. Changing the canary weight or rolling back to zero requires updating a single parameter, taking effect on the next request.

This matters for operators because it decouples routing control from network plumbing. Each microservice under migration can have its own API Gateway with an independent canary percentage. A payments service might run at 30 percent while an orders service stays at 5 percent. Each gateway emits separate CloudWatch metrics, so monitoring and alarms map directly to the service being migrated. The shared Lattice service network absorbs new services without modification, and adding a service only requires deploying a lightweight API Gateway and forwarder Lambda.

The architecture requires a compute layer in a VPC to bridge API Gateway and Lattice. Lambda is the lightest option, but any VPC-attached compute works. The forwarder must sign requests with SigV4 if the target service enforces IAM authentication. The pattern assumes a shared VPC Lattice service network across accounts, which teams must configure through AWS Resource Access Manager.
