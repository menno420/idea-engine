# The best estimate of a population's size is LARGER than the largest one you have seen: sample k distinct serial numbers from an unknown fleet numbered 1..N and the naive guess "N = the biggest serial I saw" (the sample maximum m) is systematically too LOW — E[m] = k(N+1)/(k+1) < N. The minimum-variance unbiased estimator EXTRAPOLATES above the largest observed serial, N̂ = m(1 + 1/k) − 1 = "sample max + the average gap between samples", is unbiased (E[N̂] = N exactly), and beats the obvious "twice the mean" unbiased estimator on variance by a factor (k+2)/3. Estimation is not "the biggest I've seen" — it is the biggest plus the gap the sampling left above it.

> **State:** sim-ready
> **Class:** fleet (unrelated / cross-cutting) · statistical estimation theory · the German-tank problem (MVUE for the maximum of a discrete uniform population)
> **Target:** sim-lab (VERDICT 133, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@e0612a9 · fetched 2026-07-18T06:07:44Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/German_tank_problem — the frequentist MVUE N̂ = m(1 + k⁻¹) − 1 = m + (m−k)/k ("sample maximum plus the average gap between observations"), unbiased with variance (N−k)(N+1)/(k(k+2)); verified reachable 2026-07-18 (WebFetch, confirms the estimator exceeds the sample maximum by an average-gap correction that compensates the negative bias of the sample max).

## The phenomenon (one line)
Draw `K` distinct serial numbers without replacement from an unknown fleet numbered `1..N`. The obvious estimate for N is the largest serial you observed, `m`. That estimate is biased LOW — it can never exceed the true N and almost always falls short. The **minimum-variance unbiased estimator adds a correction that pushes the estimate ABOVE the largest serial you saw**: `N̂ = m(1 + 1/K) − 1`. On the pinned world (`N=1000`, `K=5`) the sample maximum averages `≈834`, the MVUE averages `≈1000` (exactly N), and the MVUE lands on average **≈166 above** the largest serial ever observed.

## The folk belief
"To estimate how many of something exist when you can only see a sample of serial numbers, the best you can do is the largest number you have seen. You can't justify guessing a value ABOVE your maximum observation — you have no evidence for anything bigger, so the sample maximum is the estimate; at most round up a little." The intuition treats the largest observed serial as an upper anchor for the estimate and refuses to extrapolate past it, and treats "average the sample and double it" as an equally-good alternative when it does extrapolate.

## The estimation thesis (reasoned to its fuller form — Q-0254 duty)
The intuition confuses "the largest value I could have the *evidence* to name" with "the best *estimate* of the maximum." The sample maximum `m` is a downward-biased estimator of `N` precisely because a finite sample almost never contains the top of the range: the expected gap between the largest observed serial and the true maximum is not zero. For `K` distinct draws without replacement from `1..N`, order statistics give the exact bias

    E[m] = K·(N+1)/(K+1),   so   N − E[m] = (N − K)/(K+1) > 0,

a strictly positive shortfall. The fix is to ADD BACK the expected gap. The `K` sampled serials partition `1..m` into `K` gaps of equal expected width `(m − K)/K` (the spacings of a uniform sample are exchangeable), and the unobserved stretch ABOVE `m` up to `N` has that same expected width. So the bias-corrected estimator is

    N̂ = m + (m − K)/K = m·(1 + 1/K) − 1   ("sample maximum + the average sample gap"),

which is **exactly unbiased**: `E[N̂] = N`. It is also the *minimum-variance* unbiased estimator (Lehmann–Scheffé: `m` is a complete sufficient statistic for `N`, so the unique unbiased function of `m` is the MVUE), with the exact variance

    Var(N̂) = (N − K)(N + 1) / (K·(K + 2)) ≈ N²/K²   for small K.

Two consequences the folk belief misses. **(1) The estimate lies ABOVE the maximum you saw.** Since `m ≥ K` always (the maximum of `K` distinct positive serials is at least `K`), the correction `(m−K)/K ≥ 0`, so `N̂ ≥ m` always — the honest best estimate is at or above the largest serial observed, never below it. **(2) The obvious alternative is worse.** A second, equally-intuitive unbiased estimator is "twice the sample mean, minus one," `Ñ = 2·x̄ − 1` (the sample mean estimates the midpoint `(N+1)/2`), which is ALSO unbiased but uses the whole sample inefficiently:

    Var(Ñ) = (N + 1)(N − K)/(3K),   so   Var(Ñ)/Var(N̂) = (K + 2)/3.

For `K = 5` the mean-doubling estimator has `(5+2)/3 = 7/3 ≈ 2.33×` the variance of the MVUE — the max-based estimator, which throws away everything but the largest serial, is the *more* efficient one, because `m` is sufficient (it captures all the information the sample carries about `N`). The honest reading: to estimate a maximum from a sample, take the largest value you saw and add the average gap the sampling left above it — and prefer the max-based correction to the mean-based one.

## The formal model (committed constants — sim-lab must reproduce exactly)
- A "fleet" is the discrete uniform population `{1, 2, …, N}` with `N = N_TRUE` unknown to the estimator; the estimator observes only the sample.
- A sample is `K` DISTINCT serials drawn WITHOUT replacement (serials are unique) — `rng.sample(range(1, N+1), K)`.
- Per sample record the maximum `m` and: the MVUE `N̂ = m·(1 + 1/K) − 1`; the sample maximum `m` itself (the naive estimator); the alternative unbiased estimator `Ñ = 2·x̄ − 1` where `x̄` is the sample mean.
- Per replication (`SAMPLES = 4000` independent samples) record the batch MEAN of `N̂`, the batch MEAN of `m`, and the batch sample VARIANCES of `N̂` and of `Ñ`.
- A statistic's mean and standard error are taken over `TRIALS = 200` independent replications, `se = sample-sd / √TRIALS` (the P104…P116 /se convention: z on an estimated statistic).
- Closed-form anchors are exact for the discrete uniform: `E[m] = K(N+1)/(K+1)`, `Var(N̂) = (N−K)(N+1)/(K(K+2))`, `Var(Ñ) = (N+1)(N−K)/(3K)`.

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned; SEEDLESS discipline)
- N_TRUE = 1000, K = 5 (distinct serials, without replacement)
- SAMPLES = 4000 per replication, TRIALS = 200, SIGMA_GATE = 3.0
- Exact closed-form anchors (N = 1000, K = 5): `E[m] = 834.166667`; max-bias `N − E[m] = 165.833333`; `Var(N̂) = 28457.0`; `Var(Ñ) = 66399.666667`; efficiency ratio `Var(Ñ)/Var(N̂) = 2.333333 = (K+2)/3`; `E[N̂] = N = 1000` exactly.

## Pre-registered gates (APPROVE iff ALL hold)
- **G1 — MVUE unbiased (headline + control):** the measured mean of `N̂` is within 3σ of the true `N = 1000` (|z| < 3, z on its standard error). The estimator that extrapolates ABOVE the largest observed serial is spot-on for the population size — no residual bias.
- **G2 — max biased low + MVUE above the max:** (a) the mean sample maximum `m` is strictly BELOW `N` by ≥3σ (the naive "population = largest serial seen" systematically underestimates); AND (b) the mean `N̂` exceeds the mean sample maximum by ≥3σ. The best estimate lands ABOVE the largest serial ever observed — the counterintuitive core.
- **G3 — closed-form anchor MATCH + efficiency:** (a) the empirical `Var(N̂)` reproduces the exact closed form `(N−K)(N+1)/(K(K+2)) = 28457.0` within 3σ (|z| < 3); AND (b) the MVUE is strictly MORE efficient than the unbiased mean-doubling estimator `Ñ`: `Var(Ñ) − Var(N̂)` is ≥ 0 by ≥3σ. The max-based bias correction is both correct and minimum-variance.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier (the verifier's `all_pass` field encodes exactly `G1 ∧ G2 ∧ G3`). Any gate failing → REJECT (the German-tank MVUE claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; margins reported in σ on the standard error of the estimated statistic.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- mean MVUE `N̂` = **999.927753** (se 0.183300) — true N = 1000
- mean sample maximum `m` = **834.106461** (se 0.152750) — exact anchor E[m] = 834.166667
- MVUE-above-max gap `N̂ − m` = **165.821292** (se 0.238603) — the estimate lands ~166 above the largest serial observed
- empirical Var(`N̂`) = **28509.405891** (se 53.306373) — exact anchor 28457.0
- empirical Var(`Ñ`) = **66476.372769** (se 96.462074) — exact anchor 66399.666667
- variance gap Var(`Ñ`) − Var(`N̂`) = **37966.966877** (se 110.211166)
- **G1 MVUE-unbiased:** mean N̂ 999.927753 vs 1000 at |z| = **0.3941** (< 3) — PASS (the above-the-max estimator is unbiased for N)
- **G2 max-biased-low + MVUE-above-max:** mean max 834.106461 below 1000 at z_bias = **1086.0456** AND N̂ − m gap 165.821292 above 0 at z_above = **694.9667** — PASS (naive max underestimates by ~166; the MVUE lands above the largest serial seen)
- **G3 anchor-match + efficiency:** Var(N̂) 28509.405891 vs 28457.0 at |z| = **0.9831** (< 3) AND variance gap 37966.966877 at z_efficiency = **344.4929** — PASS (exact closed-form variance reproduced; MVUE strictly beats the mean-doubling estimator)
- all_pass = true; **exit 0**
- Two runs byte-identical (deterministic under SEED).
- **Disclosed results-dict sha256 = 37cea2bfb9b3f60c564d78bb6e5b31c9fcfe8ee7cb11c2fbafe38ddf9af31531**
  (this is the sha256 of `json.dumps(results, sort_keys=True, separators=(",",":"))` over the results dict BEFORE its `results_sha256` self-field is added — the value the verifier prints as `Results-JSON sha256:`; the P112/P104/P116 self-field posture. The pretty-printed on-disk `german_tank_mvue_results.json` artifact's own `sha256sum` is NOT this digest, and that artifact is not committed.)

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `ideas/fleet/german_tank_mvue.py`. Seeds once with SEED=20260717, then for each of TRIALS=200 replications draws SAMPLES=4000 independent size-K=5 samples (distinct serials, without replacement) from `1..N=1000`, computing per sample the MVUE `N̂ = m(1+1/K)−1`, the naive sample maximum `m`, and the alternative unbiased `Ñ = 2·x̄−1`; it records per-batch means of `N̂`/`m` and per-batch variances of `N̂`/`Ñ`, then takes means and standard errors over the 200 replications, evaluates G1/G2/G3 on the /se margin against the EXACT closed-form anchors, and emits a canonical (sorted-keys, comma/colon-separated) results JSON with its sha256. Exit 0 iff all three gates pass.

Reproduce:

```
python3 ideas/fleet/german_tank_mvue.py
```

Expected: all_pass=true, exit 0, G1 |z|=0.3941, G2 z_bias=1086.0456 / z_above=694.9667, G3 z_var_match=0.9831 / z_efficiency=344.4929, results-dict sha256 = 37cea2bfb9b3f60c564d78bb6e5b31c9fcfe8ee7cb11c2fbafe38ddf9af31531.

## Why it matters (cross-cutting)
Any "estimate the size / top / total of a population from a sample of labels" problem — how many distinct users, requests, invoices, or SKUs exist given a sample of sequential IDs; the total run-length of a job queue from sampled ticket numbers; the fleet size behind observed sequential asset tags; the number of concurrent sessions from sampled monotonic tokens — invites the same two mistakes: (1) anchoring the estimate at the largest label observed (biased LOW by the average gap the sampling left above it), and (2) reaching instead for "average × 2" when you do extrapolate, which is unbiased but ~2.3× noisier at K=5. Decision rule for an operator/analyst: when serials/IDs are roughly uniform over an unknown range and you have K distinct observations, estimate the maximum as `m(1 + 1/K) − 1` (largest observed + average gap), report its standard error from `(N−K)(N+1)/(K(K+2))`, and prefer this max-based correction to any mean-based estimator — the sample maximum is a *sufficient* statistic, so the extra information you think the mean adds is already captured, and the mean-doubling estimator only adds variance.

## Dedup
Distinct from the nearby fleet/unrelated and probability priors:
- **coupon-collector-tail** (fleet, occupancy/collection — completion COST φ = H_m/H_N to draw a full set): a sampling-effort claim about a fixed pool; this proposal has no collection, no coverage, no harmonic sum — its object is a POINT ESTIMATE of an unknown population maximum and its bias/variance.
- **inspection-paradox-wait-inflation** (fleet — size-biased sampling / renewal length-bias, `E[W] = E[X²]/(2E[X])`): a length-biased WAITING-TIME inflation of a renewal stream; this proposal has no renewal process, no waiting time, no length-bias weighting — it is unbiased point estimation of a discrete-uniform maximum from an unweighted sample.
- **secretary-rule-cardinal-regret** (fleet, optimal stopping — the 1/e stopping rule and cardinal regret): a sequential DECISION / stopping object; this proposal makes no decision, has no stopping rule, no online arrival — it is a batch estimator of a fixed parameter.
- **variance-blind-provisioning-trap** (fleet — M/M/1 utilization / `Wq = ρ/(1−ρ)·(1+CV²)/2` queueing tail): a congestion / provisioning object; no queue, no utilization, no service-time variance here.
- **arcsine-lead-illusion** (P116, stochastic processes — the sojourn-time DISTRIBUTION of a fair walk), **kelly-overbet-ruin** (P100, information theory — growth-optimal bet fraction), **series-reliability-collapse** (P112, reliability — min-of-exponentials MTBF), **epidemic-overshoot** (P104, SIR final size), **regression-to-mean** (P108, conditional-mean shrinkage): different domains, different objects (a distribution, a bet fraction, an MTBF, an epidemic size, a conditional mean) — none is point estimation of an unknown population maximum with a bias-correction + minimum-variance-unbiased structure.
- This proposal is **the German-tank MVUE** — the minimum-variance unbiased estimator `N̂ = m(1 + 1/K) − 1` for the maximum of a discrete uniform population, isolated by an unbiasedness control (the estimate hits N), a max-biased-low control (the naive maximum underestimates by the average gap), a closed-form variance anchor, and an efficiency control (it strictly beats the unbiased mean-doubling estimator) — matching none of the completion-cost, waiting-time, optimal-stopping, queueing, sojourn-distribution, bet-sizing, MTBF, epidemic, or regression priors.

## Model basis (declared model-dependence — the P024 discipline)
The exact anchors `E[m] = K(N+1)/(K+1)`, `Var(N̂) = (N−K)(N+1)/(K(K+2))`, and `Var(Ñ) = (N+1)(N−K)/(3K)` rest on the sampling being `K` DISTINCT draws WITHOUT replacement from the discrete uniform `{1..N}` (so `m` is a complete sufficient statistic and the order-statistic moments are exact). The QUALITATIVE claim — the sample maximum underestimates the population maximum, the bias-corrected "max + average gap" estimator is unbiased and minimum-variance, and it beats the mean-doubling unbiased estimator — holds for the continuous uniform analogue too (the `N→∞` limit gives `N̂ = m(K+1)/K` with `Var/N² = 1/(K(K+2))`), so the discrete choice just makes the anchors exact and the seed reproducible. The result depends on standard structural choices, all pinned: (a) sampling is WITHOUT replacement / distinct serials (with-replacement would change the max's law and the sufficiency argument); (b) the population is uniform over `1..N` with no gaps in the serial numbering (real serial systems with resets or blocks break uniformity — the classic caveat); (c) `N ≫ K` so the range is not nearly exhausted (`K = 5 ≪ N = 1000`). The claim is scoped: for `K` distinct serials sampled without replacement from a uniform `1..N`, the MVUE `N̂ = m(1+1/K)−1` is unbiased (`E[N̂]=N`) with variance `(N−K)(N+1)/(K(K+2))` and strictly beats `2x̄−1`, demonstrated on the pinned constants, mechanism-explained (sufficiency of `m` + the expected-gap correction), not asserted as a universal law.

## Probe report (v0, 2026-07-18)

**1. What is this really?** A point-estimation claim: the best estimate of an unknown population maximum `N` from `K` distinct sampled serials is NOT the largest serial seen (`m`, biased low: `E[m] = K(N+1)/(K+1) < N`) but the bias-corrected `N̂ = m(1+1/K)−1` = "largest observed + the average sample gap", which is unbiased (`E[N̂]=N`) and the minimum-variance unbiased estimator (since `m` is sufficient). Controls: the naive max is biased low by the exact gap (measured mean `m` **834.106461** vs N=1000), and the MVUE lands ABOVE the max by a **165.821292** gap while hitting N (mean N̂ **999.927753**).
**2. What would make it false?** If the mean of `N̂` drifted off `N=1000` by ≥3σ (G1 — residual bias in the corrected estimator), or the sample max were NOT biased low or the MVUE did NOT exceed the max by ≥3σ (G2 — either the naive max doesn't underestimate or the correction points the wrong way), or the empirical `Var(N̂)` did NOT match the closed form `28457.0` within 3σ or the MVUE were NOT strictly more efficient than `2x̄−1` by ≥3σ (G3 — wrong variance / no efficiency edge). Any → REJECT.
**3. Simplest version that still bites?** SEED=20260717, 200 replications × 4000 samples of `K=5` distinct serials from `1..1000`; per sample take the max `m` → `N̂ = m·1.2 − 1`; report mean `N̂`, mean `m`, empirical Var(`N̂`), and Var(`2x̄−1`) against the exact closed-form anchors.
**4. What is the counterintuitive core?** The best estimate of how many exist is LARGER than the largest one you have seen — on this world the largest observed serial averages **834** but the honest estimate of `N` is **1000**, an extrapolation of **~166 ABOVE the maximum observation**, because a finite sample almost never catches the top of the range and the expected gap must be added back. And the "obvious" mean-doubling unbiased estimator is **2.33×** noisier than the max-based one.
**5. Where could I be fooling myself?** The unbiasedness control G1 is the guard that the above-the-max correction is exactly right and not an over-correction — measured mean N̂ **999.927753** (|z|=0.3941 vs 1000). The variance gate uses the EXACT order-statistic closed form `(N−K)(N+1)/(K(K+2))`, not an asymptotic `N²/K²`, so there is no small-`K` slop in the anchor — G3 lands at |z|=**0.9831**. The distinct-without-replacement sampling (`rng.sample`) is exactly the regime for which `m` is sufficient and the moments are exact.
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 mean N̂ 999.927753 (se 0.183300) |z|=**0.3941**; G2 mean max 834.106461 (se 0.152750) below N at z_bias=**1086.0456**, N̂−m gap 165.821292 (se 0.238603) at z_above=**694.9667**; G3 Var(N̂) 28509.405891 (se 53.306373) vs 28457.0 |z|=**0.9831** and variance gap 37966.966877 (se 110.211166) at z_efficiency=**344.4929** — G1/G3(a) match the anchors within ~1σ, G2 and G3(b) clear their bars by hundreds of σ; exit 0; results-dict sha256 37cea2bf…af31531.
**7. What decision does it change?** When estimating a population size / maximum from sampled sequential IDs, do NOT anchor at the largest ID observed (biased low) and do NOT reach for "average × 2" (unbiased but ~2.3× noisier at K=5); use `m(1 + 1/K) − 1` (largest observed + average gap) and report its se from `(N−K)(N+1)/(K(K+2))`.
**8. How will we know it worked?** The committed stdlib verifier reproduces the German-tank MVUE under SEED=20260717 with all three gates holding (G1 mean N̂ within 3σ of 1000, G2 max biased low and MVUE above max both by ≥3σ, G3 Var(N̂) within 3σ of the exact closed form AND MVUE strictly more efficient than 2x̄−1 by ≥3σ) and the results-dict sha256 matching 37cea2bfb9b3f60c564d78bb6e5b31c9fcfe8ee7cb11c2fbafe38ddf9af31531.

## One-line correction
To estimate a population maximum from a sample of serials, use the largest one you saw PLUS the average gap the sampling left above it — `N̂ = m(1 + 1/K) − 1`, unbiased and minimum-variance — never the bare maximum (biased low) and never "twice the mean" (unbiased but ~2.3× noisier at K=5).

**Recommendation: sim-ready**
