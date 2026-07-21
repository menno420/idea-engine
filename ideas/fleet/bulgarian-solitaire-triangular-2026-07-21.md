# Bulgarian solitaire's triangular-number fixed point: the move is "remove one card from every pile, then form ONE new pile whose size = the number of piles you had" — a deterministic self-map on integer partitions of n. If n is triangular, n = T_k = k(k+1)/2, then from EVERY partition of T_k the iteration converges to the UNIQUE period-1 fixed point, the staircase δ_k = (k, k−1, …, 2, 1), and the MAXIMUM number of steps over all partitions of T_k is EXACTLY k²−k — verified by full enumeration for k=1..8 (M(k) ∈ {0,2,6,12,20,30,42,56}, all matching k²−k, 0 nonconvergent). Non-triangular n admit NO fixed point (every orbit lands in a period>1 limit cycle), which refutes the naive "non-triangular n also settle to a unique fixed point" foil on a 40000-draw uniform-partition sample at |z|≈4·10⁴ (the smallest witness: n=2 cycles (1,1)↔(2)). This is a deterministic dynamical system on partitions, not an impartial-game Grundy value.

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** fleet · combinatorial dynamics / integer partitions / Bulgarian solitaire
**Proposal:** 251 → Verdict 264 (+13 offset)
**Verifier:** [`verify_251_bulgarian_solitaire.py`](verify_251_bulgarian_solitaire.py) · stdlib only (json, hashlib, math, random) · SEED=20260717
**Digest:** `results_sha256 = f9fdd4c7a787d5b559248f8897ca00d82fa3e556535f67fd552a6854e0b19537`

## What this proposal does

Adds a fleet PROPOSAL establishing the **triangular-number fixed-point law** of **Bulgarian solitaire** — a deterministic dynamical system on the finite set of **integer partitions** of `n`. A partition is a multiset of positive pile sizes; the **move** is:

> remove one card from **every** pile, then collect the removed cards into **ONE** new pile whose size = the number of piles you had (piles that hit zero vanish).

Formally, for `p = (p₁ ≥ … ≥ p_m)` with `m = len(p)` piles, `step(p) = sort_desc([x−1 for x in p if x−1>0] + [m])`. Then:

1. if `n` is **triangular**, `n = T_k = k(k+1)/2`, then from **EVERY** partition of `T_k` the iteration **converges** to the **unique period-1 fixed point**, the **staircase** `δ_k = (k, k−1, …, 2, 1)`;
2. the **maximum** number of steps to reach `δ_k`, taken over **ALL** partitions of `T_k`, is **EXACTLY `k²−k`** (Wikipedia states "`k²−k` moves or fewer" — an upper bound; the **exact tightness**, that some partition attains it with equality, is derived here by full enumeration);
3. if `n` is **not** triangular, **no** fixed point exists — every orbit lands in a **limit cycle of period > 1**.

**Headline instance (k=6, n=T_6=21):** all **792** partitions of 21 converge to `δ_6 = (6,5,4,3,2,1)`; the max steps over all 792 is `M(6) = 30 = 6²−6`, and a uniform-random partition takes on average `μ ≈ 20.17` steps (`σ ≈ 8.47`). **Smallest non-triangular witness (n=2):** the two partitions `(2)` and `(1,1)` form the period-2 cycle `(1,1) → (2) → (1,1)` — no fixed point. **Fleet framing:** a redistribution rule where each active lane sheds one unit per tick and the shed units seed a new lane sized to the lane-count; on a triangular budget the fleet provably relaxes to the staircase within a hard `k²−k` horizon, and on a non-triangular budget it never settles (it orbits) — a clean settle-vs-orbit dichotomy keyed purely on whether the total is triangular. The proposal ships a stdlib-only firsthand verifier that (i) enumerates ALL partitions of `T_k` for `k=1..8` and matches `M(k)` to `k²−k` exactly (0 nonconvergent), (ii) confirms the enumerated population mean/std of step-counts against a uniform-sampler Monte-Carlo draw, (iii) shows the invariants — card-total conservation at every step and pile-order-invariance of the map — and (iv) **falsifies** the "non-triangular n also has a unique fixed point" foil.

**Distinctness.** This is a **deterministic self-map on integer partitions** and its **orbit structure**, NOT an impartial-combinatorial-game Grundy value. There is no second player, no XOR/nim-sum, no `mex`, no game tree — the object is the orbit of a fixed map and the conserved quantity is the card total `n`. It is orthogonal to every shipped game head: Sprague-Grundy nim-sum (P219), Wythoff (P239), Green Hackenbush (P247), Fibonacci-Nim (P243), Penney, and the Banzhaf/Shapley power-index heads. `Bulgarian`, `solitaire`, `staircase`, `triangular fixed point`, `k^2-k` on partitions is **grep-0** as a head across both repos.

## Method

Exact integer enumeration first, uniform-sampler Monte-Carlo second.

**Dynamical system (exact, integer arithmetic).** `bulgarian_step(p)` implements the move on a descending tuple; `partitions(n)` generates ALL partitions of `n` as descending tuples in a deterministic order; `orbit_to_cycle(p)` iterates with a `seen`-dict `{state: index}` and, on the first repeat, returns `(steps_to_first_cycle_state, canonical_cycle, period)` (the cycle canonicalized to its lexicographically smallest rotation so it is invocation-stable); `steps_to_fixed_point(p, target)` counts steps until `state == target`, guarded by a `MAX_ITER` cap. The fixed point `δ_k = staircase(k) = (k, …, 1)` is a **period-1** point: `bulgarian_step(δ_k) == δ_k` (decrement to `(k−1, …, 1, 0)`, drop the 0, append a new pile of size `k` → `(k, …, 1)`).

**Uniform partition sampler (Nijenhuis–Wilf RANPAR).** `partition_counts(n)` precomputes `p(0..n)` by the standard DP recurrence. `ranpar(n, pcount, rng)` samples a partition of `n` **uniformly**: with `m` cards remaining, pick a pair `(i, d)` with `i·d ≤ m` with probability `i·p(m−i·d)/(m·p(m))`, append `d` parts of size `i`, set `m ← m − i·d`, repeat until `m = 0`. Because the step-count of a **uniform-random partition** is an **iid** draw (each sample is an independent partition, not a step along one autocorrelated path), the plain iid z-test is the honest one — **no** batch-means / thinning (that is only for autocorrelated Markov sample paths, which this is not). A correct uniform sampler MUST reproduce the enumerated population mean within the accept band; a wildly-off `z` would indict the sampler, not the theorem.

## Exact reference

Full enumeration, exact integer arithmetic, `k = 1..8` (`n = T_k` up to 36). `M(k)` = max steps-to-fixed-point over ALL partitions of `T_k`:

| k | n = T_k | staircase δ_k | num partitions | M(k) = max steps | k²−k | match |
|---|---|---|---|---|---|---|
| 1 | 1 | (1) | 1 | 0 | 0 | ✓ |
| 2 | 3 | (2,1) | 3 | 2 | 2 | ✓ |
| 3 | 6 | (3,2,1) | 11 | 6 | 6 | ✓ |
| 4 | 10 | (4,3,2,1) | 42 | 12 | 12 | ✓ |
| 5 | 15 | (5,4,3,2,1) | 176 | 20 | 20 | ✓ |
| 6 | 21 | (6,5,4,3,2,1) | 792 | 30 | 30 | ✓ |
| 7 | 28 | (7,…,1) | 3718 | 42 | 42 | ✓ |
| 8 | 36 | (8,…,1) | 17977 | 56 | 56 | ✓ |

**Nonconvergent partitions across all k: 0.** Every one of the `1+3+11+42+176+792+3718+17977` enumerated partitions reaches its staircase, and the max is exactly `k²−k` for every `k`. Smallest non-triangular contrast (period > 1, no fixed point): `n=2`, cycle `(1,1) → (2) → (1,1)` (period 2).

## Four gates (each in its own direction)

- **G1 — EXACT (integer arithmetic, zero tolerance).** For `k=1..8`, enumerate ALL partitions of `T_k`; for each, run `steps_to_fixed_point` to `δ_k`; count `nonconvergent` (must be 0) and record `M(k) = max steps`; assert `M(k) == k²−k` exactly. The enumeration route (max over all orbits) and the closed-form `k²−k` route are independent; their exact agreement is the teeth. **total_nonconvergent = 0**, all `M(k)` match (`0,2,6,12,20,30,42,56`). `z` is not applicable and is reported `null` / `"exact"`. PASS.
- **G2 — Monte-Carlo agreement (`|z| < 3`).** At `k=6` (`n=21`, `792` partitions), full enumeration gives the exact population mean `μ = 20.167929` and std `σ = 8.471034` of steps-to-fixed-point. Draw `N_mc = 40000` partitions of `T_6` **uniformly** with RANPAR (seeded); sample mean `x̄ = 20.167375`; `z = (x̄ − μ)/(σ/√N) = −0.0131`, `|z| < 3` [Z_ACCEPT = 3.0]. **convergence_rate = 1.000000** (100% of sampled partitions reach `δ_6` within `k²−k = 30` steps). iid partition draws are **not** autocorrelated → plain iid SE is honest (no batch means). PASS.
- **G3 — invariance (exact, 0 mismatches).** (a) **Conservation:** over ALL orbits of ALL enumerated partitions (`k=1..8`), assert `sum(step(p)) == sum(p)` at **every** step — `908472` steps checked, **0 violations** (the card total `n` is the conserved invariant). (b) **Order-invariance:** for a seeded sample of `1400` partitions, apply `bulgarian_step` to a randomly **shuffled** tuple representation and confirm the sorted result equals stepping the canonical descending tuple — **0 mismatches** (the map is a function of the multiset, not of pile order). PASS.
- **G4 — falsifiability (reject at large `|z|`, OPPOSITE polarity to G2).** Pre-registered naive foil: *"non-triangular n also converge to a unique period-1 fixed point, just like triangular n."* REFUTED. (i) **Exact witness:** for each non-triangular `n` in `2..25` (excluding `{1,3,6,10,15,21}` → 19 values), enumerate partitions and find limit cycles; **all 19** exhibit a period>1 cycle, and the smallest is `n=2` with cycle `(1,1) → (2)`. (ii) **MC z:** draw `N=40000` (random non-triangular `n`, RANPAR partition) pairs, iterate each to its cycle; fraction landing in a period>1 cycle `f = 1.000000` (the foil predicts `f=0`); the observed rate sits `z_foil = 40000.5000` SE above the foil-null of 0 (SE floored at a single-event boundary since `f=1` exactly), `|z_foil| ≫ 6` [Z_REJECT = 6.0]. PASS (foil rejected, ≥1 exact witness cycle found).

All four gates PASS; `all_pass = true`, `first_failing_gate = null`, `results_sha256 = f9fdd4c7a787d5b559248f8897ca00d82fa3e556535f67fd552a6854e0b19537`. Deterministic three ways: in-process double-run byte-identical (`in_process_double_run: IDENTICAL`), a `--selfcheck` path printing `SELFCHECK: byte-identical`, and a separate-process re-invocation byte-identical. `random.seed(SEED)` is re-seeded at the START of each MC gate so gate order does not perturb the payload. SEED = 20260717 (hardcoded module constant). Verifier file sha256 `a317b1f8a61826cb96cf62c6beffb2c0e8c1762b16840c1c87d9d2bb35fdf326`.

## Grounding

One pinned Wikipedia revision (MediaWiki API `revisions.sha1` == self-computed `hashlib.sha1` of the raw wikitext — exact match):

- **"Bulgarian solitaire"**, oldid 1340511625:
  `https://en.wikipedia.org/w/index.php?title=Bulgarian_solitaire&oldid=1340511625@f5566931386c46e2b0d37407d24ac25fa8dcd9a3` (2385 bytes), fetched 2026-07-21. API `sha1 = f5566931386c46e2b0d37407d24ac25fa8dcd9a3`; self-computed `hashlib.sha1(rawwikitext) = f5566931386c46e2b0d37407d24ac25fa8dcd9a3` — **match**.

**Quoted** literally on the pinned revision (grep count > 0):
- The **move / rules** — "for each pile, remove one card; collect the removed cards together to form a new pile (piles of zero size are ignored)".
- The **triangular-number convergence to the staircase** — "If `N` is a triangular number (that is, `N=1+2+⋯+k` for some `k`), then it is known that Bulgarian solitaire will reach a stable configuration in which the sizes of the piles are `1,2,…,k`" (grep `triangular` = 3, `1,2,\ldots, k` = 1, `stable configuration` = 2).
- The **`k²−k` bound** — "This state is reached in `k²−k` moves or fewer" (grep `k^2-k` = 1). **The bound is literally on the page, stated as an upper bound.**
- The **non-triangular limit cycle** — "If `N` is not triangular, no stable configuration exists and a limit cycle is reached" (grep `limit cycle` = 1).
- The name **Bulgarian solitaire** (grep 7); the Gardner attribution.

**Derived** firsthand (grep count 0 on the pinned raw wikitext): the **exact tightness** of the bound — that the max over all partitions of `T_k` is **EXACTLY** `k²−k` (the page says "or fewer", an upper bound; equality-attainment is enumerated here); the per-`k` `M(k)` values `{0,2,6,12,20,30,42,56}` and partition counts; the population mean/std of step-counts (`μ=20.17`, `σ=8.47` at `k=6`); the RANPAR uniform sampler and the Monte-Carlo agreement; the full enumeration of period>1 cycles for non-triangular `n`; the `n=2` witness cycle; every z-value; SEED 20260717; and the results digest. The word **"partition"** is itself **grep 0** on the page (it says "piles" / "divided into several piles").

**Honest posture — disclosed seams.** (1) The article is **thin** (2385 bytes): it states the triangular-convergence result and the `k²−k` **upper bound** in one sentence each and cites Akin–Davis (1985) and Gardner (1983), but carries **no proof, no per-`k` step counts, and no tightness claim** — so the load-bearing firsthand contribution is the **exact enumeration** proving `M(k) = k²−k` with equality for `k=1..8` and `0` nonconvergent, plus the invariance and falsifiability legs. (2) The word "partition" is grep 0 (the page says "piles"); "period-1 / period>1", "staircase", "fixed point", and "order statistic" are my labels for the standard construction, not literally on the page. Nothing oversold as novel: Bulgarian solitaire and the triangular fixed-point result are textbook (Gardner 1983; Akin–Davis, *Amer. Math. Monthly* 1985; the pinned page), cited as such; the exact `M(k) = k²−k` tightness enumeration, the conservation + order-invariance legs, the uniform-sampler MC agreement, the non-triangular-cycle falsification, and every z-value + the digest are the firsthand contribution.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 enumerates ALL partitions of `T_k` for `k=1..8` (up to 17977 partitions at `k=8`) in exact integer arithmetic, iterates each orbit to the staircase, and finds `M(k)` equal to `k²−k` for **every** `k` (`0,2,6,12,20,30,42,56`) with **0** nonconvergent. The enumeration route (max over all orbits) and the closed-form `k²−k` route are independent, and they agree with equality — the article only guarantees "`k²−k` or fewer", so the exact tightness is a genuine firsthand strengthening, not a fit.

**2. Could the numbers be an artefact of the sampler rather than the dynamics?** No. The exact law (G1) is fixed before any RNG is touched — it is full enumeration, not sampling. The Monte-Carlo gate (G2) only *confirms* the enumerated population mean/std of step-counts (`μ=20.167929`, `σ=8.471034` at `k=6`), and even there the target comes from exhaustive enumeration of all 792 partitions; the uniform RANPAR sample reproduces it at `z = −0.0131`, deep inside the accept band, with 100% convergence — evidence the sampler is correct, not that the dynamics are sampled.

**3. What is the most plausible wrong belief this could be confused with?** That **non-triangular** `n` also settle to a unique fixed point (the "it always converges" over-generalization) — pre-registered as G4 and refuted: all 19 non-triangular `n` in `[2,25]` have a period>1 cycle, `100%` of sampled orbits land in one (`f=1.0`, `|z_foil| ≈ 4·10⁴`), and the smallest witness `n=2` cycles `(1,1) ↔ (2)`. A secondary confusion — that this is an impartial-game Grundy head — is addressed by the distinctness note: there is no opponent, no nim-sum, no `mex`; it is an orbit of a fixed map with conserved total `n`.

**4. Is the verifier deterministic and self-checking?** Yes. `build_results()` is a pure function of SEED and the module constants; `random.seed(SEED)` is re-seeded at the START of each MC gate so gate order cannot perturb the payload; cycles serialize as their lexicographically-smallest rotation, every float via a fixed `f"{x:.6f}"` / `f"{z:.4f}"` string, counts as ints — no wall-clock / PID / unordered-set iteration enters the hashed payload. `main()` asserts an in-process double-run is byte-identical, `--selfcheck` prints "SELFCHECK: byte-identical", and two separate invocations reproduce the digest byte-for-byte. Whole-dict `results_sha256 = f9fdd4c7a787d5b559248f8897ca00d82fa3e556535f67fd552a6854e0b19537`.

**5. Does the grounding actually support the claim, or is it overstated?** Honest and tight, seams disclosed. The move, the triangular-convergence-to-staircase result, the `k²−k` **upper bound**, and the non-triangular limit cycle are all QUOTED on the pinned revision; the article is thin (no proof, no step counts, no tightness). Disclosed: the page says "`k²−k` or fewer" (upper bound) while this proposal's **exactness** (equality-attainment) is DERIVED by enumeration; the word "partition" is grep 0 (the page says "piles"); "staircase"/"fixed point"/"period" are my labels. The per-`k` `M(k)` values, `μ/σ`, the RANPAR MC, the non-triangular cycle census, every z-value, and the digest are DERIVED.

**6. Does it scale / is it robust?** The dynamical-system code is general — `bulgarian_step`, `partitions`, `orbit_to_cycle`, `steps_to_fixed_point`, and `ranpar` take arbitrary `n`. G1 exercises `k=1..8` (`n` up to 36, 17977 partitions); G3 checks conservation over `908472` steps across every enumerated orbit and order-invariance over `1400` shuffled samples; G4 censuses all 19 non-triangular `n` in `[2,25]`. The result is a property of the partition set and the map, not of a hard-coded orbit — the max is read off the full enumeration and equals `k²−k` at every `k`.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the single most plausible over-generalization ("non-triangular n also has a unique fixed point") and refutes it on both exact (all 19 `n` have a period>1 cycle) and Monte-Carlo (`f=1.0`, `|z_foil| ≈ 4·10⁴`) evidence, while G2 confirms the triangular case agrees with the enumerated mean at `z=−0.0131`. A wrong step rule, an off-by-one in the "new pile = number of piles" count, or a non-tight bound would break the exact G1 identity or push a G2 `z` out of band.

**8. Any residual risk before ruling?** The Monte-Carlo legs are **iid** partition-draw estimators (not autocorrelated sample paths), so the plain iid SE is the honest one and batch means are deliberately *not* used — stated explicitly in the verifier docstring; the exact enumeration (G1) is what carries the claim and is RNG-free with two independent routes (max-over-orbits vs closed-form `k²−k`). For G4's `f=1` boundary the SE is floored at a single-event rate (rule-of-three / Laplace style) so `z_foil` is finite, principled, and clearly `≫ 6` rather than a divide-by-zero. Bulgarian solitaire and the triangular fixed-point result are textbook (Gardner 1983; Akin–Davis 1985; the pinned page) and cited as such; the exact `M(k)=k²−k` tightness, the invariance legs, the MC agreement, the non-triangular falsification, and every z-value + the digest are the firsthand contribution. The paired sim-lab VERDICT 264 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
