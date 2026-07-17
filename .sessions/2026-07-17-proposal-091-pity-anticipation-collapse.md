# Session — PROPOSAL 091: pity-timer anticipation-collapse retention cliff (round-20 game slot)

> **Status:** `complete`
> **📊 Model:** opus-4.8 · high · idea/planning

(Card born in-progress as the designed session-gate HOLD — the born-red FIRST commit; the Status badge flips to `complete` in this PR's final commit, after the heartbeat, releasing the landing workflow.)

## Scope / objective
Draft and land round-20 game-slot PROPOSAL 091 (fleet→venture→game→unrelated rotation; the prior two pipeline slices served fleet (P089) and venture (P090)). One genuinely new game-mechanics idea, deduped against all game priors, grounded firsthand, with pre-registered gates calibrated on a seeded dry-sim (≥3σ, corrections disclosed), a disclosed verifier spec, and a pinned world → the +13-offset VERDICT 104 for sim-lab to simulate.

## 💡 Session idea
Pity-timer anticipation-collapse retention cliff: a gacha/loot pity ceiling guaranteeing a reward after K dry pulls maximizes retention at an INTERIOR K, not the tightest. A tight ceiling floods the schedule with predictable "forced" rewards and collapses the variable-ratio anticipation (boredom churn); a loose ceiling lets long droughts drive frustration churn. Dry-sim: interior optimum K*=6 beats the tightest pity (K=2) by 61.4σ and the loosest (K=16) by 43.1σ; removing boredom (c=0) collapses the optimum to the tightest ceiling, removing frustration (a=0) collapses it to the loosest — both hazards are necessary.

## What happened (drafting slice)
1. Hard-synced both repos to origin HEAD (idea-engine d75c7f1, sim-lab be4a6bc); bootstrap check --strict exit 0; read inbox/status/outbox at HEAD — no blocking order (ORDER 016/011 satisfied by this task; sim-lab ORDER-010c kit upgrade stays PARKED on owner auth).
2. Verified the baton: control/status.md names the round-20 GAME slot PROPOSAL 091 → VERDICT 104 (+13) as the next slice.
3. Pruned the terminal V103 claim (control/claims/verdict-103-big-pond-badge-inversion.md) after verifying idea-engine #469, #470 and sim-lab #176 all merged live.
4. Wrote and ran a seeded stdlib dry-sim to calibrate the gates; K*=6 interior, R1 61.4σ/43.1σ, R2 exact-hazard unimodal (E[h_frust]≡0 for K≤L0), R3 9/9 interior across p∈{0.10,0.12,0.15}×a±20%, R4 dual control flips to both endpoints; results-dict sha256 15b375c2…. One R3 correction disclosed: the initial p-envelope {0.10,0.15,0.20} put one far corner (p=0.20, a×0.8) at the loose endpoint; tightened to a P090-style modest envelope {0.10,0.12,0.15} centered on the pinned world, with the high-p boundary disclosed in Model basis.
5. Authored ideas/superbot-games/pity-anticipation-collapse-2026-07-17.md (State: sim-ready, full 8-question probe battery, pinned world, disclosed verifier spec, Model basis / P024 declared model-dependence), claimed it in control/claims/, appended PROPOSAL 091 to control/outbox.md exactly once.

## Constraints honored
- TRUTH bar: every gate margin is measured from the dry-sim, not asserted; grounding cites idea-engine@d75c7f1 · fetched this session; SEEDLESS (shared block 20261730 untouched, own SEED=20260718).
- Dedup: distinct object from every game prior — no pity/gacha ceiling, variable-ratio reinforcement, or predictability-vs-drought retention tradeoff exists in the tree (grep-confirmed).
- Model-attribution (ORDER 001): 📊 Model line family-level, PL-004 class idea/planning.
- Heartbeat overwritten LAST before this flip; inbox left to its writer.

## ⟲ Previous-session review
Prior session (V103 fan-in mirror, .sessions/2026-07-17-verdict-103-big-pond-badge-inversion.md): mirrored P090's big-pond badge-starvation inversion APPROVE into idea-engine, all four gates green (R1 242.8σ, R2 445.2σ, R3 7/7 interior, R4 50.2σ), twins agreed, byte-identical double run. Clean: seeded Poisson-thinning reps, twin-evaluator agreement, honest σ-margin ledger. Carried forward here: the seeded-reps / σ-margin discipline and the R4 control-collapse structure — P091's dual (c=0 / a=0) control is the same isolate-the-cause move applied to two hazards. One nit continued: older cards' model-line advisory is cosmetic (check --strict stays exit 0); this card uses the corrected `opus-4.8 · high · idea/planning` form.
