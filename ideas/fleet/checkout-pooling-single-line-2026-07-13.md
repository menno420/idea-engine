# Checkout pooling priced at its showcase load — does ONE shared line really beat per-register lines by ≥ 2× at ρ = 9/10?

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain
> slot, round 7; the domain itself is stochastic service operations / queue-discipline
> design — the supermarket checkout pooling question from the operations-management
> canon — fleet-external by design and DIFFERENT from round 1's social choice
> (PROPOSAL 017), round 2's congestion routing (PROPOSAL 024), round 3's tournament
> seeding (PROPOSAL 028), round 4's pattern races (PROPOSAL 032), round 5's optimal
> stopping (PROPOSAL 036), and round 6's spatial self-organization (PROPOSAL 040), so
> the rotation now spans SEVEN domains) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/idea-engine@3e47fadffab9d0586fa3fa31319dde442ac761c9 · fetched 2026-07-13T19:31:07Z
> (the dedup-sweep pin — this repo's own tree at drafting HEAD, the only read this head
> takes; the sim itself is fully hermetic: zero repo/network reads at verdict time,
> every fixture constructed in-sim from the pinned constants in this file)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous pipeline —
"continue coming up with new ideas, that is your main purpose"), the rotation established
by ORDER 004 rule 3 ("fleet backlogs → venture's book/product space → game mechanics →
COMPLETELY UNRELATED domains") — round 7's other three slots are already served (fleet
backlogs → PROPOSAL 041, venture → PROPOSAL 042, game mechanics → PROPOSAL 043), so this
slice closes the round at the unrelated slot; PROPOSAL 017 opened the lane with social
choice, PROPOSAL 024 rotated it into congestion routing, PROPOSAL 028 into
tournament-format design, PROPOSAL 032 into pattern-race probability, PROPOSAL 036 into
sequential search / optimal stopping, PROPOSAL 040 into emergent spatial
self-organization; this is round 7's closer, rotated into a SEVENTH fleet-external domain
(stochastic service operations / queue-discipline design). **Placement note
(decide-and-flag):** sections are roster-derived and inventing one ad hoc is forbidden
(README § Sections; `check_sections.py` reds an ORPHAN section against the live roster),
and that checker's own carve-out rules that sim-lab-shaped ideas "ride `ideas/fleet/` or
the proposing section" — so this fleet-external head lives here, flagged rather than
silently squatting, exactly as PROPOSALs 017, 024, 028, 032, 036, and 040 did.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The folk belief.** "One line, many registers" is the most repeated piece of applied
queueing folklore in existence: banks, airports, and every operations-management course
teach that a SINGLE shared FIFO line feeding all c registers dramatically beats one
line per register — the pooled system wastes no server on an empty local line while
another line backs up, and no customer gets stuck behind one slow transaction while an
adjacent register sits idle. The strong popular form says the improvement is not
marginal but dramatic — at busy-hour loads, several-fold. The settled part is the
qualitative direction (pooling helps; continuous-time M/M/c theory and every textbook
say so). The measured unknown is the MAGNITUDE on a fully-pinned, deliberately
conservative DISCRETE frame: Bernoulli-per-tick arrivals (at most ONE arrival per tick
— strictly less bursty than the Poisson stream the textbook ratio is derived from),
a LOW-VARIABILITY integer service pmf (squared coefficient of variation 41/245 ≈ 0.17,
far below the exponential's 1 — short queues everywhere, less room for pooling to
shine), a finite measured window with warm-up, and waits counted in whole ticks. NO
closed form decides this frame: the Pollaczek–Khinchine formula is a Poisson/
continuous-time result that does not bind a Bernoulli-arrival discrete-tick system,
and the pooled multi-server general-service queue has no exact closed form even in
continuous time. Whether the folk law's "≥ 2× better" survives THIS conservative frame
at the showcase load ρ = 9/10 is genuinely open — REJECT, APPROVE, and NULL are all
live and only the run settles it. This mirrors the accepted
P017/P024/P028/P032/P036/P040 pattern: the effect is settled in principle; its
magnitude on a committed, fully-pinned frame at the committed operating point is the
unknown.

**The model (fixed, fully pinned — every constant a decision of this file, none left
to the implementer).**

- **Time:** discrete ticks t = 0, 1, 2, …; arrivals stop after tick T − 1 with
  T = 20,000; the system then DRAINS to empty (no censored waits — every customer's
  wait is an exactly measured integer). Absolute drain cap: a run still non-empty at
  tick 80,000 is INVALID (see validity).
- **Registers:** c = 3 identical servers, indices 0/1/2.
- **Arrival stream (per tick):** exactly one draw `rng.randrange(35)`; an arrival
  occurs iff the draw < A. The DECISION cell is A = 27; the reporting load sweep is
  A ∈ {21, 24, 30}. With mean service 7/2 this gives EXACT utilizations
  ρ = (A/35)·(7/2)/3 = A/30 ∈ {7/10, 4/5, 9/10, 1} — the A = 30 cell is the
  saturation boundary, reporting-only by construction.
- **Service pmf (integer ticks):** S ∈ {2, 3, 4, 6} with weights {3, 3, 2, 2} out of
  10 — drawn per arrival as `u = rng.randrange(10)`: u < 3 → 2, u < 6 → 3, u < 8 → 4,
  else 6. Mean E[S] = 7/2 exactly; E[S²] = 143/10; variance 41/20; SCV = 41/245
  (all exact rationals, pinned here so the gates can assert them from the fixture).
- **Queue label (per arrival):** one `rng.randrange(3)` — consumed by EVERY arrival
  in the stream (so the stream is configuration-independent), USED only by
  SPLIT-RANDOM, ignored by the other configurations.
- **Common random numbers, pinned:** the per-run stream (arrival flags, service
  times, queue labels) is generated ONCE from the run's draws and fed IDENTICALLY to
  all three configurations — the per-run ratio compares the same customers under
  different disciplines. RNG = stdlib `random.Random(seed)`, ONE generator per leg,
  runs drawn sequentially in pinned loop order, draws per tick in pinned order
  (arrival draw → if arrival: service draw → label draw). Per-run draw-count
  sentinel: exactly T + 2·(number of arrivals) draws.
- **Tick semantics (identical across configurations, pinned):** at each tick t —
  (1) COMPLETIONS: a customer that started service at tick s with service S occupies
  its server for ticks s .. s+S−1; the server is free to pull again from tick s+S;
  (2) ARRIVAL: the tick-t arrival (if any) is appended to its queue;
  (3) STARTS: idle servers scanned in index order 0, 1, 2, each pulling the head of
  its queue (POOLED: the single shared queue); the pulled customer's WAIT =
  t − arrival_tick (an integer ≥ 0; same-tick start = wait 0).
- **The three configurations:**
  - **POOLED** (decision arm): ONE shared FIFO queue; any idle server pulls its head.
  - **SPLIT-RANDOM** (decision arm): three FIFO queues, one per register; each
    arrival joins the queue named by its stream label; no jockeying, no switching —
    the naive "pick a line at random and stay in it" shopper.
  - **SPLIT-JSQ** (reporting-only): three FIFO queues; each arrival joins the queue
    with the fewest customers COUNTING the one in service at that register; ties →
    lowest index; the stream label is ignored. This is the informed shopper — it
    rides along to price the folk corollary "it's not the shared line, it's picking
    the short one", and it CANNOT flip the decision.
- **Runs:** M = 32 runs at the decision cell on the main leg; M = 16 on the
  stability leg; M = 16 per load cell on the reporting leg. Pinned loop order: cells
  in ascending A, run index 0 .. M−1 within a cell, all runs of a leg drawn from
  that leg's single generator in pinned order.

**Primary metric.** Per run and configuration: the MEASURED COHORT is every customer
whose arrival tick lies in [2,000, 20,000) — the first 2,000 ticks are warm-up,
excluded; because the run drains to empty, every cohort customer's wait is measured
exactly (no censoring). Ŵ(config) = the cohort mean wait, an exact
`fractions.Fraction` (integer wait sum / cohort count). The per-run DECISION RATIO is
R = Ŵ(SPLIT-RANDOM) / Ŵ(POOLED) — same stream, same customers, an exact rational.
The decision number is the MEDIAN of the valid main-leg runs' R values at the
decision cell A = 27 (median of an even count = the mean of the two middle order
statistics; of an odd count = the middle — still an exact rational, compared to
exact-rational bands).

**Per-run validity (pinned):** a run is INVALID iff (a) it fails to drain to empty
before absolute tick 80,000, or (b) its POOLED cohort mean wait is exactly 0 (the
ratio is then undefined — disclosed degenerate case; at ρ = 9/10 over 18,000 ticks
this is a pathology guard, not an expected event). Invalid runs contribute no ratio;
the leg's median is over its valid runs.

**Seeds (registered):** 20261313 (main decision leg, A = 27, M = 32) / 20261314
(stability leg, A = 27, M = 16, must reproduce the ruling for any APPROVE) /
20261315 (reporting leg — the load sweep A ∈ {21, 24, 30}, M = 16 per cell) /
20261316 (aux — NEVER read by any decision number; reserved for the named NULL
probe). Allocated strictly above the P043 registry high-water 20261312, re-checked
tree-wide at drafting HEAD `3e47fad` (`rg -o -g '!bootstrap.py' -g '!.substrate'
'202613[0-9][0-9]'` maxes at 20261312). Byte-identity: stdout + results.json
byte-identical across two process runs; CPython minor version pinned in the fixture.

**Pre-registered decision rule (fixed BEFORE any code exists; evaluated in this
order, REJECT FIRST; bands exact rationals 3/2 and 2, disjoint by construction).**
Both bands carry the same pre-registered VALIDITY CONJUNCT: "AND fewer than 1/4 of
the leg's runs are invalid" — a band whose conjunct fails cannot fire, and the
outcome falls through to NULL with settlement failure the named binding axis.

- **REJECT** ("the pooling folk law fails at its own showcase load on this
  conservative frame — the dramatic-improvement story is a parameterization
  artifact of burstier arrivals and fatter service tails, not a law"): the
  seed-20261313 median R < 3/2 — random-split waits are less than 1.5× pooled
  waits. Checked FIRST — the costly-error rationale: REJECT kills the head outright
  (the folk claim fails where it is supposed to shine), so the
  protect-against-false-life arm cannot be shadowed by an eager APPROVE.
- **APPROVE** ("one line, many registers — the folk law survives its conservative
  parameterization"): the seed-20261313 median R ≥ 2 AND the seed-20261314
  stability leg reproduces the SAME ruling under the identical rule (its own median
  ≥ 2 and its own validity conjunct passing). Pooling at least HALVES the measured
  wait of the identical customer population at ρ = 9/10.
- **NULL** (anything else — a legitimate, reportable outcome): the citable pin is
  then the measured R(ρ) curve and the named BINDING AXIS — the pre-registered
  candidates: (i) band straddle, median R ∈ [3/2, 2) — pooling helps but short of
  the folk "dramatic"; (ii) settlement failure — the validity conjunct fails at the
  decision cell (drain-cap or degenerate-denominator pathologies); (iii) stability
  non-reproduction — the 20261314 leg lands a different ruling; (iv) the
  load-sensitivity flip — the reporting cells ρ = 7/10 and ρ = 4/5 landing on
  opposite sides of a band edge names LOAD as the binding axis (reporting-only: it
  CANNOT flip the decision, it names the axis). **Cheapest live probe, named:**
  re-run ONLY the A = 27 decision cell at T = 100,000 (horizon ×5, same warm-up
  fraction: cohort [10,000, 100,000), drain cap 400,000) on the reserved aux seed
  20261316 — one cell, zero new tooling — settling whether the finite window is
  doing the work before the band is re-litigated.

**Band liveness (disclosed — the P034/P035/P036/P040 discipline).** NO closed form
decides any band on THIS frame: Pollaczek–Khinchine and Erlang-C price the
CONTINUOUS-TIME Poisson cousins, not a Bernoulli-per-tick lattice system, and the
pooled 3-server general-service queue lacks a closed form even there. The
continuous cousins are honest heuristic anchors, disclosed as non-binding: a P–K
estimate for each split line at ρ = 9/10 gives ≈ 18.4-tick waits, and an
Erlang-C-with-SCV-correction estimate for the pooled side gives ≈ 5.6 ticks —
ratio ≈ 3.3, arguing APPROVE. REJECT is live because every conservative choice cuts
the split side's queueing more than the pooled side's: at most one arrival per tick
kills arrival bursts (the split system's pain is a burst landing on one line),
the low-SCV service pmf (41/245 vs the exponential's 1) shrinks all queues toward
the deterministic-service regime where both systems run lean, and integer-tick
waits at single-digit magnitudes leave room for granularity to compress measured
ratios. NULL has four pre-registered shapes named above. This file pins NO expected
landing; whichever way it lands, the R(ρ) curve plus the JSQ column is the durable
side pin.

**What a reader DOES differently on the verdict.**

- **APPROVE** → the pooling folk law may be cited with a measured, conservative pin
  attached: even a low-variability, burst-free discrete frame at least halves waits
  at ρ = 9/10; any fleet prose invoking "pool the servers / one queue not three"
  (worker dispatch, review queues, CI runners) cites the measured R(9/10) and the
  R(ρ) curve, not the folklore.
- **REJECT** → the unqualified citation dies: the dramatic advantage is a property
  of bursty-arrival, high-variability parameterizations, and any future use of the
  story must name which lever does the work (burstiness or service variability) —
  with the JSQ column and the named follow-up (the SCV sweep, below) the natural
  next measurement.
- **NULL** → the conditional finding ships: the binding axis (straddle / settlement
  / stability / load) is named, the R(ρ) curve is the citable pin, and the aux-seed
  horizon-×5 probe is the pre-priced next step; the soundbite may not be cited as
  settled either way.

**Gates (run invalid on any failure).**

- **Hand fixture (pinned in this file, verified exactly at startup):** the 8-tick
  stream — arrivals at ticks {0, 1, 2, 3, 5, 7} with service times {4, 3, 2, 6, 2, 3}
  and queue labels {0, 0, 1, 0, 2, 1}, no warm-up, drain to empty — must reproduce,
  under the tick semantics above, EXACTLY: POOLED per-customer waits (0, 0, 0, 1, 0, 0),
  mean 1/6; SPLIT-RANDOM waits (0, 3, 0, 4, 0, 0), mean 7/6; SPLIT-JSQ waits
  (0, 0, 0, 1, 0, 0), mean 1/6 (JSQ routes the six customers to queues 0, 1, 2, 0, 1, 1
  under the counting-in-service + lowest-index tie rule). The fixture's ratio
  R = 7 also exercises the ratio arithmetic.
- **A = 0 control leg** (main seed, M = 4): zero arrivals → zero starts, zero busy
  ticks, draw sentinel EXACTLY T (identity of the arrival machinery).
- **Work-conservation identity:** per run and configuration, the sum of service
  times of all started customers = total busy server-ticks, exactly.
- **Stream identity across configurations:** all three configurations of a run must
  report the identical arrival count and identical service-time sum (they consumed
  the same stream).
- **Cohort conservation:** cohort arrivals = cohort served, exactly (drain-to-empty
  makes this an identity; a mismatch is a bug, not noise).
- **Pooled-dominance audit (reporting, flagged loudly on violation, never
  invalidating):** per run, Ŵ(POOLED) ≤ Ŵ(SPLIT-RANDOM) is expected but is NOT a
  samplewise theorem on a discrete tie-broken frame — a violating run prints a
  first-class anomaly line with its seed offset.
- **Monotonicity audit (reporting, flagged loudly):** per configuration, the mean
  cohort wait is expected non-decreasing in A across {21, 24, 27}; a violation does
  not invalidate but is printed as a first-class anomaly line.
- **Per-leg draw-count sentinels** (T + 2·arrivals per run), **twin
  independently-written decision evaluators**, **stdout + results.json
  byte-identical across two process runs**, **CPython minor pinned** — the
  P017–P043 standing battery.

**Reporting-only legs (seed 20261315 and labeled main-leg columns — CANNOT flip the
decision):** the full R(ρ) curve over A ∈ {21, 24, 27, 30} (the A = 30 saturation
cell disclosed as boundary behavior — expect long drains; its validity flags are
reported, and it sits outside every band by construction); the JSQ column — the
median of Ŵ(SPLIT-JSQ)/Ŵ(POOLED) per cell, pricing the "informed shopper recovers
pooling" corollary; per-cell mean and p95 cohort wait per configuration (p95 = the
⌈0.95·n⌉-th smallest wait, an integer order statistic); maximum queue length;
server-utilization fractions (busy ticks / (3 · elapsed ticks), exact Fractions);
drain lengths. Aux seed 20261316 is reserved and never read by any decision number.

**Grounding / hermeticity.** ZERO network reads at verdict time AND zero repo reads
— the entire world (c, T, the arrival denominators, the service pmf, the load grid,
seeds, bands, warm-up, drain cap, the 8-tick hand fixture with its three
hand-computed wait tables) is constructed in-sim from the pinned constants in this
file, committed as a small fixture JSON alongside one stdlib file. Decision
arithmetic exact `fractions.Fraction` at the measurement points (per-run means,
ratios, medians, band comparisons); the inner loop is pure integer/list work.
Feasibility arithmetic: one run ≈ 20,000 ticks + drain, three configurations ≈
70,000 tick-steps of O(c) work; the full battery (32 + 16 + 3×16 + control runs ≈
100 runs) ≈ 10⁷ elementary steps — well under a minute in CPython; the worst case
(saturation-cell drains) adds seconds. No dependencies.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the outbox (PROPOSALs 001–043): nothing prior occupies SERVICE-DISCIPLINE
  DESIGN — no proposal compares queue configurations, prices resource pooling, or
  touches multi-server waiting systems. Nearest by MACHINERY, checked by name:
  PROPOSAL 033 (assign-at-merge queue tax → V035 null) builds a SINGLE-server FIFO
  event sim of the fleet's merge pipeline with P–K/M/M/1 closed forms as gates —
  its question is a fleet-internal BUILD-COST frontier (is the Option-3 mechanism
  worth its CI tax), not a discipline comparison; zero shared fixtures, metrics,
  bands, or consumers — method precedent only, exactly as PROPOSAL 039 was for
  PROPOSAL 040. PROPOSALs 019 and 037 tune alarm THRESHOLDS on fleet workflow
  backlogs ("queue" as a to-do list and a dial on it, not queueing dynamics);
  PROPOSAL 040's own rhyme check already classified them so. The Braess head
  (P024) prices selfish ROUTING on a congestion network — equilibrium flow
  assignment, no waiting-line dynamics, no servers.
- Dedup sweep at the grounding pin (`3e47fad`): `rg -i -g '!bootstrap.py' -g
  '!.substrate' 'supermarket|checkout pool|single shared line|shortest queue|JSQ|
  jockey|erlang'` (the erlang/jockey/JSQ terms are this domain's fingerprints)
  returns ZERO hits; `rg -i 'pooled|pooling'` hits only P034's "pooled paradox
  frequency" (statistical pooling of Braess fixture results — a different sense of
  the word) — no prior art anywhere in ideas/, control/, .sessions/, or docs/.
- Runners-up this slice, weighed and dropped on merit: **inspection paradox / bus
  waiting** (the stationary answer E[H²]/2E[H] is a one-line closed form — no live
  REJECT); **birthday-collision scheduling** (fully closed-form, nothing a sim
  settles); **Benford first digits** (the crisp exact-census version has no
  falsifiable folk claim a reader ACTS on, and the stochastic version's decision
  arithmetic goes float); **auction format comparison** (discrete-value equilibria
  need computed mixed strategies — the machinery outweighs the head, and the
  mechanism-design flavor sits uncomfortably near P017's social-choice world);
  **epidemic thresholds** (already weighed and dropped by P040 as too close to
  P024's network world — the recorded reasoning stands). Checkout pooling won on:
  a named folk claim everyone repeats, a single scalar decision ratio, stdlib-exact
  integer/rational arithmetic end-to-end, and a genuinely undecided landing on the
  committed conservative frame.

## Model basis (declared model-dependence — the P024/P040 discipline)

This verdict's numbers are CONDITIONAL on an embedded model, named up front:

- **(1) Statistical assumption:** the discrete-time service frame — Bernoulli
  arrivals (≤ 1 per tick), the pinned 4-point low-SCV service pmf, FIFO within
  every queue, no jockeying/reneging/balking, identical servers, and the
  common-random-numbers pairing that makes the per-run ratio exact. Every choice is
  the conservative one for the claim under test (less burstiness and less service
  variability both SHRINK the pooling advantage); the measured curve is a property
  of THIS frame.
- **(2) Single most-likely-to-flip alternative:** SERVICE VARIABILITY — re-running
  the identical battery with a high-SCV service pmf (same mean 7/2, fat tail; e.g.
  {2:8, 14:2}/10, SCV ≈ 1.9) is widely held to blow the ratio far open; "R(9/10)
  as a function of service SCV" is the natural follow-up head with the entire
  engine reusable. Softer flips, named as out of the registered scope: bursty/
  batch arrivals, jockeying (which empirically drags split systems toward pooled),
  customer abandonment, heterogeneous servers, priority classes, and
  time-varying arrival rates.

## Probe report battery (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide
> sweep quoted in `## Relations` returned ZERO domain hits at the grounding pin
> (`3e47fad`); PROPOSALs 001–043 re-scanned at HEAD before drafting, and the six
> prior rotation occupants (P017 social choice, P024 routing, P028 seeding, P032
> pattern races, P036 optimal stopping, P040 spatial self-organization) are all
> different domains; the nearest-machinery head P033 (merge-queue tax, single
> server, build-cost frontier) is disclosed in `## Relations`. (b) **kill test NOT
> triggered** — no prior proposal, idea file, or session-card 💡 touches
> queue-discipline comparison, resource pooling, or multi-server waiting systems.
> (c) **feasibility + liveness arithmetic checked** — runtime bounded in the
> preamble (under a minute, stdlib only); liveness disclosed in its own subsection
> with NO expected landing pinned (the continuous-time anchors are named as
> non-binding heuristics; all three rulings reachable, the four NULL shapes named).

**1. What is this really?** A pre-registered MEASUREMENT of the most-repeated piece
of applied queueing folklore: does the single-shared-line advantage actually reach
"dramatic" (operationalized: ≥ 2×) at the showcase load ρ = 9/10 on a deliberately
CONSERVATIVE fully-pinned discrete frame (burst-free Bernoulli arrivals, low-SCV
integer service, 3 registers, drain-to-empty exact waits) — the median per-run
common-random-numbers wait ratio R = Ŵ(SPLIT-RANDOM)/Ŵ(POOLED) over 32
registered-seed runs, judged against exact-rational bands fixed before any code
(REJECT < 3/2 first, APPROVE ≥ 2 with stability reproduction, NULL with four named
binding axes), every decision number an exact Fraction, byte-identical across two
process runs.

**2. What is the possibility space?** (i) Don't run it — the round-7 unrelated slot
goes unserved and the rotation closes short. (ii) Re-use a prior round's domain —
fails the owner's "rotate" ask (P017/P024/P028/P032/P036/P040 occupy voting,
routing, tournaments, pattern races, stopping, spatial self-organization). (iii) A
literature summary ("M/M/c beats c×M/M/1, see Erlang") — retells continuous-time
folklore, measures nothing on a committed frame, and the folk claim as lived is
about checkout LINES, not exponential idealizations. (iv) An exact closed-form arm
— unavailable by the frame's nature (no P–K for Bernoulli-lattice arrivals, no
closed form for pooled multi-server general service at all); the honest
compensations are the identity gates, the hand fixture, the CRN pairing, the
stability leg, and byte-identity. (v) This head: seeded CRN census over a pinned
discrete frame, REJECT-first bands on the median ratio, four pre-registered NULL
shapes, sensitivity legs quarantined as reporting-only. (vi) Over-scope (jockeying,
abandonment, batch arrivals, SCV sweeps, priority classes, time-varying rates) —
each named in `## Model basis` or the boundary statements as a follow-up or
out-of-scope flip.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~250-line stdlib file: a stream generator (three `randrange`
draw kinds in pinned order), one tick-loop engine parameterized by a routing rule
(pooled / label / JSQ — the ONLY code that differs between configurations), integer
waits, `fractions.Fraction` only at the per-run measurement point. That single file
yields a quantitative, reproducible ruling on the best-known service-design maxim
at its showcase load — with the full R(ρ) curve, the JSQ informed-shopper column,
p95 waits, and utilization/drain tables as free side pins — from a sim a verdict
session runs cold in under a minute.

**4. What breaks it? (assumptions made explicit)** (a) **The frame is a choice** —
`## Model basis` names every conservative pick and the service-SCV flip as the
follow-up; the bands quantify only over the pinned frame. (b) **Band placement
could cherry-pick** — both bands are committed in this file BEFORE any code, are
DISJOINT (3/2 < 2), NULL is first-class with four named shapes, and NO expected
landing is pinned (disclosed: the continuous anchors argue APPROVE but do not bind
this lattice frame). (c) **A finite-window artifact could masquerade as evidence**
— warm-up 2,000 ticks is excluded, drain-to-empty removes censoring entirely, the
validity conjunct forces NULL on drain pathologies, and the named cheapest probe
(aux-seed horizon ×5, one cell) prices the fix. (d) **A physics bug** — the 8-tick
hand fixture with three hand-computed wait tables gates the tick semantics, work
conservation and cohort conservation are exact identities, the stream-identity
gate proves all three configurations consumed the same customers, and the A = 0
control leg gates the arrival machinery. (e) **Metric myopia** — R is a MEAN-wait
ratio; a reader wanting tail behavior gets p95 columns reporting-only, and the
measurement boundary states that "dramatically better" is operationalized as
R ≥ 2 on cohort MEAN wait, nothing more.

**5. What does it unlock?** The pipeline's SEVENTH fleet-external verdict and the
rotation lane's proof it spans domains (voting → routing → tournaments → pattern
races → stopping → spatial self-organization → service operations); a measured,
citable answer whenever "one queue, many workers" comes up — which it does INSIDE
the fleet too (worker dispatch, shared review queues, CI runner pools all lean on
the pooling intuition); the R(ρ) curve and JSQ column as standalone side pins; and
on any landing a pre-priced follow-up head (the service-SCV sweep) with the entire
engine reusable.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external —
by design: no repo, no network, no dataset at verdict time; every fixture (c, T,
warm-up, drain cap, arrival denominators, the service pmf, the load grid, seeds
20261313–316, bands 3/2 · 2, the validity fraction 1/4, the 8-tick hand fixture
with its three wait tables) is stated in this file and committed as a small JSON
alongside the sim. Kill tests, run live this slice: a prior queueing-discipline or
pooling head anywhere in the tree (NOT found — sweep empty at `3e47fad`; P033/P019/
P037 classified and disclosed in `## Relations`); an occupied round-7 unrelated
slot (NOT found — P041/P042/P043 serve the other three slots; no PROPOSAL 044
block, no P044 claim, no open PR at drafting); infeasible runtime (NOT found —
arithmetic in the preamble); a seed collision (NOT found — 20261313–316 strictly
above the P043 high-water 20261312, re-swept tree-wide at drafting). Sim-worthy or
judgment-only: sim-worthy — the entire question is a computable median against
pre-registered thresholds; the one judgment call (are 3/2 and 2 the RIGHT edges
for "fails the folk law" and "dramatic"?) is pinned by pre-registration and stated
as the thing a reader may dispute — about the bands, never about the measured
numbers.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs it (its harness, its verdict grammar; the sim file + fixture JSON committed in
its sims/ tree per convention). No fleet lane consumes the verdict as a build input
— the consumer is the owner/manager as READERS (plus, concretely, any future fleet
design conversation about pooling workers, reviewers, or runners behind one queue,
which inherits the measured curve for free). Duplicates nothing: the domain sweep
found zero prior queue-discipline art in this tree, and the nearest-machinery head
(P033) prices a different question in a different world with a different consumer.

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one stdlib
file (stream generator + one routing-parameterized engine + gates + twin
evaluators), one fixture JSON ({c = 3, T = 20,000, warm-up 2,000, drain cap 80,000,
arrival denominator 35, the load grid A ∈ {21, 24, 27, 30} with the A = 27 decision
cell, the service pmf {2:3, 3:3, 4:2, 6:2}/10, seeds 20261313–316, bands 3/2 · 2,
the validity fraction 1/4, M = 32/16, the 8-tick hand fixture with its three
hand-computed wait tables}, values copied verbatim from this file), one results
table {per (A, leg, configuration): per-run cohort mean waits and ratios, the
median, p95, max queue length, utilization, drain length, validity flags; the JSQ
column; every gate outcome} ending in exactly one of APPROVE / REJECT / NULL per
the pre-registered rule — reproducible from the fixtures alone, byte-identical on
re-run (single-generator pinned draw order, exact rationals at every decision
point, CPython minor pinned), no flags.

**Recommendation: sim-ready** — the question is crisp and completely computable,
the bands and decision rule are registered above BEFORE any code exists with the
two decision bands disjoint by construction and the liveness disclosure honest
about what this domain cannot supply (no closed form binds the pinned lattice
frame — the continuous anchors are named as non-binding heuristics, NO expected
landing is pinned, and the four NULL shapes are named), both genre failure modes
are pre-empted (model-dependence → a deliberately conservative pinned frame + the
`## Model basis` declaration + a first-class NULL; stochastic error → registered
seeds, common random numbers pairing the configurations customer-for-customer, a
stability leg that must reproduce the ruling, identity gates, a hand fixture with
three hand-computed tables, twin evaluators, two-process byte-identity), and the
verdict changes what a reader may cite in every branch. THE ONE QUESTION for the
simulator: *Under the pinned discrete service frame (c = 3 registers; ticks with
completions → arrival → index-order starts; Bernoulli arrivals `randrange(35) < A`
with the decision cell A = 27 giving ρ = 9/10 exactly; service pmf
{2:3, 3:3, 4:2, 6:2}/10 with mean 7/2; per-arrival queue labels; one
`random.Random(seed)` per leg with pinned draw order and draw-count sentinels;
T = 20,000 with warm-up 2,000 and drain-to-empty, drain cap 80,000), what is the
MEDIAN over M = 32 seed-20261313 runs of the per-run common-random-numbers cohort
mean-wait ratio R = Ŵ(SPLIT-RANDOM)/Ŵ(POOLED) — measured exactly (integer waits,
exact-Fraction means and ratios), swept reporting-only across A ∈ {21, 24, 30} and
the SPLIT-JSQ configuration on seed 20261315 — and does it land (bands disjoint,
REJECT stated first, both bands carrying the < 1/4-invalid validity conjunct)
REJECT ("the pooling folk law fails at its showcase load on this conservative
frame") iff median R < 3/2, APPROVE ("one line, many registers — pooling at least
halves the wait") iff median R ≥ 2 AND the seed-20261314 stability leg (M = 16)
reproduces the same ruling, or NULL (anything else — binding axis named from the
pre-registered four: band straddle, settlement failure, stability
non-reproduction, load-sensitivity flip; cheapest live probe: the A = 27 cell
alone at horizon ×5 on aux seed 20261316)?* Done-when: the committed stdlib sim +
fixture JSON reproduce the full results table byte-identically across two process
runs, every gate passes (the 8-tick hand fixture's three wait tables exactly, the
A = 0 control identities, work conservation, stream identity across
configurations, cohort conservation, draw-count sentinels, twin decision
evaluators), the stability leg reproduces the ruling on any APPROVE, and the
verdict issues exactly ONE of APPROVE/REJECT/NULL per the pre-registered rule —
stating the frame boundary (results rule on THIS discrete frame only: burst-free
Bernoulli arrivals, the pinned low-SCV service pmf, FIFO, no jockeying — the
service-SCV sweep is the named most-likely-to-flip follow-up), the measurement
boundary ("dramatically better" is operationalized as R ≥ 2 on cohort MEAN wait;
p95 and JSQ columns ride reporting-only), and the load boundary (the decision is
the ρ = 9/10 cell; the R(ρ) curve and the ρ = 1 saturation cell are reporting-
only); honest-null explicit: a NULL lands as a finalized verdict naming the
binding axis and the pre-priced aux-seed probe, not a re-run request.
