# PROPOSAL 176 — The giant-component phase transition: a random graph's largest cluster snaps from a vanishing fraction to a macroscopic one exactly as average degree crosses 1

> **State:** sim-ready
> **Class:** network science / statistical physics
> **Slot:** round-42 UNRELATED
> **Anchor:** Erdős–Rényi random-graph evolution — the giant component emerges at the critical average degree c = 1
> **Target:** sim-lab (VERDICT 189, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Giant_component@66da05b62033927be39802f77888c6408fdee263 · fetched 2026-07-19T16:36:37Z
> **Reference (external, reachable):** https://en.wikipedia.org/w/index.php?title=Giant_component&oldid=1340194064 — HTTP 200, permalink (oldid 1340194064)
> **Verifier (firsthand):** `ideas/fleet/giant_component_threshold.py` · results-dict sha256 `14875022bef41594dbc8d19bd2960724d2f86f6dedcadf1b339f228915469537`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)

In a random graph on n nodes formed by adding m = round(c·n/2) uniformly random edges (average degree ≈ c), the fraction of nodes in the largest connected component is not a smooth function of c — it stays a vanishing fraction (order log n / n) for c < 1 and jumps to a constant fraction ρ(c) > 0 the instant c crosses 1.

## The folk belief

"Connectivity accretes gradually: add twice the edges, get roughly twice the largest cluster. There is nothing special about one edge per node." Under this view the largest component grows smoothly and roughly linearly in average degree.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Exploring the component of a node is a branching process: following edges, each node reaches on average c new nodes. When c < 1 the branching is subcritical — exploration dies out after order 1/(1−c) steps, so every component is tiny and the largest over n starts is only order log n (a vanishing fraction). When c > 1 the branching is supercritical — exploration survives with positive probability, and all surviving explorations coalesce into a single macroscopic "giant" component whose fraction ρ solves the mean-field self-consistency ρ = 1 − exp(−c·ρ); every other component stays order log n. The transition at c = 1 is exactly the branching-process criticality boundary (mean offspring = 1). It is the same universality class as bond percolation on the complete graph: the giant component is the percolating cluster. So the folk "smooth growth" picture is wrong twice over — nothing macroscopic exists below the threshold, and above it a constant fraction appears abruptly rather than accreting linearly.

## The formal model (committed constants — sim-lab must reproduce exactly)

Each condition draws TRIALS = 40 i.i.d. random graphs. A graph G(n, m) has m = round(c·n/2) edges, each edge a uniform random ordered pair (self-loops skipped, multi-edges permitted — asymptotically equivalent to G(n, p = c/n)). Connectivity is computed by union-find (disjoint-set, union-by-size + path halving). The measured statistic per graph is largest_component_size / n. Per condition we report the mean and standard error over the 40 trials.

## Pinned world (committed constants)

- `SEED = 20260717`, `Z_GATE = 3.0`, `TRIALS = 40`.
- Sizes: `n1 = 4000`, `n2 = 16000` (a 4× scale shift for the robustness gate).
- Average degrees probed: `c ∈ {0.5, 0.7, 0.9, 1.1, 1.4}`.
- Single `random.Random(SEED)` stream drawn in a fixed condition order (subcritical/supercritical at n1, then subcritical/supercritical at n2, then c=0.5, 0.9, 1.1 at n2).
- Mean-field anchor: `ρ = 1 − exp(−c·ρ)` ⇒ ρ(1.4) ≈ 0.51.

## Pre-registered gates (APPROVE iff ALL hold, in order G1 -> G2 -> G3; z_gate = 3.0)

- **G1 — existence.** Supercritical (c=1.4, n=4000) largest-component fraction `0.507138` ≥ 0.30 AND subcritical (c=0.7, n=4000) fraction `0.008025` ≤ 0.08 AND z of the difference `263.375801` ≥ 3.0. PASS.
- **G2 — robustness (4× scale shift).** At n=16000 the supercritical giant fraction `0.511348` ≥ 0.30 with z vs the 0.30 floor `204.254546` ≥ 3.0; size-invariant (|0.511348 − 0.507138| = 0.004211 ≤ 0.05); and the subcritical fraction shrinks with n (0.008025 → 0.002861). PASS.
- **G3 — sharpness / placebo.** Near-threshold jump frac(1.1) − frac(0.9) = 0.169817 − 0.010175 = 0.159642 exceeds the far-subcritical jump frac(0.7) − frac(0.5) = 0.002861 − 0.001248 = 0.001612 by z = `33.80426` ≥ 3.0, with all sub-threshold fractions ≤ 0.15 — growth is concentrated at c ≈ 1, rejecting the smooth-linear-growth null. PASS.

## Pre-registered decision rule

APPROVE iff `all_pass == true` (G1 ∧ G2 ∧ G3, evaluated in order) and the reproduced results-dict sha256 equals `14875022bef41594dbc8d19bd2960724d2f86f6dedcadf1b339f228915469537` byte-for-byte under SEED=20260717. Any gate fail, or any digest mismatch, is a REJECT; `first_failing_gate` names the earliest failure.

## Dry-sim results (SEED=20260717, verbatim stdout of the verifier)

```json
{
  "all_pass": true,
  "conditions": {
    "n16000_c0.5": {
      "mean": 0.001248,
      "se": 4.8e-05
    },
    "n16000_c0.9": {
      "mean": 0.010175,
      "se": 0.000742
    },
    "n16000_c1.1": {
      "mean": 0.169817,
      "se": 0.004614
    },
    "sub_n16000_c0.7": {
      "mean": 0.002861,
      "se": 0.000123
    },
    "sub_n4000_c0.7": {
      "mean": 0.008025,
      "se": 0.000439
    },
    "sup_n16000_c1.4": {
      "mean": 0.511348,
      "se": 0.001035
    },
    "sup_n4000_c1.4": {
      "mean": 0.507138,
      "se": 0.001844
    }
  },
  "first_failing_gate": null,
  "gates": {
    "G1_existence": {
      "pass": true,
      "sub_mean": 0.008025,
      "sup_mean": 0.507138,
      "z": 263.375801
    },
    "G2_robustness": {
      "pass": true,
      "size_gap": 0.004211,
      "sub_shrinks": true,
      "sup_mean_n16000": 0.511348,
      "z_vs_floor": 204.254546
    },
    "G3_sharpness": {
      "jump_far": 0.001612,
      "jump_near": 0.159642,
      "pass": true,
      "z": 33.80426
    }
  },
  "head": "giant-component-threshold",
  "seed": 20260717,
  "trials": 40,
  "z_gate": 3.0
}
Results-JSON sha256: 14875022bef41594dbc8d19bd2960724d2f86f6dedcadf1b339f228915469537
```

## Verifier

`ideas/fleet/giant_component_threshold.py` — stdlib only (`hashlib`, `json`, `math`, `random`). Union-find over n nodes; TRIALS random graphs per condition; per-gate z-scores. Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: the results dict carries no digest field; `main()` runs `compute()` twice in-process, asserts byte-identical compact-canonical (`sort_keys=True, separators=(",",":")`) serializations, prints the pretty (`indent=2, sort_keys=True`) dump, then `Results-JSON sha256: <hex>` over the compact-canonical form. Nothing is written to disk.

## Reproduce

```
python3 ideas/fleet/giant_component_threshold.py
python3 ideas/fleet/giant_component_threshold.py   # run twice; stdout must be byte-identical
```
Expect `"all_pass": true`, `"first_failing_gate": null`, and `Results-JSON sha256: 14875022bef41594dbc8d19bd2960724d2f86f6dedcadf1b339f228915469537` on every invocation (Python 3.11).

## Why it matters

Percolation-style thresholds govern any system whose usefulness switches on with connection density: an ad-hoc mesh network becomes globally reachable, a rumor or failure cascades across a whole population, a material conducts. The counterintuitive design fact is that the transition is sharp — a system at average degree 0.95 is essentially disconnected and one at 1.05 is globally connected, so "add a few more links" near the threshold is not a marginal improvement but a phase change. Provisioning to average degree exactly 1 is the worst place to sit: maximum sensitivity, order n^(2/3) critical fluctuations.

## Dedup (contrast vs prior lane heads)

- **Stein / James-Stein shrinkage-dominance (P128 → V141, `ideas/fleet/stein_shrinkage_dominance.py`):** a decision-theoretic result on the inadmissibility of the multivariate-mean MLE. This head is a connectivity phase transition governed by branching-process criticality — different phenomenon, different mechanism.
- **friendship-paradox size-bias head (P164):** degree-sampling bias on a fixed graph (your friends have more friends than you). This head is about the emergence of macroscopic connectivity as edge density crosses a threshold — no sampling bias, a different object.
- Dedup search run on-branch: `git grep -il "giant component | percolation | erdos | random graph"` across `ideas/` returned no prior head on this mechanism.

## Model basis (declared model-dependence)

The head is the classical Erdős–Rényi result: the c = 1 threshold and the fixed point ρ = 1 − exp(−c·ρ) are asymptotic (n → ∞). The verifier measures finite-n graphs, so the gates use generous absolute bounds (giant ≥ 0.30, subcritical ≤ 0.08 / 0.15) that the asymptotics clear comfortably at n = 4000 and 16000; the direction (sharp threshold at c ≈ 1, size-invariant giant above it) is what is tested, not exact critical-window values. G(n, m) with uniform random pairs is used in place of G(n, p); the two are asymptotically equivalent and multi-edges/self-loops are negligible at this density.

## Gate power + margin ledger

| Gate | Statistic | Measured | Null | z | Margin over z_gate=3.0 |
|------|-----------|----------|------|-----|------------------------|
| G1 | sup − sub fraction (n=4000) | 0.507138 − 0.008025 | 0 | 263.375801 | ~88× |
| G2 | sup fraction (n=16000) vs 0.30 floor | 0.511348 | 0.30 | 204.254546 | ~68× |
| G3 | near-jump − far-jump | 0.159642 − 0.001612 | 0 | 33.80426 | ~11× |

All gates clear z_gate by an order of magnitude or more; the head is not marginal.

## Probe report (v0, self-adversarial)

**1. Is the supercritical giant fraction genuinely intensive (size-invariant), or a finite-n artifact?** Intensive: at c=1.4 the fraction is 0.507138 (n=4000) vs 0.511348 (n=16000), a gap of 0.004211 ≤ 0.05, while the subcritical fraction at c=0.7 shrinks 0.008025 → 0.002861 as n quadruples (order log n / n → 0). G2 confirms at z=204.25 vs the 0.30 floor.

**2. Is the growth concentrated at c ≈ 1 rather than smooth and linear in average degree?** Yes: the jump crossing the threshold (frac(1.1) − frac(0.9) = 0.159642) is roughly a hundred times the equal-width far-subcritical jump (frac(0.7) − frac(0.5) = 0.001612), z=33.80 ≥ 3 — a sharp transition, not linear accretion. A linear-growth null predicts equal jumps for equal Δc and is rejected.

**3. Does the measured ρ(1.4) match the mean-field fixed point ρ = 1 − exp(−c·ρ)?** Yes: solving ρ = 1 − exp(−1.4ρ) gives ρ ≈ 0.51, matching the measured 0.511348 (n=16000) within 0.002.

**4. Does the grounding source document the specific c=1 threshold head, not just random graphs generally?** The Wikipedia "Giant component" article documents the emergence of a giant component at the phase transition where expected degree crosses 1 — the exact c = 1 threshold head. Grounding pinned at content hash `66da05b62033927be39802f77888c6408fdee263` / oldid 1340194064, HTTP 200.

**5. Is the result an artifact of the G(n, m) uniform-pair model versus G(n, p)?** No. The two models are asymptotically equivalent; at m = round(c·n/2) the induced degree distribution is Poisson(c) in the limit, and the c = 1 threshold is model-independent. Self-loops are skipped and multi-edges are negligible at O(n) edges.

**6. Could the union-find measurement bias the largest-component size upward?** No — union-find computes exact connected components; `largest` tracks the true maximum set size. The reported statistic is exact per graph, and determinism is asserted by a byte-identical in-process double-run.

**7. Is `all_pass` gameable by a single degenerate parameter?** No: the three gates test three distinct directions (existence above threshold, scale-invariance under a 4× shift, sharpness at the threshold). No single degenerate setting satisfies all three; a verdict session reproduces the exact digest to confirm the constants.

**8. How will a verdict session know it reproduced the head?** It re-runs the stdlib verifier under SEED=20260717 and confirms `all_pass=true`, `first_failing_gate=null`, and the results-dict sha256 equals `14875022bef41594dbc8d19bd2960724d2f86f6dedcadf1b339f228915469537` byte-for-byte; any gate fail or digest mismatch is a REJECT.

## One-line design fix

For any density-gated system, do not provision to average degree ≈ 1 (the critical point of maximum sensitivity): sit comfortably above 1 to guarantee a giant component, because near the threshold connectivity is a phase change, not a dial.

**Recommendation: sim-ready**
