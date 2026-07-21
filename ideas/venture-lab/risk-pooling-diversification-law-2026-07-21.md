# Insurance risk-pooling / diversification variance law

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** venture-lab · insurance / diversification identity
**Proposal:** 238 → Verdict 251 (+13 offset)
**Verifier:** [`verify_238_risk_pooling.py`](verify_238_risk_pooling.py) · stdlib only · SEED=20260717
**Digest:** `results_sha256 = 1e0520c849597c1b6a4135598ee76617488c49659c1820e1841b255b9115cbbb`

> **Grounding:** https://en.wikipedia.org/wiki/Variance@fc0e7d78428fe749117408dbeceb3d004b978c6f · fetched 2026-07-21

## Claim

A mutual pool has n members. Each member's annual loss is an **independent**
Bernoulli(p) unit claim — a loss of 1 with probability p, else 0. The pooled
per-member cost is L̄ = S / n, where S = Σ of the n losses ~ Binomial(n, p).
The pool charges each member the pooled cost L̄. Then, **exactly**:

    E[L̄]   = p                 (the fair premium is scale-free in n)
    Var[L̄] = p·(1 − p) / n     (per-member risk falls as 1/√n)

The mean premium is the individual expected loss p for **every** pool size, but
the *variance* of what any one member actually pays shrinks like 1/n — this is
the diversification / law-of-large-numbers engine underneath insurance.

## Exact reference

At p = 1/10, n = 100:

| quantity | value |
|---|---|
| E[L̄] (fair premium) | 1/10 = 0.1 (unchanged vs. a lone member) |
| Var[L̄] | 9/10000 |
| single-member cost sd, √(p(1−p)) | √(9/100) = 0.3 |
| pooled cost sd (n=100), √(p(1−p)/n) | √(9/10000) = 0.03 |
| √n reduction (0.3 / 0.03) | exactly 10 = √100 |

Pooling 100 independent members cuts each member's cost standard deviation from
0.3 to exactly 0.03 — a √n = 10× reduction — while the mean premium stays 0.1.

The naive **comonotonic** belief (falsified): if the members' losses were
perfectly correlated (ρ = 1, everyone claims together or no one does), pooling
would buy nothing — Var[L̄] = p(1 − p) = 9/100 for *every* n, no √n benefit.
That is the opposite limit from the independent baseline claimed here.

## Why it holds

Two textbook facts compose exactly:

- **Bienaymé — variance of a sum of independent terms is the sum of variances.**
  For independent losses X₁…Xₙ, Var(S) = Var(ΣXᵢ) = ΣVar(Xᵢ) = n·p(1 − p), since
  each Bernoulli(p) term has variance p(1 − p).
- **Scaling — Var(aX) = a²·Var(X).** With a = 1/n, Var(L̄) = Var(S/n) =
  Var(S)/n² = n·p(1 − p)/n² = p(1 − p)/n.

Linearity of expectation gives E[L̄] = E[S]/n = np/n = p with no independence
needed. Independence is what collapses the covariance cross-terms in Bienaymé's
general identity Var(ΣXᵢ) = ΣVar(Xᵢ) + Σ_{i≠j}Cov(Xᵢ,Xⱼ) to the pure sum —
exactly the term the comonotonic foil keeps.

## Relation to the shipped correlated-fleet-variance-floor head

This is the **ρ = 0 independent baseline**. The shipped
`correlated-fleet-variance-floor` head (fleet lane) is the **ρ > 0
generalization**: with a common shock the per-member variance no longer vanishes
but floors at the correlated component, capping the effective pool size
N_eff → 1/ρ as n → ∞. The two limits bracket this head: ρ = 0 here recovers the
full p(1 − p)/n → 0 diversification, and the comonotonic ρ = 1 foil recovers the
no-benefit floor p(1 − p). This proposal pins the ρ = 0 endpoint exactly and
falsifies the ρ = 1 endpoint on the same sample; it does not restate the
interior ρ ∈ (0,1) result, which is the other head's territory.

## Four gates (each in its own direction)

- **G1 — exact identity (`fractions.Fraction`).** Var[L̄] is computed two
  independent ways and must be EQUAL as exact rationals: Route A the closed form
  Var(S)/n², Route B a full-binomial-pmf reconstruction E[(S/n)²] − E[S/n]²
  summed over k = 0…n. Both return 9/10000 with zero error; the pmf sums to
  exactly 1.
- **G2 — Monte-Carlo agreement.** 100 000 independent pools of n = 100
  Bernoulli(1/10) members; the empirical mean cost and the empirical Var[L̄]
  agree with p and with 9/10000, max |z| = 1.4513, |z| < 3 (Z_ACCEPT = 3.0).
- **G3 — invariance / robustness.** (i) Var[L̄]·n == p(1 − p) exactly across
  n ∈ {1, 10, 100, 1000} — the σ²/n law; (ii) the coefficient of variation of
  the per-member cost is independent of claim severity (scaling every loss by a
  constant c leaves CV² = (1 − p)/(p·n) unchanged). Both exact via `Fraction`.
- **G4 — falsifiability.** On the same MC sample, the naive comonotonic variance
  p(1 − p) = 9/100 is rejected by the independent pool's empirical Var[L̄] at
  |z| ≈ 21771.77 ≫ 8 (Z_REJECT = 8.0).

All four gates PASS; `all_gates_pass = true`, `first_failing_gate = null`,
`decision = sim-ready`. Deterministic: in-process double-run and separate
re-invocation are byte-identical (`results_sha256` above, disclosed in full).

## Grounding

**Variance** (Wikipedia), pinned current revision:
`https://en.wikipedia.org/wiki/Variance@fc0e7d78428fe749117408dbeceb3d004b978c6f`
(rev 1364418626, 2026-07-16T11:46:43Z, 64971 bytes; API `revisions.sha1` ==
self-computed `sha1sum` of the raw wikitext — exact match).

**Binomial distribution** (Wikipedia), pinned current revision:
`https://en.wikipedia.org/wiki/Binomial_distribution@c6efae850469278e57d9b578c96871400e61c6b2`
(rev 1359203125, 2026-06-13T20:20:06Z, 55316 bytes; API `revisions.sha1` ==
self-computed `sha1sum` — exact match).

- **Quoted** literally on the pinned revisions: the scaling rule
  `Var(aX) = a²Var(X)` and Bienaymé's sum-of-independent-variances identity
  `Var(ΣXᵢ) = ΣVar(Xᵢ)` (Variance article); the binomial variance `npq = np(1−p)`
  (Binomial distribution article).
- **Derived** firsthand (grep count 0 on the pinned raw wikitext): the pooled
  insurance law `Var[L̄] = p(1−p)/n`, the 0.3 → 0.03 √n = 10× reduction, and the
  comonotonic ρ = 1 foil numbers. The σ²/n variance-of-the-mean and the np(1−p)
  binomial variance are textbook; the pooled-insurance framing, the exact
  rational instance (9/10000), and the four-gate battery are firsthand. Nothing
  is oversold as novel.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 computes
Var[L̄] two independent exact ways — the closed form Var(S)/n² and a full
binomial-pmf reconstruction E[(S/n)²] − E[S/n]² summed as `fractions.Fraction`
over k = 0…n — and checks they are EQUAL rationals, both 9/10000, with the pmf
summing to exactly 1. E[L̄] = p is linearity of expectation, independence-free.
No float tolerance is used for the headline values.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?**
No. Every headline value (Var = 9/10000, sd 0.3 → 0.03, CV² = (1−p)/(pn)) is
fixed by exact rational arithmetic before any RNG is touched. The Monte-Carlo
gate (G2, 100 000 independent pools) only confirms the exact targets survive
under sampling: empirical mean cost agrees with p and empirical Var[L̄] agrees
with 9/10000 at max |z| = 1.4513 (< 3).

**3. What is the most plausible wrong belief this could be confused with?** The
comonotonic intuition that pooling gives no benefit — Var[L̄] = p(1 − p) = 9/100
for all n, the ρ = 1 limit. G4 pre-registers exactly that naive variance and
rejects it against the independent pool's empirical Var[L̄] at |z| ≈ 21771.77
(≫ 8) on the SAME sample where the correct 9/10000 target agrees at |z| = 1.4513.
The 100× gap between 9/100 and 9/10000 is the whole diversification benefit.

**4. Is the verifier deterministic and self-checking?** Yes. The sampling gate
consumes a single seeded `random.Random(20260717)` in fixed order; `compute()`
is a pure function of SEED and the module constants (no wall-clock / PID /
unordered-set iteration in the hashed payload). `main()` asserts an in-process
double-run is byte-identical, and a separate re-invocation reproduces the digest
byte-for-byte. Whole-dict `results_sha256 =
1e0520c849597c1b6a4135598ee76617488c49659c1820e1841b255b9115cbbb`, carrying no
self-reference.

**5. Does the grounding actually support the claim, or is it overstated?**
Honest split. The pinned Variance revision carries `Var(aX) = a²Var(X)` and
Bienaymé's `Var(ΣXᵢ) = ΣVar(Xᵢ)` verbatim; the pinned Binomial distribution
revision carries `npq = np(1−p)` verbatim — quoted. The pooled law p(1−p)/n, the
0.3 → 0.03 reduction, and the comonotonic foil are flagged derived (grep count 0
on the pinned wikitext). The σ²/n and np(1−p) facts are textbook; the firsthand
contribution is the exact rational insurance instantiation and the gate battery.
Neither oversold nor undersold.

**6. Does it scale / is it robust?** The claim is a closed-form identity, so it
is structurally size-independent. G3(i) confirms Var[L̄]·n == p(1 − p) exactly
across n ∈ {1, 10, 100, 1000} — the exact σ²/n law, not a large-n asymptotic.
G3(ii) adds severity-invariance: scaling every claim by a constant c leaves the
coefficient of variation CV² = (1 − p)/(p·n) unchanged, so the diversification
benefit is a property of the pool size, not the currency units.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the
plausible-but-wrong comonotonic variance p(1 − p) and rejects it at ~21771σ on
the same sample G2 shows agreeing with the truth. Any mislabeled correlation, or
a dropped 1/n scaling, would break the exact `Var[L̄] == p(1−p)/n` equality in
G1/G3 and move the G2 z past the accept band.

**8. Any residual risk before ruling?** The independence precondition is the
whole content of the claim — it is what collapses Bienaymé's covariance
cross-terms; a positively correlated pool floors above p(1−p)/n and is the
`correlated-fleet-variance-floor` head's territory, not a defect here. The
variance-of-the-mean and binomial-variance facts are textbook and cited as such;
the firsthand contribution is the exact rational pooled instance, the four-gate
machine-checked reproduction, and the falsification of the comonotonic error.
The paired sim-lab VERDICT 251 reproduction is a separate coordinator-driven
slice. No further blocker.

**Recommendation: sim-ready**
