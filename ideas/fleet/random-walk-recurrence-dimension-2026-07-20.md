# A drunk man always finds his way home, but a drunk bird may be lost forever: a symmetric random walk returns to its start with probability 1 in two dimensions yet only about 34% of the time in three.

> **State:** sim-ready
> **Class:** fleet · probability · random-walk recurrence
> **Target:** sim-lab (VERDICT 225, +13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Random_walk&oldid=1359285496@bdcc6ea9d1ec88b8313eb470f475758301f9dd77 · fetched 2026-07-20
> **Verifier (firsthand):** stdlib-only, SEED=20260717; results-dict sha256 66ca292316986d8121a552e3c4c61557182d787b2e25cf54659a0130d0dede07

## The phenomenon (one line)
A nearest-neighbour walker that steps to a uniformly random neighbour on the integer lattice is certain to return to its starting point in one and two dimensions (recurrent), but in three dimensions it escapes to infinity and never comes back about 66% of the time (transient) - the return probability drops from exactly 1 to about 0.3405 the moment a third axis is added.

## The folk belief
"Wander at random long enough and you always get back to where you started." True on a line and true on a plane - but false in space. Intuition reads "more room to roam" as merely slower return, not permanent escape, so it treats dimension as a quantitative dial. It is not: d=3 is a hard qualitative threshold. Adding one axis converts certain return into probable never-return.

## The recurrence thesis (reasoned to its fuller form - Q-0254 duty)
Recurrence is governed by the Green's function at the origin, U = sum_{n>=0} p_d(2n), where p_d(2n) is the probability the walk is back at the origin after 2n steps. A walk is recurrent (returns with probability 1) iff U diverges, and transient (return probability 1 - 1/U < 1) iff U is finite (Polya 1921; Chung-Fuchs). The local central limit theorem gives p_d(2n) ~ 2 (d / (4 pi n))^{d/2}, so the summand decays like n^{-d/2}. The series sum n^{-d/2} diverges for d <= 2 and converges for d >= 3: the exponent crosses the summability threshold exactly at d=2. Hence 1D and 2D are recurrent (U infinite, return probability 1) while 3D is transient (U = Watson's integral ~ 1.5164, return probability 1 - 1/1.5164 ~ 0.3405). The surprise is entirely in that one integer step of the exponent.

## The formal model (committed constants, exact)
Simple symmetric random walk on Z^d: from any site the walker moves to one of its 2d nearest neighbours with equal probability 1/(2d), independently each step, on the unbounded lattice in discrete time, started at the origin. "Return" = the walk revisits the origin at some step >= 1. Exact combinatorics of length-2n closed walks:
- 2D: a2(n) = C(2n,n)^2 (Vandermonde), so p2(2n) = C(2n,n)^2 / 4^{2n}.
- 3D: a3(n) = sum_{i+j+k=n} (2n)! / (i!^2 j!^2 k!^2), so p3(2n) = a3(n) / 6^{2n}.

## Pinned world (committed constants)
SEED=20260717. Exact enumeration at 2n in {2,4,6} (2D) and {2,4} (3D). Scaled-decay probes at n=2000 (2D) and n=60 (3D). Monte-Carlo: K=15000 walks per dimension, horizons T_lo=100 and T_hi=1200. RNG protocol: one random.Random(SEED) stream; all K 2D walks generated first (index 0..K-1), then all K 3D walks; each step draws rng.randrange(2d) as the move index (axis = idx>>1, sign = idx&1); a walk stops at its first return.

## Pre-registered gates (sim-ready iff ALL hold, in order)
- **G1 - exact 2D enumeration (exactly-true).** For 2n in {2,4,6}, the brute-force count of length-2n closed 2D walks equals the closed form C(2n,n)^2 exactly (integer equality). Direction: exact ==.
- **G2 - exact 3D enumeration (exactly-true).** For 2n in {2,4}, the brute-force count equals sum_{i+j+k=n} (2n)!/(i!^2 j!^2 k!^2) exactly (integer equality). Direction: exact ==.
- **G3 - 2D non-summable (recurrent).** n * p2(n) at n=2000 lands in [0.30, 0.335] (predicted 1/pi ~ 0.3183); the return series behaves like sum 1/(pi n), which diverges, forcing return probability 1. Direction: matches 1/n decay => divergent => recurrent.
- **G4 - 3D summable (transient).** n^{1.5} * p3(n) at n=60 lands in [0.19, 0.29] (predicted 2(3/4pi)^{1.5} ~ 0.2333); the return series behaves like sum n^{-3/2}, which converges, so return probability < 1. Direction: matches n^{-3/2} decay => convergent => transient.
- **G5 - 3D empirically transient.** The Monte-Carlo within-horizon 3D return fraction f3 sits at least 3 sigma below the recurrence line 0.5 and inside [0.28, 0.38] (near Polya's constant 0.3405). Direction: (0.5 - f3)/sigma >= 3.
- **G6 - 2D dominates and grows with horizon (divergent-return signature, robustness/shift gate).** f2 exceeds f3 by >= 3 sigma, AND f2 rises with the horizon by >= 3 sigma (T=100 -> 1200) while 3D stays comparatively flat (2D horizon-shift z exceeds 3D's by at least 3). Direction: 2D return fraction keeps climbing (no ceiling); 3D has plateaued.

## Pre-registered decision rule
sim-ready iff G1 and G2 and G3 and G4 and G5 and G6 all hold AND the full battery is byte-identical across an in-process double run. Any gate red => not sim-ready.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```json
{
  "determinism_double_run_ok": true,
  "exact_2d": [
    {
      "2n": 2,
      "closed": 4,
      "enum": 4,
      "eq": true
    },
    {
      "2n": 4,
      "closed": 36,
      "enum": 36,
      "eq": true
    },
    {
      "2n": 6,
      "closed": 400,
      "enum": 400,
      "eq": true
    }
  ],
  "exact_3d": [
    {
      "2n": 2,
      "closed": 6,
      "enum": 6,
      "eq": true
    },
    {
      "2n": 4,
      "closed": 90,
      "enum": 90,
      "eq": true
    }
  ],
  "f2_hi": 0.6814,
  "f2_lo": 0.5808,
  "f3_hi": 0.335467,
  "f3_lo": 0.314667,
  "gates": {
    "G1": true,
    "G2": true,
    "G3": true,
    "G4": true,
    "G5": true,
    "G6": true
  },
  "mc_K": 15000,
  "mc_T_hi": 1200,
  "mc_T_lo": 100,
  "scaled_2d_n2000": 0.31827,
  "scaled_2d_target_1_over_pi": 0.31831,
  "scaled_3d_n60": 0.231839,
  "scaled_3d_target": 0.233291,
  "seed": 20260717,
  "sim_ready": true,
  "z_dominate_2d_over_3d": 63.8705,
  "z_shift_2d": 18.1551,
  "z_shift_3d": 3.8467,
  "z_transient_3d": 42.6792
}
```
results_sha256=66ca292316986d8121a552e3c4c61557182d787b2e25cf54659a0130d0dede07

**Disclosed results-dict sha256 = 66ca292316986d8121a552e3c4c61557182d787b2e25cf54659a0130d0dede07**

## Verifier
`ideas/fleet/random-walk-recurrence-dimension-2026-07-20.py` - stdlib only (`hashlib, json, math, random, fractions`).
```reproduce
python3 ideas/fleet/random-walk-recurrence-dimension-2026-07-20.py
```

## Why it matters
Dimension is not a dial you can trade against patience. A search, rendezvous, gossip, or coverage process that is effectively planar is guaranteed to revisit any target given time; give it a genuine third degree of freedom and revisit stops being certain - a constant fraction of trajectories escape forever no matter how long you wait. The same threshold governs polymer looping, diffusion-limited capture, and whether two independent random searchers are guaranteed to meet.

## Dedup
Grepped all lanes (ideas/**): the only "polya" hit is the distinct Polya-URN card (P208, reinforcement/exchangeability). Existing random-walk cards cover the arcsine sojourn law, gambler's-ruin first-passage, Banach-matchbox imbalance, and Benford mantissa - none the return-probability / dimension-dependence result. Green's-function / return-probability / drunkard: zero hits. Head is un-built.

## Model basis (declared model-dependence - the P024 discipline)
The claim is a theorem of the simple symmetric nearest-neighbour walk on Z^d. It depends on: uniform steps to the 2d neighbours, an unbounded lattice, and discrete time. It does NOT hold universally - biased walks, bounded domains, long-range (heavy-tailed) steps, or non-lattice graphs can move the recurrence threshold. The 2D-recurrent / 3D-transient split is specific to the standard model committed above.

## One-line design fix
When a random process must guarantee return or rendezvous, keep it effectively <= 2-dimensional (pin a coordinate); when it must guarantee escape or dispersal, give it a real third degree of freedom.

## Probe report (v0, 2026-07-20)
**1. Is the head counterintuitive-but-true under a clean, standard model?** Yes - Polya (1921). The 2D-recurrent / 3D-transient split is textbook, genuinely surprising to intuition, and exactly true under the committed simple-symmetric-walk model.
**2. Is there an exactly-true anchor, not just a simulation?** Yes - G1/G2 match brute-force enumeration of every step sequence to the closed forms C(2n,n)^2 and sum (2n)!/(i!^2 j!^2 k!^2) with exact integer equality.
**3. Is the verifier deterministic and stdlib-only?** Yes - SEED=20260717, a single committed random.Random stream, no third-party imports, and the battery is byte-identical across an in-process double run and across separate invocations.
**4. Are the gates directional and pre-registered?** Yes - six gates each with a stated direction; thresholds are fixed by the local-CLT constants (1/pi and 2(3/4pi)^{1.5}) and the recurrence line 0.5 before running.
**5. Does the grounding cite an external source accurately?** Yes - Wikipedia's *Random walk* article is pinned by revision id and a hex SHA1 of the raw wikitext; the caveat states only what the page verbatim asserts versus what the verifier proves firsthand. The article states Polya's recurrence theorem (the simple symmetric lattice walk is recurrent in dimensions 1-2 and transient in dimension 3 and higher), reporting that in 1921 George Polya proved almost-sure return in the 2-dimensional walk while for 3 dimensions or higher the probability of returning to the origin decreases (to roughly 34% in 3D), and carries the "drunk man / drunk bird" aphorism ("A drunk man will find his way home, but a drunk bird may get lost forever"). The page asserts these results but does NOT contain the brute-force enumeration identity, the exact Green's-function decay-law check, or the seeded simulation - those are proven firsthand by the committed verifier. (Note: the exact figure 0.3405 does not appear in the page text, which states "roughly 34%"; the constant is cited only via the linked MathWorld "Polya's Random Walk Constants".)
**6. Could the result be a numerical artifact?** No - the exact gates use integer arithmetic; the decay-law gates use Fraction-exact single-step probabilities; the Monte-Carlo gates only corroborate, with >=3 sigma margins against the wrong hypothesis (3D recurrent / dimensions equal).
**7. Is it distinct from prior cards (dedup)?** Yes - distinct from the Polya-urn card (P208) and from the four existing random-walk cards (arcsine, gambler's ruin, Banach matchbox, Benford); the cross-lane grep is clean.
**8. Is it reproducible by an independent sim-lab re-implementation?** Yes - the closed forms and the RNG protocol are fully specified, so a clean-room build under the same seed should reproduce the disclosed digest byte-for-byte.
**Recommendation: sim-ready**
