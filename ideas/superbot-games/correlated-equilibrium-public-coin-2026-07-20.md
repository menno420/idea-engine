# In the game of Chicken, a public coin that only *suggests* moves - obeyed by choice, binding on no one - pays both players more than the symmetric Nash equilibrium and lifts total welfare above every Nash equilibrium.

> **State:** sim-ready
> **Class:** superbot-games · game theory / mechanism design · correlated equilibrium
> **Target:** sim-lab (VERDICT 224, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Correlated_equilibrium@3cc56b870b48a8977dfccbba41497de9b9dc0549 · fetched 2026-07-20
> **Verifier (firsthand):** stdlib-only, SEED=20260717; results-dict sha256 33e4293…f00fa (see Dry-sim)

## The phenomenon (one line)
Hand two Chicken players a shared public signal that merely *recommends* Dare or Chicken-out - enforceable by no one - and if they choose to obey, both earn 5, beating the 14/3 they get at the symmetric Nash equilibrium, and their combined 10 beats every Nash equilibrium's total.

## The folk belief
"You can't do better than equilibrium without changing the game. A signal nobody is forced to follow is cheap talk: rational players ignore it, so it can't move the outcome. To make both players better off you'd need enforcement, side-payments, or repetition."

## The game-design thesis (reasoned to its fuller form - Q-0254 duty)
The folk belief conflates *binding* with *credible*. Aumann's correlated equilibrium (1974) is the exact counterexample: a mediator - here a public coin drawing one of three cards - privately recommends a move to each player; the distribution is a correlated equilibrium when, conditional on your own recommendation, obeying is a best response given the posterior over the other player's recommendation. No enforcement is needed - obedience is self-enforcing.

In Chicken the three-card device - (C,C), (D,C), (C,D) each with probability 1/3 - never recommends the mutual-crash cell (D,D). When you are told "Dare," you can infer the other player was told "Chicken-out," so daring is strictly best (7 > 6). When you are told "Chicken-out," the other player is equally likely to have been told Dare or Chicken-out, and obeying yields 4 against a deviation's 3.5. Both obedience constraints hold, so the device is a genuine equilibrium - yet it correlates the players *away* from the (D,D) disaster that independent mixing keeps hitting. The dividend is exactly the crash the players can no longer stumble into: each earns 5 instead of 14/3, and the pair earns 10 instead of the best Nash's 28/3.

The design lesson for any competitive system (matchmaking, turn order, resource contention): a cheap, public, non-binding coordinating signal can Pareto-improve a congestion / anti-coordination game without any authority to enforce it - provided the signal's recommendation distribution is incentive-compatible.

## The formal model (committed constants - sim-lab must reproduce exactly)
Game of Chicken, players row and col, actions Dare (D) and Chicken-out (C). Payoffs (row, col):

| | col: Dare | col: Chicken-out |
|---|---|---|
| **row: Dare** | 0, 0 | 7, 2 |
| **row: Chicken-out** | 2, 7 | 6, 6 |

Correlating device μ: a public draw picks one card from {(C,C), (D,C), (C,D)}, each with probability 1/3, and privately tells each player their component. Players may obey or deviate; payoffs are as tabled.

Mixed Nash equilibrium (symmetric): each player Dares with probability q = 1/3, giving 14/3 per player.

## Pinned world (committed constants)
- SEED = 20260717
- Monte-Carlo rounds N = 200000 per condition, one shared loop, RNG = Python `random.Random(20260717)`; per-round call order: `randrange(3)` (device card index into [(C,C),(D,C),(C,D)]), then `random()` (row Dare test vs q=1/3), then `random()` (col Dare test vs q=1/3).
- Robustness band: mutual-reward w in {5, 21/4, 11/2, 23/4, 6} (Fraction-exact), all strictly below the dominance boundary w* = sqrt(39) ≈ 6.2450 at which the mixed NE overtakes the device.
- All equilibrium quantities computed with `fractions.Fraction` (exact).

## Pre-registered gates (sim-ready iff ALL hold, in order)
- **G1 - exact CE validity + payoff [equality / slack >= 0]:** every obedience constraint of the device holds under exact Fraction arithmetic (all slacks >= 0) and the device pays exactly (5, 5).
- **G2 - statistical dominance [higher, >= 3 sigma]:** the Monte-Carlo realized per-player payoff under the device exceeds independent mixed-NE play with z = (mean_device - mean_mixedNE) / se >= 3.0 (expected z ≈ 45).
- **G3 - robustness band [strict >]:** for every w in the band the device remains a valid CE and its per-player payoff strictly exceeds the mixed NE's.
- **G4 - exactly-true agreement [equality]:** closed-form device payoff equals the exhaustive enumeration over the three recommendations equals 5 (Fraction); the per-player gap equals 1/3 and the total-welfare gap equals 2/3, exactly.

## Pre-registered decision rule
sim-ready iff G1 and G2 and G3 and G4 all hold and the in-process double-run digest is identical (determinism). Any gate failing -> not sim-ready.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
{
  "exact": {
    "best_nash_total": "28/3",
    "ce_payoff_col": "5",
    "ce_payoff_row": "5",
    "ce_total_welfare": "10",
    "device_valid_ce": true,
    "mixed_nash_total": "28/3",
    "mixed_ne_dare_prob": "1/3",
    "mixed_ne_payoff": "14/3",
    "obedience_slacks": [
      "1",
      "1/2"
    ],
    "per_player_gap_vs_mixed_ne": "1/3",
    "pure_nash_total": "9",
    "total_welfare_gap_vs_best_nash": "2/3"
  },
  "gates": {
    "G1": true,
    "G2": true,
    "G3": true,
    "G4": true
  },
  "model": {
    "device": "cards (C,C),(D,C),(C,D) each prob 1/3",
    "game": "chicken",
    "payoffs": {
      "CC": "6,6",
      "CD": "2,7",
      "DC": "7,2",
      "DD": "0,0"
    }
  },
  "n": 200000,
  "proposal": "P211-correlated-equilibrium-public-coin-chicken",
  "robustness": [
    {
      "ce_payoff": "14/3",
      "dominates": true,
      "mixed_ne_payoff": "7/2",
      "valid_ce": true,
      "w": "5"
    },
    {
      "ce_payoff": "19/4",
      "dominates": true,
      "mixed_ne_payoff": "56/15",
      "valid_ce": true,
      "w": "21/4"
    },
    {
      "ce_payoff": "29/6",
      "dominates": true,
      "mixed_ne_payoff": "4",
      "valid_ce": true,
      "w": "11/2"
    },
    {
      "ce_payoff": "59/12",
      "dominates": true,
      "mixed_ne_payoff": "56/13",
      "valid_ce": true,
      "w": "23/4"
    },
    {
      "ce_payoff": "5",
      "dominates": true,
      "mixed_ne_payoff": "14/3",
      "valid_ce": true,
      "w": "6"
    }
  ],
  "seed": 20260717,
  "sim_ready": true,
  "statistical": {
    "determinism_in_process": true,
    "mean_device": 4.989885,
    "mean_mixed_ne": 4.66785,
    "var_device": 4.682576,
    "var_mixed_ne": 6.006326,
    "z_score": 44.050568
  }
}
results_sha256=33e42932057eb0ec92c04530b302a1d4cc56314ef9e702099e6d156d9bcf00fa
```
**Disclosed results-dict sha256 = 33e42932057eb0ec92c04530b302a1d4cc56314ef9e702099e6d156d9bcf00fa**

## Verifier
Full verifier committed alongside this doc: `ideas/superbot-games/correlated-equilibrium-public-coin-2026-07-20.py`.
```reproduce
python3 ideas/superbot-games/correlated-equilibrium-public-coin-2026-07-20.py
# expected: results_sha256=33e42932057eb0ec92c04530b302a1d4cc56314ef9e702099e6d156d9bcf00fa  (exit 0)
```

## Why it matters (game design)
Anti-coordination and congestion games (lane contention, matchmaking, turn priority, spawn / resource races) are exactly the shape of Chicken: independent randomization keeps colliding at the worst cell. A public, non-binding coordinating signal - a shared clock, a published queue token, a lobby seed - can move players onto a correlated equilibrium that Pareto-beats independent play, at zero enforcement cost, as long as the recommendation distribution is incentive-compatible. This is the theory under "just add a shared random beacon" as a cheap fix for contention.

## Dedup
Grepped all ideas/ lanes 2026-07-20. Correlated equilibrium is un-built. Distinct from: vickrey-truthful-dominance (dominant-strategy mechanism, not correlation), allpay-rent-dissipation (all-pay auction), voting-power-not-weight (power indices / Banzhaf-Shapley), penney-game (non-transitive sequences), price-of-anarchy-pigou (congestion inefficiency without a coordinating device), blotto-evenness-trap, intransitive-efron-dice, condorcet-*. None model a mediator / correlating device or the CE-vs-Nash payoff gap.

## Model basis (declared model-dependence - the P024 discipline)
Everything here is a claim ABOUT the committed 2x2 Chicken payoff matrix and the specific three-card device - a clean, exactly-solvable model, not an empirical claim about real players. The CE payoffs, the Nash values, and the gaps are exact rational facts of this matrix; the Monte-Carlo gate only confirms that obeying the device empirically realizes the exact mean. The robustness band shows the result is not a knife-edge (it holds across w in [5, sqrt(39))), and the disclosed boundary w* = sqrt(39) is where the mixed NE overtakes - an honest limit, not a hidden failure.

## One-line design fix
When a competitive subsystem behaves like Chicken (players anti-coordinate into a mutual-worst outcome), publish a cheap non-binding recommendation drawn from an incentive-compatible correlated distribution before enforcing anything - it can Pareto-improve both sides for free.

## Probe report (v0, 2026-07-20)
**1. What is this really, in one sentence?** A firsthand, Fraction-exact demonstration that Aumann's three-card correlated equilibrium in Chicken pays each player 5 - beating the symmetric mixed Nash's 14/3 and every Nash equilibrium's total - even though obeying the device is entirely voluntary.

**2. Is the headline claim exactly true under the committed model, or approximately?** Exactly true: the CE payoffs (5,5), the mixed-NE value 14/3, the per-player gap 1/3, and the total-welfare gap 2/3 are all exact rationals of the committed matrix, verified with `fractions.Fraction`; the Monte-Carlo gate only confirms the empirical mean converges to the exact value.

**3. What would make it FALSE / what is the sharpest failure mode?** If any obedience constraint failed (a slack < 0) the device would not be a correlated equilibrium and a rational player would deviate. It does not fail here - all slacks >= 0 - but it WOULD fail outside the band: for mutual reward w >= sqrt(39) ≈ 6.245 the symmetric mixed NE overtakes the device, and for w > 7 the "Dare when told Dare" constraint breaks. Both boundaries are disclosed.

**4. Is it already built here or upstream?** Un-built in this repo (grepped all lanes 2026-07-20). Upstream it is Aumann (1974); the pinned Wikipedia revision gives the same Chicken matrix and three-card device firsthand.

**5. What does the verifier actually prove vs assume?** Proves firsthand: the exact obedience-constraint slacks (>= 0), the exact CE and Nash payoffs, the closed-form-vs-enumeration agreement, the >= 3 sigma Monte-Carlo dominance, and the robustness band. Assumes: the committed payoff matrix and the rationality / obedience model (players best-respond to their posterior).

**6. What is the grounding and is the caveat accurate?** Grounded to the pinned Wikipedia "Correlated equilibrium" revision (sha1 3cc56b8…, 2025-10-01). The page firsthand gives the identical Chicken payoffs (0,0 / 7,2 / 2,7 / 6,6), the (C,C)/(D,C)/(C,D)-each-1/3 device, the Aumann 1974 attribution, and states the CE payoff 5 is "higher than the expected payoff of the mixed strategy Nash equilibrium." Accurate caveat: the page compares the device only to the MIXED Nash (not to the asymmetric pure Nash 7,2 / 2,7), and it uses no "traffic light," "mediator," "social welfare," or "convex hull" wording. This verifier additionally proves the obedience constraints firsthand and adds the total-welfare-vs-every-Nash framing and the robustness band - neither is asserted on the page.

**7. What is the smallest thing sim-lab must reproduce to confirm?** Re-implement the exact-rational block (device validity + payoffs + Nash values) and the seeded Monte-Carlo with the committed RNG protocol, and reproduce results_sha256 byte-for-byte with all four gates holding.

**8. What decision does a sim-ready verdict unblock?** It validates "publish a cheap non-binding correlated signal" as a real, incentive-compatible Pareto-improvement lever for Chicken-shaped contention subsystems - a mechanism-design tool the fleet can reach for.

**Recommendation: sim-ready**
