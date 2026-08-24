---
title: "Morse Micro Ships Wi-Fi HaLow USB Dongle Reference Designs"
date: 2026-08-24T07:16:41-07:00
summary: "Morse Micro released two USB dongle reference designs that add kilometer-range Wi-Fi HaLow to existing devices."
tags: ["wifi-halow", "usb", "edge-ai", "long-range"]
source_type: press
sources:
  - "https://iot-now.com/2026/08/24/158025-morse-micro-announces-two-wi-fi-halow-usb-dongle-reference-designs-to-enable-long-range-edge-ai-connectivity/"
---

Morse Micro announced two Wi-Fi HaLow USB dongle reference designs that bring kilometer-range connectivity to existing devices through a USB port. The designs, [reported by IoT Now](https://iot-now.com/2026/08/24/158025-morse-micro-announces-two-wi-fi-halow-usb-dongle-reference-designs-to-enable-long-range-edge-ai-connectivity/), give developers a way to add Wi-Fi HaLow to deployed hardware without redesigning the product.

Both designs run on Morse Micro's MM8108 system-on-chip. The MM8108-RD09 reference design provides native Wi-Fi HaLow connectivity for access point and station products. It ships with OpenWRT drivers for routers and access points that have USB interfaces. For client devices, it includes native Windows and Linux drivers plus a MacOS application. Users connect to Wi-Fi HaLow networks the same way they connect to traditional Wi-Fi networks.

The MM8108-RD17 reference design uses a different approach to broaden compatibility. It presents itself as a standard CDC-NCM Ethernet interface when plugged into a host, which removes the need for device-specific drivers. This lets it work with industrial computers, robotics, point-of-sale terminals, and tablets or phones running Android or iOS. The design supports Wi-Fi Easy Connect (DPP) authentication through a physical pairing button.

Wi-Fi HaLow networks provide native IP connectivity at ranges up to one kilometer, according to Morse Micro. The schematics and software for both reference designs are available to tier-1 customers through Morse Micro sales contacts.

Michael De Nil, co-founder and CEO of Morse Micro, said the company anticipates the designs will accelerate Wi-Fi HaLow adoption. The RD09 lets internet service providers upgrade existing wireless routers to give customers kilometer-range connectivity. The RD17 brings Wi-Fi HaLow to laptops, phones, and tablets across large properties without requiring additional software updates.

For network practitioners, these dongles solve a practical deployment problem. They extend IP reach across warehouses, campuses, or industrial sites without a forklift upgrade of existing equipment. The RD17's driverless operation is particularly useful for adding low-power, long-range links to deployed devices where modifying host software is impractical or unsupported.

Equipment makers get a tested blueprint for building HaLow products. The two approaches, native drivers versus CDC-NCM Ethernet, let vendors pick the model that fits their target devices and operational constraints. This flexibility could reduce development time and testing overhead for companies adding IoT connectivity to their product lines.
