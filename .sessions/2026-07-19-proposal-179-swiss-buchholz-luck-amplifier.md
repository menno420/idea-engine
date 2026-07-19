# PROPOSAL 179 — Swiss-system Buchholz tiebreak is a luck amplifier (round-42 GAME slot, P179 → V192, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card lands `in-progress` on the first commit to hold the PR red under the substrate-gate born-red rule. It flips to `complete` only after the verifier is written, run twice cross-invocation with identical output, and the outbox block is appended. The HOLD clears at that flip.

## Objective

Show by deterministic simulation that the Buchholz tiebreak used to order players tied on match points in a Swiss-system tournament is set almost entirely by opponent-draw luck, not by the tied players' own skill. Organizers treat Buchholz ("strength of schedule") as a merit tiebreak; the claim is that among equal-score players it ranks the luckier opponent draw ahead of the stronger player.

## Constraints honored

- stdlib-only Python 3 verifier; SEED=20260717 pinned; deterministic.
- in-process double-run assert plus identical cross-invocation stdout.
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture (compact-canonical results-dict sha256 IS the digest; pretty dump indent=2, floats 6 dp).
- >= 3 sigma gates; one robustness gate under a shifted skill distribution.
- grounding pinned to a live Wikipedia revision documenting Buchholz = sum of opponents' scores.

## Gate-plan (pre-registered)

Monte Carlo over many Swiss tournaments (N players, R rounds, Elo-logistic results, rematch-avoiding score pairing). For every unordered pair of players finishing on EQUAL match points (a tied cohort), the Buchholz-winner is the one with higher Buchholz. Per pair record skill_agree (Buchholz-winner also has the higher TRUE skill) and luck_agree (Buchholz-winner also drew the higher summed opponent TRUE skill). Let p_skill, p_luck be their means over all tied pairs.

- **G1 — luck dominates:** p_luck >= 0.70 and z = (p_luck - 0.5)/SE >= 3.0.
- **G2 — skill signal is weak (ratio):** |p_luck - 0.5| / |p_skill - 0.5| >= 3.0, z on the paired difference (luck_agree - skill_agree) >= 3.0, and p_skill within +/-0.10 of a coin flip.
- **G3 — robustness (shifted distribution):** repeat under a wider skill spread (sigma 200 -> 350) and a larger bracket (N 64 -> 128, R 7 -> 9); G1 and the G2 ratio persist, each z >= 3.0.

all_pass = G1 and G2 and G3.

## GROUNDING (verified at HEAD)

Wikipedia, "Tie-breaking in Swiss-system tournaments" — the Buchholz score is the sum of the scores of a player's opponents, a strength-of-schedule measure. The proposal doc carries the exact revision-id pin and the quoted sentence.

## Probe questions

Carried in the proposal doc's `## Probe report` section.

## Outcome

Filled at flip.

## ⟲ Previous-session review

Filled at flip.

## 💡 Session idea

Filled at flip.
