---
title: "NEC tests parking billing that starts only after driver exits vehicle"
date: 2026-08-10T07:31:03-07:00
summary: "NEC is piloting parking technology that delays charging fees until the driver leaves the vehicle."
tags: ["parking", "iot", "billing", "sensors"]
source_type: press
sources:
  - "https://www.theregister.com/software/2026/08/10/nec-tests-parking-tech-that-only-starts-charging-once-you-exit-your-car/5285245"
---

NEC is testing parking technology that only starts charging once the driver exits the vehicle, [The Register Networks](https://www.theregister.com/software/2026/08/10/nec-tests-parking-tech-that-only-starts-charging-once-you-exit-your-car/5285245) reported.

The system links billing activation to occupancy detection rather than entry time. Traditional parking meters and gate systems begin charging when a car enters the space or takes a ticket. NEC's approach waits for the exit event to trigger the tariff calculation, which implies continuous monitoring of the parking space state through hardware installed at each bay.

For operators, this shifts the technical requirements from entry-based timestamping to persistent occupancy verification. The setup likely relies on sensors, cameras, or floor pads to confirm presence, paired with payment infrastructure that holds the session open until departure. It removes the need for drivers to estimate duration upfront or rush back to avoid overage fees, but it also means the infrastructure must maintain real-time state on each individual bay and handle edge cases such as quick stops or sensor errors.

The test suggests a move toward consumption-based pricing models in physical infrastructure. Network operators managing smart city deployments or campus Internet of Things (IoT) networks should note the change in data flow: instead of simple entry/exit pairs, the system must stream occupancy status continuously and process payment events asynchronously. This adds bandwidth and latency requirements for sensor networks and backend billing systems, but eliminates the customer friction of pre-payment and the operational overhead of refunding unused time. Integration with existing payment gateways and mobile apps would require new APIs that handle deferred charging sessions and final settlement upon exit.

NEC has not announced wider deployment timelines or pricing for the technology.
