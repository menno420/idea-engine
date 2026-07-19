# Scheduling a single-server dispatch queue is zero-sum: no work-conserving discipline can lower the load-weighted mean wait

> **State:** sim-ready
> **Class:** counterintuitive-invariant / fleet-ops (dispatch + scheduling)
> **Slot:** round-36 fleet
> **Target:** sim-lab (VERDICT 166, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine/blob/6a29f119a6ca13c7c1e112c373ce8e8da337cf27/control/outbox.md@05c6e63d399bceed50b337b4a884a74eea0a05b3 · fetched 2026-07-19T03:52:21Z
> **Reference (external, reachable):** L. Kleinrock, "A conservation law for a wide class of queueing disciplines," Naval Research Logistics Quarterly 12(2):181-192 (1965); "Queueing Systems, Volume II: Computer Applications" (1976), sec. 3.3-3.4. Secondary (reachable): Wikipedia "M/G/1 queue" — https://en.wikipedia.org/wiki/M/G/1_queue (Pollaczek-Khinchine mean value + work conservation).
> **Harvest source (firsthand):** ideas/fleet/kleinrock_conservation_zero_sum.py + its recorded double-run (this branch).

## The phenomenon (one line)
In a single-server queue where the server never idles while work waits, you can reorder WHO waits however you like — but the load-weighted average wait sum_i rho_i W_i is fixed; make one class faster and another gets compensatingly slower.

## The folk belief
"Add a smart priority rule and the whole fleet gets faster." A dispatcher that pushes short jobs to the front feels like a free win — short jobs finish sooner and nobody notices the bill. The intuition treats mean wait as something scheduling can shrink. It cannot: at a fixed offered load, non-preemptive work-conserving scheduling is a zero-sum transfer.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Single server, Poisson arrivals split into two classes: short jobs (mean service S1) and long jobs (mean service S2 >> S1). Class load rho_i = lambda_i * E[S_i]; total load rho = rho1 + rho2 < 1. Kleinrock's conservation law for the M/G/1 queue under ANY non-preemptive, work-conserving discipline:

    sum_i rho_i W_i = (rho / (1 - rho)) * W_0,    W_0 = sum_i lambda_i * E[S_i^2] / 2.

The right-hand side is built only from arrival rates and service moments — it contains no scheduling choice. So the load-weighted mean wait is an invariant of the workload, not of the policy. Workload view: with the same arrivals and service times, the unfinished-work backlog of a work-conserving server is essentially pathwise identical across disciplines — the server always has the same work to burn down; a discipline only permutes the order in which that fixed backlog is charged to classes. Hence, comparing FIFO to priority-to-short:

    rho1 * (W1_fifo - W1_short) = rho2 * (W2_short - W2_fifo).

The load-weighted wait short jobs SAVE under priority-to-short equals, sign-for-sign, the load-weighted wait long jobs PAY. FIFO sits in the middle; priority-to-long is the mirror image. Every discipline lands on the same sum_i rho_i W_i.

## Pinned world (committed constants — the verifier is the contract)
SEED=20260717 · single server · classes {short S1=1.0, long S2=8.0} · P(short)=0.80 · utilization rho=0.85 (=> lambda=0.354167, rho1=0.283333, rho2=0.566667 — the 20%-of-arrivals long jobs carry two-thirds of the load) · N_JOBS=20000 per replication · WARMUP=4000 discarded completions · R_REPS=30 · disciplines FIFO / PRIO_SHORT / PRIO_LONG run on a COMMON arrival+service realization (common random numbers). Shifted (robustness) world: P(short)=0.60, S2=6.0, rho=0.80.

## Pre-registered gates (evaluation order G1 → G2 → G3; APPROVE iff ALL hold)
- **G1 — scheduling really moves wait (the transfer is real and large).** transfer_short = rho1*(W1_fifo - W1_short) > 0 at z >= 3 vs null 0. Observed transfer_short_mean = **+7.450148**, z = **+30.100904**. Underlying swing: W1 33.088966 → 6.794325 (a 4.87x cut for short jobs); W2 33.186088 → 46.364871 (+39.7% for long jobs).
- **G2 — the saving is paid back (conservation holds).** the leak |transfer_short - transfer_long| / transfer_short stays below 0.10 at z >= 3 below the ceiling. Observed leak_mean = **0.040689**, z = **+12.680569** — at least 95.9% of the load-weighted short-job saving reappears as long-job wait.
- **G3 — robust to a shifted class mix and utilization.** under P(short)=0.60, S2=6.0, rho=0.80, the same leak stays below 0.10 at z >= 3. Observed shift_leak_mean = **0.023037**, z = **+23.740077**.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold on a clean-room re-run (SEED=20260717) with the results-dict sha256 matching. Any gate false → REJECT naming first_failing_gate. Observed all_pass = **true**, first_failing_gate = **null**. Direct invariance readout (averaged over reps): sum_i rho_i W_i = 28.180657 (FIFO) / 28.198485 (priority-short) / 28.177276 (priority-long) — a max-to-min spread of 0.021 (~0.08%) while W1 swings 4.87x.

## Disclosed verifier (the sim-lab spec)
`ideas/fleet/kleinrock_conservation_zero_sum.py` — stdlib only (hashlib, json, math, random, collections.deque). Discrete-event single-server simulator; each discipline runs on the SAME (arrival, class, service) stream; per-class mean waits measured after warmup; z-tested across 30 replications. Posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY — builds the ordered results dict, asserts an in-process double run is byte-identical, prints the pretty dict and its sha256. Expected results-dict sha256:

    1b40af51baa24c2041bbd822b190e5447c6299840604822580b3b3bb3153ee18

Re-run twice cross-invocation; both must print IDENTICAL output and the sha256 above; exit 0 iff all_pass.

## Why it matters
Fleet dispatch tuning is sold as a throughput win, but at fixed load it is a redistribution, not a reduction: a "fast lane" for short jobs is paid for, to the load-weighted cent, by everything else in the queue. The levers that actually lower sum_i rho_i W_i are not scheduling — they are cutting rho (more capacity), cutting service variance (W_0 shrinks), or shedding load. Conservation is why chasing SLAs by re-prioritizing feels like whack-a-mole: the aggregate wait is pinned, so every class you rescue surfaces the delay somewhere else. It bounds what any dispatcher can promise and prices, load-weighted, exactly what a priority policy costs the jobs it deprioritizes.

## Dedup (contrast vs prior lane heads)
- vs **service-variance-wait-tax / erlang-b-trunking / two-choices-routing / fan-out-tail** — those lower wait by changing capacity, variance, or routing (they move W_0 or rho). Conservation is orthogonal: at FIXED load and variance it says the DISCIPLINE cannot move the aggregate at all. Different axis (order, not resources).
- vs **round-robin-domain-starvation-cliff** — that shows one policy starving a class; conservation is the general invariant that EXPLAINS why relief for one class must starve another.
- vs **inspection-paradox-wait-inflation** — a sampling/measurement bias in observed gaps; this is a scheduling invariant on true waits.
- vs **braess-paradox (P152)** — Braess: adding capacity worsens the selfish equilibrium (topology lever). Conservation: reordering service cannot change aggregate wait (scheduling lever). Both "you can't win," different mechanism and lever; no equilibrium/routing overlap.
- Crossover honesty: conservation is adjacent to any "no free lunch in scheduling" framing, but no prior fleet head states or tests the rho-weighted invariant across disciplines. Distinct.

## Model basis (declared model-dependence — the P024 discipline)
Exact given the model: single server, Poisson arrivals, non-preemptive work-conserving disciplines, finite class service moments. Dependence disclosed honestly: (1) PREEMPTIVE disciplines (e.g. preemptive-resume SRPT) break the non-preemptive form and CAN lower mean wait — conservation as stated is a non-preemptive law; (2) non-work-conserving policies (deliberate idling) sit outside it; (3) it is a steady-state MEAN statement — finite-sample transients leave a residual leak (the ~4% G2 leak is Monte-Carlo noise around the exact 0, not a violation, and it shrinks with N_JOBS). The SIGN and the invariance are structural for the non-preemptive work-conserving class; the small leak is finite-run, disclosed, and bounded by G2/G3.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | z | Verdict |
|------|------|-----------|----------|---|---------|
| G1 | transfer real | mean > 0, z>=3 | +7.450148 | +30.100904 | PASS |
| G2 | conservation | leak < 0.10, z>=3 | 0.040689 | +12.680569 | PASS |
| G3 | robustness | shift leak < 0.10, z>=3 | 0.023037 | +23.740077 | PASS |

## Probe report (v0, self-adversarial)
**1. Real invariance or one lucky arrival stream?** Measured across 30 independent replications, each a fresh seeded arrival+service realization; the conserved sum coincides to ~0.08% every time while W1 swings 4.87x. Not one stream.
**2. Is priority-to-short actually non-preemptive and work-conserving?** Yes — the server picks the next job only when it frees (no preemption) and never idles while any job waits (work-conserving). Both priority disciplines meet the law's hypotheses; a preemptive SRPT would not, and is explicitly out of scope.
**3. Could the ~4% leak be a hidden violation?** No — conservation is a steady-state mean identity; on a finite path the empirical rho-weighted sums differ by Monte-Carlo noise. G2 bounds that noise below 10% at z=12.7, and common random numbers already suppress it (the three disciplines share one workload).
**4. z inflated by huge N?** The z's come from R=30 replications (n=30 per z-test), not from N_JOBS. G1's large z reflects a large, stable transfer; G2/G3's reflect a leak sitting well below the 0.10 ceiling with small spread.
**5. Rigged constants?** Textbook two-class M/G/1 (short S1=1, long S2=8, 80/20 split, rho=0.85). The load split (20% of jobs = two-thirds of load) is a consequence of S2 >> S1, not a tuned knob. G3 re-runs under a different mix and utilization.
**6. Determinism?** SEED pinned; in-process double run asserted byte-identical; cross-invocation double run printed IDENTICAL with sha256 1b40af51... A verdict re-run must reproduce that digest.
**7. Real phenomenon or toy?** Kleinrock's conservation law (1965 / 1976) is a load-bearing queueing result used to bound what dispatch policies can achieve; the reflex it corrects — "a priority rule speeds up the fleet" — is exactly the folk belief above.
**8. Float ordering perturbing the digest?** All dict floats round()-ed to 6 dp before hashing; sums taken in fixed replication order; deque operations deterministic. The in-process assert catches drift.

**Recommendation: sim-ready**
