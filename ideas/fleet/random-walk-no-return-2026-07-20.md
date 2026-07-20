# Feller's no-return identity: for the simple symmetric ±1 walk on Z from 0, the probability of AVOIDING the origin through step 2n equals the probability of being AT the origin at step 2n — both exactly u_{2n} = C(2n,n)/4ⁿ

> **State:** sim-ready
> **Status:** `sim-ready` — PROPOSAL 228 (round-54 UNRELATED slot) → VERDICT 241 (+13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Random_walk&oldid=1359285496@bdcc6ea9d1ec88b8313eb470f475758301f9dd77 · fetched 2026-07-20
>
> Verifier (merged in sim-lab): `sims/verdict-241-random-walk-no-return/random-walk-no-return.py`. Paired verdict: VERDICT 241 (offset +13; sim-lab PR #325).
> results_sha256 = `75f5b3c166916598983389896cc762c906b1ef346c70f8b5c639b3a60e140f46`

## Head

Take the simple symmetric random walk S₀ = 0, S_k = X₁ + … + X_k with i.i.d. X_i ∈ {+1, −1} each with probability 1/2 (Feller, *An Introduction to Probability Theory and Its Applications*, Vol. I, Ch. III). Two events on the first 2n steps:

- **RETURN:** S_{2n} = 0 — the walk is at the origin at time 2n.
- **NO-RETURN:** S₁ ≠ 0, S₂ ≠ 0, …, S_{2n} ≠ 0 — the walk never revisits 0 across steps 1..2n.

The return probability is the central-binomial term u_{2n} := P(S_{2n} = 0) = C(2n,n)/2^{2n} = C(2n,n)/4ⁿ. **Feller's identity** is that the two probabilities coincide exactly:

- **P(NO-RETURN over 1..2n) = u_{2n} EXACTLY** — avoiding the origin is exactly as likely as landing on it.

Equivalently, over all 2^{2n} equally-likely sign sequences,

- **#{paths with S_{2n} = 0} = #{paths that never revisit 0 in 1..2n} = C(2n,n)** (exact integer identity),

so both events carry the same rational probability C(2n,n)/4ⁿ. The coincidence is genuinely surprising: "come back to where you started" and "get away and stay away forever within the window" are opposite-sounding events, yet they are equinumerous path-for-path.

## Why it matters (fleet framing)

A pair of opposite-sounding events with a provably identical exact probability is the cleanest possible unit test for any first-passage / hitting-time or return-time component in the fleet. A correct return-time sampler over the ±1 walk must reproduce the SAME empirical rate for "at 0 at step 2n" and for "never at 0 through 2n" — to the last bit, at every n — while a subtly wrong one (an off-by-one on the endpoint, a strict-vs-weak inequality slip on the hit test, a walk that isn't mean-zero) breaks the coincidence and the gate fires. The falsifiability tooth is sharper still: the intuitive "avoiding 0 over 2n steps ≈ n independent coin-pair survivals ⇒ (1/2)ⁿ" is wrong by three orders of magnitude at n = 12, so any code that silently assumes independence across steps is caught. The no-return probability decays like 1/√(πn), NOT geometrically — the walk's null-recurrent stickiness is exactly what the naive independence model misses.

## Exact core identities (what the verifier proves)

1. **Exhaustive exact (n ∈ {1,2,3,4,5,6}):** enumerate all 2^{2n} sign sequences; count A := #{S_{2n} = 0} and B := #{never touch 0 in 1..2n}. For every n, A == B == C(2n,n) as integers ({2, 6, 20, 70, 252, 924}), and Fraction(A, 4ⁿ) == Fraction(B, 4ⁿ) == Fraction(C(2n,n), 4ⁿ) == u_{2n} ({1/2, 3/8, 5/16, 35/128, 63/256, 231/1024}). Zero float enters this leg.
2. **Shared exact target under sampling:** the SAME rational u_{2n} is the target for both the return count and the no-return count under Monte-Carlo, so the two empirical rates must both agree with one number.
3. **Left/right symmetry:** the no-return event splits into two mirror-image one-sided excursions — P(strictly positive throughout) == P(strictly negative throughout) — the reflection symmetry of the ±1 walk.

## Gate battery (each in its own direction)

- **G1 — EQUALITY (exhaustive, exact):** all 2^{2n} sign sequences for n ∈ {1,2,3,4,5,6}; A == B == C(2n,n) and Fraction(A,4ⁿ) == Fraction(B,4ⁿ) == u_{2n}. Exact, no sampling — counts land on {2, 6, 20, 70, 252, 924} at n = 1..6.
- **G2 — AGREEMENT |z| < 3:** Monte-Carlo n = 12 (24 steps), N = 200 000; against the SHARED exact u_24 = 676039/4194304 ≈ 0.16118026, the return side gives p̂_return = 0.161965 (z = +0.954447) and the no-return side gives p̂_noreturn = 0.158995 (z = −2.657831). Both |z| < 3.
- **G3 — INVARIANT + AGREEMENT:** across n ∈ {5,8,12,20}, N = 50 000 each, p̂_noreturn agrees with the exact u_{2n} at z_noreturn ∈ {+0.397783, −0.833398, −1.678589, −1.181800}; and the left/right symmetry holds at z_symmetry ∈ {−1.528616, +1.503479, −0.901617, +0.249505}. All |z| < 3.
- **G4 — REJECTION |z| > 6:** the naive independence fallacy "avoiding 0 over 2n steps behaves like n independent pairs ⇒ P(no-return) = (1/2)ⁿ" predicts 1/4096 ≈ 0.000244 at n = 12; on the SAME N = 200 000 sample as G2, the observed p̂_noreturn ≈ 0.158995 rejects it at z_vs_naive = +4544.269481 (|z| ≫ 6). The fallacy is falsified — the true u_24 ≈ 0.161 is ~660× the naive prediction.

## Determinism & digest

`SEED = 20260717`; a single `random.Random(SEED)` is consumed in the fixed order G2 → G3 → G4 (G1 is exhaustive / RNG-free; G4 reuses G2's sample, drawing no fresh randomness). `build_results()` is a pure function of the seed and fixed constants; `main()` runs it twice in-process and asserts byte-identical canonical JSON, and a separate re-invocation is byte-identical. Whole-dict sha256 (no self-field), stdout only:

`results_sha256 = 75f5b3c166916598983389896cc762c906b1ef346c70f8b5c639b3a60e140f46`

## Grounding & scope

Grounding pins English Wikipedia "Random walk" at oldid 1359285496 (2026-06-14T10:43:03Z), raw-wikitext sha1 `bdcc6ea9d1ec88b8313eb470f475758301f9dd77` (57898 bytes, `action=raw`). **On that pinned revision (quoted):** the recurrence of the 1-D simple random walk — *"a simple random walk on ℤ will cross every point an infinite number of times. This result has many names: the level-crossing phenomenon, recurrence or the gambler's ruin"*; the general point-mass formula — *"the probability that S_n = k is equal to 2^{−n} \binom{n}{(n+k)/2}"* (given twice, §Prediction and §Relation to Wiener process); and Feller, *An Introduction to Probability Theory and its Applications*, Vol. 1 in the reference list. **Derived, NOT on the page:** Feller's specific no-return = return identity P(S₁≠0,…,S_{2n}≠0) = u_{2n}, the central-binomial return probability u_{2n} = C(2n,n)/4ⁿ as such (it is the k = 0, n ↦ 2n specialization of the quoted general 2^{−n}\binom{n}{(n+k)/2}, a one-line substitution the revision does not carry out), the exact count identity #{never revisit 0} = C(2n,n), and the 1/√(πn) decay of the no-return probability. The revision names no "first return", no arcsine law, and no u-notation; the "self-avoiding walk / never revisit a site" it does mention is a different object (never revisiting ANY site, on ℤ^d). Every number in the gate battery is computed by the verifier, not quoted — the SEED, the n-grids, the Monte-Carlo procedure, and the results_sha256 are this verifier's firsthand computation. The exact statement for general n rests on the cited Feller theorem; here it is additionally PROVEN firsthand by exhaustive enumeration of the complete path space for n ≤ 6 (G1, zero slack) and cross-checked by Monte-Carlo agreement (G2/G3) and a pre-registered falsifiability gate (G4). The +13 offset (PROPOSAL 228 → VERDICT 241) is the standing round convention.

## Reproduce

```
python3 sims/verdict-241-random-walk-no-return/random-walk-no-return.py
# exit 0; prints the results dict, four PASS lines, all_pass: True,
# results_sha256: 75f5b3c166916598983389896cc762c906b1ef346c70f8b5c639b3a60e140f46
```

## Probe report (v0, self-adversarial)

**1. Is the core identity exactly true (not merely approximate)?** Yes. G1 enumerates every one of the 2^{2n} sign sequences for n = 1..6 and finds A = #{S_{2n}=0} == B = #{never touch 0} == C(2n,n) with zero slack (counts {2,6,20,70,252,924}); the equality of probabilities is a `fractions.Fraction` identity Fraction(A,4ⁿ) == Fraction(B,4ⁿ) == u_{2n}, not a float comparison.

**2. Could the coincidence be an artefact of the sampler rather than the walk?** No. It is an exact integer identity over the complete path space (G1), proven before any RNG is touched; the Monte-Carlo gates (G2/G3) only confirm the shared exact u_{2n} survives under sampling from BOTH the return side and the no-return side, and G3's left/right symmetry ties the split to the walk's reflection geometry.

**3. What is the most plausible wrong belief this could be confused with?** That avoiding 0 for 2n steps is a product of independent per-step survivals, giving (1/2)ⁿ — the geometric-decay intuition. G4 pre-registers exactly this fallacy and rejects it at z ≈ +4544 (true ≈ 0.161 vs naive ≈ 0.000244 at n = 12); the real decay is 1/√(πn), sub-geometric, which is the whole surprise of null recurrence.

**4. Is the verifier deterministic and self-checking?** Yes. A single seeded `random.Random(20260717)` consumed in a fixed order G2 → G3 → G4 (G1 RNG-free, G4 reuses G2's draws); in-process double-run asserts byte-identical canonical JSON and a separate re-invocation reproduces the digest byte-for-byte; the whole-dict sha256 carries no self-reference. Digest 75f5b3c1…e140f46.

**5. Does the grounding actually support the claim, or is it overstated?** Honest split. The 1-D recurrence and the general point-mass formula 2^{−n}\binom{n}{(n+k)/2} are quoted verbatim from the pinned revision; the specific u_{2n} = C(2n,n)/4ⁿ (a k = 0 specialization), Feller's no-return = return identity, and the count identity are explicitly flagged as derived-not-quoted — the revision states neither the identity nor the central-binomial return probability as such. The citation is neither oversold (the sim, seed, and digest are firsthand) nor undersold (the recurrence and the parent formula genuinely appear).

**6. Does it scale / is it robust?** G3 holds the p̂_noreturn == u_{2n} agreement across n ∈ {5,8,12,20} and confirms the left/right symmetry at each size (all |z| < 3); the identity is size-independent by construction (it holds for every n), and the exhaustive G1 pins it exactly for n ≤ 6.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers a plausible-but-wrong alternative (the (1/2)ⁿ independence model) and rejects it at ~4544σ on the same sample that G2 shows agreeing with the truth; had the walk been mis-specified (non-mean-zero steps, or an off-by-one on the hit test) the coincidence would break and G1/G2 would fire.

**8. Any residual risk before ruling?** Exhaustive coverage stops at n = 6 by combinatorial necessity (2^{12} = 4096 paths at n = 6; 2^{14} at n = 7). n ≥ 7 rests on the cited Feller theorem plus the Monte-Carlo invariant gates — the intended division of labour. The sim-lab verifier for this head is already merged (PROPOSAL 228 → VERDICT 241, +13 offset; PR #325). No further blocker.

**Recommendation: sim-ready**
