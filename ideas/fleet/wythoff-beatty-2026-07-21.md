# Wythoff's game: the cold (P) positions are exactly the golden-ratio Beatty pairs

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** fleet · combinatorial game theory / Sprague-Grundy cold positions (Wythoff)
**Proposal:** 239 → Verdict 252 (+13 offset)
**Verifier:** [`verify_239_wythoff_beatty.py`](verify_239_wythoff_beatty.py) · stdlib only · SEED=20260717
**Digest:** `results_sha256 = 9fe0e90d2c4544a9c38c051be34b9369fdf84f12b53e4ed16818feb5c87eabcc`

## Claim

Wythoff's game: two piles; a move removes k ≥ 1 tokens from one pile, or the *same* k ≥ 1 from both piles; the player unable to move (both piles empty) loses. The P-positions (cold / previous-player-wins positions — the Sprague-Grundy value-0 positions) are exactly the golden-ratio Beatty pairs

    P_n = (a_n, b_n),   a_n = ⌊n·φ⌋,   b_n = ⌊n·φ²⌋,   n = 0, 1, 2, …

with φ = (1 + √5)/2 the golden ratio, together with the exact integer identity

    b_n = a_n + n.

The lower sequence {a_n} (OEIS A000201) and the upper sequence {b_n} (A001950) **partition** the positive integers: because 1/φ + 1/φ² = 1, Beatty's theorem makes them complementary, so every positive integer appears in exactly one of them. The lower sequence therefore has natural density 1/φ ≈ 0.618034 — **not** 1/2.

## Exact reference

Exact floor with **no floats** (integer arithmetic only):

    a_n = (n + isqrt(5·n²)) // 2,   b_n = a_n + n.

This is exact because n√5 is irrational for n ≥ 1, so ⌊(n + n√5)/2⌋ = (n + ⌊n√5⌋) // 2 = (n + isqrt(5n²)) // 2 regardless of the parity of n + ⌊n√5⌋. First nine P-positions (sanity anchors):

| n | a_n = ⌊nφ⌋ | b_n = ⌊nφ²⌋ = a_n + n |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 1 | 2 |
| 2 | 3 | 5 |
| 3 | 4 | 7 |
| 4 | 6 | 10 |
| 5 | 8 | 13 |
| 6 | 9 | 15 |
| 7 | 11 | 18 |
| 8 | 12 | 20 |

## Four gates (each in its own direction)

- **G1 — exact identity (integer/exact arithmetic, `fractions.Fraction` where a ratio appears).** Over the board panel N ∈ {30, 60, 90}, a Sprague-Grundy mex-DP (from (x, y): remove k ≥ 1 from one pile → (x−k, y) or (x, y−k); remove k ≥ 1 from both → (x−k, y−k); G = mex of reachable Grundy values) yields the Grundy-0 positions with x ≤ y, and this set equals **exactly** the isqrt-Beatty pairs {(a_n, b_n) : b_n ≤ N}. The closed-form P-position count equals the mex-DP count (checked as `Fraction`). Additionally b_n − a_n == n for all n up to 200 000, and the exact Beatty **partition** holds on 1..M for M ∈ {1 000, 100 000, 1 000 000}: {a_n} ∪ {b_n} covers every integer 1..M with zero overlap, and |{a_n ≤ M}| + |{b_n ≤ M}| == M as an exact `Fraction`. `error_count = 0`.
- **G2 — Monte-Carlo agreement.** Building the lower set {a_n ≤ M} for M = 1 000 000 via the exact isqrt floor, K = 200 000 uniform random integers in [1, M] are classified by membership; the estimate p̂ = 0.617290 agrees with the theoretical density 1/φ = 0.618034 at z = **−0.684799**, |z| < 3 [Z_ACCEPT = 3.0].
- **G3 — invariance / robustness.** Two **independent** P-position generators agree exactly over the panel: (i) the isqrt-Beatty closed form, and (ii) the classic greedy/mex construction a_n = mex{a_i, b_i : i < n}, b_n = a_n + n. PLUS the Grundy table is pile-swap symmetric: G(x, y) == G(y, x) for every board cell. `mismatch_count = 0`.
- **G4 — falsifiability.** On the SAME MC sample: (F2) the naive "even 50/50 split" belief — lower-Wythoff density = 1/2 — is rejected at z_reject = **104.907365**, |z| ≥ 6 [Z_REJECT = 6.0]. (F1) the naive universal rule "every P-position is (k, 2k), i.e. b_n = 2·a_n" is refuted exactly: it holds only at the two coincidental smallest fits n = 0 → (0, 0) and n = 1 → (1, 2), and breaks at the very next position n = 2 → (3, 5) and at every n ≥ 2 thereafter (199 999 counterexamples over the panel; first counterexample (3, 5)).

All four gates PASS; `all_gates_pass = true`, `first_failing_gate = null`, `decision = PASS`. Deterministic: in-process double-run and separate re-invocation are byte-identical; `results_sha256 = 9fe0e90d2c4544a9c38c051be34b9369fdf84f12b53e4ed16818feb5c87eabcc`.

## Grounding

Wythoff's game (Wikipedia), pinned revision:
`https://en.wikipedia.org/w/index.php?title=Wythoff%27s_game&oldid=1338739976&action=raw@e6a8c57f1d809b945097cf91b2e265d0fcc1783c` (rev 2026-02-16T23:20:58Z, 5313 bytes; API `revisions.sha1` == self-computed `sha1sum` of the raw wikitext — exact match).

- **Quoted** literally on the pinned revision: the golden-ratio closed form `n_k = \lfloor k \phi \rfloor` and `m_k = \lfloor k \phi^2 \rfloor = \lceil n_k \phi \rceil = n_k + k` — so the exact identity b_n = a_n + n appears verbatim as `n_k + k`; "φ is the golden ratio" and the floor function; the Beatty-sequence framing ("The two sequences n_k and m_k are the Beatty sequences associated with the equation" `1/φ + 1/φ² = 1`); the complementary/partition property ("each positive integer appears exactly once in either sequence"); and the first cold positions (0, 0), (1, 2), (3, 5), (4, 7), (6, 10), (8, 13).
- **Derived** firsthand (grep count 0 on the pinned raw wikitext): the explicit φ = (1+√5)/2 form (the page names "golden ratio" and uses the symbol φ but never writes (1+√5)/2); the exact-floor isqrt formula a_n = (n + isqrt(5n²))//2; the Sprague-Grundy *value*/mex-DP construction (the page carries only a "Grundy's game" see-also link — no mex computation); the density 1/φ ≈ 0.618034 and the naive foil F2 "1/2 even split" (the word "density" is absent, count 0); the naive foil F1 "(k, 2k)/b = 2a" (absent, count 0); the cold positions beyond (8, 13) — i.e. (9, 15), (11, 18), (12, 20) (the page lists only through (8, 13)); the word "Fibonacci" (absent, count 0 — so the Fibonacci framing is ours, not the page's); the 199 999-position panel values; and every Monte-Carlo statistic (G2 z = −0.684799, G4 z_reject = 104.907365) and the results_sha256. The Beatty/golden-ratio characterisation is standard textbook material and cited as such; the firsthand contribution is the float-free isqrt instantiation, the Sprague-Grundy mex-DP cross-check against the closed form, the exact 1..M partition verification, the four-gate machine-checked reproduction, and the falsification of the "(k, 2k)" and "even 50/50 split" errors. Nothing oversold as novel.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 computes the cold set two independent exact ways — a Sprague-Grundy mex-DP over the whole board (integer Grundy values, cold = Grundy 0) and the isqrt-Beatty closed form (integer floors) — and asserts exact set identity on N ∈ {30, 60, 90}, plus b_n − a_n == n for 200 001 values of n and the exact 1..M Beatty partition for M up to 1 000 000. `error_count = 0`; no float enters G1.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?** No. Every structural claim is fixed by exact integer arithmetic (G1/G3) before any RNG is touched. The Monte-Carlo gate (G2, K = 200 000) only confirms the *density* 1/φ survives under uniform sampling (z = −0.684799); the membership test is against the exact isqrt set, so the sampler cannot manufacture the value.

**3. What is the most plausible wrong belief this could be confused with?** Two, both pre-registered. F1: "the losing positions are (k, 2k)" — superficially plausible because the two smallest cold positions (0, 0) and (1, 2) genuinely satisfy b = 2a; G4 exhibits that it breaks at the very next position (3, 5) and at all 199 999 larger n. F2: "the lower Beatty sequence is a 50/50 split of the integers" — G4 rejects density = 1/2 at z_reject = 104.9 on the same sample where 1/φ agrees at |z| < 1; the true density is 1/φ ≈ 0.618, not 1/2, precisely because 1/φ + 1/φ² = 1 with unequal terms.

**4. Is the verifier deterministic and self-checking?** Yes. The single sampling gate consumes one seeded `random.Random(20260717)` in fixed order; `build_results()` is a pure function of SEED and the module constants (no wall-clock / PID / unordered-set iteration in the hashed payload). `main()` asserts an in-process double-run is byte-identical, and a separate process re-invocation reproduces the digest byte-for-byte. Whole-dict `results_sha256 = 9fe0e90d2c4544a9c38c051be34b9369fdf84f12b53e4ed16818feb5c87eabcc`, carrying no self-reference.

**5. Does the grounding actually support the claim, or is it overstated?** Honest split. The pinned Wythoff's-game revision carries the golden-ratio closed form ⌊kφ⌋/⌊kφ²⌋, the exact b = a + k identity (as `n_k + k`), the Beatty-sequence framing, the equation 1/φ + 1/φ² = 1, the complementary-partition statement, and the first cold positions through (8, 13) — all quoted. The explicit (1+√5)/2 form, the isqrt exact floor, the mex-DP Grundy construction, the 1/φ density, both naive foils, the cold positions past (8, 13), and every z-value and the digest are flagged derived-not-quoted; "Fibonacci" is not on this revision, so that framing is ours. Neither oversold (the sim/seed/digest are firsthand) nor undersold (the identity genuinely appears and is cited as textbook).

**6. Does it scale / is it robust?** The claim is a closed-form characterisation valid for all n, so it is structurally parameter-independent. G1 confirms the mex-DP ↔ closed-form identity on three board sizes and the partition on three M scales up to 10⁶. G3 adds a robustness leg: an entirely independent greedy/mex generator (a_n = mex of previously used values, b_n = a_n + n) reproduces the same sequence, and the Grundy table is pile-swap symmetric — a check that the DP respects the game's structure.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers two plausible-but-wrong beliefs and refutes both: the "(k, 2k)" universal rule (breaks at (3, 5), 199 999 counterexamples) and the "50/50 split" density (rejected at ~105σ on the same sample where 1/φ agrees). Any mis-stated floor, wrong isqrt, or a mex-DP that mishandled the both-piles move would break the exact G1 set identity or move the G2 z past the accept band.

**8. Any residual risk before ruling?** The mex-DP cross-check is exhaustive only up to N = 90 (the closed form is what generalises, and G1 anchors it to Grundy ground truth on every panel row); the partition and identity legs run to M = 10⁶ and n = 2×10⁵. The characterisation itself is textbook (Wythoff 1907, Beatty's theorem) and cited as such; the firsthand contribution is the float-free isqrt instantiation, the Sprague-Grundy cross-check, the exact 1..M partition, the four-gate machine-checked reproduction, and the falsification of the two naive errors. The paired sim-lab VERDICT 252 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
