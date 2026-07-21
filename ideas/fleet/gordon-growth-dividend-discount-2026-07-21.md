# Gordon growth / dividend-discount model: the present value of a growing perpetuity with first cashflow D1 at t=1, constant growth g and discount rate r (r>g>−1) is EXACTLY PV = D1/(r−g) — the closed sum of the geometric series Σ_{t≥1} D1(1+g)^{t−1}/(1+r)^t — while the naive level-perpetuity P = D1/r (which ignores growth) is provably wrong for g≠0 (at D1=1, r=1/10, g=4/100 the truth is 50/3≈16.667, not 10)

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** fleet · venture / valuation
**Proposal:** 246 → Verdict 259 (+13 offset)
**Verifier:** [`verify_246_gordon_growth_ddm.py`](verify_246_gordon_growth_ddm.py) · stdlib only (json, hashlib, math, random, fractions) · SEED=20260717
**File sha256:** `afdd5047a87a048bf86f8a4b1c13e0307da2826c914e616bedfe3b7e8b89da9f`
**Digest:** `results_sha256 = 3cb527ff7b7873d2bacb56dcb4eea6f490ef7817b67766f45696ab6d706230e4`

## What this proposal does

Adds a fleet PROPOSAL establishing the exact closed form for the **present value of a growing perpetuity** — the constant-growth **dividend-discount model**, a.k.a. the **Gordon growth model** (Gordon & Shapiro 1956; Williams 1938). A cashflow stream pays `D1` at `t=1` and grows at a constant rate `g` per period thereafter, discounted at rate `r` with `r > g > −1`. Its present value is **exactly**

    PV = D1 / (r − g),

the closed sum of the infinite geometric series `Σ_{t≥1} D1 (1+g)^{t−1} / (1+r)^t`. The proposal ships a stdlib-only firsthand verifier that (i) proves the exact identity in `fractions.Fraction` three independent ways (finite partial sum + exact tail, the fixed-point recurrence, and the closed form), (ii) confirms it against a Monte-Carlo simulation of a **stochastic-dividend DDM** whose per-period multiplicative shocks are mean-1, (iii) shows the value is invariant to the noise structure and **exactly** invariant to a common shift of `r` and `g`, and (iv) **falsifies** the plausible-but-wrong naive belief that the level-perpetuity `P = D1/r` (which ignores growth) values a growing stream. Fills a confirmed gap: gordon-growth / dividend-discount is grep-0 across both repos and orthogonal to the named prior venture heads — Markowitz GMV (P242), Kelly (P100), put-call parity (P234), newsvendor critical-fractile, St. Petersburg cap-collapse, Cournot/Stackelberg, Vickrey/revenue-equivalence — this is the exact closed-form valuation of a growing perpetuity, not a portfolio/auction/stopping object.

## Method

Exact rational arithmetic first, Monte-Carlo second. The present value of the growing perpetuity is the sum of the infinite series

    PV = Σ_{t≥1} D1 (1+g)^{t−1} / (1+r)^t
       = (D1 / (1+r)) · Σ_{k≥0} ρ^k ,   ρ = (1+g)/(1+r) < 1  (since r > g),
       = (D1 / (1+r)) · 1/(1 − ρ)
       = D1 / (r − g).

**Fixed-point recurrence.** The value satisfies `PV = D1/(1+r) + PV·(1+g)/(1+r)` — the first cashflow discounted one period, plus the same growing perpetuity one period later, itself grown by `(1+g)` and discounted. Solving gives `PV·(r − g) = D1`, i.e. `PV = D1/(r − g)`. The verifier checks this fixed point in exact `Fraction` (`cf == D1/(1+r) + cf·(1+g)/(1+r)`) alongside `cf·(r−g) == D1`.

**Finite-T residual identity.** Truncating at `T` terms leaves an exact geometric tail: `partial_sum(T) + PV·ρ^T == PV`, and the finite-horizon expectation of the Monte-Carlo target is `PV·(1 − ρ^T)`. G1 verifies `partial_sum(D1,r,g,T) + exact_tail(D1,r,g,T) == PV` over a 10-triple battery at `T = 60`, all in `fractions.Fraction`.

**Stochastic-dividend Monte-Carlo (G2).** The simulation multiplies each period's dividend by `(1+g)·ε` where `ε ∈ {1−δ, 1+δ}` with equal probability (mean-1, so `E[dividend_t] = D1(1+g)^{t−1}` unchanged), discounts by `(1+r)^t`, and sums over `T = 160` periods — one present-value draw per i.i.d. path, so the sample SE is honest with **no thinning**. The mean of `N` independent paths agrees with the exact finite-horizon target `PV·(1 − ρ^T)` at `|z| < 3`.

## Exact reference

The closed form, the fixed-point recurrence, and the finite-partial-sum-plus-exact-tail agree bit-for-bit over the battery as exact `fractions.Fraction`. Sanity anchors reproduced exactly:

| D1 | r | g | PV = D1/(r−g) exact | naive D1/r |
|---|---|---|---|---|
| 1 | 1/10 | 0 | **10** | 10 |
| 1 | 1/10 | 4/100 | **50/3 ≈ 16.667** | 10 |
| 6 | 1/10 | 2/100 | **75** | 60 |
| 3 | 1/5 | 1/20 | **20** | 15 |
| 2 | 12/100 | 5/100 | **200/7 ≈ 28.571** | 50/3 |

At `g = 0` the growing perpetuity collapses to the level perpetuity `D1/r` (first row, both 10) — the naive form is exact **only** there. For every `g > 0` the growing-perpetuity value `D1/(r−g)` sits strictly **above** `D1/r`, and the gap is precisely what G4 detects.

## Four gates (each in its own direction)

- **G1 — EXACT identity (`fractions.Fraction`, zero tolerance).** Over the 10-triple battery `{(1,1/10,0),(1,1/10,4/100),(6,1/10,2/100),(3,1/5,1/20),(2,12/100,5/100),(10,8/100,3/100),(5,7/100,−2/100),(100,15/100,6/100),(7/2,9/100,1/100),(1,1/4,1/10)}` the closed form `D1/(r−g)`, the reconstruction `partial_sum(T=60) + exact_tail(T=60)`, the fixed-point `cf·(r−g)==D1`, and the recurrence `cf==D1/(1+r)+cf·(1+g)/(1+r)` are **exactly equal** — `mismatches = 0`, `anchor_mismatches = 0`, **max discrepancy exactly 0** (z not applicable, reported `null` / `"exact"`). Anchors `(1,1/10,0)→10`, `(1,1/10,4/100)→50/3`, `(6,1/10,2/100)→75`, `(3,1/5,1/20)→20`, `(2,12/100,5/100)→200/7` pinned.
- **G2 — Monte-Carlo agreement (`|z| < 3`).** The stochastic-dividend DDM at the headline `(D1=1, r=1/10, g=4/100)` with `N = 100 000` i.i.d. mean-1-shock paths (`δ = 0.3`, `T = 160`) gives `mean_hat = 16.6681667254` against the exact finite-horizon target `PV·(1−ρ^160) = 16.6645563219` (infinite-horizon `E = 50/3 ≈ 16.6666666667`), `se = 0.088431733702`, `z = 0.0408270129`, `|z| < 3` [Z_ACCEPT = 3.0]. Independent paths, one PV draw each, **no thinning**.
- **G3 — invariance / robustness (own direction).** The value is invariant to the noise structure: a second noise configuration `B` (`δ = 0.5`, mean-1) at `SEED+1` gives `meanB = 16.662406346`, `zB = −0.0034001459`, against config `A`'s `zA = 0.0408270129`; the two independent samples agree with **each other** (two-sample `z = 0.0090221259`), all `|z| < 3`. The exact **shift-invariance** sub-check (own leg, `Fraction`): `D1/(r−g)` is unchanged under a common shift `(r,g) → (r+c, g+c)` for `c ∈ {1/100, 3/100, 1/2, −1/50}` across three triples — `shift_invariance_mismatches = 0` over the 12-case battery (the value depends only on the **spread** `r − g`, not on the levels).
- **G4 — falsifiability (own direction, on the SAME G2 sample).** The plausible naive alternative "value = level perpetuity `D1/r` (ignoring growth)" is **false** for `g ≠ 0`. On the same headline sample the truth is `50/3 ≈ 16.667` while the naive value is `D1/r = 10`; `z_naive = 75.4046816262`, **`|z| ≫ 3` REJECTED** [Z_REJECT = 3.0]. The same sample that **agrees** with the exact growing-perpetuity value (G2, `|z| = 0.04`) **rejects** the level-perpetuity foil — that is the teeth: ignoring growth undervalues a growing stream, exactly by the factor `r/(r−g)`.

All four gates PASS; `all_pass = true`, `first_failing_gate = null`, `decision = PASS`, `results_sha256 = 3cb527ff7b7873d2bacb56dcb4eea6f490ef7817b67766f45696ab6d706230e4`. Deterministic three ways: in-process double-run byte-identical (`main()` asserts it), a `--selfcheck` path printing `SELFCHECK OK: in-process double-run byte-identical`, and a separate-process re-invocation byte-identical. SEED = 20260717 (hardcoded module constant).

## Grounding

One pinned Wikipedia revision (API `revisions.sha1` == self-computed `sha1sum` of the raw wikitext — exact match):

- **"Dividend discount model"**, oldid 1345461329:
  `https://en.wikipedia.org/w/index.php?title=Dividend_discount_model&oldid=1345461329@4e3d4d4d29f5cc6486b0fa92fe5cca52c547f45b` (9106 bytes, fetched 2026-07-21).

- **Quoted** literally on the pinned revision (grep count > 0): the exact closed form `P = \frac{D_1}{r-g}` (grep `frac{D_1}` = 6; also `P_0 = \frac{D_0(1+g)}{r-g} = \frac{D_1}{r-g}`); the name "**Gordon growth model**" / "Gordon" (grep 6); the infinite **geometric series** `P_0 = \sum_{t=1}^{\infty} D_0 (1+g)^t/(1+r)^t` verbatim (a `D_0`-indexed writing of my `D_1(1+g)^{t−1}` series — equivalent since `D_1 = D_0(1+g)`); the variable glossary "`P` is the current stock price … `g` is the constant growth rate in perpetuity … `r` is the constant **cost of equity** capital … `D_1` is the value of dividends at the end of the first period"; "**perpetuity**" (grep 2); "growth rate" (grep 5); "cost of equity" (grep 5); the fixed-point rearrangement `\frac{D_1}{r-g}=P_0 \Rightarrow \frac{D_1}{P_0}+g=r` (line 31); `r-g` literal (grep 4) with "`r-g` cannot be negative"; and — critically for G4 — the zero-growth case `P_0 = \frac{D_1}{r}` presented on the page as the `g = 0` "dividend is capitalized" special case (grep 1).
- **Derived** firsthand (grep count 0 on the pinned raw wikitext): all exact rational instances — 10, 50/3, 75, 20, 200/7 (grep 0 for `50/3`, `200/7`, `101/31`); the finite-T residual identity `partial_sum(T)+PV·ρ^T=PV` and the finite-horizon MC target `PV·(1−ρ^T)`; the stochastic-dividend Monte-Carlo agreement; the mean-1-shock noise-structure invariance (configs A/B); the exact common-shift invariance `(r,g)→(r+c,g+c)`; the falsification of the level-perpetuity `D1/r` foil for `g ≠ 0`; and every z-value plus the digest.
- **Honest posture / relabeling disclosed.** The pinned page uses `P`/`P_0` (price) for what I call `PV` (present value) — the same object; `r` = "cost of equity capital" for what I call the discount rate (the article's "Yield-plus-growth" variant also writes it as `k`, `\frac{D_1}{k-g}`, grep `k-g` = 1); and it indexes the series as `D_0(1+g)^t` where I index `D_1(1+g)^{t−1}` (equivalent). The phrase "required rate of return" is **grep 0** (the article says "required total return" and cites a paper titled "Required Rate of Profit") — I do not claim it. The quoted formula sits specifically in the **constant-growth DDM / Gordon growth model** context. Note the naive `D1/r` that G4 rejects is not an error the page makes: the page presents `D1/r` correctly as the `g=0` case, and my firsthand contribution is the falsification that it **undervalues** a stream with `g > 0` (by the exact factor `r/(r−g)`). Nothing oversold as novel — the closed form and the series are textbook and cited as such; the exact instances, the finite-T identity, the stochastic-DDM MC agreement, the two invariance legs, the falsification, and every z-value + the digest are the firsthand contribution.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 computes the growing-perpetuity present value three independent exact ways — the closed form `D1/(r−g)`, the fixed-point `cf·(r−g)==D1` and recurrence `cf==D1/(1+r)+cf·(1+g)/(1+r)`, and the finite partial sum plus exact geometric tail `partial_sum(60)+exact_tail(60)` — entirely in `fractions.Fraction`, and they agree bit-for-bit over a 10-triple battery (`mismatches = 0`). The anchors `50/3`, `75`, `20`, `200/7` are exact rationals, no float involved. The geometric-series sum supplies a closed proof, so the equality is a theorem, not a fit.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?** No. The exact identity (G1) is fixed before any RNG is touched. The Monte-Carlo gate (G2) only confirms the *mean present value* of a genuinely stochastic dividend stream (per-period mean-1 multiplicative shocks), landing at `|z| = 0.04` against the exact finite-horizon target `16.6645563219`. Because `E[ε] = 1`, the noisy stream has the same expected present value as the deterministic one — the sampler stresses the mechanism, it does not manufacture the answer.

**3. What is the most plausible wrong belief this could be confused with?** That the level-perpetuity `P = D1/r` values a growing stream — pre-registered as G4 and refuted on the same sample at `|z| = 75.4` (the true `50/3 ≈ 16.667` strictly exceeds the naive `10`). The naive form is exact only at `g = 0`; for `g > 0` it undervalues by the factor `r/(r−g)`.

**4. Is the verifier deterministic and self-checking?** Yes. Independent `random.Random(SEED)` and `random.Random(SEED+1)` streams are seeded once and consumed in fixed order; `build_results()` is a pure function of SEED and the module constants. Every float serializes via `round(v,10)`/`round(v,12)` and exact rationals via `Fraction`, so the bytes are stable. `main()` asserts an in-process double-run is byte-identical, `--selfcheck` prints "SELFCHECK OK: in-process double-run byte-identical", and two separate process invocations reproduce the digest byte-for-byte. Whole-dict `results_sha256 = 3cb527ff7b7873d2bacb56dcb4eea6f490ef7817b67766f45696ab6d706230e4`.

**5. Does the grounding actually support the claim, or is it overstated?** Honest and tight — this grounding is unusually direct. The pinned "Dividend discount model" revision carries the exact closed form `P=\frac{D_1}{r-g}`, the "Gordon growth model" name, the infinite geometric series, the variable glossary, and the zero-growth `P_0=\frac{D_1}{r}` — all quoted (grep > 0). Derived-not-quoted (grep 0): all exact instances, the finite-T identity, the stochastic-DDM MC agreement, both invariance legs, the falsification, and every z-value. Notation relabelings (`P`↔`PV`, cost-of-equity `r`↔discount rate, `k-g` variant, `D_0(1+g)^t`↔`D_1(1+g)^{t−1}`) are disclosed; "required rate of return" is explicitly grep 0.

**6. Does it scale / is it robust?** The claim is a closed-form present value valid for every `(D1, r, g)` with `r > g > −1`. G1 anchors it exactly across the battery. G3 adds two robustness legs specific to the object: invariance to the noise structure (configs A/B two-sample `|z| = 0.01`) and the exact shift-invariance — the value depends only on the spread `r − g`, not the levels of `r` and `g` (`shift_invariance_mismatches = 0` over 12 cases).

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the single most plausible wrong belief (level perpetuity `D1/r`) and refutes it on the same evidence at `|z| = 75.4`, while G2 shows that same sample agrees with the exact growing-perpetuity value at `|z| = 0.04`. A sign error in `(r−g)`, an off-by-one in the first-cashflow timing, or dropping the `(1+g)` growth would break the exact G1 identity or push a G2 z past the accept band.

**8. Any residual risk before ruling?** The Monte-Carlo leg draws one independent present-value per path (mean-1 shocks) so — unlike an autocorrelated queueing simulator — the reported sample SE is honest with **no thinning**, stated explicitly in the docstring. The exact identity (G1) is what carries the claim and is RNG-free, backed by the geometric-series closed form. The closed form and the series are textbook (Gordon & Shapiro 1956; Williams 1938; the pinned "Dividend discount model" page) and cited as such; the exact instances, the finite-T identity, the stochastic-DDM MC agreement, the two invariance legs, and the falsification of the level-perpetuity foil are the firsthand contribution. The paired sim-lab VERDICT 259 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
