# The festival the engine cannot show: the timed-events design's piecewise-exact fold and its "visibly richer in the exact T6 proportion" promise are jointly unsatisfiable — the canonical tier-1 start cell pays ZERO extra for every event multiplier below ×2, a +10% window is delivered as +0% or +100% but never +10%, and each of the three available repairs breaks a different committed sentence

> **State:** sim-ready
> **Class:** fleet-backlogs (pipeline rotation — the standing ORDER 003
> FLEET-BACKLOGS slot, round 16 OPENER; round 15 fully served: fleet P073
> (#437), venture P074 (#438), game P075 (#439), unrelated P076 (#440, merged
> 2026-07-15T11:37:34Z by github-actions[bot]), so round 16 reopens at fleet
> backlogs per ORDER 004 rule 3, confirmed against the slot's own spacing
> history (…P065, P069, P073 → P077, spacing 4). Source: SUPERBOT-IDLE — a
> genuinely FRESH fleet-slot source; the slot's full tap history is websites
> (P019, P053), superbot (P021/P033/P061), substrate-kit (P025/P029),
> fleet-manager (P037, P065), curious-research (P041, P049), mineverse (P045,
> P073), trading (P057), own bus (P069) — superbot-idle never.)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline;
> the deliverable is a committed stdlib sim + a citable measured verdict — no
> lane build)
> **Grounding:** https://github.com/menno420/superbot-idle/blob/884aeae9687742a389a2e2086a4cc930e5a4f3ee/docs/design/timed-events-scoping.md@884aeae9687742a389a2e2086a4cc930e5a4f3ee · fetched 2026-07-15T22:57:00Z
> **Grounding:** https://github.com/menno420/superbot-idle/blob/884aeae9687742a389a2e2086a4cc930e5a4f3ee/idle_engine/engine.py@884aeae9687742a389a2e2086a4cc930e5a4f3ee · fetched 2026-07-15T22:57:00Z
> (FIRSTHAND pin: read-only clone via the local git proxy at superbot-idle
> HEAD `884aeae9687742a389a2e2086a4cc930e5a4f3ee` — the scoping doc, the
> engine fold, `idle_engine/economy.py`'s registered percents, the full
> 18-pack theme catalog (`grep base_rate themes/*.yaml`: eighteen `1`s,
> seventeen `5`s, zero `balance` blocks), and `idle_engine/state.py`'s
> schema-bounded `rate_multiplier_pct` all read from that tree. The sim
> itself is fully hermetic: zero repo/network reads at verdict time, every
> fixture constructed in-sim from the pinned constants in this file.)

**Origin:** drafted under the standing owner ORDER 003 (continuous pipeline)
and ORDER 004 rule 3's rotation, round 16 opener at the fleet-backlogs slot,
with the EAP extension to 2026-07-21 (ORDER 015) as the standing frame and
the owner's live resume confirmation this session as the wake authority.

## The harvested tension (both horns committed, verbatim)

`docs/design/timed-events-scoping.md` @ `884aeae` (status `plan`, written
2026-07-11 — **no engine code exists**; § 6: "nothing in this doc is built,
scheduled, or parameter-bearing") scopes timed events (festivals, bonus
windows) and commits, in the same document:

- **Horn 1 — the fold and its exactness argument (§ 2, verbatim):**
  `rate(generator) = base_rate * count * upgrade_pct * prestige_pct *
  milestone_pct * theme_pct * event_pct // 10_000_000_000`, "one more integer
  percent, still ONE floor division per generator per second", with the
  graduation identity "(x * 100) // 10_000_000_000 == x // 100_000_000 making
  no-event spans byte-for-byte identical to today's outputs". § 1a's whole
  recommendation rides on this: rate as an integer-valued step function of
  absolute time is what makes "a single closed-form offline calculation
  equals the sum of any number of smaller ticks" survive events at all.
- **Horn 2 — the visibility promise (§ 1a's recommendation, verbatim):** the
  chosen design "directly produces the thing an event is FOR: the world
  visibly runs richer during the window, for idlers and actives alike, in
  the exact T6 proportion the economy already registered." And SE-2 (§ 5):
  players offline across a full window "get credited exactly the window
  bonus, independent of WHEN they return."

The committed world these sentences must live in (all firsthand @ `884aeae`):
`idle_engine/engine.py`'s shipped six-factor fold `base_rate * count * pct *
global_pct * earned_pct * rate_multiplier_pct // 100_000_000` ("The floor
division happens ONCE per generator per second, inside the rate — so the rate
is a plain integer"); `idle_engine/economy.py`'s registered percents (upgrade
+25/level, prestige +10/unit, milestone +5/earned); every one of the 18
committed theme packs shipping tier-1 `base_rate: 1` (17 ship tier-2 `5`,
zero packs ship a `balance` block, so theme pct is 100 everywhere today,
schema-bounded 90..110 per `state.py`).

**The collision, in one line:** Horn 1 forces the delivered event bonus to be
the integer staircase `Δ = x·E // 10^10 − x // 10^8` (x = the six-factor
pre-floor product), and on the committed low-rate lattice that staircase
cannot express Horn 2's proportionality — the start state's staircase step is
literally zero for the entire sane bonus band.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Five exact structure theorems, EVERY registered numeral produced by the
drafting script this session (`draft_p077.py`, 26/26 checks PASS, exit 0,
~11 s; V080 live-verify + V084 NO-DERIVED-LITERALS):

- **T1 — the DEAD BAND on the canonical cell.** The state every pack's tier-1
  generator starts in (base 1, count 1, no upgrades/prestige/milestones,
  theme 100) has pre-floor product exactly 10^8 and committed rate exactly
  1/s. Under the doc's own fold, `rate_during_event = E // 100`: the event
  pays ZERO extra for EVERY integer E in 101..199 — **99 of 99 dead** — and
  the first paying multiplier is **exactly ×2.00 (E = 200)**, a registered
  margin-0 contact (rate 1 → 2). One upgrade does not fix it (1.25·1.5 =
  1.875 → still 1 at ×1.5); the first ×1.5-paying neighbour needs the upgrade
  PLUS two milestones (1.375·1.5 = 2.0625 → 2). A weekend festival at any
  sane bonus pays a new player **0 extra units in 3600 s, exactly** — the
  precise audience a re-engagement lever targets.
- **T2 — the LATTICE CENSUS.** Over the registered committed lattice (base
  {1,5} × count 1..25 × upgrade level 0..12 × prestige 0..10 × milestones
  0..9 × theme {90,100,110} = 214,500 cells; 214,496 alive at rate ≥ 1; the 4
  zero-rate cells are theme-90 artifacts, reported separately): alive-but-
  event-dead cells number **4,151 at ×1.10 (1.94%), 675 at ×1.25, 56 at
  ×1.50, 14 at ×1.75, and 0 at ×2.00 exactly** (certificate: floor(2r) ≥
  2·floor(r) > floor(r) for r ≥ 1). Deadness is confined to low rates: **zero
  dead cells have rate ≥ 20** at any grid multiplier.
- **T3 — the QUANTIZATION JACKPOT (over-pay is the same theorem).** The
  realized multiplier `(x·E//10^10) / (x//10^8)` versus the nominal `E/100`:
  at ×1.10 the maximum realized/nominal ratio on the lattice is **exactly
  20/11** — the cell (base 1, count 1, L0, prestige 2, milestones 8, theme
  110) has rate 1 and event rate 2, so a +10% window is delivered as +100%.
  The minimum at ×1.10 is 10/11 (the dead start cell: +10% delivered as +0%).
  A +10% event on this lattice is NEVER delivered as +10% at rate 1 — only
  as one of the two staircase steps. The exact envelope `floor(R·E/100) ≤
  RE ≤ ceil((R+1)·E/100) − 1` holds on every alive cell and BOTH edges are
  attained at every grid E.
- **T4 — the REPAIR FORK (three arms, each priced, each breaking a different
  committed sentence).** (a) *V038's own registered fallback* (the
  min-visible-delta floor, sized by V038's inertness table): kills deadness
  by construction but overshoots — on the canonical cell at ×1.10 it delivers
  exactly the same **20/11** ratio (a +10% promise paid as +100%), now
  guaranteed on every previously-dead cell; the T6 proportion dies in the
  opposite direction. (b) *Granularity migration* (milli-unit ledger, G =
  1000): the dead census drops to **0 across the entire lattice × grid**
  (certificate: an alive cell has x ≥ 10^8, so the milli-delta at ×1.10 is
  ≥ 100 − 1 slack = 99 > 0; measured minimum on the canonical cell exactly
  100) — but every registered economy number rescales and the doc's § 3
  "v0 shape needs NO new save state / `state_version` stays 2" promise dies
  in a v3 format bump. (c) *A registered rate-floor precondition* R\* = 20
  ("event proportionality is only promised at rate ≥ 20"): zero code change,
  deadness zero above the floor (T2), and the maximum relative deviation of
  realized vs nominal multiplier on rate-≥ 20 cells is **exactly 1/22
  (4.545%, at ×1.10)** — ≤ 5% — but the start state stays dead: Horn 2's
  "for idlers and actives alike" is conceded exactly where re-engagement
  aims. No arm preserves both horns; the fork is the decision the doc's
  step-2 build gate must take knowingly.
- **T5 — the TRUE SENTENCE, confirmed (the head rejects proportionality, not
  exactness).** Partition equivalence — piecewise closed-form credit equals
  the 1-second tick loop byte-for-byte across event boundaries — verified on
  pencil calendars (5 segments, alternating active/inactive) on four lattice
  cells × all five grid multipliers, including the degenerate all-zero-delta
  trace. SE-2's return-time invariance is REAL under candidate (a); what the
  window credits exactly is, on the dead cells, exactly nothing.

## Pinned model (committed constants — grounded + invented-but-pinned, exact)

- **Committed (firsthand @ `884aeae`):** the seven-factor fold and `//
  10_000_000_000` denominator + graduation identity (timed-events-scoping.md
  § 2, code block verbatim); the shipped six-factor fold and `// 100_000_000`
  (engine.py, `production_per_second`); upgrade +25%/level, prestige
  +10%/unit, milestone +5%/earned, 9 milestone rungs max (economy.py
  registered constants + `build_milestone_specs`); base_rate multiset {1×18,
  5×17} and zero `balance` blocks (themes/\*.yaml); theme pct schema bounds
  90..110 (state.py docstring + theme-balance-v0.md); the visibility and
  SE-2 sentences (§ 1a, § 5); the "no new save state" promise (§ 3); V038's
  "felt = integer rate delta > 0" definition and min-visible-delta fallback
  (sim-lab verdict-038 REPORT, read on the dedup clone @ `d212882`).
- **Invented-but-pinned (disclosed, swept where applicable):** lattice caps
  count ≤ 25, upgrade level ≤ 12, prestige units ≤ 10 (axis-cap convention —
  a NULL axis below); the candidate multiplier grid E ∈ {110, 125, 150, 175,
  200} (the doc registers NO values by design — every theorem is per-E and T1
  quantifies over ALL integer E in 101..199, so no value is assumed); the
  rate-floor candidate R\* = 20; the milli-granularity candidate G = 1000;
  the pencil calendar (7,off)(5,on)(11,off)(3,on)(2,off).
- **Fixture line (registered, the V089 lesson):** Arm-R draw-order grammar —
  one `random.Random(seed)` per trace set; per trace exactly three draws in
  this order: (1) cell index uniform over the alive-cell list in lattice
  iteration order (base, count, L, u, m, theme — itertools.product order),
  (2) E uniform over the grid tuple, (3) window length W uniform integer in
  600..86400 s; 10,000 traces per seed; seeds 20261690/691/692
  reporting-only; aux 20261693 NEVER read.

## Pre-registered decision rule (evaluation order: REJECT first)

- **R1 (dead band):** on the canonical cell, the event delta is 0 for all 99
  integer E in 101..199 AND the first paying E is exactly 200 AND the
  one-upgrade neighbour is still dead at E = 150 — all three by exact
  re-derivation.
- **R2 (census + jackpot):** the alive-cell dead censuses land exactly
  (4,151 / 675 / 56 / 14 / 0 across the grid) AND the ×1.10 realized/nominal
  maximum is exactly 20/11 with a rate-1 witness AND the staircase envelope
  holds with both edges attained at every grid E.
- **R3 (repair fork):** arm (a) overshoot at the canonical cell = 20/11
  exactly; arm (b) milli-census = 0 with the ≥ 99 certificate; arm (c)
  deviation bound = 1/22 exactly with zero dead cells at rate ≥ 20.
- **REJECT** (the doc's Horn-2 sentence is unkeepable under Horn 1 as
  committed) iff R1 AND R2 AND R3. **APPROVE** (proportionality survives)
  iff every grid E has dead census 0 AND realized/nominal ∈ [20/21, 21/20]
  on all alive cells — mutually exclusive with REJECT by arithmetic. **NULL**
  on the named axes: (i) committed-packs sub-lattice (theme = 100 only) —
  pre-checked non-flipping at drafting (the canonical cell is a theme-100
  cell and is dead at four grid multipliers), disclosed for the verdict to
  re-derive; (ii) axis-cap convention (count/L/u caps moved up one notch must
  not flip R1/R3 — R1 is cap-free by construction); (iii) the E-grid
  convention (T1's all-E sweep is grid-free; census rows are per-E findings,
  never aggregated). **INVALID** on any gate failure (F1–F6below).
- Honest-null explicit: every NULL is a finalized, citable finding with its
  exact censuses attached, never a re-run request.

## Gates (run INVALID on any failure)

- **F1 identities:** graduation identity asserted on every lattice cell;
  lattice size 214,500 = 2·25·13·11·10·3; alive = 214,496 with the 4
  zero-rate theme-90 cells enumerated by name.
- **F2 theorems:** T1–T5 re-derived from scratch (zero trust in this file's
  numbers).
- **F3 census anchors:** the dead-census row (4,151 / 675 / 56 / 14 / 0),
  dead-at-rate-≥ 20 row (0/0/0/0/0), jackpot 20/11 + witness cell
  (1,1,0,2,8,110), minimum ratios (10/11, 4/5, 2/3, 4/7, 1), deviation
  1/22, milli-minimum 100, first-paying-E 200, dead-E count 99.
- **F4 pencil worlds:** the 3600 s festival paying 0 on the canonical cell
  and 3600 on the jackpot cell; the five-segment calendar's closed-form ==
  tick-loop equality; the 1.375·1.5 = 2.0625 first-paying neighbour.
- **F5 degeneracy/convention controls:** theme-100 sub-lattice non-flipping;
  cap-bump non-flipping on R1/R3; E = 100 neutrality (delta identically 0).
- **F6 battery:** twin evaluators exact-equal through FOUR typed must-equal
  contacts (99 = 199−101+1; the min-delta overshoot == the ×1.10 jackpot
  ratio, both 20/11; the ×1.10 dead census == the independent Fraction-
  classifier count; payers-at-×2 == alive exactly); Arm-R determinism
  (each seed reproduces itself) and the registered draw-order grammar.

**Arms:** Arm A — pure-integer lattice enumeration (seedless, exact). Arm B —
independently-written Fraction-based classifier + closed-form staircase
envelope, exact-equal to Arm A through the typed contacts. Arm R —
seeded window traces REPORTING-ONLY (drafting previews: seed 20261690 →
(49 dead traces, 40,533,190,487 total extra units), 20261691 →
(41, 39,898,597,051), 20261692 → (43, 39,906,644,697); 10,000 traces each);
aux 20261693 never read by any leg.

## Expected landing (DISCLOSED per the P048–P076 exact-arm norm)

Drafting-run landing: **REJECT** — R1, R2, R3 all fire at the numbers above
(26/26 drafting checks). The sim re-derives everything from scratch; the
disclosed landing binds nothing. Falsifiability is live and named: a
different lattice reading (e.g. the engine folding count OUTSIDE the floor)
would dissolve T1 — it does not (engine.py multiplies count inside the
single floor, verbatim); a milestone-aware start state (packs granting free
milestones) would move the canonical cell — no pack does; and the APPROVE
witness world is constructible (an engine whose ledger is already
milli-granular — arm (b) — satisfies it), so the ruling genuinely
discriminates between the committed engine and its repaired sibling.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

REJECT → paste-ready structured choice to the superbot-idle lane,
recommendation first (Q-0263.2), timed to land BEFORE the doc's step-2 build
slice re-registers shapes:

- **(a, recommended)** adopt the doc's candidate (a) UNCHANGED for exactness
  but amend § 1a's promise sentence and § 5 to scope proportionality: add
  the rate-floor precondition (R\* = 20 delivers ≤ 1/22 deviation — the T3
  envelope is the sizing table) AND pre-register the low-rate reality as
  data ("below rate 20 an event pays in staircase steps; below ×2 the rate-1
  start state pays zero") so SE-1/SE-2 stay exact and no player-facing copy
  over-promises. One doc revision, zero code, zero save-state cost.
- **(b)** milli-granularity migration (G = 1000) in the same PR as the event
  fold: dead census 0 everywhere, true proportionality within 1/1000 — at
  the committed price of save-format v3 + the golden-corpus same-PR policy
  and a full economy-constant re-registration.
- **(c)** V038's min-visible-delta floor extended to the event fold: no dead
  cells, but every low-rate window over-pays up to 20/11 and the graduation
  identity gains a conditional branch — priced here so it is chosen (or not)
  with its exact overshoot table attached, not on vibes.

Known co-consumers of the verdict: the doc's own SE-1..SE-5 registration
(SE-2's "exactly the window bonus" needs the T1 caveat verbatim), V038's
open min-delta-floor sizing thread (arm (a)'s overshoot table is its missing
event-side column), the theme-balance gate (theme 90 creates the 4 zero-rate
cells this census had to special-case), and every fleet surface that folds
stacked integer percents through one floor (mineverse's boost stack, the
games hub's booster fold — the B·T/w-style transfer: check the smallest
pre-floor product before promising a percent).

## Dedup

- Swept at HEAD `97b8865` (idea-engine, `grep -ri 'timed.event|event_pct|
  festival|piecewise|quantiz'` excluding kit machinery) + sim-lab READ-ONLY
  @ `d212882` (newest VERDICT 089): no proposal P001–P076 and no verdict
  V001–V089 prices the event fold, its quantization, or any
  exactness-vs-visibility collision. Nearest kins, disclosed and argued:
  - **V038 (idle economy feel), ASK-1:** established "felt = integer rate
    delta" and the upgrade staircase `1 + L//4` at the start cell, and
    registered the min-visible-delta fallback. IMPORTED here as a fixture
    definition and as repair arm (a) — the new object is the UNBUILT event
    fold's joint-unsatisfiability theorem plus the three-way repair pricing,
    neither of which V038 states or implies (its scope was purchase
    feltness; events did not exist in its packet).
  - **P059's runner-up ledger** dropped "timed-events scoping" ("values
    unregistered; no committed constants to pin") and "milestone feltness
    floor" ("a corollary of V038"). Both drop reasons consumed: this head
    pins committed SHAPES (fold, identity, base-rate multiset), not values —
    T1 quantifies over the entire sane band — and its theorems (dead band,
    jackpot envelope, repair fork) are not corollaries of V038's purchase
    staircase: they price a different fold factor against a different
    committed sentence in a doc V038 predates.
  - **P071/V084 (trophy-record quantization ceiling):** same integer-floor
    family, different repo (superbot hub fishing), different object (a
    reward-record ceiling vs a design-doc collision priced pre-build); zero
    shared fixtures.
  - **P006/P015/P059 (this repo's prior taps, all game/idle slots):** SIM-001
    kernel relay, purchase-path T10, prestige reset policy — different
    documents, different mechanisms; the only shared constants are the
    repo's own registered percents, unavoidable and disclosed. The P076
    card's baton (round-16 GAME slot P079 → superbot-idle by
    least-recently-drawn) is left intact: this fleet tap prices an unbuilt
    scoping doc, not a game-balance surface, and P079 remains free to draw
    the lane's live mechanics.
- Word collisions cited: "granularity" appears in V025/V086 (pooling/rate
  windows — unrelated senses); "quantization" in V084 (argued above);
  "piecewise" in V031 (a quantile description).

## Model basis (declared model-dependence — the P024 discipline)

- **(1) Statistical assumptions:** none in any decision arm — the world is
  deterministic and every decision number is exact integer/Fraction
  arithmetic. Arm R is reporting-only.
- **(2) Modeling assumptions:** the lattice caps (count 25 / L 12 / u 10) are
  reachability conveniences — R1 is cap-free (one cell + an all-E sweep) and
  R3's certificates are algebraic, so the REJECT does not lean on the caps;
  the census rows do, and say so. The multiplier grid is a candidate set BY
  DESIGN (the doc registers no values); per-E rows never aggregate. Theme
  90/110 columns are schema-reachable but pack-unshipped — the theme-100
  sub-lattice control keeps the ruling honest about which world it binds.
- **(3) What a hostile reviewer says:** "V038 already told the lane low
  rates eat percents." Answer: V038 priced PURCHASES against a shipped fold;
  this prices an UNBUILT fold against its own design doc's promise sentence,
  before the build slice re-registers shapes — the cheapest-moment class
  (P073 precedent) — and delivers the three-way repair table that decision
  actually needs. The staircase arithmetic is elementary; the value is that
  it is now a committed, pre-registered, citable object with exact censuses
  attached to the exact sentences it falsifies.

## Probe report (v0, 2026-07-15)

> Single-pass battery (panel not escalated: self-contained mechanism probe on
> committed constants, sim is report-only evidence, no
> spend/publish/irreversible surface — README § probe battery). Verify-first
> ran FIRST, live this slice: (a) **dedup** — the tree-wide and sim-lab
> sweeps above returned no prior pricing of the event fold or the collision
> (nearest kins cited and argued); (b) **kill test NOT triggered** — no prior
> proposal, idea file, or session-card 💡 prices timed events; two prior
> sessions explicitly DECLINED this head and both drop reasons are consumed
> above; (c) **feasibility + liveness arithmetic checked LIVE** — every
> registered numeral was PRODUCED by the drafting script this session
> (`draft_p077.py`, 26/26 PASS, exit 0, ~11 s): the 99/99 dead band and the
> E = 200 contact, the full lattice census row, the jackpot 20/11 and its
> witness, the envelope with both edges attained, all three repair arms, the
> pencil calendars, the four typed contacts, and the Arm-R previews; expected
> landing DISCLOSED (REJECT), all four rulings reachable under the
> pre-registered rule, the APPROVE-witness world named, and the INVALID
> controls gated.

**1. What is this really?** A pre-registered EXACT MEASUREMENT of whether the
timed-events design's two load-bearing sentences can both be true — taken
where the meaning lives: the integer staircase the committed fold actually
delivers, enumerated over the committed parameter lattice. Five theorems
carry it: the canonical cell's dead band (zero bonus below ×2, exactly), the
lattice dead censuses, the quantization jackpot (nominal +10% delivered as
+100%, exactly 20/11), the three-way repair fork with each arm's exact price,
and the confirmation that the doc's EXACTNESS sentence survives — only its
proportionality sentence dies. All decision arithmetic is seedless exact
integers/Fractions judged against bands fixed before any code.

**2. What is the possibility space?** (i) Don't run it — step 2 of the doc's
build plan re-registers the fold shape with the collision unpriced, and the
first real festival ships a zero-paying window to exactly the players it
means to re-engage. (ii) Tap a least-recently-tapped source instead
(websites/curious-research) — keeps rotation cosmetics but leaves a FRESH
source unopened and this committed contradiction unpriced. (iii) A prose bug
report ("your festival pays zero at rate 1") — states the smell, not the
structure: no censuses, no envelope, no repair table, nothing the step-2
gate can decide with. (iv) An MC-only sim — seed noise on exact
combinatorics (the V065/V067 lesson); MC is demoted to reporting.

**3. What is the most advanced capability reachable by the simplest
mechanism?** One floor division, fully understood. The entire head — dead
band, jackpot, envelope, repair pricing — is the arithmetic of
`floor(x·E/10^10) − floor(x/10^8)` taken seriously over a finite committed
lattice. Nothing stochastic, nothing tunable, nothing that cannot be
re-derived from this file in an afternoon.

**4. What breaks it? (assumptions made explicit)** (a) **The fold reading** —
if the build slice folds `count` or the event pct OUTSIDE the single floor,
T1 changes; the doc's § 2 code block and engine.py's shipped precedent both
pin it inside, verbatim, and the sim carries the alternative fold as a named
control. (b) **The lattice caps** — census rows are cap-relative (disclosed);
R1/R3 are cap-free. (c) **The start-state claim** — a pack granting free
milestones/prestige at birth would move the canonical cell; the catalog
sweep found none. (d) **Perception** — "visible" here = integer rate delta
> 0, V038's committed definition; a UI showing fractional rates would change
the question (and the engine exposes none).

**5. What does it unlock?** For the superbot-idle lane: the step-2 build gate
gets its decision table (keep candidate (a) + scope the promise, or pay the
v3 migration, or extend the min-delta floor — each with exact prices) and
SE-2's registration inherits the T1 caveat before it is written down as a
test. For V038's open thread: the event-side overshoot column its fallback
sizing was missing. For the fleet: the transferable one-liner — before
promising a PERCENT through a single-floor integer fold, compute the smallest
pre-floor product it must serve; if that product times the percent's fraction
is below the denominator, the promise is a staircase, not a proportion.

**6. What is the cheapest experiment that decides it?** The whole head IS the
cheapest experiment: a stdlib enumeration of 214,500 cells × 5 multipliers
plus closed-form certificates, ~11 s at drafting, no network, no state, no
seeds in any decision arm. The sim adds only the from-scratch re-derivation,
the twin evaluator, the controls, and the report.

**7. What would make this a mistake to run?** If the collision were already
priced (swept: it is not — V038 is purchases, V084 is fishing records, P059
declined this exact head for a reason that no longer holds); if the doc were
already superseded (swept @ `884aeae`: it is the newest design doc, `plan`
status, nothing built); or if the lane had a live build slice mid-flight that
this REJECT would whipsaw (the lane's current-state shows steady-state hold;
the step-2 gate explicitly waits on a ruling — this IS the input it waits
for). None hold.

**8. How will we know it worked?** A committed sim-lab report with: the full
census table and both staircase edges, the four typed contacts green, the
three repair arms priced at exactly the registered numbers (or a documented
divergence — which would itself be the finding), one ruling under the
pre-registered rule, and — downstream, not gating — the lane's step-2
revision citing the verdict when it either scopes the promise sentence,
schedules the migration, or adopts the floor with the overshoot table
attached.

**Recommendation: sim-ready**
