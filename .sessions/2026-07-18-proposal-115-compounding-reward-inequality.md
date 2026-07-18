# PROPOSAL 115 — the compounding-reward inequality engine (round-26 GAME slot, P115 → V128, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus 4.x · high · proposal-draft

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Draft and land the round-26 GAME-slot proposal (P115): one genuinely new, counterintuitive, stdlib-simulable game-economy mechanism, distinct from the prior game slots P099 (shop-reroll optimal stopping), P103 (streak-shield regressivity), P107 (energy-cap overflow forfeiture), P111 (matchmaking win-rate mirage), P091 (gacha-pity), P095 (rubber-band PID) and the fleet coupon-collector-tail head — the compounding-reward inequality engine, where a fair daily percentage bonus (each day wealth changes by g ~ Normal(MU_G, SIGMA_G) with a small positive average, no skill, no choice) COMPOUNDS on the running total, so terminal wealth is log-normal and concentrates almost all the wealth in a handful of players purely by compounding — with pre-registered ≥3σ gates, exact log-normal closed-form anchors, and a same-shocks additive control that freezes the compounding, fanned to sim-lab as VERDICT 128 (+13).

## Constraints honored
- HARD-SYNC to origin HEAD (idea-engine 0945d59) before reading.
- Claim filed before work; born-red card is the first commit (HOLD); PR opened READY immediately; heartbeat before flip; Status→complete is the last commit.
- Monte Carlo of an identical-player wealth population with a pinned SEED=20260717 and ≥3σ gates against exact log-normal closed forms (Gini = 2Φ(σ_T/√2)−1, top-decile share = Φ(σ_T−Φ⁻¹(1−p))); the gate z is on the ESTIMATED MEAN via its standard error se=std/√TRIALS (the P104…P114 /se convention). Stdlib-only verifier (random, math, json, hashlib) — no numpy/scipy. Model line family-level.
