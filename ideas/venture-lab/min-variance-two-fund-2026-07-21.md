# Markowitz global minimum-variance portfolio & two-fund separation: for n assets with SPD covariance Σ the least-variance fully-invested portfolio is w*=Σ⁻¹𝟙/(𝟙ᵀΣ⁻¹𝟙) with variance 1/(𝟙ᵀΣ⁻¹𝟙) — for Σ=[[4,1/2],[1/2,1]] w*=(1/8,7/8), σ*²=15/16 — beating both naive equal-weight (3/2) and the best single asset (1), with efficient weights affine in target return

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** venture-lab · portfolio optimization / mean-variance identity
**Proposal:** 242 → Verdict 255 (+13 offset)
**Verifier:** [`verify_242_min_variance_two_fund.py`](verify_242_min_variance_two_fund.py) · stdlib only · SEED=20260717
**Digest:** `results_sha256 = 3c1ec97050d0ca481e084976055ce3ea0e435c86b794e909507757e3eedf3f9c`

> **Grounding:** https://en.wikipedia.org/w/index.php?title=Modern_portfolio_theory&oldid=1359858554@7936722ffb730765fc0172ef339b5fd19b40bbf8 · fetched 2026-07-21

## Claim

For **n risky assets** with a symmetric positive-definite (SPD) covariance
matrix **Σ**, the **global minimum-variance (GMV) portfolio** — the
fully-invested portfolio (weights sum to 1) of least return variance — has
weights and variance

    w* = Σ⁻¹𝟙 / (𝟙ᵀΣ⁻¹𝟙),      σ*² = 1 / (𝟙ᵀΣ⁻¹𝟙),

where 𝟙 is the all-ones vector. Equivalently, at the optimum **every asset's
marginal contribution to variance is equalised**: (Σw*)_i = σ*² for every i.
For two assets (variances s₁², s₂², covariance s₁₂):

    w₁* = (s₂² − s₁₂)/(s₁² + s₂² − 2s₁₂),   σ*² = (s₁²s₂² − s₁₂²)/(s₁² + s₂² − 2s₁₂).

Headline exact rationals for **Σ = [[4, 1/2], [1/2, 1]]** (variances 4 and 1,
covariance 1/2, correlation 1/4):

- **w* = (1/8, 7/8)** and **σ*² = 15/16.**

The GMV variance 15/16 is **strictly below even the lower-variance single asset**
(asset 2, variance 1) and far below the **naive equal-weight** portfolio
(variance 3/2). Diversification buys a portfolio *safer than any of its
ingredients*.

This **refutes two naive foils**, each evaluated on the same Monte-Carlo sample:

- **(F1) "equal weights 1/n are optimal (naive diversification)."** The 1/2:1/2
  portfolio has variance 3/2 ≠ 15/16.
- **(F2) "just hold the single lowest-variance asset."** Asset 2 has variance
  1 > 15/16, so the diversified GMV strictly dominates it.

**Two-fund separation:** the mean-variance efficient weight vector w(m) at target
mean return m is **affine in m**, w(m) = g + h·m, so every efficient portfolio is
an exact affine combination of two fixed funds.

## Exact reference

For Σ = [[4, 1/2], [1/2, 1]]:

| quantity | value |
|---|---|
| GMV weights w* | (1/8, 7/8) |
| GMV variance σ*² | 15/16 = 0.9375 |
| lower-variance single asset (asset 2) | 1 |
| naive equal-weight (1/2:1/2) variance | 3/2 = 1.5 |
| GMV vs best single asset | 15/16 < 1 (strict) |
| GMV vs equal-weight | 15/16 < 3/2 (strict) |

The GMV variance 15/16 sits **below** the best single asset's variance 1 — the
signature of genuine diversification: a fully-invested long/short-free portfolio
(both weights positive: 1/8, 7/8) whose variance undercuts every one of its
constituents.

## Why it holds

Two textbook facts compose exactly:

- **Constrained minimisation of a quadratic form.** Minimising w^TΣw subject to
  the fully-invested constraint 𝟙ᵀw = 1 is a Lagrange problem; the stationarity
  condition is Σw = λ𝟙, so w ∝ Σ⁻¹𝟙, and normalising 𝟙ᵀw = 1 fixes the constant,
  giving w* = Σ⁻¹𝟙/(𝟙ᵀΣ⁻¹𝟙). Then σ*² = w*ᵀΣw* = 1/(𝟙ᵀΣ⁻¹𝟙).
- **First-order equalisation.** Σw* = λ𝟙 says (Σw*)_i is the SAME scalar for
  every i, and dotting with w* gives that scalar = σ*². So at the GMV every
  asset's marginal variance contribution is equal — the FOC-equalisation form.

**Two-fund separation** follows because the parametric efficient problem
(minimise w^TΣw subject to Rᵀw = m and 𝟙ᵀw = 1) has a Lagrange linear system
whose solution w(m) is affine in the parameter m: w(m) = g + h·m for fixed
vectors g, h. Hence any two distinct frontier portfolios span the whole frontier
by affine combination, and the GMV is recovered on that frontier at m = B/A
(A = 𝟙ᵀΣ⁻¹𝟙, B = 𝟙ᵀΣ⁻¹R).

## Four gates (each in its own direction)

- **G1 — exact identity (`fractions.Fraction`).** (w*, σ*²) computed two
  independent exact ways — the two-asset closed form and the general matrix form
  via an exact Fraction Gauss-Jordan solve of Σx = 𝟙 — agree bit-for-bit
  (w* = (1/8, 7/8), σ*² = 15/16). Across a 2/3/4-asset SPD panel the FOC
  (Σw*)_i == σ*² holds for every i and 𝟙ᵀw* == 1 exactly. `error_count = 0`.
- **G2 — Monte-Carlo agreement.** N = 200 000 **iid** return vectors with
  covariance exactly Σ (Cholesky map L = [[2,0],[1/4, √15/4]] of iid standard
  normals); the realised sample variance of the GMV portfolio, s²_gmv =
  0.9389802396, agrees with σ*² = 0.9375 at z = **0.4992990385**, |z| < 3
  (Z_ACCEPT = 3.0). Because the draws are iid (not a correlated sample path), the
  Gaussian sample-variance standard error SE = σ²·√(2/N) is honest with **no
  thinning required** — in contrast to the queueing gates whose arrival-to-arrival
  autocorrelation forces thinning.
- **G3 — invariance / robustness (two own directions).** (i) **Scale-equivariance:**
  Σ → kΣ (k = 4) leaves w* identical and scales σ*² by exactly k
  (Fraction-exact), and the MC z is byte-identical under the √k sample-path
  rescaling (mc_z_base = mc_z_scaled = 0.4992990385). (ii) **Two-fund
  separation:** on a 3-asset frontier w(m) is affine in m, verified exactly by
  w(m_C) == α·w(m_A) + (1−α)·w(m_B) with α = 1/2 (m_A,m_B,m_C = 1,3,2), each
  w(m) summing to 1, and the GMV recovered on the frontier at m = B/A. All exact.
- **G4 — falsifiability (own direction, on the SAME MC sample).** The naive
  "equal weights are optimal" (variance 3/2) is rejected at z_eq =
  **191.0595200324** and the naive "hold the single lowest-variance asset"
  (variance 1) at z_a2 = **21.4684726468**, both |z| ≥ 6 (Z_REJECT = 6.0); and
  exactly 3/2 ≠ 15/16 and 1 ≠ 15/16.

All four gates PASS; `all_gates_pass = true`, `first_failing_gate = null`,
`decision = PASS`, `results_sha256 =
3c1ec97050d0ca481e084976055ce3ea0e435c86b794e909507757e3eedf3f9c`. Deterministic:
in-process double-run and separate re-invocation byte-identical; `--selfcheck`
prints "SELFCHECK: byte-identical".

## Grounding

**Modern portfolio theory** (Wikipedia), pinned current revision:
`https://en.wikipedia.org/w/index.php?title=Modern_portfolio_theory&oldid=1359858554@7936722ffb730765fc0172ef339b5fd19b40bbf8`
(rev 1359858554, 2026-06-17T17:40:04Z, 59536 bytes; API `revisions.sha1` ==
self-computed `sha1sum` of the raw wikitext — exact match).

- **Quoted** literally on the pinned revision: the mean-variance objective —
  minimise `w^T Σ w` subject to `Σᵢ wᵢ = 1` (the fully-invested constraint,
  present verbatim) with Σ "the covariance matrix for the returns on the assets"
  and `w^T Σ w` "the variance of portfolio return"; the parametric efficient
  frontier and its **Lagrange-multiplier linear system** (the block matrix with
  `2Σ`, `R`, `𝟙`); the **Global Minimum Variance Portfolio (GMVP)**, "the vertex
  of the hyperbola … the portfolio with the lowest possible risk among all
  combinations of risky assets"; and the **two mutual fund theorem** ("also known
  as the separation theorem") — "any portfolio on the efficient frontier can be
  constructed as a linear combination of any two distinct portfolios already
  located on the frontier", `P_target = α P₁ + (1−α) P₂`, the tangent points
  "always falling on a single line".
- **Derived** firsthand (grep count 0 on the pinned raw wikitext): the *solved
  closed form* `w* = Σ⁻¹𝟙/(𝟙ᵀΣ⁻¹𝟙)` and `σ*² = 1/(𝟙ᵀΣ⁻¹𝟙)` — the page gives the
  Lagrange block-matrix *system* and a graphical/parametric solution, not the
  solved-out inverse-covariance formula (grep 0 for `Sigma^{-1}`); the
  FOC-equalisation `(Σw*)_i = σ*²`; the exact rational instances
  w* = (1/8, 7/8), σ*² = 15/16, equal-weight 3/2, single-asset 1 (grep 0 for
  "1/8", "7/8", "15/16", "3/2"); the two foil framings; and every z-value and the
  digest. Honest posture — the mean-variance objective, the fully-invested
  efficient-frontier Lagrange system, the GMVP concept, and the two-fund
  separation theorem are QUOTED textbook material on the single pinned page; the
  explicit inverse-covariance GMV closed form is standard textbook but derived
  here from that quoted system (not literally on the page); the exact rational
  instance, the FOC-equalisation, the scale-equivariance and two-fund exact
  checks, the iid Monte-Carlo agreement, and the two falsifications are the
  firsthand contribution. Nothing oversold as novel.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 computes
(w*, σ*²) two independent exact ways — the two-asset closed form and the general
matrix form via an exact `fractions.Fraction` Gauss-Jordan solve of Σx = 𝟙 — and
checks they are EQUAL rationals: w* = (1/8, 7/8), σ*² = 15/16, with the FOC
(Σw*)_i == σ*² holding exactly on every asset across the 2/3/4-asset panel and
𝟙ᵀw* == 1. No float tolerance touches the headline values.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?**
No. Every headline value (w* = (1/8,7/8), σ*² = 15/16, the 3/2 and 1 foils) is
fixed by exact rational arithmetic before any RNG is touched. The Monte-Carlo
gate (G2) only confirms the exact target survives under sampling: 200 000 iid
returns with covariance exactly Σ give s²_gmv = 0.9389802396 agreeing with
σ*² = 0.9375 at z = 0.4992990385 (< 3).

**3. What is the most plausible wrong belief this could be confused with?** Two,
both pre-registered in G4. "Equal weights 1/n are optimal" — the naive-diversification
guess that splitting evenly minimises risk; rejected at z ≈ 191 on the same
sample where 15/16 agrees at |z| < 1. And "just hold the single lowest-variance
asset" — the belief that diversification cannot beat the best ingredient;
rejected at z ≈ 21, and exactly 15/16 < 1, so the diversified GMV strictly
dominates.

**4. Is the verifier deterministic and self-checking?** Yes. The sampling gate
consumes a single seeded `random.Random(20260717)` in fixed order;
`build_results()` is a pure function of SEED and the module constants (no
wall-clock / PID / unordered-set iteration in the hashed payload). Exact
rationals serialize via `str(Fraction)` and every float via a fixed `f"{v:.10f}"`
string. `main()` asserts an in-process double-run is byte-identical, `--selfcheck`
prints "SELFCHECK: byte-identical", and a separate re-invocation reproduces the
digest byte-for-byte. Whole-dict `results_sha256 =
3c1ec97050d0ca481e084976055ce3ea0e435c86b794e909507757e3eedf3f9c`.

**5. Does the grounding actually support the claim, or is it overstated?** Honest
and explicitly split. The single pinned "Modern portfolio theory" revision
carries the mean-variance objective, the fully-invested constraint Σᵢwᵢ = 1, the
efficient-frontier Lagrange system, the GMVP concept, and the two mutual fund /
separation theorem verbatim — quoted. Flagged derived-not-quoted (grep count 0):
the *solved* inverse-covariance closed form w*=Σ⁻¹𝟙/(𝟙ᵀΣ⁻¹𝟙) (the page gives the
Lagrange system, not the solved formula), the FOC-equalisation, the exact
rationals (1/8, 7/8, 15/16, 3/2, 1), the foil framings, and the z-values/digest.
Neither oversold nor undersold.

**6. Does it scale / is it robust?** The claim is a closed-form identity valid
for every SPD Σ. G1 anchors it exactly across 2/3/4-asset SPD panels via the FOC
equalisation. G3 adds two robustness legs: scale-equivariance (Σ → kΣ leaves w*
identical and scales σ*² by exactly k — the GMV is a property of Σ's *shape*, not
its units) and two-fund separation (the efficient frontier is spanned affinely by
any two of its portfolios, verified exactly on a 3-asset frontier with the GMV
recovered at m = B/A).

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers two
plausible-but-wrong beliefs and refutes both on the same evidence: "equal weights
are optimal" (rejected at ≈191σ where 15/16 agrees at <1σ) and "hold the single
lowest-variance asset" (rejected at ≈21σ, and exactly 15/16 < 1). A dropped
inverse, a mis-normalised weight vector, or an off-by-one in the FOC test would
break the exact G1 identity or push the G2 z past the accept band.

**8. Any residual risk before ruling?** The Monte-Carlo returns are **iid
independent draws** (a fresh covariance-Σ Cholesky map per sample, not a
correlated sample path), so the Gaussian sample-variance standard error
SE = σ²·√(2/N) is honest with **no thinning needed** — unlike the M/M/c queueing
gates, whose arrival-to-arrival autocorrelation forces a THIN step to restore an
honest binomial SE. The exact identity (G1) is what carries the claim and is
RNG-free. The mean-variance objective, the efficient-frontier Lagrange system,
the GMVP, and the two-fund separation theorem are textbook (Markowitz; Merton;
the pinned MPT page) and cited as such; the firsthand contribution is the exact
rational instance, the two-route exact cross-check with FOC-equalisation, the
iid Monte-Carlo agreement, the scale-equivariance and two-fund exact legs, and
the two falsifications. The paired sim-lab VERDICT 255 reproduction is a separate
coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
