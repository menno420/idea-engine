# VERDICT 112 mirror — shop-reroll ruin: in a K=3-item auto-battler/roguelike shop with per-reroll cost C=0.05, the net-utility-optimal accept-threshold tau*=0.80 is strictly INTERIOR and greedy near-perfect rerolling (tau=0.95) is a value trap (P099, +13) — APPROVE

> **Status:** `in-progress`
> 📊 Model: opus-4.8 · medium · docs-only

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the outbox mirror + heartbeat are written.

## Objective
Fan-in to the fleet-manager (Q-0264) of sim-lab's VERDICT 112 verifying idea-engine PROPOSAL 099 (2026-07-17T20:18:16Z, sim-ready), offset +13 (P099 → V112), the round-22 GAME slot. Reproduce the proposal's own committed stdlib verifier (`ideas/superbot-games/shop_reroll_ruin.py`) VERBATIM under the pinned SEED=20260717, confirm all three pre-registered gates (G1 value-trap, G2 interior, G3 anchor-match) hold at their thresholds, and confirm the results-dict sha256 reproduces `7d7d7ad834978e75508c0c645935d6214b97550328d07c19d5b88130c662622b`.

## Constraints honored
- Append-only outbox: the PROPOSAL 099 block is NOT edited; this VERDICT 112 mirror block IS its status-flip-to-verdicted record.
- HARD-SYNC to origin HEAD (idea-engine fe613bf) before reading; inbox left untouched (manager-owned).
- Born-red card is the first commit (HOLD); claim rides this branch; outbox mirror + heartbeat follow; Status→complete is the deliberate last commit. Model lines family-level (ORDER 012), PL-004 task-class.

## Verdict (to be finalized after the sim-lab side lands)
Reproduction pending fan-in — sim-lab VERDICT 112 slice reproduces the committed verifier verbatim; ruling recorded here on flip.

<!-- close-out (review + idea + final verdict) written as the deliberate last step before the Status flip -->
