---
title: "EARI-MAC: Energy-Aware MAC for IoT Harvesting"
date: 2026-10-12T07:25:29-07:00
summary: "A preprint proposes EARI-MAC, a receiver-initiated MAC protocol that adapts to both stored energy and real-time harvesting power for IoT devices."
tags: ["iot", "mac-protocol", "energy-harvesting", "wireless"]
source_type: research
sources:
  - "https://arxiv.org/abs/2610.11492"
---

A [preprint on arXiv](https://arxiv.org/abs/2610.11492) introduces EARI-MAC, an energy-aware receiver-initiated Medium Access Control (MAC) protocol designed for Internet of Things (IoT) devices that harvest energy from their environment. The paper, titled "Energy-Aware Receiver-initiated MAC Protocol for Energy Harvesting IoT" and posted to the cs.NI category, presents a method to extend operational autonomy by adjusting the receiver's duty cycle based on both stored energy and current harvesting power.

Most existing MAC protocols for energy-harvesting IoT devices rely only on stored battery energy to make decisions. This approach can interrupt device operation when energy harvesting is low, blocking ongoing tasks. EARI-MAC uses a mathematical formulation that considers both the battery level and the real-time harvesting power. This dual approach keeps receivers running during scarce energy periods and boosts performance when energy is plentiful. The protocol operates in receiver-initiated mode, where the receiver triggers communication when ready, which naturally suits scenarios where receiving costs more than transmitting.

The researchers evaluated EARI-MAC through simulation using three days of real solar data recorded in Novi Sad. They compared it against QPPD-MAC and an energy-unaware MAC protocol. Simulation results demonstrate that EARI-MAC improves packet delivery ratio and network throughput by more than 10 percent. It also reduces receiver energy consumption by 5.6 percent compared to QPPD-MAC and 8.2 percent compared to the energy-unaware protocol. Energy consumption per bit drops by 9.6 percent and 13.9 percent respectively.

For network operators deploying solar-powered IoT sensors or edge devices, these gains translate to more reliable data collection and longer operational intervals without manual intervention. The protocol's ability to adapt to real-time harvesting conditions means devices can maintain network participation even during cloudy periods or variable indoor lighting. This directly extends autonomy without requiring larger batteries or hardware changes, making it relevant for remote agricultural sensors, industrial monitoring, and urban low-power wide-area networks where consistent uptime matters more than peak throughput.
