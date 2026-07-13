# Kill-clock horizon — is the products lane's T+14 zero-sale kill clock right-sized against its own committed alternatives on proven-product throughput?

> **State:** sim-ready
> **Class:** venture (pipeline rotation — the standing ORDER 003 VENTURE slot,
> round 9, NON-BOOKS/PRODUCTS half on the slot's own half-alternation read from
> the actual sequence: P018 books (r1) → P022/P026 trading (r2/r3) → P030 books
> (r4) → P034 trading (r5) → P038 books (r6) → P042 products (r7) → P046 books
> (r8), so r9 = non-books due, served from the PRODUCTS lane per P042's own
> precedent reading of ORDER 004's "venture's book/product space"; round 9
> opened at fleet backlogs with P049 (#358), so the venture slot is next per
> ORDER 004 rule 3.)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/idea-engine@763b19e26d237f3d042a32ebf32f02bc297cd7c6 · fetched 2026-07-13T23:19:54Z
> (the SECONDHAND pin, disclosed: every venture-lab constant used here is quoted
> from PROPOSAL 042's verbatim harvest of venture-lab @
> `be6c75d4e3379efc108f27d17f2c8ff5adb9a74f`, as recorded in THIS repo's
> `control/outbox.md` at the HEAD above — a direct venture-lab read was attempted
> exactly once this session and denied, verbatim: `Access denied: repository
> "menno420/venture-lab" is not configured for this session. Allowed
> repositories: menno420/idea-engine, menno420/sim-lab` — deny-wins, no retry.
> The sim itself is fully hermetic: zero repo/network reads at verdict time,
> every fixture constructed in-sim from the pinned constants in this file.)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous
pipeline) and ORDER 004 rule 3's rotation ("fleet backlogs → venture's
book/product space → game mechanics → COMPLETELY UNRELATED domains") — round 9
opened at the fleet-backlogs slot (PROPOSAL 049, PR #358), so this slice serves
the VENTURE slot, products half. The harvested item is the products lane's
KILL-CLOCK FAMILY — three committed clock values that all gate the same
decision, "when does a launched zero-sale product stop occupying the lane's
attention": the **T+7 checkpoint** (armed for 2026-07-19), the **T+14 kill
rule** (armed for 2026-07-26), and the **30-day signal window** that P042's
harvest calls "the lane's own kill-rule window", with success defined by the
same harvest as the **≥1-organic-sale leg** (the reads/inbound leg was named
out of scope there and stays out of scope here). The lane's own evidence line
rides the same harvest: *"0 organic sales across 7 click-queued products"*.
P042 → V053 priced WHERE the next build token goes (channel concentration vs
diversification) while explicitly taking the kill semantics as given — its
consequence section names the T+7/T+14 clocks only as "the pre-priced live
probe". Nobody has ever priced the clock ITSELF: T+14 sits between two other
committed values of the very same dial, and which of the three maximizes
proven products per slot-quarter is a real, undecided allocation question —
kill early and the slot recycles into fresh draws faster; kill late and slow
burners get their chance. This head builds nothing in venture-lab and never
edits its files (routing is the manager's per Q-0260); it prices the dial and
hands the lane a pre-registered ruling.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested decision, stated back.** A launched product either records its
first organic sale (it is PROVEN — it graduates from the experimental slot to
the catalog) or it sits at zero. The lane's committed machinery checks at T+7,
kills at T+14, and calls 30 days the signal window — three values of ONE dial,
shipped without a stated tradeoff. The tradeoff is real and two-sided: a
zero-sale product at day 14 might be dead (most are — the lane's own 0-for-7
says so) or a slow burner whose first sale was 10 days away; killing it frees
the slot for a fresh draw after a build downtime, keeping it burns slot-days
on a maybe. The falsifiable core: **on a pinned renewal model of one
experimental product slot, at the lane's own three committed clock values
T ∈ {7, 14, 30}, does the shipped KILL@14 maximize expected proven products
per 90 slot-days to within a pre-registered margin across a pre-registered
prior-belief × build-downtime grid — and where it loses, in which DIRECTION
(shorter or longer) does the winner lie?** No prior proposal or verdict prices
a kill/stop threshold in the venture world (Relations below); the two-sided
structure keeps all three rulings live (liveness below — and the drafting-time
landing is computed and DISCLOSED per the P048/P049 closed-form-arm norm).

**The model (fixed, fully pinned — every constant a decision of this file,
none left to the implementer; probabilities exact rationals throughout).**

- **Time and slot.** Time in whole days. ONE experimental slot, horizon
  **H = 90** slot-days (invented, pinned; sensitivity H ∈ {60, 180},
  reporting-only). Slots are modeled independently, so per-slot results
  multiply out to any slot count — disclosed as the independence boundary.
- **Product draws.** Each launched product carries an unknown true per-day
  organic-sale probability p, i.i.d. across products, drawn from the cell's
  prior over the pinned grid **P = {0, 1/60, 1/30, 1/14, 1/7}** — a dead
  product, a ~60-day burner, a ~30-day burner, a ~14-day burner, a ~7-day
  burner (mean first-sale times 1/p; the grid brackets the three clock values
  deliberately). Sensitivity grid P′ = {0, 1/90, 1/45, 1/21, 1/10},
  reporting-only.
- **Prior-belief axis (3 pre-registered pmfs over P — the lane's 0-for-7
  evidence motivates dead-heavy mass; the pmfs are invented-but-pinned and
  the axis is IN the grid, not assumed):**
  - **SKEPTIC** (3/4, 1/10, 3/40, 1/20, 1/40) — the 0-for-7 reading: most
    products are dead.
  - **NEUTRAL** (1/2, 1/8, 1/8, 1/8, 1/8) — half dead, flat over the living.
  - **HOPEFUL** (1/4, 1/4, 1/4, 3/20, 1/10) — most products would sell
    eventually.
- **Build-downtime axis.** Replacing a product costs **B slot-days** of
  downtime (the lane's token-denominated BUILD caps — 70k/60k/50k per P042's
  harvest — converted to slot-days by fiat; the conversion is invented,
  disclosed, and promoted INTO the grid): **B ∈ {2, 5, 10}**.
- **Policy KILL@T, T ∈ {7, 14, 30} (the lane's own three committed values —
  no invented fourth arm; the decision compares the lane to itself).** Launch;
  each live day is an independent Bernoulli(p) sale trial. First sale on day
  x ≤ T → **GRADUATION** (count 1; the product leaves the experimental slot
  for the catalog — slot freed). Zero sales through day T → **KILL** (count
  0). Either way the slot then spends B days building; the next product
  launches from a fresh prior draw. Products still live at horizon end
  contribute nothing further. (The alternative world where a graduated
  product BLOCKS its slot for the rest of the horizon — the
  maintenance-drag reading — is a named sensitivity world, reporting-only.)
- **Outcome.** **G(cell, T) = expected graduations in H slot-days**, exact
  rational. Primary metric, decision-bearing: the shipped clock's relative
  shortfall **D(cell) = (max_T G(cell, T) − G(cell, 14)) / G(cell, 14)**,
  exact per cell, with the winning direction (argmax T, ties to 14) recorded.
  Secondary, reported, NEVER decision-bearing: the full 9-cell × 3-clock G
  table, expected kills and expected slot-days-idle per cell, the per-p
  conditional graduation split (WHICH burners each clock saves or kills),
  and the wasted-graduation column (graduations the shorter clock forfeits).
- **The grid: 3 priors × 3 build downtimes = 9 pre-registered cells**, cell
  order pinned (SKEPTIC, NEUTRAL, HOPEFUL) × (B = 2, 5, 10).

**Two arms.**

- **Arm A (decision arm — exact, seedless):** the renewal structure gives a
  finite exact dynamic program over `fractions.Fraction`: with G(h) the
  expected further graduations when a fresh draw launches with h slot-days
  left (G(h) = 0 for h ≤ 0),
  G(h) = Σ_p π(p) · [ Σ_{x=1..min(T,h)} p(1−p)^{x−1} · (1 + G(h−x−B)) +
  1{T < h} · (1−p)^T · G(h−T−B) ], and the cell value is G(H). ≤ H × |P| × T
  Fraction terms per (cell, clock) — sub-second, stdlib only. The ruling
  rides Arm A alone.
- **Arm S (confirmation arm — seeded MC):** **N = 200,000 trajectories per
  (cell, clock)** via `random.Random(20261337)`, cells in the pinned order,
  clocks in order (7, 14, 30) within a cell; per trajectory, pinned draw
  order: p from the cell prior, then daily sale trials day-by-day until
  graduation/kill/horizon, repeating across renewals. Estimator: mean
  graduations per trajectory. **Agreement gate:** |ArmS − ArmA| ≤ 3/200
  absolute on EVERY (cell, clock) AND ≥ 4·SE headroom verified per leg from
  the per-trajectory sample SD (G per trajectory is bounded by
  ⌈H/(1+B)⌉ ≤ 30, SD in practice ≈ 0.5–1.5, so 4·SE ≈ 0.004–0.013 at
  N = 200,000 — the pre-check asserts 4·SE ≤ 3/200 per leg) — any breach
  invalidates the run.

**Seeds (registered):** 20261337 (Arm S main confirmation leg) / 20261338
(stability leg, 20,000 trajectories per (cell, clock) — the twin evaluators
must reproduce the Arm-A ruling on it under the widened gate ≤ 3/50,
pre-checked ≥ 4·SE at n = 20,000) / 20261339 (reporting leg — the H ∈ {60,
180}, grid-P′, graduation-blocks-slot, and margin-sweep sensitivity
confirmations, 20,000 each) / 20261340 (aux — NEVER read by any decision
number; reserved for the named NULL probe bookkeeping). Allocated strictly
above the PROPOSAL 049 high-water **20261336** — re-swept at drafting:
digit-boundary regex over this tree at HEAD `763b19e` plus the sim-lab
working copy with `results.json` excluded shows max allocation 20261336 (the
larger numerals — 20261542/20261664/20261833 aliases and kin — are digit
substrings inside sim-lab `results.json` exact-Fraction numerators, data not
seeds; sim-lab allocates no seeds of its own, the standing P041-established
rule). Byte identity: stdout + results.json byte-identical across two process
runs; Arm A platform-independent exact Fractions, Arm S pinned to a stated
CPython minor version.

**Pre-registered decision rule (fixed BEFORE any code exists; evaluated in
this order, REJECT FIRST; margin m = 1/20 exact).** Per cell, on Arm-A exact
numbers: D(cell) and the winning direction dir(cell) ∈ {SHORTER (argmax
T = 7), HELD (argmax T = 14, D = 0), LONGER (argmax T = 30)}.

- **REJECT** ("the shipped T+14 kill clock is materially mis-set at the
  modeled populations — one of the lane's own OTHER committed clock values
  beats it by ≥ 5% proven-product throughput, consistently"): **D(cell) ≥
  1/20 in ≥ 7 of 9 cells AND dir agrees (all SHORTER or all LONGER) in every
  such cell.** Checked FIRST — the costly-error rationale: the T+14 clock
  gates EVERY future product the lane launches; a mis-set threshold silently
  taxes the whole pipeline forever, and "T+14 feels reasonable" is exactly
  the kind of unpriced default this pipeline exists to price.
- **APPROVE** ("T+14 is right-sized among the lane's own committed clock
  values"): **D(cell) < 1/20 in ≥ 7 of 9 cells, AND in ≥ 2 of the 3 SKEPTIC
  cells** (the evidence-favored row — the lane's own 0-for-7 makes the
  dead-heavy prior the operative one, so the ruling must hold there), the
  seed-20261338 stability leg reproducing the ruling through the twin
  evaluators. Mutually exclusive with REJECT by arithmetic (REJECT needs ≥ 7
  cells AT/OVER the margin, APPROVE needs ≥ 7 under it; 7 + 7 > 9).
- **NULL** (anything else — a legitimate, reportable outcome): the citable
  pin is the full 9-cell D table with directions and the named BINDING AXIS
  — pre-registered candidates: (i) **direction-straddle** — SHORTER wins
  some over-margin cells and LONGER others (the drafting-time tables already
  show the shape: fast-build worlds favor T = 7, the slow-build optimistic
  corner favors T = 30): the finding IS that the right clock hinges on the
  dead-share belief and the build cost, with the flip boundary named; (ii)
  **build-cost-conditional** — over-margin cells concentrate in one B
  column: the clock should be set WITH the build-downtime number, not
  independently of it; (iii) **margin-thin** — the ruling flips inside the
  margin sweep m ∈ {1/50, 1/10} (reported next to the registered 1/20
  ruling, never replacing it); (iv) **arm disagreement** — the agreement
  gate fails (a model/implementation defect is the finding, no ruling
  issues); (v) **sensitivity straddle** — a reporting-only leg (H, P′,
  graduation-blocks-slot) lands a band conjunct on the other side of its
  edge (the named axis is the finding; reporting legs CANNOT flip the
  decision). **Cheapest live probe, named — it is the lane's own already-
  armed machinery:** every launched product carries a launch date and (if
  any) a first-sale date; the empirical first-sale-time histogram the lane
  accumulates for free is exactly the p-mixture this grid brackets — each
  observed product pins one row, zero new tooling.

**Expected landing, DISCLOSED (the P048/P049 closed-form-arm norm — the
decision arm is an exact DP, so the drafting-time landing was computed and
is disclosed rather than feigning openness; the sim re-derives everything
from scratch and must not trust these numbers).** At the pinned constants,
the drafting DP lands **APPROVE, thinly**: D = 0 exactly in 5 of 9 cells
(T = 14 is itself the argmax), and the four nonzero cells are SKEPTIC/B=2
D ≈ 0.0440 (SHORTER), NEUTRAL/B=2 D ≈ 0.0699 (SHORTER — the ONE cell over
the 1/20 margin), HOPEFUL/B=2 D ≈ 0.0036 (SHORTER), HOPEFUL/B=10 D ≈ 0.0482
(LONGER) — so APPROVE fires 8-of-9 with 3/3 SKEPTIC cells, and REJECT is
nowhere near (1 over-margin cell vs the 7 required). Falsifiability is real
and disclosed: two cells sit just UNDER the margin edge (0.0440, 0.0482),
one sits over it, and the directions already straddle — at m = 1/100 the
ruling would be the direction-straddle NULL, and the P′/H sensitivity worlds
plausibly move the near-edge cells across. A sharpening the disclosure buys:
T = 30 (waiting out the full signal window) is the argmax in exactly ONE
corner and is beaten in the other 8 cells — whatever the ruling, the "let it
run to 30" instinct loses almost everywhere at these widths.

**What a reader DOES differently on the verdict** (all routing lane-side via
the manager per Q-0260 — this repo edits nothing in venture-lab). A
pre-registered APPLICATION GUARD rides every branch, TWO conditions: (1) the
verdict conditions on the kill-clock family as pinned here secondhand — the
≥1-organic-sale success leg with clock values {7, 14, 30}; if the lane's
committed kill-rule text differs materially from this shape (a dominant
reads/inbound leg, different clock values, a non-kill T+14 semantics), the
conditioning is stale and nothing applies without a re-run on the true shape
— the pin is honest about being secondhand (Grounding above); (2) it
conditions on "0 organic sales as of 2026-07-13" — a live organic sale
before application moves the lane off the modeled prior row and stales the
conditioning (the P042/V053 guard, inherited).

- **APPROVE** → the T+14 kill clock gains its measured basis: the lane cites
  the 9-cell table instead of a bare date, and the T+30 instinct ("give it
  the full signal window") is retired with numbers.
- **REJECT** → the manager gets a paste-ready structured choice — (a,
  recommended if dir = SHORTER) move the kill decision to the T+7 checkpoint
  the lane ALREADY runs (zero new machinery — the checkpoint becomes the
  kill), or (b, if dir = LONGER) extend the kill to the 30-day signal window
  — with the 9-cell table and the per-p conditional split attached either
  way.
- **NULL** → the named axis ships with its flip boundary: on
  direction-straddle or build-cost-conditional, the finding routes as "set
  the clock WITH the build-cost and dead-share numbers" plus the free live
  probe above (the lane's own launch/first-sale timestamps accumulate the
  histogram that collapses the axis — zero new tooling).

**Gates (run invalid on any failure).**

- **Hand fixture (pinned, verified at startup):**
  1. **F1 — prior normalization:** each of the three pmfs sums to 1 exactly.
  2. **F2 — point-mass identities (exact):** at point mass p = 0, G = 0
     exactly for every (T, B, H); at point mass p = 1 (fixture constant, not
     on the grid), every launch graduates on day 1 and G = ⌈H/(1+B)⌉ exactly
     — asserted at H = 90 for B = 2/5/10 (30, 15, 9).
  3. **F3 — truncated-geometric identity:** Σ_{x=1..T} p(1−p)^{x−1} =
     1 − (1−p)^T exactly for every grid p and clock T; per-launch graduation
     probability non-decreasing in T.
  4. **F4 — hand world:** H = 6, B = 1, T = 2, point prior p = 1/2 ⇒
     **G = 31/16 exactly** (hand-derived: G(1) = 1/2, G(2) = 3/4, G(3) = 1,
     G(4) = 11/8, G(5) = 13/8, G(6) = 31/16).
  5. **F5 — theorem gates (exact, both arms where applicable):** (a) G
     non-increasing in B for every (prior, T) — more downtime never helps;
     (b) the degenerate all-dead prior (point mass 0) ⇒ G = 0 and kills =
     renewal count exactly; (c) expected slot accounting — graduation-days +
     kill-days + build-days + live-at-horizon-days = H exactly in Arm A's
     bookkeeping identity.
- **Arm agreement gate** (bounds above), **per-leg draw-count sentinels**
  (daily-trial draws ≡ recorded live days), **twin independently-written
  decision evaluators**, **stdout + results.json byte-identical across two
  process runs**, **CPython minor pinned** — the P017–P049 standing battery.

**Reporting-only legs (Arm A exact re-evaluations + seed-20261339 Arm-S
confirmations at 20,000 trajectories — CANNOT flip the decision):** the full
9 × 3 G table with directions; expected kills / idle days / wasted
graduations per cell; the per-p conditional graduation split; H ∈ {60, 180};
the sensitivity grid P′; the graduation-blocks-slot world; the margin sweep
m ∈ {1/50, 1/10}. Aux seed 20261340 is reserved and never read by any
decision number.

**Grounding / hermeticity.** ZERO network reads at verdict time AND zero repo
reads — the entire world (the p grid, the three pmfs, the B and H constants,
the clock set, the renewal rule, the bands, the hand fixture) is constructed
in-sim from the pinned constants in this file, committed as a small fixture
JSON alongside one stdlib file; the harvested clock family and evidence line
(T+7 checkpoint 2026-07-19 · T+14 kill rule 2026-07-26 · 30-day signal
window · ≥1-organic-sale leg · "0 organic sales across 7 click-queued
products") are quoted in the fixture with their DOUBLE pin — venture-lab
`be6c75d` via idea-engine outbox `763b19e` — for citation only, secondhand
status stated in the fixture itself. Decision arithmetic exact
`fractions.Fraction`. Feasibility: Arm A ≈ 27 DP tables × ≤ 90 × 5 × 30
Fraction terms — seconds; Arm S ≈ 27 × 200,000 trajectories × ≤ ~90 draws ≈
5 × 10⁸ RNG calls worst case, bounded in practice by early
graduation/kill — minutes, pure CPython; the 20,000-trajectory legs are
noise on top. No dependencies.

## Relations (adjacent heads — deliberately links, not duplication)

- Nearest by WORLD: **P042 → V053** (channel concentration vs
  diversification) — the SAME products lane and the same harvested doc
  family, but the orthogonal fork: P042 allocates BUILD TOKENS ACROSS
  CHANNELS holding the kill semantics fixed (its model consumes "the 30-day
  signal window" as a given constant and names the T+7/T+14 clocks only as
  its NULL probe); this head prices the CLOCK ITSELF holding the channel
  fixed. Zero shared machinery: allocation cells over channel posteriors
  there, a renewal DP over censored first-sale times here. V053's APPROVE
  (reserve a build slot for an untested channel) composes with any ruling
  here — where to build and when to kill are separate dials.
- Nearest by MOVE (stop/keep thresholds elsewhere in the rotation): **P022 →
  V024 + P034 → V036** (trading KEEP margins / drift-gating) price
  SELECTION margins on noisy cross-sectional backtest statistics — no time
  axis, no censoring, no slot economics; **P030 → V032** (adaptive
  versioning) prices produce→observe→version on a noisy sales SIGNAL in the
  books catalog — observation feeds a production allocation, not a
  kill/recycle renewal; **P036 → V047** (secretary/37%) is optimal stopping
  over a RANK stream with no recycling (each candidate seen once, no
  downtime economics). This head's machinery — censored geometric first-sale
  times + slot renewal under build downtime — appears in none of them.
- The pricing SIM-REQUEST verdicts **V037/V039/V040/V041** set PRICE POINTS
  for specific venture listings; no clock, no kill rule, no renewal.
- **P049** (magnet press-fit band) is method kin only — pricing a shipped
  default against a pinned population, the same SHAPE this head applies to a
  time threshold — zero shared world or fixture.
- The tree-wide dedup sweep `rg -i -g '!bootstrap.py' -g '!.substrate'
  'kill.clock|kill.rule|T\+14|first.sale|renewal'` at drafting HEAD
  `763b19e` hits only P042's harvest quotes (the clock family as CONTEXT,
  never as the priced object), the V037–V041 pricing blocks, and ORDER
  005/006 relay text; the sim-lab sweep hits V053's inherited guard line.
  No prior proposal (P001–P049), verdict (V001–V060, headers + subject
  lines swept), idea file, or session-card 💡 prices a kill/stop clock or
  any censored-observation renewal threshold.
- Runners-up this slice, weighed and dropped on merit: **the ideation
  rubric's weight vector** (Distribution 35 / Buildability 20 / … — a real
  unpriced surface, but its honest sim needs the doc's actual 9 × 5 score
  table, unreadable this session; a fully synthetic score table would price
  the rubric's GEOMETRY, not the lane's rubric — re-openable the day a
  venture read is available); **the 180k-token cycle budget's cap-vs-actual
  inflation** (the webhook-kit 2.3×-over datapoint is a single actual — one
  point pins no distribution); **per-product PWYW-vs-fixed follow-ups**
  (V039/V041 already own that surface). The kill clock won on: three
  committed values of one dial already on the record secondhand, a crisp
  two-sided tradeoff, and a genuinely undecided landing at honest widths.

## Model basis (declared model-dependence — the P024 discipline)

This verdict's numbers are CONDITIONAL on an embedded model, named up front:

- **(1) Statistical assumptions:** sales are a stationary per-day Bernoulli
  process per product (no launch spike, no decay, no weekday structure);
  products i.i.d. from the cell prior; one experimental slot, slots
  independent; build downtime deterministic; the success leg is FIRST sale
  only (the ≥1-organic-sale leg — reads/inbound named out of scope by the
  harvest itself). Invented-and-pinned where the lane is silent: the p grid,
  the three prior pmfs, the token→slot-day conversion behind B, and H —
  each disclosed inline, the prior and B axes promoted INTO the decision
  grid rather than assumed; the grounded constants (the clock values 7/14/
  30, the success leg, the 0-for-7 evidence line) are the lane's own via
  the P042 harvest @ `be6c75d`. **The invented-widths boundary, stated
  plainly: there is no live first-sale-time datapoint anywhere in the fleet**
  (the lane's launched products have ZERO sales — that is the harvested
  evidence itself), so the p grid and priors bracket SCALE, not measured
  shape — and the cheapest live probe (the lane's own launch/first-sale
  timestamps, already recorded by its kill-clock machinery) measures the
  real mixture directly, product by product, at zero new tooling.
- **(2) Single most-likely-to-flip alternative:** the STATIONARITY
  assumption — real product launches typically front-load attention (a
  launch spike): sales evidence then concentrates in the first days, waiting
  past day ~7 buys little discrimination, and the optimal clock shortens.
  The stationary model is therefore GENEROUS TO LONG CLOCKS (direction
  stated — an APPROVE of T+14 against T+7 must be read net of it; a REJECT
  toward SHORTER would be reinforced by it). Softer flips, named as out of
  the registered scope: correlated product quality (the 0-for-7 indicting
  the lane's whole funnel rather than the draws — V053's world, priced
  there); non-sale signals (reads/inbound — out of scope by the harvest's
  own line); multi-sale value beyond the first (graduation is binary here).

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe
> over pinned fleet-internal constants, sim is report-only evidence, no
> spend/publish/irreversible surface — README § probe battery). Verify-first
> ran FIRST, live this slice: (a) **source verified at the honest pin** —
> venture-lab direct read attempted ONCE and denied (verbatim error in the
> Grounding header above; deny-wins, no retry); every constant instead
> quoted from P042's verbatim harvest @ `be6c75d` as committed in THIS
> repo's outbox at HEAD `763b19e`, and the SECONDHAND status is carried into
> the fixture and the application guard rather than laundered. (b) **dedup**
> — the tree-wide topic sweep (Relations above) at HEAD `763b19e` plus the
> sim-lab working copy; PROPOSALs 001–049 (headers + summary lines) and
> VERDICTs 001–060 (headers + subject lines) swept before drafting; the
> nearest-neighbor families (P042/V053 same-lane orthogonal fork, P022/P034/
> P030/P036 stop-threshold method kin, V037–V041 pricing points) argued
> distinct by world/machinery above. (c) **kill test NOT triggered** — no
> prior head prices a kill/stop clock or censored-renewal threshold. (d)
> **feasibility + liveness arithmetic checked** — runtime bounded in the
> preamble (seconds exact arm + minutes MC, stdlib only); the drafting-time
> DP was actually RUN and its landing DISCLOSED (APPROVE, thinly, with the
> near-edge cells and the straddle direction named — the P048/P049 norm).

**1. What is this really?** A pre-registered pricing of the products lane's
shipped T+14 zero-sale kill clock against the lane's own two other committed
clock values (T+7, T+30) as a censored-observation renewal problem: expected
proven products per 90 slot-days over a 9-cell prior × build-downtime grid,
primary metric the shipped clock's exact relative shortfall D with its
direction, exact-Fraction DP decision arm confirmed by seeded MC under an
agreement gate, judged against bands fixed before any code (REJECT first: a
consistent ≥ 5% loss in ≥ 7 of 9 cells; APPROVE: within 5% of best in ≥ 7 of
9 including the SKEPTIC row; NULL with five named axes), byte-identical
across two process runs.

**2. What is the possibility space?** (i) Don't run it — the round-9 venture
slot goes unserved and the clock stays an unpriced date. (ii) Serve the
products half from the rubric or budget surfaces — weighed and dropped in
Relations (the rubric needs the unreadable score table; the budget has one
datapoint). (iii) A prose answer ("14 days is obviously enough") — measures
nothing and the drafting DP already shows cells where it is NOT the argmax.
(iv) Wait for live first-sale data — the RIGHT data eventually (the free
probe), but the clock fires on 2026-07-26 and gates every product NOW. (v)
This head: hermetic, exact-arithmetic, pre-registered — the pipeline's
standing shape.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file + one fixture JSON yields: the exact
9 × 3 throughput surface for the lane's own three clocks with the flip
boundary located on both the belief and the build-cost axis, the per-p
conditional split naming exactly WHICH burners each clock forfeits, a
measured retirement (or vindication) of the "give it the full signal
window" instinct, and a reusable pattern — censored-observation renewal
under downtime — that transfers to any future fleet head with a
kill/keep-waiting dial (idle-game re-roll timers, review-queue staleness
cutoffs, probe-retry budgets).

**4. What breaks it? (assumptions made explicit)** (a) **Stationarity** —
the named most-likely flip; direction stated (the stationary model is
generous to LONG clocks; a launch-spike world shortens the optimal T). (b)
**The invented widths** — the p grid, priors, B conversion, H carry no
measurement (disclosed; the prior and B are grid axes, P′/H have reporting
legs; the lane's own timestamps are the named live measurement). (c) **The
secondhand pin** — the kill-rule text was not read directly this session
(the denial is quoted verbatim; the application guard makes the verdict
conditional on the pinned shape, so a mismatched real rule voids application
rather than misapplying). (d) **Binary graduation** — first sale only, no
multi-sale value; named out of scope. None of these is hidden; each is a
grid axis, a sensitivity leg, a named flip, a guard condition, or a stated
scope bound.

**5. What does it unlock?** The kill clock stops being decorative: either
T+14 gains a measured basis and the T+30 instinct retires with numbers
(APPROVE — the disclosed drafting landing), or the lane gets a paste-ready
structured choice onto machinery it ALREADY runs (REJECT — the T+7
checkpoint becomes the kill, or the window extends), or the binding axis is
named with the lane's own free timestamps as the pre-priced measurement
(NULL). The fleet gains its first kill/stop-threshold verdict pattern; the
venture slot's products half gains its second head (P042 priced where to
build; this prices when to stop); and V053's application guard gains a
sibling that shares its 0-sales conditioning.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external at verdict time — fully hermetic by construction (the P017–P049
precedent). The harvest grounding is one already-committed outbox read (the
secondhand pin, disclosed). Cheapest kill BEFORE simming: a prior fleet
verdict on kill/stop thresholds (none found — P001–P049 and V001–V060
swept), or a venture-side committed kill-rule text contradicting the pinned
shape (unreadable this session — the application guard carries exactly this
risk instead of hiding it). Cheapest confirm AFTER a NULL: the lane's own
launch/first-sale timestamps — zero new tooling, each observed product pins
one grid row.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab builds and runs the sim (the Q-0264 pipeline's verify seat — this
file is its intake spec); venture-lab's products lane consumes the verdict
as a clock keep/move/condition decision on its kill rule, routed by the
manager per Q-0260; this repo builds nothing. It displaces nothing in
flight (V060 closed P049's world; no verdict session holds a venture head)
and duplicates nothing (Relations dedup above; P042/V053 own the channel
fork, V037–V041 own the price points).

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib Python file (both arms + gates + twin evaluators), one fixture JSON
(every pinned constant in this file, copied verbatim: the p grid and P′,
the three pmfs, B and H sets, the clock set {7, 14, 30}, the renewal and
blocking-world rules, band constants (1/20, 7-of-9, the 2-of-3 SKEPTIC
conjunct, the direction-agreement conjunct), the F1–F5 fixtures with the
31/16 hand value, per-leg trajectory counts, seeds 20261337–340, the
harvested clock/evidence lines with their double pin `be6c75d` via
`763b19e` and the quoted denial), one REPORT.md with the 9 × 3 G table, the
D column with directions, the ruling, and the named-axis/probe line on NULL
— the standing INTAKE/VERDICT grammar, nothing else.

**Recommendation: sim-ready** — every constant pinned here, bands registered
REJECT-first before any code, seeds 20261337–340 above the verified
high-water 20261336, fully hermetic at verdict time, the drafting-time
landing computed and disclosed; the honest next step is the sim itself.
