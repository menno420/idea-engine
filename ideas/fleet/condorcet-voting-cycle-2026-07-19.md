# PROPOSAL 168 — Condorcet's paradox: rational voters, an irrational majority

> **State:** sim-ready
> **Class:** social-choice paradox
> **Slot:** round-39 UNRELATED
> **Anchor:** rational parts, irrational whole
> **Target:** sim-lab (VERDICT 181, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Condorcet_paradox@1360635422 · fetched 2026-07-19T11:53:11Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Condorcet_method
> **Verifier (firsthand):** `ideas/fleet/condorcet_voting_cycle.py` — Results-JSON sha256 `70de2ab46cf482130fa35b051f579d72215efa757dfcf7b5f60e56d85fc08fbe`
> 📊 Model: Claude Opus · high · proposal/idea-generation

## The phenomenon (one line)
Feed an electorate whose every member holds a fully rational, transitive ranking of the candidates, and the group's own pairwise-majority preference can still cycle A>B>C>A — with 3 candidates under impartial culture that happens in ~8.7% of electorates, and the share climbs steeply as candidates are added.

## The folk belief
If every voter is individually rational (transitive), a simple majority over each pair must yield a consistent group ranking with a clear winner. It feels like consistency should aggregate — that a population of coherent individuals cannot compose into an incoherent whole.

## The mechanism (reasoned, Q-0254 duty)
Majority preference is built pairwise, and here is the reasoned-out core: each pairwise majority is computed on a DIFFERENT sub-electorate. The A-vs-B verdict is decided by the split of voters who rank A above B; the B-vs-C verdict by a different split; the C-vs-A verdict by a third. Nothing ties these three independent majorities together, so nothing forces them to be mutually consistent. Under impartial culture the six strict rankings of 3 candidates are equiprobable. Line them up and two of the six configurations form cycles — the three rotations of A>B>C and the three rotations of its reverse — and those are exactly the electorates in which no candidate wins all of its pairwise majorities, i.e. no Condorcet winner and a top cycle instead. Because those cyclic configurations carry fixed positive probability, a fixed positive fraction of random electorates land in a cycle. Now add candidates: each new candidate multiplies the number of pairwise majorities that must ALL line up for a single winner to exist, and every added constraint is another chance for the majorities to disagree, so the no-winner rate rises monotonically toward 1. The individual voters never stop being transitive; the intransitivity is a property that emerges only in the aggregate, from the pairwise construction itself.

## The formal model (committed constants)
m candidates; n=101 voters (odd, so every pairwise majority is strict — no ties); each voter draws an independent uniform strict ranking (impartial culture). "No Condorcet winner" = no candidate wins all m-1 of its pairwise majorities. Monte-Carlo estimates the no-winner rate over many independent electorates. Robustness variant: rankings drawn by Plackett–Luce with weights 1.00/0.85/0.72 (a mild popularity tilt) instead of uniform, to check that cycles are not an artifact of perfect symmetry.

## Pinned world (committed constants)
SEED=20260717; z_gate=3.0; n_voters=101; primary m=3 N=40,000; scaling m∈{3,4,5,7} N=10,000 each; robustness m=3 N=20,000; documented reference rate m=3,n=101 = 8.690% (asymptotic 8.77%).

## Pre-registered gates (G1→G2→G3, z_gate=3.0)
- **G1 — head (cycles exist):** impartial culture, m=3, n=101 voters, N=40,000 elections — the share with no Condorcet winner is >=3 sigma above zero; rejects the folk belief that rational individuals compose into a consistent group ranking.
- **G2a — documented magnitude:** the measured m=3 no-Condorcet-winner rate lands within 3 sigma of the documented impartial-culture value 8.690% (source n=101 row).
- **G2b — monotone in candidate count:** the rate strictly increases across m=3<4<5<7 (n=101), each successive step >=3 sigma, matching the documented candidate-scaling trend.
- **G3 — robustness under a shifted distribution:** under a mild popularity tilt (Plackett–Luce weights 1.00/0.85/0.72), cyclic majorities persist >=3 sigma above zero — the paradox is not an artifact of perfect symmetry.

## Pre-registered decision rule
sim-ready iff G1 ∧ G2a ∧ G2b ∧ G3 all pass; otherwise revise. The shipped verifier's `all_pass` field is exactly this conjunction (G1 ∧ G2a ∧ G2b ∧ G3), so a green `all_pass=true` and the decision rule are the same statement.

## Dry-sim results
```json
{
  "all_pass": true,
  "gates": {
    "G1_head_cycles_exist": true,
    "G2a_matches_documented_rate": true,
    "G2b_monotone_in_candidates": true,
    "G3_robust_under_tilt": true
  },
  "meta": {
    "doc_asymptotic_m3": 0.0877,
    "doc_m3_n101": 0.0869,
    "n_voters": 101,
    "seed": 20260717,
    "z_gate": 3.0
  },
  "monotone_step_z": [
    19.391074,
    11.951024,
    18.627769
  ],
  "primary_m3": {
    "n_trials": 40000,
    "no_condorcet_winner": 3451,
    "rate": 0.086275,
    "z_vs_documented": -0.443753,
    "z_vs_zero": 61.456062
  },
  "robustness_tilt_m3": {
    "n_trials": 20000,
    "no_condorcet_winner": 445,
    "rate": 0.02225,
    "weights": [
      1.0,
      0.85,
      0.72
    ],
    "z_vs_zero": 21.333696
  },
  "scaling": {
    "3": {
      "n_trials": 10000,
      "no_condorcet_winner": 867,
      "rate": 0.0867
    },
    "4": {
      "n_trials": 10000,
      "no_condorcet_winner": 1789,
      "rate": 0.1789
    },
    "5": {
      "n_trials": 10000,
      "no_condorcet_winner": 2479,
      "rate": 0.2479
    },
    "7": {
      "n_trials": 10000,
      "no_condorcet_winner": 3685,
      "rate": 0.3685
    }
  }
}
Results-JSON sha256: 70de2ab46cf482130fa35b051f579d72215efa757dfcf7b5f60e56d85fc08fbe
```

## Verifier
`ideas/fleet/condorcet_voting_cycle.py` — stdlib only (`math`, `json`, `hashlib`, `random`), seeded at SEED=20260717. `main()` runs `run()` twice in-process and asserts the two compact-canonical (sorted-keys, 6-dp-rounded) serializations are byte-identical before hashing; the digest is the compact-canonical results dict's OWN sha256 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: the dict carries no digest field, and nothing is written to disk — the digest appears only on stdout after the indent=2 dump).

## Reproduce
```
python3 ideas/fleet/condorcet_voting_cycle.py
```
Prints the results JSON then the `Results-JSON sha256:` line; deterministic across invocations (a second run is byte-identical). Exit 0 with `all_pass=true`.

## Why it matters
Collective rationality is not the sum of individual rationality: a group of perfectly transitive individuals can hold a genuinely cyclic majority preference with no winner at all. Any pairwise-majority aggregation — ranked ballots, A/B bake-offs, head-to-head tournaments, committee votes, model-vs-model preference comparisons — can therefore surface a stable-looking but actually intransitive group ordering, and because each added option multiplies the pairwise constraints that must line up, the risk grows steeply with the number of options on the table.

## Dedup (contrast vs prior lane heads)
- vs **`ideas/fleet/condorcet-jury-correlation-floor-2026-07-18.md`** (the Condorcet Jury Theorem) — that head is a correlated-agent ACCURACY ceiling (how the probability of a correct majority verdict saturates below 1 once voters' errors are correlated). This head shares Condorcet's name but is the opposite quantity: not the accuracy of a majority, but the very EXISTENCE of a consistent majority preference. Different mechanism (accuracy saturation vs pairwise intransitivity), different gate family.
- vs **`ideas/superbot-games/balance-triangle-pick-rate-inversion-2026-07-18.md`** (RPS zero-sum matrix) — that is intransitivity baked into a FIXED payoff matrix (rock<paper<scissors) driving pick-rate inversion; here intransitivity is EMERGENT, arising from aggregating transitive individual rankings, not assumed in a payoff structure.
- vs **`ideas/fleet/penney-game-responder-edge-decay-2026-07-13.md`** (intransitive coin sequences) — that is a fixed non-transitive dominance among coin-flip patterns; this head is the paradox of cyclic MAJORITY PREFERENCE (no Condorcet winner) produced by independent transitive voters. Distinct mechanism and domain.

## Model basis (P024 discipline)
Impartial-culture Monte-Carlo with NO fitted parameters — every voter draws an independent uniform strict ranking, and the no-winner rate is measured, not tuned. The reference rate 8.690% is the source's published n=101 impartial-culture value (a documented quantity, not a fitted one), and G2a gates the finite-n rate actually simulated rather than the asymptotic 8.77% limit.

## Gate power + margin ledger
| Gate | quantity | observed | threshold | margin |
|------|----------|----------|-----------|--------|
| G1 | m=3 no-winner z_vs_zero | 61.456062 | z >= 3.0 | 58.456062 |
| G2a | \|z_vs_documented\| (vs 8.690%) | 0.443753 | \|z\| < 3.0 | 2.556247 |
| G2b | min monotone step z (m=3<4<5<7) | 11.951024 | z >= 3.0 | 8.951024 |
| G3 | robustness tilt z_vs_zero | 21.333696 | z >= 3.0 | 18.333696 |

## Probe report (v0, self-adversarial)
**1. Is "no Condorcet winner" the same as a full 3-cycle?** For m=3 they coincide (no winner ⇒ a top cycle); for m≥4 the verifier gates the documented "no Condorcet winner" quantity, which is exactly what the source measures.
**2. Could pairwise ties inflate the count?** No — n=101 is odd, so every pairwise majority is strict; ties are impossible by construction.
**3. Does the mild tilt secretly still allow a guaranteed winner?** No — weights 1.00/0.85/0.72 keep all three rankings live; G3 measures, not assumes, that cycles persist.
**4. Is the 8.690% target cherry-picked?** It is the source's own n=101 impartial-culture row; the asymptotic 8.77% is disclosed as the large-n limit, and G2a gates the finite-n value actually simulated.
**5. Why not gate m=4,5,7 against absolute documented numbers?** The source's scaling table uses 25 voters while the verifier uses 101, so only the monotone trend is gated, not the absolute values — disclosed.
**6. Is determinism real?** A fresh random.Random(SEED) drives every draw; the harness runs the trial function twice in-process and asserts byte-identical canonical JSON; the digest reproduces cross-invocation.
**7. Does this collide with the committed Condorcet Jury head?** No — the Jury Theorem head is a correlated-accuracy ceiling; this is the paradox of cyclic majority preference (no Condorcet winner). Distinct mechanism, disclosed in Dedup.
**8. What breaks the effect?** Single-peaked / spatial preferences (Black's theorem) collapse the cycle rate toward zero; disclosed as a non-gated crossover, not claimed as robustness.

## One-line design fix
When a pairwise-majority aggregate must yield a decision, detect the cycle explicitly (check whether a Condorcet winner exists) and fall back to a documented tie-break — e.g. a Copeland or Schulze rule — rather than trusting that a consistent winner exists.

**Recommendation: sim-ready**
