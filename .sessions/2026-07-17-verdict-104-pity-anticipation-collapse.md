# VERDICT 104 (mirror) — pity-timer anticipation collapse: PROPOSAL 091 confirmed APPROVE by sim-lab

> **Status:** `in-progress`
> 📊 Model: opus-4.8 · high · verdict-mirror

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the heartbeat.

## Objective
Fan-in mirror of sim-lab VERDICT 104 (PR #177) into this repo's outbox + heartbeat, for the fleet-manager (Q-0264). The sim ran sim-lab-side; this half records the verdict, prunes the terminal P091 claim, and advances the loop baton. Numbering P091 → VERDICT 104 (+13).

## What happened
sim-lab's independent stdlib-only reimplementation (not the P091 dry-sim) reproduced the retention sweep + hazard surface to the decimal and returned **APPROVE**, all four gates clear, twins agree APPROVE, 16/16 self-checks, byte-identical double run.

- R1 argmax retention K*=6 beats the tightest pity Kmin=2 by 61.4σ and the loosest Kmax=16 by 43.1σ.
- R2 exact per-cycle E[h_total] unimodal with its unique minimum at K=6; E[h_frust]≡0 for all K≤L0=6.
- R3 robust: 9/9 sweep worlds interior (eight land K*=6; the ninth, p=0.15 / a×0.8, lands K14).
- R4 dual control: c=0 → argmax collapses to the tight endpoint K*=2 (interior peak gone); a=0 → argmax collapses to the loose endpoint K*=16 by 31.6σ over K=14.

Non-gating finding (disclosed-anchor defect): the proposal's disclosed first-12 fixture anchor L=[4,6,6,6,6,3,6,6,6,6,6,6] does NOT reproduce under the registered per-(K,rep) stream; the actual reproducible anchor is L=[4,6,6,6,4,6,6,6,6,6,6,5]. The committed fixtures.json carries the actual anchor; the mechanism is unaffected — a proposal-side fixture transcription defect. Recommend correcting the proposal's disclosed anchor in ideas/superbot-games/pity-anticipation-collapse-2026-07-17.md.

Digests (sim-lab sims/verdict-104-pity-anticipation-collapse/): results.json `7e8d0ac6…`, run-stdout.txt `d42c6368…`, fixtures.json `4697f91c…`.

## Constraints honored
- One repo per PR: sim + fixtures landed in sim-lab (#177, merged); this PR is the idea-engine mirror + heartbeat only.
- Independent implementation from the registered spec; verdict follows the pre-registered R1→R4 rule, not softened.
- Claim rides this PR; the terminal P091 drafting claim is pruned here (its work PR #471 is merged, verified live at HEAD f8f9854).

## ⟲ Previous-session review
P091 (round-20 game slot) landed sim-ready on main via #471 (HEAD f8f9854); its idea file, outbox block, and session card are all on main. V103 mirror (#470) landed terminal — round-19 closed, claim pruned. No regressions.

## 💡 Session idea
The pity ceiling K has an interior retention optimum because a tight ceiling floods the schedule with predictable forced rewards (variable-ratio anticipation collapse → boredom churn) while a loose ceiling lets long droughts drive frustration churn — removing either hazard (c=0 or a=0) collapses the optimum to the opposite endpoint. Natural follow-ups (each named, none in scope): a two-currency pity (soft + hard ceiling interaction) and a heterogeneous-player mixture (frustration-tolerance distribution).

📊 Model: opus-4.8 · high · verdict-mirror
