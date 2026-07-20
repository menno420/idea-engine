# Jackson product-form independence — in an open network of M/M/1 stations that feed each other (with feedback routing), the internal flow between stations is provably NOT Poisson, yet the joint stationary queue-length law factors EXACTLY into independent M/M/1 marginals with zero equal-time cross-station correlation

> **State:** sim-ready
> **Class:** queueing theory · open Jackson networks · product-form / stochastic independence · counterintuitive
> **Target:** sim-lab (VERDICT 210, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Jackson_network&oldid=1358616430@2bb20c407ea3d109bc936dabc7039de2f671b7cb · fetched 2026-07-20
> **Reference (external, reachable):** [Jackson network — Wikipedia](https://en.wikipedia.org/w/index.php?title=Jackson_network&oldid=1358616430) — live English Wikipedia "Jackson network" revision oldid 1358616430; my computed sha1 of the raw wikitext byte-matches MediaWiki's own reported revision sha1 `2bb20c407ea3d109bc936dabc7039de2f671b7cb` (clean byte-pin). The article states the head verbatim: "In an open Jackson network of m M/M/1 queues where the utilization ρᵢ is less than 1 at every queue, the equilibrium state probability distribution … is given by the product of the individual queue equilibrium distributions: π(k₁,…,k_m) = ∏ᵢ π_i(k_i) = ∏ᵢ ρᵢ^{kᵢ}(1−ρᵢ)." Caveat: the sha1 pins the raw wikitext (not rendered HTML); the product form appears in `<math>` LaTeX markup, and the adjacent general theorem is where the word "independent" is stated. The exact global-balance residual and the Monte-Carlo gates below are firsthand.
> **Verifier (firsthand):** ideas/fleet/jackson-product-form-independence.py · results-dict sha256 29d55fa57612782046831e792beb1584cb5c688bc181b6363d12774b56cae258

## The phenomenon (one line)
Three single-server exponential stations wired into a feedback loop physically recirculate one queue's congestion into another, yet at any instant their joint backlog law is EXACTLY the product of three independent M/M/1 geometrics — each station behaves as a standalone M/M/1 with its own Poisson feed — even though the internal traffic between stations is provably not Poisson.

## Domain
Queueing theory — the product-form (Jackson / BCMP) stationary distribution of an open network of M/M/1 stations under Markov feedback routing, and the exact stochastic independence of the station queue lengths. Outside venture and game-theory; a fleet-capacity lane.

## The folk belief
The stations are coupled — each feeds the next and feedback loops recirculate congestion — so naive intuition says (a) their backlogs must be positively correlated, and (b) a busy server reshapes its departure stream, so downstream arrivals cannot possibly be Poisson, which should further break any clean per-station analysis. Coupling ⇒ correlation, and non-Poisson internal flow ⇒ no independent-M/M/1 shortcut.

## The thesis (reasoned to its fuller form — Q-0254 duty)
Half the intuition is right and half is exactly wrong, at the same time. The internal traffic IS non-Poisson: the stream flowing into a fed-back station is bursty (squared coefficient of variation CV² ≠ 1), so the folk objection "a server's output can't be Poisson" is literally true. But the joint stationary queue-length distribution nonetheless factors EXACTLY into a product of independent M/M/1 marginals:

π(n₁,…,n_M) = ∏ᵢ (1−ρᵢ)·ρᵢ^{nᵢ},  with ρᵢ = λᵢ/μᵢ,

where the effective per-station arrival rates λ solve the linear traffic equations λᵢ = λ0ᵢ + Σⱼ λⱼ·R_{ji} (external Poisson feed λ0, Markov routing matrix R). Each marginal is precisely the M/M/1 law an isolated station with Poisson rate λᵢ would have — even though its actual input is not Poisson — and the equal-time cross-station correlation is EXACTLY zero. Jackson's theorem is the statement that the product measure solves the network's global-balance (CTMC) equations; the non-Poisson internal flow and the exact product form are not in tension, because product form is a statement about the joint stationary law, not about the marginal character of the internal streams. The independence is instantaneous, not dynamic: at a single time the queues are independent, but as time series they are lag-coupled (see honest nuance).

## The formal model / Pinned world (committed constants)
- 3 single-server exponential (M/M/1) stations, external Poisson arrivals, Markov routing matrix R with a feedback cycle; open network (customers eventually leave). All parameters rational so the exact leg is exact.
- **Set 1 (strong feedback, 3→1 w.p. 3/4):** λ0 = (1, 0, 0), μ = (8, 7, 6) → traffic-equation solution λ = (4, 4, 4), ρ = (1/2, 4/7, 2/3).
- **Set 2 (partial 3-cycle, each station also exits):** λ0 = (1, 0, 0), μ = (2, 6/7, 4/7) → λ = (8/7, 4/7, 2/7), ρ = (4/7, 2/3, 1/2).
- SEED = 20260717; 800000 events, 50000 warmup, 30 batches per set; Z_GATE = 3.0.
- Exact leg uses fractions.Fraction over the full 0..3 cube (64 interior states) per set; the unbiased covariance estimator subtracts the KNOWN closed-form M/M/1 means/variances as fixed references (never per-batch sample means — that injects an O(1/T) bias that does not vanish).

## Pre-registered gates
- **EXACTLY-TRUE gate (closed-form vs exact global balance).** The product measure π(n) = ∏ᵢ(1−ρᵢ)ρᵢ^{nᵢ} solves the CTMC global-balance equations EXACTLY: `exact_balance_max_abs_residual = 0/1` over 64 interior states (full 0..3 cube), BOTH param sets, using fractions.Fraction. The traffic-equation residual is also exactly 0. No sampling — a rational identity.
- **≥3σ non-Poisson-internal gate (the surprise).** The merged external + fed-back arrival stream into station 1 (Set 1) has CV² = 1.404111 (se 0.019995) → z_nonpoisson = 20.210254 ≥ 3. The internal traffic is provably NOT Poisson (a Poisson stream has CV² = 1).
- **Product-form-holds gate (consistency + independence, |z| < 3).** Set 1 marginal means vs the M/M/1 value ρ/(1−ρ): z = 0.133253, 0.575864, 0.983478; pairwise equal-time correlations (0.004074, 0.007377, 0.012071) → z = 0.233043, 0.336708, 0.455705 ≈ 0. Set 2: means z = 1.224147, 1.098711, 0.591916; correlations z = 0.677484, 0.424487, 0.395371. Every marginal matches its isolated-M/M/1 law and every cross-station correlation is statistically zero.
- **Robustness / shift gate.** Set 2 — a different routing topology AND different service rates — re-passes the exact global-balance gate (residual 0/1 over 64 states) and the product-form gate (means and correlations all within 3σ). The phenomenon is not a Set-1 artifact.
- **Determinism.** In-process double-run byte-identical; cross-invocation identical across two subprocess runs (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture, floats 6 dp, no on-disk JSON, SEED = 20260717).

## Pre-registered decision rule
sim-ready iff the exactly-true gate (residual 0/1 both sets), the ≥3σ non-Poisson-internal gate (z ≥ 3), the product-form-holds gate (all marginal and correlation |z| < 3, both sets), and the robustness gate all hold, with a byte-identical results-dict sha256 across an in-process double-run and a separate cross-invocation. Any gate failing, or any digest drift, blocks (verifier exits 0 iff all gates hold).

## Dry-sim results (SEED=20260717, verbatim from ideas/fleet/jackson-product-form-independence.py)
- EXACTLY-TRUE: Set 1 and Set 2 both `exact_balance_max_abs_residual = 0/1` over 64 interior states (fractions.Fraction); traffic-equation residual exactly 0 → pass.
- NON-POISSON (Set 1 station-1 merged stream): CV² = 1.404111, se = 0.019995, z_nonpoisson = 20.210254 ≥ 3 → pass (internal flow is not Poisson).
- PRODUCT-FORM Set 1: means z = {0.133253, 0.575864, 0.983478} < 3; corr = {0.004074, 0.007377, 0.012071}, z = {0.233043, 0.336708, 0.455705} ≈ 0 → pass.
- PRODUCT-FORM Set 2: means z = {1.224147, 1.098711, 0.591916} < 3; corr z = {0.677484, 0.424487, 0.395371} ≈ 0 → pass.
- Determinism: in-process double-run + separate cross-invocation byte-identical. Results-dict sha256 `29d55fa57612782046831e792beb1584cb5c688bc181b6363d12774b56cae258` (full 64 hex), exit 0.

## Honest nuance (disclosed)
- Equal-time cross-station covariance is EXACTLY zero (that is the product form), but LAGGED cross-covariance is nonzero — the stations are independent at a single instant, not as time series. Product form is an instantaneous-independence statement, not a claim of dynamic independence.
- The unbiased covariance estimator subtracts the KNOWN closed-form M/M/1 means and variances as fixed references; subtracting per-batch sample means would inject an O(1/T) bias that does not vanish with more events.
- Product form requires exponential service and these Markov routing disciplines (the Jackson / BCMP conditions). General service-time distributions (non-BCMP) generally have NO product form — the result is model-dependent, not a universal law of coupled queues.

## Reproduce
```
python3 ideas/fleet/jackson-product-form-independence.py
```
Prints the pretty results dict then `RESULTS_SHA256=29d55fa57612782046831e792beb1584cb5c688bc181b6363d12774b56cae258`; exits 0 iff every gate holds.

## Verifier
`ideas/fleet/jackson-product-form-independence.py`, stdlib only (hashlib, json, math, random, fractions). Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: the compact-canonical sha256 over the results dict is the digest, the dict carries no self field, floats rounded 6 dp, no on-disk JSON, in-process double-run asserts byte-identical. The exact leg is fractions.Fraction global balance over the full 0..3 cube; the empirical leg is a seeded event-driven simulation (no wall-clock).

## Why it matters
The trap is reading "these queues feed each other, so I cannot size them independently." Jackson's theorem says the opposite for exponential stations under Markov routing: solve the linear traffic equations for the effective per-station rate λᵢ, then size each station as a standalone M/M/1 at ρᵢ = λᵢ/μᵢ — the joint law is exactly the product, so per-station capacity planning is EXACT, not an approximation, despite the feedback and despite the bursty internal flow. The fleet analogue: a pipeline of services with retry/feedback routing can be provisioned station-by-station from the closed-form M/M/1 marginals once the traffic equations are solved, and the equal-time backlogs are uncorrelated — but only under the exponential/Markov conditions, and only instantaneously (lagged coupling remains, so a burst still propagates over time).

## Dedup
No Jackson-network / product-form / open-queueing-independence head exists in ideas/ (grepped jackson, product-form, product form, M/M/1, traffic equation, on origin/main — no fleet hit). Distinct from shipped queueing/fleet heads: Kleinrock conservation is a zero-sum delay-weight identity, sqrt-safety-staffing and Palm/Erlang concern staffing/insensitivity, USL/two-choices concern scaling and routing cliffs, series-reliability concerns product-of-survivals. This is uniquely the EXACT product-form factorization of a feedback network's joint stationary law into independent M/M/1 marginals with non-Poisson internal flow.

## Model basis (declared model-dependence — the P024 discipline)
Depends on: (a) exponential (memoryless) service at every station and Poisson external arrivals — the Jackson/BCMP conditions; (b) Markov (state-independent) probabilistic routing, including the feedback cycle; (c) open, stable network (ρᵢ < 1 at every station). The claim is exactly the product form under these conditions: change service to a general distribution (non-BCMP) and the product form generally fails; drive any ρᵢ ≥ 1 and the station is unstable and has no stationary law. The independence is equal-time only; lagged cross-covariance is nonzero and is disclosed, not gated away.

## Probe report (v0, 2026-07-20)
**1. What is the precise claim, as a mechanism?** The joint stationary queue-length law of an open Jackson network of M/M/1 stations with feedback routing factors EXACTLY into independent M/M/1 marginals π(n₁,…,n_M) = ∏ᵢ(1−ρᵢ)ρᵢ^{nᵢ}, with ρᵢ = λᵢ/μᵢ and λ solving the traffic equations λᵢ = λ0ᵢ + Σⱼ λⱼR_{ji}; equal-time cross-station correlation is exactly zero — even though the internal flow between stations is not Poisson.
**2. Why is it counterintuitive — what does naive intuition predict?** Coupling (each station feeds the next, feedback recirculates congestion) predicts positively correlated backlogs and a reshaped, non-Poisson internal stream that should break any per-station M/M/1 shortcut. Reality: the internal stream really is non-Poisson (CV² ≠ 1), yet the joint law is exactly the product of independent M/M/1s with zero equal-time correlation.
**3. Is the model clean and stdlib-simulable deterministically?** Yes — 3 exponential stations, rational parameters, a seeded event-driven simulation (no wall-clock), stdlib only; the digest reproduces byte-identically in-process and cross-invocation.
**4. Where is the exactly-true content, and how is it gated?** The product measure solves the CTMC global-balance equations with fractions.Fraction residual 0/1 over 64 interior states, BOTH param sets; the traffic equations solve to exact rationals with residual 0. A rational identity, no sampling.
**5. What are the ≥3σ empirical gates and their z-scores?** Non-Poisson internal stream (Set 1 station 1): CV² = 1.404111, z_nonpoisson = 20.210254 ≥ 3. Consistency/independence (must be small): Set-1 marginal-mean z ≤ 0.983478 and correlation z ≤ 0.455705; Set-2 marginal-mean z ≤ 1.224147 and correlation z ≤ 0.677484 — all < 3.
**6. What is the robustness/shift check?** A second rational param set (Set 2) with a different routing topology and different service rates re-passes both the exact global-balance gate (residual 0/1 over 64 states) and the product-form gate (all marginal and correlation |z| < 3).
**7. What could falsify it or where does it break?** Non-exponential service or non-BCMP disciplines generally lose the product form; any ρᵢ ≥ 1 makes a station unstable (no stationary law); and equal-time independence is not lagged independence — the stations remain coupled as time series. Any nonzero global-balance residual or a digest drift also falsifies.
**8. What external source grounds the head, and does it support the specific claim?** English Wikipedia "Jackson network" oldid 1358616430, raw wikitext byte-pinned (self-computed sha1 = MediaWiki's reported sha1 2bb20c407ea3d109bc936dabc7039de2f671b7cb); it states the product form π(k₁,…,k_m) = ∏ᵢ ρᵢ^{kᵢ}(1−ρᵢ) verbatim and the adjacent theorem states the queue independence. Caveat: the sha1 pins raw wikitext, not rendered HTML, and the product form appears in `<math>` LaTeX markup; the exact global-balance and Monte-Carlo gates are firsthand.

**Recommendation: sim-ready**
