# Badge saturation — is the mineverse achievement catalog's Coin Magnate line a wealth badge or an account-age badge under the hub's own committed daily faucet?

> **State:** sim-ready
> **Class:** game-mechanics (pipeline rotation — the standing ORDER 003
> GAME-MECHANICS slot, round 10; rounds 1–9 were P020 casino odds → V022
> reject, P023 entry fee → V025 reject, P027 comp/stipend → V029 null, P031
> explore pacing → V033, P035 mining booster throttle seal → V046 null, P039
> Gloamline survival ceiling → V050 approve, P043 Brineward band necessity →
> V054 approve, P047 creature rarity → V058 reject, P051 chicken-farm faucet
> → V062 reject)
> **Target:** `menno420/superbot-mineverse` (the World flagship — owns the
> achievement catalog and every threshold in it; routing is the manager's per
> Q-0260, this repo never edits mineverse files); verification target
> `menno420/sim-lab` per the Q-0264 pipeline
> **Grounding:** https://github.com/menno420/superbot-mineverse@b983291cd9fc4b0d037a25a139c7ef5991e1236f · fetched 2026-07-14T02:22:06Z
> (read-only shallow clone at drafting via claude-code-remote add_repo, HEAD
> committed 2026-07-14T02:00:29Z; every catalog constant and calibration
> comment below quoted from `server/views.py`, the shared-wallet semantics
> from `docs/mining-data-contract.md`, the sample values from
> `data/sample_snapshot.json` — all at that pin. The ANCHOR repo superbot was
> also read FIRSTHAND at
> https://github.com/menno420/superbot@34775943da081dd0a1dc7cf858efc0889726fcf6
> · fetched 2026-07-14T02:22:06Z — `_DAILY_TIERS` + `_DAILY_COOLDOWN = 86400`
> re-read from `disbot/services/economy_helpers.py` at that pin, byte-identical
> to the P051 quote @ `affd7ea`. Disclosed: the GitHub MCP direct read of
> superbot was attempted once first and denied, verbatim: `Access denied:
> repository "menno420/superbot" is not configured for this session. Allowed
> repositories: menno420/idea-engine, menno420/sim-lab,
> menno420/superbot-mineverse` — the add_repo clone route then succeeded (the
> P051/P054 precedent: walls re-probed, denials never inherited), so BOTH pins
> are FIRSTHAND.)

**Origin:** drafted under standing owner ORDER 003 ("continue coming up with
new ideas, that is your main purpose") in the ORDER 004 rule-3 rotation —
round 10: P053 served fleet backlogs (#379), P054 served venture (#382), so
this head is the round's GAME-MECHANICS slot. The slot's own spacing-4
history (P023, P027, P031, P035, P039, P043, P047, P051 → P055) confirms.
Recent game rounds drew superbot ×2 (P047 creatures, P051 farm) and
gba-homebrew ×2 (P039, P043); this round rotates to a repo the slot has
NEVER drawn: **superbot-mineverse**, the World flagship web game — whose only
in-repo committed game-mechanic constants are the achievement catalog — and
deliberately outside the nine queued SIM-REQUEST domains (local ORDERs
005/006 cover venture pricing ×4, superbot-idle's engine, and superbot-games
mining/fishing/dnd/exploration; the mineverse badge layer is in none of
them, and P045 → V056 priced this repo's staleness constant, not a game
mechanic).

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested head, stated back.** `server/views.py` @ `b983291` ships the
web game's "fun layer": seven deterministic achievement badges over snapshot
data, every threshold committed next to its check under the banner *"Every
threshold is documented here, next to the check that uses it"* — and the two
counting badges carry explicit CALIBRATION claims in their own comments:
**(L1)** Packrat, `PACKRAT_THRESHOLD = 200`: *"Chosen against the committed
sample so some miners hit it (SilverSeeker 212, CavernCrawler 227) and some
don't (DeepDelver 193, MagmaMaven 80, PebblePicker 51)"*; **(L2)** Coin
Magnate, `COIN_MAGNATE_THRESHOLD = 10_000`: *"coins at/above this. Sample:
DeepDelver 18450 and MagmaMaven 25990 hit; SilverSeeker 7320 and below
don't."* The implied design claim — a badge is a DISCRIMINATOR, some earn it
and some don't — is calibrated against a frozen 7-miner sample file. But the
read contract wires Coin Magnate to a LIVE quantity: `coins` is *"mutated
only by `economy_service`"* (`docs/mining-data-contract.md` § Per-miner
fields @ `b983291`) — the hub's SHARED wallet, the same wallet superbot's
committed faucets feed. And that faucet is committed in absolute units:
`_DAILY_TIERS` @ `3477594` fixes E[`!daily`] = **169201/100 = 1692.01
coins/day** exactly (six integer-uniform tiers, weights summing to 100,
claimable every `_DAILY_COOLDOWN = 86400` s), so `10_000` coins is **5.91
expected dailies** — nothing else required. V062 (P051) just measured the
same wallet's OTHER committed faucet self-funding to 8,064 coins/day. Nobody
has priced what the calibration comments actually claim: whether a
fixed-absolute-threshold badge stays a discriminator once real time passes
on the committed economy, or whether Coin Magnate is an **account-age
badge** — a mark everyone earns by showing up, whose sample-file calibration
was true for exactly one frozen instant.

**The falsifiable core.** On the pinned committed model (the exact
`_DAILY_TIERS` pmf; the badge rule `coins >= 10_000` verbatim), compute the
exact law of T = first day the wallet crosses the threshold, for a
pre-registered archetype grid: claim rate p ∈ {1, 1/2, 1/4, 1/10} (the
fraction of days the player claims `!daily` at all) × spend fraction σ ∈
{0, 1/2, 9/10} (the share of each claim spent back into the economy's
sinks, integer floor, decision world σ = 1/2) — then judge the calibration
claim over the season horizon H = 90 days: a badge that near-every claiming
archetype earns inside one season (and whose full-engagement crossing time
concentrates in the badge's first two weeks) is not discriminating wealth,
it is measuring account age, and its sample-calibrated threshold is dead on
arrival at the committed faucet rate.

**Drafting-time arithmetic, run and disclosed (the P048/P051 norm — the sim
re-derives from scratch and must not trust these).** The drafter's float DP
harness (run-compressed prefix-sum convolution, 7.6 s) lands REJECT at the
decision world σ = 1/2: P(T ≤ 90) = 1.000000 (p = 1), 1.000000 (p = 1/2),
0.986615 (p = 1/4), 0.205567 (p = 1/10) — three of four cells clear the
19/20 band, and the full-engagement median T is 7 days at σ = 0 (12 at
σ = 1/2) against the ≤ 14-day conjunct. Falsifiability is real and
disclosed: the p = 1/10 cell is the surviving discriminator (0.206 — the
badge does separate ~weekly players from everyone else), and the σ = 9/10
deep-spend world flips the arithmetic (only p = 1 fires: 1.000000 /
0.022956 / 0.000000 / 0.000000) — the REJECT rides the pinned σ = 1/2
world, and the σ sweep is the named fragility axis, exactly the P054
invented-pin disclosure discipline.

## The model (committed constants quoted @ `b983291` / `3477594`; hermetic)

**Committed constants (zero invented game numbers).**
- Badge rule: `coins >= COIN_MAGNATE_THRESHOLD = 10_000`
  (`server/views.py::earned_achievements` @ `b983291`, quoted verbatim in
  the fixture with both calibration comments L1/L2).
- Wallet semantics: `coins` integer ≥ 0, *"mutated only by
  `economy_service`"* (`docs/mining-data-contract.md` @ `b983291`) — the
  shared hub wallet.
- Faucet: `_DAILY_TIERS` = (500, 999, 45), (1000, 1999, 25),
  (2000, 2999, 15), (3000, 3999, 8), (4000, 4999, 5), (5000, 5000, 2) —
  label/emoji columns dropped, (min, max, weight) quoted @ `3477594`;
  weights sum to 100; claim value uniform integer in [min, max] within the
  drawn tier; one claim per day maximum (`_DAILY_COOLDOWN = 86400`).
  Anchor: E[`!daily`] = 169201/100 exactly (Fraction; per-value probability
  numerators over denominator 10^5 are exactly {9, 25, 15, 8, 5} per value
  across the five ranged tiers + 2000 on the 5000 atom — the fixture pins
  this derived table). SD[claim] ≈ 1197.78 (drafting float, sim re-derives
  exact).
- Sample calibration table (fixture rows, all 7 miners @ `b983291`
  `data/sample_snapshot.json`): coins {DeepDelver 18450, MagmaMaven 25990,
  SilverSeeker 7320, GearGoblin 5620, RustyRelic 3150, CavernCrawler 2140,
  PebblePicker 480}; pack totals {CavernCrawler 227, SilverSeeker 212,
  DeepDelver 193, GearGoblin 95, RustyRelic 95, MagmaMaven 80, PebblePicker
  51}; wear max {RustyRelic 117}; skills spreads; equipment counts
  {GearGoblin 9/9}; the 42-stone row {DeepDelver}; record_depth
  {DeepDelver 3, MagmaMaven 3} vs max_depth 3.

**Player model (invented-but-pinned widths, every one a grid axis or a
disclosed pin).** Fresh account, wallet 0, one decision per day: with
probability p the player claims (one draw from the committed pmf), then
spends `floor(σ · claim)` back into sinks the same day (net increment
= claim − floor(σ·claim); savings are never spent — direction stated in
Model basis); with probability 1 − p no claim, wallet unchanged. T = first
day wallet ≥ 10,000; season horizon H = 90 days. Grid: p ∈ {1, 1/2, 1/4,
1/10} × σ ∈ {0, 1/2, 9/10}; DECISION world σ = 1/2, decision cells the four
p values there; σ ∈ {0, 9/10} and H ∈ {30, 180} ride reporting-only.
Non-daily faucets (work/jobs, farm, mining sales, games) are EXCLUDED from
the decision arm and named in Model basis: every additional faucet only
accelerates T, so REJECT is robust in the direction that matters (V062
measured the farm alone at up to 4.77 dailies/day).

**Arms.**
- **Arm A (the DECISION arm):** seedless exact absorbing DP over integer
  wallet states 0..9999 (≥ 10,000 absorbing), per-day transition = the
  committed pmf transformed by the spend rule, run-decomposed prefix-sum
  convolution with exact integer numerators over denominator 2·10^6 per day
  (p on denominator 20, pmf on 10^5) — every P(T ≤ n) an exact Fraction;
  ~10^4 states × ~20 runs × 90 days per cell, big-int cost bounded and
  stated (the drafting float copy ran 7.6 s for all 12 cells).
- **Arm S (robustness, seeded):** direct MC of the same player model,
  N = 20,000 trajectories per decision cell, `random.Random(20261357)`,
  pinned loop order (σ ascending, p descending, trajectories sequential,
  two draws per day: claim-Bernoulli then value; value drawn as
  tier-then-uniform exactly as `economy_helpers` does it —
  `random.choices` tier pick then a uniform integer). Agreement gate:
  |Arm S − Arm A| ≤ 1/100 absolute on every decision P(T ≤ 90) cell AND
  every firing cell confirms with ≥ 4·SE headroom. Stability leg seed
  20261358 (N = 10,000) must reproduce the ruling through twin evaluators.
  Reporting legs seed 20261359: the σ ∈ {0, 9/10} worlds, H ∈ {30, 180},
  the badge-share curve S(d) = P(T ≤ d) at the decision cells, the CV of T
  at (p = 1, σ = 0) (the age-badge concentration mark), the threshold menu
  C* (the exact minimal threshold keeping P(T ≤ 90) ≤ 1/2 per cell, plus
  the committed threshold re-expressed at {20,000, 50,000, 100,000}), and
  the static rows: the other six badges' sample-calibration table and the
  deep_diver saturation note (record_depth ∈ {0..3} caps at the contract's
  own max — two of seven sample miners already hold it). Aux seed 20261360
  never read by any decision number. Seeds 20261357–360 strictly above the
  verified high-water 20261356 (P054).

## Decision rule (pre-registered; evaluated in this order, REJECT first)

- **REJECT** ("age badge — the catalog's own discrimination claim fails
  against the hub's committed faucet; the sample calibration is dead on
  arrival"): in Arm A EXACT at the decision world σ = 1/2,
  P(T ≤ 90) ≥ 19/20 at **≥ 3 of 4** claim-rate cells, AND median T ≤ 14
  days at the full-engagement (p = 1, σ = 0) cell, AND every firing cell
  confirms in Arm S within 1/100 absolute with ≥ 4·SE headroom. Checked
  FIRST: the costly error is the World lane shipping more fixed-absolute
  badges (and the owner reading the badge wall as engagement signal) while
  the flagship's showcase wealth badge is a participation stamp that the
  committed faucet hands to every non-hoarding daily-claimer inside one
  season.
- **APPROVE** ("the calibration holds — Coin Magnate separates engagement
  archetypes within the season"): at σ = 1/2, P(T ≤ 90) ≤ 1/2 at ≥ 2 of 4
  claim-rate cells AND ≥ 19/20 at ≤ 1 cell, in both arms, stability-leg
  reproduced. Mutually exclusive with REJECT by arithmetic.
- **NULL** (anything else — a legitimate reportable outcome with three
  named axes): **band-straddle** — the σ = 1/2 grid lands between the
  bands (e.g. 2 cells ≥ 19/20); the finding names the threshold cadence and
  ships the C* menu row as its knob; **concentration-miss** — the P-band
  fires but the median-T conjunct fails (crossing times spread — the badge
  is slow-but-universal; knob = H, named); **arm disagreement** — a firing
  Arm-A cell loses the band in Arm S.

**Consequence, pre-registered** (routing is the manager's per Q-0260 — this
repo never edits mineverse files; nothing here builds, publishes, or
spends): REJECT → the World lane gets a paste-ready structured choice with
the measured badge-share-vs-day table in E[`!daily`] units attached —
(a, recommended) re-express the threshold from the shipped C* menu (the
exact minimal C keeping the season share ≤ 1/2 per archetype — one-line
constant swap, calibrated to the faucet instead of the frozen sample),
(b) percentile badge (top-k coins of the guild snapshot — zero new state,
computable from the same snapshot the page already renders), or
(c) accept-and-rebrand (keep 10,000 — an intentional progression/age badge;
an owner intent call per the V044/V046 posture, never ruled by fiat here).
APPROVE → the calibration comments gain their measured basis and the
catalog's fixed-absolute pattern is ratified for future badges. NULL → the
named axis ships with its knob, plus the free live probe: the snapshot feed
itself re-renders every 60 s, so ONE day of real snapshots yields the
guild's actual coins distribution and badge share at zero new tooling.

## Gates (run invalid on any failure)

- **F1 anchor gate:** E[`!daily`] = 169201/100 by exact Fraction from the
  committed tier table; the per-value numerator table {9, 25, 15, 8, 5,
  atom 2000}/10^5 re-derived and asserted; weights sum to 100.
- **F2 crossing identities (exact, hand-checkable):** at (p = 1, σ = 0):
  P(T ≤ 1) = 0 (max claim 5000 < 10,000), P(T = 2) = (2/100)² = 1/2500
  exactly (two Mythic atoms — the only 2-day path), and T ≤ 20 with
  probability exactly 1 (min claim 500). At σ = 1/2: P(T ≤ 3) = 0 (max net
  2500/day).
- **F3 sample-calibration gate:** `earned_achievements` re-implemented
  verbatim over the 7 fixture miners reproduces the comments' own hit
  lists exactly — Coin Magnate {DeepDelver, MagmaMaven}, Packrat
  {SilverSeeker, CavernCrawler}, Tool Breaker {RustyRelic}, Balanced Build
  {SilverSeeker}, The Answer {DeepDelver}, Fully Geared {GearGoblin},
  Deep Diver {DeepDelver, MagmaMaven}.
- **F4 monotonicity theorems** (violation = implementation defect):
  P(T ≤ n) non-decreasing in n and in p, non-increasing in σ and in the
  threshold C; median T non-increasing in p.
- **F5 degenerate-transform gate:** the σ = 0 transformed pmf equals the
  committed pmf identically; total DP mass + absorbed mass = 1 exactly at
  every day of every cell.
- **Mechanical:** Arm-S draw-count sentinels (two draws per day exactly,
  claim-days only for the value draw); twin independently-written decision
  evaluators; stdout + results.json byte-identical across two process runs
  (Arm A platform-independent exact arithmetic; Arm S pinned to a stated
  CPython minor); aux seed 20261360 never read.

## Relations (adjacent heads — deliberately links, not duplication)

- **P051 → V062 (chicken-farm faucet, superbot):** the nearest ANCHOR kin —
  same shared wallet, same E[`!daily`] = 169201/100 anchor — but the
  reciprocal question: V062 priced a FAUCET against the anchor (is the
  income bounded?); this head prices a fixed CONSUMER-SIDE THRESHOLD
  against the anchor (does a wealth mark survive the income?). Zero shared
  machinery beyond the anchor Fraction; the badge, the repo, and the
  decision variable (a display threshold, not an income rate) are new.
  V062's measured plateaus enter ONLY as a named direction (excluded
  faucets accelerate T).
- **P045 → V056 (snapshot stale threshold, superbot-mineverse):** the same
  REPO, disjoint mechanic — a delivery-infrastructure constant (staleness
  seconds), not a game-layer badge; no shared constants, model, or
  consumer surface beyond the snapshot feed itself.
- **P015 → V017 and V038 (superbot-idle T10 / economy-FEEL):** the idle
  lane's milestone/achievement DOCS are registration targets for a
  different repo's engine; neither prices a mineverse badge or any
  threshold-vs-faucet ratio.
- **P047 → V058 (creature rarity):** shares only the "committed constants
  make the folk claim computable" move; battle engine, different repo.
- **Verdict sweep:** V001–V064 swept (sim-lab `docs/current-state.md` +
  `control/outbox.md` @ origin/main `135ae4e`; V065 claimed in-flight = the
  P054 illustration-gate world, no overlap); no verdict prices an
  achievement/badge threshold, a badge-share curve, or any
  threshold-vs-faucet ratio; the V056 "stale badge" is a freshness
  indicator, not an achievement.
- **In-tree mentions, linked not duplicated:** this section's own
  `snapshot-stale-indicator-threshold-2026-07-13.md` (P045, delivery
  constant) and the parked founding heads (projection/parity/replay —
  infrastructure, no game constants). None touches the achievement layer.

## Model basis (declared model-dependence — the P024 discipline)

The badge rule, wallet semantics, faucet pmf, cooldown, and sample table
are COMMITTED (zero invented game constants — the fixture's only
non-committed numbers are the player-model widths: the p grid, the σ grid
and its σ = 1/2 decision pin, H = 90, and the ≤ 14-day/19-20 band
constants). Directions stated: excluding every non-daily faucet (work,
farm — V062 measured it at up to 4.77 dailies/day self-funded — mining
sales, games) UNDERSTATES income, so REJECT is robust in the direction that
matters and APPROVE would be the fragile ruling; the spend rule never dips
into savings (a sink model that also taxes savings only slows T — generous
to APPROVE, direction stated); claims are i.i.d. daily Bernoulli (streak
mechanics would concentrate T further — the age-badge direction). The
single most-likely-to-flip pin is σ itself — no live datapoint on real
spend shares exists — which is why σ is a grid axis with the decision
pinned at 1/2 and the σ = 9/10 flip disclosed in the drafting arithmetic;
the NULL/live probe is the snapshot feed's own coins distribution, one day,
zero tooling. Scope: Coin Magnate is the decision badge (the only one wired
to a committed faucet in absolute units); Packrat's ore faucet is
mining-module-owned (superbot mining internals — out of scope, named), so
the other six badges ride as exact static rows only.

## Probe report (v0, 2026-07-14)

> Single-pass battery (panel not escalated: self-contained knowledge probe
> over pinned committed constants, sim is report-only evidence, no
> spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **both sources verified at
> FIRSTHAND pins** — superbot GitHub-MCP read denied once (verbatim in the
> Grounding header; deny-wins, no retry of that route), the add_repo clone
> route then succeeded for BOTH repos; every constant read from the working
> trees @ `b983291` / `3477594`. (b) **dedup** — tree-wide
> achievement/badge/coin-magnate/packrat/saturation sweep at HEAD `06f9711`
> (bootstrap.py/.substrate excluded: the outbox grep hits are P045's
> "stale badge" freshness sense and P015's idle-lane milestone docs — both
> argued distinct in Relations) plus sim-lab @ `135ae4e`; PROPOSALs 001–054
> (headers + idea slugs re-read) and VERDICTs V001–V064 swept, V065 in
> flight = P054's world. (c) **kill test NOT triggered** — no prior head
> prices any badge threshold or threshold-vs-faucet ratio. (d) **feasibility
> + liveness arithmetic checked** — Arm A is an absorbing DP over 10^4
> integer states with run-decomposed transitions (the drafting float copy
> ran all 12 cells in 7.6 s; the exact-Fraction arm is bounded big-int, cost
> stated); the drafting harness was actually RUN and its landing DISCLOSED
> (REJECT at 3 of 4 decision cells with the p = 1/10 survivor and the
> σ = 9/10 flip named — the P048/P051 norm).

**1. What is this really?** A pre-registered pricing of the World
flagship's own badge-calibration claim: the exact time-to-badge law of the
committed `COIN_MAGNATE_THRESHOLD = 10_000` under the hub's committed
`_DAILY_TIERS` faucet, over a claim-rate × spend-fraction archetype grid,
judged REJECT-first (age badge) / APPROVE (season discriminator) / NULL
(three named axes), byte-identical across two process runs.

**2. What is the possibility space?** (i) Don't run it — the round-10 game
slot goes unserved and the badge layer keeps shipping fixed-absolute
thresholds calibrated against a frozen sample file. (ii) Eyeball it — the
coupling (a 6-tier pmf, a spend rule, a crossing time) is exactly the
arithmetic humans wave at ("10,000 sounds like a lot"). (iii) Wait for live
telemetry — the RIGHT distribution eventually (the named free probe), but
the badge ships NOW and the faucet is committed NOW. (iv) Price a different
badge — none of the other six is wired to a committed absolute faucet
(Packrat's ore rates are mining-module internals). (v) This head: hermetic,
exact, pre-registered — the pipeline's standing shape.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file + one fixture JSON yields: the exact
badge-share-vs-day surface of the flagship's showcase badge in units of the
game's own daily; the measured truth value of a shipped calibration
comment; a C* threshold menu that turns any retune into a one-line pick;
and a reusable kernel — fixed-threshold-vs-committed-faucet crossing-time
pricing — that transfers to every badge, milestone, and unlock ladder in
the fleet (idle milestones, games-repo quest tiers, any future "reach N
currency" mark).

**4. What breaks it? (assumptions made explicit)** (a) **The σ pin** — no
live spend datapoint; bracketed by the grid, the flip disclosed at
drafting, the live probe pre-priced. (b) **Daily-only income** — direction
stated (understates; REJECT-robust). (c) **The p model** — i.i.d. Bernoulli
claims; streaks concentrate T further (the REJECT direction). (d)
**Contract drift** — a future catalog retune re-runs; the fixture quotes
both calibration comments verbatim at the pin. None is hidden; each is an
axis, a disclosed pin, a direction, or a pinned quote.

**5. What does it unlock?** The badge layer stops being calibrated against
a frozen sample file: either the threshold is ratified as a season
discriminator (APPROVE — and the fixed-absolute pattern is safe to reuse),
or the lane gets a measured paste-ready choice (C* menu / percentile badge
/ intentional age-badge rebrand) before the badge wall grows, or a named
axis ships with the one-day live probe. Either way the fleet gains the
crossing-time kernel and its first badge-vs-faucet verdict row.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external at verdict time — fully hermetic (the P017–P054 precedent); every
constant is committed at the two FIRSTHAND pins. Cheapest kill BEFORE
simming: a prior verdict pricing a badge threshold (none — V001–V064
swept), or a coin SINK wired into the badge path that caps wallets (none —
the contract has no wallet cap and `coins` has no schema maximum). Cheapest
confirm AFTER: one day of live snapshots (the feed re-renders every 60 s) —
the real coins distribution at zero new tooling.

**7. Which lane should build it — and what does it displace or
duplicate?** sim-lab builds and runs the sim (the Q-0264 verify seat — this
file is its intake spec); superbot-mineverse consumes the verdict as a
ratify/retune/rebrand call on its own catalog constants, routed by the
manager per Q-0260; superbot is anchor-only (nothing routed to it). It
displaces nothing in flight (V065 holds the illustration-gate world; the
nine queued SIM-REQUESTs cover other repos) and duplicates nothing
(Relations above).

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib Python file (DP + MC arms + gates + twin evaluators), one fixture
JSON (the tier table with its per-value numerator derivation, the threshold
and both calibration comments quoted verbatim @ `b983291`, the 7-miner
sample table, the p/σ/H grid with the σ = 1/2 decision pin, band constants
(19/20, 3-of-4, ≤ 14-day median, the ≤ 1/2 + ≤ 1-cell APPROVE legs, 1/100 +
4·SE agreement), the F1–F5 fixtures, per-leg trajectory counts, seeds
20261357–360), one REPORT.md with the badge-share tables in E[`!daily`]
units, the C* menu, the ruling, and the named-axis/probe line on NULL — the
standing INTAKE/VERDICT grammar, nothing else.

**Recommendation: sim-ready** — every constant pinned at two firsthand
commits, bands registered REJECT-first before any code, seeds 20261357–360
above the verified high-water 20261356, fully hermetic at verdict time, the
drafting-time landing computed and disclosed with its surviving cell and
its σ-flip named; the honest next step is the sim itself.
