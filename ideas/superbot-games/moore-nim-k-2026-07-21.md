# Moore's Nim (Nim_k) under normal play (last to move wins): a move selects between 1 and k heaps inclusive and removes a positive number of tokens from EACH selected heap; writing every heap in binary and letting c_j = Σ_i bit_j(a_i) be the column-sum of bit j across all heaps, the position is a P-position (player to move loses) IF AND ONLY IF c_j ≡ 0 (mod k+1) for every bit-position j — for k=1 the modulus is 2 and the criterion collapses to ordinary Nim (nim-sum XOR == 0, Bouton's theorem).

> **State:** sim-ready
> **Status:** sim-ready
> **📊 Model:** Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Nim&oldid=1362772636@750a8fd6ead1d0b082596aab4f84d9d4bd49da78 · fetched 2026-07-21

**Lane:** superbot-games · combinatorial game / Sprague–Grundy · Moore's Nim (Nim_k)
**Proposal:** 259 → Verdict 272 (+13 offset) — named by the `## PROPOSAL 259` block in `control/outbox.md`
**Verifier:** [`verify_259_moore_nim_k.py`](verify_259_moore_nim_k.py) · stdlib only (argparse, functools, hashlib, itertools, json, math, random, sys, fractions) · SEED=20260717
**File sha256:** `e8e117d135dc4875744d060a764f920840957a6bf15ca3efe0b86901f9e03969`
**Digest:** `results_sha256 = da147d54d970d71754baa2994189c9e5f73cfbbf1ad36c7b2366f9ddf870402d`

## What this proposal does

Adds a superbot-games PROPOSAL establishing the exact P-position closed form for **Moore's Nim (Nim_k)** — the multi-heap generalisation of Nim analysed by E. H. Moore in 1910. A position is a multiset of heap sizes `(a_1,…,a_m)`. A **move** selects between **1 and k** heaps inclusive and removes a **positive** number of tokens from **each** selected heap. Normal play: the last player to move wins (a player who cannot move loses).

The claim is Moore's theorem:

1. **Column-sum criterion.** Write every heap in binary. For each bit-position `j`, let `c_j = Σ_i bit_j(a_i)` be the **column-sum** of bit `j` across all heaps. The position is a **P-position** (the player to move loses) **if and only if** `c_j ≡ 0 (mod k+1)` for **every** bit-position `j`.
2. **k=1 collapse.** For `k=1` the modulus is `k+1 = 2`, so the criterion becomes "every binary column-sum is even" — equivalently the **nim-sum (XOR)** of the heaps is `0`. This is exactly ordinary Nim (Bouton's theorem): first player wins iff the nim-sum is nonzero.

The proposal ships a stdlib-only firsthand verifier that proves the theorem by pitting an **independent from-scratch game oracle** — a memoized P/N outcome recursion over sorted-tuple canonical states that knows nothing of the theorem — against the closed-form predicate, through **four gates each in its own direction** (an exact exhaustive equivalence sweep, a Monte-Carlo P-density agreement against an independently-derived exact fraction, an invariance/robustness leg, and a falsifiability leg that rejects the ordinary-Nim rule mis-applied to `k=2`), all wrapped in a reproducible `SEED=20260717` digest.

**Distinctness.** This is **Moore's Nim / index-k nim / Nim_k**, categorically distinct from every shipped game head: Mock Turtles / coin-turning odious closed form (**P255**), Green Hackenbush = Nim / colon principle (**P247**), Wythoff (**P239**), Fibonacci-nim / Zeckendorf (**P243**), the subtraction game (**P219**, `g(n)=n mod 4`). What is new here is the multi-heap "touch up to k heaps per move" rule and the generalisation of the P-criterion from mod 2 (XOR) to **mod (k+1)** on binary column-sums. `moore` / `index-k` / `nim_k` is **grep-0** across both repos.

## Method

Ground-truth engine first, closed-form predicate second, then the two are forced to agree.

**The game oracle (assumes no theorem).** A position is canonicalised to the **sorted tuple of its strictly-positive heap sizes**. `successors(state, k)` enumerates every legal Nim_k move exactly: choose `1..k` of the (nonzero) heaps and replace each chosen heap value `v` by any new value in `[0, v)` (remove a positive number from each). `outcome_oracle(heaps, k)` is a memoized recursion (`functools.lru_cache` keyed on `(state, k)`): the terminal (all-zero / empty) position is a **P-position** (the mover loses); a position is **N** iff some legal move leads to a P-position, else **P**. This engine plays the game; it never references the column-sum rule.

**The closed form.** `moore_predicate(heaps, k)` independently checks that for every bit-position the column-sum of that bit across all heaps is `≡ 0 (mod k+1)`. `xor_all` supplies the `k=1` classical invariant for the collapse gate.

**Determinism.** `SEED=20260717` (hardcoded). Each sampling gate draws from a fresh `random.Random(SEED[+offset])` so gate order cannot perturb the payload; every heap multiset is canonicalised to a sorted tuple; every float enters the payload via a fixed 6-dp format string and every count as an int; fractions are stored as `"num/den"`. The digest is the sha256 of the canonical-JSON results dict (full 64 hex, never truncated). Determinism is verified three ways — in-process double-run, a `--selfcheck` path, and a separate process re-invocation — all byte-identical.

## Exact reference

The from-scratch oracle and the column-sum predicate agree on every anchor:

| heaps | k | column-sums (bit0,bit1,bit2,…) | mod (k+1) all zero? | moore_predicate | true outcome |
|---|---|---|---|---|---|
| (3,5,7) | 1 | bit0=3, bit1=1, bit2=2 | no (mod 2) | P=False | N |
| (1,1,1) | 2 | bit0=3 | yes (mod 3) | P=True | P |
| (2,2,2) | 2 | bit1=3 | yes (mod 3) | P=True | P |
| (1,1) | 2 | bit0=2 | no (mod 3) | P=False | N |
| (7,7,7) | 2 | bit0=3, bit1=3, bit2=3 | yes (mod 3) | P=True | P |
| (1,2,3) | 3 | bit0=2, bit1=2 | no (mod 4) | P=False | N |

For `k=1`, `(3,5,7)` has nim-sum `3⊕5⊕7 = 1 ≠ 0`, an N-position — the classical Nim invariant, recovered as the `k=1` special case of the mod-(k+1) rule. For `k=2`, `(1,1,1)` is a P-position because a single move touches at most 2 of the 3 unit heaps, always leaving a nonzero column-sum mod 3.

## Four gates (each in its own direction)

- **G1 — EXACT (exhaustive, integer/XOR, zero tolerance).** For `k ∈ {1,2,3}`, enumerate **ALL** positions with `m` heaps (`m = 1..4`) and each heap in `[0,H)` — `k=1: H=8`, `k=2: H=6`, `k=3: H=5` — and assert `moore_predicate(heaps,k) == (outcome_oracle(heaps,k) is P)` for **every** position. `positions_checked = 7014` (k1=4680, k2=1554, k3=780), `mismatches = 0`. Direction: theorem ⇔ true game outcome. **PASS.**
- **G2 — Monte-Carlo agreement (`|z| < 3`).** With `(k,m,b) = (2,5,6)`, heaps uniform in `[0,2^6)`. The exact analytic P-fraction is derived independently: modulus `q = k+1 = 3`; each bit-column is a sum of `m=5` iid Bernoulli(1/2) bits, so `P(one column ≡ 0 mod 3) = (C(5,0)+C(5,3))/2^5 = 11/32`; the `b=6` columns are independent, so `f = (11/32)^6 = 1771561/1073741824 ≈ 0.001650`. `N = 200000` iid positions give `p̂ = 0.001765`, `z = 1.268354`, `|z| < 3`. Direction: sampled frequency vs an independently-derived exact probability (genuine sampling variance). **PASS.**
- **G3 — invariance / robustness (0 violations).** (a) **k=1 collapse:** over an exhaustive range (`m ≤ 4`, `H ≤ 8`) assert `moore_predicate(heaps,1) == (xor_all(heaps) == 0)` for every position — `collapse_violations = 0`, tying the theorem to the classical Nim invariant. (b) **Permutation + zero-pad invariance:** for 400 random positions (random `k ∈ {1,2,3}`, `m ≤ 4`), assert both `moore_predicate` and `outcome_oracle` are unchanged under a random permutation of the heaps and under appending zero heaps — `perm_violations = 0`, `pad_violations = 0`. Direction: structural symmetries. **PASS.**
- **G4 — falsifiability (reject at `|z| > 3`).** The naive **foil** applies the ordinary-Nim rule (predict P ⇔ nim-sum XOR `== 0`, i.e. columns mod 2) to Moore's Nim with **k=2** (whose true modulus is 3). Over `N = 5000` random `k=2` positions with SMALL heaps (`m=4`, values `0..3`, so the true oracle is affordable), the foil misclassifies at error rate `ê = 0.345800` against the TRUE outcome oracle, `z_foil = 51.409363`. On the SAME sample the true theorem predicate makes `theorem_errors = 0`. Direction: refute a plausible-but-wrong rule. **PASS.**

All four gates PASS; `all_gates_pass = true`, `first_failing_gate = null`, `decision = PASS`, `results_sha256 = da147d54d970d71754baa2994189c9e5f73cfbbf1ad36c7b2366f9ddf870402d`. Deterministic three ways (in-process double-run, `--selfcheck`, separate re-invocation), all byte-identical. SEED = 20260717 (hardcoded). Verifier file sha256 `e8e117d135dc4875744d060a764f920840957a6bf15ca3efe0b86901f9e03969`.

## Grounding

One pinned Wikipedia revision (MediaWiki API `revisions.sha1` == self-computed `hashlib.sha1` of the raw wikitext — exact match):

- **"Nim"**, oldid `1362772636`:
  `https://en.wikipedia.org/w/index.php?title=Nim&oldid=1362772636@750a8fd6ead1d0b082596aab4f84d9d4bd49da78` (30663 bytes), fetched 2026-07-21. API `sha1 = 750a8fd6ead1d0b082596aab4f84d9d4bd49da78`; self-computed `hashlib.sha1(rawwikitext) = 750a8fd6ead1d0b082596aab4f84d9d4bd49da78` — **match**.

The Nim article carries a dedicated **"Index-k nim"** section (§ Index-k nim) stating this exact theorem, so a single primary pin suffices — the coverage is not thin.

**Quoted** literally on the pinned revision (grep count > 0 in the raw wikitext):
- The **name and attribution**: *"A generalization of multi-heap nim was called 'nim_k' or 'index-k' nim by E. H. Moore … who analyzed it in 1910."*
- The **move rule**: *"In index-k nim, instead of removing objects from only one heap, players can remove objects from at least one but up to k different heaps."*
- The **column-sum criterion and modulus**: *"In ordinary nim one forms the XOR-sum (or sum modulo 2) of each binary digit, and the winning strategy is to make each XOR sum zero. In the generalization to index-k nim, one forms the sum of each binary digit modulo k + 1."*
- The **P/N two-directional characterisation**: *"the winning strategy is to move such that this sum is zero for every digit. Indeed, the value thus computed is zero for the final position, and given a configuration of heaps for which this value is zero, any change of at most k heaps will make the value non-zero. Conversely, given a configuration with non-zero value, one can always take from at most k heaps, carefully chosen, so that the value will become zero."*
- The **k=1 / ordinary-Nim collapse**: the nim-sum "sum modulo 2" of each binary digit and Bouton's theorem — *"the player making the first move has a winning strategy if and only if the nim-sum of the sizes of the heaps is not zero"* (§ Proof of the winning strategy).

**Derived firsthand** (not spelled out on the pinned page): the independent memoized **P/N outcome oracle** (recursion over sorted-tuple states that assumes no theorem); the **exhaustive equivalence proof** (moore_predicate ⇔ true outcome over 7014 positions with 0 mismatches); the exact Monte-Carlo P-fraction `f = (11/32)^6` and its derivation from independent binary columns of iid Bernoulli(1/2) bits; all `z`-values; the falsifiability foil (ordinary Nim applied to k=2) and its rejection statistic; SEED; and the results digest.

**Honest posture — disclosed seams.** (1) **Variable relabel:** the article uses `k` for the number of heaps a move may touch (matching our `k`), and separately uses `r` for an *optional per-heap removal cap* (*"the number of elements that may be removed from each heap may be either arbitrary or limited to at most r"*). Our claim takes the **arbitrary-removal** variant (remove any positive number from each chosen heap, no cap), which is exactly the article's stated "either arbitrary" option — so our column-sum-mod-(k+1) rule applies directly with **no r term**; the article's parenthetical "heap sizes modulo r + 1" pre-reduction is the *bounded* variant we do not use. Disclosed, not oversold. (2) **Phrasing:** the article states the strategy as "make the sum zero for every digit"; our "P-position IFF every column-sum ≡ 0 (mod k+1)" is the equivalent P-position statement (a position all of whose digit-sums are zero mod k+1 is precisely the one from which no single move preserves that property — the article's two-directional characterisation). (3) **"column-sum"** is our term for the article's "sum of each binary digit"; **"P-position / player to move loses"** is the normal-play "final position … cannot move" phrasing. Nothing oversold: the game, its name/attribution, the move rule, the mod-(k+1) column criterion, and the k=1 collapse are all QUOTED; the outcome oracle, the exhaustive proof, every statistic, and the digest are the firsthand contribution.

## Probe report (v0, self-adversarial)

**1. What is this really?** The exact statement that Moore's Nim (Nim_k) — touch 1..k heaps per move, remove a positive amount from each, normal play — has P-positions characterised by "every binary column-sum ≡ 0 (mod k+1)", generalising the XOR==0 nim-sum criterion of ordinary Nim (the k=1 case). It is proved firsthand by an independent memoized P/N oracle that plays the game, not by asserting the theorem: the oracle matches the predicate on all 7014 exhaustively-enumerated positions across k∈{1,2,3} (G1).

**2. Is it non-trivial / not a duplicate?** Yes. `moore` / `index-k` / `nim_k` is grep-0 across both repos. It is the multi-heap Moore generalisation, orthogonal to Mock Turtles (P255), Green Hackenbush (P247), Wythoff (P239), Fibonacci-nim (P243), and the subtraction game (P219). Ordinary Nim is recovered only as the k=1 special case, verified as the G3 collapse.

**3. How could the oracle be wrong, and what guards it?** A memoization or move-generation bug could produce wrong P/N values that happen to agree with a buggy predicate. Guarded by (i) the **exhaustive** G1 sweep over three distinct moduli (k+1 ∈ {2,3,4}) with 0 mismatches, where the two computations are genuinely independent (game recursion vs binary column arithmetic); (ii) the G3 permutation/zero-pad invariance leg (both functions must agree under relabeling); and (iii) the G4 falsifiability leg where the *wrong* modulus (mod 2 on a k=2 game) is rejected at z=51.4 while the true predicate scores 0 errors — a shared bug would have to corrupt all of these identically across three moduli.

**4. Is the digest deterministic?** Yes. `build_results()` is a pure function of SEED and fixed params; each sampling gate reseeds a fresh `random.Random`; every float is a fixed 6-dp format string, every count an int, every fraction a "num/den" string; no wall-clock / PID / unordered-set iteration enters the payload (states are sorted tuples). In-process double-run, `--selfcheck`, and a separate re-invocation are byte-identical. `results_sha256 = da147d54d970d71754baa2994189c9e5f73cfbbf1ad36c7b2366f9ddf870402d`.

**5. What does the foil rule out?** G4 pre-registers the most plausible wrong rule — "use ordinary Nim (XOR/mod 2)" on a k=2 game — and rejects it at `z_foil = 51.41` (error rate 0.35 vs the true oracle) while the true mod-3 predicate makes 0 errors on the same sample. This isolates the mod-(k+1) generalisation as the load-bearing correction: mod 2 is not merely imprecise, it is substantially wrong once k>1.

**6. What are the limits?** The P/N oracle is exponential in the heaps/sizes, so the exhaustive sweep is capped at m≤4 and small H, and the G4 oracle leg at m=4, heaps 0..3. The exact identity (G1) carries the claim across three moduli; G2 confirms the P-density on wider heaps (b=6) where only the predicate is needed, and the closed form scales freely beyond the oracle's horizon.

**7. Who consumes it?** sim-lab, as the paired **VERDICT 272** (+13 offset) reproduction — a separate coordinator-driven slice that re-runs the byte-identical verifier and checks the digest and the four gates.

**8. How will we know it worked?** Byte-identical digest reproduction: sim-lab VERDICT 272 re-runs `SEED=20260717` and obtains `results_sha256 = da147d54d970d71754baa2994189c9e5f73cfbbf1ad36c7b2366f9ddf870402d` (in-process double-run + `--selfcheck` + separate re-invocation byte-identical), with all four gates PASS each in its own direction and `all_gates_pass = true`, `first_failing_gate = null`, `decision = PASS`.

**Recommendation: sim-ready**
