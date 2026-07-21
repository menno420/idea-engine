# Buffon's needle: a short needle (ℓ ≤ d) dropped uniformly at random on a plane ruled with parallel lines spaced d apart crosses a line with probability exactly 2ℓ/(πd)

> **State:** sim-ready
> **Status:** sim-ready — PROPOSAL 244 (fleet geometric-probability slot) → VERDICT 257 (+13 offset)
> **Class:** geometric probability / integral geometry · **Target:** sim-lab
> **Grounding:** https://en.wikipedia.org/wiki/Buffon%27s_needle_problem?oldid=1356796927@9b4b9930ae1f4bafc5c7a44fcf2627a7807da30c · fetched 2026-07-21T05:49:13Z
>
> Verifier: `ideas/fleet/verify_244_buffon_needle.py` (stdlib only: json, hashlib, math, random, fractions).
> results_sha256 = `20f5616bae9df0533ab9ac0b6f23206cc1f457c2105b83103ed51bec98ff8a1b`

## Head

**Buffon's needle problem.** A needle of length `ℓ` is dropped uniformly at random on a plane ruled with parallel lines spaced a distance `d` apart. In the **short-needle** regime `ℓ ≤ d`, the probability that the needle crosses one of the lines is EXACTLY

    P = 2ℓ / (πd).

Equivalently, tossing the needle `N` times and counting `C` crossings gives an estimator of π via `π ≈ 2ℓN/(dC)` — the classic Monte-Carlo route to π.

**Why π appears.** The needle's position is fixed by its center's perpendicular offset to the nearest line and its orientation. By symmetry the offset `u ~ Uniform[0, d/2]` and the acute angle `θ ~ Uniform[0, π/2]` are independent uniforms; the needle crosses iff `u ≤ (ℓ/2)·sinθ`. The conditional crossing probability given `θ` is `min(1, (ℓ/d)·sinθ)`, and for `ℓ ≤ d` the clamp never binds, so averaging over `θ` gives `(ℓ/d)·E[sinθ] = (ℓ/d)·(2/π) = 2ℓ/(πd)`. π enters precisely because the orientation law is rotationally symmetric — the `2/π` is the mean of `sinθ` over a quarter turn.

## The drop (one line)

Center offset to the nearest line `u ~ Uniform[0, d/2]`; acute angle to the lines `θ ~ Uniform[0, π/2]`; the needle crosses iff `u ≤ (ℓ/2)·sinθ`. This is the standard short-needle reduction (`ℓ ≤ d`), and it is exactly the Bernoulli event the verifier samples.

## The exact result — reasoned to its fuller form (Q-0254 duty)

Write the crossing indicator `[u ≤ (ℓ/2)·sinθ]`. Because `u` is uniform on `[0, d/2]`, the conditional crossing probability given `θ` is

    P(cross | θ) = min(1, ((ℓ/2)·sinθ)/(d/2)) = min(1, (ℓ/d)·sinθ).

For the short needle `ℓ ≤ d` and `sinθ ≤ 1`, the argument `(ℓ/d)·sinθ ≤ 1` always, so the `min` clamp is inert and `P(cross | θ) = (ℓ/d)·sinθ`. Averaging over `θ ~ Uniform[0, π/2]`,

    P = (ℓ/d) · (2/π) ∫₀^{π/2} sinθ dθ = (ℓ/d) · (2/π) · 1 = 2ℓ/(πd).

The exact rational kernel `min(1, (ℓ/d)·s)` and the expectation factorization `E[cross] = (ℓ/d)·mean(s)` are what the verifier's G1 pins with `fractions.Fraction`; the continuous `2/π` average is what the Monte-Carlo G2 measures against `1/π` at `ℓ/d = 1/2`.

## The scale and parametrization invariance (constructive)

`P` depends only on the ratio `ℓ/d`: scaling both `ℓ` and `d` by any `k > 0` leaves `2ℓ/(πd)` unchanged, because the whole sample path (offset scale `d/2`, threshold `(ℓ/2)sinθ`) scales together and every crossing decision is preserved. Likewise the answer is independent of how the angle is parametrized: drawing `θ` over the full circle `[0, 2π)` and using `|sinθ|` yields the same crossing rate as the quarter-turn `[0, π/2]`. The verifier's G3 checks both directions with real Monte-Carlo samples.

## Method

A stdlib-only firsthand verifier `verify_244_buffon_needle.py` (SEED = `20260717`, Monte-Carlo size `N = 2,000,000`, invariance size `N_inv = 1,000,000`). It implements the DROP — it does NOT assume the closed form. A single `random.Random(SEED)` is seeded once and consumed in a fixed order across all Monte-Carlo legs; every float is stored with a fixed `f"{x:.12g}"` format and every exact rational serializes via `str(Fraction)`, so the serialization is invocation-stable.

Four gates, each with real teeth and its own direction:

- **G1 — EXACT identity (fractions.Fraction, no floats).** Over the rational grid `ℓ/d ∈ {1/4, 1/2, 3/4, 1}` and rational (Pythagorean) sines `s ∈ {0, 1/2, 3/5, 4/5, 1}` (20 pairs), the conditional crossing probability `P(cross | sinθ = s)` computed two independent ways — (a) directly `min(1, (ℓ·s)/d)`, and (b) via the offset-area model `((ℓ/2)·s)/(d/2)` clamped to 1 — is EXACTLY equal; `identity_mismatches = 0`. Plus the exact expectation factorization: for `θ` uniform over the sine multiset (`mean_sines = 29/50`), `E[cross] = (ℓ/d)·mean(s)` computed two ways is EXACTLY equal; `expectation_mismatches = 0`. An off-by-2 in the offset normalization or a `sin`-vs-`|sin|` bug fails this exactly.
- **G2 — Monte-Carlo agreement (|z| < 3).** Continuous model at `ℓ/d = 1/2` so `P = 1/π ≈ 0.318309886184`. Draw `N = 2,000,000` i.i.d. drops, count crossings `C = 636571`; `p̂ = 0.3182855`; binomial-proportion `z = (p̂ − 1/π)/√(P(1−P)/N) = −0.0740355452082`, `|z| < 3`. The drops are i.i.d. Bernoulli — NO autocorrelation, so no thinning is needed. Buffon π-estimate readout `π̂ = 2ℓN/(dC) = 3.14183335402`.
- **G3 — invariance / robustness (max |z| < 3).** (a) Scaling both `ℓ` and `d` by `k ∈ {2, 5, 0.3, 100}` leaves `P̂` within sampling error of `2ℓ/(πd) = 1/π`; each scaled config `|z| < 3` (worst `k = 5`: `z = −1.15685382694`). (b) Sampling `θ` over the full circle `[0, 2π)` with `|sinθ|` matches `θ ~ [0, π/2]`, `z = −0.229457897577`. `max|z| = 1.15685382694 < 3`.
- **G4 — falsifiability (large |z|).** Primary naive foil "no angle factor" `P_naive = ℓ/d = 0.5` (forgets the `2/π` angle-averaging): on the SAME G2 sample, `z_naive = (p̂ − 0.5)/√(0.5·0.5/N)`, `|z_naive| = 513.96622076 ≫ 3` → REJECTED. Subtler foil "assume E[sinθ] = ½ instead of 2/π" `P_naive2 = (ℓ/d)·½ = 0.25`: `|z| = 223.019509108 ≫ 3` → REJECTED. The gate passes by rejecting both naive alternatives.

**Determinism & digest.** `build_results()` is a pure function of `SEED` and the fixed params. `main()` builds the results twice in one process and asserts the canonical JSON forms are byte-identical, then prints a human summary and `results_sha256=<64hex>` on its own line, exiting 1 if any gate fails. Two separate shell invocations reproduce the identical digest. Full 64-hex:

```
results_sha256=20f5616bae9df0533ab9ac0b6f23206cc1f457c2105b83103ed51bec98ff8a1b
```

## Grounding & scope

The problem statement, the short-needle probability, the `ℓ ≤ d` (page: `l ≤ t`) case, and the π-estimation rearrangement are all grounded in the English Wikipedia article **"Buffon's needle problem"** at pinned revision `https://en.wikipedia.org/wiki/Buffon%27s_needle_problem?oldid=1356796927`@`9b4b9930ae1f4bafc5c7a44fcf2627a7807da30c` (fetched 2026-07-21T05:49:13Z; the raw wikitext is 28001 bytes and its self-computed SHA-1 equals the pinned oldid's sha1 — exact match, verified two ways: fetch + `sha1sum`, and grep of the formula both directions). The page uses `l` for the needle length and `t` for the strip width; the only relabel is the trivial `l → ℓ`, `t → d`.

Honest quoted-vs-derived split (grep of the pinned raw wikitext, both directions):

| # | Cited value | Quoted / derived | Exact wikitext snippet (pinned revision 1356796927) |
|---|---|---|---|
| 1 | short-needle probability `p = (2/π)·(l/t)` | **quoted** | `p=\frac{2}{\pi} \cdot \frac{l}{t}` |
| 2 | closed form `= 2l/(tπ)` | **quoted** | `\frac{2 l}{t\pi}` |
| 3 | short-needle case `l ≤ t` | **quoted** | `=== Case 1: Short needle ({{math|''l'' ≤ ''t''}}) ===` |
| 4 | π-estimation rearrangement `π = 2l/(tP)` | **quoted** | `\pi = \frac{2l}{tP}` |
| 5 | SEED = 20260717 | **derived** | absent (grep count 0) |
| 6 | results_sha256 digest | **derived** | absent (grep count 0) |
| 7 | four gate z-values (G2 `\|z\|`, G3 max`\|z\|`, G4 foils) | **derived** | absent — page carries no z-values |
| 8 | exact discrete-Buffon Fraction identity (G1) | **derived** | absent — page states the average, not the rational kernel check |
| 9 | scale-invariance robustness numbers (G3) | **derived** | absent |
| 10 | both naive-foil `\|z\|` rejections (G4) | **derived** | absent |

**Scope caveat.** The pinned article states the short-needle formula, the `l ≤ t` case, and the π-estimation rearrangement in prose/formulae. What is established FIRSTHAND by the verifier — not taken from Wikipedia — is the computational proof: the exact rational crossing kernel and expectation factorization via `Fraction` (G1), the i.i.d. Monte-Carlo `z` against `1/π` (G2), the scale- and parametrization-invariance `z` values (G3), the two falsification `z` values (G4), and the results-dict digest. The page carries no `z`-values, no SEED, and no digest.

## Gate power + margin ledger

| Gate | Type | Threshold | Observed | Margin | Verdict |
|---|---|---|---|---|---|
| G1 exact identity (route a == route b, 20 pairs) | zero-mismatch (Fraction) | 0 mismatches | identity_mismatches=0 | exact | PASS |
| G1 expectation factorization E=(ℓ/d)·mean(s) | zero-mismatch (Fraction) | 0 mismatches | expectation_mismatches=0 | exact | PASS |
| G2 MC vs 1/π (N=2e6, i.i.d.) | match (\|z\|<3) | <3σ | \|z\|=0.0740355452082 | 2.93σ headroom | PASS |
| G3(a) scale invariance k∈{2,5,0.3,100} | each \|z\|<3 | <3σ | max at k=5, \|z\|=1.15685382694 | 1.84σ headroom | PASS |
| G3(b) full-circle \|sinθ\| == [0,π/2] | \|z\|<3 | <3σ | \|z\|=0.229457897577 | 2.77σ headroom | PASS |
| G4 foil "no angle factor" P=ℓ/d rejected | reject (\|z\|>3) | >3σ | \|z\|=513.96622076 | ≫3σ | PASS |
| G4 foil "E[sinθ]=½" P=(ℓ/d)/2 rejected | reject (\|z\|>3) | >3σ | \|z\|=223.019509108 | ≫3σ | PASS |

## Probe report (v0, self-adversarial)

**1. What is this really?** Buffon's needle: a needle of length `ℓ ≤ d` dropped uniformly at random on a plane ruled with parallel lines spaced `d` apart. The claim: the crossing probability is EXACTLY `P = 2ℓ/(πd)`. Verified by a firsthand DROP simulator (offset `u ~ Uniform[0, d/2]`, angle `θ ~ Uniform[0, π/2]`, cross iff `u ≤ (ℓ/2)sinθ`) plus an exact `Fraction` kernel check — the `2/π` angle average is measured, not assumed.

**2. What would make it false?** Any `(ℓ/d, s)` pair where the two exact routes to `min(1, (ℓ/d)s)` disagree, or the expectation factorization mismatches (G1 `> 0`); a sampled crossing-rate off `1/π` by `|z| ≥ 3` at `ℓ/d = 1/2` (G2); any scaled config or the full-circle parametrization drifting `|z| ≥ 3` (G3); or a naive foil NOT being rejected (G4). Any gate failing → REJECT.

**3. Simplest version that still bites?** The G2 leg alone: 2,000,000 i.i.d. drops at `ℓ = 1, d = 2`, count crossings, compare `p̂` to `1/π`. `p̂ = 0.3182855` vs `0.318309886184`, `|z| = 0.074`. The G1 Fraction leg is the exact spine: it needs no floats and would catch an off-by-2 in the offset normalization instantly.

**4. What is the counterintuitive core?** π appears in a problem with no circles — because the needle's orientation is uniform on a half-turn and `E[sinθ] = 2/π`. The naive "the answer is just `ℓ/d`" (the fraction of the strip the needle could span) forgets that a randomly-angled needle projects to `(2/π)` of its length on average; that single factor is the whole subtlety, and G4 rejects the no-factor guess at `|z| ≈ 514`.

**5. Where could I be fooling myself?** Assuming the closed form instead of the drop. The verifier samples the raw geometric event `u ≤ (ℓ/2)sinθ` and only THEN compares the rate to `1/π` — the `2/π` is a measured agreement, not an input. The exact-`Fraction` G1 uses no floats at all, and the offset-area route is computed structurally differently from the direct route, so an off-by-2 or `sin`-vs-`|sin|` bug cannot hide.

**6. What is the honest calibration?** SEED=20260717: G1 `identity_mismatches=0`, `expectation_mismatches=0` over 20 pairs; G2 `P=1/π=0.318309886184`, crossings=636571, `p̂=0.3182855`, `z=−0.0740355452082` (`<3`), `π̂=3.14183335402`; G3 `max|z|=1.15685382694` (worst scale `k=5`), full-circle `z=−0.229457897577`; G4 foil-no-angle-factor `|z|=513.96622076`, foil-half-mean-sine `|z|=223.019509108`. Exit 0; `results_sha256=20f5616b…ff8a1b`; two runs byte-identical.

**7. What decision does it change?** When a random-orientation geometric event is in play, do not reason by "fraction of the gap the object spans" — average over the orientation, which contributes a `2/π` for a uniform half-turn. The falsifiability gate kills the no-angle-factor guess at `|z| ≈ 514` and the `E[sinθ]=½` guess at `|z| ≈ 223`, so a heuristic that "feels linear in `ℓ/d`" is decisively rejected against the true `2ℓ/(πd)`.

**8. How will a verdict session know it reproduced the head?** Re-run the stdlib verifier under SEED=20260717 and confirm `all_pass=true`, `first_failing_gate=null`, and results-dict sha256 `20f5616bae9df0533ab9ac0b6f23206cc1f457c2105b83103ed51bec98ff8a1b` byte-for-byte (in-process double-run guard AND a separate re-invocation are byte-identical); any gate fail or digest mismatch is a REJECT.

**Recommendation: sim-ready**
