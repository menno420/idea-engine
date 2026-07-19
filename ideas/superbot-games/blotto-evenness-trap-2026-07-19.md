# PROPOSAL 171 — the Colonel Blotto evenness trap: equal budget does NOT buy equal share. On B battlefields each won by whoever commits more, a lopsided allocator that CONCEDES a minority of fields (allocates zero) and OVERLOADS the rest wins a strict MAJORITY of battlefields against an equal-budget uniform splitter — and holds the majority even while spending up to nearly HALF LESS budget. Spreading evenly is a dominated strategy; concentration beats distribution, and the "fair" even split loses the count.

> **State:** sim-ready
> **Class:** superbot-games · resource-allocation / strategy-budgeting · concentration-vs-distribution dominance + budget-deficit frontier
> **Slot:** round-40 GAME
> **Anchor:** in Colonel Blotto each of B battlefields goes to whoever allocates strictly more; a uniform splitter puts an equal T/B on every field, so a challenger who concedes k fields (0 there) and spreads its budget over the remaining B-k overloads each of them above T/B and wins them — winning B-k > B/2 fields whenever k < B/2, i.e. a strict majority, at equal budget; with a deficit d the overloaded fields still exceed uniform iff k > d*B, so a winning concede-count exists whenever d*B < k < B/2, feasible up to d -> 1/2
> **Target:** sim-lab (VERDICT 184, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Blotto_game@1346038465 · fetched 2026-07-19T13:57:50Z
> **Reference (external, reachable):** Wikipedia, "Blotto game" — fetched live HTTP 200 at revision 1346038465 (permalink https://en.wikipedia.org/w/index.php?title=Blotto_game&oldid=1346038465). The article defines the game as players who "simultaneously distribute limited resources over several objects (battlefields)," with each field won by "the player devoting the most resources to a battlefield" and payoff "equal to the total number of battlefields won," and shows the uniform split (2,2,2) is NOT uniquely optimal — the lopsided (1,2,3) is a co-equilibrium — while the deficit case ("Enemy has a fraction of resources less than 1 ... equilibrium ... depend[s] on that resource level relationship") is exactly the budget-asymmetry frontier this head prices.
> **Verifier (firsthand):** `ideas/superbot-games/blotto_evenness_trap.py` · results-dict sha256 `05afdeffd9f44721fd6e71ee4595a024541b99976176bd30449b043c1755be63`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
On B contested battlefields each won by whoever commits more, an allocator who concedes just under half the fields (zero there) and pours its whole budget over the rest beats an equal-budget uniform splitter in a strict MAJORITY of battlefields — and holds that majority even spending up to ~50% less — so the intuitive "spread your budget evenly / fairly" strategy is dominated by deliberate concentration.

## The folk belief
"Both sides have the same total budget, so an even split across all fronts is the safe, fair, roughly optimal play — equal resources should mean about an equal share of the fields." The first clause is true (equal budget), but the conclusion does not follow: a field is decided by the LOCAL comparison, not the global budget, so a player who refuses to contest a minority of fields can be locally superior everywhere it does contest. Equal global budget and equal field-share are not the same statement; the second does not follow from the first.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Model B battlefields, each worth a value v_i, and two allocators. The uniform splitter U spends its budget T equally: T/B on every field (with T=B, exactly 1.0 each). The challenger R picks a set of k fields to CONCEDE (allocate 0) and spreads its budget over the remaining keep = B-k fields, budget_R/keep each. A field is won by whoever allocates strictly more (a tie splits its value). Because U is flat at T/B, R's only decision is which fields to abandon and how hard to overload the rest.

**Equal budget (budget_R = T = B).** On each overloaded field R commits T/keep = B/(B-k); since k >= 1, keep < B, so B/(B-k) > 1 = U's stake — R wins every overloaded field STRICTLY. R loses the k conceded fields (0 < 1). So R wins exactly keep = B-k fields; that is a strict MAJORITY whenever B-k > B/2, i.e. k < B/2. R can therefore concede up to just under half the fields — abandoning a whole minority front — and still take the majority, with the SAME budget the uniform player spread thin. Evenness converted U's budget into a tie-or-loss on every contested field; concentration converted R's identical budget into a strict win on a majority.

**Budget deficit (budget_R = (1-d)*T).** Now R's overloaded stake is (1-d)*B/(B-k); it beats U iff (1-d)*B/(B-k) > 1 <=> k > d*B. Combined with the majority condition k < B/2, a winning concede-count exists iff d*B < k < B/2 — a nonempty window iff d < 1/2. So R wins the majority of fields while spending up to nearly HALF LESS than U: the "cheaper AND wins" regime, bounded exactly at a one-half budget deficit. As B grows the largest feasible deficit approaches 1/2 (the integer-k granularity gap shrinks like 1/B).

**Heterogeneous values (the shifted world).** When fields carry unequal values, R sharpens the trap by conceding the CHEAPEST fields and overloading the dearest: even at a 40% deficit it captures a majority of total VALUE, because the conceded minority is low-value by construction. (Crossover, not the head: against an opponent that also randomizes or best-responds, Blotto's mixed-strategy equilibria replace the pinned-uniform win — the uniform splitter is not an equilibrium, which is exactly why it loses here; and a deficit past 1/2 closes the window. All disclosed below; the VERIFIED claim is the beat-the-uniform-splitter concentration dominance and its deficit frontier, not an equilibrium-vs-equilibrium result.)

## The formal model (committed constants — sim-lab must reproduce exactly)
- B battlefields ~ randint[8,40] per replication; budget T = B, so uniform allocation = T/B = 1.0 on every field.
- Uniform splitter U: alloc_u[i] = 1.0 for all i.
- Concede-and-overload challenger R: choose a concede-set of size k; alloc_r = 0 on conceded fields and budget_R/(B-k) on the rest.
  - **G1 (equal budget)**: budget_R = T; k = kmax = (B+1)//2 - 1 (the largest concession that still leaves a winning majority); concede-set = a random size-kmax subset.
  - **deficit-demo (d=0.4)**: budget_R = 0.6*T; k drawn uniform in [floor(d*B)+1, (B+1)//2 - 1] (the feasible window d*B < k < B/2); random subset.
  - **G3 (shifted; d=0.4, values v_i ~ U[0.2,5.0])**: budget_R = 0.6*T; k = floor(d*B)+1 (minimum to overload above 1.0); concede-set = the k CHEAPEST fields.
- Field outcome: alloc_r[i] > alloc_u[i] -> R wins v_i; == -> 0.5*v_i; < -> 0. R's share = (value R wins)/(total value).
- G2 identity sweep (deterministic): for B in 8..40, k in 1..B-1, d in {0.00,0.05,...,0.90}, the real game's share must equal the closed-form prediction (keep/B if the overloaded stake exceeds 1.0, 0.5*keep/B if equal, else 0) with zero mismatch.

## Pinned world (committed constants)
SEED=20260717 · Z_GATE=3.0 · battlefields B ~ randint[8,40] · budget T=B (uniform=1.0/field) · G1 300 reps (equal budget, unit values) · deficit-demo 300 reps (d=0.4) · G3 300 reps (d=0.4, values ~ U[0.2,5.0]). Independent streams: G1 Random(SEED+11), deficit-demo Random(SEED+22), G3 Random(SEED+33); G2 is a deterministic full sweep.

## Pre-registered gates (APPROVE iff ALL hold, in order G1 -> G2 -> G3; z_gate = 3.0)
- **G1 evenness-beaten (head)** — across 300 randomized-B contests the equal-budget concede-and-overload allocator's mean battlefield share is strictly above 0.5 at >=3 sigma, rejecting the "equal budget => equal 0.5 share" folk null. Measured: mean_share **0.537637**, z **25.27061**. PASS.
- **G2 concede-arithmetic identity (mechanism anchor)** — over the deterministic (B, k, deficit) sweep the real concede-and-overload game's share equals the closed-form concede-arithmetic prediction with EXACTLY zero mismatches, and the majority-feasibility deficit frontier climbs toward 1/2 as B grows. Measured: **0** mismatches over **14421** checks; deficit frontier B8 **0.37**, B20 **0.44**, B40 **0.47** (-> 1/2). PASS. This proves the whole effect is the concede-overload arithmetic and prices the "cheaper AND still wins" claim.
- **G3 robustness / heterogeneous-value deficit (shifted world)** — under random per-field values AND a 40% budget deficit, the value-targeted concede-and-overload still wins >0.5 of total VALUE at >=3 sigma AND deepens versus the homogeneous equal-budget baseline. Measured: mean_value_share **0.788032** > baseline **0.537637**, z **112.524168**. PASS. (Non-gated corroboration — deficit-demo: at a 40% budget deficit the challenger still wins the field majority, share **0.553794**, z **40.335299**.)

## Pre-registered decision rule
APPROVE (sim-ready confirmed) iff sim-lab reproduces `ideas/superbot-games/blotto_evenness_trap.py` byte-for-byte under SEED=20260717, the results-dict sha256 equals `05afdeffd9f44721fd6e71ee4595a024541b99976176bd30449b043c1755be63` exactly, and G1/G2/G3 all PASS in order (all_pass=true, first_failing_gate=null, exit 0). Any digest mismatch, gate failure, or non-deterministic double-run => REJECT (or QUALIFY on a disclosed environment difference).

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```json
{
  "all_pass": true,
  "deficit_demo": {
    "deficit": 0.4,
    "mean_share": 0.553794,
    "note": "R spends 40% LESS and still wins the field majority",
    "share_sd": 0.0231,
    "z": 40.335299
  },
  "first_failing_gate": null,
  "g1_evenness_beaten": {
    "mean_share": 0.537637,
    "null": "equal budget => equal 0.5 battlefield share",
    "pass": true,
    "share_sd": 0.025796,
    "z": 25.27061
  },
  "g2_concede_arithmetic_identity": {
    "checks": 14421,
    "deficit_frontier_max_d": {
      "20": 0.44,
      "40": 0.47,
      "8": 0.37
    },
    "mismatches": 0,
    "note": "analytic majority frontier d -> 1/2 as B grows (deficit*B < k < B/2)",
    "pass": true
  },
  "g3_robustness_hetero_value_deficit": {
    "baseline_share": 0.537637,
    "deepens": true,
    "deficit": 0.4,
    "mean_value_share": 0.788032,
    "pass": true,
    "share_sd": 0.044336,
    "z": 112.524168
  },
  "gates": [
    {
      "id": "G1",
      "name": "evenness_beaten",
      "pass": true,
      "z": 25.27061
    },
    {
      "id": "G2",
      "mismatches": 0,
      "name": "concede_arithmetic_identity",
      "pass": true
    },
    {
      "id": "G3",
      "name": "robustness_hetero_value_deficit",
      "pass": true,
      "z": 112.524168
    }
  ],
  "head": "blotto_evenness_trap",
  "params": {
    "battlefields_range": [
      8,
      40
    ],
    "budget_rule": "T = B (uniform allocation = 1.0 per field)",
    "deficit": 0.4,
    "deficit_demo_replications": 300,
    "g1_replications": 300,
    "g3_replications": 300,
    "value_dist_shifted": [
      0.2,
      5.0
    ]
  },
  "proposal": 171,
  "seed": 20260717,
  "slot": "round-40 GAME",
  "z_gate": 3.0
}
Results-JSON sha256: 05afdeffd9f44721fd6e71ee4595a024541b99976176bd30449b043c1755be63
```

## Verifier
`ideas/superbot-games/blotto_evenness_trap.py` — stdlib only (`math`, `json`, `hashlib`, `random`). Runs the equal-budget head (G1, 300 randomized-B contests), the deterministic concede-arithmetic identity sweep (G2), a 40%-deficit Monte Carlo demo, and the heterogeneous-value 40%-deficit robustness head (G3, 300 contests). WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture: the results dict carries no digest field; `main()` runs `run()` twice, asserts the two compact-canonical (sorted-keys, 6-dp-rounded) serializations are identical, prints the indent=2 dump, then the `Results-JSON sha256:` line. No JSON is written to disk.

## Reproduce
```
python3 ideas/superbot-games/blotto_evenness_trap.py
```
Expected tail:
```
Results-JSON sha256: 05afdeffd9f44721fd6e71ee4595a024541b99976176bd30449b043c1755be63
```
Exit 0 (all_pass=true); a second invocation is byte-identical.

## Why it matters (competitive game design / strategy budgeting)
Every game that hands a player a fixed budget to spread across contested fronts — RTS army splits, MOBA lane and jungle assignment, tower-defense placement, stat/power-point budgeting, deck resource curves, even ad-auction and campaign spend — is a Colonel Blotto game, and the intuitive "cover everything evenly" heuristic is exactly the dominated strategy. Two design consequences invert intuition: (1) a symmetric budget does NOT guarantee a symmetric outcome — a player who concentrates force wins a majority of fronts against an equal-budget spreader, so "balanced" builds are structurally beaten by committed ones; (2) resource ADVANTAGE is worth less than it looks — the trailing player can still take the majority of fronts while behind by up to nearly half the budget, so a designer who wants leads to feel decisive must break the Blotto structure (raise the tie/overkill cost, add per-field diminishing returns, or make fronts sequential/observable) rather than assume a bigger stockpile settles it.

## Dedup (contrast vs prior lane heads)
- vs **matchmaking-winrate-mirage / mmr-rating-deflation** — those are competitive-rating dynamics (win-rate fixed point; pool-mean drift); this is a single-contest allocation-dominance result with no rating system in play. No shared gate or number.
- vs **single-elim-favorite-collapse / tournament-seeding-bracket-optimality / arcsine-lead-illusion** — bracket/lead order-statistics over match outcomes; this is a within-match resource-split geometry, decided by per-field arithmetic, not tournament structure.
- vs **guild-volunteer-dilemma / raid-coordination-overhead** — those are multi-player coordination/free-riding games; Blotto here is strictly two-sided allocation with no coordination term.
- vs **st-petersburg-cap-collapse / drop-rate-median-gap** — payout-distribution heads; Blotto's payoff is the deterministic count/value of fields won given the two allocations, no heavy tail.
- Crossover honesty: the classic Blotto literature is about MIXED-STRATEGY EQUILIBRIA (both sides randomize); the VERIFIED claim here is the narrower, sharper fact that a uniform splitter — which is NOT an equilibrium — loses the majority to a concede-and-overload opponent at equal or deficit budget, with the equilibrium regime and the past-1/2 deficit disclosed as crossovers, not asserted.

## Model basis (declared model-dependence)
The head rests on an **exact per-field arithmetic identity** (G2: the game's share equals the closed-form concede prediction, 0 mismatches over 14421 cases) plus the majority/deficit inequalities k < B/2 and k > d*B. The SIGN of the result is structural — a uniform splitter loses every overloaded field and wins every conceded one, so it takes at most k < B/2 fields whenever R concedes fewer than half. **Declared modelling choices** (flagged, not hidden): (1) the opponent is a FIXED uniform splitter, not a best-responder — this is the folk strategy the head indicts, and the equilibrium case is the disclosed crossover; (2) ties split value, and the head regime wins strictly (no result rests on tie-breaking); (3) the exact deficit frontier is 1/2 only in the large-B limit — at finite B the integer-k granularity caps it slightly below (B8 0.37, B40 0.47), which G2 measures rather than assumes. Sequential/observable fronts, per-field diminishing returns, and best-responding opponents are named out-of-scope regimes.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | z | Verdict |
|------|------|-----------|----------|---|---------|
| G1 | head (evenness beaten) | mean_share > 0.5 at z >= 3 | 0.537637 | 25.27061 | PASS |
| G2 | mechanism anchor (identity) | mismatches == 0 | 0 / 14421 | n/a | PASS |
| G3 | robustness (shifted, hetero-value deficit) | value-share > 0.5 at z >= 3, deepens | 0.788032 > 0.537637 | 112.524168 | PASS |

## Probe report (v0, self-adversarial)
**1. What is this really?** A concentration-dominance law for fixed-budget contests: a field is decided locally, so conceding a minority of fields and overloading the rest converts an equal (or smaller) budget into a strict majority of fields against a uniform splitter.
**2. What would make it false?** If the concede-and-overload share did NOT exceed 0.5 across contests (G1 — the head is wrong), or if the real game's share did NOT match the concede-arithmetic prediction (G2 — the win is not the arithmetic I claim), or if the value-share collapsed to <=0.5 or failed to deepen under random values plus a deficit (G3 — an artifact of homogeneous unit values). Any of G1/G2/G3 failing => REJECT.
**3. Simplest version that still bites?** SEED=20260717; B=8 fields, equal budgets of 8 each; R concedes 3 fields (0 there) and puts 8/5=1.6 on each of the other 5, beating the uniform 1.0 on all five and winning 5 of 8 fields — a majority — with the identical budget.
**4. What is the counterintuitive core?** Equal budget does NOT buy equal share: spreading your resources evenly is dominated by concentrating them, so the "fair" even split loses the majority of fronts to a lopsided opponent spending the same or up to ~half less.
**5. Where could I be fooling myself?** By choosing a weak opponent — but the uniform split is precisely the intuitive folk optimum this head indicts, and G2's exact identity shows the win is the concede arithmetic, not a tie-break or float artifact; the >=3 sigma results are across randomized boards (and, in G3, randomized values), not one configuration.
**6. Determinism?** SEED=20260717 pinned; `run()` executed twice in-process, compact-canonical serializations asserted byte-identical before hashing; cross-invocation double-run printed identical stdout with sha256 05afdeff...5be63. All dict floats round()-ed to 6 dp; no set/dict-ordering nondeterminism (sort_keys).
**7. Real or toy?** Colonel Blotto is the textbook model for RTS/MOBA lane and army-split decisions, tower-defense placement, stat/power budgeting, and (per the cited article) voting and auction bidding — the uniform-is-dominated result is the documented core, not a toy.
**8. How will we know it worked?** The committed stdlib verifier reproduces, under SEED=20260717, the evenness-beaten head (G1), the concede-arithmetic identity (G2), and the heterogeneous-value deficit robustness head (G3) at Z_GATE=3.0, with the results-dict sha256 matching 05afdeffd9f44721fd6e71ee4595a024541b99976176bd30449b043c1755be63 across a deterministic double-run.

## One-line design fix
If you want a fixed resource budget to be spent evenly (or a stockpile lead to feel decisive), break the Blotto structure — add per-field diminishing returns or an overkill cap, make fronts sequential or observable so committing early can be punished, or reward field VALUE unevenly — otherwise concentration will keep beating distribution and the trailing player will keep stealing the majority of fronts.

**Recommendation: sim-ready**
