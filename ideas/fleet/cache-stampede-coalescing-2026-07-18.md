# Caching a HOT key does not reduce its worst-case origin recompute load — it CONCENTRATES it into a herd whose size grows LINEARLY with request rate: at a 1 s recompute a key served 30 req/s unleashes ~30 simultaneous origin recomputes on every expiry (Poisson(λT)=30), and request coalescing collapses that herd to exactly 1 — INDEPENDENT of rate (cache stampede / dogpile)

> **State:** sim-ready
> **Class:** fleet (unrelated / cross-cutting) · caching / concurrency (thundering-herd) · cache-stampede herd size + single-flight coalescing
> **Target:** sim-lab (VERDICT 158, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@c58f29b17ccf40b0cd8258735724c828d6bb8fe5 · fetched 2026-07-18T20:10:49Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Cache_stampede — cache stampede, locking, and probabilistic early expiration (XFetch, Vattani, Chierichetti & Lowenstein, "Optimal Probabilistic Cache Stampede Prevention", VLDB 2015); verified reachable 2026-07-18 via WebFetch

## The phenomenon (one line)
When a hot cached key expires it is stale for the length of one recompute T, and under a plain TTL cache every request arriving in that window independently recomputes it at the origin — so the per-expiry origin burst is Poisson(λT) and scales with request rate, and request coalescing (single-flight) collapses it to exactly 1.

## The folk belief
"A cache with a near-100% hit ratio protects the origin, and a HOTTER key is SAFER because it is almost always served from cache — so to tame origin load you raise the hit ratio or lengthen the TTL. Origin load per key is bounded by the miss rate, which caching drives toward zero."

## The probabilistic thesis (reasoned to its fuller form — Q-0254 duty)
Model one expiry event as a window [0, T) of length T = the time to recompute-and-repopulate the value. Requests to the key arrive as a Poisson process of rate λ. Under a plain TTL cache WITHOUT coordination, every request that arrives while the value is stale (i.e. in [0, T), before the first recompute has repopulated) misses and launches its OWN origin recompute — none of them can see the others in flight. The number that pile onto the origin in one expiry is therefore exactly the count of Poisson arrivals in [0, T): **Poisson(λT), expected herd E = λT.** This is the Wikipedia cache-stampede example verbatim — 10 req/s with a 3 s render gives "30 processes simultaneously recomputing the rendering of the page" (λT = 10·3 = 30). The herd SCALES with the request rate: doubling traffic doubles the per-expiry origin burst, even as the cache hit ratio climbs toward 100% — a hotter key stampedes HARDER, the opposite of the folk intuition. Request coalescing (single-flight / dogpile lock) lets the FIRST request in the window acquire the recompute and makes every subsequent request wait on that single in-flight result, collapsing the herd to exactly **1 recompute per expiry** (E = 1 − e^{−λT}, ≈ 1 for any hot key) — INDEPENDENT of λ. The lever that matters is coalescing, not TTL length: a longer TTL lowers the expiry *frequency* but leaves each expiry's herd size λT completely untouched.

## The formal model (committed constants — sim-lab must reproduce exactly)
Per replication (one expiry event): draw a Poisson(λ) arrival process on [0, T) by summing interarrival ~ Exp(λ) until the clock passes T; naive herd = the count of arrivals strictly inside the window (exactly Poisson(λT)); coalesced recomputes = 1 if the herd ≥ 1 else 0. R independent replications; the reported statistic is the mean over replications, se = sample-std / √R (an honest independent-replication standard error). z = (mean − anchor) / se. The head statistic is the paired amplification (naive_herd − coalesced_recomputes) per replication versus zero.

## Pinned world (committed constants)
SEED = 20260717 (one random.Random(SEED) drawn sequentially in the fixed config order). T_RECOMPUTE = 1.0. SIGMA_GATE = 3.0. Configs (name, λ, T, R, coalesce):
- CFG_LOW: λ=5.0, T=1.0, R=4000, naive — anchor = exact Poisson mean λT = 5
- CFG_HIGH: λ=30.0, T=1.0, R=4000, naive — anchor = exact Poisson mean λT = 30
- CFG_HEAD: λ=30.0, T=1.0, R=4000, coalesced — head statistic = paired amplification vs 0

## Pre-registered gates (PASS iff ALL hold, in order CFG_LOW → CFG_HIGH → CFG_HEAD)
1. **CFG_LOW verifier-correctness** — MC naive herd matches the exact Poisson mean λT = 5 within |z| < 3 (the simulator draws a correct Poisson(λT) herd).
2. **CFG_HIGH verifier-correctness** — MC naive herd matches the exact Poisson mean λT = 30 within |z| < 3, i.e. 6× the CFG_LOW herd for 6× the rate: the mechanism control that the herd is Poisson(λT) and SCALES linearly with request rate (a hotter key stampedes harder — the folk "more caching → less origin load" guess fails here).
3. **CFG_HEAD counterintuitive headline (z ≥ 3)** — with request coalescing the paired amplification (naive_herd − coalesced_recomputes) per expiry sits z ≥ 3 ABOVE zero: coalescing removes ~λT − 1 redundant origin recomputes per expiry (a ~30× → 1× collapse) that a plain TTL cache never touches.

## Pre-registered decision rule
APPROVE VERDICT 158 iff sim-lab reproduces ideas/fleet/cache_stampede_coalescing.py byte-identical under SEED=20260717, the results-dict sha256 matches EXACT, and all three gates PASS in order, exit 0 across a deterministic double-run. Else REJECT.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
CFG_LOW   lam=5    herd=4.9123 coalesced=0.9928 anchor=5.0000 (exact_poisson_mean_lambda*T) z=-2.5226 PASS
CFG_HIGH  lam=30   herd=30.0830 coalesced=1.0000 anchor=30.0000 (exact_poisson_mean_lambda*T) z=+0.9635 PASS
CFG_HEAD  lam=30   herd=30.1382 coalesced=1.0000 anchor=0.0000 (zero_amplification) z=+341.6440 PASS
all_gates_pass = True
first_failing_gate = None
```
CFG_HEAD amplification = mean_naive_herd 30.13825 − mean_coalesced_recomputes 1.0 = 29.13825 (se 0.085288), amplification_factor ≈ 30.14× — coalescing collapses a ~30-strong origin herd to a single recompute. Two CLI runs byte-identical + in-process double-run assertion, exit 0. **Disclosed results-dict sha256 = 81929730f04afec22fcacffd0d44d81609c6d2d2e395dd0803ec77ee29f19422** (sha of the compact canonical json.dumps(sort_keys=True,separators=(",",":")) of the whole results dict; WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY — no self-referential sha field, no on-disk JSON; every float rounded to 6 dp, and the P127+ twist — the stdout DUMP is pretty indent=2 while the hashed payload is compact).

## Verifier
Stdlib-only reference: `ideas/fleet/cache_stampede_coalescing.py` (random, json, hashlib, math). Reproduce: `python3 ideas/fleet/cache_stampede_coalescing.py`. Expected: the three gate lines above, `all_gates_pass = True`, `first_failing_gate = None`, the pretty results dump, `Results-JSON sha256: 81929730f04afec22fcacffd0d44d81609c6d2d2e395dd0803ec77ee29f19422`, exit 0.

## Why it matters (cross-cutting)
Every read-through cache in front of an expensive origin is a stampede risk: rendered pages, DB query caches, config/feature-flag fetches, token/JWKS caches, memoized model calls. The stampede law prices the instinct "cache the hot path and origin load takes care of itself": the origin's WORST-case load is not the average miss rate but the per-expiry herd λT, which grows with exactly the traffic that caching was supposed to shield the origin from — the hottest keys generate the largest bursts. The fix is a coordination primitive (single-flight / request coalescing / a per-key recompute lock, or probabilistic early expiration), NOT a longer TTL: coalescing makes the per-expiry origin cost O(1) regardless of rate, so a hot key becomes cheap to protect instead of dangerous. Because the herd is Poisson(λT) and quantifiable up front, the coalescing decision can be made deliberately per key rather than discovered in an origin brown-out when a popular key expires.

## Dedup
- **metastable-retry-storm-collapse (2026-07-17)** — a bistable CONGESTION-COLLAPSE result: retries under overload push the system into a stable jammed metastable state (hysteresis / tipping). This is a single TTL-expiry HERD with no retries, no bistability, no load-dependent service — the object is the Poisson(λT) recompute count at one expiry and its O(1) collapse under coalescing, not a metastable operating point.
- **hedged-request-tail-cure (2026-07-18)** — duplicate requests deliberately ISSUED as a CURE for tail latency (send a second copy, take the first to return). Here duplicate work is the PROBLEM and coalescing (suppressing duplicates) is the cure — the opposite direction; the object is per-EXPIRY herd size vs per-REQUEST tail latency.
- **erlang-b-trunking-efficiency / checkout-pooling-single-line** — loss/delay QUEUEING systems (blocking probability, wait time) at steady state. This is not a queue: no servers, no service discipline; it is the count of concurrent recomputes triggered by one cache expiry.
- **fan-out-tail-amplification / two-choices-routing-cliff** — tail latency from fan-out and placement imbalance across many backends. This is a single-key origin-recompute herd, not a fan-out or load-placement object.
- **epidemic-overshoot (2026-07-17)** — SIR-style contagion overshoot on a population. Different object entirely: no infection graph, no compartments; a Poisson herd at a TTL boundary.

## Model basis (declared model-dependence — the P024 discipline)
The headline is exact for the standard cache-stampede abstraction: Poisson arrivals, a fixed recompute window T, and a plain TTL cache with no coordination (every in-window request recomputes). Two declared choices: (i) the recompute window is modelled as a FIXED length T rather than "until the first recompute completes" — this is the classic textbook abstraction (and the Wikipedia example's model); relaxing it to "stale until first refill lands" only makes the naive herd LARGER (the window is at least T and can be longer under load), so the coalescing benefit is conservative. (ii) Arrivals are Poisson (independent); real request streams for a hot key can be bursty/super-Poisson, which makes the herd MORE variable and the stampede WORSE, not better — again conservative for the coalescing direction. Neither relaxation changes the sign or the O(1)-vs-O(λT) contrast.

## Probe report (v0, 2026-07-18)
**1. What is this really?** The number of concurrent origin recomputes triggered by one expiry of a hot cached key (Poisson(λT)) and how a single-flight lock collapses it to O(1) — a concurrency/coordination result, not a hit-ratio result.
**2. What would make it false?** If the per-expiry herd were bounded independent of rate under a plain TTL cache. It is not: with no coordination every in-window arrival recomputes, so the herd is Poisson(λT) and grows with λ — CFG_HIGH being ~6× CFG_LOW at 6× the rate is the direct evidence.
**3. Simplest version that still bites?** One key, 30 req/s, a 1 s recompute: every expiry stampedes the origin with ~30 simultaneous recomputes; a single-flight lock makes it 1.
**4. Counterintuitive core?** A higher hit ratio does NOT bound origin load — the hottest keys produce the LARGEST per-expiry bursts, and the burst scales with the very traffic caching was meant to absorb. TTL length changes expiry frequency, not herd size; only coalescing changes herd size.
**5. Where could I be fooling myself?** Single-trajectory noise is handled by R independent replications with a between-replication se; the naive herd must reproduce EXACT Poisson(λT), which gates 1–2 enforce (CFG_LOW z=−2.52 and CFG_HIGH z=+0.96 both within |z|<3 — the simulator draws the right distribution at both rates). The head is a paired amplification, so it is not inflated by any shared-rate bias.
**6. Honest calibration?** High confidence: the Poisson-herd result is a textbook exact identity (E[arrivals in a window] = λT) and the coalesced count is trivially ≤ 1; the only thing under test is that the committed simulator reproduces it and that coalescing's amplification sits dozens of σ above zero (z=+341.6).
**7. What decision does it change?** Whether to put a single-flight / coalescing primitive (or probabilistic early expiration) in front of an expensive origin, and whether "longer TTL" is a valid stampede fix. It is not — coalescing is; and the decision is per-key, priced by λT.
**8. How will we know it worked?** sim-lab reproduces the verifier byte-identical, the sha256 matches, all three gates PASS in order (two |z|<3 correctness gates + one z≥3 head), exit 0 on a deterministic double-run.

## One-line correction
Origin load per hot key is set by the per-expiry herd λT, not by the hit ratio — so a hotter key stampedes harder, a longer TTL doesn't help, and request coalescing (not caching more) is what makes the per-expiry cost O(1).

**Recommendation: sim-ready**
