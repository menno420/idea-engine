# PROPOSAL 114 — the freemium support-cost inversion (round-26 VENTURE slot, P114 → V127, +13)

> **Status:** `in-progress`

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Draft and land the round-26 VENTURE-slot proposal (P114): one genuinely new, counterintuitive, stdlib-simulable freemium / product-led-growth mechanism, distinct from the prior venture slots P098 (referral-bonus value trap), P102 (growth cash-trough trap), P106 (retention-survivorship mirage) and P110 (discount-depth breakeven trap) — the freemium support-cost inversion, where per-free-user contribution is V·p−c and conversion probability p DECLINES with acquisition volume (lower-intent marginal users), so total contribution V·Σp−c·n is concave, peaks where p crosses the serving-cost breakeven c/V (n*=ln(V·P0/c)/K), then falls through zero into value destruction even as signups and total conversions keep rising — with pre-registered ≥3σ gates and exact closed-form contribution anchors, fanned to sim-lab as VERDICT 127 (+13).

## Constraints honored
- HARD-SYNC to origin HEAD (idea-engine 834fa90) before reading.
- Claim filed before work; born-red card is the first commit (HOLD); PR opened READY immediately; heartbeat before flip; Status→complete is the last commit.
- `python3 bootstrap.py check --strict` green (exit 0) before push.
- Monte Carlo of a per-user Bernoulli conversion population with a pinned SEED=20260717 and ≥3σ gates against the exact closed-form contribution C(n)=V·S(n)−c·n; the gate z is on the ESTIMATED MEAN via its standard error se=std/√TRIALS (the P104…P113 /se convention). Stdlib-only verifier (random, math, json, hashlib) — no numpy/scipy. Model line family-level.
