---
title: "Nokia launches GPU-based AI-RAN with Nvidia"
date: 2026-10-12T07:33:14-07:00
summary: "Nokia will sell GPU-based radio access network gear next year, betting on AI workloads and software flexibility over custom silicon."
tags: ["ai-ran", "nokia", "gpu", "ran"]
source_type: press
sources:
  - "https://www.lightreading.com/5g/nokia-to-start-dealing-out-gpus-in-high-stakes-ai-ran-gamble"
---

Nokia has teamed up with Nvidia to design radio access network products built on graphics processing units (GPUs) and will stop developing new custom silicon with Marvell Technology, with commercial availability slated for early next year, according to a [Light Reading](https://www.lightreading.com/5g/nokia-to-start-dealing-out-gpus-in-high-stakes-ai-ran-gamble) report. The Finnish vendor will continue to support its existing 4G and 5G gear for years, but new features will require new hardware.

The new design slots a slimline GPU into Nokia's existing Airscale chassis, originally built for Marvell silicon. Nokia executives promise the GPU card will match the power draw and price of the ASIC it replaces. A Hardware Abstraction Layer (HAL) sits between the RAN software and the silicon, which Nokia says will insulate operators from hardware changes and support algorithm upgrades for years. The platform runs on Nvidia's CUDA software stack, the vendor-specific platform that ties it tightly to Nvidia GPUs.

Nokia claims the GPU approach will double spectral efficiency by 2028 and let operators run AI inference workloads directly on the RAN. But the claim faces skepticism. Marcus Weldon, former Nokia CTO and Bell Labs president, says Bell Labs ran similar GPU RAN projects and saw gains closer to 20 to 30 percent, not 2x, and only in niche scenarios. The gains depend on the baseline: a site already near its theoretical limit has less headroom than one suffering from interference or channel estimation errors.

Timing constraints also limit what GPUs can do. Critical Layer 1 RAN functions must finish within the transmission time interval (TTI), roughly 500 microseconds. That leaves little room for large AI models. Some scheduling tasks have longer budgets of 5 to 10 milliseconds, where bigger models could help, but those use cases are limited. Chetan Sharma, a telecom analyst who wrote a Nokia-endorsed white paper, notes that a GPU RAN must not cost more in total energy than a traditional RAN plus a separate AI inference server.

For operators, the shift changes the hardware investment model. ASIC refresh cycles typically run three to five years. Nokia argues that GPUs amortize over a seven-year window and reduce forced upgrades. But if the GPU strategy fails to win operator support, Nokia has no companion ASIC strategy, creating what Weldon calls "jeopardy." Verizon CTO Yago Tenorio has already dismissed the idea of running RAN workloads on GPUs, saying they should stick to AI inference.

The bet is that the CUDA ecosystem and software flexibility will outweigh the cost, energy, and lock-in risks. If Nokia can prove the gains, it could recover 5G market share lost to Ericsson and Samsung. If not, it has committed to a path with no obvious retreat.
