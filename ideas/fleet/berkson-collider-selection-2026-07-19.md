# PROPOSAL 172 — Berkson's collider paradox: selecting the elite on an additive composite manufactures a negative correlation between two independent traits

> **State:** sim-ready
> **Class:** fleet (cross-cutting) · statistics of selection / collider bias · Berkson conditioning
> **Slot:** round-40 UNRELATED
> **Anchor:** For independent X, Y, conditioning on the top-quantile of X+Y makes Corr(X,Y | selected) < 0, deepening toward -1 as the quantile tightens.
> **Target:** sim-lab (VERDICT 185, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Berkson%27s_paradox@359b1430d077f98bbae0254c000e85772ed846a6 · fetched 2026-07-19T14:21:49Z
> **Reference (external, reachable):** Wikipedia "Berkson's paradox" (Berkson 1946), HTTP 200 at oldid 1340658864, fetched 2026-07-19T14:21:49Z
> **Verifier (firsthand):** `ideas/fleet/berkson_collider_selection.py` · results-dict sha256 `42a47b8890316dd5d9da056f1598ad4e3b7472678ffb0e4d3a62c25cadc19e0b`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
Two traits that are independent in the whole population become negatively correlated inside any group selected on their sum — clearing the composite bar forces a trade-off between its parts.

## The folk belief
"If two traits are uncorrelated in the population they are uncorrelated in the winners; and in an elite selected for being high on both, if anything the two should track together." Wrong on both counts.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Let S = X + Y and D = X - Y. For independent, equal-variance X, Y, S and D are uncorrelated (Cov(S,D) = Var X - Var Y = 0). Selection keeps the top quantile of S and does not touch D, so within the selected set Var(S|sel) shrinks (upper-tail truncation) while Var(D|sel) = Var(D) is unchanged. Since X = (S+D)/2 and Y = (S-D)/2,
Cov(X,Y|sel) = (Var(S|sel) - Var(D)) / 4 < 0 once truncation makes Var(S|sel) < Var(D),
and r = (Var(S|sel) - Var(D)) / (Var(S|sel) + Var(D)) -> -1 as the quantile tightens. This is a collider: X and Y both feed the selection variable S, and conditioning on a common effect couples independent causes.

## The formal model (committed constants — sim-lab must reproduce exactly)
Draw N=8000 i.i.d. pairs per trial, TRIALS=200. Rank by the additive composite X+Y; keep the top TOP=10% (also TIGHT=2%, LOOSE=40%). Compute the within-selected Pearson r; average across trials; z = -mean / (std / sqrt(TRIALS)). Worlds: gaussian N(0,1) for G1 and G2, plus uniform(0,1) and exponential(1) for G3. The population control r uses all N points.

## Pinned world (committed constants)
SEED = 20260717 · Z_GATE = 3.0 · TRIALS = 200 · N = 8000 · TOP = 0.10 · TIGHT = 0.02 · LOOSE = 0.40 · floats rounded 6dp · whole-dict / no-self-field / stdout-only.

## Pre-registered gates (APPROVE iff ALL hold, in order G1 -> G2 -> G3; z_gate = 3.0)
- **G1 — selected elite is negatively correlated.** Gaussian top-10%-by-sum mean Pearson r < 0 at >= 3 sigma. Observed r = -0.710835, z = 459.110893.
- **G2 — the negativity is selection-induced (reversal).** Full-population r ~ 0 (|mean| < 0.01) while selected r is strictly below it; the paired (selected - population) difference is negative at >= 3 sigma. Observed population r = -0.000017, selected - population = -0.710818, z = 454.654805.
- **G3 — robust under shifted (non-normal) marginals.** Uniform AND exponential independent marginals each give selected r < 0 at >= 3 sigma. Observed uniform r = -0.49835 (z = 305.311106), exponential r = -0.738422 (z = 531.488409).

## Pre-registered decision rule
APPROVE iff G1 AND G2 AND G3 all hold in order with all_pass=true and the results-dict sha256 reproduces byte-for-byte; else REJECT with first_failing_gate named.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```json
{
  "all_pass": true,
  "deepening_diff_mean": -0.271863,
  "deepening_loose_mean_r": -0.52506,
  "deepening_tight_mean_r": -0.796923,
  "deepening_z": 110.99457,
  "first_failing_gate": null,
  "g1_selected_mean_r": -0.710835,
  "g1_selected_std_r": 0.021896,
  "g1_z": 459.110893,
  "g2_selected_minus_pop_mean": -0.710818,
  "g2_z": 454.654805,
  "g3_exponential_mean_r": -0.738422,
  "g3_exponential_z": 531.488409,
  "g3_uniform_mean_r": -0.49835,
  "g3_uniform_z": 305.311106,
  "gates": {
    "G1_selected_negative": true,
    "G2_selection_induced_reversal": true,
    "G3_robust_nonnormal": true
  },
  "loose_frac": 0.4,
  "n_per_trial": 8000,
  "population_mean_r": -1.7e-05,
  "population_std_r": 0.010299,
  "seed": 20260717,
  "tight_frac": 0.02,
  "top_frac": 0.1,
  "trials": 200,
  "z_gate": 3.0
}
```
Results-JSON sha256: 42a47b8890316dd5d9da056f1598ad4e3b7472678ffb0e4d3a62c25cadc19e0b

## Verifier
`ideas/fleet/berkson_collider_selection.py` — stdlib-only (math, json, hashlib, random). run() returns the whole results dict with no self-digest field; main() runs it twice, asserts byte-identical canonical JSON, prints the pretty dict then the sha256.

## Reproduce
```
python3 ideas/fleet/berkson_collider_selection.py
```
Expect exit 0, all_pass=true, and Results-JSON sha256 42a47b88...c19e0b identical across two invocations.

## Why it matters (selection is everywhere)
Any dataset assembled by clearing a bar — university admits, funded startups, hospital in-patients (Berkson's original case-control setting), hired candidates — reads independent inputs as if they trade off. "Elite schools show SAT and GPA negatively related" and "admitted patients show risk factor A protects against disease B" are the same artifact, not a finding. Fleet analog: any leaderboard or gate that ranks agents on a summed score will show its component metrics anti-correlated among the survivors, which is not evidence the metrics conflict.

## Dedup (contrast vs prior lane heads)
Distinct from the friendship paradox (size-biased sampling of a fixed graph — a marginal-mean shift, not a manufactured correlation), from Will Rogers migration (relabeling shifts both group means with no within-unit change), and from Simpson-style aggregation. Berkson's is specifically a collider: conditioning on a common effect of two independent causes. Nearest neighbour is the friendship paradox (both selection biases); the contrast is direction — Berkson manufactures a negative pairwise correlation, the friendship paradox shifts a marginal mean.

## Model basis (declared model-dependence)
Assumes independent, roughly equal-variance traits and selection monotone in the sum. A large positive population correlation offsets the truncation term and can weaken or flip the induced sign; strongly unequal variances shift the S/D decomposition; a non-additive selection score changes the geometry but not the collider logic. All disclosed; gates test only the pinned equal-variance independent-additive world plus the two robustness marginals.

## Gate power + margin ledger
| Gate | Statistic | Observed | Threshold | Margin |
|---|---|---|---|---|
| G1 | selected mean r, z | -0.710835, z=459.11 | r<0, z>=3 | ~456 sigma |
| G2 | selected-pop, z; pop r | -0.710818, z=454.65; pop -0.000017 | diff<0, z>=3, abs(pop)<0.01 | ~451 sigma |
| G3 | uniform r/z; exp r/z | -0.49835/305.31; -0.738422/531.49 | both r<0, z>=3 | ~302 sigma |
| (non-gated) deepening | tight vs loose r, z | -0.796923 vs -0.52506, z=110.99 | — | trends to -1 |

## Probe report (v0, self-adversarial)
**1. Sum-only, or any monotone score?** Any selection monotone in a score to which both traits contribute positively induces the collider coupling; the sum is the cleanest case. A score using only X would not couple them. Gates pin the additive sum; the generality is noted, not gated.
**2. Finite-sample bias?** No — the population r over the same N is -0.000017 (G2), so the negativity is not a small-sample Pearson artifact; it appears only after conditioning.
**3. Positive population correlation?** Disclosed in Model basis: a large enough positive Corr(X,Y) offsets the truncation term and the induced sign weakens or flips. The pinned world is independent; that is the honest scope.
**4. Top-k vs threshold?** Top-k with continuous marginals is a random threshold on S; the two agree in expectation. Top-k is pinned for determinism.
**5. Non-normality — sign or magnitude?** Only magnitude: uniform (-0.49835) is shallower, exponential (-0.738422) deeper than gaussian (-0.710835); all strictly negative (G3). The sign is distribution-free.
**6. Deepening monotonic?** Tight 2% (-0.796923) < top 10% (-0.710835) < loose 40% (-0.52506), z=110.99 on the tight-loose difference; monotone toward the r -> -1 limit.
**7. Which real decisions?** Case-control epidemiology (Berkson's original), admissions and hiring composites, any "quality index" gate. Reported, not gated.
**8. Closest prior head / distinctness?** Friendship paradox (a selection bias, but a marginal-mean shift, not a pairwise-correlation flip); see Dedup.

## One-line design fix
When you must read a correlation inside a selected group, condition-correct: recover the population correlation from the selected correlation and the known selection fraction, or measure the traits on an unselected holdout — never trust a within-elite correlation at face value.

**Recommendation: sim-ready**
