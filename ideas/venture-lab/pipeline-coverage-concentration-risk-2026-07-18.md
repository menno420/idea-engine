# At a FIXED 3× pipeline coverage ratio and a FIXED per-deal win probability, two pipelines with identical coverage and identical win-rate — one granular (75 equal deals), one concentrated (a few whales) — have identical EXPECTED bookings yet the concentrated one MISSES quota far more often (~16% vs ~0%), because bookings variance is exactly proportional to the Herfindahl concentration of deal values: Var(B)=p(1−p)·V²·HHI — so "3× coverage" is not a sufficient statistic for attainment; concentration is

> **State:** sim-ready
> **Class:** venture-lab · sales-ops / pipeline forecasting · quota-attainment concentration risk
> **Slot:** round-33 venture
> **Target:** sim-lab (VERDICT 155, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@b8ba1916398efb099b943f93bb8c4462d013da91 · fetched 2026-07-18T17:55:52Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index (HHI = Σ share²; the concentration of deal values — verified reachable 2026-07-18 via WebFetch) + https://en.wikipedia.org/wiki/Bernoulli_distribution (Var[X] = p(1−p) for a Bernoulli win/loss indicator — verified reachable 2026-07-18 via WebFetch)
> **Harvest source (firsthand):** sales-ops / revenue-operations pipeline practice — the "we're covered, we have 3× pipeline coverage on the number" quarterly-forecast heuristic, applied to a book whose expected value is concentrated in a few large deals.

## The phenomenon (one line)
Two sales pipelines with the SAME coverage ratio (E[bookings]/quota = 3×) and the SAME per-deal win probability have identical expected bookings, but the one whose value is concentrated in a few large deals misses quota far more often — miss-risk is set by the Herfindahl concentration (HHI) of deal values, which the coverage ratio does not see.

## The folk belief
"Pipeline coverage ratio is how you know you'll hit the number. We carry 3× coverage — expected pipeline value is three times quota at our historical win rate — so we're safe. Coverage is the forecast health metric: get to 3× and attainment takes care of itself." Coverage is treated as a sufficient statistic for quota attainment.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Let a pipeline hold deals with values v₁…v_N, each won independently with the same probability p (iid Bernoulli win indicators Xᵢ). Bookings are B = Σ Xᵢvᵢ. By independence,

  E[B] = p·Σvᵢ = p·V,  Var(B) = Σ Var(Xᵢvᵢ) = p(1−p)·Σvᵢ².

The coverage ratio is E[B]/QUOTA = p·V/QUOTA. Two pipelines with the SAME p and the SAME total value V have the SAME coverage and the SAME expected bookings — coverage fixes only the first moment. But rewrite the variance in the deal-share weights wᵢ = vᵢ/V:

  Var(B) = p(1−p)·V²·Σwᵢ² = p(1−p)·V²·HHI,  where HHI = Σwᵢ² is the Herfindahl–Hirschman concentration index of deal values.

So the second moment is governed entirely by HHI, which coverage does not constrain. Hold p and V fixed (identical coverage, identical win-rate) and the variance RATIO between two pipelines is EXACTLY their HHI ratio — p(1−p) and V² cancel:

  Var_conc / Var_gran = HHI_conc / HHI_gran   (an exact identity, not an approximation).

A granular pipeline of N equal deals has HHI = 1/N (its floor, by Cauchy–Schwarz HHI ≥ 1/N for any share vector); a pipeline concentrated in a few whales has HHI ≫ 1/N. With QUOTA = 1,000,000, COVERAGE = 3.0, p = 0.40 ⇒ V = COVERAGE·QUOTA/p = 7,500,000, take a granular book of N_G = 75 equal deals (HHI = 1/75 = 0.013333) and a concentrated book of 8 deals on the ladder [0.40, 0.20, 0.1333, 0.0933, 0.0667, 0.0533, 0.0333, 0.02]·V (HHI = 0.235289, i.e. HHI_ratio = 17.65). Both have E[B] = 3,000,000 = exactly 3× quota. Yet the concentrated bookings SD is √17.65 ≈ 4.2× the granular SD, so its distribution has far more mass below the 1,000,000 quota line. In the pinned world the granular pipeline essentially never misses (its bookings cluster tightly at 3× quota) while the concentrated pipeline misses ~16% of the time — the SAME coverage, the SAME win-rate, an order-of-magnitude different miss probability. The trap: the pipeline-coverage metric certifies both books as equally healthy, then attainment forecasting is blind-sided when the concentrated book's two-whale quarter comes up short — the miss risk was set by concentration, not coverage, all along.

## Pinned world (committed constants — sim-lab must reproduce exactly)
- SEED = 20260717 — fleet-pinned; one `random.seed(SEED)`, single stream, granular simulated before concentrated.
- P_WIN = 0.40 — per-deal win probability, iid Bernoulli, held EQUAL across both pipelines.
- QUOTA = 1,000,000 (dollars) — the period quota; miss ⇔ bookings < QUOTA (strict).
- COVERAGE = 3.0 — the pipeline coverage ratio E[B]/QUOTA, held EQUAL across both pipelines.
- PIPELINE_VALUE = COVERAGE·QUOTA/P_WIN = 7,500,000 — the total pipeline value V both books share (so E[B] = P_WIN·V = 3,000,000 = 3× quota for both).
- N_G = 75 equal deals (each 100,000) — the granular pipeline; HHI = 1/75 = 0.013333.
- Concentrated ladder weights [0.40, 0.20, 0.1333333333, 0.0933333333, 0.0666666667, 0.0533333333, 0.0333333333, 0.02], rescaled so the deals sum to exactly V — the "few whales" pipeline; HHI = 0.235289.
- N_BATCH = 40 independent batches × BATCH_TRIALS = 2000 trials = 80,000 trials per pipeline — batch-means (method of independent replications) for honest, distribution-free standard errors on the coverage/variance/miss estimators.
- SIGMA = 3.0 — all gates.
- Closed-form anchor: Var(B) = p(1−p)·V²·HHI, with the EXACT identity var_ratio = HHI_ratio (= 17.646667) because p(1−p) and V² cancel between the two pipelines. Both means are pinned at p·V = 3,000,000.

## Pre-registered gates (evaluation order G1 → G2 → G3; APPROVE iff ALL hold)
- **G1 — anchor / variance law.** The empirical per-trial bookings variance matches the closed form p(1−p)·Σvᵢ² for BOTH the granular and the concentrated tier within |z| ≤ 3σ (two-sided). This anchors the simulator to the second-moment identity Var(B) = p(1−p)·V²·HHI before any headline fires. Observed z = 1.014985 (the max over the two tiers).
- **G2 — coverage control (the confound held).** Both empirical coverage ratios (mean bookings / QUOTA) equal COVERAGE = 3.0 within |z| ≤ 3σ (two-sided). This PROVES coverage is held equal between the two pipelines, so coverage cannot be the differentiator behind the miss-rate gap — the only thing that differs is concentration. Observed z = 1.218738 (the max over the two tiers; empirical coverage_granular = 2.998414, coverage_conc = 2.993622).
- **G3 — head / the counterintuitive result.** The concentrated pipeline's quota-miss rate strictly EXCEEDS the granular pipeline's, miss_conc − miss_gran at z ≥ 3σ (one-sided). At identical coverage and identical win-rate, concentration alone drives a large miss-rate gap. Observed z = 144.379268 (miss_conc = 0.1562, miss_gran = 0.0, miss_diff = 0.1562).

## Pre-registered decision rule
APPROVE (sim-ready → APPROVE) iff G1 ∧ G2 ∧ G3 all hold on the byte-identical committed verifier at SEED = 20260717, the results-dict sha256 matches EXACT, and the double-run is deterministic (exit 0 both times). Any gate miss (G1/G2 |z| > 3, or G3 z < 3), digest mismatch, or non-determinism → REJECT.

## Disclosed verifier (the sim-lab spec)
Committed at `ideas/venture-lab/pipeline_coverage_concentration_risk.py`, stdlib only (`random, math, json, hashlib`). Digest posture: **WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY** — the results dict carries NO `results_sha256` field; the sha256 is taken over the COMPACT canonical serialization (`json.dumps(results, sort_keys=True, separators=(",",":"))`), while stdout prints the PRETTY `indent=2` form (the TWIST — the pretty stdout dump is NOT the hashed preimage). No on-disk JSON is written. Determinism: one `random.seed(SEED)`, single stream, granular pipeline simulated before concentrated, fixed batch/trial/deal order, no wall-clock.
Expected results-dict sha256 (this pinned world) = `e8534a6c6097e08e632ef492de89cf7c0abc06f41c6cc56937db5ffb3fc5eb64`.

## Why it matters (venture-ops)
Sales forecasting, board commits, and hiring/spend plans lean on "pipeline coverage" — get to 3× (or 4×) and the number is safe. This result says coverage certifies only the MEAN; the probability of actually missing quota is governed by the concentration of the pipeline's value (HHI), which the coverage ratio is structurally blind to. Two reps or two regions at the SAME 3× coverage can have wildly different miss odds if one is carrying its number on two whales and the other on fifty mid-market deals. The fix is to report the pipeline's HHI (or its inverse, the effective number of deals N_eff = 1/HHI) alongside coverage, size the attainment-at-risk band off √HHI, and treat a low effective-deal-count book as a coverage-invisible miss risk — the same lens antitrust and portfolio theory already use for concentration. It also flips a common comfort: adding coverage by landing one more whale can RAISE miss risk (it raises HHI) even as it raises the coverage ratio; only broadening the deal mix lowers it.

## Dedup
Distinct from every prior venture-lab head:
- **referral-bonus-value-trap** — unit-economics of a referral incentive; a mean/CAC argument, not a variance/attainment one.
- **growth-cash-trough** — cash-flow timing under growth; a liquidity-timing result, no concentration/variance object.
- **retention-survivorship-mirage** — survivorship bias in cohort retention; a point-estimate bias, not a second-moment concentration result.
- **discount-breakeven** — the volume needed to offset a discount; a deterministic margin identity.
- **freemium-support-cost-inversion** — support cost outrunning conversion; a mean-cost inversion.
- **sales-ramp-capacity-drag** — ramp-time drag on effective capacity; a throughput/timing result.
- **nrr-composition-mirage** — NRR as a mix (composition) bias; a point-estimate mix result on revenue composition, not a bookings-variance result.
- **partner-channel-margin-stacking** — double-marginalization down a channel; a pricing/margin identity.
- **annual-prepay-financing-trap** — the financing cost hidden in annual prepay; a timing/discount result.
- **blended-churn-ltv** — Jensen convexity of 1/churn biasing an LTV point estimate; a convexity bias on a point estimate.
- **usage-based-billing-variance-shock (P138)** — the CLOSEST relative: it too rides HHI, but it is about *metered-revenue* volatility (CV of a sum of independent account USAGE draws diversifying as 1/HHI, a per-account CV·√HHI result). THIS head is about a different object: pipeline-coverage SUFFICIENCY and quota-MISS probability, where the randomness is Bernoulli WIN/LOSS on deals (not usage magnitude), the metric is P(bookings < quota) (a threshold-crossing tail probability, not a CV), and the punchline is that the coverage RATIO — a first-moment forecast metric with no analogue in the billing head — fails to bound miss risk. Both invoke HHI; the modeled quantity (win indicator vs usage size), the reported statistic (miss probability vs revenue CV), and the folk metric under attack (coverage ratio vs account count) are all different. Touched by none of the above.

## Model basis (declared model-dependence — the P024 discipline)
- Wins modeled as iid Bernoulli(p) per deal — independent, equal win probability. The variance identity Var(B) = p(1−p)·Σvᵢ² and the exact var_ratio = HHI_ratio hold for ANY independent-deal model with a common per-deal win probability; the result is model-LIGHT — the second-moment law is distribution-free in the win mechanism as long as deals are independent.
- The MAIN dependence is the independence assumption. Positively correlated wins (a common macro/quarter shock hitting all deals) only ADD variance on top of the HHI floor, so independence makes the miss-rate gap CONSERVATIVE — real correlation widens it. Heterogeneous per-deal win probabilities (e.g. whales harder to close) shift the exact numbers but not the sign; the HHI-driven ordering survives as long as the concentrated book's value-weighted variance exceeds the granular book's.
- The concrete miss rates (~16% vs ~0%) and HHI_ratio = 17.65 are specific to the pinned p, quota, coverage, N_G, and the 8-deal ladder; the exact identity var_ratio = HHI_ratio and the "coverage does not bound miss risk" conclusion are general.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed z | Margin | Verdict |
|------|------|-----------|-----------|--------|---------|
| G1 anchor / variance law | bracket (two-sided) | \|z\| ≤ 3σ | z = 1.014985 | 1.985 | PASS |
| G2 coverage control | bracket (two-sided) | \|z\| ≤ 3σ | z = 1.218738 | 1.781 | PASS |
| G3 head / miss-rate gap | one-sided sep. | z ≥ 3σ, diff > 0 | z = 144.379268 | 141.379 | PASS |

## Probe report (v0, self-adversarial)
**1. Isn't this just portfolio concentration restated?** Structurally yes — Var(B) = p(1−p)·V²·HHI is a portfolio second-moment identity — but the content is the SALES-OPS consequence: the coverage RATIO, the field's headline forecast-health metric, is a pure first-moment object and therefore cannot see the very concentration that sets miss risk. The novelty is naming coverage as an insufficient statistic and showing the miss-rate gap it hides, not re-deriving HHI.
**2. Does the result survive correlated wins?** The exact var_ratio = HHI_ratio identity assumes independence. Positive correlation across deals ADDS a covariance term to BOTH pipelines' variance, which only widens the concentrated book's tail below quota — so correlation makes the miss-rate gap larger, not smaller. The independence model is the conservative case; the sign is robust.
**3. Is "3× coverage" a real folk belief or a strawman?** Real and standard: pipeline coverage (3×–4× of quota) is a near-universal sales-forecasting rule of thumb, tracked in every major CRM/RevOps dashboard as the headline "are we covered" metric. The claim under attack — that hitting the coverage number certifies attainment — is exactly how it is used.
**4. Why strict b < QUOTA for a miss?** Quota attainment is conventionally "made the number or not"; bookings exactly equal to quota is attainment, so a miss is strictly below. The strict inequality is the standard convention and, with continuous-ish dollar sums, ties are negligible anyway.
**5. Does the granular pipeline ever miss?** In the pinned world its miss rate is ~0 (miss_granular = 0.0 over 80,000 trials) — 75 equal deals at p = 0.40 concentrate bookings tightly at 3× quota (SD ≈ √(p(1−p))·V/√75), so the 1× quota line sits far in the left tail. That is the whole point: identical coverage, and one book essentially never misses while the other misses ~16%.
**6. Is the HHI variance identity exact or asymptotic?** EXACT and finite-sample — Var(B) = p(1−p)·Σvᵢ² is an algebraic identity for a sum of independent scaled Bernoullis, no large-N limit invoked. The var_ratio = HHI_ratio cancellation (p(1−p), V² drop out) is likewise exact. G1 checks the simulator reproduces it; it is not an approximation being tested.
**7. Would unequal p per deal break it?** It changes the exact numbers — with deal-specific pᵢ the variance is Σ pᵢ(1−pᵢ)vᵢ² and no longer factors cleanly through a single HHI — but the ORDERING survives whenever the concentrated book's value-weighted win variance exceeds the granular book's, which holds broadly (a whale contributes vᵢ² to the variance regardless of its pᵢ). The sign and the "coverage is insufficient" conclusion are robust; only the clean HHI_ratio identity needs equal p.
**8. Is the effect an artifact of the specific 8-deal ladder?** No — the ladder is one concrete high-HHI book chosen for a clean HHI_ratio ≈ 17.65; ANY pipeline with HHI ≫ 1/N_G at the same coverage produces the same qualitative gap (larger HHI ⇒ larger gap). G1 anchors the variance to the ladder's actual HHI, and G2 confirms coverage is held equal, so the gap is attributable to concentration, not to the particular weights.

**Recommendation: sim-ready**
