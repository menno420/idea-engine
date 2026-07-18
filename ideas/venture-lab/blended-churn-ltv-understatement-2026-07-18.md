# Collapsing a heterogeneous customer book to ONE blended churn rate and computing LTV = m/churn UNDERSTATES the portfolio's true average LTV by ~30% — the gap is driven by churn DISPERSION, not its level (Jensen on the convex 1/c)

> **State:** sim-ready
> **Class:** venture-lab · unit-economics · blended-churn LTV bias
> **Target:** sim-lab (VERDICT 147, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@d3e2bb18bfedba1bd6c0431c30ba33131caaf952 · fetched 2026-07-18T12:52:35Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Jensen%27s_inequality (convexity ⇒ E[f(X)] ≥ f(E[X]); verified reachable 2026-07-18 via WebFetch) + https://en.wikipedia.org/wiki/Customer_lifetime_value (LTV ≈ margin / churn; verified reachable 2026-07-18 via WebFetch)
> **Harvest source (firsthand):** SaaS unit-economics practice — the standard "LTV = ARPU / churn" one-liner applied to a single blended churn number across a heterogeneous book.

## The phenomenon (one line)
A book of customers with heterogeneous churn, summarized by ONE blended churn rate c̄ and turned into LTV = m/c̄, reports a portfolio LTV strictly BELOW the true average of per-customer LTVs — and the shortfall widens with churn dispersion even when mean churn is unchanged.

## The folk belief
"LTV = margin ÷ churn. Use the blended churn rate across the book and you get the average customer's LTV; heterogeneity averages out." The blended number is treated as an unbiased summary, so teams set CAC ceilings, gate GTM spend, and prune 'low-LTV' segments off it.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Expected customer lifetime is geometric: a customer who survives each period with retention r = 1−c lives 1/(1−r) = 1/c periods in expectation, so LTV = m/c. The map c ↦ m/c is strictly CONVEX on c>0. Jensen's inequality then forces, for churn drawn across the book, E[m/c] ≥ m/E[c] = m/c̄, with equality only if churn is identical for everyone. The left side is the true average per-customer LTV; the right side is the blended-churn LTV. So the blended figure is a systematic UNDER-estimate, never an over-estimate. A second-order (delta-method) expansion pins the size: gap ≈ m·Var(c)/c̄³ — it scales with the VARIANCE of churn and is independent of shifts that leave the mean fixed. Hold c̄ constant and widen the spread and the gap grows; the low-churn tail (long-lived accounts) has LTV that blows up like 1/c and drags the true mean far above the blended point estimate. Concretely, with churn uniform on 5%–35% (retention 65%–95%, mean churn 20%) the true mean LTV is ln(7)/0.30 = 6.486367 lifetimes versus the blended 1/0.20 = 5.000000 — a 29.7% understatement — while a same-mean book with churn tightly on 19%–21% shows a gap of 0.004173, essentially nil. The trap runs opposite to intuition: diligence braces for LTV being OVER-stated (survivorship, optimistic cohorts) and discounts it — then prices off a number that already understates the heterogeneous truth, pruning segments and starving GTM against LTV it actually has.

## Pinned world (committed constants — sim-lab must reproduce exactly)
- SEED = 20260717 — fleet-pinned; one `random.seed(SEED)`, single stream.
- TRIALS = 200000 — draws per band.
- m (margin) = 1.0 — per-period gross margin, normalized; LTV scales linearly in m.
- WIDE band: churn c ~ Uniform[0.05, 0.35] — retention 65%–95%, mean churn 0.20.
- NARROW band: churn c ~ Uniform[0.19, 0.21] — SAME mean churn 0.20, tiny spread (isolates dispersion for G3).
- SIGMA = 3.0 — all gates.
- Closed-form anchors (c ~ U[a,b] ⇒ E[m/c] = m(ln b − ln a)/(b−a), blended = 2m/(a+b)):
  - WIDE: true = ln(7)/0.30 = 6.486367, blended = 5.000000, gap = 1.486367 (29.7%); delta-method gap = 2(0.30)²/[3(0.40)³] = 0.937500 (under-predicts — higher-order terms matter at this spread).
  - NARROW: true = (ln0.21 − ln0.19)/0.02 = 5.004173, blended = 5.000000, gap = 0.004173.

## Pre-registered gates (evaluation order G1 → G2 → G3; APPROVE iff ALL hold)
- **G1 — understatement bias exists.** The simulated WIDE-band gap (per-customer LTV − blended LTV) is strictly POSITIVE at ≥ 3σ. Confirms the blended number under-estimates, with the sign Jensen predicts. Observed z = 171.221384.
- **G2 — sim reproduces the EXACT closed form.** The simulated WIDE mean LTV equals the analytic E[m/c] = (ln b − ln a)/(b−a) = 6.486367 within noise: |z| < 3σ (no-significant-deviation bracket). Anchors the estimator to closed form. Observed z = 0.363449.
- **G3 — the gap is DISPERSION-driven, not a level offset.** With mean churn held at 0.20, the WIDE-band gap exceeds the NARROW-band gap at ≥ 3σ, and the narrow-band gap is negligible (< 0.05). Isolates variance as the driver. Observed z = 170.572090, narrow gap = 0.004628.

## Pre-registered decision rule
APPROVE (sim-ready → APPROVE) iff G1 ∧ G2 ∧ G3 all hold on the byte-identical committed verifier at SEED 20260717, the results-dict sha256 matches EXACT, and the double-run is deterministic (exit 0 both times). Any gate miss, digest mismatch, or non-determinism → REJECT.

## Disclosed verifier (the sim-lab spec)
Committed at `ideas/venture-lab/blended_churn_ltv_understatement.py`, stdlib only (`random, math, json, hashlib`). Digest posture: **WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY** — the results dict carries NO `results_sha256` field; the sha256 is taken over the COMPACT canonical serialization (`json.dumps(results, sort_keys=True, separators=(",",":"))`), while stdout prints the PRETTY `indent=2` form (the TWIST — pretty stdout ≠ hashed preimage). No on-disk JSON is written. Determinism: one `random.seed(SEED)`, single stream, WIDE band drawn before NARROW, no wall-clock.
Expected results-dict sha256 (dry-sim, this pinned world) = `f45e6609e866d7ee0cf536a302cba40a9d82dbee8926280fbeadb43f763f489b`.

## Why it matters (venture-ops)
CAC ceilings, payback gates, and segment-pruning decisions run off a single blended churn/LTV number. This result says that number is biased LOW in exactly the direction that makes healthy heterogeneous books look marginal: the long-lived, low-churn tail is where value concentrates, and collapsing to the mean churn erases it. A board deck reporting LTV = m/c̄ understates a dispersed book — the fix is to compute LTV per cohort and average (E[m/c]), or to carry the dispersion term m·Var(c)/c̄³. It also flips the usual worry: diligence braces for LTV inflation, but the blended-churn construction is conservative to a fault, and teams that "haircut" it further compound the error.

## Dedup
Distinct from the venture-lab book: P098 referral trap (network multiplier), P102 cash-trough (timing), P106 retention mirage (survivorship in a MEASURED retention curve — this is a bias in the LTV FORMULA from churn dispersion, not a measurement artifact), P110 discount-depth, P114 freemium inversion, P118 sales-ramp drag, P122 NRR mirage (revenue composition), P126 double marginalization (pricing chain), P130 annual-prepay trap (financing/timing). The mechanism here is Jensen convexity of 1/c over the churn distribution — a formula-level aggregation bias, not covered elsewhere. Convexity/aggregation also appears in fleet-lab (fan-out tail, birthday-collision) but on latency/collision, not unit economics.

## Model basis (declared model-dependence — the P024 discipline)
- Expected lifetime = 1/c assumes memoryless geometric survival (constant per-period churn per customer). Real churn is often duration-dependent; the convexity direction (understatement) survives any convex lifetime-vs-churn map, but the exact 30% is specific to the uniform band + geometric lifetime.
- Churn modeled Uniform[a,b] across the book. The SIGN and dispersion-scaling are distribution-free (Jensen + delta method); the exact closed forms use the uniform. A heavier low-churn tail widens the gap.
- Margin m constant and independent of churn. If low-churn customers also carry higher margin (common), the true understatement is LARGER — the result is conservative.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed (dry-sim) | Margin | Verdict |
|------|------|-----------|--------------------|--------|---------|
| G1 understatement bias | one-sided sep. | z ≥ 3σ, gap>0 | z = 171.221384 | 168.221 | PASS |
| G2 matches closed form | bracket | \|z\| < 3σ | z = 0.363449 | 2.637 | PASS |
| G3 dispersion-driven | one-sided sep. | z ≥ 3σ, narrow<0.05 | z = 170.572090, narrow = 0.004628 | 167.572 | PASS |

## Probe report (v0, 2026-07-18)
**1. Is the sign forced or could the blended number over-state?** Forced. 1/c is strictly convex on c>0, so Jensen gives E[m/c] ≥ m/E[c] with equality only at zero dispersion — the blended figure can never over-state. G1 is a direction check, not a fit.
**2. Does the result just restate Jensen with no content?** No — the content is (a) the SIGN is the opposite of what diligence braces for, and (b) the magnitude scales with Var(c)/c̄³, so a same-mean book can go from ~0 gap to ~30% gap purely by spreading churn. G3 isolates that.
**3. Why does the delta-method gap (0.937500) miss the true gap (1.486367)?** The band is wide relative to the mean (spread 0.30 vs mean 0.20), so third+ order terms are non-trivial; the delta term is a lower bound on the effect, and the sim/exact closed form (G2) is the authority, not the delta approximation. Documented, not hidden.
**4. Is TRIALS large enough for the ≥3σ gates?** G1 and G3 are enormous separations (z in the hundreds), insensitive to TRIALS. G2 is a bracket a well-behaved bounded RV (LTV∈[2.857,20]) clears at 200k with CLT to spare; z is TRIALS-invariant in distribution and the seeded value is reported.
**5. Could G2 falsely fail on an unlucky seed?** G2 is ~N(0,1); the pinned SEED gives the reported z (|z|<3). It is the honest agreement test — a large |z| would signal an estimator bug, which is the point.
**6. Does NARROW share the WIDE stream and confound G3?** They are drawn as separate consecutive segments of the one seeded stream (WIDE first, then NARROW); the difference gate treats them as independent (variance added), which only makes the ≥3σ bar harder.
**7. Is this actionable or just a curiosity?** Actionable: the fix is one line — average per-cohort LTV (E[m/c]) or add the m·Var(c)/c̄³ correction — and it reverses "prune this marginal segment" calls on dispersed books.
**8. What would REJECT it?** G1 gap ≤ 0 or under 3σ, G2 |z| ≥ 3σ, G3 wide≤narrow or narrow ≥ 0.05, any digest mismatch or non-deterministic double-run.

**Recommendation: sim-ready**
