# The Gaussian integral ∫_{−∞}^{∞} e^{−x²} dx = √π — a self-contained pure-math closed form with an EXACT rational backbone. The irrational value √π is verified through the DIMENSIONLESS even-moment ratios R_m = M_{2m}/M_0 = (2m−1)!!/2^m = (2m)!/(4^m·m!), which are exactly rational (√π cancels): the integration-by-parts recurrence M_{2m} = ((2m−1)/2)·M_{2m−2} and the closed form agree with 0 mismatches over m=0..12 in exact `fractions.Fraction`. A uniform-importance Monte-Carlo estimator of ∫_{−L}^{L} e^{−x²} dx agrees with √π·erf(L) at |z|=0.70; the dimensionless ratio is scale-invariant exactly (65 Fraction checks, 0 mismatches) and the full integral obeys √a·∫e^{−ax²}dx = √π across 6 (a, μ) configs (max |z|=1.54); and the naive foil that confuses the Gaussian integral with the standard-normal normalizer ∫e^{−x²/2}dx = √(2π) ≈ 2.5066 is REJECTED on the same sample at |z_foil|=133.8. A pure closed-form result outside the fleet/venture/game domains.

> **State:** sim-ready
> **Status:** sim-ready
> **📊 Model:** Claude Opus · high · idea/planning

**Lane:** fleet · pure mathematics / analysis / the Gaussian (Euler–Poisson) integral
**Proposal:** 252 → Verdict 265 (+13 offset) — named by the `## PROPOSAL 252` block in `control/outbox.md`
**Verifier:** [`verify_252_gaussian_integral_sqrt_pi.py`](verify_252_gaussian_integral_sqrt_pi.py) · stdlib only (json, hashlib, math, random, fractions, sys) · SEED=20260717
**Digest:** `results_sha256 = f8d553495590f7e0dc52d702e6b3dbb813464b4b48e8bc3a159f140b1e88c0d8`

## What this proposal does

Adds a fleet PROPOSAL establishing the **Gaussian integral** as a self-contained, exactly-verifiable pure-math closed form — the "unrelated / pure-math" slot, orthogonal to every fleet, venture, and game head:

> ∫_{−∞}^{∞} e^{−x²} dx = √π,   and more generally   M_{2m} := ∫_{−∞}^{∞} x^{2m} e^{−x²} dx = √π · (2m−1)!! / 2^m.

The value √π is irrational, so the **exact** teeth come from the **dimensionless even-moment ratio**

> R_m := M_{2m}/M_0 = (2m−1)!!/2^m = (2m)!/(4^m·m!),

which is **exactly rational** — the √π cancels. Integration by parts gives the exact three-term recurrence `M_{2m} = ((2m−1)/2)·M_{2m−2}` (the boundary term `x^{2m−1} e^{−x²}` vanishes at ±∞), and the closed form must satisfy it identically. The verifier confirms this in exact `fractions.Fraction` arithmetic (0 mismatches over m=0..12), estimates √π directly by Monte-Carlo integration, exhibits the exact scale-invariance of R_m and the `√a·∫e^{−ax²}dx = √π` scale/translation law of the full integral, and **falsifies** the single most plausible confusion — that ∫e^{−x²}dx equals the standard-normal normalizer √(2π).

**Headline numbers.** Exact ratios `R_1 = 1/2`, `R_2 = 3/4`, `R_3 = 15/8`, `R_6 = 10395/64` (recurrence route == closed-form route == `(2m−1)!!/2^m` route, 0 mismatches). MC estimate of ∫_{−6}^{6} e^{−x²} dx = `1.776277` vs target √π·erf(6) = `1.772454`, `z = 0.7004`. Exact scale-invariance of R_m across `a ∈ {1, 2, 3, 5, 1/2}` and `m=0..12`: 65 checks, 0 mismatches. MC scale/translation law across 6 configs: max `|z| = 1.5375`. Foil √(2π) = `2.506628` rejected at `z_foil = −133.7896` on the **same** sample that accepts √π at `z = 0.7004`.

**Distinctness.** This is a **pure-analysis closed form** — no fleet lane, no venture cash-flow, no game value, no opponent, no Markov chain. The object is a definite integral over ℝ and its exact rational moment structure. `gaussian integral`, `sqrt(pi)`, `wallis`, `e^{-x` and `e^-x` are **grep-0** across both repos (`control/outbox.md`, `ideas/`, `sims/`); the only nearby tokens are the Gaussian *distribution* / Gaussian *noise* used as machinery inside statistical heads (Stein shrinkage, min-variance, probit) and `(2n−1)!!` used as the *matching count* in the non-crossing-matching Catalan head (P240) — a different object (a combinatorial count, not an even moment). It is orthogonal to every shipped math head: random-walk return (P228), coprime density → 6/π² (P232, which uses ζ(2) as machinery — this uses NO zeta), Burnside (P236), non-crossing Catalan (P240), Buffon (P244), Cantor set (P248), derangements → 1/e (P229), Bulgarian solitaire (P251). The distinctive content here is the **exact rational moment-ratio backbone of an irrational integral** plus its scale-invariance and the √π↔√(2π) falsification.

## Method

Exact rational identity first, Monte-Carlo agreement second.

**Exact backbone (`fractions.Fraction`, no floats).** `moment_ratio_recurrence(m, a)` builds `R_m(a) = ∏_{j=1}^m (2j−1)/(2a)` purely from the integration-by-parts recurrence; `moment_ratio_closed_form(m)` returns `(2m)!/(4^m·m!)`; `double_factorial_odd(m)` returns `(2m−1)!!`. G1 asserts all three routes agree and that the integer identity `(2m−1)!!·2^m·m! == (2m)!` holds — zero tolerance, zero mismatches. Because the ratio is dimensionless, the irrational √π never enters the exact arithmetic.

**Monte-Carlo integral (uniform importance sampling).** `mc_integral(rng, n, hw, a, mu)` draws `X ~ Uniform[mu−hw, mu+hw]` and averages `g = 2·hw·e^{−a(X−mu)²}`, so `E[g] = ∫_{mu−hw}^{mu+hw} e^{−a(x−mu)²} dx`. For the headline `a=1, mu=0, hw=L=6`, `E[g] = √π·erf(6)`; since `erf(6) = 1 − 2.2·10⁻¹⁷` underflows to exactly `1.0` in IEEE double, the honest target `√π·erf(6)` equals √π to full machine precision (zero truncation bias in the comparison). Each draw is an **independent** sample, so the plain iid standard error is the honest one — **no** batch means / thinning (those are only for autocorrelated sample paths, which this is not; stated in the verifier docstring). `random.seed(SEED)` is re-seeded at the START of each MC gate so gate order cannot perturb the payload.

## Exact reference

Dimensionless even-moment ratios `R_m = M_{2m}/M_0` (exact `Fraction`, three independent routes agree, 0 mismatches):

| m | (2m−1)!! | R_m = (2m−1)!!/2^m | = (2m)!/(4^m·m!) |
|---|---|---|---|
| 0 | 1 | 1 | 1 |
| 1 | 1 | 1/2 | 1/2 |
| 2 | 3 | 3/4 | 3/4 |
| 3 | 15 | 15/8 | 15/8 |
| 4 | 105 | 105/16 | 105/16 |
| 5 | 945 | 945/32 | 945/32 |
| 6 | 10395 | 10395/64 | 10395/64 |

All the way through m=12: `checked = 13`, `mismatches = 0`. The recurrence route (`∏ (2j−1)/2`) and the closed form (`(2m)!/(4^m·m!)`) are independent derivations that agree exactly — the teeth of G1.

## Four gates (each in its own direction)

- **G1 — EXACT (`fractions.Fraction`, zero tolerance).** For m=0..12 assert that the integration-by-parts recurrence route `R_m = ∏_{j=1}^m (2j−1)/2`, the closed form `(2m)!/(4^m·m!)`, and the double-factorial form `(2m−1)!!/2^m` are all exactly equal, and that `(2m−1)!!·2^m·m! == (2m)!`. `checked = 13`, `mismatches = 0`. This is the exact rational backbone that underlies the irrational √π. `z` is not applicable → reported `"exact"`. PASS.
- **G2 — Monte-Carlo agreement (`|z| < 3`).** Estimate ∫_{−6}^{6} e^{−x²} dx by uniform importance sampling, `N = 400000`. Sample estimate `1.776277`, SE `0.005459`, honest target `√π·erf(6) = 1.772454`, `z = (x̄ − target)/SE = 0.7004`, `|z| < 3` [Z_ACCEPT = 3.0]. iid draws → plain iid SE is honest (no batch means). PASS.
- **G3 — invariance (own direction).** (a) **Exact scale-invariance** (`Fraction`, 0 mismatches): for `a ∈ {1, 2, 3, 5, 1/2}` and m=0..12, the scaled recurrence `M_{2m}(a) = ((2m−1)/(2a))·M_{2m−2}(a)` gives a dimensionless quantity `a^m · (M_{2m}(a)/M_0(a)) == (2m−1)!!/2^m` **independent of `a`** — `exact_checked = 65`, `exact_mismatches = 0`. (b) **MC scale + translation law** (`|z| < 3`): the full integral obeys `√a·∫e^{−a(x−μ)²}dx = √π` for every scale `a` and shift `μ`; across 6 configs `(a,μ) ∈ {(1,0),(2,0),(½,0),(1,3),(1,−2),(3,1)}`, every `√a·estimate` agrees with √π, `max |z| = 1.5375`. PASS.
- **G4 — falsifiability (reject at large `|z|`, own direction, SAME sample as G2).** Pre-registered naive foil: *"the Gaussian integral ∫e^{−x²}dx equals the standard-normal normalizer ∫e^{−x²/2}dx = √(2π) ≈ 2.5066"* (also Stirling's constant — the single most common confusion). On the **same** N=400000 sample, `z_foil = (x̄ − √(2π))/SE = −133.7896`, `|z_foil| ≫ 50` [Z_REJECT = 50.0] → REJECTED, while the same sample AGREES with √π at `z = 0.7004`. PASS.

All four gates PASS; `all_pass = true`, `first_failing_gate = null`, `results_sha256 = f8d553495590f7e0dc52d702e6b3dbb813464b4b48e8bc3a159f140b1e88c0d8`. Deterministic three ways: in-process double-run byte-identical (`in_process_double_run: IDENTICAL`), a `--selfcheck` path printing `SELFCHECK: byte-identical`, and a separate-process re-invocation byte-identical. SEED = 20260717 (hardcoded module constant). Verifier file sha256 `1f348d8524b2a4f6f662c880455662c0fe1daa00226a0fc24e76464f51dd5115`.

## Grounding

One pinned Wikipedia revision (MediaWiki API `revisions.sha1` == self-computed `hashlib.sha1` of the raw wikitext — exact match):

- **"Gaussian integral"**, oldid 1365252560:
  `https://en.wikipedia.org/w/index.php?title=Gaussian_integral&oldid=1365252560@6d8b0d941ef6028c1331a63443a49c199f3c1c2d` (22230 bytes), fetched 2026-07-21. API `sha1 = 6d8b0d941ef6028c1331a63443a49c199f3c1c2d`; self-computed `hashlib.sha1(rawwikitext) = 6d8b0d941ef6028c1331a63443a49c199f3c1c2d` — **match**.

**Quoted** literally on the pinned revision (grep count > 0):
- The **core closed form** — `\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt{\pi}` (grep `\sqrt{\pi}` = 8, `\int_{-\infty}^\infty e^{-x^2}` = 8; the result appears verbatim in the lede, the polar-coordinates proof, and the summary).
- The **names** — "Gaussian integral", "Euler–Poisson integral" (grep `Euler` = 2, `Poisson` = 2), "Carl Friedrich Gauss" (grep `Gauss` = 20), de Moivre 1733 / Gauss 1809 attribution.
- The **scale + translation form** — `\int_{-\infty}^{\infty} e^{-a(x+b)^2}\,dx = \sqrt{\frac{\pi}{a}}` (grounds G3's scale law and translation invariance directly).
- The **even-moment closed form** — `\int_{-\infty}^\infty x^{2n} e^{-\alpha x^2}\,dx = \sqrt{\frac{\pi}{\alpha}}\frac{(2n-1)!!}{(2\alpha)^n}` (grep `(2n-1)!!` = 3, `double factorial` = 4) — this is exactly the M_{2m} identity used in G1/G3, with `α` for the scale.
- The constant **√(2π)** appears (grep `\sqrt{2\pi}` = 2), in the normal-distribution / Fresnel-adjacent section — the foil constant is real, though the confusion refuted in G4 is not made by the page.

**Derived** firsthand (grep count 0 on the pinned raw wikitext): the phrase **"moment"** (grep 0 — my label for `∫x^{2n}e^{−x²}`; the integral itself is quoted); **"integration by parts"** as the recurrence route (grep 0 — the page derives the even moments by *differentiating under the integral sign* `∂ⁿ/∂αⁿ`, an **independent** route to the SAME quoted closed form, disclosed below); the **dimensionless scale-invariant ratio** framing `a^m·R_m(a) = (2m−1)!!/2^m`; the **exact `Fraction` zero-mismatch** identity check across the three routes; the **uniform-importance Monte-Carlo estimator** and every z-value; the specific **"√π confused with √(2π)"** foil framing; SEED 20260717; and the results digest.

**Honest posture — disclosed seams.** (1) The article is **rich** (22230 bytes): the closed form, the scale/translation general form, and the even-moment closed form are all **quoted verbatim**, with a full polar-coordinates proof — so nothing here is a novel *theorem*. The firsthand contribution is the **verification apparatus**: the exact rational moment-ratio identity checked three independent ways in `Fraction` with 0 mismatches, the exact scale-invariance leg, the Monte-Carlo agreement, the √(2π) falsification, and every z-value + the digest. (2) My recurrence route uses **integration by parts** (`M_{2m} = ((2m−1)/2)·M_{2m−2}`), whereas the page reaches the same closed form by **parameter differentiation** under the integral — the two routes are independent and agree exactly (disclosed, not hidden). (3) The word "moment" is grep 0 (my label). (4) The √(2π) foil confusion is my construction — the page states √(2π) only in its own (normal-distribution / imaginary-argument) context and never equates it with ∫e^{−x²}dx. Nothing oversold as novel: the Gaussian integral is textbook (de Moivre 1733; Gauss 1809; the pinned page), cited as such.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes, and the exactness is the point. √π is irrational, so it cannot be pinned by rational arithmetic directly — but the **dimensionless even-moment ratios** `R_m = M_{2m}/M_0 = (2m−1)!!/2^m` are exactly rational because √π cancels. G1 verifies, in exact `fractions.Fraction`, that the integration-by-parts recurrence route, the closed form `(2m)!/(4^m·m!)`, and the `(2m−1)!!/2^m` form all agree for m=0..12 with `mismatches = 0`, and that the integer identity `(2m−1)!!·2^m·m! == (2m)!` holds. The irrational value √π is then the shared normalization `M_0`, quoted verbatim on the source page.

**2. Could the numbers be an artefact of the sampler rather than the mathematics?** No. The exact backbone (G1) and the exact scale-invariance leg (G3a) are RNG-free — pure `Fraction` arithmetic fixed before any random draw. The Monte-Carlo legs (G2, G3b) only *confirm* the analytic values: G2 estimates ∫_{−6}^{6} e^{−x²} dx and lands `z = 0.7004` from the honest target √π·erf(6); G3b confirms `√a·∫e^{−ax²}dx = √π` across scales/shifts at `max |z| = 1.5375`. A wrong sampler would push these z's out of band, not fake agreement across six independent configs plus the exact identities.

**3. What is the most plausible wrong belief this could be confused with?** That ∫e^{−x²}dx = √(2π) — confusing the **Gaussian integral** with the **standard-normal normalizer** ∫e^{−x²/2}dx = √(2π) (≈ 2.5066, also Stirling's constant). This is pre-registered as G4 and refuted: on the same N=400000 sample that accepts √π at `z = 0.7004`, the foil √(2π) sits `z_foil = −133.8` away, `|z_foil| ≫ 50`. A secondary confusion — that the ½ in the exponent doesn't matter — is exactly what the scale law `√a·∫e^{−ax²}dx = √π` (G3) pins down: the exponent's coefficient rescales the value by `1/√a`.

**4. Is the verifier deterministic and self-checking?** Yes. `build_results()` is a pure function of SEED and the module constants; `random.seed(SEED)` is re-seeded at the START of each MC gate so gate order cannot perturb the payload; every float enters the hashed payload via a fixed `f"{x:.6f}"` / `f"{z:.4f}"` string and every exact ratio as a `str(Fraction)`, so no float repr / wall-clock / PID / set-iteration instability enters. `main()` asserts an in-process double-run is byte-identical, `--selfcheck` prints "SELFCHECK: byte-identical", and two separate invocations reproduce the digest byte-for-byte. Whole-dict `results_sha256 = f8d553495590f7e0dc52d702e6b3dbb813464b4b48e8bc3a159f140b1e88c0d8`.

**5. Does the grounding actually support the claim, or is it overstated?** Honest and tight, seams disclosed. The core closed form, the scale/translation general form, and the even-moment closed form are all QUOTED verbatim on the pinned revision (the article is rich, with a polar-coordinates proof) — so nothing is oversold as a novel theorem. Disclosed: "moment" and "integration by parts" are grep 0 (my label + my recurrence route, which the page reaches by parameter differentiation instead — same closed form, independent route); the √(2π) foil confusion is my construction, not the page's; the exact `Fraction` verification, the MC agreement, the invariance legs, every z-value, SEED, and the digest are the firsthand contribution.

**6. Does it scale / is it robust?** The apparatus is general: `moment_ratio_recurrence(m, a)` takes any rational scale `a` and any moment index; `mc_integral` takes any half-width, scale, and shift. G1 exercises m=0..12; G3a checks 65 exact scale-invariance cases across 5 scales; G3b checks 6 `(a, μ)` MC configs; G2 uses N=400000 draws. The result is a property of the integral and its exact rational moment structure, not of a hard-coded value.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the single most plausible confusion (√π vs √(2π)) and refutes it at `|z_foil| = 133.8` on the same sample that accepts √π at `z = 0.70`. An error in the exponent normalization, a dropped ½, or the √(2π) confusion would fail either the exact scale law (G3, `exact_mismatches` > 0) or push the G2/G3b z's far out of band while the foil moved into band — the gates read in opposite directions.

**8. Any residual risk before ruling?** The Monte-Carlo legs are **iid** importance-sampling estimators (not autocorrelated sample paths), so the plain iid SE is the honest one and batch means are deliberately *not* used — stated in the verifier docstring; the exact `Fraction` backbone (G1) and scale-invariance leg (G3a) carry the claim RNG-free with independent routes (recurrence vs closed form vs double-factorial). The `erf(6)` truncation defect underflows to exactly 0.0 in IEEE double, so the honest target equals √π to machine precision (disclosed). The Gaussian integral is textbook (de Moivre 1733; Gauss 1809; the pinned page) and cited as such; the exact identity verification, the invariance legs, the MC agreement, the √(2π) falsification, and every z-value + the digest are the firsthand contribution. The paired sim-lab VERDICT 265 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
