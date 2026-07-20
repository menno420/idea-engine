# Session 2026-07-20 — P204 hat-check fixed-points invariance (round-48 UNRELATED slot)

> **Status:** complete

## 💡 Session idea
Land PROPOSAL 204: the hat-check invariance. When n patrons each grab a coat at random, the number who get their own coat back has mean EXACTLY 1 and variance EXACTLY 1 for every n≥2 — crowd size cancels — and the chance nobody does converges to 1/e ≈ 36.8%, with the whole fixed-point count going Poisson(1). A deterministic stdlib verifier proves E=1 & Var=1 exactly by exhaustive Fraction enumeration (n=1..8) with brute derangements = inclusion-exclusion = recurrence (G1), clears the folk "essentially never" derangement floor 0.30 at z_floor 40.9 while sitting within 3σ of 1/e (G2, n=200), shows the mean does not move with crowd size (G3 range 0.021875 over n∈{10,100,1000,2000}), and fits Poisson(1) (G4 χ²=1.36<18.467). Pairs to VERDICT 217 (+13).

## ⟲ Previous-session review
Prior UNRELATED-lane / immediately preceding proposal was P203 (voting power ≠ voting weight, Banzhaf / Shapley–Shubik), which landed as #755 pairing VERDICT 216 (+13); outbox high-water was P203. This session authors the round-48 UNRELATED slot (closes the fleet→venture→game→unrelated loop) on the un-built hat-check / rencontres-numbers fixed-point invariant — dedup-clear on mechanism (only adjacency: two shipped permutation heads that key on CYCLE-LENGTH structure, not fixed points). This card is born red to HOLD the PR until authoring + preflight are green; flipping it to complete releases merge-on-green.

> 📊 Model: Claude Opus · high · idea/planning

## Decisions made
- Landed on the fixed-point-count / derangement invariant (rencontres numbers) after dedup: distinct from the two shipped permutation heads (hundred-prisoners, cycle-following-coupling) which key on cycle-length structure, not fixed points.
- Four gates, all deterministic and cross-invocation stable; G1 Fraction-exact (E=1, Var=1, D_n three-way agree n=1..8). Disclosed results_sha256 7b99e6504b7cfa776ce871b7756b2ff71ed5bcd025e9dd6134d0f8d8e246dfb0.
- Grounding byte-pinned to Wikipedia "Rencontres numbers" rev 1340506236 (raw-wikitext sha1 256b0417a6785bd9d1e50a6aa9766175ee329dc5), which states mean=1, the Poisson(1) moments, and the 1/e derangement limit firsthand.

## Next session should know
- P204 → VERDICT 217 (+13) is now awaiting sim-lab reproduction of digest 7b99e650…6dfb0; outbox high-water advanced P203 → P204. Heartbeat (control/status.md) left to the coordinator.
- A reusable exact/Monte-Carlo fixed-point harness (Fraction enumeration + seeded RNG gates) now lives in ideas/fleet/hat-check-fixed-points-invariance.py.
