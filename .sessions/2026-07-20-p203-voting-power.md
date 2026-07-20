# Session 2026-07-20 — P203 voting power ≠ voting weight (round-48 GAME slot)

> **Status:** complete

## 💡 Session idea
Land PROPOSAL 203: voting power is not voting weight. With a 50-49-1 weighted majority vote the 49-weight bloc has EXACTLY the same power as the 1-weight bloc (⅕ each Banzhaf), while the near-identical 50-weight bloc holds ⅗ — a 2% weight edge buys 3× the power. A deterministic stdlib verifier proves the exact rational Banzhaf & Shapley–Shubik indices by exhaustive coalition enumeration (cross-checked by a generating-function DP), sweeps all n=4 majority games for dummies and index disagreement, and adds a ≥3σ large-voter-premium sample. Pairs to VERDICT 216 (+13).

## ⟲ Previous-session review
Prior GAME slot was P199 (Vickrey truthful dominance, VERDICT 212 APPROVED, sim-lab PR #287 merged). Boot outbox high-water: P202/V215 (V214 last finalized). This session first drafted Parrondo's paradox (already sim-ready at ideas/fleet/parrondo-losing-games-combine-2026-07-13.md) then Gale–Shapley duality (already sim-ready as P068 at ideas/fleet/deferred-acceptance-proposer-advantage-2026-07-15.md); both dropped after a full cross-lane dedup scan, pivoted to the un-built power-index paradox. This card is born red to HOLD the PR until authoring + preflight are green; flipping it to complete releases merge-on-green.

> 📊 Model: Claude Opus · high · idea/planning

## Decisions made
- Pivoted twice on dedup collisions (Parrondo → already sim-ready in ideas/fleet/; Gale–Shapley duality → already sim-ready as P068) before landing on the un-built Banzhaf / Shapley–Shubik power-index paradox after a full cross-lane dedup scan.
- Headline instance [51;50,49,1]: normalized Banzhaf exactly (3/5,1/5,1/5), Shapley–Shubik (2/3,1/6,1/6) — the 49-bloc equals the 1-bloc. Four gates, all exact/deterministic, cross-invocation stable. Disclosed results_sha256 660bb1e59107c98a1b10256d3dfa195346a02298cba9753a9aef3e2281ece254.
- Grounding byte-pinned to Wikipedia "Banzhaf power index" rev 1347671339.

## Next session should know
- P203 → VERDICT 216 (+13) is now awaiting sim-lab reproduction of digest 660bb1e5…ece254; outbox high-water advanced P202 → P203. Heartbeat (control/status.md) left to the coordinator.
- A reusable exact power-index harness (Banzhaf brute + generating-function DP cross-check, Shapley–Shubik) now lives in ideas/superbot-games/voting-power-not-weight-2026-07-20.py.
