# Adaptive versioning on early signal — does a two-stage produce→observe→version policy beat V020's mode fork?

> **State:** sim-ready
> **Class:** venture · **Target:** `menno420/venture-lab` (verdict consumer — its book
> pipeline's night-allocation default; verification target `menno420/sim-lab` per the
> Q-0264 pipeline)
> **Grounding:** https://raw.githubusercontent.com/menno420/sim-lab/76dc487ff15ad564156d4309ff76ed0253532f9b/sims/verdict-020-book-versioning/REPORT.md@76dc487ff15ad564156d4309ff76ed0253532f9b · fetched 2026-07-13T07:22Z

**Origin:** drafted under standing owner ORDER 003 (continuous pipeline — "continue
coming up with new ideas, that is your main purpose"). The ORDER 003 VENTURE rotation
slot, round 4: rounds 1–3 were P018 (books → V020 null), P022 (trading → V024 null),
P026 (trading → V028 approve); round 4 returns to the BOOKS half deliberately —
VERDICT 020's own "What it did NOT settle" section names this head verbatim:
"**Adaptive K.** Static quota only; per-title adaptation on early signal is a named
follow-up, not scope creep" (sim-lab `sims/verdict-020-book-versioning/REPORT.md`
@ `76dc487`). V020's NULL found the two publication modes give OPPOSITE static
defaults (Mode P pick-best: K\*=1 in 85.19% of cells; Mode A publish-all: K\*≥2 in
88.89%, grid-median K\*=6) with "the publication mode itself the binding fork" —
so no static quota can be the pipeline default without first settling the mode.
This head asks whether a SIGNAL-DIRECTED policy dissolves the fork: produce breadth
first, observe a cheap noisy early signal per title, then spend the rest of the
budget versioning the winners — one mode-blind policy instead of a mode-conditional
static quota. The successor move is committed precedent (P023 priced V022's routed
lever, P026 priced V024's power half, P029 priced V027's routed slice) — applied to
the venture books slot's own parent for the first time.

## The idea (reasoned to its fuller form — Q-0254 duty)

V020 settled the STATIC question: at fixed budget, versions-per-title quotas are
mode-dependent (pick-best → breadth; publish-all with any audience separation →
version-heavy), and the venture lane was left holding a CONDITIONAL rule that
requires deciding the publication mode before allocating a production night. But
real nights are sequential, and the owner's BOOKS directive ("versions are cheap
once the research exists") makes stage-2 versioning cheap to REDIRECT: write one
version of many titles first, look at whatever early signal exists (first-day
draws, impressions, an internal quality read on version 1), then pour the remaining
budget into extra versions of the titles the signal likes. If the signal is
informative enough, this two-stage policy should capture most of Mode A's
version-heavy upside (extra tickets land on high-θ titles) while never paying
Mode P's versioning tax (a low-fidelity picker wastes extra versions however they
are allocated — adaptation targets titles, not the picker). Whether it actually
does — and how sharp the signal must be — is a computable question on exactly
V020's committed model, with V020's own numbers as chained anchors.

**The sim (fully hermetic — the PROPOSAL 017–029 precedent; every fixture a pinned
constant committed with the sim, zero repo/network reads in the verdict session):**
inherit V020's model VERBATIM — title appeal θ ~ N(0,1); version quality
q_i = θ + ε_i, ε ~ N(0, σ_v²), **σ_v ∈ {0.2, 0.5, 1.0}**; revenue exp(q + L) in
relative units, L ~ N(−σ_m²/2, σ_m²) so E[exp(L)] = 1 exactly,
**σ_m ∈ {0.5, 1.5, 2.5}**; version cost **c ∈ {0.25, 0.5, 0.75}**; budget
**B = 12** (B = 6 reporting-only); Mode P pick-best with fidelity
**f ∈ {0.2, 0.6, 1.0}**; Mode A publish-all with audience separation
**s ∈ {0, 0.5, 1}**, R = (1−s)·max_i r_i + s·Σ_i r_i. ONE new axis: the early
signal on a title's first version, y = θ + ε_1 + η with η ~ N(0, σ_e²),
**σ_e ∈ {0.25, 1.0}** (sharp vs blurry early read — the axis V020 could not carry
because static policies never observe anything). Decision cells: Mode P
c×σ_v×σ_m×f×σ_e = 162, Mode A c×σ_v×σ_m×s×σ_e = 162 — **324 cells**.

Nights are simulated whole (integer quarter-unit budget arithmetic, B4 = 48;
version costs 4c ∈ {1, 2, 3} quarter-units — exact):

- **Adaptive policy AD(ω), ω ∈ {0.5, 0.75}:** stage 1 produces T1 = round(ω·B)
  titles (one version each, cost 1); observe y per title; stage 2 spends the
  remaining budget on extra versions at cost c each, allocated by repeated passes
  over titles in y-descending order (one extra version per title per pass, cap
  **K_cap = 4** versions per title), until the budget cannot buy one more version
  (remainder discarded and reported per cell).
- **Static baselines S(K), K ∈ {1, 2, 3, 4, 6}** (V020's grid): produce
  ⌊B4/(4+4c(K−1))⌋ full K-version titles, then one partial title from the
  remainder (1 version + as many extras as it affords) — the integer-night
  realization of V020's fractional T_eff.
- Per (cell, policy) the metric is **mean night revenue per unit budget** over
  **M = 8,000 nights** (main leg), with the variance-controlled estimator
  discipline V020's intake disclosed (unbiased conditional-expectation /
  control-variate estimators over exactly the pinned draws — formulas committed in
  the fixture; the raw exp(q+L) sample mean cannot meet tight gates at σ_m = 2.5,
  measured by the parent). Per-cell MC SE ships alongside every mean.

**Comparisons (both computed per cell, per ω):** Δ_cond = R_AD/R_cond − 1 against
the PRACTICAL baseline R_cond = the V020-conditional static default (Mode P: K=1;
Mode A: K=6 — the parent's committed grid-median K\*); Δ_or = R_AD/R_or − 1 against
the in-cell static ORACLE R_or = max_K R_S(K) (hindsight-best static quota — the
bar a mode-blind policy must not fall materially below anywhere).

**Pre-registered bands and decision rule (set BEFORE any code; evaluated in this
order, REJECT first — the costly error is adopting an adaptive template that does
not pay, so the protect-the-default arm cannot be shadowed):**

- **REJECT** ("early-signal adaptation buys nothing — V020's conditional rule
  stands") iff for EVERY ω and BOTH σ_e: median-over-cells Δ_cond ≤ +0.02 in BOTH
  modes.
- **APPROVE** ("one mode-blind two-stage policy beats the fork") iff ∃ ONE ω (the
  SAME across all cells, both modes, both σ_e) with median Δ_cond ≥ +0.10 in BOTH
  modes at BOTH σ_e AND Δ_or ≥ −0.02 in ≥ 80% of cells in each of the four
  (mode × σ_e) quadrants — never materially worse than the hindsight-best static
  quota — stability-reproduced.
- **NULL** otherwise — a legitimate, reportable outcome: the flip axis named via
  per-axis median Δ_cond and pass shares over {mode, σ_e, c, σ_v, σ_m, f/s};
  expected candidates: the MODE axis (at f = 0.2 extra versions are near-worthless
  however targeted — adaptation cannot fix a blind picker) and σ_e; the CONDITIONAL
  rule is the citable finding.

**Arms and gates (run invalid on any failure):** Arm A (analytic, seedless) — the
K=1 identity: efficiency = exp((1+σ_v²)/2) exactly in both modes at every (c, σ_m)
(E[exp(L)] = 1 by construction, asserted); Mode A s=1 static additivity
E[R_title(K)] = K·exp((1+σ_v²)/2) exactly; the Mode P f=1 static slice against
V020's committed Arm A quadrature values. **Chained anchor gate:** a per-title-
expectation static leg (the parent's machinery re-derived) at a fresh seed must
reproduce V020's committed ruling row — Mode P share(K\*=1) 0.851851852 / median ΔR
0.0; Mode A share(K\*≥2) 0.888888889 / median ΔR 0.40621411 (source:
`sims/verdict-020-book-versioning/results.json` `ruling` block @ sim-lab
`76dc487ff15ad564156d4309ff76ed0253532f9b`, values quoted verbatim into the
fixture) — within a tolerance PRE-CHECKED in the fixture as ≥ 2.5σ of the
registered-M estimator BEFORE any run (the P029 design rule; the V028
gate-calibration lesson applied at design time, not mid-session). Aux
signal-degeneracy self-check: an aux leg replacing y with pure noise must be
statistically indistinguishable (pre-checked tolerance) from the matched
uniform-order allocation. **Seeds 20260760 main / 20260761 stability (M = 2,000,
must reproduce the ruling) / 20260762 reporting / 20260763 aux** — allocated
strictly above the P029 registry high-water 20260759. Reporting-only legs (cannot
flip): B = 6, K_cap = 6, the perfect-signal σ_e = 0 leg (the adaptation upper
bound), discarded-budget fractions. Pinned loop order, one uniform per normal
(`NormalDist().inv_cdf`), draw-count sentinels, twin decision evaluator, CPython
minor pinned, stdout + results.json byte-identical across two process runs.

**Consequence, pre-registered:** APPROVE → the venture book pipeline adopts the
TWO-STAGE night template (produce breadth → observe the early signal → version the
winners) with the pinned (ω, K_cap) row as the fixed-budget default; the allocation
decision no longer waits on the publish-mode fork or on knowing s/f up front —
V020's conditional rule is superseded FOR ALLOCATION (its two-version live probe
stays named for the LISTING decision, which this sim does not touch). REJECT →
V020's mode-conditional static rule stays the standing default, no adaptive
tooling is built, early-signal capture is NOT required for allocation, and the
quantified reason (the Δ_cond table) rides the manager sweep. NULL → the
named-axis conditional rule ships (e.g. adapt only on publish-all nights when a
sharp early signal exists) and the cheapest LIVE probe is named: one new column in
the pipeline log — the earliest observable per-title signal (first-24h draws or
impressions on version 1) recorded next to later realized draws for the SAME
titles — measures σ_e in the wild at zero new tooling, locating the lane's real
signal cell before any template decision.

## Relations (adjacent heads — deliberately links, not duplication)

- vs [`book-versioning-breadth-depth-allocation-2026-07-13.md`](book-versioning-breadth-depth-allocation-2026-07-13.md)
  (the parent, deliberately): its STATIC question is settled by VERDICT 020 (null —
  modes give opposite defaults) and is NOT re-asked; this head prices the parent
  report's own named follow-up (adaptive K on early signal), with the parent's
  committed ruling row as chained anchors and its model constants inherited
  verbatim. New axes exist in no prior grid: σ_e, the two-stage budget split ω,
  and signal-ordered allocation.
- vs the outbox (PROPOSALs 001–029, re-read at HEAD `0e168bf`): P022/P026 are the
  venture-rotation TRADING half (selection inference/power — zero shared model,
  metric, fixture, or consumer); P026 → V028 is the same successor-move PATTERN
  (pricing a parent verdict's open half) — method precedent only. No proposal
  001–029 touches sequential/adaptive allocation, early signals, or two-stage
  policies (tree-wide `rg -i 'adaptive|two-stage|early[ -]signal|sequential'`,
  `bootstrap.py`/`.substrate` excluded — hits are the parent's and P026's own
  "named follow-up"/over-scope lines and unrelated maker prose).
- vs sim-lab (local clone @ `76dc487`, offset map read): no verdict V001–V030
  runs an adaptive/sequential policy anywhere; V020's REPORT.md is the only file
  containing the phrase "adaptation on early signal" — as its unbuilt follow-up.
- The pricing/bundling shape stays deliberately untouched (webhook price
  elasticity was routed to sim-lab by the venture lane itself — the P018
  precedent clause), and relative units only: Q-0259 r.4 forecast discipline
  untouched.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained modeling head on a
> committed parent model, sim is report-only evidence, no spend/publish/
> irreversible surface — README § probe battery). Verify-first ran FIRST, local
> this slice: (a) **grounding** — V020's REPORT.md "What it did NOT settle"
> re-read at the local sim-lab clone @ `76dc487` (the named follow-up quoted
> verbatim above, not from memory); the anchor constants read from the committed
> `results.json` `ruling` block at the same pin. (b) **dedup** — the sweeps above;
> zero prior adaptive-allocation content in either tree. (c) **feasibility
> arithmetic** — 324 cells × (2 adaptive + shared static legs) × 8,000 nights ×
> ~40 draws/night ≈ high hundreds of millions of draws, the V024/V028 measured
> runtime class (~5 min stdlib CPython); the anchor leg re-runs the parent's
> per-title machinery once.

**1. What is this really?** A pre-registered two-stage allocation-policy sim for
the venture book pipeline: does produce-breadth → observe-early-signal →
version-the-winners beat the static mode-conditional default V020 left behind —
measured across V020's full cell grid extended by one signal-noise axis, against
both the practical baseline (V020's conditional K) and the in-cell static oracle.

**2. What is the possibility space?** (i) Don't run it — the lane keeps a
conditional rule that requires deciding the publish mode before every night, and
the parent's named follow-up stays prose. (ii) Ask the owner which mode books
nights run in — a structured-choice question with zero evidence about whether the
answer even matters under adaptation. (iii) A/B live — the honest endgame for
σ_e, but it costs real nights; the sim tells the lane WHETHER adaptation pays
before any night is spent instrumenting it. (iv) This head: 324 cells, two
policy variants, bands registered first, NULL names the binding axis. (v)
Over-scope (threshold policies with tuned cutoffs, per-title stopping rules,
signal-dependent K_cap, multi-night carryover) — natural follow-ups only if this
lands non-REJECT; the two fixed-ω round-robin variants are the minimal honest
policy family.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~300-line stdlib file: a night is ~12 title/version draws
plus one sort; both modes' revenue rules are the parent's two lines; the analytic
K=1/s=1 identities are one `math.exp` each; the anchor leg re-derives the
parent's per-title expectation machinery it must match. That file yields the
full 324-cell two-policy table, four analytic gates, and a decision the venture
lane can apply to its next production night — from a sim a verdict session runs
cold in minutes.

**4. What breaks it? (assumptions made explicit)** (a) **Models are models** —
the signal model y = θ + ε_1 + η is the neutral minimal choice (the signal reads
version-1 quality, not θ directly); real early signals may be biased, not just
noisy — the σ_e sweep brackets sharpness, not bias, and this is stated in the
verdict (the live probe measures the real thing). (b) **Policy family is finite**
— two ω values, round-robin descending allocation, fixed K_cap; the measured
Δ_cond is a LOWER bound on what smarter adaptation could earn, so a REJECT rules
on this family only (stated; APPROVE is the fragile direction and carries the
oracle-floor clause). (c) **Estimator discipline** — the parent measured that raw
lognormal sample means cannot meet tight gates at σ_m = 2.5; the CE/CV estimator
requirement is inherited by citation, formulas committed in the fixture.
(d) **Relative units only** — allocation, never earnings; Q-0259 r.4 untouched.
(e) **Static-mode boundary** — the sim varies allocation, not the publish mode
itself; mode stays a cell axis exactly as in the parent, so cross-mode policy
switching mid-night is out of scope by design.

**5. What does it unlock?** The venture books slot's first verdict-chained
successor: either a mode-blind two-stage template (the fork dissolved for
allocation), or a measured confirmation that V020's conditional rule is the real
default plus the named σ_e probe — and on any outcome, the first priced answer to
"is early-signal capture worth a pipeline-log column?"

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external
at sim time — every constant ({B, c, σ_v, σ_m, f, s, σ_e, ω, K_cap, K grid, M,
seeds 20260760–63, band constants, anchor row}) is stated in this file and
committed as fixture JSON. Kill tests, run live this slice: an existing
adaptive-allocation head anywhere in either tree (NOT found — sweeps above); the
parent's follow-up already built in sim-lab (NOT found — V020's sims dir carries
only the static grid); infeasible runtime (NOT found — arithmetic in the
preamble). Sim-worthy or judgment-only: sim-worthy — a computable policy
comparison against pre-registered bands; the judgment lines (+0.02/+0.10/−0.02,
80%) are pinned by pre-registration and shipped with full tables so a re-drawn
line re-reads, never re-runs.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab runs it (its harness, its verdict grammar; the V020 machinery and anchor
constants are in its own tree). The verdict's consumer is the venture-lab book
pipeline (night-allocation default + template line) and the manager's routing
sweep. Duplicates nothing: the parent's static grid is chained, not re-run, and
the one venture question already at sim-lab from the lane itself (webhook price
elasticity) is a pricing head this file deliberately avoids.

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one stdlib
file (night engine + both modes + anchor leg + gates), one fixture JSON (all
constants verbatim from this file), one results table {R_AD, R_S(K), Δ_cond,
Δ_or, MC SE} × (324 cells × 2 ω) plus the anchor/stability/reporting legs, ending
in exactly one of APPROVE/REJECT/NULL per the pre-registered rule — reproducible
from the fixtures alone, byte-identical on re-run, no flags.

**Recommendation: sim-ready** — the question is crisp and computable on a
committed parent model, the bands and decision rule are registered above BEFORE
any code exists, the genre's failure modes are pre-empted (anchor-gate
transcription risk → verbatim-quoted ruling row + pre-checked ≥ 2.5σ tolerances;
estimator noise → the parent's own disclosed CE/CV discipline; model-dependence →
dual-baseline comparison + axis-naming NULL), and every outcome changes what the
venture lane does with its next production night. THE ONE QUESTION for the
simulator: *Under V020's pinned model inherited verbatim (B = 12; c ∈ {0.25, 0.5,
0.75}; θ ~ N(0,1); ε ~ N(0, σ_v²), σ_v ∈ {0.2, 0.5, 1.0}; revenue exp(q + L),
σ_m ∈ {0.5, 1.5, 2.5}; Mode P f ∈ {0.2, 0.6, 1.0}; Mode A s ∈ {0, 0.5, 1})
extended by early-signal noise σ_e ∈ {0.25, 1.0} on y = θ + ε_1 + η, do the
two-stage adaptive policies AD(ω ∈ {0.5, 0.75}) (stage 1: round(ω·B) one-version
titles; stage 2: remaining budget as extra versions by y-descending round-robin,
K_cap = 4) beat the V020-conditional static default (Mode P K=1 / Mode A K=6) and
stay within −0.02 of the in-cell static oracle max_K R_S(K) — measured as
Δ_cond and Δ_or per (cell, ω) over M = 8,000 integer-budget nights (seed
20260760; stability M = 2,000 seed 20260761; CE/CV estimators per the V020
disclosure; K=1 and s=1 analytic identities; the chained V020 anchor row
reproduced within pre-checked ≥ 2.5σ tolerances) — landing REJECT (∀ω, both σ_e:
median Δ_cond ≤ +0.02 in both modes; checked FIRST), APPROVE (∃ one ω: median
Δ_cond ≥ +0.10 in both modes at both σ_e AND Δ_or ≥ −0.02 in ≥ 80% of cells in
all four mode×σ_e quadrants, stability-reproduced), or NULL (anything else — flip
axis named via per-axis median Δ_cond and pass shares; expected candidates the
MODE axis and σ_e; the conditional rule the citable finding)?* Done-when: the
committed sim + fixture JSON reproduce the full table and all legs
byte-identically, every gate passes, the stability leg reproduces the ruling, and
the verdict issues exactly one of APPROVE/REJECT/NULL per the pre-registered rule
with the signal-model, policy-family-floor, relative-units, and static-mode
boundaries stated and the reporting-only legs (B = 6, K_cap = 6, σ_e = 0,
discarded-budget fractions) reported as sensitivity that cannot flip the decision.
