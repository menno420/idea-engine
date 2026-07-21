# PROPOSAL 242 — Markowitz global minimum-variance portfolio & two-fund separation: for n assets with SPD covariance Σ the least-variance fully-invested portfolio is w*=Σ⁻¹𝟙/(𝟙ᵀΣ⁻¹𝟙) with variance 1/(𝟙ᵀΣ⁻¹𝟙) — Σ=[[4,1/2],[1/2,1]] gives w*=(1/8,7/8), σ*²=15/16 — beating naive equal-weight (3/2) and the best single asset (1), with efficient weights affine in target return

> **Status:** complete

> **📊 Model:** Claude Opus · high · idea/planning
started: 2026-07-21T06:10:00Z

💓 Heartbeat:
- round/slot: venture · portfolio optimization / mean-variance — the Markowitz GMV portfolio and two-fund separation, distinct from the risk-pooling diversification-law head and the IRR heads
- lane: P242 → V255 (+13 offset)
- branch: claude/proposal-242-min-variance-two-fund
- verifier: ideas/venture-lab/verify_242_min_variance_two_fund.py (stdlib only: json, hashlib, math, random, fractions)
- SEED: 20260717 · results_sha256: 3c1ec97050d0ca481e084976055ce3ea0e435c86b794e909507757e3eedf3f9c
- determinism: in-process double-run IDENTICAL · --selfcheck byte-identical · separate re-invocation byte-identical
- G1 EXACT identity (closed form == matrix GMV; FOC equalised, exact via fractions.Fraction) — two independent exact routes to (w*, σ*²) agree bit-for-bit (w*=(1/8,7/8), σ*²=15/16); across a 2/3/4-asset SPD panel (Σw*)_i == σ*² for all i and 𝟙ᵀw*==1; error_count=0 · pass
- G2 MC agreement — 200000 iid return vectors with covariance exactly Σ (Cholesky map of iid standard normals); s²_gmv=0.9389802396 agrees with σ*²=0.9375 at z=0.4992990385, |z|<3 [Z_ACCEPT=3.0]; iid draws so SE=σ²·√(2/N) honest, NO thinning needed · pass
- G3 invariance — (i) scale-equivariance Σ→kΣ (k=4) leaves w* identical, scales σ*² by exactly k, MC z byte-identical under √k rescale (mc_z_base=mc_z_scaled=0.4992990385); (ii) two-fund separation w(m) affine in m, exact w(m_C)==α·w(m_A)+(1−α)·w(m_B) with α=1/2, GMV recovered on frontier at m=B/A · pass
- G4 falsifiability — SAME MC sample: naive "equal weights optimal" (variance 3/2) REJECTED at z_eq=191.0595200324; naive "hold single lowest-variance asset" (variance 1) REJECTED at z_a2=21.4684726468; both |z|≥6 [Z_REJECT=6.0]; exactly 3/2≠15/16 and 1≠15/16 · pass
- all_pass: true · first_failing_gate: null · decision: PASS

✅ Flip note (born-red → complete): this card committed FIRST with Status: in-progress to hold the PR red behind the substrate-gate; it flips to complete as the deliberate LAST commit, after the idea doc, the verifier, the outbox PROPOSAL 242 block, the full-64 digest match, and all four gates landed. The flip clears the born-red HOLD and releases native squash auto-merge. FLIPPED: idea doc + verifier (results_sha256=3c1ec97050d0ca481e084976055ce3ea0e435c86b794e909507757e3eedf3f9c, all four gates PASS) + outbox PROPOSAL 242 block landed in commit 1 (PR #858); the paired sim-lab reproduction mirror opened READY (PR #340); this commit flips Status in-progress → complete to release merge-on-green.

## What this proposal does
Adds a venture-lab PROPOSAL establishing the Markowitz global minimum-variance (GMV) portfolio and two-fund separation. For n risky assets with SPD covariance Σ, the fully-invested (𝟙ᵀw=1) portfolio of least return variance is w*=Σ⁻¹𝟙/(𝟙ᵀΣ⁻¹𝟙) with variance σ*²=1/(𝟙ᵀΣ⁻¹𝟙); equivalently every asset's marginal variance contribution is equalised, (Σw*)_i=σ*² for all i. For Σ=[[4,1/2],[1/2,1]] (variances 4 and 1, cov 1/2, corr 1/4): w*=(1/8,7/8), σ*²=15/16 — strictly below the best single asset (variance 1) and far below naive equal-weight (variance 3/2). Ships a stdlib-only firsthand verifier that computes (w*,σ*²) two exact ways (two-asset closed form + general Fraction matrix solve), confirms the FOC-equalisation across a 2/3/4-asset SPD panel, runs an iid Monte-Carlo agreement gate, checks scale-equivariance and two-fund separation exactly, and falsifies the "equal weights optimal" and "hold the single lowest-variance asset" naive beliefs. Fills a confirmed gap: the Markowitz GMV / two-fund separation head is grep-0 across both repos (distinct from the risk-pooling diversification-law head P238/V251 and the IRR heads).

## Method
Exact closed form + an iid Monte-Carlo. (w*,σ*²) via: (a) the two-asset closed form w₁*=(s₂²−s₁₂)/(s₁²+s₂²−2s₁₂), σ*²=(s₁²s₂²−s₁₂²)/(s₁²+s₂²−2s₁₂); (b) the general matrix form via an exact Fraction Gauss-Jordan solve of Σx=𝟙, w*=x/𝟙ᵀx, σ*²=1/𝟙ᵀx. All in fractions.Fraction. G1 asserts the two routes agree exactly and the FOC (Σw*)_i==σ*² holds on every asset across the 2/3/4-asset SPD panel. G2 draws MC_N=200000 iid return vectors with covariance exactly Σ (Cholesky L=[[2,0],[1/4,√15/4]] of iid standard normals) and checks the GMV portfolio's sample variance agrees with σ*² at |z|<3 (iid ⇒ honest Gaussian SE=σ²·√(2/N), no thinning). G3 checks Σ→kΣ scale-equivariance exactly and two-fund separation (w(m)=g+h·m affine, exact affine combination, GMV on frontier). G4 rejects equal-weight (3/2) at z≈191 and single-asset (1) at z≈21 on the same sample.

## ⟲ Previous-session review
PROPOSAL 241 (Erlang-C delay probability for an M/M/c agent pool → V254) landed with the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly on the venture-lab lane. It is distinct from the shipped venture-lab heads: the risk-pooling / diversification variance law (P238/V251 — the σ²/n law for an independent Bernoulli pool) and the IRR heads; this is the Markowitz mean-variance GMV portfolio and two-fund separation, a portfolio-optimization object (the least-variance fully-invested weight vector for a general SPD covariance), grep-0 across both repos.

## 💡 Session idea
Next untaken mean-variance / portfolio atoms surfaced in dedup: (a) the tangency (max-Sharpe) portfolio and the capital-market-line one-fund theorem with a risk-free asset; (b) the efficient-frontier hyperbola in (σ,μ) space with its exact vertex at the GMV; (c) the diversification ratio / effective-number-of-bets as a function of Σ's eigenstructure. All grep-checked today.
