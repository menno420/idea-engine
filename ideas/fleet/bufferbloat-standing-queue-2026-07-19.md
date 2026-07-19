# PROPOSAL 185 — Bufferbloat's standing queue: on a saturated server, ENLARGING the buffer grows latency ~linearly in K while goodput stays pinned at μ — a bigger buffer buys delay, not throughput

> **State:** sim-ready
> **Class:** fleet (cross-cutting) · queueing / buffer sizing · bufferbloat (standing-queue latency)
> **Slot:** round-44 FLEET
> **Anchor:** On a saturated FCFS server (offered load ρ = λ/μ > 1) the finite buffer K sits essentially full, so by Little's law mean sojourn W ≈ (K − ρ/(ρ−1))/μ grows ~linearly in K while throughput stays pinned at μ. The extra buffer is a permanent standing queue: pure latency, zero goodput.
> **Target:** sim-lab (VERDICT 198, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Bufferbloat@b060bda448fe039b88d48c76235f82ecefac8d80 · fetched 2026-07-19T21:43:29Z
> **Reference (external, reachable):** Wikipedia "Bufferbloat" (revid 1354864082), raw wikitext fetched live 2026-07-19T21:43:29Z (19446 bytes, sha1 b060bda448fe039b88d48c76235f82ecefac8d80), states verbatim: "In a first-in first-out queuing system, overly large buffers result in longer queues and higher latency, and do not improve network throughput." Gettys & Nichols, "Bufferbloat: Dark Buffers in the Internet", ACM Queue 9(11), 2011 — cited on the live page, the standing-queue/latency-without-throughput law the mechanism rests on is the part verified live.
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
Take a server that is already saturated and give it a bigger queue: mean latency rises in near-exact proportion to the added buffer, and the throughput does not move at all. Buffer you added becomes backlog you carry.

## The folk belief
"Bigger buffers absorb bursts, so more buffer is safer — worst case you trade a little memory for fewer drops." Under sustained saturation there is no burst to absorb: the buffer fills once and stays full, and every added slot is a customer that every later customer must wait behind. You bought latency and called it headroom.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Model a single FCFS server as M/M/1/K: Poisson arrivals rate λ, exponential service rate μ, finite system capacity K (in service + waiting); arrivals that find K in the system are dropped. Run it saturated, ρ = λ/μ > 1. Because offered load exceeds capacity, the occupancy pins near the ceiling: P(system full) → 1 and P(idle) → 0, so the server is busy essentially always and the departure rate (goodput) → μ regardless of K. Little's law on the finite system gives L = λ_eff · W with λ_eff = μ, and the deep-overload occupancy is L ≈ K − ρ/(ρ−1); hence W ≈ (K − ρ/(ρ−1))/μ. Two consequences fall out: (1) W is affine in K with slope 1/μ — doubling the buffer nearly doubles the wait; (2) throughput is flat at μ — the added buffer moves no extra work. The buffer converts one-for-one into standing queue. This is bufferbloat: the delay is not congestion you can drain, it is capacity you permanently occupy.

## The formal model (committed constants — sim-lab must reproduce exactly)
Discrete-event M/M/1/K, FCFS. Per trial draw one arrival stream (Poisson, rate λ = ρ·μ) and one per-customer service-time stream (exponential, rate μ), then simulate BOTH buffer sizes K_SMALL and K_LARGE against that SAME stream (common random numbers), so ΔW = W(K_LARGE) − W(K_SMALL) is a low-variance paired difference. Sojourn is measured for served customers arriving after WARM. Throughput = served / (last departure time). G1 measures ΔW over TRIALS trials at ρ = R_BASE. G2 checks the two throughputs are within EPS·μ of each other and both ≥ (1−EPS)·μ (server saturated, no goodput dividend). G3 repeats G1 and G2 at a shifted load ρ = R_SHIFT.

## Pinned world (committed constants)
SEED = 20260717 · Z_GATE = 3.0 · TRIALS = 40 · N_ARR = 20000 · WARM = 4000 · MU = 1.0 · R_BASE = 1.25 · R_SHIFT = 1.5 · K_SMALL = 25 · K_LARGE = 75 · EPS = 0.02 · FCFS M/M/1/K · floats rounded 6 dp · whole-dict / no-self-field / stdout-only.

## Pre-registered gates (APPROVE iff ALL hold, in order G1 -> G2 -> G3; z_gate = 3.0)
- **G1 — latency scales with buffer size.** Paired ΔW = W(K_LARGE) − W(K_SMALL) > 0 at >= 3 sigma. Observed ΔW mean = 49.954161, z = 508.993574; W(K_SMALL) = 21.09712, W(K_LARGE) = 71.05128, ratio = 3.367819.
- **G2 — no goodput dividend.** |thr(K_SMALL) − thr(K_LARGE)| <= EPS·μ AND both >= (1−EPS)·μ. Observed thr(K_SMALL) = 0.999952, thr(K_LARGE) = 0.999687, gap = 0.000265 — the added latency buys no throughput.
- **G3 — robust under a shifted load.** At ρ = 1.5: ΔW > 0 at >= 3 sigma (mean = 50.033018, z = 581.376023) AND the no-dividend bound holds (thr 1.000961 vs 1.000406, gap = 0.000555, both >= 1−EPS).

## Pre-registered decision rule
APPROVE iff G1 AND G2 AND G3 all hold in order with all_pass=true and the results-dict sha256 reproduces byte-for-byte; else REJECT with first_failing_gate named.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```json
{
  "all_pass": true,
  "eps_throughput": 0.02,
  "first_failing_gate": null,
  "g1_dwait_mean": 49.954161,
  "g1_dwait_std": 0.620711,
  "g1_w_large_mean": 71.05128,
  "g1_w_ratio": 3.367819,
  "g1_w_small_mean": 21.09712,
  "g1_z": 508.993574,
  "g2_thr_gap": 0.000265,
  "g2_thr_large_mean": 0.999687,
  "g2_thr_small_mean": 0.999952,
  "g3_dwait_mean": 50.033018,
  "g3_thr_gap": 0.000555,
  "g3_thr_large_mean": 1.000406,
  "g3_thr_small_mean": 1.000961,
  "g3_z": 581.376023,
  "gates": {
    "G1_latency_scales_with_buffer": true,
    "G2_no_goodput_dividend": true,
    "G3_robust_shifted_load": true
  },
  "k_large": 75,
  "k_small": 25,
  "load_base": 1.25,
  "load_shift": 1.5,
  "mu": 1.0,
  "n_arrivals": 20000,
  "seed": 20260717,
  "trials": 40,
  "warmup": 4000,
  "z_gate": 3.0
}
```
Results-JSON sha256: d968600582b39bde30bbbead4b192a0d08c4d1bcb64c3b5c1a17f40924139142

## Verifier
`ideas/fleet/bufferbloat_standing_queue.py` — stdlib-only (sys, math, json, hashlib, random, collections). run() returns the whole results dict with no self-digest field; main() runs it twice, asserts byte-identical canonical JSON, prints the pretty dict then the sha256.

## Reproduce
```
python3 ideas/fleet/bufferbloat_standing_queue.py
```
Expect exit 0, all_pass=true, and Results-JSON sha256 d968600582...139142 identical across two invocations.

## Why it matters (buffer sizing as a latency knob, not a safety knob)
Any FCFS stage that is occasionally driven past capacity — a work queue, a socket send buffer, a message-broker partition, a retry backlog, a thread-pool inbox — converts every extra buffer slot under saturation into standing latency at 1/μ per slot, with zero throughput gain. The fleet analog: sizing an agent task queue or an outbox backlog "generously" to avoid drops does not raise how much work clears; it raises how stale the work is when it clears. The cure is not a bigger buffer but a shorter one plus load-shedding (admission control / active queue management): drop or shed early so the standing queue never forms, trading a small, bounded loss for a large latency cut.

## Dedup (contrast vs prior lane heads)
Distinct from coordinated-omission (a measurement artifact where a stalled load generator under-samples the very latency it causes; here every served customer's sojourn is measured directly), from the inspection-paradox wait-inflation (a sampling bias in observing an ongoing interval; here W is the true mean sojourn), from service-variance-wait-tax / Pollaczek-Khinchine (wait driven by service-time VARIANCE at fixed utilization; here service is memoryless and the lever is buffer SIZE under overload), from wip-cap-dryness-floor (a cap set too LOW starving the server; here the cap is too HIGH inflating delay), and from variance-blind-provisioning (provisioning to the mean ignoring variance). This head is the first-order finite-buffer standing-queue effect: under ρ > 1, W is affine in K at slope 1/μ with flat throughput. A `git grep` for "bufferbloat", "standing queue", "M/M/1/K" over ideas/ returned no prior head.

## Model basis (declared model-dependence)
Assumes sustained saturation (ρ > 1); under ρ < 1 the queue is not persistently full and W saturates at its stable-queue value rather than scaling with K — the effect is a saturation/overload phenomenon, disclosed. Assumes FCFS (a LIFO or priority discipline changes which customers eat the standing delay but not the aggregate L ≈ K, so mean W is unchanged; tail shape changes). Memoryless arrivals/service isolate the buffer-size lever from variance effects; heavier-tailed service inflates W further but preserves the affine-in-K direction. All disclosed; the gates pin the saturated memoryless world plus the load shift.

## Gate power + margin ledger
| Gate | Statistic | Observed | Threshold | Margin |
|---|---|---|---|---|
| G1 | ΔW mean, z | 49.954161, z=508.99 | ΔW>0, z>=3 | ~506 sigma |
| G2 | throughput gap | 0.000265 | <=0.02·μ, both>=0.98μ | 75x inside bound |
| G3 | shifted-load ΔW, z | 50.033018, z=581.38 | ΔW>0, z>=3 | ~578 sigma |

## Probe report (v0, self-adversarial)
**1. Is the latency growth just an artifact of measuring more customers?** No — W is the mean per-customer sojourn (time in system), not a count; it grows because each admitted customer sits behind an on-average-larger standing queue. G1's paired ΔW isolates the K change on a common arrival stream.
**2. Could the flat throughput be a measurement window artifact?** No — throughput = served / last-departure-time over 20000 arrivals with a 4000 warmup discarded from the latency sample; both buffers deliver within 0.0003 of μ because the server is busy essentially always under ρ > 1. G2 pins this.
**3. Does the effect need the exact K values 25 and 75?** No — the mechanism is W ≈ (K − ρ/(ρ−1))/μ, affine in K; 25→75 gives the observed 21.1→71.1 (ratio 3.37, slightly above the 3.0 K-ratio because the −ρ/(ρ−1) offset shrinks the small-K wait). Any K pair under saturation shows the same slope.
**4. Is it only a heavy-overload (ρ=1.25) curiosity?** No — G3 reruns at ρ = 1.5 and both the ≥3σ latency growth and the no-dividend bound hold; deeper overload pins the queue fuller, if anything strengthening the effect.
**5. Would a non-Poisson or non-exponential model break it?** The affine-in-K, flat-throughput result follows from saturation + finite K + a work-conserving discipline, not from the memoryless assumption; variance changes W's level, not its scaling in K. Disclosed under Model basis.
**6. Does the grounding source actually document this head?** Yes — the live Bufferbloat page states verbatim that in a FIFO system overly large buffers give longer queues and higher latency and do not improve throughput; verified 2026-07-19T21:43:29Z, revid 1354864082.
**7. Is this distinct from the service-variance wait tax already in the lane?** Yes — that head varies service-time C_s² at fixed utilization (Pollaczek-Khinchine); this head fixes memoryless service and moves buffer SIZE under overload. Different lever, different regime. See Dedup.
**8. Does the cross-invocation double run reproduce the digest, and does the in-process assert hold?** Yes — two invocations printed the identical results-dict sha256 d968600582...139142, and main() asserts the in-process double run is byte-identical before printing.

## One-line design fix
Under sustained overload, do not size the buffer up — size it down and shed: a short queue plus admission control / active queue management (drop or mark early) trades a small bounded loss for a large latency cut, because the throughput ceiling is μ no matter how much backlog you are willing to hold.

**Recommendation: sim-ready**
