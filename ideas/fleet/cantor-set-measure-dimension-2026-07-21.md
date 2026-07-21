# Middle-thirds Cantor set: an uncountable set with Lebesgue measure EXACTLY 0 and Hausdorff = box-counting dimension EXACTLY log 2 / log 3 = ln2/ln3 ≈ 0.6309297535714574 — refuting the naive "you only ever remove one middle third, so ~2/3 survives" (measure 2/3) and the naive "an uncountable subset of the line must have dimension 1" (or a measure-zero dust dimension 0)

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** fleet · unrelated math / measure & fractal geometry
**Proposal:** 248 → Verdict 261 (+13 offset)
**Verifier:** [`verify_248_cantor_set.py`](verify_248_cantor_set.py) · stdlib only (json, hashlib, math, random, fractions) · SEED=20260717
**Digest:** `results_sha256 = 6303e32144742d019f280177b5119001b90e2e87a16d36ec0634a17460c9885e`
> **📊 Model:** Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Cantor_set&oldid=1342784138@b997266daad6f1819028b1da0adb13a18489ca6e · fetched 2026-07-21

## What this proposal does

Adds a fleet PROPOSAL in a domain OUTSIDE fleet/venture/game mechanics — real analysis and fractal geometry — establishing the two exact closed forms of the **middle-thirds Cantor set** `C = ∩ₙ Cₙ` (start from `[0,1]`; at every step delete the **open** middle third of each remaining closed interval, forever):

- **Lebesgue measure EXACTLY 0.** The level-`n` approximation `Cₙ` is a union of `2ⁿ` disjoint closed intervals each of length `3⁻ⁿ`, so `λ(Cₙ) = 2ⁿ·3⁻ⁿ = (2/3)ⁿ`, and `λ(C) = limₙ (2/3)ⁿ = 0`. Equivalently the **removed** set has full measure: `Σ_{k≥1} 2^{k−1}·3⁻ᵏ = 1`.
- **Hausdorff = box-counting dimension EXACTLY `d = log 2 / log 3 = ln2/ln3 ≈ 0.6309297535714574`.** `C` is the self-similar attractor of `N = 2` similarity maps of ratio `r = 1/3` satisfying the open-set condition, so the Moran equation `N·rᵈ = 1` gives `d = log₃(2)`. At resolution `ε = 3⁻ⁿ` the minimal box count is `N(ε) = 2ⁿ`, and the critical-dimension mass `N(ε)·εᵈ = 2ⁿ·3^{−nd} = 2ⁿ·2⁻ⁿ = 1` is EXACTLY bounded for every `n`.

The proposal ships a stdlib-only firsthand verifier that (i) proves the exact measure identity `λ(Cₙ) = (2/3)ⁿ` two independent ways in `fractions.Fraction`, (ii) confirms `P(x ∈ Cₙ) = (2/3)ⁿ` against a Monte-Carlo simulation of the actual ternary-digit membership test, (iii) shows the dimension and the surviving fraction are independent of resolution scale and of the ambient interval length, and (iv) **falsifies** two plausible-but-wrong beliefs. Fills a confirmed gap: the Cantor set (and `Hausdorff`, `fractal`, `box-counting`, `middle-third Cantor`) is **grep-0** across both repos and disjoint from every prior head in the unrelated-math lane — random-walk recurrence (P228), coprime density → 6/π² (P232), Burnside necklace (P236), non-crossing-matching Catalan (P240), Buffon's needle (P244), open-addressing probes (P245).

## Method

Exact rational arithmetic first, Monte-Carlo second.

**Measure (exact, two ways).** Route A rebuilds `Cₙ` literally: start with `[(0,1)]`, and at each level replace every `[a,b]` with `[a, a+(b−a)/3] ∪ [b−(b−a)/3, b]`, all endpoints exact `Fraction`; sum the interval lengths. Route B is the closed form `(2/3)ⁿ`. G1 asserts `route A == route B` for `n = 0…12` (`measure_mismatches = 0`), that `Cₙ` has exactly `2ⁿ` intervals each of length exactly `3⁻ⁿ` (`count_mismatches = 0`), and the telescoping removed-length identity `Σ_{k=1}^{n} 2^{k−1}·3⁻ᵏ == 1 − (2/3)ⁿ` (`removed_length_mismatches = 0`). The total removed length is exactly `1`, so the survivor measure is exactly `0`.

**Dimension (exact self-similarity + box counting).** `C` satisfies the Moran equation `2·(1/3)ᵈ = 1`, i.e. `3^{−d} = 1/2`, i.e. `d = log₃ 2 = ln2/ln3`. The verifier checks the algebraic residual `|2·(1/3)ᵈ − 1| < 1e-12` and, in G3, the exact box-count identity `N(3⁻ⁿ) = 2ⁿ` for `n = 1…20`, so the box dimension `log N(ε)/log(1/ε) = log(2ⁿ)/log(3ⁿ) = log2/log3` holds at **every** resolution, not merely in the limit.

**Monte-Carlo model (G2/G4).** One membership trial draws `n` **independent** uniform ternary digits, each `Uniform{0,1,2}` from `random.Random(20260717)`; the point lies in `Cₙ` iff no digit equals 1 (the pinned page's own criterion). Drawing `n` uniform ternary digits *is* sampling one uniform real in `[0,1]` to `n`-digit precision, and `Cₙ`-membership depends only on the first `n` digits, so `P(in Cₙ) = (2/3)ⁿ` exactly. Trials are **independent** (a fresh `n`-digit point per trial) — no autocorrelation, **no thinning**.

## Exact reference

`λ(Cₙ) = (2/3)ⁿ` computed as literal interval-subdivision and as the closed form agree bit-for-bit as `Fraction`. Sanity anchors reproduced exactly:

| n | intervals | interval length | λ(Cₙ) = (2/3)ⁿ | removed by level n |
|---|---|---|---|---|
| 0 | 1 | 1 | **1** | 0 |
| 1 | 2 | 1/3 | **2/3** | 1/3 |
| 2 | 4 | 1/9 | **4/9** | 5/9 |
| 3 | 8 | 1/27 | **8/27** | 19/27 |
| 6 | 64 | 1/729 | **64/729 ≈ 0.08779** | 665/729 |

`λ(Cₙ) = (2/3)ⁿ → 0`, so `λ(C) = 0` exactly; and `d = log 2 / log 3 = 0.6309297535714574`, with the critical-dimension mass `N(ε)·εᵈ = 1` for every `n` (dimension 1 sends it to `0`, dimension 0 sends it to `∞`).

## Four gates (each in its own direction)

- **G1 — EXACT identity (`fractions.Fraction`, zero tolerance).** Over `n = 0…12`: `λ(Cₙ)` by literal subdivision `==` closed form `(2/3)ⁿ` (`measure_mismatches = 0`); exactly `2ⁿ` intervals each of length `3⁻ⁿ` (`count_mismatches = 0`); telescoping removed-length `Σ 2^{k−1}3⁻ᵏ == 1 − (2/3)ⁿ` (`removed_length_mismatches = 0`); Moran residual `|2·(1/3)ᵈ − 1| = 0.0`. Anchors `(2/3)ⁿ ∈ {1, 2/3, 4/9, 8/27, 64/729}` pinned. `z` is not applicable and is reported `null` (exact gate).
- **G2 — Monte-Carlo agreement (`|z| < 3`).** Headline `n = 6`, `N = 500 000` i.i.d. ternary-digit points; `hits = 43778`, `p̂ = 0.087556` against `p = 64/729 ≈ 0.0877914952`; `z = −0.5884286072`, `|z| < 3` [Z_ACCEPT = 3.0]. Independent trials, no thinning.
- **G3 — invariance / robustness (own direction).** (a) Exact box-count identity `N(3⁻ⁿ) = 2ⁿ` for `n = 1…20` (`box_count_mismatches = 0`) so the dimension `= log2/log3 = 0.6309297535714574` at every resolution; the critical-mass `2ⁿ·3^{−nd} == 1` holds for all `n` (`critical_mass_mismatches = 0`). (b) Exact scale-invariance: building `Cₙ` on `[0,L]` gives `λ_L(Cₙ)/L == (2/3)ⁿ` for `L ∈ {1, 3, 5, 1/2, 100}`, `n = 0…8` (`scale_invariance_mismatches = 0`). (c) MC agreement at a **second** configuration `n = 4`, independent RNG stream (SEED+1), `N = 300 000`: `p̂ = second_config` vs `16/81`, `z = 0.0492540510`, `|z| < 3` — agreement across configs.
- **G4 — falsifiability (own direction, on the SAME G2 sample).** (i) The naive "you only ever remove one middle third, so ~2/3 survives" (`measure = 2/3`, ignoring that removal compounds every level) is **rejected** on the headline sample at `z_naive = −868.666` (`|z| ≫ 3`, Z_REJECT = 3.0) while the same sample **agrees** with the exact `64/729` at `z = −0.5884286072`. (ii) Exact analytic teeth: only `d = log2/log3` keeps `N(ε)·εˢ` bounded — at `n = 12`, `mass@dim1 = 0.0077 → 0` (dimension 1 refuted), `mass@dim0 = 4096 → ∞` (dimension 0 refuted), `mass@dim(log2/log3) = 1.0`.

All four gates PASS; `all_gates_pass = true`, `first_failing_gate = null`, `decision = PASS`, `results_sha256 = 6303e32144742d019f280177b5119001b90e2e87a16d36ec0634a17460c9885e`. Deterministic three ways: in-process double-run byte-identical; `--selfcheck` prints "in-process double-run BYTE-IDENTICAL"; a separate-process re-invocation reproduces the digest byte-for-byte. SEED = 20260717 (hardcoded module constant).

## Grounding

One pinned Wikipedia revision (API `revisions.sha1` == self-computed `sha1sum` of the raw wikitext — exact match):

- **"Cantor set"**, oldid 1342784138: `https://en.wikipedia.org/w/index.php?title=Cantor_set&oldid=1342784138@b997266daad6f1819028b1da0adb13a18489ca6e` (44004 bytes; `sha1 b997266daad6f1819028b1da0adb13a18489ca6e`, API-sha1 = self-computed-sha1 exact match).

- **Quoted** literally on the pinned revision (grep count > 0): "the Cantor set is **uncountable** but has **Lebesgue measure 0**" (measure zero / "zero measure", grep > 0; uncountable, grep 4); the **Hausdorff dimension `\log_3(2)`** — "the set has a **Hausdorff measure of `1` in its dimension of `\log_3(2)`**" (`log_3(2)`, grep 1); the **removed-length geometric progression** `Σ_{n=0}^∞ 2ⁿ/3^{n+1} = 1/3 + 2/9 + 4/27 + ⋯ = 1`, "so that the proportion left is `1 − 1 = 0`" (verbatim); the **construction** — deleting the open middle third `(1/3, 2/3)` from `[0,1]` leaving `[0,1/3]∪[2/3,1]`, then `[0,1/9]∪[2/9,1/3]∪[2/3,7/9]∪[8/9,1]` (verbatim); the **ternary digit criterion** — "those numbers with a ternary representation such that the first digit after the radix point is not 1 are the ones remaining after the first step" and "a ternary numeral where neither of the first two digits is 1" (verbatim); the general-removal facts `total removed = Σ 2^{n−1}rⁿ`, limiting measure `(1−3r)/(1−2r)`, decay `(1−f)ⁿ → 0`, and the Smith–Volterra–Cantor `r = 1/4` case with measure `1/2` (all grep 1).
- **Derived** firsthand (grep count 0 on the pinned raw wikitext): the explicit per-level survivor closed form `(2/3)ⁿ` written as such and computed two independent ways in `Fraction` (grep 0 for `(2/3)^n`); the **decimal** `0.6309297535714574` (grep 0 for `0.6309`/`0.630`/`0.631` — the page writes `\log_3(2)` symbolically only); the **box-counting** count `N(3⁻ⁿ) = 2ⁿ` and the **critical-mass identity** `2ⁿ·3^{−nd} = 1` (`box-count`/`Minkowski` grep 0 — the page states the *Hausdorff measure* is 1 at dimension `log₃2`, a related but distinct object I flag explicitly); the exact scale-invariance leg; all Monte-Carlo `z`-values (`Monte` grep 0); `SEED 20260717` (grep 0); the naive-`2/3` falsifier and the exact `dim ∈ {0,1}` refutation; and the digest. **Honest posture** — measure 0, the dimension `log₃(2)`, the removed-length sum = 1, the construction, and the ternary criterion are QUOTED on the pinned page; the per-level `(2/3)ⁿ` Fraction identity, the decimal dimension, the box-count/critical-mass identities, the scale-invariance leg, the MC agreement, both falsifications, every `z`-value, and the digest are the firsthand contribution. The page separately asserts the **Hausdorff measure** at dimension `log₃2` is exactly `1`; my critical-dimension **box-count product** `N(ε)·εᵈ = 1` is a distinct (box-counting) quantity that happens to equal 1 too — labeled DERIVED, not conflated with the page's Hausdorff-measure statement. Nothing oversold as novel: measure 0 and dimension `log₃2` are textbook (Cantor 1883; Hausdorff), cited as such.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 computes `λ(Cₙ)` two independent exact ways (literal subdivision vs closed form) entirely in `fractions.Fraction`, agreeing bit-for-bit over `n = 0…12` (`measure_mismatches = 0`), with the interval-count/length identity and the telescoping removed-length identity both at 0 mismatches. `λ(C) = lim (2/3)ⁿ = 0` and `d = log₃2` follow from the Moran equation `2·(1/3)ᵈ = 1` (residual `0.0`). No float enters the exact leg.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?** No. The exact measure/dimension identities (G1, G3-exact legs) are fixed before any RNG is touched. The Monte-Carlo gate (G2) only confirms the survival *probability* `(2/3)⁶ = 64/729` via the ternary-digit membership test; it lands at `|z| = 0.59`. The dimension is carried by the exact box-count identity `N(3⁻ⁿ) = 2ⁿ`, RNG-free.

**3. What is the most plausible wrong belief this could be confused with?** Two, both pre-registered in G4: (a) "you only ever remove one middle third, so ~2/3 of the mass survives" (measure `2/3`) — refuted at `|z| = 868.7` on the same sample; (b) "an uncountable subset of the line must have dimension 1" (or a measure-zero dust must have dimension 0) — refuted exactly by the critical-mass product (`dim 1 → 0`, `dim 0 → ∞`, only `log₃2 → 1`).

**4. Is the verifier deterministic and self-checking?** Yes. `random.Random(20260717)` instances are seeded inside `compute_results()` and consumed in a fixed order; the results dict is a pure function of SEED and module constants (no wall-clock / PID / unordered iteration in the payload). Exact rationals serialize via `str(Fraction)`; every float via `round(x, 10)`. The dict is canonical-JSON (`sort_keys=True`) hashed to `results_sha256 = 6303e32144742d019f280177b5119001b90e2e87a16d36ec0634a17460c9885e`. `--selfcheck` runs the pipeline twice and asserts byte-identical; two separate process invocations reproduce the digest byte-for-byte.

**5. Does the grounding actually support the claim, or is it overstated?** Honest and tight. The pinned "Cantor set" revision literally states measure 0 (uncountable, zero measure), the Hausdorff dimension `\log_3(2)`, the removed-length sum `= 1` with proportion left `0`, the explicit construction, and the ternary "first digit not 1" criterion. Derived-not-quoted (grep 0): the `(2/3)ⁿ` Fraction identity, the decimal `0.6309…`, the box-count/critical-mass identities (distinct from the page's Hausdorff-measure-1 statement, flagged), the scale-invariance leg, and every `z`-value. Neither oversold nor undersold.

**6. Does it scale / is it robust?** The claims are closed forms valid at every level `n` and every ambient length. G1 anchors `λ(Cₙ)` exactly to `n = 12`; G3 shows the box dimension `= log₃2` at every resolution `n = 1…20` (`box_count_mismatches = 0`) and the survivor fraction invariant to ambient length `L ∈ {1,3,5,1/2,100}` (`scale_invariance_mismatches = 0`), with a second MC config (`n = 4`) agreeing at `|z| = 0.05`.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the two most plausible wrong beliefs and refutes both: the naive `measure = 2/3` at `|z| = 868.7` (same sample agrees with `64/729` at `|z| = 0.59`), and the naive dimensions `{0, 1}` by the exact critical-mass product. A wrong middle-third polarity, an off-by-one in the digit test, or forgetting that removal compounds would break the exact G1 identity or push the G2 `z` out of band.

**8. Any residual risk before ruling?** The Monte-Carlo leg is i.i.d. Bernoulli per trial (one independent `n`-digit point each) so the binomial SE is honest with **no thinning**, stated in the docstring. The exact identities (G1, G3-exact) carry the claim and are RNG-free. Measure 0 and dimension `log₃2` are textbook and cited; the `(2/3)ⁿ` Fraction identity, box-count/critical-mass identities, scale-invariance, MC agreement, both falsifications, and the digest are the firsthand contribution. The paired sim-lab VERDICT 261 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
