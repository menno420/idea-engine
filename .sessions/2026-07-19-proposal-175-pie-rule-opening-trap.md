# PROPOSAL 175 — pie-rule opening trap: the strongest opening becomes the worst move under the swap rule (P175 → V188, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD (cleared).** This card landed first as `in-progress` to hold the substrate-gate red while the proposal was authored and the verifier proven; this final commit flips it to `complete`, releasing merge-on-green.

## Objective

Author PROPOSAL 175 (round-41 GAME slot): a fresh, counterintuitive, quantifiable game-design mechanism grounded in a real documented phenomenon (the pie / swap rule), with a stdlib-only deterministic verifier (SEED=20260717, ordered ≥3σ gates including a robustness gate under a shifted distribution) and a full proposal doc, then land it on green for a future VERDICT 188 (+13 offset).

## Constraints honored

- Stdlib-only verifier; SEED=20260717 pinned; in-process double-run determinism assert.
- Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (compact-canonical sha256, pretty stdout dump).
- Pre-registered ordered gates G1 → G2 → G3 at z_gate = 3.0; the gate plan matches the shipped verifier.
- Grounding URL verified reachable (HTTP 200) and documents the specific head.
- Timestamps from `date -u`.

## GROUNDING (verified at HEAD)

Pie rule / swap rule (Hex and other first-player-advantage games): the second player may, in lieu of a reply, swap sides — so the first player is incentivized to make a balanced opening rather than a strong one. Grounding pinned in the proposal doc: https://en.wikipedia.org/wiki/Pie_rule (HTTP 200, oldid 1200819498, content hash 681de3e5…).

## Gate plan (pre-registered — matches the shipped verifier)

- **G1** — first-move edge exists without the rule: greedy-strongest opening, no pie rule, win rate 0.900505 (z=598.381968) > 0.5 by ≥3σ.
- **G2** — the trap: greedy-strongest opening UNDER the pie rule yields realized first-mover win rate 0.10111 (z=−591.72081) < 0.5 by ≥3σ.
- **G3** — robustness (shifted opening distribution): balanced play (0.50116) beats naive-strong (0.04946) by gap 0.4517 (z_gap=370.907761) ≥3σ, and the balanced rate is within 2 points of a fair 0.5.

## Probe questions

**1.** Is `min(f, 1−f)` the correct realized value under the swap rule, or does optimal responder play differ?
**2.** Does the head survive a shifted opening catalogue, or is it an artifact of the chosen f-values?
**3.** Is this distinct from the existing first-mover / responder-edge heads (Penney game) in the fleet lane?
**4.** Does the grounding source document the incentive to play balanced, not merely the swap mechanic?

## Outcome

Complete. Verifier proven twice cross-invocation (byte-identical), `all_pass=true`, `first_failing_gate=null`, results-dict sha256 `72950442cc7509423256f28470c2281c9f79de3b601611b9feb931d083e8cb08`. Gates: G1 z=598.381968, G2 z=−591.72081, G3 z_gap=370.907761 (balanced 0.50116 within 2pt of fair). Grounding HTTP 200 (Wikipedia "Pie rule", oldid 1200819498) — documents the swap mechanic and the balanced-opening incentive. Outbox PROPOSAL 175 appended (sim-ready), proposal high-water advanced P174 → P175, targeting VERDICT 188 (+13). Landed on green via merge-on-green, PR #665.

## ⟲ Previous-session review

P174 (IRR speed-trap, sibling, sim-ready) reads sound: clean +13 offset, pinned grounding, deterministic digest. This session mirrored its outbox-block grammar and per-block offset-ledger discipline. No correction needed.

## 💡 Session idea

A companion GAME head worth a future slot: "auction-draft winner's overpay" — in a blind pick-and-ban draft auction, the player who wins a contested pick systematically overpays relative to the pick's marginal roster value (a winner's-curse variant scoped to draft economies), quantifiable as the expected value gap between the winning bid and the second-highest valuation. Distinct from the term-sheet winner's-curse (venture lane) by being about roster-slot marginal value, not equity price.
