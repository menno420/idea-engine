# Kill-clock anchor vs owner-gated funnel onset — does the committed listing-live T+14 window measure product viability, or owner click latency?

> **State:** sim-ready
> **Class:** venture (pipeline rotation — the standing ORDER 003 VENTURE slot,
> round 13, PRODUCTS half on the slot's own half-alternation read from the
> actual sequence: P018 books (r1) → P022/P026 trading (r2/r3) → P030 books
> (r4) → P034 trading (r5) → P038 books (r6) → P042 products (r7) → P046 books
> (r8) → P050 products (r9) → P054 books (r10) → P058 products (r11) → P062
> books (r12), so r13 = products due; round 13 opened at fleet backlogs with
> P065 (#428), so the venture slot is next per ORDER 004 rule 3.)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/venture-lab@520bdfca71ca4f119808d1098cd4ecf7fc6e6732 · fetched 2026-07-15T05:31Z
> (FIRSTHAND pin, public shallow clone read this session — the P058/P062
> precedent; every venture-lab sentence quoted below was read directly at this
> pin. The sim itself is fully hermetic: zero repo/network reads at verdict
> time, every fixture constructed in-sim from the pinned constants in this
> file.)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous
pipeline) and ORDER 004 rule 3's rotation ("fleet backlogs → venture's
book/product space → game mechanics → COMPLETELY UNRELATED domains") — round
13 opened at the fleet-backlogs slot (PROPOSAL 065, PR #428), so this slice
serves the VENTURE slot, products half. The harvested item is the products
lane's committed kill-rule **measurement plan** — the one document,
`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md` @ `520bdfc`, that commits
BOTH horns of an unpriced incoherence:

- **The anchor (verbatim):** "**T+14 (deadline)** = **2026-07-26** — **signal
  = ≥1 organic sale OR ≥1 qualified inbound within 14 days of the listing
  going live.** No signal by T+14 → ledger ⚑E a **NEGATIVE** and **pause /
  delist** the product." The clock starts at **listing-live**.
- **The evidence channel (verbatim, same document):** "BASE CASE is **0
  sales** until a distribution channel is wired (the free gotcha article →
  gist → StackOverflow answer → listing → r/stripe funnel is still
  owner-gated), so payback is INDEFINITE absent traffic."

Sales evidence flows only through a funnel that goes live on a SEPARATE,
un-synchronized owner click — yet the window that judges the product is
anchored on the listing click. The lane's one lived launch happened to wire
its funnel same-day (listing verified live 2026-07-12T16:25:16Z, the dev.to
funnel-top article live 2026-07-12T17:18:47Z — onset τ = 0 days, both
timestamps committed in the same log), but the queue behind it holds **10
publish-READY products** whose publish clicks are batched for "one sitting"
(`docs/publishing/OWNER-QUEUE.md` family) while their funnels remain
owner-gated at unspecified later dates. The committed channel shortlist
(`docs/launch/distribution-channels.md` @ `520bdfc`) even commits the traffic
SHAPES: "Show HN … Spiky: 0 to a few hundred visits … One shot", "Dev.to …
Long-tail SEO, low … Slow-burn", "In-repo README buy badge … Near-zero
traffic, but free". Nobody has priced what the anchor choice DOES to the kill
rule's error arithmetic. P050 → V061 priced the DIAL (T ∈ {7, 14, 30}) on a
stationary intrinsic-demand model with no exposure channel at all — and its
own break-note names "stationarity" as its most-likely flip, direction
stated, unpriced. This head holds the dial FIXED at the committed 14 and
prices the ANCHOR. It builds nothing in venture-lab and never edits its files
(routing is the manager's per Q-0260); it prices the anchor and hands the
lane a pre-registered ruling whose repair needs ZERO new constants — the
lane's own committed **30-day signal window** is exactly the cap that makes
the funnel-anchored fix bounded.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested rule, stated back.** A product launches when the owner clicks
publish (calendar day 0). Its kill window is calendar days 1–14: at least one
organic sale inside the window or the product is ledgered NEGATIVE and
delisted. Sales require visits; visits require a funnel; the funnel goes live
τ days after listing-live, where τ is owner click latency — a quantity with
NOTHING to do with product viability. The committed rule therefore evaluates
the composite (product, τ), and the falsifiable core: **on a pinned
exposure-conversion model at the lane's own committed constants (14-day
window, ≥1-sale threshold, 30-day signal window) and committed channel
shapes, how much of the kill verdict is click latency — exactly — and does
anchoring the window at funnel-live, capped at the committed 30-day signal
window, restore timing-invariance at bounded slot cost?** Two-sided: if
truncation loss at plausible onsets is immaterial, the calendar anchor is
VINDICATED with numbers (the APPROVE branch is genuinely live — the drafting
grid contains cells where it fires).

**The model (fixed, fully pinned — every constant a decision of this file,
none left to the implementer; probabilities exact rationals throughout).**

- **Time.** Whole calendar days, listing-live = day 0, the committed kill
  window = calendar days 1..14 (T = 14 FIXED — the dial is P050's served
  territory, never re-priced here). The committed **30-day signal window**
  enters only as the cap constant of anchor A-CAP30.
- **Funnel onset τ.** The funnel goes live τ whole days after listing-live;
  funnel-day d (d = 1, 2, …) is calendar day τ + d. Grid **τ ∈ {0, 3, 7, 10,
  13, 20}** — 0 = the lane's one lived launch (measured, committed
  timestamps: 16:25:16Z listing / 17:18:47Z article, same day); 20 = the
  committed base case ("0 sales until a distribution channel is wired") where
  the funnel misses the listing-anchored window entirely. τ is exogenous
  (owner click latency), never optimized.
- **Traffic shapes (pinned integer visit schedules, funnel-relative; the
  magnitudes are invented-but-pinned readings of the channel table's own
  committed adjectives, disclosed):**
  - **SPIKE** ("Spiky: 0 to a few hundred visits … One shot" — Show HN):
    v_d = 200 if d = 1 else 0.
  - **BURN** ("Long-tail SEO, low … Slow-burn" — the dev.to article, the
    lane's ONE actually-wired channel, hence the decision shape):
    v_d = floor(60/d) for d = 1..60, else 0 (total mass 261 visits over 60
    days; first-14 mass 192).
  - **DRIP** ("Near-zero traffic, but free" — the in-repo badge): v_d = 2
    for d = 1..365, else 0.
- **Conversion.** Each visit converts to a sale i.i.d. w.p. q; viable-product
  grid **q ∈ {1/30, 1/100, 1/300}**, decision cell **q = 1/100** (a ~1%
  landing-page conversion, conservative; invented-but-pinned, bracketed by
  the grid). A dead product is q = 0 (degeneracy row F5: the rule's
  SPECIFICITY is perfect by construction — dead products never sell and are
  always correctly killed; this head prices SENSITIVITY only).
- **Anchors (the priced policy family, 3):**
  - **A-LIST** (committed): evidence window = calendar days 1..14 → visible
    funnel-days d with τ + d ≤ 14.
  - **A-FUNNEL**: evidence window = funnel-days 1..14 (calendar τ+1..τ+14) —
    unbounded slot occupancy τ + 14.
  - **A-CAP30**: funnel-anchored but hard-capped at the committed 30-day
    signal window — funnel-days d with d ≤ 14 AND τ + d ≤ 30; slot occupancy
    min(τ + 14, 30).
- **Metrics (all exact integers/rationals).** Evidence mass **N(shape,
  anchor, τ)** = Σ visits inside the evidence window; **false-kill
  probability FK = (1 − q)^N** (zero sales among N i.i.d. Bernoulli(q)
  visits — exact rational bignum); the τ-profile FK(τ) per anchor; the
  doubling onset min{τ on grid : FK(τ) ≥ 2·FK(0)}; slot occupancy per
  anchor; the ≥1-sale threshold held at the committed value (the
  qualified-inbound leg is named out of scope, exactly as P050 scoped it).

**Three structure theorems (hand-provable, riding as gates F2).**

1. **ANCHOR INVARIANCE.** Under A-FUNNEL the evidence window is funnel-days
   1..14 for EVERY τ, so N — and therefore FK — is exactly τ-invariant at
   every shape and every q. (Proof: window membership is d ≤ 14,
   τ-independent.)
2. **SPIKE STEP.** Under A-LIST the spike's entire mass sits on funnel-day 1
   (calendar day τ + 1), so N = 200·1[τ ≤ 13]: FK is a STEP function —
   constant at (1−q)^200 through τ = 13, exactly 1 at τ ≥ 14. One-shot
   channels are all-or-nothing under the calendar anchor.
3. **CAP-30 EQUIVALENCE + BOUNDEDNESS.** A-CAP30 ≡ A-FUNNEL exactly for all
   τ ≤ 16 (since τ + 14 ≤ 30 ⇔ τ ≤ 16), so the repair inherits theorem 1's
   τ-invariance on the whole plausible-onset range while slot occupancy is
   bounded by 30 days (vs A-FUNNEL's unbounded τ + 14); truncation resumes
   only at τ > 16 (at τ = 20 the cap admits funnel-days 1..10: N = 174 at
   BURN, by pencil from the schedule). The lane ALREADY OWNS both constants
   of the repair — 14 and 30.

Plus **MONOTONE TRUNCATION** as a gate family: under A-LIST, N(τ) is
nonincreasing in τ, zero at τ ≥ 14; FK nondecreasing in τ, exactly 1 at
τ ≥ 14 for every shape and q — the committed base case is a CERTAIN false
kill of every viable product whose funnel misses the window.

**Decision rule (pre-registered, evaluated in this order; decision cell =
BURN, A-LIST, q = 1/100 unless stated; all quantities seedless exact
rationals).**

- **REJECT** ("the committed listing-live anchor makes the T+14 verdict a
  measurement of owner click latency, not product viability — and the repair
  is free: the lane's own 30-day signal window is exactly the cap that makes
  the funnel-live anchor bounded"): **R1** FK(τ=13) ≥ 1/2 AND FK(τ=0) ≤ 1/5
  (the SAME viable product flips risk class on click timing alone); AND
  **R2** the doubling onset min{τ ∈ grid : FK(τ) ≥ 2·FK(0)} ≤ 13 (the
  doubling sits inside the window itself); AND **R3** A-CAP30 holds FK(τ) =
  FK(0) EXACTLY at every grid τ ≤ 16 with worst-case slot occupancy ≤ 30
  days (the theorem-gated conjunct, disclosed as such — falsifiability rides
  R1/R2). Checked FIRST because the costly direction is fleet-wide: every
  calendar-anchored evidence deadline whose evidence channel is gated on a
  separate un-synchronized click inherits FK(τ) — the 10 queued products'
  kill clocks, the T+7 checkpoint, KDP book launches vs marketing onset, any
  pre-registered probe window armed before its instrumentation is live.
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate
  failing (below).
- **APPROVE** ("the calendar anchor is immaterial at plausible onsets — the
  committed rule measures the product"): FK(τ=13) ≤ (6/5)·FK(τ=0) AND
  FK(τ=13) ≤ 1/4 — mutually exclusive with R1 by arithmetic (1/4 < 1/2, and
  FK(0) ≤ 1/5 makes (6/5)·FK(0) ≤ 6/25 < 1/2).
- **NULL** (anything else — pre-registered axes, each a finalized citable
  finding): band-straddle (FK(13) ∈ (1/4, 1/2), or the doubling onset lands
  off-grid-right — the finding is the exact FK table); shape-conditional
  (the promoted clause flips at SPIKE — drafting says SPIKE lands the
  APPROVE clauses exactly: the truncation tax is a slow-burn phenomenon,
  named, never ruling); q-conditional (both q edges land outside R1 —
  disclosed below); a theorem failure without gate failure (the drafter's
  window algebra is wrong — the corrected law is the finding); twin-arm
  disagreement surviving the INVALID diagnosis.

**Arms.** **Arm A** (DECISION arm, seedless): exact-Fraction schedule-sum
arithmetic over the full grid (3 shapes × 3 anchors × 6 τ × 3 q + degeneracy
rows), byte-identical across process runs. **Arm B** (twin, seedless,
INDEPENDENTLY-WRITTEN): a literal calendar day-walk simulator — walks
calendar days 1..60, deposits each day's visits per (shape, τ), tests window
membership per anchor as a date comparison, accumulates N, computes FK — and
must reproduce every Arm-A number EXACTLY. **Arm R** (seeded,
REPORTING-ONLY): the literal Bernoulli visit process at the decision cell,
anchors {A-LIST, A-CAP30} × τ ∈ {0, 13}: 100,000 episodes on
random.Random(20261580) (draw order: one uniform per visit in schedule
order, counts counted and asserted), stability leg random.Random(20261581)
at 20,000, presentation shuffle 20261582, aux 20261583 NEVER read. No
statistical gate rides Arm R — a trace drift from the exact FK values is a
named finding, never a ruling.

**Gates (INVALID if any fails).**

- **F1 model identities:** FK = (1−q)^N with N recomputed by both arms;
  conservation per cell (in-window + pre-window + post-window visits =
  shape total mass, exact); monotonicity (FK nonincreasing in q and in N);
  anchor coincidence at τ = 0 (all three anchors agree exactly, every cell).
- **F2 the three structure theorems + monotone truncation** (statements
  above, checked on the exact arithmetic across the FULL grid, not just the
  decision cell).
- **F3 closed-form anchors:** the BURN pencil row N(τ) = (192, 179, 155,
  125, 60, 0) across the τ grid under A-LIST (from the cumulative schedule
  60, 90, 110, 125, 137, 147, 155, 162, 168, 174, 179, 184, 188, 192);
  BURN total mass 261; DRIP N = 2·(14 − τ)⁺ under A-LIST; (99/100)^5 =
  9509900499/10000000000 exact; the CAP30 τ = 20 BURN cell N = 174.
- **F4 hand world:** shape (3, 2, 1), window 3 days, q = 1/2, τ = 1: A-LIST
  admits funnel-days 1..2 → N = 5, FK = 1/32 by pencil; the funnel anchor
  admits days 1..3 → N = 6, FK = 1/64.
- **F5 degeneracies:** q = 0 → FK = 1 everywhere (the dead-product row —
  perfect specificity, disclosed boundary); q = 1 → FK = 1[N = 0] (the
  anchor certainty edge); the τ = 20 A-LIST row = 1 exactly at every shape
  and q (the committed base case as arithmetic).
- **F6 battery:** Arm B exact-equal on every number; twin
  independently-written decision evaluators agree on the token; Arm-R
  draw-count sentinels counted and asserted; aux seed 20261583 never read
  (constructor registry); stdout + results.json byte-identical across two
  process runs; CPython minor pinned.

**GATE POWER, computed at registration for a correct implementation (the
V065/V067 lesson, applied):** the sim is FULLY DETERMINISTIC — every decision
clause and every F-gate is an exact-rational identity, structural assertion,
or byte comparison; the only seeded arm is reporting-only with NO statistical
gate (its sole gates are the draw-count sentinel and exact reproducibility,
pass probability 1 for a correct implementation). JOINT pass probability
across all gates for a correct implementation = 1 EXACTLY (the P059–P065
no-stochastic-gate precedent: determinism proven by byte-identical re-run,
not estimated). Decision separation is noise-free exact arithmetic — R1
clears its 1/2 line at 1.094× (thin, disclosed: it is exact, not noisy; a
different pinned BURN magnitude could land it elsewhere, which is exactly
what makes the clause falsifiable rather than certain) and its 1/5 line at
1.377× under; R2 lands exactly at grid τ = 13 with τ = 10 at 1.9608× — ONE
GRID STEP below the doubling line, the knife-edge disclosed; the ruling
cannot move except via a mis-implemented model, which the anchor gates catch
as INVALID.

**Expected landing DISCLOSED per the P048–P065 closed-form-arm norm (drafting
prototype ran this session; the sim re-derives from scratch and must not
trust these):** REJECT on all three conjuncts — decision cell FK(τ) =
(0.145197, 0.165463, 0.210598, 0.284708, 0.547157, 1.0) across the τ grid
(exact rationals (99/100)^N at N = 192, 179, 155, 125, 60, 0); R1: 0.547157
≥ 1/2 (1.094×) and 0.145197 ≤ 1/5 (1.377× under); R2: doubling onset τ = 13
(ratio 3.768× there; τ = 10 at 1.9608×, one step below); R3: A-CAP30
constant at 0.145197 for every τ ≤ 16, occupancy ≤ 30 (at τ = 20 the cap
admits N = 174 → FK ≈ 0.173990 vs A-LIST's exact 1). Falsifiability real on
every clause — **SPIKE at the same cell lands the APPROVE clauses exactly**
(FK constant 0.133980 through τ = 13: the truncation tax is a slow-burn
phenomenon and the decision-shape choice is load-bearing, justified by the
lane's one wired channel BEING the slow-burn article); **both q edges land
outside R1** (q = 1/30: FK(13) = 0.130799 < 1/2 — high-conversion products
survive truncation in absolute class, though the ratio is 87.8×; q = 1/300:
FK(0) = 0.526729 > 1/5 — the window fails even at τ = 0, P050's dial
territory, not an anchor problem); DRIP lands FK(0) = 0.754719 (the
"near-zero but free" channel cannot feed a 14-day ≥1-sale rule at 1%
regardless of anchor — the reporting row that gives the LAUNCH-LOG's "BASE
CASE 0 sales" reading its number). Disclosed sharpening, reporting-only: the
lived SWTK launch sits at the τ = 0 column by measured timestamps — the
committed rule has never yet been exercised at the τ values where it
misbehaves, which is exactly why pricing it BEFORE the 10-product queue
clears is the cheap moment.

**Consequence, pre-registered** (routing the manager's per Q-0260 — this repo
never edits venture-lab files, nothing here builds, publishes, or spends;
APPLICATION GUARD, two conditions: (1) the verdict conditions on the
committed rule text — the T+14 ≥1-organic-sale-from-listing-live deadline and
the 30-day signal window as committed @ 520bdfc; an amended kill-rule grammar
means re-run, not reuse; (2) it conditions on the funnel being a SEPARATE
owner-gated click — a lane that wires the funnel in the same sitting as the
publish click sits at the τ = 0 column by construction, where all three
anchors coincide exactly):

- **REJECT** → paste-ready structured choice, recommendation first per
  Q-0263.2 — **(a, recommended: zero new constants)** re-anchor the kill
  window at FUNNEL-LIVE with the committed 30-day listing-live cap (A-CAP30):
  one line in the vetting-packet §7 kill-rule grammar / LAUNCH-LOG template
  ("T+14 counted from funnel-live, never past listing-live + 30"), τ-invariant
  evidence for every onset ≤ 16 days, occupancy bounded by the constant the
  lane already ships; **(b)** keep the listing-live anchor but SYNCHRONIZE
  the clicks — put each product's funnel-wiring click in the same owner-queue
  sequence as its publish click (the queue already batches one sitting; the
  repair is queue composition, zero rule changes, and V073's served
  attention-order machinery composes); **(c)** treat a zero-evidence window
  (no funnel wired by T+14) as VOID (re-arm once) rather than NEGATIVE — a
  rule-grammar change whose measured basis is the τ = 20 row's exact FK = 1.
  An owner/lane intent call, never ruled by fiat here.
- **APPROVE** → the calendar anchor gains a measured basis at plausible
  onsets and the FK table ships as the T+7 checkpoint's reading aid.
- **NULL** → the named axis ships with the exact FK table plus the free
  probe (the N/FK function re-runs on any future channel schedule at zero
  marginal cost).

**Boundaries (stated in the verdict):** the exposure-conversion boundary
(demand = visits × per-visit i.i.d. conversion; correlated visit bursts and
word-of-mouth compounding are named unmodeled channels, direction stated:
positive correlation fattens the zero-sale tail and moves every FK
REJECT-ward); the magnitude boundary (shape totals are pinned readings of
committed ADJECTIVES — the structure theorems and the τ = 20 certainty row
are magnitude-free, the R1/R2 magnitudes are not, which the grids bracket);
the threshold boundary (the ≥1-sale leg only; the qualified-inbound leg is
out of scope, P050's own scoping inherited); the dial boundary (T = 14 held
fixed — the dial is V061's served territory; this head prices the ANCHOR at
the committed dial value); the single-product boundary (per-product
arithmetic; the 10-product queue row is a reporting multiplication, no
cross-product interaction modeled — deliberately NOT the dropped
release-cadence head, see Relations). Honest-null explicit: every NULL axis
is a finalized, citable finding with its exact numbers, never a re-run
request.

## Relations (adjacent heads — deliberately links, not duplication)

- Nearest by WORLD: **P050 → V061** (kill-clock horizon) — the SAME kill-rule
  family, the orthogonal fork, and this head's REOPEN provenance: P050
  priced the DIAL (T ∈ {7, 14, 30}) on a stationary model where each live
  day is an intrinsic Bernoulli(p) sale trial — NO exposure channel, no
  funnel, no onset; its break-note (a) names "stationarity" as the named
  most-likely flip ("the stationary model is generous to LONG clocks; a
  launch-spike world shortens the optimal T") and prices it nowhere. This
  head serves that named flip axis with a DIFFERENT decision object: the
  anchor policy at the committed T = 14, under the committed non-stationary
  funnel. Zero shared machinery (censored renewal DP there; truncated
  Bernoulli exposure mass here). Also the pin class differs: P050's venture
  constants were SECONDHAND (its direct read was denied that session,
  verbatim error recorded in its Grounding) — the LAUNCH-LOG measurement
  plan whose two committed sentences form this head was structurally
  invisible to P050's drafter; it is read FIRSTHAND here @ 520bdfc.
- **P042 → V053** (channel concentration) — allocates BUILD TOKENS across
  channels, consumes the signal window as a given constant; no window
  arithmetic. **P062 → V073** (owner-queue attention order) — completion-time
  scheduling of the owner's clicks with zero demand-side machinery;
  consequence branch (b) composes with its served verdict rather than
  re-pricing it. **P058 → V069** (rubric weight robustness) — the instrument-
  audit KIN by move (audit a committed instrument's arithmetic layer),
  different instrument, zero shared fixtures.
- **P053 → V064** (healthcheck blind windows) — detection latency of a
  MONITOR with scheduled gaps; here the window is an evidence DEADLINE and
  the priced object is a decision rule's error under exposure truncation —
  no detection process, no renewal machinery.
- **The dropped release-cadence head — NOT revived** (disclosed): P054's
  Relations weighed and dropped "dump vs drip against the committed
  3-titles/day cap" for its fully-invented VISIBILITY model, and P062's
  runners-up declined to revive it. This head is not that head: no
  visibility pool, no cross-product attention split, no cadence choice —
  single-product window arithmetic whose centerpiece theorems
  (anchor invariance, spike step, cap-30 equivalence, the τ ≥ 14 certainty
  row) are magnitude-free exact statements that hold under ANY shape
  magnitudes; only R1/R2's absolute levels ride the pinned magnitudes, and
  those are grid-bracketed readings of the channel table's own committed
  adjectives, not an invented interaction mechanism.
- The ORDER 005/006 queued pricing SIM-REQUESTs (Ultramarine serial,
  photo-pack PWYW, Ship-It $59 anchors, narrow-TAM $19-vs-PWYW) price PRICE
  POINTS of specific SKUs — no window, no anchor, no error arithmetic; and
  `webhook-test-kit-family-2026-07-11.md` records that price elasticity was
  already routed to sim-lab by the venture lane itself, the reason this head
  (like P030's) deliberately avoids the pricing shape entirely.
- Method kin: the P059–P065 fully-deterministic no-stochastic-gate shape
  (exact decision arm + independently-written twin + reporting-only seeded
  traces); the evidence-window/calendar-window decomposition and the
  anchor-policy family are this head's own additions to the battery. No
  proposal P001–P065 and no verdict V001–V077 (ledger read FIRSTHAND at
  sim-lab origin/main 71337e2: finalized through V077 on P064's world;
  V078 in flight on P065's world per the coordinator relay) prices a
  measurement-window ANCHOR, exposure truncation, or click-latency
  confounding — the pipeline's first evidence-anchoring head.

## Model basis (declared model-dependence — the P024 discipline)

The exposure-conversion factorization (sales = visits × i.i.d. per-visit
conversion) is the model claim everything decision-bearing rides on; it is
the standard funnel reading of the lane's OWN committed measurement plan
("dev.to article views → Gumroad listing visits → sales" — the funnel line
is verbatim in the LAUNCH-LOG's measurement section). The three theorems are
model-free window algebra (they hold for any visit schedule); the FK levels
are model-conditional and say so. The shape magnitudes (200 / floor(60/d) /
2-per-day) are invented-but-pinned quantifications of committed adjectives —
disclosed in the Origin, bracketed by the q and shape grids, and the named
live measurement is free: the lane's own Gumroad/dev.to dashboards will
eventually hand the owner real visit schedules, at which point the FK
function (committed with the verdict) re-runs on measured schedules at zero
marginal cost.

## Probe report (v0, 2026-07-15)

**1. What is this really?** A pre-registered audit of a committed decision
rule's ANCHOR: the products lane's T+14 kill clock starts at listing-live
while its evidence channel starts at an unrelated owner click, and the audit
prices exactly how much of the kill verdict is click latency — with the
repair already sitting in the lane's own constant set (anchor at funnel-live,
cap at the committed 30-day signal window).

**2. What is the possibility space?** (i) Don't run it — the 10-product
queue clears at some point, funnels wire late (the committed base case says
they do), and the lane ledgers NEGATIVE verdicts that measured click
latency; the error is silent because a zero-sale T+14 looks identical under
both explanations. (ii) Wait for live data — the RIGHT data eventually (the
free probe above), but the clocks arm at publish time and the queue is
batched for one sitting NOW. (iii) A prose answer ("obviously wire the
funnel first") — measures nothing, prices neither the doubling onset nor
the repair's boundedness, and the SPIKE column shows the intuition is
shape-conditional, not universal. (iv) This head: hermetic,
exact-arithmetic, pre-registered — the pipeline's standing shape.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file + one fixture JSON yields: the full exact
FK(shape × anchor × τ × q) surface, three hand-provable window theorems as
gates, the doubling-onset row, the repair's exact equivalence-and-bound
statement, and a transferable pattern — CALENDAR-ANCHORED DEADLINE +
CLICK-GATED EVIDENCE = LATENCY MEASUREMENT — that audits every fleet surface
with a window armed before its instrumentation is live (probe windows,
checkpoint reviews, deadman expiries with gated activity channels).

**4. What breaks it? (assumptions made explicit)** (a) The exposure
factorization — correlated bursts unmodeled; direction stated
(REJECT-ward). (b) The invented magnitudes — R1/R2 levels ride them
(disclosed; theorems and the certainty row do not; grids bracket; live
schedules are the named free measurement). (c) Exogenous τ — if the owner
systematically wires funnels only for products he privately believes in, τ
correlates with viability and the confound gains a selection layer (named,
out of scope, direction unstated by design). (d) Binary ≥1-sale threshold —
the committed value; richer evidence (views, inbounds) is the named
follow-up. None is hidden; each is a boundary, a grid axis, or a named
follow-up.

**5. What does it unlock?** The kill rule's verdicts become attributable:
either the anchor is repaired for free (REJECT branch — one grammar line,
zero new constants) or the calendar anchor gains a measured defense
(APPROVE), and either way the 10 queued launches inherit a rule that
measures products. The fleet gains its first evidence-anchoring verdict
pattern; the venture products half gains its fourth head (P042 where to
build, P050 when to stop, P058 whether the scorer is robust — this one:
whether the stopwatch starts at the right event).

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external at verdict time (fully hermetic; every fixture in this file). The
cheapest kill at drafting was reading the LAUNCH-LOG's measurement plan
firsthand — if the committed rule had anchored at funnel-live already, this
head dies in one sentence; it does not (the anchor sentence is quoted
verbatim above). The cheapest confirm after the verdict: the lane's own
dashboards hand over one real visit schedule and the committed FK function
re-runs on it.

**7. Which lane should build it — and what does it displace or interact
with?** sim-lab builds the verdict (the standing pipeline); venture-lab is
the CONSUMER via the manager's routing (Q-0260). It displaces nothing — the
dial verdict (V061), the allocation verdict (V053), and the attention-order
verdict (V073) all compose with any ruling here (different objects on the
same machinery).

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib sim file (Arm A exact schedule sums + Arm B independently-written
calendar day-walk + Arm R reporting traces), one fixtures.json (every
constant in this file copied verbatim), results.json + stdout byte-stable
across two runs, the pre-registered rule applied in the registered order.
Feasibility: the full grid is 3 × 3 × 6 × 3 ≈ 162 cells of bignum
exponentiation plus a 100,000-episode reporting trace — seconds to a minute,
pure CPython, no dependencies.
