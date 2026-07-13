# Schelling tipping priced at the integration-compatible threshold — does a 30%-minority-content preference still self-sort?

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain
> slot, round 6; the domain itself is emergent spatial self-organization / agent-based
> relocation dynamics — Schelling's segregation model from the micromotives-and-
> macrobehavior canon — fleet-external by design and DIFFERENT from round 1's social
> choice (PROPOSAL 017), round 2's congestion routing (PROPOSAL 024), round 3's
> tournament seeding (PROPOSAL 028), round 4's pattern races (PROPOSAL 032), and round
> 5's optimal stopping (PROPOSAL 036), so the rotation now spans SIX domains) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/idea-engine@ab66463c865a90ab570e45a8476b3b7587268fb2 · fetched 2026-07-13T17:11:18Z
> (the dedup-sweep pin — this repo's own tree at drafting HEAD, the only read this head
> takes; the sim itself is fully hermetic: zero repo/network reads at verdict time,
> every fixture constructed in-sim from the pinned constants in this file)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous pipeline —
"continue coming up with new ideas, that is your main purpose"), the rotation established
by ORDER 004 rule 3 ("fleet backlogs → venture's book/product space → game mechanics →
COMPLETELY UNRELATED domains") — round 6's other three slots are already served (fleet
backlogs → PROPOSAL 037, venture → PROPOSAL 038, game mechanics → PROPOSAL 039), so this
slice serves the unrelated slot; PROPOSAL 017 opened the lane with social choice,
PROPOSAL 024 rotated it into congestion routing, PROPOSAL 028 into tournament-format
design, PROPOSAL 032 into pattern-race probability, PROPOSAL 036 into sequential search /
optimal stopping; this is round 6's head, rotated into a SIXTH fleet-external domain
(emergent spatial self-organization). **Placement note (decide-and-flag):** sections are
roster-derived and inventing one ad hoc is forbidden (README § Sections;
`check_sections.py` reds an ORPHAN section against the live roster), and that checker's
own carve-out rules that sim-lab-shaped ideas "ride `ideas/fleet/` or the proposing
section" — so this fleet-external head lives here, flagged rather than silently
squatting, exactly as PROPOSALs 017, 024, 028, 032, and 036 did.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The folk belief.** Schelling's segregation model is THE canonical demonstration that
macro-level outcomes can betray micro-level intentions: agents with only a MILD
preference about their neighbors — perfectly content as a local minority — nonetheless
self-sort into starkly segregated neighborhoods. The popularized story ("nobody wants
segregation, everybody gets it") is repeated far more often than it is measured, and the
quantitative core is genuinely parameterized: HOW mild can the preference be and still
tip? The claim under test here is the strongest popular form: at τ = 0.30 — an agent is
satisfied so long as merely 30% of its occupied neighbors are its own type, i.e. it
happily lives as a 3-in-10 minority, a preference COMPATIBLE with full integration
(a well-mixed grid leaves the typical agent near 50% like-neighbors, far above 0.30) —
the population still self-sorts far beyond anything the preference demands. The settled
part is the qualitative textbook claim (Schelling's original counters and every ABM
course reproduce SOME amplification on SOME parameterization). The measured unknown is
whether THIS fully-pinned, conservative parameterization — uniform random relocation
(not preference-seeking moves), a mere 10% vacancy pool, live random-serial updating —
clears a pre-registered "strong segregation" band at exactly τ = 0.30, or whether the
amplification story quietly depends on kinder-to-segregation modeling choices. No
closed form decides it: Schelling dynamics have no analytic fixation distribution, so
REJECT, APPROVE, and NULL are all live and only the run settles it. This mirrors the
accepted P017/P024/P028/P032/P036 pattern: the effect is settled in principle; its
magnitude on a committed, fully-pinned dynamics at the committed threshold is the
unknown.

**The model (fixed, fully pinned — every constant a decision of this file, none left to
the implementer).**

- **Grid:** N = 40 → a 40×40 TORUS (both axes wrap), 1,600 cells, row-major indices
  0..1599 (cell (r, c) ↦ 40r + c).
- **Population:** exactly 720 type-A agents (45%), 720 type-B agents (45%), 160 vacant
  cells (10%). Conservation of all three counts is a per-sweep gate.
- **Neighborhood:** Moore 8-neighborhood with toroidal wraparound (the 8 cells at
  Chebyshev distance 1).
- **Satisfaction:** an agent is SATISFIED iff its like-fraction among OCCUPIED neighbors
  is ≥ τ, tested in exact integers as `like · τ_den ≥ τ_num · occ` (no floats anywhere
  in a decision path). **No-occupied-neighbors convention, pinned:** an agent with ZERO
  occupied neighbors is SATISFIED (vacuously content — the convention that biases
  AGAINST amplification, since isolated agents never flee).
- **τ grid:** {1/8, 1/4, 3/10, 3/8, 1/2, 5/8, 3/4} — seven exact-rational cells; the
  DECISION cell is τ = 3/10 = 0.30; all other cells are the reporting curve s(τ).
- **Initialization (per run):** build the 1,600-entry label list in the pinned
  construction order [720 × A, then 720 × B, then 160 × vacant], then one
  `rng.shuffle` of that list → the starting grid. The initial placement IS the
  well-mixed baseline; its s is measured (see the τ = 0 control leg).
- **Dynamics (random-serial relocation, live evaluation):** one SWEEP = (a) collect the
  currently occupied cell indices in ascending order and `rng.shuffle` them; (b) process
  agents in that order — each agent, at its turn, evaluates satisfaction against the
  LIVE grid (moves earlier in the same sweep are visible); (c) an unsatisfied agent
  relocates to a uniformly random vacant cell — destination = the current vacant-cell
  list in ascending index order, position drawn by `rng.randrange(len(vacancies))` —
  its old cell becomes vacant immediately. Agents move only themselves, so every entry
  in the sweep order is still in place at its turn. RNG = stdlib
  `random.Random(seed)`, ONE generator per leg, draws in the pinned order (init
  shuffle → per-sweep order shuffle → one randrange per relocation); per-leg draw
  counts are sentinel-checked.
- **Termination:** FIXATION = a full sweep with zero relocations (under live evaluation
  this certifies a stable configuration, independently re-verified — see gates), else
  the pinned SWEEP CAP = 500 sweeps. A cap-terminated run's s is recorded but
  CAP-CENSORED for decision purposes (see the validity conjunct in the decision rule).
- **Runs:** M = 32 runs per τ cell on the main leg, M = 16 on the stability leg; pinned
  loop order (τ ascending, run index 0..M−1), all runs of a leg drawn from that leg's
  single generator in pinned order.

**Primary metric.** s(τ) = the mean like-neighbor share at termination: over all agents
with ≥ 1 occupied neighbor, the mean of (like occupied neighbors / occupied neighbors),
computed as an exact `fractions.Fraction` once per run at termination (per-agent
denominators ≤ 8; the mean is a single exact rational). The decision number is the
MEDIAN of the 32 main-leg run values at τ = 3/10 (median of 32 = the mean of the 16th
and 17th order statistics — still an exact rational, compared to exact-rational bands).
Well-mixed anchor: at random placement with equal type counts, s concentrates tightly
near 1/2 — measured, not assumed, by the τ = 0 control leg.

**Seeds (registered):** 20261297 (main decision leg) / 20261298 (stability leg, M = 16,
must reproduce the ruling) / 20261299 (reporting leg — sensitivity sweeps) / 20261300
(aux — NEVER read by any decision number; reserved for the named NULL probe).
Allocated strictly above the P039 registry high-water 20261296, re-checked across all
prior outbox blocks at drafting. Byte-identity: stdout + results.json byte-identical
across two process runs; CPython minor version pinned in the fixture.

**Pre-registered decision rule (fixed BEFORE any code exists; evaluated in this order,
REJECT FIRST; bands exact rationals 11/20 and 7/10, disjoint by construction).** Both
bands carry the same pre-registered VALIDITY CONJUNCT: "AND fewer than 1/4 of the 32
main-leg runs at τ = 3/10 are cap-censored" — a band whose conjunct fails cannot fire,
and the outcome falls through to NULL with non-convergence the named binding axis.

- **REJECT** ("amplification absent on this conservative dynamics — the tipping story
  is a parameterization artifact here, not a law"): the seed-20261297 median s(3/10)
  < 11/20 — the outcome is statistically near the well-mixed baseline (≈ 1/2), i.e.
  the mild preference produced at most mild sorting. Checked FIRST — the costly-error
  rationale: REJECT kills the head outright (the folk claim fails at its own showcase
  threshold), so the protect-against-false-life arm cannot be shadowed by an eager
  APPROVE.
- **APPROVE** ("mild preference, strong segregation — the tipping claim survives its
  conservative parameterization"): the seed-20261297 median s(3/10) ≥ 7/10 AND the
  seed-20261298 stability leg reproduces the SAME ruling under the identical rule (its
  own median ≥ 7/10 and its own validity conjunct passing). An agent content at 30%
  like-neighbors ends up with ≥ 70% — more than double its demand.
- **NULL** (anything else — a legitimate, reportable outcome): the citable pin is then
  the measured s(τ) curve and the named BINDING AXIS — the pre-registered candidates:
  (i) band straddle, median ∈ [11/20, 7/10) — real but sub-"strong" sorting; (ii)
  non-convergence — the validity conjunct fails at the decision cell (dynamics not
  settled at cap 500; s is then cap-censored evidence, not a fixation measurement);
  (iii) stability non-reproduction — the 20261298 leg lands a different ruling; and
  (iv) the vacancy-fraction sensitivity flip — the reporting leg's 1/20 / 1/5 vacancy
  cells landing on opposite sides of a band edge names vacancy supply as the binding
  axis (reporting-only: it CANNOT flip the decision, it names the axis). **Cheapest
  live probe, named:** re-run ONLY the τ = 3/10 decision cell at sweep cap 2,000 on
  the reserved aux seed 20261300 — one cell, zero new tooling — settling the
  non-convergence axis before the band is re-litigated.

**Band liveness (disclosed — the P034/P035/P036 discipline, honestly weaker here by the
domain's nature).** NO closed form decides any band: Schelling dynamics have no
analytic fixation distribution, and this file deliberately pins NO expected landing.
All three rulings are reachable: REJECT is live because this parameterization is
conservative on purpose — at τ = 3/10 the large majority of randomly placed agents
start satisfied (a 50/50 neighborhood clears 0.30 easily), movers relocate to UNIFORM
vacancies (not preference-seeking ones), and the 10% vacancy pool is thin, so the
dynamics can freeze close to the mixed start; APPROVE is argued by the classic
qualitative results (unsatisfied-agent churn seeds like-clusters whose boundaries
recruit); NULL has four pre-registered shapes named above, and small-grid/high-vacancy/
low-cap variants are exactly the reporting legs. Whichever way it lands, the s(τ)
curve across all seven cells is the durable side pin.

**What a reader DOES differently on the verdict.**

- **APPROVE** → the tipping story may be cited with a measured, conservative pin
  attached: even uniform-relocation dynamics with 10% vacancies more than doubles a
  0.30 demand into ≥ 0.70 like-neighborhoods; any fleet prose invoking
  "emergent segregation" cites the measured s(0.30) and the s(τ) curve, not the
  folklore.
- **REJECT** → the popularized claim loses its unqualified citation rights in fleet
  prose: amplification at the showcase threshold is a property of kinder
  parameterizations (preference-seeking moves, fatter vacancy pools), and any future
  use of the story must name which lever does the work — with the follow-up head
  (destination-rule flip, below) the natural next measurement.
- **NULL** → the conditional finding ships: the binding axis (straddle /
  non-convergence / stability / vacancy) is named, the s(τ) curve is the citable pin,
  and the aux-seed cap-2,000 probe is the pre-priced next step; neither soundbite may
  be cited as settled.

**Gates (run invalid on any failure).**

- **Hand fixture:** a pinned 4×4 torus configuration with hand-computed occupied/like
  counts for all 16 cells, verified exactly at startup (guards neighborhood + wrap
  arithmetic).
- **τ = 0 control leg** (main seed, M = 32): no agent is ever unsatisfied (like·den ≥ 0
  always) → EXACTLY zero relocations (identity), and every run's initial-placement s
  must land in [47/100, 53/100] — the measured well-mixed baseline anchoring the
  REJECT band's "near baseline" reading.
- **Conservation identity:** type-A/type-B/vacant counts recounted at every sweep end —
  must equal 720/720/160 exactly.
- **Fixation certification:** every fixation-terminated run is re-verified by an
  INDEPENDENTLY WRITTEN satisfaction function scanning all agents at termination —
  zero unsatisfied required (the twin-evaluator discipline applied to the physics, not
  just the decision).
- **Monotonicity audit (reporting, flagged loudly on violation):** the main-leg mean
  s(τ) is expected non-decreasing in τ across {1/8 … 1/2}; a violation does not
  invalidate (high-τ non-convergence can bend it) but is printed as a first-class
  anomaly line.
- **Per-leg draw-count sentinels**, **twin independently-written decision evaluators**,
  **stdout + results.json byte-identical across two process runs**, **CPython minor
  pinned** — the P017–P039 standing battery.

**Reporting-only legs (seed 20261299 and labeled main-leg columns — CANNOT flip the
decision):** the full s(τ) curve over all seven cells; satisfied-agent fraction and
interface density (unlike occupied-adjacent pairs / all occupied-adjacent pairs) at
termination; sweeps-to-fixation quartiles and cap-hit counts per cell; the VACANCY
sensitivity pair — vacancy fraction ∈ {1/20, 1/5} at τ = 3/10 (populations 760/760/80
and 640/640/320), M = 16 each; the GRID sensitivity cell — N = 25 (625 cells,
281/281/63 via the same 45/45/10 rounding rule ⌊0.45·N²⌋ with the remainder to
vacancies) at τ = 3/10, M = 16. Aux seed 20261300 is reserved and never read by any
decision number.

**Grounding / hermeticity.** ZERO network reads at verdict time AND zero repo reads —
the entire world (grid size, counts, τ grid, seeds, bands, sweep cap, the 4×4 hand
fixture) is constructed in-sim from the pinned constants in this file, committed as a
small fixture JSON alongside one stdlib file. Decision arithmetic exact
`fractions.Fraction` at the measurement points (per-run s, medians, band comparisons);
the inner loop is pure integer/list work. Feasibility arithmetic: one sweep ≈ 1,440
live evaluations × 8 neighbor reads ≈ 12k reads; the main leg is 7 × 32 = 224 runs,
worst case (every run capping at 500 sweeps) ≈ 1.4 × 10⁹ neighbor reads — tens of
minutes in pure CPython at the absolute worst; typical far less (low-τ cells fixate in
tens of sweeps; the high-τ cells are the only plausible cappers and they are
reporting-only). No dependencies.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the outbox (PROPOSALs 001–039): nothing adjacent by DOMAIN — no proposal touches
  spatial self-organization, residential dynamics, agent relocation, or any
  lattice/grid statistical model. Nearest by SLOT: PROPOSAL 024 (Braess paradox →
  V026 null) — also a "individually rational choices produce a collectively perverse
  outcome" head, but that is NETWORK FLOW EQUILIBRIUM (Wardrop equilibria on a
  four-edge routing graph, exact Fraction census) versus SPATIAL RELOCATION DYNAMICS
  (stochastic serial updating on a torus to fixation): zero shared machinery, fixture,
  metric, or consumer. Nearest by SHAPE/METHOD: PROPOSALs 017/024 (the seeded
  Monte-Carlo arm with registered bands and honest-NULL), PROPOSAL 039 (a seeded
  dynamics census over a fully-pinned per-step update loop with policy/leg grids —
  method precedent only, different repo-world entirely), and PROPOSAL 038 (exact-
  Fraction decision numbers riding a seeded arm). No shared domain with any of them.
- vs superficial rhymes, checked by name: PROPOSAL 019's backlog low-water THRESHOLD
  and PROPOSAL 037's review-queue row THRESHOLD are policy dials in queueing models —
  "threshold" as a knob, not emergent tipping; PROPOSAL 032's clustering is
  pattern-overlap algebra on coin words. The tree-wide dedup sweep
  `rg -i -g '!bootstrap.py' -g '!.substrate' 'schelling|segregation|tipping'` at the
  grounding pin (`ab66463`) returns ZERO hits — no prior art anywhere in ideas/,
  control/, .sessions/, or docs/.
- Runners-up this slice, weighed and dropped on merit: **boids/flocking emergence**
  (no crisp falsifiable folk CLAIM, and float geometry breaks the byte-identity
  discipline); **sandpile self-organized criticality** (the honest question is a
  power-law exponent — estimation machinery outweighs the head); **epidemic threshold
  on networks** (R₀ folklore is real but graph-neighborhood-shaped, sitting
  uncomfortably close to P024's network world); **Conway density/ash statistics** (no
  decision a reader acts on). Schelling won on: a named folk claim, a single scalar
  metric, stdlib-exact decision arithmetic, and a genuinely undecided landing.

## Model basis (declared model-dependence — the P024 discipline)

This verdict's numbers are CONDITIONAL on an embedded model, named up front:

- **(1) Statistical assumption:** the classic two-type Schelling frame — fixed 45/45/10
  composition, Moore-8 torus neighborhoods, a THRESHOLD (not graded) utility, and
  UNIFORM random relocation of unsatisfied agents in live random-serial order. The
  uniform-destination choice is the conservative one (a mover may land somewhere
  worse); the threshold form is Schelling's own; the torus removes boundary effects.
  The measured curve is a property of THIS frame.
- **(2) Single most-likely-to-flip alternative:** the DESTINATION RULE — letting movers
  relocate only to cells where they would be satisfied (the common textbook variant)
  is widely held to segregate harder and faster; "s(0.30) under satisfying-destination
  moves" is the natural follow-up head with the entire engine reusable. Softer flips,
  named as out of the registered scope: graded/continuous utilities, unequal group
  sizes, von Neumann neighborhoods, open boundaries, noise/temperature (Glauber-style
  regret moves), and swap (rather than vacancy) dynamics.

## Probe report battery (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide
> sweep `rg -i -g '!bootstrap.py' -g '!.substrate' 'schelling|segregation|tipping'`
> returned ZERO hits at the grounding pin (`ab66463`); PROPOSALs 001–039 re-read at
> HEAD before drafting, and the five prior rotation occupants (P017 social choice,
> P024 routing, P028 seeding, P032 pattern races, P036 optimal stopping) are all
> different domains. (b) **kill test NOT triggered** — no prior proposal, idea file,
> or session-card 💡 touches spatial self-organization, segregation dynamics, or
> lattice agent models. (c) **feasibility + liveness arithmetic checked** — runtime
> bounded in the preamble (worst case tens of minutes, stdlib only); liveness
> disclosed in its own subsection with NO expected landing pinned (no closed form
> exists; all three rulings reachable, the four NULL shapes named).

**1. What is this really?** A pre-registered MEASUREMENT of the most-cited emergence
parable in social science: does Schelling tipping actually fire at the
integration-compatible threshold τ = 0.30 on a deliberately CONSERVATIVE, fully-pinned
dynamics (uniform relocation, 10% vacancies, live random-serial order, 40×40 torus) —
the median terminal like-neighbor share s(0.30) over 32 registered-seed runs, judged
against exact-rational bands fixed before any code (REJECT < 11/20 first, APPROVE
≥ 7/10 with stability reproduction, NULL with four named binding axes), every decision
number an exact Fraction, byte-identical across two process runs.

**2. What is the possibility space?** (i) Don't run it — the round-6 unrelated slot
goes unserved and the rotation's standing rule is dead letter this cycle. (ii) Re-use
a prior round's domain — fails the owner's "rotate" ask (P017/P024/P028/P032/P036
occupy voting, routing, tournaments, pattern races, stopping). (iii) A literature
summary ("Schelling showed mild preferences segregate") — retells the parable,
measures nothing, pins no parameterization; the open question is whether THIS
conservative frame clears a band at THIS threshold. (iv) An exact closed-form arm —
unavailable by the domain's nature (no analytic fixation distribution); the honest
compensations are the identity gates, the τ = 0 measured baseline, the stability leg,
and byte-identity. (v) This head: seeded census on a committed grid, REJECT-first
bands, four pre-registered NULL shapes, sensitivity legs quarantined as
reporting-only. (vi) Over-scope (destination-rule variants, graded utilities, unequal
groups, noise dynamics, global segregation indices as decision metrics) — each named
in `## Model basis` or the measurement boundary as a follow-up or out-of-scope flip.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~300-line stdlib file: a list-of-ints grid, an 8-offset toroidal neighbor table
precomputed once, one `random.Random` per leg, `fractions.Fraction` only at the
per-run measurement point. That single file yields a quantitative, reproducible ruling
on the century's most-quoted agent-based model at its showcase threshold — with the
full s(τ) response curve, vacancy/grid sensitivity, and fixation-time distributions as
free side pins — from a sim a verdict session runs cold in minutes to tens of minutes.

**4. What breaks it? (assumptions made explicit)** (a) **The frame is a choice** — the
`## Model basis` note names uniform-destination as the conservative pick and the
satisfying-destination flip as the follow-up; the bands quantify only over the pinned
frame. (b) **Band placement could cherry-pick** — both bands are committed in this
file BEFORE any code, are DISJOINT (11/20 < 7/10), NULL is first-class with four named
shapes, and NO expected landing is pinned (disclosed: no closed form exists to pin
one honestly). (c) **Cap-censoring could masquerade as evidence** — the validity
conjunct forces NULL when ≥ 1/4 of decision-cell runs cap out, and the named cheapest
probe (aux-seed cap 2,000, one cell) prices the fix. (d) **A physics bug** — the 4×4
hand fixture gates wrap arithmetic, the τ = 0 leg gates the no-move identity and the
measured baseline, conservation is recounted every sweep, and every fixation is
re-certified by an independently written satisfaction scan. (e) **Metric myopia** —
s is a LOCAL mixing metric; a reader wanting global cluster structure gets interface
density reporting-only, and the measurement boundary states that "strong segregation"
is operationalized as s ≥ 7/10 on THIS metric, nothing more.

**5. What does it unlock?** The pipeline's SIXTH fleet-external verdict and the
rotation lane's proof it spans domains (voting → routing → tournaments → pattern races
→ stopping → spatial self-organization); a measured, citable answer whenever the
"mild preferences, segregated outcomes" parable comes up — with the conservative
parameterization making an APPROVE unusually strong and a REJECT genuinely newsworthy;
the s(τ) response curve as a standalone side pin; and on any landing a pre-priced
follow-up head (the destination-rule flip) with the entire engine reusable.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external — by
design: no repo, no network, no dataset at verdict time; every fixture (grid size,
counts, τ grid as rationals, seeds 20261297–300, bands 11/20 · 7/10, cap 500, the
validity fraction 1/4, the hand fixture) is stated in this file and committed as a
small JSON alongside the sim. Kill tests, run live this slice: a prior
Schelling/segregation/spatial head anywhere in the tree (NOT found — sweep empty at
`ab66463`); an occupied round-6 unrelated slot (NOT found — P037/P038/P039 serve the
other three slots; no PROPOSAL 040 block, no P040 claim, no open PR at drafting);
infeasible runtime (NOT found — arithmetic in the preamble); a seed collision (NOT
found — 20261297–300 strictly above the P039 high-water 20261296, re-checked across
all prior blocks). Sim-worthy or judgment-only: sim-worthy — the entire question is a
computable median against pre-registered thresholds; the one judgment call (are 11/20
and 7/10 the RIGHT band edges for "near baseline" and "strong"?) is pinned by
pre-registration and stated as the thing a reader may dispute — about the bands,
never about the measured numbers.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs it (its harness, its verdict grammar; the sim file + fixture JSON committed in
its sims/ tree per convention). No fleet lane consumes the verdict as a build input —
the consumer is the owner/manager as READERS (plus, incidentally, any future
mechanic or workflow that ever leans on an emergence/tipping narrative — spatial
clustering in game maps, community-formation stories — which would inherit the
measured curve for free). Duplicates nothing: the domain sweep found zero prior
spatial-dynamics art in this tree, and no sim-lab verdict through the current ledger
touches lattice models or segregation dynamics.

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one stdlib file
(engine + gates + twin evaluators), one fixture JSON ({N = 40, counts 720/720/160,
Moore-8 torus, the τ grid {1/8, 1/4, 3/10, 3/8, 1/2, 5/8, 3/4}, satisfaction ≥ with
the vacuous-satisfaction convention, sweep cap 500, M = 32/16, seeds 20261297–300,
bands 11/20 · 7/10, validity fraction 1/4, the vacancy pair {1/20, 1/5}, the N = 25
cell, the 4×4 hand fixture}, values copied verbatim from this file), one results
table {per (τ, leg): the 32-run s values, median, satisfied fraction, interface
density, sweeps-to-fixation quartiles, cap-hit count; the sensitivity cells; the gate
outcomes} ending in exactly one of APPROVE / REJECT / NULL per the pre-registered
rule — reproducible from the fixtures alone, byte-identical on re-run (single-
generator pinned draw order, exact rationals at every decision point, CPython minor
pinned), no flags.

**Recommendation: sim-ready** — the question is crisp and completely computable, the
bands and decision rule are registered above BEFORE any code exists with the two
decision bands disjoint by construction and the liveness disclosure honest about the
one thing this domain cannot supply (no closed form, therefore NO pinned expected
landing — only the four named NULL shapes), both genre failure modes are pre-empted
(model-dependence → a deliberately conservative pinned frame + the `## Model basis`
declaration + a first-class NULL; stochastic error → registered seeds, a stability
leg that must reproduce the ruling, identity gates, a measured baseline, twin
evaluators, two-process byte-identity), and the verdict changes what a reader may
cite in every branch. THE ONE QUESTION for the simulator: *Under the pinned Schelling
frame (40×40 torus, 720/720/160 A/B/vacant, Moore-8, satisfaction = like-fraction
among occupied neighbors ≥ τ with zero-occupied-neighbors ⇒ satisfied, live
random-serial sweeps with uniform-random vacant-cell relocation, fixation or cap 500,
stdlib `random.Random` with pinned draw order), what is the median terminal mean
like-neighbor share s(τ = 3/10) over M = 32 seed-20261297 runs — measured exactly (per-
run s an exact Fraction), swept reporting-only across τ ∈ {1/8, 1/4, 3/10, 3/8, 1/2,
5/8, 3/4} plus vacancy {1/20, 1/5} and N = 25 sensitivity cells on seed 20261299 —
and does it land (bands disjoint, REJECT stated first, both bands carrying the
< 1/4-cap-censored validity conjunct) REJECT ("amplification absent — near the
well-mixed baseline") iff median < 11/20, APPROVE ("mild preference, strong
segregation") iff median ≥ 7/10 AND the seed-20261298 stability leg (M = 16)
reproduces the same ruling, or NULL (anything else — binding axis named from the
pre-registered four: band straddle, non-convergence at the cap, stability
non-reproduction, vacancy-sensitivity flip; cheapest live probe: the τ = 3/10 cell
alone at cap 2,000 on aux seed 20261300)?* Done-when: the committed stdlib sim +
fixture JSON reproduce the full results table byte-identically across two process
runs, every gate passes (4×4 hand fixture, τ = 0 zero-move identity + baseline band
[47/100, 53/100], per-sweep conservation 720/720/160, independent fixation
re-certification, draw-count sentinels, twin decision evaluators), the stability leg
reproduces the ruling on any APPROVE, and the verdict issues exactly ONE of
APPROVE/REJECT/NULL per the pre-registered rule — stating the family-of-dynamics
boundary (THIS update rule/grid only; the satisfying-destination flip is the named
follow-up), the termination boundary (fixation-or-cap with the validity conjunct),
and the measurement boundary (s is a local mixing metric; "strong segregation" means
s ≥ 7/10 on this metric, global cluster indices reporting-only); honest-null
explicit: a NULL lands as a finalized verdict naming the binding axis and the
pre-priced probe, not a re-run request.
