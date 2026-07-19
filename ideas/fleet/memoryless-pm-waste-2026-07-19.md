# PROPOSAL 165 — preventive maintenance of a memoryless component is pure waste: age replacement holds the unplanned-failure rate at exactly λ while raising cost rate (round-39 FLEET slot, P165 -> V178, +13) — Barlow–Proschan (1965); reliability-centered maintenance

> **State:** sim-ready
> **Class:** fleet · reliability / maintenance policy · age-replacement renewal-reward under constant vs increasing hazard
> **Slot:** round-39 FLEET
> **Anchor:** for a constant-hazard unit, replacing at any finite age holds unplanned failures at exactly λ and only adds planned-swap cost; the age-replacement payoff is a function of hazard shape, not intuition.
> **Target:** sim-lab (VERDICT 178, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Reliability-centered_maintenance@1318353310 · fetched 2026-07-19T10:08:16Z
> **Reference (external, reachable):** Memorylessness (https://en.wikipedia.org/wiki/Memorylessness rev 1349523249) — a survived exponential unit is as-good-as-new; Barlow & Proschan, Mathematical Theory of Reliability (1965) — age-replacement cost has an interior optimum iff the lifetime is strictly IFR.
> **Verifier (firsthand):** `ideas/fleet/memoryless_pm_waste.py` · results-dict sha256 `0a9c4406e8abc9a6fa51b80a0101c6f55277f3304c3d8b468b13f4600424bd69`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
Age-based preventive replacement of a memoryless (exponential) fleet component does not reduce the unplanned-failure rate at all — it stays at exactly λ — while strictly raising the long-run cost rate; the payoff of age replacement is real only for wear-out (increasing-hazard) units.

## The folk belief
"Preventive maintenance always reduces failures: swap the part before it breaks and you'll see fewer unplanned outages." Applied blindly to random-failure (constant-hazard) items, this is false and expensive.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Model a component's lifetime L. Under an age-replacement policy with threshold T, each renewal cycle ends at min(L, T): if L ≤ T the unit failed (unplanned, cost c_fail); if L > T it was replaced on schedule (planned, cost c_plan < c_fail). Long-run rates follow renewal-reward: failure rate = P(L ≤ T)/E[cycle], cost rate = E[cost]/E[cycle].

For an exponential lifetime, R(t)=e^(-λt), so E[cycle]=(1-e^(-λT))/λ and P(L≤T)=1-e^(-λT). The failure rate is therefore (1-e^(-λT))/[(1-e^(-λT))/λ] = λ — identically, for every finite T. The memoryless property is the reason: a unit that has survived to age t has the same residual-life distribution as a fresh one, so replacing it early swaps like for like and cannot lower the failure rate. Meanwhile the cost rate is strictly decreasing in T (its derivative in e^(-λT) equals λ·c_plan/(1-e^(-λT))^2 > 0, and e^(-λT) falls as T grows), so it is minimised at T → ∞ (run-to-failure) and every finite T strictly overpays. The naive "PM cuts failures" belief mistakes a wear-out reflex for a law; it holds only when the hazard rises with age.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Baseline lifetime: Exp(λ), λ = 1.0 (mean life 1.0).
- Age-replacement threshold: T = 0.5. Costs c_plan = 1.0, c_fail = 5.0.
- Run-to-failure = the T → ∞ policy (renew only on failure).
- Strawman benefit (folk-expectation gate): DELTA_NULL = 0.10 → a promised failure-rate reduction of 0.10·λ.
- Shifted (robustness) world: λ' = 1.7, T' = 0.3, c_plan' = 1.0, c_fail' = 8.0.
- Wear-out contrast (non-gated): Weibull(shape 2.5), mean matched to the exponential.
- SEED = 20260717, TRIALS = 30 replicates × N_CYCLES = 100000 cycles, z_gate = 3.0.

## Pinned world (committed constants)
All constants above are frozen in the verifier header. Per replicate the verifier computes cost/failure rates for the PM policy and for run-to-failure; it aggregates across TRIALS; the SE of a difference combines both arms (conservative — independent, not paired).

## Pre-registered gates (APPROVE iff ALL hold, in order G1 -> G2 -> G3; z_gate = 3.0)
- **G1 — cost penalty.** cost_rate(PM) - cost_rate(RTF) > 0 with z ≥ 3.0. Age replacement strictly overpays a constant-hazard unit.
- **G2 — benefit absent.** The promised 0.10·λ failure-rate reduction is rejected: (0.10·λ - observed_reduction)/se ≥ 3.0. Observed reduction is statistically zero.
- **G3 — robustness under a shifted distribution.** In the shifted (λ', T', costs') exponential world, both G1 and G2 hold at z ≥ 3.0. The paradox is not an artifact of the baseline constants.

Non-gated crossover diagnostic (disclosed, bounds the claim): under Weibull(shape 2.5, same mean), a finite T* < ∞ strictly beats run-to-failure — age replacement pays off exactly when hazard increases with age.

## Pre-registered decision rule
APPROVE iff all_pass = true (G1 ∧ G2 ∧ G3) AND the reproduced results-dict sha256 equals 0a9c4406...424bd69 byte-for-byte under SEED=20260717 with exit 0 and an identical in-process double-run. Any gate false, digest mismatch, or nondeterminism → REJECT.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
{
  "all_pass": true,
  "base": {
    "cost_penalty_pct": 30.81864,
    "failure_rate_reduction": 8.1e-05,
    "pm_cost_rate": 6.541129,
    "pm_failure_rate": 0.999949,
    "promised_reduction": 0.1,
    "rtf_cost_rate": 5.000151,
    "rtf_failure_rate": 1.00003,
    "z_benefit": 111.984471,
    "z_cost": 362.634738
  },
  "crossover": {
    "weibull_beats_rtf": true,
    "weibull_best_cost_rate": 3.071961,
    "weibull_best_t": 0.55,
    "weibull_rtf_cost_rate": 5.0,
    "weibull_shape": 2.5
  },
  "first_failing_gate": null,
  "gates": {
    "G1_cost_penalty": true,
    "G2_benefit_absent": true,
    "G3_robustness": true
  },
  "params": {
    "c_fail": 5.0,
    "c_fail_shift": 8.0,
    "c_plan": 1.0,
    "c_plan_shift": 1.0,
    "delta_null": 0.1,
    "lam": 1.0,
    "lam_shift": 1.7,
    "n_cycles": 100000,
    "t_pm": 0.5,
    "t_pm_shift": 0.3,
    "trials": 30,
    "weibull_shape": 2.5
  },
  "proposal": "PROPOSAL 165",
  "seed": 20260717,
  "shifted": {
    "cost_penalty_pct": 18.764686,
    "failure_rate_reduction": 0.000595,
    "pm_cost_rate": 16.149977,
    "pm_failure_rate": 1.699192,
    "promised_reduction": 0.17,
    "rtf_cost_rate": 13.598299,
    "rtf_failure_rate": 1.699787,
    "z_benefit": 82.044394,
    "z_cost": 159.820952
  },
  "sigma_gate": 3.0,
  "slot": "round-39 FLEET",
  "theory": {
    "exp_failure_rate_invariant": 1.0,
    "exp_pm_cost_rate": 6.541494,
    "exp_rtf_cost_rate": 5.0
  }
}
Results-JSON sha256: 0a9c4406e8abc9a6fa51b80a0101c6f55277f3304c3d8b468b13f4600424bd69
```

## Verifier
`ideas/fleet/memoryless_pm_waste.py` — stdlib only (math, json, hashlib, random). Simulates the age-replacement and run-to-failure policies by direct renewal sampling; computes z-margins; analytically integrates the Weibull cost rate for the crossover. WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: run() twice in-process, canonical-dict sha256 asserted equal, dict printed at indent=2 sorted 6 dp, then the sha256 line. No file writes.

## Reproduce
```
python3 ideas/fleet/memoryless_pm_waste.py
# expect: all_pass true, exit 0, Results-JSON sha256: 0a9c4406e8abc9a6fa51b80a0101c6f55277f3304c3d8b468b13f4600424bd69
```

## Why it matters
Fleet maintenance budgets are routinely spent on calendar/age-based replacement of components whose empirical hazard is flat (electronics, many software-restart regimes, random-shock failures). For those, this head is a strict cost sink with zero reliability return — the lever is spares depth and fast repair (Palm), not PM cadence. It also gives a clean, checkable decision rule: measure the hazard slope before scheduling PM; schedule age replacement only where hazard demonstrably increases (the Weibull crossover shows a ~39% cost cut is available there).

## Dedup (contrast vs prior fleet heads)
Distinct from `palm-spares-insensitivity` (spare-stock level insensitive to repair-time distribution — a stocking result, not a replacement-policy result), `checkpoint-interval-optimum` (Young/Daly √(2δ·MTBF) checkpoint spacing — an interior optimum exists there; here the optimum is the boundary T→∞), and `series-reliability-collapse` (structural reliability of series systems). No prior fleet head addresses age-replacement / PM policy or the constant-vs-increasing-hazard crossover.

## Model basis (declared model-dependence — the P024 discipline)
The head is exact for a constant-hazard lifetime (memorylessness). It weakens or reverses under: increasing hazard (wear-out — disclosed Weibull crossover), imperfect repair, nonzero replacement lead-time (adds an availability tax that RTF also pays), or economies of batching planned work. These are the honest boundaries; the gates test only the constant-hazard claim and its robustness to parameter shifts.

## Gate power + margin ledger
| Gate | Claim | Statistic | Observed | Threshold | Result |
|---|---|---|---|---|---|
| G1 | PM overpays (baseline) | z of Δcost | 362.63 | ≥ 3.0 | PASS |
| G2 | promised benefit absent (baseline) | z of (0.10λ - reduction) | 111.98 | ≥ 3.0 | PASS |
| G3a | PM overpays (shifted) | z of Δcost | 159.82 | ≥ 3.0 | PASS |
| G3b | benefit absent (shifted) | z of (0.10λ' - reduction) | 82.04 | ≥ 3.0 | PASS |
| — | baseline cost penalty | Δcost % | +30.82% | > 0 | disclosed |
| — | Weibull wear-out crossover | T* / cost vs RTF | 0.55 / 3.072 vs 5.0 | beats RTF | disclosed |

## Probe report (v0, self-adversarial)
**1. Isn't a real fleet's failure rate obviously lowered by replacing old parts?** Only if "old" carries higher hazard. For constant hazard, "old" and "new" are statistically identical; the sim confirms the failure rate stays at λ for every T.
**2. Could the cost penalty be an artifact of c_fail/c_plan = 5?** No — the cost rate falls in T for any c_fail > c_plan > 0; the shifted world (ratio 8) reproduces the penalty at z ≈ 160.
**3. Is DELTA_NULL = 0.10 cherry-picked to be easy to reject?** It's a deliberately modest strawman (a 10% reduction is small); the observed reduction is ~0, so even this small promised benefit is rejected by >80σ.
**4. Does the digest depend on float order?** Floats are rounded to 6 dp before canonical hashing; the in-process double-run assert guarantees stability; cross-invocation identical on the same runtime (verified twice this session).
**5. Why independent (not paired) replicates?** Independence inflates the difference SE, making the z-margins conservative; paired sampling would only raise them.
**6. Is the Weibull crossover cooked?** It's analytic (trapezoid over the survival function), non-gated, and disclosed precisely to bound the claim — it shows where PM does pay (T*≈0.55, ~39% cheaper than RTF), the honest counterpoint.
**7. What about replacement lead-time / downtime?** Not modelled; it adds an availability tax that run-to-failure also incurs, and can shift the trade-off — flagged as a boundary and a candidate follow-up head.
**8. What exactly must the verdict reproduce?** The verifier byte-for-byte under SEED=20260717, matching results-dict sha256 0a9c4406...424bd69, all_pass=true, the G1/G2/G3 z-margins as tabled, exit 0, and an identical double-run.

## One-line design fix
Before funding any age/calendar PM schedule, estimate the component's hazard slope; schedule age replacement only where hazard rises with age, and otherwise put the money into spares depth and repair speed.

**Recommendation: sim-ready**
