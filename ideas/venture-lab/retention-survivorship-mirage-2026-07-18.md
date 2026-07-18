# A subscriber base that is a static MIXTURE of constant-hazard segments shows an OBSERVED cohort retention curve that RISES with tenure toward the loyal segment's rate — even though no individual customer ever gets stickier — because the churny segment burns off first. Reading the climbing curve as real stickiness/cohort-quality improvement is a survivorship-bias mirage.

> **State:** sim-ready
> **Class:** venture-lab · subscription/SaaS churn-cohort unit economics · retention-cohort survivorship
> **Target:** sim-lab (VERDICT 119, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@a0564e3 · fetched 2026-07-18T00:52:20Z
> **Harvest source (firsthand):** the retention-cohort idea space read against the venture-lab tree @a0564e3 — the venture priors model referral branching (P098), cash-flow timing (P102), pricing/exposure windows (kill-clock, impulse-price, sample-window) and read-through saturation, but NONE model the elementary duration-analysis fact that a survivor-weighted average over heterogeneous constant-hazard segments drifts up with tenure. The mechanism is the mover-stayer / unobserved-heterogeneity result (Blumen–Kogan–McCarthy 1955; Vaupel–Manton–Stallard frailty 1979; Fader–Hardie shifted-beta-geometric 2007), grounded firsthand by the disclosed sim below (results-dict sha256 1dd09b8d…6856d6), no external repo fetched.

## The phenomenon (one line)
Hold every customer's monthly retention hazard fixed and constant; make the base a mixture of a loyal segment (rate r_A) and a churny segment (rate r_B < r_A). The OBSERVED cohort month-over-month retention rate R(t) — the fraction of this-month survivors still active next month — rises strictly and monotonically with tenure t toward max(r_A, r_B), so a firm that changes NOTHING watches its "retention curve" climb month after month.

## The folk belief
"Our cohort retention is improving — look, the month-over-month retention rate for this cohort was 76% early and is 97% by month 12, so the product is getting stickier / this cohort is higher quality / our retention initiatives are working." Operators read a rising aggregate cohort-retention curve as evidence of a real change in customer behaviour and attribute it to product, onboarding, or cohort quality — then forecast lifetime value and payback off the climbing late-tenure rate.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Model a cohort acquired at t=0 as a static mixture: a fraction w_A of customers are "loyal" with constant monthly retention r_A, and w_B = 1 − w_A are "churny" with constant r_B < r_A. Each customer's survival is geometric: a loyal customer is still active at tenure t with probability r_A^t, a churny one with r_B^t. Nobody's hazard ever changes — retention is constant WITHIN each segment for all time.

The number still active at tenure t is A(t) = N·(w_A·r_A^t + w_B·r_B^t). The OBSERVED cohort month-over-month retention is the ratio of consecutive survivor counts:

  R(t) = A(t+1)/A(t) = ( w_A·r_A^(t+1) + w_B·r_B^(t+1) ) / ( w_A·r_A^t + w_B·r_B^t ).

Rewrite it as a survivor-weighted average of the two segment rates. Let the surviving mix p_A(t) = w_A·r_A^t / (w_A·r_A^t + w_B·r_B^t) be the fraction of tenure-t survivors who are loyal. Then

  R(t) = p_A(t)·r_A + (1 − p_A(t))·r_B.

Because r_A > r_B, the loyal survivors decay slower, so p_A(t) is strictly INCREASING in t and p_A(t) → 1. Therefore R(t) is strictly increasing in t and R(t) → r_A = max(r_A, r_B). The whole rise is composition drift: the aging cohort is increasingly made of the low-hazard segment because the high-hazard segment burned off first. No individual customer's retention improved by a single basis point — the aggregate curve rises purely from selection/survivorship (the mover-stayer effect; unobserved heterogeneity / frailty). Counterintuitive core: a rising cohort-retention curve is the DEFAULT signature of a static heterogeneous base, not evidence of any behavioural improvement — so attributing the climb to stickiness, cohort quality, or a retention program is a survivorship-bias mirage, and forecasting LTV off the inflated late-tenure rate systematically overstates the value of the churny customers you actually keep acquiring.

## Pinned world (committed constants — sim-lab must reproduce exactly)
- SEED = 20260717 (fixed; deterministic run)
- N = 200000 (customers per cohort trial)
- T = 24 (months of observation)
- TRIALS = 400 (Monte-Carlo cohorts)
- SIGMA = 3.0 (gate strength)
- T_LATE = 12 (late tenure at which the survivorship lift is read)
- W_A = 0.5 (loyal-segment share; W_B = 0.5), split as N_A = round(W_A·N) = 100000, N_B = 100000 (exact, so mixture weights are pinned)
- R_A = 0.97 (loyal-segment constant monthly retention); R_B = 0.55 (churny-segment constant monthly retention)
- LIFT_MIN = 0.05 (honest floor the observed lift must clear)
- Per-segment survival simulated at the count level: alive_next ~ Binomial(alive, r_seg) each month (exact Bernoulli sum for small counts, normal approx for large)
- Derived closed-form anchors: R_cf(0) = 0.760000, R_cf(12) = 0.969537, lift_cf = 0.209537, asymptote max(R_A,R_B) = 0.97

## Pre-registered gates (evaluation order G1 → G2 → G3; APPROVE iff ALL hold)
- **G1 — survivorship lift (headline):** the mean observed lift R_obs(T_LATE) − R_obs(0) is ≥ LIFT_MIN = 0.05 by ≥3σ, with the z computed on the ESTIMATED MEAN via its standard error se = std/√TRIALS (the P104/P105 /se convention). Establishes that the observed cohort retention curve strictly rises with tenure.
- **G2 — individual-constant control:** the tenure-pooled within-segment observed retention matches the constant hazard r_A AND r_B within 3σ (|z| < 3 for BOTH segments). Establishes that no customer's retention rises with tenure — every segment is a constant-hazard geometric — so G1's lift is 100% composition/mixing, not a behavioural change.
- **G3 — closed-form anchor MATCH:** the mean observed R_obs(t) reproduces the mixture formula R_cf(t) at t = 0 and t = T_LATE within 3σ (|z| < 3 each). Confirms the sim implements the survivor-weighted-average model the mirage rests on.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier. Any gate failing → REJECT (the rising-curve-from-static-mixture claim, or its survivorship-not-behaviour decomposition, is falsified for these constants). No post-hoc threshold moves; margins reported in σ.

## Disclosed verifier (the sim-lab spec)
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `retention_survivorship_mirage.py`. Seed once with SEED=20260717. For each of TRIALS=400 cohorts: split N=200000 customers into N_A loyal / N_B churny; advance each segment's alive count month by month for T=24 months via Binomial(alive, r_seg) survival; record the aggregate observed month-over-month retention R_obs(0) and R_obs(T_LATE), and the tenure-pooled within-segment observed retention for each segment. Aggregate per-trial statistics with unbiased sample SEs (se = std/√TRIALS); evaluate G1/G2/G3 as above; the closed-form R_cf(t) is computed directly from the pinned weights and rates. Emit a canonical (sorted-keys, comma/colon-separated) results dict and its sha256. Expected results-dict sha256 (dry-sim, this pinned world) = 1dd09b8d06cfbd0155e5822f60f5c1fbf091bf192d4395e503c4f889dd6856d6. Exit 0 iff all gates pass. Deterministic: two runs are byte-identical.

## Why it matters (venture-ops)
Cohort-retention curves are the primary artifact indie/subscription operators use to judge product-market fit, forecast LTV, and size CAC payback. This proposal says a rising cohort-retention curve is the EXPECTED signature of a static heterogeneous base — not a signal that anything improved. Decision rule for an operator: before attributing a climbing aggregate retention curve to a product change or a "better cohort," (1) measure retention WITHIN homogeneous segments (or fit a heterogeneity model such as shifted-beta-geometric) — a genuine improvement shifts the within-segment rate, a mirage does not; (2) forecast LTV from the segment-level hazards, not from the inflated late-tenure aggregate rate, which over-credits the churny customers you keep paying CAC to acquire; (3) compare cohorts at equal tenure and equal composition, since a cohort with MORE heterogeneity can show WORSE early and BETTER late retention purely from mix. Concretely here (w_A=w_B=0.5, r_A=0.97, r_B=0.55): the observed curve climbs from 0.760 to 0.9695 over 12 months, a +0.21 "improvement" that is entirely survivorship — read literally, it would inflate the modelled steady-state lifetime by burying the churny half's real 0.55 hazard under the loyal half's 0.97.

## Dedup
Distinct from the venture and fleet priors:
- **P102 (growth cash-trough trap):** cash-flow TIMING — upfront CAC vs margin accrued over the lifetime makes the faster grower's cash trough deeper. Here there is no cash, no growth rate, no CAC/margin timing; the mechanism is composition drift of an OBSERVED RATE under attrition, a pure survivorship/selection artifact, and the counterintuitive object is a rising retention curve with no behavioural change.
- **P098 (referral-bonus value trap):** an interior optimum on a spend lever driven by a branching amplifier. Here there is no spend lever and no optimum; the claim is a monotone rising aggregate rate from a static mixture.
- **series-readthrough-saturation-crossover / channel-concentration / kill-clock priors:** read-through decay, distribution mix, exposure windows — none model a survivor-weighted average of constant-hazard segments producing a rising cohort metric.
- **P100 (Kelly overbet ruin, fleet):** variance-drag from over-betting; no cohorts, no attrition-composition effect.
The novel content is the survivorship decomposition of a cohort metric: a rising month-over-month retention curve is fully explained by a static two-segment constant-hazard mixture (R(t)=p_A(t)·r_A+(1−p_A(t))·r_B with p_A(t)↑1), with a within-segment-constant control proving the rise is composition, not behaviour.

## Model basis (declared model-dependence — the P024 discipline)
The rising-curve result depends on structural assumptions: (a) the base is a MIXTURE of ≥2 segments with DIFFERENT retention rates (a homogeneous base gives a flat R(t) — heterogeneity is the whole engine); (b) each segment has a CONSTANT hazard (geometric lifetimes) so within-segment retention is tenure-independent; (c) no re-acquisition / resurrection and no composition change other than attrition. If the base were homogeneous, or if churn were front-loaded within a segment (declining hazard) or the loyal share were replenished, the curve's shape changes. The claim is scoped: under a static heterogeneous base of constant-hazard segments — the standard, empirically dominant description of subscription churn — the observed cohort retention curve rises with tenure purely from survivorship, demonstrated on the pinned constants and mechanism-explained via the survivor-weighted-average identity, not asserted as a universal law. The direction (rise, never fall) holds for ANY two constant-hazard segments with r_A ≠ r_B; the pinned magnitudes are illustrative.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed (dry-sim) | Margin | Verdict |
|---|---|---|---|---|---|
| G1 survivorship lift (headline) | separation ≥3σ | ≥3σ | z=3079.64σ | ≫3σ | PASS |
| G2 within-segment r_A match | match (\|z\|<3σ) | <3σ | \|z\|=0.7328σ | 2.27σ headroom | PASS |
| G2 within-segment r_B match | match (\|z\|<3σ) | <3σ | \|z\|=0.8081σ | 2.19σ headroom | PASS |
| G3 anchor R_obs(0) vs R_cf(0) | match (\|z\|<3σ) | <3σ | \|z\|=0.5941σ | 2.41σ headroom | PASS |
| G3 anchor R_obs(12) vs R_cf(12) | match (\|z\|<3σ) | <3σ | \|z\|=1.672σ | 1.33σ headroom | PASS |

## Probe report (v0, 2026-07-18)

**1. What is this really?** A churn-cohort claim: a subscriber base made of a loyal (r_A=0.97) and a churny (r_B=0.55) segment, each with a CONSTANT hazard, produces an OBSERVED cohort month-over-month retention curve that rises from R(0)=0.760 to R(12)=0.9695 — a +0.21 apparent improvement — purely because the churny segment burns off first, with no customer ever getting stickier.
**2. What would make it false?** If the observed curve did NOT rise with tenure (G1 fails), or if the within-segment retention were NOT constant at r_A/r_B (G2 fails — meaning some individual hazard actually changed, so the rise is not pure mixing), or if the observed R_obs(t) did not reproduce the closed-form survivor-weighted average R_cf(t) (G3 fails). Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED=20260717, N=200000, T=24; two segments w_A=w_B=0.5, r_A=0.97, r_B=0.55; count-level Binomial survival; read R_obs(0) vs R_obs(12). The +0.21 lift appears with just two constant-hazard segments.
**4. What is the counterintuitive core?** A rising cohort-retention curve — the artifact operators read as "getting stickier" — is the DEFAULT signature of a static heterogeneous base. R(t) = p_A(t)·r_A + (1−p_A(t))·r_B with the survivor mix p_A(t)↑1, so the average is dragged up toward the loyal rate by selection alone. Nothing improved; the composition changed.
**5. Where could I be fooling myself?** Confounding composition with behaviour — G2 is the explicit control proving each segment's pooled retention matches its constant hazard (|z|=0.73 for r_A, 0.81 for r_B), so G1's lift can only be mixing. Thin late-tenure survivor counts could bias a per-tenure segment estimate, so G2 pools retention across all tenures within a segment (huge at-risk base) rather than reading a noisy late-tenure point. The result is model-dependent (heterogeneity + constant within-segment hazard).
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 lift z=3079.64σ (mean 0.209617 ≥ 0.05); G2 within-segment |z|=0.7328 (r_A) / 0.8081 (r_B), both < 3σ (match); G3 anchor |z|=0.5941 (t=0) / 1.672 (t=12), both < 3σ (match) — all clear their bars; exit 0; results-dict sha256 1dd09b8d…6856d6; two runs byte-identical.
**7. What decision does it change?** Before crediting a rising cohort-retention curve to product/onboarding/cohort-quality, measure retention within homogeneous segments (or fit a heterogeneity model), forecast LTV from segment hazards not the inflated late-tenure aggregate, and compare cohorts at equal tenure AND equal composition. Treat a climbing aggregate retention curve as the null expectation of a heterogeneous base, not as evidence of improvement.
**8. How will we know it worked?** The committed stdlib verifier reproduces the rising observed curve (G1), the within-segment-constant control (G2), and the closed-form mixture anchor (G3) at their thresholds under SEED=20260717, with the results-dict sha256 matching 1dd09b8d06cfbd0155e5822f60f5c1fbf091bf192d4395e503c4f889dd6856d6.

**Recommendation: sim-ready**
