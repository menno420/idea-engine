# PROPOSAL 107 — energy-cap overflow-forfeiture tax (round-24 GAME slot, P107 → V120, +13)

> **Status:** `in-progress`
> 📊 Model: opus-4.8 · high · idea/planning

Born in-progress as this session's first commit (born-red HOLD); to be flipped to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Draft and land the round-24 GAME-slot proposal (P107): one genuinely new, counterintuitive, stdlib-simulable free-to-play energy/stamina-pacing mechanism — the energy-cap overflow-forfeiture tax, where the fraction of regenerated stamina a player can actually spend saturates as U=1−e^{−C/μ}, so a busy player silently forfeits regen scaling with their absence and raising the cap yields exponentially diminishing returns — distinct from prior game slots (shop-reroll threshold ruin P099, streak-shield regressivity P103, gacha-pity P091, rubber-band/PID P095), with pre-registered ≥3σ gates and an exact closed-form overflow anchor, fanned to sim-lab as VERDICT 120 (+13).

## Constraints honored
- HARD-SYNC to origin HEAD (idea-engine 36f5a6f) before reading.
- Claim filed before work; born-red card is the first commit (HOLD); PR opened READY immediately; heartbeat before flip; Status→complete is the last commit.
- `python3 bootstrap.py check --strict` green (exit 0) before push.
- Monte Carlo of exponential login gaps with a pinned SEED=20260717 and ≥3σ gates against the exact overflow-fraction anchor 1−e^{−C/μ}; the gate z is on the ESTIMATED MEAN via its standard error se=std/√TRIALS (the P104/P105/P106 /se convention). Stdlib-only verifier (random, math, json, hashlib), no third-party. Model line family-level.

## What happened
- (to be completed at flip — dry-sim results, digest, and files land as the deliberate last step)

## ⟲ Previous-session review
- (to be completed at flip)

## 💡 Session idea
- (to be completed at flip)

## GROUNDING
- (to be completed at flip)
