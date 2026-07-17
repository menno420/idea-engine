# PROPOSAL 093 — metastable retry-storm collapse: aggressive lane-retries make an agent fleet bistable, so a brief load blip permanently collapses throughput (round-21 fleet opener, P093 → V106, +13)

> **Status:** `in-progress`
> 📊 Model: opus-4.8 · high · proposal-draft

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Open round 21 of the ORDER 003 pipeline at the FLEET slot (fleet→venture→game→unrelated; the round-20 unrelated closer was P092 Braess). Draft a genuinely new, counterintuitive, stdlib-simulable fleet-ops idea and land it sim-ready for sim-lab VERDICT 106 (+13): a lane pool that retries timed-out tasks is BISTABLE above a critical retry-aggressiveness r_c — a brief load blip tips it from healthy throughput into a self-sustaining retry storm that persists after load falls back (metastable hysteresis), at only 60% utilization; the fix is a retry budget, not more lanes.

## Constraints honored
- Append-only outbox: `## PROPOSAL 093` appended once; no prior entry edited.
- Claim placed before the work; the terminal VERDICT 105 claim (PRs #473/#474/#178 all merged, verified live) is pruned in this slice (housekeeping rider).
- SEEDLESS: pinned a private SEED_BASE=20260721; the shared seed-ledger block 20261730 left untouched (P089/P090/P091/P092 precedent).
- Grounded firsthand (Marc Brooker metastability post, fetched 2026-07-17T08:04:31Z; formalized in Bronson et al. HotOS '21); gates pre-registered on a seeded deterministic dry-sim, byte-identical double-run.
- Neutral heartbeat; no cross-seat inbox edits; guard-fires.jsonl left uncommitted (classifier wall).

## What happened
Drafted PROPOSAL 093 (idea file + outbox block) and calibrated four pre-registered gates on a stdlib dry-sim (byte-identical, stdout sha256 db7d7fcc…a7d9). Dry-sim APPROVE: R1 — mean-field bistable (healthy x*=61.311/goodput 59.769, unstable 104.748, collapsed 400.000/goodput≈0), stochastic cold 59.525 (199/200 healthy) vs hot 0.000 (200/200 collapsed) at z=312.4σ; R2 — hysteresis width 56.0 (λ_up 78.5, λ_down 22.5); R3 — collapse width monotone in r, critical r_c≈0.566, 6/6 coexisting sign-grid cells positive; R4 — retry-budget cap (b=0.20) eliminates the collapsed fixed point, goodput restored to 59.769. Disclosed correction: pinned load moved λ 70→60 (the only tuned constant) because at λ=70 the stochastic healthy basin escapes faster than the measurement horizon; mean-field results unchanged.

## ⟲ Previous-session review
The prior slice closed the P092→V105 loop (Braess selfish routing, APPROVE, mirrored into this repo's ledger; PRs #474/#178 merged) and rolled the baton to the round-21 fleet opener. That card's 💡 suggested a Braess-follow-up (excess-latency knob on the real router); this session instead opens a mechanistically distinct fleet head — retry-feedback bistability / metastability — a stronger standalone counterintuitive result (a second, collapsed equilibrium with hysteresis, absent from every prior fleet head P085/P089/P092). The Braess-follow-up remains available as a named future head.

## 💡 Session idea
Next baton after V106: a retry-budget-calibration head — for the manager's real lane pool, find the minimum retry-cap b (or the r_c operating ceiling) that removes the collapsed equilibrium across the observed load band, turning this proposal's knockout gate into a concrete ship setting for the dispatcher's retry policy / circuit breaker.

📊 Model: opus-4.8 · high · proposal-draft
