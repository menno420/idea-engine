# Slotted-ALOHA finite-n throughput ceiling: a contending fleet tops out at (1 − 1/n)^(n−1) → 1/e

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** fleet · coordination/contention — closed-form throughput ceiling for random-access resource sharing.
**Proposal:** 237 → Verdict 250 (+13 offset)
**Verifier:** [`verify_237_slotted_aloha.py`](verify_237_slotted_aloha.py) · stdlib only · SEED=20260717
**Digest:** `results_sha256 = fb72d76e05c3e41d3f671f7d324a76dde84ea815a6360be1652508db4fc0cb9a`

## Claim

A fleet of `n` agents contends for one shared slotted resource — a channel, a lock, a token. In each slot every agent independently transmits with probability `p`. A slot **succeeds** iff exactly one agent transmits (zero = idle, two or more = collision). The single-slot success throughput is exactly

    S(n, p) = n · p · (1 − p)^(n − 1)

which is maximised at the transmit probability

    p* = 1 / n

giving the exact rational ceiling

    S_max(n) = (1 − 1/n)^(n − 1) = (n − 1)^(n − 1) / n^(n − 1)

This ceiling is strictly decreasing in `n` and converges from above to `1/e ≈ 0.367879…`. So no matter how the fleet is tuned, a large set of uncoordinated agents can use a shared slotted resource at most about **36.8%** of the time.

## Exact reference

`p* = 1/n`, and the exact ceiling per fleet size (rational, not rounded):

| n | p* | S_max(n) exact | ≈ |
|---|-----|----------------|----|
| 2 | 1/2 | 1/2 | 0.500000000 |
| 3 | 1/3 | 4/9 | 0.444444444 |
| 4 | 1/4 | 27/64 | 0.421875000 |
| 10 | 1/10 | 387420489/1000000000 | 0.387420489 |
| 100 | 1/100 | 99^99 / 100^99 | 0.369729637 |
| → ∞ | → 0 | → 1/e | 0.367879441 |

**Naive-wrong foil (pre-registered, rejected):** "each slot carries one expected transmission (`n·p* = 1`), so throughput = 1." This ignores idle and collision slots; the true ceiling is about 0.37, not 1. G4 rejects it at |z| ≈ 445–585.

## Four gates (each in its own direction)

- **G1 — exact optimality identity (`fractions.Fraction`).** For every n ∈ {2,3,4,5,8,10,16,32,64,100}: the closed form `(n−1)^(n−1)/n^(n−1)` equals `n·p*·(1−p*)^(n−1)` at `p*=1/n` with **zero** error (rational equality), and `p*` dominates a 199-point rational grid `k/200` — exact argmax confirmation. No floats.
- **G2 — Monte-Carlo agreement.** 200,000 slots per n ∈ {2,3,5,10,25,100}, n independent Bernoulli(1/n) transmitters each; empirical success rate vs `S_max(n)`: all |z| < 3 (**max |z| = 2.2817**).
- **G3 — invariance / robustness.** Relabeling the agents by a nontrivial seeded permutation leaves the success count byte-identical (bijection-invariant); and the exact ceiling is verified strictly monotone-decreasing across all n and strictly above `1/e`.
- **G4 — falsifiability.** The pre-registered naive rule "throughput = offered load = 1.0" is rejected by the same Monte-Carlo data at **min |z| = 445.44** (per-n |z| 445–585).

all_gates_pass=true, first_failing_gate=null, decision=PASS. SEED=20260717 (hardcoded module constant); the in-process double-run and a separate re-invocation are byte-identical; `results_sha256 = fb72d76e05c3e41d3f671f7d324a76dde84ea815a6360be1652508db4fc0cb9a`.

## Grounding

> **Grounding:** https://en.wikipedia.org/w/index.php?title=ALOHAnet&oldid=1350721913&action=raw@16dda63ad347e0a81ba248ae066b4c3aede1e6b4 · fetched 2026-07-21

Pinned ALOHAnet revision oldid 1350721913 (2026-04-23T16:07:37Z, 34,678 bytes); the raw-wikitext sha1 `16dda63ad347e0a81ba248ae066b4c3aede1e6b4` was recomputed firsthand and matches the API `revisions.sha1` exactly, and the byte count matches `size`.

- **Quoted** literally on the pinned revision: the slotted-ALOHA maximum throughput `1/e ≈ 0.368 = 36.8%` reached at offered load `G = 1` (L84), the channel-efficiency figure "36%" (L112, L126), and the continuous throughput law `S_slotted = G·e^(−G)` (L82).
- **Derived** firsthand (grep count 0 on the pinned raw wikitext — genuinely absent): the exact finite-n binomial ceiling `S_max(n) = (1 − 1/n)^(n−1) = (n−1)^(n−1)/n^(n−1)`, the optimal per-agent transmit probability `p* = 1/n`, and the monotone-from-above approach to `1/e`. The article carries only the Poisson/continuous `G·e^(−G)` limit; the finite-n rational refinement is standard textbook material, not a novel result — nothing oversold.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. `S(n,p)=n p (1−p)^(n−1)` is the exact binomial probability of exactly one success among n independent Bernoulli(p) trials; its unique interior maximiser is `p*=1/n` (derivative `n(1−p)^(n−2)(1−np)=0`), and `S_max(n)=(n−1)^(n−1)/n^(n−1)` is an exact rational. G1 confirms this with `fractions.Fraction`, zero error.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?** No. G2 simulates n *independent* Bernoulli(1/n) agent transmissions per slot and counts "exactly one" — the success probability emerges, it is never drawn from `S`. Agreement holds across six fleet sizes (max |z|=2.28).

**3. What is the most plausible wrong belief this could be confused with?** That "one expected transmission per slot ⇒ full utilisation" (throughput=1), or that the ceiling is 1/e at *all* loads rather than *at the optimum* `G=1`. G4 pre-registers and decisively rejects the throughput=1 rule at |z|≈445–585.

**4. Is the verifier deterministic and self-checking?** Yes. SEED=20260717 is a hardcoded constant; the verifier computes results twice in-process (byte-identical) and a separate re-invocation reproduces the identical `results_sha256`. stdlib only (json, hashlib, math, random, fractions).

**5. Does the grounding actually support the claim, or is it overstated?** The Wikipedia pin supports the *limit* (1/e, `G·e^(−G)`, optimum at G=1) — quoted verbatim. The finite-n exact ceiling and `p*=1/n` are explicitly labelled DERIVED (absent from the pinned revision) — the honest split is stated, nothing claimed as novel.

**6. Does it scale / is it robust?** The ceiling is verified exactly across n up to 100 and shown strictly monotone toward 1/e; the Monte-Carlo agrees from n=2 to n=100; relabeling agents leaves the outcome invariant (G3).

**7. Is it falsifiable, and does it survive?** Yes — G4 states a concrete competing rule (throughput=offered load=1) that the data would confirm if true; it is rejected at overwhelming |z|, while the claimed ceiling is confirmed at |z|<3. It survives.

**8. Any residual risk before ruling?** Only cosmetic: the limit `1/e` is irrational so the strict lower-bound check in G3 uses a float comparison (labelled), while every ceiling value and the monotonicity are exact rationals. No material risk.

**Recommendation: sim-ready**
