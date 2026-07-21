# Monopoly optimal markup and the Lerner index — a monopolist facing LINEAR inverse demand p(q)=a−b·q with constant marginal cost c (0≤c<a, b>0) maximises profit at q*=(a−c)/(2b), p*=(a+c)/2, π*=(a−c)²/(4b), and the resulting Lerner index of market power satisfies the EXACT identity L=(p*−c)/p*=(a−c)/(a+c)=1/|ε*|, i.e. the optimal markup equals the RECIPROCAL of the absolute price-elasticity of demand at the optimum (|ε*|=(a+c)/(a−c)). Headline instance a=1,b=1,c=1/4 → p*=5/8, q*=3/8, π*=9/64, L=3/5, 1/|ε*|=3/5. The exact rational identity (G1, `Fraction`, two independent cross-checks — FOC MR(q*)==c and reciprocal-elasticity L==1/|ε*|==(a−c)/(a+c), swept over five rational triples), the iid Monte-Carlo agreement on a uniform-valuation microfoundation (G2, |z|=0.27), the currency-scale invariance of the unit-free Lerner index (G3, exact under λ∈{2,3,100,1/7}), and the falsification of the naive "revenue-max = profit-max" foil that prices at a/2 and ignores cost (G4, rejected at z_foil=189.87, exact profit gap 1/64) all PASS. A microeconomics / market-power head over the venture lane.

> **State:** sim-ready
> **Status:** sim-ready
> **📊 Model:** Claude Opus · high · idea/planning

**Lane:** fleet · microeconomics / market power · monopoly optimal markup and the Lerner index
**Proposal:** 254 → Verdict 267 (+13 offset) — named by the `## PROPOSAL 254` block in `control/outbox.md`
**Verifier:** [`verify_254_monopoly_lerner_markup.py`](verify_254_monopoly_lerner_markup.py) · stdlib only (math, random, fractions, hashlib, json, argparse, sys) · SEED=20260717
**Digest:** `results_sha256 = 025706848687e612a0f1b6d9e5c6bef64c9e0fc09748dd9cc93ee7626003f0c3`

## What this proposal does

Adds a fleet PROPOSAL establishing the **monopoly optimal markup and the Lerner index** — a microeconomics / market-power head. A monopolist faces LINEAR inverse demand

> `p(q) = a − b·q`,  with constant marginal cost `c`,  `0 ≤ c < a`,  `b > 0`,

and maximises profit `π(q) = (p(q) − c)·q = (a − c)·q − b·q²`. Setting marginal revenue equal to marginal cost, `MR(q) = a − 2b·q = c`, gives the closed forms

> `q* = (a − c)/(2b)`,  `p* = (a + c)/2`,  `π* = (a − c)²/(4b)`,

and the resulting **Lerner index of market power** satisfies the **exact identity**

> `L = (p* − c)/p* = (a − c)/(a + c) = 1/|ε*|`,

where `|ε*| = (a + c)/(a − c)` is the absolute price-elasticity of demand evaluated at the optimum. The optimal markup is exactly the **reciprocal of the elasticity** the firm faces.

**The insight.** Market power is a purely relative quantity: the Lerner index is **unit-free** (invariant to any currency rescale a→λa, b→λb, c→λc) and is pinned entirely by the ratio of the demand intercept to marginal cost through `(a−c)/(a+c)`. A less-elastic demand at the optimum (`|ε*|` closer to 1) supports a larger markup; the identity `L = 1/|ε*|` is the exact quantitative lever behind every markup-over-marginal-cost statement of monopoly pricing.

**Headline instance.** `a = 1, b = 1, c = 1/4` gives `p* = 5/8`, `q* = 3/8`, `π* = 9/64`, `L = 3/5`, and `1/|ε*| = 3/5`. The microfoundation for the marginal-cost estimator (G2): a unit mass of consumers with valuation `v ~ Uniform[0, a]`, each buying iff `v ≥ p`, so the demand fraction is `(a − p)/a` — exactly this linear demand with `b = a = 1` — and expected profit per consumer at price `p` is `(p − c)·(a − p)/a`, maximised at `p*` with value `π*`.

## Method

Exact rational closed forms first, Monte-Carlo agreement second.

**Structural check.** `assert 0 <= C < A` and `assert B > 0` at module top — the standard monopoly regularity conditions hold before any arithmetic runs.

**Exact backbone (`fractions.Fraction`, no float in the identity).** `q_star`, `p_star`, `pi_star`, `lerner`, and `abs_elasticity_at_opt` are exact rational functions of `(a,b,c)`. The core identity is cross-checked **two independent ways** and swept over five rational triples: (i) the first-order condition `marginal_revenue(a,b,q*) == c` exactly (setting MR = MC recovers `q*`); (ii) the reciprocal-elasticity identity `lerner == 1/abs_elasticity_at_opt` and `lerner == (a−c)/(a+c)`, both exact. Because these are exact `Fraction` arithmetic, the identity carries no floating-point error.

**Monte-Carlo (iid — no thinning).** `rng = random.Random(SEED)`; each consumer draws `v ~ Uniform(0,a)` independently, so the per-consumer profit indicators are **iid** — the plain iid standard error is the honest one (no batch means; contrast an autocorrelated sample path). The exact integer buy-counts drive both G2 (agreement with `π*`) and G4 (the same SEED stream falsifies the revenue-max foil), so the hashed payload is a deterministic function of SEED alone.

## Exact reference

The exact monopoly optimum and Lerner index for the headline instance `a=1, b=1, c=1/4` (exact `Fraction`, no float in the identity):

| quantity | value |
|---|---|
| `a` (demand intercept) | `1` |
| `b` (demand slope) | `1` |
| `c` (marginal cost) | `1/4` |
| `q* = (a−c)/(2b)` | **`3/8`** |
| `p* = (a+c)/2` | **`5/8`** |
| `π* = (a−c)²/(4b)` | **`9/64`** |
| `L = (p*−c)/p* = (a−c)/(a+c)` | **`3/5`** |
| `\|ε*\| = (a+c)/(a−c)` | `5/3` |
| `1/\|ε*\|` | **`3/5`** = `L` |

The optimal markup `L = 3/5` equals the reciprocal of the optimum-point elasticity `|ε*| = 5/3` — the exact statement that a monopolist marks up in inverse proportion to the elasticity of demand it faces.

## Four gates (each in its own direction)

- **G1 — EXACT (`fractions.Fraction`, zero tolerance).** The monopoly FOC and the Lerner/reciprocal-elasticity identity, cross-checked two independent ways and SWEPT over five rational triples `(1,1,1/4),(3,2,1),(5,7,2),(10,1,3),(2,3,1/2)`: (i) `MR(q*) = a − 2b·q* == c` exactly; (ii) `L == 1/|ε*| == (a−c)/(a+c)` exactly. All five triples hold with zero residual. No float enters the identity → reported **exact — z=n/a**. `sweep_pass = [True, True, True, True, True]`. PASS.
- **G2 — MC agreement (`|z| < 3`).** `N=2000000` iid consumer draws `v ~ Uniform(0,1)`; per-consumer profit at `p*` is `(p*−c)` if `v ≥ p*` else `0`, sample mean estimates `π* = 9/64`. `n_buy = 749815`, `SE = (p*−c)·sqrt(q*(1−q*)/N)`, `z = −0.2702`, `|z| < 3` [Z_ACCEPT=3.0]. iid draws → plain iid SE is honest (no batch means). PASS.
- **G3 — invariance (currency-scale, own direction, EXACT).** The Lerner index is **unit-free**: for `λ ∈ {2, 3, 100, 1/7}`, `lerner(λa,λb,λc) == lerner(a,b,c)` exactly via `Fraction` (and `q*` is likewise unchanged). Market power is scale-free — genuine economic content, not a formatting artefact. `lambda_pass = [True, True, True, True]` → reported **exact — z=n/a**. PASS.
- **G4 — falsifiability (reject at large `|z|`, own direction, SAME SEED stream).** Pre-registered naive foil: *"revenue maximisation equals profit maximisation"* → price at `p_rev = a/2 = 1/2`, which **ignores cost**. Exactly `π(p_rev) = (a/2−c)(a−a/2)/a = 1/8 < π* = 9/64` (exact gap `1/64 > 0`). On the same SEED-derived draws, the per-consumer difference `(profit_at_p* − profit_at_p_rev)` has sample mean estimating `π* − π(p_rev) = 1/64 > 0`; `z_foil = mean_diff/SE_diff = 189.8672`, `|z_foil| > 8` → REJECTED, and `π* > π(p_rev)` holds exactly via `Fraction`. PASS.

All four gates PASS; `all_pass = true`, `first_failing_gate = null`, `results_sha256 = 025706848687e612a0f1b6d9e5c6bef64c9e0fc09748dd9cc93ee7626003f0c3`. Deterministic three ways: in-process double-run byte-identical (`in_process_double_run: IDENTICAL`), a `--selfcheck` path printing `SELFCHECK: byte-identical`, and a separate-process re-invocation byte-identical. SEED = 20260717 (hardcoded module constant). Verifier file sha256 `84530ee2ce5e1178a17dd8192861f012f99887a4729f747b48ced3eef208b11c`.

## Grounding

Three pinned Wikipedia revisions (MediaWiki API `revisions.sha1` == self-computed `hashlib.sha1` of the raw wikitext — exact match for ALL THREE):

- **"Lerner index"**, oldid 1359509771:
  `https://en.wikipedia.org/wiki/Lerner_index?oldid=1359509771@c6d342b0e7253739d99bf8eddbbd8010f40c0937`, fetched 2026-07-21. API `sha1 = c6d342b0e7253739d99bf8eddbbd8010f40c0937`; self-computed `hashlib.sha1(rawwikitext)` — **match**.
- **"Monopoly"**, oldid 1362632265:
  `https://en.wikipedia.org/wiki/Monopoly?oldid=1362632265@e3764247a5666f85ccd81597820ed227f78fddbe`, fetched 2026-07-21. API `sha1 = e3764247a5666f85ccd81597820ed227f78fddbe`; self-computed `hashlib.sha1(rawwikitext)` — **match**.
- **"Monopoly price"**, oldid 1353939980:
  `https://en.wikipedia.org/wiki/Monopoly_price?oldid=1353939980@dbb3842dab16ac7309ca13fde3a0e1d482f76abf`, fetched 2026-07-21. API `sha1 = dbb3842dab16ac7309ca13fde3a0e1d482f76abf`; self-computed `hashlib.sha1(rawwikitext)` — **match**.

**Quoted** literally on the pinned revisions:
- *Lerner index page* — the index definition `L = (P − MC)/P`; the Lerner rule against the signed elasticity `(P − MC)/P = −1/E_d`.
- *Monopoly page* — the optimality condition "A monopoly maximises profits by producing where marginal revenue equals marginal costs" (MR = MC); the linear model with demand `x = a − by` and marginal revenue `MR = a − 2by`.
- *Monopoly price page* — the market-power framing of price above marginal cost.

**Derived** firsthand (grep count 0 on the pinned raw wikitext): `q* = (a−c)/(2b)` and `p* = (a+c)/2` (derived by setting the page's `MR = a − 2b·q` equal to our own `MC = c` substitution); `π* = (a−c)²/(4b)`; the uniform-valuation microfoundation; the marginal-cost MC estimator; the `a=1,b=1,c=1/4` instance and every rational in the reference table; the scale-invariance leg; the revenue-max foil; every z-value; SEED; and the digest.

**Honest posture — disclosed seams.** (1) The Monopoly page writes `x` = PRICE and `y` = QUANTITY (**axes swapped** relative to our `p(q)` convention): map page `x → our p`, page `y → our q`, page `a → a`, page `b → b`. Same linear model, disclosed re-lettering — the page's `MR = a − 2by` is our `MR(q) = a − 2b·q`. (2) The constant `MC = c` is **OUR label** (the page keeps MC generic), which is exactly why `q*, p*` are **derived** here rather than quoted. (3) Elasticity is **signed** `E_d` on the Lerner page (rule `L = −1/E_d`); our `1/|ε|` uses the absolute-value convention, identical since `E_d < 0`. (4) The reciprocal-elasticity derivation on the page is stated in the **general** `P(Q), C(Q)` framework; our linear model is a special case, and the identity specialises cleanly. Nothing is oversold as a novel theorem: monopoly MR = MC and the Lerner rule are textbook and quoted; the firsthand contribution is the **verification apparatus** — the exact `Fraction` identities with two independent cross-checks, the iid MC agreement, the currency-scale-invariance leg, the revenue-max falsification, and every z-value + the digest.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes, and the exactness is the point. `q* = (a−c)/(2b)`, `p* = (a+c)/2`, `π* = (a−c)²/(4b)`, and `L = (a−c)/(a+c) = 1/|ε*|` are computed in exact `fractions.Fraction`. G1 cross-checks the identity two independent ways with zero residual — the FOC `MR(q*) == c` and the reciprocal-elasticity `L == 1/|ε*| == (a−c)/(a+c)` — and holds on all five swept rational triples, not just the headline instance. No floating-point error enters the value; the MC leg only *confirms* it.

**2. Could the numbers be an artefact of the sampler rather than the mathematics?** No. The exact identity (G1) and the invariance leg (G3) are RNG-free — pure `Fraction` arithmetic fixed before any draw. The MC leg (G2) samples `v ~ Uniform(0,a)` and lands `z = −0.27` on the exact `π* = 9/64`. A wrong optimum (e.g. the revenue-max price) would push the sample out of band — which is exactly what G4 demonstrates: the revenue-max foil is rejected at `z_foil = 189.87` on the same SEED stream.

**3. What is the most plausible wrong belief this could be confused with?** That a monopolist should price to maximise **revenue** (at `p_rev = a/2`), or equivalently that cost does not shift the optimal price. Both are refuted: the revenue-max price yields `π(p_rev) = 1/8 < π* = 9/64` (exact gap `1/64`), and G4 pre-registers this foil and rejects it at `|z_foil| = 189.87` — profit-max strictly dominates because the true optimum `p* = (a+c)/2` moves with marginal cost.

**4. Is the verifier deterministic and self-checking?** Yes. `build_results()` is a pure function of SEED and the module constants; the MC legs enter the payload via **exact integer counts** (`n_buy`, `n_mid`) and fixed `f"{z:.4f}"` strings, and all rationals as `str(Fraction)` — no float-repr / wall-clock / PID / set-iteration instability enters. `main()` asserts an in-process double-run is byte-identical, `--selfcheck` prints "SELFCHECK: byte-identical", and two separate invocations reproduce the digest byte-for-byte. Whole-dict `results_sha256 = 025706848687e612a0f1b6d9e5c6bef64c9e0fc09748dd9cc93ee7626003f0c3`.

**5. Does the grounding actually support the claim, or is it overstated?** Honest and tight, seams disclosed. `L = (P − MC)/P`, the Lerner rule `(P − MC)/P = −1/E_d`, MR = MC optimality, and the linear model `x = a − by`, `MR = a − 2by` are QUOTED verbatim on the three pinned revisions (API sha1 == self-computed sha1 for all three) — so nothing is oversold as a novel theorem. Disclosed: the Monopoly page swaps axes (its `x` is price, `y` is quantity); `MC = c` is our label (so `q*, p*` are derived, not quoted); the page's elasticity is signed `E_d` while we use `1/|ε|`; the reciprocal-elasticity derivation is in the page's general `P(Q), C(Q)` framework and specialises to our linear case. The instance, the exact reference values, the MC estimator, the invariance leg, the revenue-max foil, every z-value, SEED, and the digest are the firsthand contribution.

**6. Does it scale / is it robust?** The apparatus is general: `q_star`, `p_star`, `pi_star`, `lerner`, and `abs_elasticity_at_opt` take any `(a,b,c)` with `0 ≤ c < a`, `b > 0` — G1 exercises this across five triples spanning small and large intercepts. G3 shows the Lerner index is a property of the ratio structure, not the units: it is exactly invariant under any currency rescale `λ ∈ {2,3,100,1/7}`. A natural sweep (vary `c/a` and trace `L = (a−c)/(a+c)` from near 1 down toward 0) is flagged as the follow-on.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the single most plausible wrong model (revenue-maximisation, pricing at `a/2` and ignoring cost) and refutes it. Exactly `π* − π(p_rev) = 1/64 > 0`, and on the same SEED stream the per-consumer profit difference is rejected against the null at `z_foil = 189.87` (`|z_foil| > 8`), a decisive separation at `N = 2·10⁶`. The exact `Fraction` dominance `π* > π(p_rev)` anchors the claim regardless of the sampler.

**8. Any residual risk before ruling?** The MC leg is **iid** consumer draws (independent `rng.random()`), so the plain iid SE is the honest one and batch means are deliberately *not* used — stated in the verifier docstring; the exact `Fraction` identity (G1) and the exact invariance (G3) carry the claim RNG-free. The G2 point (`z = −0.27`) sits comfortably in band. Monopoly MR = MC and the Lerner rule are textbook (the three pinned pages) and cited as such; the exact closed-form identities with two cross-checks, the MC agreement, the scale-invariance leg, the revenue-max falsification, and every z-value + the digest are the firsthand contribution. The paired sim-lab VERDICT 267 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
