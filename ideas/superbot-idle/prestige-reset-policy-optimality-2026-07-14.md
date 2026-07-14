# Prestige reset-policy optimality — does the idle engine's own "optimal-play" greedy reset loop survive the milestone fold it now ships with?

> **State:** sim-ready
> **Class:** game-mechanics (pipeline rotation — the standing ORDER 003
> GAME-MECHANICS slot, round 11; round 11 opened at fleet backlogs with P057
> (#391) and served venture with P058 (#395), so game mechanics is next per
> ORDER 004 rule 3, confirmed against the slot's own spacing-4 history
> (P020, P023, P027, P031, P035, P039, P043, P047, P051, P055 → P059). The
> slot's five most recent draws were superbot ×2, mineverse, gba-homebrew ×2 —
> this slice rotates to the ONE World repo the slot has never drawn:
> superbot-idle.)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/superbot-idle/blob/5ddd5a230d4a6504c06b52805cba5dc8b3276b44/idle_engine/prestige.py@5ddd5a230d4a6504c06b52805cba5dc8b3276b44 · fetched 2026-07-14T05:14:16Z
> (FIRSTHAND pin: superbot-idle is public and clone-authorized for read per the
> Q-0272 standing rule (superbot `docs/fleet-reading-path.md` § 0, read
> FIRSTHAND @ `50481b7` via add_repo clone); read-only shallow clone re-pinned
> at drafting — `git fetch` at 2026-07-14T05:14:16Z confirmed origin/main
> still at `5ddd5a2`. Every constant, curve shape, and quoted sentence below
> is from that read. The sim itself is fully hermetic: zero repo/network reads
> at verdict time, every fixture constructed in-sim from the pinned constants
> in this file.)

**Origin:** drafted under the standing owner ORDER 003 (continuous pipeline)
and ORDER 004 rule 3's rotation — round 11 opened at the fleet-backlogs slot
(P057, #391) and served venture (P058, #395), so this slice serves the
GAME-MECHANICS slot. The harvested head: superbot-idle's prestige/reset
mechanic ships TWO committed optimality claims — `idle_engine/prestige.py`'s
module docstring, verbatim: *"doubling a run does not double the award, so
the optimal loop is reset-and-grow rather than one endless grind"* (same
claim in `docs/design/upgrades-prestige-v0.md`: *"the optimal loop is
reset-and-regrow, not one endless grind — the core prestige feel"*), and the
committed SIM-001 harness `tools/simulate.py::simulate_s3`, whose docstring
labels its policy *"S3 — optimal-play speedrun … Policy per second matches
S2's visit order: credit, greedy-buy, prestige iff eligible"*. Meanwhile the
lane's own heartbeat flags an unpriced degeneracy of exactly that policy,
verbatim (`control/status.md` @ `5ddd5a2`): *"optimal play reaches ~80,796
resets in 14 days (late resets ~13 s each) — uncovered by any criterion,
likely wants a pre-registered cap/cooldown criterion in v2 of the doc."* And
one committed fact makes the label freshly falsifiable: the achievements
slice extended the production fold to `base_rate * count * upgrade_pct *
prestige_pct * milestone_pct * theme_pct // 100_000_000`
(`idle_engine/engine.py`) with milestones that are *"Earned once, kept
forever"* meta-progression surviving resets (`idle_engine/achievements.py`),
and the lifetime-3 rung (10,000,000 run-lifetime, +5% forever) is a rung the
greedy loop can NEVER earn — greedy runs end at ~10⁵ lifetime — **while
`tools/simulate.py` folds zero milestones (`grep -c milestone` = 0)**. The
"optimal-play" label has never been evaluated in the fold the engine actually
ships. This head prices it: a pre-registered, fully deterministic policy-grid
sim at the SIM-PINNED constants, plus the flagged cap/cooldown priced as
policy arms. This head builds nothing in superbot-idle and never edits its
files (routing is the manager's per Q-0260).

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested mechanic, stated back.** A run produces `primary` at an
integer rate; the player may reset once run-lifetime ≥ 100,000, banking
`isqrt(lifetime // 100,000)` prestige units; each unit adds +10% to all
production forever. The achievements slice added persistent milestones (+5%
each, earned once, kept forever) on run-lifetime {10³, 10⁵, 10⁷}, prestige
units {1, 5, 25}, and generators owned {10, 100, 1000}. The engine's own
docstring and harness assert the greedy loop (reset the instant you are
eligible) is the optimal way to play. The falsifiable core: **over the
registered 14-day SIM-001 horizon, at the SIM-PINNED constants and the FULL
HEAD multiplier fold, is greedy prestige-iff-eligible actually the argmax of
a pinned policy family that includes patient and hybrid reset schedules —
and what fraction of optimal output does the lane's flagged reset-cadence
cap (a minimum-run-duration cooldown) cost?** Everything is exact integer
arithmetic on a deterministic engine: no estimate, no noise, every
comparison a big-int inequality.

**The model (fixed, fully pinned — every constant a decision of this file,
none left to the implementer; all arithmetic exact integers).**

- **World = the registered SIM-001 reference world at HEAD `5ddd5a2`,
  extended by the HEAD fold:** one generator `tier1` (base_rate 1, count
  FIXED at 1 — re-seeded `owned={tier1: 1}` after every reset, the harness's
  AMB-3), theme neutral (100), one upgrade `boost1` (base_cost 60·1 = 60,
  growth 115/100 exact, effect +25 additive, `cost(L) = 60·115^L // 100^L`
  per `idle_engine/upgrades.py` semantics), one prestige track (threshold
  100,000, divisor 100,000, bonus +10/unit), milestone ladders per
  `idle_engine/economy.py`: lifetime (1,000 / 100,000 / 10,000,000),
  prestige (1 / 5 / 25), owned (10 / 100 / 1,000 — structurally unreachable
  at count 1, asserted in-sim), +5% each once earned, persistent across
  resets. Rate, one floor per second (engine.py):
  `rate = (1 · 1 · (100+25L) · (100+10P) · ms_pct · 100) // 100_000_000`,
  `ms_pct = 100 + 5·(milestones earned)`.
- **Player micro-policy (the harness's own, pinned):** greedy
  buy-while-affordable, boundary order per the S3 docstring + the
  achievements runtime contract: credit → award milestones → buy while
  affordable → award milestones → reset check → award milestones. Between
  boundaries the rate is a constant integer, so exact event scheduling
  (jump `ceil(need/rate)` seconds) equals 1-second ticking — the harness's
  own documented equivalence.
- **Horizon H = 1,209,600 s (14 days)** — the registered SIM-001 horizon,
  inherited. H/2 = 604,800 s rides as a reporting leg.
- **Policy family Π (15 policies, pinned; the decision is within-Π and says
  so):** `never` (grind forever, no reset); `fixed-m` — reset when lifetime
  ≥ m·100,000, m ∈ {1, 2, 4, 9, 16, 25, 100} (m = 1 IS the committed greedy
  policy); `hybrid-k` — greedy, except ONE patient run to 100·100,000 = 10⁷
  (banking lifetime-3, award isqrt(100) = 10) triggered at the first reset
  boundary where P ≥ k, k ∈ {0, 100, 1000, 10000}, then greedy again;
  `cooldown-τ` — greedy but a reset is legal only once the run is ≥ τ
  seconds old, τ ∈ {60, 300, 3600} (the lane's flagged cap/cooldown
  criterion, priced).
- **Decision metric, one number per policy:** `total(π)` = cumulative
  `primary` PRODUCED over [0, H] (sum of all crediting, across all runs —
  spending never subtracts; the engine's own lifetime semantics summed
  across resets). Exact integer. Final P, reset count, milestone set, and
  the reset-time series ride as reporting columns.

**Two arms (both deterministic; the seeded legs are reporting-only).**

- **Arm A (decision arm — exact, seedless):** the 15-policy grid at H,
  every `total(π)` an exact integer, evaluated by exact event scheduling on
  a from-scratch reimplementation of the pinned fold (the sim never imports
  the lane's code — fully hermetic; the anchors below prove equivalence).
- **Arm B (twin — independently written):** a second, independently coded
  evaluator (per-second or event-driven, implementer's choice) must
  reproduce every Arm-A `total(π)` EXACTLY. Byte-identical `results.json` +
  stdout across two process runs; CPython minor version pinned in the
  report (drafting prototype ran on CPython 3.11).
- **Arm R (seeded, REPORTING-ONLY — can never flip the decision, no
  agreement gate rides it):** random-policy falsification probes bracketing
  the un-pinned policy space: N = 12 hybrid triggers k ~
  `random.Random(20261373).randrange(1, 60001)` and N = 6 cooldowns τ ~
  same stream `randrange(30, 7201)`, each simulated at H exactly as Π
  members; stability leg seed 20261374 (N = 4 + 2, same grammar); ordering/
  presentation leg seed 20261375 (table shuffle only); aux seed 20261376
  NEVER read by any leg (registered reserve — the P054–P058 aux
  convention). Every Arm-R policy's total must re-evaluate EXACTLY through
  Arm B (a deterministic reproducibility gate, not a statistical one). A
  random probe that beats the Π-best is a named finding in the report,
  never a ruling.

**Seeds (registered): 20261373 / 20261374 / 20261375 / 20261376** —
allocated strictly above the PROPOSAL 058 high-water **20261372**, re-swept
at drafting: boundary-aware regex `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over
this tree at HEAD `d90a06a` (bootstrap.py/.substrate excluded) and sim-lab
READ-ONLY at origin/main (results.json + compiled bytecode excluded) maxes
at genuine 20261372 in both (the larger standalone numerals
20261542/20261833/202670087 are Fraction-numerator and decimal-fraction
digit substrings in results.json-quoting outbox text — data, not seeds; the
P046–P058 sweep-recipe trap re-confirmed).

**Pre-registered decision rule (fixed BEFORE any code exists; evaluated in
this order: REJECT first, then the INVALID controls gate, then APPROVE,
then NULL). All comparisons exact big-int.**

- **REJECT** ("the committed 'optimal-play' label is FALSE at the fold the
  engine ships — the achievements slice silently created a patient-detour
  dominance the harness cannot see because it folds zero milestones; any
  reset-cadence cap or v2 pacing criterion registered against S3-greedy
  baselines would be priced against the WRONG optimum"): **∃ π ∈ Π \
  {fixed-1}: 100·total(π) ≥ 101·total(fixed-1)** — some pinned alternative
  beats the committed greedy policy by ≥ 1% at H, in Arm A, reproduced
  exactly by Arm B. Checked FIRST — the costly-error rationale: the lane's
  own heartbeat says it "likely wants a pre-registered cap/cooldown
  criterion in v2", and registering that criterion (or graduating any
  future pacing number) against a baseline mislabeled "optimal" bakes the
  mislabel into the next pre-registration; the cheap fix (re-baseline
  before registering) is only cheap BEFORE v2 exists.
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate
  failing (constants below).
- **APPROVE** ("both committed claims hold at the HEAD fold — greedy is
  ≥ 1%-dominant in Π and reset-play crushes the endless grind"):
  **∀ π ∈ Π \ {fixed-1}: 100·total(π) ≤ 99·total(fixed-1), AND
  total(fixed-1) ≥ 2·total(never).** Mutually exclusive with REJECT by
  arithmetic on the first clause.
- **NULL** (anything else — a legitimate, reportable outcome): pre-registered
  axes: (i) **parity-straddle** — the best alternative lands inside
  (99/100, 101/100) of greedy: the finding is the exact ratio table;
  (ii) **mechanism-miss** — REJECT's clause fires but the milestones-OFF
  contrast world (gate F3's world, reporting here) shows the same beater
  also beating with milestones OFF (the attribution to the milestone fold
  fails; the finding is WHICH mechanism binds); (iii)
  **horizon-conditional** — the H/2 reporting leg lands the promoted
  ruling's clause on the other side of its line at 7 days (named, never
  ruling); (iv) twin-arm disagreement surviving the INVALID diagnosis (a
  defect is the finding, no ruling).

**Expected landing, DISCLOSED (the P048–P058 closed-form-arm norm — the
drafting prototype ran this session; the sim re-derives everything from
scratch and must not trust these).** Full 14-day grid, exact integers:
never 24,767,541 · **fixed-1 (greedy) 25,386,048,335** (P = 174,619, resets
= 174,619, milestones earned 5 — lifetime-1/2 + prestige-1/2/3, never
lifetime-3) · fixed-2 2,308,530,416 · fixed-4 5,562,567,873 · fixed-9
1,189,091,761 · fixed-16 460,817,123 · fixed-25 250,843,290 · fixed-100
56,754,018 · hybrid-0 1,905,424,414 · hybrid-100 24,975,644,645 (0.9838) ·
**hybrid-1000 27,411,200,535 = 1.0798× greedy** (the beater: one 10⁷
patient run at P ≥ 1000 banks lifetime-3's permanent +5%, which compounds
over the remaining horizon; final P = 182,276 > greedy's 174,619) ·
hybrid-10000 26,870,606,289 (1.0585 — a SECOND cell above the line) ·
cooldown-60 15,237,507,974 (0.6002) · cooldown-300 5,758,125,849 (0.2268) ·
cooldown-3600 1,041,938,127 (0.0410). So the disclosed landing is
**REJECT**: 100·27,411,200,535 ≥ 101·25,386,048,335 holds with an ≈ 7.98%
margin against the 1% line (≈ 8× the registered edge, in EXACT arithmetic —
no noise exists to move it). The docstring's own grind claim is
simultaneously CONFIRMED and reported: greedy = 1024.97× never-reset, so
the REJECT is precise, not global ("reset-and-grow" beats grinding; the
committed SCHEDULE of resetting is what fails). Falsifiability is real and
disclosed: hybrid-100 lands BELOW parity (0.9838 — detouring too early
starves the compounding base) and hybrid-0 collapses (0.0751), so the
REJECT clause genuinely discriminates within the hybrid family itself;
milestones-OFF contrast: the same hybrid-1000 LOSES at 0.9789 when the fold
drops milestones — the beat is attributable to the milestone fold, i.e. to
exactly what `tools/simulate.py` omits; horizon check: at H/2 the beater
still clears the line (1.0375 ≥ 1.01) and hybrid-10000 degenerates to
ratio exactly 1 (P never reaches 10,000 by day 7 — the detour never fires),
both disclosed for the reporting leg.

**Gate power, computed at registration for a correct implementation (the
V065/V067 lesson, applied).** This sim is fully deterministic: the engine
fold is exact integer arithmetic, the policy grid is fixed, and the ONLY
seeded legs (Arm R) are reporting-only and carry NO statistical gate — the
sole gate that touches them is exact reproducibility through the twin
evaluator, which a correct implementation passes with probability 1. Every
F-gate below is an exact-integer identity, a structural assertion, or a
byte-comparison; none is stochastic. **Joint pass probability across all
gates for a correct implementation = 1, exactly** (the V038 precedent: a
NO-RNG world where determinism is proven by byte-identical re-run, not
estimated). Decision separation is likewise noise-free: the disclosed
REJECT margin is 7.98% against a 1% line in exact arithmetic — the ruling
cannot move unless the model itself is implemented differently, which the
anchor gates (F1/F2) catch as INVALID, not as a flipped verdict.

**Gates (any failure → INVALID; constants pinned).**

- **F1 — engine-fold identities:** `cost(L)` opens 60 / 69 / 79 (L = 0, 1,
  2 — exact, quoted by V038's B0); rate-by-level at P = 0, milestones off:
  [1, 1, 1, 1, 2, 2] for L = 0..5; the HEAD fold with neutral theme and
  zero milestones is integer-identical to the legacy `// 10_000` fold
  (engine.py's own documented identity); `isqrt(1) = 1` first-award
  identity (threshold = divisor).
- **F2 — V038 cross-pins (milestones-OFF greedy world):** first prestige at
  t = 12,573 s exactly, award 1; run durations 1–3 = 12,573 / 11,536 /
  10,475 exactly (V038 B0's hard anchors, reproduced by the drafting
  prototype); 14-day reset count = 80,795 under THIS file's pinned boundary
  order (hard for the sim), sitting inside the packet's own ±100 soft band
  around the V038-reported ~80,796 (the ±1 is a boundary-convention
  difference vs the vendored harness's AMB set, disclosed — both values in
  band; the three duration anchors are the exact cross-pins).
- **F3 — milestones-OFF contrast world (attribution control):** the full
  15-policy grid re-run with `ms_pct` pinned to 100; gate: `total(π)` for
  every π must be ≤ its milestones-ON value (adding permanent nonnegative
  bonuses cannot reduce production — exact monotonicity), and fixed-1 OFF
  must reproduce F2's anchors. The OFF-grid's ratio table is the
  mechanism-attribution report for NULL axis (ii).
- **F4 — conservation identities (every policy, every run):** balance +
  cumulative upgrade spend = run lifetime at every boundary; Σ run
  lifetimes (+ the open run's partial) = total(π); owned-milestone
  assertion: Σ owned = 1 at every boundary (the owned rungs never fire).
- **F5 — hand world:** H = 200 s, milestones on, fresh state: first
  purchase at t = 60 exactly (cost 60 at rate 1), second at t = 129 (cost
  69), balance at horizon = 71, lifetime = total = 200, L = 2, no milestone
  earned (lifetime-1 = 1,000 > 200) — every value hand-derivable from the
  constants above.
- **F6 — battery:** twin independently-written evaluators agree EXACTLY on
  every total (Arm A vs Arm B); Arm-R draw-count sentinel (exactly 12 + 6
  `randrange` calls on seed 20261373, 4 + 2 on 20261374, counted and
  asserted); aux seed 20261376 never read; stdout + results.json
  byte-identical across two process runs; CPython minor version pinned;
  the P017–P058 standing battery. Runtime budget, measured at drafting:
  the heaviest single policy (fixed-1 at H, ~175k resets, event-driven)
  runs ≈ 3 s on CPython 3.11; grid + contrast world + Arm R ≈ 2–4 min per
  process run — well inside the harness norm.

**Reporting-only legs (never decision-bearing):** (a) the **H/2 = 604,800 s
grid** (horizon-robustness of the promoted ruling — disclosed above); (b)
the **k-timing curve** (total vs k over the pinned hybrid grid + the Arm-R
random triggers — where the patient detour pays); (c) the **cooldown price
table** (τ → fraction of the Π-best's output — the lane's flagged cap,
priced: drafting values 60 s → 0.56, 300 s → 0.21, 3600 s → 0.038 of the
hybrid-1000 optimum); (d) the **reset-cadence series** for the Π-best and
for greedy (resets per day, late-game run duration — the "~13 s resets"
degeneracy quantified under both); (e) the **milestone timeline** per
policy (when each rung banks).

**What a reader DOES differently on the verdict** (all routing lane-side via
the manager per Q-0260 — this repo edits nothing in superbot-idle). A
pre-registered APPLICATION GUARD rides every branch, TWO conditions: (1)
the verdict conditions on the SIM-PINNED table {60, 115/100, 25, 100000,
100000, 10}, the milestone ladders {10³/10⁵/10⁷, 1/5/25, +5%}, and the HEAD
fold @ `5ddd5a2` — a retuned constant, a changed ladder, or a generator
purchase path landing (none exists at `5ddd5a2`; V038's premise, re-checked
at drafting) means re-run, not reuse; (2) it conditions on the SIM-001
reference world (count fixed 1, theme neutral) — a multi-generator world
re-opens the owned rungs and the question with them.

- **REJECT** → the manager gets a paste-ready structured choice,
  recommendation first (Q-0263.2): **(a, recommended — zero engine changes,
  one harness fix)** fold milestones into `tools/simulate.py` (the omission
  is the measured root cause) and re-baseline "optimal play" on the full
  fold BEFORE registering the v2 cap/cooldown criterion the heartbeat says
  it wants — the verdict ships the policy evaluator (~150-line stdlib) and
  the cooldown price table as the sizing input; **(b)** keep the S3 label,
  explicitly re-scoped as "optimal in the pre-milestone fold" (a doc-line
  fix, accepting the v2 criterion inherits the mislabeled baseline);
  **(c)** treat the patient-detour dominance as a design FEATURE to
  amplify (a deliberate "ascension run" mechanic — the hybrid curve says
  players who plan one big run get ~8% over pure spam) — an owner/lane
  intent call, never ruled by fiat here.
- **APPROVE** → both committed claims gain a measured basis at the HEAD
  fold; the cooldown price table still ships (the flagged v2 criterion gets
  its sizing input either way).
- **NULL** → the named axis ships with its exact table (parity, mechanism,
  or horizon — each a citable finding), plus the free probe: the policy
  evaluator runs on any future constant set at zero marginal cost.

## Relations (adjacent heads — deliberately links, not duplication)

- **V038 (SIM-001 economy feel, superbot-idle)** — the nearest neighbor and
  the deliberate seam: V038 measured pacing, feltness, and prestige-payoff
  LEVERS under the committed greedy policy in the pre-milestone fold (its
  own premise pin: `tools/simulate.py` @ `d992c568`, zero milestone
  folding), and its report flagged nothing about policy choice. This head
  holds every constant V038 graduated FIXED and varies the POLICY — the one
  axis V038's world could not see because its harness omits the milestone
  fold that creates the effect (measured: the beater's edge inverts to
  0.9789 with milestones off). Zero shared decision numbers; V038's B0
  anchors ride here as cross-pin gates (F2).
- **P015 → V017 (generator purchase path T10)** — prices a NOT-YET-BUILT
  mechanic's cost curve (generators); this head prices a SHIPPED mechanic's
  policy claim; the no-generator premise is shared and re-verified.
- **P006 → V006 (idle economy sim kernel)** — built the SIM-001 harness
  relay this head now audits the label of; provenance, not overlap.
- **P055 → V066 (mineverse badge saturation)** — crossing-TIME of a static
  display threshold against a faucet, different repo; its depends block
  explicitly scoped idle milestone registrations OUT ("inherit the
  crossing-time METHOD only"); this head is not a crossing-time question at
  all — it is a policy-optimality question.
- **P051 → V062 (chicken-farm faucet), P020/23/27 (casino envelopes), P031
  → V033 / P035 → V046 (superbot-games pacing/throttle), P039/P043 →
  V050/V054 (gba survival bands)** — the slot's prior worlds: faucet rates,
  odds envelopes, pacing bands; none prices a reset/prestige policy space.
- **The ORDER 005/006 queued idle asks are SERVED and distinct:** IDLE
  SIM-001 economy-feel → V038 (above); the generator purchase curve rides
  fm owner-queue E#52 fed by V017. Neither asks the policy question.
- The tree-wide dedup sweep `rg -i -g '!bootstrap.py' -g '!.substrate'
  'prestige|reset.?polic|cooldown|reset.?spam|optimal.?play'` at drafting
  HEAD `d90a06a` hits only the P006/P015 idle files (harness relay + cost
  curve, argued above), P055's scope-out line, and outbox stubs quoting
  them. No proposal P001–P058 and no sim-lab verdict V001–V069 (ledger read
  locally at sim-lab origin/main; V069 = P058's rubric world, zero overlap)
  prices a reset policy, a prestige schedule, or any policy-vs-policy
  comparison in any idle/game world — the pipeline's first
  policy-optimality head.
- Runners-up this slice, weighed and dropped on merit: **timed-events
  scoping** (superbot-idle outbox — explicitly "values unregistered pending
  SIM-002"; no committed constants to pin); **milestone feltness floor**
  (+5% floors to zero at low rates — real, but a corollary of V038's ASK-1
  inertness finding, too derivative); **superbot-games escort/exploration
  re-tunes** (V042–V045 just served those exact asks). The reset-policy
  head won on: two quotable committed claims, a lane-flagged unpriced
  degeneracy, a mechanism (the milestone fold) that measurably falsifies
  the label, and a fresh repo for the slot.

## Model basis (declared model-dependence — the P024 discipline)

- **(1) Statistical assumptions:** none — the world is deterministic and
  the decision is exact arithmetic. The MODELING assumptions are the pinned
  ones: the SIM-001 reference world (count 1, theme neutral), the harness's
  own greedy micro-policy inside every macro-policy, and the within-Π scope
  of the optimality ruling. The REJECT is sound regardless of Π's
  completeness (one beater falsifies the label); the APPROVE is explicitly
  within-Π and says so.
- **(2) Single most-likely-to-flip alternative:** the METRIC — total
  production over H vs final prestige count vs final rate. Direction
  disclosed at drafting: the beater also wins on final P (182,276 vs
  174,619) and the milestone set (6 vs 5), so the promoted ruling is
  metric-robust across the three natural readings; the full per-policy
  column set ships in results.json. Softer boundaries, named: the
  **horizon** (H/2 reporting leg — disclosed: the beat holds at 7 days);
  the **micro-policy** (a player who upgrades non-greedily is a different
  world, out of scope, stated); the **adaptive-policy ceiling** (Π contains
  no DP-optimal adaptive policy; Arm R brackets the neighborhood as
  reporting — a REJECT cannot be weakened by a better policy existing, only
  sharpened).

## Probe report (v0, 2026-07-14)

> Single-pass battery (panel not escalated: self-contained knowledge probe
> over pinned committed constants, sim is report-only evidence, no
> spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **source verified
> FIRSTHAND** — superbot-idle shallow clone re-pinned at drafting
> (`git fetch` 2026-07-14T05:14:16Z, origin/main = `5ddd5a2`); every
> constant re-read from `idle_engine/economy.py` at that SHA; the harness's
> zero-milestone omission verified by grep; the no-generator-path premise
> (V038's) re-verified. (b) **dedup** — the tree-wide
> prestige/reset-policy/cooldown sweep at HEAD `d90a06a` (Relations above);
> PROPOSALs 001–058 and VERDICTs 001–069 swept via the local sim-lab clone.
> (c) **kill test NOT triggered** — no prior head prices a reset policy.
> (d) **feasibility + liveness arithmetic checked** — the drafting
> prototype RAN this session: the full 15-policy grid, the milestones-OFF
> contrast, the H/2 leg, and the V038 anchor reproduction (12,573 / 11,536
> / 10,475 exact); heaviest policy ≈ 3 s, full run ≈ 2–4 min, CPython 3.11.

**1. What is this really?** A pre-registered, fully deterministic
policy-grid audit of the idle engine's committed "optimal-play" claim at
the multiplier fold the engine actually ships: 15 pinned reset policies
(greedy / patient / one-detour hybrids / the lane's own flagged cooldown
cap) evaluated to exact-integer 14-day totals, judged REJECT-first against
a 1% dominance line, with the V038 anchors as cross-pin gates and the
milestones-OFF world as the attribution control.

**2. What is the possibility space?** (i) Don't run it — the round-11 game
slot goes unserved and the lane registers its v2 cap criterion against a
baseline nobody has audited. (ii) Re-price constants (threshold, bonus,
divisor) — V038 already did the lever arms; duplicative. (iii) A prose
answer ("obviously greedy wins, isqrt punishes patience") — the drafting
grid shows that instinct is WRONG at the HEAD fold by 8%, which is exactly
why measuring beats intuiting. (iv) Price the cap alone (cooldown arms
only) — incomplete: a cap priced against a mislabeled optimum inherits the
mislabel. (v) This head: label + cap in one pinned grid, attribution
controlled.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file + one fixture JSON yields: the exact
15-policy total table (with the committed policy beaten by 7.98% at the
disclosed landing), the mechanism attribution (milestone fold on/off), the
cooldown price table the lane's v2 criterion needs, the k-timing curve for
a possible "ascension run" mechanic, and a transferable ~150-line exact
policy evaluator any future constant set can re-run for free.

**4. What breaks it? (assumptions made explicit)** (a) The reference-world
pin — count 1, theme neutral; a generator path or non-neutral theme
re-opens it (application guard condition 2). (b) Within-Π scope on APPROVE
— stated in the rule itself; the disclosed landing is REJECT, which one
beater establishes regardless. (c) The micro-policy pin — greedy buying
inside every macro-policy (the harness's own; a smarter buyer is a
different head). (d) Mechanism gates — every gate an exact identity;
anchors from V038's published B0 catch a mis-implemented fold as INVALID
before it can masquerade as a verdict (the V065 lesson: every registered
identity recomputed at drafting — 60/69/79, [1,1,1,1,2,2], 12,573/11,536/
10,475, the 200-second hand world — all verified this session).

**5. What does it unlock?** The lane's v2 pacing/cap criterion gets an
honest baseline and a sizing table before it is pre-registered (the
cheapest possible moment); the S3 "optimal-play" label either gains a
measured basis or a measured correction; the fleet gains the pipeline's
first policy-optimality verdict shape (constants held, player varied) —
reusable on any game lane with committed strategy claims (mineverse
badges, games escort routes, gba survival routes).

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external at verdict time — fully hermetic (the P017–P058 precedent); the
harvest grounding is one already-verified read-only clone pin (FIRSTHAND,
`5ddd5a2`). Cheapest kill BEFORE simming: a prior verdict on reset policy
(none — swept), or the V038 anchors failing to reproduce under this file's
pinned boundary order (they reproduce exactly, drafting-verified).
Cheapest confirm AFTER: re-run the evaluator with V038's recommended
lever (PRESTIGE_BONUS_PERCENT 10 → 25) — one constant, second worked
example, zero new machinery.

**7. Which lane should build it — and what does it displace or
duplicate?** sim-lab builds and runs the sim (the Q-0264 pipeline's verify
seat — this file is its intake spec); superbot-idle consumes the verdict
as the baseline for its flagged v2 cap criterion and the S3 label fix,
routed by the manager per Q-0260; this repo builds nothing. It displaces
nothing in flight (V069 holds P058's rubric world; no verdict session
holds an idle head) and duplicates nothing (Relations dedup; V038 is the
adjacent world, seam argued and gated).

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib Python file (both evaluators + Arm R + gates), one fixture JSON
(the constant table {60, 115/100, 25, 100000, 100000, 10}, the milestone
ladders, the fold formula, the policy family Π with its 15 parameter
tuples, H and H/2, the decision constants 101/100 and 99/100 and the 2×
grind line, the F1–F6 anchor values including the hand world and the V038
cross-pins, Arm-R draw counts {12+6, 4+2}, seeds 20261373–376, the quoted
docstring/status/harness sentences with the FIRSTHAND pin `5ddd5a2`), one
REPORT.md with the policy table, the attribution contrast, the cooldown
price table, the ruling, and the named-axis line on NULL — the standing
INTAKE/VERDICT grammar, nothing else.

**Recommendation: sim-ready** — every constant pinned here, bands
registered REJECT-first before any code, every registered identity
recomputed exactly at drafting (the V065 lesson), zero stochastic gates
(joint pass probability for a correct implementation = 1 exactly, stated
with its reasoning — the V067 lesson applied to a deterministic world),
seeds 20261373–376 above the verified high-water 20261372, fully hermetic
at verdict time; the honest next step is the sim itself.
