# Ask for "the probability that a random chord is longer than the inscribed triangle's side" and there is no single answer: three equally natural definitions of "random chord" give exactly 1/3, 1/2, and 1/4 — the question is underspecified, not hard

> **State:** sim-ready
> **Class:** geometric probability · continuous sample-space non-uniqueness · counterintuitive
> **Target:** sim-lab (VERDICT 209, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)@884f5add3a888fef5d10c73dcd4d2bac5490f568 · fetched 2026-07-20
> **Reference (external, reachable):** [Bertrand paradox (probability) — Wikipedia](https://en.wikipedia.org/w/index.php?title=Bertrand_paradox_(probability)&oldid=1363409876) — raw wikitext verified reachable 2026-07-20 (oldid 1363409876, 13700 bytes; self-computed sha1 884f5add3a888fef5d10c73dcd4d2bac5490f568 matches MediaWiki's own sha1), stating the three arguments "all apparently valid yet yielding different results": the "random endpoints" method gives 1/3, the "random radial point" method 1/2, and the "random midpoint" method 1/4. The exact-rational geometry and deterministic quadrature agreement below are firsthand.
> **Verifier (firsthand):** ideas/fleet/bertrand_paradox_chord.py · results-dict sha256 ab79371c9908f7b16f9478d41969e224eb4c95c19d237a2773df693173b5c3cb

## The phenomenon (one line)
"Random chord" is not one experiment but many: pick chords by their two endpoints, by a point on a radius, or by their midpoint, and the probability the chord beats the inscribed equilateral triangle's side is exactly 1/3, 1/2, or 1/4 respectively — same circle, same event, three different numbers.

## Domain
Geometric probability — the non-uniqueness of "uniform at random" on a continuous (infinite) sample space. Outside fleet-ops, venture, and game-theory.

## The folk belief
"Choose a chord at random" sounds like a single, well-posed experiment, so "the probability the chord is longer than the triangle side" should be one definite number. Apply the principle of indifference — treat every chord as equally likely — and read off the answer.

## The thesis (reasoned to its fuller form — Q-0254 duty)
The phrase "a chord chosen at random" silently assumes a uniform distribution over the space of chords, but a chord is a continuous object with several inequivalent natural parametrizations, and "uniform" means something different under each. There is no canonical uniform measure on the chords of a circle the way there is on a finite set; the principle of indifference, applied to different coordinates, produces different — and each internally consistent — distributions.

Fix a unit circle; the inscribed equilateral triangle has side √3. A chord is "long" iff its perpendicular distance from the centre is d < 1/2 (chord = 2√(1−d²) > √3 ⇔ d < 1/2). Three natural mechanisms:
- **Random endpoints.** Two independent uniform points on the circumference. By rotational symmetry fix one; the chord beats the side iff the second lands on the far third of the circumference. P = **1/3**.
- **Random radial point.** Pick a radius, then a point uniform along it; the chord is perpendicular there. It is long iff the point is in the inner half of the radius. P = **1/2**.
- **Random midpoint.** Pick a point uniform over the disk as the chord's midpoint. Long iff the midpoint lies inside the concentric disk of half the radius, whose area is a quarter. P = **1/4**.

All three are legitimate; none is "the" answer. The resolution is not that two are wrong — it is that "at random" was never fully specified. Jaynes later argued that a maximum-ignorance (translation- and scale-invariant) requirement singles out the 1/2 "random radial" answer for a physical needle-tossing setup, but that adds a symmetry postulate the bare question does not contain. The lesson stands: on an infinite sample space, "uniform" is a choice, not a given.

## The formal model / Pinned world (committed constants)
- Unit circle R = 1 (swept over R ∈ {1,2,5,10} for scale-invariance); inscribed equilateral triangle side = √3·R; a chord is long iff length > √3·R ⇔ perpendicular distance d < R/2.
- Three mechanisms: endpoints (two uniform circumference points), radial (uniform distance d ∈ [0,R]), midpoint (uniform point in the disk).
- Exact closed forms: endpoints 1/3, radial 1/2, midpoint 1/4 (fractions.Fraction).
- SEED = 20260717; M_TRIALS = 200000; Z_GATE = 3.0.
- Deterministic quadrature: GRID_1D = 200000 (endpoints, radial), GRID_2D = 1500 per axis over the disk (midpoint); agreement tolerance GRID_TOL = 1e-3.

## Pre-registered gates
- **G1 — Monte-Carlo matches each closed form (≥3σ).** For each mechanism at R=1, simulate M=200000 chords; the hit rate p̂ must agree with p* ∈ {1/3,1/2,1/4} within 3 binomial σ: z = |p̂−p*| / √(p*(1−p*)/M) < 3.0. Confirms each sampler implements its stated mechanism.
- **G2 — Exactly-true (exact-rational geometry ≡ closed form, quadrature-corroborated).** For each mechanism, derive the probability as an exact Fraction from the geometric threshold (π cancels) and assert it equals the pre-registered closed form; independently confirm with a deterministic exhaustive grid quadrature within 1e-3. Not a sampling test: 1/3, 1/2, 1/4 exactly.
- **G3 — Robustness / shift + genuine non-uniqueness.** Each mechanism's probability must be scale-invariant — recomputed across R ∈ {1,2,5,10}, within-mechanism spread < 0.01 — AND the three answers must genuinely differ: cross-mechanism spread = 1/2 − 1/4 = 0.25 > 0.08. Shows the paradox is structural (not an R=1 or sampling artifact): each number is stable, and they are really three different numbers.

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 all pass under SEED=20260717 with a byte-identical results-dict sha256 across an in-process double-run and a separate cross-invocation. Any gate failing, or any digest drift, blocks.

## Dry-sim results (SEED=20260717, verbatim from ideas/fleet/bertrand_paradox_chord.py)
- G1: endpoints p̂=0.331715 vs 1/3, z=1.535286 → pass; radial p̂=0.499135 vs 1/2, z=0.77368 → pass; midpoint p̂=0.24883 vs 1/4, z=1.208371 → pass.
- G2: endpoints exact 1/3, quadrature 0.33333; radial exact 1/2, quadrature 0.5; midpoint exact 1/4, quadrature 0.249997 — all exact_match=true, quadrature_agrees=true → pass.
- G3: within-mechanism spread {endpoints 0.0, radial 0.0, midpoint 0.0} < 0.01 (scale-invariant across R∈{1,2,5,10}); cross-mechanism spread = 0.25 > 0.08 (answers_differ=true) → pass.
- all_pass = true. Results-dict sha256 `ab79371c9908f7b16f9478d41969e224eb4c95c19d237a2773df693173b5c3cb` (byte-identical across a second process).

## Reproduce
```
python3 ideas/fleet/bertrand_paradox_chord.py
```
Prints the pretty results dict then `Results-JSON sha256: ab79371c9908f7b16f9478d41969e224eb4c95c19d237a2773df693173b5c3cb`; exits 0 iff all_pass.

## Verifier
`ideas/fleet/bertrand_paradox_chord.py`, stdlib only (hashlib, json, math, random, fractions). Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: the compact-canonical sha256 over the results dict is the digest, the dict carries no self field, floats rounded 6 dp, no on-disk JSON, in-process double-run asserts byte-identical.

## Why it matters
The trap is reading "at random" as self-defining. On a finite set it is — every outcome equally likely is unambiguous — but on a continuous space the answer is a function of the coordinate you called uniform, and swapping coordinates silently swaps distributions. The fleet analogue: "sample a random task / a random shard / a random path uniformly" is under-specified whenever the object has more than one natural parametrization (by identity, by load, by position in a queue), and three defensible "uniform" samplers can return three different tail probabilities from the same population. Before trusting a "random baseline," pin the mechanism — which coordinate is uniform — or the number is not yet defined.

## Dedup
No Bertrand-paradox / random-chord / geometric-non-uniqueness head exists in ideas/ (grepped bertrand, chord, inscribed, geometric probability on origin/main — no fleet hit). Distinct mechanism from the shipped counterintuitive-probability heads: birthday and coupon-collector concern discrete collisions, inspection and arcsine concern renewal/paths, Berkson and Simpson concern conditioning, 100-prisoners concerns permutation cycles, giant-component concerns graph thresholds, Efron's dice concern intransitivity. This is uniquely the non-existence of a canonical uniform measure on a continuous sample space — the same event has three exact probabilities under three natural "uniform" definitions.

## Model basis (declared model-dependence — the P024 discipline)
Depends on: (a) taking each of the three sampling mechanisms as the definition of "uniform" — the whole point is that no bare "uniform over chords" exists; (b) the fixed inscribed-equilateral-triangle threshold (chord > √3·R ⇔ d < R/2). The claim is precisely that the answer is mechanism-dependent: 1/3, 1/2, 1/4 are exact under endpoints/radial/midpoint respectively; there is no single "correct" number, and asserting one requires an extra symmetry postulate (Jaynes' maximum-ignorance argument favours 1/2) the bare question does not supply.

## Probe report (v0, 2026-07-20)
**1. Is the head crisp and falsifiable?** Yes — three exact numbers (1/3, 1/2, 1/4) with exact-Fraction derivations and a byte-pinned verifier; any gate failure or digest drift falsifies it.
**2. Is it counterintuitive-but-true?** Yes — a well-posed-sounding probability question has no single answer; three equally valid "uniform" definitions give exactly 1/3, 1/2, 1/4, and each is exactly true under its mechanism.
**3. Is the model clean and fully pinned?** Yes — unit circle, √3 threshold ⇔ d<1/2, three explicit samplers, SEED=20260717, all constants committed; nothing tunable post-hoc.
**4. Is there an exactly-true gate?** Yes — G2 derives each probability as an exact Fraction from the geometry (π cancels) equal to 1/3, 1/2, 1/4, corroborated by deterministic exhaustive quadrature within 1e-3; no sampling involved.
**5. Is it deterministic and reproducible?** Yes — results-dict sha256 ab79371c9908f7b16f9478d41969e224eb4c95c19d237a2773df693173b5c3cb is byte-identical across an in-process double-run and a separate process invocation.
**6. Is the grounding real and external?** Yes — Wikipedia "Bertrand paradox (probability)" raw wikitext pinned at oldid 1363409876 (self-sha1 884f5add3a888fef5d10c73dcd4d2bac5490f568, matching MediaWiki's), fetched live 2026-07-20, states all three method names and the 1/3, 1/2, 1/4 results verbatim; the exact-Fraction and quadrature gates are firsthand.
**7. Could it collide with a shipped proposal?** No — no random-chord / Bertrand / continuous-sample-space head exists, and the mechanism is distinct from every shipped counterintuitive-probability head (see Dedup).
**8. What would make sim-lab reject it?** A non-reproducible digest, a gate failing under an independent reimplementation, or a mechanism whose Monte-Carlo estimate disagrees with its exact Fraction — the natural sim-lab generalization is to re-derive each probability by an independent method (exact integration for the radial law, arc-length for endpoints) and confirm the three exact values 1/3, 1/2, 1/4.

**Recommendation: sim-ready**
