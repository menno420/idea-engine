# PROPOSAL 173 — Decorrelated jitter backoff: adding random jitter to exponential retry backoff cuts total retry work and stops the thundering herd re-forming

> **State:** sim-ready
> **Class:** retry / backpressure / contention law
> **Slot:** round-41 FLEET
> **Anchor:** adding randomness to a retry schedule reduces total work
> **Target:** sim-lab (VERDICT 186, +13 offset)
> **Grounding:** https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/@310e5af1c1dda07a73e46961f046be4ae45d0873 · fetched 2026-07-19
> **Reference (external, reachable):** https://brooker.co.za/blog/2015/03/21/backoff.html — author's companion post; a durable mirror, since the AWS page serves per-request nonces so its content digest is not byte-stable and the pin records the fetch that documented the head. Also https://en.wikipedia.org/wiki/Exponential_backoff for the classic ALOHA/CSMA randomized-backoff root.
> **Verifier (firsthand):** `ideas/fleet/decorrelated_jitter_backoff.py` — Results-JSON sha256 `efea8579300ab0806132a48ea68cb8e9030105d8356b6fad51273fa8cb19e2f8`
> 📊 Model: Claude Opus · high · proposal/idea-generation

## The phenomenon (one line)
After a shared dependency fails and recovers, N=200 clients that retry with PLAIN capped-exponential backoff stay locked in phase — the whole surviving herd re-collides at every backoff instant — so draining them through a K=10/slot server takes 2100 attempts; sampling the wait UNIFORMLY inside the same backoff window (full jitter) decorrelates them and drains the same herd in 784.5 attempts, a 62.6% cut, with no change to the backoff schedule's magnitude.

## The folk belief
Randomness is something to engineer OUT: a deterministic exponential backoff is the disciplined, predictable choice, and adding jitter can only waste time (clients wait a random, on-average-shorter interval) and make behaviour harder to reason about. Under load you want every client to back off HARDER, not to roll dice.

## The mechanism (reasoned, Q-0254 duty)
The cost is not the backoff magnitude — it is the CORRELATION of retry times. With a deterministic schedule, two clients that fail in the same slot have identical failure counts, so they compute the identical next-wait and land in the identical future slot; the herd never desynchronizes, and each round K clients drain while the entire remainder collides again. Attempts sum as N + (N−K) + (N−2K) + … ≈ N²/2K — super-linear in N, the AWS "work grows with N²" observation. Full jitter breaks the correlation at its source: drawing the wait uniformly from [1, w(f)] spreads the w(f)-wide herd across w(f) slots, so the number attempting per slot falls toward the server's clear rate K and almost every attempt after the first unavoidable collision succeeds. The schedule's central tendency is barely changed (a uniform draw on [1,w] has mean ≈ w/2, within a constant of the deterministic w); ONLY variance is added, and that added variance is exactly what buys the decorrelation. Because the win comes from destroying synchronization, it is largest precisely when synchronization is worst — a tight, simultaneous herd — and fades smoothly as the arrival process becomes dispersed on its own.

## The formal model (committed constants)
A slotted contention/drain model. N=200 clients each need one success from a shared server that clears at most K=10 requests per discrete slot; when more than K attempt, K succeed (chosen uniformly at random) and the rest fail and reschedule after a capped-exponential window w(f)=min(CAP, BASE·2^f) on their f-th failure (BASE=1, CAP=64). Two retry policies share that window and differ ONLY in the wait drawn from it: "none" waits the whole window w(f) (deterministic, synchronized); "full" waits U{1..w(f)} (decorrelated). A non-gated "equal jitter" policy (w/2 + U{0..w−w/2}) is reported for comparison with the AWS variants. The tight regime seeds all clients at t=0 (a Dirac herd); the robustness regime replaces that with an over-dispersed geometric arrival smear (each client's first slot = ⌊Exp(mean=2)⌋).

## Pinned world (committed constants)
SEED=20260717; z_gate=3.0; N=200; K=10; BASE=1; CAP=64; TRIALS=400; SMEAR_MEAN=2.0; REDUCTION_FLOOR=0.30.

## Pre-registered gates (G1→G2→G3, z_gate=3.0)
- **G1 — work reduction (tight Dirac herd):** full-jitter mean total attempts is ≥3σ below the DETERMINISTIC no-jitter total AND the reduction fraction 1 − mean_full/total_none ≥ 0.30. The no-jitter drain is deterministic here (timing is independent of which clients succeed), so it is an exact baseline and the z is the full-jitter replication-SE distance from it. Rejects the folk "randomness only wastes work" belief.
- **G2 — thundering-herd flattening (same regime):** the repeated post-herd peak contention — the maximum attempts in any slot AFTER the unavoidable t=0 herd — is ≥3σ smaller under full jitter than the deterministic no-jitter value N−K, i.e. jitter stops the herd re-forming at full strength.
- **G3 — robustness under a shifted arrival distribution (≥3σ, paired):** under an over-dispersed geometric arrival smear, full jitter STILL reduces total work vs no-jitter on the SAME arrivals; the paired diff (none − full) is ≥3σ positive across trials.

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 all pass; otherwise revise. The shipped verifier's `all_pass` field is exactly this conjunction, so a green `all_pass=true` and the decision rule are the same statement.

## Dry-sim results
```json
{
  "all_pass": true,
  "gates": {
    "G1_work_reduction_tight": {
      "effect": 1315.49,
      "full_mean_total": 784.51,
      "none_total": 2100,
      "pass": true,
      "reduction_fraction": 0.626424,
      "z": 4350.282085
    },
    "G2_herd_flattening_tight": {
      "effect": 73.365,
      "full_mean_post_herd_peak": 116.635,
      "none_post_herd_peak": 190,
      "pass": true,
      "z": 244.458881
    },
    "G3_robust_shifted_arrivals": {
      "mean_paired_diff": 15.8175,
      "pass": true,
      "se_paired_diff": 1.335457,
      "z": 11.844264
    }
  },
  "meta": {
    "base": 1,
    "cap": 64,
    "capacity": 10,
    "grounding": "https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/ (Brooker, AWS Architecture Blog; Full Jitter minimizes competing calls / total work)",
    "head": "decorrelated jitter backoff: adding random jitter to exponential retry backoff decorrelates the herd, cutting total retry work and repeated peak contention vs no-jitter backoff",
    "n_clients": 200,
    "reduction_floor": 0.3,
    "seed": 20260717,
    "smear_mean": 2.0,
    "trials": 400,
    "z_gate": 3.0
  },
  "smear_herd": {
    "full_mean_total": 703.4075,
    "mean_paired_diff": 15.8175,
    "none_mean_total": 719.225,
    "se_paired_diff": 1.335457
  },
  "tight_herd": {
    "equal_mean_total": 754.49,
    "full_mean_post_herd_peak": 116.635,
    "full_mean_total": 784.51,
    "full_se_post_herd_peak": 0.300112,
    "full_se_total": 0.302392,
    "none_drain_time": 958,
    "none_post_herd_peak": 190,
    "none_total_attempts": 2100,
    "reduction_fraction": 0.626424
  }
}
Results-JSON sha256: efea8579300ab0806132a48ea68cb8e9030105d8356b6fad51273fa8cb19e2f8
```

## Verifier
`ideas/fleet/decorrelated_jitter_backoff.py` — stdlib only (`hashlib, heapq, json, random, statistics`), seeded at SEED=20260717. Each trial/arm draws from its own random.Random(int seed); `main()` runs `run()` twice in-process and asserts the two compact-canonical (sorted-keys, 6-dp-rounded) serializations are byte-identical before hashing; the digest is the results dict's OWN sha256 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: no digest field on the dict, nothing written to disk; the stdout dump is pretty indent=2, floats 6 dp).

## Reproduce
```
python3 ideas/fleet/decorrelated_jitter_backoff.py
```
Prints the results JSON then the `Results-JSON sha256:` line; deterministic across invocations (a second run is byte-identical); exit 0 with `all_pass=true`.

## Why it matters
Any client fleet that retries against a shared, capacity-limited dependency — connection pools reconnecting after a database blip, mobile clients after an API 503, workers after a queue-broker restart, a CDN fleet after an origin flap — pays the N²/K synchronization tax if its backoff is deterministic. The fix costs one line (draw the sleep uniformly from [0, backoff] instead of sleeping the whole backoff) and needs no coordination, no server change, and no extra requests; it turns a self-amplifying retry herd into a smooth drain at the server's clear rate. The result also says WHEN it does not matter: if arrivals are already dispersed, or the server has no per-slot ceiling, there is nothing to decorrelate — spend the jitter budget where herds actually form (post-outage recovery, cron-aligned wakeups, cache-expiry stampedes).

## Dedup (contrast vs prior lane heads)
- vs **`ideas/fleet/metastable-retry-storm…`** — that head is about DEMAND (retries sustaining an overloaded state past the triggering fault); this is about the TIMING/synchronization of retries and is orthogonal — jitter changes WHEN clients retry, not how many; the two compose (jitter alone does not cure a metastable overload, and a retry budget alone does not desynchronize a herd).
- vs **`ideas/fleet/cache-stampede-coalescing…`** — that dedups concurrent IDENTICAL requests server-side (single-flight); this decorrelates INDEPENDENT clients' retry timing client-side. Different layer, different quantity.
- vs **`ideas/fleet/hedged-request-tail…`** — hedging ADDS speculative duplicate requests to cut tail latency; jitter REMOVES synchronized duplicate retries to cut total work. Opposite direction on the same request-count axis.
- vs **`ideas/fleet/coordinated-omission…`** — a measurement-bias head (samples dropped during stalls), an unrelated mechanism.

## Model basis (P024 discipline)
A parameter-free discrete-event contention model; the only "tuning" is the pinned world (N, K, window), and the head is a comparison of two policies ON THE SAME world, so no fit can flatter one arm. The N²/K synchronization scaling and the jitter cure are exactly what the grounding source demonstrates by simulation; G1/G2 magnitudes are measured against an EXACT deterministic baseline, and G3 is a paired difference.

## Gate power + margin ledger
| Gate | quantity | observed | threshold | margin |
|------|----------|----------|-----------|--------|
| G1 | reduction fraction (tight) | 0.626424 | ≥ 0.30 | 0.326424 |
| G1 | z (none−full)/SE_full | 4350.282085 | z ≥ 3.0 | 4347.282085 |
| G2 | z (post-herd peak flattening) | 244.458881 | z ≥ 3.0 | 241.458881 |
| G3 | z (paired diff, shifted arrivals) | 11.844264 | z ≥ 3.0 | 8.844264 |

## Probe report (v0, self-adversarial)
**1. Does the grounding source document the specific head, not backoff in general?** Yes — the AWS post runs the exact comparison (No Backoff / No Jitter / Full / Equal / Decorrelated) and reports Full Jitter has the lowest total call count ("we've reduced our call count by more than half") and that "The no-jitter exponential backoff approach is the clear loser … more work … more time"; fetched live this session (HTTP 200).
**2. Is the no-jitter baseline a strawman?** No — both arms use the identical capped-exponential window w(f)=min(64, 2^f); they differ ONLY in whether the wait is the whole window or a uniform draw inside it, so the 62.6% reduction is attributable to that single variable, not to a weaker backoff.
**3. Is the significance valid when the no-jitter arm is deterministic?** In the tight herd the no-jitter drain is an exact constant (2100 attempts, peak 190) because timing is independent of which K clients succeed, so it is a fixed baseline and the z is the full-jitter replication-SE distance from it (G1 z=4350, G2 z=244); G3 instead uses a proper paired diff where both arms vary (z=11.8).
**4. Is the win an artifact of the perfectly synchronized t=0 herd?** No — G3 replaces the Dirac herd with an over-dispersed geometric smear and full jitter still reduces total work at ≥3σ (paired diff 15.82, z=11.8). Honest caveat: the ABSOLUTE gap shrinks sharply (719.2 → 703.4, ≈2%) because dispersed arrivals are already partly decorrelated — the benefit is largest exactly when the herd is most synchronized, which is the failure mode that matters.
**5. Could full jitter be slower even though it does less work?** No — the no-jitter drain time is 958 slots (each round waits the full doubling window) whereas jitter lets clients retry as early as slot 1 and keeps the server busy; jitter does less work AND drains sooner, matching the AWS "more time" finding (drain time reported, non-gated).
**6. Does equal or decorrelated jitter beat full jitter?** Not materially here — equal jitter's mean total (754.5) is within a few percent of full (784.5) and both crush no-jitter (2100); the head's claim is the large ANY-jitter-vs-NO-jitter gap, not the small ordering among jitter variants, which is model-dependent and disclosed as a wash.
**7. Is determinism real?** Yes — every trial/arm draws from its own random.Random(int seed); run() is executed twice in-process and asserted byte-identical before hashing; the digest reproduces cross-invocation (confirmed, sha256 efea8579…).
**8. What breaks the law?** Unbounded server concurrency (no per-slot ceiling) leaves no contention to decorrelate; already-dispersed arrivals collapse the gap (G3); and jitter trades a modest per-client latency increase (uniform wait, mean ≈ window/2) for the large systemic work saving — disclosed as the boundary, not claimed universal.

## One-line design fix
Sleep a UNIFORM random interval in [0, backoff] instead of the full backoff — one line, no coordination, no extra requests — and spend that jitter where herds actually form (post-outage recovery, cron-aligned wakeups, cache-expiry stampedes).

**Recommendation: sim-ready**
