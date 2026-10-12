---
title: "Meshery reaches CNCF incubation as infrastructure management plane"
date: 2026-10-12T07:27:27-07:00
summary: "Meshery advances to CNCF incubating status as a unified cloud native management plane."
tags: ["service-mesh", "kubernetes", "infrastructure-management", "cncf"]
source_type: engineering
sources:
  - "https://www.cncf.io/blog/2026/10/07/meshery-becomes-a-cncf-incubating-project/"
---

The Cloud Native Computing Foundation (CNCF) Technical Oversight Committee has voted to accept [Meshery](https://www.cncf.io/blog/2026/10/07/meshery-becomes-a-cncf-incubating-project/) as an incubating project. Meshery is an open source platform that functions as a unified management plane for Kubernetes and cloud native infrastructure, giving engineering teams single-pane control over service mesh lifecycle, configuration, and performance rather than maintaining separate toolchains for each environment.

Originally created by Layer5 in 2019, Meshery pairs a central server with MeshSync for continuous cluster state discovery, a NATS-based broker for event streaming, and extension points including Adapters for technology-specific management. The architecture supports over 300 integrations spanning AWS, Google Cloud, and Azure services beyond Kubernetes. Since entering the CNCF sandbox in June 2021, the project has become the fifth highest-velocity project in the foundation by code commits, with a 350 percent increase in commits during the one-year period ending July 2026. The codebase now ranks as the fourth largest in the CNCF.

For network operators, Meshery addresses the operational gap created by AI-generated configuration changes. The platform treats infrastructure as design, rendering configuration changes as visual models before deployment to expose blast radius and misconfiguration. A new Meshery MCP Server provides AI assistants with governed, read-only access to the Registry and cluster state, while human reviewers validate changes through visual diffs in GitOps workflows. This matters because syntactically valid but semantically dangerous configurations can propagate at machine speed without oversight layers, and Meshery provides the governance checkpoint to catch drift before it reaches production.

The project has split into two GitHub organizations to manage its ecosystem: meshery for core components and meshery-extensions for community integrations. With 7,065 contributors and nearly 15,000 GitHub stars, Meshery now offers the Certified Meshery Contributor program to validate expertise. The roadmap includes expanded multi-cluster fleet management with Kubernetes role-based access control (RBAC) integration and broader performance testing capabilities.
