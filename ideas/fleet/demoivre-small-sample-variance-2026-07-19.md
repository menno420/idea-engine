# PROPOSAL 184 — de Moivre's small-sample variance artifact: ranking units by an observed rate surfaces the smallest-sample units at BOTH extremes, because the standard error of a proportion scales as 1/√n

> **State:** sim-ready
> **Class:** fleet (cross-cutting) · statistics of estimation / sampling variance · de Moivre's √n law
> **Slot:** round-43 UNRELATED
> **Anchor:** When many units share ONE true rate p but differ in sample size n, SD(observed rate) = √(p(1−p)/n), so the top and bottom of a leaderboard ranked on the observed rate are dominated by the smallest-n units — a variance artifact, not a quality signal.
> **Target:** sim-lab (VERDICT 197, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Standard_error@3af4e58d40c9b4ccc94cfb3c67ba69f92bfa1ec3 · fetched 2026-07-19T21:03:48Z
> **Reference (external, reachable):** Wikipedia "Standard error" (oldid 1362665393), fetched live via the MediaWiki Action API 2026-07-19T21:03:48Z, confirms the standard error of the mean = σ/√n and the standard error of a proportion. The popular name "the most dangerous equation" and the small-schools / rural-county kidney-cancer illustrations are Howard Wainer's ("The Most Dangerous Equation", American Scientist 95(3), 2007 — real and cited on live Wikipedia, but not independently fetchable in this environment; the σ/√n law the mechanism rests on is the part verified live).
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
Rank a set of units by a rate you measured on each, when they all share the same true rate but were measured on different sample sizes: the extremes of the ranking — best AND worst — are the small-sample units, purely because √(p(1−p)/n) blows up as n shrinks.

## The folk belief
"The lanes/schools/counties at the top of the leaderboard are the good ones, and the ones at the bottom are the bad ones." When the units differ in sample size and share a common true rate, both ends are a sampling-variance illusion; the ranking says more about n than about quality.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
For a unit with true rate p measured over n independent trials, the observed rate r̂ is a sample mean of Bernoulli(p) draws, so Var(r̂) = p(1−p)/n and SD(r̂) = √(p(1−p)/n) — de Moivre's √n law for the standard error of a proportion. With one shared p, the *signal* variance across units is zero; all dispersion in r̂ is sampling noise whose scale is set by 1/√n. Sort by r̂ and the order statistics at both tails are drawn from the widest-noise (smallest-n) units: E|r̂−p| ∝ 1/√n, so a small-n unit is far likelier to reach either extreme than a large-n unit with the same p. The top of the board is not "who is best" but "who was measured least".

## The formal model (committed constants — sim-lab must reproduce exactly)
Draw M=800 units per trial, TRIALS=100. Each unit gets a sample size n drawn log-uniformly on integers in [LO, HI] and an observed rate r̂ = (Bernoulli(p) successes)/n. G1 measures the Pearson correlation across the M units between the deviation |r̂−p| and 1/√n (the de Moivre scaling law). G2 ranks the units by r̂, takes the top+bottom EXT=10%, and measures pop_mean_n − mean_n(extremes) (positive when the extremes are small-n). z = mean/(std/√TRIALS) over the TRIALS trials. G3 repeats G1 under a shifted rate p=0.1 and G2 under a shifted size range [LO2, HI2].

## Pinned world (committed constants)
SEED = 20260717 · Z_GATE = 3.0 · TRIALS = 100 · M = 800 · LO = 10 · HI = 800 · LO2 = 25 · HI2 = 250 · P = 0.5 · P_SHIFT = 0.1 · EXT = 0.10 · floats rounded 6dp · whole-dict / no-self-field / stdout-only.

## Pre-registered gates (APPROVE iff ALL hold, in order G1 -> G2 -> G3; z_gate = 3.0)
- **G1 — the √n scaling law holds.** Across units, Pearson corr(|r̂−p|, 1/√n) > 0 at >= 3 sigma. Observed mean r = 0.570449, z = 238.774053.
- **G2 — the ranking extremes are small-n.** Top+bottom 10% by observed rate have a smaller mean sample size than the population; pop_mean_n − extreme_mean_n > 0 at >= 3 sigma. Observed delta = 147.021788, z = 213.047828.
- **G3 — robust under shifted rate and shifted size range.** Under a skewed p=0.1 the G1 correlation stays > 0 at >= 3 sigma (mean r = 0.570124, z = 219.519762), and under the size range [25,250] the G2 delta stays > 0 at >= 3 sigma (delta = 38.443275, z = 129.55551).

## Pre-registered decision rule
APPROVE iff G1 AND G2 AND G3 all hold in order with all_pass=true and the results-dict sha256 reproduces byte-for-byte; else REJECT with first_failing_gate named.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```json
{
  "all_pass": true,
  "ext_frac": 0.1,
  "first_failing_gate": null,
  "g1_scaling_corr_mean": 0.570449,
  "g1_scaling_corr_std": 0.023891,
  "g1_z": 238.774053,
  "g2_extreme_delta_n_mean": 147.021788,
  "g2_extreme_delta_n_std": 6.900882,
  "g2_z": 213.047828,
  "g3a_shifted_p_corr_mean": 0.570124,
  "g3a_shifted_p_z": 219.519762,
  "g3b_shifted_range_delta_mean": 38.443275,
  "g3b_shifted_range_z": 129.55551,
  "gates": {
    "G1_deMoivre_scaling_law": true,
    "G2_extremes_small_n_dominated": true,
    "G3_robust_shifted_p_and_range": true
  },
  "n_hi": 800,
  "n_hi_shift": 250,
  "n_lo": 10,
  "n_lo_shift": 25,
  "p_base": 0.5,
  "p_shift": 0.1,
  "seed": 20260717,
  "trials": 100,
  "units": 800,
  "z_gate": 3.0
}
```
Results-JSON sha256: 8b9506d1182b6c5f3121ff8b585dfb7032d47a337013e30d4f7fbfc1e0968871

## Verifier
`ideas/fleet/demoivre_small_sample_variance.py` — stdlib-only (sys, math, json, hashlib, random). run() returns the whole results dict with no self-digest field; main() runs it twice, asserts byte-identical canonical JSON, prints the pretty dict then the sha256.

## Reproduce
```
python3 ideas/fleet/demoivre_small_sample_variance.py
```
Expect exit 0, all_pass=true, and Results-JSON sha256 8b9506d1...968871 identical across two invocations.

## Why it matters (sample size masquerades as quality)
Any leaderboard that ranks units measured on different volumes — agent lanes by success rate over unequal task counts, vendors by defect rate over unequal batch sizes, schools by mean score over unequal enrolment, counties by disease rate over unequal population — puts its smallest-n members at both extremes. Wainer's canonical cases: the "smallest schools have the highest test scores" reform push (and, symmetrically, the lowest), and the map of US counties with the lowest kidney-cancer rates being small and rural (as are the highest). Fleet analog: promoting the "top lane" or killing the "worst lane" off a raw rate, when lanes differ in attempt count, is often selecting on 1/√n, not on skill.

## Dedup (contrast vs prior lane heads)
Distinct from regression to the mean (a repeated-measurement reversion of the SAME unit toward its own mean; here units are measured once and there is no true spread to revert to), from the hot-hand / Sanjurjo finite-sequence selection bias (a conditioning-on-a-streak artifact within one sequence), from Stein shrinkage (an estimator that fixes this by pooling, not the phenomenon itself), and from Berkson's collider (selection on a common effect of two causes). This head is purely first-moment sampling variance: SD ∝ 1/√n makes small-n units the order-statistic extremes. A `git grep` for "moivre", "most dangerous", "sample size", "Wainer", "standard error of the mean" over ideas/ returned no prior head on this thesis (the two "sample size" hits are the correlated-variance-floor and German-tank docs, unrelated).

## Model basis (declared model-dependence)
Assumes a shared true rate across units (zero signal variance) and independent Bernoulli trials within a unit. Real signal variance across units competes with the 1/√n noise: the artifact dominates whenever between-unit true-rate spread is small relative to √(p(1−p)/n̄). Serial correlation within a unit inflates the effective SD but preserves the 1/√n direction. All disclosed; the gates pin the shared-p independent-trial world plus the two robustness shifts.

## Gate power + margin ledger
| Gate | Statistic | Observed | Threshold | Margin |
|---|---|---|---|---|
| G1 | corr(dev, 1/√n), z | 0.570449, z=238.77 | r>0, z>=3 | ~236 sigma |
| G2 | pop−extreme mean n, z | 147.021788, z=213.05 | delta>0, z>=3 | ~210 sigma |
| G3a | shifted-p corr, z | 0.570124, z=219.52 | r>0, z>=3 | ~217 sigma |
| G3b | shifted-range delta, z | 38.443275, z=129.56 | delta>0, z>=3 | ~127 sigma |

## Probe report (v0, self-adversarial)
**1. Is this just regression to the mean?** No — regression to the mean needs a true per-unit value the estimate reverts toward across repeated measurement; here every unit has the identical true p and is measured once, so there is nothing to revert to. The extremes are pure first-measurement sampling noise scaled by 1/√n.
**2. Could a real quality spread swamp the artifact?** Yes, and it is disclosed in Model basis: the artifact dominates only while between-unit true-rate variance is small relative to p(1−p)/n̄. The pinned world sets true spread to zero to isolate the mechanism; the gates do not claim the artifact survives arbitrary signal.
**3. Is the correlation sign an artifact of using |r̂−p| with known p?** The known p is the pinned true rate, not an estimate; |r̂−p| is the honest deviation. Using the sample grand mean instead shifts the constant but not the 1/√n slope; G2, which never references p, corroborates the same conclusion via sample size alone.
**4. Top-k vs a rate threshold?** Top-k on a continuous r̂ is a random threshold in expectation; both put small-n units at the tails. Top-k is pinned for determinism.
**5. Does the effect need p=0.5?** No — G3a at p=0.1 gives essentially the same scaling correlation (0.570124 vs 0.570449); p(1−p) rescales the magnitude but the 1/√n direction is distribution-free in n.
**6. Is it an artifact of the log-uniform size draw?** No — G3b redraws sizes on a different, narrower range [25,250] and the extremes-are-small-n delta stays positive at z=129.56. The mechanism follows n, not the particular size law.
**7. Which real decisions?** Agent-lane leaderboards over unequal attempt counts, vendor/defect ranking over unequal batches, small-schools reform, disease-rate county maps (Wainer). Reported, not gated.
**8. Closest prior head / distinctness?** Stein shrinkage (the fix, not the phenomenon) and regression to the mean (repeated-measurement reversion); see Dedup. This head is the raw SD ∝ 1/√n order-statistic effect.

## One-line design fix
Never rank on a raw rate across unequal sample sizes: shrink each unit's estimate toward the grand mean by its own reliability (empirical-Bayes / James-Stein), or gate the ranking on a minimum n, so the leaderboard reflects rate, not 1/√n.

**Recommendation: sim-ready**
