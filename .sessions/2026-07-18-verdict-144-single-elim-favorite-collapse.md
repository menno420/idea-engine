# Session 2026-07-18 — VERDICT 144 single-elim favorite-collapse (round-30 GAME slot, P131 → V144, +13)

> **Status:** `in-progress`

📊 Model: Claude Opus · effort high · task-class review/verify
🔗 GROUNDING: https://github.com/menno420/idea-engine/blob/cf2e20fa69eb04b243b5a553d7270739e6f96c43/ideas/superbot-games/single_elim_favorite_collapse.py

Born red by design: this card lands `in-progress` in the FIRST commit so the substrate HOLD holds the mirror PR red until the sim-lab reproduction is proven and independently audited; the deliberate LAST commit (a later step) flips it to `complete`. This born-red HOLD is the ONLY reason the gate reads red pre-flip.

## What
Mirror round-30 GAME-slot VERDICT 144 (P131 single-elimination favorite-collapse → V144, +13) back into idea-engine after sim-lab reproduces the pinned run. Claim staked; sim-lab reproduction in flight (branch `claude/verdict-144-favorite-collapse`, off sim-lab origin/main `71fd8fb`). Idea-engine outbox/card/status mirror is the deferred close-out step — not performed by this red-hold commit.

## 💡 Idea
Each knockout round is an independent Bradley-Terry coin-weighted haircut, so the favorite's title probability = p^R decays geometrically; a 3x-stronger favorite (p=0.75) wins a 64-player single-elimination bracket only ~18% of the time (0.75^6=0.177978) — the "bigger tournament is a truer test" folk belief is inverted. Fix: best-of-N per round or a group/Swiss stage, not more single-elim rounds.

## ⟲ Previous-session review
Prior loop landed VERDICT 145 (P132 the birthday-collision √N scaling law, round-30 UNRELATED slot closer, sim-lab PR #218 `71fd8fb`) — APPROVE, byte-identical reproduction. DIGEST-POSTURE carry-forward: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (results dict carries no `results_sha256`, no file written, compact-canonical serialization is the digest preimage; stdout dump is the pretty indent=2 form) — carries straight to V144. Object shift: V145 was a first-collision waiting-time / occupancy object; this V144 is a knockout order-statistics / geometric-decay object (favorite title probability p^R). NON-CONTIGUITY: V144 (P131) precedes V145 on the ledger and was STILL PENDING at V145 close — this slice closes it.

## VERIFY
- python3 ideas/superbot-games/single_elim_favorite_collapse.py -> exit 0, three PASS, deterministic double-run; results-dict sha256 002806188054a6eb2f768208f52629d0a3bd0d14624e0489e480efcf86c2a0f2.
- sim-lab reproduction: byte-identical verifier copy (sha256 7bb7611f…), disclosed digest reproduced, G1/G2/G3 PASS in order.
- python3 bootstrap.py check --strict -> green (after flip; deferred close-out step).
