# The treatment that wins in every subgroup and loses overall: a pooled success rate is a SIZE-WEIGHTED mean of its stratum rates, so when the allocation is confounded with the stratum baseline, treatment A can beat B in EVERY subgroup (0.931 vs 0.867 small, 0.730 vs 0.688 large) yet LOSE the pool (0.780 vs 0.826) — the reversal is a step function with a single pinned cliff at x\*=184 A-cases-in-the-hard-stratum, and the one folk repair (just compare the pooled numbers) picks the WRONG treatment while direct standardization restores A at the exact price of one recorded covariate

> **State:** sim-ready
> **Class:** fleet (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain
> slot, round 17 CLOSER; a SEVENTEENTH fleet-external domain: STATISTICS / CAUSAL
> INFERENCE — Simpson's (the aggregation / reversal) paradox, the exact reversal of a
> pooled point estimate under a confounded stratum allocation, disjoint from the sixteen
> prior occupants — social choice (P017), congestion routing (P024), tournament seeding
> (P028), pattern races (P032), optimal stopping (P036), spatial self-organization (P040),
> queue discipline (P044), stochastic ratchets (P048), occupancy & collection (P052),
> random incidence (P056), repeated-game reciprocity (P060), information cascades (P064),
> two-sided matching (P068), group testing / screening design (P072), algebraic error
> detection (P076), correlation design under shared randomness (P080) — and deliberately
> NOT adjacent to the last three unrelated slots' domains: no permutation cycle, no
> joint-vs-marginal probability and no shared random source (vs P080 — that head COUPLES
> binary success EVENTS through one permutation's cycle skeleton and the object is a joint
> probability; here nothing is random, the object is a deterministic POOLED RATE that
> reverses sign under confounded weights); no codes, no check maps and no typo census (vs
> P076); no prevalence prior, no pooled tests and no cost curve (vs P072 — that head priced
> a STOCHASTIC screening economy; here there is no test and no prevalence). Domain-switch
> note (decide-and-flag): the dispatch spec named IRV/social-choice as primary and the
> transit inspection paradox as fallback, but BOTH were already spent — IRV monotonicity is
> P017 (`ideas/fleet/irv-monotonicity-close-races-2026-07-13.md`) and the inspection paradox
> is P056 (`ideas/fleet/inspection-paradox-wait-inflation-2026-07-14.md`); the rotation
> counts DISTINCT domains, so this slice serves the fresh SEVENTEENTH one.)
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing
> is the manager's per Q-0260, this repo never edits sim-lab files)
> **Grounding:** https://github.com/menno420/idea-engine@b119a624431e40dab6abeec7d3da5c2cb13a9674 · fetched 2026-07-16T15:17:03Z
> (the dedup-sweep HEAD — the ONLY read this head takes; this is a pure statistics /
> causal-inference mechanism with NO external repo surface. HONEST SCOPE: no fleet/product
> repo is read or claimed; the head is grounded FIRSTHAND in the reasoning itself + the
> canonical Charig et al. (1986) kidney-stone reversal (BMJ 292:879, "Comparison of
> treatment of renal calculi by open surgery…"), a WITNESS table cited-not-cloned; every
> model constant below is pinned in this file and the DECISION arms are exact SEEDLESS
> integer/Fraction arithmetic with zero repo/network/RNG reads at verdict time — the
> P028/P032/P036/P076 fully-exact seedless-census precedent, no Arm R, no seed baton
> consumed, next free block stays 20261730.)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under the deliberate lane
> rotation (rule 3, "COMPLETELY UNRELATED domains — I want those too"); round 17 opened at
> fleet backlogs (P081 #448 → V094 REJECT), served venture (P082 #450 → V095 REJECT) and
> game mechanics (P083 #453 → V096 REJECT), so this head is the round-17 UNRELATED CLOSER.
> Slot spacing history P068, P072, P076, P080 → P084 (spacing 4) confirms the placement.

**Placement note (decide-and-flag):** this fleet-external pure-mechanism head lives in
`ideas/fleet/` per the `check_sections` carve-out for cross-cutting heads (roster-derived
sections — inventing one ad hoc reds `check_sections.py`) — flagged rather than silently
squatting, exactly as PROPOSALs 017 through 080 did.

## The folk belief

"If a treatment is better in every subgroup, it is better overall. A rate is a rate: if A
cures a higher fraction of small-stone patients than B AND a higher fraction of large-stone
patients than B, then A cures a higher fraction of patients, full stop — you can add up the
subgroups." This is the instinct behind every dashboard that reports a pooled conversion
rate and every A/B readout that declares a winner from two lumped totals: that a
directional effect seen in each stratum survives aggregation, so you may collapse the strata
and compare the pooled numbers. The instinct has one load-bearing half: that the pooled rate
is an ORDER-PRESERVING summary of the stratum rates — that collapsing cannot flip the sign.
It is false in an exactly measurable way whenever the subgroup ALLOCATION is correlated with
the subgroup BASELINE (the confounder): the pooled rate is not a rate you can compare
directly, it is a SIZE-WEIGHTED average of the stratum rates, and the weights belong to the
allocation, not the treatment. A treatment that is uniformly better but is administered
disproportionately in the HARD stratum carries the hard stratum's low baseline into its own
pooled number, and the uniformly-worse treatment that happens to sit in the EASY stratum
inherits the easy baseline — so the pool can rank them backwards while every subgroup ranks
them correctly. The classic kidney-stone table (Charig et al. 1986) makes the gap exact.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Pin the canonical witness. Two treatments, A (open surgery) and B (percutaneous
nephrolithotomy); two strata by stone size, S (small) and L (large); each cell a
(successes, total) pair, all integers, all committed:

- A·S = 81/87 (0.9310), A·L = 192/263 (0.7300); pooled A = 273/350 = **39/50 = 0.7800**.
- B·S = 234/270 (0.8667), B·L = 55/80 (0.6875); pooled B = **289/350 ≈ 0.8257**.

**T1 — the REVERSAL (R1).** A beats B in BOTH strata: 81/87 > 234/270 (small, gap ≈ 0.064)
AND 192/263 > 55/80 (large, gap ≈ 0.042). Yet pooled, B beats A: 289/350 > 39/50, by exactly
289/350 − 39/50 = 289/350 − 273/350 = **16/350 ≈ 0.0457**. The folk conjunction "A wins each
stratum ⇒ A wins the pool" is FALSE on the pinned table — the uniformly-better treatment
loses the aggregate.

**T2 — the PIVOT is the ALLOCATION, not the treatment (R2).** The pool is
`(σ_S + σ_L)/(n_S + n_L)` = the n-weighted mean of the stratum rates. Stratum baselines
(both treatments combined): base_S = 315/357 ≈ 0.8824 (small is EASY), base_L = 247/343 ≈
0.7201 (large is HARD). The allocation is confounded with the baseline: A puts **263/350 =
75.1%** of its cases in the HARD stratum, B puts only **80/350 = 22.9%** there (B is 77.1%
in the EASY stratum). A's pooled number is dragged toward the hard baseline it is
over-exposed to; B's is lifted by the easy baseline it is over-exposed to. The clean pivot
proof: evaluate A under B's SIZE-MIX (A's own stratum rates, B's stratum weights) —
`(81/87)·(270/350) + (192/263)·(80/350) ≈ 0.8851 > 0.8257` — A now wins the pool. Only the
weights changed, so the reversal lives ENTIRELY in the allocation; the treatment ranking
never moved.

**T3 — the CLIFF (R3).** Hold A's stratum rates fixed and sweep x = the number of A's 350
cases assigned to the HARD (large) stratum, x ∈ {0..350}. Then
`pooled_A(x) = [ (81/87)·(350 − x) + (192/263)·x ] / 350`, exact in `Fraction`. Because
81/87 > 192/263, `pooled_A(x)` is STRICTLY DECREASING in x, so it crosses the fixed
`pooled_B = 289/350` exactly ONCE — a single-threshold STEP FUNCTION, not a gradual slide.
The cliff is at **x\* = 184**: for x < 184 the uniformly-better A also wins the pool; at
x ≥ 184 the confounded allocation flips the pool to B. The pinned real table sits at x = 263,
well PAST the cliff — which is why the published table reverses. (Boundary, pinned: at
x = 183 pooled_A > pooled_B; at x = 184 pooled_A < pooled_B.)

**T4 — the priced REPAIR (R4).** Direct standardization removes the confounder: reweight
BOTH treatments' stratum rates to a COMMON stone-size distribution (the pooled marginal:
N_S = 87 + 270 = 357 small, N_L = 263 + 80 = 343 large, N = 700), so the comparison holds
the allocation fixed and lets only the treatment vary. Standardized A =
`(81/87)·(357/700) + (192/263)·(343/700)` = **634983/762700 ≈ 0.8325**; standardized B =
`(234/270)·(357/700) + (55/80)·(343/700)` = **6231/8000 ≈ 0.7789**. A > B — the paradox
VANISHES and the true (uniformly-better) ordering is restored. The direction is
WEIGHT-INVARIANT here: because A > B in EVERY stratum, standardizing to A's mix, B's mix,
50/50, or the pooled mix all give A > B (a collapsibility fact — when the effect has the
same sign in every stratum, no positive weighting can flip the adjusted comparison). **The
price** is not free: the repair REQUIRES having RECORDED the confounder (stone size) — with
only the pooled 273/350 vs 289/350 in hand you cannot recover the truth, and the naive
comparison picks the WRONG treatment (B). The transferable cost: one covariate recorded and
standardized-upon; the transferable audit: never rank two pooled rates without checking
whether the grouping variable is allocated evenly across them.

Every registered numeral above was produced live this session by the drafting script
(scratchpad `draft_p084.py`, stdlib-only, seedless): **25/25 checks PASS, exit 0**, exact on
every stratum rate, the pool, the pivot, the cliff x\* = 184, and both standardized rates,
byte-identical across two process runs.

## Pinned model (committed constants — all integers, all pinned)

- **The table (Charig et al. 1986, verbatim, (successes, total)):** A·S = (81, 87),
  A·L = (192, 263), B·S = (234, 270), B·L = (55, 80). Per-treatment total 350 each; grand
  total 700.
- **Stratum rates (exact Fractions):** A·S = 81/87, A·L = 192/263, B·S = 234/270 = 13/15,
  B·L = 55/80 = 11/16. **Pooled:** A = 273/350 = 39/50, B = 289/350. **Baselines:**
  base_S = 315/357 = 15/17, base_L = 247/343.
- **Allocation shares:** share_A(hard) = 263/350, share_B(hard) = 80/350 = 8/35;
  A@Bmix = (81/87)·(270/350) + (192/263)·(80/350).
- **Cliff sweep:** pooled_A(x) = [ (81/87)·(350 − x) + (192/263)·x ] / 350 over x ∈ {0..350};
  strictly decreasing; single crossing of 289/350 at **x\* = 184** (x=183 above, x=184 below).
- **Standardization weights (common pooled marginal):** N_S = 357, N_L = 343, N = 700;
  std_A = (81/87)·(357/700) + (192/263)·(343/700) = 634983/762700; std_B = (234/270)·(357/700)
  + (55/80)·(343/700) = 6231/8000; std_A > std_B, weight-invariant over {A-mix, B-mix, 50/50,
  pool}.
- **Arm A (DECISION, seedless):** the reversal, the pivot, the cliff sweep, the
  standardization — all exact integer/Fraction, byte-identical across process runs, ZERO
  RNG/seeds/floats in any decision leg (floats appear only as reporting-side ≈ annotations).
- **Arm B (twin, seedless, INDEPENDENTLY-WRITTEN):** re-derive the pool and the winner by
  raw integer success-count comparison (cross-multiplication, no `Fraction`), recompute the
  cliff by a from-scratch integer bisection, and recompute std_A/std_B by a common-denominator
  method — must equal Arm A through the typed contacts C1–C3 below.
- **No Arm R:** the head is fully deterministic; there is no stochastic leg, no seed, and no
  seed-baton consumption (next free block stays 20261730).
- **Typed must-equal contacts:** **C1** — Arm-B pooled winner (raw counts) == Arm-A pooled
  winner (Fraction): B pooled with pooled_A = 39/50 < pooled_B = 289/350, and A wins BOTH
  strata by cross-multiplication (81·270 > 234·87; 192·80 > 55·263). **C2** — Arm-B integer
  bisection cliff == Arm-A sweep cliff == 184, with the x=183/x=184 boundary agreeing.
  **C3** — Arm-B common-denominator std_A/std_B == Arm-A Fraction values (634983/762700 and
  6231/8000) and std_A > std_B under all four pinned weightings.
- **Runtime disclosure:** the whole battery (four gates + the 351-point cliff sweep + the
  weight-invariance loop) is ≤ 10⁴ exact-arithmetic operations — well under a second; every
  decision leg is deterministic.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "the collapse-and-compare folk rule is wrong as doctrine wherever the grouping
  variable is confounded with the outcome baseline: a treatment can be uniformly better across
  every subgroup and still lose the pooled comparison; the reversal is an exact size-weighting
  effect with a single pinned cliff; the naive pooled comparison picks the wrong treatment;
  and the standardization repair restores the truth at the exact price of one recorded
  covariate": **(R1, the reversal)** A > B in BOTH strata (81/87 > 234/270 AND 192/263 >
  55/80) while pooled B > pooled A (289/350 > 39/50) by exactly 16/350; **(R2, the pivot)**
  the pool is the n-weighted mean, A loads the hard stratum (263/350) vs B (80/350), and A
  under B's size-mix wins the pool (≈ 0.8851 > 0.8257) — the reversal lives entirely in the
  allocation; **(R3, the cliff)** pooled_A(x) is strictly decreasing with a single crossing of
  289/350 at x\* = 184, the real table at x = 263 past it; **(R4, the repair)** direct
  standardization gives std_A = 634983/762700 > std_B = 6231/8000, weight-invariant over the
  four pinned mixes, while the naive pooled comparison alone picks B (the WRONG treatment).
  (Checked FIRST because the costly direction is fleet-wide: every pooled dashboard metric,
  every A/B winner read off two lumped totals, and every "it's better in each cohort so ship
  it" call silently asserts that the grouping is balanced across arms — which is exactly what
  a confounded rollout, a skewed sampling frame, or an uneven cohort mix violates.)
- **INVALID** (controls misbehaving — report, no ruling): any F1–F5 gate failure below.
- **APPROVE** — "the folk rule holds: a uniform subgroup ordering always survives
  aggregation": arithmetically EXCLUDED by the pinned witness — the table exhibits a strict
  reversal (289/350 > 39/50 with A winning both strata), so a uniform-ordering-implies-pooled-
  ordering claim is false by one exhibited counterexample; mutually exclusive with REJECT.
- **NULL** — anything else; pre-registered axes: **estimand-weight axis** (the ADJUSTED
  comparison is asserted weight-invariant BECAUSE the effect has the same sign in every
  stratum; if a verdict session constructs a same-signed table where some positive
  standardization weight flips the adjusted sign, that collapsibility claim is wrong and the
  corrected statement is the finding — this axis is genuinely LIVE for the general claim, and
  the head confines the invariance claim to the same-sign case for exactly that reason);
  **model-arithmetic axis** (a verdict session's read of the pool, the pivot, the cliff, or a
  standardized rate contradicts a pinned Fraction — one misread of a stratum count moves the
  pooled gap and the cliff x\* together, and this axis prices exactly that); **witness-scope
  axis** (the head prices the EXISTENCE and exact structure of a reversal on the pinned table,
  not a PREVALENCE of reversals over random tables — if a verdict session judges the pinned
  witness unrepresentative of the fleet surfaces the consequence targets, that is a finalized
  NULL naming the scope mismatch, never a re-run request).

GATE POWER, computed at registration: the sim is FULLY DETERMINISTIC in every decision leg —
each clause is an exact integer inequality, an exact Fraction identity, or an exact finite
sweep; there is NO seeded arm and NO statistical gate; JOINT pass probability across all gates
for a correct implementation = 1 EXACTLY (the P028/P032/P036/P076 no-stochastic-gate
precedent). MARGIN LEDGER, disclosed: every REJECT clause is an exact-equality or
exact-inequality contact — the registered surfaces are the two stratum gaps (≈ 0.064 small,
≈ 0.042 large), the pooled reversal 16/350, the pivot value ≈ 0.8851 vs 0.8257, the cliff
x\* = 184 (with unit-margin boundary at x=183/184), and the standardized pair (634983/762700
vs 6231/8000, gap ≈ 0.054). A census landing off these exact values is INVALID-or-NULL by the
pre-registered axes, never a "close enough."

## Gates (run INVALID on any failure)

- **F1 — model identities:** each cell total matches (87/263/270/80); per-treatment totals ==
  350; grand total == 700; every stratum rate reduces to its pinned Fraction; pooled_A = 39/50
  and pooled_B = 289/350 recompute from the raw counts.
- **F2 — the structure results, exact:** (a) REVERSAL — A > B in both strata by
  cross-multiplication AND pooled B > pooled A, gap 16/350; (b) PIVOT — base_S > base_L, the
  allocation shares 263/350 vs 80/350, and A@Bmix > pooled_B; (c) CLIFF — pooled_A(x) strictly
  decreasing, exactly one crossing, x\* == 184 with the x=183/184 boundary; (d) REPAIR —
  std_A > std_B and the four-mix weight-invariance.
- **F3 — census anchors (reference values, exact):** 81/87 · 192/263 · 234/270 · 55/80 ·
  39/50 · 289/350 · 16/350 · 315/357 · 247/343 · 263/350 · 80/350 · x\* = 184 · 634983/762700 ·
  6231/8000.
- **F4 — the hand worlds (pencil):** (a) cross-multiplication 81·270 = 21,870 > 234·87 =
  20,358 pins A > B in small without division; (b) 192·80 = 15,360 > 55·263 = 14,465 pins A > B
  in large; (c) 273 < 289 pins B > A pooled at the common denominator 350 — the reversal in
  three integer comparisons, no floats; (d) APPROVE dead by the single exhibited
  counterexample.
- **F5 — degeneracy/convention controls:** if the allocation is BALANCED (give both
  treatments the same stratum weights) the reversal cannot occur — the pooled ordering equals
  the standardized ordering (the confounder is the whole mechanism); a same-stratum-rate
  control (set A·L rate = A·S rate) removes the within-A gradient and the sweep has no
  crossing; the standardized comparison on the BALANCED allocation reproduces the naive pooled
  comparison exactly (adjustment is a no-op when there is nothing to adjust for).

## Expected landing (DISCLOSED per the P028–P080 exact-arm norm)

REJECT on all four conjuncts, at the drafter's exact values (the sim re-derives everything
from scratch and must not trust these; every number computed live at drafting —
`draft_p084.py`, **25/25 checks PASS, exit 0**, seedless, byte-identical across two runs):
**R1** — A wins both strata (81/87 > 234/270, 192/263 > 55/80), pooled reversal 289/350 >
39/50 by 16/350; **R2** — A loads the hard stratum (263/350 vs 80/350), A@Bmix ≈ 0.8851 >
0.8257; **R3** — pooled_A(x) strictly decreasing, single cliff at x\* = 184, real table x =
263 past it; **R4** — std_A = 634983/762700 > std_B = 6231/8000, weight-invariant over four
mixes, naive pool picks B. Falsifiability is real and named on three axes: (i) the
**estimand-weight world** — the invariance claim is confined to the same-sign case; a
same-signed table where a positive weight flips the adjusted sign would refute the general
collapsibility statement, and the estimand-weight NULL exists for exactly that; (ii) the
**arithmetic world** — one misread stratum count moves the pooled gap and the cliff x\*
together, and the model-arithmetic NULL prices that; (iii) the **scope world** — the head
prices the exact structure of ONE pinned reversal, not a prevalence over random tables, and a
scope-mismatch judgment is a finalized NULL. Disclosed sharpening, reporting-only: the entire
head is exactly computable with no seed and no sampling — there is no stochastic sharpening to
disclose, which is itself the point (the P028/P076 seedless-census posture).

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Fleet-external head: **no lane CONSUMER**; the deliverable is the rotation lane's SEVENTEENTH
fleet-external domain coverage row (a citable measured verdict) plus a transferable
aggregation-bias correction. REJECT → "a uniform subgroup ordering survives aggregation"
retires with numbers, and the correction ships in three lines: (1) never rank two POOLED
rates without checking whether the grouping variable is balanced across the arms — a pooled
rate is a size-weighted mean whose weights belong to the ALLOCATION, so a confounded rollout,
a skewed sampling frame, or an uneven cohort mix can flip the sign while every cohort agrees
(the fleet's own instance: any dashboard or A/B readout that lumps heterogeneous cohorts —
repos, lanes, time-windows, container images — into one conversion/pass/success rate);
(2) the reversal is a CLIFF, not a drift — there is a single allocation threshold (here
x\* = 184 of 350) past which the pooled winner flips, so "the numbers are close, it won't
matter" is exactly wrong near the threshold; (3) the repair is STANDARDIZATION, and it is not
free — it requires RECORDING the confounder and reweighting to a common distribution, which is
a decision to instrument for the covariate BEFORE you need it (you cannot recover the truth
from pooled totals alone). Known co-consumers of the correction: every metric surface that
aggregates across strata (the review-queue and backlog dashboards, any pass-rate roll-up over
lanes) — the transferable audit is "is this rate pooled over a confounded grouping, and if so
what is the standardized comparison?" Follow-ups named, none in scope: the PREVALENCE of
reversals over a random-table ensemble (a different, sampling-flavored object); k-stratum and
continuous-confounder generalizations; the amount-of-confounding needed (a sensitivity curve
in the allocation gap); the DOWNWARD direction (adjustment INTRODUCING a spurious effect under
collider stratification — the same algebra, opposite hazard, needs its own fixtures).

## Dedup

Tree-wide `rg -i "simpson|aggregation.?reversal|reversal paradox|confound|collaps|standardi[sz]"`
(bootstrap.py/.substrate excluded) at HEAD b119a62: zero prior social-statistics content —
the "collapse" hits are the word (scope-collapse, series-collapse) in product/venture lane
heads, never Simpson's paradox; no idea file or proposal prices a pooled-rate reversal, a
confounded stratum allocation, or a standardization repair. The two DELIBERATELY switched-away
domains, both confirmed already occupied firsthand this slice: **P017**
(`irv-monotonicity-close-races-2026-07-13.md`) — social choice / IRV monotonicity ("how often
raising the winner makes it lose"); **P056** (`inspection-paradox-wait-inflation-2026-07-14.md`)
— renewal-theory random incidence. Both are the DISPATCH-named primary/fallback domains and
both are hard duplicates, so this slice serves the fresh SEVENTEENTH domain instead
(decide-and-flag). No proposal P001–P080 and no verdict V001–V096 prices a confounded pooled
rate. Nearest priors argued distinct: **P080 → correlation design under shared randomness**
(the nearest word-kin via "aggregation"/"pooled", but its object is a JOINT probability made a
design variable by one shared random permutation, marginals invariant — a stochastic coupling;
here nothing is random, the object is a deterministic pooled RATE that reverses under
confounded n-weights, and the "pool" is an arithmetic mean of stratum rates, not a joint
success event); **P072 → group testing** (a stochastic screening ECONOMY against a prevalence
prior — here no test, no prevalence, no cost, a deterministic reversal); **P056 → inspection
paradox** (length-biased WAITING under random incidence — a size-bias law like this head's
size-WEIGHTING, but its object is a renewal interval's sampling bias with a probabilistic
correction; here the bias is the allocation's confounding of a deterministic average, and the
correction is standardization, not de-biasing a sampled interval); **P040 → Schelling**
(emergent aggregate from local rules, but a seeded dynamics over a lattice — no strata, no
confounder, no reversal). Method kin only: the P028/P032/P036/P076 exact-census + twin-arm +
no-stochastic-gate discipline, reused as machinery on a new object — this head's own additions
to the battery: a size-weighted-mean reversal as the decision object, a single-cliff
allocation threshold (x\* = 184) registered as its own gate, a WEIGHT-INVARIANT standardization
repair confined to the same-sign case (with the general estimand-weight dependence named as
its own live NULL axis), and a priced covariate-recording cost.

## Model basis (declared model-dependence — the P024 discipline)

Four modeling commitments carry the verdict, each pinned and directional: (1) the WITNESS is
the canonical Charig et al. (1986) integer table — a real published reversal, not a
constructed toy; the head prices its EXACT structure (existence + cliff + repair), and the
witness-scope NULL prices any judgment that it is unrepresentative of the fleet surfaces the
consequence targets; (2) the DECISION arms are seedless exact integer/Fraction arithmetic —
there is no sampling and no seed, so every decision number is platform-independent and the
model-arithmetic NULL prices a misread, not a variance; (3) the STANDARDIZATION repair is
direct standardization to the pooled marginal, and its weight-invariance is claimed ONLY for
the same-sign case (collapsibility under uniform effect direction) — the estimand-weight NULL
prices the general claim, and the head confines its invariance assertion accordingly; (4) the
CLIFF is a one-dimensional sweep holding A's stratum rates fixed while moving the allocation —
a witness slice through the confounding, not a claim about all reallocations, and the sweep is
gated by direct enumeration (351 points) rather than cited. The folk belief is priced against
its own best formalization: "a uniform stratum ordering survives aggregation" is exactly the
claim the pinned reversal falsifies, and the BALANCED-allocation control (F5) registers the
case where the folk rule IS true, so the head cannot be read as a straw man.

## Probe report (v0, 2026-07-16)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep returned only
> the "collapse"-the-word hits (product/venture lane heads) and confirmed the two
> dispatch-named domains already spent (IRV = P017, inspection paradox = P056), read firsthand;
> no prior head prices a pooled-rate reversal. (b) **kill test NOT triggered** — no recorded
> drop of this domain on any card; P080/P072/P056 price different objects (argued in Dedup).
> (c) **feasibility + liveness arithmetic checked LIVE** — every registered numeral ran this
> session (draft_p084.py, 25/25 PASS, exit 0, seedless): the reversal, the pivot, the 351-point
> cliff sweep, and the four-mix standardization; expected landing DISCLOSED (REJECT), all
> rulings reachable, the estimand-weight / arithmetic / scope falsifiability worlds named.
> (d) **grounding reachability** — HONEST: this is a pure-math head with NO external repo; it
> is grounded firsthand in the reasoning + the cited canonical table, and the pin annotation
> states the no-repo scope rather than claiming a surface.

**1. What is this really?** A pre-registered EXACT MEASUREMENT of the aggregation folk rule —
"better in every subgroup ⇒ better overall" — taken on the rule's canonical counterexample: a
pooled success rate that reverses its stratum ordering under a confounded allocation. Three
exact facts the rule denies: the REVERSAL (A wins both strata, loses the pool by 16/350), the
PIVOT (the reversal lives entirely in the n-weights — A under B's mix wins), and the CLIFF +
REPAIR (a single allocation threshold x\* = 184, and standardization restores the truth at the
price of one recorded covariate).

**2. What is the possibility space?** (i) Don't run it — the round-17 unrelated closer goes
unserved and the coverage claim stalls at sixteen domains. (ii) Re-use a prior round's domain
— the dispatch spec's own IRV/inspection choices, both already spent (P017/P056); fails the
"rotate" ask, which is why this slice switched. (iii) A folklore retelling ("Simpson's paradox
is a cute stats gotcha") — retells the reversal without the exact structure: the pivot as a
weight effect, the single-cliff threshold, and the priced weight-invariant repair are what the
exact treatment uniquely gives. (iv) An MC estimate of reversal prevalence — leaves the
decision number seed-noisy when the object is exactly countable; demoted to a named follow-up.
(v) This head: exact arithmetic as the ruling, REJECT-first bands, INVALID controls, three
named NULL axes. (vi) Over-scope (k strata, continuous confounders, collider/downward
direction) — each a named follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?** One
~120-line stdlib file: four cell pairs, exact `Fraction` rates, a 351-point sweep, and a
four-weight invariance loop — that single kernel yields the reversal, the pivot, the pinned
cliff, and the weight-invariant repair, from a sim a verdict session runs cold in well under a
second, seedless and platform-independent.

**4. What breaks it? (assumptions made explicit)** (a) **The witness is one pinned table** —
the head prices its exact structure, not a prevalence; the witness-scope NULL prices an
unrepresentative-witness judgment. (b) **The repair's invariance is same-sign-only** — stated
explicitly; the estimand-weight NULL prices the general claim, and a collider/downward table
is a named follow-up, not a clause. (c) **The arithmetic is exact and seedless** — a
disagreement is a misread, not variance; the model-arithmetic NULL prices it. (d) **Band
placement could cherry-pick** — every band is an exact value committed before the sim, the
landing is DISCLOSED (REJECT), and the BALANCED-allocation control registers the case where
the folk rule is TRUE.

**5. What does it unlock?** The pipeline's SEVENTEENTH fleet-external verdict and the rotation
lane's domain-coverage proof extended (… → group testing → algebraic error detection →
correlation design under shared randomness → CONFOUNDED AGGREGATION); a measured, citable
answer to "does a uniform subgroup ordering survive aggregation" with three standalone pins
(the 16/350 reversal at uniform stratum dominance; the single cliff x\* = 184; the
weight-invariant standardization repair and its covariate-recording price); and a transferable
aggregation-bias audit for every fleet surface that pools a rate over a possibly-confounded
grouping.

**6. What is the cheapest experiment that decides it?** The whole head IS the cheapest deciding
experiment: Arm A settles every decision number exactly in well under a second with no seed.
The single cheapest probe if a reader doubts it is pencil: at the common denominator 350, A's
successes are 273 and B's are 289 (273 < 289 — B wins the pool), while 81·270 > 234·87 and
192·80 > 55·263 (A wins both strata) — the reversal in three integer comparisons, no computer.

**7. What would make this a mistake to run?** If the exact treatment were unavailable (it is
not — every decision quantity is a finite exact computation), if the domain duplicated a prior
head (it does not — Simpson's paradox is tree-wide clean; the two dispatch-named domains that
DID collide, IRV = P017 and inspection = P056, are cited and switched away from), or if the
disclosed REJECT made the run theater. It does not: the value is the independent hermetic
re-derivation (the sim re-writes the arithmetic and must reproduce the reversal, the cliff
x\* = 184, and both standardized rates from scratch), the honest no-repo grounding (a pure-math
head that claims no surface), and both non-REJECT rulings genuinely reachable (APPROVE is one
exhibited-counterexample away from being dead — it is dead; the estimand-weight and scope NULLs
are one defensible judgment away).

**8. How will we know it worked?** A committed sim-lab report with: the stratum-rate table, the
pooled reversal with its 16/350 gap, the pivot (A under B's mix), the cliff sweep with x\* =
184 and its boundary, the standardization repair with its four-mix invariance, the F1–F5 gate
results, the verdict token against the pre-registered bands, and a byte-identity note (two
process runs identical, seedless). A clean run reproduces the drafter's disclosed values
(reversal 16/350; cliff 184; std 634983/762700 vs 6231/8000) from scratch, or — the more
interesting outcome — DISAGREES and pins the drafter's error, which the pre-registered rule
then rules on honestly (the estimand-weight, model-arithmetic, and witness-scope NULL axes
exist for exactly that).

**Recommendation: sim-ready**
