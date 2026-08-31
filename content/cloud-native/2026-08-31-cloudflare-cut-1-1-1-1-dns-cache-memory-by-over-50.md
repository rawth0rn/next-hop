---
title: "Cloudflare cut 1.1.1.1 DNS cache memory by over 50%"
date: 2026-08-31T07:36:38-07:00
summary: "Cloudflare reduced per-entry memory in its 1.1.1.1 DNS cache by over 50%, freeing roughly 100 terabytes and cutting lookup latency by 19%."
tags: ["dns", "rust", "memory"]
source_type: engineering
sources:
  - "https://blog.cloudflare.com/dns-cache-memory-optimization-1111/"
---

A [Cloudflare post](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) details how five successive changes to the way its Big Pineapple platform stores DNS cache entries in memory cut the per-entry footprint by over 50%. Big Pineapple runs 1.1.1.1 and related DNS services. With more than 250 billion cache entries live at any time, the changes freed roughly 100 terabytes of memory across the fleet. Insert throughput rose 43% and lookup latency dropped 19%.

The optimizations all target Rust struct layout. The first change replaced eight `Vec` and `String` fields per entry with fixed-size `Box<[T]>` and `Box<str>`. Because cached responses never grow after insertion, dropping the unused capacity fields saved 64 bytes per entry and eliminated excess heap reservations. Engineers then collapsed the separate answer, authority, and additional record lists into a single list indexed by 2-byte offsets. That saved 28 bytes per entry, while packing boolean flags into bitflags further reduced struct padding.

Next, they stopped storing the record owner name when it matched the queried domain. Since most cached records share the query name, the owner field now uses `Option<Box<Name>>` and falls back to the cache key at read time, skipping a heap allocation for the common case. They also boxed the larger variants of a Rust enum that stores parsed record data. The enum had been padded to the size of its largest variant, NAPTR, at 144 bytes. By boxing large types such as NAPTR and leaving small A and AAAA records inline, they cut per-record overhead for the most common types by 120 bytes.

The final step moved record data into a single contiguous `Box<[u8]>` buffer holding raw wire-format bytes with 2-byte length prefixes. This removed per-variant enum overhead and scattered heap allocations entirely, improving CPU cache locality. The tradeoff is sequential access rather than random indexing, but the cost is negligible for the small record counts seen in practice.

For operators running DNS at scale, the work is a reminder that Rust's memory layout is not free. Default choices such as growable vectors, padded enums, and redundant string storage compound quickly when entries number in the billions. Cloudflare's changes required no protocol modifications or client-visible behavior shifts. They yield operational capacity equivalent to about 130 Gen 13 servers without adding hardware. The savings are especially pronounced in locations with heavy EDNS Client Subnet (ECS) use, where multiple answers per query inflate entry counts and memory per entry. For any team caching high-volume, immutable objects, auditing struct layout and allocator behavior can return capacity and latency at the same time.
