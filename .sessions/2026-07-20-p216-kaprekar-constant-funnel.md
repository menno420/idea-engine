# Session 2026-07-20 — PROPOSAL 216 Kaprekar's-constant universal funnel (round-51 UNRELATED slot)

> **Status:** in-progress

## 💡 Session idea
Kaprekar's routine on 4-digit numbers is a global contraction: every one of the 8991 valid starts funnels to the single constant 6174 in at most 7 steps — an exactly-true fact proven by exhaustion, with a 3-digit → 495 (≤6 steps) dimension-shift control and a seeded Monte-Carlo confirmation. Disclosed results-dict sha256 = 6ef877698bbb91eadffa8473c4a0ec6276f62fd3b8af73fd90855288b38ebf0d.

## ⟲ Previous-session review
Prior slot in rotation was P215 (round-51 GAME slot, Stackelberg commitment; idea-engine HEAD 31185cd at boot). Boot outbox proposal high-water P215; sim-lab at V227. Dedup grep across all lanes (`grep -ril kaprekar ideas/`) returned no dedicated Kaprekar card — head is un-built. High-water advanced P215 → P216 (union-max). This closes round-51 (fleet→venture→game→unrelated); P217 opens round-52 FLEET.

## 🫀 Heartbeat
Left to the coordinator per the single-writer rule (control/status.md is coordinator-owned; not touched here). Claim bundled into commit 1 of this branch: control/claims/claude-p216-kaprekar-funnel.md.

> 📊 Model: Claude Opus 4.8 · high · idea/planning

## Decisions made
- Head chosen: Kaprekar's constant 6174 (UNRELATED domain: recreational number theory), because it is exactly true (exhaustively provable, integer-exact), reproducible stdlib-only, and un-built. Rejected two-envelope (a fallacy, not a true fact), sleeping-beauty/newcomb (philosophically contested, no exact closed form), collatz (unproven).
- Four pre-registered gates: G1 exhaustive convergence + tight bound (max 7), G2 unique fixed point 6174, G3 ≥3σ Monte-Carlo confirmation, G4 3-digit shift → 495 (max 6). Falsifiability leg embedded in G1 (rejects the wrong ≤6 bound).

## Next session should know
P216 → VERDICT 229 (+13 offset). Next slice: P217 opens round-52 FLEET slot. Grounding pins a Wikipedia revision of the Kaprekar article; caveat scoped to what that revision states vs the firsthand exhaustive proof.
