# PROPOSAL 175 — The pie/swap rule inverts the first-move edge: a game's strongest opening becomes its worst move, because the second player simply swaps into it

> **State:** sim-ready
> **Class:** game design / combinatorial-game incentive design
> **Slot:** round-41 GAME
> **Anchor:** the pie rule (a.k.a. swap rule) — the responder may take over the mover's position instead of replying
> **Target:** sim-lab (VERDICT 188, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Pie_rule@681de3e5074ec4c7b50709ef45fb421ee7a26cdb · fetched 2026-07-19T15:56:14Z
> **Reference (external, reachable):** https://en.wikipedia.org/w/index.php?title=Pie_rule&oldid=1200819498 — HTTP 200, permalink (oldid 1200819498)
> **Verifier (firsthand):** `ideas/superbot-games/pie_rule_opening_trap.py` · results-dict sha256 `72950442cc7509423256f28470c2281c9f79de3b601611b9feb931d083e8cb08`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)

Under the pie / swap rule, the second player may swap sides in lieu of replying, so a first player who plays the strongest opening hands that strength straight to the opponent — the realized first-mover win probability from an opening `o` is `min(f(o), 1 − f(o))`, minimized exactly where the raw edge `f(o)` is largest.

## The folk belief

"A first-move advantage is an advantage: with the initiative you should press it — play the strongest opening you have." Designers add the swap rule to reduce first-move advantage and reason about it as a mild, roughly symmetric correction.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Let `f(o)` be the mover's win probability from opening `o` under optimal continuation with no swap. A genuine first-move edge means the best openings have `f(o) > 0.5`. Under the swap rule the responder, facing the position the opening created, chooses the better of the two sides: reply normally (mover keeps win prob `f`) or swap (mover keeps `1 − f`), picking whichever is worse for the mover. So the mover's realized win probability is `min(f, 1 − f)`.

This is not a mild symmetric correction — it is a fold around `f = 0.5`. The function `min(f, 1−f)` is maximized (at 0.5) exactly where the opening is balanced, and falls as the opening gets stronger. The strongest opening (largest `f`) is therefore the worst choice: it yields realized win prob `1 − f`, below 0.5. The rational first mover deliberately plays the most balanced opening it can find, and the game converges to a coin-flip regardless of how large the underlying structural edge was. The punchline: adding the swap rule doesn't merely shrink the first-move edge — it turns "press your advantage" into a losing heuristic and makes deliberate weakness optimal.

## The formal model (committed constants — sim-lab must reproduce exactly)

Each condition draws `N_GAMES = 200000` i.i.d. games. A game under opening `o` with rule `pie ∈ {False, True}` is won by the first mover with probability `realized_p(f, pie) = f` if `pie` is False else `min(f, 1 − f)`; the outcome is `Bernoulli(realized_p)`. Openings come from a committed catalogue of `f`-values. `strongest = max(catalogue)`; `most_balanced = argmin |f − 0.5|`.

## Pinned world (committed constants)

- `SEED = 20260717`, `Z_GATE = 3.0`.
- Baseline catalogue `BASE_OPENINGS = [0.50, 0.60, 0.70, 0.80, 0.90]` (G1, G2).
- Shifted catalogue `SHIFT_OPENINGS = [0.50, 0.65, 0.78, 0.88, 0.95]` (G3 robustness).
- Independent streams `random.Random(SEED + 11 / +22 / +33)` for G1 / G2 / G3.
- `N_GAMES = 200000` per condition.

## Pre-registered gates (APPROVE iff ALL hold, in order G1 -> G2 -> G3; z_gate = 3.0)

- **G1 — the edge is real without the rule.** Greedy-strongest opening (`f = 0.90`), no swap: win rate `0.900505` > 0.5, `z_vs_half = 598.381968` ≥ 3.0. PASS.
- **G2 — the trap.** Greedy-strongest opening (`f = 0.90`) UNDER the swap rule: realized first-mover win rate `0.10111` < 0.5, `z_vs_half = −591.72081` ≤ −3.0. The strongest opening is now a losing move. PASS.
- **G3 — balanced play dominates + fairness restored (shifted world).** In the shifted catalogue, balanced play (`f = 0.50`, rate `0.50116`) beats naive-strong play (`f = 0.95`, rate `0.04946`) by `gap_mean = 0.4517`, `z_gap = 370.907761` ≥ 3.0; and `|0.50116 − 0.5| ≤ 0.02` (within-2pt fair). PASS.

## Pre-registered decision rule

APPROVE iff `all_pass == true` (G1 ∧ G2 ∧ G3, evaluated in order) and the reproduced results-dict sha256 equals `72950442cc7509423256f28470c2281c9f79de3b601611b9feb931d083e8cb08` byte-for-byte. Any gate fail, or any digest mismatch, is a REJECT; `first_failing_gate` names the earliest failure.

## Dry-sim results (SEED=20260717, verbatim stdout of the verifier)

```json
{
  "all_pass": true,
  "base_openings": [
    0.5,
    0.6,
    0.7,
    0.8,
    0.9
  ],
  "first_failing_gate": null,
  "g1": {
    "n": 200000,
    "opening_f": 0.9,
    "pass": true,
    "rule": "no-pie",
    "strategy": "greedy-strongest",
    "win_rate": 0.900505,
    "z_vs_half": 598.381968
  },
  "g2": {
    "n": 200000,
    "opening_f": 0.9,
    "pass": true,
    "rule": "pie",
    "strategy": "naive-greedy-strongest",
    "win_rate": 0.10111,
    "z_vs_half": -591.72081
  },
  "g3": {
    "gap_mean": 0.4517,
    "naive_f": 0.95,
    "naive_rate": 0.04946,
    "opt_f": 0.5,
    "opt_rate": 0.50116,
    "opt_within_2pct_of_fair": true,
    "pass": true,
    "rule": "pie",
    "shift_openings": [
      0.5,
      0.65,
      0.78,
      0.88,
      0.95
    ],
    "z_gap": 370.907761
  },
  "gates": [
    {
      "gate": "G1",
      "name": "first-move edge exists (no pie rule)",
      "pass": true
    },
    {
      "gate": "G2",
      "name": "strongest opening is losing under pie rule",
      "pass": true
    },
    {
      "gate": "G3",
      "name": "balanced dominates + restores fairness (shifted world)",
      "pass": true
    }
  ],
  "head": "Under the pie/swap rule realized first-mover win prob = min(f, 1-f), so the strongest opening becomes the worst move: the first-move edge (G1) inverts below 0.5 for naive-strong play (G2) while balanced play dominates and restores a fair game (G3).",
  "n_games": 200000,
  "proposal": 175,
  "seed": 20260717,
  "slot": "round-41 GAME",
  "z_gate": 3.0
}
Results-JSON sha256: 72950442cc7509423256f28470c2281c9f79de3b601611b9feb931d083e8cb08
```

## Verifier

`ideas/superbot-games/pie_rule_opening_trap.py` — stdlib only (`hashlib`, `json`, `math`, `random`). Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: the results dict carries no digest field; `main()` runs `run()` twice in-process, asserts byte-identical compact-canonical (`sort_keys=True, separators=(",",":")`) serializations, prints the pretty (`indent=2, sort_keys=True`) dump, then `Results-JSON sha256: <hex>` over the compact-canonical form. Nothing is written to disk.

## Reproduce

```
python3 ideas/superbot-games/pie_rule_opening_trap.py
```
Expect `"all_pass": true`, `"first_failing_gate": null`, and `Results-JSON sha256: 72950442cc7509423256f28470c2281c9f79de3b601611b9feb931d083e8cb08` on every invocation.

## Why it matters

Every game that ships a swap/pie rule — Hex, many abstract-strategy and asymmetric-draft games, and any "auction then play" format — silently changes what "good opening prep" means. A bot or player trained to maximize `f(o)` (press the edge) is not merely suboptimal under the rule; it is actively losing, because it maximizes exactly the quantity the responder exploits. The design lever is quantifiable: publish the opening whose `f` is closest to 0.5, not the one with the highest `f`, and the game is fair by construction.

## Dedup (contrast vs prior lane heads)

- **penney-game-responder-edge-decay / Penney's game (fleet):** non-transitive sequence selection — the responder picks a dominating sequence. Here there is no non-transitivity; the responder picks a side of a fixed position, and the mechanism is the fold `min(f, 1−f)`, not intransitivity.
- **tournament-seeding-bracket-optimality / single-elim-favorite-collapse:** bracket/seeding luck across many matches; this is a single-position side-selection incentive.
- **matchmaking-winrate-mirage / mmr-rating-deflation:** rating-system artifacts across a population; unrelated to the swap incentive.

No pie/swap-rule head exists in either lane.

## Model basis (declared model-dependence)

The head is a deterministic identity of the swap rule (`min(f, 1−f)`) plus i.i.d. Bernoulli sampling; it assumes (a) the responder plays the swap optimally (takes the better side), and (b) `f(o)` is well-defined per opening. Both are the standard pie-rule assumptions. The magnitudes depend on the committed catalogue; the direction (strongest = worst under the rule) is catalogue-independent for any catalogue with a member `f > 0.5`, which G3's shifted catalogue confirms.

## Gate power + margin ledger

| Gate | Statistic | Measured | Null | z | Margin over z_gate=3.0 |
|------|-----------|----------|------|-----|------------------------|
| G1 | win rate (no pie) vs 0.5 | 0.900505 | 0.5 | 598.381968 | ~199x |
| G2 | win rate (pie, naive-strong) vs 0.5 | 0.10111 | 0.5 | −591.72081 | ~197x |
| G3 | opt−naive gap (pie, shifted) vs 0 | 0.4517 | 0.0 | 370.907761 | ~124x |

All gates clear z_gate by two orders of magnitude at N=200000; the head is not marginal.

## Probe report (v0, self-adversarial)

**1.** *Is `min(f, 1−f)` really optimal responder play?* Yes by construction: the responder faces a position worth `f` to the mover and picks the side worth less to the mover, i.e. `min(f, 1−f)`. A weaker responder only raises the mover's realized rate, which weakens the trap — so G2 models the trap at its genuine (optimal-swap) strength.

**2.** *Is the effect an artifact of the specific f-values?* No. G3 re-runs on a different catalogue `[0.50,0.65,0.78,0.88,0.95]` and the ordering (balanced ≫ strong under the rule) holds by ≥3σ. The direction holds for any catalogue containing an `f > 0.5`.

**3.** *Does it collide with Penney's game?* No — Penney is intransitive sequence choice; this is a side-selection fold. Disclosed in Dedup.

**4.** *Is the grounding source specific to the head?* The Wikipedia "Pie rule" article documents the swap mechanic and notes the first player is motivated to make a move that is not too strong — i.e. the balanced-opening incentive that is the head. Grounding pinned at content hash `681de3e5…` / oldid 1200819498, HTTP 200.

**5.** *Could a real game's `f(o)` be coarse so no near-0.5 opening exists?* Then the mover picks the catalogue member closest to 0.5 and realized rate is `min(f*, 1−f*)` — still ≤ 0.5 and still maximized at the most-balanced available opening. The prescription (pick the most balanced opening) is unchanged; only the achievable fairness floor moves.

**6.** *Is Bernoulli independence realistic?* Games are modeled as independent given the opening's `f`; correlation across games would change variance (hence z) but not the mean rates the gates test. At N=200000 the z-margins (~124–199x) absorb large variance inflation.

**7.** *Is `all_pass` gameable by construction?* The three gates test three different directions (edge>0.5, trap<0.5, gap>0 on a distinct catalogue); no single degenerate parameter satisfies all three trivially. A verdict session reproduces the digest to confirm the exact constants.

**8.** *Crossovers with economics/auction lanes?* The pie rule is a fair-division primitive ("I cut, you choose"); the incentive to make a balanced cut is the same fold. That crossover strengthens the grounding, but the head is scoped to game openings and disclosed here.

## One-line design fix

Ship the swap rule and tell players/bots to open with the opening whose no-swap win probability is closest to 0.5 — not the highest — because under the rule `min(f, 1−f)` makes the strongest opening the losing one.

**Recommendation: sim-ready**
