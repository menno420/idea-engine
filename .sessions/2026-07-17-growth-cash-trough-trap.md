# PROPOSAL 102 — the growth cash-trough trap (round-23 venture slot, P102 → V115, +13)

> **Status:** `complete`
> 📊 Model: opus-4.8 · high · idea/planning

Born in-progress as this session's first commit (born-red HOLD); flipped to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Draft and land the round-23 VENTURE-slot proposal (P102): one genuinely new, counterintuitive, stdlib-simulable venture-economics idea with a closed-form analytic anchor and pre-registered ≥3σ gates, fanned to sim-lab as VERDICT 115 (+13). Executes ORDER 018 (owner's live overnight generate→verify loop directive).

## Constraints honored
- HARD-SYNC to origin HEAD (idea-engine 61b72c4) before reading; control/inbox.md@HEAD confirms ORDER 018 (owner overnight directive, verbatim) is the governing order for this slice.
- Claim filed before work; born-red card is the first commit (HOLD); PR #497 opened READY immediately; heartbeat before flip; Status→complete is the last commit.
- `python3 bootstrap.py check --strict` green (exit 0) before push.
- Closed-form analytic anchor (fluid-limit E[active_k]=A0·(g^{k+1}−s^{k+1})/(g−s); critical rate g_crit=CAC·s/(CAC−m)) + dry-sim-calibrated gates at ≥3σ; stdlib-only verifier (random, math, json, hashlib), no third-party. Model line family-level (ORDER 012 / PL-004 idea/planning class).

## What happened
- Idea: two subscription ventures with IDENTICAL, positive per-customer unit economics (LTV=m/c=100 > CAC=60) but different acquisition growth rates g do NOT share cash risk — the faster grower has a strictly deeper cumulative-cash trough because CAC is paid upfront while margin accrues over the customer's lifetime. Above a closed-form critical rate g_crit=CAC·s/(CAC−m)=1.08, per-period cash flow is permanently negative despite every customer being profitable. Ruin is cash TIMING, not unit economics.
- Pinned world SEED=20260717, T=24, A0=10, M=10, c=0.10 (s=0.90), CAC=60, N_REPS=4000, K0=3000; growth sweep {1.05,1.08,1.15,1.30}, headline g_low=1.05 < g_crit=1.08 < g_high=1.30. Trough deepens monotonically (−3.06k, −5.07k, −29.06k, −498.6k); ~163× deeper at g_high; ruin prob 0.53→1.00.
- Dry-sim (stdlib verifier, exit 0, two runs byte-identical): R1 cash-trough trap z=6011.93σ; R2 unit-economics control — π0-anchor |z|=0.66σ/0.83σ, positivity z=83.87σ/83.00σ, low-vs-high |z|=1.05σ; R3 fluid-anchor |z|=0.89σ (g_low k*=11) / 1.14σ (g_high k*=23) — all PASS. Results-dict sha256 5e6b4ce7cf3a58e6c5fa912ee5365ff4152c162818113320a8c2332195bc4d95.
- Files: ideas/venture-lab/growth-cash-trough-trap-2026-07-17.md (State: sim-ready) + committed reference verifier ideas/venture-lab/growth_cash_trough_trap.py; PROPOSAL 102 block appended to control/outbox.md (P102 ↔ V115, +13); claim control/claims/proposal-102-growth-cash-trough-trap.md filed; heartbeat updated (proposal high-water → P102, baton → V115 then P103).

## ⟲ Previous-session review
Immediate predecessor P101 (round-23 FLEET opener, winner's curse in a common-value task auction) drafted sim-ready by the parallel slice (idea-engine #494), awaiting VERDICT 114 — offset ledger and baton confirmed intact before extending the rotation to the venture slot. Venture-lane predecessor P098 (the referral-bonus value trap) landed APPROVE as V111 (idea-engine #489). P102 continues the round-23 rotation (fleet→venture→game→unrelated) at the venture slot with a DISTINCT mechanism (cash-flow timing / growth-financing risk, not an interior optimum on a spend lever).

## 💡 Session idea
The unit-economics/cash-flow decomposition is a reusable "timing trap" template: a positive per-unit margin does NOT relieve a survival constraint when cost is paid upfront and revenue accrues over the unit's future life — the low-water balance is monotone in the scaling rate, with a closed-form critical rate above which profitable units still bankrupt the operator. Candidate future proposals: inventory-financed retail growth (COGS upfront vs sell-through), agency headcount ramps (salary upfront vs billings), and content/marketplace supply subsidies (acquisition cost upfront vs take-rate over lifetime) — each an upfront-cost-vs-deferred-revenue timing trap with its own g_crit.

## GROUNDING
idea-engine@61b72c4 (HEAD at sync, verified via git ls-remote). Firsthand harvest: Customer lifetime value — https://en.wikipedia.org/wiki/Customer_lifetime_value (fetched 2026-07-17T23:21:30Z, HTTP 200), "CLV is the present value of future cash flows attributed to the customer during his/her entire relationship with the company" (the deferred-cash-flow structure the trough mechanism rests on). Analytic anchor verified firsthand by the committed sim (two byte-identical runs, exit 0); disclosed results-dict sha256 5e6b4ce7…bc4d95.

📊 Model: opus-4.8 · high · idea/planning
