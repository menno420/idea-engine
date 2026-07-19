# PROPOSAL 183 — kingmaker skill-inversion: a player who can't win but decides the winner flips the sign of skill (P183 → V196, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD (cleared).** This card landed first as `in-progress` to hold the substrate-gate red while the proposal was authored and the verifier proven; this final commit flips it to `complete`, releasing merge-on-green.

## Objective

Author PROPOSAL 183 (round-43 GAME slot): a fresh, counterintuitive, quantifiable game mechanism — the kingmaker skill-inversion — grounded in a real documented phenomenon (the kingmaker scenario in multiplayer game theory), with a stdlib-only deterministic verifier (SEED=20260717, ordered >=3 sigma gates including a robustness gate under a shifted distribution) and a full proposal doc, then land it on green for a future VERDICT 196 (+13 offset).

## Constraints honored

- Stdlib-only verifier; SEED=20260717 pinned; in-process double-run determinism assert.
- Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (compact-canonical sha256, pretty stdout dump).
- Pre-registered ordered gates G1 → G2 → G3 at z_gate = 3.0; the gate plan matches the shipped verifier.
- Grounding URL verified reachable (HTTP 200) and documents the specific head.
- Timestamps from `date -u`.

## GROUNDING (verified at HEAD)

Kingmaker scenario (multiplayer game theory): a player who can no longer win still determines which of the remaining players wins. Grounding pinned in the proposal doc: https://en.wikipedia.org/wiki/Kingmaker_scenario (HTTP 200, oldid 1356902639) — verbatim: "a player who is unable to win has the capacity to determine which player among others will win."

## Gate plan (pre-registered — matches the shipped verifier)

- **G1** — skill is real without the kingmaker: skill-decided final, stronger-contender win rate 0.695125 (z=174.525106) > 0.5 by >=3 sigma.
- **G2** — the inversion: fully spiteful kingmaker eliminates the leader, stronger-contender win rate 0.193235 (z=-274.378957) < 0.5 by >=3 sigma (skill's sign flipped).
- **G3** — robustness (shifted skill spread sigma=1.5, qnoise=0.7, partial spite 0.6): stronger-contender win rate 0.410205 (z=-80.31509) < 0.5 by >=3 sigma, below the baseline 0.695125 (deepens).

## Probe questions

**1. Is the spiteful kingmaker's leader-elimination the right model, or does optimal kingmaker play differ?**
**2. Does the inversion survive a shifted skill spread and partial (0.6) spite, or is it an artifact of full spite?**
**3. Is this distinct from the existing rating-system, bracket-luck, and pie-rule heads in the lane?**
**4. Does the grounding source document a non-winning player DECIDING the winner, not merely a multiplayer game?**

## Outcome

Complete. Verifier proven twice cross-invocation (byte-identical), `all_pass=true`, `first_failing_gate=null`, results-dict sha256 `d928732259d7f54185db3ad5219322166bc2abd9f005667d2b1bd5873451432d`. Gates: G1 z=174.525106 (0.695125), G2 z=-274.378957 (0.193235), G3 z=-80.31509 (0.410205, below baseline 0.695125). Grounding HTTP 200 (Wikipedia "Kingmaker scenario", oldid 1356902639) — documents that a non-winning player decides the winner. Outbox PROPOSAL 183 appended (sim-ready), proposal high-water advanced P182 → P183, targeting VERDICT 196 (+13). `git grep -il kingmaker` across ideas/ returned zero prior hits (dedup clean).

## ⟲ Previous-session review

P182 (pay-to-play cramdown cliff, sibling venture slot, sim-ready) reads sound: clean +13 offset (P182→V195), pinned commit-SHA blob links, deterministic results-dict digest, ordered ≥3σ gates with a cold-market robustness gate. This session mirrored its outbox-block grammar and per-block offset-ledger discipline. No correction needed.

## 💡 Session idea

A companion GAME head worth a future slot: "elimination-order spite cascade" — in a 4+ player sequential-elimination format, each newly eliminated player becomes a kingmaker, so spite compounds across rounds and the survivor is selected more by accumulated grudges than by skill; quantifiable as the decay of skill→placement rank correlation as the number of elimination rounds grows. Distinct from this single-kingmaker head by measuring the multi-round cascade, not the one-shot sign flip.
