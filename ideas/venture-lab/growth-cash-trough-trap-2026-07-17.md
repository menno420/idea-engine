# Two subscription ventures with IDENTICAL, positive per-customer unit economics (LTV > CAC) do NOT have the same cash risk — the one that grows FASTER has a strictly DEEPER cash trough and a higher probability of ruin, because CAC is paid upfront while the margin trickles in over the customer's lifetime. "Our unit economics are positive, so scale acquisition hard" is a ruin trap.

> **State:** sim-ready
> **Class:** venture-lab · startup unit-economics / cash-flow dynamics · growth-financing risk
> **Target:** sim-lab (VERDICT 115, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@61b72c4 · fetched 2026-07-17T23:21:30Z
> **Harvest source (firsthand):** Customer lifetime value — https://en.wikipedia.org/wiki/Customer_lifetime_value (fetched 2026-07-17T23:21:30Z, HTTP 200): "CLV is the present value of future cash flows attributed to the customer during his/her entire relationship with the company" — i.e. the value accrues over the FUTURE relationship, while CAC is spent at acquisition; the timing gap between upfront cost and deferred, discounted cash flow is exactly the cash-trough mechanism modelled and verified firsthand by the disclosed sim below (results-dict sha256 5e6b4ce7…bc4d95).

## The phenomenon (one line)
Hold per-customer economics fixed and positive (LTV > CAC); vary only the acquisition growth rate g. The cumulative-cash low-water mark (the trough) deepens strictly and monotonically with g, and above a critical rate g_crit the firm's per-period cash flow is PERMANENTLY negative despite every customer being profitable — so the faster grower runs out of cash first for the same starting capital.

## The folk belief
"Get the unit economics right — LTV comfortably above CAC — and then pour fuel on the fire: growth is the goal, and since each customer pays back more than it costs to acquire, faster growth is unambiguously better and the growth pays for itself." Founders and boards treat a positive LTV/CAC ratio as a license to scale acquisition as fast as the funnel allows, reading cash burn during hypergrowth as a temporary, self-correcting artifact.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Model a subscription business in discrete monthly periods. In period k the firm acquires n_k ~ Poisson(A0·g^k) new customers (a geometric-growth funnel at rate g). Each new customer costs CAC, paid UPFRONT the period it is acquired. Each active customer pays margin m every period it remains active and then churns at the end of the period with probability c (survival s = 1−c); the number of paying periods is Geometric(c) with mean 1/c, so the lifetime value is LTV = m/c. Per-customer profit LTV − CAC = m/c − CAC is fixed and, by construction, POSITIVE and IDENTICAL across every growth regime.

Active customers accumulate as a survival-weighted sum of past acquisitions. In the fluid (expectation) limit — exact because expectation is linear over the Poisson acquisitions and Bernoulli churn:

  E[active_k] = A0·(g^{k+1} − s^{k+1}) / (g − s).

Cash flow in period k is CF_k = m·active_k − CAC·n_k, and cumulative cash is C_k = Σ_{i≤k} CF_i. The trough is min_k C_k. Two flows race: revenue m·active_k, which reflects the ENTIRE surviving customer base built up so far, versus acquisition spend CAC·n_k, which reflects only THIS period's fresh cohort. Asymptotically both grow like g^k, and cash flow is eventually positive iff m·g/(g−s) > CAC. Solving the boundary gives a closed-form critical growth rate:

  g_crit = CAC·s / (CAC − m).

Below g_crit the base compounds faster than fresh spend and cash recovers (a finite trough, then positive); ABOVE g_crit each period's upfront CAC outruns the margin the base can throw off, so per-period cash flow is permanently negative and the trough deepens without bound over the horizon — even though every individual customer still earns LTV − CAC > 0. Counterintuitive core: the SAME customer that is profitable across its lifetime bankrupts the firm if acquisition is scaled faster than g_crit, because the firm pays the whole acquisition bill now and collects the offsetting margin only later, spread across the customer's future life. Growth is cash-consumptive on a timing mismatch, not a unit-economics defect. "Positive LTV/CAC, so scale hard" is a value trap: the cash-survival constraint binds at a growth rate strictly below "as fast as the funnel allows," and the trough / ruin probability is monotone increasing in g.

## Pinned world (committed constants — sim-lab must reproduce exactly)
- SEED = 20260717 (fixed; deterministic run)
- T = 24 (horizon in monthly periods)
- A0 = 10.0 (period-0 acquisitions; Poisson mean, geometric funnel A0·g^k)
- M = 10.0 (margin per active customer per period)
- c = 0.10 (per-period churn; survival s = 0.90; mean lifetime 1/c = 10 periods)
- CAC = 60.0 (upfront acquisition cost)
- N_REPS = 4000 (Monte-Carlo company trajectories per growth level)
- K0 = 3000.0 (starting capital; used only for the reported ruin probability)
- Growth sweep g ∈ {1.05, 1.08, 1.15, 1.30}; headline regimes g_low = 1.05, g_high = 1.30
- Acquisitions n_k ~ Poisson(A0·g^k); churn ~ Binomial(active, c) at end of period; new customers pay m the period acquired
- Analytic: LTV = m/c = 100.0; per-customer profit (untruncated) = LTV − CAC = 40.0 (> 0, identical across g)
- Derived pins: g_crit = CAC·s/(CAC−m) = 1.080000 (g_low < g_crit < g_high); cohort-0 horizon-truncated per-customer profit π0(T) = m·(1−s^T)/c − CAC = 32.023356 (> 0, identical across g)
- Fluid trough anchors: g_low k*=11, E[C*]=−2713.71; g_high k*=23, E[C*]=−498721.23

## Pre-registered gates (evaluation order R1 → R2 → R3; APPROVE iff ALL hold)
- **R1 — cash-trough trap (headline):** the mean trough at g_high is MORE NEGATIVE than the mean trough at g_low by ≥3σ (two-sample z on min-cash): (trough̄_low − trough̄_high)/SE_diff ≥ 3. Establishes that faster growth strictly deepens the cash trough.
- **R2 — identical positive unit economics (control):** cohort-0 realized per-customer profit matches the horizon-truncated analytic π0(T) within 3σ in BOTH regimes (|z| < 3 each), is > 0 by ≥3σ in BOTH regimes, and does NOT differ between regimes (|z_low−high| < 3). Establishes that the trough gap is a TIMING/scale effect, not a unit-economics difference — both ventures make the same positive profit per customer.
- **R3 — fluid anchor consistency (MATCH):** at each regime's own fluid-trough period k*, the simulated mean cumulative cash reproduces the closed-form E[C_{k*}] within 3σ (both regimes). Confirms the sim implements the expectation model the g_crit closed form rests on.

## Pre-registered decision rule
APPROVE iff R1 ∧ R2 ∧ R3 all hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier. Any gate failing → REJECT (the growth-deepens-the-trough / timing-not-economics claim is falsified for these constants). No post-hoc threshold moves; margins reported in σ.

## Disclosed verifier (the sim-lab spec)
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `growth_cash_trough_trap.py`. Seed once with SEED=20260717. For each g in the sweep: run N_REPS=4000 company trajectories of T=24 periods (per period: Poisson(A0·g^k) acquisitions paying CAC upfront and joining the active base; all active pay margin m; end-of-period Binomial churn at rate c), recording per-trajectory cumulative-cash path, its trough (min), the ruin indicator (trough < −K0), and cohort-0's realized per-customer profit. Compute means and unbiased SEs; evaluate R1/R2/R3 as above; the fluid anchors E[active_k] and E[C_k] are computed in closed form. Emit a canonical (sorted-keys, comma/colon-separated) results dict and its sha256. Expected results-dict sha256 (dry-sim, this pinned world) = 5e6b4ce7cf3a58e6c5fa912ee5365ff4152c162818113320a8c2332195bc4d95. Exit 0 iff all gates pass. Deterministic: two runs are byte-identical.

## Why it matters (venture-ops)
The near-universal indie/startup heuristic is "fix unit economics, then scale as fast as you can." This proposal says the cash-survival constraint is a SEPARATE, binding constraint that positive LTV/CAC does not relieve: with upfront CAC and margin spread over the customer lifetime, the cumulative-cash trough deepens monotonically with the growth rate, and above g_crit = CAC·s/(CAC−m) per-period cash flow is permanently negative even though every customer is profitable. Decision rule for an operator/founder: after confirming LTV > CAC, compute g_crit from your churn s and the CAC/margin ratio, size the acquisition ramp against your ACTUAL cash runway (starting capital vs the fluid trough depth at your planned g), and treat "grow faster" as a decision that spends cash — not one that conserves it. Concretely here (g_high=1.30 vs g_low=1.05, identical π0≈32 per customer): the trough goes from −3.06k to −498.6k — a ~163× deeper cash hole from growth rate alone, ruin probability 0.53 → 1.00 at K0=3000. The lever that feels like acceleration is the lever that empties the bank.

## Dedup
Distinct from the venture and fleet priors:
- **P098 (referral-bonus value trap):** an INTERIOR optimum on the referral BONUS driven by a 1/(1−R0) branching amplifier + saturating conversion. Here there is no interior optimum on a spend lever; the trap is a monotone-deepening cash trough in the GROWTH RATE plus a critical-threshold sign flip (g_crit) driven by upfront-vs-deferred cash timing — a different lever (growth pace, not incentive size) and a different mechanism (cash-flow timing, not a branching cost amplifier).
- **P094 (refund-window interior optimum):** interior optimum on refund policy vs abuse — a policy lever, not a cash-timing/scale effect.
- **P090 / big-pond-badge-inversion:** reward-scarcity signalling; no cash-flow dynamics.
- **kill-clock-horizon / channel-concentration / versioning-depth priors:** exposure windows, distribution mix, pricing-tier depth — none model CAC-upfront vs margin-over-lifetime cash timing.
- **P100 (Kelly overbet ruin, fleet):** shares the word "ruin" but the mechanism is variance-drag / geometric-mean loss from over-betting a fraction in repeated stochastic capital growth. Here ruin is a (near-)deterministic cash-TIMING trough from paying CAC upfront against margin collected later — no bet-fraction, no variance-drag; the ruin is in the accounting sequence, not the volatility.
The novel content is the timing-not-economics decomposition: two firms with provably identical positive per-customer profit have radically different cash-ruin risk purely from growth pace, with a closed-form critical rate g_crit above which profitable customers still bankrupt the firm.

## Model basis (declared model-dependence — the P024 discipline)
The trough-deepens-with-g result and the g_crit threshold DO depend on structural assumptions: (a) CAC is paid upfront while margin accrues over the customer's future life (the timing gap that drives everything); (b) a geometric-growth acquisition funnel (A0·g^k); (c) constant per-period churn (geometric lifetimes) so the survival kernel is s^{k−j}. If revenue were collected upfront (e.g. annual prepay netting most of LTV at acquisition), or CAC were financed/amortized over the lifetime, or churn were front-loaded differently, the trough shrinks or the g_crit boundary moves. The claim is scoped: under the (very common) upfront-CAC + monthly-margin subscription regime, faster growth strictly deepens the cash trough and above g_crit profitable customers still burn cash — demonstrated on the pinned constants, mechanism-explained via the closed-form E[active_k] and g_crit, not asserted as a universal law. No discounting is applied (undiscounted cash); a positive discount rate only worsens the trap by further deferring the offsetting margin.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed (dry-sim) | Margin | Verdict |
|---|---|---|---|---|---|
| R1 trough trap (g_high vs g_low) | separation ≥3σ | ≥3σ | z=6011.93σ | 6008.9σ | PASS |
| R2 π0 anchor match (low / high) | match (\|z\|<3σ) | <3σ | \|z\|=0.66σ / 0.83σ | ≥2.17σ headroom | PASS |
| R2 π0 positivity (low / high) | separation ≥3σ | ≥3σ | z=83.87σ / 83.00σ | ≥80σ | PASS |
| R2 low-vs-high (no diff) | match (\|z\|<3σ) | <3σ | \|z\|=1.05σ | 1.95σ headroom | PASS |
| R3 fluid anchor (low / high) | match (\|z\|<3σ) | <3σ | \|z\|=0.89σ / 1.14σ | ≥1.86σ headroom | PASS |

## Probe report (v0, 2026-07-17)

**1. What is this really?** A startup cash-flow claim: with upfront CAC and margin collected over the customer lifetime, two subscription firms with IDENTICAL positive per-customer profit (LTV=100 > CAC=60) but different acquisition growth rates have very different cash-ruin risk — the faster grower (g=1.30) has a ~163× deeper cash trough (−498.6k vs −3.06k) and higher ruin probability than the slower one (g=1.05), with a closed-form critical rate g_crit=1.08 above which per-period cash flow is permanently negative.
**2. What would make it false?** If the trough did NOT deepen with g (R1 fails), or if the two regimes did not share identical positive per-customer economics (R2 fails — meaning the gap is a unit-economics artifact, not timing), or if the simulated cumulative cash did not reproduce the fluid anchor E[C_{k*}] (R3 fails). Any of R1/R2/R3 failing → REJECT.
**3. Simplest version that still bites?** SEED=20260717, T=24, A0=10, m=10, c=0.10, CAC=60, N=4000; two growth regimes g_low=1.05 and g_high=1.30 straddling g_crit=1.08; Poisson acquisitions, Binomial churn, upfront CAC vs per-period margin.
**4. What is the counterintuitive core?** The same customer that is profitable over its lifetime bankrupts the firm if you acquire faster than g_crit — because the firm pays the entire CAC now and collects the offsetting margin later, spread over the customer's future life. Growth consumes cash on a timing mismatch, independent of (positive) unit economics.
**5. Where could I be fooling myself?** Confounding growth with unit economics — R2 is the explicit control proving cohort-0 per-customer profit is statistically identical and positive across regimes (π0≈32, |z_low−high|=1.05σ), so R1's trough gap can only be timing/scale. The min-of-path trough is biased deeper than the min of the mean path, so R3 anchors on the UNBIASED expectation E[C_{k*}] at the fluid trough period, not on the mean-of-min. Result is model-dependent (upfront CAC, geometric funnel, constant churn).
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: R1 trough trap z=6011.93σ; R2 π0-anchor |z|=0.66σ/0.83σ (match), positivity z=83.87σ/83.00σ, low-vs-high |z|=1.05σ; R3 fluid-anchor |z|=0.89σ (g_low, k*=11) / 1.14σ (g_high, k*=23) — all clear their bars; exit 0; results-dict sha256 5e6b4ce7…bc4d95; two runs byte-identical.
**7. What decision does it change?** After confirming LTV > CAC, compute g_crit = CAC·s/(CAC−m) and size the acquisition ramp against actual cash runway (starting capital vs fluid trough depth at planned g), rather than scaling "as fast as the funnel allows." Treat faster growth as a cash-spending decision, not a cash-conserving one.
**8. How will we know it worked?** The committed stdlib verifier reproduces the deeper-trough-with-growth ordering (R1), the identical-positive-economics control (R2), and the fluid-anchor match (R3) at their thresholds under SEED=20260717, with the results-dict sha256 matching 5e6b4ce7cf3a58e6c5fa912ee5365ff4152c162818113320a8c2332195bc4d95.

**Recommendation: sim-ready**
