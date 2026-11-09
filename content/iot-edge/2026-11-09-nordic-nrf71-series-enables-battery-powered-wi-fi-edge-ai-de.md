---
title: "Nordic nRF71 Series enables battery-powered Wi-Fi edge AI devices"
date: 2026-11-09T07:32:43-08:00
summary: "Nordic Semiconductor released the nRF71 Series SoCs integrating Wi-Fi, Bluetooth LE, Thread, and edge AI with up to 20 times lower standby power."
tags: ["wifi", "bluetooth", "edge-ai", "iot"]
source_type: press
sources:
  - "https://iot-now.com/2026/11/04/159196-nordic-nrf71-series-edge-ai-battery-powered-wifi/"
---

Nordic Semiconductor [announced](https://iot-now.com/2026/11/04/159196-nordic-nrf71-series-edge-ai-battery-powered-wifi/) the nRF71 Series of Systems-On-Chip (SoCs), combining ultra-low-power Wi-Fi 6, Bluetooth Low Energy (LE), Thread, and edge AI onto a single die. The parts target battery-powered IoT devices that previously excluded Wi-Fi due to power constraints.

The nRF71 Series delivers up to 20 times lower standby power usage than Nordic's current nRF70 Series Wi-Fi products. Two independent radios with separate RF and processing blocks enable this architecture: a dedicated Wi-Fi radio and a 2.4 GHz multiprotocol radio drawn from the nRF54 Series. Both radios can receive simultaneously, so a device maintains its Wi-Fi cloud link while listening for Bluetooth LE or Thread traffic, without either protocol waiting for the other. This simultaneous reception eliminates the latency and power cost of radio switching common in designs that multiplex a single radio between protocols. Nordic builds the series on the same software and tools used for its Bluetooth LE products, preserving the development environment for existing customers.

For edge AI, the nRF7120E variant integrates an Axon Neural Processing Unit (NPU) that runs machine learning models 10 to 17 times faster than the on-chip 256 MHz Arm Cortex-M33 processor alone. Keyword spotting, anomaly detection, and image classification now run on battery power without an external AI accelerator, cutting component count and bill-of-materials cost. The base nRF7120 offers dual-band Wi-Fi 6, while the nRF7120E adds tri-band Wi-Fi 6E support alongside the NPU. Developers can also build ultra-small models using Nordic's Neuton software to run inference on the Cortex-M33 alone when hardware acceleration is not required. Both parts include 4 MB of on-chip non-volatile memory and 1 MB of user-accessible RAM.

For practitioners, the integration means Matter-enabled smart home hubs, Thread border routers, smart locks, security panels, wearables, and industrial sensors can operate for years on a battery while maintaining a full Wi-Fi 6 uplink. The dual-radio design ensures local Thread or Bluetooth commissioning and Matter interoperability do not interrupt cloud connectivity. The nRF71 Series is now sampling with selected customers. Developers should contact Nordic sales representatives for availability details and pricing.
