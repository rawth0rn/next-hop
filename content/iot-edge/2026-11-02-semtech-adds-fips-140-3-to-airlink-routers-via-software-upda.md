---
title: "Semtech adds FIPS 140-3 to AirLink routers via software update"
date: 2026-11-02T07:40:50-08:00
summary: "Semtech enables FIPS 140-3 compliance on existing AirLink routers through a software update, avoiding hardware replacement for public safety fleets."
tags: ["fips 140-3", "public safety", "network security", "firmware"]
source_type: press
sources:
  - "https://iot-now.com/2026/10/26/159024-semtech-5g-network-slicing-fips-140-3-iacp-2026/"
---

Semtech [released AirLink OS 6.1](https://iot-now.com/2026/10/26/159024-semtech-5g-network-slicing-fips-140-3-iacp-2026/), enabling Federal Information Processing Standards (FIPS) 140-3 compliance on its XR90, XR80, and XR60 in-vehicle 5G routers through a software update with no hardware replacement required. The update addresses the September 2026 deadline when the National Institute of Standards and Technology (NIST) Cryptographic Module Validation Program (CMVP) moved all FIPS 140-2 certificates to its Historical List, rendering the older standard obsolete for new federal procurements.

The AirLink XR series routers provide primary connectivity for public safety fleets, including police cruisers, fire apparatus, and ambulances that rely on continuous links for computer-aided dispatch, live video streaming, and mobile data terminals. These vehicles operate on FirstNet, T-Mobile T-Priority, and Verizon Frontline network slices, which prioritize traffic during congestion, but the underlying hardware must still meet federal cryptography standards to protect sensitive operational data.

Previously, achieving FIPS 140-3 validation required agencies to purchase new hardware or replace cryptographic modules in existing routers. Semtech's approach applies the security updates across the installed base via firmware, preserving capital expenditure while ensuring compliance with the new mandate. The operating system also integrates with Palo Alto Networks Next-Generation Firewalls to support Zero Trust segmentation, addressing data security concerns raised by 64 percent of first responders in a recent T-Mobile survey.

For fleet administrators, Semtech's AirLink Management Service platform now includes configuration groups that enforce the FIPS 140-3 standard across specific device models. Administrators can verify compliance immediately across the entire fleet and identify units that deviate from the policy. AirLink Manager 2.18.1 extends these controls to on-premises deployments, allowing agencies to manage routers in cloud or air-gapped environments without sacrificing cryptographic integrity.

The software update eliminates the operational disruption of hardware refresh cycles solely for cryptographic compliance. Agencies can maintain continuity with existing XR series deployments while satisfying federal requirements for protected data in transit across public safety broadband networks.
