# Under usage-based pricing a firm's monthly revenue is a sum over N independent accounts, so the law of large numbers "should" smooth it as CV_account/√N — but heterogeneous account SIZES make revenue behave like it has only N_eff = 1/HHI ≪ N accounts, a ~4× volatility shock the account-count intuition hides

> **State:** sim-ready
> **Class:** venture-lab · unit-economics · usage-based revenue concentration risk
> **Target:** sim-lab (VERDICT 151, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@f008e130a058b1a62b92d053bb6fd315ec730ac4 · fetched 2026-07-18T15:28:13Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index (HHI = Σ share²; the inverse 1/HHI is the "effective number" of equal-sized units; verified reachable 2026-07-18 via WebFetch) + https://en.wikipedia.org/wiki/Coefficient_of_variation (CV = σ/μ; verified reachable 2026-07-18 via WebFetch)
> **Harvest source (firsthand):** usage-based / consumption-pricing SaaS finance practice — the "with thousands of accounts our metered revenue is smooth by the law of large numbers" planning assumption, applied to a book whose account sizes span orders of magnitude.

## The phenomenon (one line)
A firm billing by consumption has monthly revenue R = Σᵢ Uᵢ over N independent accounts; the folk model says the revenue coefficient of variation shrinks like CV_account/√N, but when account SIZES are heterogeneous the true CV is CV_account·√HHI — governed by the Herfindahl concentration HHI = Σwᵢ², so the book diversifies as if it held only N_eff = 1/HHI accounts, not N, and revenue is far more volatile than the account count suggests.

## The folk belief
"We have N usage-based accounts, and each account's usage is independent, so the law of large numbers averages them out: relative revenue volatility falls like 1/√N. With thousands of accounts, monthly revenue is smooth — we can forecast off the mean and ignore single-account swings." Account count is treated as the diversification lever.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Let account i have mean monthly usage mᵢ and a per-account coefficient of variation CV_account (usage Uᵢ independent across accounts, with Var(Uᵢ) = CV_account²·mᵢ²). Total revenue R = Σ Uᵢ has mean Σmᵢ and, by independence, variance Σ Var(Uᵢ) = CV_account²·Σmᵢ². The revenue coefficient of variation is therefore

  CV(R) = √(CV_account²·Σmᵢ²) / Σmᵢ = CV_account · √(Σmᵢ² / (Σmᵢ)²) = CV_account · √HHI,

where HHI = Σ wᵢ² with wᵢ = mᵢ/Σm the revenue share of account i — the Herfindahl–Hirschman concentration index. Define N_eff = 1/HHI, the "effective number of equal-sized accounts." The law-of-large-numbers folk model is the special case where every account is the same size: then wᵢ = 1/N, HHI = 1/N, N_eff = N, and CV(R) = CV_account/√N. But Cauchy–Schwarz forces HHI ≥ 1/N for ANY size distribution, with equality only when all sizes are equal — so the naive CV_account/√N is a strict LOWER bound and the true CV is always ≥ it, growing as the book concentrates. The count N does NOT set diversification; the effective count N_eff = 1/HHI does, and for a heavy-tailed size book N_eff is a small constant no matter how large N grows. Concretely, with Zipf-law sizes mᵢ = 1/i for i = 1..400 (a canonical power law), Σmᵢ = 6.569930, Σmᵢ² = 1.642437, so HHI = 0.038051 and N_eff = 26.280443 — a 400-account book diversifies like ~26 accounts. At CV_account = 0.5 the true revenue CV is 0.5·√0.038051 = 0.097533 versus the naive 0.5/√400 = 0.025000 — a 3.901339× volatility multiplier, and the single largest account already carries 15.2% of revenue (w₁ = 0.152209). The trap runs opposite to the count intuition: diligence counts accounts and declares the book diversified, then is blind-sided when one metered whale's usage dip moves the whole revenue line — the variance floor was set by concentration, not count, all along.

## Pinned world (committed constants — sim-lab must reproduce exactly)
- SEED = 20260717 — fleet-pinned; one `random.seed(SEED)`, single stream.
- N = 400 accounts.
- K_SHAPE = 4.0 — per-account usage Uᵢ ~ Gamma(shape 4, scale mᵢ/4), so E[Uᵢ] = mᵢ and CV_account = 1/√4 = 0.5 (any distribution with this mean/variance gives the same CV(R) — the result is a second-moment identity, distribution-free; Gamma is the concrete stdlib draw).
- CONCENTRATED book: sizes mᵢ = 1/i for i = 1..400 (Zipf / power law, α = 1).
- UNIFORM book: every mᵢ = mean(concentrated sizes) — SAME N, SAME total mean revenue, SAME per-account CV; HHI = 1/N exactly (isolates concentration for G3).
- N_BATCH = 60 independent batches × BATCH_MONTHS = 250 months — batch-means (method of independent replications) for a valid, distribution-free SE on the CV ratio estimator.
- SIGMA = 3.0 — all gates.
- Closed-form anchors (computed exactly from the deterministic size vectors, NOT hard-coded):
  - CONCENTRATED: HHI = 0.038051, N_eff = 26.280443, CV(R)_exact = 0.097533; naive LLN CV = CV_account/√N = 0.025000; volatility multiplier = 3.901339.
  - UNIFORM: HHI = 1/400 = 0.002500, CV(R)_exact = 0.025000 (= naive exactly).

## Pre-registered gates (evaluation order G1 → G2 → G3; APPROVE iff ALL hold)
- **G1 — the diversification shortfall exists.** The simulated CONCENTRATED-book revenue CV strictly EXCEEDS the naive CV_account/√N at ≥ 3σ. Confirms the account-count intuition under-states volatility, with the sign Cauchy–Schwarz (HHI ≥ 1/N) forces. Observed z = 116.537002.
- **G2 — sim reproduces the EXACT closed form.** The simulated CONCENTRATED mean CV equals the analytic CV_account·√HHI = 0.097533 within noise: |z| < 3σ (no-significant-deviation bracket). Anchors the estimator to the second-moment identity. Observed z = −1.343306.
- **G3 — the shock is CONCENTRATION-driven, not N or per-account CV.** With N, total mean revenue, and per-account CV all held fixed, the CONCENTRATED-book CV exceeds the UNIFORM-book CV at ≥ 3σ, and the uniform CV matches the naive 1/√N (gap negligible < 0.01). Isolates size concentration (HHI) as the driver. Observed z = 113.523243, uniform–naive gap = 0.000005.

## Pre-registered decision rule
APPROVE (sim-ready → APPROVE) iff G1 ∧ G2 ∧ G3 all hold on the byte-identical committed verifier at SEED 20260717, the results-dict sha256 matches EXACT, and the double-run is deterministic (exit 0 both times). Any gate miss, digest mismatch, or non-determinism → REJECT.

## Disclosed verifier (the sim-lab spec)
Committed at `ideas/venture-lab/usage_based_billing_variance_shock.py`, stdlib only (`random, math, json, hashlib`). Digest posture: **WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY** — the results dict carries NO `results_sha256` field; the sha256 is taken over the COMPACT canonical serialization (`json.dumps(results, sort_keys=True, separators=(",",":"))`), while stdout prints the PRETTY `indent=2` form (the TWIST — pretty stdout ≠ hashed preimage). No on-disk JSON is written. Determinism: one `random.seed(SEED)`, single stream, concentrated book drawn before uniform within each batch, fixed batch/month/account order, no wall-clock.
Expected results-dict sha256 (dry-sim, this pinned world) = `4cd2fd286d5530ce001dc49becb80c29ced6484b834e051be59ed2acbf7a7d6b`.

## Why it matters (venture-ops)
Revenue forecasts, covenant headroom, and cash-runway models under usage-based pricing lean on "many accounts ⇒ smooth revenue." This result says the smoothing is governed by N_eff = 1/HHI, not the headline account count: a book whose usage is concentrated in a handful of large metered accounts carries revenue volatility a √(N/N_eff) multiple above the law-of-large-numbers estimate (~4× at Zipf sizes over 400 accounts), and the exposure is a single-account event, not a diversified wobble. The fix is to report N_eff = 1/HHI alongside the account count, size the revenue-at-risk band off CV_account·√HHI, and treat top-share accounts as concentration risk — the same lens antitrust and portfolio theory already use (HHI, inverse participation ratio). It also flips the usual comfort: growing the logo count does nothing for volatility if the new logos are small; only flattening the size distribution (or hedging the whales) moves N_eff.

## Dedup
Distinct from the venture-lab book: P098 referral trap, P102 cash-trough (timing), P106 retention mirage (survivorship), P110 discount-depth, P114 freemium inversion, P118 sales-ramp drag, P122 NRR mirage (revenue COMPOSITION, a point-estimate mix bias — this is a second-moment revenue-VARIANCE result), P126 double marginalization, P130 annual-prepay trap (financing/timing), P134 blended-churn LTV understatement (Jensen convexity of the CONVEX map 1/c biasing a POINT estimate — here the point mean revenue is unbiased; the bias is in the count-based VARIANCE model). Distinct from the fleet-lab N_eff result P109 correlated-fleet-variance-floor: that floor is CORRELATION-driven (identical units with pairwise ρ leave a residual ρσ² as N→∞); this floor is SIZE-HETEROGENEITY-driven (independent, unequal accounts; the driver is the Herfindahl concentration of sizes, and it needs no correlation at all). Both land on "effective N ≪ nominal N" but by orthogonal mechanisms (covariance vs. size dispersion) in different domains (fleet latency vs. metered revenue).

## Model basis (declared model-dependence — the P024 discipline)
- Accounts modeled as INDEPENDENT (no common shock). Real usage is often positively correlated (macro cycles, shared outages); correlation only ADDS variance on top of the concentration floor, so the independence assumption makes the result CONSERVATIVE — the true CV is ≥ CV_account·√HHI.
- Per-account CV_account held constant across accounts (0.5). If large accounts are relatively STEADIER (lower CV) the concentrated CV shrinks; if they are spikier (bursty metered workloads, common) it grows. The SIGN and the √HHI scaling are distribution-free; the exact 3.9× uses the constant-CV, Zipf-α=1 world.
- Sizes modeled Zipf α=1 (mᵢ = 1/i). The CV(R) = CV_account·√HHI identity and the HHI ≥ 1/N floor are exact for ANY size vector; the concrete N_eff ≈ 26 and 3.9× multiplier are specific to this power law and N. A heavier tail (α < 1) concentrates further and widens the gap.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed (dry-sim) | Margin | Verdict |
|------|------|-----------|--------------------|--------|---------|
| G1 shortfall exists | one-sided sep. | z ≥ 3σ, diff>0 | z = 116.537002 | 113.537 | PASS |
| G2 matches closed form | bracket | \|z\| < 3σ | z = −1.343306 | 1.657 | PASS |
| G3 concentration-driven | one-sided sep. | z ≥ 3σ, unif gap<0.01 | z = 113.523243, gap = 0.000005 | 110.523 | PASS |

## Probe report (v0, 2026-07-18)
**1. Is the shortfall forced or could the count intuition ever be right?** Forced. Cauchy–Schwarz gives HHI = Σwᵢ² ≥ (Σwᵢ)²/N = 1/N with equality only when all sizes are equal, so CV(R) = CV_account·√HHI ≥ CV_account/√N always; the naive figure can never over-state. G1 is a direction check, not a fit.
**2. Does the result just restate the HHI definition with no content?** No — the content is (a) the diversification lever is N_eff = 1/HHI, a small constant for heavy tails, so account count is nearly irrelevant to volatility, and (b) the magnitude is √(N/N_eff), a ~4× multiplier at Zipf-400. G3 isolates that concentration, not count or per-account noise, drives it.
**3. Why batch-means for the SE instead of a normal-theory CV standard error?** CV_hat = s/x̄ is a ratio estimator whose closed-form SE assumes R is normal, but the concentrated book is ~15% one Gamma(shape 4) account, so R is mildly skewed and the normal-theory SE is biased. The batch-means SE (60 independent batches, one CV each) is distribution-free — the between-batch spread captures the real sampling error. This mirrors the P137 method-of-independent-replications discipline.
**4. Are 60×250 batches enough for the ≥3σ gates?** G1 and G3 are enormous separations (z > 100), insensitive to batch counts. G2 is a bracket the estimator clears with the reported |z| = 1.343 at this seed; the batch SE is honest and the seeded value is disclosed.
**5. Could G2 falsely fail on an unlucky seed?** G2 is ~N(0,1) under the null of a correct estimator; the pinned SEED gives the reported |z| < 3. A large |z| would flag an estimator or bias bug (e.g. an uncorrected ratio-estimator bias), which is exactly what the bracket is for.
**6. Does the uniform book share the concentrated stream and confound G3?** Within each batch the concentrated book is drawn first, then the uniform book, as consecutive segments of the one seeded stream; the difference gate treats them as independent (variances add), which only makes the ≥3σ bar harder to clear.
**7. Is this actionable or a curiosity?** Actionable: report N_eff = 1/HHI next to the logo count, size revenue-at-risk off CV_account·√HHI, and flag top-share accounts as concentration risk. It reverses "we're diversified, we have thousands of accounts" on any book with a heavy size tail.
**8. What would REJECT it?** G1 diff ≤ 0 or under 3σ, G2 |z| ≥ 3σ, G3 concentrated ≤ uniform or uniform–naive gap ≥ 0.01, any digest mismatch or non-deterministic double-run.

**Recommendation: sim-ready**
