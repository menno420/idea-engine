# The spool-scale go/no-go margin — how many grams of pocket does the five-second "enough filament?" check need, and does the weigh-it-empty habit measurably pay?

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 FLEET-BACKLOGS slot,
> round 7; the harvest SOURCE rotates to a SIXTH repo for this slot — curious-research,
> the 9th seat (maker/3D-print research), untapped by ANY prior proposal — after
> round 1 websites (P019), round 2 superbot (P021), rounds 3–4 substrate-kit
> (P025/P029), round 5 superbot (P033, the V023-opened thread), round 6 fleet-manager
> (P037)) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/curious-research@a9fd5faa6a10b4d1364d205dbeac7a8678e1bd73 · fetched 2026-07-13T17:49:00Z
> (the harvest-source pin — read via read-only shallow clone this slice, HEAD
> ls-remote-verified; reading path per superbot docs/fleet-reading-path.md §0, raw-
> fetched at drafting; pokemon-mod-lab DARK, skipped per the path's own rule. The sim
> itself is fully hermetic: zero repo/network reads at verdict time, every fixture
> constructed in-sim from the pinned constants in this file)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous pipeline —
"continue coming up with new ideas, that is your main purpose"), the rotation established
by ORDER 004 rule 3 ("fleet backlogs → venture's book/product space → game mechanics →
COMPLETELY UNRELATED domains") — round 6 closed fully served (fleet backlogs → PROPOSAL
037, venture → PROPOSAL 038, game mechanics → PROPOSAL 039, unrelated → PROPOSAL 040),
so round 7 reopens at the FLEET-BACKLOGS slot and this slice serves it. The harvested
item is the spool-weight-scale build's own honest-scope contract (curious-research
`projects/spool-weight-scale/README.md` + `ideas/spool-weight-scale.md` @ `a9fd5fa`,
ritual verdict "build — the honest version"), which ships TWO load-bearing,
never-quantified lines: (1) *"±5 g resolution on a 5 kg cell. 'Roughly half a spool
left' is trustworthy. 'Exactly enough to finish this print' is not — leave yourself
margin"* (§ Honest expectations) — margin named, no number anywhere in either doc; and
(2) *"Your own measured empty weight beats the seeded table, every time"* (§ Stage 2) —
a comparative claim with no measured size. ORDER 004 rule 4 is untouched: nothing here
builds makerbench — this head is harvest → probe → outbox only, and curious-research's
own files are never edited by this repo (routing is the manager's per Q-0260).
**Placement note (decide-and-flag):** sections are roster-derived and inventing one ad
hoc is forbidden (README § Sections; `check_sections.py` reds an ORPHAN section against
the live roster) — curious-research is not a roster-derived section here, so this head
rides `ideas/fleet/`, flagged rather than silently squatting, exactly as the P019/P037
fleet-backlog heads and the P017–P040 rotation heads did.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested decision, stated back.** The spool scale answers one question — the
project's own words: *"do I have enough to start this print?" — in five seconds*
(`ideas/spool-weight-scale.md` §2 @ `a9fd5fa`). Its docs are admirably honest about the
error sources: practical resolution *~±5 g on a 5 kg cell* (cited to PCBSync's ~0.1%-of-
capacity figure), empty spools ranging *cardboard 80–297 g, plastic 113–306 g* with
brand seeds *Prusament ~201 g, Bambu ~256 g, Hatchbox ~225 g, eSun ~224 g* (cited to the
empty-spool catalogs), and drift figures (~2 g per 12–15 min creep under load). But the
DECISION RULE the whole build exists to serve is left unpriced: "leave yourself margin"
names no margin, and the whole workflow fork the docs push hardest — measure YOUR spool
empty once (Stage 2's one real habit) versus trust the seeded brand table — is asserted
("beats it, every time"), never sized. Both are exactly the sim-testable shape: a
threshold rule on a noisy estimate, with every error source already named and half of
them already carrying cited magnitudes. The falsifiable core: **at the cited ±5 g
resolution, does a measured-own-tare reading gate print starts at ≤ 1% mid-print
run-out while declining ≤ 20% of feasible prints, at a pocket margin ≤ 25 g — and does
the weigh-it-empty habit buy at least one brand-spread half-width (≥ 15 g) of margin
over the seeded table?** No closed form is on record for the composed error budget, the
window arithmetic puts the primary cell right at the band (see liveness), and REJECT,
APPROVE, and NULL are all live.

**The model (fixed, fully pinned — every constant a decision of this file, none left to
the implementer; all quantities integer grams, all probabilities exact rationals).**

- **A scenario** = one spool on the platform + one candidate print job, drawn
  independently:
  - **True filament remaining** F ~ uniform integer {0, …, 1000} (a 1 kg spool).
  - **True empty-spool weight** E and **assumed tare** Ê, per tare-knowledge regime:
    - **R-OWN** (the Stage-2 habit — weighed it empty yourself, once): E ~ uniform
      integer {80, …, 306} (the docs' own catalog span); Ê = E + ε_t with ε_t ~ uniform
      integer {−2, …, +2} (a one-time averaged measurement on the same class of scale —
      INVENTED width, pinned, disclosed; sensitivity pair {0} and {−5..+5},
      reporting-only).
    - **R-TABLE** (the seeded brand table, unverified): brand ~ uniform over the four
      seeds {201, 256, 225, 224}; Ê = the seed; E = seed + δ with δ ~ uniform integer
      {−15, …, +15} (brand-lot/spool-version spread — INVENTED width, pinned, disclosed;
      sensitivity pairs {−8..+8} and {−30..+30}, reporting-only).
    - **R-GUESS** (control — no tare knowledge; the docs' "guessing is useless" row):
      Ê = 193 (the 80–306 midpoint); E ~ uniform integer {80, …, 306}.
  - **Scale reading** W = F + E + ε_s with ε_s ~ uniform integer {−5, …, +5} (the cited
    ±5 g practical resolution — the one constant in this model with a source, held
    fixed across regimes). **Drift leg (reporting-only):** W' = W + d, d ~ uniform
    integer {0, …, +8} (a skipped fresh tare after a warm hour, scaled from the cited
    ~2 g/12–15 min creep — INVENTED, pinned, disclosed; it prices the docs' "re-zero
    each session" rule, and CANNOT flip the decision).
  - **Estimated remaining** F̂ = W − Ê (may be negative; no clamping).
  - **Print job:** slicer estimate Ĵ from the pinned mix — w.p. 1/2 uniform integer
    {5, …, 50} (small), w.p. 3/10 uniform {51, …, 200} (medium), w.p. 1/5 uniform
    {201, …, 800} (large) — INVENTED job mix, pinned, disclosed; sensitivity mix
    {1/4, 1/4, 1/2} (large-heavy), reporting-only. **Actual consumption**
    U = Ĵ + ⌈Ĵ·u/100⌉ with u ~ uniform integer {0, …, 5} percent (purge/skirt/waste
    overshoot — INVENTED, pinned, disclosed; sensitivity {0..2} and {0..10},
    reporting-only). Integer ceiling pinned as ⌈a/b⌉ = −(−a // b).
- **The decision rule under test** τ_M: START the print iff F̂ ≥ Ĵ + M, margin M swept
  over the pinned grid **{0, 5, 10, 15, 25, 40, 60, 100} g**.
- **Outcome conventions, pinned:** RUN-OUT iff started AND U > F (U = F exactly —
  finishing with zero grams spare — is NOT a run-out); FEASIBLE iff F ≥ U; FORGONE iff
  declined AND feasible.

**Primary metrics.** Per (regime, M): **RUNOUT** = P(U > F | started) and **FORGONE** =
P(declined | feasible), both exact `fractions.Fraction` in the decision arm. Derived:
**Feas(R)** = {M in the grid : RUNOUT(R, M) ≤ 1/100 AND FORGONE(R, M) ≤ 1/5} and
**M\*(R)** = min Feas(R) (undefined iff Feas(R) = ∅). Reporting per cell: start rate,
feasible share, unconditional run-out, and the full RUNOUT/FORGONE curves.

**Two arms.**

- **Arm A (decision arm — exact, seedless):** every error term lives on a small integer
  lattice and F is uniform on {0..1000}, so each cell's RUNOUT/FORGONE is an exact
  finite sum: enumerate (Ĵ, u, tare-term, ε_s) with exact weights and count the F values
  in the implied integer intervals — closed-form exact rationals, platform-independent,
  no RNG. A convolution collapse (pre-summing ε_s − ε_t, or ε_s − δ, into one net-error
  pmf) is PERMITTED iff it reproduces the direct product enumeration EXACTLY (not
  within tolerance) on the pinned spot-check sub-grid Ĵ ∈ {20, 100, 400, 800} ×
  u ∈ {0, 5} × all three regimes × M ∈ {0, 25}. The ruling rides Arm A alone.
- **Arm S (confirmation arm — seeded MC):** 200,000 scenarios per regime via
  `random.Random(20261301)`, pinned draw order (regime by regime in the order R-OWN,
  R-TABLE, R-GUESS; per scenario: F → tare term(s) → ε_s → job class → Ĵ → u), COMMON
  RANDOM NUMBERS across the margin grid (one scenario set per regime, all eight M
  evaluated on it). **Agreement gate:** |ArmS − ArmA| ≤ 3/1000 absolute on every RUNOUT
  cell and ≤ 1/100 on every FORGONE cell (pre-checked ≥ 4 SE headroom at n = 200,000
  for proportions in the observed range) — any breach invalidates the run.

**Seeds (registered):** 20261301 (Arm S main confirmation leg) / 20261302 (stability
leg, 20,000 scenarios per regime — the twin evaluators must reproduce the Arm-A ruling
on it within the same gate) / 20261303 (reporting leg — the drift and sensitivity
Arm-S confirmations, 20,000 each) / 20261304 (aux — NEVER read by any decision number;
reserved for the named NULL probe). Allocated strictly above the P040/VERDICT-051
high-water 20261300 — re-checked at drafting across every prior outbox block AND the
sim-lab tree at its live HEAD (the only two larger numerals there are substring
artifacts inside a results-JSON fraction and a float, not seeds). Byte-identity:
stdout + results.json byte-identical across two process runs; CPython minor version
pinned in the fixture.

**Pre-registered decision rule (fixed BEFORE any code exists; evaluated in this order,
REJECT FIRST; all band constants exact rationals).**

- **REJECT** ("the five-second go/no-go is dishonest even with the weigh-it-empty
  habit — the scale stays a roughly-gauge and the docs' framing needs a retreat"):
  Feas(R-OWN) = ∅ — no swept margin gets the MEASURED-tare regime to ≤ 1/100 run-out
  without declining > 1/5 of feasible prints. Checked FIRST — the costly-error
  rationale: REJECT retires the head's decision-rule framing outright, so the
  protect-against-false-life arm cannot be shadowed by an eager APPROVE.
- **APPROVE** ("a pocket margin makes the measured-tare gate honest AND the habit is
  load-bearing"): M\*(R-OWN) ≤ 25 AND (Feas(R-TABLE) = ∅ OR M\*(R-TABLE) ≥
  M\*(R-OWN) + 15) — i.e. the docs' margin advice gets its number at ≤ 25 g, and the
  weigh-it-empty habit buys at least one brand-spread half-width of margin over the
  seeded table. Both conjuncts on Arm-A exact numbers; the seed-20261302 stability leg
  must reproduce the ruling.
- **NULL** (anything else — a legitimate, reportable outcome): the citable pin is the
  measured RUNOUT/FORGONE curves and the named BINDING AXIS — pre-registered
  candidates: (i) **big-pocket** — M\*(R-OWN) ∈ (25, 100]: the gate works but needs a
  larger pocket than the docs' casual "leave yourself margin" tone implies (the number
  is the finding); (ii) **table-parity** — M\*(R-OWN) ≤ 25 but M\*(R-TABLE) <
  M\*(R-OWN) + 15: "beats the seeded table, EVERY TIME" is overstated for go/no-go
  purposes at the pinned spreads (the seeded table is nearly as good — the habit's
  real payoff is elsewhere); (iii) **arm disagreement** — the agreement gate fails
  (a model/implementation defect is the finding, no ruling issues); (iv) **sensitivity
  straddle** — a reporting-only sensitivity pair (ε_t, δ, u, job mix, drift) lands the
  primary conjuncts on opposite sides of a band edge (the named axis is the finding;
  reporting legs CANNOT flip the decision, they name the axis). **Cheapest live probe,
  named:** on the real bench, weigh ONE spool ten times with a fresh tare each time
  (pins ε_s), and weigh three empty spools of one brand (pins δ) — zero new tooling,
  the lane's own 🧪 try-it loop, turning the two invented widths into measurements
  before the band is re-litigated.

**Band liveness (disclosed — the P034–P040 discipline).** No closed form is on record
for the composed budget, and the window arithmetic puts the primary cell genuinely on
the band: under R-OWN the estimate error F̂ − F = ε_s − ε_t spans ±7, so at M = 0 a
run-out needs F inside a width-≈(overshoot + 7) window above Ĵ — with the pinned job
mix that lands RUNOUT(R-OWN, 0) in the rough vicinity of 1/100 itself, so whether the
band needs M = 0, 5, 15, or 25 is genuinely open (REJECT is live if FORGONE bites
faster than the tail thins; the FORGONE side is slack at small M by the same
arithmetic, which is exactly why the conjunct pair is the honest test). Under R-TABLE
the error spans ±20, roughly tripling the window — whether that shifts M\* by ≥ 15 g
or the discrete grid absorbs it is the undecided second conjunct. All three rulings
are reachable; this file deliberately pins NO expected landing.

**What a reader DOES differently on the verdict.**

- **APPROVE** → the two doc lines gain numbers, routed lane-side per Q-0260 (this repo
  never edits curious-research files): "leave yourself margin" becomes "leave M\*(R-OWN)
  grams at a fresh tare" in § Honest expectations, and Stage 2's habit line gains its
  measured payoff ("the table costs you ≥ Δ g of margin"); the Stage-3 OLED slice
  inherits a printable rule ("enough for a J-gram job at the M-gram pocket: YES/NO").
- **REJECT** → the go/no-go FRAMING retires from the project docs (the scale is a
  roughly-gauge; "do I have enough to start this print?" is not honestly answerable at
  ±5 g even measured-tare) — a doc-honesty fix routed to the lane, and the drybox/scale
  "filament health" pair loses a promised decision surface before anyone builds on it.
- **NULL** → the conditional finding ships with its named axis; the bench probe above
  is the pre-priced next step (and on table-parity, the docs soften "every time" to the
  measured Δ).

**Gates (run invalid on any failure).**

- **Hand fixture (pinned, verified at startup):** six scenarios with hand-computed
  outcomes — (F, E, Ê, ε_s, Ĵ, u, M) → (W, F̂, U, started, run-out, feasible, forgone):
  1. (500, 225, 225, 0, 100, 0, 25) → W 725, F̂ 500, U 100 → started, no run-out,
     feasible.
  2. (100, 201, 201, +5, 100, 3, 0) → W 306, F̂ 105, U 103 → started, **RUN-OUT**
     (103 > 100), feasible.
  3. (110, 256, 271, −5, 100, 0, 10) → W 361, F̂ 90, U 100 → declined, feasible
     (110 ≥ 100) → **FORGONE**.
  4. (0, 80, 95, +5, 5, 0, 0) → W 85, F̂ −10, U 5 → declined, infeasible → correctly
     declined (negative-estimate path exercised).
  5. (800, 306, 306, −5, 800, 5, 0) → W 1101, F̂ 795, U 840 → declined, infeasible
     (800 < 840) → correctly declined.
  6. (850, 224, 224, +5, 800, 5, 25) → W 1079, F̂ 855, U 840 → started, no run-out
     (840 ≤ 850), feasible.
- **Zero-error identity leg (Arm A, exact):** with ε_s ≡ ε_t ≡ δ ≡ u ≡ 0 and Ê = E,
  RUNOUT(R, M) = 0 for every regime and every M ≥ 0, and FORGONE(R, 0) = 0 — exact
  zeros, not tolerances.
- **Monotonicity (exact, both arms):** RUNOUT non-increasing and FORGONE non-decreasing
  in M within every regime — a theorem under shared enumeration/common random numbers,
  so any violation is an implementation defect: hard gate.
- **Convolution spot-check:** exact equality of the collapsed and direct enumerations
  on the pinned sub-grid (only if the collapse is used).
- **Arm agreement gate** (bounds above), **per-leg draw-count sentinels**, **twin
  independently-written decision evaluators**, **stdout + results.json byte-identical
  across two process runs**, **CPython minor pinned** — the P017–P040 standing battery.
- **R-GUESS control (reporting, expected-direction check flagged loudly on surprise):**
  M\*(R-GUESS) is expected to be much larger than M\*(R-TABLE) or absent — the measured
  content of the docs' "guessing is useless"; a surprise here is printed as a
  first-class anomaly line, never silently absorbed.

**Reporting-only legs (Arm A exact where stated + seed-20261303 Arm-S confirmations —
CANNOT flip the decision):** the full RUNOUT/FORGONE × (regime, M) tables; the drift
leg (d ~ {0..8} skipped-re-tare pricing of the "re-zero each session" rule); the
sensitivity pairs (ε_t ∈ {0} / {−5..5}; δ ∈ {−8..8} / {−30..30}; u ∈ {0..2} / {0..10};
the large-heavy job mix); per-job-class RUNOUT splits (does the risk concentrate in
large jobs, the docs' implicit worry). Aux seed 20261304 is reserved and never read by
any decision number.

**Grounding / hermeticity.** ZERO network reads at verdict time AND zero repo reads —
the entire world (grids, spans, brand seeds, job mix, bands, the six-scenario hand
fixture) is constructed in-sim from the pinned constants in this file, committed as a
small fixture JSON alongside one stdlib file; the harvested doc lines are quoted
verbatim in the fixture with their `a9fd5fa` pin for citation only. Decision
arithmetic exact `fractions.Fraction` at the measurement points; the inner loops are
pure integer work. Feasibility arithmetic: Arm A with the collapse ≈ 796 Ĵ × 6 u × ≤41
net-error values ≈ 2 × 10⁵ interval counts per (regime, M) → ≈ 4.7 × 10⁶ for the full
3 × 8 grid — seconds to a minute in pure CPython; Arm S is 3 × 200,000 scenarios ×
8 margins of integer comparisons — comparable. No dependencies.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the outbox (PROPOSALs 001–040): nothing adjacent by DOMAIN — no proposal touches
  physical measurement error, instrument resolution, tare/calibration knowledge, or
  any bench-hardware decision rule. Nearest by SLOT MOVE: PROPOSAL 037 (fleet-manager
  review-queue N = 50) — the same "price a doc's own unquantified decide-and-flag
  constant on its named failure axes" move, but its world is PR merge streams and
  defect escape models; zero shared fixture, metric, or consumer. Nearest by SURFACE
  RHYME: PROPOSAL 019 (backlog low-water reorder point) — "avoid running dry" as a
  phrase, but P019 is wake-driven queueing of lane work items with signal latency;
  this head is error propagation through a threshold gate on a noisy physical
  estimate. Nearest by METHOD: P037/P038 (exact-Fraction closed-form decision arm +
  seeded confirmation arm with invented-but-pinned mixture constants and sensitivity
  pairs) — method precedent only. The tree-wide dedup sweep `rg -i -g '!bootstrap.py'
  -g '!.substrate' 'spool|filament|load.cell|tare|hx711'` at drafting HEAD `ee4fb76`
  returns hits ONLY in `ideas/venture-lab/maker-gift-repo-blueprint-2026-07-12.md` and
  its companion ecosystem dossier — the makerbench gift-repo BLUEPRINT, which lists
  "Spool-weight scale" as gift project #12 and a CSV print-log filament tracker: a
  repo PLAN with no sim head, no decision rule, and no error model; ORDER 004 rule 4
  keeps makerbench unbuilt and this head does not touch it. No prior proposal,
  verdict (V001–V051 span checked via the outbox/inbox threads at HEAD), idea file,
  or session-card 💡 prices any measurement-error decision rule.
- Sibling head in the SOURCE repo, deliberately out of scope: the drybox humidity
  logger (`ideas/filament-drybox-logger.md` @ `a9fd5fa`) — different sensor, no
  threshold decision named yet; if this verdict lands APPROVE its margin machinery
  does NOT transfer (humidity is a rate problem, not a stock problem).
- Runners-up this slice, weighed and dropped on merit: **mineverse founding-day
  groomed backlog** (8 items @ `f79d0ae` — all UI/refactor/cosmetic or
  externally-blocked; no falsifiable quantitative claim a hermetic sim can price);
  **curious-research tolerance-test-coin clearances** (real bench numbers exist but
  the doc's own point is that the answer is printer-specific — a sim would launder
  bench variance it cannot know); **possibility-dossier slicer-experiment heads**
  (genuinely physical — filament rheology; no honest stdlib model). The spool-scale
  margin won on: every error source already named in the source doc, one cited
  magnitude anchoring the model, a crisp threshold rule, and a genuinely undecided
  landing.

## Model basis (declared model-dependence — the P024 discipline)

This verdict's numbers are CONDITIONAL on an embedded model, named up front:

- **(1) Statistical assumption:** independent uniform integer error terms at pinned
  widths — ε_s (±5, the one CITED constant), ε_t (±2), δ (±15), u (0–5%), and the
  three-class job mix are INVENTED where not cited, disclosed inline, each with a
  reporting-only sensitivity pair. NO bench datapoint exists anywhere in the fleet
  (the source repo's own sketch "has not been compiled" — its README says the owner's
  IDE will be its first real compile), so the sweeps bracket scale, not shape, and the
  named live probe measures ε_s and δ directly at zero new tooling.
- **(2) Single most-likely-to-flip alternative:** ERROR CORRELATION — under R-OWN the
  tare was measured on the SAME instrument, so a shared calibration-gain bias would
  partially CANCEL in F̂ = W − Ê, making the real R-OWN regime BETTER than this
  independence model says (independence is therefore conservative against APPROVE's
  habit-pays conjunct, stated); heavier-tailed drift distributions (the docs' hot-
  afternoon story) would push the other way — the drift leg brackets that direction
  reporting-only. Softer flips, named as out of the registered scope: non-uniform F
  (spools cluster near full/empty in real shelves), multi-read averaging at decision
  time, and per-material density corrections.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe over a
> pinned public doc, sim is report-only evidence, no spend/publish/irreversible
> surface — README § probe battery). Verify-first ran FIRST, live this slice:
> (a) **source verified at HEAD** — curious-research shallow-cloned, HEAD
> `a9fd5faa6a10b4d1364d205dbeac7a8678e1bd73` ls-remote-confirmed; both harvested lines
> quoted verbatim above from `projects/spool-weight-scale/README.md` and
> `ideas/spool-weight-scale.md` at that pin; no SIM-REQUEST exists in the source
> repo's `control/outbox.md` (REPORT 001 only — nothing to duplicate). (b) **dedup**
> — the tree-wide sweep (Relations above) returns only the makerbench blueprint
> mentions; PROPOSALs 001–040 re-read at HEAD `ee4fb76` before drafting; the six
> prior fleet-backlog occupants harvested five other repos (websites, superbot ×2,
> substrate-kit ×2, fleet-manager). (c) **kill test NOT triggered** — no prior
> proposal, verdict, or 💡 touches measurement-error budgets or physical-inventory
> gating. (d) **feasibility + liveness arithmetic checked** — runtime bounded in the
> preamble (seconds to minutes, stdlib only); liveness disclosed in its own
> subsection with NO expected landing pinned.

**1. What is this really?** A pre-registered error-budget MEASUREMENT of the one
decision the spool-scale build exists to serve: the go/no-go margin grid × three
tare-knowledge regimes at the cited ±5 g resolution, RUNOUT and FORGONE as exact
Fractions from a seedless enumeration arm confirmed by a seeded MC arm, judged against
bands fixed before any code (REJECT first: measured-tare infeasible; APPROVE: pocket
≤ 25 g AND the habit worth ≥ 15 g; NULL with four named axes), byte-identical across
two process runs.

**2. What is the possibility space?** (i) Don't run it — the round-7 fleet-backlogs
slot goes unserved and the rotation's standing rule is dead letter this cycle.
(ii) Re-harvest an already-tapped repo — legal but weaker: six rounds have drawn five
repos, and the untapped ninth seat carries a committed, honesty-marked backlog built
for exactly this kind of pricing. (iii) A prose answer ("±5 g, so leave ~10 g") —
invents the number the docs honestly declined to invent, measures nothing, prices
neither conjunct. (iv) A bench experiment — the RIGHT eventual step but not this
seat's to run (owner hardware, owner hands); the sim prices the decision NOW and its
NULL branch names that exact bench probe with the two dials it would pin. (v) This
head: hermetic, exact-arithmetic, pre-registered — the pipeline's standing shape.

**3. What is the most advanced capability reachable by the simplest implementation?**
One stdlib file + one fixture JSON yields: exact closed-form RUNOUT/FORGONE surfaces
over 3 regimes × 8 margins, the minimal-feasible-margin function M\*(·), a quantified
price on a habit the source docs assert qualitatively, a control row quantifying
"guessing is useless", a drift row pricing the "re-zero each session" rule, and a
reusable pattern — threshold-gate-on-noisy-estimate error budgets — that transfers to
any future fleet head with an instrument and a go/no-go (the drybox logger's eventual
alarm threshold, superbot-games' sensor-flavored mechanics).

**4. What breaks it? (assumptions made explicit)** (a) **The invented widths** — ε_t,
δ, u, and the job mix carry no bench evidence (disclosed; sensitivity pairs bracket
scale; the NULL probe measures the two that matter). (b) **Independence** — the
correlated-calibration flip is named as most-likely-to-flip, with its direction
relative to each band stated. (c) **Uniform F** — real shelves cluster; out of
registered scope, named. (d) **The 1 kg spool world** — 250 g/2.3 kg spools rescale
the span; the conclusions are for the pinned world only. None of these is hidden; all
four are either a sensitivity leg, a named flip, or a stated scope bound.

**5. What does it unlock?** The docs' two unquantified lines become numbers a lane
can commit (routed via the manager, Q-0260); the Stage-3 OLED slice inherits a
printable decision rule; the drybox sibling inherits the method when its threshold
head matures; the fleet gains its first measurement-error verdict pattern; and the
rotation ledger gains its sixth distinct harvest repo, keeping the slot's
source-diversity rule alive.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external at
verdict time — fully hermetic by construction (the P017 precedent). The harvest
grounding is one pinned public repo read, already taken and quoted. Cheapest kill
BEFORE simming: if someone finds a prior fleet verdict pricing scale-error gating
(none found — V001–V051 threads swept at HEAD), or a bench measurement of ε_s/δ
contradicting the pinned widths (none exists — the sketch has never compiled), the
grid re-pins before any code. Cheapest confirm AFTER a NULL: the named ten-weighings
+ three-empties bench probe, zero new tooling.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
builds and runs the sim (the Q-0264 pipeline's verify seat — this file is its intake
spec); curious-research consumes the verdict as a doc-line edit it makes itself on
manager routing; this repo builds nothing. It displaces nothing in flight (V050
merged, V051 in flight on a parallel session's claim — different world entirely) and
duplicates nothing (Relations dedup above; the makerbench blueprint is a plan, not a
sim, and stays unbuilt per ORDER 004 rule 4).

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one stdlib
Python file (both arms + gates + twin evaluators), one fixture JSON (every pinned
constant in this file, copied verbatim), one REPORT.md with the two tables, the
M\*(·) row, the ruling, and the named-axis/probe line on NULL — the standing
INTAKE/VERDICT grammar, nothing else.

**Recommendation: sim-ready** — every constant pinned here, bands registered REJECT-
first before any code, seeds 20261301–304 above the verified high-water, fully
hermetic at verdict time; the honest next step is the sim itself.
