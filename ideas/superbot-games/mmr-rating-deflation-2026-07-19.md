# PROPOSAL 167 — MMR/Elo rating deflation: a competitive ladder's mean rating is NOT conserved. Every game is a zero-sum transaction (winner +N, loser -N), so rating points can only cross the pool boundary WITH players; newcomers enter underrated at a provisional floor and, after climbing to their true skill, retire carrying those accumulated points OUT — so a strictly zero-sum ladder deflates in the long run, with no change in anyone's true skill, at a rate set by churn x the enter-low/retire-high gap

> **State:** sim-ready
> **Class:** superbot-games · competitive rating / matchmaking economics · zero-sum conservation + churn-driven drift
> **Slot:** round-39 GAME
> **Anchor:** an Elo/MMR game is an equal transaction — the winner gains exactly what the loser loses — so total rating is conserved WITHIN the active pool and can change only when a player joins (injecting their entry rating) or retires (removing their current rating); the long-run mean therefore drifts by (sum of entry ratings - sum of exit ratings)/pool, and the documented enter-low/retire-high asymmetry makes that drift negative (deflation), independent of any game outcome
> **Target:** sim-lab (VERDICT 180, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Elo_rating_system@1364176765 · fetched 2026-07-19T11:01:47Z
> **Reference (external, reachable):** Wikipedia, "Elo rating system" — fetched live HTTP 200 at revision 1364176765 (permalink https://en.wikipedia.org/w/index.php?title=Elo_rating_system&oldid=1364176765); the "Combating deflation" discussion states each game is an equal transaction (winner +N, loser -N) and that players "enter the system as novices with a low rating and retire ... with a high rating," so "a system with strictly equal transactions tends to result in rating deflation."
> **Verifier (firsthand):** `ideas/superbot-games/mmr_rating_deflation.py` · results-dict sha256 `dcf252dd29f271a68a835046ea712256841c39fb657fc04c4f0aa8747e5855db`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
On a competitive ladder where every game moves rating as a zero-sum transaction (winner +delta, loser -delta), the pool's mean rating still deflates over time — because points cross the pool boundary only with players, and newcomers enter underrated at a floor while retirees leave at the higher rating they climbed to, draining the ladder at a rate set by churn x the enter-low/retire-high gap, with nobody's true skill changing.

## The folk belief
"Elo/MMR is zero-sum, so the average rating on the ladder can neither inflate nor deflate — points just move around between players." The first clause is true PER GAME, but it does not bound the mean: a game conserves points only among the CURRENTLY ACTIVE players. Every join injects the entrant's rating into the pool and every retirement removes the leaver's rating; when entrants come in low (a provisional floor) and leavers depart high (climbed to skill), the pool loses points on net each cycle and the mean falls. "Zero-sum per game" and "mean rating is stable" are not the same statement — the second does not follow from the first.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Model a ladder of P players, each with a hidden true skill and a displayed rating. Games are decided by TRUE skill (logistic expected score) but settle DISPLAYED rating by the standard Elo update disp += K*(score - expected): the winner gains exactly K*delta and the loser drops exactly K*delta, so **every game is exactly zero-sum in displayed rating** and the total displayed rating of the active pool is invariant under play. The total can move ONLY at the pool boundary: a **join** adds the entrant's displayed rating, a **retirement** removes the leaver's displayed rating. Hence the exact ledger identity

    Delta(total displayed) = (sum of ratings brought IN by joiners) - (sum of ratings carried OUT by leavers)

with the game term contributing exactly zero. Now apply the documented churn asymmetry (Elo, "Combating deflation"): players **enter as novices at a low provisional floor** and, after enough games, **retire at the higher rating they climbed to**. Each completed enter-climb-retire cycle therefore removes more than it injected — Delta per cycle ~ -(climbed_rating - floor) < 0 — so the pool **deflates**, and the mean-rating drift equals the accumulated (in - out) ledger divided by the pool size. The rate is set by the **churn frequency x the enter-low/retire-high gap**, not by any game result; a deeper underrating (a lower entry floor) drains faster. (Crossover, not the head: flip the asymmetry — entrants **overrated** or leavers **underrated** — and the identical ledger runs the other way as **inflation**; and real ladders deliberately break the drain with rating floors, bonus-point injection, provisional seeding at estimated skill, or seasonal soft resets. All disclosed below; none is the verified claim.)

## The formal model (committed constants — sim-lab must reproduce exactly)
- P players; each true skill ~ Normal(mu, sigma); displayed rating warm-started at true skill (start level is irrelevant — G2 proves the drift is boundary-only).
- Per step: pick two DISTINCT players uniformly; the game result is 1/0 drawn from the TRUE-skill logistic expected(true_a, true_b); update BOTH displayed ratings by d = K*(score_a - expected(disp_a, disp_b)), disp_a += d, disp_b -= d (exactly zero-sum).
- Every `churn_every` steps: among players with games_played >= conv_games, retire one uniformly at random — record its displayed rating OUT — and replace it with a fresh entrant (new true skill ~ Normal(mu, sigma), displayed = floor, games reset), recording `floor` IN.
- Per ladder: mean_drift = (end_total_displayed - start_total_displayed)/P; identity residual = (end_total - start_total) - (ledger_in - ledger_out) (must be ~0 to float precision).
- expected(ra, rb) = 1 / (1 + 10**((rb - ra)/400)).

## Pinned world (committed constants)
SEED=20260717 · Z_GATE=3.0 · R=40 replications · P=60 pool · steps=15000 · conv_games=40 · skill mu=1500 · skill sigma=300. Baseline world: floor=1000, K=32, churn_every=50 (draws `random.Random(SEED+i)`). Shifted world: floor=700, K=24, churn_every=40 (draws `random.Random(SEED+777+i)`).

## Pre-registered gates (APPROVE iff ALL hold, in order G1 -> G2 -> G3; z_gate = 3.0)
- **G1 deflation-real** — across R=40 independent ladders the pool mean displayed-rating drift is strictly negative at >=3 sigma (drift z < -3), rejecting the zero-sum => mean-stable folk null. Measured: mean_drift -498.683032, z_deflation **-78.058838**. PASS.
- **G2 churn-ledger identity (mechanism anchor)** — the pool's total displayed-rating change equals EXACTLY (points in by joiners) - (points out by leavers); play moves zero net points. Max |residual| **0.0** (< 1e-6). PASS. This proves the drift is 100% churn ledger, 0% game outcome.
- **G3 robustness / deeper-floor scaling (shifted world)** — under floor=700 (deeper underrating) plus shifted K=24 and churn_every=40, deflation persists at >=3 sigma AND deepens (shifted drift < baseline drift). Measured: shifted mean_drift -797.745574 < baseline -498.683032, z_deflation **-131.368189**. PASS.

## Pre-registered decision rule
APPROVE (sim-ready confirmed) iff sim-lab reproduces `ideas/superbot-games/mmr_rating_deflation.py` byte-for-byte under SEED=20260717, the results-dict sha256 equals `dcf252dd29f271a68a835046ea712256841c39fb657fc04c4f0aa8747e5855db` exactly, and G1/G2/G3 all PASS in order (all_pass=true, first_failing_gate=null, exit 0). Any digest mismatch, gate failure, or non-deterministic double-run => REJECT (or QUALIFY on a disclosed environment difference).

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```json
{
  "all_pass": true,
  "baseline": {
    "drift_sd": 40.404757,
    "max_identity_residual": 0.0,
    "mean_drift": -498.683032,
    "z_deflation": -78.058838
  },
  "first_failing_gate": null,
  "g1_deflation_real": {
    "null": "zero-sum => mean drift == 0",
    "pass": true,
    "z_deflation": -78.058838
  },
  "g2_churn_ledger_identity": {
    "max_residual": 0.0,
    "pass": true
  },
  "g3_robustness_deeper_floor": {
    "baseline_drift": -498.683032,
    "deepens": true,
    "pass": true,
    "shifted_drift": -797.745574,
    "z_deflation": -131.368189
  },
  "gates": [
    {
      "id": "G1",
      "name": "deflation_real",
      "pass": true,
      "z": -78.058838
    },
    {
      "id": "G2",
      "name": "churn_ledger_identity",
      "pass": true,
      "residual": 0.0
    },
    {
      "id": "G3",
      "name": "robustness_deeper_floor",
      "pass": true,
      "z": -131.368189
    }
  ],
  "head": "mmr_rating_deflation",
  "params": {
    "baseline": {
      "K": 32.0,
      "churn_every": 50,
      "floor": 1000.0
    },
    "conv_games": 40,
    "pool_size": 60,
    "replications": 40,
    "shifted": {
      "K": 24.0,
      "churn_every": 40,
      "floor": 700.0
    },
    "skill_mu": 1500.0,
    "skill_sigma": 300.0,
    "steps": 15000
  },
  "proposal": 167,
  "seed": 20260717,
  "shifted": {
    "drift_sd": 38.406452,
    "max_identity_residual": 0.0,
    "mean_drift": -797.745574,
    "z_deflation": -131.368189
  },
  "slot": "round-39 GAME",
  "z_gate": 3.0
}
Results-JSON sha256: dcf252dd29f271a68a835046ea712256841c39fb657fc04c4f0aa8747e5855db
```

## Verifier
`ideas/superbot-games/mmr_rating_deflation.py` — stdlib only (`math`, `json`, `hashlib`, `random`). Runs R=40 independent ladders per world (baseline + shifted), each 15000 games with zero-sum Elo updates and enter-low/retire-high churn, and records per-ladder mean drift plus the churn-ledger identity residual. WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture: the results dict carries no digest field; `main()` runs `run()` twice, asserts the two compact-canonical (sorted-keys, 6-dp-rounded) serializations are identical, prints the indent=2 dump, then the `Results-JSON sha256:` line. No JSON is written to disk.

## Reproduce
```
python3 ideas/superbot-games/mmr_rating_deflation.py
```
Expected tail:
```
Results-JSON sha256: dcf252dd29f271a68a835046ea712256841c39fb657fc04c4f0aa8747e5855db
```
Exit 0 (all_pass=true); a second invocation is byte-identical.

## Why it matters (competitive game design / matchmaking integrity)
Every ranked ladder communicates skill as a rating number, and players (and designers) read that number as a fixed yardstick — "1500 means the same thing this season as last." It does not: a strictly zero-sum rating system with ordinary player churn drifts, and the documented direction is deflation because populations skew enter-low / retire-high. Two design consequences invert intuition: (1) the average rank is a MANAGED quantity, not a conserved one — a ladder that does nothing will see its mean sag over a season, so ratings are not comparable across time without an anchor; (2) the usual "anti-inflation" instinct is backwards for an open pool — the untended failure mode is deflation, which is exactly why real systems inject bonus points (USCF), seed provisional ratings near estimated skill (Glicko), set rating floors, or soft-reset each season. A designer who wants cross-season comparability has to price the enter-low/retire-high gap and counter it deliberately.

## Dedup (contrast vs prior lane heads)
- vs **matchmaking-winrate-mirage** — that head is the ~50% win-rate FIXED POINT that skill-based matchmaking forces on any player; this head is the drift of the POOL MEAN RATING, a different quantity (win-rate vs rating level) driven by a different mechanism (matchmaking feedback vs boundary churn). No shared gate or number.
- vs **rank-decay-churn-cliff** — that is loss-aversion inverting the rank-decay retention lever (a behavioural response to inactivity penalties); this is a conservation identity plus an entry/exit asymmetry, with no behavioural response modelled.
- vs **single-elim-favorite-collapse / tournament-seeding-bracket-optimality** (bracket luck) and **arcsine-lead-illusion** (lead-time distribution) — those are single-tournament order-statistics results; this is a longitudinal ladder-level drift.
- Crossover honesty: **inflation** is the identical ledger with the sign flipped (entrants overrated or leavers underrated), and the same identity prices any bonus-injection or floor policy; the VERIFIED claim here is the enter-low/retire-high DEFLATION, with inflation and the anti-deflation cures disclosed as crossovers, not asserted.

## Model basis (declared model-dependence — the P024 discipline)
The head rests on an **exact conservation identity** (G2: play moves zero net displayed points, residual 0.0) plus a **documented population asymmetry** (enter-low/retire-high). The SIGN of the drift is structural — deflation whenever leavers exit above where entrants enter — and G2 makes it start-level-independent. The **declared modelling choices** (flagged, not hidden): (1) warm-start displayed=true only fixes the zero point; G2 shows the drift is boundary-only, so the start level does not drive the result. (2) The finite horizon means deflation **self-limits**: as the pool level falls toward the floor, converged players track down with it and the per-cycle drain shrinks, so a long enough run approaches a floor-anchored equilibrium — the verifier measures the ACTIVE deflation over a fixed horizon, and the equilibrium/anti-deflation regime is disclosed as the crossover, not gated. (3) The exact MAGNITUDE depends on (floor, K, churn_every, horizon); the SIGN and the ledger identity do not, and G3 re-derives the sign under a shifted world. Constant-churn, single-pool, no rating floor / bonus injection / provisional seeding — those are the named cures, out of scope here.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | z | Verdict |
|------|------|-----------|----------|---|---------|
| G1 | head (deflation sign) | z <= -3 (drift < 0) | mean_drift -498.683032 | -78.058838 | PASS |
| G2 | mechanism anchor (identity) | max \|residual\| < 1e-6 | residual 0.0 | n/a | PASS |
| G3 | robustness (shifted, deeper floor) | z <= -3 and shifted < baseline | -797.745574 < -498.683032 | -131.368189 | PASS |

## Probe report (v0, self-adversarial)
**1. What is this really?** A conservation-plus-churn law for competitive ratings. Each game is zero-sum in displayed rating, so the pool total moves only at the boundary; enter-low/retire-high churn makes the boundary net-negative, so the mean rating deflates with nobody's true skill changing.
**2. What would make it false?** If the pool mean did NOT drift negative across ladders (G1 — the head is wrong), or if the total-rating change did NOT equal joiners-in minus leavers-out (G2 — the drift is not the churn ledger), or if the sign flipped or vanished under the deeper-floor shift (G3 — an artifact of one floor). Any of G1/G2/G3 failing => REJECT.
**3. Simplest version that still bites?** SEED=20260717; 60-player ladders, entrants seeded 500 points below the mean true skill, retiring after 40 games — the mean displayed rating falls ~499 points over the run purely from churn, while every single game stayed exactly zero-sum.
**4. What is the counterintuitive core?** "Zero-sum per game => the average can't move" is inverted: conservation holds only among active players, and the average is set by who crosses the boundary and at what rating. A perfectly zero-sum ladder still deflates.
**5. Where could I be fooling myself?** The warm start could be suspected of manufacturing the drop, but G2 is an EXACT identity (residual 0.0) showing the entire change is joiners-in minus leavers-out, independent of the start level; and the drift is measured across R=40 independent ladders, so it is not one lucky seed.
**6. Determinism?** SEED=20260717 pinned; `run()` executed twice in-process, compact-canonical serializations asserted byte-identical before hashing; cross-invocation double-run printed identical stdout with sha256 dcf252dd...5855db. All dict floats round()-ed to 6 dp; no set/dict-ordering nondeterminism (sort_keys).
**7. Real or toy?** The mechanism is the textbook chess/USCF/FIDE rating-deflation story (Elo, "Combating deflation"; Glickman's provisional-rating work), the same drift ranked video-game ladders fight with bonus points, floors, and seasonal resets. The model is the correct baseline those cures modify, not a toy.
**8. How will we know it worked?** The committed stdlib verifier reproduces, under SEED=20260717, the deflation head (G1), the churn-ledger identity (G2), and the deeper-floor robustness head (G3) at Z_GATE=3.0, with the results-dict sha256 matching dcf252dd29f271a68a835046ea712256841c39fb657fc04c4f0aa8747e5855db across a deterministic double-run.

## One-line design fix
Treat the ladder's mean rating as a MANAGED quantity, not a conserved one — seed provisional ratings near estimated true skill, inject bonus points or set a rating floor, or soft-reset each season — so the enter-low/retire-high drain is neutralized and ratings stay comparable across time.

**Recommendation: sim-ready**
