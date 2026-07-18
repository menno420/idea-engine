# PROPOSAL 131 — the single-elimination favorite-collapse: each knockout round is an independent coin-weighted haircut, so a 3x-stronger favorite wins a 64-player bracket only ~18% of the time — the "bigger tournament is a truer test" folk belief is inverted; the fix is best-of-N rounds or a group stage.

> **State:** sim-ready
> **Class:** superbot-games · competitive-format design / order statistics
> **Anchor:** Bradley-Terry (1952); Ryvkin & Ortmann (2008), *Management Science* 54(3), single-elimination selection efficiency
> **Target:** sim-lab (VERDICT 144, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@e8c0193 · fetched 2026-07-18T10:26:15Z
> **Reference (external, reachable):** [Bradley-Terry model — Wikipedia](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model) — verified reachable 2026-07-18
> **Verifier (firsthand):** `ideas/superbot-games/single_elim_favorite_collapse.py` · results-dict sha256 `002806188054a6eb2f768208f52629d0a3bd0d14624e0489e480efcf86c2a0f2`

## The phenomenon (one line)
In a single-elimination bracket the strongest entrant must win *every* round, so its title probability is the product of its per-match win probabilities — a quantity that shrinks geometrically as the bracket grows.

## The folk belief
"A bigger, longer tournament is a truer test — more rounds means the cream rises and the best player is more likely to win the whole thing." Designers add rounds and expand brackets to make a format feel more legitimate.

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
Model each entrant by a Bradley-Terry strength theta; a match between strengths a and b is won by a with probability a/(a+b). Put one favorite at strength f>1 and a field of identical "normal" entrants at strength 1. Because the normals are indistinguishable, whoever the favorite draws each round is a normal, so its per-match win probability is the constant **p = f/(f+1)** — *every round, at every bracket size, under any seeding.* The favorite wins the title iff it wins all R = log2(N) matches:

    P_title(R) = p^R,   p = f/(f+1).

This is strictly decreasing in R: adding a round cannot raise the favorite's title odds, it multiplies them by p<1. So a "longer test" makes it *more* likely a normal is crowned, not less. With f=3 (a 3x dominant favorite, p=0.75): a 16-player bracket (R=4) -> **31.6%**; a 64-player bracket (R=6) -> **17.8%**; a 256-player bracket (R=8) -> **10.0%**. The best player is dethroned in the large majority of runs, and it gets *worse* the "truer" you make the test.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Entrants: N = 2^R — one favorite (strength f = 3.0), N-1 normals (strength 1.0).
- Match: Bradley-Terry, P(a beats b) = a/(a+b); favorite-vs-normal => p = 3/4 = 0.75.
- Simulate the actual R-match knockout path per trial (per-match RNG draws), Monte-Carlo over TRIALS, at R in {2,4,6,8}.
- Closed-form anchor: P_title(R) = 0.75^R.

## Pinned world (committed constants)
- SEED = 20260717
- TRIALS = 200000
- FAVORITE_STRENGTH = 3.0 -> P_MATCH = 0.75
- ROUNDS = (2, 4, 6, 8) -> N = 4, 16, 64, 256
- SIGMA_GATE = 3.0
- Analytic anchors: 0.75^2 = 0.5625, 0.75^4 = 0.31640625, 0.75^6 = 0.177978515625, 0.75^8 = 0.1001129150390625

## Pre-registered gates (APPROVE iff ALL hold, in order G1 -> G2 -> G3)
- **G1 — sim correct.** At R=8, MC favorite title frequency matches 0.75^8 = 0.10011 within z<3sigma.
- **G2 — constant geometric haircut.** The MC ratio P_title(8)/P_title(4) matches 0.75^4 = 0.31641 within z<3sigma (delta method) — each added round is the *same* multiplicative haircut, not a "truer test".
- **G3 — inversion.** At R=6 (64-player esports bracket), MC P(favorite loses) > 0.5 AND matches 1 - 0.75^6 = 0.82202 within z<3sigma — the strongest entrant is dethroned in the majority; the folk belief is reversed with a >3sigma margin.

## Pre-registered decision rule
APPROVE (sim-ready confirmed) iff G1 AND G2 AND G3 all hold in order and the verifier exits 0 with a reproducible results-dict sha256 across a deterministic double-run. Any gate failing => REJECT/REVISE.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
{
  "all_pass": true,
  "closed_form_title_prob": {
    "2": 0.5625,
    "4": 0.31640625,
    "6": 0.177978515625,
    "8": 0.1001129150390625
  },
  "favorite_strength": 3.0,
  "g1_sim_correct": true,
  "g1_z": 0.5096944639694352,
  "g2_geometric_haircut": true,
  "g2_ratio_anchor": 0.31640625,
  "g2_ratio_mc": 0.3185710208353154,
  "g2_z": 0.9163465017212093,
  "g3_anchor": 0.822021484375,
  "g3_inversion": true,
  "g3_majority": true,
  "g3_p_favorite_loses_r6": 0.82266,
  "g3_z": 0.7465538727644705,
  "mc_title_freq": {
    "2": 0.562975,
    "4": 0.31533,
    "6": 0.17734,
    "8": 0.100455
  },
  "p_match": 0.75,
  "proposal": 131,
  "rounds": [
    2,
    4,
    6,
    8
  ],
  "seed": 20260717,
  "sigma_gate": 3.0,
  "trials": 200000
}
Results-JSON sha256: 002806188054a6eb2f768208f52629d0a3bd0d14624e0489e480efcf86c2a0f2
G1 sim-correct  : PASS (z=+0.510)
G2 geometric    : PASS (z=+0.916)
G3 inversion    : PASS (z=+0.747, P(fav loses)=0.8227)
```
Results-dict sha256: `002806188054a6eb2f768208f52629d0a3bd0d14624e0489e480efcf86c2a0f2` (deterministic double-run, exit 0 both times).

## Verifier
`ideas/superbot-games/single_elim_favorite_collapse.py` — stdlib only (`random, math, json, hashlib`). Builds the favorite's R-match knockout path under Bradley-Terry, Monte-Carlos the title frequency at each R, computes the three pre-registered z-gates against the closed-form p^R anchors, and emits the whole results dict (no self-referential sha field; the compact canonical serialization's sha256 IS the disclosed digest).

## Reproduce
```
python3 ideas/superbot-games/single_elim_favorite_collapse.py
```
Expected: prints the results JSON, `Results-JSON sha256: 002806188054a6eb2f768208f52629d0a3bd0d14624e0489e480efcf86c2a0f2`, three `PASS` lines, exit 0.

## Why it matters (game design)
Format legitimacy is bought with rounds, but each round is an independent upset lottery. If a ladder wants the best team to actually win, single-elimination is the *least* selection-efficient common format (Ryvkin & Ortmann 2008); the correct levers are (a) best-of-N per match (raises the per-stage win prob toward 1) and (b) a group/Swiss stage before the bracket (averages out variance). Seeding alone does not fix it — under indistinguishable normals, seeding is irrelevant to the favorite's p^R.

## Dedup
- Distinct from all prior game-lane cards: shop-reroll (optimal stopping), streak-shield, energy-cap, matchmaking-winrate-mirage, compounding-reward-inequality, PRD proc compression, snipe-clearing-leak (auction microstructure), guild-volunteer-dilemma (public goods), pity-anticipation-collapse, rubber-band controller. None model *tournament-format selection efficiency / knockout title decay.*
- FIRST competitive-format / bracket-selection card in the game lane.

## Model basis (declared model-dependence — the P024 discipline)
Result is exact under the Bradley-Terry indistinguishable-normals model; the p^R law holds for any seeding. Relaxing "normals identical" (a heterogeneous field) only *lowers* the favorite's title odds further (it can draw a strong normal), so the inversion is conservative. The magnitude (~18% at 64) is specific to f=3; the *direction* (geometric decay, folk belief inverted) is model-robust for any finite f.

## Probe report (v0, 2026-07-18)

**1. What is this really?** A competitive-format identity: in single-elimination the favorite must win every one of R=log2(N) rounds, and because the field's "normal" entrants are indistinguishable it faces a normal each round at the constant Bradley-Terry win prob **p=f/(f+1)**, so its exact title probability is the closed form **P_title(R)=p^R**. With f=3 (p=**0.75**): R=4→**31.6%**, R=6→**17.8%**, R=8→**10.0%** — geometric decay in the number of rounds.
**2. What would make it false?** If the MC favorite title frequency did NOT match p^8 at R=8 (G1 fails — the sim is wrong), or if the per-round haircut were NOT constant so P_title(8)/P_title(4)≠p^4 (G2 fails — not a clean geometric decay), or if at R=6 the favorite were NOT dethroned in the majority / P(favorite loses) did not match 1−p^6 (G3 fails — no inversion). Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED=20260717; a 3x favorite (p=0.75) in a 64-player bracket (R=6): P_title=0.75^6=**17.8%**, so P(favorite loses)=**82.2%** — the best player is dethroned in the large majority with a single closed-form line and no tuning.
**4. What is the counterintuitive core?** "A bigger tournament is a truer test that rewards the best" is inverted — each added round is an independent coin-weighted haircut that MULTIPLIES the favorite's odds by p<1, so more rounds make it MORE likely a non-favorite is crowned, not less. A 3x-dominant favorite wins a 256-player single-elim bracket only **10%** of the time.
**5. Where could I be fooling myself?** Assuming seeding or bracket layout rescues the favorite. It does not: under indistinguishable normals the favorite draws a normal every round regardless of layout, so p^R is seeding-invariant. And a heterogeneous field only LOWERS the favorite's odds further (it can draw a strong normal), so the inversion is **conservative** — G2's constant-haircut gate is the explicit control that each round is the same multiplicative p, not a "truer test".
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 sim-correct z=**+0.510** < 3σ (MC 0.100455 vs anchor 0.100113); G2 geometric z=**+0.916** < 3σ (ratio_mc **0.318571** vs anchor **0.316406**); G3 inversion z=**+0.747** < 3σ with P(fav loses)=**0.82266** > 0.5 (anchor **0.822021**); all PASS, exit 0; results-dict sha256 **002806188…c2a0f2**; two runs byte-identical. The z's are small because the sim is exactly the closed-form process — the gates confirm correctness, not a threshold artifact.
**7. What decision does it change?** If the ladder must crown the best, don't add rounds — add DEPTH per round (best-of-N pushes each stage's win prob toward 1.0) or a group/Swiss stage before the bracket (averages out variance). Price format legitimacy as selection efficiency, not bracket size: single-elimination is the least selection-efficient common format (Ryvkin & Ortmann 2008), and seeding alone does not fix it.
**8. How will we know it worked?** The committed stdlib verifier reproduces the sim-correct gate (G1), the constant geometric per-round haircut (G2), and the R=6 inversion with P(favorite loses)>0.5 (G3) at their 3σ bars under SEED=20260717, with the results-dict sha256 matching 002806188054a6eb2f768208f52629d0a3bd0d14624e0489e480efcf86c2a0f2.

## One-line design fix
If the ladder must crown the best, don't add rounds — add *depth per round* (best-of-N) or a group stage; a bigger single-elimination bracket is a longer coin-flip, not a truer test.

**Recommendation: sim-ready**
