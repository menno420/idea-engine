# For two SaaS companies matched on current ARR and current growth, a marginal point of growth endurance buys strictly more terminal ARR than a marginal point of current growth

> **State:** sim-ready
> **Class:** counterintuitive-compounding / venture-lab (growth-decay slot)
> **Slot:** round-36 VENTURE
> **Target:** sim-lab (VERDICT 167, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine/blob/ff4ac714e8e68f7c28f070b7f69141fd8cda873d/control/outbox.md@05c6e63d399bceed50b337b4a884a74eea0a05b3 · fetched 2026-07-19T04:04:35Z
> **Reference (external, reachable):** Bessemer Venture Partners "State of the Cloud" — growth-endurance benchmarks (the fraction of last year's growth a cloud company retains this year); McKinsey & Company, "Grow fast or die slow" (2014) — growth persistence dominates margin in long-run software value creation.
> **Harvest source (firsthand):** ideas/venture-lab/growth_endurance_dominance.py + its recorded double-run (this branch).

## The phenomenon (one line)
Take two SaaS companies with the same current ARR and the same current growth; the one whose growth DECAYS more slowly (higher endurance r) ends up worth far more — and at the margin an extra point of endurance buys strictly more terminal ARR than an extra point of headline growth, because endurance sits in the amplifying denominator of the compounding sum.

## The folk belief
Growth is the number that matters: to build terminal value you buy the highest current growth rate you can, and endurance ("will it keep growing?") is a soft, second-order concern. Under that model two companies matched on current growth are worth the same, and a marginal point of headline growth always beats a marginal point of persistence.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Model growth as geometric decay: period-k growth g_k = g0 · r**k, where g0 is current growth and r ∈ (0,1) is growth endurance (the fraction of last period's growth that persists). Terminal ARR after a horizon is the product of (1 + g_k), so terminal log-ARR is the sum
    L(g0, r) = Σ_{k<H} log1p(g0 · r**k).
For small growth this sum is ≈ Σ g0·r**k = g0/(1−r) over an infinite horizon — the geometric sum. Endurance r sits in the denominator (1−r), so terminal log-scale is far more sensitive to r than to g0. Matched marginal perturbations DELTA=0.05 applied to each:
    sens_r = L(g0, r+DELTA) − L(g0, r),   sens_g = L(g0+DELTA, r) − L(g0, r).
The ratio sens_r / sens_g ≈ [g0/(1−r)²] / [1/(1−r)] = g0/(1−r): a marginal point of endurance dominates a marginal point of current growth exactly when g0 > 1−r — the growth-stage regime. It crosses over (headline growth wins) for low-growth companies where g0 < 1−r — the honest boundary, disclosed below.

## Pinned world (committed constants — the verifier is the contract)
SEED=20260717 · N=1500 companies per trial · TRIALS=300 independent trials → between-trial z-scores · HORIZON=12 years of ARR accumulation · DELTA=0.05 matched perturbation applied to g0 and to r · REL_NULL=0.10 (G2 null). Base draw: g0 ~ clamp(lognormal(ln 0.60, 0.40), [0.15, 2.00]), r ~ clamp(normal(0.78, 0.06), [0.55, 0.93]). Shifted draw (tighter market — lower endurance, higher headline growth): g0 ~ clamp(lognormal(ln 0.90, 0.40), [0.20, 2.50]), r ~ clamp(normal(0.68, 0.06), [0.50, 0.90]). Reseeded per run; redrawn per company.

## Pre-registered gates (evaluation order G1 → G2 → G3; APPROVE iff ALL hold)
- **G1 — the dominance has the right sign.** mean(sens_r − sens_g) > 0 at z ≥ 3. Observed gap_mean = **+0.354025**, z = **+996.770037**, frac_dominant = **0.992229**.
- **G2 — the dominance is large, not marginal.** mean(sens_r/sens_g − 1) ≥ 0.10 at z ≥ 3 (one-sample z vs null 0.10). Observed rel_mean = **+2.219712** (≈ +222%), z = **+925.513190**.
- **G3 — robust to a shifted (tighter-market) distribution.** under the shifted draw (lower endurance, higher headline growth), mean(sens_r − sens_g) > 0 at z ≥ 3. Observed gap_mean = **+0.322362**, z = **+1107.766114**, frac_dominant = **0.997938**.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold on a clean-room re-run (SEED=20260717) with the results-dict sha256 matching. Any gate false → REJECT naming first_failing_gate. Observed all_pass = **true**, first_failing_gate = **null**.

## Disclosed verifier (the sim-lab spec)
`ideas/venture-lab/growth_endurance_dominance.py` — stdlib only (math, json, hashlib, random, statistics). Posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY. Builds the ordered results dict, asserts an in-process double run is byte-identical, prints the compact JSON dict (sort_keys) and its sha256. Expected results-dict sha256:
    5dccb475a6fde0ebd5c557b3baa393be8430b91902bbadedb7f5bd16754495bf
Re-run twice cross-invocation; both must print IDENTICAL output and the sha256 above; exit 0 iff all_pass.

## Why it matters
Growth-endurance is the load-bearing correction to "buy the highest growth rate." Two companies at the same ARR and same current growth are NOT worth the same — the slower-decaying one compounds to a far larger terminal ARR, and at the margin an operator or investor gets more terminal value per point of retained persistence than per point of headline acceleration. The same denominator amplification recurs wherever a decaying series compounds: net-dollar-retention on an expanding base, subscriber-growth persistence, any "will the growth stick" question. It is a clean, quantitative instance of why the durability of growth, not its instantaneous level, drives long-run software value — the exact signature Bessemer's growth-endurance benchmarks and McKinsey's "grow fast or die slow" were built to name.

## Dedup (contrast vs prior lane heads)
- vs **refund-window-abuse-threshold (P prior)** — a post-purchase refund-policy optimum under a step-discontinuous abuse term; this is top-line ARR growth *decay* over a horizon, no refund/return mechanic and no discontinuity.
- vs **series-readthrough-saturation-crossover / bundle-pwyw-floor-lattice / impulse-price-blanket** — pre-purchase price/quality structure on a catalog; none models a compounding growth series or a persistence parameter.
- vs any **cohort retention / churn** head — those model the fraction of *customers* retained period to period; this models the fraction of last period's *growth* that persists (a top-line growth-rate decay, r on g_k), a distinct object: growth endurance, not customer retention.
- Crossover honesty: adjacent to any prior "compounding / retention" framing, but no prior venture head models a geometric growth-decay series or the g0/(1−r) sensitivity. Distinct mechanism.

## Model basis (declared model-dependence — the P024 discipline)
Exact given the model: geometric growth decay g_k = g0·r**k, terminal value as the product of (1+g_k), matched additive DELTA perturbation, 12-year horizon truncation of the infinite product. NOT a claim about a specific company; the claim is that this documented mechanism is real, sign-correct, large, and robust to draw noise within the growth-stage regime. Dependence disclosed: the *sign* is structural wherever g0 > 1−r (growth-stage); for low-growth companies (g0 < 1−r) it crosses over and headline growth wins. The horizon is a truncation — the 12-year product is horizon-stable (the tail terms r**k vanish geometrically), not a tuned cutoff.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | z | Verdict |
|------|------|-----------|----------|---|---------|
| G1 | sign | mean gap > 0, z≥3 | +0.354025 | +996.770037 | PASS |
| G2 | effect size | mean rel ≥ 0.10, z≥3 | +2.219712 | +925.513190 | PASS |
| G3 | robustness | shifted mean gap > 0, z≥3 | +0.322362 | +1107.766114 | PASS |

## Probe report (v0, self-adversarial)
**1. Real dominance or a rigged perturbation?** Matched — the identical DELTA=0.05 is applied to g0 and to r, and each sensitivity is a finite difference of the same terminal-log function. No asymmetric nudge; the gap is the structure g0/(1−r), not a tuned step.
**2. Knife-edge at the nominal draw?** No — G1 samples 300 trials × 1500 companies ~ base draw; frac_dominant = 0.992, i.e. dominance holds for ~99% of drawn growth-stage companies. A broad regime, not a point.
**3. Where does it break?** For low-growth companies where g0 < 1−r the ratio g0/(1−r) < 1 and headline growth wins — the crossover. The base draw is a growth-stage population (median g0 ≈ 0.60, r ≈ 0.78, so 1−r ≈ 0.22 < g0), so ~0.8% of draws fall on the far side and reverse. Disclosed, not hidden.
**4. z inflated by huge N?** The z is large because the effect is large relative to between-trial variance, not merely because N=1500. G2's z is against a *non-zero* null (0.10) to test magnitude, not just sign; the relative dominance is ≈ +222%, far past the 10% floor.
**5. Determinism?** SEED=20260717 pinned; in-process double run asserted byte-identical; cross-invocation double run printed IDENTICAL with sha256 5dccb475…95bf. A verdict re-run must reproduce that digest.
**6. Horizon rigged?** HORIZON=12 truncates an infinite product whose tail terms r**k vanish geometrically (r ≤ 0.93 → r**12 ≤ 0.42, and the log1p of a decayed growth is small); the sign and ordering are horizon-stable, not a cutoff tuned to force a pass. Constants pinned and stated.
**7. Float ordering perturbing the digest?** All dict floats round()-ed to 6 dp before hashing; trial sums in fixed order; compact JSON with sort_keys; no set/dict-ordering nondeterminism. The in-process assert catches drift.
**8. Real or toy?** The growth-endurance benchmark (last year's growth retained this year) is a published field signature — Bessemer's "State of the Cloud" tracks it directly, and McKinsey's "Grow fast or die slow" found growth persistence, not instantaneous level, separates long-run software winners. The mechanism names why.

**Recommendation: sim-ready**
