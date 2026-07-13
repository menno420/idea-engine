# The snapshot stale-indicator threshold — is "3 missed cycles ≈ 180 s" the honest number for the mineverse READ contract's cry-wolf/latency tradeoff?

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 FLEET-BACKLOGS slot,
> round 8; the harvest SOURCE rotates to a SEVENTH repo for this slot — superbot-mineverse,
> the mining-guild web viewer, untapped by ANY prior proposal — after
> round 1 websites (P019), round 2 superbot (P021), rounds 3–4 substrate-kit
> (P025/P029), round 5 superbot (P033, the V023-opened thread), round 6 fleet-manager
> (P037), round 7 curious-research (P041)) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/superbot-mineverse@ae98dd094100f7b864f2c36b91494c8fb2cd1f31 · fetched 2026-07-13T20:18:54Z
> (the harvest-source pin — read via read-only shallow clone this slice, HEAD
> ls-remote-verified; reading path per superbot docs/fleet-reading-path.md;
> pokemon-mod-lab DARK, skipped per the path's own rule. The sim itself is fully
> hermetic: zero repo/network reads at verdict time, every fixture constructed
> in-sim from the pinned constants in this file)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous pipeline —
"continue coming up with new ideas, that is your main purpose"), the rotation established
by ORDER 004 rule 3 ("fleet backlogs → venture's book/product space → game mechanics →
COMPLETELY UNRELATED domains") — round 7 closed fully served (fleet backlogs → PROPOSAL
041, venture → PROPOSAL 042, game mechanics → PROPOSAL 043, unrelated → PROPOSAL 044),
so round 8 reopens at the FLEET-BACKLOGS slot and this slice serves it. The harvested
item is the mining snapshot READ contract's staleness rule (superbot-mineverse
`docs/mining-data-contract.md` § Delivery expectations @ `ae98dd0`), which ships one
load-bearing, hedged-by-its-own-words constant: *"**Staleness**: consumers compare
`generated_at` to now. Beyond a staleness threshold (default suggestion: 3 missed
cycles ≈ 180 s), the frontend shows a stale indicator next to the snapshot metadata
instead of presenting old numbers as live"* — against the same section's cadence
promise, *"the bot pushes a fresh snapshot into the read relay periodically — target
every **60 s** — plus on-demand refreshes"*. The contract names the harm on one side
(presenting old numbers as live) and the mechanism on the other (an indicator that,
if it fires during benign jitter, cries wolf and stops being believed) — and then
pins the tradeoff with a "default suggestion" nobody has priced. Note this head is a
DIFFERENT artifact from the founding-day groomed backlog that P041's Relations
surveyed and dropped @ `f79d0ae` (all UI/refactor/cosmetic or externally blocked);
the READ contract's threshold is exactly the sim-testable shape that survey found
missing. **Placement note:** superbot-mineverse IS a roster-derived section here
(`ideas/superbot-mineverse/`, SECTION COMPLETE 2026-07-11 with "new heads arrive by
capture or harvest per README § Sections" — this is that harvest), so this head rides
its own section, not `ideas/fleet/`.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested decision, stated back.** The mineverse web app is a client-only
viewer: the bot pushes `mining_snapshot.v1` documents into a read relay at a 60 s
target cadence; the browser compares the envelope's `generated_at` to its own "now"
and, past a threshold T, stops presenting the numbers as live. T is a pure
decide-and-flag constant: too small and benign scheduler jitter, an occasional
missed push, or ordinary browser clock skew paints a healthy feed STALE (the
indicator cries wolf next to numbers that are in fact ≤ 2 minutes old — and a
cry-wolf badge protects nobody once users learn to ignore it); too large and a
genuinely dead feed keeps presenting old coins/depth/leaderboard rows as live for
minutes — the exact harm the contract's own sentence exists to prevent. The
falsifiable core: **at the contract's own 60 s target cadence, under the pinned
disturbance model, the suggested 3-missed-cycles threshold (T = 180 s) holds
false-stale to ≤ 1/200 of healthy viewer loads while no ≤ 2-cycle threshold does —
i.e. 180 s is the right-sized default, neither dishonest nor lazily
over-provisioned.** No closed form is on record for the composed disturbance budget,
the window arithmetic puts the neighboring grid cells genuinely near the band (see
liveness), and APPROVE and both directional NULLs are all live, with REJECT as the
protect arm.

**The model (fixed, fully pinned — every constant a decision of this file, none left
to the implementer; all times integer seconds, all probabilities exact rationals).**

- **Producer (healthy):** push ATTEMPTS occur at successive instants separated by
  I ~ uniform integer {55, …, 75} (the 60 s target with −5 s early / +15 s late
  scheduler drift — INVENTED width, pinned, disclosed; sensitivity pairs {58..62}
  and {45..90}, reporting-only). Each attempt independently FAILS with probability
  f = 1/25 (a missed cycle — relay hiccup, transient error; INVENTED, pinned,
  disclosed; sensitivity pair 1/100 and 1/10, reporting-only). A successful attempt
  lands a snapshot stamped `generated_at` = the attempt instant. The inter-SUCCESS
  gap is therefore G = Σᵢ₌₁ᴺ Iᵢ with P(N = n) = f^(n−1)(1 − f), n ≥ 1.
- **Viewer:** loads the page at a uniformly random instant in producer steady state.
  Perceived age at load = A + c, where A is the stationary age of the success
  renewal process and c ~ uniform integer {−30, …, +30} s is the composed
  browser-clock-skew + serve-pipeline offset (INVENTED width, pinned, disclosed;
  sensitivity pairs {0} and {−120..+120}, reporting-only). **Indicator rule under
  test:** show STALE iff A + c > T, threshold grid
  **T ∈ {90, 120, 150, 180, 240, 300, 360} s** (1.5–6 nominal cycles; the contract's
  suggestion is the 180 cell).
- **Outage model:** the producer halts cleanly at a uniformly random healthy
  instant (crash/stop — pushes cease, the relay keeps serving the last document;
  the lane's own no-last-good-cache rule already answers the *missing/invalid feed
  file* case with an honest 503, so a silent halt-while-serving is exactly the case
  the indicator exists for). Per-viewer detection latency
  **L(T) = max(0, T − A − c)** — time from the halt until that viewer's indicator
  turns on (0 if it was already showing).
- **Outcome conventions, pinned:** FALSESTALE(T) = P(A + c > T) in healthy steady
  state — by renewal-reward, FALSESTALE(T) = E_c[ E[(G − (T − c))⁺] ] / E[G];
  LAT(T) = E[L(T)] over the stationary age at the halt and c. Strict inequality
  (perceived age EXACTLY T is LIVE) — pinned.

**Primary metrics.** Per T: FALSESTALE(T) and LAT(T), both exact
`fractions.Fraction` in the decision arm. Derived: **Feas** = {T in the grid :
FALSESTALE(T) ≤ 1/200 AND LAT(T) ≤ 240} and **T\*** = min Feas (undefined iff
Feas = ∅). Band constants pinned: 1/200 (a false stale flag on at most one in two
hundred healthy page loads — an indicator seen more often than that next to
fresh numbers is a cry-wolf badge) and 240 s mean detection (a dead feed is
flagged, on average across viewers, within four minutes — presenting old numbers
as live for longer defeats the sentence's purpose). Reporting per cell: the full
FALSESTALE/LAT curves, P(L > 300), and the per-c splits.

**Two arms.**

- **Arm A (decision arm — exact, seedless):** every disturbance lives on a small
  integer lattice. The gap pmf is the geometric mixture of n-fold convolutions of
  uniform{55..75}: computed exactly for n ≤ 8 (at n = 8, min G = 440 > 390 = the
  largest x = T + |c| any cell evaluates, so every n > 8 term contributes its
  closed-form geometric-tail expectation exactly — no truncation error).
  FALSESTALE via the renewal-reward identity above; LAT via the exact stationary
  age pmf P(A = a) = P(G > a)/E[G]. Exact rationals end to end, no RNG. The
  ruling rides Arm A alone. A tail-closure spot-check (direct enumeration extended
  to n ≤ 12 reproducing the n ≤ 8 + analytic-tail numbers EXACTLY on the pinned
  sub-grid T ∈ {90, 240} × c ∈ {−30, 0, +30}) is a hard gate.
- **Arm S (confirmation arm — seeded MC):** one simulated push timeline per leg —
  warm-up 10,000 s then horizon 5,000,000 s — via `random.Random(20261317)`,
  pinned draw order (per attempt: interval I then fail-bit; then 200,000 viewer
  samples: instant t then offset c; then 200,000 halt samples: instant t then
  offset c), COMMON RANDOM NUMBERS across the whole T grid (one scenario set, all
  seven T evaluated on it; age lookups by bisection over the success timeline).
  **Agreement gate:** |ArmS − ArmA| ≤ 1/1000 absolute on every FALSESTALE cell
  (≥ 8 SE headroom at n = 200,000 in the plausible range) and ≤ 5 s on every LAT
  cell — any breach invalidates the run.

**Seeds (registered):** 20261317 (Arm S main confirmation leg) / 20261318
(stability leg, 20,000 viewer + 20,000 halt samples on a fresh 1,000,000 s
timeline — the twin evaluators must reproduce the Arm-A ruling on it within the
same gates) / 20261319 (reporting leg — the sensitivity and burst-leg Arm-S
confirmations, 20,000 samples each) / 20261320 (aux — NEVER read by any decision
number; reserved for the named live probe's analysis). Allocated strictly above
the P044 high-water 20261316 — re-checked at drafting across every prior outbox
block, the full idea-engine tree at HEAD `0cad099`, AND a fresh sim-lab shallow
clone at its live HEAD `692fcf1` (its largest seed numeral anywhere is 20261316).
Byte-identity: stdout + results.json byte-identical across two process runs
(Arm A platform-independent exact Fractions; Arm S pinned to a stated CPython
minor version).

**Pre-registered decision rule (fixed BEFORE any code exists; evaluated in this
order, REJECT FIRST; all band constants exact rationals).**

- **REJECT** ("a client-side age threshold cannot be made honest at the pinned
  cadence — the staleness leg needs a producer-side health signal, not a bigger
  number"): Feas = ∅ — no swept threshold holds false-stale to ≤ 1/200 without
  blowing the 240 s mean-detection band. Checked FIRST — the costly-error
  rationale: REJECT retires the contract's client-side framing outright, so the
  protect-against-stale-as-live arm cannot be shadowed by an eager APPROVE.
- **APPROVE** ("the contract's default is right-sized"): 180 ∈ Feas AND
  Feas ∩ {90, 120} = ∅ — the suggested 3-missed-cycles threshold is honest, and
  no ≤ 2-cycle threshold is (so the suggestion wastes at most one sub-cycle grid
  step of latency — 150 ∈ Feas does not defeat it; a full cheaper CYCLE would).
  Both conjuncts on Arm-A exact numbers; the seed-20261318 stability leg must
  reproduce the ruling.
- **NULL** (anything else — a legitimate, reportable outcome): the citable pin is
  the measured FALSESTALE/LAT curves and the named BINDING AXIS — pre-registered
  candidates: (i) **under-provisioned** — Feas ≠ ∅ but 180 ∉ Feas (at the pinned
  disturbances 3 missed cycles still cries wolf; the latency band caps the grid
  at 240, so the finding is "4 cycles, not 3" — the number is the finding);
  (ii) **over-provisioned** — some T ≤ 120 ∈ Feas (2 nominal cycles are already
  honest; the default buys nothing and costs a full cycle of detection latency —
  the measured margin is the finding); (iii) **arm disagreement** — the agreement
  gate fails (a model/implementation defect is the finding, no ruling issues);
  (iv) **sensitivity straddle** — a reporting-only sensitivity pair (jitter, f,
  c, burstiness) lands a primary conjunct on the opposite side of a band edge
  (the named axis is the finding; reporting legs CANNOT flip the decision).
  **Cheapest live probe, named:** once FLAG 1 goes live, log one day of real push
  timestamps from the relay (pins jitter AND the miss rate f — the two invented
  widths that matter) — zero new tooling, re-litigate the band with measured
  widths before anyone tunes the frontend constant.

**Band liveness (disclosed — the P034–P041 discipline).** No closed form is on
record for the composed budget, and the window arithmetic puts the decisive cells
genuinely near the band: a false stale flag needs the perceived age to outrun
T, and with one missed cycle (probability f·(1−f) ≈ 3.8%) the gap spans only
110–150 s — so at T = 180 a false flag needs TWO consecutive misses (probability
≈ 1/651) or one miss plus adverse skew, landing FALSESTALE(180) plausibly below
1/200, while at T = 120 the single-miss window plus skew bites directly and
plausibly lands above it; where T = 150 falls, and whether the second APPROVE
conjunct (nothing at ≤ 120 feasible) survives the f = 1/100 world, is exactly
what the exact enumeration decides. At the PRIMARY constants the genuinely
undecided fork is APPROVE vs both directional NULLs; REJECT is the protect arm,
reachable within the registered space if the rough window arithmetic above
underestimates the composed mass (that arithmetic is back-of-envelope — this
file deliberately pins NO expected landing) and directly live under the
loose-jitter/high-f sensitivity worlds, which is why it is checked first.

**What a reader DOES differently on the verdict.**

- **APPROVE** → the contract line drops its "default suggestion" hedge and gains a
  measured basis, routed lane-side per Q-0260 (this repo never edits mineverse
  files): "3 missed cycles ≈ 180 s" becomes "180 s (false-stale ≤ 1/200 of healthy
  loads, mean outage detection ≤ 240 s at the pinned model)", and the eventual
  FLAG-1 frontend badge ships that constant with a citable curve.
- **REJECT** → the client-side framing retires: the lane's contract v-next
  question becomes a producer-side health signal (a heartbeat field or relay-side
  freshness flag) instead of a bigger client threshold — named BEFORE anyone
  builds the badge on sand.
- **NULL** → the conditional finding ships with its named axis; the one-day
  push-timestamp log above is the pre-priced next step (and on
  over-provisioned, the lane learns 2 cycles suffice — a free minute of detection
  latency).

**Gates (run invalid on any failure).**

- **Hand fixture (pinned, verified at startup):** six scenarios with
  hand-computed outcomes:
  1. Gap leg: G = 60, c = 0, T = 180 → x = T − c = 180, (G − x)⁺ = 0.
  2. Gap leg: G = 200, c = +10, T = 180 → x = 170, (G − x)⁺ = 30.
  3. Latency leg: A = 40, c = −30, T = 90 → L = max(0, 90 − 40 + 30) = 80.
  4. Latency leg: A = 100, c = +30, T = 120 → 120 − 100 − 30 = −10 → L = 0
     (already showing stale at the halt).
  5. Indicator leg: A = 155, c = +30, T = 180 → perceived 185 > 180 → STALE.
  6. Indicator leg: A = 155, c = +20, T = 180 → perceived 175 ≤ 180 → LIVE
     (strict inequality pinned).
- **Zero-disturbance identity leg (Arm A, exact):** with I ≡ 60, f = 0, c ≡ 0:
  G ≡ 60, FALSESTALE(T) = 0 exactly for every grid T, the stationary age is
  uniform on {0..59}, and LAT(T) = T − 59/2 exactly — exact values, not
  tolerances.
- **Monotonicity (exact, both arms):** FALSESTALE non-increasing and LAT
  non-decreasing in T — a theorem under shared enumeration/common random numbers,
  so any violation is an implementation defect: hard gate.
- **Tail-closure spot-check (Arm A):** exact equality of the n ≤ 8 + analytic
  tail against a direct n ≤ 12 enumeration on the pinned sub-grid (above).
- **Arm agreement gate** (bounds above), **per-leg draw-count sentinels**, **twin
  independently-written decision evaluators**, **stdout + results.json
  byte-identical across two process runs**, **CPython minor pinned** — the
  P017–P044 standing battery.

**Reporting-only legs (Arm A exact where stated + seed-20261319 Arm-S
confirmations — CANNOT flip the decision):** the full FALSESTALE/LAT × T tables
with P(L > 300) rows; the sensitivity pairs (jitter {58..62} / {45..90};
f = 1/100 / 1/10; c ≡ {0} / {−120..+120}); the **burst leg** — failures as a
two-state Markov chain, P(fail → fail) = 1/2 and P(ok → fail) = 1/48 (stationary
miss rate exactly 1/25, matching the primary — deploy-window correlated outages;
Arm S only, disclosed: the geometric closed form does not apply, direction
stated: bursts lengthen gaps and push toward REJECT/NULL(i)); the on-demand
refresh note (the contract's "plus on-demand refreshes" only SHORTENS gaps, so
the modeled world overstates FALSESTALE — direction stated, conservative against
APPROVE's first conjunct). Aux seed 20261320 is reserved and never read by any
decision number.

**Grounding / hermeticity.** ZERO network reads at verdict time AND zero repo
reads — the entire world (the interval/failure/skew lattices with every
sensitivity pair, the T grid, band constants (1/200, 240, 300), the six-scenario
hand fixture, the burst-leg transition pair, horizon/sample counts, seeds
20261317–320) is constructed in-sim from the pinned constants in this file,
committed as a small fixture JSON alongside one stdlib file; the two harvested
contract sentences are quoted verbatim in the fixture with their `ae98dd0` pin
for citation only. Decision arithmetic exact `fractions.Fraction` at the
measurement points. Feasibility arithmetic: Arm A is eight convolutions of a
21-point lattice (support ≤ ~600) plus per-cell sums over 7 T × 61 c — well
under a second; Arm S is one ~80,000-attempt timeline plus 2 × 200,000 bisection
lookups × 7 thresholds — seconds in pure CPython. No dependencies.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the outbox (PROPOSALs 001–044): nothing prices a freshness/staleness
  indicator, an age-of-information process, or any client-side timing threshold.
  Nearest by MOVE FAMILY: PROPOSAL 025/029 (substrate-kit claim expiry / lease
  renewal, → V027 reject / V031 null) — also "a silence-keyed threshold balancing
  false firing against detection latency", but their world is session-renewed
  claim files at wake cadence with lane-death semantics; this head is a 60 s
  machine push relay read by clock-skewed browsers, renewal-reward viewer-time
  metrics, a different consumer (the mineverse frontend) and zero shared fixture —
  the same same-move-different-world distinction P041's Relations drew against
  P037. Nearest by SLOT MOVE: PROPOSAL 037 (review-queue N = 50) and P041 (spool
  margin) — the standing "price a doc's own unquantified decide-and-flag constant
  on its named failure axes" pattern. Nearest by SURFACE: PROPOSAL 013 (heartbeat
  contradiction linter) — heartbeat/staleness VOCABULARY only; that head is
  deterministic lint grammar, no stochastic threshold. P012 (routine cadence
  economics) prices wake-cadence cost/benefit, not detection. The tree-wide dedup
  sweep `rg -i -g '!bootstrap.py' -g '!.substrate' 'stale|staleness|generated_at|missed cycle|age.of.information|freshness'`
  at drafting HEAD `0cad099` returns, beyond coordination/status prose and the
  P025/P029 claim-expiry docs (relation drawn above): the 2026-07-10 captured
  checker/tag heads (`queue-slice-staleness-age`, `session-start-staleness-banner`,
  `harvest-freshness-checker`, `generated-artifact-freshness-umbrella`,
  `fleet-manifest-freshness-checker`, and kin — all DETERMINISTIC guard/banner/tag
  specs: detect-and-report drift, no stochastic threshold, no false-fire/latency
  pricing) and this section's own schema-shape heads — none prices a freshness
  threshold on its failure axes. No prior proposal, verdict
  (V001–V054 span checked via the sim-lab `sims/` tree at `692fcf1` + the
  outbox/inbox threads at HEAD; V055 in flight = P044's checkout-pooling world),
  idea file, or session-card 💡 touches it.
- Sibling heads in THIS section, deliberately distinct: the four 2026-07-11
  snapshot heads (`snapshot-field-parity-audit`, `snapshot-contract-shared-constant`,
  `mining-projection-single-source`, `shim-replay-determinism-harness`) are all
  SHAPE/schema/idempotency heads — none touches delivery TIMING; the contract's
  § Delivery expectations is the one leg of the READ contract no prior head
  priced.
- Runners-up this slice, weighed and dropped on merit: **mineverse
  founding-day groomed backlog** (re-read @ `ae98dd0` — unchanged from the
  `f79d0ae` state P041 already dismissed: UI/refactor/cosmetic or externally
  blocked, nothing sim-shaped); **the minigame section spec**
  (`docs/design/minigame-section-spec-2026-07-13.md` @ `ae98dd0` — inventory +
  categorical enable-semantics recommendations, no falsifiable quantitative
  claim, and its own §1 routes sim/balance questions elsewhere);
  **superbot-idle timed-events / theme-balance heads** (economy tuning is
  explicitly blocked on the queued IDLE SIM-001 verdict, and local ORDERs
  005/006 already queue nine idle/games SIM-REQUESTs — drafting there would
  crowd priority intake, ORDER 032). The stale-indicator threshold won on: both
  cadence constants already cited in the source contract, a crisp threshold rule
  with both failure axes named by the contract's own sentence, and a genuinely
  undecided landing.

## Model basis (declared model-dependence — the P024 discipline)

This verdict's numbers are CONDITIONAL on an embedded model, named up front:

- **(1) Statistical assumption:** independent uniform integer scheduler jitter
  (±5/+15 around the CITED 60 s target), i.i.d. Bernoulli missed cycles
  (f = 1/25), and uniform viewer clock offset (±30 s) — the widths are INVENTED
  where not cited (the two cited constants are the 60 s target cadence and the
  180 s suggestion itself), disclosed inline, each with a reporting-only
  sensitivity pair. NO live push timeline exists anywhere in the fleet (FLAG 1
  is unpicked — stage 1 serves a committed fixture whose `generated_at` is
  "honest about being a fixture", the contract's own words), so the sweeps
  bracket scale, not shape, and the named one-day timestamp-log probe measures
  jitter and f directly at zero new tooling.
- **(2) Single most-likely-to-flip alternative:** CORRELATED failures — deploys
  and relay outages kill several consecutive pushes, fattening the gap tail
  beyond the geometric model; the burst leg (Markov persistence 1/2 at the same
  stationary miss rate) brackets that direction reporting-only, and its
  direction is stated: burstiness raises FALSESTALE at every T, pushing toward
  REJECT/NULL(i) — so the i.i.d. primary is the assumption APPROVE leans on,
  named. Softer flips, named as out of the registered scope: the halt-while-503
  case (already honest by the lane's no-last-good-cache rule), on-demand
  refreshes (only shorten gaps — modeled world conservative against APPROVE's
  first conjunct), page-focus re-render timing (the indicator recomputes on
  render; a backgrounded tab's latency is a browser fact, not a threshold fact),
  and multi-guild relays.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe over a
> pinned public contract doc, sim is report-only evidence, no
> spend/publish/irreversible surface — README § probe battery). Verify-first ran
> FIRST, live this slice: (a) **source verified at HEAD** — superbot-mineverse
> shallow-cloned, HEAD `ae98dd094100f7b864f2c36b91494c8fb2cd1f31`
> ls-remote-confirmed; both harvested sentences quoted verbatim above from
> `docs/mining-data-contract.md` § Delivery expectations at that pin; the lane's
> own outbox/backlog re-read at the pin — no SIM-REQUEST exists there (nothing to
> duplicate) and the founding-day backlog is byte-unchanged from P041's dismissal.
> (b) **dedup** — the tree-wide sweep (Relations above); PROPOSALs 001–044 re-read
> at HEAD `0cad099` before drafting; the sim-lab `sims/` tree listed at `692fcf1`
> (verdicts through 054, V055 in flight on P044 — different world); the seven
> prior fleet-backlog occupants harvested six other repos. (c) **kill test NOT
> triggered** — no prior proposal, verdict, or 💡 prices a staleness indicator or
> age-of-information threshold. (d) **feasibility + liveness arithmetic checked**
> — runtime bounded in the preamble (sub-second Arm A, seconds Arm S, stdlib
> only); liveness disclosed in its own subsection with NO expected landing pinned.

**1. What is this really?** A pre-registered error-budget MEASUREMENT of the one
constant the READ contract's staleness sentence hangs on: the stale-indicator
threshold grid at the cited 60 s cadence, FALSESTALE and LAT as exact Fractions
from a seedless renewal-reward enumeration arm confirmed by a seeded timeline MC
arm, judged against bands fixed before any code (REJECT first: no honest
threshold exists; APPROVE: 180 honest AND ≤ 2 cycles not; NULL with four named
axes), byte-identical across two process runs.

**2. What is the possibility space?** (i) Don't run it — the round-8
fleet-backlogs slot goes unserved and the rotation's standing rule is dead letter
this cycle. (ii) Re-harvest an already-tapped repo — legal but weaker: seven
rounds have drawn six repos, and the one roster lane untapped by ANY proposal
carries a binding contract with a self-declared unpriced constant. (iii) A prose
answer ("3 cycles sounds right") — restates the contract's own hedge, measures
nothing, prices neither axis. (iv) Wait for live push logs — the RIGHT eventual
calibration but FLAG 1 is externally gated with no ETA; the sim prices the
decision NOW and its NULL branch names that exact log as the next step. (v) This
head: hermetic, exact-arithmetic, pre-registered — the pipeline's standing shape.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file + one fixture JSON yields: exact
FALSESTALE/LAT surfaces over 7 thresholds, the minimal-honest-threshold function
T\*, a ratify-or-move ruling on a binding contract's named default, a burst-leg
bracket on the correlated-outage direction, and a reusable pattern —
renewal-reward pricing of freshness-indicator thresholds — that transfers to any
fleet surface comparing a timestamp to "now" (the roster's staleness verdicts,
heartbeat freshness windows, harvest-pin staleness) WITHOUT this verdict claiming
any of those worlds.

**4. What breaks it? (assumptions made explicit)** (a) **The invented widths** —
jitter, f, and c carry no live datapoint (disclosed; sensitivity pairs bracket
scale; the one-day log probe measures the two that matter). (b) **Independence**
— the correlated-outage flip is named as most-likely-to-flip, direction stated,
burst leg brackets it. (c) **The clean-halt outage model** — a producer that
keeps pushing STALE CONTENT (fresh `generated_at`, dead upstream DB) defeats any
age-based indicator by construction; out of registered scope, named (that is a
producer-honesty question, not a threshold question). (d) **The pinned-world
boundary** — 60 s target worlds only; a re-cadenced contract re-runs the grid
with one fixture edit. None of these is hidden; all four are a sensitivity leg,
a named flip, or a stated scope bound.

**5. What does it unlock?** The contract's hedged constant becomes a number the
lane can commit (routed via the manager, Q-0260); the eventual FLAG-1 frontend
badge ships with a citable false-stale rate instead of a guess; REJECT would
redirect the lane to a producer-side health signal BEFORE the badge is built;
the fleet gains its first age-of-information verdict pattern; and the rotation
ledger gains its seventh distinct harvest repo — the first one that closes the
"untapped by any proposal" set.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external
at verdict time — fully hermetic by construction (the P017 precedent). The
harvest grounding is one pinned public repo read, already taken and quoted.
Cheapest kill BEFORE simming: a prior fleet verdict pricing freshness
thresholds (none found — V001–V054 swept via the sim-lab tree at `692fcf1`), or
a live push-timestamp log contradicting the pinned widths (none exists — FLAG 1
unpicked). Cheapest confirm AFTER a NULL: the named one-day timestamp log, zero
new tooling.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab builds and runs the sim (the Q-0264 pipeline's verify seat — this file
is its intake spec); superbot-mineverse consumes the verdict as a contract-doc
edit it makes itself on manager routing; this repo builds nothing. It displaces
nothing in flight (V055 is P044's checkout-pooling intake on a parallel claim —
different world entirely; local ORDERs 005/006 queue idle/games/venture
SIM-REQUESTs — none touches mineverse) and duplicates nothing (Relations dedup
above; the four sibling snapshot heads are schema-shape, not timing).

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one stdlib
Python file (both arms + gates + twin evaluators), one fixture JSON (every
pinned constant in this file, copied verbatim), one REPORT.md with the two
curves, the T\* row, the ruling, and the named-axis/probe line on NULL — the
standing INTAKE/VERDICT grammar, nothing else.

**Recommendation: sim-ready** — every constant pinned here, bands registered
REJECT-first before any code, seeds 20261317–320 above the verified high-water
20261316, fully hermetic at verdict time; the honest next step is the sim
itself.
