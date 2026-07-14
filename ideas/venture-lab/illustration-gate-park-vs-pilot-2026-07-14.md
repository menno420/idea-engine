# The illustration gate — is "park the kids titles" right-priced against the plan's own two committed spend options?

> **State:** sim-ready
> **Class:** venture (pipeline rotation — the standing ORDER 003 VENTURE slot,
> round 10, BOOKS half on the slot's own half-alternation read from the actual
> sequence: P018 books (r1) → P022/P026 trading (r2/r3) → P030 books (r4) →
> P034 trading (r5) → P038 books (r6) → P042 products (r7) → P046 books (r8) →
> P050 products (r9), so r10 = books due; round 10 opened at fleet backlogs
> with P053 (#379), so the venture slot is next per ORDER 004 rule 3.)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/venture-lab/blob/d93aee502a4daf2b3f7cd249067eb5c5a5ac046c/docs/publishing/PUBLISHING-PLAN.md@d93aee502a4daf2b3f7cd249067eb5c5a5ac046c · fetched 2026-07-14T01:47:58Z
> (FIRSTHAND pin, a first for the venture slot since P046: `add_repo` for
> venture-lab SUCCEEDED this session — the P050 denial did not recur — and the
> constants below are read directly from a read-only shallow clone at the HEAD
> above, `git log -1` verified `d93aee5… 2026-07-14T01:16:13+00:00`. Companion
> file read at the same pin: `docs/publishing/OWNER-QUEUE.md` (the three live
> hard-gated kids sequences). The sim itself is fully hermetic: zero
> repo/network reads at verdict time, every fixture constructed in-sim from
> the pinned constants in this file.)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous
pipeline) and ORDER 004 rule 3's rotation ("fleet backlogs → venture's
book/product space → game mechanics → COMPLETELY UNRELATED domains") — round
10 opened at the fleet-backlogs slot (PROPOSAL 053, PR #379), so this slice
serves the VENTURE slot, books half. The harvested item is the publishing
plan's §3 kids-book **illustration money-decision**: the catalog's kids
picture books "cannot publish without interior art", and §3 commits exactly
three options — **(A) Commission art** ("~$100–$400 per spread"; "Reedsy's
market average is **$1,540–$4,950** for a 24pp book; a budget freelancer can
land under $1,500 with quality/consistency risk"), **(B) AI-generated art**
("Tool cost is near-zero (~$0–$30/mo). KDP permits AI-generated cover and
interior art but requires you to DISCLOSE it at publish time"; caveats:
"undisclosed or low-quality AI content risks title removal / account action"
and "the copyright status of purely AI-generated images is legally unsettled")
— and **(C) Park** ("Defer all kids titles until Tier-1 revenue (or the
Stripe Kit line) funds commissioned art"). The seat's committed
recommendation, verbatim: *"**Park the kids titles (C) and publish Tier 1
first.** Kids books carry the full illustration cost up front against the
same unknown-author zero base case — spending four figures on art before any
title has sold is the wrong order. If the owner wants to test the kids line
cheaply, pilot **AI art on ONE title (with disclosure)** rather than
commissioning the whole series."* That recommendation is now the **blocking
DEFAULT on three live owner-queue publish sequences** (The Painted Stones,
The Puddle Museum, The Windmill Mouse — each carries "illustration
money-decision — Commission / AI / Park (seat recommends Park; §5). Blocking:
nothing below proceeds without it." in `docs/publishing/OWNER-QUEUE.md` @ the
same pin). The plan's own V049 note shows what happens to unpriced defaults
in this document: the §4 blanket "KDP Select: Yes" was STRUCK by a measured
verdict (P038 → V049, this pipeline). §3's park default is the sibling
surface — a real, live, blocking owner money-gate, recommended on a stated
qualitative argument ("the wrong order") and never priced against the plan's
OWN committed unit economics ($12.99 list · flat ~$3.60 print · "≈
**$4.19/unit**" — §1 CORRECTION #1) and the plan's own zero base case (§6:
"Base case for an unknown author with no marketing is ≈ $0"). This head
builds nothing in venture-lab and never edits its files (routing is the
manager's per Q-0260); it prices the gate and hands the lane a pre-registered
ruling.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested decision, stated back.** Three kids titles sit fully vetted
with their whole publish sequences hard-blocked on one defaulted click:
park, or spend. The tradeoff is real and three-cornered: commissioning costs
four figures per title against a base case the plan itself calls ≈ $0;
AI art costs approximately nothing and is explicitly KDP-permitted with
disclosure, but the seat declines it for the flagship on an unquantified
IP/quality reservation; parking spends nothing and earns nothing — and
forfeits the cheap information a published pilot would generate. The
falsifiable core: **on a pinned line-level sales model built from the plan's
own committed unit economics, does PARK maximize expected net dollars over a
pre-registered dead-share-belief × commissioned-art-cost grid against the
plan's own committed alternatives (A, B, and the seat's own AI-pilot-one
hedge) to within a pre-registered margin — and where it loses, WHICH spend
family wins?** No prior proposal or verdict prices an up-front spend gate, a
value-of-information pilot, or any decision denominated in dollars
(Relations below); the drafting-time landing is computed and DISCLOSED per
the P048–P053 closed-form-arm norm.

**The model (fixed, fully pinned — every constant a decision of this file,
none left to the implementer; money and probabilities exact rationals
throughout).**

- **Time and horizon.** Whole days; horizon **H = 365** from day 0 (invented,
  pinned; sensitivity H ∈ {180, 730}, reporting-only).
- **The line.** **K = 5** kids titles (the §3 outlay line's own count: "a
  3-book Comet Biscuit series + 2 standalone kids titles"; sensitivity K = 7
  adding the §2 re-tiered The Painted Stones + The Lantern Door,
  reporting-only; the owner queue's three packet-vetted sequences are the
  live subset, disclosed).
- **Line state (the hierarchical reading of §6's "base case ≈ $0" — for ONE
  unknown author the dominant risk is line-level, not per-title):** the kids
  line is DEAD with probability **π_L** (every title's true daily sale
  probability p = 0) else ALIVE, and each title then draws p i.i.d. from the
  living pmf **ω = (7/20, 3/10, 1/5, 1/10, 1/20)** over **P_live = {1/60,
  1/30, 1/10, 1/3, 1}** (a ~bimonthly seller … a daily-ceiling hit;
  invented-but-pinned, mass on slow sellers; sensitivity ω′ = uniform 1/5
  each, reporting-only). Mean living rate μ_live = **143/1200** exactly.
- **Belief axis (IN the grid, not assumed):** π_L ∈ **{3/4 (SKEPTIC — the
  §6 zero-base-case reading), 1/2 (NEUTRAL), 1/4 (HOPEFUL)}**.
- **Art-cost axis (the plan's own committed anchors):** commissioned cost per
  title **c ∈ {1500, 3245, 4950}** dollars — the "under $1,500" budget
  floor, the Reedsy band midpoint (derived from the committed endpoints
  1540/4950, disclosed), and the Reedsy high anchor.
- **The grid: 3 beliefs × 3 art costs = 9 pre-registered cells**, order
  pinned (SKEPTIC, NEUTRAL, HOPEFUL) × (1500, 3245, 4950).
- **Revenue.** Each PUBLISHED title, each day, sells independently with
  probability f·p — **at most one sale per day** (the P050/P051 Bernoulli
  convention; the boundary is named below and its direction stated) — where
  f = 1 for commissioned art and f = **q = 7/10** for AI art (invented
  quality discount; sensitivity {1/2, 9/10}). Royalty per sale **r =
  2097/500** dollars exactly (= 60% · $12.99 − $3.60 — the plan's §1
  CORRECTION #1 unit economics at the $12.99 list all three queue sequences
  default to; the plan's rounded "≈ $4.19" asserted consistent in-gate).
- **AI specifics.** Pilot/line tool cost **a = 30** dollars total (the §3(B)
  "~$0–$30/mo" read as one shared tool-month; the per-title accounting
  world a = 150 is a named reporting leg); per-AI-title removal risk
  **ρ = 1/20** at publish (the §3(B) caveat, invented magnitude, sensitivity
  {0, 1/10}) — a removed title earns 0, spend stays spent.
- **Pilot window W = 90 days** — the lane's own committed 90-day unit (the
  KDP Select term and V049's named "90 days of KDP dashboard data on ONE
  enrolled title" probe).
- **Policy family (7, pre-registered — the plan compared to itself):**
  1. **PARK** — publish nothing; NET = 0. (The shipped §3 recommendation C.)
  2. **COMM-ALL** — commission all K at day 0 (spend K·c), publish day 0.
     (§3 option A at face value.)
  3. **COMM-PILOT-SALE** — commission ONE title day 0 (spend c); if it
     records **≥ 1 sale by day W** (the lane's own committed
     ≥1-organic-sale success leg — the P042/P050 harvests), commission the
     remaining K−1 (spend (K−1)·c), publishing at day W; else stop. The
     pilot keeps selling through H either way.
  4. **COMM-PILOT-EV** — as 3, but committing additionally requires the
     exact posterior continuation to clear cost: **V_cont = μ_live · r ·
     (H−W) > c** (on ≥ 1 sale the line is alive with certainty — dead lines
     cannot sell — so the remaining titles' per-title expected gross is
     V_cont exactly; proven in-sim).
  5. **AI-ALL** — AI-art all K at day 0 (spend a total), publish day 0 with
     disclosure; each title sells at q·p, each independently removed w.p. ρ.
     (§3 option B at face value.)
  6. **AI-PILOT-SALE** — AI-art ONE title day 0 (spend a; removed w.p. ρ →
     stop at −a); on ≥ 1 sale by W, commission the remaining K−1 at c each
     (the seat's own hedge shape: pilot cheap, build the flagship properly),
     publishing at day W; else stop, the pilot selling on through H at q·p.
  7. **AI-PILOT-EV** — as 6 with the V_cont > c gate on committing.
- **Outcome.** **NET(cell, policy) = expected dollars net of all spend over
  H**, exact rational. Primary metric, decision-bearing: **Δ(cell) =
  max_{policy ≠ PARK} NET(cell, policy) − NET(cell, PARK)** with the winning
  policy and its family (AI-led vs COMMISSION-led) recorded. Secondary,
  reported, NEVER decision-bearing: the full 9 × 7 NET table; the
  break-even art cost c* = V_cont; the break-even alive-share for AI-ALL
  (margin-clearing and EV-zero); the commit probabilities per pilot policy;
  the per-p conditional revenue split.

**Two arms.**

- **Arm A (decision arm — exact, seedless):** every NET is a finite exact
  expected-value tree over `fractions.Fraction` — linearity gives per-title
  gross in closed form (f·p·r·days), the pilot branches weight on the exact
  commit probability P(≥1 sale in W | p, f) = 1 − (1−f·p)^W mixed over the
  prior, and the posterior alive-certainty on ≥ 1 sale collapses the
  continuation to V_cont exactly. Sub-second, stdlib only. The ruling rides
  Arm A alone.
- **Arm S (confirmation arm — seeded MC):** **N = 200,000 scenario draws per
  cell** via `random.Random(20261353)`, cells in pinned order; per scenario,
  pinned draw order: line state → per-title p (K draws) → per-title removal
  coin where AI-published → daily Bernoulli sale trials day-by-day per
  published title; **common random numbers** — one scenario's draws are
  replayed against all 7 policies. Estimator: mean net dollars. **Agreement
  gate:** |ArmS − ArmA| ≤ 10 dollars absolute on EVERY (cell, policy) AND
  ≥ 4·SE headroom verified per leg from the per-scenario sample SD — any
  breach invalidates the run.

**Seeds (registered):** 20261353 (Arm S main confirmation leg) / 20261354
(stability leg, 20,000 scenarios per cell — the twin evaluators must
reproduce the Arm-A ruling on it under the widened gate ≤ 25 dollars) /
20261355 (reporting legs — H ∈ {180, 730}, K = 7, ω′, q ∈ {1/2, 9/10},
ρ ∈ {0, 1/10}, a ∈ {0, 150}, W ∈ {45, 180}, and the margin sweep, 20,000
each) / 20261356 (aux — NEVER read by any decision number). Allocated
strictly above the PROPOSAL 053 high-water **20261352** — re-swept at
drafting: digit-boundary regex over this tree at HEAD `442be87` plus the
sim-lab working copy READ-ONLY at `f37d9b1` with `results.json` excluded
shows max allocations 20261352 / 20261348 (the larger numerals —
20261542/20261664/20261833 and kin — are digit substrings inside exact-
Fraction numerators quoted from sim-lab results.json, data not seeds; the
P046/P050/P051/P052/P053 rule re-confirmed). Byte identity: stdout +
results.json byte-identical across two process runs; Arm A
platform-independent exact Fractions, Arm S pinned to a stated CPython minor
version.

**Pre-registered decision rule (fixed BEFORE any code exists; evaluated in
this order, REJECT FIRST; margin m = 100 dollars exact — the plan's own
smallest per-spread art quantum, the "$100–$400 per spread" floor rate;
reporting sweep m ∈ {25, 400}, the two committed band edges).**

- **REJECT** ("the park-everything default is materially mis-set at the
  plan's own committed constants — a spend option the plan itself commits
  beats parking by at least one spread-floor per cell, consistently; the
  park recommendation then survives only as an implicit ≥ m-per-cell price
  on the unmodeled IP/quality reservation, and that shadow price becomes a
  number the owner can accept or reject"): **Δ(cell) ≥ 100 in ≥ 7 of 9
  cells AND the winning policy's family (AI-led or COMMISSION-led) is the
  same in every such cell.** Checked FIRST — the costly-error rationale:
  three live owner-queue sequences sit hard-blocked on this default; a
  wrongly-parked line forfeits both revenue and the cheap information that
  would unlock it, and the blocking gate propagates to every downstream
  click in all three sequences.
- **APPROVE** ("park-first holds at the plan's own beliefs and costs"):
  **Δ(cell) < 100 in ≥ 7 of 9 cells AND in ≥ 2 of the 3 SKEPTIC cells**
  (the evidence-favored row — §6's zero base case makes the dead-heavy
  belief the operative one), the seed-20261354 stability leg reproducing
  the ruling through the twin evaluators. Mutually exclusive with REJECT by
  arithmetic (7 + 7 > 9).
- **NULL** (anything else — a legitimate, reportable outcome): the citable
  pin is the full 9 × 7 NET table with Δ, families, and the named BINDING
  AXIS — pre-registered candidates: (i) **belief-conditional** — over-margin
  cells concentrate in the NEUTRAL/HOPEFUL rows: the gate hinges on the
  dead-share belief, flip boundary named (the drafting tables already locate
  it: AI-ALL clears the margin above alive-share ≈ 0.2143 and clears zero
  above ≈ 0.0495); (ii) **cost-conditional** — over-margin cells concentrate
  in one c column: the gate should be set WITH the art-cost quote in hand;
  (iii) **family-split** — AI-led wins some over-margin cells and
  COMMISSION-led others (parking still loses, but WHICH spend wins is
  belief/cost-conditional — the finding); (iv) **margin-thin** — the ruling
  flips inside the m ∈ {25, 400} sweep; (v) **arm disagreement** — the
  agreement gate fails (a defect is the finding, no ruling); (vi)
  **sensitivity straddle** — a reporting-only leg (H, K, ω′, q, ρ, a, W)
  lands a band conjunct on the other side of its edge (named, never
  flipping the decision). **Cheapest live probe, named — it is machinery
  the lane ALREADY carries:** each of the three queue sequences already
  includes the AI-disclosure click and the $12.99 default; ONE pilot
  title's 90-day KDP dashboard read (the V049 probe pattern, verbatim)
  pins the real p row and the real removal/quality experience at zero new
  tooling.

**Expected landing, DISCLOSED (the P048–P053 closed-form-arm norm — the
decision arm is a closed-form expected-value tree, so the drafting-time
landing was computed and is disclosed rather than feigning openness; the sim
re-derives everything from scratch and must not trust these numbers).** At
the pinned constants the drafting tree lands **REJECT, 9 of 9 cells, argmax
AI-ALL in every cell**: Δ is row-constant and column-independent — SKEPTIC
**778482513/6400000 ≈ $121.64**, NEUTRAL **874482513/3200000 ≈ $273.28**,
HOPEFUL **2719447539/6400000 ≈ $424.91** — because the commission channel is
**strictly dominated at every posterior the pilot can reach**: the exact
per-title continuation ceiling V_cont = μ_live·r·275 = **$137.44** sits a
factor ~11 below the committed $1,500 art-cost floor, so no pilot outcome
ever rationally commissions (COMM-ALL runs ≈ −$6,800 … −$24,500). Two
sharpenings the disclosure buys: (1) **the information channel is dead at
the committed prices** — the 90-day pilot cannot buy enough information to
justify commissioning at ANY posterior, so the only live comparison is the
$30 AI spend vs the $0 park, and THAT hinges purely on the dead-line belief;
(2) the seat's own hedge (AI-PILOT-EV) sits at **+$0.33** in the SKEPTIC
row — the $30 pilot is an almost exactly break-even bet at the lane's own
most skeptical belief (reported curiosity, decision-irrelevant at m = 100).
Falsifiability is real and disclosed: the **a = 150 per-title-accounting
world lands 6 of 9** (REJECT fails → belief-conditional NULL), the
**q = 1/2 world lands 6 of 9**, and the H = 730 world pushes every row
further over — so the pre-registered bands genuinely discriminate and two
named reporting legs would already flip the count if promoted.

**What a reader DOES differently on the verdict** (all routing lane-side via
the manager per Q-0260 — this repo edits nothing in venture-lab). A
pre-registered APPLICATION GUARD rides every branch, TWO conditions: (1) the
verdict conditions on the §3 option set and the pinned unit economics
($12.99 list · $3.60 print · 60% print royalty · the 1500/1540–4950 art
anchors · the $0–30/mo AI reading) — a materially different committed
art-cost or royalty text means re-run, not reuse; (2) it conditions on
**zero published kids titles as of 2026-07-14** — a kids title going live
before application replaces belief rows with a measured p and stales the
conditioning (the V049/V053 guard pattern, inherited).

- **REJECT** → the manager gets a paste-ready structured choice with the
  9 × 7 NET table attached, recommendation first (Q-0263.2): **(a,
  recommended — it is the seat's own committed hedge, now with numbers)**
  execute the AI-pilot-one click with disclosure at the pinned ~$30 on ONE
  queue title; **(b)** AI-all with disclosure, accepting the named
  unsettled-IP boundary; **(c)** keep parking — now explicitly priced as
  paying the per-cell shadow premium (the Δ column) for IP cleanliness — an
  owner intent call per the V044/V046 posture, never ruled by fiat here.
- **APPROVE** → the §3 park default gains its measured basis and the three
  blocking queue gates cite a table instead of a sentiment.
- **NULL** → the named axis ships with its flip boundary (belief threshold,
  cost column, or family split) plus the free live probe above.

**Gates (run invalid on any failure).**

- **F1 — normalization:** ω sums to 1 exactly; every π_L row a legal
  probability.
- **F2 — unit-economics recompute (exact):** r = 60/100 · 1299/100 −
  360/100 = **2097/500** exactly; consistency with the plan's rounded
  figure asserted |r − 419/100| = 1/250 ≤ 1/100.
- **F3 — dead-line identities (exact):** at π_L = 1: NET(PARK) = 0,
  NET(AI-ALL) = −30, NET(COMM-ALL) = −K·c, every pilot = −a resp. −c
  exactly (commit probability exactly 0).
- **F4 — hand world:** H = 4, W = 2, K = 2, point prior p = 1/2, π_L = 1/2,
  c = 3, a = 1, q = 1/2, ρ = 0, r = 1 ⇒ **NET(AI-ALL) = 0 exactly**
  (hand chain: E[p] = 1/4; per-title gross q·E[p]·r·H = 1/2; two titles = 1;
  minus a = 1 ⇒ 0).
- **F5 — theorem gates (exact, both arms where applicable):** (a)
  NET(COMM-ALL) strictly decreasing in c; (b) every policy's NET
  non-decreasing in the alive share 1−π_L; (c) AI-ALL ≥ AI-PILOT-EV under
  the pinned shared-tool accounting (breaks BY DESIGN under the a = 150
  reporting world — asserted there in reverse as the accounting boundary);
  (d) Δ column-independence asserted structurally whenever V_cont < min c.
- **F6 — battery:** arm agreement gate (bounds above); per-scenario
  draw-count sentinels (one line-state draw + K p-draws + removal coins ≡
  AI-published titles + daily trials ≡ recorded published-title-days); twin
  independently-written decision evaluators; stdout + results.json
  byte-identical across two process runs; CPython minor pinned — the
  P017–P053 standing battery.

**Reporting-only legs (Arm A exact re-evaluations + seed-20261355 Arm-S
confirmations at 20,000 scenarios — CANNOT flip the decision):** the full
9 × 7 NET table with Δ and families; c* = V_cont and the AI-ALL break-even
alive-shares; commit probabilities per pilot policy per cell; the per-p
conditional revenue split; H ∈ {180, 730}; K = 7; ω′ uniform; q ∈ {1/2,
9/10}; ρ ∈ {0, 1/10}; a ∈ {0, 150}; W ∈ {45, 180}; the margin sweep
m ∈ {25, 400}. Aux seed 20261356 is reserved and never read by any decision
number.

**Grounding / hermeticity.** ZERO network reads at verdict time AND zero
repo reads — the entire world (the belief rows, ω and P_live, the cost
anchors, q/ρ/a/W/H/K, the bands, the hand fixture) is constructed in-sim
from the pinned constants in this file, committed as a small fixture JSON
alongside one stdlib file; the harvested §3 option texts, the seat
recommendation, the three queue-gate lines, and the unit-economics rows are
quoted in the fixture with their FIRSTHAND pin (venture-lab `d93aee5`) for
citation only. Decision arithmetic exact `fractions.Fraction`. Feasibility:
Arm A is a closed-form tree — milliseconds; Arm S ≈ 9 cells × 200,000
scenarios × (K p-draws + bounded day loops, dead lines short-circuiting at
one draw) — minutes, pure CPython (the P050 scale precedent); the
20,000-scenario legs are noise on top. No dependencies.

## Relations (adjacent heads — deliberately links, not duplication)

- Nearest by DOCUMENT: **P038 → V049** (KU-exclusivity fork) — the SAME
  publishing plan, the sibling unpriced default: V049 priced §4's blanket
  "KDP Select: Yes" (WHERE a published ebook may sell) and its REJECT is
  already applied in the doc; this head prices §3's park default (WHETHER a
  kids title gets to exist at all). Zero shared machinery — a per-contact
  buy-vs-borrow revenue mixture there, an investment gate with a
  value-of-information pilot here; the two verdicts compose (enrollment is
  downstream of publication).
- Nearest by MOVE: **P050** (kill clock) is a stopping threshold on a
  RUNNING slot (renewal economics, no up-front spend); **P042 → V053**
  allocates build TOKENS across channels (budget allocation, not a
  spend/no-spend dollar gate); **P018 → V020 / P030 → V032** allocate
  production budget across titles/versions (token-denominated). No prior
  head prices an up-front investment, a pilot's information value, or ANY
  quantity in dollars — this is the pipeline's first dollar-denominated
  decision head.
- The pricing SIM-REQUEST verdicts **V037/V039/V040/V041** set price POINTS
  on products already publishable; no spend gate, no VOI.
- **P046** (keyword tiling) is the books half's discoverability-allocation
  head — finished titles, no money.
- The tree-wide dedup sweep `rg -i -g '!bootstrap.py' -g '!.substrate'
  'illustration|picture.?book|art.?(cost|spend)|kids.?(book|title|line)|commission'`
  at drafting HEAD `442be87` plus the sim-lab working copy at `f37d9b1`
  hits only incidental prose (a substrate-kit idea's "output, not
  illustration" phrasing; gba/casino blocks matching "commission"-adjacent
  text) — no proposal P001–P053, no verdict V001–V063 (V064 in flight on
  P053's healthcheck world, zero overlap), no idea file and no session-card
  💡 prices an art spend, an illustration gate, an investment decision, or
  a value-of-information pilot.
- Runners-up this slice, weighed and dropped on merit: **the §5
  English-first translation strategy** (its spend-avoidance argument is
  already partially sunk — Dutch editions exist in vetting — but the
  decisive constants are external market claims, not committed unit
  economics; weaker pin); **the release-cadence question** (dump vs drip
  against the committed 3-titles/day cap — the visibility-boost model would
  be entirely invented with no committed anchor on EITHER side); **the
  Ultramarine serial free-first-episode funnel** (V037's world). The
  illustration gate won on: a live BLOCKING owner money-decision, all
  decisive constants committed in one document, a committed
  default AND its committed alternatives to price against each other, and
  the V049 precedent proving this exact document acts on measured verdicts.

## Model basis (declared model-dependence — the P024 discipline)

This verdict's numbers are CONDITIONAL on an embedded model, named up front:

- **(1) Statistical assumptions:** sales are stationary per-day Bernoulli
  per published title, **at most one sale/day** — the cap boundary is
  load-bearing and its direction stated: a breakout tail (multiple
  sales/day) is exactly what the model EXCLUDES, and excluding it
  UNDERSTATES publishing value, so the model is GENEROUS TO PARK — the
  disclosed REJECT is robust to it, and an APPROVE would have to be read
  net of it. Line-level hierarchical risk (one dead/alive coin for the
  whole line) with i.i.d. titles given alive; deterministic costs; no
  marketing/ads (§6's own frame); removal risk and quality discount for AI
  art only; no seasonality. Invented-and-pinned where the plan is silent:
  P_live, ω, the π_L rows, q, ρ, the shared-tool a-accounting, H, and the
  margin m — each disclosed inline, the belief and cost axes promoted INTO
  the decision grid rather than assumed; the grounded constants ($12.99 ·
  $3.60 · 60% · the art anchors · $0–30/mo · W = 90 · the option set · the
  park default · the ≥1-sale leg · the zero base case) are the plan's own
  @ `d93aee5`. **The invented-widths boundary, stated plainly: there is no
  live kids-line sales datapoint anywhere in the fleet** (the catalog has
  ZERO published kids titles — that is the harvested gate itself), so
  P_live and ω bracket SCALE, not measured shape — and the cheapest live
  probe (one pilot title's 90-day KDP dashboard, the V049 pattern)
  measures the real row directly at zero new tooling.
- **(2) Single most-likely-to-flip alternative:** the SALE-RATE MODEL
  itself — if real unknown-author kids paperbacks sell materially below
  even the pinned slow tail (the true row sits under 1/60/day with the
  living mass overstated), the AI cells shrink toward −a and the ruling
  moves APPROVE-ward; if the breakout tail is real, it moves further
  REJECT-ward. Both directions are covered by named grid/reporting axes
  (π_L rows; ω′; the cap boundary above). Softer flips, named as out of
  the registered scope: the **legally-unsettled AI-image copyright** (§3's
  own caveat — inspection-decidable, never simulated; the verdict carries
  it as the SHADOW-PRICE reading, not a probability); the kids **ebook/KU
  edition** (the kids path is print-first fixed-layout — out of registered
  scope); the **3-new-titles-per-day cap** (never binds at K ≤ 7); Tier-1
  cross-funding interactions (§3(C)'s "until Tier-1 revenue funds art" —
  the option value of parking is horizon-bounded here, disclosed).

## Probe report (v0, 2026-07-14)

> Single-pass battery (panel not escalated: self-contained knowledge probe
> over pinned lane constants, sim is report-only evidence, no
> spend/publish/irreversible surface — README § probe battery). Verify-first
> ran FIRST, live this slice: (a) **source verified FIRSTHAND** —
> `add_repo` for venture-lab attempted once and SUCCEEDED (the P050 denial
> did not recur; the wall is evidently session-scoped, recorded for
> CAPABILITIES routing), read-only shallow clone `git log -1`-verified at
> `d93aee502a4daf2b3f7cd249067eb5c5a5ac046c`; every §1/§3/§6 constant and
> all three OWNER-QUEUE gate lines read directly and quoted verbatim above.
> (b) **dedup** — the tree-wide topic sweep (Relations above) at HEAD
> `442be87` plus the sim-lab working copy at `f37d9b1`; PROPOSALs 001–053
> (headers + summary lines) and VERDICTs 001–063 (headers + subject lines)
> swept before drafting; nearest-neighbor families (P038/V049 same-document
> sibling default, P050/P042/P018/P030 allocation-and-stopping kin,
> V037–V041 price points) argued distinct by machinery above. (c) **kill
> test NOT triggered** — no prior head prices a spend gate, an art
> decision, a VOI pilot, or anything in dollars. (d) **feasibility +
> liveness arithmetic checked** — runtime bounded in the preamble
> (milliseconds exact arm + minutes MC, stdlib only); the drafting-time
> tree was actually RUN and its landing DISCLOSED (REJECT 9/9, argmax
> AI-ALL, with the two 6-of-9 reporting worlds named — the P048–P053 norm).

**1. What is this really?** A pre-registered pricing of the publishing
plan's §3 park-the-kids-titles default against the plan's own two committed
spend options (commission at the committed anchors, AI art at the committed
tool cost with disclosure) plus the seat's own AI-pilot-one hedge, as a
7-policy expected-net-dollars decision over a 9-cell dead-share-belief ×
art-cost grid at the plan's own committed unit economics, primary metric the
best non-park policy's margin over park with its family, exact-Fraction
closed-form decision arm confirmed by common-random-numbers seeded MC under
an agreement gate, judged against bands fixed before any code (REJECT first:
≥ one spread-floor in ≥ 7 of 9 cells with family agreement), byte-identical
across two process runs.

**2. What is the possibility space?** (i) Don't run it — the round-10
venture slot goes unserved and three publish sequences stay blocked on an
unpriced sentiment. (ii) Serve the books half from the translation-strategy
or release-cadence surfaces — weighed and dropped in Relations (external
pins; fully-invented boost model). (iii) A prose answer ("obviously don't
spend before sales exist") — measures nothing, and the drafting tree already
shows the committed-constants answer is NOT that sentence: the cheap spend
beats park in every cell while the expensive spend loses catastrophically —
the sentiment conflates two options the numbers separate. (iv) Wait for
live sales data — there will never be any while the gate blocks publication;
the gate is self-sealing, which is exactly why it needs pricing. (v) This
head: hermetic, exact-arithmetic, pre-registered — the pipeline's standing
shape.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file + one fixture JSON yields: the exact 9 × 7
net-dollar surface separating all three committed options AND the pilot
hybrids, the proof that the commission channel is dead at every reachable
posterior (c* = $137.44 vs the $1,500 floor — the "wrong order" instinct
vindicated with a factor-11 number), the quantified shadow price the park
default implicitly puts on the unsettled-IP reservation ($122–$425 per
cell), and a reusable pattern — investment gate + VOI pilot under a
hierarchical dead-line prior — that transfers to any future fleet head with
an up-front-spend dial (cover commissions, ad tests, translation spends,
hardware buys).

**4. What breaks it? (assumptions made explicit)** (a) **The sale-rate
model** — the named most-likely flip; no live kids datapoint exists;
direction covered on both sides (grid rows + the cap boundary, which is
GENEROUS TO PARK so the disclosed REJECT is robust in the direction that
matters). (b) **The invented AI parameters** — q, ρ, and the shared-tool
accounting carry no measurement; all three have named reporting legs, and
two of them (a = 150, q = 1/2) already land 6-of-9 — disclosed as the
REJECT's genuine fragility axes. (c) **The unsettled-IP boundary** — never
simulated; the verdict's REJECT reading is deliberately shaped as a shadow
price so the reservation is priced, not overruled. (d) **Horizon-bounded
park** — parking's option value beyond H is not modeled (named; the H = 730
leg brackets the direction). None of these is hidden; each is a grid axis,
a sensitivity leg, a named flip, a guard condition, or a stated scope bound.

**5. What does it unlock?** The last blocking DEFAULT in the kids queue
stops being decorative: either the park default is REJECT-priced and the
owner gets a three-option paste-ready choice in which the seat's own hedge
is the numbered recommendation, or park gains its measured basis, or the
binding axis is named with a free 90-day probe. The plan document gets its
second measured-default correction (V049 struck §4's; this prices §3's).
The pipeline gains its first dollar-denominated verdict and its first
value-of-information head; the venture slot's books half gains its fourth
distinct dial (production → enrollment → discoverability → existence).

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external at verdict time — fully hermetic by construction (the P017–P053
precedent). The harvest grounding is one already-verified read-only clone
pin (FIRSTHAND, `d93aee5`). Cheapest kill BEFORE simming: a prior fleet
verdict on spend gates (none — P001–P053 and V001–V063 swept), or a
committed venture-side art quote contradicting the pinned anchors (none in
the clone at the pin). Cheapest confirm AFTER a NULL or REJECT: the pilot
itself — one owner click the queue already sequences, 90 days of dashboard
data the V049 probe already specifies.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab builds and runs the sim (the Q-0264 pipeline's verify seat — this
file is its intake spec); venture-lab's books lane consumes the verdict as
a keep/execute/re-price decision on the §3 gate, routed by the manager per
Q-0260; this repo builds nothing. It displaces nothing in flight (V064
holds P053's healthcheck world; no verdict session holds a venture head)
and duplicates nothing (Relations dedup above; V049 owns §4's fork,
V037–V041 own the price points).

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib Python file (both arms + gates + twin evaluators), one fixture JSON
(every pinned constant in this file, copied verbatim: P_live and ω with
ω′, the π_L rows, the c anchors, r = 2097/500, a/q/ρ/W/H/K with their
sensitivity pairs, the 7-policy definitions with the ≥1-sale and V_cont
commit rules, band constants (100, 7-of-9, the family-agreement conjunct,
the 2-of-3 SKEPTIC conjunct, the {25, 400} sweep), the F1–F6 fixtures with
the hand-world zero, per-leg scenario counts, seeds 20261353–356, the
harvested §3/§6/queue lines with the FIRSTHAND pin `d93aee5`), one
REPORT.md with the 9 × 7 NET table, the Δ column with families, the
ruling, and the named-axis/probe line on NULL — the standing INTAKE/VERDICT
grammar, nothing else.

**Recommendation: sim-ready** — every constant pinned here, bands registered
REJECT-first before any code, seeds 20261353–356 above the verified
high-water 20261352, fully hermetic at verdict time, the drafting-time
landing computed and disclosed; the honest next step is the sim itself.
