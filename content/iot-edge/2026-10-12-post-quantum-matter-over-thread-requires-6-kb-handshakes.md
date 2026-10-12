---
title: "Post-Quantum Matter over Thread Requires 6 kB Handshakes"
date: 2026-10-12T07:24:46-07:00
summary: "Researchers measure that fully post-quantum Matter handshakes exceed Thread limits, but caching reduces size to 6.1 kB."
tags: ["post-quantum", "matter", "thread", "iot"]
source_type: research
sources:
  - "https://arxiv.org/abs/2610.13026"
---

The arXiv preprint [Post-Quantum Session Establishment for Matter over Thread: Message Size, Transport, and Protocol Options](https://arxiv.org/abs/2610.13026) measures that a drop-in post-quantum replacement for Matter's operational handshake balloons from 1.6 kB to 22.8 kB, far exceeding Thread's 1178-byte message limit and making fragmentation mandatory.

Matter's current post-quantum upgrade only protects device attestation with ML-DSA. Its main session key exchange, CASE, still uses P-256 ECDH, leaving recorded traffic vulnerable to future quantum computers. Thread's strict frame size means every message must fit within 127 bytes, and Matter caps messages at 1178 bytes. The researchers built a byte-exact model of CASE messages and found no fully post-quantum configuration using standard FIPS 203/204/205 algorithms fits within that limit.

The transport impact is worse than the size alone suggests. The team ran a Monte Carlo model of multi-hop Thread networks, calibrated against OpenThread and Matter source code. Fragmented IPv6 datagrams trigger spurious retransmissions when a message and its reply outlast Matter's retransmission timer. At three to four hops, the bloated handshake takes 1.8 to 2.6 times longer than with a proper block transfer protocol, and up to 33 percent of handshakes with sleepy end devices fail. Simply increasing timers does not fix the problem.

Caching helps. If certificate chains are cached and the device authenticates with a pre-distributed ML-KEM key, the handshake shrinks to 6.1 kB and requires only 44 ms of device computation. As an interim step, the paper proposes a hybrid P-256 plus ML-KEM-512 key exchange with cached device chains. This protects session keys against harvest-now, decrypt-later attacks while keeping every message under the current limit.

The results matter for IoT network architects planning post-quantum migration. Fully post-quantum Matter requires either protocol changes to support larger messages or acceptance of slower, less reliable handshakes in multi-hop Thread deployments. The hybrid approach offers a practical near-term defense without breaking existing frame constraints or device silicon requirements.
