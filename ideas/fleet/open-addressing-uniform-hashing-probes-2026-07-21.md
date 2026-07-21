# Open-addressing unsuccessful search under uniform hashing: with m slots and n occupied (load factor α=n/m) the EXPECTED number of probes is EXACTLY (m+1)/(m−n+1) — proved via the hockey-stick identity from the exact sum-of-products Σ_{i=0}^{n} C(n,i)/C(m,i) — converging monotonically up to the classic 1/(1−α), refuting the naive belief that 1/(1−α) holds exactly at finite (m,n) (at m=100,n=70 the truth is 101/31≈3.258, not 10/3≈3.333)

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** fleet · hashing / load-balancing
**Proposal:** 245 → Verdict 258 (+13 offset)
**Verifier:** [`verify_245_open_addressing_probes.py`](verify_245_open_addressing_probes.py) · stdlib only (json, hashlib, math, random, fractions) · SEED=20260717
**Digest:** `results_sha256 = 98d7398935db83b93f4e5b71ef4393abf487d3bc4371018d0d9d16e4f75e1746`

## What this proposal does

Adds a fleet PROPOSAL establishing the exact finite-table probe cost of an **unsuccessful search** in an **open-addressing hash table** under the **uniform-hashing model** — the idealisation in which each key's probe sequence is a uniformly random permutation of all `m` slots (Knuth / CLRS). With `m` slots and `n` occupied, load factor `α = n/m`, the expected number of probes an unsuccessful search makes is **exactly**

    E_unsucc(m, n) = (m + 1) / (m − n + 1),

and as `m, n → ∞` at fixed `α` this **increases monotonically** to the classic closed form `1/(1 − α)`. The proposal ships a stdlib-only firsthand verifier that (i) proves the exact identity from its combinatorial definition, (ii) confirms it against a Monte-Carlo simulation of the actual uniform-hashing search, (iii) shows the count depends only on `(m, n)` and not on which slots are occupied, and (iv) **falsifies** the plausible-but-wrong belief that `1/(1 − α)` holds exactly at finite `(m, n)`. Fills a confirmed gap: open-addressing uniform-hashing unsuccessful-search probes is grep-0 across both repos and disjoint from the named prior hashing/allocation heads — birthday-collision (P132), balls-into-bins (P225), consistent-hashing-max-gap, and Maekawa grid-quorum (P209).

## Method

Exact rational arithmetic first, Monte-Carlo second. An unsuccessful search probes slots in a uniformly random order and stops at the first **empty** slot (which certifies the key is absent); the probe count equals the position of the first empty slot in the probe permutation. Written as a sum of tail events,

    E = Σ_{i≥0} P(first i probes all land on OCCUPIED slots)
      = Σ_{i=0}^{n}  (n/m)·((n−1)/(m−1))·…·((n−i+1)/(m−i+1))
      = Σ_{i=0}^{n}  C(n, i) / C(m, i).

**Exact identity (hockey-stick proof).** Because `C(n,i)/C(m,i) = C(m−i, n−i)/C(m,n)` (both equal `n!(m−i)! / ((n−i)! m!)`),

    Σ_{i=0}^{n} C(n,i)/C(m,i) = (1/C(m,n)) Σ_{i=0}^{n} C(m−i, n−i)
                              = (1/C(m,n)) Σ_{j=0}^{n} C(m−n+j, j)      (j = n−i)
                              = C(m+1, n) / C(m,n)                      (hockey-stick)
                              = (m + 1) / (m − n + 1).

The verifier checks the finite sum, the closed form, and the hockey-stick ratio `C(m+1,n)/C(m,n)` as exact `fractions.Fraction` values (G1). The Monte-Carlo leg (G2) draws a uniformly random permutation of the `m` slots with the seeded RNG, `n` occupied, and counts probes until the first empty slot — one probe-count per trial, so the trials are **independent** and **no thinning is needed** (stated explicitly in the verifier docstring). G3 runs two occupancy configurations at the same `(m, n)` and adds an exact monotone-convergence sub-check; G4 rejects the naive `1/(1−α)`-at-finite-`(m,n)` belief on the same headline sample.

## Exact reference

The finite sum-of-products definition and the closed form, computed three independent ways as exact `fractions.Fraction` (the finite sum, the closed form `(m+1)/(m−n+1)`, and the hockey-stick ratio `C(m+1,n)/C(m,n)`), agree bit-for-bit over the battery. Sanity anchors reproduced exactly:

| m | n | α | E_unsucc exact | naive 1/(1−α) |
|---|---|---|---|---|
| 1 | 0 | 0 | **1** | 1 |
| 2 | 1 | 1/2 | **3/2** | 2 |
| 3 | 2 | 2/3 | **2** | 3 |
| 10 | 7 | 7/10 | **11/4 = 2.75** | 10/3 ≈ 3.333 |
| 100 | 70 | 7/10 | **101/31 ≈ 3.258** | 10/3 ≈ 3.333 |

The finite formula sits strictly **below** the asymptotic `1/(1−α)` at every finite table and rises to it monotonically as `m` grows at fixed `α` — e.g. at `α = 7/10`: `E(10)=11/4`, `E(100)=101/31`, `E(1000)=143/43`, `E(10000)=10001/3001`, `E(100000)=100001/30001`, all strictly increasing and strictly below the limit `10/3`.

## Four gates (each in its own direction)

- **G1 — EXACT identity (`fractions.Fraction`, zero tolerance).** Over the battery `{(1,0),(2,1),(3,2),(5,3),(10,7),(13,0),(16,8),(23,17),(50,35),(100,70),(128,96),(257,200)}` the finite sum `Σ_{i=0}^{n} C(n,i)/C(m,i)`, the closed form `(m+1)/(m−n+1)`, and the hockey-stick ratio `C(m+1,n)/C(m,n)` are **exactly equal** — `mismatches = 0`, `anchor_mismatches = 0`, **max discrepancy exactly 0** (z is not applicable and is reported `null` / `"exact"`). Anchors `(1,0)→1`, `(2,1)→3/2`, `(3,2)→2`, `(10,7)→11/4` pinned.
- **G2 — Monte-Carlo agreement (`|z| < 3`).** Simulating the actual uniform-hashing unsuccessful search at the headline `(m=100, n=70)` with `N = 200 000` i.i.d. trials (uniformly random probe permutation per trial via the seeded RNG; count probes to the first empty slot) gives `mean_hat = 3.2596` against `E_exact = 101/31 ≈ 3.2581`, `z = 0.2616711626`, `|z| < 3` [Z_ACCEPT = 3.0]. The trials are **independent** — exactly one probe-count per trial — so **no thinning is needed** (unlike autocorrelated queueing simulators); this is stated explicitly in the verifier docstring.
- **G3 — invariance / robustness (own direction).** The expected probe count depends **only** on `(m, n)`, not on **which** slots are occupied. Two occupancy configurations at `(100, 70)` — occupied = the first `n` slots vs occupied = a fixed pseudo-random `n`-subset — both agree with `E_exact` (config A `z = 0.3374925104`, config B `z = −1.1046610225`) and with **each other** (two-sample difference `z_invariance = 1.0187955206`), all `|z| < 3`. Robustness sub-check (exact, `Fraction`): at fixed `α = 7/10` the sequence `E(m)` for `m ∈ {10, 100, 1000, 10000, 100000}` is `11/4, 101/31, 143/43, 10001/3001, 100001/30001` — **strictly monotone increasing**, every term strictly **below** the limit `10/3`, and approaching it (`monotone_increasing = below_limit = approaches_limit = True`).
- **G4 — falsifiability (own direction, on the SAME G2 sample).** The plausible naive alternative "expected probes = `1/(1−α)` exactly at finite `(m, n)`" is **false** for finite tables. On the same headline `(100, 70)` sample the truth is `101/31 ≈ 3.258` while the naive value is `10/3 ≈ 3.333`; `z_naive = 12.5653466132`, **`|z| ≫ 3` REJECTED** [Z_REJECT = 3.0]. The same sample that **agrees** with the exact finite value (G2, `|z| = 0.26`) **rejects** the naive asymptotic — that is the teeth: `1/(1−α)` is a limit, not a finite-table equality.

All four gates PASS; `all_pass = true`, `first_failing_gate = null`, `decision = PASS`, `results_sha256 = 98d7398935db83b93f4e5b71ef4393abf487d3bc4371018d0d9d16e4f75e1746`. Deterministic three ways: in-process double-run byte-identical (`in_process_double_run: IDENTICAL`), a `--selfcheck` path printing `SELFCHECK: byte-identical`, and a separate-process re-invocation byte-identical. SEED = 20260717 (hardcoded module constant).

## Grounding

One pinned Wikipedia revision (API `revisions.sha1` == self-computed `sha1sum` of the raw wikitext — exact match):

- **"Open addressing"**, oldid 1353211902:
  `https://en.wikipedia.org/w/index.php?title=Open_addressing&oldid=1353211902@164df5a783e58eb4bb744e87fe2e7a5c227199bb` (8806 bytes).

- **Quoted** literally on the pinned "Open addressing" revision (grep count > 0): the load factor `α = n/m` (`\alpha=n/m`, grep 1); the phrase "**load factor**" (grep 7) as "the proportion of the slots in the array that are used"; "the number of probes in an **unsuccessful search**" `U_n` (grep 1); the open-addressing search mechanism verbatim ("searching through alternative locations in the array (the *probe sequence*) until either the target record is found, or an unused array slot is found, which indicates that there is no such key in the table"); and the subexpression `1/(1−α)` (`\frac{1}{1-\alpha}`, grep 1) — **but embedded in the LINEAR-PROBING unsuccessful formula** `EU_n = ½(1 + 1/(1−α)) + Θ(1/m)`, a *different* probe model from uniform hashing.
- **Derived** firsthand (grep count 0 on the pinned raw wikitext): the exact finite identity `(m+1)/(m−n+1)` (grep 0 for `m-n+1` / `m+1`); the **uniform-hashing** model itself (uniformly random permutation probe sequence) and its standalone unsuccessful-search asymptotic `1/(1−α)` — the page's `1/(1−α)` is the *linear-probing* sub-term `½(1 + 1/(1−α))`, whereas the uniform-hashing standalone limit (CLRS Theorem 11.6) is not on this revision as such; the sum-of-products definition `Σ C(n,i)/C(m,i)`; the hockey-stick proof; all exact rational instances (1, 3/2, 2, 11/4, 101/31); the Monte-Carlo agreement, the invariance leg, the falsification, and every z-value and the digest. **Honest posture** — the load factor `α = n/m`, the "number of probes in an unsuccessful search" object, and the subexpression `1/(1−α)` are QUOTED on the pinned page (the last inside the linear-probing formula, a distinct model); the exact finite identity `(m+1)/(m−n+1)`, the uniform-hashing model, all exact instances, the hockey-stick proof, the MC agreement, the invariance leg, and the falsification of "`1/(1−α)` exact at finite `(m, n)`" are the firsthand contribution — a falsification that directly clarifies that the page's asymptotic is a limit, not a finite-table equality. Nothing oversold as novel.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 computes the unsuccessful-search expectation three independent exact ways — the finite sum-of-products `Σ_{i=0}^{n} C(n,i)/C(m,i)`, the closed form `(m+1)/(m−n+1)`, and the hockey-stick ratio `C(m+1,n)/C(m,n)` — entirely in `fractions.Fraction`, and they agree bit-for-bit over a 12-pair battery (`mismatches = 0`). The anchors `(1,0)→1`, `(2,1)→3/2`, `(3,2)→2`, `(10,7)→11/4` are exact rationals, no float involved. The hockey-stick identity supplies a closed proof, so the equality is a theorem, not a fit.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?** No. The exact identity (G1) is fixed before any RNG is touched. The Monte-Carlo gate (G2) only confirms the *average probe count* of the actual search: draw a uniformly random permutation of the `m` slots, `n` occupied, count probes to the first empty. It lands at `|z| = 0.26` against the exact `101/31`.

**3. What is the most plausible wrong belief this could be confused with?** That the textbook asymptotic `1/(1−α)` holds exactly at finite `(m, n)` — pre-registered as G4 and refuted on the same sample at `|z| = 12.57` (the true finite value `101/31 ≈ 3.258` is strictly below the naive `10/3 ≈ 3.333`). A secondary confusion — that the answer depends on *which* slots are occupied — is refuted by G3 (invariance `|z| = 1.02`).

**4. Is the verifier deterministic and self-checking?** Yes. A single `random.Random(20260717)` is seeded once and consumed in a fixed order across all Monte-Carlo legs; `build_results()` is a pure function of SEED and the module constants (no wall-clock / PID / unordered-set iteration in the hashed payload). Exact rationals serialize via `str(Fraction)` and every float via a fixed `f"{v:.10f}"` string, so the bytes are stable. `main()` asserts an in-process double-run is byte-identical, `--selfcheck` prints "SELFCHECK: byte-identical", and two separate process invocations reproduce the digest byte-for-byte. Whole-dict `results_sha256 = 98d7398935db83b93f4e5b71ef4393abf487d3bc4371018d0d9d16e4f75e1746`.

**5. Does the grounding actually support the claim, or is it overstated?** Honest and tight. The pinned "Open addressing" revision carries the load factor `α = n/m`, the "number of probes in an unsuccessful search" object, the search mechanism verbatim, and the subexpression `1/(1−α)` — the last inside the *linear-probing* formula `½(1 + 1/(1−α))`, a distinct probe model, which I flag explicitly. Derived-not-quoted (grep 0): the exact finite identity `(m+1)/(m−n+1)`, the uniform-hashing model and its standalone `1/(1−α)` limit (CLRS-specific), all exact instances, and every z-value. Neither oversold nor undersold — and the falsification directly clarifies the page's asymptotic as a limit.

**6. Does it scale / is it robust?** The claim is a closed-form expectation valid for every `(m, n)` with `n ≤ m`. G1 anchors it exactly across `m = 1 … 257`. G3 adds a robustness leg specific to the object: the answer depends only on `(m, n)` (invariance `|z| = 1.02` across two occupancy configurations) and the exact `E(m)` at fixed `α` is monotone increasing and bounded above by `1/(1−α)`, approaching it — verified as exact Fractions.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the single most plausible wrong belief ("`1/(1−α)` exact at finite `(m, n)`") and refutes it on the same evidence at `|z| = 12.57`, while G2 shows that same sample agrees with the exact `101/31` at `|z| = 0.26`. An off-by-one in the "first empty slot" test, a wrong occupied/empty polarity, or using the asymptotic in place of the finite formula would break the exact G1 identity or push a G2 z past the accept band.

**8. Any residual risk before ruling?** The Monte-Carlo leg is i.i.d. Bernoulli-like per trial (one probe-count per independent trial) so — unlike an autocorrelated queueing simulator — the reported binomial/sample SE is honest with **no thinning**, stated explicitly in the docstring. The exact identity (G1) is what carries the claim and is RNG-free, backed by the hockey-stick proof. The load factor `α = n/m`, the unsuccessful-search object, and the `1/(1−α)` subexpression are textbook (Knuth; CLRS Theorem 11.6; the pinned "Open addressing" page) and cited as such; the exact finite identity, all exact instances, the proof, the MC agreement, the invariance leg, and the falsification are the firsthand contribution. The paired sim-lab VERDICT 258 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
