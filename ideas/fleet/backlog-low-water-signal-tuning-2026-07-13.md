# Backlog low-water signal: does the "~3" threshold earn its heartbeat line?

> **State:** sim-ready
> **Class:** process · **Target:** the fleet itself (verdict consumers: substrate-kit
> — heartbeat-grammar token decision + planted default; fleet-manager — the routing
> consumer; websites — the source bullet's disposition; idea-engine — consumer #1 of
> any adopted signal; verification target `menno420/sim-lab` per the Q-0264 pipeline)
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8f9765483a7df57ce426e7d11d200f10b5495ed7/docs/ideas/backlog.md@8f97654 · fetched 2026-07-13T01:28Z

*(Pin integrity: the fetched bytes hash to blob
`e14bb15408b1f45de14eae72efe990024f0e548c` by `git hash-object` — byte-identical to
the blob the PR #244 lane-backlog groom recorded at the same pin.)*

**Origin:** drafted under standing owner ORDER 003 (continuous pipeline) + ORDER 004
rule 3's rotation ("fleet backlogs → venture's book/product space → game mechanics →
COMPLETELY UNRELATED domains") — PROPOSALs 015/016 were game mechanics, 017 the
unrelated slot, 018 the venture slot; this slice restarts the cycle at FLEET
BACKLOGS. Harvest source, quoted verbatim from the websites lane's own backlog
(`docs/ideas/backlog.md` @ websites `8f97654`, blob `e14bb15`, lines 125–130):
"**Backlog low-water signal in the heartbeat** · `captured` — when the
captured+planned count drops below ~3, the heartbeat notes carry `backlog: low (N
left)` so the manager routes work BEFORE a lane hits upkeep-dry (routing latency
beats idle wakes); rung telemetry records which rung fired, not depth." That bullet
contains an invented constant (the "~3") and an untested mechanism claim ("routing
latency beats idle wakes") — and its fleet-generalized form is ORDER 003's own
done-when made mechanical: "the PROPOSAL→VERDICT pipeline is never dry" is a
low-water-signal policy for THIS seat's backlog too. This head pre-registers the
threshold question and hands the fleet a measured default (or a measured retirement)
instead of a vibe.

## The idea (reasoned to its fuller form — Q-0254 duty)

Every never-idle lane runs the same hidden inventory loop: a backlog of workable
items is drawn down roughly one per work wake, refilled organically in bursts
(harvest sweeps, close-out waves), and — the bullet's proposal — refillable ON
SIGNAL, if the lane tells the manager it is running low and the manager routes work
after some latency. Whether that signal is worth a heartbeat line, and at what
threshold, is a classic base-stock/reorder-point question nobody has run the
numbers on: too low a threshold and the lane goes upkeep-dry while replenishment is
in flight (the exact failure ORDER 004 rule 3 patches by hand: "An empty intake
means HARVEST, never idle"); too high and the signal fires constantly, training the
manager to ignore it (alarm fatigue — the cost the bullet never prices). The
websites backlog's own committed history supplies a real calibration anchor: across
its four measured re-pin intervals (2026-07-10T22:33Z → 2026-07-12T01:47Z, pins
`144dfce → 8c19e93 → d862364 → c81ce76 → 8f97654`), captured-bullet counts moved
13 → 10 → 6 → 6 → 14, with per-interval births {2, 5, 4, 11} and consumptions
{5, 9, 4, 3} — near-balanced in the mean (22 born vs 21 consumed) but heavily
bursty, which is precisely the regime where reorder-point policies earn or waste
their keep.

**The sim (fully hermetic — the PROPOSAL 017/018 precedent; every fixture is a
pinned constant committed with the sim, zero repo/network reads in the verdict
session):** discrete wakes t = 1..H, **H = 2,000**, backlog starts **b₀ = 6**. Each
wake, in pinned order: (1) any in-flight replenishment due this wake lands (+R,
**R = 4** primary); (2) consumption — the wake demands backlog work with probability
**p_c ∈ {0.6, 1.0}** (not every wake picks the backlog rung); if it demands and
b > 0, b −= 1; if it demands and b = 0, count a **dry wake**; (3) organic arrival —
with probability q, a batch of size g lands, per arrival regime: **A1 steady-small**
(q = 0.30, g uniform on {1, 2, 3}; mean 0.60/wake), **A2 bursty-real** (q = 0.10, g
uniform on the OBSERVED multiset {2, 4, 5, 11}; mean 0.55/wake — anchored to the
four measured websites re-pin births), **A3 harvest-scarce** (q = 0.05, g uniform on
{2, 3, 4}; mean 0.15/wake); (4) signal policy — threshold **N ∈ {0(off), 1, 2, 3,
4, 6}**: if b ≤ N and no replenishment is in flight, emit a signal (one outstanding
at a time — the wake-hygiene rule) and schedule +R to land at wake t + L, manager
routing latency **L ∈ {1, 2, 4}** wakes (same-sweep / next-sweep / overnight).
Cells: 3 arrival regimes × 2 p_c × 3 L = **18 cells**; per (cell, N): **M = 300**
seeded replications, `random.Random(20260719)`, pinned loop order (cells
lexicographic, N ascending, replications sequential; per-wake draw order:
consumption, arrival-fire, batch-size). Metrics per (cell, N): **D** = dry wakes /
demand wakes (the fraction of work wakes that find the cupboard bare), **S** =
signals per 100 wakes (the alarm cost), mean backlog (bloat, reporting-only).
Reporting-only sensitivity legs that cannot flip the decision: R ∈ {2, 8}, b₀ ∈
{3, 12}, H = 500, and a decision-stability leg at M = 50 with seed 20260720 that
must reproduce the same ruling. Results table pins the CPython minor version;
byte-identical on re-run.

**Pre-registered acceptance bands and decision rule** (set BEFORE any code runs;
evaluated in this order):

- Per cell, **N\*(cell)** = the smallest N ∈ {1, 2, 3, 4, 6} with **D(N) ≤ 0.05 AND
  S(N) ≤ 25** (per 100 wakes); it may not exist. **ΔD(cell) = D(0) − D(N\*)** where
  N\* exists.
- **REJECT-a** ("organic refill suffices — retire the bullet") iff D(0) ≤ 0.05 in
  ≥ 80% of the 18 cells. Checked FIRST.
- **APPROVE** ("ship the signal; pin the threshold") iff N\* exists in ≥ 80% of
  cells AND median ΔD ≥ 0.10 (the signal buys ≥ 10 points of dry-wake reduction
  over signal-off). Recommended threshold = grid-median N\*; the verdict must state
  whether the bullet's own "~3" lies within ±1 of it.
- **REJECT-b** ("no robust threshold exists") iff N\* exists in < 50% of cells.
- **NULL** otherwise — a legitimate reportable outcome: the verdict names the flip
  axis (for each swept axis, the N\*-exists share and median ΔD at each of its
  values; largest spread = the named boundary — expected candidates: routing
  latency L and the A3 harvest-scarce regime), and the citable finding is the
  CONDITIONAL rule (e.g. "signal only for harvest-scarce lanes / long-latency
  routing"), not either camp's default.

**Consequence:** on APPROVE — the substrate-kit lane gets the evidence row for
declaring a `backlog:` token in the kit-owned heartbeat grammar (`src/engine/
grammar.py` — the extension-key declaration story already routed via
`ideas/substrate-kit/README.md`'s heartbeat cross-links) with the sim-pinned
threshold as the planted default; the websites bullet graduates from "~3 by vibe"
to the measured N\* (relayed via the manager sweep — the lane is PARKED, self-serve
never comes, the PR #244 groom's own finding); idea-engine adopts the signal as
consumer #1 (a notes-line first, per the fold-in-over-declare rule, until the kit
token lands). On REJECT — the bullet is retired with the quantified reason routed
to the manager sweep for the websites backlog, and NO kit grammar token is spent (a
grammar line avoided is a real win — undeclared keys measurably leak into `phase`
through hand-kept parsers, the PR #59 fold-in evidence). On NULL — the conditional
rule is the citable finding, and the cheapest LIVE probe is named: idea-engine logs
its own per-wake backlog depth alongside the rung it fired in its heartbeat `notes:`
for ~a week (zero new tooling), locating this seat's real (arrival, p_c, L) cell
before anyone spends a grammar decision on it.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the harvest source: `ideas/websites/lane-backlog-2026-07-10.md` link-indexes
  the bullet (born at the third re-pin, still `captured` at the fourth @ `8f97654`)
  and the PR #244 groom classed it lane-internal, minting NO idea file — this head
  is deliberately NOT the capture-the-bullet move (the link-index-only rule holds);
  it is the gap the bullet EXPOSES: an invented threshold constant riding a live
  backlog, fleet-generalized by ORDER 003's never-dry done-when. Same harvest
  pattern as the groom's one named candidate
  (`carried-watch-verdict-inheritance-guard-2026-07-12.md`, websites bullet →
  ideas/fleet/ head), different bullet, different question class (sim-tunable
  policy vs grammar/checker rider).
- vs the outbox (PROPOSALs 001–018, re-read at HEAD `d0dca70`): nearest by FAMILY is
  PROPOSAL 012 (routine-cadence economics; its verdict is VERDICT 014 by sim-lab's
  own offset map — source numbers cited verbatim, never derived): both are
  fleet-ops policy grids with pre-registered decision rules — but 012's control
  variable is WAKE SCHEDULING (failsafe cadence × chain × event-driven), its
  objective worker-turns per caught trigger vs catch latency, its consumer the
  coordinator's routine posture; this head's control variable is a BACKLOG
  REPLENISHMENT THRESHOLD, its objective dry-wake fraction vs alarm cost, its
  consumers the kit grammar token + the websites bullet + this seat's harvest rung.
  No shared fixture, metric, or consumer. PROPOSAL 013 (heartbeat contradiction
  linter → VERDICT 015) shares only the kit-heartbeat LANDING ZONE — it lints
  content; this tunes a signal policy. PROPOSALs 017/018 are method precedent only
  (hermetic fixtures + APPROVE/REJECT/NULL bands; band discipline reused, zero
  shared domain).
- vs sim-lab (local clone @ `a3b921b`, verdicts through 018 + offset map read this
  slice): no verdict touches backlog depth, low-water signaling, or replenishment
  policy; VERDICT 014 is the family neighbor addressed above.
- Tree-wide dedup sweep (`rg -g '!bootstrap.py' -g '!.substrate'` for
  low-water/upkeep-dry/dry-wake/`backlog: low`/replenish/base-stock/reorder over
  ideas/ + .sessions/ + control/ + docs/): the ONLY hits are the harvested
  lane-backlog index itself (the bullet, quoted above) and its sibling bullet #12's
  passing phrase "backlog dryness" (rung telemetry — records which rung fired, not
  depth; the bullet's own text distinguishes it). No prior threshold, queueing, or
  inventory-policy content anywhere in the tree.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained modeling head, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **grounding** — the bullet
> re-fetched raw at the pinned sha and byte-verified against the groom's recorded
> blob (`git hash-object` = `e14bb15…`), quoted verbatim above, not from memory.
> (b) **dedup** — the sweeps above; zero prior threshold/inventory content.
> (c) **feasibility arithmetic** — 18 cells × 6 N × 300 replications × 2,000 wakes
> ≈ 64.8M wake-steps at ~2–3 RNG calls each: a few minutes in pure CPython, no
> dependencies; sensitivity legs add < 40% on top.

**1. What is this really?** A pre-registered reorder-point sim for never-idle lane
backlogs: at which low-water threshold N (if any) does a heartbeat signal +
manager-routed replenishment keep work wakes from going dry, without the alarm-cost
of a threshold that cries constantly — swept across arrival burstiness (one regime
anchored to the websites backlog's four measured intervals), consumption rates, and
routing latencies, with the source bullet's "~3" tested against the measured N\*.

**2. What is the possibility space?** (i) Don't run it — the bullet stays captured
in a PARKED lane forever, and every lane keeps patching dryness by hand (ORDER 004
rule 3 is exactly that patch). (ii) Adopt the bullet as written — spend a kit
grammar token on an invented constant; the PR #59 fold-in evidence says undeclared
keys leak, so adoption is not free. (iii) Ask the manager/owner — a
structured-choice question with zero evidence attached; strictly worse after this
verdict prices the options (Q-0263.2). (iv) This head: 18-cell policy grid, bands
registered first, NULL names the flip axis and the cheapest live probe. (v)
Over-scope (multi-lane coupled routing, manager-side prioritization queues,
adaptive thresholds) — natural follow-ups ONLY if this lands non-NULL; the static-N
single-lane question is the one the bullet poses.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~200-line stdlib file: the wake loop is four pinned steps,
each policy cell an independent replication loop; the whole grid plus sensitivity
legs runs cold in minutes and yields a fleet-default threshold (or a measured
retirement) any kit-adopted lane inherits.

**4. What breaks it? (assumptions made explicit)** (a) **Models are models** — the
arrival regimes are pinned constructs; that is why A2 is anchored to the observed
multiset (values quoted in this file, committed in the fixture — no verdict-time
reads) and why a regime-dependent result is a pre-registered NULL naming the axis,
never a judgment call. (b) **n=4 anchor** — four observed intervals cannot fit a
distribution; they BRACKET one regime (burst sizes, near-balance), and the other
two regimes sweep the bracket's sides; the anchor leg is reporting-only. (c)
**Latency in wakes, not hours** — L ∈ {1, 2, 4} spans same-sweep to overnight
without asserting wall-clock; the mapping is stated, not measured. (d) **One lane,
one signal** — manager-side contention (five lanes signaling at once) is out of
scope by design and named as the follow-up. (e) **PRNG stability** —
`random.Random(20260719)` pinned, loop order pinned, CPython minor version pinned
in the results table.

**5. What does it unlock?** The fleet's first measured never-dry primitive: an
evidence row for the kit `backlog:` grammar decision (or the evidence to NOT spend
that token), the websites bullet's disposition without waking a PARKED lane, and —
on any outcome — ORDER 003's standing done-when ("the pipeline is never dry")
turned from prose into a number this seat can operate.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external at
sim time — every fixture ({H, M, b₀, R, N-grid, L-grid, regime constants incl. the
observed multisets, p_c grid, band constants, seeds}) is stated in this file and
committed as a small JSON alongside the sim. Kill tests, run live this slice: a
prior low-water/threshold head anywhere in the tree (NOT found — sweeps above), a
sim-lab verdict on backlog policy (NOT found — verdicts through 018 read), the
bullet already promoted/built upstream (NOT found — still `captured` at the
re-fetched pin, lane PARKED), infeasible runtime (NOT found — arithmetic in the
preamble). Sim-worthy or judgment-only: sim-worthy — the entire question is
computable dry-wake/alarm trade-off arithmetic against pre-registered thresholds;
the one judgment question (are 0.05 dry / 25-per-100 alarm / +0.10 material the
RIGHT lines?) is pinned by pre-registration and stated as the disputable bands,
never the measured numbers.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs it (its harness, its verdict grammar; sim + fixture JSON committed in its
sims/ tree). The verdict's consumers are named in the header (kit grammar decision;
manager routing; websites bullet disposition; idea-engine as first adopter).
Duplicates nothing: VERDICT 014 is the family neighbor and shares no control
variable, metric, fixture, or consumer (dedup section above); the bullet itself is
link-indexed, deliberately un-minted by the groom, and untested.

**8. What is the smallest shippable slice?** One sim-lab intake dir: one stdlib
file (wake loop + policy grid + sensitivity legs), one fixture JSON (all constants
copied verbatim from this file), one results table {D, S, mean backlog} × (cell, N)
plus the N\*/ΔD summary and per-axis shares, ending in exactly one of APPROVE /
REJECT / NULL per the pre-registered rule — reproducible from the fixtures alone,
byte-identical on re-run, no flags.

**Recommendation: sim-ready** — the question is crisp and computable, the bands and
decision rule (with stated evaluation order) are registered above BEFORE any code
exists, the genre's failure modes are pre-empted (model-dependence → anchored
regime + axis-naming NULL; grammar-token creep → REJECT explicitly prices NOT
shipping; n=4 anchor → bracketing regimes + reporting-only anchor leg), and every
outcome changes what a named seat does next. THE ONE QUESTION for the simulator:
*Under the pinned never-idle lane model (H = 2,000 wakes, b₀ = 6; consumption
demand p_c ∈ {0.6, 1.0} with a dry wake counted when demand meets an empty backlog;
organic arrivals A1 (q=0.30, g uniform {1,2,3}) / A2 (q=0.10, g uniform on the
observed multiset {2,4,5,11}) / A3 (q=0.05, g uniform {2,3,4}); signal policy
N ∈ {0(off),1,2,3,4,6} with one outstanding signal, replenishment R = 4 landing
after L ∈ {1,2,4} wakes; M = 300 replications per (cell, N), seed 20260719, pinned
loop order; sensitivity legs R ∈ {2,8}, b₀ ∈ {3,12}, H = 500, stability leg M = 50
seed 20260720, all reporting-only), what are D (dry wakes / demand wakes) and S
(signals per 100 wakes) per (cell, N) across the 18 cells — and does the result
land REJECT-a (D(0) ≤ 0.05 in ≥ 80% of cells → organic refill suffices, retire the
bullet, spend no grammar token; checked first), APPROVE (N\* = smallest N with
D ≤ 0.05 and S ≤ 25 exists in ≥ 80% of cells AND median ΔD = D(0) − D(N\*) ≥ 0.10
→ ship the signal with threshold = grid-median N\*, stating whether the bullet's
"~3" lies within ±1), REJECT-b (N\* exists in < 50% of cells → no robust threshold),
or NULL (anything else → the flip axis named via per-axis N\*-exists shares and
median ΔD, the conditional rule is the citable finding, and idea-engine's ~1-week
depth-logging notes-line probe is the named next step)?* Done-when: the committed
sim + fixture JSON reproduce the full results table and summary byte-identically,
the stability leg reproduces the same ruling, and the verdict issues exactly one of
APPROVE/REJECT/NULL per the pre-registered rule (evaluation order stated) with the
n=4 anchor caveat and the latency-in-wakes mapping stated, and the sensitivity legs
reported as legs that cannot flip the decision.
