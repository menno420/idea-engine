# Session 2026-07-20 — P203 voting power ≠ voting weight (round-48 GAME slot)

> **Status:** in-progress

## 💡 Session idea
Land PROPOSAL 203: voting power is not voting weight. With a 50-49-1 weighted majority vote the 49-weight bloc has EXACTLY the same power as the 1-weight bloc (⅕ each Banzhaf), while the near-identical 50-weight bloc holds ⅗ — a 2% weight edge buys 3× the power. A deterministic stdlib verifier proves the exact rational Banzhaf & Shapley–Shubik indices by exhaustive coalition enumeration (cross-checked by a generating-function DP), sweeps all n=4 majority games for dummies and index disagreement, and adds a ≥3σ large-voter-premium sample. Pairs to VERDICT 216 (+13).

## ⟲ Previous-session review
Prior GAME slot was P199 (Vickrey truthful dominance, VERDICT 212 APPROVED, sim-lab PR #287 merged). Boot outbox high-water: P202/V215 (V214 last finalized). This session first drafted Parrondo's paradox (already sim-ready at ideas/fleet/parrondo-losing-games-combine-2026-07-13.md) then Gale–Shapley duality (already sim-ready as P068 at ideas/fleet/deferred-acceptance-proposer-advantage-2026-07-15.md); both dropped after a full cross-lane dedup scan, pivoted to the un-built power-index paradox. This card is born red to HOLD the PR until authoring + preflight are green; flipping it to complete releases merge-on-green.

> 📊 Model: Claude Opus · high · idea/planning

## Decisions made
_(filled at close)_

## Next session should know
_(filled at close)_
