# PROPOSAL 160 — Cauchy no-averaging: the law of large numbers fails for infinite-variance data

> **State:** sim-ready
> **Class:** probability / heavy-tailed inference · stable laws (undefined mean, infinite variance) · estimator concentration
> **Slot:** round-37 UNRELATED
> **Anchor:** averaging infinite-variance data buys zero precision — the sample mean of n i.i.d. standard-Cauchy variates is itself standard Cauchy for every n, so its spread never shrinks; the 1/√n error reduction the CLT promises is a finite-variance privilege the Cauchy forfeits.
> **Target:** sim-lab (VERDICT 173, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine/blob/40aa68ce5671706a4ac6b11960ef91b14f0d4e75/ideas/fleet/cauchy_no_averaging.py@460d9ffea7b80339ceebb4fb4cac1bd3d983d77a · fetched 2026-07-19T07:05:57Z
> **Reference (external, reachable):** Wikipedia "Cauchy distribution" https://en.wikipedia.org/wiki/Cauchy_distribution — the sample mean of i.i.d. standard-Cauchy variates is itself standard Cauchy, so the average does not converge and the law of large numbers does not apply.
> **Verifier (firsthand):** `ideas/fleet/cauchy_no_averaging.py` · results-dict sha256 `413e56925e89e34148cb9286df0f392c1a9881fc9072c7683b9f181f39ae7b5c`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
For i.i.d. Cauchy(0, γ) measurements the sample mean M_n is itself Cauchy(0, γ) for every n — its dispersion (IQR/2 = γ) does not fall with n, so averaging never concentrates; the sample median, on the same data, does concentrate ~ 1/√n.

## The folk belief
"Average more noisy readings and the estimate gets more precise; the spread falls like 1/√n, so 100 readings are ~10× tighter than one." That is a theorem for finite variance; for a heavy enough tail (Cauchy: undefined mean, infinite variance) it is simply false — 100 averaged Cauchy readings are exactly as spread as one.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
The 1/√n shrink is not a property of "more data" — it is a property of the **finite-variance CLT**. The sample mean of n i.i.d. variables has variance σ²/n only when σ² exists; the standard error √(σ²/n) is what the law of large numbers rides on. The Cauchy law has **no finite mean and infinite variance**, so that machinery has nothing to stand on. Concretely the Cauchy is a **stable law** (α=1): a sum of n i.i.d. Cauchy(0, γ) is Cauchy(0, nγ), and dividing by n rescales back to **Cauchy(0, γ)** — the mean of n draws is distributed *exactly* as a single draw, for every n. So its robust spread (half the interquartile range, IQR/2, which for Cauchy(0, γ) equals γ exactly) is **flat in n**: spread(mean, 100)/spread(mean, 1) → 1, not 0.1. The tail is doing this: the max of n Cauchy draws grows like n (each draw can be arbitrarily large), and that single worst reading drags the average as much as all the others combined — averaging *imports* the tail instead of cancelling it. The cure is not more samples but a **different estimator**: the sample **median** ignores the tail by construction, has asymptotic law Normal(0, (πγ)²/(4n)), and so *does* concentrate ~ 1/√n on the very same data. Same n, same draws — the estimator you pick decides whether averaging buys anything. (Crossover, not the head: this is the α=1 Cauchy specifically; for a general stable law with index 1<α<2 the mean's spread shrinks like n^(1/α − 1) — slower than √n but not flat — and for α≥2 (finite variance) the CLT is restored. Both disclosed below, neither is this claim.)

## The formal model (committed constants — sim-lab must reproduce exactly)
X_i ~ Cauchy(0, γ), drawn by the inverse-CDF map X = γ·tan(π·(U − 0.5)) for U ~ Uniform(0,1).
- sample mean:   M_n = (1/n)·Σ X_i ~ **Cauchy(0, γ)** for every n (stable, scale-invariant)
- sample median: asymptotic law **Normal(0, (πγ)²/(4n))**, so scale ~ πγ/(2√n)
- robust dispersion measure: **spread(·) = IQR/2 = ½(q₀.₇₅ − q₀.₂₅)**, which for Cauchy(0, γ) equals γ exactly
- CLT-shrink reference for the mean at n: 1/√n (= 0.1 at n=100, ≈ 0.0707 at n=200)

## Pinned world (committed constants)
SEED=20260717 · Z_GATE=3.0 · R=30 replications · TRIALS=2000 sample-statistics each · GAMMA=1.0 · N_BASE=1 · N_AVG=100 · GAMMA_SHIFT=2.5 · N_SHIFT=200. A single `random.Random(SEED)` stream feeds the whole run in fixed order (base block then shift block). Per replication the verifier records spread(mean, n)/spread(mean, 1) and spread(median, n)/spread(median, 1); z-scores are on the /se margin across the R replications. `run()` is executed twice in-process and the two compact-canonical (sorted-keys, 6-dp-rounded) digests are asserted identical.

## Pre-registered gates (APPROVE iff ALL hold, in order G1 → G2 → G3)
- **G1 mean-does-not-concentrate** — the mean-spread ratio spread(mean, n=100)/spread(mean, n=1) exceeds the CLT-shrink null 1/√100 = 0.1 at ≥3σ (observed ≈ 1, NOT 0.1). Measured: mean_ratio 1.016435, z **+91.179099**. PASS. Head: averaging 100 Cauchy readings is as spread as one — no concentration.
- **G2 median-does-concentrate** — on the SAME sample, the median-spread ratio spread(median, n=100)/spread(median, n=1) falls **below** the no-concentration null 1.0 at ≥3σ (observed ≈ 1/√100). Measured: med_ratio 0.106589, z **+1103.622367**. PASS. Head: the estimator, not the data, decides — the median concentrates where the mean cannot.
- **G3 robust-under-shift** — at γ′=2.5, n′=200 both survive: mean-non-concentration (ratio rejects 1/√200 ≈ 0.0707) AND median-concentration (ratio rejects 1.0), each at ≥3σ. Measured: mean_ratio 0.999453, z_mean **+105.248919**; med_ratio 0.074954, z_med **+1871.391001**. PASS. Head: the split is a property of the Cauchy law and the estimator, not of one scale or one n.

## Pre-registered decision rule
APPROVE iff sim-lab reproduces `ideas/fleet/cauchy_no_averaging.py` byte-for-byte under SEED=20260717, the results-dict sha256 equals `413e56925e89e34148cb9286df0f392c1a9881fc9072c7683b9f181f39ae7b5c` exactly, and all three gates PASS in order (all_pass=true, first_failing_gate=null, exit 0). Any digest mismatch, gate failure, or non-deterministic double-run ⇒ REJECT (or QUALIFY on a disclosed environment difference).

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```json
{
  "all_pass": true,
  "first_failing_gate": null,
  "g1_mean_no_concentrate": {
    "clt_null": 0.1,
    "mean_ratio": 1.016435,
    "pass": true,
    "se": 0.010051,
    "z": 91.179099
  },
  "g2_median_concentrates": {
    "clt_reference": 0.1,
    "med_ratio": 0.106589,
    "no_concentration_null": 1.0,
    "pass": true,
    "se": 0.00081,
    "z": 1103.622367
  },
  "g3_robust_shift": {
    "clt_null": 0.070711,
    "mean_ratio": 0.999453,
    "med_ratio": 0.074954,
    "pass": true,
    "z_mean": 105.248919,
    "z_med": 1871.391001
  },
  "gates": [
    true,
    true,
    true
  ],
  "params": {
    "R": 30,
    "TRIALS": 2000,
    "gamma": 1.0,
    "gamma_shift": 2.5,
    "n_avg": 100,
    "n_base": 1,
    "n_shift": 200
  },
  "proposal": 160,
  "readout": {
    "median_asymptotic_scale_const": 1.059486
  },
  "seed": 20260717,
  "sigma_gate": 3.0,
  "slot": "round-37 UNRELATED (statistics-of-science / heavy-tailed inference)"
}
Results-JSON sha256: 413e56925e89e34148cb9286df0f392c1a9881fc9072c7683b9f181f39ae7b5c
```

## Verifier
`ideas/fleet/cauchy_no_averaging.py` — stdlib-only (`math`, `json`, `hashlib`, `random`). Draws R=30 replications × TRIALS=2000 sample-statistics at γ=1.0 (n=1 vs n=100) and γ=2.5 (n=1 vs n=200), measures the mean-spread ratio and median-spread ratio via IQR/2, and gates each against its CLT-shrink or no-concentration null at ≥3σ. WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture: the results dict carries no digest field; `main()` runs `run()` twice, asserts the two compact-canonical (sorted-keys, 6-dp-rounded) digests are identical, prints the indent=2 dump, then the `Results-JSON sha256:` line. No JSON is written to disk.

## Reproduce
```
python3 ideas/fleet/cauchy_no_averaging.py
```
Expected tail:
```
  "all_pass": true,
  ...
Results-JSON sha256: 413e56925e89e34148cb9286df0f392c1a9881fc9072c7683b9f181f39ae7b5c
```
Exit 0; a second invocation is byte-identical.

## Why it matters (measurement + inference)
Any pipeline that pools noisy measurements by **averaging** — sensor fusion, benchmark timing, financial return aggregation, A/B lift on a revenue metric, ratio-of-quantities estimators — silently assumes finite variance. When the underlying quantity is heavy-tailed (ratios of near-zero denominators, insurance losses, network latencies, anything with an undefined or infinite second moment), collecting more samples buys **no** precision: the mean's spread is flat in n and one freak reading dominates the average. The honest fix is not "collect more data" but "**use the median or a trimmed/winsorized estimator**," which concentrates ~1/√n on the same data — the split this proposal verifies. The failure is diagnostic, not merely cautionary: if your error bars shrink like 1/√n on real data that ought to be heavy-tailed, you are measuring the wrong statistic and your confidence intervals are fiction. (Disclosed crossover, honestly: the effect is strongest at the α=1 Cauchy boundary; for a stable law with 1<α<2 the mean *does* concentrate, just slower than √n (like n^(1/α−1)), and at α≥2 the CLT is fully restored — so the "averaging is useless" head is the Cauchy extreme, and nearby heavy-tail/stable-law heads inherit a weaker version of it.)

## Dedup (contrast vs prior lane heads)
- This is **NOT regression-to-the-mean** — that is the reversion of an extreme observation toward a *finite* mean under repeated sampling; here there is **no finite mean** to revert to, and the sample mean does not settle at all.
- This is **NOT the inspection paradox / length-biased sampling** — no size-weighting of what gets observed is at play; every draw is unbiased and i.i.d.; the failure is the *variance* of the estimator, not a sampling bias in the draws.
- This is **NOT James–Stein shrinkage** — that improves a *multivariate* mean estimate by shrinking toward a point under finite variance; here the mean estimator is scalar and shrinkage cannot help because the object it would shrink has no finite second moment.
- This is the **failure of the law of large numbers under infinite variance**: the α=1 stable (Cauchy) sample mean is scale-invariant in n, so averaging cannot concentrate — and the median, which does, is the contrast. No prior lane head states the estimator-choice split for an undefined-mean law.

## Model basis (declared model-dependence — the P024 discipline)
The **sign** and **order of magnitude** are model-free *given* the Cauchy: the mean-spread ratio is exactly 1 for every n (stable-law scale invariance, not a modelling choice), and the median-spread ratio is O(1/√n) < 1 — so G1 (ratio ≫ 0.1) and G2 (ratio ≪ 1) do not depend on the estimator of spread or on n. Declared model-dependence: (1) the **exact** median asymptotic constant πγ/(2√n) is a *large-n* limit; at finite n the measured median ratio (0.1066 at n=100, 0.0750 at n=200) sits a hair above the bare 1/√n, and the readout `median_asymptotic_scale_const` ≈ 1.0595 (= Φ⁻¹(0.75)·π/2) is reported as the asymptote, not gated. (2) The IQR/2 spread is chosen precisely *because* for Cauchy it equals γ and needs no finite moment; a variance-based spread would be undefined and is deliberately avoided. (3) Cauchy (α=1) only: for a general stable law 1<α<2 the mean concentrates like n^(1/α−1) and the head weakens continuously — named as the crossover, not tested here.

## Probe report (v0, self-adversarial)
**1. Is the mean really non-concentrating, or just MC noise / too-few TRIALS?** — Stable-law fact: mean of n Cauchy(0, γ) is Cauchy(0, γ) exactly, so spread is flat in n by construction. G1 measures ratio 1.0164 at z=+91.2 vs the CLT null 0.1; the ratio hugs 1, not noise around 0.1.
**2. Is the median-concentration gate (G2) circular given how spread is defined?** — No; both estimators use the *same* IQR/2 spread on the *same* draws. The mean's IQR/2 is flat (ratio ≈ 1) and the median's IQR/2 falls (ratio ≈ 1/√n); the split is the estimator, not the measure.
**3. Does the inverse-CDF sampler bias the tail?** — X = γ·tan(π·(U−0.5)) is the standard exact Cauchy quantile map; the claim is distributional, not sampler-specific, and determinism is asserted across an in-process double-run (identical digests).
**4. Is 1/√n the right null for G1, or a strawman?** — It is exactly the CLT promise the folk belief invokes (√(σ²/n) with unit scale); rejecting it at ≥3σ is precisely the point — the finite-variance shrink does not occur.
**5. Could a different γ or n flip the result?** — G3 re-runs at γ′=2.5, n′=200: mean non-concentration (z_mean +105.2) and median concentration (z_med +1871.4) both survive. Scale-invariant in γ, and n only sharpens the median gate.
**6. Is this just "Cauchy has no mean" restated?** — The novel, verified content is the **estimator split** on identical data: the mean cannot concentrate but the median can, quantified at ≥3σ. The no-mean fact is the anchor, disclosed, not the whole claim.
**7. Overlap with other heavy-tail / stable-law heads?** — Explicit dedup and crossover: this is the α=1 extreme where averaging is *useless*; 1<α<2 heads get a weaker n^(1/α−1) shrink and α≥2 restores the CLT. No shared gate or number with a finite-variance head.
**8. What would falsify it?** — A reproduction where the mean-spread ratio drifts toward 1/√n (concentrating), or the median-spread ratio fails to fall below 1, or a non-deterministic double-run. None occur; all three gates pass at ≥3σ across two scales.

## One-line design fix
When pooling measurements that could be heavy-tailed (ratios, latencies, losses, undefined-mean quantities), report the **median or a trimmed/winsorized estimate** — whose spread concentrates ~1/√n — instead of the sample mean, whose error bars are fiction under infinite variance.

**Recommendation: sim-ready**
