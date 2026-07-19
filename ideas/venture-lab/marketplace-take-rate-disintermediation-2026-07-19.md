# For a marketplace, net take-rate revenue is a hump in the rake: raising the take-rate past its interior optimum strictly LOWERS revenue, because it drives sellers off-platform

> **State:** sim-ready
> **Class:** counterintuitive-pricing / venture-lab (marketplace unit-economics slot)
> **Slot:** round-37 VENTURE
> **Target:** sim-lab (VERDICT 171, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine/blob/40d15868a57883f182b6c604765a643f16e5f4d4/control/outbox.md@11871e4b9ed41aa7727aed3bbe04053fb9e98cff · fetched 2026-07-19T05:56:50Z
> **Reference (external):** Bill Gurley, "A Rake Too Far: Optimal Platform Pricing Strategy" (Above the Crowd, 2013) — the canonical statement that high take-rates invite disintermediation and competitive undercut, so the revenue-optimal rake is lower than "charge what the market bears" intuition. (Live URL returns 404 and archive.org is transiently offline at authoring time; the mechanism's core — R = p·Q(p) monopoly pricing on a downward-sloping demand curve — is textbook and distribution-independent.)
> **Harvest source (firsthand):** ideas/venture-lab/marketplace_take_rate_disintermediation.py + its recorded double-run (this branch).

## The phenomenon (one line)
A marketplace's take-rate is not a pure margin multiplier: raising the rake t past an interior optimum t* strictly lowers net platform revenue, because every extra point of rake pushes the sellers whose on-platform switching cost is below t to transact off-platform.

## The folk belief
The take-rate is a direct multiplier on revenue — each point of rake is pure margin skimmed off every transaction — so a platform should charge as much as the market will bear, and a higher commission always means more money.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Give each seller an idiosyncratic switching cost c: the value of staying on-platform (discovery, trust, escrow, payments, dispute resolution). A seller keeps a transaction on-platform iff the rake t it pays is no more than that value, t ≤ c; otherwise the transaction leaks off-platform. So the on-platform GMV fraction is the survival curve of the switching-cost distribution, S(t) = P(c ≥ t), and platform revenue is
    R(t) = t · S(t) · GMV0.
This is exactly the monopoly-pricing identity R = p · Q(p): the rake is a *price*, and S(t) is a downward-sloping *demand curve*. Revenue is therefore a hump, not a line — it climbs while the extra margin per transaction outweighs the leakage, peaks where the rake elasticity of on-platform GMV hits 1 (t·f(t)/S(t) = 1, with f = −S′), and falls thereafter. For switching costs c ~ Uniform[0, C] the demand is linear, S(t) = 1 − t/C, and the revenue-optimal rake is the closed form
    t* = C/2,   R(t*) = C/4.
Pushing past t* is doubly costly: revenue falls, and it falls at an accelerating (convex, quadratic-near-the-peak) rate. The aggressive "charge what you can" rake T_MAX is strictly dominated by the interior optimum.

## Pinned world (committed constants — the verifier is the contract)
SEED=20260717 · N=4000 sellers per trial · TRIALS=300 independent trials → between-trial z-scores · base switching costs c ~ Uniform[0, C_MAX=0.50] (analytic optimum t*=0.25) · aggressive rake T_MAX=0.45 · REL_NULL=0.10 (G2 null). Shifted (lower-loyalty) draw: c ~ Uniform[0, C_MAX_SHIFT=0.35] (analytic optimum t*_shift=0.175). Reseeded per run; redrawn per seller. Revenue is measured empirically (count the sellers with c ≥ t), not plugged from the closed form.

## Pre-registered gates (evaluation order G1 → G2 → G3; APPROVE iff ALL hold)
- **G1 — the optimum dominates the aggressive rake (the hump has the right sign).** mean(R(t*) − R(T_MAX)) > 0 at z ≥ 3. Observed gap_mean = **+0.080126**, z = **+592.387661**, frac_dominant = **1.0**.
- **G2 — overshooting costs a large fraction of revenue, not a rounding error.** mean((R(t*) − R(T_MAX)) / R(t*)) ≥ 0.10 at z ≥ 3 (one-sample z vs null 0.10). Observed rel_mean = **+0.640656** (≈ 64% of extractable revenue destroyed by overshooting), z = **+581.508639**.
- **G3 — robust to a shifted (lower-loyalty) switching-cost distribution.** under c ~ Uniform[0, 0.35], mean(R(t*_shift) − R(T_MAX)) > 0 at z ≥ 3. Observed gap_mean = **+0.087422**, z = **+1142.566654**, frac_dominant = **1.0** — and the optimum moves LOWER (t*_shift=0.175 < t*=0.25) as loyalty falls (disclosed).

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold on a clean-room re-run (SEED=20260717) with the results-dict sha256 matching. Any gate false → REJECT naming first_failing_gate. Observed all_pass = **true**, first_failing_gate = **null**.

## Disclosed verifier (the sim-lab spec)
`ideas/venture-lab/marketplace_take_rate_disintermediation.py` — stdlib only (math, json, hashlib, random, statistics). Posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY. Builds the ordered results dict, asserts an in-process double run is byte-identical, prints the compact canonical JSON (sort_keys) and its sha256. Expected results-dict sha256:
    9b8be9fcc3e51afcff0561e43930aa5a38b32f803708c1602f7cf3d69e3b1f43
Re-run twice cross-invocation; both must print IDENTICAL output and the sha256 above; exit 0 iff all_pass.

## Why it matters
The rake is the single most consequential number a marketplace sets, and the folk model treats it as free margin. It is not: it is a price on a disintermediation demand curve, so there is a revenue-optimal rake and a hard ceiling above it. The lever that actually raises extractable revenue is *lowering the switching cost* — deepening on-platform lock-in (better discovery, trust, escrow, payments) shifts the whole S(t) curve out — not cranking the commission. The headline is stark: at the 25% optimum the platform captures 0.12507 of GMV; at a 45% rake only 0.044944 — a 64% self-inflicted haircut; and under lower loyalty (max switching cost 35%) the 45% rake captures ZERO — total disintermediation — while the 17.5% optimum still captures 0.087422. It is the quantitative statement of why the most durable marketplaces (Gurley's thesis) run *lower* rakes than their pricing power would nominally allow.

## Dedup (contrast vs prior lane heads)
- vs **founder-dilution-waterfall / any cap-table head** — those model equity splits and liquidation preferences at a financing/exit event; this models an operating pricing decision (the commission) on a live transaction flow. No equity, no waterfall.
- vs **growth-endurance-dominance / retention-survivorship / nrr-composition** — those model a SaaS revenue base compounding or decaying over cohorts; this is a static single-period marketplace revenue-vs-price hump, no cohort or time series.
- vs **discount-breakeven-trap / annual-prepay-financing-trap / usage-based-billing** — SaaS list-price and billing-term mechanics for a single vendor; none models a two-sided platform's rake or off-platform leakage.
- vs any **casino house-edge / entry-fee** head in other lanes — those set a fixed edge on a closed game; this is a two-sided platform where the counterparty can EXIT the platform (disintermediate) when the rake is too high. The exit option is the whole mechanism. First marketplace-rake head in any lane.

## Model basis (declared model-dependence — the P024 discipline)
Exact given the model: seller keeps a transaction on-platform iff rake ≤ switching cost; on-platform GMV = GMV0·S(t); revenue = t·S(t). NOT a claim about a specific marketplace's numbers. The claim is that this documented mechanism is real, sign-correct, large, and robust to draw noise. Disclosed dependence: the optimum LOCATION (t*=C/2 for uniform costs) depends on the switching-cost law — a different distribution moves t* — but the SIGN (revenue is a hump; the aggressive rake is dominated) and the order of magnitude survive the shifted draw (G3). The uniform switching-cost law is a declared linear-demand choice, the cleanest closed-form case; heavier-tailed loyalty distributions move t* but preserve the hump.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | z | Verdict |
|------|------|-----------|----------|---|---------|
| G1 | sign | mean gap > 0, z≥3 | +0.080126 | +592.387661 | PASS |
| G2 | effect size | mean rel ≥ 0.10, z≥3 | +0.640656 | +581.508639 | PASS |
| G3 | robustness | shifted mean gap > 0, z≥3 | +0.087422 | +1142.566654 | PASS |

## Probe report (v0, self-adversarial)
**1. Real hump or a rigged pair of rakes?** The optimum t*=C/2 is the analytic argmax of t·(1−t/C) — the closed-form maximizer of the modelled revenue, not a cherry-picked point; T_MAX=0.45 is a plausible "aggressive" rake below C=0.50. Revenue is measured by actually counting on-platform sellers, not by plugging the formula.
**2. Knife-edge at the nominal draw?** No — frac_dominant = 1.0 across all 300 trials × 4000 sellers in both the base and shifted worlds; the optimum beats the aggressive rake in every trial. A robust regime, not a point.
**3. Where does it break?** The optimum LOCATION is model-dependent (t*=C/2 for uniform costs); a different switching-cost distribution moves t*. Disclosed. The SIGN and magnitude do not break under the shifted draw (G3). If switching costs were unbounded above the rake (perfect lock-in, S(t)≡1) there would be no leakage and no hump — but that is the empirically false limit the phenomenon exists to correct.
**4. z inflated by huge N?** The z is large because the effect (a 64% revenue gap) is large relative to between-trial variance, not merely because N=4000. G2's z is against a *non-zero* null (0.10) to test magnitude, not just sign; the relative loss is ≈+64%, far past the 10% floor.
**5. Determinism?** SEED=20260717 pinned; in-process double run asserted byte-identical; cross-invocation double run printed IDENTICAL with sha256 9b8be9f…1f43. A verdict re-run must reproduce that digest.
**6. Are the constants tuned to force a pass?** C_MAX=0.50 (max switching cost = half the transaction value) and T_MAX=0.45 are round, plausible values; the optimum t*=0.25 (a 25% rake) sits squarely in the real-world marketplace range (~15–30%). The shifted world (C_MAX_SHIFT=0.35) tests a distinctly less loyal market. No constant is tuned to the pass margin.
**7. Float ordering perturbing the digest?** All dict floats round()-ed to 6 dp before hashing; trial means in fixed order; compact JSON with sort_keys; no set/dict-ordering nondeterminism. The in-process assert catches drift.
**8. Real or toy?** The marketplace-rake ceiling is a documented field phenomenon — Gurley's "A Rake Too Far" is its canonical statement, and disintermediation (going around the platform to dodge the fee) is a first-order concern for every real marketplace. The mechanism names why the rake has a revenue-optimal interior point.

**Recommendation: sim-ready**
