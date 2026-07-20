# Put–call parity in a no-arbitrage binomial market

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** venture-lab · option/portfolio identity
**Proposal:** 234 → Verdict 247 (+13 offset)
**Verifier:** [`verify_234_put_call_parity.py`](verify_234_put_call_parity.py) · stdlib only · SEED=20260717
**Digest:** `results_sha256 = 637c7b8a0b3a12090d377c4cf10994d81880aed0095bc3966a8a9328b587ede4`

## Claim

In an n-period recombining binomial market with spot S₀, strike K, up/down factors u > d > 0, and per-period gross risk-free return R with d < R < u (no arbitrage), the risk-neutral prices of a European call C and put P (same strike K, same maturity n) satisfy put–call parity **exactly**:

    C − P = S₀ − K · R⁻ⁿ

independent of u, d, and of the option values themselves.

## Exact reference

S₀ = 100, K = 100, u = 2, d = 1/2, R = 5/4, n = 2 ⇒ risk-neutral q = (R−d)/(u−d) = 1/2.

| quantity | value |
|---|---|
| Call C | 48 |
| Put P | 12 |
| C − P | 36 |
| S₀ − K·R⁻² = 100 − 64 | 36 |

The plausible naive rule that forgets to discount the strike, C − P = S₀ − K = 0, is off by exactly K(1 − R⁻ⁿ) = 36.

## Four gates (each in its own direction)

- **G1 — exact identity (`fractions.Fraction`).** Over a 4-market rational panel, path-enumeration prices equal the combinatorial binomial-sum prices, and C − P = S₀ − K·R⁻ⁿ holds exactly on every row.
- **G2 — Monte-Carlo agreement.** 400 000 risk-neutral trials; the estimator of E[R⁻ⁿ(call − put payoff)] agrees with the exact target 36 at z = −0.112845, |z| < 3.
- **G3 — invariance / robustness.** (a) C − P is invariant across four (u,d) volatility pairs though C and P each move; (b) options are homogeneous of degree 1, so scaling (S₀,K) by λ scales C − P and the parity target identically. Both exact via `Fraction`.
- **G4 — falsifiability.** On the same MC sample, the naive undiscounted-strike rule C − P = S₀ − K (target 0) is rejected at z_naive = 246.993214, |z| ≥ 6.

All four gates PASS; `all_gates_pass = true`, `first_failing_gate = null`, `decision = sim-ready`. Deterministic: in-process double-run and separate re-invocation are byte-identical.

## Grounding

Put–call parity (Wikipedia), pinned revision:
`https://en.wikipedia.org/w/index.php?title=Put%E2%80%93call_parity&oldid=1304770990@8457ac93f9e181b278a8f170e3225d2afb5bed5c` (rev 2025-08-08, 15558 bytes; API `revisions.sha1` == self-computed `sha1sum`).

- **Quoted** literally on the pinned revision: "put-call parity", "no arbitrage", and the identity in discounted-strike form `C − P = S − D·K` and `C + D·K = P + S`, with the time-explicit `C(t) − P(t) = S(t) − K·B(t,T)` and `B(t,T) = e^{−r(T−t)}`.
- **Derived** firsthand (grep count 0 on the pinned raw wikitext): the entire binomial reference market and its numbers (C=48, P=12, C−P=36, S₀=K=100, u=2, d=1/2, R=5/4, q=1/2, n=2), plus the framing terms "binomial" and "risk-neutral" — the article's own derivation is a static replication argument. The single-line `C − P = S − K·e^{−rT}` is composed by substitution from the quoted `C − P = S − D·K` and `B = e^{−rT}`, not printed verbatim.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 prices each market two independent exact ways — path enumeration over all 2ⁿ up/down paths and the combinatorial binomial sum — entirely in `fractions.Fraction` (RNG-free), and checks `C − P == S₀ − K·R⁻ⁿ` as equality of exact rationals on every panel row. The reference market returns C=48, P=12, C−P=36 = 100 − 64 exactly; the other three panel markets return non-round rationals (e.g. C−P = 6480/1331, 993080/21609, 0) that still match their targets exactly — equality of rationals, not a float tolerance.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?** No. Every headline value is fixed by exact rational arithmetic (G1, G3) before any RNG is touched; the Monte-Carlo gate (G2, N=400000) only confirms the exact target 36 survives under sampling (z=−0.112845, |z|<3). The per-path identity call_payoff − put_payoff = max(S_T−K,0) − max(K−S_T,0) = S_T − K makes the estimand E[R⁻ⁿ(S_T−K)] provably equal to S₀ − K·R⁻ⁿ, so the sample only stress-tests a value already pinned exactly.

**3. What is the most plausible wrong belief this could be confused with?** That C − P equals the undiscounted spread S₀ − K (= 0 in the reference market). G4 pre-registers exactly that naive rule and rejects it at z_naive=246.993214 (≥6) on the SAME sample where the correctly-discounted target agrees at z=−0.112845 — the K(1−R⁻ⁿ)=36 gap is the strike-discount, not sampling noise.

**4. Is the verifier deterministic and self-checking?** Yes. Each gate that samples consumes a single seeded `random.Random(20260717)` in fixed order; `build_results()` is a pure function of SEED and the module constants (no wall-clock / PID / unordered-set iteration in the hashed payload). `main()` asserts an in-process double-run is byte-identical, and a separate re-invocation reproduces the digest byte-for-byte. Whole-dict `results_sha256 = 637c7b8a0b3a12090d377c4cf10994d81880aed0095bc3966a8a9328b587ede4`, carrying no self-reference.

**5. Does the grounding actually support the claim, or is it overstated?** Honest split. The pinned Put–call parity revision carries the parity identity in discounted-strike form (`C − P = S − D·K`, `C + D·K = P + S`, the time-explicit `C(t) − P(t) = S(t) − K·B(t,T)` with `B(t,T) = e^{−r(T−t)}`) and the "no arbitrage" framing — quoted. Every binomial specific (the reference market S₀=K=100, u=2, d=1/2, R=5/4, n=2, q=1/2 and the numbers C=48, P=12, C−P=36, even the terms "binomial" and "risk-neutral") is flagged derived-not-quoted; the article's own derivation is a static replication argument. Neither oversold (sim/seed/digest are firsthand) nor undersold (the parity theorem genuinely appears and is cited as textbook).

**6. Does it scale / is it robust?** The claim is a closed-form identity, so it is structurally size- and parameter-independent. G1 confirms it on a 4-market panel spanning n=2…5 and distinct rational (u,d,R). G3 adds two robustness legs, both exact via `Fraction`: (a) volatility invariance — across four (u,d) pairs C and P each move but C−P stays exactly 36; (b) degree-1 homogeneity — scaling (S₀,K) by λ∈{3,7/2,1/5} scales C−P and the parity target identically.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the plausible-but-wrong undiscounted-strike rule and rejects it at ~247σ on the same sample G2 shows agreeing with the truth. Any mis-priced call or put, or a dropped R⁻ⁿ discount, would break the exact `C − P == S₀ − K·R⁻ⁿ` equality in G1/G3 and move the G2 z past the accept band.

**8. Any residual risk before ruling?** The no-arbitrage precondition d < R < u is asserted per market (a violated market has no risk-neutral q and is out of scope by construction, not a defect). The parity theorem itself is textbook and cited as such; the firsthand contribution is the exact rational binomial instantiation, the four-gate machine-checked reproduction, and the falsification of the undiscounted-strike error. The paired sim-lab VERDICT 247 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
