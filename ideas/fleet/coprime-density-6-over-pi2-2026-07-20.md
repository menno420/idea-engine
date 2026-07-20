# Coprime density: two integers drawn uniformly from {1,…,N} are coprime with probability Q(N)=(1/N²)·Σμ(k)⌊N/k⌋² — converging to 6/π²=1/ζ(2)≈60.8%, and it is NOT the naive "avoid a shared factor of 2 ⇒ 3/4"

> **State:** sim-ready
> **Class:** fleet (cross-cutting slot — pure number theory / probability)
> **Target:** sim-lab (VERDICT 245, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/wiki/Coprime_integers?oldid=1363371102@254a5e6988f14ce74d40502b159f687ea8c4947c · fetched 2026-07-20
> **Reference (external, reachable):** [Coprime integers — Wikipedia](https://en.wikipedia.org/w/index.php?title=Coprime_integers&oldid=1363371102) — supports the head firsthand: the pinned revision's "Probability of coprimality" section states `\prod_{\text{prime }p}(1-1/p^2) = 1/\zeta(2) = 6/\pi^2 \approx 0.607927102 \approx 61\%` and that P_N (the probability two numbers in {1,…,N} are coprime) approaches 6/π² as N→∞ (Cesàro 1881; Hardy–Wright Theorem 332). Byte-pinned to the raw-wikitext sha1 of the cited revision.
> **Verifier (firsthand):** ideas/fleet/verify_232_coprime_density.py · results-dict sha256 `754580401315c5e987d30467f1d99ee125605f6203de69d9340f910308840fec`

## The phenomenon (one line)
Pick two whole numbers at random from {1,…,N}; the chance they share no common factor bigger than 1 settles at about 60.8% — the Basel value 6/π²=1/ζ(2) — and it is provably NOT the "just avoid both being even ⇒ 3/4" guess.

## Domain
Analytic / elementary number theory meets probability — the coprime-density theorem, Möbius inversion, the Euler product ∏(1−p⁻²)=1/ζ(2), and the Basel problem ζ(2)=π²/6. The finite-N object is the count of coprime lattice points in [1,N]².

## The folk belief
Two wrong intuitions: (a) "coprimality is mostly about parity — two numbers fail to be coprime mainly when both are even, so P(coprime) ≈ 1−1/4 = 3/4"; (b) more vaguely, that the answer is some clean rational with no π in it. Both are wrong: every prime p removes a factor (1−1/p²), and the full product over ALL primes is 1/ζ(2)=6/π²≈0.6079 — a transcendental-looking constant, decisively below 3/4.

## The thesis (reasoned to its fuller form — Q-0254 duty)
Let A(N)=#{(a,b)∈[1,N]²: gcd(a,b)=1} and Q(N)=A(N)/N².

1. **Exact finite-N density by Möbius inversion.** Counting pairs whose gcd is divisible by k gives ⌊N/k⌋², and Möbius inversion peels off exactly the coprime pairs: A(N)=Σ_{k=1}^{N} μ(k)⌊N/k⌋², so Q(N)=(1/N²)Σ_{k=1}^{N} μ(k)⌊N/k⌋². This is exact for every finite N (no limit yet).
2. **Two independent exact routes agree.** A(N) can be computed by brute-force gcd enumeration OR by the Möbius sum; getting the identical integer for a spread of N (small and large) is a genuine cross-check of the inversion, not a restatement.
3. **The limit is 6/π², not 3/4.** As N→∞, Q(N)→∏_{p prime}(1−1/p²)=1/ζ(2)=6/π²≈0.6079271018540267 (Euler product; Basel ζ(2)=π²/6). The parity-only guess 3/4 keeps only the p=2 factor (1−1/4); the true density multiplies in (1−1/9)(1−1/25)… over every prime, pulling the answer down to ≈0.6079.
4. **A clean partition invariant certifies the count.** Every pair in [1,N]² has a unique gcd d, and the pairs of gcd exactly d correspond to coprime pairs in [1,⌊N/d⌋]²; hence Σ_{d=1}^{N} A(⌊N/d⌋)=N² exactly — an independent integer identity the verifier checks with real teeth.
5. **The naive 3/4 is a distinct, falsifiable number.** A large Monte-Carlo sample at N=10000 lands on p̂≈0.6088 (agreeing with Q_N≈0.60795 at |z|≈0.77) and rejects 3/4 at z_naive≈−146.

Fuller form, one sentence: *the coprime probability of two uniform draws from {1,…,N} is the exact Möbius density Q(N)=(1/N²)Σμ(k)⌊N/k⌋², converging to 6/π²=1/ζ(2), and it is provably not the parity-only 3/4.*

## The formal model / Pinned world (committed constants)
- Object: two independent uniform draws a,b from {1,…,N} via a seeded RNG (`random.Random(SEED)`); coprime iff `math.gcd(a,b)==1`.
- Exact arithmetic via `fractions.Fraction`; μ via a simple sieve.
- SEED = 20260717; a single `random.Random(SEED)` is consumed once, in the Monte-Carlo pass; the SAME sample feeds both G2 (exact-density agreement) and G4 (naive-3/4 rejection).
- Committed constants: G1 N∈{1,2,3,4,5,6,10,50,100,200}; G2/G4 N=10000, M=200000, Z_ACCEPT=3.0, Z_REJECT=8.0, NAIVE_P=0.75; G3 partition identity over N∈{1,2,3,10,20,50,100,200}.

## Pre-registered gates
- **G1 — EXACT identity, two independent routes.** For every N, brute A(N)=#{gcd=1} equals Möbius B(N)=Σμ(k)(N//k)² as ints AND Fraction(A,N²)==Fraction(B,N²). *Direction:* every N equal; a single mismatch fails. Q(6)=23/36.
- **G2 — Monte-Carlo agreement (|z|<3).** N=10000; Q_N=Fraction(B(N),N²); p̂=coprime/M; z=(p̂−float(Q_N))/√(float(Q_N)(1−float(Q_N))/M). *Direction:* small |z| = agreement.
- **G3 — EXACT partition invariant.** Σ_{d=1}^{N} A(⌊N/d⌋)==N² (unique-gcd decomposition) as exact integer equality for all tested N, plus 0<Q(N)<1 for N≥2. *Direction:* every identity exact; any mismatch fails.
- **G4 — falsifiability (naive 3/4 REJECTED).** On the SAME MC sample, z_naive=(p̂−0.75)/√(0.75·0.25/M). *Direction:* PASS iff the exact density is accepted (G2) AND the 3/4 fallacy is rejected at |z_naive|≥8.

## Determinism & digest
`SEED = 20260717`; one `random.Random(SEED)` consumed once (the MC pass is the sole RNG consumer). `build_results()` is a pure function of the seed and fixed constants; `main()` runs it twice in-process and asserts byte-identical canonical JSON, and a separate re-invocation is byte-identical. Whole-dict sha256 over the compact canonical JSON (no self-field), printed as the full 64 hex on stdout:

`results_sha256 = 754580401315c5e987d30467f1d99ee125605f6203de69d9340f910308840fec`

Observed gate results (this pinned world): **G1 PASS** (exact, all N; Q(6)=23/36). **G2** z_agreement=+0.774312 (|z|<3), p̂=0.608795, Q_N=60794971/100000000≈0.60794971 vs asymptote 6/π²≈0.6079271018540267. **G3 PASS** (partition identity exact for all N∈{1,2,3,10,20,50,100,200}; 0<Q<1 for N≥2, Q(1)=1 boundary). **G4** z_naive=−145.835897 (|z|≥8), naive 3/4 REJECTED. `all_pass=true`, `first_failing_gate=null`.

## Grounding & scope
Grounding pins English Wikipedia "Coprime integers" at oldid 1363371102, raw-wikitext sha1 `254a5e6988f14ce74d40502b159f687ea8c4947c` (17,251 bytes; the API revision sha1 and a self-computed sha1 of the `action=raw` wikitext agree exactly). Quoted vs derived, scrupulously separated:

**On that pinned revision (QUOTED — literally present, grepped):**
- The product/limit: `\prod_{\text{prime } p} \left(1-\frac{1}{p^2}\right) = … = \frac{1}{\zeta(2)} = \frac{6}{\pi^2} \approx 0.607927102 \approx 61\%.`
- The Basel evaluation of ζ(2) as π²/6 (named as the Basel problem, Euler 1735).
- P_N (the probability two randomly chosen numbers in {1,…,N} are coprime) "approaches 6/π²" as N→∞, with the note that P_N "will never equal 6/π² exactly" (Cesàro 1881; Hardy–Wright Theorem 332).

**Derived here, NOT on the pinned revision (grep count 0):**
- The **exact finite-N Möbius identity** Q(N)=(1/N²)Σμ(k)⌊N/k⌋² — the page gives no Möbius/floor finite-N formula.
- The **partition invariant** Σ_{d=1}^{N} A(⌊N/d⌋)=N².
- The **naive 3/4 "avoid a shared factor of 2" falsifier** and its rejection.
- Every **Monte-Carlo number** (z_agreement=+0.774312, z_naive=−145.835897, p̂) — firsthand from the verifier.

Honest posture: the *core asymptotic claim* (P(coprime)→6/π²=1/ζ(2)) is QUOTED essentially verbatim from the pinned revision; this proposal's firsthand contribution is the exact finite-N Möbius density, the two-route reproduction, the partition invariant, the seeded Monte-Carlo confirmation, and the pre-registered rejection of the parity-only 3/4 model. Nothing is oversold as novel.

## Reproduce

```
python3 ideas/fleet/verify_232_coprime_density.py
# exit 0; prints the results dict, in_process_double_run: IDENTICAL,
# results_sha256: 754580401315c5e987d30467f1d99ee125605f6203de69d9340f910308840fec
# decision: sim-ready
```

## Probe report (v0, self-adversarial)

**1. Is the core identity exactly true (not merely approximate)?** Yes. G1 computes A(N) two independent ways (brute gcd count vs Möbius sieve sum) as ints and `fractions.Fraction` for ten values of N and asserts exact equality — no floats, zero slack (e.g. Q(6)=23/36 both ways).

**2. Could the 6/π² be an artefact of the sampler?** No. The finite-N value is a counting identity proved exactly in G1/G3; the Monte-Carlo gate G2 only confirms the N=10000 ratio agrees (|z|=0.77), and the asymptote 6/π²=1/ζ(2) is the quoted Euler-product limit.

**3. What is the most plausible wrong belief this could be confused with?** The parity-only guess 3/4 (keep only the p=2 factor). G4 pre-registers it as the falsifier and rejects it at z_naive≈−146 on the same sample — 0.75 vs 0.6079 is decisively distinguished.

**4. Is the verifier deterministic and self-checking?** Yes. Single seeded RNG consumed once in a fixed order; in-process double-run + separate re-invocation both byte-identical; whole-dict sha256 with no self-reference.

**5. Does the grounding actually support the claim, or is it overstated?** The 6/π²=1/ζ(2) value and the P_N→6/π² limit are quoted verbatim from the pinned revision; the finite-N Möbius identity, the partition invariant, and the 3/4 falsifier are explicitly flagged derived — the citation is neither over- nor under-claimed.

**6. Does it scale / is it robust?** G1 spans N up to 200 exactly; G3 holds the partition identity exactly through N=200; the asymptote is size-independent by construction, and G2 confirms convergence already at N=10000.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the plausible-but-wrong parity-only 3/4 alternative and rejects it at z≈−146; had the sampler produced a 3/4-like law, G4 would fire.

**8. Any residual risk before ruling?** The exact gates cover N up to 200; the asymptotic 6/π² rests on the quoted Euler-product limit. Monte-Carlo is confirmatory only, at N=10000. No blocker.

**Recommendation: sim-ready**
