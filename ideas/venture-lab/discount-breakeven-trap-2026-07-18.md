# A price cut of depth d on a product with gross margin m requires a unit-volume UPLIFT of exactly d/(m−d) just to hold gross profit — a CONVEX function that explodes as d→m and is impossible for any d≥m — so a "reasonable" 20%-off promotion at a 40% margin needs +100% units, realizes only ~+10% on inelastic demand, and DESTROYS ~45% of gross profit even though unit sales rise. Reading higher promo volume as success is a margin-dilution mirage.

> **State:** sim-ready
> **Class:** venture-lab · retail/DTC promotional-pricing unit economics · discount breakeven / margin dilution
> **Target:** sim-lab (VERDICT 123, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@d445094 · fetched 2026-07-18T02:05:28Z
> **Harvest source (firsthand):** the promotional-pricing idea space read against the venture-lab tree @d445094 — the venture priors model referral branching (P098), cash-flow timing (P102), retention-cohort survivorship (P106), and pricing/exposure windows (kill-clock, impulse-price, bundle-pwyw, sample-window), but NONE model the elementary retail-margin fact that the breakeven volume uplift for a discount is the convex d/(m−d), so a shallow-looking discount on an inelastic curve destroys gross profit. The mechanism is the standard discount-breakeven identity (retail gross-margin math; constant-elasticity / exponential-WTP demand), grounded firsthand by the disclosed sim below (results-dict sha256 fd870ec6…ce927ee0), no external repo fetched.

## The phenomenon (one line)
Cut the price by a fraction d on a product whose gross margin is m. To hold gross profit constant you need unit sales to rise by exactly u*(d) = d/(m−d). This required uplift is CONVEX in d and blows up as d approaches m; for any d ≥ m no finite volume breaks even (you would sell at or below cost). Because the required uplift is far larger than a realistic demand response on an inelastic curve, a promotion that visibly increases unit sales can still shrink gross profit — and the shallower the margin, the more brutal the trade.

## The folk belief
"Our promo worked — units were up double digits during the sale." Operators judge a discount by whether volume rose and by top-line revenue, and treat a bump in units as proof the promotion paid off. They rarely compute the breakeven uplift d/(m−d) for their actual margin, so they discount into negative gross-profit territory while congratulating themselves on the volume, then repeat the promotion because "it moved units."

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Full price P0, unit cost C, gross margin m = (P0 − C)/P0. A discount of depth d sets the promo price to P0(1 − d), so the promo UNIT margin is P0(1 − d) − C = P0(m − d): every point of discount comes straight off the unit margin, one-for-one, because cost is fixed. Let Q0 be units at full price and Q_d units at the discounted price. Gross profit is GP = units × unit-margin:

  GP(0) = Q0 · P0·m,   GP(d) = Q_d · P0·(m − d).

Break-even (GP(d) = GP(0)) requires Q_d/Q0 = m/(m − d), i.e. a volume UPLIFT of

  u*(d) = Q_d/Q0 − 1 = m/(m − d) − 1 = d/(m − d).

This is the whole result: the breakeven uplift is d/(m − d), CONVEX and increasing, with a vertical asymptote at d = m. At m = 0.40 it reads 0.10→+33%, 0.20→+100%, 0.30→+300%, and d ≥ 0.40 → impossible. Now put demand on it. Under exponential willingness-to-pay (WTP ~ Exp(λ), so the fraction buying at price P is D(P) = e^{−λP}, a constant-elasticity-at-a-point curve with point elasticity λP), the REALIZED uplift from P0 to P0(1 − d) is

  Q_d/Q0 = e^{−λP0(1−d)} / e^{−λP0} = e^{λ·P0·d},

so the realized uplift is e^{λP0d} − 1, and the exact gross-profit ratio is

  GP(d)/GP(0) = e^{λ·P0·d} · (m − d)/m.

The discount is profit-neutral only when the realized uplift factor e^{λP0d} equals the breakeven factor m/(m − d); below the breakeven elasticity λ* = ln(m/(m−d))/(P0·d) the SAME discount destroys profit, above it the same discount helps. Counterintuitive core: whether a promotion pays is NOT "did units go up" — units almost always go up — it is whether the realized uplift clears the convex breakeven d/(m−d), which for typical retail margins is a demand response most products cannot deliver. On the pinned inelastic world (λ=0.5 ⇒ elasticity 0.5 at P0, m=0.40, d=0.20) the breakeven needs +100% units, demand delivers only +10.5%, and gross profit collapses to e^{0.1}·0.5 = 0.5526 of its full-price level — a ~45% destruction of gross profit from a promotion that raised unit sales.

## Pinned world (committed constants — sim-lab must reproduce exactly)
- SEED = 20260717 (fixed; deterministic run)
- N = 200000 (buyers drawn per trial; nested WTP population)
- TRIALS = 400 (Monte-Carlo trials)
- SIGMA = 3.0 (gate strength)
- P0 = 1.0 (full/list price, normalized)
- MARGIN = m = 0.40 (gross margin at full price ⇒ unit cost C = P0(1−m) = 0.60)
- DISCOUNT = d = 0.20 (promo depth ⇒ discounted price P0(1−d) = 0.80, promo unit margin P0(m−d) = 0.20)
- LAMBDA_LO = 0.5 (inelastic demand: WTP ~ Exp(rate 0.5); point elasticity λ·P0 = 0.5)
- LAMBDA_HI = 5.0 (elastic control demand: point elasticity 5.0)
- EROSION_MIN = 0.10 (honest floor the inelastic discount's gross-profit erosion must clear)
- Nested-buyer sampling: n_disc ~ Binomial(N, e^{−λP_disc}); n_full ~ Binomial(n_disc, e^{−λP0d}) (everyone who buys at the lower price is a superset of full-price buyers — exact conditional, count level)
- Derived closed-form anchors: breakeven uplift u*(0.20) = 0.20/(0.40−0.20) = 1.000000; realized uplift (inelastic) e^{0.5·1·0.2}−1 = 0.105171; GP ratio (inelastic) e^{0.1}·(0.20/0.40) = 0.552585; GP ratio (elastic control) e^{5·0.2}·(0.20/0.40) = 1.359141; breakeven table u*(0.10)=0.333333, u*(0.20)=1.000000, u*(0.30)=3.000000

## Pre-registered gates (evaluation order G1 → G2 → G3; APPROVE iff ALL hold)
- **G1 — margin-dilution erosion (headline):** the mean gross-profit erosion 1 − GP(d)/GP(0) on the pinned INELASTIC demand is ≥ EROSION_MIN = 0.10 by ≥3σ, with z computed on the ESTIMATED MEAN via its standard error se = std/√TRIALS (the P104/P105/P106 /se convention). Establishes that a discount which raises unit sales still destroys a large fraction of gross profit.
- **G2 — elasticity-necessity control:** the SAME discount d at the SAME margin m on the ELASTIC control demand (λ_HI) has mean GP ratio > 1 by ≥3σ — the same promotion RAISES gross profit. Establishes that the erosion in G1 is driven by the margin/elasticity breakeven (insufficient realized uplift relative to d/(m−d)), NOT by discounting being universally bad or by a sim artifact: flip the elasticity across the breakeven and the sign of the effect flips.
- **G3 — closed-form anchor MATCH:** the mean simulated GP ratio reproduces the exact closed form e^{λP0d}·(m−d)/m for BOTH the inelastic and elastic curves, and the realized inelastic volume uplift reproduces e^{λP0d}−1, each within 3σ (|z| < 3). Confirms the sim implements the demand + breakeven model the mirage rests on.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier. Any gate failing → REJECT (the convex-breakeven claim, or its elasticity-necessity control, or its closed-form decomposition is falsified for these constants). No post-hoc threshold moves; margins reported in σ.

## Disclosed verifier (the sim-lab spec)
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `discount_breakeven_trap.py`. Seed once with SEED=20260717. For each of TRIALS=400 trials and each demand curve: draw the nested buyer counts n_disc ~ Binomial(N, e^{−λP_disc}) and n_full ~ Binomial(n_disc, e^{−λP0d}) at the count level; compute the per-trial gross-profit ratio GP(d)/GP(0) = [n_disc·(m−d)]/[n_full·m] and (inelastic) the realized uplift n_disc/n_full − 1. Aggregate per-trial statistics with unbiased sample SEs (se = std/√TRIALS); evaluate G1 (inelastic erosion), G2 (elastic-control GP ratio > 1), G3 (closed-form anchor match) as above; the closed forms are computed directly from the pinned constants. Emit a canonical (sorted-keys, comma/colon-separated) results dict and its sha256. Expected results-dict sha256 (dry-sim, this pinned world) = fd870ec6310b687a0a7ad966773404db56401b882116239c9803b405ce927ee0. Exit 0 iff all gates pass. Deterministic: two runs are byte-identical.

## Why it matters (venture-ops)
Discounting is the most-reached-for growth lever in retail/DTC, and it is routinely judged by unit volume and top-line revenue — the two metrics a discount almost always improves while gross profit falls. This proposal gives the operator a hard pre-commit rule: before running a promotion of depth d on a product with margin m, compute the breakeven uplift d/(m−d) and ask whether the product's measured price elasticity can plausibly deliver it. Concretely here (m=0.40): a 20% discount needs +100% units to break even, a 30% discount needs +300%, and a discount at or beyond the 40% margin can never break even at any volume. Decision rule: (1) size promotions against the convex breakeven d/(m−d) for the actual margin, not against "did units go up"; (2) reserve deep discounts for genuinely elastic SKUs (measured λP0 above the breakeven elasticity ln(m/(m−d))/(P0·d)) — for the pinned world that threshold is λ*≈3.47, so an elasticity of 0.5 destroys profit while an elasticity of 5 makes the same discount pay; (3) on thin-margin catalog items, prefer levers that do not come one-for-one off the unit margin (bundling, attach, retention) over headline depth. The trap is that the breakeven is convex and margin-coupled, so the "small" discount on the low-margin item is exactly the one that bleeds the most.

## Dedup
Distinct from the venture and fleet priors:
- **P102 (growth cash-trough trap):** cash-flow TIMING — upfront CAC vs margin accrued over a lifetime makes the faster grower's cash trough deeper. Here there is no time, no growth rate, no CAC; the object is a single-period gross-profit ratio under a price cut, and the counterintuitive core is a convex breakeven threshold on discount depth against margin.
- **P098 (referral-bonus value trap):** an interior optimum on a spend lever driven by a branching amplifier. Here there is no branching and no interior optimum — the claim is a monotone, convex breakeven requirement (deeper d ⇒ strictly harder), and the effect is a sign flip across an elasticity threshold, not a hump.
- **P106 (retention-survivorship mirage):** composition drift of an OBSERVED RATE under attrition (a survivorship artifact over heterogeneous constant-hazard segments). Here there is no cohort, no attrition, no survivor mixing; the mechanism is deterministic gross-margin algebra plus a demand response, and the mirage is "units rose so the promo worked," not "the retention curve rose so we got stickier."
- **impulse-price-blanket / bundle-pwyw-floor / kill-clock / sample-window priors:** pricing/exposure-window and bundle-floor mechanisms — none model the discount breakeven uplift d/(m−d) or the elasticity threshold at which a promotion flips from profit-destroying to profit-making.
The novel content is the convex discount-breakeven decomposition: the volume uplift needed to hold gross profit is exactly d/(m−d) (explosive as d→m, impossible for d≥m), and under an explicit demand curve the promotion's profitability is governed by whether the realized uplift e^{λP0d}−1 clears that breakeven — with an elastic-demand necessity control proving the erosion is the margin/elasticity breakeven, not discounting per se.

## Model basis (declared model-dependence — the P024 discipline)
The breakeven identity u*(d)=d/(m−d) is exact and model-FREE: it follows from fixed unit cost and gross profit = units × unit-margin, for ANY demand curve. What is model-dependent is the REALIZED uplift (hence whether the breakeven is cleared): the pinned world uses exponential WTP D(P)=e^{−λP} (constant point-elasticity λP), which gives the clean realized uplift factor e^{λP0d}. A different demand family (linear, logit, kinked, reference-dependent) changes the realized uplift and thus the profitability verdict for a given (d, m), but not the breakeven requirement itself. Assumptions: (a) unit cost is fixed across the promo (no marginal-cost economies from volume); (b) no cross-period effects — no stockpiling, reference-price erosion, or demand pull-forward (those make discounting worse, not better, so the claim is conservative); (c) the discount applies to the whole demand curve, not a segmented coupon. The claim is scoped: under fixed cost and a stable within-period demand curve — the standard retail-margin description of a promotion — the breakeven uplift is the convex d/(m−d) and an inelastic curve fails to clear it, demonstrated on the pinned constants and mechanism-explained via the gross-profit identity, not asserted as a universal law. The direction (convex, explosive near d=m, impossible for d≥m) holds for ANY margin; the pinned elasticities are illustrative and bracket the breakeven.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed (dry-sim) | Margin | Verdict |
|---|---|---|---|---|---|
| G1 margin-dilution erosion (headline) | separation ≥3σ | ≥3σ | z=13287.66σ | ≫3σ | PASS |
| G2 elasticity-necessity control (elastic GP>1) | separation ≥3σ | ≥3σ | z=250.42σ | ≫3σ | PASS |
| G3 anchor GP ratio (inelastic) vs closed form | match (\|z\|<3σ) | <3σ | \|z\|=1.17σ | 1.83σ headroom | PASS |
| G3 anchor GP ratio (elastic) vs closed form | match (\|z\|<3σ) | <3σ | \|z\|=2.08σ | 0.92σ headroom | PASS |
| G3 anchor realized uplift (inelastic) vs closed form | match (\|z\|<3σ) | <3σ | \|z\|=1.17σ | 1.83σ headroom | PASS |

## Probe report (v0, 2026-07-18)

**1. What is this really?** A promotional-pricing claim: a discount of depth d on a product with gross margin m needs a unit-volume uplift of exactly d/(m−d) just to hold gross profit — convex, explosive as d→m, impossible for d≥m — so on the pinned inelastic world (m=0.40, d=0.20, elasticity 0.5) the promotion needs +100% units, gets +10.5%, and destroys ~45% of gross profit even though unit sales rose.
**2. What would make it false?** If the inelastic discount did NOT erode gross profit by ≥10% (G1 fails), or if the SAME discount on elastic demand did NOT raise gross profit (G2 fails — meaning the erosion is not a margin/elasticity breakeven effect), or if the simulated GP ratios / realized uplift did not reproduce the closed forms e^{λP0d}(m−d)/m and e^{λP0d}−1 (G3 fails). Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED=20260717, N=200000; one product P0=1, cost 0.60 (m=0.40), discount 0.20; exponential WTP at λ=0.5; read GP(d)/GP(0). The ~45% gross-profit destruction appears with a single SKU and a single discount.
**4. What is the counterintuitive core?** "Units went up" is not success. The breakeven uplift d/(m−d) is convex and margin-coupled, so a shallow-looking 20% discount at a 40% margin secretly demands a doubling of units; realized demand falls far short and gross profit collapses. Profitability flips sign only when elasticity crosses ln(m/(m−d))/(P0·d) ≈ 3.47 — below it, deeper discounts destroy more.
**5. Where could I be fooling myself?** Confusing "discounting is bad" with "this discount is bad" — G2 is the explicit control: the SAME d and m on elastic demand (λ=5) RAISES gross profit (ratio 1.36), so the erosion is the breakeven, not discounting per se. The nested-buyer sampling (n_full drawn within n_disc) keeps the realized uplift correctly ≥0 and coupled. The breakeven identity is model-free; only the realized-uplift magnitude is demand-model-dependent (declared).
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 erosion mean 0.447445 ≥ 0.10, z=13287.66σ; G2 elastic GP ratio 1.362147 > 1, z=250.42σ; G3 |z|=1.17 (inelastic ratio) / 2.08 (elastic ratio) / 1.17 (uplift), all < 3σ (match) — all clear their bars; exit 0; results-dict sha256 fd870ec6…ce927ee0; two runs byte-identical.
**7. What decision does it change?** Before running a promo of depth d on margin m, compute the breakeven uplift d/(m−d) and check the product's measured elasticity can deliver it; reserve deep discounts for genuinely elastic SKUs; on thin-margin items prefer levers that don't come one-for-one off the unit margin. Treat "units rose" as the null expectation of any discount, not as evidence the promotion paid.
**8. How will we know it worked?** The committed stdlib verifier reproduces the inelastic gross-profit erosion (G1), the elastic-control profitability flip (G2), and the closed-form GP-ratio + uplift anchors (G3) at their thresholds under SEED=20260717, with the results-dict sha256 matching fd870ec6310b687a0a7ad966773404db56401b882116239c9803b405ce927ee0.

**Recommendation: sim-ready**
