# Fragmenting a loss-system fabric into small independent pools at the SAME offered-load-per-server MULTIPLIES blocking — a fabric of 50 two-server pools (each 0.8 offered/server) drops ~33% of calls while ONE pooled 100-server system at the identical 0.8 offered/server drops ~0.4% (Erlang-B trunking efficiency)

> **State:** sim-ready
> **Class:** fleet (unrelated / cross-cutting) · queueing / teletraffic (loss systems) · Erlang-B first-blocking probability
> **Target:** sim-lab (VERDICT 154, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@c03594b0a4b828c8c241bfad8ef38fc5cc81bd86 · fetched 2026-07-18T17:11:43Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Erlang_(unit)#Erlang_B_formula — Erlang-B loss formula, verified reachable 2026-07-18

## The phenomenon (one line)
At a fixed offered load *per server*, the fraction of calls a blocked-calls-cleared pool drops falls sharply as the pool grows — so carving one big pool into many small pools at the same utilization multiplies the loss.

## The folk belief
"Blocking is a function of utilization. Two pools each running at 80% offered load block the same fraction as one big pool at 80% — capacity is additive, so splitting a fabric into per-tenant / per-shard pools at the same utilization is free."

## The probabilistic thesis (reasoned to its fuller form — Q-0254 duty)
Model each pool as an M/M/c/c loss system: Poisson arrivals rate λ, exponential service rate μ, c servers, NO queue, blocked calls cleared. Offered load a = λ/μ Erlangs. By PASTA the probability an arriving call is blocked is the Erlang-B loss formula B(c, a) = (a^c / c!) / Σ_{k=0}^{c} a^k / k!, computed stably by B(0,a)=1, B(k,a) = a·B(k−1,a) / (k + a·B(k−1,a)). Hold the offered load PER server fixed at ρ = a/c and grow c: B(c, cρ) does not stay constant — it falls fast (trunking efficiency). At ρ = 0.8: B(2,1.6) ≈ 0.329896907, B(10,8) ≈ 0.121661064, B(100,80) ≈ 0.003992029. Same utilization, blocking drops ~90× from a 2-server pool to a 100-server pool. Equivalently, fragment a 100-server / 80-Erlang fabric (ρ=0.8) into 50 independent 2-server pools at the same ρ and the fabric's loss jumps from ~0.4% to ~33% — small pools have no statistical-multiplexing headroom to absorb coincident bursts, and each fragment independently rejects during its own local peak, so the penalty compounds rather than averaging out.

## The formal model (committed constants — sim-lab must reproduce exactly)
Event-driven M/M/c/c per replication: draw interarrival ~ Exp(λ) then service ~ Exp(μ) per arrival (two draws/arrival, that order); accept if any server's free-at time ≤ the clock, else block/clear. Empirical blocking = blocked / measured arrivals after warmup W. R independent replications; mc = mean of per-replication blocking fractions; se = sample-std / √R (an honest independent-replication standard error — within-replication autocorrelation is folded into the between-replication spread). z = (mc − anchor) / se.

## Pinned world (committed constants)
SEED = 20260717 (one random.Random(SEED) drawn sequentially in the fixed config order). μ = 1.0. SIGMA_GATE = 3.0. Offered-load-per-server ρ = 0.8 for every config. Pooled anchor L = exact B(100, 80) = 0.003992029. Configs (name, c, a, R, A, W):
- CFG_SMALL: c=2, a=1.6, R=400, A=8000, W=1500 — anchor = exact B(2,1.6)
- CFG_MED: c=10, a=8.0, R=400, A=8000, W=1500 — anchor = exact B(10,8)
- CFG_HEAD: c=2, a=1.6, R=400, A=8000, W=1500 — anchor = pooled exact B(100,80)

## Pre-registered gates (PASS iff ALL hold, in order CFG_SMALL → CFG_MED → CFG_HEAD)
1. **CFG_SMALL verifier-correctness** — MC blocking of a 2-server pool matches exact B(2,1.6) within |z| < 3.
2. **CFG_MED verifier-correctness** — MC blocking of a 10-server pool matches exact B(10,8) within |z| < 3, already far below CFG_SMALL at the identical 0.8 offered-load-per-server (the trunking gradient is real, not a sim artifact).
3. **CFG_HEAD counterintuitive headline (z ≥ 3)** — a 2-server fragment's MC blocking sits z ≥ 3 ABOVE the pooled-fabric prediction L = exact B(100,80): the folk "same-utilization → same-blocking" guess understates a fragment's loss by dozens of σ (~90× in level).

## Pre-registered decision rule
APPROVE VERDICT 154 iff sim-lab reproduces ideas/fleet/erlang_b_trunking_efficiency.py byte-identical under SEED=20260717, the results-dict sha256 matches EXACT, and all three gates PASS in order, exit 0 across a deterministic double-run. Else REJECT.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
CFG_SMALL  c=2   a=1.6  mc=0.330324 anchor=0.329897 (exact_B(2,1.6)) z=+1.194 PASS
CFG_MED    c=10  a=8    mc=0.122158 anchor=0.121661 (exact_B(10,8)) z=+1.377 PASS
CFG_HEAD   c=2   a=1.6  mc=0.329770 anchor=0.003992 (pooled_exact_B(100,80)) z=+959.483 PASS
all_gates_pass = True
```
Two CLI runs byte-identical + in-process double-run assertion, exit 0. **Disclosed results-dict sha256 = a9556fa032f268407b136f9aa0d93bdb936f26bd1eb2d609b019e9d60959173a** (sha of the compact canonical json.dumps(sort_keys=True,separators=(",",":")) of the whole results dict; WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY — no self-referential sha field, no on-disk JSON).

## Verifier
Stdlib-only reference: `ideas/fleet/erlang_b_trunking_efficiency.py` (random, json, hashlib). Reproduce: `python3 ideas/fleet/erlang_b_trunking_efficiency.py`. Expected: the three gate lines above, `all_gates_pass = True`, the pretty results dump, `Results-JSON sha256: a9556fa032f268407b136f9aa0d93bdb936f26bd1eb2d609b019e9d60959173a`, exit 0.

## Why it matters (cross-cutting)
Every bounded no-queue resource in the fleet is a loss system: connection pools that reject on exhaustion, fixed thread pools that drop overflow, per-tenant rate-limit token buckets, reserved-capacity worker fabrics. The trunking law says the instinct to isolate — a pool per tenant, per shard, per lane — is not free: at matched utilization, many small isolated pools drop dramatically more work than one shared pool of the same total size. Consolidation buys statistical-multiplexing headroom; isolation buys blocking. Because the cost is Erlang-B and quantifiable up front, isolation can be traded against its blast-radius benefit deliberately instead of paid by surprise under a coincident burst.

## Dedup
- **checkout-pooling-single-line (2026-07-13)** — a DELAY system (M/M/c queue, Erlang-C): calls WAIT, the metric is expected wait / queue length. This is a LOSS system (M/M/c/c, Erlang-B): calls are DROPPED, no queue, the metric is blocking probability. Different formula (B vs C), different object.
- **service-variance-wait-tax (P137)** — M/G/1 waiting-time inflation from service-time VARIANCE (Pollaczek–Khinchine), single-server delay. This is multi-server LOSS with exponential service; the effect is pool-SIZE-driven at fixed utilization, not variance-driven.
- **variance-blind-provisioning-trap (2026-07-16)** — provisioning under demand variance. This is the exact steady-state loss law of a fixed pool, not a provisioning-under-uncertainty argument.
- **two-choices-routing-cliff** — load balancing / max-load of balls-in-bins (assignment imbalance). Different object: admission loss, not placement imbalance.

## Model basis (declared model-dependence — the P024 discipline)
The headline is exact for M/M/c/c (Poisson arrivals, exponential service, blocked-calls-cleared). Erlang-B is famously insensitive to the service-time DISTRIBUTION (it depends only on the mean; holds for M/G/c/c), so the loss-level claim generalizes; it does NOT hold if blocked calls RETRY (blocked-calls-held raises effective load) or if arrivals are strongly bursty (super-Poisson) — both make real fragmentation penalties LARGER, not smaller, so the pooled-vs-fragmented direction is conservative.

## Probe report (v0, 2026-07-18)
**1. What is this really?** The steady-state loss probability of a finite no-queue server pool (Erlang-B) as a function of pool size at fixed utilization — economy of scale in admission.
**2. What would make it false?** If B(c, cρ) were flat in c at fixed ρ. It is not: the recursion drives B down as c grows. A sim showing constant blocking across CFG_SMALL/MED would refute it.
**3. Simplest version that still bites?** Two servers vs ten at 80% offered load: ~33% dropped vs ~12% dropped — same utilization, from pool size alone.
**4. Counterintuitive core?** Utilization does NOT determine blocking; pool size at fixed utilization does. Isolation into small pools is a hidden, compounding loss even when every pool runs at a "safe" load.
**5. Where could I be fooling myself?** Single-trajectory autocorrelation would understate the error bar — handled by independent replications with a between-replication se. Warmup transient could bias blocking low — handled by discarding W arrivals. The sim must reproduce EXACT Erlang-B, which gates 1–2 enforce.
**6. Honest calibration?** High confidence: Erlang-B is a century-old exact result; the only claim under test is that the committed simulator reproduces it and that the fragmented level sits dozens of σ above the pooled anchor.
**7. What decision does it change?** Whether to shard a bounded resource into per-tenant/per-lane pools. The trunking law prices isolation: below a pool size, isolation's blocking cost dominates its blast-radius benefit.
**8. How will we know it worked?** sim-lab reproduces the verifier byte-identical, the sha256 matches, all three ≥3σ gates PASS in order, exit 0 on a deterministic double-run.

## One-line correction
Blocking is set by pool SIZE at a given utilization, not by utilization alone — so splitting a fabric into small same-utilization pools multiplies the calls it drops.

**Recommendation: sim-ready**
