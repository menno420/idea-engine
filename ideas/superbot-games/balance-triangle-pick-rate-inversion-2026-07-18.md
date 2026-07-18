# PROPOSAL 135 — the balance-triangle pick-rate inversion: a weighted rock-paper-scissors metagame is a skew-symmetric zero-sum game whose equilibrium plays each unit in proportion to the margin of the matchup it is NOT part of, so buffing one unit can DROP its own pick rate and DOUBLE its counter's while the game value stays 0 — "balance = equal pick rates" is inverted; the fix is inverse-margin weighting, not equalizing usage.

> **State:** sim-ready
> **Class:** superbot-games · competitive-balance design / zero-sum matrix-game equilibrium
> **Anchor:** von Neumann (1928) minimax; skew-symmetric matrix games have value 0 with a symmetric optimum (Gale, Kuhn & Tucker 1950); generalized/weighted rock-paper-scissors mixed equilibria
> **Target:** sim-lab (VERDICT 148, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@787483a · fetched 2026-07-18T13:41:10Z
> **Reference (external, reachable):** [Rock paper scissors — Wikipedia](https://en.wikipedia.org/wiki/Rock_paper_scissors) — verified reachable 2026-07-18 (weighted/unbalanced variants shift the optimal mix off uniform 1/3)
> **Verifier (firsthand):** `ideas/superbot-games/balance_triangle_pick_rate_inversion.py` · results-dict sha256 `92de2d5454c34f274869bc83d302682909b376380c16e60b6afcb12756424a4b`

## The phenomenon (one line)
A three-unit balance triangle (R beats S beats P beats R) is a skew-symmetric zero-sum game; its equilibrium pick rate for each unit is proportional to the winning margin of the matchup it is NOT in, so a buff propagates AROUND the cycle instead of to the buffed unit.

## The folk belief
"Balance means equal usage. If a unit is under-played, buff it and it gets picked more; if pick rates are all near 1/3, the roster is balanced." Designers read pick-rate equality as the definition of balance and patch toward it.

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
Model the metagame as a matrix game over three units in a beat-cycle R>S>P>R, with winning margins **a = margin(R beats S)**, **b = margin(S beats P)**, **c = margin(P beats R)**. The row player's expected match score (on [−1,1], order R,P,S) is the skew-symmetric matrix

    M[R] = [ 0, -c,  a],   M[P] = [ c,  0, -b],   M[S] = [-a,  b,  0]     (M = -Mᵀ).

Because M is skew-symmetric the game value is **0** and the symmetric optimum x* solves **M x* = 0**. Solving the three indifference equations gives

    x*_R : x*_P : x*_S = b : a : c,

so **each unit's equilibrium pick rate is proportional to the margin of the matchup it is NOT part of** — R's share tracks b (the S-vs-P fight), P's tracks a (R-vs-S), S's tracks c (P-vs-R). Start from the symmetric roster a=b=c (uniform 1/3 each) and **buff R by raising a** (R crushes S harder, 0.2→0.4): the new mix is (b:a:c)=(0.2:0.4:0.2) → **x* = (R 0.25, P 0.50, S 0.25)**. R's own pick rate *drops* from 33.3% to 25%, and **P — the unit that beats R — doubles to 50%**. The buff never lands on R: a stronger R suppresses S (R's prey), scarce S makes P (which S beats) safe, so P thrives. Pick-rate response flows around the cycle, and the game value stays 0 — nobody's equilibrium payoff moved.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Three units in cycle R>S>P>R; row payoff = skew-symmetric M(a,b,c) above; value 0.
- Equilibrium mix (closed form): x* = (b, a, c)/(a+b+c), order (R, P, S).
- SKEWED world (R buffed): a=0.4, b=0.2, c=0.2 → x* = (0.25, 0.50, 0.25).
- SYMMETRIC world (placebo): a=b=c=0.2 → x* = (1/3, 1/3, 1/3).
- Monte-Carlo: fix the opponent at a mix, sample its action per trial, average the realized row payoff → an i.i.d. estimate of the expected payoff with a real standard error.

## Pinned world (committed constants)
- SEED = 20260717
- TRIALS = 200000
- SIGMA_GATE = 3.0
- Skewed margins (a, b, c) = (0.4, 0.2, 0.2); symmetric margins = (0.2, 0.2, 0.2)
- Exact anchors: x*_skewed = (0.25, 0.50, 0.25); uniform-meta best-response edge (skewed) = (a−c)/3 = 0.0666667; symmetric-meta exploitability = 0.0 exactly

## Pre-registered gates (APPROVE iff ALL hold, in order G1 → G2 → G3)
- **G1 — equilibrium (indifference).** With the opponent fixed at the closed-form mix x* = (0.25, 0.50, 0.25), each of the row's three pure actions has MC mean payoff within z<3σ of 0 — x* makes the field indifferent, confirming it solves the skew-symmetric game (value 0).
- **G2 — inversion.** In the SKEWED triangle, against the intuitive UNIFORM (1/3-each) meta the best pure response (R) has MC mean payoff > 0 with z=mean/se ≥ 3σ AND matches the exact anchor (a−c)/3 = 0.06667 within z<3σ. "Equal pick rates" is exploitable; balance needs pick rates ∝ the inverse margins (b, a, c), so buffing a raises x*_P not x*_R — the folk reading is reversed.
- **G3 — placebo.** In the SYMMETRIC triangle the exact exploitability of the uniform meta is 0.0 for every action (max|row-vs-uniform| == 0.0 exactly) AND the MC best-action payoff vs uniform is within z<3σ of 0 — the effect vanishes when margins are equal (it is caused by asymmetry, not by the sim).

## Pre-registered decision rule
APPROVE (sim-ready confirmed) iff G1 AND G2 AND G3 all hold in order and the verifier exits 0 with a reproducible results-dict sha256 across a deterministic double-run. Any gate failing ⇒ REJECT/REVISE.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
{
  "all_pass": true,
  "g1_equilibrium": true,
  "g1_indifference_mean_payoff": {
    "P": 0.0003870000000000028,
    "R": 0.0005559999999995368,
    "S": 0.0007189999999969626
  },
  "g1_max_abs_z": 1.3143865915026838,
  "g1_z": {
    "P": 1.226341070122763,
    "R": 1.0143917430473668,
    "S": 1.3143865915026838
  },
  "g2_anchor": 0.06666666666666667,
  "g2_best_action": "R",
  "g2_exact_vs_uniform_skewed": {
    "P": 0.0,
    "R": 0.06666666666666667,
    "S": -0.06666666666666667
  },
  "g2_inversion": true,
  "g2_mc_payoff_R_vs_uniform": 0.0672109999998512,
  "g2_z_anchor": 0.9748529872924236,
  "g2_z_exist": 120.3689727128182,
  "g3_exact_vs_uniform_symmetric": {
    "P": 0.0,
    "R": 0.0,
    "S": 0.0
  },
  "g3_max_abs_exact_exploit": 0.0,
  "g3_mc_payoff_R_vs_uniform_sym": 0.0002170000000000004,
  "g3_placebo": true,
  "g3_z": 0.5939951919337725,
  "proposal": 135,
  "seed": 20260717,
  "sigma_gate": 3.0,
  "skewed_margins": {
    "a_R_beats_S": 0.4,
    "b_S_beats_P": 0.2,
    "c_P_beats_R": 0.2
  },
  "symmetric_margins": {
    "a": 0.2,
    "b": 0.2,
    "c": 0.2
  },
  "trials": 200000,
  "x_star_skewed": {
    "P": 0.5,
    "R": 0.25,
    "S": 0.25
  },
  "x_star_symmetric": {
    "P": 0.3333333333333333,
    "R": 0.3333333333333333,
    "S": 0.3333333333333333
  }
}
Results-JSON sha256: 92de2d5454c34f274869bc83d302682909b376380c16e60b6afcb12756424a4b
G1 equilibrium  : PASS (max|z|=1.314)
G2 inversion    : PASS (R vs uniform=+0.06721, z_exist=+120.37, z_anchor=+0.975)
G3 placebo      : PASS (max|exact|=0.0e+00, z=+0.594)
```
Results-dict sha256: `92de2d5454c34f274869bc83d302682909b376380c16e60b6afcb12756424a4b` (deterministic double-run, exit 0 both times).

## Verifier
`ideas/superbot-games/balance_triangle_pick_rate_inversion.py` — stdlib only (`random, math, json, hashlib`). Builds the skew-symmetric payoff matrix and the closed-form equilibrium mix x*=(b,a,c)/(a+b+c), Monte-Carlos the row's expected payoff against a fixed opponent mix (indifference at x*, exploitability vs uniform), computes the three pre-registered z-gates against the exact anchors, and emits the whole results dict (no self-referential sha field; the compact canonical serialization's sha256 IS the disclosed digest).

## Reproduce
```
python3 ideas/superbot-games/balance_triangle_pick_rate_inversion.py
```
Expected: prints the results JSON, `Results-JSON sha256: 92de2d5454c34f274869bc83d302682909b376380c16e60b6afcb12756424a4b`, three `PASS` lines, exit 0.

## Why it matters (game design)
Pick rate is a lagging, self-referential signal, not a balance target. Because the equilibrium usage of a unit tracks a matchup it is not even in, chasing "equal pick rates" with buffs pushes the metagame around the cycle and can *widen* the very imbalance it was meant to fix — a buff to an under-played unit may inflate the usage of that unit's counter instead. The correct lever is the matchup margins (a, b, c): balance the *win margins*, and the equilibrium pick rates follow as x* ∝ (b, a, c); do not equalize usage directly. Read pick-rate data as an equilibrium response to the margin matrix, and price a balance patch by its effect on margins, not on the headline usage bars.

## Dedup
- Distinct from all prior game-lane cards: shop-reroll (optimal stopping), streak-shield, energy-cap (renewal overflow), matchmaking-winrate-mirage (Elo compression under SBMM), compounding-reward-inequality (log-normal Gini), PRD proc compression, snipe-clearing-leak (auction microstructure), guild-volunteer-dilemma (N-player public-goods *provision*, symmetric, non-zero-sum), pity-anticipation-collapse, rubber-band controller, single-elim favorite-collapse (tournament order statistics). None model a **zero-sum matrix-game / minimax equilibrium** or **pick-rate ∝ inverse margin**.
- Distinct from fleet-lane intransitivity heads: Penney's game (fair-coin sequence race — a different intransitive object, no pick-rate/matrix equilibrium) and Braess selfish-routing (congestion/Wardrop). This is the FIRST zero-sum matrix-game / competitive-balance-equilibrium card in the game lane.

## Model basis (declared model-dependence — the P024 discipline)
The result is exact for the three-unit skew-symmetric matrix game: value 0, symmetric optimum x* solving Mx=0, x*∝(b,a,c). The *direction* (pick rate tracks the off-unit margin; a buff flows around the cycle; uniform is exploitable unless margins are equal) holds for any strictly intransitive three-strategy zero-sum triangle with positive margins. The specific magnitudes (R→0.25, P→0.50) are pinned to (a,b,c)=(0.4,0.2,0.2). Real rosters have >3 units, ties/mirror matchups, and non-zero-sum payoffs; the triangle is the minimal object that exhibits the inversion, and adding transitive strength (a globally stronger unit) only layers a dominance term on top of this cyclic core.

## Probe report (v0, 2026-07-18)

**1. What is this really?** A competitive-balance identity: a three-unit beat-cycle with winning margins (a,b,c) is a skew-symmetric zero-sum game whose value is 0 and whose equilibrium mix is **x* = (b, a, c)/(a+b+c)** — each unit's pick rate is proportional to the margin of the matchup it is NOT in. Buffing R's margin a from the symmetric 0.2 to **0.4** moves x* from (1/3,1/3,1/3) to **(R 0.25, P 0.50, S 0.25)**: R's own share falls, P's doubles.
**2. What would make it false?** If the MC payoffs at x* were NOT all ~0 (G1 fails — x* is not the equilibrium / the sim is wrong), or if the uniform meta were NOT exploitable in the skewed triangle so the best response earned ≤0 or ≠(a−c)/3 (G2 fails — "equal pick rates" would already be balanced), or if the symmetric triangle showed nonzero exploitability (G3 fails — the effect would not be caused by margin asymmetry). Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED=20260717; a single buff to one matchup margin (a: 0.2→0.4) in a 3-unit triangle relocates 50% of equilibrium play onto P — the unit that beats the buffed R — with a one-line closed form x*∝(b,a,c) and no tuning.
**4. What is the counterintuitive core?** "Buff a unit to see it played more; equal pick rates mean balance" is inverted. Equilibrium pick rate tracks the *off-unit* margin, so a buff to R **drops R to 25% and doubles its counter P to 50%**, and the game value never budges from 0 — usage is an equilibrium response that flows around the cycle, not a dial the buffed unit controls.
**5. Where could I be fooling myself?** Assuming pick-rate equality is the equilibrium, or that a buff's usage effect lands on the buffed unit. Neither holds: uniform 1/3 is the equilibrium ONLY when a=b=c (G3's placebo — exploitability exactly 0 there), and off-symmetry the response is on the off-unit margin (G2 shows uniform is exploitable by (a−c)/3=**0.0667** in the skewed world). G1's indifference gate is the control that x*=(0.25,0.50,0.25) genuinely zeroes every action's payoff, i.e. it IS the equilibrium.
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 indifference max|z|=**1.314** < 3σ (all three actions' MC payoff ≈ 0 at x*); G2 inversion z_exist=**+120.37** ≥ 3σ with R-vs-uniform payoff **+0.06721** matching anchor (a−c)/3=**0.066667** (z_anchor=**+0.975** < 3σ); G3 placebo max|exact|=**0.0** exactly with symmetric MC z=**+0.594** < 3σ; all PASS, exit 0; results-dict sha256 **92de2d54…24a4b**; two runs byte-identical. G1/G3 z's are small because those legs confirm an exact-zero equilibrium property; G2's z is large because uniform is genuinely, measurably exploitable off-symmetry.
**7. What decision does it change?** Stop patching toward equal pick rates. Tune the matchup *margins* (a,b,c) — the equilibrium usage x*∝(b,a,c) follows — and read a proposed buff by its effect on the margin matrix and the resulting equilibrium, not on the headline usage bars. Expect a buff's usage effect to appear on the buffed unit's *counter*, one step around the cycle.
**8. How will we know it worked?** The committed stdlib verifier reproduces the indifference-at-x* gate (G1), the uniform-meta exploitability inversion in the skewed triangle (G2, R edge (a−c)/3), and the symmetric-triangle placebo (G3, exploitability exactly 0) at their 3σ bars under SEED=20260717, with the results-dict sha256 matching 92de2d5454c34f274869bc83d302682909b376380c16e60b6afcb12756424a4b.

## One-line design fix
Balance the *margins*, not the usage bars: in a beat-cycle the equilibrium pick rate is x*∝(inverse margins), so a buff flows to a unit's counter — read pick rates as an equilibrium response to the margin matrix, never as the target.

**Recommendation: sim-ready**
