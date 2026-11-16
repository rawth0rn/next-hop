---
title: "Amazon VPC Lattice Bridges JWT and SigV4 for External gRPC"
date: 2026-11-16T07:34:22-08:00
summary: "AWS published a reference architecture for authenticating external gRPC clients through VPC Lattice by translating JWT claims to SigV4 signatures."
tags: ["grpc", "jwt", "sigv4", "vpc-lattice"]
source_type: engineering
sources:
  - "https://aws.amazon.com/blogs/networking-and-content-delivery/authenticate-external-grpc-clients-with-amazon-vpc-lattice/"
---

AWS published a [reference architecture](https://aws.amazon.com/blogs/networking-and-content-delivery/authenticate-external-grpc-clients-with-amazon-vpc-lattice/) that authenticates external gRPC clients through Amazon VPC Lattice by bridging JSON Web Tokens (JWT) to AWS Signature Version 4 (SigV4) while preserving end-to-end HTTP/2 framing. The solution addresses the gap between external identity providers that issue JWTs and Amazon VPC Lattice's native SigV4 authentication model.

The architecture deploys an Application Load Balancer (ALB) with jwt-validation actions to verify RS256-signed access tokens from Amazon Cognito or other OpenID Connect providers. When validation succeeds, the ALB forwards requests over TLS to an Amazon Elastic Container Service (Amazon ECS) proxy tier running on AWS Fargate. The proxy extracts claims including client_id, scope, and sub from the validated JWT payload, then maps these to stable HTTP headers x-client-id, x-client-scope, and x-client-sub that Amazon VPC Lattice auth policies can evaluate. The proxy removes the original authorization header containing the Bearer token and signs outbound requests with SigV4 using its Amazon ECS task role credentials. These identity headers remain in the SignedHeaders list, ensuring they cannot be modified in transit.

Amazon VPC Lattice resolves the SigV4 signature to the task role's AWS Identity and Access Management (AWS IAM) principal and enforces per-service authorization through IAM policies attached to individual services. This creates a trust boundary where external OAuth 2.0 identity translates to internal AWS identity without exposing AWS credentials to external clients. The architecture maintains gRPC over HTTP/2 from client to backend by configuring ALB target groups with Protocol HTTPS and ProtocolVersion HTTP/2, ensuring the gRPC framing remains intact across the ALB and proxy layers. The implementation demonstrates two SigV4 signing approaches: native AWS SDK signing and an Envoy proxy filter, with each mapped to distinct backend services to demonstrate how IAM policies can distinguish between workload identities.

For operators running gRPC workloads, this pattern solves the identity federation challenge without terminating gRPC at the edge. It moves JWT validation to the ALB, keeping proxy logic simple and preventing invalid requests from consuming backend compute. The approach enables granular IAM policies that restrict which external client scopes can reach specific internal APIs based on the translated header claims, while preserving end-to-end HTTP/2 framing for gRPC compatibility.
