# Rubric weight-robustness — is the fresh batch's band partition (best/borderline/no-build) an artifact of the fifth decimal of a judgment-call weight vector?

> **State:** sim-ready
> **Class:** venture (pipeline rotation — the standing ORDER 003 VENTURE slot,
> round 11, PRODUCTS half on the slot's own half-alternation read from the
> actual sequence: P018 books (r1) → P022/P026 trading (r2/r3) → P030 books
> (r4) → P034 trading (r5) → P038 books (r6) → P042 products (r7) → P046 books
> (r8) → P050 products (r9) → P054 books (r10), so r11 = products due; round 11
> opened at fleet backlogs with P057 (#391), so the venture slot is next per
> ORDER 004 rule 3.)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/venture-lab/blob/a9e202d69433dc69623a78dd3164ac4689d7c8f0/docs/products/ideas-2026-07-13-night.md@a9e202d69433dc69623a78dd3164ac4689d7c8f0 · fetched 2026-07-14T03:56:56Z
> (FIRSTHAND pin: `add_repo` for venture-lab succeeded in this session's recon
> slice; read-only shallow clone re-pinned at drafting — `git fetch` at
> 2026-07-14T03:56:56Z confirmed origin/main still at `a9e202d`, and the batch
> doc was re-read at that SHA via `git show`. Every score, weight, and band
> sentence below is quoted from that read. The sim itself is fully hermetic:
> zero repo/network reads at verdict time, every fixture constructed in-sim
> from the pinned constants in this file.)

**Origin:** drafted under the standing owner ORDER 003 (continuous pipeline)
and ORDER 004 rule 3's rotation — round 11 opened at the fleet-backlogs slot
(PROPOSAL 057, PR #391), so this slice serves the VENTURE slot, PRODUCTS half.
The harvested head: venture-lab's fresh 7-concept ideation batch
(`docs/products/ideas-2026-07-13-night.md` @ `a9e202d`) scores every concept
on the shipped kill-rule-intake rubric — fixed weights **Distribution 35 /
Buildability 20 / Launch-effort 15 / Speed 15 / WTP 15** — and reads the
totals against the rubric's own bands, verbatim: *"below ~3.0 = do not build;
3.0–3.5 = borderline, tight budget only; above 3.5 = best available"*. The
batch publishes the **full 7 × 5 per-criterion score table** (every axis row
of every concept), which makes a question priceable that two prior venture
slices explicitly could NOT price and said so on the record: the P050 card
dropped "the otherwise-attractive rubric-weights head" as **UNDRAFTABLE**
("its honest sim needs the doc's actual … score table, which no prior block
quotes"), re-openable "the day a venture read is available" — that day is
today — and P042's Relations dropped "pricing the rubric's Distribution-35
weight itself" because *whether 35 is right* is a judgment call with no
falsifiable core. This head asks the question that IS falsifiable at the
published numbers: **does the partition the weights induce depend on the
judgment call, within a stated neighborhood?** The batch's own headline makes
it live: the sole above-band concept totals **3.525** — 0.025 above the 3.5
edge — and the batch's own text calls that "borderline-band territory"; the
lowest surviving borderline concept totals **3.025** — 0.025 above the
no-build edge. Two of seven verdict-carrying numbers sit 1/40 of a rubric
point from their band boundaries. This head builds nothing in venture-lab and
never edits its files (routing is the manager's per Q-0260); it prices the
instrument and hands the lane a pre-registered ruling.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested instrument, stated back.** The lane scores concepts on five
axes, takes the weighted total at fixed judgment-call weights, and reads the
total against fixed bands. The weights are precise (35/20/15/15/15) but not
measured — nothing in the repo derives them; they encode a belief about what
matters. If the band assignment of the batch is stable under any reasonable
perturbation of that belief, the partition is a finding; if it flips inside a
few percent of weight jitter, the partition is an artifact of the weight
vector's fifth decimal and the honest unit of report is the concept's
DISTANCE-TO-EDGE, not its band. The falsifiable core: **under bounded
multiplicative jitter of the five weights (each weight scaled by an
independent Uniform[1−x, 1+x] factor, then renormalized to sum 1 — one
jittered judge rescoring the whole batch per draw), is the induced band
partition of the 7 published concepts preserved — and what is each concept's
exact critical radius x\* (the smallest jitter at which its band can
change)?** Both halves are computable against the published numbers alone:
the critical radii in exact `fractions.Fraction` arithmetic (the weighted
total is a linear-fractional function of the jitter factors, so its extrema
over the jitter box sit at the 32 box vertices — exact per-vertex linear
solves, no search), the flip probability by seeded MC.

**The model (fixed, fully pinned — every constant a decision of this file,
none left to the implementer; all decision arithmetic exact rationals).**

- **Score table S (7 concepts × 5 criteria, axis order Distribution,
  Buildability, Launch-effort, Speed, WTP — copied from the batch doc's
  per-concept tables @ `a9e202d`, halves exact):**
  1. AI Novella Production Kit — (3, 9/2, 4, 4, 5/2)
  2. Fiction Vetting-Packet Kit — (5/2, 9/2, 4, 4, 2)
  3. Pre-Registered Experiment Kit — (5/2, 4, 4, 4, 5/2)
  4. Trilingual Edition Factory — (2, 9/2, 4, 4, 5/2)
  5. Dead-Session Recovery Playbook — (2, 9/2, 4, 4, 2)
  6. Agent Session Retro Kit — (2, 9/2, 4, 4, 3/2)
  7. Provenance-Freshness Checker Kit — (3/2, 4, 4, 4, 3/2)
- **Weights w₀ = (7/20, 1/5, 3/20, 3/20, 3/20)** — the shipped rubric's
  35/20/15/15/15, exact; sums to 1 exactly.
- **Published totals (identity gate F1):** the exact recomputed totals must
  equal the doc's published totals exactly: **141/40 (3.525) · 131/40 (3.275)
  · 13/4 (3.25) · 127/40 (3.175) · 31/10 (3.10) · 121/40 (3.025) · 11/4
  (2.75)** — verified at drafting, they do.
- **Bands (the rubric's own reading, pinned):** no-build if t < 3, borderline
  if 3 ≤ t ≤ 3.5, best-available if t > 3.5. (Edge-inclusion convention is
  immaterial for the MC legs — under continuous jitter an exact-edge total is
  a measure-zero event — and no published total sits on an edge; stated.)
- **Baseline partition B₀ = (best, borderline, borderline, borderline,
  borderline, borderline, no-build)** — the batch's own arithmetic layer.
- **Jitter mechanism (decision-bearing):** radius x; u_j i.i.d.
  Uniform[1−x, 1+x], j = 1..5, one 5-vector per draw; perturbed weights
  w′_j = w₀_j·u_j / Σ_k w₀_k·u_k; perturbed total t_i(u) = Σ_j w′_j·S_ij for
  every concept i under the SAME u. **Flip event:** the band vector of
  (t_1..t_7) differs from B₀ in any coordinate. **p(x) = P(flip)**.
- **Radius grid, order pinned: x ∈ {1/50, 1/20, 1/10, 1/5}; the decision
  cell is x = 1/10** (±10% — small against any defensible reading of "the
  weights are a judgment call"; the 1/50 cell is the exact-zero control, the
  1/5 cell brackets the coarse end, both reporting).

**Two arms.**

- **Arm A (decision arm — exact, seedless):** for each concept and each band
  edge e ∈ {3, 7/2}, the perturbed total restricted to a vertex sign-pattern
  P ∈ {−1, +1}⁵ is t_P(x) = (a₀ + a₁x)/(1 + b₁x) with a₀ = Σ w₀_j S_ij,
  a₁ = Σ P_j w₀_j S_ij, b₁ = Σ P_j w₀_j — solving t_P(x) = e is one exact
  linear equation per (pattern, edge); **x\*_i = the minimum solution in
  (0, 1) over all 32 patterns and both edges**, an exact Fraction. Because a
  linear-fractional function attains its extrema over a box at the box's
  vertices, the 32-vertex min/max at any radius x is the exact reachable
  range of t_i (used by gates F2/F3/F4). Milliseconds, stdlib only.
- **Arm S (confirmation arm — seeded MC):** **N = 100,000 draws per radius**
  via `random.Random(20261369)`, radii in pinned grid order, pinned draw
  order (5 uniforms per draw, criterion order); estimator p̂(x) = flip
  fraction; per-concept band-change attribution recorded per radius.

**Seeds (registered):** 20261369 (Arm S main confirmation leg — the only
seed any decision number reads) / 20261370 (stability leg — N = 20,000 per
radius, same pinned order; the twin evaluators must reproduce the ruling on
it under the cross-seed gate) / 20261371 (reporting legs only — the
Dirichlet-mechanism worlds and attribution tables below, never
decision-bearing) / 20261372 (**aux — reserved, NEVER read by any leg**; the
P054/P057 aux convention). Allocated strictly above the PROPOSAL 057
high-water **20261368** — re-swept at drafting: boundary-aware regex
`(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over this tree at HEAD `267b4d5` maxes
at genuine 20261368 (the larger standalone numerals
20261542/20261833/202670087 are Fraction-numerator and decimal-fraction
digit substrings in results.json-quoting outbox text — data, not seeds; the
P046–P057 sweep-recipe trap re-confirmed). Byte identity: stdout +
results.json byte-identical across two process runs; Arm A
platform-independent exact Fractions, Arm S pinned to a stated CPython minor
version.

**Pre-registered decision rule (fixed BEFORE any code exists; evaluated in
this order: REJECT first, then the INVALID controls gate, then APPROVE, then
NULL).**

- **REJECT** ("the band partition is knife-edge fragile at the batch's own
  published numbers — the headline BUILD line and the no-build floor are
  artifacts of a few percent of a judgment-call weight vector, and the honest
  unit of report is distance-to-edge, not band"): **p̂(1/10) on the main leg
  ≥ 1/10, AND Arm A's exact critical radius for concept 1 is ≤ 1/20, AND Arm
  A's exact critical radius for concept 6 is ≤ 1/20.** Checked FIRST — the
  costly-error rationale: the rubric is the lane's standing GO/park/kill
  instrument and the NEXT ideation batch inherits it unchanged; reading
  "3.525 > 3.5" as a robust BUILD verdict (or "3.025 vs 2.75" as a robust
  kill boundary) when both sit 1/40 of a point from an edge invites budget
  decisions the weights cannot actually support.
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate or
  the cross-seed agreement gate failing (constants below).
- **APPROVE** ("the partition is weight-robust — the bands mean what they
  say at any reasonable reading of the weights"): **p̂(1/10) on the main leg
  ≤ 1/20, AND Arm A's exact critical radii are > 1/20 for ALL seven
  concepts.** Mutually exclusive with REJECT by arithmetic (1/20 < 1/10 on
  the p̂ clause; the x\* clauses contradict directly).
- **NULL** (anything else — a legitimate, reportable outcome): pre-registered
  axes: (i) **p-straddle** — p̂(1/10) ∈ (1/20, 1/10): the finding is the
  exact p̂ with the full x\* table; (ii) **arms-split** — the MC clause and
  the x\* clauses land on opposite sides (fragility reachable but rare, or
  frequent without touching the two named concepts): the finding is WHICH
  mechanism binds, with the per-concept attribution table; (iii)
  **mechanism-conditional** — a Dirichlet reporting world (below) would flip
  a promoted decision: named, never ruling; (iv) **arm disagreement**
  surviving the INVALID diagnosis (a defect is the finding, no ruling).

**Expected landing, DISCLOSED (the P048–P057 closed-form-arm norm — the
decision constants were computed at drafting and are disclosed rather than
feigning openness; the sim re-derives everything from scratch and must not
trust these).** Exact critical radii (min over both edges, per-vertex linear
solves over all 32 patterns): **x\*₁ = 1/27 ≈ ±3.70%** (down through 3.5),
x\*₂ = 9/37 ≈ 24.3% (up through 3.5), x\*₃ = 1/3 ≈ 33.3%, x\*₄ = 7/41 ≈
17.1%, x\*₅ = 1/11 ≈ 9.1%, **x\*₆ = 1/47 ≈ ±2.13%** (down through 3.0 — the
global minimum), x\*₇ = 1/5 = 20% (up through 3.0). Drafting MC (throwaway
seed 999, N = 100,000 per radius — NOT the registered seeds): p̂(1/50) = 0
exactly (forced: 1/50 < 1/47), p̂(1/20) ≈ 0.061, **p̂(1/10) ≈ 0.225**,
p̂(1/5) ≈ 0.355. So the disclosed landing is **REJECT on all three
conjuncts**: 0.225 ≥ 1/10 with ≈ 95 SD of margin at N = 100,000; 1/27 ≤ 1/20;
1/47 ≤ 1/20. Falsifiability is real and disclosed: at x = 1/20 the flip
probability ≈ 0.061 sits BELOW the 1/10 line — a decision radius registered
one grid step tighter would have landed in the p-straddle NULL, so the bands
genuinely discriminate; and five of seven concepts tolerate ≥ ±9% jitter —
the fragility is a property of the two knife-edge rows, not of the rubric
arithmetic as such (the disclosed sharpening: at x = 1/10 the flip event is
led by concept 6 at ≈ 0.225 with concept 1's crossing region ≈ 0.095 sitting
almost entirely inside it — reported with the attribution table, never a
gate).

**Gate power, computed at registration for a correct implementation.** The
only stochastic gate is the cross-seed agreement gate — every other gate is
deterministic for a correct implementation (F3's zero-flip identity is
deterministic because 1/50 < 1/47 = min x\* exactly, so a flip at x = 1/50
is impossible, not merely improbable; F1/F2/F4/F5/F6 are exact-arithmetic or
structural checks). Cross-seed gate arithmetic: SD of p̂ on the main leg at
N = 100,000 is at most √(0.25/100000) = 0.00158; on the stability leg at
N = 20,000 at most √(0.25/20000) = 0.00354; SD of the difference ≤
√(0.00158² + 0.00354²) = 0.00388, so the registered absolute gate **|p̂_main
− p̂_stab| ≤ 1/50 = 0.020 at every radius** sits ≥ 0.020/0.00388 ≈ 5.15 SD
wide — breach probability ≤ 2·Φ(−5.15) ≈ 2.6×10⁻⁷ per radius, ≤ 1.1×10⁻⁶
across the 4 radii by union bound. Decision separation: the drafting
estimate p̂(1/10) ≈ 0.225 sits (0.225 − 0.100)/0.00132 ≈ 95 SD above the
REJECT edge on the main leg (σ = √(0.225·0.775/100000) = 0.00132) and ≈ 42
SD on the stability leg — MC noise cannot move the ruling; if the true p in
fact sits inside (1/20, 1/10), the p-straddle NULL is the honest finding,
not a power failure. **Joint pass probability across all gates, all radii,
all seeds for a correct implementation ≥ 1 − 2×10⁻⁶** — comfortably above
the 95% registration floor; INVALID is not the modal outcome of a correct
sim (the V067 lesson applied: every tolerance absolute, sized in SD at the
registered N, no relative gates near small numbers, no "respectively").

**Gates (any failure → INVALID; constants pinned).**

- **F1 — identity:** w₀ sums to 1 exactly; the seven recomputed exact totals
  equal 141/40, 131/40, 13/4, 127/40, 31/10, 121/40, 11/4 respectively-free:
  concept-by-concept in table order; the baseline band vector equals B₀.
- **F2 — critical-radius self-consistency (exact):** for every concept i,
  the exact 32-vertex range at x\*_i − 1/1000 keeps t_i strictly inside its
  baseline band, and at x\*_i + 1/1000 the crossed edge lies inside the
  exact range (both Fraction evaluations; x\*₆ − 1/1000 = 953/47000 > 0, so
  every probe point is legal).
- **F3 — zero-flip identity (deterministic):** 1/50 < 1/47 = min_i x\*_i
  (exact comparison recomputed in-sim), therefore EVERY MC leg at x = 1/50
  must record exactly zero band changes over all draws and all concepts; a
  single flip invalidates the run.
- **F4 — containment:** every sampled per-concept total at every radius lies
  within Arm A's exact 32-vertex range widened by 10⁻⁹ absolute (the
  linear-fractional extreme-point property; the tolerance covers float
  evaluation only).
- **F5 — hand world:** one concept, two criteria, weights (1/2, 1/2), scores
  (3, 4): total = 7/2 exactly; the exact vertex range at x = 1/10 is
  [69/20, 71/20] by hand (t = (7 ∓ x·1)/2 at the two extreme patterns —
  denominator identically 1 because the two weights are equal).
- **F6 — battery:** RNG draw-count sentinel (exactly 5 uniform calls per
  draw: total calls = 5·N per (seed, radius) leg, counted and asserted);
  twin independently-written decision evaluators; stdout + results.json
  byte-identical across two process runs; CPython minor version pinned; the
  P017–P057 standing battery.
- **Cross-seed agreement gate:** |p̂_main(x) − p̂_stab(x)| ≤ 1/50 absolute at
  every radius (arithmetic above).

**Reporting-only legs (seed 20261371, N = 20,000 each — CANNOT flip the
decision, no agreement gates ride them):** (a) **Dirichlet-mechanism worlds**
— w′ ~ Dirichlet(κ·w₀) via `random.gammavariate(κ·w₀_j, 1)` renormalized,
κ ∈ {100, 400} (weight SDs ≈ 0.047/0.024 on the Distribution axis —
bracketing the decision radius from a mechanism the lane might find more
natural; MC only, no exact vertex counterpart, disclosed); (b) the
**per-concept attribution table** at every radius (which concept's band
change drives each flip; the near-nesting of concept 1's region inside
concept 6's, reported); (c) the **p(x) curve** across the grid with the
exact x\* table beside it; (d) the **band-edge convention note** (strict vs
inclusive at 3.0/3.5 — measure-zero under continuous jitter, asserted by
counting exact-edge hits, expected 0).

**What a reader DOES differently on the verdict** (all routing lane-side via
the manager per Q-0260 — this repo edits nothing in venture-lab). A
pre-registered APPLICATION GUARD rides every branch, TWO conditions: (1) the
verdict conditions on the published 7 × 5 score table, the 35/20/15/15/15
weights, and the 3.0/3.5 band sentences @ `a9e202d` — an amended rubric, a
re-scored batch, or changed band text means re-run, not reuse; (2) it
conditions on the batch's pre-evidence state (0 organic sales as of
2026-07-13; the sole BUILD publish-READY, owner-click-gated) — real sales
evidence re-anchors banding to measured rates and stales the
partition-as-instrument premise (the V049/V053 guard pattern, inherited).

- **REJECT** → the manager gets a paste-ready structured choice,
  recommendation first (Q-0263.2): **(a, recommended — zero new data, the
  sim ships the function)** future batch docs report each concept's exact
  critical radius x\* beside its total (one extra column; a ~40-line stdlib
  function the verdict dir commits), and any verdict with x\* ≤ 1/20 carries
  a "band-fragile" flag: decide it on the stated qualitative axes, not the
  band — which is what THIS batch already did informally (it killed three
  ≥ 3.0 concepts on named fatal axes and called its own 3.525 top scorer
  "borderline-band territory"; the verdict gives that instinct its measured
  basis); **(b)** keep the bands as-is, now explicitly accepting the
  headline BUILD line is band-fragile at ±3.7%; **(c)** re-cut the bands —
  an owner/lane intent call, never ruled by fiat here.
- **APPROVE** → the 3.0/3.5 bands gain a measured robustness basis and the
  next batch can cite it.
- **NULL** → the named axis ships with its numbers, plus the free probe: the
  x\* column costs nothing to compute on any future batch (exact
  arithmetic, no MC needed).

## Relations (adjacent heads — deliberately links, not duplication)

- **The recorded re-open ticket:** the P050 drafter card
  (`.sessions/2026-07-13-proposal-050-kill-clock-horizon.md`) dropped
  exactly this head as UNDRAFTABLE for want of the score table, re-openable
  "the day a venture read is available" — this file is that re-open, with
  the read FIRSTHAND and a fresher batch that publishes the full table.
- **The recorded objection, answered:** P042's Relations dropped "pricing
  the rubric's Distribution-35 weight itself (the weight is a judgment
  call, not a rate — no falsifiable quantitative claim a hermetic sim can
  price)". This head does NOT price whether 35 is right; it prices whether
  the PARTITION depends on the judgment call within a stated neighborhood —
  a purely arithmetic property of the published table, falsifiable to the
  last Fraction.
- Nearest venture kin, zero shared machinery: **P042 → V053** allocates
  build tokens across channels; **P046 → V057** allocates keyword tiles;
  **P050 → V061** prices kill-clock horizons (a stopping rule); **P054 →
  V065** prices an art-spend gate (dollars); **P038 → V049** the KU fork.
  None touches the scoring instrument itself.
- The ORDER 005/006 queued pricing SIM-REQUESTs (photo-pack PWYW-vs-$5,
  Ship-It $59 anchors, narrow-TAM $19-vs-PWYW) price PRICE POINTS of
  specific SKUs — not the rubric, not robustness, no shared fixtures.
- Method kin in other worlds, argued distinct: **P017** (IRV monotonicity),
  **P028** (bracket seeding optimality), **P036** (secretary-rule cardinal
  regret) stress decision RULES under perturbation/noise, but in
  voting/tournament/stopping worlds with zero shared fixtures and different
  consumers; no prior head jitters a weight vector or prices a scoring
  partition.
- The tree-wide dedup sweep `rg -i -g '!bootstrap.py' -g '!.substrate'
  'rubric|weight.?(robust|sensitiv|perturb|jitter)|dirichlet'` at drafting
  HEAD `267b4d5` hits only (i) the superbot critical-review-rubric family —
  "rubric" in the review-checker sense (finding-classes, not scoring
  weights), (ii) P042's own runner-up prose (the recorded objection above),
  and (iii) the P050 card's re-open ticket. No proposal P001–P057 and no
  verdict V001–V068 (V068 in flight on P057's paper-lane world, zero
  overlap) prices scoring-weight robustness, band fragility, or any rubric
  arithmetic.
- Runners-up this slice, weighed and dropped on merit: **publish-ORDER /
  click-budget allocation across the 10 READY SKUs vs the 256-click owner
  queue** (real, but the decisive constants — per-SKU click counts and
  conversion beliefs — are not published as a table; weaker pin); **band
  calibration against the observed 0-sale base rate** (needs sales data
  that does not exist yet — the T+14 clock at 2026-07-26 is the free
  probe); **measurement-mode length** (V061's "what it did NOT settle"
  neighborhood — too close to a NULL verdict's own follow-up to be a fresh
  head). The weight-robustness head won on: a fully published fixture set,
  a recorded re-open ticket, and two knife-edge rows sitting 1/40 of a
  point from their edges in the lane's newest committed decision document.

## Model basis (declared model-dependence — the P024 discipline)

- **(1) Statistical assumptions:** the jitter model prices REWEIGHTING
  uncertainty only — the per-criterion scores are held fixed at their
  published values. Score noise is a different, unmodeled fragility channel
  and its direction is stated qualitatively: adding score uncertainty
  cannot make a weight-fragile partition robust (it adds variation around
  the same knife edges); an APPROVE would still have to be read as
  "weight-robust, score-robustness unpriced". The multiplicative-uniform
  box is the pinned decision mechanism because it admits EXACT reachable
  ranges (linear-fractional vertex arithmetic) — the Dirichlet worlds
  bracket mechanism-dependence as reporting legs.
- **(2) Single most-likely-to-flip alternative:** the jitter MECHANISM and
  RADIUS — a reader who thinks ±10% is too generous a neighborhood for a
  "judgment call" reads the x = 1/20 cell (flip ≈ 6%) and the exact x\*
  table instead; the per-concept radii are radius-free facts and carry the
  finding on their own. Softer boundaries, named: the **editorial overlay**
  (the batch's actual BUILD/PARK/KILL verdicts already override raw bands
  on qualitative axes — #2 parked as a subset-fold, #4–#6 killed on named
  fatal axes despite ≥ 3.0 totals; this head prices the ARITHMETIC layer
  the rubric text itself defines, scope stated); the **band-edge
  convention** (measure-zero under continuous jitter, counted in-sim); the
  **batch-scope boundary** (the verdict is about THIS table's partition;
  the transferable deliverable is the x\* function, not the numbers).

## Probe report (v0, 2026-07-14)

> Single-pass battery (panel not escalated: self-contained knowledge probe
> over pinned published constants, sim is report-only evidence, no
> spend/publish/irreversible surface — README § probe battery). Verify-first
> ran FIRST, live this slice: (a) **source verified FIRSTHAND** — venture-lab
> shallow clone re-pinned at drafting (`git fetch` 2026-07-14T03:56:56Z,
> origin/main = `a9e202d`), the batch doc re-read at that SHA, all seven
> per-criterion score rows extracted and re-summed EXACTLY against the
> published totals (they match, Fraction-exact, gate F1). (b) **dedup** —
> the tree-wide rubric/weight/jitter sweep at HEAD `267b4d5` (Relations
> above); PROPOSALs 001–057 and VERDICTs 001–068 swept; the two recorded
> prior touches (P042's drop, P050's re-open ticket) argued as provenance,
> not overlap. (c) **kill test NOT triggered** — no prior head prices
> scoring-weight robustness. (d) **feasibility + liveness arithmetic
> checked** — the drafting prototype RAN this session: exact x\* table and
> the flip curve computed (throwaway seed, disclosed above); runtime
> bounded (Arm A milliseconds; Arm S ≈ 4 radii × 100,000 draws × 5 uniforms
> + 7 totals — tens of seconds pure CPython; stability + reporting legs
> noise on top).

**1. What is this really?** A pre-registered robustness audit of the
products lane's standing GO/park/kill scoring instrument, run at the
newest batch's own published 7 × 5 score table: exact critical jitter
radii per concept (linear-fractional vertex arithmetic, seedless
Fractions) plus seeded-MC flip probability of the induced band partition
under bounded multiplicative weight jitter, judged against bands fixed
before any code (REJECT first: flip ≥ 1/10 at ±10% AND both knife-edge
concepts' exact radii ≤ 1/20), byte-identical across two process runs.

**2. What is the possibility space?** (i) Don't run it — the round-11
venture slot goes unserved and the recorded P050 re-open ticket stays
open despite its unlock condition being met. (ii) Serve the products half
from the click-budget or band-calibration surfaces — weighed and dropped
in Relations (unpublished constants; needs sales data that doesn't exist).
(iii) A prose answer ("3.525 is obviously borderline") — the batch itself
already says this qualitatively; measuring it is what turns an instinct
into an instrument rule. (iv) Price WHETHER the weights are right — P042's
recorded dead end (judgment call, unfalsifiable). (v) This head: the
falsifiable neighbor — partition stability, exact at the published
numbers.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file + one fixture JSON yields: the exact
seven-row critical-radius table (the batch's headline BUILD verdict
survives only ±3.70% of weight jitter; the no-build floor ±2.13%; the
median concept ±17–33%), the flip-probability curve with per-concept
attribution, and a transferable ~40-line exact x\* function any future
batch (or any fleet rubric — superbot's review classes, fleet-manager's
scoring sheets) can run as a one-column addendum at zero MC cost.

**4. What breaks it? (assumptions made explicit)** (a) The jitter
mechanism/radius choice — bracketed by the Dirichlet reporting worlds and
carried radius-free by the exact x\* table (Model basis (2)). (b) Score
noise unmodeled — direction stated; an APPROVE reads "weight-robust only".
(c) The editorial overlay — the lane already overrides bands
qualitatively; the head prices the arithmetic layer the rubric text
defines, and the REJECT consequence explicitly RATIFIES the override
instinct with numbers rather than fighting it. (d) Mechanism gates — every
tolerance absolute and SD-sized at the registered N (the V064/V067
lesson), every registered constant recomputed exactly at drafting (the
V065 lesson: 141/40 … 11/4 verified, 1/27 and 1/47 verified, 1/50 < 1/47
verified, the hand world verified).

**5. What does it unlock?** The lane's scoring instrument gains a
robustness meter it can run on every future batch for free; the knife-edge
reading of 3.525 ("borderline-band territory", the batch's own words)
gets a number; the pipeline gains its first instrument-audit head (prior
venture heads priced decisions; this prices the decision-MAKER); and the
x\* column pattern transfers to any weighted-rubric surface in the fleet.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external at verdict time — fully hermetic (the P017–P057 precedent); the
harvest grounding is one already-verified read-only clone pin (FIRSTHAND,
`a9e202d`). Cheapest kill BEFORE simming: a prior verdict on rubric
robustness (none — swept), or the published totals failing the exact
recompute (they pass, drafting-verified). Cheapest confirm AFTER: run the
x\* function on the PRIOR batch's 9 × 5 table (`ideas-2026-07-13.md`, also
published) — same instrument, second worked example, zero new machinery.

**7. Which lane should build it — and what does it displace or
duplicate?** sim-lab builds and runs the sim (the Q-0264 pipeline's verify
seat — this file is its intake spec); venture-lab's products lane consumes
the verdict as an instrument rule for its next ideation batch, routed by
the manager per Q-0260; this repo builds nothing. It displaces nothing in
flight (V068 holds P057's paper-lane world; no verdict session holds a
venture head) and duplicates nothing (Relations dedup; the two recorded
prior touches are provenance).

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib Python file (both arms + gates + twin evaluators), one fixture JSON
(the 7 × 5 score table and w₀ exact, the published-totals identity row,
the band constants 3 and 7/2, the radius grid {1/50, 1/20, 1/10, 1/5}
with decision cell 1/10, the decision constants 1/10 and 1/20, the
cross-seed gate 1/50, the F1–F6 fixtures with the hand world, per-leg draw
counts {100000, 20000, 20000}, seeds 20261369–372, the harvested weight
and band sentences with the FIRSTHAND pin `a9e202d`), one REPORT.md with
the x\* table, the flip curve, the attribution table, the ruling, and the
named-axis/probe line on NULL — the standing INTAKE/VERDICT grammar,
nothing else.

**Recommendation: sim-ready** — every constant pinned here, bands
registered REJECT-first before any code, every registered identity
recomputed exactly at drafting (the V065 lesson), every stochastic gate
SD-sized at its registered N with joint pass ≥ 1 − 2×10⁻⁶ (the V067
lesson), seeds 20261369–372 above the verified high-water 20261368, fully
hermetic at verdict time; the honest next step is the sim itself.
