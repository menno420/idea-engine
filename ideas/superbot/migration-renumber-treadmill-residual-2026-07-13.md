# Migration renumber treadmill: does the shipped checker suffice, or must the shared append point go?

> **State:** sim-ready
> **Class:** process · **Target:** `menno420/superbot` (verdict consumers: the superbot
> lane — disposition of the captured idea's remaining Options 2/3, and the evidence row
> for the Option-3 assign-at-merge plan if it is ever built; verification target
> `menno420/sim-lab` per the Q-0264 pipeline)
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/migration-number-collision-guard-2026-06-22.md@fd638e3 · fetched 2026-07-13T02:26Z

*(Premise re-verified at superbot LIVE HEAD `4522522937aaaba140f60998a2abe8fbcef69f43`
this slice, 2026-07-13T02:31Z: the canonical doc's status block is unchanged — "Option 1
SHIPPED 2026-06-22 (`scripts/check_migration_collision.py`) … Options 2 (merge-aware
local mirror) + 3 (assign-number-at-merge) remain" — and the Option-1 checker file
answers 200 at the same HEAD. The window this head prices is still open.)*

**Origin:** drafted under standing owner ORDER 003 (continuous pipeline) + ORDER 004
rule 3's rotation ("fleet backlogs → venture's book/product space → game mechanics →
COMPLETELY UNRELATED domains") — round 2 of the cycle restarts at FLEET BACKLOGS
(round 1: 019 fleet-backlogs / 018 venture / 020 game-mechanics / 017 unrelated), and
this round the harvest weight goes to the deepest, barely-tapped backlog: this
section's 237-doc superbot index. Harvest source, quoted verbatim from the canonical
doc (@ `fd638e3`, byte-same at live `4522522`): migrations are numbered `NNN_name.sql`
and the number is "a **single shared append point**: the next free integer above the
highest on `main`. Under a fast multi-session fleet, several PRs in flight all pick
the *same* next number, and whichever merges first wins." The recorded incident:
reaction-roles PR 6 (#1279), "a held `needs-hermes-review` PR whose migration was
renumbered **four times** (085→086→088→089) in one afternoon as the active routine
fleet kept appending the next number to `main`" — because "the fix (renumber +
re-merge) takes longer than the fleet's inter-migration interval, so by the time CI
re-runs, `main` has appended *another* migration and the collision recurs." Option 1
(a local pre-push collision checker) shipped same-day; the doc's own open fork is
whether that is ENOUGH, or whether Option 3 — "assign the migration number at **merge
time** … removing the shared append point entirely. This is the real fix but a
meaningful infra change (own plan)" — has to land. Nobody has priced that fork: the
checker moves the detection point but cannot shrink the push→merge exposure window,
and the treadmill is a positive feedback (every renumber delays a merge, delayed
merges bunch up, bunched merges raise the collision pressure on everyone else) that
no single-PR intuition prices. This head pre-registers exactly that question.

## The idea (reasoned to its fuller form — Q-0254 duty)

Shared-sequence ID allocation under concurrency is a classic race, and superbot runs
the naive protocol: pick `max(main)+1` at some point before merge, hope nobody merges
that number first. Three policies exist on the doc's own ladder: **P0** no guard
(collision discovered only by CI on the merge result — one full CI round-trip per
discovery; this is the pre-2026-06-22 world that produced #1279); **P1** the shipped
Option-1/Option-2 family (re-pick the number locally at every push — detection moves
to push time at ~zero cost, but the residual exposure window push→merge stays, and a
collision inside it still costs a fix + CI round); **P3** Option 3, assign-at-merge
(the number is minted at the merge instant — collisions impossible by construction,
at the price of a real infra build). The genuinely open quantity is the RESIDUAL
treadmill under P1 — and critically, its **endogenous amplification**: when the
append process on `main` is not an external clock but the other in-flight
migration-bearing PRs themselves, renumber storms feed back into the very collision
pressure that causes them. A single-PR closed form exists for the exogenous
approximation (below, it is the sim's exact Arm A); whether the coupled system sits
above or below it, and by how much, is not readable off any formula — that is the
sim's headline number, and the APPROVE/REJECT boundary runs through the middle cells
of the grid.

**The sim (fully hermetic — the PROPOSAL 017/018/019/020 precedent; every fixture is
a pinned constant committed with the sim, zero repo/network reads in the verdict
session):** continuous-time event simulation, horizon **H = 2,000 h** per run with
the first **200 h discarded** as warm-up. Migration-bearing PRs arrive Poisson at
rate **λ ∈ {1, 4, 12} per day** ({1/24, 1/6, 1/2} per hour — calm lane / busy lane /
the recorded #1279-afternoon class); each PR opens, develops for **W = 8 h** (pick →
push), then enters validation of duration **V ∈ {0.25, 2, 24} h** (auto-merge
fast-lane / same-day review / held-for-review — #1279 was held), and at validation
end attempts to merge: if its held number has meanwhile been merged by another PR,
that is a **collision** — the PR renumbers (fix latency **d = 0.5 h**) to the next
free number as of the fix, then re-validates (another V). Number-picking time is the
policy: **P0** picks at open and at each fix start (round-1 exposure W+V, later
rounds d+V); **P1** re-picks at every push, i.e. at the start of every validation
window (every round's exposure = V exactly — the shipped checker's semantics);
**P3** assigns at the merge instant (exposure 0; the sim must measure exactly zero
collisions — a built-in control). Decision grid: **9 cells = 3 λ × 3 V**, policies
P0/P1/P3 each; **M = 40** seeded replications per (cell, policy),
`random.Random(20260723)`, pinned loop order (cells lexicographic λ ascending then V
ascending; policy P0, P1, P3; replications sequential; within a run, event-queue
ties broken by PR id). Metrics per (cell, policy), merged-PR population after
warm-up: **R** = renumbers per merged PR, **T** = share of merged PRs with ≥ 2
renumbers (the treadmill class — #1279's class), and reporting-only: mean/p95
open→merge inflation vs the same cell's P3, max simultaneous holders of one number,
and the **endogenous/exogenous amplification ratio** R_endo/R_exo per cell.
**Arm A (exact, seedless):** the exogenous single-PR closed forms — with
p(w) = 1 − e^(−λw) and per-policy windows (w₁, w₂) as above: P(N ≥ 1) = p(w₁),
P(N ≥ 2) = p(w₁)·p(w₂), E[N] = p(w₁)·e^(λw₂) — computed for every cell × {P0, P1}.
**Validation gate:** Arm S re-run in EXOGENOUS mode (appends = external Poisson λ,
one focal PR, **M = 20,000** focal PRs per cell-policy, seed **20260726**) must
agree with Arm A within **1.0 percentage point absolute** on P(N ≥ 1) and P(N ≥ 2)
in every covered cell, and the endogenous P3 legs must report exactly zero
collisions, or the run is invalid. Reporting-only legs that cannot flip the
decision: sensitivity **d ∈ {0.25, 2}**, **W ∈ {1, 24}**; a jitter leg (seed
**20260725**) redrawing W, V, d exponentially with the pinned means (tests
fixed-window knife-edging); a decision-stability leg at **M = 8** with seed
**20260724** that must reproduce the same ruling; and the **#1279 anchor** — under
(λ = 12/day, V = 2 h, d = 0.5 h, P0) report E[N] and P(N ≥ 3), stating whether the
recorded four-renumber afternoon sits inside the model's mass (a plausibility
report against an n=1 anecdote, never a fit). Results table pins the CPython minor
version; byte-identical on re-run.

**Pre-registered acceptance bands and decision rule** (set BEFORE any code runs;
evaluated on the ENDOGENOUS P1 cells, in this order):

- **APPROVE** ("Option 1 suffices fleet-wide — retire Options 2/3 with the
  quantified reason") iff **R ≤ 0.10 AND T ≤ 0.01** in ≥ 80% of the 9 cells (i.e.
  ≥ 8), in Arm S endogenous mode with the validation gate passed. Checked FIRST —
  the build-nothing arm, so an eager build recommendation cannot shadow it (the
  PROPOSAL 019 evaluation-order discipline).
- **REJECT** ("the shared append point must go — route the Option-3 assign-at-merge
  build") iff **T > 0.05** in ≥ 50% of the 9 cells (i.e. ≥ 5). The verdict must
  attach the per-cell residual-tax table (R, T, latency inflation vs P3) as the
  Option-3 plan's evidence row.
- **NULL** otherwise — a legitimate and here EXPECTED-USEFUL outcome: the verdict
  names the flip axis (for each of λ and V, the APPROVE-pass share and median T at
  each of its values; largest spread = the named boundary — expected candidate: V,
  because the checker cannot shrink the push→merge window, so λ·V is the collision
  pressure per round), and the citable finding is the CONDITIONAL per-PR-class rule
  (e.g. "Option 1 suffices for auto-merge-fast PRs at any swept fleet rate; held
  PRs above rate X need assign-at-merge"), not either camp's default.

**Consequence, pre-registered:** on APPROVE — the canonical doc's remaining Options
2/3 are retired with the quantified reason (routed lane-side via the manager sweep,
Q-0260 — the doc is superbot's, never edited from here), and the only remaining
slice is the doc's own unfinished ask, wiring the shipped checker into the Stop hook
/ pre-pr step. On REJECT — the Option-3 assign-at-merge design (the doc's "own
plan") gets its evidence row: the measured residual treadmill UNDER the shipped
guard, per-cell, plus the latency tax — the difference between "we have a checker"
and "the race is gone", priced. On NULL — the conditional per-class rule ships, and
the cheapest LIVE probe is named: derive superbot's REAL cell from its own git
history — migration-file merge timestamps give λ, PR open/push/merge times give W
and V, renumber commits give d (one `git log` pass over `migrations/` and the PR
refs, zero new tooling) — locating the repo's actual (λ, V) before anyone spends an
infra build on a corner of the grid it does not occupy.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the harvest source: this section's own link-index
  [`migration-number-collision-guard-2026-07-10.md`](migration-number-collision-guard-2026-07-10.md)
  (state `captured`) indexes the canonical doc and is deliberately left untouched —
  this head is NOT the capture (the link-index-only rule holds) and NOT the
  already-shipped Option-1 build; it is the fork the doc itself leaves open
  ("Options 2 + 3 remain") turned into a pre-registered, computable question. Same
  harvest pattern as PROPOSAL 019 (websites bullet → new head), source lane
  different, question class the same: an untested mechanism claim riding a live
  process.
- vs the outbox (PROPOSALs 001–020, re-read at HEAD `da20713`): no prior proposal
  touches migration numbering, ID allocation, renumbering, or merge-order races.
  Nearest by REPO-FAMILY is PROPOSAL 009 (settle-once guard → VERDICT 010 by
  sim-lab's own offset map — source numbers cited verbatim, never derived): same
  hub, but a runtime money-settlement CORRECTNESS contract vs this head's
  dev-process ID-allocation THROUGHPUT policy — zero shared fixture, metric, or
  consumer. Nearest by SIM-FAMILY are PROPOSALs 012 (routine-cadence economics →
  VERDICT 014) and 019 (backlog low-water → VERDICT 021): all three are fleet-ops
  policy grids with pre-registered bands, but 012's control variable is wake
  scheduling, 019's a replenishment threshold, and this head's an ID-ASSIGNMENT
  POLICY (pick-at-open / re-pick-at-push / assign-at-merge) with objective
  renumbers-per-PR and treadmill share — no shared model, metric, or consumer.
  PROPOSALs 017/018/020 are method precedent only (hermetic fixtures, dual arms,
  APPROVE/REJECT/NULL with stated evaluation order; discipline reused, zero shared
  domain).
- vs sim-lab (local clone @ `a7edcad`, verdicts through 021 finalized + VERDICT 022
  in flight for PROPOSAL 020, offset map read this slice): no verdict touches
  migration numbering, ID allocation, or renumber dynamics; VERDICTs 014/021 are
  the family neighbors addressed above.
- Tree-wide dedup sweep (`rg -g '!bootstrap.py' -g '!.substrate'` for
  renumber / migration-number / collision / append point / assign-at-merge over
  ideas/ + .sessions/ + control/ + docs/): every hit is either this section's own
  link-index row, unrelated renumbering prose (venture-lab slice numbering,
  gba-homebrew anchor rows, substrate-kit heartbeat-counter renumber rule, the
  INTAKE 018 race note), or the repo README's session-branch numbering convention.
  No prior treadmill, ID-race, or allocation-policy sim content anywhere in the
  tree.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained modeling head, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **grounding** — the
> canonical doc fetched raw at the harvest pin `fd638e3` AND re-fetched at live HEAD
> `4522522` (status block byte-same; Option-1 checker file answers 200 at HEAD), so
> the open fork is real, not archaeology. (b) **dedup** — the sweeps above; zero
> prior content. (c) **feasibility arithmetic** — 9 cells × 3 policies × 40 runs ×
> ~(λ·1,800 h) PRs/run with a handful of events each ≈ low-millions of events for
> the whole endogenous grid, plus 9 × 2 × 20,000 short exogenous replications: well
> under a minute per arm in pure CPython, no dependencies.

**1. What is this really?** A pre-registered queueing sim for a shared-sequence ID
race that superbot demonstrably pays for (#1279: four renumbers, one afternoon),
asking the one question the shipped mitigation left open: is the RESIDUAL treadmill
under re-pick-at-push negligible, fatal, or PR-class-conditional — with the
endogenous feedback (renumber storms breed renumber storms) measured against the
exact exogenous closed form, so the amplification itself is a deliverable.

**2. What is the possibility space?** (i) Do nothing — the doc's Options 2/3 sit
captured forever while every migration-bearing PR pays an unmeasured tax; the fleet
already paid four rounds in one afternoon once. (ii) Build Option 3 on vibes — "a
meaningful infra change (own plan)" bought without evidence that the checker left a
material gap. (iii) Ask the owner — a structured-choice question with zero numbers
attached; strictly worse after this verdict prices the fork (Q-0263.2). (iv) This
head: 9-cell endogenous grid, exact analytic control arm, bands registered first,
NULL names the per-class rule. (v) Over-scope (multi-repo shared sequences,
merge-queue design, optimal checker placement) — follow-ups only if this lands
non-NULL; the doc's own fork is the question as posed.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~250-line stdlib file: an event heap, three number-picking
policies expressed as one "pick time" parameter each, closed forms in ~10 lines as
the control arm — and it yields the fleet's first measured answer to "when does a
detection-time guard stop being enough for an allocation race", a shape that recurs
(migration numbers today; any shared counter tomorrow).

**4. What breaks it? (assumptions made explicit)** (a) **Models are models** — λ,
V, W, d are pinned dials, not measurements; that is why the NULL consequence names
the git-history probe that locates superbot's REAL cell, and why a cell-dependent
result is a pre-registered NULL naming the axis, never a judgment call. (b)
**Poisson arrivals** — real fleet merges bunch; the endogenous mode generates
bunching from the mechanism itself, and the jitter leg redraws all windows, but
exogenous burst processes are out of scope by design (stated boundary). (c) **One
repo, one sequence** — cross-repo or per-directory sequences are not modeled. (d)
**Uniform discipline** — every simulated author runs the checker on every push under
P1; real compliance is ≤ that, so P1's simulated residual is a FLOOR (stated in the
verdict: an APPROVE is therefore the fragile direction, a REJECT is conservative).
(e) **PRNG stability** — `random.Random(20260723)` pinned (fresh seeds 20260723–26;
the seed registry swept across all prior heads 20260713–22 before picking — the
PROPOSAL 020 card's collision warning heeded), loop order pinned, CPython minor
version pinned in the results table.

**5. What does it unlock?** The disposition of a captured idea that has sat with an
open fork since 2026-06-22, an evidence row that makes the Option-3 plan buildable
(or killable) on numbers, the first measured "detection guard vs structural fix"
boundary in the fleet's corpus — and, on any outcome, the git-history probe recipe
that turns this class of question from modeling into measurement next time.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external at
sim time — every fixture ({λ-grid, V-grid, W, d, H, warm-up, M per leg, seeds
20260723–26, band constants, per-policy pick-time definitions}) is stated in this
file and committed as a small JSON alongside the sim. Kill tests, run live this
slice: the fork already closed upstream (NOT killed — doc status byte-same at live
`4522522`, checker present, Options 2/3 verbatim "remain"), a prior allocation-race
head anywhere in the tree (NOT found — sweeps above), a sim-lab verdict on it (NOT
found — verdicts through 021 read, 022's subject is PROPOSAL 020's casino envelope),
infeasible runtime (NOT found — arithmetic in the preamble). Sim-worthy or
judgment-only: sim-worthy — the entire question is computable renumber/latency
arithmetic against pre-registered thresholds; the one judgment question (are 0.10
renumbers/PR, 1% and 5% treadmill the RIGHT lines?) is pinned by pre-registration
and stated as the disputable bands, never the measured numbers.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs it (its harness, its verdict grammar; sim + fixture JSON committed in its
sims/ tree). The verdict's consumers are named in the header (the superbot lane owns
both the doc disposition and any Option-3 build; routing is the manager's per
Q-0260 — this repo never edits superbot's files). Duplicates nothing: VERDICT 010 is
the same-repo neighbor and shares no question class; VERDICTs 014/021 are the
same-method neighbors and share no domain (dedup section above); the shipped
Option-1 checker is an INPUT to the model (P1's semantics), not a competitor.

**8. What is the smallest shippable slice?** One sim-lab intake dir: one stdlib
file (event heap + three pick-time policies + closed-form arm + legs), one fixture
JSON (all constants copied verbatim from this file), one results table {R, T,
latency inflation, amplification ratio} × (cell, policy) plus the per-axis shares
and the anchor/jitter/stability legs, ending in exactly one of APPROVE / REJECT /
NULL per the pre-registered rule — reproducible from the fixtures alone,
byte-identical on re-run, no flags.

**Recommendation: sim-ready** — the question is crisp and computable, the bands and
decision rule (with stated evaluation order) are registered above BEFORE any code
exists, the genre's failure modes are pre-empted (model-dependence → exact exogenous
control arm + axis-naming NULL + the named live probe; compliance optimism → the
floor statement; predetermined-outcome risk → the middle cells sit where only the
measured endogenous amplification decides between REJECT and the conditional NULL),
and every outcome changes what a named seat does next. THE ONE QUESTION for the
simulator: *Under the pinned endogenous migration-race model (PRs arrive Poisson
λ ∈ {1, 4, 12}/day, develop W = 8 h, validate V ∈ {0.25, 2, 24} h, fix latency
d = 0.5 h, H = 2,000 h with 200 h warm-up, M = 40 replications per cell-policy, seed
20260723, pinned loop order; policies by pick time — P0 at open/fix, P1 at every
push, P3 at merge (must measure exactly zero collisions); exogenous validation legs
M = 20,000 seed 20260726 gated within 1.0 pp of the exact closed forms
P(N≥1) = p(w₁), P(N≥2) = p(w₁)·p(w₂), E[N] = p(w₁)·e^(λw₂) with p(w) = 1 − e^(−λw);
sensitivity d ∈ {0.25, 2}, W ∈ {1, 24}, jitter leg seed 20260725, stability leg
M = 8 seed 20260724, #1279 anchor leg — all reporting-only), what are R (renumbers
per merged PR) and T (share of merged PRs with ≥ 2 renumbers) per endogenous (λ, V)
cell under P1 — and does the result land APPROVE (R ≤ 0.10 AND T ≤ 0.01 in ≥ 8 of 9
cells → Option 1 suffices, retire Options 2/3 with the quantified reason; checked
first), REJECT (T > 0.05 in ≥ 5 of 9 cells → the shared append point must go, the
per-cell residual-tax table rides to the Option-3 plan as its evidence row), or NULL
(anything else → the flip axis named via per-axis APPROVE-pass shares and median T,
the conditional per-PR-class rule is the citable finding, and the git-history probe
— superbot's real λ, V, W, d from one `git log` pass — is the named next step)?*
Done-when: the committed sim + fixture JSON reproduce the full results table and
summary byte-identically, the exogenous gate and the P3 zero-collision control pass,
the stability leg reproduces the same ruling, and the verdict issues exactly one of
APPROVE/REJECT/NULL per the pre-registered rule (evaluation order stated) with the
Poisson-arrivals and uniform-compliance boundaries stated (P1's residual is a floor
— the APPROVE direction is the fragile one) and the reporting-only legs stated as
legs that cannot flip the decision.
