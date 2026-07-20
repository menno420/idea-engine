# PROPOSAL 191 — Penney's game second-mover advantage: in a fair-coin sequence duel, committing FIRST to a length-3 H/T pattern is a losing move — for every one of the 8 patterns player 1 can pick, player 2 has a reply that wins strictly more than half the time (worst case HTT, still 2:1 to HHT), so the "appears-first" relation is NON-TRANSITIVE and there is no best sequence (round-45 GAME slot, P191 → V204, +13)

> **Status:** complete
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD — intended.** This card lands on the FIRST commit with `Status: in-progress`, holding the substrate-gate red while the verifier + doc are authored and proven. The flip to `complete` (last commit, after the outbox ledger) releases that HOLD (merge-on-green); the earlier gate-red is the born-red exception, not a defect.

## Objective
Show, with a deterministic stdlib simulation, that a two-player Penney's game on a fair coin is decided by COMMITMENT ORDER: for every length-3 pattern the first player commits to, the second player has a standard reply R(p) = (¬p2) p1 p2 that appears first with probability strictly above 1/2 (exact 2/3 to 7/8), so no pattern is undominated and the "appears-first" tournament is non-transitive. The exact odds come from an absorbing Markov chain over the last L-1 flips; a seeded Monte-Carlo reproduces them. The effect survives lengthening the patterns to L=4 (edge shrinks but stays strictly positive).

## Constraints honored
- stdlib-only (`random, math, json, hashlib`); Python 3.
- SEED = 20260717 pinned; fully deterministic (base seed SEED, shift seed SEED+1).
- Exact ground truth (absorbing Markov chain, Gaussian elimination) cross-checked against seeded Monte-Carlo (G4), so the "exactly true" odds are firsthand, not asserted.
- In-process double-run determinism asserted (`compute()` run twice → identical canonical dict); two cross-invocation runs byte-identical.
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest: sha256 of the compact-canonical results dict IS the digest; the dict carries no self-referential sha field; no on-disk JSON.
- Pre-registered ordered gates G1→G2→G3→G4, matching the shipped verifier exactly.
- Grounding line resolves live (raw-file-at-SHA fetch, HTTP 200).
- Timestamps from `date -u`.

## Pinned world (committed constants — sim-lab must reproduce exactly)
SEED = 20260717 · BASE_L = 3 · SHIFT_L = 4 · TRIALS = 30000 · P_HEADS = 0.5 · optimal reply R(p) = (1−p[1],)+p[:L−1] · Z_GATE = 3.0 · SIGN_FRAC = 1.0 · MIN_EDGE = 0.05 · EXACT_TOL = 0.02 · floats 6 dp · whole-dict / no-self-field / stdout-only. Base regime: L=3, 8 first-picks, rng seed SEED. Shift regime: L=4, 16 first-picks, rng seed SEED+1. First player ranges over all 2^L patterns; second player answers each with R(p); player-2 win = its pattern appearing before player 1's.

## Gate-plan (pre-registered — must match the shipped verifier; z_gate = 3.0)
- **G1 — second player always wins (≥3σ).** Across all 8 base first-picks, the minimum z of (MC player-2 win rate − 0.5) ≥ Z_GATE = 3.0.
- **G2 — universal + material.** favor_frac (fraction of first-picks with edge > 0) ≥ SIGN_FRAC = 1.0 AND min edge ≥ MIN_EDGE = 0.05.
- **G3 — robust to a structural shift (≥3σ).** At L=4 (seed SEED+1): min z ≥ 3.0 AND all 16 first-picks favor player 2 (same sign as base).
- **G4 — exactly true.** For every first-pick in both regimes, |MC win rate − exact Markov odds| ≤ EXACT_TOL = 0.02.

all_pass = G1 ∧ G2 ∧ G3 ∧ G4.

## GROUNDING (verified live at HEAD)
Penney's game (Walter Penney, 1969) is the standard example of non-transitive waiting times: for a fair coin and length-3 patterns, whichever pattern the first player names, the second player can name one that appears first with probability ≥ 2/3; Conway's leading-number algorithm gives the exact odds, and the "beats-more-than-half" relation among patterns contains a cycle (no dominant sequence). The mechanism is pattern overlap: first-appearance depends on self- and cross-overlap, not on the (uniform) fixed-window probability. This card grounds the claim FIRSTHAND — an exact absorbing-Markov-chain solver (the last L-1 flips are a sufficient statistic for length-L completion) whose odds are reproduced by a seeded Monte-Carlo to within 0.0071 (G4). Machine grounding line pins idea-engine main at `45ad3eb` (house provenance convention), verified live this session via raw-file-at-SHA fetch (HTTP 200). Honest caveat: the pinned URL is a repo provenance/reachability pin, not a content citation of Penney's game; the substantive support is the standard Penney/Conway theorem plus this card's reproducible exact+Monte-Carlo verifier, which is stronger firsthand evidence than any single citation.

## Probe questions
**1.** Does the base-regime minimum z (over all 8 first-picks) clear ≥ 3.0 under SEED = 20260717?
**2.** Do ALL first-picks favor player 2 (favor_frac = 1.0) with minimum edge ≥ 0.05?
**3.** Does the L=4 shift (seed SEED+1) keep min z ≥ 3.0 and all 16 first-picks favoring player 2?
**4.** Does the cross-invocation double run reproduce the results-dict sha256 byte-for-byte?
**5.** Does the in-process double-run assertion hold (compute() twice → identical canonical dict)?
**6.** Do the Monte-Carlo win rates match the exact absorbing-Markov odds to within EXACT_TOL = 0.02 for every first-pick (G4)?
**7.** Is the effect caused by second-mover commitment specifically — i.e. would simultaneous blind commitment erase the edge?
**8.** Are the pre-registered gates here identical to the gates the verifier ships?

## Outcome
Measured — all four gates PASS; born-red HOLD cleared at this flip. Verifier `ideas/superbot-games/penney_game_second_mover_advantage.py` + doc `ideas/superbot-games/penney-game-second-mover-advantage-2026-07-20.md` authored and proven; outbox PROPOSAL 191 block targets sim-lab VERDICT 204 (P191 → V204, +13).
- Results-dict sha256: `8942324fa0c31abf11a053bb56b98306709611f73b9a2ad344fe0034d87744f4` (byte-identical across two cross-invocation runs)
- G1 second-player-always-wins: base min z = 58.90958 (≥ 3σ, PASS)
- G2 universal + material: favor_frac 1.0, min edge 0.161 (≥ 1.0 and ≥ 0.05, PASS)
- G3 robust (L=4 shift): min z = 27.726515, all 16 favor player 2 (PASS)
- G4 exactly-true: base max |MC−exact| 0.007067, shift 0.005933 (≤ 0.02, PASS)
- all_pass = `true`; exit 0
- Grounding: https://github.com/menno420/idea-engine@45ad3eb resolved live (raw-file-at-SHA, HTTP 200).
- Targets sim-lab VERDICT 204 (P191 → V204, +13).

## ⟲ Previous-session review
PROPOSAL 190 (positive-EV ruin / ergodicity, round-45 VENTURE slot, sim-ready, targets V203, +13, landed at PR #705): under a multiplicative repeated bet with positive expected value, the time-average growth rate is negative, so the typical (median) investor is ruined even though the ensemble mean grows — the ergodicity gap. This P191 takes the round-45 GAME slot (rotation FLEET → VENTURE → GAME → UNRELATED); no blocker seen. Note round-45 FLEET (P189 ski-rental keep-warm → V202) already ruled on the sim-lab side at 067bcfa.

## 💡 Session idea
Companion GAME head for a future slot: **the intransitive-dice draft trap** — offer players a sequential pick from a set of Efron-style non-transitive dice (A beats B beats C beats A), and show that a drafter who picks FIRST from the "strongest-looking" die is beaten by the second picker more than half the time regardless of which die they take, so first-pick in a dice draft is a structural disadvantage exactly as in Penney's game; simulate the round-robin win matrix (exact enumeration) plus a seeded head-to-head Monte-Carlo, gate the second-picker edge at ≥3σ with a 4-dice robustness shift. Stdlib-checkable; same non-transitivity family, different mechanism (dice faces vs sequence overlap).

(End of card content.)
