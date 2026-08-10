---
title: "WisdPi USB-C 10GbE Adapter Brings Realtek RTL8159 to Servers"
date: 2026-08-10T07:08:18-07:00
summary: "ServeTheHome reviews the WisdPi WP-UT9 USB 10GbE adapter with Realtek RTL8159 chipset."
tags: ["usb", "10gbe", "adapter", "realtek"]
source_type: roundup
sources:
  - "https://www.servethehome.com/wisdpi-wp-ut9-usb-10gbe-adapter-realtek-rtl8159-review/"
---

Data center networking saw few major announcements this week, but a new hardware review highlights incremental progress in compact connectivity options for edge devices and small servers.

ServeTheHome published a [review](https://www.servethehome.com/wisdpi-wp-ut9-usb-10gbe-adapter-realtek-rtl8159-review/) of the WisdPi WP-UT9 USB 10GbE adapter, a compact USB-C to 10Gbase-T solution built around the Realtek RTL8159 controller.

The adapter fits a 10Gbase-T PHY and the RTL8159 controller into a small aluminum enclosure with a ridged metal shell that helps dissipate heat. One end offers an RJ45 port supporting standard Ethernet speeds from 100Mbps up to 10Gbps, including 2.5GbE and 5GbE intermediate rates when paired with multi-gig switches. The opposite end provides a USB Type-C connector that handles both data and power, eliminating the need for an external power brick. The review notes the included USB-C to USB-C cable is functional but short, though users can substitute a longer cable if needed. The bottom of the unit carries a large black label that contrasts with the otherwise clean aluminum construction.

This is the second RTL8159-based adapter ServeTheHome has reviewed this year, following the Xikestor SKN-U310GT. While the internal controller and expected performance characteristics match, the WisdPi unit differs in its housing design and bundled cable. Both adapters deliver the same core capability: 10GbE connectivity through a USB-C interface.

Driver support has matured since the Xikestor review. On Windows 11, the adapter uses the standard Realtek driver and is properly recognized in Device Manager once installed. On Linux, the RTL8159 driver integration is now queued for Linux 7.2, having been merged into the net-next tree for the r8152 driver. Earlier kernels still require Realtek’s out-of-tree driver or a distribution backport. This mainline progress matters for practitioners managing Linux servers.

The adapter gives data center operators a way to add 10GbE connectivity to laptops, small form factor systems, or edge devices that lack expansion slots. Drawing power solely from USB simplifies deployment without extra cables or power supplies. The pending mainline Linux driver support also signals better long-term maintainability for server and edge environments that run Linux.

The WisdPi WP-UT9 is available now.
