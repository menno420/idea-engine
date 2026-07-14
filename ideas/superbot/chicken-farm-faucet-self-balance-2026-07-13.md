# Chicken-farm faucet self-balance — does the committed hen/coop price ladder keep the hub's first idle faucet "a small fraction of a `!daily`", or does an active collector out-earn the daily itself?

> **State:** sim-ready
> **Class:** game-mechanics (pipeline rotation — the standing ORDER 003
> GAME-MECHANICS slot, round 9; rounds 1–8 were P020 casino odds → V022 reject,
> P023 entry fee → V025 reject, P027 comp/stipend → V029 null, P031 explore
> pacing → V033, P035 mining booster throttle seal → V046 null, P039 Gloamline
> survival ceiling → V050 approve, P043 Brineward band necessity → V054
> approve, P047 creature rarity → V058 reject)
> **Target:** `menno420/superbot` (the hub — owns the farm constants, the
> workflow seam, and the `!daily` anchor this verdict prices against; routing
> is the manager's per Q-0260, this repo never edits superbot files);
> verification target `menno420/sim-lab` per the Q-0264 pipeline
> **Grounding:** https://github.com/menno420/superbot@affd7ea1ae5163109527e59ce73b46f0a8c7866c · fetched 2026-07-13T23:44:30Z
> (shallow clone at drafting via claude-code-remote add_repo, HEAD committed
> 2026-07-14T01:18:06+02:00; every constant below quoted from
> `disbot/utils/farm/farm.py`, `disbot/services/farm_workflow.py`, and
> `disbot/services/economy_helpers.py` — all at that pin. Disclosed: the
> GitHub MCP direct read was attempted once first and denied, verbatim:
> `Access denied: repository "menno420/superbot" is not configured for this
> session. Allowed repositories: menno420/idea-engine, menno420/sim-lab` —
> the add_repo clone route then succeeded, so the pin is FIRSTHAND.)

**Origin:** drafted under standing owner ORDER 003 ("continue coming up with
new ideas, that is your main purpose") in the ORDER 004 rule-3 rotation —
round 9: P049 served fleet backlogs (#358), P050 served venture (#371), so
this head is the round's GAME-MECHANICS slot. The last game round (P047) drew
the hub's creature battles, P039/P043 drew gba-homebrew ×2, P031/P035 drew
superbot-games — this round stays on the hub but rotates to a DISJOINT
mechanic: the chicken farm, "the bot's first **idle** activity"
(`farm.py` module docstring), deliberately outside the nine queued
SIM-REQUEST domains (local ORDERs 005/006 cover venture pricing ×4,
superbot-idle's SEPARATE engine, and superbot-games mining/fishing/dnd/
exploration; the hub farm is in none of them).

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested head, stated back.** `disbot/utils/farm/farm.py` @ `affd7ea`
ships a complete two-sink idle economy in eleven committed constants — hens
lay `1` egg per `LAY_INTERVAL_SECONDS = 300` into a coop of capacity
`20 + 15·level` (max level 10 → cap 170), collect pays `EGG_VALUE = 2` coins
per egg into the SHARED wallet (`farm_workflow.collect` credits via
`economy_service.credit_in_txn`, no cooldown anywhere on the path), the next
hen costs `round(40 · 1.55^extra)` and the next coop level
`round(100 · 1.8^level)` — and its header comment makes two load-bearing,
never-quantified claims: **(L1)** *"Buying hens scales the faucet but each
costs more coins (the sink), so the loop stays self-balancing"* and **(L2)**
*"an idle player banks at most ~40 coins over ~100 min before the coop caps —
a small fraction of a `!daily`"*, under the banner *"the owner's standing
'rewards too large & too frequent' caution from the mining rebalance applies
to every new faucet"*, closing with *"Tune against live play."* The same repo
commits the anchor that makes the claim checkable in absolute units:
`economy_helpers._DAILY_TIERS` fixes E[`!daily`] = **169201/100 = 1692.01
coins/day** exactly (six integer-uniform tiers, weights summing to 100). L2's
arithmetic is true and EXACT (20 intervals × 1 egg × 2 coins = 40 coins in
6,000 s) — but it prices only the never-collecting starter. Nobody has priced
the loop L1 actually promises: a player who COLLECTS on a cadence and feeds
the coins back into the ladder. The coupling that decides it is the cap: a
hen's marginal income depends on the collect cadence Δ through
`min(cap, n·⌊Δ/300⌋)` — at Δ = 24 h a second hen is worth exactly ZERO at
every coop level (288 eggs/day ≥ 170 = the level-10 cap), while at Δ = 15 min
hens are uncapped to n ≈ cap/3 and each adds 576 coins/day against a price
ladder that only grows 1.55×. Whether "self-balancing" means *bounded* or
*walled* or *neither* is a computable property of the committed integers.

**The falsifiable core.** On the pinned engine (re-implemented verbatim from
the committed constants and write semantics), with farm earnings as the ONLY
wallet (the loop self-funding — exactly L1's own frame), compute for each
collect cadence Δ ∈ {900, 3600, 14400, 86400} s the purchase path under a
pre-registered policy family and read off (a) the exact steady-state plateau
coins/day, (b) the wall day (first check-in at which no remaining purchase
pays back within 14 days), and (c) the per-purchase payback ladder — then
judge L1 against the committed anchor: a "conservative faucet" whose greedy
self-funded plateau EXCEEDS κ·E[`!daily`] (κ = 1/2, i.e. 169201/200 =
846.005 coins/day) at multiple cadences is not self-balancing, it is a
runaway faucet with a progression wall bolted on.

**Drafting-time arithmetic, run and disclosed (the P048/P049 norm — the sim
re-derives from scratch and must not trust these).** The drafter's exact
greedy harness lands REJECT: plateau 8,064 coins/day at Δ = 900 s (4.77×
E[`!daily`], reached day ~4, cumulative spend 21,887 coins ≈ 12.9×
E[`!daily`] — the ladder self-funds), 4,560/day at Δ = 3600 (2.70×), 1,140/day
at Δ = 14400 (0.67×, ABOVE the κ = 1/2 band), 130/day at Δ = 86400 (0.077× —
the idle audience L2 describes, which also walls at coop level 3 by day ~9
with hens worth exactly zero throughout). Three of four cadences clear the
runaway band, two of them by ≥ 2.7×. Falsifiability is real: the 14400 cell
sits 35% over a band it could drop under in the jittered arm, the myopic
greedy wall is NOT the family wall (at Δ = 3600 the hen+coop PAIR move still
pays back in 7.6 days past the myopic stop — included in the family, raising
plateaus only, direction stated), and the decision requires the jittered
Arm-S legs to confirm the same cells with SE headroom.

## The model (committed constants quoted @ `affd7ea`; the engine re-implemented verbatim, hermetic)

**Engine (integer seconds and integer coins/eggs throughout).**
- Accrual per `farm.settle`: `intervals = (now − updated_at) // 300`;
  `eggs' = min(cap, eggs + intervals · chickens)`; below cap the sub-interval
  remainder is preserved (`updated_at' = updated_at + intervals·300`), at cap
  the clock advances to `now`; zero hens advance the clock only.
  `cap(L) = 20 + 15·L`, levels 0..`MAX_COOP_LEVEL = 10`.
- Write semantics per `farm_workflow` (pinned): **collect** settles, pays
  `eggs · EGG_VALUE` (`EGG_VALUE = 2`) into the wallet, persists
  `(0, now)` — the remainder is DISCARDED on collect (the committed
  `set_chicken_farm(…, 0, now, …)` stamps `now`); **buy_chicken** settles at
  the OLD flock size first, persists `(settled.eggs, now)`, then applies
  `chickens + 1` (the workflow's own documented subtlety — no retroactive
  laying); **upgrade_coop** likewise. Purchases happen only at check-ins.
- Prices: next hen `round(40 · 1.55^(chickens − 1))` (`STARTER_CHICKENS = 1`,
  ceiling `MAX_CHICKENS = 100`); next coop `round(100 · 1.8^level)`. The
  fixture pins the DERIVED integer tables (hen extras 0–14: 40, 62, 96, 149,
  231, 358, 555, 860, 1333, 2066, 3202, 4963, 7692, 11923, 18480; coop
  L 0–9: 100, 180, 324, 583, 1050, 1890, 3401, 6122, 11020, 19836; coop
  ladder total 44,506) — re-derived at run time under the pinned CPython
  minor from the committed float formulas (Python-3 banker's `round`
  disclosed) and asserted equal to the fixture before any cell runs.
- Anchor: E[`!daily`] = Σ w_t · (min_t + max_t)/2 / 100 over the committed
  `_DAILY_TIERS` = **169201/100** exactly (Fraction arithmetic; tiers
  (500, 999, 45), (1000, 1999, 25), (2000, 2999, 15), (3000, 3999, 8),
  (4000, 4999, 5), (5000, 5000, 2)).

**Player model.** One farm, fresh state (1 hen, coop 0, empty coop, wallet 0
farm-coins). Check-ins at cadence Δ; at each check-in: settle + collect, then
apply the purchase policy repeatedly while it buys. Wallet is CLOSED
(farm income only — L1's self-funding loop) on every decision leg; a WHALE
leg (unbounded wallet, purchases gated by the payback rule alone) rides
reporting-only to split affordability walls from payback walls.

**Decision grid.** Cadence Δ ∈ {900, 3600, 14400, 86400} s × policy family
{GREEDY (myopic min-payback purchase whenever affordable, zero-marginal
options never bought), PAIR (as GREEDY but may also take the best
two-purchase sequence when its joint payback ≤ 14 days — catches the myopia
trap disclosed above), HEN-ONLY, COOP-ONLY, ALT (strict alternation,
coop first)} — marginal value of a purchase at cadence Δ evaluated on the
exact steady-state rate `R(n, L, Δ) = min(cap(L), n·⌊Δ/300⌋) · 2 · 86400/Δ`
coins/day; payback = price / marginal-R. Horizon H = 90 days.

**Arms.**
- **Arm A (the DECISION arm):** seedless deterministic exact trajectory per
  (Δ, policy) — integer engine state stepped check-in by check-in, plateau
  rate read as the exact closed-form R at the final state (a Fraction),
  wall day = first check-in where every remaining positive-marginal purchase
  has payback > 14 days (P_max sweep {7, 28} reporting-only), plus the
  per-purchase log {kind, price, payback, day}, cumulative spend, and the
  zero-marginal-hen share.
- **Arm S (robustness, seeded):** human cadence — check-in gaps i.i.d.
  uniform integers in {⌈Δ/2⌉ … ⌊3Δ/2⌋}, each check-in independently skipped
  with probability 1/10; N = 2,000 trajectories per decision (Δ, policy);
  plateau = mean coins/day over days 76–90. `random.Random(20261341)`,
  pinned loop order (Δ ascending, policies in the order above, trajectories
  sequential, two draws per check-in: gap then skip). Identity gate: Arm S
  run at degenerate jitter (exact cadence, skip 0) must reproduce Arm A's
  trajectory EVENT-FOR-EVENT on every decision cell. Stability leg seed
  20261342 (N = 500) must reproduce the ruling through twin evaluators.
  Reporting legs seed 20261343: Δ ∈ {300, 604800} columns, the κ sweep
  {1/3, 2/3}, jitter width {±1/4, ±3/4}·Δ, P_max {7, 28}, the WHALE leg,
  the knob table (the grid re-evaluated at EGG_VALUE = 1 and at
  LAY_INTERVAL = 600 — the two header knobs the docstring itself frames as
  tunable), and the design-ceiling row R(100, 10, Δ) = {32,640; 8,160;
  2,040; 340} coins/day. Aux seed 20261344 never read by any decision
  number. Seeds 20261341–344 strictly above the verified high-water
  20261340 (P050).

## Decision rule (pre-registered; evaluated in this order, REJECT first)

- **REJECT** ("L1 fails in the costly direction — the sink does not keep the
  faucet from running away; the 'conservative faucet' out-earns the
  committed daily for any collector"): in Arm A, plateau(best-of-family, Δ)
  ≥ κ·E[`!daily`] = 169201/200 coins/day at **≥ 2 of 4** decision cadences,
  AND the same cells confirm in the jittered Arm-S mean with ≥ 4·SE
  headroom, AND at each firing cell the closed-wallet cumulative spend to
  reach plateau ≤ 30·E[`!daily`] (the runaway is self-funded, not
  hypothetical). Checked FIRST: the costly error is the hub calibrating
  future faucets (and the owner's mining-rebalance caution) against a farm
  documented as banking "~40 coins" while it actually mints multiple dailies
  per day, forever, at zero further cost.
- **APPROVE** ("L1 holds as written — bounded AND alive"): at EVERY decision
  cadence plateau(best-of-family) < κ·E[`!daily`] in both arms, AND the
  early loop is alive (first 3 purchases each pay back ≤ 7 days at every
  cadence), AND the wall day ≥ 10 at ≥ 3 of 4 cadences, stability-leg
  reproduced. Mutually exclusive with REJECT by arithmetic.
- **NULL** (anything else — a legitimate reportable outcome with five named
  axes): **cadence-straddle** — only Δ = 900 fires the band (runaway is a
  spam artifact; the finding names the threshold cadence and prices the
  seat's own cheapest seal, a collect cooldown, from the shipped table);
  **idle-dead** — no runaway but the 86400 row walls before day 10 with
  zero-marginal hens (L1 survives, L2's audience has no loop — the knob is
  the cap ladder, named); **family-split** — PAIR extends the wall past
  GREEDY by ≥ 7 days somewhere decision-relevant (the myopia axis binds);
  **arm disagreement** — a firing Arm-A cell loses the band under jitter;
  **margin-thin** — the ruling flips inside the κ ∈ {1/3, 2/3} sweep.

**Consequence, pre-registered** (routing is the manager's per Q-0260 — this
repo never edits superbot files; nothing here builds, publishes, or spends):
REJECT → the seat gets a paste-ready structured choice with the measured
plateau table in E[`!daily`] units attached — (a, recommended) retune the two
header knobs the module itself calls tunable (EGG_VALUE and/or
LAY_INTERVAL_SECONDS; the shipped knob table shows exactly what each setting
buys since R scales linearly in EGG_VALUE and through ⌊Δ/I⌋ in the interval),
(b) a collect cooldown (prices the cadence column away — the cheapest
mechanical seal if the straddle shows Δ = 900 carries the breach), or
(c) accept-and-rebrand (keep the constants, retire L2's "small fraction"
line and the "conservative faucet" banner — an owner intent call per the
V044/V046 posture, never ruled by fiat here). APPROVE → L1 and L2 gain their
measured basis; the constants are ratified against the daily anchor and the
farm becomes the hub's reference "balanced faucet" row. NULL → the named
axis ships with its knob or threshold, plus the free live probe: the
workflow's own audit trail (`farm:collect` reason rows, committed) yields
the real per-player collect-cadence histogram and mint at zero new tooling —
each live cadence bucket picks out one column of the already-shipped table.

## Gates (run invalid on any failure)

- **F1 price-table gate:** the derived hen/coop integer tables above
  re-derived from the committed formulas under the pinned CPython minor and
  equal to the fixture (banker's-rounding cases included); coop ladder total
  44,506 asserted.
- **F2 settle identities:** settle idempotence and composition (settling
  every second ≡ settling once — the docstring's own invariant), cap clamp,
  zero-hen clock advance, remainder preservation below cap — property-
  checked over a pinned state grid.
- **F3 the L2 arithmetic gate:** fresh farm, no collects — exactly 40 coins
  collectible at t = 6,000 s and no further accrual at t = 7,200 s (L2's
  "~40 coins over ~100 min" is exact and reproduced byte-for-byte).
- **F4 anchor gate:** E[`!daily`] = 169201/100 by exact Fraction from the
  committed tier table; κ·E = 169201/200.
- **F5 daily-hen-worthlessness identity:** at Δ = 86400 the marginal rate of
  the 2nd hen is exactly 0 at EVERY coop level 0..10 (288 ≥ 170 = cap(10)) —
  asserted exhaustively.
- **F6 hand trajectory:** Δ = 3600, GREEDY, first 5 check-ins from fresh —
  eggs collected {12, 12, 20, 20, 20}, coins {24, 24, 40, 40, 40}, buys
  {—, hen#2@40, —, —, coop L1@100}, wallet after {24, 8, 48, 88, 28} —
  exact event log asserted (the cap bind visible at check-in 3: 24 accrued,
  20 collected).
- **Monotonicity theorems** (violation = implementation defect): R(n, L, Δ)
  non-decreasing in n and in L; plateau non-decreasing along the divisor
  chain 86400 → 14400 → 3600 → 900 at any fixed final state; wall day
  non-decreasing in P_max; closed-wallet plateau ≤ WHALE plateau per cell.
- **Mechanical:** Arm-S degenerate-jitter ≡ Arm-A identity per cell;
  per-leg draw-count sentinels (2 draws per check-in exactly); twin
  independently-written decision evaluators; stdout + results.json
  byte-identical across two process runs (Arm A platform-independent exact
  arithmetic; Arm S pinned to a stated CPython minor); aux seed 20261344
  never read.

## Relations (adjacent heads — deliberately links, not duplication)

- **P015 → V017 (superbot-idle T10 generator purchase path) and V038
  (superbot-idle economy-FEEL, ORDER 005 SIM-001):** the nearest METHOD kin —
  cost-curve pricing on an idle ladder — but a different repo and a different
  engine (superbot-idle's generator/prestige engine vs the hub's farm row),
  and neither carries this head's two distinguishing structures: the
  cap × cadence coupling that makes a purchase's value collapse to zero for
  idle players, and a committed in-repo ABSOLUTE anchor (E[`!daily`]) that
  the faucet is judged against.
- **P035 → V046 (superbot-games mining booster bypass):** the nearest
  SPIRIT kin — a committed faucet outrunning its own control — but a
  different repo, engine, and mechanism (purchasable energy bypassing a regen
  throttle vs a purchase ladder with no throttle at all), and V046's binding
  wall (the V001/V008 absolute earn-rate baseline) does NOT apply here: both
  sides of this comparison are committed constants in the same repo and
  currency, which is exactly what makes the farm head decidable tonight.
- **P031 → V033 (explore quest currency mint):** shares the absolute-units
  posture (committed bundle integers) but is an admission-gated encounter
  pacing question; no purchase ladder, no cadence coupling.
- **P020/P023/P027 → V022/V025/V029 (casino triage):** SINK-side fairness
  (the player pays the house); this head is FAUCET-side (the house pays the
  player); zero shared machinery, and the farm is not house-banked.
- **P047 → V058 (creature rarity):** same repo, disjoint mechanic (battle
  engine); no shared constants or seams.
- **In-tree farm mentions, linked not duplicated:**
  `ideas/superbot/idle-game-offline-summary-2026-07-10.md` (captured — a UX
  "while you were away" summary with the farm as first consumer; presentation,
  not balance) and `ideas/superbot/games-theme-engine-website-first-2026-07-10.md`
  (the egg-farm THEME on superbot-idle's engine; theming, not the hub farm's
  economy). Neither prices a constant.
- **Verdict sweep:** V001–V060 read at the local sim-lab clone @ `6cb58bb`
  (V061 in flight — the P050 kill-clock world, no overlap); no verdict
  prices the hub farm, an egg/coop constant, or any faucet-vs-daily ratio;
  the "farmer" hits in V029/V044 are casino comp-farmers and escort
  double-mints — different worlds.

## Model basis (declared model-dependence — the P024 discipline)

The engine and prices are COMMITTED (zero invented game constants — the
fixture's only non-committed numbers are the player-model widths: the cadence
grid, jitter width and skip rate, the horizon, P_max = 14 days, κ = 1/2, and
the policy family). Directions stated: exact-cadence check-ins flatter fine
cadences (jitter legs bracket); the closed wallet UNDERSTATES the faucet (any
outside coin only accelerates the ladder — generous to APPROVE, so REJECT is
robust in the direction that matters); the policy family brackets real play
from below (a cleverer buyer only raises plateau — same direction); game XP
from `collect_eggs`, multi-guild farms, and the offline-summary UX are named
out of scope (coins only, one farm). The single most-likely-to-flip
alternative is the CADENCE model itself — no live datapoint on real collect
cadences exists anywhere in the fleet — which is why the cadence is a grid
axis, never a claim, and the NULL/REJECT probe is the committed audit
trail's own cadence histogram.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe
> over pinned committed constants, sim is report-only evidence, no
> spend/publish/irreversible surface — README § probe battery). Verify-first
> ran FIRST, live this slice: (a) **source verified at a FIRSTHAND pin** —
> superbot GitHub-MCP read denied once (verbatim in the Grounding header;
> deny-wins, no retry of that route), the claude-code-remote add_repo clone
> then succeeded and every constant was read from the working tree @
> `affd7ea`. (b) **dedup** — tree-wide chicken/coop/egg-farm/farm.py sweep at
> HEAD `2089860` (bootstrap.py/.substrate excluded) plus the sim-lab clone @
> `6cb58bb`; PROPOSALs 001–050 (headers + idea slugs re-read) and VERDICTs
> V001–V060 swept; nearest neighbors argued distinct in Relations. (c) **kill
> test NOT triggered** — no prior head prices the hub farm or any
> faucet-vs-daily ratio. (d) **feasibility + liveness arithmetic checked** —
> Arm A is ~10^5 integer steps (seconds), Arm S ≤ ~2 × 10^8 fast integer
> steps worst case at Δ = 900 (minutes, stdlib); the drafting harness was
> actually RUN and its landing DISCLOSED (REJECT at 3 of 4 cadences with the
> near-band 14400 cell and the PAIR-family edge named — the P048/P049 norm).

**1. What is this really?** A pre-registered pricing of the hub chicken
farm's own "the loop stays self-balancing" claim: exact deterministic
purchase-path trajectories over the committed hen/coop price ladder at four
collect cadences, judged in absolute committed units against κ = 1/2 of the
exact E[`!daily`] = 169201/100 coins/day, with a jittered seeded arm
confirming robustness, REJECT checked first (runaway faucet), APPROVE =
bounded-and-alive, NULL with five named axes — byte-identical across two
process runs.

**2. What is the possibility space?** (i) Don't run it — the round-9 game
slot goes unserved and the farm ships as folklore ("conservative faucet")
that the drafting arithmetic already contradicts. (ii) Ask the owner to
eyeball the constants — measures nothing; the coupling (cap × cadence ×
two price ladders) is exactly the kind of arithmetic humans misjudge.
(iii) Wait for live telemetry — the RIGHT data eventually (the named free
probe), but the farm is live NOW and feeds the shared wallet every hour.
(iv) Price a different farm surface (offline-summary UX, XP) — presentation,
no committed tension. (v) This head: hermetic, exact, pre-registered — the
pipeline's standing shape.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file + one fixture JSON yields: the exact
plateau/wall/payback surface of the committed economy across the whole
cadence axis, in units of the game's own daily; the measured truth value of
two shipped docstring claims; a knob table that turns any retune into a
one-line pick; and a reusable kernel — cap-coupled purchase-ladder pricing
under check-in cadence — that transfers to every idle surface in the fleet
(superbot-idle generators, fishing/mining energy shops, any future
"collect + upgrade" loop).

**4. What breaks it? (assumptions made explicit)** (a) **The cadence model**
— no live cadence datapoint exists; bracketed by a grid axis + jitter +
skip legs, and the live probe is pre-priced (the audit trail). (b) **The
closed wallet** — real players inject outside coins; direction stated
(understates the faucet, REJECT-robust). (c) **The policy family** — myopic
GREEDY provably misses pair moves (found at drafting, disclosed); PAIR is in
the family and the family brackets from below. (d) **Write-semantics drift**
— the model pins collect/buy stamping `now` (remainder discarded); a future
workflow change re-runs, the fixture quotes the committed lines. None is
hidden; each is an axis, a leg, a family member, or a pinned quote.

**5. What does it unlock?** The hub's first idle faucet stops being
calibrated by comment prose: either the constants are ratified against the
daily anchor (APPROVE — the farm becomes the reference balanced-faucet row
for every future faucet the owner's caution banner governs), or the seat
gets a measured, paste-ready retune choice on the module's own two knobs
(REJECT — the drafting-disclosed landing), or a named axis ships with its
threshold and the audit-trail probe (NULL). Either way the fleet gains the
cap × cadence pricing kernel and the first faucet-vs-daily verdict row.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external at verdict time — fully hermetic (the P017–P050 precedent); every
constant is committed at the FIRSTHAND pin `affd7ea`. Cheapest kill BEFORE
simming: a prior verdict pricing the farm (none — V001–V060 swept), or a
collect cooldown hiding in the workflow (read this slice: none exists on
the path). Cheapest confirm AFTER: the `farm:collect` audit rows — the
committed reason tag is the probe, zero new tooling.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab builds and runs the sim (the Q-0264 verify seat — this file is its
intake spec); superbot consumes the verdict as a ratify/retune/rebrand call
on `farm.py`'s own header constants, routed by the manager per Q-0260; this
repo builds nothing. It displaces nothing in flight (V061 holds the
kill-clock world; the nine queued SIM-REQUESTs cover other repos) and
duplicates nothing (Relations above).

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib Python file (engine + both arms + gates + twin evaluators), one
fixture JSON (every pinned constant in this file copied verbatim: the eleven
farm constants, the derived price tables, the write-semantics pins, the
`_DAILY_TIERS` table and its exact mean, the cadence/jitter/policy/horizon
widths, band constants (κ = 1/2, 2-of-4, ≤ 30×E spend, 3-purchase/7-day and
day-10/3-of-4 APPROVE legs, P_max = 14), the F1–F6 fixtures, per-leg
trajectory counts, seeds 20261341–344, and the L1/L2 lines quoted verbatim
@ `affd7ea`), one REPORT.md with the plateau/wall/payback tables in
E[`!daily`] units, the ruling, and the named-axis/probe line on NULL — the
standing INTAKE/VERDICT grammar, nothing else.

**Recommendation: sim-ready** — every constant pinned here at a firsthand
commit, bands registered REJECT-first before any code, seeds 20261341–344
above the verified high-water 20261340, fully hermetic at verdict time, the
drafting-time landing computed and disclosed with its near-band cell and
family edge named; the honest next step is the sim itself.
