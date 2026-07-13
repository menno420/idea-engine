# Assign-at-merge, priced — does the routed Option-3 build survive its own merge-queue re-validation tax?

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 FLEET-BACKLOGS
> slot, round 5; the successor move applied to the fleet slot's V023 line for the
> first time: rounds 1–4 were P019 websites → V021 approve, P021 superbot → V023
> reject, P025 kit doctrine → V027 reject, P029 V027's routed fix → V031 null —
> this round follows round 2's own verdict-opened thread, the Option-3
> assign-at-merge build V023 routed while stating verbatim "nothing here prices
> Option 3's build cost") ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/idea-engine@2e5d73f59407521922c8bfdb474d7738105fb046 · fetched 2026-07-13T08:38:25Z
> (drafting HEAD for the dedup sweep; parent-anchor home: the local sim-lab clone
> @ `c7340aeb330f2b05655f55e8b542b0e62c71d061` — every anchor constant below is
> quoted verbatim from `sims/verdict-023-renumber-treadmill/results.json` at that
> pin; the sim itself is fully hermetic: zero repo/network reads at verdict time,
> every fixture a pinned constant committed with the sim)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous
pipeline — "continue coming up with new ideas, that is your main purpose"; verified
open/standing at HEAD `2e5d73f` before any work), FLEET-BACKLOGS rotation round 5.
VERDICT 023 (idea-engine PROPOSAL 021) REJECTED the shipped Option-1 checker as
sufficient — "the shared append point must go — route the Option-3 assign-at-merge
build" — and handed the build its evidence row: the per-cell residual-tax table
{R, T, latency inflation vs P3}. But that row prices only the NOT-building side.
V023's own gate LIMITS line says so verbatim: "nothing here prices Option 3's build
cost", and its recommendation names "the Option-3 plan's build-cost side" as
follow-up material. The un-simmed half is the mechanism's operational price: V023's
P3 was a FREE oracle (number assigned at the merge instant, zero latency, zero
collisions — durations exactly W+V), while any REAL assign-at-merge build must
serialize merges of migration-bearing PRs through the shared sequence and pay a
re-validation at the head of that line (the number lands in tested content, so "CI
tested exactly what merged" forces a re-run against current main). This head prices
that queue: the same successor move as P023←V022, P026←V024, P029←V027, and
P030←V020, applied to the fleet slot's superbot line for the first time.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The unpriced fork.** The routed build's implicit claim is V023's latency-inflation
column: P1 (the shipped re-pick-at-push checker) pays 1.14×–15.4× mean open→merge
inflation vs the free P3 oracle in the five treadmill cells. A real Option-3 build
does not get the oracle — it gets a FIFO merge queue over the shared migration
sequence, one PR re-validated at a time (duration V_q, the CI re-run against current
main with the freshly assigned number), merged at re-validation completion. That
queue has its own arithmetic: utilization ρ = λ·V_q, Pollaczek–Khinchine waiting,
and a hard ceiling at ρ → 1 where the queue itself becomes the treadmill. Whether
the routed build actually beats the measured P1 residual depends on where (λ, V_q)
sits — and drafting-side arithmetic says the frontier is genuinely OPEN, not
rhetorical: at lam04·V2 (P1 committed mean 11.416983 h) a 2 h re-validation gives
P3Q ≈ 12.5 h (LOSES) while 0.5 h gives ≈ 10.52 h (wins); at lam12 (0.5 arrivals/h)
a 2 h re-validation is ρ = 1.0 exactly — the queue is unstable by arithmetic before
any run. REJECT, APPROVE, and NULL are all live.

**The pinned model (constants inherited from P021/V023 verbatim, new axis V_q).**
Migration-bearing PRs arrive Poisson λ ∈ {1, 4, 12} per day (per-hour: 1/24, 1/6,
1/2); develop W = 8 h (open → push), validate V ∈ {0.25, 2, 24} h; horizon
H = 2,000 h per replication with 200 h warm-up discarded; M = 40 seeded
replications per (cell, V_q); non-migration PRs never touch the shared sequence and
are out of scope by construction (stated). **Policy P3Q** (the build, the new
object): after a PR's validation completes (open + W + V), it enters a FIFO queue
for the shared migration sequence; the queue serves one PR at a time; service = a
deterministic re-validation of duration V_q; at service completion the number is
assigned and the PR merges. Zero collisions and zero renumbers by construction —
the sim must MEASURE exactly zero on every leg (the V023 P3-control discipline
inherited). Because every PR's open→queue-entry delay is the constant W + V, the
queue's arrival process is exactly Poisson λ — so the P3Q mean has a closed form.

- **V_q grid:** decision {0.1, 0.5, 2} h (a fast targeted re-check / a typical CI
  run / a full heavy suite), plus V_q = 0 control (must reproduce V023's committed
  P3 durations {8.25, 10.0, 32.0} h EXACTLY — the chained regression gate), plus
  V_q = 8 h reporting-only stress.
- **Stability rule, pre-registered:** a (λ, V_q) point with ρ = λ·V_q ≥ 0.9 is
  UNSTABLE and fails WIN by rule (no steady state to compare). Its only member on
  the decision grid is lam12 × V_q = 2 (ρ = 1.0 exactly) — a pre-computable
  arithmetic exclusion, the P029 θ_r = 168 precedent; every other decision point
  has ρ ≤ 1/3.

**Dual arms (the P017–P032 committed discipline).**

- **Arm A (exact, seedless, platform-independent):** the M/D/1
  Pollaczek–Khinchine mean wait W_q = λ·V_q² / (2·(1 − ρ)) gives the P3Q mean
  open→merge latency W + V + W_q + V_q in closed form at EVERY decision point,
  zero sampling error. The P1 comparison side enters as V023's COMMITTED measured
  numbers, quoted verbatim into the fixture (below) — the P023/P027 chained-anchor
  pattern; Arm A therefore evaluates every WIN cell exactly.
- **Arm S (seeded event-driven MC):** the queue simulated whole (arrivals, FIFO
  wait, deterministic service), M = 40 × H = 2,000 h with 200 h warm-up; the
  Arm-S mean must agree with Arm A at every covered point under tolerances
  pre-checked in the fixture and calibrated FAMILYWISE at registration (the
  V027/V031 pipeline lesson, now two committed data points: per-point σ-multiple
  contracts across ~30 gates carry material aggregate breach odds — the fixture
  pins SE-multiple ≈ 3.5σ per point so the expected familywise breach count is
  ≪ 1, with the breach-handling protocol pinned before any draw, the V031
  precedent). Arm S also supplies what the closed form cannot: the P3Q p95
  open→merge per point (shipped with MC SE, reporting-only — the decision is on
  means, stated) and the jitter leg.

**Chained anchors (quoted verbatim at drafting from
`sims/verdict-023-renumber-treadmill/results.json` @ sim-lab `c7340ae`; the
verdict session should additionally re-run the parent's committed runner once
out-of-sim and require byte-identical results.json before use — the V031
precedent, ~58 s):** per-cell P1 committed {mean_dur_f, p95_dur_f} —
lam01·V0.25 {8.257576, 8.25} · lam01·V2 {10.259473, 12.5} · lam01·V24
{183.525239, 473.0} · lam04·V0.25 {8.283372, 8.25} · lam04·V2 {11.416983, 17.5} ·
lam04·V24 {493.583020, 1379.5} · lam12·V0.25 {8.361490, 9.0} · lam12·V2
{121.019534, 440.0} · lam12·V24 {493.408451, 1355.0}; P3 committed means
{8.25, 10.0, 32.0} by V column (exactly W + V, the V_q = 0 gate values); the five
treadmill cells and their committed T (share of merged PRs with ≥ 2 renumbers) —
lam01·V24 T = 1938/2615 ≈ 0.741 · lam04·V2 T = 2/15 ≈ 0.133 · lam04·V24
T = 2470/2921 ≈ 0.846 · lam12·V2 T = 28713/33020 ≈ 0.870 · lam12·V24
T = 1262/1491 ≈ 0.846.

**Decision metric and bands (registered BEFORE any code; evaluated REJECT first).**
WIN(cell, V_q) := P3Q mean open→merge (Arm A exact) ≤ the cell's committed P1 mean
AND ρ < 0.9. V_q*(cell) := the largest decision-grid V_q with WIN. Decision cells =
the FIVE treadmill cells V023's REJECT bound (where the build was routed); the four
calm cells ride reporting-only (the build was never routed for them; expected and
worth printing: P3Q is strictly WORSE there at any realistic V_q — the checker
keeps its fast lane, V023's "the checker was worth shipping" restated with numbers).

- **REJECT** ("the queue tax eats the routed win — descope the naive build before
  spend"): V_q* exists in ≤ 2 of the 5 treadmill cells (even the 0.1 h re-check
  loses in ≥ 3). Checked FIRST — the costly error is an infra build that
  measurably re-creates the latency it was routed to remove.
- **APPROVE** ("the build wins with full-CI headroom — the routed row stands,
  now priced"): V_q* ≥ 2 h in ≥ 4 of the 5 treadmill cells, stability-leg
  reproduced.
- **NULL** (anything else — a legitimate and here plausible outcome): the per-cell
  V_q* frontier table IS the pin; flip axes named via per-axis WIN shares —
  expected candidates λ (the serialization ceiling ρ = λ·V_q: lam12 × V_q = 2 is
  excluded by arithmetic) and the V = 2 same-day-review column (P1's committed
  mean there is nearly clean, 11.42 h vs the free 10.0 h, so the queue has only
  1.42 h of headroom to spend) — and the CONDITIONAL rule is the citable finding:
  the build pays wherever the repo's real (λ, V_q) sits inside the frontier.

**Consequence, pre-registered.** APPROVE → the Option-3 plan proceeds with the
queue-discipline row attached (FIFO + re-validate-at-head; the frontier table
names the CI budget per cell) and V023's evidence row gains its build-side price.
REJECT → the NAIVE serial-queue build is descoped before spend with the quantified
reason; V023's interim mitigation (keep held migration-bearing PRs off the hot
path) stays the standing rule, and any future Option-3 proposal must be a
batching/merge-train design carrying its own sim (a REJECT here rules on the
simplest build only, stated). NULL → the conditional frontier ships, and the TWO
zero-tooling live probes locate superbot's real cell before any spend: V023's
already-named git-history probe for (λ, V, W, d), plus the NEW probe this head
names — the repo's real V_q measured as CI wall-time on migration-touching PRs
from its committed Actions history.

**Seeds and registry.** 20260768 main / 20260769 stability (half-M = 20, must
reproduce the ruling) / 20260770 reporting (jitter, V_q = 8 stress, p95 legs) /
20260771 aux self-check stream (never read by any decision number) — allocated
strictly above the PROPOSAL 031 registry high-water 20260767 (PROPOSAL 032 drew
zero, per its own card).

**Reporting-only legs (cannot flip the decision):** the four calm cells at every
V_q; the V_q = 8 h stress column (ρ ∈ {1/3, 4/3, 4} — the last two unstable by
arithmetic, printed as such); the JITTER leg — service redrawn exponential at mean
V_q (the M/M/1 wait ρ·V_q/(1 − ρ) is its own exact check), bracketing real CI
variance between deterministic and memoryless; the P3Q p95 table vs P1's committed
p95 column; queue-length and busy-fraction traces; and the churn column: P3Q's
R = T = 0 by construction vs the five cells' committed T values — the free win the
latency-parity metric deliberately does not count (see Model basis (3)).

**Self-checks (run invalid on any failure):** the V_q = 0 leg reproduces V023's
committed P3 means {8.25, 10.0, 32.0} EXACTLY; zero renumbers/collisions under
P3Q measured on every leg; Little's law (mean queue length ≡ λ·mean wait) and
busy-fraction ≡ ρ within pre-checked tolerance on every stable point; the M/M/1
closed form reproduced on the jitter leg; per-leg draw-count sentinels; twin
independently-written decision evaluators; stdout + results.json byte-identical
across two full process runs; CPython minor pinned and asserted.

**Fixture (every value copied verbatim from this file into a committed JSON):**
{λ-grid, V-grid, W, H, warm-up, M per leg, V_q decision/control/stress grids, the
ρ ≥ 0.9 stability bound, band constants (≤ 2 of 5 / ≥ 4 of 5 / V_q† = 2 h), the
V023 anchor table above (9 × {P1 mean, P1 p95, P3 mean} + the five treadmill-cell
T values, with the results.json pin `c7340ae`), seeds 20260768–71, familywise
gate tolerances with their pre-run SE arithmetic}.

**Feasibility arithmetic:** ≤ 9 cells × 5 V_q values × 40 replications × ~85–1,000
arrivals each — well under a minute of event-driven stdlib CPython; Arm A is a
handful of closed-form evaluations.

## Relations (adjacent heads — deliberately links, not duplication)

- vs **PROPOSAL 021 → VERDICT 023** (the parent, deliberately): its answered
  question — does the shipped Option-1 checker suffice? REJECT, T > 0.05 in 5/9
  cells — is settled and NOT re-asked; P1 and its treadmill enter this grid only
  as committed anchor constants. The parent's P3 was a free oracle; this head's
  P3Q is the priced mechanism — a policy object that exists in no prior grid.
  Zero measured numbers recomputed; the V_q = 0 gate ties the two grids exactly.
- vs the successor-move family **P023←V022 / P026←V024 / P029←V027 / P030←V020**:
  same committed pattern (price the parent verdict's own routed/named follow-up
  before build spend), zero shared domain, fixture, metric, or consumer.
- vs **PROPOSAL 012 → VERDICT 014** and **P019/P025/P029 → V021/V027/V031**
  (fleet-ops policy grids): method family only — control variables wake cadence /
  backlog threshold / claim horizons / renewal grace vs MERGE-QUEUE RE-VALIDATION
  BUDGET here.
- Dedup, tree-wide at the grounding pin (`rg -i "merge.?queue|re.?validat|
  assign.?at.?merge|pollaczek|khinchine|m/d/1"`, bootstrap.py + .substrate
  excluded): every hit is the P021/V023 family's own prose, the websites lane's
  unrelated merge-hold/review-queue heads, or this section's link-index; no
  proposal 001–032 and no sim-lab verdict V001–V032 (local clone @ `c7340ae`,
  offset map read; V033/V034 for P031/P032 not yet ledgered at that pin) prices a
  merge queue, re-validation latency, batching, or any assign-at-merge mechanism
  cost.
- Alternatives weighed this slice and passed on merit: V015's second-repo linter
  re-measure (a labeling/measurement task, not a pre-registerable stdlib sim —
  the corpus-labeling burden is the wall); V031's jitter-robust grace-rule design
  (a THIRD consecutive kit-claims head in this slot, and V031's own named next
  step is the live warn-first counter, which another model sweep would preempt);
  superbot-next/mineverse heads (P025's committed survey measured those sections
  sim-dry by their own probes).

## Model basis (declared model-dependence — the P024 discipline)

This verdict's numbers are CONDITIONAL on an embedded model, named up front:

- **(1) Statistical assumptions:** Poisson migration-PR arrivals; deterministic
  W, V, and service V_q (the jitter leg brackets service variance between
  deterministic and memoryless); one shared sequence; FIFO, one-at-a-time
  service; only migration-bearing PRs queue. Model hours, not wall-clock — the
  parent's boundary inherited verbatim.
- **(2) Single most-likely-to-flip alternative:** the repo's REAL (λ, V_q) cell —
  deliberately the same measurement as the NULL-case live probes (git history for
  λ/V; Actions history for V_q). Second-order: re-validation FAILURES at the queue
  head (a failed re-run adds fix latency and re-queues) are out of the registered
  scope — their direction is one-sided, they only worsen P3Q, so APPROVE is the
  fragile direction and a REJECT is conservative (stated in the verdict).
- **(3) The latency-parity metric is conservative toward the build:** WIN counts
  only mean latency; P3Q's churn elimination (R = T = 0 vs committed T up to
  0.870) rides free and un-scored. A cell that narrowly misses WIN may still be
  worth building for churn alone — the verdict must state this, and the churn
  column ships so the reader can re-weigh; the pre-registered ruling stays on the
  latency metric.
- **(4) Out of scope by design, named:** the P1→P3Q transition window (both
  mechanisms coexisting); batching/merge-train service disciplines (the named
  rescue design if REJECT lands); cross-repo sequences.

## Probe report battery (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained successor head over
> committed parent evidence, no spend/publish/irreversible surface — README §
> probe battery). Verify-first ran FIRST, live this slice: (a) **parent evidence
> read direct** — V023's verdict text AND its committed
> `sims/verdict-023-renumber-treadmill/results.json` read at sim-lab origin/main
> `c7340ae`; the anchor table above is transcribed from the results file, not
> from prose. (b) **dedup** — the tree-wide merge-queue/re-validation sweep above
> returned only the parent family's own prose at `2e5d73f`; PROPOSALs 001–032
> re-read at HEAD before drafting. (c) **kill test NOT triggered** — no prior
> proposal, idea file, or card 💡 prices any assign-at-merge mechanism; the
> parent's P3 was explicitly a free oracle. (d) **feasibility arithmetic
> checked** — closed forms + a small event sim, under a minute.

**1. What is this really?** A pre-registered pricing of the OTHER side of VERDICT
023's fork: the parent measured what NOT building Option 3 costs (the residual
renumber treadmill under the shipped checker — T up to 0.870, latency inflation
to 15.4×); this head measures what BUILDING it costs (the serialized merge queue
with re-validation that a real assign-at-merge mechanism forces), on the same
pinned (λ, V) grid, against the parent's own committed per-cell numbers as exact
chained anchors, with the M/D/1 closed form as a seedless exact arm.

**2. What is the possibility space?** (i) Don't run it — the Option-3 build rides
to a plan with only its benefit priced, the exact one-sided-evidence failure this
pipeline exists to prevent. (ii) Route the build as-is and let the builder
discover the queue arithmetic — the discovery cost is an infra build that can
re-create the latency it was routed to remove (lam04·V2 loses at V_q = 2 by
drafting arithmetic). (iii) Judgment-only ("queues are fine at low utilization")
— unquantified exactly where the frontier is close. (iv) Measure superbot's real
λ, V, V_q first — named as the NULL-case live probes, but the frontier TABLE is
what makes those measurements decision-ready. (v) This head: price the mechanism
per cell against the parent's committed residual, bands registered first.
(vi) Over-scope (batching disciplines, failure/retry loops, transition window) —
named out of scope; batching is the rescue design a REJECT would route to.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~250-line stdlib file: a FIFO event loop (arrivals,
service, merge), the P–K/M/M/1 closed forms as functions, the committed anchor
table as a dict, twin decision evaluators. That single file turns "route the
Option-3 build" from a direction into a priced frontier — per fleet-rate and
review-class cell, the exact CI-time budget under which the build beats the
measured treadmill — and reproduces the parent's P3 column exactly as its own
regression gate.

**4. What breaks it? (assumptions made explicit)** (a) **Model-truth** — Poisson
arrivals and deterministic stages are the parent's own neutral choices, inherited;
the jitter leg brackets service variance; the real-(λ, V_q) gap is the declared
flip axis and the live probes are the instruments. (b) **Anchor transcription** —
the anchor table is machine-read from the parent's committed results.json and the
verdict session re-runs the parent's runner once out-of-sim requiring byte
identity (the V031 precedent) — a transcription slip is caught before any
decision number exists. (c) **Band placement could cherry-pick** — both bands are
committed here before any code; the frontier table ships whole on every outcome
so a re-drawn line re-reads, never re-runs. (d) **MC error near a close frontier**
— the decision arm is Arm A (exact closed forms vs committed constants, zero
sampling error); Arm S gates the machinery at familywise-calibrated tolerances
(the V027/V031 two-datapoint lesson applied at design time). (e) **Un-modeled
P3Q failure modes** (re-validation failures, transition window) — one-sided
against P3Q, disclosed: APPROVE is the fragile direction, REJECT conservative.

**5. What does it unlock?** The Option-3 routing decision gets both sides priced
(V023's residual-tax row + this frontier) — the manager can route build/descope/
measure-first with numbers on every arm; the two zero-tooling probes become
decision-ready (their outputs land in a table instead of a vibe); the calm-cell
column quantifies V023's "the checker was worth shipping"; and the queue kernel
(M/D/1 vs measured baseline with chained anchors) is reusable art for any future
shared-sequence mechanism head (deploy trains, release queues, the fleet's own
merge-ordering questions).

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing live — by
design: every fixture is a pinned constant in this file (model constants inherited
from P021 verbatim; anchors machine-read from the parent's committed results.json
@ `c7340ae`; seeds 20260768–71). Kill tests, run live this slice: a prior
merge-queue/assign-at-merge pricing anywhere in the tree (NOT found — sweep at
`2e5d73f` hits only the parent family's prose); parent anchors unavailable (NOT
found — results.json read direct, values transcribed above); infeasible runtime
(NOT found — arithmetic in the preamble). Sim-worthy or judgment-only: sim-worthy
— the frontier is a computable table against pre-registered bands; the one
judgment call (is latency parity the right WIN line given the free churn win?) is
pinned by pre-registration and disclosed as Model basis (3), about the metric,
never about the measured numbers.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab runs it (its harness, its verdict grammar; the sim + fixture JSON
committed in its sims/ tree; the parent's committed runner re-run once as the
anchor gate). The verdict consumer is superbot (the Option-3 plan's
build/descope/measure-first fork) via the manager's routing per Q-0260 — this
repo never edits superbot's files. Duplicates nothing: the parent priced
not-building; no verdict through V032 prices any mechanism cost on this seam;
the shipped Option-1 checker stays an input, not a competitor.

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one stdlib
file (FIFO event sim + P–K/M/M/1 closed forms + anchor gates + twin evaluators),
one fixture JSON (grids, bands, seeds, the V023 anchor table with its
results.json pin), one results table {P3Q mean/p95, WIN, V_q* per cell; the calm
and stress columns; jitter and churn legs} ending in exactly one of
APPROVE/REJECT/NULL per the pre-registered rule — reproducible from the fixtures
alone, byte-identical stdout + results.json across two process runs, CPython
minor pinned, no flags.

**Recommendation: sim-ready** — the question is crisp and fully computable
against committed parent anchors, the bands and decision rule are registered
above BEFORE any code exists (REJECT checked first; the stability exclusion is
pre-computable arithmetic), both genre failure modes are pre-empted
(model-dependence → constants inherited from the parent + the declared flip axes
+ the two named live probes; machinery error → an exact seedless decision arm,
familywise-calibrated MC gates, the V_q = 0 exact regression to the parent's
committed P3 column, and the out-of-sim byte-identity re-run of the parent's
runner), and the verdict changes what the manager may route in every branch. THE
ONE QUESTION for the simulator: *Under the pinned migration-race frame inherited
from PROPOSAL 021/VERDICT 023 verbatim (Poisson migration-bearing PRs λ ∈ {1, 4,
12}/day; develop W = 8 h; validate V ∈ {0.25, 2, 24} h; H = 2,000 h, warm-up
200 h, M = 40; anchors = V023's committed per-cell P1 {mean, p95} and P3 means
quoted from `sims/verdict-023-renumber-treadmill/results.json` @ sim-lab
`c7340ae`), what is the per-cell re-validation budget V_q*(cell) — the largest
V_q ∈ {0.1, 0.5, 2} h at which the REAL Option-3 mechanism P3Q (FIFO merge queue
over the shared sequence; service = one deterministic re-validation V_q at the
head; number assigned at merge, zero renumbers by construction, measured) beats
the parent's committed P1 mean open→merge latency (WIN := Arm-A-exact
W + V + λV_q²/(2(1−ρ)) + V_q ≤ committed P1 mean, AND ρ = λ·V_q < 0.9 — the ρ ≥
0.9 stability exclusion's only decision-grid member is lam12 × V_q = 2, ρ = 1.0
exactly) across the FIVE treadmill cells V023's REJECT bound (lam01·V24,
lam04·V2, lam04·V24, lam12·V2, lam12·V24 — committed T 0.741/0.133/0.846/0.870/
0.846), with Arm S (seeded event MC, seeds 20260768–71 allocated above the P031
high-water 20260767, familywise-calibrated gates per the V027/V031 lesson, the
V_q = 0 leg reproducing the committed P3 means {8.25, 10.0, 32.0} exactly, Little's
law and busy-fraction identities, twin evaluators, two-process byte-identity)
supplying p95 and the exponential-service jitter leg reporting-only — landing
(REJECT first) REJECT ("the queue tax eats the routed win — descope the naive
build") iff V_q* exists in ≤ 2 of 5 treadmill cells, APPROVE ("the build wins
with full-CI headroom — the routed row stands, priced") iff V_q* ≥ 2 h in ≥ 4 of
5 stability-reproduced, or NULL (anything else — the per-cell V_q* frontier is
the citable pin, flip axes named via per-axis WIN shares, expected candidates λ
and the V = 2 column, and the conditional rule ships: the build pays wherever the
repo's real (λ, V_q) sits inside the frontier, located by the two zero-tooling
probes — V023's git-history probe for (λ, V) plus CI wall-time on
migration-touching PRs from committed Actions history for V_q)?* Done-when: the
committed stdlib sim + fixture JSON reproduce the full frontier table
byte-identically across two process runs (CPython minor pinned), every gate
passes (anchor byte-identity re-run of the parent's runner, V_q = 0 ≡ committed
P3 exactly, zero renumbers under P3Q measured, familywise Arm-S gates, Little's
law/busy-fraction/M/M/1 identities, twin evaluators), the seed-20260769
stability leg reproduces the same ruling, and the verdict issues exactly ONE of
APPROVE/REJECT/NULL per the pre-registered rule — stating the latency-parity
conservatism (the churn win R = T = 0 rides free and un-scored, the churn column
shipped), the one-sided un-modeled P3Q failure modes (APPROVE fragile, REJECT
conservative), the model-hours boundary, and the batching/transition-window
out-of-scope lines with batching named as the REJECT-case rescue design;
honest-null explicit: a NULL lands as a finalized verdict naming the binding
axis and the conditional frontier, not a re-run request.
