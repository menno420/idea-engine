# Channel concentration vs diversification at fixed build budget — does deepening the one channel with 0 organic sales beat probing fresh ones, and which prior belief flips the answer?

> **State:** sim-ready
> **Class:** venture (pipeline rotation — the standing ORDER 003 VENTURE slot,
> round 7, NON-BOOKS half on the slot's own half-alternation (P038's block states
> it verbatim: "r4 books → r5 trading → r6 books due", so r7 = non-books due);
> round history: P018 books → V020 null, P022 trading → V024 null, P026 trading →
> V028 approve, P030 books → V032 reject, P034 trading → V036 reject, P038 books →
> V049 reject. Prior non-books rounds (P022/P026/P034) all served the half from the
> TRADING lane; this round deliberately serves it from venture-lab's PRODUCTS lane
> instead — ORDER 004 rule 3's literal phrase is "venture's book/product space",
> and the products lane shipped, the same day, exactly the self-critique this head
> prices. Decide-and-flag: both readings cited, the product reading taken.)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/venture-lab@be6c75d4e3379efc108f27d17f2c8ff5adb9a74f · fetched 2026-07-13T18:26:50Z
> (read via read-only clone this slice, HEAD re-verified by rev-parse at drafting.
> The sim itself is fully hermetic: zero repo/network reads at verdict time, every
> fixture constructed in-sim from the pinned constants in this file)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous
pipeline — "continue coming up with new ideas, that is your main purpose"), the
rotation established by ORDER 004 rule 3 ("fleet backlogs → venture's book/product
space → game mechanics → COMPLETELY UNRELATED domains") — round 7 opened at the
fleet-backlogs slot (PROPOSAL 041, merged #331), so this slice serves the VENTURE
slot next. The harvested item is the products lane's own batch-level kill-rule
self-critique: the 2026-07-13 ideation batch (`docs/products/ideas-2026-07-13.md`
@ `be6c75d`, nine concepts scored on the shipped rubric at fixed weights
Distribution 35 / Buildability 20 / Launch-effort 15 / Speed 15 / WTP 15) picks
three BUILDs and then concedes, in its own Kill-Rule-2 note, that *"all three ride
the same saturated agent-ops/dev-article funnel that has produced 0 organic sales
across 7 click-queued products so far — the batch does not diversify channel risk,
it deepens a channel whose first proof point (SWTK T+7 checkpoint, 2026-07-19) has
not yet arrived."* The critique names the decision — deepen the incumbent channel
vs diversify — states the evidence (0 organic sales, 7 products), and prices
NOTHING: no number says when the evidence is bad enough that the next batch should
stop deepening. That unpriced fork is exactly the sim-testable shape. This head
builds nothing in venture-lab and never edits its files (routing is the manager's
per Q-0260); it prices the fork and hands the lane a pre-registered ruling.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested decision, stated back.** The products lane launches developer kits
into one distribution channel — the agent-ops/dev-article → Gumroad funnel. Its
catalog at `be6c75d` (`docs/current-state.md` "Product catalog" + the batch's own
no-duplicates checklist): SWTK $29, the only LIVE product, *"has 0 organic sales
as of 2026-07-13"*; six more sit click-queued behind it (membership-kit $49 ·
template-packs $19 PWYW · field manual $39 · kill-rule kit $15 · false-green $15 ·
merge-wall cookbook $19 — the batch's "7 click-queued products"). The new batch
allocates its whole build budget to three more products in that same channel,
because the channel is where the lane's amortized template lives — the ORDER 008
thesis, quoted in concept #1's pitch: *"product N+1 is measurably cheaper."* So the
real trade is not "good channel vs bad channel"; it is **cheap exposures in a
channel with only bad evidence, versus expensive exposures in channels with no
evidence at all** — a budgeted explore/exploit fork under a prior. The falsifiable
core: **given the observed evidence (0 organic sales across the incumbent
channel's product-exposures), does CONCENTRATE (all builds in the incumbent, at
the batch's own token costs) beat SPLIT and EXPLORE-THEN-COMMIT (builds spread
into untested channels at a pinned cost premium) on the probability of at least
one organic sale by horizon end — and across which pre-registered prior-belief
cells does the winner flip?** No prior proposal or verdict prices channel-level
allocation of build budget (Relations below); the cost asymmetry keeps all three
rulings live (liveness below).

**The model (fixed, fully pinned — every constant a decision of this file, none
left to the implementer; probabilities exact rationals throughout).**

- **Channels.** One INCUMBENT channel plus K = 3 untested channels u1, u2, u3
  (K invented, pinned, disclosed — "untested channel" abstracts any distribution
  surface with zero exposure evidence; the lane's docs name only surfaces inside
  the incumbent funnel class, which is the point). Each channel c carries an
  unknown per-product-exposure organic-sale rate p_c on the pinned grid
  **P = {0, 1/50, 1/10, 1/4, 1/2}** (p_c = the probability that one product
  launched into c records ≥1 organic sale in its 30-day signal window — the
  window from the lane's own kill-rule fields, "≥1 sale … within 30 days").
  Channels are INDEPENDENT draws (the load-bearing assumption — see Model basis).
- **The prior grid (9 pre-registered cells = 3 optimism pmfs × 3 evidence
  counts).** The agent's beliefs and the generative world are the SAME cell
  (self-consistent Bayes; the sweep over cells is the sweep over "under what
  prior beliefs does the answer flip"). Optimism pmfs over P, pinned exactly:
  - **SKEPTIC** = (1/2, 1/4, 1/8, 1/16, 1/16) — most mass on dead/near-dead rates;
  - **NEUTRAL** = (1/5, 1/5, 1/5, 1/5, 1/5);
  - **HOPEFUL** = (1/10, 1/5, 3/10, 1/4, 3/20).
  Untested channels draw p from the cell's pmf. The incumbent draws p from the
  SAME pmf conditioned on the observed evidence **0 successes in n_inc
  exposures** (posterior ∝ π(p)·(1−p)^n_inc), with **n_inc ∈ {7, 3, 1}** the
  second grid axis: 7 = the critique's own count ("7 click-queued products"),
  1 = the honest floor (only SWTK is actually LIVE; six of the seven were never
  published — click-queued exposure is a generous reading of "the channel
  produced 0 sales"), 3 = pinned midpoint (invented, disclosed). Cell order,
  pinned: (SKEPTIC, NEUTRAL, HOPEFUL) × (n_inc = 7, 3, 1).
- **Fixed build budget, in tokens (the doc's own currency).** Per-cycle budget
  **T = 180k tokens** — the batch's own summed BUILD caps (≤70k + ≤60k + ≤50k,
  concepts #1–#3). Incumbent build cost **c_inc = 60k** (the batch's median
  cap — template-amortized, the ORDER 008 thesis made a number). Untested-channel
  build cost **c_new = 90k** (1.5 × c_inc: a fresh channel means a fresh surface,
  fresh listing conventions, no template — INVENTED, pinned, disclosed;
  sensitivity pair c_new ∈ {60k (equal-cost), 120k (2×)}, reporting-only). The
  known fleet datapoint that build ACTUALS run over caps (the stripe kit spent
  ~284k against its 120k cap, ~2.3×, per this repo's venture index mirror) is
  disclosed and does not move the model: uniform inflation cancels at a fixed
  budget — only DIFFERENTIAL inflation matters, which is exactly the c_new
  sensitivity axis. Unspent tokens within a cycle are LOST (no carryover —
  pinned, conservative, disclosed). Horizon **H = 4 cycles** (invented, pinned;
  sensitivity H ∈ {2, 8}, reporting-only). One cycle = build + observe: a
  build's outcome (its 30-day window) is known before the next cycle allocates
  (matches the lane's kill-clock cadence; disclosed as a model idealization).
- **The three policies (allocation fully pinned).**
  - **CONCENTRATE** — every cycle: ⌊T/c_inc⌋ = 3 incumbent builds. Total 12
    incumbent product-exposures over H = 4.
  - **SPLIT** — every cycle: ⌊T/c_new⌋ = 2 untested-channel builds, assigned
    round-robin in the pinned order u1, u2, u3, u1, u2, u3, u1, u2 → totals
    u1: 3, u2: 3, u3: 2 over H = 4. Zero incumbent builds (the polar
    alternative to the batch — deliberate; ETC is the middle).
  - **EXPLORE-THEN-COMMIT (ETC)** — cycle 1: build in u1 and u2 (2 × 90k =
    180k). Cycle 2: build in u3 (90k) + one incumbent build (60k); 30k lost.
    Then COMMIT by the pre-registered switch rule: compute each channel's
    posterior-mean rate from ALL evidence (incumbent: n_inc + 1 exposures —
    the prior evidence plus the observed cycle-2 build; u1/u2/u3: 1 exposure
    each), and spend cycles 3–4 wholly in the argmax channel — 3 builds/cycle
    if the incumbent (6 exposures), 2 builds/cycle if an untested channel
    (4 exposures). Ties broken by the pinned order incumbent → u1 → u2 → u3
    (status-quo-first, disclosed). No re-switching after commit.
- **Outcomes.** Each build in channel c is one Bernoulli(p_c) trial: success =
  that product records ≥1 organic sale in its window. **Primary metric,
  decision-bearing: P_any = P(at least one launched product succeeds by horizon
  end).** Secondary, reported, NEVER decision-bearing: **E_hits** = expected
  number of successful products. (The kill-rule signal's other leg — "≥50
  article reads" / "qualified inbound" — is out of the registered scope, named.)

**Two arms.**

- **Arm A (decision arm — exact, seedless):** everything lives on the 5-point
  rate grid, so every quantity is a finite exact sum of `fractions.Fraction`
  terms. CONCENTRATE: P_any = 1 − E_post[(1−p)^12], a 5-term sum against the
  incumbent posterior. SPLIT: 1 − E_post[(1−p)^0] · Π over u-channels of
  E_prior[(1−p)^{n_u}] with (n_u1, n_u2, n_u3) = (3, 3, 2). ETC: exact
  enumeration over the ≤ 5⁴ true-rate combinations × 2⁴ probe-outcome patterns
  (u1, u2, u3, incumbent cycle-1/2 builds), the committer applied to each
  pattern's exact posterior means, then the committed channel's exact
  no-success tail — ≤ 10⁴ terms per cell. The ruling rides Arm A alone.
- **Arm S (confirmation arm — seeded MC):** 200,000 trajectories per cell via
  `random.Random(20261305)`, cells in the pinned order, one stream; per
  trajectory, pinned draw order: p_inc from the incumbent posterior pmf →
  p_u1, p_u2, p_u3 from the cell pmf → CONCENTRATE's 12 outcome draws → SPLIT's
  8 (pinned allocation order) → ETC's probe 4 + committed draws. Common rate
  draws across the three policies (the comparison is variance-reduced; outcome
  draws are per-policy). **Agreement gate:** |ArmS − ArmA| ≤ 5/1000 absolute on
  every (cell, policy) P_any (pre-checked ≥ 4 SE headroom: SE ≤ 1/(2·√200000)
  ≈ 0.00112, 4·SE ≈ 0.0045) — any breach invalidates the run.

**Seeds (registered):** 20261305 (Arm S main confirmation leg) / 20261306
(stability leg, 20,000 trajectories per cell — the twin evaluators must
reproduce the Arm-A ruling on it under the widened gate ≤ 15/1000, pre-checked
≥ 4 SE at n = 20,000: 4·SE ≈ 0.0141) / 20261307 (reporting leg — the c_new, H,
and E_hits sensitivity confirmations, 20,000 each) / 20261308 (aux — NEVER read
by any decision number; reserved for the named NULL probe bookkeeping).
Allocated strictly above the PROPOSAL 041 high-water **20261304** — re-checked
at drafting: the tree-wide sweep `rg -g '!bootstrap.py' -g '!.substrate' -o
'202613[0-9][0-9]'` at HEAD `498a88e` maxes at 20261304 (P041's block and idea
file; control/status.md's "high-water 20261300" line is stale prose, not an
allocation), and — as P041's block established by sweeping V001–V051 — sim-lab
allocates no seeds of its own (verdicts consume pre-registered proposal seeds);
the parallel V052 session live at drafting consumes P041's 20261301–304 and
allocates none. Byte-identity: stdout + results.json byte-identical across two
process runs; CPython minor version pinned in the fixture.

**Pre-registered decision rule (fixed BEFORE any code exists; evaluated in this
order, REJECT FIRST; all band constants exact rationals).** Per cell, on Arm-A
exact numbers: CON = P_any(CONCENTRATE), DIV = max(P_any(SPLIT), P_any(ETC)).

- **REJECT** ("the diversification critique does not beat the incumbent at
  honest costs — concentration stands"): **DIV − CON < 1/100 in ≥ 7 of the 9
  cells.** Checked FIRST — the costly-error rationale: the expensive mistake is
  ordering the lane OFF its only live, template-amortized funnel on a modeling
  artifact; the protect-the-incumbent arm must not be shadowed by an eager
  APPROVE.
- **APPROVE** ("diversification robustly wins — the self-critique gets a
  quantitative backstop"): **DIV − CON ≥ 1/100 in ≥ 7 of the 9 cells, AND in
  ≥ 2 of the 3 n_inc = 1 cells** (the evidence-weakest row: only SWTK is
  actually live, so an APPROVE that dies when the generous 7-exposure reading
  is dropped is not robust). Mutually exclusive with REJECT by construction
  (7 + 7 > 9 and the margin conditions are complementary at 1/100); the
  seed-20261306 stability leg must reproduce the ruling.
- **NULL** (anything else — a legitimate, reportable outcome): the citable pin
  is the full 9-cell CON/DIV table and the named BINDING AXIS — pre-registered
  candidates: (i) **prior-straddle** — the winner flips across the optimism
  axis within a fixed n_inc row: the finding is the flip-boundary prior itself,
  the direct answer to "under what prior beliefs does the answer flip";
  (ii) **evidence-straddle** — the winner flips across the n_inc axis within a
  fixed optimism row: the finding is that the ruling hinges on whether
  click-queued-but-unpublished products count as channel evidence — an
  empirical question the lane's own kill clocks settle for free; (iii)
  **margin-thin** — a consistent direction that clears neither ≥ 7-cell band;
  (iv) **arm disagreement** — the agreement gate fails (a model/implementation
  defect is the finding, no ruling issues); (v) **sensitivity straddle** — a
  reporting-only leg (c_new ∈ {60k, 120k}, H ∈ {2, 8}) lands a band conjunct
  on the other side of its edge (the named axis is the finding; reporting legs
  CANNOT flip the decision). **Cheapest live probe, named:** the SWTK T+7
  funnel checkpoint (2026-07-19) and T+14 kill-rule (2026-07-26) — zero new
  work, already armed packet-side: they either break the 0-sale streak or move
  the incumbent's evidence past the modeled n_inc rows, collapsing the
  evidence axis before the band is re-litigated.

**Band liveness (disclosed — the P034–P041 discipline).** No closed form is on
record for the composed comparison, and the cost asymmetry keeps it genuinely
open: at c_new = 1.5×, SPLIT buys 8 exposures against CONCENTRATE's 12 — a
one-third exposure tax — so diversification wins a cell only where the
incumbent's 0/n_inc handicap plus the fresh-channel option value (four
independent rate draws instead of one) outweighs four lost exposures. Under
SKEPTIC × n_inc = 1 the handicap is small (one failure barely moves a pmf with
half its mass at rate 0) and the tax plausibly dominates — REJECT is live.
Under NEUTRAL/HOPEFUL × n_inc = 7 the handicap is large ((1−p)^7 crushes the
upper rates that carry almost all of P_any) and diversification plausibly wins
— APPROVE is live. Whether either side clears SEVEN of nine cells at a 1/100
margin, and whether the n_inc = 1 conjunct holds, is genuinely undecided —
straddle NULLs are live on both axes. This file deliberately pins NO expected
landing.

**What a reader DOES differently on the verdict** (all routing lane-side via
the manager per Q-0260 — this repo edits nothing in venture-lab). A
pre-registered APPLICATION GUARD rides every branch: the verdict conditions on
*"0 organic sales as of 2026-07-13"*; if the incumbent channel records an
organic sale before application (e.g. at the 2026-07-19 T+7 checkpoint), the
conditioning is stale and the lane applies nothing without a re-run on updated
evidence — the sim is hermetic and cannot know, so the guard is consumer-side.

- **APPROVE** → the batch-level Kill-Rule-2 self-critique gains its
  quantitative backstop: the next ideation batch reserves ≥ 1 of its BUILD
  slots for an untested channel (or its INTAKE must argue why the verdict's
  cells do not apply), and the critique's prose line cites the measured 9-cell
  table instead of gesturing at "channel risk".
- **REJECT** → concentration stands QUANTITATIVELY: the lane's committed next
  slice ("write full INTAKE.md … for concept #1, then #2" — both
  incumbent-channel) proceeds with the channel-risk worry priced, and the
  Kill-Rule-2 line hardens from a hedge into a citation — at the batch's own
  cost structure, deepening the channel is defensible, not merely cheap.
- **NULL** → the named axis ships with the flip boundary: on prior-straddle,
  the owner learns exactly which belief about untested channels is
  decision-bearing (a structured-choice ask, recommendation first, per the
  working agreement); on evidence-straddle, the already-armed T+7/T+14 clocks
  are the pre-priced probe that collapses the axis at zero new work.

**Gates (run invalid on any failure).**

- **Hand fixture (pinned, verified at startup):**
  1. **F1 — posterior:** SKEPTIC, n_inc = 1: posterior over P =
     (800, 392, 180, 75, 50)/1497 (unnormalized 1/2·1, 1/4·49/50, 1/8·9/10,
     1/16·3/4, 1/16·1/2 on the common denominator 1600).
  2. **F2 — fresh-channel tail:** NEUTRAL prior, one untested channel, 2
     exposures: P_none = 35829/50000, P_any = 14171/50000.
  3. **F3 — committer tie:** with all four posterior-mean inputs equal, the
     committer returns the incumbent (the pinned status-quo-first order).
  4. **F4 — SPLIT allocation:** H = 4 yields exposure counts (u1, u2, u3) =
     (3, 3, 2) under the pinned round-robin.
  5. **F5 — budget arithmetic:** ⌊180/60⌋ = 3, ⌊180/90⌋ = 2; ETC cycle 2
     spends 150k with 30k lost.
  6. **F6 — point-prior identity:** with the prior replaced by a point mass at
     p = 1/10, evidence conditioning changes nothing and
     P_any(CONCENTRATE) = 1 − (9/10)^12 exactly.
- **Degenerate-zero gate (exact):** prior replaced by a point mass at rate 0 →
  P_any = 0 and E_hits = 0 for every policy — exact zeros, not tolerances.
- **Horizon monotonicity (exact, both arms):** for every cell and policy,
  P_any(H = 2) ≤ P_any(H = 4) ≤ P_any(H = 8) — exposures are only added, so a
  violation is an implementation defect: hard gate across the H reporting runs.
- **Equal-cost direction check (reporting, expected-direction, flagged loudly
  on surprise):** under the c_new = 60k sensitivity with n_inc = 7, SPLIT ≥
  CONCENTRATE is expected in every cell (a fresh prior stochastically dominates
  the 0/7-conditioned posterior, and the exposure tax is zero); a surprise
  prints as a first-class anomaly line, never silently absorbed.
- **Arm agreement gate** (bounds above), **per-leg draw-count sentinels**,
  **twin independently-written decision evaluators**, **stdout + results.json
  byte-identical across two process runs**, **CPython minor pinned** — the
  P017–P041 standing battery.

**Reporting-only legs (Arm A exact where stated + seed-20261307 Arm-S
confirmations — CANNOT flip the decision):** the full 9-cell × 3-policy P_any
and E_hits tables; the SPLIT-vs-ETC decomposition (which diversifier carries
DIV per cell); the c_new ∈ {60k, 120k} and H ∈ {2, 8} sweeps; the per-cell
committed-channel distribution under ETC (how often the probe sends the budget
home to the incumbent). Aux seed 20261308 is reserved and never read by any
decision number.

**Grounding / hermeticity.** ZERO network reads at verdict time AND zero repo
reads — the entire world (the rate grid, the three pmfs, the n_inc axis, the
token costs and budget, the allocation orders, the switch rule, the bands, the
six-item hand fixture) is constructed in-sim from the pinned constants in this
file, committed as a small fixture JSON alongside one stdlib file; the
harvested doc lines (the Kill-Rule-2 note, the 0-organic-sales line, the three
BUILD caps, the T+7/T+14 dates) are quoted verbatim in the fixture with their
`be6c75d` pin for citation only. Decision arithmetic exact
`fractions.Fraction`. Feasibility: Arm A ≈ 9 cells × ≤ 10⁴ ETC terms ≈ 10⁵
Fraction operations — seconds; Arm S ≈ 9 × 200,000 trajectories × ≤ ~30 draws
≈ 5 × 10⁷ RNG calls — a minute-scale pure-CPython run. No dependencies.

## Relations (adjacent heads — deliberately links, not duplication)

- Nearest by CONSUMER: **V037/V039/V040/V041** (the ORDER 010 relay of sim-lab
  pricing verdicts into venture-lab's inbox) — those price individual
  product/pricing POINTS taking the channel state as given; none allocates the
  build budget ACROSS channels — zero shared fixture, metric, or decision.
  **P038 → V049 reject** (KU exclusivity fork, the books half) — distribution-
  shaped but a per-title enrollment fork on verified royalty constants, not
  build-budget allocation, and the other half of this slot.
- Nearest by MOVE: **P018 → V020 + P030 → V032** (book versioning
  breadth-vs-depth K-allocation) — fixed-budget allocation, but WITHIN one
  catalog and one channel; this head's axis is ACROSS sale channels with
  asymmetric evidence and asymmetric per-build cost — the two dimensions those
  verdicts hold constant.
- Nearest by METHOD: **P022 → V024 + P034 → V036** (trading selection-noise /
  drift) — selecting among options on noisy evidence, methodological kin only;
  different world, no shared fixture. **P037/P038/P041** — exact-Fraction
  decision arm + seeded confirmation with invented-but-pinned constants and
  sensitivity pairs: method precedent only.
- The tree-wide dedup sweep `rg -i -g '!bootstrap.py' -g '!.substrate'
  'channel.concentration|diversif|organic sale'` at drafting HEAD `498a88e`
  returns ZERO files; a companion sweep on the bare token 'channel' hits only
  Discord-channel senses in the superbot tree plus the venture
  sellables-brainstorm's per-candidate sell-channel LISTS — a capture list
  with no sim head, no decision rule, no error model. No prior proposal
  (P001–P041 re-read at HEAD), verdict (V001–V052 span — V052 in flight on a
  parallel session's claim, targeting P041's spool world, unrelated), idea
  file, or session-card 💡 prices channel-level allocation of build budget.
- Runners-up this slice, weighed and dropped on merit: **pricing the rubric's
  Distribution-35 weight itself** (the weight is a judgment call, not a rate —
  no falsifiable quantitative claim a hermetic sim can price); **GWTK's named
  learnable unknown** (GitHub delivery/redelivery semantics — product-internal
  verification work, not sim-shaped); **the PARK-fold decision (#4 into #3)**
  (an audience-subset argument the batch already settles qualitatively; no
  undecided quantitative core). The channel fork won on: the lane's own doc
  names the decision AND the evidence, the cost side is already quantified in
  the doc's own token caps, and the landing is genuinely undecided.

## Model basis (declared model-dependence — the P024 discipline)

This verdict's numbers are CONDITIONAL on an embedded model, named up front:

- **(1) Statistical assumptions:** one Bernoulli trial per launched product
  with a channel-constant rate on a 5-point grid; channels INDEPENDENT; the
  agent's beliefs equal the cell's generative prior (self-consistent Bayes —
  the cell grid, not a single prior, is the registered hedge against this
  being wrong); build outcomes observed before the next cycle (the 30-day
  window idealized to the build cadence). Invented-and-pinned where the docs
  are silent: c_new = 1.5 × c_inc (sensitivity 1×/2×), H = 4 (sensitivity
  2/8), K = 3, the n_inc = 3 midpoint row, and the three optimism pmfs — each
  disclosed inline; the grounded constants (T = 180k, c_inc = 60k, n_inc ∈
  {7, 1}, the 0-successes conditioning, the 30-day window, the T+7/T+14
  dates) are the batch's and ledger's own numbers @ `be6c75d`. Success is the
  ≥1-organic-sale leg only; the reads/inbound leg of the lane's kill-rule
  signal is out of the registered scope, named.
- **(2) Single most-likely-to-flip alternative:** CORRELATED channel quality —
  if the 0-sales evidence indicts the PRODUCTS or overall market appetite
  rather than the channel (one shared latent factor across channels), fresh
  channels inherit the same handicap and diversification's option value
  collapses; correlation therefore moves the answer toward REJECT, so the
  independence assumption is GENEROUS TO APPROVE (direction stated — an
  APPROVE must be read net of it, a REJECT is reinforced by it). Softer flips,
  named as out of the registered scope: channel-saturation dynamics (the
  doc's own word "saturated" implies a decaying incumbent rate — would favor
  diversification); cross-channel spillover (an article in one channel feeding
  another's funnel); multiple sales per product (E_hits undercounts, secondary
  only); and the click-queue subtlety that six of the seven incumbent
  "exposures" were never published — handled as the registered n_inc axis
  rather than left as a flip.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe over
> a pinned fleet-internal doc, sim is report-only evidence, no
> spend/publish/irreversible surface — README § probe battery). Verify-first
> ran FIRST, live this slice: (a) **source verified at HEAD** — venture-lab
> read via read-only clone, HEAD `be6c75d4e3379efc108f27d17f2c8ff5adb9a74f`
> rev-parse-confirmed at drafting; the Kill-Rule-2 note, the 0-organic-sales
> line, the three BUILD caps, the rubric weights, and the T+7/T+14 kill-clock
> dates all quoted verbatim above from `docs/products/ideas-2026-07-13.md` and
> `docs/current-state.md` at that pin. (b) **dedup** — the tree-wide topic
> sweep (Relations above) returns zero files; PROPOSALs 001–041 re-read at
> HEAD `498a88e` before drafting; the four nearest-neighbor families
> (V037/V039–V041 point-pricing, V049 books-half fork, P018/P030 K-allocation,
> P022/P034 selection-noise) argued distinct by consumer/move/method above.
> (c) **kill test NOT triggered** — no prior proposal, verdict, or 💡 touches
> channel-level budget allocation. (d) **feasibility + liveness arithmetic
> checked** — runtime bounded in the preamble (seconds + a minute-scale MC,
> stdlib only); liveness disclosed in its own subsection with NO expected
> landing pinned.

**1. What is this really?** A pre-registered pricing of the products lane's own
batch-level self-critique: CONCENTRATE vs SPLIT vs EXPLORE-THEN-COMMIT at the
batch's own fixed 180k-token cycle budget, over a 9-cell prior-belief grid
(3 optimism pmfs × 3 readings of the 0-sales evidence), primary metric
P(≥1 organic sale by horizon), exact-Fraction enumeration arm confirmed by a
seeded MC arm, judged against bands fixed before any code (REJECT first:
concentration stands; APPROVE: diversification wins ≥ 7/9 cells including the
evidence-weakest row; NULL with five named axes), byte-identical across two
process runs.

**2. What is the possibility space?** (i) Don't run it — the round-7 venture
slot goes unserved and the lane's channel-risk hedge stays a prose gesture next
to three INTAKEs that deepen the channel anyway. (ii) Serve the half from
trading again — legal but weaker: three of the slot's six rounds already drew
trading, and the products lane shipped, the same day, a named unpriced fork
with its own evidence attached. (iii) A prose answer ("obviously diversify —
zero sales!") — ignores the cost asymmetry the lane's own ORDER 008 thesis
quantifies, and measures nothing. (iv) Wait for the T+7/T+14 clocks — the
RIGHT data eventually, but the next batch's INTAKEs are the lane's committed
next slice NOW, and the verdict's evidence axis plus the application guard
already price exactly how those clocks change the answer. (v) This head:
hermetic, exact-arithmetic, pre-registered — the pipeline's standing shape.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file + one fixture JSON yields: the exact 9-cell
CON/DIV surface with the flip boundary located on both belief axes, a
quantified answer to whether the lane's one live funnel deserves its next
build batch, the ETC committed-channel distribution (how often a cheap probe
round sends the budget home), and a reusable pattern — budgeted
explore/exploit over a pre-registered prior grid with asymmetric per-arm cost
— that transfers to any future fleet head allocating scarce build effort
across surfaces with unequal evidence (the trading lane's config-family
selection, the books lane's series-vs-new-title fork).

**4. What breaks it? (assumptions made explicit)** (a) **Channel independence**
— the named most-likely flip; direction stated (generous to APPROVE).
(b) **The invented constants** — c_new, H, K, the pmfs, the n_inc midpoint
carry no measurement (disclosed; the c_new and H sensitivity pairs bracket
scale; the prior GRID is itself the hedge on the pmfs). (c) **Stationary
rates** — "saturated" hints at decay; out of registered scope, named.
(d) **The evidence reading** — whether click-queued products count as
exposures is genuinely contestable; promoted INTO the grid as the n_inc axis
rather than assumed away. None of these is hidden; each is a grid axis, a
sensitivity leg, a named flip, or a stated scope bound.

**5. What does it unlock?** The Kill-Rule-2 critique stops being decorative:
either it gains a measured backstop that reshapes the next batch's BUILD
selection (APPROVE), or it is retired as priced-and-cleared (REJECT), or its
binding belief is named for the owner as a one-line structured choice (NULL) —
all routed lane-side per Q-0260. The fleet gains its first channel-allocation
verdict pattern; the venture slot's non-books half gains its first
products-lane serving (flagged in the rotation statement); and the T+7/T+14
clocks gain a pre-registered consumer for whichever way they land.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external at verdict time — fully hermetic by construction (the P017–P041
precedent). The harvest grounding is one pinned fleet-repo read, already taken
and quoted. Cheapest kill BEFORE simming: a prior fleet verdict on channel
allocation (none found — P001–P041 and the V001–V052 span swept at HEAD), or
an incumbent organic sale before drafting (none — the doc's own 2026-07-13
line). Cheapest confirm AFTER a NULL: the already-armed kill clocks
(2026-07-19 / 2026-07-26), zero new tooling — they move n_inc or break the
0-sale conditioning, and the application guard already says what that does to
the verdict.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab builds and runs the sim (the Q-0264 pipeline's verify seat — this file
is its intake spec); venture-lab's products lane consumes the verdict as a
batch-selection rule change, an INTAKE argument bar, or a hardened prose line,
whichever branch lands — routed by the manager per Q-0260; this repo builds
nothing. It displaces nothing in flight (V052 runs in parallel on P041's
spool world — disjoint fixtures, disjoint consumers) and duplicates nothing
(Relations dedup above; the sellables-brainstorm's channel LISTS are capture
prose, not a decision head).

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib Python file (both arms + gates + twin evaluators), one fixture JSON
(every pinned constant in this file, copied verbatim: the rate grid, the three
pmfs, the n_inc axis, T/c_inc/c_new/H/K, the allocation orders, the switch
rule, band constants (1/100, 7-of-9, the 2-of-3 conjunct), the six-item hand
fixture, per-leg trajectory counts, seeds 20261305–308, the harvested doc
lines quoted @ `be6c75d`), one REPORT.md with the 9-cell table, the
SPLIT-vs-ETC decomposition, the ruling, and the named-axis/probe line on NULL
— the standing INTAKE/VERDICT grammar, nothing else.

**Recommendation: sim-ready** — every constant pinned here, bands registered
REJECT-first before any code, seeds 20261305–308 above the verified high-water
20261304, fully hermetic at verdict time; the honest next step is the sim
itself.
