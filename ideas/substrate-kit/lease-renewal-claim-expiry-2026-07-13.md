# Lease-renewal claim expiry — pin the `renewed:` slice's constants before the kit builds them

> **State:** sim-ready
> **Class:** process (pipeline rotation — inbox ORDER 004 rule 3's FLEET-BACKLOGS
> slot, round 4; round 1 harvested the websites backlog (P019 → V021 approve),
> round 2 the superbot backlog (P021 → V023 reject), round 3 the kit claims
> doctrine (P025 → V027 reject), and this round follows round 3's own
> verdict-opened thread — V027's routed-but-undesigned lease-renewal fix) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline);
> verdict consumer: `menno420/substrate-kit` — the lane V027 routed the
> lease-renewal slice to, which would otherwise build it around a fresh
> invented horizon (the exact failure class P025 just priced).

**Origin:** drafted this slice under standing owner ORDER 003 (continuous
pipeline; inbox @ HEAD: "continue coming up with new ideas, that is your main
purpose") in the FLEET-BACKLOGS rotation slot, round 4. The slot does NOT
rotate to a fourth harvest source this round, deliberately: P025's own
committed survey (its Origin section) found the fleet-slot-untapped sections
sim-dry by their own probes — "no sim-lab proposal — no simulator question" on
all six substrate-kit heads, "nothing sim-shaped" across superbot-next,
mineverse SECTION COMPLETE, product-forge 4/4 disposed — and that finding is
hours old, not stale. The slot's freshest genuinely sim-shaped material is the
thread its own round-3 entry opened: VERDICT 027 REJECTED silence-keyed claim
expiry ("silence is the wrong signal — route the lease-renewal slice") and
then, in its own LIMITS line, named exactly what remains unpriced: it "does
not design the renewal mechanism". This file designs and prices it — the
P023-after-V022 / P027-after-V025 / P026-after-V024 successor pattern (price
the routed lever before the build fixes it by accident), applied to the fleet
slot's own parent for the first time.

## The premise (pinned, verified this slice)

- **V027's routed fix is a mechanism with no constants.** VERDICT 027
  (sim-lab `control/outbox.md` @ fe51983, finalized 2026-07-13T05:23:41Z)
  rejected horizon tuning — Feas(cell) = ∅ in 6/9 cells on the exact arm — and
  routed: "claim bullets carry an explicit `renewed: <ISO8601>` field
  re-stamped each working wake, and `claims-stale` keys on missed renewals (a
  signal an alive-but-quiet lane CAN send and a dead lane CANNOT)". That
  sentence carries THREE unpinned design constants: the renewal cadence a lane
  must sustain, the expiry horizon on the renewal stream, and — the axis no
  prior grid has — the compliance the mechanism silently assumes. A lane that
  works but forgets to re-stamp is indistinguishable from a dead lane; the
  mechanism's whole win over silence-inference rides on lanes actually
  stamping. Nobody has priced how much forgetting the mechanism tolerates.
- **The build window is open.** V027 finalized ~05:24Z tonight; its routing is
  a manager-sweep relay (Q-0260 — this repo never edits kit files; the natural
  ride is the kit-lane fan-in bundle this section already tracks). No ORDER in
  this repo's inbox @ HEAD 92b653a and no claim in `control/claims/` shows a
  renewal build in flight. When the kit lane picks the slice up, it will need
  an expiry constant — and the kit's own comment culture ("Seeded at 72h;
  revisable by data like every horizon constant", check_claims.py:97–101 @
  917261b3) shows exactly what happens absent evidence: another seeded number.
- **The structural half of V027 caps what renewal can fix — and that shapes
  this grid honestly.** V027's hand-pinned, distribution-free identity: O95 =
  θ + ln(20)/λ_c, so at 48 h-mean contender-check sparseness (C48) the 120 h
  orphan band is unmeetable at ANY horizon — that is contender-side detection
  latency, which NO signal design (silence, renewal, anything) can shrink.
  Renewal competes only on the SIGNAL side. This grid therefore decides on the
  two contender tempos where the orphan band is meetable (C4, C12 — V027's own
  grid values) and carries the C48 column reporting-only with the identity
  restated by citation, never re-run.
- **The empirical anchor V027 named is RUN here, not just named** (the
  zero-tooling git-log probe, executed at drafting on this repo's local clone
  @ 92b653a — the first fleet datapoint of its kind): (a) work-claim lifetimes
  from `git log --diff-filter=AD --format='%cI' --name-status -- control/claims/`
  — n=11 completed claims, create→delete hours multiset {0.14, 0.25, 0.49,
  1.37, 2.21, 2.65, 3.13, 3.69, 3.70, 3.72, 4.01}, median 2.65 h; (b) this
  repo's real wake cadence from `control/status.md` commit times — n=19
  re-stamp gaps {0.17, 0.17, 0.26, 0.27, 0.33, 0.65, 0.78, 0.86, 0.98, 1.08,
  1.38, 1.54, 1.73, 1.74, 1.93, 2.23, 2.32, 2.44, 5.52} h, median 1.08 h, max
  5.52 h. Both multisets are quoted into the fixture at drafting
  (reporting-only anchors — n small, they BRACKET the hot end of the wake-
  cadence grid, they do not fit a distribution; the P019 four-interval
  precedent). Tonight's real lane sits at ~1–2 h wakes and ~0.1–4 h claim
  holds — the grid's p_w = 2 / H_c = 4 h anchor leg reads that class directly.

## The simulation question (pre-registered)

Under the pinned renewal-race model — an alive lane holds one work claim for
H_c = 168 h (decision-binding worst case; H_c ∈ {4, 24} h reporting-only, the
4 h leg reading tonight's measured claim class) and wakes on a deterministic
cadence p_w ∈ {2, 12, 24} h (failsafe-2h / half-daily / daily; phase uniform),
re-stamping `renewed:` at each wake EXCEPT an i.i.d. forget with probability
p_f ∈ {0.02, 0.10, 0.25} (careful / typical / sloppy — the compliance axis no
prior grid carries); with probability p_d = 0.10 the lane instead dies silent
at a uniformly chosen wake and never stamps again (p_d deliberately NOT a
decision axis — T conditions on alive claims, O95 on dead ones, V027's own
construction); contender sessions check at Poisson rate λ_c and take over any
claim whose `renewed:` age exceeds θ_r ∈ {6, 12, 24, 48, 72} h (the grid caps
at 72 BY pre-computation: θ_r = 168 gives O95 ≥ 168 + 35.94 > 120 at the
decision tempo, dead on the orphan band before any run; the planted 72 h
constant is in-grid by design); metrics composed worst-case-per-metric from
V027's own tempo grid — T (false-takeover probability for an alive-throughout
claim, the twin-work risk) evaluated at the FASTEST tempo λ_c = 1/4 h⁻¹, O95
(p95 death→takeover latency, the deadlock cost) at the SLOWEST decision tempo
λ_c = 1/12 h⁻¹; 9 decision cells = 3 p_w × 3 p_f — in BOTH Arm A (exact,
seedless, platform-independent: T by finite DP over the wake lattice — ≤ 84
wakes at H_c = 168/p_w = 2 — with exposure accumulating wherever renewal age
exceeds θ_r, a run of j consecutive forgets exposing (j·p_w − θ_r)⁺ hours, and
P(takeover) = 1 − E[exp(−λ_c · total exposure)] computed exactly over the
forget-run distribution; O95 by the exact mixture quantile of (θ_r − A)⁺ +
Exp(λ_c) with A the lattice-valued renewal age at death; Arm A covers ALL 45
decision points with zero sampling error) and Arm S (seeded event-driven MC:
M_S = 4,000 claims per (cell, θ_r), random.Random(20260756), pinned loop order
— cells lexicographic p_w then p_f ascending, θ_r ascending, replications
sequential; gates, run invalid on failure: |T_S − T_A| ≤ 1.0 pp and |O95_S −
O95_A| ≤ max(4 h, 5% relative) on every point, BOTH tolerances pre-checked in
the fixture as ≥ 2.5σ of the registered-M_S estimators BEFORE any run — the
V027 pipeline lesson ("register per-point MC gate tolerances as multiples of
the registered-n sampling SE") applied as a design rule for the first time;
decision-stability leg seed 20260757 M_S = 1,000 must reproduce the ruling;
reporting-only legs seed 20260758 that cannot flip the decision: exponential
wake jitter at mean p_w, H_c ∈ {4, 24}, p_d ∈ {0.02, 0.30}, the C48 column,
and the empirical-anchor leg at the quoted multisets; aux self-check stream
seed 20260759 never read by any decision number; seeds 20260756–59 allocated
strictly above the P027 registry high-water 20260755 — P028 drew zero, stated
per its own card; self-checks: p_f = 0 ∧ alive ⇒ zero exposure exactly, θ_r →
∞ ⇒ T = 0 exactly, per-leg draw-count sentinels, stdout + results.json
byte-identical across two process runs) — with the CHAINED ANCHOR that the
silence-keyed baseline leg re-computes V027's committed exact closed form
T = 1 − (1 − Σ_i w_i·e^(−θ/m_i)·λ_c·m_i/(1+λ_c·m_i))^M at V027's committed
regime constants and must reproduce its committed Feas map EXACTLY (feasible
cells {R1-C4, R1-C12, R2-C12} with θ* = {48, 24, 72} and no others — the
P026/P028 chained-anchor precedent), so the headline reads as ΔFeas of
renewal-keyed over silence-keyed on shared bands — for which cells is
Feas(cell) = {θ_r : T ≤ 0.05 AND O95 ≤ 120 h} non-empty (bands inherited
VERBATIM from V027 by design — the P023 inherited-bands contract; disclosed
up front: in the decision cells the orphan band binds nowhere by the same
arithmetic that kills C48 — max O95 ≈ 72 + 35.94 ≈ 108 h < 120 — so renewal
moves the entire game to the twin side, and the O95 column ships per point for
cell-addressable comparison with the parent), and does the result land
(evaluated in this pre-registered order) REJECT ("renewal fails the same bands
— descope the slice before it is built": Feas(cell) = ∅ in ≥ 5 of 9 cells;
checked FIRST — the costly error is a fleet-wide doctrine build that
measurably does not fix the infeasibility, so the protect-the-build-budget arm
cannot be shadowed by an eager mechanism recommendation), APPROVE ("ship the
renewal slice with the pinned row": ∃ single θ_r† feasible in ≥ 8 of 9 cells,
stability-reproduced → recommended row: `renewed: <ISO8601>` re-stamped each
working wake + expiry at θ_r† + the measured COMPLIANCE FLOOR — the largest
swept p_f at which θ_r† still holds — + the wake-cadence requirement stated
per row, with the verdict stating whether the planted WORK_CLAIM_STALE_HOURS
= 72 read onto the renewal stream lies at θ_r†), or NULL (anything else — a
legitimate and here plausible outcome: the flip axis named via per-axis
feasible-cell shares and per-axis median θ*, expected candidates the p_f =
0.25 sloppy column and the p_w = 24 daily row — at daily cadence every single
forget is a full exposure once ⌈θ_r/p_w⌉ = 1 — with the CONDITIONAL rule the
citable finding, e.g. renewal is twin-safe only for lanes waking ≤ 12-hourly
at forget rates ≤ 10%, which makes the kit's Stop-hook renewal reminder
load-bearing rather than cosmetic)?

**Consequence, pre-registered:** APPROVE → the substrate-kit lease-renewal
build (V027's routed slice) lands with sim-pinned constants — θ_r†, the
compliance floor, the cadence requirement, warn-first per the kit's posture —
instead of a fresh seeded horizon, closing the "revisable by data" contract
with data twice in one night (routed lane-side via the manager sweep, Q-0260 —
this repo never edits kit files; natural ride: the kit-lane fan-in bundle);
REJECT → the renewal slice is descoped BEFORE build spend, silence-expiry
plus V027's local-feasibility table stay as the doctrine, and the residual
routes to the manager as a doctrine question (claims need an explicit
release/handoff protocol, not a better timeout — the measured per-cell
infeasibility table of BOTH mechanisms as the evidence row); NULL → the
conditional per-cadence/per-compliance rule ships, and the cheapest LIVE probe
is named: ship the `renewed:` field warn-first and count missed-renewal
warnings per lane-week — p_f, the axis this sim can only sweep, becomes
MEASURABLE the day the field exists, at zero extra tooling.

## done-when (the verdict's own acceptance test)

The committed stdlib sim + fixture JSON ({p_w grid, p_f grid, θ_r grid, λ_c
decision pair + C48 reporting value, H_c values, p_d constants, M_S per leg,
seeds 20260756–59, band constants (0.05, 120 h, 8/9, 5/9), the V027 anchor
constants — regime mixtures (w, m1, m2, M) verbatim, the committed Feas map,
the C48 identity — and the two empirical multisets quoted at drafting}, values
copied verbatim from this file) reproduce the full {T, O95} × (cell, θ_r)
table plus the Feas/θ*/per-axis-share summary, the silence-baseline chained
anchor, and all gate/self-check results byte-identically on re-run (Arm A
platform-independent exact DP/closed forms; Arm S pinned to a stated CPython
minor version), both agreement gates pass at their pre-checked ≥ 2.5σ
tolerances, the exact-identity self-checks pass, the seed-20260757 stability
leg reproduces the same ruling, and the verdict issues exactly ONE of
APPROVE/REJECT/NULL per the pre-registered rule (evaluation order stated,
REJECT first) — stating the model-basis caveat (deterministic-cadence wakes ×
i.i.d. forgets × Poisson contender checks are the neutral choices; the single
most-likely-to-flip alternative is the real forget process — correlated
forgetting, a sick harness missing EVERY renewal, sits between the i.i.d.
sweep and lane death, and is named as exactly what the warn-first live counter
measures), the contender-side boundary (C48 unmeetable by V027's identity for
ANY signal design — restated, not re-run), the compliance boundary (p_f is
swept, not measured — no fleet datapoint exists until the field ships; the
i.i.d. assumption is the disclosed weakest joint), the cooperative-lanes and
single-claim boundaries (adversarial silence and contender contention out of
scope, V027's registration inherited), with the reporting-only legs stated as
legs that cannot flip the decision; honest-null explicit: a NULL lands as a
finalized verdict naming the binding axis and the conditional rule, not a
re-run request.

## Dedup (nearest priors, and why this differs)

- **PROPOSAL 025 → VERDICT 027** — the parent, deliberately. Its answered
  question (can silence-keyed expiry be tuned fleet-wide? REJECT — Feas = ∅ in
  6/9 cells) is settled and NOT re-asked; this head prices the fix its
  recommendation ROUTED, and its LIMITS line names the gap verbatim ("does not
  design the renewal mechanism"). Different signal model (explicit scheduled
  stamp stream vs natural work-gap silence), different control variables
  (renewal cadence p_w + compliance p_f + horizon-on-renewal-stream θ_r vs
  silence horizon θ over gap-tail regimes), one NEW axis existing in no prior
  grid (compliance), and the parent's numbers enter only as chained anchors
  (the silence-baseline leg + the C48 identity + the inherited bands).
- **The successor pattern is committed precedent, not novelty risk:** P023
  priced V022's routed lever on inherited bands, P027 priced V025's, P026
  priced V024's power half — this is the same move applied to the fleet slot's
  own parent.
- **PROPOSAL 019 → VERDICT 021** (fleet slot round 1) — same fleet-ops
  policy-grid family, different control variable (backlog replenishment
  threshold vs renewal expiry), objective (dry-wake fraction vs the twin/orphan
  race), and consumer (heartbeat `backlog:` token vs claims doctrine).
- **PROPOSAL 012 → VERDICT 014** — wake scheduling economics: wake cadence is
  a COST there (worker-turns per caught trigger), a SIGNAL CARRIER here; zero
  shared metric or consumer.
- **Tree-wide sweep this slice** (`rg -i -g '!bootstrap.py' -g '!.substrate'
  'renew|lease|re-stamp|restamp'` over ideas/ + .sessions/ + control/ +
  docs/): hits are V027's own routing lines quoted in P025's file and index
  row, the claims doctrine README prose, and unrelated "renewal" in TALLY
  upkeep prose — no proposal, idea file, card, or sim-lab verdict V001–V028
  (local clone @ fe51983, offset map read; V029/V030 in flight for P027/P028)
  designs, sweeps, or prices a renewal/lease mechanism.

## Fixture plan (stdlib, hermetic)

One stdlib-only Python file + `fixtures.json` committed together in the
sim-lab build subtree; every constant above copied verbatim into the JSON at
build; zero repo/network reads in the verdict session — the V027 anchors and
both empirical multisets travel INSIDE the fixture (quoted at drafting, this
file is their pin); Arm A is exact and seedless (fractions/exact DP where
integer-supported, platform-independent); Arm S draws only from
random.Random(seed) streams named above in the pinned loop order;
byte-identical stdout + results.json across two full process runs by external
diff; runtime target under a minute (the lattice is ≤ 84 wakes × 45 points ×
9 cells; V027's kernel shapes are reusable art at the same pin).

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained mechanism sim over
> pinned constants; report-only evidence, no spend/publish/irreversible
> surface — README § probe battery). Verify-first ran FIRST, live this slice:
> (a) **premise pins** — VERDICT 027 read in the local sim-lab clone at
> fe51983 (finalized 05:23:41Z; its `recommendation:` routing sentence and
> LIMITS "does not design the renewal mechanism" quoted above verbatim); this
> repo's inbox @ HEAD 92b653a carries no renewal build ORDER and
> `control/claims/` no renewal claim — the window is open. (b) **the
> empirical probe ran for real** — both git-log passes executed on the local
> clone at drafting; the two multisets in the Premise section are measured
> output, not illustration. (c) **dedup** — outbox 001–028 re-read at HEAD
> (tail verified `PROPOSAL 028 · 2026-07-13T06:25:48Z`); sim-lab verdict
> ledger read through V028 (V029/V030 in flight for P027/P028); the tree-wide
> renew/lease sweep above. (d) **feasibility arithmetic** — Arm A is a ≤
> 84-state lattice DP × 45 points × 9 cells (instant); Arm S is 9 × 5 × 4,000
> short walks (~10⁶ wake events) — seconds in pure CPython, stdlib-only.

**1. What is this really?** A pre-registered measurement of whether the
mechanism V027 routed as the FIX actually clears the bands its parent failed —
before the kit spends a build on it — and, if it does, WHICH constants it
ships with (expiry horizon, cadence requirement, compliance floor) instead of
another seeded number.

**2. What is the possibility space?** (i) Build the slice as routed — the kit
picks a horizon by comment culture; the compliance assumption stays silent and
untested. (ii) Wait for live incident data — the field does not exist yet, so
p_f is unmeasurable until AFTER a build; circular. (iii) A prose design review
— decides nothing (no bands, no consequence). (iv) This head: dual-arm sweep
with the parent's bands inherited, three pre-registered consequences, each a
real routed action — including the one nobody wants to discover post-build
(REJECT: renewal fails the same bands too). (v) Over-scope (correlated forget
processes, multi-contender arbitration, adversarial lanes) — named out of
scope; the warn-first live counter is the registered instrument for the first.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~250-line stdlib file. The deterministic-cadence ×
i.i.d.-forget choice makes T an exact finite DP and O95 an exact mixture
quantile — the whole decision surface in Arm A with zero sampling error — with
the MC arm reduced to validation, exactly the parent's architecture at the
same code scale.

**4. What breaks it? (assumptions made explicit)** (a) **The forget model is
i.i.d.** — real non-compliance is likely correlated (a harness bug misses
EVERY renewal, which sits between the sweep and lane death); disclosed as the
weakest joint and as exactly what the warn-first counter measures. (b)
**Deterministic wake cadence** — real cadences jitter; the exponential-jitter
leg brackets it, reporting-only. (c) **The contender model is inherited** —
Poisson checks, V027's own; any error there is shared with the parent by
construction, which is what chained anchors are for. (d) **p_f has no fleet
datapoint** — swept, not measured; the NULL/APPROVE consequences both carry
the measurement instrument.

**5. What does it unlock?** The renewal slice ships with evidence or dies
before build spend — either way the "revisable by data" contract gets served
twice in one night on the same doctrine surface; and the compliance axis
enters the fleet's vocabulary as a measured quantity, reusable by every
future stamp-shaped mechanism (heartbeats, leases, watchdogs).

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing at
verdict time (hermetic; every anchor travels in the fixture). At drafting:
the V027 pins and the two git-log passes — all executed, quoted above. Kill
test: if V027's Feas map fails to reproduce from its committed closed form,
the chained anchor is broken and the run is invalid by its own gate.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab builds the sim (method provider; V027's kernel shapes are reusable
art at the same pin). The verdict consumer is substrate-kit via the manager
sweep (Q-0260). Displaces nothing: no verdict V001–V028 prices a renewal
mechanism; the parent's answered question is not re-asked.

**8. What is the smallest shippable slice?** One sim-lab intake dir: one
stdlib file + fixtures.json + REPORT.md, the committed dual-arm run, the
chained-anchor reproduction, and the pre-registered ruling — nothing else.

**Recommendation: sim-ready** — the question is crisp and fully computable,
the bands and three-consequence decision rule are registered above BEFORE any
code exists, the parent's two genre hazards are pre-empted by inheritance
(model-dependence → the same declared basis plus chained anchors that must
reproduce the parent's committed map; gate mis-calibration → the V027 pipeline
lesson applied as a design rule, tolerances pre-checked at ≥ 2.5σ of the
registered-M estimators), and every outcome changes what a builder does: ship
the slice with a pinned row, descope it before spend, or ship the conditional
rule with the warn-first counter as the p_f instrument.

**State stays** `sim-ready` (= this repo's PROPOSAL 029; expected
verdict number by the sim-lab offset map: VERDICT 031 — constant +2, cited
from sim-lab docs/current-state.md, never derived silently).
