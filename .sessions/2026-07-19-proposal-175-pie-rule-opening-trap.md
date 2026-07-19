# PROPOSAL 175 — pie-rule opening trap: the strongest opening becomes the worst move under the swap rule (P175 → V188, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card lands first as `in-progress` to hold the substrate-gate red while the proposal is authored and the verifier is proven; it flips to `complete` as the final commit.

## Objective

Author PROPOSAL 175 (round-41 GAME slot): a fresh, counterintuitive, quantifiable game-design mechanism grounded in a real documented phenomenon (the pie / swap rule), with a stdlib-only deterministic verifier (SEED=20260717, ordered ≥3σ gates including a robustness gate under a shifted distribution) and a full proposal doc, then land it on green for a future VERDICT 188 (+13 offset).

## Constraints honored

- Stdlib-only verifier; SEED=20260717 pinned; in-process double-run determinism assert.
- Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (compact-canonical sha256, pretty stdout dump).
- Pre-registered ordered gates G1 → G2 → G3 at z_gate = 3.0; the gate plan below matches the verifier's shipped gates.
- Grounding URL verified reachable (HTTP 200) and documents the specific head.
- Timestamps from `date -u`.

## GROUNDING (verified at HEAD)

Pie rule / swap rule (Hex and other first-player-advantage games): the second player may, in lieu of a reply, swap sides — so the first player is incentivized to make a balanced opening rather than a strong one. Reference pinned in the proposal doc's Grounding line.

## Gate plan (pre-registered — matches the shipped verifier)

- **G1** — first-move edge exists without the rule: greedy-strongest opening, no pie rule, win rate > 0.5 by ≥3σ vs 0.5.
- **G2** — the trap: greedy-strongest opening UNDER the pie rule yields realized first-mover win rate < 0.5 by ≥3σ (the responder swaps into the strong opening).
- **G3** — robustness (shifted opening distribution): balanced play (f≈0.5) strictly dominates naive-strong play by ≥3σ, and the balanced realized rate is within 2 percentage points of a fair 0.5.

## Probe questions

**1.** Is `min(f, 1−f)` the correct realized value under the swap rule, or does optimal responder play differ?
**2.** Does the head survive a shifted opening catalogue, or is it an artifact of the chosen f-values?
**3.** Is this distinct from the existing first-mover / responder-edge heads (Penney game) in the fleet lane?
**4.** Does the grounding source document the incentive to play balanced, not merely the swap mechanic?

## Outcome

_Pending — flips to complete after the verifier is proven twice cross-invocation, the outbox block is appended, and the heartbeat is refreshed._

## ⟲ Previous-session review

_(to be filled at flip)_

## 💡 Session idea

_(to be filled at flip)_
