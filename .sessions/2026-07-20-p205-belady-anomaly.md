# Session 2026-07-20 — P205 Bélády's anomaly (round-49 FLEET slot)

> **Status:** in-progress

## 💡 Session idea
Land PROPOSAL 205: Bélády's anomaly. Give a FIFO page cache one MORE frame and it can fault MORE — on the textbook string [1,2,3,4,1,2,5,1,2,3,4,5] FIFO takes 9 faults at 3 frames but 10 at 4 (Δ=+1) — while LRU, a stack algorithm, provably never faults more when given more memory (Mattson et al. 1970 inclusion property). A deterministic stdlib verifier proves the exact canonical witness and LRU's monotone curve (G1), enumerates all 4⁸=65536 length-8 strings on 4 pages showing FIFO_anomalous=0 AND LRU_anomalous=0 — pinning the anomaly threshold above 4 distinct pages (G2), and shows the FIFO anomaly is a real ≥3σ signal against LRU's hard zero over uniform-random strings (G3 N=200000 z=6.000270; G4 shifted regime N=200000 rate 0.000545>0.0003, z=10.441729). Pairs to VERDICT 218 (+13).

## ⟲ Previous-session review
Prior slot was P204 (hat-check fixed-points invariance, round-48 UNRELATED), which landed as #757 pairing VERDICT 217 (+13); outbox proposal high-water was P204. This session opens the round-49 FLEET slot (fresh rotation) on Bélády's anomaly — dedup-clear on mechanism (Belady/page replacement/FIFO/LRU/LFU all no-hit on origin/main; only adjacency is Graham's scheduling anomaly P201, a DISTINCT non-monotonicity in scheduling makespan, disclosed). The original pre-registered G3/G4 constants were caught as impossible/mis-floored before authoring (A=4 can never be FIFO-anomalous; the true random rate is basis points, not "few %"); the coordinator reframed the battery into exact-threshold + signal-vs-hard-zero gates (all four now pass on the real numbers). This card is born red to HOLD the PR until authoring + preflight are green; flipping it to complete releases merge-on-green.

> 📊 Model: Claude Opus · high · idea/planning

## Decisions made
- Reframed the four gates after firsthand measurement showed the original G3 (">0 over 4⁸") is mathematically impossible (4 distinct pages can never be FIFO-anomalous) and the original G4 floor 0.005 was ~10× above the true ~0.00054 rate. New battery: G1 exact canonical witness + LRU monotone curve; G2 exhaustive 4⁸ with FIFO_anomalous=0 AND LRU_anomalous=0 (threshold pin); G3 ≥3σ signal (z=6.000270) vs LRU=0; G4 robustness shift (rate 0.000545>0.0003, z=10.441729) — all deterministic, cross-invocation stable. Disclosed results_sha256 e5c3517c9d3408bc76941be37b820d0216fcbe0fb00c2cffaf1d8bf763bf7bff.
- Grounding byte-pinned to Wikipedia "Bélády's anomaly" rev 1312057235 (raw-wikitext sha1 ffabfee5a2daf46ebc33fca9e3ed94c854e2bd38), which states firsthand that FIFO faults can increase with more frames while optimal/stack-based algorithms like LRU decrease, and gives the same 9-at-3-frames / 10-at-4 example.
- Honest nuance disclosed: the anomaly is real but RARE over random strings (~1.8 and ~5.5 per ten-thousand), needs ≥5 distinct pages (classic minimal 5 pages length 12), and is distinct from Graham's scheduling anomaly P201.

## Next session should know
- P205 → VERDICT 218 (+13) is now awaiting sim-lab reproduction of digest e5c3517c…7bff; outbox proposal high-water advances P204 → P205. Heartbeat (control/status.md) left to the coordinator.
- A reusable FIFO/LRU fault-counter + anomaly-predicate harness (exhaustive enumeration + seeded two-proportion z gates) now lives in ideas/fleet/belady-anomaly-fifo-nonmonotonicity.py.
