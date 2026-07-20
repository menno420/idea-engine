# Give a greedy scheduler one more machine and the batch can finish *later*

> **State:** sim-ready
> **Class:** fleet-ops / scheduling / distributed-systems
> **Target:** sim-lab (VERDICT 214, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/w/index.php?title=List_scheduling&oldid=1291511174@e2de39981e1fdc4d2daf8d7411f1f3dc0f32aaa2 · fetched 2026-07-20
> **Reference (external, reachable):** [Wikipedia — List scheduling, rev 1291511174](https://en.wikipedia.org/w/index.php?title=List_scheduling&oldid=1291511174) — verified reachable; states both the bound and the anomalies. Quote: "The algorithm always returns a partition of the jobs whose makespan is at most 2−1/m times the optimal makespan." and "Adding a machine has enlarged the makespan." (R. L. Graham, "Bounds on Multiprocessing Timing Anomalies", SIAM J. Appl. Math., 1969).
> **Verifier (firsthand):** ideas/fleet/graham_scheduling_anomaly.py · results-dict sha256 2f81534216b6d8dee3d99446a0e451bde7cd64019d5f10b7de59a01921129eef

## The phenomenon (one line)
A greedy list scheduler is non-monotone: giving it another machine, shortening every job, or dropping a dependency can each make the batch finish *later* — while the same greedy schedule is provably never worse than (2 − 1/m)× the optimum.

## Domain
Fleet-ops batch/job scheduling on m identical workers with precedence constraints (build farms, CI shards, DAG task runners, MapReduce-style stages). The scheduler is greedy list scheduling: whenever a worker is idle it starts the highest-priority ready task.

## The folk belief
More resources never hurt. Add a worker, or make every task faster, or remove a dependency, and the batch can only finish sooner (or at worst the same). Capacity is monotone.

## The thesis (reasoned to its fuller form — Q-0254 duty)
Greedy list scheduling fixes a *priority order*, not a plan. Relaxing an input changes *which* task is ready at each instant, which reshuffles the greedy choices downstream — and the reshuffle can strand the critical path behind a newly-started long task. Graham (1969) proved this is not a quirk of one scheduler but intrinsic: for the same instance, `makespan(m+1)` can exceed `makespan(m)`; `makespan(shorter jobs)` can exceed `makespan(original)`; `makespan(fewer edges)` can exceed `makespan(more)`. The saving grace is a tight worst-case guarantee: greedy makespan ≤ (2 − 1/m)·OPT, so the anomaly can never blow up by more than a bounded factor. Both halves are exactly true and both are shown here: the non-monotonicity empirically (three independent levers) and the bound exactly (Fraction arithmetic against the exhaustively-computed optimum).

## The formal model / Pinned world (committed constants)
- SEED = 20260717. Each gate draws from its own `random.Random(SEED + k)` (G1: k=0, G2: k=1, G3: k=2) so streams are independent and byte-reproducible.
- Instances: n jobs (n∈[6,12] for G1/G2, n∈[3,6] for G3), m machines (m∈[2,4] for G1/G2, m∈{2,3} for G3), integer durations in [1,9], random acyclic precedence (edge prob 0.25, only earlier→later), random priority order.
- Scheduler: greedy non-preemptive list scheduling, event-driven, exact integer time.
- Optimum (G3 only): idle-allowing branch search — greedy/non-delay schedules do not always contain the makespan optimum under precedence, so the optimizer may leave a machine deliberately idle.

## Pre-registered gates
- **G1 — surprise (DIRECTION: high z).** Remove one random precedence edge (a relaxation); null hypothesis "monotone in constraints" predicts the makespan-increase rate = 0. Gate: z1 = p̂/SE ≥ 10 over N1 = 60000 eligible DAGs.
- **G2 — robustness (DIRECTION: high z on each).** The same non-monotonicity under two more independent levers: (i) add-a-machine `list(m+1) > list(m)`; (ii) shorten every job by 1 `list(t−1) > list(t)`. Gate: both z ≥ 3 over N2 = 500000.
- **G3 — exactly-true (DIRECTION: zero violations, Fraction-exact).** Over K = 20000 small instances, `Fraction(greedy, optimum) ≤ Fraction(2m−1, m)` with zero violations and a non-trivial max ratio (> 1) — the closed-form (2 − 1/m) bound checked against the exhaustively-computed true optimum.
- `all_pass = G1 and G2(i) and G2(ii) and G3`.

## Pre-registered decision rule
Ship as sim-ready iff `all_pass = true` and the results-dict sha256 is byte-identical across two fresh invocations. sim-lab APPROVEs iff an independent re-implementation reproduces the sha256 and all four gate conditions.

## Dry-sim results (SEED=20260717, verbatim from graham_scheduling_anomaly.py)
- G1 remove-edge: count 5470 / N 60000, p̂ = 0.091167, z1 = 77.580315 ≥ 10 → PASS.
- G2 add-a-machine: count 72 / N 500000, p̂ = 0.000144, z = 8.485892 ≥ 3 → PASS.
- G2 shorten-all: count 85 / N 500000, p̂ = 0.000170, z = 9.220328 ≥ 3 → PASS.
- G3 (2−1/m) bound: 20000 instances, 0 violations, max ratio 11/7 ≈ 1.571429, 8122 non-trivial → PASS.
- Add-a-machine witness: m=2 makespan 27 → m=3 makespan 28 (strictly larger).
- `all_pass = true`; results-dict sha256 = 2f81534216b6d8dee3d99446a0e451bde7cd64019d5f10b7de59a01921129eef, byte-identical across two fresh invocations.

## Reproduce
```
python3 ideas/fleet/graham_scheduling_anomaly.py
```

## Verifier
`ideas/fleet/graham_scheduling_anomaly.py`, stdlib-only (random, math, hashlib, json, fractions, functools, itertools). Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY — the sha256 is over the canonical JSON of the results dict (sorted keys, compact separators), and the sha field is not part of the hashed dict. ~68s wall-clock.

## Why it matters
Fleet capacity planning assumes monotonicity: add workers, speed up tasks, loosen a dependency → never worse. Graham's anomaly says a greedy scheduler can violate all three, so a capacity bump can regress p100 batch completion. The operational lesson is the pair: expect non-monotonicity from greedy priority schedulers (validate scaling changes on the real DAG, don't assume), but rely on the (2 − 1/m) bound — the regression is provably capped, and a better order (e.g. LPT) tightens it.

## Dedup
`git grep -il 'graham\|makespan\|list.schedul\|multiprocess\|anomaly'` over `ideas/` finds no prior instance of this head. Nearest neighbors are distinct: `round-robin-domain-starvation-cliff` (single-resource starvation, not makespan non-monotonicity) and `venture-lab/owner-queue-attention-order` (single-machine SPT/LPT mean-completion sequencing, not multiprocessor makespan). Queueing-insensitivity heads (`service-variance-wait-tax`, `kleinrock-conservation`, `palm-spares-insensitivity`, `jackson-product-form`) are a different lane (stochastic steady-state), not this deterministic combinatorial anomaly.

## Model basis (declared model-dependence — the P024 discipline)
The empirical anomaly rates (G1/G2) depend on the pinned instance distribution (n/m ranges, edge prob 0.25, durations 1–9); the rates would shift under a different generator, but the *existence* of the anomaly and the (2 − 1/m) bound (G3) are distribution-free — G3 is a worst-case guarantee proved against the exact optimum, not a sampled estimate. The head claims non-monotonicity + the bound, both of which hold for any instance distribution producing precedence-constrained DAGs.

## Probe report (v0, 2026-07-20)
**1. Is the effect real and correctly stated?** Yes — Graham's 1969 timing anomaly; the verifier finds concrete witnesses for all three levers and a specific add-a-machine instance (m=2→3, makespan 27→28).
**2. Is the mechanism sound rather than a scheduling bug?** Yes — the list scheduler is textbook greedy non-preemptive; the optimum is an idle-allowing branch search validated on tiny known cases and cross-checked (opt ≤ every list schedule over 300 random instances).
**3. Is it counterintuitive?** Yes — it refutes the "more resources never hurt" monotonicity folk belief on three independent axes (machines, job sizes, dependencies).
**4. Is the verifier deterministic and reproducible?** Yes — stdlib-only, SEED=20260717, results-dict sha256 byte-identical across two fresh processes (2f81…eef).
**5. Are the gates pre-registered with explicit directions?** Yes — G1/G2 want high z (surprise/robustness), G3 wants zero violations (exactly-true, Fraction-exact); all pass with margin.
**6. Is the grounding external and specific?** Yes — Wikipedia "List scheduling" rev 1291511174 states both the (2−1/m) bound and the three anomalies verbatim, citing Graham 1969; pinned by the revision's 40-hex sha1.
**7. Is it un-built / non-duplicate?** Yes — no prior makespan/list-scheduling/Graham head in `ideas/`; nearest neighbors are distinct phenomena (see Dedup).
**8. Is it sim-lab reproducible and worth a VERDICT?** Yes — a clean-room re-implementation of list scheduling + branch-search optimum reproduces the sha256 and all four gate conditions from the pinned seed; the exact (2−1/m) bound gate gives sim-lab a Fraction-exact target.

**Recommendation: sim-ready**
