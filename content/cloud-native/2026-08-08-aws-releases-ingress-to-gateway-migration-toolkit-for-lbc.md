---
title: "AWS Releases Ingress-to-Gateway Migration Toolkit for LBC"
date: 2026-08-08T15:09:50-07:00
summary: "AWS shipped a toolkit to automate migration from Kubernetes Ingress to Gateway API for its load balancer controller."
tags: ["kubernetes", "gateway-api", "aws", "load-balancing"]
source_type: engineering
sources:
  - "https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-the-lbc-ingress-to-gateway-api-migration-toolkit/"
---

AWS released the [Ingress-to-Gateway API migration toolkit](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-the-lbc-ingress-to-gateway-api-migration-toolkit/) for the AWS Load Balancer Controller (LBC). The toolkit gives Kubernetes operators a guided path to convert Ingress resources to the Gateway API standard without hand-rewriting YAML.

The toolkit centers on `lbc-migrate`, a command-line interface (CLI) tool that translates LBC Ingress manifests into Gateway API equivalents. It reads existing Ingress, Service, and IngressClass definitions and emits HTTPRoute, Gateway, and GatewayClass resources. The tool handles annotations, path rules, and IngressGroup configurations automatically. It can read from static files or a live cluster using the `--from-cluster` flag. A dry-run mode stamps generated Gateways with `gateway.k8s.aws/dry-run: "true"`, letting the controller validate AWS resource modeling without provisioning an Application Load Balancer (ALB).

The toolkit also bundles Migration Console, a local web user interface (UI) launched via `lbc-migrate --console`. It offers a read-only, side-by-side comparison of Ingress and proposed Gateway configurations for teams that prefer visual review over command-line interface (CLI) output.

The Kubernetes project froze the Ingress API in March 2026. It remains stable but receives no new features. The Gateway API is now the recommended successor, offering typed Custom Resource Definitions (CRDs) with schema validation, first-class weighted traffic splitting, and cross-namespace routing through ReferenceGrant resources. Migrating by hand requires rewriting annotations, TLS configuration, and path rules, and errors can drop production traffic.

The toolkit mitigates that risk by running new ALBs in parallel with existing Ingress ALBs. Operators can validate behavior before cutting over DNS. The tool flags annotations it cannot translate fully, such as regex capture groups in URI rewrites, so nothing is missed. When the translation is clean, teams shift traffic on their own schedule and clean up the old Ingress resources only after sustained, error-free operation.
