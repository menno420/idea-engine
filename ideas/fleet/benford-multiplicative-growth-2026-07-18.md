# Random growth does NOT spread the leading digit evenly — MULTIPLICATIVE growth makes it Benford: a quantity built by repeated random multiplication has log₁₀(x) doing a random walk, so its mantissa equidistributes and its first significant digit follows P(d)=log₁₀(1+1/d) — digit 1 leads ~30.1% of the time, digit 9 under 4.6%, NOT the naive uniform 1/9≈11.1%. The smallest digit is ~6.6× more likely than the largest, purely from the growth being multiplicative — and the SAME shocks ADDED instead of multiplied are far from Benford. The first digit is a fingerprint of the generating process, not a coin flip.

> **State:** sim-ready
> **Class:** fleet (unrelated / cross-cutting) · number theory / statistics · the leading-digit law (Benford's law) emerging from multiplicative growth
> **Target:** sim-lab (VERDICT 137, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@8b5432c · fetched 2026-07-18T07:40:31Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Benford%27s_law — the first-significant-digit law P(d)=log₁₀(1+1/d) (digit 1 ~30%, digit 9 <5%); "many real-world examples of Benford's law arise from multiplicative fluctuations… the logarithm of the stock price is undergoing a random walk", "most accurate when values are distributed across multiple orders of magnitude"; verified reachable 2026-07-18 (WebFetch, confirms the law and its multiplicative-process / log-random-walk origin).

## The phenomenon (one line)
Grow a quantity by repeated random MULTIPLICATION (each step ×`exp(shock)`) for enough steps and its first significant digit is **not** uniform on 1..9 — it follows **Benford's law** `P(d)=log₁₀(1+1/d)`: **digit 1 about 30.1% of the time, digit 9 under 4.6%**. On the pinned world (100 lognormal multiplicative steps) the simulated digit-1 frequency is **0.299856** against the naive-uniform expectation `1/9≈0.111`, and the whole digit distribution reproduces Benford to a max error of **0.001174**. Take the SAME shocks and ADD them instead of multiplying, and the leading digit is far from Benford (TV distance **0.693128** vs **0.015051**).

## The folk belief
"If a number is produced by a long series of random growth events, its leading digit is as likely to be a 9 as a 1 — randomness should smear the first digit evenly across 1 through 9, so each digit shows up about 1/9 ≈ 11% of the time. A leading-digit distribution that is lumpy (30% ones) means the data was tampered with or hand-picked; genuine random growth gives flat digits." The intuition treats "random" as "uniform on the digits" and reads any first-digit skew as evidence of manipulation rather than as the ordinary signature of a multiplicative process.

## The number-theoretic thesis (reasoned to its fuller form — Q-0254 duty)
The intuition confuses uniformity of the VALUE with uniformity of its LEADING DIGIT, and confuses "random" with "additive." Write any positive `x` as `x = 10^{⌊log₁₀ x⌋} · 10^{frac(log₁₀ x)}`; the leading digit is `d = ⌊10^{frac(log₁₀ x)}⌋`. So the leading digit is a deterministic function of the **fractional part of `log₁₀ x`** (the *mantissa*), and it equals `d` exactly when

    frac(log₁₀ x) ∈ [log₁₀ d, log₁₀(d+1)),   an interval of width log₁₀(1+1/d).

If `frac(log₁₀ x)` is **uniform on [0,1)**, then `P(leading digit = d) = log₁₀(1+1/d)` — Benford's law — by construction. Now multiply: under multiplicative growth `x_n = x_0·∏_{i≤n} exp(g_i)`, so

    log₁₀ x_n = log₁₀ x_0 + (1/ln 10)·Σ_{i≤n} g_i,

which is a **random walk** on the log scale. As `n` grows the walk's spread covers many decades, and the fractional part of a wide-support distribution equidistributes on [0,1) (a Weyl/CLT-mod-1 effect: for a Gaussian log with standard deviation `σ₁₀` decades, the deviation of `frac` from uniform decays like `exp(−2π²σ₁₀²)`, i.e. essentially zero once `σ₁₀ ≳ 1`). Hence the mantissa becomes log-uniform and the leading digit converges to Benford. This is exactly why Benford's law is the leading-digit distribution of prices, populations, account balances, and download counts — quantities built by compounding.

Two consequences the folk belief misses. **(1) It is multiplicativity, not randomness.** Take the identical shocks and ADD them: `x_n = x_0 + Σ_{i≤n} exp(g_i)`. The sum concentrates by the central limit theorem — its coefficient of variation shrinks like `1/√n` — so `x_n` clusters around a single magnitude `n·E[shock]`, its `log₁₀` occupies a tiny sub-decade band, `frac(log₁₀ x_n)` is nowhere near uniform, and the leading digit spikes on whatever single digit that magnitude happens to land on. Additive growth is emphatically **not** Benford. The digit law is a test of the PROCESS (multiplicative vs additive), not of "randomness." **(2) It emerges with mixing.** Few multiplicative steps span too few log-decades for the mantissa to equidistribute, so few-step growth is measurably farther from Benford than many-step growth — Benford is a limit that the compounding *approaches*, and it needs the quantity to range over multiple orders of magnitude (a metric trapped in one decade fails Benford for entirely benign reasons). The honest reading: a lumpy 30%-ones leading digit is the *expected* fingerprint of a compounding quantity, and it is a *deviation* from Benford in such a quantity — not its presence — that flags an anomaly (the basis of Benford-law audit/fraud tests).

## The formal model (committed constants — sim-lab must reproduce exactly)
- A "trajectory" starts at `x₀ = START` and takes `STEPS_MANY` multiplicative steps; each step multiplies by `exp(g)` with `g ~ Normal(LOG_MU, LOG_SIGMA)` (a lognormal growth factor).
- Per trajectory the SAME shock sequence drives three measurements (paired common random numbers): the multiplicative value at `STEPS_FEW` (early checkpoint), the multiplicative value at `STEPS_MANY` (late), and the additive value at `STEPS_MANY` = `START + Σ exp(g_i)`.
- The leading digit of a positive value `v` is `d = ⌊10^{frac(log₁₀ v)}⌋ ∈ {1..9}` (scale-invariant — works for `v<1` too).
- Per replication (`POP = 5000` trajectories) record the batch leading-digit frequency vector for each of the three measurements, and the total-variation distance to Benford `TV = ½·Σ_d |f(d) − log₁₀(1+1/d)|`.
- A statistic's mean and standard error are taken over `TRIALS = 200` independent replications, `se = sample-sd / √TRIALS` (the P104…P122 /se convention: z on an estimated statistic).
- Exact anchor: Benford `P(d) = log₁₀(1+1/d)`; uniform null `1/9`.

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned; SEEDLESS discipline)
- POP = 5000 trajectories per replication, TRIALS = 200 replications
- STEPS_MANY = 100 (converged), STEPS_FEW = 2 (under-mixed early checkpoint)
- LOG_MU = 0.0, LOG_SIGMA = 0.5 (natural-log per-step drift / volatility), START = 1.0
- SIGMA_GATE = 3.0
- Exact Benford anchor: `P(d)=log₁₀(1+1/d)` = {1:0.30103, 2:0.176091, 3:0.124939, 4:0.096910, 5:0.079181, 6:0.066947, 7:0.057992, 8:0.051153, 9:0.045757}; uniform null `1/9 = 0.111111`.

## Pre-registered gates (APPROVE iff ALL hold)
- **G1 — existence (Benford-heavy, not uniform):** the mean digit-1 frequency under many-step multiplicative growth EXCEEDS the uniform null `1/9` by ≥3σ (z on its standard error). Multiplicative growth makes the leading digit Benford-heavy (~30%), not uniform (~11%) — the counterintuitive headline.
- **G2 — dose-response (emergence with steps):** the total-variation distance to Benford SHRINKS from the few-step checkpoint to the many-step checkpoint by ≥3σ (paired common random numbers — the same trajectories measured early vs late). Benford is a limit the compounding approaches: more multiplicative steps ⇒ better mantissa equidistribution ⇒ closer fit.
- **G3 — specificity (multiplicativity, not randomness):** the TV-to-Benford under the ADDITIVE process (the same shocks, summed) EXCEEDS the TV-to-Benford under the MULTIPLICATIVE process by ≥3σ. Additive growth is NOT Benford — the effect is caused by multiplication, not by the shocks being random.

Plus a closed-form ANCHOR cross-check (reported, not a gate): the many-step multiplicative leading-digit frequencies reproduce the exact Benford law `P(d)=log₁₀(1+1/d)` — max abs error over d=1..9 disclosed.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier (the verifier's `all_pass` field encodes exactly `G1 ∧ G2 ∧ G3`). Any gate failing → REJECT (the Benford-from-multiplicative-growth claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; margins reported in σ on the standard error of the estimated statistic.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- mean digit-1 frequency (multiplicative, 100 steps) = **0.299856** (se 0.000470) — Benford `P(1)=0.30103`, uniform null `0.111111`
- digit-1 excess over the uniform null = **0.188745** — the leading digit is ~2.7× the naive 1/9
- mean TV-to-Benford, few-step (2 steps) = **0.095872** (se 0.000466); many-step (100 steps) = **0.015051** (se 0.000299)
- dose (TV few − TV many) = **0.080821** (se 0.000528) — the fit improves with multiplicative steps
- mean TV-to-Benford, additive (100 steps) = **0.693128** (se 0.000073) — additive growth is far from Benford
- specificity (TV add − TV mult) = **0.678077** (se 0.000309)
- closed-form anchor: mean multiplicative digit distribution reproduces Benford to **max abs err 0.001174** (e.g. d=1 sim 0.299856 vs 0.30103; d=9 sim 0.046028 vs 0.045757)
- **G1 existence:** digit-1 excess 0.188745 > 0 at z = **401.6009σ** — PASS (Benford-heavy, not uniform)
- **G2 dose-response:** dose 0.080821 > 0 at z = **152.9590σ** — PASS (Benford fit emerges with steps)
- **G3 specificity:** spec 0.678077 > 0 at z = **2193.9875σ** — PASS (additive is NOT Benford; effect specific to multiplication)
- all_pass = true; **exit 0**
- Two runs byte-identical (deterministic under SEED).
- **Disclosed results-dict sha256 = f9fe4ce5b6350fd76ca5ad9135d7b76bf1b4dabe594cc397fa8d103ce0209598**
  (this is the sha256 of `json.dumps(results, sort_keys=True, separators=(",",":"))` over the results dict BEFORE its `results_sha256` self-field is added — the value the verifier prints as `Results-JSON sha256:`; the P104/P112/P116/P120 self-field posture. The pretty-printed on-disk `benford_multiplicative_growth_results.json` artifact's own `sha256sum` is NOT this digest, and that artifact is not committed.)

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `ideas/fleet/benford_multiplicative_growth.py`. Seeds once with SEED=20260717, then for each of TRIALS=200 replications simulates POP=5000 trajectories of STEPS_MANY=100 lognormal multiplicative shocks under paired common random numbers, measuring the leading-digit distribution of the multiplicative value at STEPS_FEW and STEPS_MANY and of the additive value (same shocks, summed) at STEPS_MANY; it records per-batch digit-1 frequency and TV-to-Benford, then takes means and standard errors over the 200 replications, evaluates G1/G2/G3 on the /se margin, cross-checks the many-step distribution against the exact Benford anchor, and emits a canonical (sorted-keys, comma/colon-separated) results JSON with its sha256. Exit 0 iff all three gates pass.

Reproduce:

```
python3 ideas/fleet/benford_multiplicative_growth.py
```

Expected: all_pass=true, exit 0, G1 z=401.6009σ, G2 z=152.9590σ, G3 z=2193.9875σ, anchor max abs err 0.001174, results-dict sha256 = f9fe4ce5b6350fd76ca5ad9135d7b76bf1b4dabe594cc397fa8d103ce0209598.

## Why it matters (cross-cutting)
Any quantity built by compounding — prices, account balances, populations, file sizes, download/view/request counts, revenue that grows by percentages — has a Benford-distributed leading digit, and that fact is a free audit lens. Decision rule for an operator/analyst: (1) never expect uniform leading digits from "random" growth — multiplicativity forces Benford (digit 1 ~30%), additivity does not, so a first-digit test is really a test of the *generating process*; (2) a *deviation* from Benford in a genuinely-compounding metric is the anomaly signal (fabricated figures, capped/floored values, unit-mixing, or an additive process masquerading as multiplicative) — the presence of Benford is the null, not the red flag; (3) the digit test needs the metric to span multiple orders of magnitude — a quantity confined to one decade fails Benford for benign reasons, so scope the audit to wide-range fields (transaction amounts, populations), not narrow ones (ages, percentages). The same multiplicative machinery that makes wealth concentrate log-normally (Gibrat) leaves this leading-digit fingerprint — one mechanism, two observable signatures.

## Dedup
Distinct from the nearby fleet/unrelated and probability priors:
- **Prior UNRELATED closers** — **kelly-overbet-ruin** (P100, information theory — growth-optimal bet fraction), **epidemic-overshoot** (P104, SIR final size), **regression-to-mean** (P108, conditional-mean shrinkage), **series-reliability-collapse** (P112, reliability — min-of-exponentials MTBF), **arcsine-lead-illusion** (P116, the sojourn-time DISTRIBUTION of a fair walk), **german-tank-mvue** (P120, point estimation of a discrete-uniform maximum): different domains and different objects (a bet fraction, an epidemic size, a conditional mean, an MTBF, a sojourn distribution, a point estimate). None is the leading-digit distribution of a compounding quantity, and none uses the equidistribution-mod-1-of-log₁₀ mechanism or the Benford anchor `log₁₀(1+1/d)`.
- **compounding-reward-inequality** (P115, GAME lane — Gibrat / multiplicative wealth dynamics): shares the log-normal / multiplicative-growth machinery but the OBJECT is different — P115 measures terminal-wealth CONCENTRATION (top-decile share, Gini ~0.68) and prescribes additive/capped rewards for an egalitarian economy; this proposal measures the LEADING-DIGIT distribution (Benford `P(d)=log₁₀(1+1/d)`) and its multiplicative-vs-additive specificity. Wealth-inequality (a Lorenz/Gini object) ≠ leading-digit law (a mantissa-equidistribution object); no shared metric, gate, or anchor.
- **coupon-collector-tail** (fleet, occupancy/collection — completion COST), **inspection-paradox-wait-inflation** (fleet — length-biased renewal waiting time), **secretary-rule-cardinal-regret** (fleet — optimal stopping), **variance-blind-provisioning-trap** (fleet — M/M/1 queueing tail), **simpsons-paradox-aggregation-reversal** (fleet — aggregation reversal): different objects (a completion cost, a waiting time, a stopping rule, a queueing tail, an aggregation reversal) — none is a leading-digit / mantissa-distribution claim.
- The Benford and birthday-collision heads were "set aside by a prior sweep as fully closed-form, nothing a sim settles" — that referred to the STATIC leading-digit audit / static collision probability (a one-line combinatorial fact). This proposal is the DYNAMICAL emergence: a Monte-Carlo that reproduces the Benford DISTRIBUTION from a geometric random walk against the exact anchor AND isolates the mechanism with a dose-response (emergence with steps) and a specificity control (additive is not Benford) — the same sim-reproduces-closed-form posture as P104/P108/P112/P116, not a one-line probability.

## Model basis (declared model-dependence — the P024 discipline)
The exact anchor `P(d)=log₁₀(1+1/d)` is the leading-digit distribution of ANY quantity whose `log₁₀` is uniform mod 1; the multiplicative random walk drives the mantissa to that log-uniform limit (a Weyl/CLT-mod-1 equidistribution). The claim rests on standard structural choices, all pinned: (a) the growth is multiplicative with iid lognormal factors `exp(N(LOG_MU,LOG_SIGMA))` — heavier or thinner-tailed positive factors change the convergence RATE but not the Benford limit, provided the log-shocks have a density and the walk spreads over ≥1 decade; (b) the additive control uses the SAME shocks summed, so the specificity contrast isolates the operation (× vs +), not the shock law; (c) STEPS_MANY=100 with LOG_SIGMA=0.5 gives a log-spread of `≈0.5·√100/ln10 ≈ 2.17` decades, far past the `σ₁₀≳1` equidistribution threshold, so the many-step case is essentially exact Benford while STEPS_FEW=2 (`≈0.31` decades) is deliberately under-mixed to expose the dose-response. The QUALITATIVE claim — multiplicative growth ⇒ Benford leading digits, additive growth ⇒ not, fit improves with log-decades — is the classical Benford result (Hill 1995; the multiplicative-fluctuation / log-random-walk account), so the pinned constants just make the anchor exact and the seed reproducible. The claim is scoped: for iid lognormal multiplicative growth over enough log-decades the leading digit follows `P(d)=log₁₀(1+1/d)`, demonstrated on the pinned constants, mechanism-explained (mantissa equidistribution) with an additive-process specificity control, not asserted as a universal law of all data.

## Probe report (v0, 2026-07-18)

**1. What is this really?** A distributional claim: the first significant digit of a MULTIPLICATIVELY-grown quantity is not uniform on 1..9 (`1/9≈11.1%`) but Benford, `P(d)=log₁₀(1+1/d)` (digit 1 ~30.1%), because `log₁₀(x)` does a random walk whose fractional part (the mantissa) equidistributes on [0,1). Controls: the SAME shocks ADDED are far from Benford (TV **0.693128** vs **0.015051**), and the fit EMERGES with steps (few-step TV **0.095872** → many-step **0.015051**).
**2. What would make it false?** If the many-step multiplicative digit-1 frequency did NOT exceed `1/9` by ≥3σ (G1 — no Benford skew), or the TV-to-Benford did NOT shrink from few-step to many-step by ≥3σ (G2 — no emergence with mixing), or the additive TV did NOT exceed the multiplicative TV by ≥3σ (G3 — additive is just as Benford, so the effect isn't specific to multiplication). Any → REJECT.
**3. Simplest version that still bites?** SEED=20260717, 200 replications × 5000 trajectories; each trajectory multiplies START=1 by `exp(N(0,0.5))` 100 times; take the leading digit `⌊10^{frac(log₁₀ x)}⌋`; report the digit-1 frequency vs `1/9`, the TV-to-Benford at 2 vs 100 steps, and the TV-to-Benford of the same shocks SUMMED, against the exact `log₁₀(1+1/d)` anchor.
**4. What is the counterintuitive core?** "Random growth spreads the first digit evenly" is wrong — multiplicative growth makes digit 1 ~**30%** and digit 9 under **5%**, the smallest leading digit ~6.6× the largest, purely from the ×-operation; and the identical shocks ADDED give a leading digit that is NOT Benford at all. The digit law is a fingerprint of multiplicativity, not of randomness.
**5. Where could I be fooling myself?** The specificity control G3 is the guard against "it's just any random growth": the SAME shocks summed give TV **0.693128** (far from Benford) vs **0.015051** multiplied. The anchor is the EXACT `log₁₀(1+1/d)`, not an asymptotic, and the many-step distribution matches it to **max abs err 0.001174**. Paired common random numbers make the few-vs-many and mult-vs-add contrasts within-trajectory, so the dose and specificity margins are not confounded by between-batch noise.
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 digit-1 excess 0.188745 (se 0.000470) z=**401.6009σ**; G2 dose 0.080821 (se 0.000528) z=**152.9590σ**; G3 spec 0.678077 (se 0.000309) z=**2193.9875σ**; anchor max abs err **0.001174** — all three clear their ≥3σ bars by hundreds-to-thousands of σ and the distribution matches Benford within ~0.001; exit 0; results-dict sha256 f9fe4ce5…0209598.
**7. What decision does it change?** When auditing a compounding metric (transaction amounts, balances, populations, counts), treat a Benford leading-digit distribution as the NULL, not a red flag; investigate DEVIATIONS from Benford; and only run the test on wide-range fields (multiple orders of magnitude) — a one-decade field fails Benford benignly. Never read a lumpy 30%-ones first digit as tampering when the quantity compounds.
**8. How will we know it worked?** The committed stdlib verifier reproduces Benford-from-multiplicative-growth under SEED=20260717 with all three gates holding (G1 digit-1 freq above `1/9` by ≥3σ, G2 TV-to-Benford shrinking with steps by ≥3σ, G3 additive TV above multiplicative TV by ≥3σ), the many-step distribution matching `log₁₀(1+1/d)` within ~0.001, and the results-dict sha256 matching f9fe4ce5b6350fd76ca5ad9135d7b76bf1b4dabe594cc397fa8d103ce0209598.

## One-line correction
The first significant digit of a compounding quantity is Benford (`P(d)=log₁₀(1+1/d)`, digit 1 ~30%), NOT uniform (~11%) — it is a fingerprint of multiplicative growth (additive growth is not Benford), so a first-digit skew is the expected signature of compounding, and it is a *deviation* from Benford, in a wide-range compounding field, that flags an anomaly.

**Recommendation: sim-ready**
