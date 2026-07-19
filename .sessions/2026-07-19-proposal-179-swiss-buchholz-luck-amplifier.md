# PROPOSAL 179 — Swiss-system Buchholz tiebreak is a luck amplifier (round-42 GAME slot, P179 → V192, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card lands `in-progress` on the first commit to hold the PR red under the substrate-gate born-red rule. It flips to `complete` only after the verifier is written, run twice cross-invocation with identical output, and the outbox block is appended. The HOLD clears at that flip.

## Objective

Show by deterministic simulation that the Buchholz tiebreak used to order players tied on match points in a Swiss-system tournament is set far more by opponent-draw luck than by the tied players' own skill (a ≈3× luck-to-skill signal ratio at an even field). Organizers treat Buchholz ("strength of schedule") as a merit tiebreak; the claim is that among equal-score players it ranks the luckier opponent draw ahead of the stronger player.

## Constraints honored

- stdlib-only Python 3 verifier; SEED=20260717 pinned; deterministic.
- in-process double-run assert plus identical cross-invocation stdout.
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture (compact-canonical results-dict sha256 IS the digest; pretty dump indent=2, floats 6 dp).
- >= 3 sigma gates; one robustness gate under a shifted skill distribution.
- grounding pinned to a live Wikipedia revision documenting Buchholz = sum of opponents' scores.

## Gate-plan (pre-registered)

Monte Carlo over many Swiss tournaments (N players, R rounds, Elo-logistic results, rematch-avoiding score pairing). For every unordered pair of players finishing on EQUAL match points (a tied cohort), the Buchholz-winner is the one with higher Buchholz. Per pair record skill_agree (Buchholz-winner also has the higher TRUE skill) and luck_agree (Buchholz-winner also drew the higher summed opponent TRUE skill). Let p_skill, p_luck be their means over all tied pairs.

- **G1 — luck dominates:** p_luck ≥ 0.70 and z_luck = (p_luck − 0.5)/SE ≥ 3.0.
- **G2 — luck beats skill:** base ratio |p_luck−0.5|/|p_skill−0.5| ≥ 3.0, z on the paired difference (luck_agree − skill_agree) ≥ 3.0, and (p_luck − p_skill) ≥ 0.15.
- **G3 — robustness (shifted distribution):** under a wider skill spread (σ 200→350) and larger bracket (N 64→128, R 7→9) the dominance persists: p_luck ≥ 0.70, z_diff ≥ 3.0, and (p_luck − p_skill) ≥ 0.10. The luck/skill *ratio* compresses under wider σ because own skill becomes a more legible tiebreak signal; the systematic dominance does not — G3 tests the dominance, not the ratio.

all_pass = G1 and G2 and G3.

## GROUNDING (verified at HEAD)

Wikipedia, "Tie-breaking in Swiss-system tournaments" — the Buchholz score is the sum of the scores of a player's opponents, a strength-of-schedule measure. The proposal doc carries the exact revision-id pin and the quoted sentence.

## Probe questions

Carried in the proposal doc's `## Probe report` section.

## Outcome

PROPOSAL 179 sim-ready. Verifier `ideas/superbot-games/swiss_buchholz_luck_amplifier.py` runs deterministically (two cross-invocation runs identical), all_pass=true, results-dict sha256 `0e591bb44f57f72fdff6536417a3ba009b74dfb9c07f2c41073bdbd9876c0fa8`. Base (σ=200, N=64, R=7): p_luck=0.80491 vs p_skill=0.597399, ratio=3.130521, z_luck=511.92, z_diff=234.75. Shift (σ=350, N=128, R=9): dominance persists — p_luck=0.870756, gap=0.183947, z_diff=265.70 (the luck/skill ratio compresses to 1.98 under wider σ, disclosed). Grounded to https://en.wikipedia.org/wiki/Swiss-system_tournament@1357112228 (Buchholz = sum of opponents' scores), verified live. Outbox PROPOSAL 179 block appended, proposal high-water P178 → P179, claim released. PR #673, targeting sim-lab VERDICT 192 (+13).

## ⟲ Previous-session review

P178 (post-money SAFE stacking, round-42 VENTURE, PR #672) shipped sim-ready with a convex founder stacking tax x²/(1+x) and very strong gates (z>600). Append-only outbox discipline and born-red HOLD were observed cleanly; no defects noted.

## 💡 Session idea

Companion GAME head — Buchholz vs Sonneborn-Berger as skill proxies: SB weights each win by the beaten opponent's score, so among tied players it may track own skill more and opponent-draw luck less than raw Buchholz. Quantify which tiebreak is the better skill estimator at an even field.
