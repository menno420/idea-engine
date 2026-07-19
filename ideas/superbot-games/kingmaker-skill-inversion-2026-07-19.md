# PROPOSAL 183 — the kingmaker skill-inversion: adding a player who can no longer win, but who still decides the winner, flips the sign of skill — under a spiteful kingmaker the stronger contender becomes the underdog

> **State:** sim-ready
> **Class:** superbot-games · multiplayer game design / social-choice incentive · elimination-order + spite targeting
> **Slot:** round-43 GAME
> **Anchor:** the kingmaker scenario — a player who can no longer win still has the power to decide which of the remaining players wins; a spiteful kingmaker eliminates the standings leader, and because standings track skill, raw skill turns from asset to liability
> **Target:** sim-lab (VERDICT 196, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Kingmaker_scenario@1356902639 · fetched 2026-07-19T20:31:48Z
> **Reference (external, reachable):** Wikipedia, "Kingmaker scenario" — fetched live HTTP 200 at revision 1356902639 (permalink https://en.wikipedia.org/w/index.php?title=Kingmaker_scenario&oldid=1356902639); the article states that in a multiplayer game "a player who is unable to win has the capacity to determine which player among others will win," which is exactly the elimination-into-decider role this head quantifies.
> **Verifier (firsthand):** `ideas/superbot-games/kingmaker_skill_inversion.py` · results-dict sha256 `d928732259d7f54185db3ad5219322166bc2abd9f005667d2b1bd5873451432d`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
In a 3-player game where the lowest qualifier drops out but still chooses who wins, a spiteful kingmaker who eliminates the standings leader makes raw skill anti-correlate with winning: the stronger of the two remaining contenders — usually the leader — wins only ~0.19 of the time, below the ~0.70 it earns when the final is decided by skill.

## The folk belief
"Be the best player and you win more; a rival who has already lost can't hurt you." Both clauses fail here. A rival who can no longer win is precisely the one free to act on spite, and because standings track skill, the strongest surviving contender is the most likely target — so being the best raises, not lowers, your chance of being knocked out. "Skill predicts winning" holds in the ordinary game and inverts the moment an out-of-contention player gets to pick the loser.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Three players draw hidden skills s ~ Normal(mu, sigma). A qualifying phase gives each a noisy score q_i = s_i + Normal(0, qnoise); the lowest q_i is eliminated and becomes the **kingmaker** — a player who can no longer win but still acts. The two survivors are the **contenders**; the higher-q contender is the **leader**, the other the **trailer**. The final resolves one of two ways:

- **Skill-decided (no kingmaker influence).** The contenders play; contender a beats b with the logistic probability 1/(1+exp(-(s_a - s_b)/scale)). The stronger-skill contender wins more than half the time — skill is an asset. (G1.)
- **Spiteful kingmaker.** The eliminated player, unable to win, acts on spite and knocks out the **leader**, handing the game to the trailer. Because q tracks s, the leader is usually the stronger-skill contender — so the stronger contender is the one eliminated, and its win rate drops below half. Skill is now a liability. (G2.)

The counterintuitive core is the **sign flip**: the same quantity (true skill) that predicts winning in the ordinary game predicts *losing* once an out-of-contention player gets to pick the loser. This is not a rigged edge case — it survives when the kingmaker acts spitefully only part of the time (G3, spite=0.6) and under a wider skill spread, because any positive spite weight pulls the stronger-contender win rate toward the anti-leader value. (Crossover, not the head: a *random* kingmaker who picks uniformly leaves skill's sign intact — restores ~0.5 plus the residual skill edge — and a *pro-leader* kingmaker would amplify skill; the verified claim is specifically the SPITEFUL / anti-leader kingmaker, with random and pro-leader disclosed as crossovers, not asserted.)

## The formal model (committed constants — sim-lab must reproduce exactly)
- Per game: draw s0, s1, s2 ~ Normal(mu, sigma) (three sequential rng.gauss draws), then q_i = s_i + rng.gauss(0, qnoise) for i in 0,1,2.
- kingmaker = argmin_i q_i; the other two are contenders a, b in ascending index order; leader = the contender with the higher q, trailer = the other; stronger = the contender with the higher s.
- Draw u = rng.random(); if u < spite: winner = trailer (spiteful kingmaker eliminates the leader). Else: winner = a with probability 1/(1+exp(-(s_a - s_b)/scale)) via a second rng.random() draw, else b.
- Per condition: stronger_win_rate = (games where winner == stronger) / n_games.
- z_vs_half(p, n) = (p - 0.5) / sqrt(0.25 / n).

## Pinned world (committed constants)
SEED=20260717 · Z_GATE=3.0 · N_GAMES=200000 per condition. Baseline / G1: mu=0, sigma=1.0, qnoise=0.5, scale=1.0, spite=0.0, stream random.Random(SEED+11). Spiteful / G2: same skill params, spite=1.0, stream random.Random(SEED+22). Shifted / G3: mu=0, sigma=1.5, qnoise=0.7, scale=1.0, spite=0.6, stream random.Random(SEED+33).

## Pre-registered gates (APPROVE iff ALL hold, in order G1 -> G2 -> G3; z_gate = 3.0)
- **G1 skill-is-real (no kingmaker)** — with a skill-decided final the stronger contender wins above half at >=3 sigma, establishing that skill is an asset in the ordinary game. Measured: stronger_win_rate 0.695125, z_vs_half **174.525106**. PASS.
- **G2 the inversion (spiteful kingmaker)** — with a fully spiteful kingmaker (spite=1.0) that eliminates the leader, the stronger contender wins below half at >=3 sigma; skill's sign is flipped. Measured: stronger_win_rate 0.193235, z_vs_half **-274.378957**. PASS.
- **G3 robustness (shifted skills, partial spite)** — under a wider skill spread (sigma=1.5, qnoise=0.7) and a kingmaker who acts spitefully only 60% of the time, the inversion persists at >=3 sigma AND stays below the baseline rate. Measured: stronger_win_rate 0.410205 < 0.5, z_vs_half **-80.31509**, below baseline 0.695125 (deepens=true). PASS.

## Pre-registered decision rule
APPROVE (sim-ready confirmed) iff sim-lab reproduces `ideas/superbot-games/kingmaker_skill_inversion.py` byte-for-byte under SEED=20260717, the results-dict sha256 equals `d928732259d7f54185db3ad5219322166bc2abd9f005667d2b1bd5873451432d` exactly, and G1/G2/G3 all PASS in order (all_pass=true, first_failing_gate=null, exit 0). Any digest mismatch, gate failure, or non-deterministic double-run => REJECT (or QUALIFY on a disclosed environment difference).

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```json
{
  "all_pass": true,
  "first_failing_gate": null,
  "g1_skill_is_real": {
    "null": "no kingmaker => stronger contender wins > 0.5",
    "pass": true,
    "stronger_win_rate": 0.695125,
    "z_vs_half": 174.525106
  },
  "g2_inversion": {
    "null": "spiteful kingmaker => stronger contender wins < 0.5",
    "pass": true,
    "stronger_win_rate": 0.193235,
    "z_vs_half": -274.378957
  },
  "g3_robustness": {
    "baseline_win_rate": 0.695125,
    "deepens": true,
    "pass": true,
    "stronger_win_rate": 0.410205,
    "z_vs_half": -80.31509
  },
  "gates": [
    {"id": "G1", "name": "skill_is_real_no_kingmaker", "pass": true, "z": 174.525106},
    {"id": "G2", "name": "inversion_spiteful_kingmaker", "pass": true, "z": -274.378957},
    {"id": "G3", "name": "robustness_shifted_partial_spite", "pass": true, "z": -80.31509}
  ],
  "head": "kingmaker_skill_inversion",
  "n_games": 200000,
  "params": {
    "baseline": {"mu": 0.0, "qnoise": 0.5, "scale": 1.0, "sigma": 1.0, "spite": 0.0},
    "shifted": {"mu": 0.0, "qnoise": 0.7, "scale": 1.0, "sigma": 1.5, "spite": 0.6},
    "spiteful": {"mu": 0.0, "qnoise": 0.5, "scale": 1.0, "sigma": 1.0, "spite": 1.0}
  },
  "proposal": 183,
  "seed": 20260717,
  "slot": "round-43 GAME",
  "z_gate": 3.0
}
Results-JSON sha256: d928732259d7f54185db3ad5219322166bc2abd9f005667d2b1bd5873451432d
```

## Verifier
`ideas/superbot-games/kingmaker_skill_inversion.py` — stdlib only (`hashlib`, `json`, `math`, `random`). Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: the results dict carries no digest field; `main()` runs `run()` twice in-process, asserts byte-identical compact-canonical (`sort_keys=True, separators=(",",":")`) serializations, prints the pretty (`indent=2, sort_keys=True`) dump, then `Results-JSON sha256: <hex>` over the compact-canonical form. Nothing is written to disk. Three conditions (baseline/spiteful/shifted) each draw N_GAMES=200000 i.i.d. 3-player games from independent streams.

## Reproduce
```
python3 ideas/superbot-games/kingmaker_skill_inversion.py
```
Expect `"all_pass": true`, `"first_failing_gate": null`, and `Results-JSON sha256: d928732259d7f54185db3ad5219322166bc2abd9f005667d2b1bd5873451432d` on every invocation (byte-identical on a second run).

## Why it matters
Multiplayer and free-for-all designers reason about skill as monotone: reward the best play and the best players rise. The kingmaker scenario breaks that monotonicity — the moment a player is out of contention but still acts, an anti-leader motive (spite, grudge, "deny the winner") makes the strongest surviving player the likeliest to be eliminated, so skill anti-predicts winning. Two consequences invert intuition: (1) leaderboards and MMR computed from free-for-all formats with live, targetable elimination can systematically UNDER-rate strong players, because their skill draws targeting; (2) the fix is structural — hide standings until the end, make elimination non-targetable (chance- or rules-based), or reward the eventual winner's eliminator — not "add more skill." A bot trained to maximize visible-standing dominance in such a format is training itself into the crosshairs.

## Dedup (contrast vs prior lane heads)
- Disclosed search: `git grep -il kingmaker` across `ideas/` returns ZERO hits — no kingmaker head exists in either lane. Nearest neighbours below.
- vs **mmr-rating-deflation / matchmaking-winrate-mirage** — longitudinal rating-system population artifacts (pool drift, win-rate fixed point) across many games; this is a single-game elimination-order incentive that flips skill's sign, with no rating system modelled.
- vs **single-elim-favorite-collapse / tournament-seeding-bracket-optimality** — bracket/seeding luck removing a favourite by chance; here the favourite is removed on PURPOSE by an out-of-contention decider, and the measured quantity is the SIGN of the skill->win-rate relationship, not bracket variance.
- vs **pie-rule-opening-trap** — a 2-player side-selection fold (min(f, 1-f)); this is a 3-player elimination-plus-spite structure with a third, non-winning actor.
- vs **rubber-band-controller-instability** — a catch-up mechanic that compresses skill gaps continuously; the kingmaker is a discrete, adversarial elimination of the leader, not a feedback gain.

## Model basis (declared model-dependence — the P024 discipline)
The head rests on two structural facts: (a) noisy skill-based qualifying makes the standings leader usually the stronger-skill contender (positive rank correlation), and (b) an anti-leader kingmaker maps "leader" to "loser." Their composition flips skill's sign whenever spite weight is positive and the leader–skill correlation is positive. Declared modelling choices (flagged, not hidden): the qualifying noise qnoise sets how tightly standings track skill — larger qnoise weakens the leader–skill link and shrinks the inversion (never reverses it while positive); the logistic scale sets the baseline G1 edge; spite sets how far toward the anti-leader value G2/G3 travel. The SIGN of the effect (skill inverts under a spiteful kingmaker) is structural; the MAGNITUDE depends on (sigma, qnoise, scale, spite), and G3 re-derives the sign under a shifted (sigma, qnoise, spite). A random or pro-leader kingmaker is the named crossover, out of scope here.

## Gate power + margin ledger
| Gate | Statistic | Measured | Null | z | Verdict |
|------|-----------|----------|------|-----|---------|
| G1 | stronger-win (skill-decided) vs 0.5 | 0.695125 | 0.5 | 174.525106 | PASS |
| G2 | stronger-win (spiteful) vs 0.5 | 0.193235 | 0.5 | -274.378957 | PASS |
| G3 | stronger-win (shifted, spite 0.6) vs 0.5 | 0.410205 | 0.5 | -80.31509 | PASS |

All gates clear z_gate=3.0 by one-to-two orders of magnitude at N=200000; the head is not marginal.

## Probe report (v0, self-adversarial)
**1. What is this really?** A sign-flip of skill caused by an out-of-contention decider. A player who can no longer win still eliminates someone; if it targets the leader, and standings track skill, the strongest survivor is the likeliest casualty, so skill predicts losing.
**2. What would make it false?** If the stronger contender did NOT win > 0.5 under a skill-decided final (G1 — no baseline edge to invert), or did NOT fall below 0.5 under a fully spiteful kingmaker (G2 — no inversion), or if the sign vanished under the shifted-spread partial-spite world (G3 — an artifact of full spite or one distribution). Any of G1/G2/G3 failing => REJECT.
**3. Simplest version that still bites?** SEED=20260717; three N(0,1) skills, a noisy qualifier, lowest out. Skill-decided, the stronger survivor wins 0.695125; hand the elimination to a spiteful kingmaker and it wins 0.193235 — the same skill advantage, inverted, with nothing else changed.
**4. What is the counterintuitive core?** "Being the best player helps you win" reverses: once a loser gets to pick who loses, being the best marks you as the target. The stronger contender goes from ~0.20 above even to ~0.31 below it.
**5. Where could I be fooling myself?** The spiteful kingmaker is defined to hit the leader, so one might call G2 rigged — but the head is precisely that this documented behaviour inverts SKILL, and G3 shows it needs neither full spite (0.6 suffices) nor the baseline spread; a random kingmaker (disclosed crossover) leaves skill's sign intact, so the inversion is a property of anti-leader targeting, not of merely adding a third player.
**6. Determinism?** SEED=20260717 pinned; three independent streams (SEED+11 / +22 / +33); `run()` executed twice in-process, compact-canonical serializations asserted byte-identical before hashing; cross-invocation double-run printed identical stdout with sha256 d928732259d7f54185db3ad5219322166bc2abd9f005667d2b1bd5873451432d. All floats round()-ed to 6 dp; sort_keys throughout, no set/dict-ordering nondeterminism.
**7. Real or toy?** The kingmaker scenario is a named, documented failure mode of multiplayer game design (Wikipedia "Kingmaker scenario"; widely discussed in board-game and multiplayer-balance design). The model is the minimal elimination-plus-spite structure that produces it, not a contrived toy.
**8. How will we know it worked?** A verdict session re-runs the stdlib verifier under SEED=20260717 and confirms all_pass=true, first_failing_gate=null, and the results-dict sha256 equals d928732259d7f54185db3ad5219322166bc2abd9f005667d2b1bd5873451432d byte-for-byte; any gate fail or digest mismatch is a REJECT.

## One-line design fix
Deny the kingmaker a target: hide live standings, make elimination non-targetable (chance- or rules-based rather than chosen), or pay out on final placement so an out-of-contention player has no lever to hand the game away — otherwise the strongest visible player is the one who gets knocked out.

**Recommendation: sim-ready**
