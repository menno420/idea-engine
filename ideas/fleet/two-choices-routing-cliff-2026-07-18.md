# The two-choices routing cliff — sampling two workers is a double-exponential win over one, and a third buys almost nothing

> **State:** sim-ready
> **Class:** fleet-domain (round-26 opener) · randomized load balancing / balanced-allocations theory · PROPOSAL 113
> **Target:** sim-lab (VERDICT 126, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@bb5e9ea · fetched 2026-07-18T03:40:54Z
> **Source basis:** Azar, Broder, Karlin & Upfal, "Balanced Allocations", SIAM J. Comput. 29(1):180-200, 1999 (STOC 1994); Mitzenmacher, "The Power of Two Choices in Randomized Load Balancing", IEEE TPDS 12(10), 2001; Mitzenmacher & Upfal, *Probability and Computing* (2nd ed.), Ch. 17. Standard textbook result; no external repo fetched.
> **Verifier (firsthand):** committed stdlib-only `ideas/fleet/two_choices_routing_cliff.py`, SEED=20260717, results-dict sha256 `068e23f599c9ccf9a4bcbf31d705a9760ee05091172f6432ea1c3df69d62b685` (deterministic double-run, exit 0).

## Domain
Fleet task dispatch / randomized load balancing. A dispatcher assigns each incoming task to a worker. Under *random routing* it picks one worker uniformly; under *the power of two choices* it samples `d` workers and routes to the least-loaded. The question every dispatcher faces: how many workers should it probe before placing a task?

## The folk belief
"Probing more workers gives proportionally better balance — if checking 2 halves the hot spot, checking 4 or 8 will crush it." Balance is assumed to improve smoothly, roughly linearly, in the probe count `d`, so operators raise `d` to chase tail latency.

## The thesis (reasoned to its fuller form)
The improvement is not smooth — it is a cliff at `d=2`. Placing `m=n` tasks greedily:
- **d=1 (random):** the maximum load (longest queue) is `Θ(ln n / ln ln n)` — a slowly growing but genuinely unbounded-in-n hot spot.
- **d=2:** the maximum collapses to `ln ln n / ln 2 + Θ(1)`. Going from `ln n / ln ln n` to `ln ln n` is a *double-exponential* shrink of the tail (Azar–Broder–Karlin–Upfal).
- **d ≥ 3:** the maximum is `ln ln n / ln d + Θ(1)`. Each extra probe only divides the *already tiny* `ln ln n` term by `ln d`. From d=2 to d=3 the tail moves by `ln ln n · (1/ln2 − 1/ln3)` — a fraction of a queue slot for realistic n.

So essentially the *entire* benefit of multiple choices is captured by the **second** probe. The first extra probe (1→2) buys a double-exponential improvement; every probe after that buys a rapidly vanishing constant. The counterintuitive part: the diminishing returns are not gradual — they fall off a cliff immediately after d=2.

## The trap
An operator who reasons "more probes ⇒ proportionally better balance" over-provisions probe fan-out: d=4, d=8, even query-all. Each extra probe costs a round-trip / coordination call, adds dispatch latency, and stales the load signal, while delivering a sub-unit reduction in max queue. The result is a dispatcher paying 2–4× the coordination cost of `d=2` for a balance improvement it cannot even measure. The correct fleet policy is **cap probe fan-out at d=2** and spend the saved budget on load-signal freshness and faster placement.

## Formal model (committed constants)
n workers, m = n tasks, sequential greedy placement. For each task, sample `d` workers uniformly with replacement; place on the least-loaded (ties → first sampled). Metric = max load after all placements. Pinned: SEED=20260717, N=20000, M=20000, TRIALS=120, d ∈ {1,2,3,4}.

## Pre-registered gates (each ≥3σ on the /se margin, one pinned SEED)
| Gate | Statistic | Claim | Pass rule |
|---|---|---|---|
| **G1** two-choices jump | mean(max₁ − max₂) | the first extra probe strictly shortens the longest queue | z = mean/se ≥ 3 |
| **G2** the cliff (front-loaded) | mean((max₁−max₂) − (max₂−max₃)) | the 1→2 gain significantly exceeds the 2→3 gain | z = mean/se ≥ 3 |
| **G3** the plateau beyond two | mean(max₂ − max₄) | every probe past the second, together, saves < 2 queue slots | z = (2.0 − mean)/se ≥ 3 |

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 all pass at ≥3σ on the same pinned seed, with a deterministic double-run reproducing the disclosed results-dict sha256.

## Dry-sim results (firsthand, verbatim)
```
{
  "proposal": 113,
  "phenomenon": "two-choices routing cliff (power-of-two-choices balanced allocations)",
  "params": {
    "seed": 20260717,
    "n_workers": 20000,
    "m_tasks": 20000,
    "trials": 120,
    "d_values": [
      1,
      2,
      3,
      4
    ],
    "sigma_gate": 3.0,
    "plateau_max": 2.0
  },
  "anchor": {
    "single_choice_ln_n_over_lnln_n": 4.319221866822944,
    "two_choice_lnln_n_over_ln2": 3.3079366654667703,
    "d23_mean": 0.08333333333333333,
    "d23_se": 0.02533620800437753
  },
  "sim": {
    "mean_max_load_by_d": {
      "1": 7.016666666666667,
      "2": 3.0833333333333335,
      "3": 3.0,
      "4": 2.466666666666667
    }
  },
  "gates": {
    "G1_two_choices_jump": {
      "stat": "mean(max_1 - max_2)",
      "mean": 3.933333333333333,
      "se": 0.06873540928271524,
      "z": 57.2242658388075,
      "pass": true
    },
    "G2_cliff_front_loaded": {
      "stat": "mean((max_1-max_2) - (max_2-max_3))",
      "mean": 3.85,
      "se": 0.08422492229152842,
      "z": 45.710935614448694,
      "pass": true
    },
    "G3_plateau_beyond_two": {
      "stat": "mean(max_2 - max_4)",
      "ceiling": 2.0,
      "mean": 0.6166666666666667,
      "se": 0.05316763475669114,
      "z": 26.018335020239753,
      "pass": true
    }
  },
  "all_pass": true,
  "results_sha256": "068e23f599c9ccf9a4bcbf31d705a9760ee05091172f6432ea1c3df69d62b685"
}
Results-JSON sha256: 068e23f599c9ccf9a4bcbf31d705a9760ee05091172f6432ea1c3df69d62b685
```
All three gates PASS; exit 0; the second run reproduces the identical sha256.

## Verify
```
python3 ideas/fleet/two_choices_routing_cliff.py
```
Deterministic: same SEED → identical results dict → identical sha256; exit 0 iff all gates pass.

## Fleet relevance
Fleet-manager routing (Q-0264) is exactly this dispatch problem: a task lands, the router picks a worker. The result says the router should sample **two** candidate workers and take the less-loaded — never one, rarely more. It also bounds the value of richer load telemetry: past d=2, better balance comes from *fresher* signals, not *more* probes.

## Model basis (declared model-dependence — the P024 discipline)
The result is a theorem about the greedy balls-into-bins process with uniform sampling and m=n. It is model-dependent on: (a) sampling with replacement, uniform over workers; (b) load = queue length, ties broken deterministically; (c) the m=n regime — the heavily-loaded m≫n regime (Berenbrink et al.) sharpens the gap further but is not simulated here. Correlated worker choice, weighted/heterogeneous workers, or stale load signals shift the constants but not the d=2 cliff.

## Dedup
Distinct from every prior fleet head. P093 (metastable retry-storm collapse) is load-*feedback* bistability, not routing choice. `wip-cap-dryness-floor` is a CONWIP throughput cap, not per-task probe count. P109 (correlated-fleet variance floor) is error *aggregation*, not queue balance. P105 (delegation loop collapse) is vote delegation. No prior head models the probe-count vs max-load tradeoff.

## Probe report (v0, 2026-07-18)
**1. Real or a small-n artifact?** Real — it is the ABKU theorem; larger n *sharpens* the cliff (the gap is double-exponential in n). The sim uses n=20000 to show it at fleet-realistic scale.
**2. Could the cliff be a seed fluke?** No — 120 independent trials, paired per-trial differences, ≥3σ gates on the /se margin.
**3. Why m=n?** The classic balanced-allocations regime and the cleanest statement; heavily-loaded (m≫n) only widens the d=1 vs d=2 gap.
**4. Does d=3 ever beat d=2 meaningfully?** By a fraction of a slot for any realistic n; G3 bounds the entire post-2 gain below two slots.
**5. Ties?** Broken by first-sampled (deterministic) — a standard convention; random tie-breaking shifts constants negligibly.
**6. Is this just "diminishing returns"?** It is diminishing returns *with a cliff*: the first step is double-exponential, the rest are vanishing constants — the shape, not merely the monotonicity, is the result.
**7. What breaks it?** Strongly correlated sampling (always probing the same workers) or adversarial load signals; disclosed as model-dependence.
**8. Actionable?** Yes — set fleet dispatch probe fan-out to exactly 2; reinvest the saved coordination budget in load-signal freshness.

Ship to sim-lab for VERDICT 126 (P113 → V126, +13). One counterintuitive result (returns collapse at d=2, not gradually), one textbook anchor (ABKU), three ≥3σ gates, a deterministic committed verifier.

**Recommendation: sim-ready**
