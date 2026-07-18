# Checkpointing a long fleet job MORE often is not safer: total wasted time is U-shaped in the checkpoint interval, so there is a unique best interval τ*=√(2·C·MTBF) (Young–Daly) and BOTH over- and under-checkpointing waste strictly more. On the pinned world (checkpoint cost C=1, MTBF M=200) the optimum wastes ~10.7% of wall time, but checkpointing 8× too often OR 8× too rarely each waste ~41–55%. And the best interval grows only as √MTBF: a 4× more reliable machine warrants only a 2× longer interval and halves the achievable overhead. "Checkpoint as often as you can afford" is a wasteful instinct — the optimum is interior, and the overhead floor is √(2C/MTBF).

> **State:** sim-ready
> **Class:** fleet (fault-tolerant computing / long-running-job scheduling) · the Young–Daly optimal checkpoint interval (checkpoint/restart overhead minimisation)
> **Target:** sim-lab (VERDICT 130, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@9e0861a · fetched 2026-07-18T05:05:06Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Application_checkpointing — checkpoint/restart fault tolerance and the optimum-checkpoint-interval literature (Gelenbe, "On the optimum checkpoint interval", JACM 1979; the closed form is Young, "A first order approximation to the optimum checkpoint interval", CACM 1974, τ*=√(2·δ·M), and Daly, "A higher order estimate of the optimum checkpoint interval for restart dumps", FGCS 2006); verified reachable 2026-07-18.
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/fleet/checkpoint_interval_optimum.py` (random, math, json, hashlib) — dry-sim exit 0, all gates PASS, results-dict sha256 43a77ca7…6be566a81 (see Verifier + Dry-sim below).

## The phenomenon (one line)
A long fleet job (a big training run, a multi-hour batch, a long agent task) can crash and restart from its last checkpoint. Checkpoint too RARELY and each crash discards a lot of recomputed work; checkpoint too OFTEN and the direct checkpoint cost dominates. Total wasted wall time is a **U-shaped** function of the checkpoint interval τ, minimised at a unique **interior** optimum τ* = √(2·C·M) (C = checkpoint cost, M = MTBF), where the achievable overhead is √(2C/M). On the pinned world (C=1, M=200) the optimum interval is **τ*=20** with overhead **~10.7%**, while checkpointing 8× too often (τ=2.5) wastes **~41.2%** and 8× too rarely (τ=160) wastes **~54.5%** — over-checkpointing is not "safer", it is wasteful.

## The folk belief
"Failures are the enemy of a long job, and a checkpoint is insurance against losing work, so to be safe you should checkpoint as frequently as you can afford — the more often you snapshot, the less you can ever lose to a crash. Wasted time falls monotonically as you checkpoint more; the only limit is how much checkpoint overhead you're willing to pay." The intuition treats checkpoint frequency as a one-sided safety dial (more = safer) and forgets that the checkpoints themselves are pure overhead paid on EVERY interval whether or not a crash ever happens.

## The scheduling thesis (reasoned to its fuller form — Q-0254 duty)
The intuition tracks only ONE of the two wastes. There are two, and they pull in opposite directions:

1. **Checkpoint overhead** — each checkpoint costs C, and you take one every τ units of useful work, so the direct cost per unit of useful work is ~ **C/τ**: *decreasing* in τ (fewer checkpoints, less overhead).
2. **Lost recompute work** — a crash discards everything since the last checkpoint. With Poisson failures at rate 1/M, a crash lands on average halfway through the current interval, so the expected recomputation per unit of useful work is ~ **τ/(2M)**: *increasing* in τ (longer intervals, more work at risk).

Total overhead per unit work ≈ `C/τ + τ/(2M)` — a **convex sum of a falling term and a rising term**, so it has a unique interior minimum where the two are equal: `C/τ = τ/(2M)` ⇒ **τ* = √(2·C·M)** (Young 1974). At that interval the two wastes are equal and the total overhead floor is `2·√(C/(2M)) = √(2C/M)` (Daly 2006 refines this with the exact model below). Three consequences the folk belief misses:

- **(1) The optimum is INTERIOR — more is not safer.** Because overhead is U-shaped, moving τ *below* τ* (checkpointing more often) *increases* total waste through the C/τ term. Over-checkpointing trades an unbounded reduction in recompute risk for an unbounded rise in direct overhead; at τ→0 the overhead diverges. The instinct "checkpoint as often as possible" walks *up* the left arm of the U.
- **(2) The two failure modes are SYMMETRIC in the leading order.** At τ = τ*·k the overhead is `C/(τ*k) + τ*k/(2M)`, and at τ = τ*/k it is `Ck/τ* + τ*/(2Mk)` — the same two numbers swapped. Checkpointing k× too often and k× too rarely inflate the *total* overhead by the same leading-order factor `½(k + 1/k)`. Neither extreme is privileged; both are wasteful.
- **(3) The optimum scales only as √M.** τ* = √(2CM) grows as the SQUARE ROOT of the MTBF, and the overhead floor √(2C/M) *falls* as 1/√M. So a machine 4× more reliable (M→4M) warrants an interval only **2× longer**, not 4×, and its achievable overhead **halves** (√(2C/M) → √(2C/4M) = ½·√(2C/M)) — you do not get to checkpoint 4× less often, and reliability buys overhead reduction sub-linearly.

Honest reading: the checkpoint interval is an OPTIMISATION, not a safety maximisation. There is a right answer, τ*=√(2CM); both checkpointing more and checkpointing less than that waste strictly more wall time, and the achievable overhead floor is set by √(2C/M) — reliability and checkpoint cost, not by "how paranoid you are".

## The formal model (committed constants — sim-lab must reproduce exactly)
- A job needs `W` units of useful work. It is done in segments of `τ` useful work, each followed by a checkpoint of cost `C`, so each attempt is exposed to failure for `L = τ + C`.
- Failures are Poisson at rate `1/M` (memoryless exponential inter-failure times), independent of checkpoints. **Restart cost R = 0.** On a crash at time `t < L` the wall time `t` is spent and the segment's partial work is LOST (retry from the last checkpoint); on success the attempt costs `L` and advances `τ` useful work.
- **Overhead fraction** of a run = `wall_time / effective_useful_work − 1`, where effective useful work = `n_seg · τ` and `n_seg = round(W/τ)`.
- By memorylessness the expected wall time per SUCCESSFUL segment is `M·(exp(L/M) − 1)`, so the exact expected overhead is the closed form (Daly 2006, R=0):

      O(τ) = (M/τ)·(exp((τ+C)/M) − 1) − 1

  minimised near `τ* = √(2CM)` with minimum near `√(2C/M)` (Taylor-expand exp to recover `O(τ) ≈ C/τ + τ/(2M)`).
- A scenario's overhead mean and standard error are taken over `TRIALS = 200` independent job runs, `se = sample-sd / √TRIALS` (the P104…P116 /se convention: z on the estimated mean).
- Closed-form anchors are the **exact Daly law** `O(τ)` above (evaluated in stdlib `math.exp`); the Young first-order values `τ*=√(2CM)` and `√(2C/M)` are reported descriptively.

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned; SEEDLESS discipline)
- C = 1.0 (checkpoint cost), M = 200.0 (MTBF), W = 40000.0 (useful work per run), K = 8 (extreme factor), TRIALS = 200, SIGMA_GATE = 3.0
- DELTA_MIN = 0.05 (G1/G2a min penalty in overhead-fraction), HALVE_MIN = 0.02 (G2b min optimum-overhead drop when the MTBF quadruples)
- Intervals: τ* = √(2·C·M) = **20.0**; frequent = τ*/K = **2.5** (8× too often); rare = τ*·K = **160.0** (8× too rarely); √-law control at M2 = 4M = 800 uses τ*(4M) = √(2·C·4M) = **40.0** (= 2·τ*)
- Exact Daly anchors: O(20) = **0.107106**, O(2.5) = **0.412322**, O(160) = **0.545871**, O(40 at M=800) = **0.051720**. Young first-order (descriptive): min overhead √(2C/M) = **0.10** at M=200, √(2C/4M) = **0.05** at M=800.

## Pre-registered gates (APPROVE iff ALL hold)
- **G1 — over-checkpointing (headline):** checkpointing K=8× MORE often than the optimum (interval τ*/K) wastes strictly MORE wall time than τ* — the frequent penalty `overhead(τ*/K) − overhead(τ*)` is ≥ DELTA_MIN = 0.05 by ≥3σ (z on its standard error). Inverts "checkpoint as often as possible is safest".
- **G2 — U-shape + square-root-law (control):** (a) checkpointing K=8× LESS often (interval τ*·K) ALSO wastes strictly more — the rare penalty `overhead(τ*·K) − overhead(τ*)` is ≥ DELTA_MIN = 0.05 by ≥3σ, so total waste is U-shaped with an INTERIOR optimum (neither extreme wins); AND (b) quadrupling the MTBF (M → 4M) with the interval scaled to its NEW optimum τ*(4M) = 2·τ* drops the optimum overhead by ≥ HALVE_MIN = 0.02 by ≥3σ — the overhead floor falls as √(2C/M) (roughly halving), isolating the √ law as the cause of the optimum's location.
- **G3 — closed-form anchor MATCH:** the three measured overheads reproduce the exact Daly law `O(τ) = (M/τ)(exp((τ+C)/M) − 1) − 1` within 3σ each — optimum vs 0.107106, frequent vs 0.412322, rare vs 0.545871 (|z| < 3 each). The effect IS the checkpoint-restart overhead law, and the Young optimum τ*=√(2CM) with minimum √(2C/M) sit at the measured minimum.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier (the verifier's `all_pass` field encodes exactly `G1 ∧ G2 ∧ G3`). Any gate failing → REJECT (the U-shaped-optimum / √-law claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; margins reported in σ on the standard error of the estimated mean.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- overhead at τ*=20 = **0.106933** (se 0.000300) — exact Daly anchor 0.107106 (Young descriptive 0.10)
- overhead at τ*/8=2.5 = **0.412435** (se 0.000065) — exact Daly anchor 0.412322 (8× too often)
- overhead at τ*·8=160 = **0.545241** (se 0.003414) — exact Daly anchor 0.545871 (8× too rarely)
- overhead at τ*(4M)=40, M=800 = **0.052066** (se 0.000313) — exact Daly anchor 0.051720 (Young descriptive 0.05)
- frequent penalty (τ*/8 − τ*) = **0.305502** (se 0.000307); rare penalty (τ*·8 − τ*) = **0.438308** (se 0.003427); halving drop (τ*@M − τ*@4M) = **0.054867** (se 0.000433)
- **G1 over-checkpointing:** frequent penalty 0.305502 ≥ 0.05 at z = **833.5744σ** — PASS (checkpointing 8× too often wastes ~30 more points of wall time)
- **G2 U-shape + √-law:** rare penalty 0.438308 ≥ 0.05 at z_rare = **113.2963σ** AND halving drop 0.054867 ≥ 0.02 at z_halve = **80.5085σ** — PASS (both arms rise; the optimum overhead halves when the MTBF quadruples)
- **G3 closed-form anchor:** opt 0.106933 vs 0.107106 |z| = **0.5778**; frequent 0.412435 vs 0.412322 |z| = **1.7438**; rare 0.545241 vs 0.545871 |z| = **0.1845** — all |z| < 3, PASS (exact Daly law reproduced)
- all_pass = true; **exit 0**
- Two runs byte-identical (deterministic under SEED).
- **Disclosed results-dict sha256 = 43a77ca77563e81f873cd73c81d35c684a2ec48bc26d2d740b083ef6be566a81**
  (this is the sha256 of `json.dumps(results, sort_keys=True, separators=(",",":"))` over the results dict BEFORE its `results_sha256` self-field is added — the value the verifier prints as `Results-JSON sha256:`; the P112/P116 self-field posture. The pretty-printed on-disk `checkpoint_interval_optimum_results.json` artifact's own `sha256sum` is NOT this digest, and that artifact is not committed.)

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `ideas/fleet/checkpoint_interval_optimum.py`. Seeds once with SEED=20260717, then for each of TRIALS=200 runs simulates a job of W=40000 useful work at each of four intervals — the optimum τ*=√(2CM)=20, the frequent τ*/8=2.5, the rare τ*·8=160, and the √-law control τ*(4M)=40 at the quadrupled MTBF M2=800 — segment-by-segment under Poisson(1/M) failures (fresh `expovariate` draws; a crash costs the elapsed time and loses the segment, retry from the last checkpoint), recording the overhead fraction `wall/effective_work − 1`. It takes means and standard errors over the runs, evaluates G1/G2/G3 on the /se margin against the EXACT Daly closed form `O(τ)=(M/τ)(exp((τ+C)/M)−1)−1` (the Young first-order `√(2CM)`/`√(2C/M)` values reported descriptively only, never used as a gate anchor), and emits a canonical (sorted-keys, comma/colon-separated) results JSON with its sha256. Exit 0 iff all three gates pass.

Reproduce:

```
python3 ideas/fleet/checkpoint_interval_optimum.py
```

Expected: all_pass=true, exit 0, G1 z=833.5744, G2 z_rare=113.2963 / z_halve=80.5085, G3 z_opt=0.5778 / z_frequent=1.7438 / z_rare=0.1845, results-dict sha256 = 43a77ca77563e81f873cd73c81d35c684a2ec48bc26d2d740b083ef6be566a81.

## Why it matters (cross-cutting)
Any fleet activity that does long work interruptibly against a persisted snapshot faces this exact tradeoff — a multi-hour training run checkpointing weights, a batch pipeline writing intermediate state, a long agent task committing progress, a stream processor snapshotting offsets, a simulation dumping restart files. The transferable correction: the checkpoint (or snapshot / commit / save) interval is an OPTIMISATION with a closed-form answer, not a safety dial to max out. Set the interval to τ*=√(2·C·M) where C is the snapshot cost and M the mean time between interruptions; both snapshotting more often and less often than that waste strictly more total time. Because the optimum scales as √M and the overhead floor as √(C/M), the two levers that actually move your overhead are cheaper checkpoints (smaller C) and a longer MTBF (larger M) — and improving reliability buys you overhead reduction only sub-linearly (4× the MTBF halves the overhead). Do NOT reason "more checkpoints = safer"; measure C and M and put the interval at the U's minimum, then spend engineering effort on shrinking C (incremental/async checkpoints) rather than on raising the frequency.

## Dedup
Distinct from the nearby fleet and reliability priors:
- **two-choices-routing-cliff** (P113, balanced-allocations — the max queue length under d-choice routing, a double-exponential drop at d=2): a load-balancing max-load claim about probe COUNT; this proposal has no routing, no bins, no max load — its object is the overhead of a checkpoint/restart process as a function of the checkpoint INTERVAL, minimised at √(2CM).
- **series-reliability-collapse** (P112, reliability engineering — min-of-exponentials, system MTBF T/N): P112 is about the LIFETIME of a series system (order statistics of exponentials); this proposal takes the MTBF as a GIVEN input M and asks how to schedule checkpoints against it — a scheduling optimisation, not a lifetime law, with a U-shaped overhead and a √(2CM) optimum absent from P112.
- **metastable-retry-storm-collapse** (fleet — timeout-retry load feedback / bistable congestion collapse): a load-feedback bistability about RETRIES amplifying offered load; this proposal has no retries-under-load, no congestion, no bistability — a single job's checkpoint overhead vs a fixed independent failure process, with a smooth convex (not bistable) objective.
- **correlated-fleet-variance-floor** (P109, error aggregation — N_eff→1/ρ), **delegation-loop-collapse** (P105, vote delegation), **winners-curse-task-auction** (P101, common-value auction), **braess / routing** heads: different objects (estimation MSE, delegation graph, auction bid, network routing) with no checkpoint/restart overhead structure.
- **kelly-overbet-ruin** (P100, growth-optimal bet fraction), **coupon-collector-tail** (completion cost): both have a single tunable and a closed-form optimum, but neither is a U-shaped overhead in a snapshot interval against a Poisson failure process; the checkpoint objective's two-competing-wastes structure (falling C/τ + rising τ/2M) and its √(2CM) / √(2C/M) / √M-scaling anchors match none of them.
- This proposal is **the Young–Daly optimal checkpoint interval** — the U-shaped total-overhead of a checkpoint/restart job, minimised at τ*=√(2CM) with floor √(2C/M), isolated by an over-checkpointing headline (τ*/8 wastes more), a U-shape control (τ*·8 also wastes more), and a square-root-law control (quadrupling the MTBF halves the optimum overhead at the doubled interval) — matching none of the routing, reliability-lifetime, retry-storm, aggregation, delegation, auction, bet-sizing, or collection priors.

## Model basis (declared model-dependence — the P024 discipline)
The exact Daly law `O(τ)=(M/τ)(exp((τ+C)/M)−1)−1` rests on: (a) failures are a homogeneous POISSON process (exponential, memoryless inter-failure times) — the memorylessness is what makes the expected wall per successful segment exactly `M(exp(L/M)−1)` and makes the Monte-Carlo match the closed form; a heavy-tailed or aging failure process would change the constant but not the U-shape; (b) restart cost R=0 (nonzero R shifts τ* to √(2C(M+R))-type forms — Daly's second-order — but keeps the U-shape and √-scaling); (c) checkpoint cost C is fixed per checkpoint and lost work on a crash is exactly the work since the last checkpoint (no partial-checkpoint credit). The QUALITATIVE claims — total overhead is U-shaped in τ, minimised at an interior τ*∝√(CM), with an overhead floor ∝√(C/M) that falls as 1/√M — hold for any light-tailed failure model where the two wastes are a falling C/τ and a rising τ/(2M)+O(τ²/M²) (Young's first-order argument), so the exponential choice just makes the anchor exact and the seed reproducible. The claim is scoped: for a checkpoint/restart job under Poisson failures with fixed checkpoint cost and zero restart cost, the total wasted-time fraction is U-shaped in the checkpoint interval and minimised at τ*=√(2CM) with floor √(2C/M) (Young 1974 / Daly 2006), demonstrated on the pinned constants, mechanism-explained (two competing wastes C/τ and τ/2M), not asserted as a universal law across arbitrary failure distributions.

## Probe report (v0, 2026-07-18)

**1. What is this really?** A U-shaped-optimisation claim: a checkpoint/restart job's total wasted wall time is `C/τ + τ/(2M) + …` — a falling overhead term plus a rising recompute term — so it has a unique INTERIOR optimum interval τ*=√(2·C·M) (Young 1974 / Daly 2006), and both checkpointing more often and less often waste strictly more. Controls: over-checkpointing 8× wastes more (frequent penalty **0.305502**, z=833.57), under-checkpointing 8× also wastes more (rare penalty **0.438308**, z=113.30), and quadrupling the MTBF halves the optimum overhead (**0.106933 → 0.052066**, z=80.51) — the √-law.
**2. What would make it false?** If checkpointing 8× more often did NOT waste more (G1 — a monotone "more is safer" would show a negative or sub-3σ frequent penalty), or checkpointing 8× less often did NOT waste more or the optimum overhead did NOT drop when the MTBF quadrupled (G2 — no interior U-minimum, or no √-scaling), or the measured overheads did NOT match the exact Daly closed form within 3σ (G3 — the sim isn't the checkpoint-restart law). Any → REJECT.
**3. Simplest version that still bites?** SEED=20260717, 200 runs of a W=40000 job at τ ∈ {2.5, 20, 160} under Poisson(1/200) failures; report the overhead at each and the two penalties vs the τ*=20 optimum, plus a τ=40 run at M=800 for the √-law control, against the exact Daly anchors.
**4. What is the counterintuitive core?** Checkpointing MORE often is not safer — total wasted time is U-shaped, so the optimum is interior (τ*=√(2CM)=**20**, overhead **~10.7%**), and 8× too often (**~41.2%**) is just as wasteful, in the leading order, as 8× too rarely (**~54.5%**). And a 4× more reliable machine warrants only a 2× longer interval and halves the overhead floor — reliability buys overhead reduction sub-linearly (√MTBF).
**5. Where could I be fooling myself?** The G3 anchor is the EXACT Daly closed form `O(τ)=(M/τ)(exp((τ+C)/M)−1)−1`, not the Young first-order approximation (which is why the descriptive Young 0.10 differs from the anchor 0.107106 — the sim lands at the exact model, |z|=0.5778, not the approximation); the U-shape is isolated by TWO arms (G1 frequent + G2a rare), so a one-sided "overhead falls with τ" artefact cannot pass; the √-law control (G2b) rescales the interval to τ*(4M)=2τ* so it tests the SCALING, not just "bigger M is better".
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 frequent penalty 0.305502 (se 0.000307) z=**833.57σ**; G2 rare penalty 0.438308 (se 0.003427) z=**113.30σ** and halving drop 0.054867 (se 0.000433) z=**80.51σ**; G3 opt 0.106933 vs 0.107106 |z|=**0.5778**, frequent 0.412435 vs 0.412322 |z|=**1.7438**, rare 0.545241 vs 0.545871 |z|=**0.1845** — G1/G2 clear their bars by tens-to-hundreds of σ, G3 matches the exact Daly law within 2σ; exit 0; results-dict sha256 43a77ca7…6be566a81.
**7. What decision does it change?** Set the checkpoint/snapshot interval to τ*=√(2·C·M), not "as often as affordable"; don't read more checkpoints as safer (you climb the left arm of the U); and invest in shrinking the checkpoint cost C (incremental/async snapshots) rather than raising the frequency, since the overhead floor is √(2C/M) and the optimum scales only as √M.
**8. How will we know it worked?** The committed stdlib verifier reproduces the checkpoint-overhead U-shape under SEED=20260717 with all three gates holding (G1 frequent penalty ≥0.05 by ≥3σ, G2 rare penalty ≥0.05 and halving drop ≥0.02 both by ≥3σ, G3 three overheads within 3σ of the exact Daly anchors) and the results-dict sha256 matching 43a77ca77563e81f873cd73c81d35c684a2ec48bc26d2d740b083ef6be566a81.

## One-line correction
The checkpoint interval is an optimisation, not a safety dial: put it at τ*=√(2·C·MTBF), because total wasted time is U-shaped (overhead floor √(2C/MTBF)) and BOTH over- and under-checkpointing waste strictly more — and since the optimum scales only as √MTBF, spend effort shrinking the checkpoint cost, not raising the frequency.

**Recommendation: sim-ready**
