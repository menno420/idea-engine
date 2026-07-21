# Catalan numbers count non-crossing handshakes: a uniformly random perfect matching of 2n circle points is non-crossing with probability exactly C_n/(2n−1)!!

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** fleet · enumerative combinatorics / non-crossing perfect matchings (Catalan)
**Proposal:** 240 → Verdict 253 (+13 offset)
**Verifier:** [`verify_240_catalan_noncrossing.py`](verify_240_catalan_noncrossing.py) · stdlib only · SEED=20260717
**Digest:** `results_sha256 = 6b7c1a8ba3ca4a96e91ca5405c089cb037d3cf32d933fcf20b508e5f8faf24bf`

## Claim

Fix 2n points labelled 0, 1, …, 2n−1 in circular order on a circle. A **perfect matching** pairs them into n chords ("handshakes"); the number of perfect matchings is the odd double factorial

    (2n−1)!! = 1·3·5···(2n−1).

Draw a matching **uniformly at random**. The probability that it is **non-crossing** (no two chords cross) is exactly

    P(n) = C_n / (2n−1)!!,

where C_n = binom(2n,n)/(n+1) is the n-th Catalan number, because the number of non-crossing perfect matchings of 2n circle points is exactly C_n. Headline exact values:

- n = 2 → **2/3** (3 matchings, 2 non-crossing),
- n = 3 → **1/3** (15 matchings, 5 non-crossing),
- n = 4 → C_4 / 7!! = **14/105 = 2/15**.

The naive belief that "half of all matchings are planar", P = 1/2, is decisively wrong, and so is "the non-crossing count is 2^(n−1)" (2^(3−1) = 4 ≠ 5 = C_3).

## Exact reference

Catalan number three exact ways (all integer / `fractions.Fraction`, agreeing for n = 2…6):

    (a) recurrence  C_0 = 1,  C_{k+1} = Σ_{i=0}^{k} C_i · C_{k−1−i}
    (b) closed form C_n = binom(2n,n)/(n+1)          (Fraction, asserted integral)
    (c) difference  C_n = binom(2n,n) − binom(2n,n+1)

Two chords (a,b), (c,d) written with the smaller endpoint first (a < b, c < d) **cross** iff exactly one of {c, d} lies strictly inside the arc from a to b, i.e. iff a < c < b < d or c < a < d < b (standard interleaving test). A matching is non-crossing iff no pair of its chords crosses.

Brute-force enumeration of all (2n−1)!! matchings (sanity anchors):

| n | total = (2n−1)!! | non-crossing = C_n | P(n) = C_n/(2n−1)!! |
|---|---|---|---|
| 2 | 3   | 2  | 2/3  |
| 3 | 15  | 5  | 1/3  |
| 4 | 105 | 14 | 2/15 |

## Four gates (each in its own direction)

- **G1 — exact identity (closed form == brute force, exact rational via `fractions.Fraction`).** For n ∈ {2,3,4,5,6} the three Catalan routes (recurrence, binom(2n,n)/(n+1), binom(2n,n)−binom(2n,n+1)) agree exactly. For n ∈ {2,3,4} the code enumerates **all** perfect matchings of 2n labelled circle points, counts the non-crossing ones, and asserts total == (2n−1)!! and non-crossing == C_n, then asserts P_brute = Fraction(non_crossing, total) equals the closed form Fraction(C_n, (2n−1)!!) **exactly**. `error_count = 0`; P_exact = {2: 2/3, 3: 1/3, 4: 2/15}.
- **G2 — Monte-Carlo agreement.** MC_N = 200 000 uniform random matchings (greedy: pair the first unmatched point with a uniformly random other unmatched point — uniform over all (2n−1)!! matchings). For n = 3 (P = 1/3) the estimate agrees at z = **1.0262**; for n = 4 (P = 2/15) at z = **−0.8332**; both |z| < 3 [Z_ACCEPT = 3.0].
- **G3 — invariance / robustness.** Non-crossing is invariant under the dihedral action (rotation + reflection) on the circle labels. The n = 3 MC is re-run applying a random rotation r ∈ [0, 2n) and optional reflection to the labels each trial; it still agrees with P = 1/3 at z = **0.3336**, |z| < 3. PLUS, deterministically: for n ∈ {3, 4} the brute-force non-crossing COUNT is identical under **all** 2n rotations and reflection (exact equality to C_n) — `count_invariant = True` for both n = 3 and n = 4.
- **G4 — falsifiability.** On the SAME n = 3 MC sample, the plausible naive belief P_naive = 1/2 ("half of all matchings are planar") is rejected at z_naive = **−148.1037**, |z| ≥ 6 [Z_REJECT = 6.0], opposite polarity to G2. AND the naive "non-crossing count = 2^(n−1)" fails exactly: 2^(3−1) = 4 ≠ 5 = C_3.

All four gates PASS; `all_gates_pass = true`, `first_failing_gate = null`, `decision = PASS`. Deterministic: in-process double-run and separate re-invocation are byte-identical; `results_sha256 = 6b7c1a8ba3ca4a96e91ca5405c089cb037d3cf32d933fcf20b508e5f8faf24bf`.

## Grounding

Two pinned Wikipedia revisions (both API `revisions.sha1` == self-computed `sha1sum` of the raw wikitext — exact match):

- **"Catalan number"**, oldid 1365143256:
  `https://en.wikipedia.org/w/index.php?title=Catalan_number&oldid=1365143256@9a2c93a8caa3f7f97d47ef594333a08c98477011` (41 459 bytes).
- **"Double factorial"**, oldid 1350553238:
  `https://en.wikipedia.org/w/index.php?title=Double_factorial&oldid=1350553238@04250b93d9b17c83de37d85273794dd14acd939e` (29 346 bytes).

- **Quoted** literally on the pinned "Catalan number" revision: the closed form C_n = `\frac{1}{n+1}\binom{2n}{n}`; the recurrence `C_0 = 1` and `C_{n+1} = Σ_{i=0}^{n} C_i C_{n−i}`; the difference form `\binom{2n}{n} − \binom{2n}{n+1}`; the small values (the sequence `1, 1, 2, 5, 14, 42`, so C_2 = 2, C_3 = 5, C_4 = 14); and the non-crossing perfect-matching interpretation — verbatim: "C_n is also the number of **noncrossing partitions** of the set {1, …, 2n} in which **every block is of size 2**" (a non-crossing partition of {1,…,2n} into blocks of size 2 is precisely a non-crossing perfect matching).
- **Quoted** literally on the pinned "Double factorial" revision: (2n−1)!! = the number of **perfect matchings** of 2n points / **chord diagrams** ("sets of chords of a set of n+1 points evenly spaced on a circle such that each point is the endpoint of exactly one chord"), with the K4 example "a complete graph with four vertices … has three perfect matchings" and the K6 caption "fifteen different perfect matchings … counted by the double factorial 15 = (6 − 1)‼".
- **Derived** firsthand (grep count 0 on both pinned raw wikitexts): the word "handshake" (absent — the handshake framing is ours); the explicit interleaving crossing test a < c < b < d ∨ c < a < d < b; the probability statement P(n) = C_n/(2n−1)!! as a single formula (both facts are on the two pages separately; assembling them into the uniform-random probability is ours); the naive foils P = 1/2 and "count = 2^(n−1)"; every Monte-Carlo z-value (G2 z = 1.0262 / −0.8332, G3 z = 0.3336, G4 z_naive = −148.1037) and the results_sha256. Honest posture — the Catalan closed form / recurrence / small values / non-crossing-matching count and the (2n−1)!! = #matchings fact are QUOTED textbook material across the two pinned pages; the firsthand contribution is casting them as the exact uniform-random non-crossing **probability** C_n/(2n−1)!!, the brute-force enumeration cross-check, the exact rational identity, the dihedral-invariance leg, and the two falsifications. Nothing oversold as novel.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 enumerates every perfect matching of 2n points for n ∈ {2,3,4} and counts the non-crossing ones with the exact integer interleaving test; the counts are exactly C_n (2, 5, 14) out of (2n−1)!! (3, 15, 105), and P_brute = Fraction(non_crossing, total) equals Fraction(C_n, (2n−1)!!) exactly — 2/3, 1/3, 2/15. `error_count = 0`; no float enters G1.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?** No. The core equality is fixed by exact enumeration (G1) before any RNG is touched. The Monte-Carlo gates (G2/G3, 200 000 trials) only confirm the *frequency* under uniform sampling; the greedy sampler (pair the first unmatched point with a uniformly random partner) is provably uniform over all (2n−1)!! matchings, and G2 agrees at |z| < 1.1 for both n = 3 and n = 4.

**3. What is the most plausible wrong belief this could be confused with?** Two, both pre-registered in G4. "Half the matchings are planar" (P = 1/2) — superficially plausible symmetry intuition; rejected at |z| = 148 on the same n = 3 sample where 1/3 agrees at |z| < 1. And "the non-crossing count is 2^(n−1)" — fits nothing past the smallest case; 2^(3−1) = 4 ≠ 5 = C_3, exact.

**4. Is the verifier deterministic and self-checking?** Yes. Each Monte-Carlo stream consumes its own `random.Random(20260717)` in a fixed order; `build_results()` is a pure function of SEED and the module constants (no wall-clock / PID / unordered-set iteration in the hashed payload). `main()` asserts an in-process double-run is byte-identical, `--selfcheck` runs the whole computation twice and asserts byte-identical serialization, and two separate process invocations reproduce the digest byte-for-byte. Whole-dict `results_sha256 = 6b7c1a8ba3ca4a96e91ca5405c089cb037d3cf32d933fcf20b508e5f8faf24bf`.

**5. Does the grounding actually support the claim, or is it overstated?** Honest split across two pinned pages. The "Catalan number" revision carries the closed form, the recurrence, the difference form, the small values, and — crucially — the non-crossing perfect-matching count ("noncrossing partitions of {1,…,2n} in which every block is of size 2"). The "Double factorial" revision carries (2n−1)!! = #perfect matchings of points on a circle (chord diagrams), with the exact K4 "three matchings" and K6 "fifteen matchings" examples. The word "handshake", the interleaving crossing test, the assembled probability C_n/(2n−1)!!, the two foils, and every z-value are flagged derived-not-quoted. Neither oversold nor undersold.

**6. Does it scale / is it robust?** The claim is a closed-form probability valid for all n. G1 anchors the enumeration to n ∈ {2,3,4} (where (2n−1)!! is 3/15/105 — fully enumerable) and the Catalan identity to n ∈ {2,…,6}. G3 adds a robustness leg: the estimate is invariant under a random dihedral relabeling of the circle, and the exact non-crossing count is provably unchanged under all 2n rotations and reflection for n ∈ {3,4} — a check that the crossing test respects the circle's symmetry group.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers two plausible-but-wrong beliefs and refutes both: P = 1/2 (rejected at ~148σ on the same sample where 1/3 agrees at < 1σ) and count = 2^(n−1) (fails exactly at n = 3). Any wrong crossing test, a biased sampler, or an off-by-one in the enumeration would break the exact G1 identity or push the G2 z past the accept band.

**8. Any residual risk before ruling?** The brute-force enumeration is exhaustive only through n = 4 (105 matchings); the closed form C_n/(2n−1)!! is what generalises, and G1 anchors it to ground truth on every enumerable row while the Catalan identity is checked to n = 6. The Catalan / non-crossing-matching characterisation is textbook (Catalan, Stanley's *Enumerative Combinatorics*) and cited as such; the firsthand contribution is the uniform-random probability framing, the enumeration cross-check, the exact rational identity, the dihedral-invariance leg, and the two falsifications. The paired sim-lab VERDICT 253 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
