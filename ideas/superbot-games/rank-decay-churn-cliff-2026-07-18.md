# PROPOSAL 143 — rank-decay churn cliff: loss aversion inverts the decay lever. A ranked ladder applies rank decay so idle players lose rank; the folk belief is "more decay = more activity" (decay pressures people to keep playing). Model the ladder as a loss-averse agent population and the lever INVERTS — a prospective rank loss is felt LAMBDA≈2.25× as strongly as an equal gain, so beyond a small optimal decay rate aggressive decay pushes marginal players to QUIT the game entirely (churn), and total ladder activity FALLS as decay rises; the SIGN of decay's effect on activity depends on the loss-aversion coefficient — with no loss aversion decay is harmless (folk belief holds), with realistic loss aversion decay backfires.

> **State:** sim-ready
> **Class:** superbot-games · competitive ranked-ladder rank-decay design / loss-aversion-driven churn (prospect theory)
> **Anchor:** Kahneman & Tversky (1979) prospect theory; Tversky & Kahneman (1992) loss-aversion coefficient λ ≈ 2.25 — a prospective loss is felt ~2.25× as strongly as an equal gain
> **Target:** sim-lab (VERDICT 156, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@66b78325cc7e7fae1834bc66e8c2b25e41c66b83 · fetched 2026-07-18T19:20:10Z
> **Reference (external, reachable):** [Loss aversion — Wikipedia](https://en.wikipedia.org/wiki/Loss_aversion) — verified reachable 2026-07-18 via WebFetch ("Loss aversion is a cognitive bias in which the same situation is perceived as worse if it is framed as a loss, rather than a gain … Empirically, losses tend to be treated as if they were twice as large as an equivalent gain … first proposed by Amos Tversky and Daniel Kahneman as an important component of prospect theory")
> **Verifier (firsthand):** `ideas/superbot-games/rank-decay-churn-cliff-2026-07-18.py` · results-dict sha256 `ea060663fecf79059bedeb98d43c4f010d2daca6ff273ebf6a97545ddc83ac59`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
Rank decay has two opposed channels on an idle player — a folk RECOVERY channel (losing rank raises future win probability, pulling them back) and a loss-averse PAIN channel (the felt rank loss accumulates and, past a patience threshold, makes them quit); under realistic loss aversion the pain channel wins for marginal players, so raising the decay rate past a small optimum REDUCES total ladder activity instead of raising it.

## The folk belief
"Rank decay keeps a ladder healthy. If players lose rank when they stop playing, decay pressures them to keep playing — nobody wants to watch their rank slide — so more decay means more logins and more matches. Crank decay up to fight inactivity." Ladder designers treat decay as a monotone activity lever: more decay, more activity.

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
Model a ranked ladder as a population of N players. Each player i has a fixed **true_rank** (their real skill) and a moving **current_rank** that starts at true_rank. Underranking **underrank = true_rank − current_rank** drives matchmaking win probability **p = clip(0.5 + K·underrank, 0.05, 0.95)** — an underranked player (current below true) faces easier opponents and wins more (this is the folk "grind your rank back" channel). Each period a player draws a fresh **per-match enjoyment u ~ Uniform[0, U_MAX]** (their day-to-day disposition to play) and forms a loss-averse subjective match value

    v = u + DELTA·(p − LAMBDA·(1 − p)),

where a prospective rank GAIN of DELTA is valued +DELTA and a prospective rank LOSS of DELTA is valued −LAMBDA·DELTA. **LAMBDA is the loss-aversion coefficient** — with LAMBDA = 1 a gain and a loss of equal size cancel (risk-neutral); with the empirical LAMBDA = 2.25 a loss stings 2.25× as much as an equal gain.

Each period, for each surviving player:
- **If v > 0** the player PLAYS one match (win w.p. p → current_rank += DELTA; else current_rank −= DELTA), counts one unit of activity, and resets accumulated idle pain to 0.
- **If v ≤ 0** the player is idle: apply decay **current_rank −= d** (this raises underranking and hence future p — the folk recovery channel), accumulate loss-averse pain **pain += LAMBDA·d**, and if **pain > PATIENCE** the player QUITS the game permanently (churn).

Now the two channels compete. When an idle player's rank decays, their future win probability p climbs (recovery — good), but the felt rank loss accrues as pain at rate LAMBDA·d (bad). A marginal player recovers (v turns positive again) only if p rises enough BEFORE pain crosses PATIENCE. The recovery deadline scales like LAMBDA·(deficit)/K while the pain deadline scales like PATIENCE/LAMBDA — so **higher LAMBDA both slows recovery and speeds the quit**: past a small decay rate, aggressive decay churns marginal players out faster than it grinds them back. With no loss aversion (LAMBDA = 1) the pain channel is weak, decay is a harmless (even mildly helpful) stabilizer, and the folk belief holds; with realistic loss aversion (LAMBDA = 2.25) the churn dominates and total activity FALLS as decay rises. The lever's SIGN is set by the loss-aversion coefficient — the whole result is a model-dependence claim (P024).

Concretely (SEED = 20260717, committed constants): at LAMBDA = 2.25, moving from no decay to aggressive decay drops steady-state activity from **657.0 to 581.0 matches/period** (a **−76.1**, ~11.6% cut) while churning the surviving population from **1000 to 709** (291 players quit). At LAMBDA = 1.0 the SAME decay leaves activity essentially unchanged (**963.0 → 966.5**, +0.4%) and churns **nobody** (1000 → 1000). Same lever, opposite sign — set by loss aversion.

## The formal model (committed constants — sim-lab must reproduce exactly)
- N players, T periods, R independent trials (per-trial RNG seed offset from SEED by r·7919); true_rank fixed at 0 so underrank = −current_rank.
- Per period per surviving player: draw u ~ Uniform[0, U_MAX]; p = clip(0.5 − K·current_rank, 0.05, 0.95); v = u + DELTA·(p − LAMBDA·(1 − p)).
- v > 0 → play (win w.p. p: current += DELTA; else current −= DELTA), activity += 1, pain = 0. v ≤ 0 → current −= d, pain += LAMBDA·d, quit permanently if pain > PATIENCE.
- Steady-state total activity = average matches played per period over the last half of T; surviving population = players not yet quit.
- Two worlds LAMBDA_CONTROL = 1.0 and LAMBDA_REAL = 2.25, each at d = 0 (baseline) and d = D_HIGH (aggressive); the per-trial reduction is baseline_activity − highdecay_activity under COMMON RANDOM NUMBERS (baseline and highdecay share the trial seed) for a low-variance paired estimator.
- **Model note (declared):** u is the per-MATCH enjoyment, drawn fresh each period — the intrinsic day-to-day disposition to play. This is what makes a no-decay ladder a LIVING population (players cycle in and out on their own) rather than a degenerate one where any single declined match freezes a player forever; every other quantity is exactly as stated.

## Pinned world (committed constants)
- SEED = 20260717
- SIGMA_GATE = 3.0
- N = 1000; T = 200; R = 20
- K = 0.03; DELTA = 1.0; U_MAX = 2.0; PATIENCE = 3.0; D_HIGH = 0.3
- LAMBDA_CONTROL = 1.0; LAMBDA_REAL = 2.25 (empirical prospect-theory coefficient)
- Headline metric = paired reduction baseline_activity − highdecay_activity (common random numbers per trial)

## Pre-registered gates (APPROVE iff ALL hold, in order G1 → G2 → G3)
- **G1 — estimator agreement.** Split the R headline (LAMBDA = 2.25) paired reductions into two independent halves; the half-vs-half difference has |z| < SIGMA_GATE — the two halves do NOT significantly disagree, so the estimator is stable and the headline is not an artifact of one noisy half.
- **G2 — mechanism control.** In the LAMBDA_CONTROL = 1.0 world, aggressive decay does NOT reduce activity — the reduction (baseline − highdecay) is NOT significantly positive (z = reduction/se < SIGMA_GATE). Without loss aversion the backfire is absent (decay is harmless/mildly helpful — folk belief holds), isolating loss aversion as the cause. (One-sided by construction: the control asserts decay does not HURT; a negative reduction — decay helping — passes.)
- **G3 — head.** In the LAMBDA_REAL = 2.25 world, aggressive decay SIGNIFICANTLY reduces activity — the reduction has z = reduction/se ≥ SIGMA_GATE. The counterintuitive backfire: more decay, less activity.

## Pre-registered decision rule
APPROVE (sim-ready confirmed) iff G1 AND G2 AND G3 all hold in order and the verifier exits 0 with a reproducible results-dict sha256 across a deterministic double-run. Any gate failing ⇒ REJECT/REVISE.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
{
  "all_pass": true,
  "control_base_activity": 963.0025,
  "control_base_pop": 1000.0,
  "control_high_activity": 966.487,
  "control_high_pop": 1000.0,
  "first_failing_gate": null,
  "g1_agreement": true,
  "g1_half_a_reduction": 75.023,
  "g1_half_b_reduction": 77.079,
  "g1_z": -0.835097,
  "g2_control": true,
  "g2_control_reduction": -3.4845,
  "g2_se": 0.258057,
  "g2_z": -13.502832,
  "g3_head": true,
  "g3_head_reduction": 76.051,
  "g3_se": 1.221153,
  "g3_z": 62.278027,
  "n": 1000,
  "params": {
    "d_high": 0.3,
    "delta": 1.0,
    "k": 0.03,
    "lambda_control": 1.0,
    "lambda_real": 2.25,
    "patience": 3.0,
    "u_max": 2.0
  },
  "proposal": 143,
  "r": 20,
  "real_base_activity": 657.044,
  "real_base_pop": 1000.0,
  "real_high_activity": 580.993,
  "real_high_pop": 709.0,
  "seed": 20260717,
  "sigma_gate": 3.0,
  "t": 200
}
Results-JSON sha256: ea060663fecf79059bedeb98d43c4f010d2daca6ff273ebf6a97545ddc83ac59
G1 agreement    : PASS (half_a-half_b, z=-0.84, |z|<3.0)
G2 control      : PASS (lambda=1 reduction=-3.4845, z=-13.50, not-sig-positive z<3.0)
G3 head         : PASS (lambda=2.25 reduction=+76.0510, z=+62.28, z>=3.0)
all_pass        : True first_failing_gate: None
```
Results-dict sha256: `ea060663fecf79059bedeb98d43c4f010d2daca6ff273ebf6a97545ddc83ac59` (deterministic double-run, exit 0 both times).

## Verifier
`ideas/superbot-games/rank-decay-churn-cliff-2026-07-18.py` — stdlib only (`random, math, json, hashlib`). Simulates the N-player ladder over T periods for two loss-aversion worlds (LAMBDA ∈ {1.0, 2.25}) at two decay levels (0 and D_HIGH), R paired trials each under common random numbers, and runs the three ordered z-gates (half-vs-half estimator agreement, the LAMBDA = 1 not-significantly-positive control, and the LAMBDA = 2.25 significant-reduction head). Emits the whole results dict (no self-referential sha field; every float rounded to 6 decimals; the compact canonical serialization's sha256 IS the disclosed digest; stdout dumps the pretty indent=2 view — the WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture, P127+ twist). Writes no JSON to disk.

## Reproduce
```
python3 ideas/superbot-games/rank-decay-churn-cliff-2026-07-18.py
```
Expected: prints the results JSON, `Results-JSON sha256: ea060663fecf79059bedeb98d43c4f010d2daca6ff273ebf6a97545ddc83ac59`, three `PASS` lines, exit 0.

## Why it matters (game design)
Rank decay is not a monotone activity dial — it is a lever whose SIGN flips with how loss-averse your players are. A no-decay or gently-decaying ladder keeps marginal players in the pool (they cycle in and out on their own disposition); an aggressively-decaying ladder makes the marginal player watch a rank they earned bleed away, and because a felt loss stings ~2.25× an equal gain, the honest response is not "grind it back" but "quit." Design consequences: (1) treat decay as a churn risk, not a retention tool — past a small optimum it trades a little forced activity for a lot of permanent departures; (2) if you must decay (to keep leaderboards fresh), soften the LOSS frame — decay toward a soft floor, show "provisional rank" rather than deducting earned rank, or pause decay after a short absence, so the pain channel never fires; (3) measure churn as a function of decay rate, not just activity in the first week — the activity bump is real and immediate, the churn cliff is delayed and permanent. Read "we added decay and logins went up but the population is shrinking" as the loss-aversion churn cliff, not a seasonal dip.

## Dedup
- Distinct from every prior game-lane card: shop-reroll (optimal stopping), streak-shield (regression to the mean), energy-cap (renewal overflow forfeiture), matchmaking-winrate-mirage (Elo compression under SBMM), compounding-reward-inequality (log-normal Gini), PRD proc-rate compression, snipe-clearing-leak (auction microstructure), guild-volunteer-dilemma (N-player public-goods provision), single-elim favorite-collapse (tournament order statistics), balance-triangle pick-rate inversion (zero-sum matrix equilibrium), Ringelmann raid coordination overhead (group-size per-capita output decay), pity-anticipation-collapse (gacha pity timing), rubber-band PID controller instability. **None model a ranked-ladder rank-DECAY lever, loss-aversion-driven CHURN, or a decay-rate/activity inversion whose SIGN flips with the loss-aversion coefficient.**
- Closest neighbours are streak-shield (also a rank/rating dynamic) and energy-cap (also an "if you don't act you lose value" pressure): streak-shield is about regression-to-the-mean in a protected rating and energy-cap is about deterministic renewal overflow — neither has a loss-averse quit decision or a sign-flipping lever. This is the FIRST prospect-theory / loss-aversion card and the FIRST rank-DECAY card in the game lane.

## Model basis (declared model-dependence — the P024 discipline)
The result is a **sign-dependence** claim: the sign of ∂(activity)/∂(decay rate) is set by the loss-aversion coefficient LAMBDA. The DIRECTION (decay harmless/mildly helpful at LAMBDA = 1, activity-reducing and churn-inducing at LAMBDA = 2.25) holds for any model where (a) idle players decay, (b) the felt rank loss accumulates at a rate proportional to LAMBDA and triggers a quit past a patience threshold, and (c) decay's recovery channel (higher p) is slower to rescue a marginal player than the pain channel is to churn them — which is exactly the LAMBDA > 1 regime. The specific magnitudes (−76 activity, 291 quits at LAMBDA = 2.25 vs +3.5 activity, 0 quits at LAMBDA = 1) are pinned to (K, DELTA, U_MAX, PATIENCE, D_HIGH) = (0.03, 1.0, 2.0, 3.0, 0.3) and N = 1000, T = 200. **Two declared modelling choices** (flagged, not hidden): (i) u is the per-MATCH enjoyment drawn fresh each period — required so that a no-decay baseline is a living population rather than a degenerate frozen one (with a single fixed per-player u, any player who ever declines a match is frozen out permanently, which is not a meaningful "healthy ladder" baseline and would make decay trivially helpful); (ii) G2 is the one-sided pre-registered control "decay does not significantly REDUCE activity" (reduction not significantly positive) — matching the thesis that absent loss aversion decay is harmless (folk belief holds), so a negative reduction (decay mildly helping) passes. Real ladders add seasonal resets, MMR/visible-rank splits, soft floors, and heterogeneous patience; the minimal single-rank model is the smallest object that exhibits the loss-aversion churn cliff, and richer loss frames only move where the cliff sits.

## Probe report (v0, 2026-07-18)

**1. What is this really?** A sign-flip lever. Rank decay acts on an idle player through two opposed channels — a folk recovery channel (lost rank ⇒ easier matches ⇒ pulled back) and a loss-averse pain channel (the felt rank loss accumulates ⇒ quit). The net sign of decay's effect on total activity is set by the loss-aversion coefficient LAMBDA: harmless at LAMBDA = 1, activity-reducing and churn-inducing at the empirical LAMBDA = 2.25. "More decay = more activity" is true only for risk-neutral players.
**2. What would make it false?** If the LAMBDA = 2.25 reduction were ≤ 0 or z < 3σ (G3 fails — aggressive decay does not actually cut activity), or if the LAMBDA = 1 control showed a significant reduction too (G2 fails — the backfire is not specific to loss aversion, so it is some other artifact), or if the two halves of the trials disagreed (G1 fails — the estimator is unstable). Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED = 20260717; a 1000-player ladder, K = 0.03 win-prob slope, a modest aggressive decay D_HIGH = 0.3, patience 3, and the single empirical constant LAMBDA = 2.25 already cut steady-state activity ~11.6% and churn 291 of 1000 players — while the exact same decay at LAMBDA = 1 churns nobody and leaves activity flat. One free parameter (LAMBDA) flips the lever.
**4. What is the counterintuitive core?** "Decay pressures idle players back, so more decay = more activity" is inverted. Because a felt rank LOSS is worth ~2.25× an equal gain, aggressive decay makes the marginal player's honest move "quit," not "grind back" — so past a small optimum, raising decay LOWERS total activity while quietly shrinking the population. The activity dial runs backwards exactly where designers reach for it hardest (to fight inactivity).
**5. Where could I be fooling myself?** The paired common-random-numbers estimator could look artificially tight — G1 guards it by requiring two independent halves of the trials to agree (z = −0.84, |z| < 3). The backfire could be some generic sim artifact rather than loss aversion — G2 is the control: the identical decay at LAMBDA = 1 produces NO significant reduction (z = −13.5 in the harmless direction) and zero churn, so loss aversion is doing the work. And the baseline could be a degenerate frozen state inflating the gap — the declared per-match u redraw keeps the no-decay ladder a living population (pop stays 1000, activity 963–657 across worlds), so the reduction is a real activity cut, not a freezing artifact.
**6. What is the honest calibration?** Dry-sim at SEED = 20260717: G3 head reduction = **+76.05** matches/period, z = **+62.28** ≥ 3σ, with churn 1000 → **709** (291 quits) at LAMBDA = 2.25; G2 control reduction = **−3.48**, z = **−13.50** (not significantly positive — decay is mildly helpful, folk belief holds) with churn 1000 → **1000** (zero quits) at LAMBDA = 1; G1 halves agree, z = **−0.84**. All PASS in order, exit 0; results-dict sha256 **ea060663…83ac59**; two runs byte-identical. The z-values are large because the population is big (N = 1000) and the paired estimator is low-variance — the honest headline is the ~11.6% activity cut and the 29% population churn, not the z magnitude.
**7. What decision does it change?** Stop reaching for rank decay as a retention lever and price it as a churn risk. If leaderboard freshness demands decay, soften the LOSS frame (decay toward a soft floor, show provisional rank, grace-period the recently-absent) so the pain channel never fires, and instrument CHURN-vs-decay-rate rather than the immediate activity bump. Read "we added decay, logins rose, population fell" as the loss-aversion cliff.
**8. How will we know it worked?** The committed stdlib verifier reproduces, under SEED = 20260717, the estimator agreement (G1, halves within noise), the loss-aversion-free control (G2, no significant reduction and zero churn at LAMBDA = 1), and the head (G3, a ≥ 3σ activity reduction with 291/1000 churn at LAMBDA = 2.25) at their SIGMA_GATE = 3.0 bars, with the results-dict sha256 matching ea060663fecf79059bedeb98d43c4f010d2daca6ff273ebf6a97545ddc83ac59 across a deterministic double-run.

## One-line design fix
Treat rank decay as a churn risk, not a retention dial: because a felt rank loss stings ~2.25× an equal gain, decay past a small optimum churns marginal players faster than it grinds them back — so soften the loss frame (soft floor, provisional rank, grace period) or cap the decay rate, and measure churn-vs-decay, not the immediate activity bump.

**Recommendation: sim-ready**
