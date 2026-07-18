# PROPOSAL 120 — the German-tank estimator (round-27 UNRELATED slot, P120 → V133, +13)

> **Status:** `in-progress`
> 📊 Model: opus-4.8 · high · idea/planning

Born in-progress as this session's first commit (born-red HOLD); will flip to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Draft and land the round-27 UNRELATED-slot closer (P120): one genuinely new, counterintuitive, stdlib-simulable pure-mechanism head OUTSIDE the fleet/venture/game domains and distinct from the prior unrelated closers P100 (Kelly overbet / information theory), P104 (epidemic overshoot / epidemiology), P108 (regression to the mean / statistics), P112 (series-system MTBF collapse / reliability engineering), P116 (arcsine lead illusion / stochastic processes). Domain: statistical estimation theory — the German-tank problem (MVUE for the max of a discrete uniform population). With pre-registered ≥3σ /se gates, an unbiasedness control, and a closed-form variance anchor + efficiency control. Fanned to sim-lab as VERDICT 133 (+13). This slice does NOT write the verdict.

## Plan
- Claim filed + this born-red card = first commit (HOLD); PR opened READY immediately (born-red card holds it red, not draft state); heartbeat before flip; Status→complete is the last commit.
- Idea doc `ideas/fleet/german-tank-mvue-2026-07-18.md` (grammar-gated: `> **State:**`, `## Probe report` 8-question battery, `**Recommendation: sim-ready**`, `> **Grounding:** <url>@<sha> · fetched <ISO>`, external reference on a separate reachable line).
- Committed stdlib-only verifier `ideas/fleet/german_tank_mvue.py` (random, math, json, hashlib — no numpy): SEED=20260717, sample k distinct serials without replacement from 1..N, compute MVUE N̂ = m(1+1/k)−1, the naive max m, and the alternative unbiased 2·x̄−1; /se z convention over TRIALS replications; ≥3σ gates; canonical sorted-keys results dict + sha256; deterministic (two runs byte-identical, exit 0).
- Outbox P120 block (P120 ↔ V133, +13, cited not written); heartbeat proposal HW → P120.

The full close-out (dry-sim numbers, dedup, previous-session review, session idea, GROUNDING) is written at flip time.
