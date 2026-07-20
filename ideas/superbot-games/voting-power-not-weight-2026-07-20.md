# Voting power is not voting weight — a 50-49-1 split gives the 49-bloc exactly the same power as the 1-bloc

> **State:** sim-ready
> **Class:** superbot-games · mechanism design / voting power · Banzhaf & Shapley–Shubik indices
> **Target:** sim-lab (VERDICT 216, +13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Banzhaf_power_index&oldid=1347671339@ec2eab5bed81ab8f7385fe3dfd4b758ae507b79e · fetched 2026-07-20T08:08:06Z
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/superbot-games/voting-power-not-weight-2026-07-20.py` (hashlib, json, sys, random, itertools, math, fractions.Fraction) — results-dict sha256 660bb1e5… (full 64 hex in Dry-sim below).

## The phenomenon (one line)
In the weighted majority game [51; 50, 49, 1] the 49-weight bloc has exactly the same voting power as the 1-weight bloc (Banzhaf ⅕ each), while the near-identical 50-weight bloc holds ⅗ — a 2% weight edge buys three times the power, and a 48-weight gap buys none.

## The folk belief
"Give a bloc more votes and it gets proportionally more say; voting weight is voting power." Seat allocations, share-weighted votes, and council quotas are routinely designed as if power scaled with weight.

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
Power in a weighted vote is a voter's frequency of being *pivotal* — of turning a losing coalition into a winning one — not their weight. That frequency is a step function of the quota geometry, so it is wildly non-linear in weight: two very differently-weighted voters can be pivotal in exactly the same coalitions (equal power), and a positive-weight voter can be pivotal in NONE (a "dummy" with real votes and zero power). Any system that assigns influence by weight — DAO share-voting, guild-council seats, weighted alliance votes, board quotas — is therefore mis-pricing influence unless it is designed against the *power index*, not the weight. Worse, the two textbook power indices (Banzhaf, Shapley–Shubik) disagree on the numbers, so "how much power does this bloc have" has no single canonical answer.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Weighted game [q; w_1..w_n]: coalition S wins iff Σ_{i∈S} w_i ≥ q. Majority quota q = ⌊Σw⌋/2 + 1.
- Voter i swings in S (i∉S) iff S loses and S∪{i} wins. Banzhaf swing count = #such S; normalized Banzhaf = swings_i / Σ swings. Shapley–Shubik = Σ_{S swing for i} |S|!(n−1−|S|)!/n!.
- Dummy = positive weight, zero swings. Power/weight ratio = (power-share) ÷ (weight-share).

## Pinned world (committed constants)
SEED = 20260717 · Z_GATE = 3.0 · headline instance [51; 50,49,1] · exhaustive n=4 sweep over all weights ∈ {1..6}^4 (1296 games, majority quota) · robustness sample n ∈ {5,6,7}, weights 1..20, 1000 each. Digest recipe: sha256 of `json.dumps(results, sort_keys=True, separators=(",",":"))`, exact Fractions serialized as "num/den" strings, floats rounded to 6 dp, whole results dict, stdout-only, no self-referential sha field.

## Pre-registered gates (sim-ready iff ALL hold, in order G1 -> G2 -> G3 -> G4)
- **G1 — the headline instance (EXACT; direction: exact fraction equality).** For [51; 50,49,1], normalized Banzhaf = (3/5, 1/5, 1/5) and Shapley–Shubik = (2/3, 1/6, 1/6) exactly; the 49-bloc equals the 1-bloc under both indices. Banzhaf swings agree brute-force vs generating-function DP (closed-form vs enumeration).
- **G2 — power ≠ weight, exhaustively (EXACT; direction: counts > 0, methods agree).** Over all 1296 n=4 majority games: positive-weight dummies occur (count > 0), the max power-share ÷ weight-share strictly exceeds 1, and brute-vs-DP Banzhaf agree for every game.
- **G3 — the two indices disagree (EXACT; direction: count > 0).** Over the same sweep, the Banzhaf and Shapley–Shubik normalized vectors differ in a nonzero number of games; the max L1 gap is pinned.
- **G4 — large-voter premium (robustness + ≥3σ; direction: mean > 0).** Over the seeded n ∈ {5,6,7} sample, the top voter's Banzhaf power-share minus its weight-share has strictly positive mean with z ≥ 3.0.

## Pre-registered decision rule
APPROVE (VERDICT 216) iff an independent sim-lab re-implementation reproduces `results_sha256` byte-for-byte AND all four gates hold in order. Any gate failing, or any digest mismatch, is a REJECT.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
G1: PASS
G2: PASS
G3: PASS
G4: PASS
all_pass: True
```
- **G1** headline [51; 50,49,1] quota 51: normalized Banzhaf = ["3/5", "1/5", "1/5"], Shapley–Shubik = ["2/3", "1/6", "1/6"], methods_agree = true → the 49-bloc equals the 1-bloc under both indices, the 50-bloc holds 3× (Banzhaf).
- **G2** over 1296 n=4 games: dummy_count = 540 (first dummy game [[1,1,1,4], quota 4]), methods_agree_all = true, max_power_weight_ratio = 5/2 at game [[1,2,6,6], quota 8] (> 1).
- **G3** over 1296 n=4 games: index_unequal_count = 80, max_index_l1 = 1/10 at game [[1,1,1,3], quota 4].
- **G4** sample = 3000: mean_power_minus_weight_share = 0.033793, sem = 0.001295, z = 26.104016 (mean > 0, z ≥ 3.0).

**Disclosed results-dict sha256 = 660bb1e59107c98a1b10256d3dfa195346a02298cba9753a9aef3e2281ece254**

## Verifier
`swings_brute()` counts each voter's swing coalitions by full subset enumeration; `swings_dp()` recomputes the same counts via an exact weight generating-function (cross-check); `banzhaf_norm()` and `shapley_shubik()` return exact-Fraction normalized indices; `gate1()` pins the [51;50,49,1] instance; `gate23()` sweeps all 1296 n=4 majority games for dummies, the max power/weight ratio, and Banzhaf-vs-Shapley disagreement; `gate4()` runs the seeded large-voter-premium sample; `main()` double-runs `build_results()` in-process (aborts exit 3 on divergence) before emitting the digest.
Reproduce:
```
python3 ideas/superbot-games/voting-power-not-weight-2026-07-20.py
```
Expected output ends with `all_pass: True` and `results_sha256: 660bb1e59107c98a1b10256d3dfa195346a02298cba9753a9aef3e2281ece254` (exit 0). A separate second invocation reproduces the identical digest (cross-invocation determinism).

## Why it matters (game design)
Weighted voting is everywhere in live systems: DAO share-votes, guild/alliance councils, weighted-stake governance, board quotas. This says influence must be designed against the power index, not the vote weight — otherwise a bloc can be handed real weight and zero power (a dummy), or two blocs with a 48× weight difference can wield identical influence. And because Banzhaf and Shapley–Shubik disagree, any governance spec must name WHICH power measure it targets.

## Dedup
Distinct from every existing head: this is coalition-pivotality power measurement, not auction truthfulness (P199 vickrey), matching (fleet deferred-acceptance), routing (fleet braess / price-of-anarchy), social choice tallies (fleet condorcet / irv / delegation — those count votes, they do not compute a power index), or zero-sum matrix value (superbot-games balance-triangle). `git grep -il` for banzhaf / "shapley value" / "power index" / "voting power" returns nothing on the power-index mechanism prior to this doc. Pivot note: this session first drafted Parrondo's paradox and the Gale–Shapley duality, found both already sim-ready in ideas/fleet/, and pivoted here after a full cross-lane dedup scan.

## Model basis (declared model-dependence — the P024 discipline)
Depends on: simple weighted majority games (win iff Σweights ≥ ⌊Σw⌋/2+1), power defined as pivotality (Banzhaf swing frequency / Shapley–Shubik order-pivot share). Under this standard model the results are theorems: the [51;50,49,1] indices are exact rationals, and the dummy / disproportion / index-disagreement phenomena are confirmed by exhaustive enumeration of the whole n=4 weight cube, not sampled.

## One-line design fix
Design weighted-governance influence against the power index (Banzhaf or Shapley–Shubik — and say which), never against raw vote weight; audit every proposed weight vector for dummies and disproportion before shipping it.

## Probe report (v0, 2026-07-20)
**1. What is this really?** The Banzhaf/Shapley–Shubik power-index result: a voter's power is their frequency of being pivotal, which is a step-function of the quota geometry and therefore not proportional to weight — canonically, [51;50,49,1] gives the 49-bloc and 1-bloc equal power.
**2. Is it genuinely surprising / counterintuitive?** Yes — "more votes = more power, proportionally" is the near-universal intuition; that a 49-weight bloc equals a 1-weight bloc, and that a positive-weight voter can have zero power, violates it directly.
**3. Is it TRUE (exactly, under a clean model)?** Yes. The indices are exact rationals: (3/5,1/5,1/5) Banzhaf and (2/3,1/6,1/6) Shapley–Shubik for the headline game, and the dummy / disproportion / index-disagreement facts are verified by exhaustive enumeration of all 1296 n=4 majority games — no floats in any sign or equality decision.
**4. Is it reproducible deterministically with stdlib only?** Yes — hashlib/json/sys/random/itertools/math/fractions only, SEED=20260717, exact Fraction arithmetic, in-process double-run guard plus a byte-identical second invocation; the results-dict sha256 is disclosed. Banzhaf is independently cross-checked brute-vs-DP.
**5. What would REFUTE it?** The [51;50,49,1] indices differing from the committed fractions; brute and DP Banzhaf disagreeing on any game; zero dummies or a max power/weight ratio ≤ 1 in the sweep; the two indices never differing; or a non-positive / sub-3σ large-voter premium.
**6. Is it distinct from every prior head (dedup)?** Yes — no prior head computes a coalition power index; the grep is clean. See Dedup (and the Parrondo / Gale–Shapley pivot note).
**7. Is the grounding real and specific to this head?** Yes — the pinned Wikipedia revision (Banzhaf power index, oldid 1347671339) documents Banzhaf power being non-proportional to weight: it gives an example where three differently-weighted states each hold exactly 1/3 of the power, and a California example where a positive-electoral-vote state holds power 1 while the others are dummies at 0. Caveat: the article's worked examples use electoral-vote weights, not the exact 50-49-1 triple — our [51;50,49,1] is a standard textbook instance of the same non-proportionality (equal power across unequal weights) the article documents.
**8. What does it unblock / why does sim-lab care?** It gives the fleet an exactly-verified warning — with a reusable exact power-index harness — that weighted-governance influence (DAO/guild/board votes) must be priced by power index, not weight, and that the choice of index is itself load-bearing.

**Recommendation: sim-ready**
