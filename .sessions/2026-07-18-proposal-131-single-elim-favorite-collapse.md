# Session 2026-07-18 — PROPOSAL 131 single-elim favorite-collapse (round-30 GAME slot)

> **Status:** `in-progress`

📊 Model: Claude Opus · effort high · task-class proposal-draft
🔗 GROUNDING: https://github.com/menno420/idea-engine/blob/e8c019308c77396e51aaea9ff398c77bf8b065f5/control/outbox.md

## What
Draft + land round-30 GAME-slot PROPOSAL 131 (single-elimination favorite-collapse; P131 → VERDICT 144, +13). Markdown-first idea doc + committed stdlib verifier (SEED=20260717, three >=3sigma gates, whole-dict sha256).

## 💡 Idea
Each knockout round is an independent Bradley-Terry coin-weighted haircut, so the favorite's title probability = p^R decays geometrically; a 3x-stronger favorite wins a 64-player single-elimination bracket only ~18% of the time — the "bigger tournament is a truer test" folk belief is inverted. Fix: best-of-N per round or a group/Swiss stage, not more single-elim rounds.

## ⟲ Previous-session review
Reviewed the freshest merged cards: P130 annual-prepay financing trap (#561, e8c0193, round-30 VENTURE) and P129 correlated-vote Condorcet jury ceiling (#560, FLEET). Conventions carried forward: GROUNDING real permalink@SHA, probe-report canonical 8-question battery, recommendation line, dated-claim filename prefix, version-less Model line, whole-dict sha256 posture (P123/P127 family). No defects found. This previous-session review discharges the session-card close-out requirement.

## VERIFY
- python3 ideas/superbot-games/single_elim_favorite_collapse.py -> exit 0, three PASS, deterministic double-run digest.
- python3 bootstrap.py check --strict -> green (after flip).
- Outbox P131 block appended (-> V144); status.md heartbeat: proposal HW=P131, baton "next: V144 for P131; then round-30 unrelated-slot P132".
