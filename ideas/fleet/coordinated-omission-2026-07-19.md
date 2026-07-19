# PROPOSAL 149 — Coordinated omission: a closed-loop / synchronous load generator waits for each request to return before issuing the next, so during a service stall it has exactly ONE request outstanding and CANNOT send the requests it was scheduled to send — it silently OMITS the coordinated backlog those requests would have measured. The reported latency distribution is biased LOW by orders of magnitude: the closed loop records ~1 inflated sample per stall where the true user experience is a pile-up of ~D/tau backlogged requests, so the p99/p99.9 it prints is set by the MEASUREMENT METHOD, not the system under test. An HdrHistogram-style CO-correction (back-fill the omitted samples) lifts the measured tail back toward the open-loop truth.

> **State:** sim-ready
> **Class:** fleet (unrelated / cross-cutting) · performance measurement (load-generation artifact) · coordinated omission — closed-loop tail blindness + HdrHistogram back-fill correction · PROPOSAL 149
> **Target:** sim-lab (VERDICT 162, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine/blob/c49830ddd7defc2e9f104380961d2b48635b5f15/ideas/fleet/coordinated_omission.py@d276fb5047473a5bc569f8747c1dd7a04311bbc5 · fetched 2026-07-19
> **Reference (external):** coordinated omission — Gil Tene (HdrHistogram author), "How NOT to Measure Latency" / "Your Load Generator Is Probably Lying to You"; the CO-correction back-fill is HdrHistogram's `recordValueWithExpectedInterval(value, expectedInterval)`, which synthesises the samples a coordinated (evenly-paced) load would have recorded during a stall.
> **Verifier (firsthand):** `ideas/fleet/coordinated_omission.py` · file sha256 `6780d06a213ad27d218331447bb922898a1eb8aa716396bf343590c16eda762c` · git blob `d276fb5047473a5bc569f8747c1dd7a04311bbc5` · 323 lines · results-dict sha256 `12d3ce4fce9a4f1cc218be0ee6f5dbc945d42a5e45173a46044704524dbfab5d`
> 📊 Model: Claude Opus · high · idea/planning

## Domain

Performance measurement — the load generator itself, not the system under test. One single-server FIFO system is measured two ways over the SAME stall schedule and the SAME per-request service times: an OPEN-LOOP measurement (arrivals happen on a fixed schedule regardless of completions — the ground truth of what a user experiences) and a CLOSED-LOOP measurement (a synchronous load generator with exactly one request outstanding — the common but flawed benchmark harness). The question is the one every latency dashboard implicitly asks: *is the p99 my load test printed the p99 my users actually feel?*

## The folk belief

"My load generator drives the system at rate λ and records every request's latency, so the p99/p99.9 it reports IS the tail my users experience. If the system stalls, the benchmark will see the stall — the high latencies show up in the histogram. A closed-loop harness (fire a request, wait for the response, fire the next) is a faithful sampler of the latency distribution." Every synchronous benchmark loop — `for (i=0;i<N;i++){ t=now(); doRequest(); record(now()-t); }` — rests on this intuition.

## The thesis (reasoned to its fuller form — Q-0254 duty)

The closed-loop harness is NOT a faithful sampler. It waits for each request to return before issuing the next, so it can only ever have ONE request outstanding. When the system stalls for a duration D, the harness fires exactly one request, that request blocks for the whole stall, and the loop is stuck — it issues NOTHING else until the stall clears. It therefore records ONE inflated sample of size ~D and then resumes. But a system driven at the intended rate λ (inter-arrival τ = 1/λ) should have received ~D/τ requests during that stall — and every one of them would have queued behind the stall and experienced a large latency. The closed loop **omits** all of them. This is **coordinated omission**: the missing samples are precisely the ones that would have measured the tail, and they are missing *because* the load generator's pacing is coordinated with (backs off during) the very stalls it is meant to measure.

The consequence is a tail biased LOW by orders of magnitude:

- The open loop sees a **backlog** of ~D/τ requests per stall, with latencies spread from ~0 up to ~D. A large fraction of all requests land in this elevated band, so the p99 sits deep in the stall tail (~D).
- The closed loop sees ~1 inflated sample per stall, drowned among the vastly more numerous fast between-stall samples. Those few large samples fall ABOVE the 99th percentile (they are <1% of the closed samples), so the closed p99 is set by the *fast* path (~sub-millisecond) — it never sees the tail at all.
- The gap is a property of the MEASUREMENT METHOD, not the system: both loops ran on the identical server, identical stalls, identical service times. Only the pacing (open vs synchronous) differs, and that alone moves the reported p99 by ~100×.

The **CO-correction** (HdrHistogram's back-fill) recovers the omitted samples analytically. For each recorded closed sample L that exceeds the expected interval τ, it synthesises the samples a coordinated load would have recorded — L−τ, L−2τ, … down to > τ — and unions them with the originals. Those synthetic samples repopulate the elevated band, lifting the corrected p99 back toward the open-loop truth.

## The trap

Any latency SLO signed off from a closed-loop benchmark ("p99 = 0.5 ms, ship it") is reading the measurement artifact, not the user experience. Under a stall the true p99 is ~D (here ~100× larger). The harness will (i) certify a system whose real tail violates the SLO, and (ii) hide the exact pathology — GC pauses, JVM safepoints, lock convoys, cron-driven stalls, failover freezes — that load tests exist to catch, because those pauses stall the harness in lockstep. The correct controls are an **open-loop / constant-arrival load generator** (decouple issue time from completion time) or an **HdrHistogram-style CO-correction** on the closed-loop samples.

## Formal model (committed constants — sim-lab must reproduce exactly)

Single-server FIFO, one underlying system. Pinned world: **SEED = 20260717**, R = 200 independent replicates; replicate i draws from `random.Random(SEED + i)`. λ = 1000 → τ = 1 ms; horizon T = 1.0 s; base service time i.i.d. Exp(mean μ_s = 0.1 ms) so utilisation μ_s/τ = 0.1 (low); n_stalls = 6 stalls of duration D = 50 ms (D/τ = 50 ≫ 1), at per-replicate non-overlapping offsets (one per equal cell of [0,T], shared by both loops). The server is FROZEN during each stall. Both loops consume the SAME per-replicate service-time list (N_svc = 12000 pre-drawn values), request i using service time i.

- **OPEN-LOOP:** arrivals at fixed times k·τ; each queues at arrival; FIFO; latency_i = completion_i − arrival_i.
- **CLOSED-LOOP:** dispatch_0 = 0; dispatch_{i+1} = completion_i (one outstanding); latency_i = completion_i − dispatch_i.
- **CO-CORRECTION:** for each closed sample L > τ, back-fill L−τ, L−2τ, … down to > τ; union with the originals.

Per replicate: p99 (nearest-rank, q = 0.99) of {open, closed, corrected} latencies, and the count of requests whose in-system interval overlaps a stall window (the coordinated backlog) for open vs closed. z = mean/se across replicates, se = sample-std/√R, tested against H0 mean 0.

## Pre-registered gates (ordered; each z = mean/se, one pinned SEED; require z ≥ 3.0)

| Gate | Statistic | Claim | Pass rule |
|---|---|---|---|
| **G1** tail-blindness | z = mean( log(open_p99 / closed_p99) ) / se | the closed-loop p99 understates the open-loop p99 (the measured tail is blind to the real tail) | z ≥ 3 |
| **G2** omitted-backlog | z = mean( open_stall_count − closed_stall_count ) / se | the open loop carries ~D/τ backlogged requests per stall that the closed loop omits (~1 per stall) | z ≥ 3 |
| **G3** correction-recovery | z = mean( log(corrected_p99 / closed_p99) ) / se | the HdrHistogram-style CO-correction lifts the measured tail back up toward the truth | z ≥ 3 |

Descriptive companion to G3: mean recovery fraction (corrected_p99 − closed_p99)/(open_p99 − closed_p99).

## Pre-registered decision rule

APPROVE VERDICT 162 iff sim-lab reproduces `ideas/fleet/coordinated_omission.py` byte-identical under SEED = 20260717, the results-dict sha256 matches EXACT, and all three gates PASS in order across a deterministic double-run, exit 0. Else REJECT.

## Dry-sim results (SEED = 20260717, verbatim from the committed verifier)

```
G1 tail-blindness    : mean log(open/closed p99)=+4.6433 z=+2505.7334 PASS
G2 omitted-backlog   : mean(open-closed stall count)=+294.6350 z=+5148.2784 PASS
G3 correction-recov  : mean log(corr/closed p99)=+4.4086 z=+2606.6706 PASS
recovery fraction    : 0.7888  (open p99 0.048583  closed p99 0.000468  corr p99 0.038420)
all_pass = True  first_failing_gate = None
{
  "all_pass": true,
  "config": {
    "D_over_tau": 50.0,
    "horizon_T": 1.0,
    "lam": 1000.0,
    "mu_service": 0.0001,
    "n_stalls": 6,
    "n_svc": 12000,
    "percentile_q": 0.99,
    "replicates": 200,
    "seed": 20260717,
    "stall_D": 0.05,
    "tau": 0.001,
    "utilisation": 0.1,
    "z_gate": 3.0
  },
  "descriptive": {
    "mean_closed_p99": 0.000468,
    "mean_closed_stall_count": 6.0,
    "mean_corrected_p99": 0.03842,
    "mean_open_over_closed_p99": 103.855766,
    "mean_open_p99": 0.048583,
    "mean_open_stall_count": 300.635,
    "mean_recovery_fraction": 0.788774
  },
  "first_failing_gate": null,
  "gates": {
    "G1_tail_blindness": {
      "mean": 4.643332,
      "pass": true,
      "se": 0.001853,
      "statistic": "mean log(open_p99/closed_p99)",
      "z": 2505.733369
    },
    "G2_omitted_backlog": {
      "mean": 294.635,
      "pass": true,
      "se": 0.05723,
      "statistic": "mean (open_stall_count - closed_stall_count)",
      "z": 5148.278412
    },
    "G3_correction_recovery": {
      "mean": 4.408601,
      "pass": true,
      "se": 0.001691,
      "statistic": "mean log(corrected_p99/closed_p99)",
      "z": 2606.670555
    }
  },
  "mechanism": "coordinated-omission",
  "proposal": 149
}
Results-JSON sha256: 12d3ce4fce9a4f1cc218be0ee6f5dbc945d42a5e45173a46044704524dbfab5d
```

All three gates PASS in order; exit 0; the second run reproduces the identical sha256. The closed loop reports p99 ≈ 0.47 ms while the true open-loop p99 is ≈ 48.6 ms — a **~104× understatement** (mean_open_over_closed_p99 = 103.86) produced by the pacing alone. The open loop carries ~300 backlogged requests across the 6 stalls (~50 = D/τ each) where the closed loop carries ~6 (one frozen sample per stall); the difference is 294.6 at z ≈ 5148σ. The CO-correction lifts the measured p99 from 0.47 ms to 38.4 ms — recovery fraction 0.79 of the way back to the open-loop truth — at z ≈ 2607σ.

## Reproduce

```
python3 ideas/fleet/coordinated_omission.py
```

Expected: the three gate lines above, `all_pass = True`, `first_failing_gate = None`, the pretty results dump, `Results-JSON sha256: 12d3ce4fce9a4f1cc218be0ee6f5dbc945d42a5e45173a46044704524dbfab5d`, exit 0. **Done-when: a deterministic double-run reproduces the results-dict sha256 `12d3ce4fce9a4f1cc218be0ee6f5dbc945d42a5e45173a46044704524dbfab5d` byte-for-byte.**

## Verifier

`ideas/fleet/coordinated_omission.py` — stdlib only (`hashlib, json, math, random`), 323 lines, file sha256 `6780d06a213ad27d218331447bb922898a1eb8aa716396bf343590c16eda762c`, git blob `d276fb5047473a5bc569f8747c1dd7a04311bbc5`. Builds one FIFO server with a per-replicate stall schedule and service-time list, runs the open and closed loops over the identical inputs, applies the HdrHistogram-style back-fill correction to the closed samples, and computes the three ordered z-gates (tail-blindness, omitted-backlog, correction-recovery). Emits the whole results dict (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY, P127+ twist: no self-referential sha field, every float rounded to 6 dp, the compact canonical serialization's sha256 IS the disclosed digest, the stdout dump is pretty indent=2), writes no JSON to disk, and asserts an in-process double-run byte-identity. Exit 0 iff all three gates pass.

## Fleet relevance

The fleet benchmarks latency constantly: task-completion times, CI step durations, tool-call round-trips, agent-loop iteration latency, queue-drain times. Almost every naive harness is closed-loop — issue a call, await the result, issue the next — which means every one of them is blind to exactly the pauses the fleet most needs to catch: a GC/safepoint freeze, a rate-limit backoff, a failover, a cron-driven stall, a lock convoy. The transferable rule: **a closed-loop / synchronous load generator cannot measure the tail it stalls in; its p99/p99.9 is set by the measurement method, not the system, and understates the truth by orders of magnitude during any stall.** Guard it by (i) driving load open-loop / constant-arrival (decouple issue time from completion time), or (ii) applying an HdrHistogram-style coordinated-omission correction to the recorded samples. Either restores the tail; a bigger sample count or more warm-up does NOT.

## Why it matters (beyond the fleet)

Coordinated omission is why a JMeter/wrk/ab run can report a 2 ms p99 on a service that freezes for 100 ms every few seconds — the harness backs off in lockstep with the freeze and never records the backlog. It is the reason Gil Tene built HdrHistogram's expected-interval correction and gave the "How NOT to Measure Latency" talk. The same artifact corrupts any synchronous benchmark: database driver latency tests, RPC p99 dashboards, browser synthetic monitors that wait for one page before loading the next. The fix is architectural, not statistical: measure open-loop, or correct for the omission — never trust a closed-loop tail.

## Dedup

Distinct from the two nearest fleet heads, both of which are QUEUEING LAWS about a *real* system property; this is a MEASUREMENT ARTIFACT about the *load generator*:

- **inspection-paradox-wait-inflation (2026-07-14)** — the inspection paradox: a randomly-arriving observer is more likely to land in a LONG inter-event gap, so the *sampled* wait is length-biased upward. That is a property of unbiased sampling of a real interval-length distribution (the waits are genuinely inflated for the sampler). Coordinated omission is the OPPOSITE failure and about a different actor: the load generator's pacing is NOT unbiased — it deterministically *stops sampling* during the long events, so the tail is biased DOWN by omission, not up by length-bias. Inspection-paradox inflates what you measure; coordinated omission deletes what you should have measured.

- **service-variance-wait-tax (2026-07-18)** — a queueing law (Pollaczek–Khinchine): service-time VARIANCE inflates the true mean WAIT even at fixed utilisation; the waits it describes are real and experienced. Coordinated omission is not a queueing law and does not change any true latency — the open-loop latencies here ARE the P-K-style truth; the phenomenon is that a closed-loop *measurement* of that same truth omits the tail. One is "the system's real wait is larger than you think" (a property of the system); the other is "your measurement of the wait is smaller than it is" (a property of the instrument).

A grep of `ideas/` and `control/` at HEAD for "coordinated omission" / "coordinated-omission" returned zero prior heads; this head takes the round-35 FLEET slot.

## Model basis (declared model-dependence — the P024 discipline)

The result is exact for the standard coordinated-omission abstraction: a synchronous (one-outstanding) load generator on a server with stalls, versus a fixed-schedule open-loop drive of the same server. Declared choices, flagged not hidden: (i) the server is modelled as FROZEN for a fixed stall duration D — the classic pause abstraction (GC/safepoint/failover); relaxing it to a load-dependent slowdown only makes the open-loop backlog LARGER, deepening the gap, so the closed-loop understatement is conservative. (ii) Base service is Exp(μ_s) at low utilisation so the between-stall path is fast and the closed loop's few inflated samples stay above its own p99 — this is what makes the closed p99 blind; at higher base utilisation the closed loop still omits the backlog but its baseline rises, and the open-vs-closed p99 gap persists as long as D ≫ τ. (iii) The CO-correction uses expected-interval τ = 1/λ, exactly HdrHistogram's `recordValueWithExpectedInterval`; the recovery fraction (~0.79) is a descriptive quantity, not gated — G3 only asserts the correction lifts the tail significantly (log(corrected/closed) ≫ 0), which holds for any D ≫ τ. Neither choice changes the SIGN or the order-of-magnitude of the tail understatement.

## Probe report (v0, 2026-07-19)

**1. Is the mechanism genuinely new against the fleet backlog?** Yes — it is a MEASUREMENT artifact (the load generator's pacing), not a queueing law about a real system property. The two nearest heads (inspection-paradox-wait-inflation, service-variance-wait-tax) both describe real waits; coordinated omission describes a mis-measurement of waits that are unchanged. A grep for "coordinated omission" at HEAD returned zero prior heads.

**2. Do all pre-registered gates PASS in order on the /se margin?** Yes — G1 tail-blindness z = +2505.7, G2 omitted-backlog z = +5148.3, G3 correction-recovery z = +2606.7, all ≫ 3.0, in order, at SEED 20260717.

**3. Does the digest reproduce EXACTLY and deterministically?** Yes — both CLI runs and the in-process double-run assertion produce results-dict sha256 `12d3ce4fce9a4f1cc218be0ee6f5dbc945d42a5e45173a46044704524dbfab5d`; every float rounded to 6 dp, replicate i seeded `random.Random(SEED + i)`, exit 0.

**4. Real or a coding artifact?** Real — it is coordinated omission (Gil Tene / HdrHistogram). Both loops run on the byte-identical server, stall schedule, and service-time list; only the pacing differs, and that alone drives the ~104× p99 gap. The CO-correction (HdrHistogram's expected-interval back-fill) recovers ~79% of the gap analytically.

**5. Could the gap be a seed fluke?** No — 200 independent replicates, the tail-blindness ratio clears at z ≈ 2506σ and the omitted-backlog difference at z ≈ 5148σ; se on the log-ratio is ~0.0019.

**6. Why understated and not overstated?** Because the closed loop STOPS issuing during a stall (one request outstanding, blocked), so the ~D/τ requests that should have queued behind the stall are never sampled; the few inflated samples it does record are <1% of its total samples and fall above its own p99, so its reported p99 is set by the fast between-stall path.

**7. What breaks it — i.e. what removes the artifact?** Driving load open-loop (fixed-schedule arrivals, decoupling issue time from completion time) or applying the HdrHistogram CO-correction. Both are demonstrated: the open loop IS the truth, and the correction lifts the closed p99 from 0.47 ms to 38.4 ms.

**8. Actionable?** Yes — any fleet latency SLO signed off from a synchronous/closed-loop harness must be re-measured open-loop or CO-corrected before it is trusted; a closed-loop tail is not evidence about the user-experienced tail during any stall.

Ship to sim-lab for VERDICT 162 (P149 → V162, +13). One counterintuitive result (a ~104× tail understatement from pacing alone, on a system whose latencies are unchanged), one published anchor (coordinated omission / HdrHistogram, Gil Tene), three ordered ≥3σ gates (tail-blindness, omitted-backlog, correction-recovery), a deterministic committed verifier.

**Recommendation: sim-ready**
