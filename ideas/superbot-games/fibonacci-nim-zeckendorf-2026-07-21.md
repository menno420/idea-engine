# Fibonacci nim (Whinihan's game): the player to move loses iff n is a Fibonacci number, and the optimal winning move is to remove the smallest Zeckendorf summand

> **State:** sim-ready
> **Status:** `sim-ready` — PROPOSAL 243 (superbot-games GAME slot) → VERDICT 256 (+13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Fibonacci_nim&oldid=1341159330@fcebea2e6f696f94d6d9efda5edc537bf38f18d3 · fetched 2026-07-21T05:04:43Z
>
> Verifier: `ideas/superbot-games/verify_243_fibonacci_nim.py` (stdlib only: json, hashlib, math, random, fractions).
> results_sha256 = `344cdaa21a550c745184aaab00951db1063f522d3fe25544738299fdf8ee7dce`

## Head

**Fibonacci nim** (Whinihan 1963) is a one-pile take-away game. There is a single pile of `n` tokens. On the FIRST move a player may remove any `m` with `1 ≤ m ≤ n−1` (they may not take the whole pile). On every SUBSEQUENT move a player may remove `1 ≤ m ≤ 2·(the number the opponent just removed)`, capped at the tokens remaining. The player who removes the last token wins (normal play).

**Exact theorem.** The player to move LOSES (the position is a *P-position*) **if and only if `n` is a Fibonacci number** — 1, 2, 3, 5, 8, 13, 21, 34, …. Equivalently the first player has a winning strategy iff `n` is NOT a Fibonacci number.

**The optimal strategy ties to Zeckendorf's theorem.** Every positive integer has a unique representation as a sum of non-consecutive Fibonacci numbers (its Zeckendorf representation). From a winning position, remove the **smallest Fibonacci summand** in `n`'s Zeckendorf representation; this is always a legal move (it is `≤ n−1`) and it always leaves the opponent a P-position, because the new quota (twice the removed summand) is strictly smaller than the smallest Fibonacci summand of the remainder.

## The game (one line)

One pile; first move takes `1..n−1`; thereafter take `1..2·(opponent's last take)`, capped at what's left; last token wins. The per-move cap is a *moving* bound — the whole subtlety is that a large take hands the opponent a large quota.

## The exact theorem (Whinihan) — reasoned to its fuller form (Q-0254 duty)

State a position as `(q, cap)`: `q` tokens remain and the mover may take `1..min(cap, q)`. A fresh pile of `n` is the state `(n, n−1)`; `n = 1` is `(1, 0)` — no legal move, so the mover loses. Define `win(q, cap)` = True iff the mover can force the last token. The mover wins iff some legal `m` either takes the last token (`m = q`) or lands the opponent in a losing `(q−m, min(q−m, 2m))`.

The closed form: a fresh pile of `n` is a P-position (mover loses) **iff `n ∈ {Fibonacci}`**. The engine is Zeckendorf. If `n` is itself Fibonacci, its Zeckendorf representation is the single term `n`, whose smallest summand `n` exceeds the opening quota `n−1` — so the first player cannot immediately reach a P-position and, with best opposing play, loses. If `n` is NOT Fibonacci, its Zeckendorf representation has a smallest summand `s ≤ n−1`; removing `s` is legal and leaves `n−s` (itself a P-position for the opponent because the quota `2s` is smaller than the smallest Zeckendorf summand of `n−s`). This is exactly the recursive structure the verifier checks against a from-scratch game oracle.

## The Zeckendorf strategy (constructive)

For a winning `n` (non-Fibonacci): let `s` be the smallest Fibonacci number in the Zeckendorf representation of `n` (found by the greedy largest-first subtraction). Remove `s`. Then the opponent faces `(n−s, min(2s, n−s))`, and `2s` is strictly below the smallest Zeckendorf summand of `n−s`, so the opponent can never reach the next P-position and is themselves in a P-position. The verifier's G1 checks this move is legal AND leaves a P-position for EVERY winning `n ∈ [1, N]` (0 violations).

## Method

A stdlib-only firsthand verifier `verify_243_fibonacci_nim.py` (SEED = `20260717`, exact-DP horizon `N = 800`, second horizon `N2 = 1200`). It implements the GAME — it does NOT assume the theorem. A bottom-up table `win(n, cap)` is built over `n ∈ [1, N]` (so recursion depth is never an issue): a move takes `m ∈ 1..min(cap, n)`; `m = n` wins immediately, else the opponent faces `(n−m, min(n−m, 2m))`; the mover wins iff some `m` leaves the opponent losing; `cap = 0` (the `n = 1` opening) is a loss. The Fibonacci set and Zeckendorf decompositions are built independently by integer recurrence, then compared to the oracle. No floats where integers suffice; every stored float uses a fixed `f"{x:.12g}"` format and `p0` is stored as the exact `"a/b"` fraction, so the serialization is invocation-stable.

Four gates, each with real teeth and its own direction:

- **G1 — EXACT identity (integer arithmetic).** For every `n ∈ [1, N]`, `(loses(n) == True) == (n ∈ Fib)`; `mismatches = 0` over `n_tested = 800`. Plus the constructive Zeckendorf strategy: for every winning `n`, the smallest Zeckendorf summand `s` satisfies `s ≤ n−1` and `win(n−s, min(2s, n−s)) == False`; `zeckendorf_strategy_violations = 0`.
- **G2 — Monte-Carlo agreement (|z| < 3).** Exact P-density `p0 = |Fib ∩ [1,N]| / N = 14/800 = 7/400 = 0.0175` (kept as an exact Fraction and its float). With `random.Random(SEED)`, draw `n_samples = 200000` uniform integers in `[1, N]`, classify each via the DP table; `p_hat = 0.01785`, `z = (p_hat − p0)/√(p0(1−p0)/n) = 1.19370699368`, `|z| < 3`.
- **G3 — invariance / robustness.** (a) The DP oracle is recomputed for `N2 = 1200`; the P-position set on `[1, 800]` is identical to the N-run and equals the Fibonacci prefix — `invariance_discrepancies = 0`. (b) Randomized-play robustness: with a fresh `random.Random(SEED)`, from every winning start `n ∈ [1, N]` play `R = 40` complete games where our player uses the DP to pick a winning move and the opponent plays a uniformly-random legal move; `games_played = 31440`, `optimal_player_losses = 0`.
- **G4 — falsifiability (large |z|).** Primary naive foil "P-positions are the multiples of 3": disagreement with the true DP outcome over `[1, N]` is `274/800`, `|z| = 20.413966739 ≫ 3` → REJECTED. Secondary foil "P-positions are the powers of two": disagreement `18/800`, `|z| = 4.29119123911 > 3` → REJECTED. Both naive alternatives are rejected outside 3σ.

**Determinism & digest.** `build_results()` is a pure function of `SEED` and the fixed params. `main()` builds the results twice in one process and asserts the canonical JSON forms are byte-identical, then prints a human summary and `results_sha256=<64hex>` on its own line, exiting 1 if any gate fails. Two separate shell invocations reproduce the identical digest. Full 64-hex:

```
results_sha256=344cdaa21a550c745184aaab00951db1063f522d3fe25544738299fdf8ee7dce
```

## Grounding & scope

The game rules, the Fibonacci-number P-position characterisation, and the smallest-Zeckendorf-summand optimal move are all grounded in the English Wikipedia article **"Fibonacci nim"** at pinned revision `https://en.wikipedia.org/w/index.php?title=Fibonacci_nim&oldid=1341159330`@`fcebea2e6f696f94d6d9efda5edc537bf38f18d3` (fetched 2026-07-21T05:04:43Z; the API `rvprop=sha1` equals the self-computed SHA-1 of the raw wikitext — exact match, 10087 bytes). Zeckendorf uniqueness (unique non-consecutive-Fibonacci representation) is grounded in the article **"Zeckendorf's theorem"** at pinned revision oldid `1344127047`@`0cc894e5c3131f80c51a0db6f6fb042b76b73654` (sha1 verified the same two ways).

Honest quoted-vs-derived split (grep of the pinned raw wikitext, both directions):

| # | Cited value | Quoted / derived | Exact wikitext snippet (pinned revision) |
|---|---|---|---|
| 1 | losing positions ⟺ Fibonacci numbers | **quoted** (Fibonacci_nim) | "the first player can win if and only if the starting number of coins is not a Fibonacci number" |
| 2 | remove at most twice the previous move | **quoted** (Fibonacci_nim) | "on each move taking at most twice as many coins as the previous move, and winning by taking the last coin" |
| 3 | remove smallest Zeckendorf summand (optimal move) | **quoted** (Fibonacci_nim) | "it is always a winning move to remove all the coins (if this is allowed) or otherwise to remove a number of coins equal to the smallest Fibonacci number in the Zeckendorf representation" |
| 4 | Zeckendorf uniqueness (non-consecutive representation) | **quoted** (Zeckendorf's theorem) | "every positive integer can be represented uniquely as the sum of one or more distinct Fibonacci numbers in such a way that the sum does not include any two consecutive Fibonacci numbers" |

**Scope caveat.** The pinned articles state the theorem, the rule, and the strategy in prose. What is established FIRSTHAND by the verifier — not taken from Wikipedia — is the computational proof: the from-scratch game oracle `win(n, cap)` over `[1, 800]` (and `[1, 1200]`), the exact P-density `7/400`, the Monte-Carlo `z`, the randomized-play robustness over 31440 games, the two falsification `z` values, and the results-dict digest. The pages carry no `z`-values, no density fraction, and no digest.

## Gate power + margin ledger

| Gate | Type | Threshold | Observed | Margin | Verdict |
|---|---|---|---|---|---|
| G1 exact identity (loses(n) ⟺ n∈Fib) | zero-mismatch, n∈[1,800] | 0 mismatches | mismatches=0 | exact | PASS |
| G1 Zeckendorf-strategy legality + leaves-P | zero-violation, all winning n | 0 violations | zeckendorf_strategy_violations=0 | exact | PASS |
| G2 MC density vs exact 7/400 | match (\|z\|<3) | <3σ | \|z\|=1.19370699368 | 1.81σ headroom | PASS |
| G3(a) invariance N2=1200 on overlap | byte-identical == Fib prefix | 0 discrepancies | invariance_discrepancies=0 | exact | PASS |
| G3(b) randomized-play robustness | 0 losses over 31440 games | 0 losses | optimal_player_losses=0 | exact | PASS |
| G4 foil "multiples of 3" rejected | reject (\|z\|>3) | >3σ | \|z\|=20.413966739 | ≫3σ | PASS |
| G4 foil "powers of two" rejected | reject (\|z\|>3) | >3σ | \|z\|=4.29119123911 | 1.29σ over bar | PASS |

## Probe report (v0, self-adversarial)

**1. What is this really?** Fibonacci nim (Whinihan 1963): one pile of `n`, first move takes `1..n−1`, then take `1..2·(opponent's last take)`, last token wins. The claim: the mover loses iff `n` is a Fibonacci number, and from any winning `n` the optimal move is to remove the smallest Fibonacci summand of `n`'s Zeckendorf representation. Verified over `n ∈ [1, 800]` against a from-scratch game oracle with `mismatches = 0`.

**2. What would make it false?** Any `n ∈ [1, 800]` where the game oracle `loses(n)` disagrees with `n ∈ Fib` (G1 `mismatches > 0`); any winning `n` where the smallest Zeckendorf summand is illegal or fails to leave a P-position (G1 `zeckendorf_strategy_violations > 0`); a sampled loss-rate off the exact `7/400` by `|z| ≥ 3` (G2); the second horizon disagreeing on the overlap (G3a); any game our DP player loses to a random opponent (G3b); or a naive foil NOT being rejected (G4). Any gate failing → REJECT.

**3. Simplest version that still bites?** The bottom-up `win(n, cap)` table over `[1, 800]` with the opening state `(n, n−1)`, compared to the integer-recurrence Fibonacci set — 0 mismatches. The Zeckendorf leg is just: greedy-decompose each winning `n`, remove the smallest summand, assert the opponent is in a P-position. The `n = 1 → (1,0)` base case already fixes the first Fibonacci P-position with no floats.

**4. What is the counterintuitive core?** The losing positions are exactly the Fibonacci numbers, and the reason is Zeckendorf: a Fibonacci pile's representation is a single term larger than the opening quota, so the first player cannot reach a P-position; every non-Fibonacci pile has a small enough smallest summand to hand over. The moving cap (`2×` the last take) is what makes "just take the smallest summand" safe — the opponent's quota can never reach the next Fibonacci step.

**5. Where could I be fooling myself?** Assuming the theorem instead of the game. The verifier builds `win(n, cap)` purely from the move rules (`m = n` wins; else recurse on `(n−m, min(n−m, 2m))`) and only THEN compares to the independently-built Fibonacci set — the identity is a discovered agreement, not an input. The state uses integer caps only; `p0` is an exact Fraction; floats are fixed-format, so the digest is invocation-stable.

**6. What is the honest calibration?** SEED=20260717: G1 `mismatches=0`, `zeckendorf_strategy_violations=0` over `n_tested=800`; G2 `p0=7/400=0.0175`, `p_hat=0.01785`, `z=1.19370699368` (`<3`); G3 `invariance_discrepancies=0`, `games_played=31440`, `optimal_player_losses=0`; G4 foil-multiples-of-3 `|z|=20.413966739` (274 disagreements), foil-powers-of-two `|z|=4.29119123911` (18 disagreements). Exit 0; `results_sha256=344cdaa2…8ee7dce`; two runs byte-identical.

**7. What decision does it change?** When a take-away sub-task has a doubling reply cap, do not reason by pile parity or "round numbers" — the losing set is the Fibonacci numbers, and the safe move is the smallest Zeckendorf summand. The falsifiability gate kills the two intuitive foils (multiples of 3 at `|z|≈20`, powers of two at `|z|≈4.3`), so a heuristic that "feels regular" is decisively rejected against the true Fibonacci structure.

**8. How will a verdict session know it reproduced the head?** Re-run the stdlib verifier under SEED=20260717 and confirm `all_pass=true`, `first_failing_gate=null`, and results-dict sha256 `344cdaa21a550c745184aaab00951db1063f522d3fe25544738299fdf8ee7dce` byte-for-byte (in-process double-run guard AND a separate re-invocation are byte-identical); any gate fail or digest mismatch is a REJECT.

**Recommendation: sim-ready**
