# Fan-out tail amplification: waiting on all N leaves turns a 1%-per-leaf tail into a coin flip at N≈69

> **State:** `sim-ready`
> **Class:** fleet / distributed-systems tail latency (round-31 FLEET slot)
> **Target:** sim-lab — VERDICT 146 (PROPOSAL 133 → VERDICT 146, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine/blob/main/ideas/fleet/fan_out_tail_amplification.py · fetched 2026-07-18T12:23:31Z
> **Reference (external, reachable):** Dean & Barroso, "The Tail at Scale," Communications of the ACM 56(2):74–80, 2013 — https://web.archive.org/web/https://dl.acm.org/doi/10.1145/2408776.2408794
> **Verifier (firsthand):** ideas/fleet/fan_out_tail_amplification.py · results-dict sha256 `4b3de5012a6cedc99de8e446c3fdd0aa79b1988fd0594c3cbb9e33702131c42d` (SEED=20260717, TRIALS=120000)

## The phenomenon

A scatter-gather request fans out to N independent leaf servers and can only finish when the LAST leaf answers. Its tail is the OR of the leaves' tails, not their average.

## The folk belief

"Each leaf is fast 99% of the time, so a fan-out request is basically always fast." Operators reason about the *typical* leaf and expect the request to inherit it.

## The probabilistic thesis (Q-0254)

Waiting on all N leaves means the request is slow whenever ANY leaf is slow, so its slow-probability is 1 − (1−p)^N — which climbs to a coin flip astonishingly fast. With a 1%-per-leaf tail, the MEDIAN request is already slow at a mere ~69-way fan-out, and a 200-way fan-out is slow ~87% of the time. The rare per-leaf tail becomes the common case; the crossover is N* = ln2 / (−ln(1−p)) ≈ 0.693/p.

## The formal model

- N independent leaves; each is "slow" (misses its latency SLO) with probability p, i.i.d.
- The request waits for all N → it is slow iff at least one leaf is slow.
- P_slow(N) = 1 − (1−p)^N.
- Expected slow leaves per request = N·p (linearity of expectation; the count is ~Poisson(Np) for small p).
- Median crossover (P_slow ≥ ½): N* = ln2 / (−ln(1−p)) ≈ 0.693/p. For p=0.01, N*=69 (real root 68.97).

## Pinned world

SEED=20260717 · TRIALS=120000 · p_leaf=0.01 · N_GRID=(10, 69, 100, 200) · z_gate=3.0. Each trial draws N independent Bernoulli(p) leaves; a request is slow iff ≥1 leaf slow.

## Pre-registered gates (≥3σ, /se z convention)

- **G1 — union-bound tail (N=100):** simulated P_slow matches the closed form 1−(1−p)^N = 0.633968. Pass iff |z| < 3.
- **G2 — median crossover (N*=69):** simulated P_slow ≈ 0.5002, AND the integer crossover is bracketed by the closed form (P_slow(68) < ½ ≤ P_slow(69)) with N*==69. Pass iff |z| < 3 and the bracket holds.
- **G3 — mean slow leaves linear (N=100):** simulated mean slow leaves matches N·p = 1.0. Pass iff |z| < 3.

## Pre-registered decision rule

sim-ready ⇔ all three gates pass in a deterministic dry run (exit 0, byte-identical double run).

## Dry-sim results (firsthand, exit 0, double-run identical)

| N | P_slow (sim) | P_slow (exact) | mean slow leaves (sim) | = N·p |
|---|---|---|---|---|
| 10 | **0.0959** | 0.09562 | 0.1002 | 0.10 |
| 69 | **0.50014** | 0.50016 | 0.68813 | 0.69 |
| 100 | **0.6335** | 0.63397 | 1.00016 | 1.00 |
| 200 | **0.86674** | 0.86602 | 2.00391 | 2.00 |

Gates: **G1 z=−0.336 PASS · G2 z=−0.015 (bracket ✓, N*=69) PASS · G3 z=+0.055 PASS**. `all_pass: true`. Results-dict sha256 **`4b3de5012a6cedc99de8e446c3fdd0aa79b1988fd0594c3cbb9e33702131c42d`** (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY; stdout dump pretty indent=2, digest preimage compact canonical).

## Verifier

`ideas/fleet/fan_out_tail_amplification.py` — stdlib only (hashlib, json, math, random). `run()` returns the results dict (no self-digest field); `main()` computes the compact-canonical sha256, prints the pretty dump + a `Results-JSON sha256:` line, exits 0/1 on `all_pass`.

## Reproduce

    python3 ideas/fleet/fan_out_tail_amplification.py
    # → prints the results JSON, then: Results-JSON sha256: 4b3de50…31c42d ; exit 0

## Why it matters

Fleet scatter-gather (sharded search, multi-shard reads, quorum-of-all) hides this: teams provision on the *typical* leaf and are surprised that request-level p50 degrades as they add shards. The levers are direct — cut per-leaf p (tighter leaf SLO), cut N (coarser sharding), or break the wait-for-all with a cure like [[hedged-request-tail-cure]] / partial-response quorums. The number to remember: at a 1% leaf tail, ~69 leaves is a coin flip.

## Dedup

Distinct from every existing fleet card. Nearest neighbor is [[hedged-request-tail-cure]] (P121) — that card is the *cure* (redundant/hedged requests recover the tail); this is the *phenomenon* (why the tail exists at all). Also distinct from [[two-choices-routing-cliff]] (probe fan-out for load balancing, not wait-for-all), [[correlated-fleet-variance-floor]] (correlation floor N_eff=1/ρ), and [[condorcet-jury-correlation-floor]] (majority-vote accuracy ceiling). No card models the 1−(1−p)^N wait-for-all tail amplification.

## Model basis (P024 discipline)

Closed form derived from first principles (independent Bernoulli leaves, OR of tails); each gate anchors the simulation to an independently-computed exact value; SEED-pinned, byte-identical double run, whole-dict digest disclosed.

## Probe report (v0)

1. **Is the claim counterintuitive?** Yes — operators expect the request to inherit the typical leaf's 99% fast rate; instead ~**69** leaves flips it to a coin toss.
2. **Is it falsifiable?** Yes — three ≥3σ gates against independently-computed closed forms; a wrong model fails G1/G2/G3.
3. **Is the anchor real?** Yes — Dean & Barroso, "The Tail at Scale," CACM 2013, the canonical statement of this effect.
4. **Is the sim deterministic?** Yes — SEED=**20260717**, byte-identical double run, disclosed sha256 **4b3de50…31c42d**.
5. **Is it stdlib-only?** Yes — hashlib/json/math/random.
6. **Does it dedupe?** Yes — distinct object from hedged-request (cure vs phenomenon) and all fleet cards.
7. **Is the number memorable?** Yes — N* ≈ **0.693/p**; p=1% → **69** leaves is a coin flip.
8. **Is there a lever?** Yes — lower p, lower N, or break wait-for-all (hedging / partial quorum).

## One-line correction

Not "each leaf is 99% fast, so the request is 99% fast" — the request is slow whenever ANY of N leaves is slow, so P_slow = 1−(1−p)^N and the median request is already slow at N ≈ 0.693/p (69 leaves at a 1% leaf tail).

**Recommendation: sim-ready** — reproduce the committed verifier byte-identical in sim-lab, confirm results-dict sha256 4b3de5012a6cedc99de8e446c3fdd0aa79b1988fd0594c3cbb9e33702131c42d EXACT and all three ≥3σ gates, then APPROVE as VERDICT 146.
