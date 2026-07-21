# Counting necklaces under rotation (cyclic group C_n): the Burnside / Pólya orbit count

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** fleet · combinatorics / group-action orbit count (necklaces)
**Proposal:** 236 → Verdict 249 (+13 offset)
**Verifier:** [`verify_236_necklace_burnside.py`](verify_236_necklace_burnside.py) · stdlib only · SEED=20260717
**Digest:** `results_sha256 = 4ce987eb3da551811389d54d5d70f72ec27cadcd8600efc73320ad9860938ece`

## Claim

The number of distinct necklaces of n beads in k colours, counting two colourings equivalent when one is a rotation of the other (the cyclic group C_n acting on bead positions), is the exact integer

    N_k(n) = (1/n) · Σ_{d | n} φ(d) · k^(n/d)

where φ is Euler's totient. This is Burnside's lemma specialised to C_n: each rotation by s fixes k^gcd(s,n) colourings, and grouping the n rotations by the order d = n/gcd(s,n) of the cyclic subgroup they generate gives φ(d) rotations each fixing k^(n/d) colourings.

## Exact reference

Headline instance n = 6, k = 3. Divisors of 6: {1, 2, 3, 6}.

| divisor d | φ(d) | k^(n/d) = 3^(6/d) | φ(d)·k^(n/d) |
|---|---|---|---|
| 1 | 1 | 3^6 = 729 | 729 |
| 2 | 1 | 3^3 = 27 | 27 |
| 3 | 2 | 3^2 = 9 | 18 |
| 6 | 2 | 3^1 = 3 | 6 |

Sum = 780, and N_3(6) = 780 / 6 = **130** (exact integer — the Fraction reduces, denominator 1). The naive "divide by the group order" rule would give k^n / n = 729 / 6 = 121.5, which is not even an integer and undercounts by ignoring the non-free orbits (the 3 constant colourings and the shorter-period colourings whose orbits are smaller than n).

## Four gates (each in its own direction)

- **G1 — exact orbit count (`fractions.Fraction`).** Over a 5-instance panel — (6,3)=130, (4,2)=6, (5,2)=8, (6,2)=14, (4,3)=24 — the closed-form Fraction (1/n)·Σφ(d)k^(n/d) reduces to an integer (denominator 1) and equals BOTH the brute-force orbit count (enumerate every k^n colouring, bucket by the lexicographically minimal rotation) AND the expected value, on every row. The headline returns `Fraction(130, 1)`.
- **G2 — Monte-Carlo agreement.** Drawing 400 000 uniform random colourings of the headline (6, 3), the unbiased estimator N_hat = k^n·mean(1/orbit_size) agrees with the exact N = 130 at N_hat = 129.934834, z = −0.842145, |z| < 3. (Unbiased because Σ_colourings 1/orbit_size equals the orbit count, so E[k^n·(1/orbit_size)] = N.)
- **G3 — invariance / robustness.** The orbit count is a function of orbit structure only, hence invariant to a colour relabelling. Permuting every colour by the cyclic +1 (mod k) map and re-counting reproduces the brute orbit count for (6, 3) → 130 and (5, 2) → 8. A canonical form that was not rotation-only would break this against G1.
- **G4 — falsifiability.** On the same MC sample, the plausible naive rule "N == k^n / n" (divide by the group order, ignoring non-free orbits) with value 729/6 = 121.5 is rejected at z_reject = 109.003526, |z| ≥ 6.

All four gates PASS; `all_gates_pass = true`, `first_failing_gate = null`, `decision = PASS`. Deterministic: in-process double-run and separate re-invocation are byte-identical; `results_sha256 = 4ce987eb3da551811389d54d5d70f72ec27cadcd8600efc73320ad9860938ece`.

## Grounding

Necklace (combinatorics) (Wikipedia), pinned revision:
`https://en.wikipedia.org/w/index.php?title=Necklace_(combinatorics)&oldid=1364788638@1f77b5497f8b77bfcee5550af16aeb4cbd1ed1f7` (rev 2026-07-18, 9449 bytes; API `revisions.sha1` == self-computed `sha1sum` of the raw wikitext — exact match). Note the article writes the count as N_n(k) (length subscript, colour argument); the claim here writes N_k(n) — the same formula, subscript/argument convention transposed.

- **Quoted** literally on the pinned revision: the closed-form necklace count `N_n(k)=\frac{1}{n}\sum_{d\mid n}\varphi(d)k^{n/d}` (and its equivalent gcd form `\frac{1}{n}\sum_{i=1}^n k^{\gcd(i,n)}`), with φ named "Euler's totient function"; the cyclic-group orbit framing ("represent a necklace as an orbit of the cyclic group acting on n-character strings", "the action of the cyclic group C_n acting on the set of all functions"); the attribution to "Pólya's enumeration theorem"; and the aperiodic/Lyndon count `M_n(k)=\frac{1}{n}\sum_{d\mid n}\mu(d)k^{n/d}` with μ the "Möbius function", "aperiodic necklace" and "Lyndon word" (Moreau's necklace-counting function).
- **Derived** firsthand (grep count 0 as a necklace count on the pinned raw wikitext): the value N_3(6) = 130 (the only "130" on the page is inside an archive-URL timestamp `web/20061002130346`, NOT a necklace count — no small-case table on this revision lists it); the headline parameters (n=6, k=3) and k^n = 729 (grep count 0 for "729"); the literal word "Burnside" (count 0 — the page attributes the count to Pólya's enumeration theorem, of which Burnside's lemma is the specialisation, so the identity is quoted but that name is ours); the 5-instance panel values; the naive falsifier N = k^n/n = 121.5; and every Monte-Carlo statistic (G2 N_hat = 129.934834, z = −0.842145; G4 z_reject = 109.003526) and the results_sha256. The closed-form identity is textbook and cited as such; the firsthand contribution is the exact instantiation at (6, 3), the brute-force orbit-enumeration cross-check, the four-gate machine-checked reproduction, and the falsification of the "divide by group order" error. Nothing oversold as novel.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 computes each panel instance's count two independent exact ways — the closed form (1/n)·Σφ(d)k^(n/d) as a `fractions.Fraction`, and a brute-force orbit count that enumerates every one of the k^n colourings and buckets each by the lexicographically minimal rotation — and checks equality of exact integers, additionally asserting the Fraction reduces (denominator 1). The headline returns `Fraction(130, 1)` == brute 130 == expected 130; the other four panel rows return 6, 8, 14, 24, each matching brute and expected exactly.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?** No. Every headline value is fixed by exact arithmetic (G1) before any RNG is touched — both the closed-form Fraction and the exhaustive brute enumeration. The Monte-Carlo gate (G2, N=400000) only confirms the exact target N = 130 survives under sampling (z = −0.842145, |z| < 3); the estimator N_hat = k^n·mean(1/orbit_size) is unbiased by construction because Σ_colourings 1/orbit_size equals the orbit count.

**3. What is the most plausible wrong belief this could be confused with?** That you count orbits by simply dividing the colouring count by the group order: N = k^n / |C_n| = k^n / n. G4 pre-registers exactly that naive rule (value 729/6 = 121.5) and rejects it at z_reject = 109.003526 (≥6) on the SAME sample where the correct N = 130 agrees at z = −0.842145. The rule fails because C_n does not act freely — constant and shorter-period colourings sit in orbits smaller than n, so orbit sizes are not all equal and 121.5 is not even an integer.

**4. Is the verifier deterministic and self-checking?** Yes. The single sampling gate consumes one seeded `random.Random(20260717)` in fixed order; `build_results()` is a pure function of SEED and the module constants (no wall-clock / PID / unordered-set iteration in the hashed payload). `main()` asserts an in-process double-run is byte-identical, and a separate re-invocation reproduces the digest byte-for-byte. Whole-dict `results_sha256 = 4ce987eb3da551811389d54d5d70f72ec27cadcd8600efc73320ad9860938ece`, carrying no self-reference.

**5. Does the grounding actually support the claim, or is it overstated?** Honest split. The pinned Necklace (combinatorics) revision carries the closed-form count (1/n)·Σφ(d)k^(n/d) verbatim (with φ named Euler's totient), the cyclic-group orbit framing, the Pólya-enumeration-theorem attribution, and the companion Möbius/aperiodic formula — quoted. The specific value N_3(6) = 130, the parameters and k^n = 729, the panel, the naive falsifier 121.5, and every z-value and the digest are flagged derived-not-quoted; the word "Burnside" is not on this revision (the page uses Pólya's enumeration theorem, of which Burnside's lemma for C_n is the special case). Neither oversold (the sim/seed/digest are firsthand) nor undersold (the identity genuinely appears and is cited as textbook).

**6. Does it scale / is it robust?** The claim is a closed-form identity valid for all (n, k), so it is structurally parameter-independent. G1 confirms it on a 5-instance panel spanning distinct (n, k) and distinct counts (130, 6, 8, 14, 24). G3 adds a robustness leg: the orbit count is invariant under a nontrivial colour relabel (cyclic +1 mod k), reproduced for (6, 3) and (5, 2) — a check that the canonical form respects only rotation, not colour identity.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the plausible-but-wrong "divide by group order" rule and rejects it at ~109σ on the same sample G2 shows agreeing with the truth. Any mis-stated φ, wrong divisor set, or a canonical form that mixed colour with rotation would break the exact G1 equality or move the G2 z past the accept band.

**8. Any residual risk before ruling?** The brute-force cross-check is exhaustive only because the panel instances are small (max k^n = 729); the closed form is what generalises, and G1 anchors it to ground truth on every panel row. The identity itself is textbook and cited as such; the firsthand contribution is the exact (6, 3) instantiation, the exhaustive orbit-enumeration cross-check, the four-gate machine-checked reproduction, and the falsification of the divide-by-group-order error. The paired sim-lab VERDICT 249 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
