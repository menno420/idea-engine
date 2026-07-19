# Ordering to a base-stock target is not variance-neutral: an order-up-to policy inflates order variance by 1+2L/p+2L^2/p^2, no matter the demand distribution

> **State:** sim-ready
> **Class:** counterintuitive-invariant / fleet-ops (replenishment + inventory)
> **Slot:** round-37 fleet
> **Target:** sim-lab (VERDICT 170, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine/blob/95d0107afe1b8b8a579679bb3b245a77fe3e2749/control/outbox.md@535e33451074a2d9257ecd60fee695e99edb0c9a · fetched 2026-07-19T05:35:56Z
> **Reference (external, reachable):** J. Forrester, "Industrial Dynamics" (MIT Press, 1961); H. Lee, V. Padmanabhan, S. Whang, "The Bullwhip Effect in Supply Chains," Sloan Management Review 38(3):93-102 (1997); closed form in F. Chen, Z. Drezner, J. Ryan, D. Simchi-Levi, "Quantifying the Bullwhip Effect in a Simple Supply Chain: The Impact of Forecasting, Lead Times, and Information," Management Science 46(3):436-443 (2000). Secondary (reachable): Wikipedia "Bullwhip effect" — https://en.wikipedia.org/wiki/Bullwhip_effect.
> **Harvest source (firsthand):** ideas/fleet/bullwhip_order_variance_amplification.py + its recorded double-run (this branch).

## The phenomenon (one line)
Feed a perfectly steady, i.i.d. stream of demand into a textbook order-up-to policy and the orders it emits are provably noisier than the demand — by a factor 1 + 2L/p + 2L^2/p^2 set entirely by the lead time L and the forecast window p, not by the customers.

## The folk belief
"Just reorder what you used." A replenishment rule that chases observed demand feels variance-neutral — orders should be about as steady as sales, and any wild swing upstream must mean the customers got wild. Both halves are wrong: at fixed i.i.d. demand a rational base-stock policy manufactures excess order variance, and it does so distribution-free — the amplification is a property of the control loop, not the demand.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Single stage, periodic review, i.i.d. demand D_t (mean mu, variance sigma^2). The retailer forecasts one-period demand with a p-period moving average D_hat_t = (1/p) sum_{i=1}^{p} D_{t-i}, and orders up to a base-stock level S_t that covers the lead-time-L demand forecast plus a fixed safety term: S_t = L * D_hat_t + (constant). The order placed each period restores the inventory position:

    Q_t = D_{t-1} + (S_t - S_{t-1}) = D_{t-1} + (L/p) * (D_{t-1} - D_{t-1-p}).

The constant safety term cancels between consecutive targets, leaving an order that is last period's demand PLUS a forecast-correction that levers the one-period demand change by L/p. Because D_{t-1} and D_{t-1-p} are independent (p >= 1 apart) draws of the same i.i.d. law:

    Var(Q) = (1 + L/p)^2 * sigma^2 + (L/p)^2 * sigma^2 = [1 + 2L/p + 2L^2/p^2] * sigma^2.

So the order-to-demand variance ratio is exactly 1 + 2L/p + 2L^2/p^2 (Chen-Drezner-Ryan-Simchi-Levi 2000). It exceeds 1 for every L >= 1, RISES with lead time (a slow supplier forces bigger forecast corrections) and FALLS with the forecast window (more smoothing damps the correction). Nothing on the right-hand side is a demand-distribution shape term — only L, p, and sigma^2 — so the ratio is distribution-free. Up an N-stage chain each stage amplifies the stage below, so the variance ratio compounds roughly multiplicatively: the factory sees a storm the customers never made.

## Pinned world (committed constants — the verifier is the contract)
SEED=20260717 · base: i.i.d. Normal demand (mean 100, sd 20) · lead time L=4 · forecast window p=8 (=> closed-form ratio 1 + 2(0.5) + 2(0.25) = 2.5) · N_PER=40000 order periods per replication · WARMUP=8000 discarded · R_REPS=30 independent replications. Order-up-to recursion Q_t = D_{t-1} + (L/p)(D_{t-1} - D_{t-1-p}); Var(Q)/Var(D) measured post-warmup. Shifted (robustness) world: heavy-tailed exponential demand (same mean 100), lead time L=6, window p=4 (=> closed-form ratio 1 + 2(1.5) + 2(2.25) = 8.5).

## Pre-registered gates (evaluation order G1 → G2 → G3; APPROVE iff ALL hold)
- **G1 — the amplification is real (orders are NOT as stable as demand).** the order-to-demand variance ratio exceeds the null ratio 1 at z >= 3. Observed ratio_mean = **2.499097**, z = **+880.399457** — a 2.5x variance blow-up from a steady demand stream.
- **G2 — it is the policy's closed form.** the relative error |ratio_measured - (1+2L/p+2L^2/p^2)| / (1+2L/p+2L^2/p^2) stays below 0.05 at z >= 3 below the ceiling. Observed relerr_mean = **0.002767** against the closed form 2.5, z = **+104.491569** — measured 2.499097 vs predicted 2.500000.
- **G3 — distribution-free under a shifted mix.** under heavy-tailed exponential demand with L=6, p=4, the same relative error against the closed form 8.5 stays below 0.05 at z >= 3. Observed shift_relerr_mean = **0.005070**, z = **+91.810513** — measured 8.495599 vs predicted 8.500000, a non-Normal demand shape leaving the ratio unchanged.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold on a clean-room re-run (SEED=20260717) with the results-dict sha256 matching. Any gate false → REJECT naming first_failing_gate. Observed all_pass = **true**, first_failing_gate = **null**. Direct readout: a steady demand stream (sd 20 on a mean of 100) emerges as orders with 2.5x its variance under a mild (L=4, p=8) policy and 8.5x under a slower, twitchier (L=6, p=4) one — the customers never changed.

## Disclosed verifier (the sim-lab spec)
`ideas/fleet/bullwhip_order_variance_amplification.py` — stdlib only (hashlib, json, math, random). Draws i.i.d. demand, runs the order-up-to recursion, measures Var(Q)/Var(D) over 30 replications, z-tests the ratio and its relative error against the closed form. Posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY — builds the ordered results dict, asserts an in-process double run is byte-identical, prints the pretty dict and its sha256. Expected results-dict sha256:

    b45986240123fd6f922ce4f4a72d6a2c76ab7d3d8edb2da3b2d76b4efa13a49b

Re-run twice cross-invocation; both must print IDENTICAL output and the sha256 above; exit 0 iff all_pass.

## Why it matters
The order swings a spare-parts supplier or upstream depot sees are, to first order, not a signal about the fleet — they are the fleet's own replenishment control loop talking to itself. Chasing that phantom demand by stockpiling treats a policy artifact as real volatility. The levers that actually cut it are structural: SHORTEN the replenishment lead time L (the dominant term is quadratic in L/p), LENGTHEN or smooth the forecast window p, or share downstream demand data so each stage stops re-forecasting from orders instead of true demand. "Order what you used" is exactly the rule that amplifies; the bullwhip is designed in, and the same three levers un-design it.

## Dedup (contrast vs prior lane heads)
- vs **service-variance-wait-tax / erlang-b-trunking / kleinrock-conservation** — those are queueing-wait results (how service variance or scheduling moves WAIT at a server). This is a supply-chain result on ORDER variance propagating across periods and stages; no server, no wait — a different quantity and a different loop.
- vs **correlated-fleet-variance-floor** — that raises a variance floor via cross-unit correlation at one instant. Bullwhip is temporal: an autoregressive control loop amplifying variance over time and up echelons, even with independent demand.
- vs **inspection-paradox-wait-inflation / regression-to-mean** — sampling/measurement biases on observed values. Bullwhip is a real dynamical amplification of a control signal, not an observation artifact.
- vs **metastable-retry-storm-collapse** — a positive-feedback collapse under overload. Bullwhip is a linear, stable amplification with an exact closed-form gain; no collapse, no threshold.
- Crossover honesty: adjacent to any "demand signal distortion" framing, but no prior fleet head states or tests the 1+2L/p+2L^2/p^2 order-variance ratio. Distinct.

## Model basis (declared model-dependence — the P024 discipline)
Exact given the model: single stage, periodic review, i.i.d. demand with finite variance, order-up-to policy with a p-period moving-average forecast of lead-time demand, and orders permitted to go negative (returns). Dependence disclosed honestly: (1) the exact ratio 1+2L/p+2L^2/p^2 is the i.i.d. case; positively autocorrelated (AR(1), rho>0) demand amplifies MORE — the i.i.d. form is the published lower bound, so the head UNDERSTATES real-world bullwhip; (2) an exponential-smoothing or optimal (Kalman) forecaster changes the constant but not the "ratio > 1, grows in L, falls in p" structure; (3) if orders are censored at zero (no returns) the linear variance identity is an approximation. The SIGN, the strict amplification, and the L/p scaling are structural for order-up-to control; the exact 2.5 / 8.5 constants are the pinned i.i.d. moving-average case, verified.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | z | Verdict |
|------|------|-----------|----------|---|---------|
| G1 | amplification real | ratio > 1, z>=3 | 2.499097 | +880.399457 | PASS |
| G2 | matches closed form | relerr < 0.05, z>=3 | 0.002767 | +104.491569 | PASS |
| G3 | distribution-free | shift relerr < 0.05, z>=3 | 0.005070 | +91.810513 | PASS |

## Probe report (v0, self-adversarial)
**1. Real amplification or one lucky demand stream?** Measured across 30 independent replications, each a fresh seeded i.i.d. stream of 40000 periods; the ratio lands at 2.499 every time (z=880 vs the null 1). Not one stream.
**2. Is the order-up-to recursion the standard one?** Yes — Q_t = D_{t-1} + (S_t - S_{t-1}) with S_t = L * (p-period MA) + constant is the textbook base-stock policy; the constant safety term cancels, leaving the (L/p) forecast-correction lever. No non-standard tuning.
**3. Could the 2.5 be a coincidence of the constants?** No — G2 gates the measured ratio against the independently-computed closed form 1+2L/p+2L^2/p^2 = 2.5 at z=104, and G3 re-derives 8.5 for a different (L,p) and matches it at z=92. The formula predicts, the sim confirms.
**4. Does the amplification need Normal demand?** No — G3 swaps in heavy-tailed exponential demand (same mean, much larger dispersion, skewed) and the ratio still matches the closed form to 0.5% (relerr 0.005070). The gain is a property of the control loop, not the demand shape.
**5. z inflated by huge N?** The z's come from R=30 replications (n=30 per z-test), not from N_PER. G1's z reflects a large, rock-steady ratio; G2/G3's reflect relative errors sitting far below the 0.05 ceiling with tiny spread across reps.
**6. Rigged constants?** Textbook base-stock inputs (mean-100/sd-20 demand, L=4, p=8). The ratio 2.5 is forced by L/p=0.5 through the closed form, not chosen; G3 changes L and p and the demand law and the match holds.
**7. Determinism?** SEED pinned; in-process double run asserted byte-identical; cross-invocation double run printed IDENTICAL with sha256 b45986240123... A verdict re-run must reproduce that digest.
**8. Real phenomenon or toy?** The bullwhip effect is a load-bearing supply-chain result (Forrester 1961; Lee-Padmanabhan-Whang 1997; Chen et al. 2000 closed form) documented from Procter & Gamble diapers to semiconductor fabs; the reflex it corrects — "reorder what you used and orders stay as calm as sales" — is exactly the folk belief above.

**Recommendation: sim-ready**
