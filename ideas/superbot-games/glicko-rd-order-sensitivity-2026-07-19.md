# A competitive game's Glicko ladder prices the ORDER of your results, not just the results: a player who posts the SAME 6-win / 6-loss record against the SAME field of opponents ends at a DIFFERENT rating depending only on whether those wins and losses arrive in a STREAK (WWWWWW then LLLLLL) or ALTERNATING (WLWLWL...). Because the rating deviation RD shrinks after every rated game, early games move the rating far more than late ones, so streak order lands ~60 Glicko points BELOW alternating order for an identical record. Order is not information — Glicko prices it anyway.

> **State:** sim-ready
> **Class:** superbot-games · rating-system microstructure · Glicko RD-weighted update (Glickman)
> **Target:** sim-lab (VERDICT 200, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@702e168 · fetched 2026-07-19T22:44:35Z
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/superbot-games/glicko_rd_order_sensitivity.py` (random, math, json, hashlib) — double-run byte-identical, all gates PASS, results-dict sha256 d4f690a5…d168ba6 (see Verifier + Dry-sim below).

## The phenomenon (one line)
On a Glicko ladder that updates one game at a time, an identical 6W-6L record against an identical opponent field settles at a rating that depends on the ORDER of the games: streak order (all wins, then all losses) ends a mean ~60 Glicko points BELOW alternating order (base regime, SEED=20260717), with the same sign in >99.9% of trials and the effect surviving a +200 shift of the whole opponent field — a pure artifact of the RD-weighted step, since order carries no information about skill.

## The folk belief
"A rating system is a scoreboard for your record. If two players beat the same six opponents and lose to the same six others, they earned the same season, so they should land at the same rating — the system is just tallying wins and losses against strength of schedule. The ORDER you happened to play them in is scheduling trivia; a good rating system is path-independent, so a hot streak and a see-saw with the identical record converge to the same number. Anything else would be the system rewarding luck of the calendar, which it obviously doesn't."

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
The folk belief is true of a BATCHED Glicko update (all games in one rating period) and true of Elo with a constant K-factor, but it is false of the sequential, per-game Glicko update that a live ladder actually runs — and the reason is the RD-weighting that is the whole point of Glicko. Glicko replaces Elo's constant step with a change scaled by the player's current rating deviation RD: the update is

    r' = r + (q / (1/RD^2 + 1/d^2)) * g(RD_j) * (s - E),
    RD' = sqrt( 1 / (1/RD^2 + 1/d^2) ),   with  d^2 = 1 / ( q^2 * g(RD_j)^2 * E(1-E) ),

so RD' < RD after every rated game — RD shrinks monotonically as evidence accumulates. The rating step is proportional to 1/(1/RD^2 + 1/d^2), which is INCREASING in RD, so a game processed while RD is still large moves the rating much further than the same game processed after RD has shrunk. A fresh player (RD0 = 350) who plays twelve games therefore front-loads almost all of their rating motion into the first few games. Now hold the record fixed and permute:
- **Streak order (WWWWWW then LLLLLL):** the six wins land first, at the highest RD, and drive the rating sharply UP while RD collapses; by the time the six losses arrive RD is small, so each loss barely moves the (now high) rating — the net of "big early up-moves, small late down-moves against an inflated rating" settles LOW.
- **Alternating order (WLWLWL...):** wins and losses interleave while RD is still large, so the early up- and down-moves partly cancel at high leverage and the rating tracks the true ~50% signal more tightly, settling HIGHER than streak order.

The empirical gap is a mean of ~60 Glicko points (z ~= -119 over 5000 paired trials) — sign-consistent in 99.96% of trials and ~54 points (z ~= -101) after shifting the opponent field +200. The counterintuitive core: the system that is CORRECTLY designed to grow more confident as it sees more games (shrinking RD) is, for exactly that reason, order-dependent within a rating period — a hot-and-cold see-saw and a streak with the identical record do NOT converge. The honest reading for a ladder designer: if you update per-game (not per-period) and seed new players at max RD, then the sequencing of a placement run is a rating lever, and two players with identical placement records can be ranked a full division apart on order alone. Batch the placement games into one rating period, or cap the early RD, to remove the sequencing edge.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Player starts at r = R0 = 1500.0, RD = RD0 = 350.0 (a fresh entrant at maximum deviation — the regime where RD-weighting bites hardest).
- Twelve opponents per trial, ratings drawn iid Normal(BASE_MEAN=1500, OPP_SD=200), each with fixed RD_j = OPP_RD = 30.0 (established opponents). The player's result vs opponent i is a WIN (s=1) on even indices i and a LOSS (s=0) on odd indices i — a fixed 6W-6L record wired to the opponent list, so permuting the processing order permutes the SAME (opponent, result) pairs.
- **Glicko-1 per-game update (one game = one rating period, no inactivity growth):** q = ln(10)/400; g(RD_j) = 1/sqrt(1 + 3 q^2 RD_j^2 / pi^2); E = 1/(1 + 10^(-g(RD_j)(r-r_j)/400)); d^2 = 1/(q^2 g(RD_j)^2 E(1-E)); r' = r + (q/(1/RD^2 + 1/d^2)) g(RD_j)(s-E); RD' = sqrt(1/(1/RD^2 + 1/d^2)).
- **Alternating regime:** process the twelve pairs in index order 0..11 (results W,L,W,L,...). **Streak regime:** process the six even-index (win) pairs first, then the six odd-index (loss) pairs (WWWWWW then LLLLLL). Both consume the identical pair multiset.
- **Paired common random numbers:** within a trial both regimes see the identical opponent draws and identical results; only the processing order differs, so Effect = final_r(streak) - final_r(alternating) is a clean paired difference with no cross-regime noise.
- **Robustness regime:** repeat the whole experiment with the opponent field drawn from Normal(SHIFT_MEAN=1700, 200) (a +200 shift) under a distinct seed (SEED+1), to confirm the order effect is not a one-regime artifact.

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned)
- TRIALS = 5000, N_GAMES = 12
- R0 = 1500.0, RD0 = 350.0, OPP_RD = 30.0, OPP_SD = 200.0
- BASE_MEAN = 1500.0, SHIFT_MEAN = 1700.0
- Z_GATE = 3.0, SIGN_FRAC = 0.90, MIN_POINTS = 5.0
- Base rng seed = SEED; shifted rng seed = SEED + 1.

## Pre-registered gates (sim-ready iff ALL hold, in order G1 -> G2 -> G3)
- **G1 — order matters (headline, >=3σ):** base-regime mean(streak - alternating) is nonzero at |z| = |mean/(sd/sqrt(TRIALS))| >= Z_GATE = 3.0. Identical record + identical opponents + different order -> an overwhelming rating difference.
- **G2 — real and material (sign + magnitude):** the fraction of trials whose effect shares the sign of the mean is >= SIGN_FRAC = 0.90 (consistent direction, not noise) AND |mean effect| >= MIN_POINTS = 5.0 Glicko points (materially above any rounding artifact).
- **G3 — robust under a shifted field (>=3σ):** with the opponent field shifted +200, the mean effect clears |z| >= 3.0 AND keeps the SAME sign as the base regime.

all_pass = G1 ∧ G2 ∧ G3.

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier (its `all_pass` field encodes exactly G1 ∧ G2 ∧ G3). Any gate failing -> REJECT (the order-sensitivity claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; margins are reported in σ on the standard error over N=TRIALS. Note the SIGN of the effect (streak below alternating) is an empirical finding reported, not gated beyond G2's sign-consistency; the gates test order-dependence, its materiality, and its robustness, not a pre-committed sign magnitude.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- Base regime: mean(streak - alternating) = -60.205174 Glicko points, z = -118.692568, same-sign fraction 0.9996.
- Shifted (+200) regime: mean = -54.313763, z = -100.513794, same-sign fraction 0.9954.
- **G1 order-effect:** |z| = 118.692568 >= 3.0 — PASS.
- **G2 sign+magnitude:** same-sign 0.9996 >= 0.90 AND |mean| 60.205174 >= 5.0 — PASS.
- **G3 robust (+200 shift):** |z| = 100.513794 >= 3.0 AND sign matches base (both negative) — PASS.
- all_pass = true; exit 0.
- In-process double-run assertion holds; two cross-invocation runs byte-identical.
- **Disclosed results-dict sha256 = d4f690a51493a8fc32dd0971548078b059277ba81b6e02c84364415f4d168ba6** (the sha256 of `json.dumps(results, sort_keys=True, separators=(",",":"))` — the value the verifier prints as `Results-JSON sha256:`; the results dict carries NO self-referential sha field, so there is no field-omission step and no JSON artifact is committed).

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `ideas/superbot-games/glicko_rd_order_sensitivity.py`. It seeds once per regime (base: SEED; shifted: SEED+1) and runs TRIALS=5000 paired trials: each trial draws twelve opponent ratings, wires a fixed 6W-6L record to them, processes the identical pair multiset in streak order and in alternating order under the Glicko-1 per-game update, and accumulates the paired effect (streak - alt). It reports each regime's mean effect, sd, se, z=mean/se and same-sign fraction, tests G1 (base |z|>=3), G2 (sign-fraction>=0.90 and |mean|>=5.0), G3 (shifted |z|>=3 and matching sign), asserts in-process determinism (compute() run twice -> identical canonical dict), and emits a canonical (sorted-keys, comma/colon-separated) results JSON with its sha256. Exit 0 iff all three gates pass.

Reproduce:

```
python3 ideas/superbot-games/glicko_rd_order_sensitivity.py
```

Expected: all_pass=true, exit 0, G1 base z=-118.6926, G2 same-sign 0.9996 / |mean| 60.205174, G3 shifted z=-100.5138, results-dict sha256 = d4f690a51493a8fc32dd0971548078b059277ba81b6e02c84364415f4d168ba6.

## Why it matters (game design)
Competitive ladders — chess servers, fighting-game and MOBA ranked queues, matchmaking-rating (MMR) systems — increasingly use Glicko/Glicko-2 precisely because RD lets a rating move fast when uncertain and slow when settled. This proposal shows the price of that virtue: a per-game Glicko update is ORDER-DEPENDENT within a placement run. Two consequences a designer usually misses. (1) **Placement sequencing is a rating lever.** A new account seeded at max RD that happens to get its wins clustered lands at a different placement rating than the identical record spread out — a ~60-point (roughly a division) gap on order alone, invisible to the player and un-earned. (2) **It rewards calendar luck.** A player on a genuine hot streak and a player see-sawing to the identical record are ranked apart, so the ladder encodes WHEN your wins arrived, not just how many — a fairness leak that widens the higher you seed the initial RD. The fixes are cheap and known: batch placement games into a single rating period (Glickman's own recommended usage — updates are defined PER rating period, not per game), or cap the initial RD / number of high-RD games, so the sequencing edge collapses to zero.

## Dedup
Distinct from the nearby rating / matchmaking / tournament priors in the game and fleet lanes:
- **mmr-rating-deflation** (population-level Elo/MMR drift as the pool changes) — a MEAN-DRIFT claim about the whole ladder over time; this card is a WITHIN-PLAYER, fixed-record, order-permutation claim and never changes the population.
- **matchmaking-winrate-mirage** (SBMM compresses win-rate toward 50%) — about the win-RATE a matcher induces; this card holds the record fixed and varies only processing order.
- **swiss-buchholz-luck-amplifier**, **tournament-seeding-bracket-optimality**, **single-elim-favorite-collapse** — bracket / tiebreak luck in tournament FORMATS; this card is about the rating UPDATE's path-dependence, with no bracket, no tiebreak, no elimination.
- **de Moivre small-sample variance** (fleet) — a variance-of-the-mean law; this card is a deterministic ORDER effect on a paired difference, not a sampling-variance claim.
- No existing head touches the RD-weighted Glicko update's order-dependence. `git grep` for "glicko" across ideas/ returns a single passing mention (in mmr-rating-deflation) and no dedicated Glicko mechanism; "order-sensitivity", "path-dependent rating", and "RD-weighted step" appear nowhere. This is the FIRST rating-system-microstructure card whose object is the sequential Glicko update itself.

## Model basis (declared model-dependence — the P024 discipline)
The result rests on standard, pinned structural choices. Load-bearing: (a) **per-game processing** — one game per rating period, which is how a live ladder updates in real time; the BATCHED Glicko update (all games in one period) is order-invariant BY CONSTRUCTION, so the effect is a property of per-game updating, not of Glicko's formulas per se, and the doc says so plainly. (b) **fresh player at RD0=350** — the maximum-uncertainty entrant, where the early/late step-size gap is largest; a low-RD veteran shows a smaller (but same-signed) effect because RD barely moves. (c) **fixed 6W-6L record wired to iid Normal(1500,200) opponents** — a balanced record isolates order from strength-of-schedule; unbalanced records or correlated opponents shift magnitudes but not the existence of an order effect. (d) **Glicko-1** — chosen for a clean closed-form per-game step; Glicko-2 adds a volatility σ that AMPLIFIES order-dependence (erratic sequences inflate σ), so Glicko-1 is the conservative choice. The QUALITATIVE claim — a sequential RD-weighted rating update is order-dependent, materially and robustly, because the step size shrinks with RD — holds for any RD-weighted system; the pinned constants make the ~60-point magnitude reproducible under the seed. The claim is scoped: under per-game Glicko-1 with RD0=350 and a fixed 6W-6L record vs iid Normal opponents, streak order ends ~60 Glicko points below alternating order at SEED=20260717 — demonstrated on the pinned constants, mechanism-explained (monotone RD shrink -> decaying step size), not asserted as a universal magnitude.

## Probe report (v0, 2026-07-19)

**1. What is this really?** A path-dependence claim on a Glicko ladder: an identical 6W-6L record against an identical opponent field settles at a DIFFERENT final rating depending only on the order the games are processed, because the RD-weighted step shrinks after each game and so weights early games more. Paired common-random-numbers sim over 12 games: Effect = final_r(streak WWWWWWLLLLLL) - final_r(alternating WLWLWL...), base mean ~-60 Glicko points, z ~= -119, sign-consistent in 99.96% of 5000 trials.
**2. What would make it false?** If the base-regime mean effect were NOT nonzero by |z| >= 3σ (G1 — order doesn't matter), or the same-sign fraction were < 0.90 or |mean| < 5.0 points (G2 — the effect is noise or immaterial), or the +200 shifted field failed |z| >= 3σ or flipped sign (G3 — one-regime artifact). Any -> REJECT.
**3. Simplest version that still bites?** SEED=20260717, one player at RD0=350, twelve opponents, a fixed 6W-6L record: process it WWWWWW-then-LLLLLL and again WLWLWL..., subtract the two final ratings — the gap is ~60 Glicko points, and it holds the same sign across essentially every trial and after shifting the opponents +200.
**4. What is the counterintuitive core?** A rating system you expect to be path-independent — same record, same number — is order-dependent for the exact reason it is well-designed: RD shrinks as evidence accumulates, so early games carry more rating weight than late ones, and a streak and a see-saw with the identical record diverge by roughly a division.
**5. Where could I be fooling myself?** The paired common-random-numbers design (same opponents, same results, only order differs) is the guard that the gap is order, not sampling noise — the per-trial effect is deterministic given the draw. The batched-Glicko sanity note (order-invariant by construction) is the guard that the effect is the per-game update, not a coding asymmetry. The +200 shift is the guard against a single-regime artifact. A low-RD veteran or a batched placement run would shrink the effect toward zero — consistent with the RD-weighting mechanism, not a contradiction.
**6. What is the honest calibration?** Dry-sim at SEED=20260717: base mean -60.205174 (z=-118.692568, same-sign 0.9996); shifted +200 mean -54.313763 (z=-100.513794, same-sign 0.9954). G1/G3 clear 3σ by ~100σ; G2's magnitude bar (5.0 points) is cleared ~12x. The sign (streak below alternating) is empirical and reported, not a pre-committed magnitude. Exit 0; results-dict sha256 d4f690a5…d168ba6.
**7. What decision does it change?** Treat per-game Glicko placement as a rating lever: batch placement games into one rating period (Glickman's defined usage) or cap the initial RD, so two identical placement records can't be ranked a division apart on sequencing alone.
**8. How will we know it worked?** The committed stdlib verifier reproduces the paired sim under SEED=20260717 with all three gates holding (G1 base |z|>=3, G2 sign>=0.90 and |mean|>=5.0, G3 shifted |z|>=3 same sign), the in-process double-run assertion passing, and the results-dict sha256 matching d4f690a51493a8fc32dd0971548078b059277ba81b6e02c84364415f4d168ba6.

## One-line design fix
Update placement games as a SINGLE Glicko rating period (or cap the initial RD) instead of one rating period per game, so an identical win/loss record settles at the same rating regardless of the order the games happened to arrive — removing the ~60-point sequencing edge the per-game RD-weighted update silently grants.

**Recommendation: sim-ready**
