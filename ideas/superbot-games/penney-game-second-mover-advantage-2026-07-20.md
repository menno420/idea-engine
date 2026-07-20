# In Penney's game — a coin-flip sequence duel where each player commits to one length-3 heads/tails pattern and whoever's pattern appears first in a stream of fair flips wins — committing FIRST is a losing move: for EVERY one of the 8 patterns the first player can pick, the second player has a reply that wins STRICTLY more than half the time (the hardest case, first-player HTT, still loses 2:1 to the reply HHT). Because whatever you commit to can be out-picked, there is NO best sequence — the "beats-more-than-half" relation among patterns is NON-TRANSITIVE, and the entire advantage belongs to whoever chooses SECOND. Order of commitment, not the patterns themselves, decides the game.

> **State:** sim-ready
> **Class:** superbot-games · sequential-competition microstructure · Penney's game / non-transitive waiting times (Penney 1969; Conway leading-number algorithm)
> **Target:** sim-lab (VERDICT 204, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@45ad3eb · fetched 2026-07-20T01:37:04Z
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/superbot-games/penney_game_second_mover_advantage.py` (random, math, json, hashlib) — an exact absorbing-Markov-chain solver cross-checked by a seeded Monte-Carlo, double-run byte-identical, all four gates PASS, results-dict sha256 8942324f…7744f4 (see Dry-sim below).

## The phenomenon (one line)
On a fair-coin sequence duel, the second player — seeing the first player's committed length-3 pattern — can always answer with a pattern that appears first more than half the time (exact win probability from 2/3 up to 7/8), so across all 8 first-choices the minimum second-player win rate is 0.661 (SEED=20260717, min z = 58.90958 over 30000 trials per first-pick), the advantage holds for 100% of first-choices, survives lengthening the patterns to 4 bits, and the Monte-Carlo win rates match the exact Markov-chain odds to within 0.0071 — order of commitment, not skill or the patterns, decides the winner.

## The folk belief
"A coin-sequence race is symmetric and fair. Every length-3 head/tail pattern is equally likely to appear — each has probability 1/8 on any three flips — so which pattern you pick can't matter, and it certainly can't matter WHO picks first. If anything, going first lets you grab the 'best' sequence before your opponent, so first-mover should be neutral or slightly favored. Two players choosing patterns for a fair coin is a coin flip about a coin flip: 50/50, and there is surely some strongest sequence you'd want to claim early."

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
Every claim in the folk belief is individually true and the conclusion is still wrong. Yes, each length-3 pattern has probability 1/8 on a fixed window of three flips — but a duel is not a fixed window, it is a RACE to first appearance in an unbounded stream, and first-appearance (waiting time) is governed by the patterns' self-overlap, not by their fixed-window probability. A pattern that can overlap itself (like HHH: after HH a single H both completes it and re-primes it) has a longer, heavier-tailed waiting time than one that cannot, and — crucially — the race between two patterns depends on their CROSS-overlap, how the tail of one seeds the head of the other. This makes the "appears-first" relation a TOURNAMENT that need not be transitive.

The second player exploits exactly this. Given the first player's pattern p = b1 b2 b3, the standard optimal reply is R(p) = (¬b2) b1 b2 — prepend the complement of the first player's SECOND symbol to the first player's first two symbols. R(p) is built to sit "one step upstream" of p: on the way to completing p, the coin stream must pass through a configuration from which R(p) has already appeared, so R(p) tends to win the race. Conway's leading-number algorithm gives the exact odds, and they are never worse than 2:1 for the second player: R(HHH)=THH wins 7:1, R(HHT)=THH wins 3:1, R(HTH)=HHT wins 2:1, R(HTT)=HHT wins 2:1 (and the four T-mirror cases by symmetry). So there is no pattern the first player can hide behind — the reply map R sends EVERY pattern to a pattern that beats it. A tournament in which every vertex is beaten by another has no dominant element, so it must contain a directed cycle: the "beats-more-than-half" relation is non-transitive, and "pick the best sequence" is not a well-defined move. The only dominant strategy is procedural: make the other player commit first.

The counterintuitive core: fairness of the coin and uniformity of the patterns are real, yet they live at the level of a single three-flip window; the GAME lives at the level of first-appearance in a stream, where self- and cross-overlap break the symmetry the folk belief assumes. The honest reading for a game designer: any mechanic that is secretly a "first pattern / configuration to appear wins" race (first to spell a word, first combo to land, first to hit a target sub-sequence) can be non-transitive and second-mover-decided even when every atomic outcome is uniform and the coin is fair — so committing order is a hidden, un-earned lever.

## The formal model (committed constants — sim-lab must reproduce exactly)
- **Duel.** Two players each hold a length-L binary pattern over {H=1, T=0}. A fair coin (P_HEADS=0.5) is flipped repeatedly; the first player whose pattern appears as L consecutive flips wins that trial.
- **First player** ranges over ALL 2^L patterns. **Second player** answers each with the standard optimal reply R(p) = (¬p2) · p1 · … · p_{L-1} (complement of the second symbol, then the first L-1 symbols). Player 2's win = its pattern appearing before player 1's.
- **Exact odds (ground truth).** `exact_p2_winrate(pa, pb)` builds an absorbing Markov chain whose transient states are all binary strings of length 0..L-1 (the last L-1 flips are a sufficient statistic for which length-L pattern completes next) with two absorbing states (pa first, pb first), and solves h_∅ = P(pb absorbs before pa) by stdlib Gaussian elimination. This is the exactly-true value (2/3, 3/4, 7/8, … for L=3).
- **Monte-Carlo (reproducible dry-sim).** `mc_p2_winrate` seeds one `random.Random(seed)` per regime and, for each first-pick, flips a fair coin until pa or pb appears, over TRIALS=30000 trials, recording player 2's empirical win rate.
- **Base regime:** L=3 (8 first-picks), rng seed = SEED. **Robustness/shift regime:** L=4 (16 first-picks), rng seed = SEED+1 — lengthening the patterns is the structural shift (longer patterns → smaller but still strictly positive second-mover edge).
- **Paired to the exact value:** every Monte-Carlo win rate is compared to the exact Markov odds for the same pair, so G4 tests that the empirical race reproduces the exact non-transitive odds, not merely that some effect exists.

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned); base rng seed = SEED, shifted rng seed = SEED + 1.
- BASE_L = 3, SHIFT_L = 4, TRIALS = 30000, P_HEADS = 0.5.
- Optimal reply R(p) = (1 − p[1],) + p[:L−1].
- Z_GATE = 3.0, SIGN_FRAC = 1.0, MIN_EDGE = 0.05, EXACT_TOL = 0.02.
- Floats rounded 6 dp; results dict carries no self-referential sha field; digest = sha256 of the compact-canonical (sort_keys, comma/colon) results JSON, printed to stdout.

## Pre-registered gates (sim-ready iff ALL hold, in order G1 -> G2 -> G3 -> G4)
- **G1 — second player always wins (headline, ≥3σ):** across all 2^BASE_L first-picks, the MINIMUM z-score of (Monte-Carlo player-2 win rate − 0.5) is ≥ Z_GATE = 3.0. Every first choice is beaten by its reply at overwhelming significance.
- **G2 — universal and material (sign + magnitude):** the fraction of first-picks that favor player 2 (edge > 0) is ≥ SIGN_FRAC = 1.0 (ALL of them, not a majority) AND the minimum edge over first-picks is ≥ MIN_EDGE = 0.05 (the worst case is materially above 50%, not a rounding artifact).
- **G3 — robust to a structural shift (≥3σ):** repeat at SHIFT_L = 4 under seed SEED+1; the minimum z ≥ 3.0 AND every first-pick still favors player 2 (same sign as base). The second-mover advantage is not an artifact of length 3.
- **G4 — the odds are EXACTLY true:** for every first-pick in both regimes, |Monte-Carlo win rate − exact Markov win rate| ≤ EXACT_TOL = 0.02. The empirical race reproduces the exact, closed-form non-transitive odds.

all_pass = G1 ∧ G2 ∧ G3 ∧ G4.

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 ∧ G4 hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier (its `all_pass` field encodes exactly G1 ∧ G2 ∧ G3 ∧ G4). Any gate failing → REJECT (the second-mover-advantage / non-transitivity claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; z-scores are the standard error on a Bernoulli proportion over N=TRIALS. The SIGN of the effect (player 2 favored) is the claim itself and is gated by G2 (favor_frac = 1.0), not merely reported.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- Base regime (L=3, 8 first-picks): min z = 58.90958, min edge = 0.161, min win rate = 0.661, favor_frac = 1.0, max |MC − exact| = 0.007067. Hardest first-pick = HTT (100); its reply HHT (110) wins exactly 0.666667 (MC 0.661).
- Shift regime (L=4, 16 first-picks): min z = 27.726515, min edge = 0.079033, min win rate = 0.579033, favor_frac = 1.0, max |MC − exact| = 0.005933. Hardest first-pick = 0011; its reply 1001 wins exactly 0.583333 (MC 0.579033).
- **G1 second-player-always-wins:** min z = 58.90958 ≥ 3.0 — PASS.
- **G2 universal + material:** favor_frac = 1.0 ≥ 1.0 AND min edge 0.161 ≥ 0.05 — PASS.
- **G3 robust (L=4 shift):** min z = 27.726515 ≥ 3.0 AND all 16 favor player 2 — PASS.
- **G4 exactly-true:** base max dev 0.007067 ≤ 0.02 AND shift max dev 0.005933 ≤ 0.02 — PASS.
- all_pass = true; exit 0.
- In-process double-run assertion holds; two cross-invocation runs byte-identical.
- **Disclosed results-dict sha256 = 8942324fa0c31abf11a053bb56b98306709611f73b9a2ad344fe0034d87744f4** (sha256 of `json.dumps(results, sort_keys=True, separators=(",",":"))`; the results dict carries NO self-referential sha field, so no field-omission step and no JSON artifact is committed).

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `ideas/superbot-games/penney_game_second_mover_advantage.py`. For each first-pick it computes the exact player-2 win probability by solving an absorbing Markov chain over the last L-1 flips (Gaussian elimination) and the empirical win rate by seeded Monte-Carlo coin flips (TRIALS=30000), then tests G1 (base min z ≥ 3), G2 (favor_frac ≥ 1.0 and min edge ≥ 0.05), G3 (L=4 shift min z ≥ 3 and all favor P2), G4 (|MC − exact| ≤ 0.02 everywhere), asserts in-process determinism (compute() run twice → identical canonical dict), and emits a canonical results JSON with its sha256. Exit 0 iff all four gates pass.

Reproduce:

```
python3 ideas/superbot-games/penney_game_second_mover_advantage.py
```

Expected: all_pass=true, exit 0, G1 base min_z=58.9096, G2 favor_frac 1.0 / min_edge 0.161, G3 shift min_z=27.7265, G4 devs 0.00707 / 0.00593, results-dict sha256 = 8942324fa0c31abf11a053bb56b98306709611f73b9a2ad344fe0034d87744f4.

## Why it matters (game design)
Any competitive mechanic that resolves as "first target configuration to appear in a stream wins" inherits Penney's non-transitivity, and designers routinely build such mechanics without noticing. Examples: a race to be first to spell a word from a shared letter feed, first to land a specified combo/input sub-sequence, first to roll a target face-run, first pattern-match in a shared board feed. In all of these, if players commit their target in sequence (one picks, then the other), the second picker can hold a 2:1-to-7:1 edge that no amount of skill closes, and there is no "strongest" target to pre-claim because the tournament cycles. Two consequences a designer usually misses. (1) **Commit order is a hidden rating lever.** Reveal-then-pick (sequential commitment) hands the later committer a structural edge invisible to the earlier one — a fairness leak orthogonal to skill. (2) **"Pick the best pattern" is not a strategy.** Because the beats-relation is non-transitive, guides that rank "the best sequence" are selling a fiction; the meta has no dominant target, only a rock-paper-scissors cycle. The fix is procedural and cheap: require SIMULTANEOUS commitment (both players lock their pattern blind), or randomize which player commits first each round, so the second-mover edge cannot be farmed.

## Dedup
Distinct from every occupied game-lane head:
- **glicko-rd-order-sensitivity** (P187) — order of RESULTS within one player's rating update; this card is about order of COMMITMENT between two players in a waiting-time race, no rating system involved.
- **swiss-buchholz-luck-amplifier** (P179), **single-elim-favorite-collapse** (P131), **pie-rule-opening-trap** (P175) — tournament FORMAT / tiebreak / swap effects; this card has no bracket, no tiebreak, no seeding — a two-player sequence race on a fair coin.
- **blotto-evenness-trap** (P171), **kingmaker-skill-inversion** (P183) — allocation and three-player spite; this card is a two-player, zero-allocation, pure-timing game.
- No existing head touches waiting-time / first-appearance races, self-overlap, non-transitive coin-sequence dueling, or Conway's leading-number odds. `git grep` for "penney", "non-transitive", "waiting time", "leading number", "optimal reply" across ideas/ returns nothing. This is the FIRST sequential-race / non-transitive-timing card in the lane.

## Model basis (declared model-dependence — the P024 discipline)
Load-bearing structural choices, all pinned: (a) **fair coin, uniform patterns** — the model deliberately grants the folk belief its strongest footing (every atomic outcome symmetric) and still produces the asymmetry, so the effect is not smuggled in via a biased coin; (b) **the standard optimal reply R(p)** — a fixed, well-known deterministic rule, not an optimizer, so the second player's edge is a floor (a per-pattern exhaustive best-reply would only widen it); (c) **L ∈ {3,4}** — length 3 is the classic regime; length 4 is the shift, where the edge SHRINKS (min edge 0.161 → 0.079033) yet stays strictly positive, confirming the advantage is structural, not a length-3 coincidence; (d) **absorbing Markov chain over the last L-1 flips** — exact by the standard sufficiency of the last L-1 symbols for length-L pattern completion, and independently corroborated by the seeded Monte-Carlo (G4). The QUALITATIVE claim — a two-player first-appearance race on a fair coin is second-mover-decided and non-transitive because first-appearance depends on overlap, not fixed-window probability — is a theorem (Penney 1969; Conway), true for all L ≥ 3; the pinned constants make the specific win rates (min 0.661 at L=3) reproducible under the seed. The claim is scoped: under a fair coin with the standard optimal reply, every length-3 first-pick loses to its reply with exact probability ≥ 2/3, min empirical 0.661 at SEED=20260717 — demonstrated on the pinned constants and mechanism-explained (overlap-driven waiting times), not asserted as a universal magnitude.

## Probe report (v0, 2026-07-20)

**1. What is this really?** A non-transitive waiting-time claim: in a fair-coin race between two committed length-3 patterns, whoever commits SECOND can always pick a reply that appears first more than half the time (exact odds 2/3–7/8), so no pattern is best and the game is decided by commitment order, not by the coin or the patterns. Exact absorbing-Markov odds cross-checked by a seeded 30000-trial Monte-Carlo per first-pick.
**2. What would make it false?** If the base-regime minimum z (over all 8 first-picks) were < 3σ (G1 — some first-pick is not beaten), or any first-pick failed to favor player 2 or the worst edge were < 0.05 (G2 — the advantage is not universal or immaterial), or the L=4 shift dropped below 3σ or flipped a sign (G3 — a length-3 artifact), or any Monte-Carlo rate disagreed with the exact Markov odds by > 0.02 (G4 — the "exactly true" cross-check fails). Any → REJECT.
**3. Simplest version that still bites?** SEED=20260717, first player picks HTT; second player answers HHT; flip a fair coin until one appears — HHT wins exactly 2 times out of 3 (MC 0.661), and the same second-mover win holds for all 8 first-picks. That single 2:1 case already refutes "coin races are 50/50."
**4. What is the counterintuitive core?** Every length-3 pattern is equally likely on a fixed three-flip window AND the coin is fair, yet the RACE to first appearance is not symmetric, because first-appearance is governed by pattern overlap, not fixed-window probability — so the second picker always has a winning answer and there is no best sequence to pre-claim.
**5. Where could I be fooling myself?** The exact Markov solver is the guard against a simulation coding artifact: G4 forces the empirical race to match the closed-form odds to 0.02, so a bug in either the flip loop or the chain would break G4. Uniform patterns + fair coin is the guard against smuggling the asymmetry into the inputs. The L=4 shift (where the edge shrinks but persists) is the guard against a length-3 coincidence. A simultaneous-commitment variant would erase the effect — consistent with the mechanism (the edge is second-mover-specific), not a contradiction.
**6. What is the honest calibration?** Base (L=3): min z 58.90958, min edge 0.161, min win rate 0.661, all 8 favor player 2, max |MC−exact| 0.007067. Shift (L=4): min z 27.726515, min edge 0.079033, all 16 favor player 2, max |MC−exact| 0.005933. G1/G3 clear 3σ by ~28–59σ; G2's magnitude bar (0.05) is cleared ~3× even at L=4; G4 clears its 0.02 tolerance ~3×. Exit 0; results-dict sha256 8942324f…7744f4.
**7. What decision does it change?** Treat any "first configuration to appear wins" mechanic as potentially non-transitive and second-mover-decided: require simultaneous blind commitment or randomize commit order each round, and stop publishing "best sequence" guides for a meta that provably cycles.
**8. How will we know it worked?** The committed stdlib verifier reproduces both regimes under SEED=20260717 with all four gates holding (G1 base min z ≥ 3, G2 favor_frac = 1.0 and min edge ≥ 0.05, G3 L=4 min z ≥ 3 all-favor, G4 |MC−exact| ≤ 0.02 everywhere), the in-process double-run assertion passing, and the results-dict sha256 matching 8942324fa0c31abf11a053bb56b98306709611f73b9a2ad344fe0034d87744f4 across two separate invocations.

## One-line design fix
Make both players commit their target pattern SIMULTANEOUSLY and blind (or randomize which player commits first each round), so the second picker can't answer the first's pattern with a 2:1–7:1 reply — removing the un-earned, skill-independent commit-order edge that a sequential "first pattern to appear wins" race silently grants.

**Recommendation: sim-ready**
