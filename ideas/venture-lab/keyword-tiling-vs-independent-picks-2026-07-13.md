# Keyword tiling vs independent picks — is the keyword map's first-claim-wins convention worth its coordination cost in catalog discovery traffic?

> **State:** sim-ready
> **Class:** venture (pipeline rotation — the standing ORDER 003 VENTURE slot,
> round 8, BOOKS half on the slot's own half-alternation read from the actual
> sequence: P018 books (r1) → P022/P026 trading (r2/r3) → P030 books (r4) →
> P034 trading (r5) → P038 books (r6) → P042 products/non-books (r7), so r8 =
> books due; round 8 opened at fleet backlogs with P045 (#343), so the venture
> slot is next per ORDER 004 rule 3.)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/venture-lab@be6c75d4e3379efc108f27d17f2c8ff5adb9a74f · fetched 2026-07-13T20:57:26Z
> (read via the read-only clone this slice, HEAD re-verified by rev-parse at
> drafting. The sim itself is fully hermetic: zero repo/network reads at verdict
> time, every fixture constructed in-sim from the pinned constants in this file)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous
pipeline) and ORDER 004 rule 3's rotation ("fleet backlogs → venture's
book/product space → game mechanics → COMPLETELY UNRELATED domains") — round 8
opened at the fleet-backlogs slot (PROPOSAL 045, PR #343), so this slice serves
the VENTURE slot, books half. The harvested item is the books lane's KDP
keyword/category allocation map (`docs/publishing/keyword-map.md` @ `be6c75d`),
which enforces a deliberate TILING convention across the 14-title catalog on a
stated but never-quantified theory. The map's own header states both the theory
and the mechanism verbatim: *"vetting packets draft \"2 categories + 7
keywords\" in isolation, so with 14 titles heading for the same storefront
several will converge on the same high-value phrases and cannibalize each
other's placement"*, and the adopted cure: *"This map makes each packet CLAIM
its phrases at vetting time — the way `control/claims/` claims work — so the
catalog deliberately tiles the KDP search space instead of piling onto the same
shelf."* The rule is hard — *"First claim on `main` wins a collision."* — and
its category-side rationale is equally explicit (C1): *"Two catalog titles
occupying the same second node compete with each other for the same
also-boughts and category ranking instead of covering two shelves."* The
convention carries a real, visible coordination cost (a CONFLICTS section
resolved *"before a packet ships"*, ⚑ OWNER gates on reallocations, one
ownership row per phrase per PR, register-etiquette rules) and the
cannibalization theory it buys was adopted as a convention and never priced
against the alternative it replaced: INDEPENDENT per-packet choice, each title
picking its own best phrases greedily, collisions allowed. That unpriced fork
is exactly the sim-testable shape. This head builds nothing in venture-lab and
never edits its files (routing is the manager's per Q-0260); it prices the fork
and hands the lane a pre-registered ruling.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested decision, stated back.** Each of the catalog's 14 titles ships
with exactly 2 KDP browse categories + 7 search keywords (the map's own
constants). Pre-map behavior — described by the map itself — is each packet
drafting its 9 cells in isolation: the greedy, collision-blind policy. The map
replaces it with first-claim-wins tiling: no two titles occupy the same cell,
later claimants must spread to uncontested phrases. The theory: same-catalog
collisions cannibalize search placement (rank dilution, split also-boughts).
The counter-theory the map never weighs: search traffic is heavy-tailed, so
forcing late claimants off the few high-traffic phrases onto uncontested tail
phrases may cost more than the collisions ever did — two catalog listings on a
big shelf still capture two result slots, while a "covered" tail shelf is worth
almost nothing. The falsifiable core: **on a pinned synthetic search-shelf
model at the map's own 14 × (2 + 7) constants, does TILE (first-claim-wins,
pinned claim order) beat GREEDY (independent isolation drafting, collisions
allowed) on catalog-level expected discovery traffic by a pre-registered margin
— and across which pre-registered cannibalization-strength × register-overlap
cells does the winner flip?** No prior proposal or verdict prices keyword or
discoverability allocation (Relations below); the heavy-tail counterweight
keeps all three rulings live (liveness below).

**The model (fixed, fully pinned — every constant a decision of this file, none
left to the implementer; probabilities exact rationals throughout).**

- **Two search universes.** Keywords: M = 120 phrases, popularity (probability
  a random discovery event is a search on phrase k) w_k = (1/k)/H_120, the
  exact Zipf weights with H_120 = Σ_{j=1..120} 1/j. Categories: C = 30 browse
  nodes, v_c = (1/c)/H_30. A discovery event is a keyword search with
  probability **3/5** and a category browse with probability **2/5** (invented,
  pinned, disclosed; sensitivity pairs (1/2, 1/2) and (4/5, 1/5),
  reporting-only). All universe constants are invented-but-pinned: the fleet
  has zero live KDP traffic data (see the invented-widths boundary).
- **Catalog and fit.** N = 14 titles, each claims exactly 7 keywords + 2
  categories (the map's constants). Title t has a keyword home h_t and a
  category home g_t on the phrase lines; fit f_{t,k} = (24 − d)/24 for
  d = |k − h_t| < 24 else 0 (keyword window L = 24); category fit
  (10 − d)/10 for d < 10 (window L_c = 10). Fit is the title's genuine
  relevance to the phrase — the register structure. **Overlap axis (3
  pre-registered rows, pinned homes):**
  - **LOW** — spread registers: h_t = 8t − 7 (1, 9, …, 105); g_t = 2t − 1
    (1, 3, …, 27). Keyword tiling fully feasible (98 claims, reachable cells
    1..120); category tiling tight but feasible (28 claims, 30 nodes).
  - **MED** — adjacent registers: h_t = 5t − 4 (1, 6, …, 66); g_t = t
    (1..14). Keyword reachable cells 1..89; categories exhaust (28 claims,
    23 reachable nodes → forced sharing).
  - **HIGH** — crowded registers: h_t = 3t − 2 (1, 4, …, 40); g_t = ⌈t/2⌉
    (1, 1, 2, 2, …, 7 — paired homes, the C1 "same second node" situation
    exactly). Keyword cells exhaust too (98 claims, 63 reachable cells).
  Where tiling exhausts, the pinned **fallback rule** applies: a claimant with
  no unclaimed positive-fit cell left claims its best already-claimed cell —
  the map's own C4 edition-sharing precedent (shared rows exist in the real
  map; §3 exists because niche space is finite). Fallback shares are counted
  and reported per cell.
- **Shelf mechanics (per phrase, both universes).** Shelf k carries E_k
  external competitor listings with pinned fits — the first E_k of
  (4/5, 3/5, 2/5, 1/5); E_k = 4 for k ≤ 20, 3 for 21 ≤ k ≤ 60, 2 for k ≥ 61
  (keywords); E_c = 4 for c ≤ 10, else 3 (categories) — popular turf is more
  contested. A shelf shows S = 5 result positions with pinned position-bias
  click pmf **β = (1/2, 1/4, 1/8, 1/16, 1/16)** (steep — disclosed as GENEROUS
  TO TILE, direction stated in Model basis; flatter leg
  (1/3, 4/15, 1/5, 2/15, 1/15) reporting-only). A discovery event on shelf k
  clicks position i with probability β_i; positions beyond the occupant count
  produce no purchase (mass lost). Occupants are ranked by effective fit,
  descending; ties broken externals-first (conservative against the catalog),
  then by lower title index (the first-claim seniority the map itself uses).
- **The cannibalization rule (the harvested theory, made a dial).** When j ≥ 2
  catalog titles claim the same cell, EACH one's effective fit on that shelf is
  **f / (1 + γ·(j − 1))** — same-catalog rank dilution (C1's "compete with each
  other for the same also-boughts and category ranking", modeled statically).
  Externals are never diluted. **γ ∈ {0, 1/4, 1, 4}** is the second grid axis:
  γ = 0 — no cannibalization, collisions are pure position-stacking; γ = 4 —
  two colliding mates crash to f/5, well below external fits. γ carries no
  measurement anywhere in the fleet — it is THE invented width this verdict is
  conditional on, hence a registered axis, not an assumption.
- **The two policies (allocation fully pinned; allocation is γ-independent by
  construction — both policies score in isolation, which is the point).**
  - **GREEDY (independent picks — the map header's own description of pre-map
    behavior, "draft … in isolation"):** title t scores every positive-fit cell
    by SOLO expected traffic — the position it would take on a shelf of
    externals only (insert f_{t,k} among the external fits, externals-first on
    ties): score = w_k · β_pos (0 if below position 5) — and takes its top 7
    keywords and top 2 categories, ties by lower k. Collisions across titles
    allowed and uncoordinated.
  - **TILE (the map's rule):** identical solo scoring, but titles claim in the
    pinned order t = 1..14 (first-claim-on-main made an order; the map's own
    vetted-packet sequence is its real-world counterpart) and each pick is
    restricted to UNCLAIMED cells; on exhaustion the fallback rule above.
  Within a title, its own picks are distinct cells under both policies.
- **Outcome.** Catalog expected discovery traffic per world:
  T = 3/5 · Σ_k w_k · (catalog click mass on shelf k) + 2/5 · Σ_c v_c ·
  (catalog click mass on node c), computed under that world's allocation and
  the cell's γ. **Primary metric, decision-bearing: the relative gain
  R = (T_TILE − T_GREEDY) / T_GREEDY per grid cell,** exact rational.
  Secondary, reported, NEVER decision-bearing: per-title traffic under both
  policies (the fairness column — tiling taxes late claimants; who pays?),
  GREEDY collision counts and TILE fallback counts per cell, and the
  keyword/category decomposition.

**Two arms.**

- **Arm A (decision arm — exact, seedless):** the whole model is deterministic
  given a grid cell — allocations, rankings, and expected traffic are finite
  exact computations over `fractions.Fraction` (150 shelves, ≤ 19 occupants
  each; 6 allocations — 3 overlap rows × 2 policies — evaluated at 4 γ values
  = the 12-cell R table, plus sensitivity re-evaluations). No enumeration
  blow-up anywhere; the reduced lattice IS the model. The ruling rides Arm A
  alone.
- **Arm S (confirmation arm — seeded MC):** 200,000 discovery events per grid
  cell via `random.Random(20261321)`, cells in the pinned order (LOW, MED,
  HIGH) × (γ = 0, 1/4, 1, 4); per event, pinned draw order: universe coin
  (keyword w.p. 3/5) → phrase index by the universe's popularity pmf → click
  position by β; the SAME draws score both worlds (common random numbers —
  the TILE/GREEDY comparison is variance-reduced; an event scores a catalog
  click in a world iff the clicked position on that shelf is occupied by a
  catalog title there). Estimator: per-world catalog-click frequency vs
  Arm A's exact per-event catalog-click probability. **Agreement gate:**
  |ArmS − ArmA| ≤ 5/1000 absolute on BOTH worlds in EVERY cell (pre-checked
  ≥ 4 SE headroom: SE ≤ 1/(2·√200000) ≈ 0.00112, 4·SE ≈ 0.0045) — any breach
  invalidates the run.

**Seeds (registered):** 20261321 (Arm S main confirmation leg) / 20261322
(stability leg, 20,000 events per cell — the twin evaluators must reproduce
the Arm-A ruling on it under the widened gate ≤ 15/1000, pre-checked ≥ 4 SE at
n = 20,000: 4·SE ≈ 0.0141) / 20261323 (reporting leg — the mass-split,
position-bias, and margin-sweep sensitivity confirmations, 20,000 each) /
20261324 (aux — NEVER read by any decision number; reserved for the named NULL
probe bookkeeping). Allocated strictly above the PROPOSAL 045 high-water
**20261320** — re-swept at drafting: control/outbox.md range notations
(P045's "seeds 20261317–320" is the truncated-literal high-water) plus this
tree plus the sim-lab working copy show nothing ≥ 20261321 as an allocation
(the only larger matches are digit substrings inside sim-lab `results.json`
exact-Fraction numerators and one `se_rel` decimal — data, not seeds; sim-lab
allocates no seeds of its own, the standing P041-established rule). Byte
identity: stdout + results.json byte-identical across two process runs;
CPython minor version pinned in the fixture.

**Pre-registered decision rule (fixed BEFORE any code exists; evaluated in
this order, REJECT FIRST; margin m = 1/50 exact).** Per grid cell, on Arm-A
exact numbers: R = (T_TILE − T_GREEDY)/T_GREEDY.

- **REJECT** ("the tiling convention is dead weight at the modeled widths"):
  **R < 1/50 in ALL 12 cells** — first-claim-wins never buys even 2% catalog
  discovery traffic anywhere on the grid, including the
  strongest-cannibalization corner; the coordination machinery
  (CONFLICTS-before-ship, ⚑ OWNER gates, one-row-per-phrase PR discipline)
  purchases nothing measurable. Checked FIRST — the costly-error rationale:
  the convention imposes a real, recurring process tax on every future packet,
  and an unexamined "of course tiling helps" is exactly the kind of plausible
  theory this pipeline exists to price.
- **APPROVE** ("the convention robustly buys discovery"): **R ≥ 1/50 in ≥ 9 of
  the 12 cells, AND in ≥ 2 of the 3 γ = 1/4 cells** (the
  weakest-nonzero-cannibalization row: an APPROVE that only holds when
  same-catalog dilution is assumed strong would lean entirely on the one
  unmeasured width), the seed-20261322 stability leg reproducing the ruling
  through the twin evaluators. Mutually exclusive with REJECT by construction
  (REJECT: zero cells clear the margin; APPROVE: at least nine do).
- **NULL** (anything else — a legitimate, reportable outcome): the citable pin
  is the full 12-cell R table and the named BINDING AXIS — pre-registered
  candidates: (i) **γ-conditional** — tiling clears the margin only at γ ≥ 1:
  the convention's value hinges on the one unmeasured width, and the finding
  IS that dependence, with the C2 live probe (below) as the pre-priced
  measurement; (ii) **overlap-conditional** — tiling clears the margin only in
  HIGH cells: the map's collision-resolution machinery (C1/C3) earns its keep
  exactly where registers crowd, and its universal per-row discipline
  elsewhere does not; (iii) **arm disagreement** — the agreement gate fails (a
  model/implementation defect is the finding, no ruling issues); (iv)
  **sensitivity straddle** — a reporting-only leg (mass split, flatter β,
  margin m ∈ {1/100, 1/25}) lands a band conjunct on the other side of its
  edge (the named axis is the finding; reporting legs CANNOT flip the
  decision). **Cheapest live probe, named — it is the map's own C2 protocol:**
  *"revisit only if live search results ever show the two listings landing on
  the same results page"* — once ≥ 2 catalog titles are live, one owner browse
  session records, for the two C2 watched-adjacency phrase pairs plus one
  tiled control pair, page-1 co-occurrence and ranks: the live counterpart of
  γ, zero new tooling.

**Band liveness (disclosed — the P034–P045 discipline).** No closed form is on
record for the composed comparison, and the heavy tail keeps it genuinely
open in BOTH directions. For REJECT: w_k is Zipf, so the tail shelves TILE
spreads onto are nearly worthless (w_98/w_1 = 1/98), while GREEDY's collided
listings still hold positions 2–3 of high-w shelves even when diluted — the
coverage gain may be sub-margin everywhere, including γ = 4. For APPROVE: the
steep β means a second listing on the same shelf earns at most half of a fresh
top slot, and at γ ≥ 1 diluted mates drop below the pinned external fits
entirely — spreading plausibly clears 2% in most cells. Whether either side
clears its band — all 12 cells vs 9 of 12 including the γ = 1/4 row — is
genuinely undecided; the γ-conditional and overlap-conditional NULLs are live
in between. This file deliberately pins NO expected landing.

**What a reader DOES differently on the verdict** (all routing lane-side via
the manager per Q-0260 — this repo edits nothing in venture-lab). A
pre-registered APPLICATION GUARD rides every branch: the verdict conditions on
the map's shape @ `be6c75d` (14 titles × 2 categories + 7 keywords,
first-claim-wins, the C1–C4 rules); if the map's claim discipline is
restructured before application, the conditioning is stale and nothing applies
without a re-run on the updated shape.

- **APPROVE** → the map header's cannibalization theory gains its measured
  basis: the convention's coordination cost is priced as worth paying, the
  header cites the 12-cell table instead of gesturing at "cannibalize each
  other's placement", and C2-style KEEP BOTH stays the argued exception, not
  the default.
- **REJECT** → the convention is dead weight at the modeled widths: the
  manager gets a paste-ready structured choice — (a, recommended) relax
  first-claim-wins to C2-style watched adjacencies by default (keep the map as
  an INDEX of who targets what, drop the blocking claim discipline and its
  ⚑ OWNER dispute machinery), or (b) keep the hard rule citing its non-traffic
  benefits (register etiquette, title-adjacent-piracy avoidance — named out of
  this verdict's scope), with the 12-cell table attached either way.
- **NULL** → the named axis ships with its flip boundary: on γ-conditional,
  the C2 watched-adjacency browse check is the pre-priced live measurement; on
  overlap-conditional, the finding routes as "keep the CONFLICTS machinery for
  crowded registers (C1/C3 territory), drop the universal per-row tax" — a
  one-line structured choice with the recommendation first, per the working
  agreement.

**Gates (run invalid on any failure).**

- **Hand fixture (pinned, verified at startup):**
  1. **F1 — popularity normalization:** Σ_k w_k = 1 and Σ_c v_c = 1 exactly;
     w_1/w_2 = 2 exactly.
  2. **F2 — two-title hand world (the fixture that exhibits both regimes):**
     2 shelves, weights (2/3, 1/3); one external of fit 3/4 per shelf; titles
     t1 (fit 1 on shelf 1 only) and t2 (fit 1 on shelf 1, 1/2 on shelf 2); one
     pick each; keyword-only mass. Hand-computed exact values, asserted:
     GREEDY puts both titles on shelf 1; at γ = 1 the external outranks the
     diluted pair (effective 1/2 each) and **T_GREEDY = 2/3 · (1/4 + 1/8) =
     1/4**; at γ = 0 the undiluted pair outranks it and **T_GREEDY = 2/3 ·
     (1/2 + 1/4) = 1/2**. TILE sends t2 to shelf 2 and **T_TILE = 2/3 · 1/2 +
     1/3 · 1/4 = 5/12** at every γ — so the fixture itself shows GREEDY
     winning at γ = 0 (1/2 > 5/12) and TILE winning at γ = 1 (5/12 > 1/4).
  3. **F3 — tie order:** equal effective fits rank externals first (a catalog
     fit of exactly 3/4 sits below the 3/4 external), then by lower title
     index; the TILE claimant order is t = 1..14 exactly.
  4. **F4 — position pmf:** β sums to 1 exactly and is non-increasing; a
     1-occupant shelf yields at most 1/2 click mass (empty-position mass lost).
  5. **F5 — dilution identities:** j = 1 ⇒ effective fit = f at every γ;
     γ = 1, j = 2 ⇒ f/2 exactly; γ = 4, j = 3 ⇒ f/9 exactly.
  6. **F6 — theorem gates (exact, both arms where applicable):**
     (a) T_TILE is γ-invariant within an overlap row whose TILE allocation
     reports ZERO fallback shares, exact equality (LOW keywords by
     construction); in rows with fallback > 0, T_TILE is non-increasing in γ.
     (b) T_GREEDY is non-increasing in γ within every overlap row (dilution
     only demotes catalog listings past never-diluted externals) — violations
     are implementation defects, hard gate. (c) Degenerate-zero: all fits 0 ⇒
     T = 0 exactly for both policies at every γ.
- **Allocation sanity gates:** every title holds exactly 7 + 2 claims in both
  worlds; TILE reports zero same-cell catalog pairs except counted fallback
  shares; GREEDY's collision count in LOW ≤ MED ≤ HIGH (register crowding
  monotonicity — expected-direction, flagged loudly as a first-class anomaly
  on surprise, reporting).
- **Arm agreement gate** (bounds above), **per-leg draw-count sentinels**,
  **twin independently-written decision evaluators**, **stdout + results.json
  byte-identical across two process runs**, **CPython minor pinned** — the
  P017–P045 standing battery.

**Reporting-only legs (Arm A exact re-evaluations + seed-20261323 Arm-S
confirmations at 20,000 events — CANNOT flip the decision):** the full 12-cell
R table with keyword/category decomposition; per-title traffic under both
policies (who pays the tiling tax); GREEDY collision and TILE fallback counts
per cell; the mass-split pairs (1/2, 1/2) and (4/5, 1/5); the flatter position
pmf (1/3, 4/15, 1/5, 2/15, 1/15); the margin sweep m ∈ {1/100, 1/25} (how the
ruling would read at a softer/harsher bar — reported next to the registered
1/50 ruling, never replacing it). Aux seed 20261324 is reserved and never read
by any decision number.

**Grounding / hermeticity.** ZERO network reads at verdict time AND zero repo
reads — the entire world (both Zipf universes, the fit windows and home
tables, the external-competition profile, β, the dilution rule, the γ and
overlap grids, the mass split, the fallback rule, the bands, the hand fixture)
is constructed in-sim from the pinned constants in this file, committed as a
small fixture JSON alongside one stdlib file; the harvested map sentences (the
header's cannibalization theory and tiling cure, "First claim on `main` wins a
collision.", the C1 also-boughts line, the C2 revisit protocol) are quoted
verbatim in the fixture with their `be6c75d` pin for citation only. Decision
arithmetic exact `fractions.Fraction`. Feasibility: Arm A ≈ 6 allocations +
12 × 2 shelf-table evaluations over 150 shelves ≈ 10⁴ Fraction operations —
sub-second; Arm S ≈ 12 × 200,000 events × 3 draws ≈ 7 × 10⁶ RNG calls plus the
20,000-event legs — well under a minute, pure CPython. No dependencies.

## Relations (adjacent heads — deliberately links, not duplication)

- Nearest by MOVE: **P042 → V053** (channel concentration vs diversification)
  — the same allocation-SHAPE (spread vs concentrate scarce placements across
  surfaces under an interference assumption, REJECT-first at a margin), in a
  different world entirely: sale channels for BUILD BUDGET under evidence
  asymmetry there, search-shelf cells for FINISHED titles under rank dilution
  here — zero shared fixture, metric, or consumer (products lane vs books
  lane).
- Nearest by WORLD (the books half's own prior rounds): **P018 → V020 + P030 →
  V032** (versioning breadth-vs-depth) allocate PRODUCTION budget within the
  catalog — their cannibalization sense is sales substitution BETWEEN VERSIONS
  OF ONE TITLE; here production is done, the allocated resource is search
  placement, and the interference is BETWEEN TITLES via shelf rank. **P038 →
  V049** (KU exclusivity fork) is a per-title binary enrollment fork on
  verified royalty constants — no cross-catalog allocation at all; its
  "cannibalization" is borrower-vs-buyer substitution within one title.
- The tree-wide dedup sweep `grep -riE 'tiling|cannibaliz|keyword.map|
  discoverab' --exclude=bootstrap.py --exclude-dir=.substrate` at drafting
  HEAD `fda76a7` hits only the P018/P038 sales-substitution senses above plus
  this head's own files; the outbox token sweep for `keyword` hits only inside
  P018's and P030's model prose (version-differentiation lists), never an
  allocation head. No prior proposal (P001–P045), verdict (V001–V055 span;
  V056 in flight on the parallel session's claim, targeting P045's staleness
  world, unrelated), idea file, or session-card 💡 prices keyword,
  category, or any discoverability-placement allocation.
- Runners-up this slice, weighed and dropped on merit: **pricing C1's specific
  Ultramarine category swap** (a single already-argued qualitative call with a
  pending ⚑ OWNER decision — no undecided quantitative core); **the §3
  name-level reservation system** (blocking value rests on future-title demand
  the fleet has zero data for, and no committed constants anchor a model);
  **the C4 NL-namespace rule** (its no-cross-language-cannibalization premise
  is definitional — different query languages — not falsifiable in-sim). The
  tiling fork won on: the map's own header states the theory AND the
  mechanism, the constants (14 × 2 + 7, first-claim order, the conflict
  machinery) are the map's own, and the landing is genuinely undecided.

## Model basis (declared model-dependence — the P024 discipline)

This verdict's numbers are CONDITIONAL on an embedded model, named up front:

- **(1) Statistical assumptions:** discovery is a single-phrase event stream
  (no cross-shelf substitution — a buyer who misses on one phrase does not
  re-search another); shelves are independent; rankings are static (no
  feedback from sales to rank — C1's also-bought mechanism is DYNAMIC in
  reality and modeled here as static rank dilution γ); external competition
  is fixed and never diluted; both policies score with the same solo
  knowledge (GREEDY is the map header's own "draft … in isolation", TILE adds
  only the claim registry — so the comparison isolates the CONVENTION, not
  information). Invented-and-pinned where the map is silent: the Zipf
  popularity shapes, β, the external fit/count profile, the fit windows and
  home spacings, the 3/5–2/5 mass split, and γ itself — each disclosed
  inline, γ and overlap promoted INTO the decision grid rather than assumed;
  the grounded constants (14 titles, 2 + 7 cells, first-claim-wins order,
  isolation drafting, the fallback/sharing precedent) are the map's own @
  `be6c75d`. **The invented-widths boundary, stated plainly: there is no live
  KDP traffic, search-placement, or sales datapoint anywhere in the fleet**
  (the catalog's own titles are pre-launch/zero-sale), so popularity and
  cannibalization widths bracket SCALE, not measured shape — the cheapest
  live probe (the map's own C2 page-co-occurrence check, one owner browse
  session once two titles are live) is named in the decision rule and
  measures γ's live counterpart directly.
- **(2) Single most-likely-to-flip alternative:** the CLICK MODEL — if real
  buyers scroll deep (flat position bias), multiple same-catalog listings on
  one popular shelf approach additive capture and GREEDY gains; the pinned
  steep β penalizes stacking and is therefore GENEROUS TO APPROVE (direction
  stated — an APPROVE must be read net of it, a REJECT is reinforced by it);
  the flatter reporting leg brackets the direction. Softer flips, named as
  out of the registered scope: dynamic also-bought feedback (compounds either
  way); a buyer's multi-phrase session (substitution would soften both
  policies' losses); the map's non-traffic benefits (etiquette, piracy
  avoidance) — real, unpriced here, and named in the REJECT consequence as
  option (b).

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe
> over a pinned fleet-internal doc, sim is report-only evidence, no
> spend/publish/irreversible surface — README § probe battery). Verify-first
> ran FIRST, live this slice: (a) **source verified at HEAD** — venture-lab
> read via the read-only clone, HEAD
> `be6c75d4e3379efc108f27d17f2c8ff5adb9a74f` rev-parse-confirmed at drafting;
> the header theory/cure sentences, the first-claim rule, the C1 also-boughts
> line, and the C2 revisit protocol all quoted verbatim above from
> `docs/publishing/keyword-map.md` at that pin. (b) **dedup** — the tree-wide
> topic sweep (Relations above) returns only the P018/P038
> sales-substitution senses; PROPOSALs 001–045 checked at HEAD `fda76a7`
> before drafting; the three nearest-neighbor families (P042/V053
> allocation-move kin, P018/P030 within-catalog budget kin, P038 books-half
> fork kin) argued distinct by move/world above. (c) **kill test NOT
> triggered** — no prior proposal, verdict, or 💡 touches
> keyword/discoverability allocation. (d) **feasibility + liveness arithmetic
> checked** — runtime bounded in the preamble (sub-second exact arm + a
> sub-minute MC, stdlib only); liveness disclosed in its own subsection with
> NO expected landing pinned.

**1. What is this really?** A pre-registered pricing of the keyword map's
first-claim-wins tiling convention against the independent-isolation drafting
it replaced: TILE vs GREEDY over a pinned synthetic search-shelf world at the
map's own 14 × (2 categories + 7 keywords) constants, a 12-cell decision grid
(cannibalization strength γ × register overlap), primary metric the relative
catalog discovery-traffic gain R as an exact Fraction, exact deterministic
Arm A confirmed by a seeded MC Arm S under an agreement gate, judged against
bands fixed before any code (REJECT first: the convention is dead weight;
APPROVE: it robustly buys ≥ 2% in ≥ 9/12 cells including the
weakest-dilution row; NULL with four named axes), byte-identical across two
process runs.

**2. What is the possibility space?** (i) Don't run it — the round-8 venture
slot goes unserved and the convention keeps taxing every future packet on an
unpriced theory. (ii) Serve the books half from the publishing plan's other
constants (pricing, tiers) — weaker: P038 already priced the plan's sharpest
per-title fork, and the map is the books lane's newest, most
convention-shaped surface. (iii) A prose answer ("obviously don't compete
with yourself") — ignores the heavy-tail counterweight the map never weighs,
and measures nothing. (iv) Wait for live search data — the RIGHT data
eventually (the C2 probe), but titles are pre-launch and the convention
binds packets NOW, at vetting time. (v) This head: hermetic,
exact-arithmetic, pre-registered — the pipeline's standing shape.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file + one fixture JSON yields: the exact
12-cell TILE-vs-GREEDY surface with the flip boundary located on both the
cannibalization and the overlap axis, a quantified answer to whether the
catalog's coordination machinery buys discovery traffic, the per-title
tiling-tax table (which claimant pays for the convention), and a reusable
pattern — allocation-under-interference on a pinned shelf world with the
interference strength as a registered axis — that transfers to any future
fleet head allocating placements on a shared surface (storefront categories,
site landing pages, Discord discovery channels).

**4. What breaks it? (assumptions made explicit)** (a) **The click model** —
the named most-likely flip; direction stated (steep β is generous to
APPROVE; the flatter leg brackets it). (b) **The invented widths** — γ,
Zipf shapes, external profile, mass split carry no measurement (disclosed;
γ and overlap are grid axes, the rest have reporting legs; the C2 browse
check is the named live measurement). (c) **Static ranking** — C1's
also-bought mechanism is dynamic; modeled as static dilution, named. (d)
**Single-phrase sessions** — no substitution; named out of scope. None of
these is hidden; each is a grid axis, a sensitivity leg, a named flip, or a
stated scope bound.

**5. What does it unlock?** The map's header theory stops being decorative:
either the coordination cost gains a measured justification (APPROVE), or the
manager gets a paste-ready structured choice to relax first-claim-wins to
watched adjacencies (REJECT), or the binding regime is named with the map's
own C2 protocol as the pre-priced measurement (NULL) — all routed lane-side
per Q-0260. The fleet gains its first discoverability-allocation verdict
pattern; the venture slot's books half gains its first post-launch-surface
head (P018/P030/P038 all priced production or enrollment, never placement);
and the C2 watched-adjacency protocol gains a pre-registered consumer for
whatever it observes.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external at verdict time — fully hermetic by construction (the P017–P045
precedent). The harvest grounding is one pinned fleet-repo read, already
taken and quoted. Cheapest kill BEFORE simming: a prior fleet verdict on
placement allocation (none found — P001–P045 and the V001–V055 span swept at
HEAD), or live search-placement data contradicting the model's premise (none
exists — zero organic sales, titles pre-launch). Cheapest confirm AFTER a
NULL: the map's own C2 browse check once two titles are live — zero new
tooling, one owner session, measures γ's live counterpart directly.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab builds and runs the sim (the Q-0264 pipeline's verify seat — this
file is its intake spec); venture-lab's books lane consumes the verdict as a
convention keep/relax/scope decision on the keyword map, routed by the
manager per Q-0260; this repo builds nothing. It displaces nothing in flight
(V056 runs in parallel on P045's staleness world — disjoint fixtures,
disjoint consumers) and duplicates nothing (Relations dedup above; the
P018/P038 cannibalization senses are sales substitution, not search
placement).

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib Python file (both arms + gates + twin evaluators), one fixture JSON
(every pinned constant in this file, copied verbatim: both Zipf universes,
the fit windows and home tables, the external profile, β and the flatter
leg, the dilution rule, the γ × overlap grid, the mass split and its pairs,
the fallback rule, band constants (1/50, 9-of-12, the 2-of-3 γ-row
conjunct), the F1–F6 hand fixture, per-leg event counts, seeds 20261321–324,
the harvested map sentences quoted @ `be6c75d`), one REPORT.md with the
12-cell R table, the per-title tax column, the ruling, and the
named-axis/probe line on NULL — the standing INTAKE/VERDICT grammar, nothing
else.

**Recommendation: sim-ready** — every constant pinned here, bands registered
REJECT-first before any code, seeds 20261321–324 above the verified
high-water 20261320, fully hermetic at verdict time; the honest next step is
the sim itself.
