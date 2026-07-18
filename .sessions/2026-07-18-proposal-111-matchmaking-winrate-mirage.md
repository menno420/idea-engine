# PROPOSAL 111 — the matchmaking win-rate mirage (round-25 GAME slot, P111 → V124, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus 4.x · high · game-proposal

Born in-progress as this session's first commit (born-red HOLD); will flip to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Draft and land the round-25 GAME-slot proposal (P111): one genuinely new, counterintuitive, stdlib-simulable competitive-game mechanism — the matchmaking win-rate mirage, where skill-based matchmaking (SBMM) drives every player's long-run win rate to a skill-independent ~50% fixed point, so the observed win rate carries near-zero information about true skill while the hidden Elo rating recovers it fully; the same games yield one statistic (rating) that ranks skill and another (win rate) that does not — distinct from prior game slots (shop-reroll threshold ruin P099, streak-shield regressivity P103, energy-cap overflow P107, gacha-pity P091, rubber-band/PID P095), with pre-registered ≥3σ /se gates. Fanned to sim-lab as VERDICT 124 (+13).

## Constraints honored
- HARD-SYNC to origin HEAD (idea-engine 0db4bfd) before reading.
- Claim filed before work; born-red card is the first commit (HOLD); PR opened READY immediately; heartbeat before flip; Status→complete is the last commit.
- `python3 bootstrap.py check --strict` green (exit 0) before push.
- Monte Carlo of an N-player SBMM Elo season with a pinned SEED=20260717 and ≥3σ gates; the gate z is on the ESTIMATED MEAN via its standard error se=std/√TRIALS (the P104/P105/P106/P107 /se convention). Stdlib-only verifier (random, math, json, hashlib), no third-party. Model line family-level.

_Close-out (What happened / Previous-session review / Session idea / GROUNDING) written at flip._
