# The stale-ink mirror — Wickroad's "bet on your own stale information" is a rigged coin: under the committed 12-day triangle law, week-old ink is exactly inverted, 12-day ink is exactly fresh, and two mornings decode a town forever

> **State:** sim-ready
> **Class:** game-mechanics (pipeline rotation — the standing ORDER 003
> GAME-MECHANICS slot, round 13; round 13 opened at fleet backlogs with P065
> (#428) and served venture with P066 (#429), so game mechanics is next per
> ORDER 004 rule 3, confirmed by the slot's own spacing history (P020, P023,
> P027, P031, P035, P039, P043, P047, P051, P055, P059, P063 → P067); source
> rotation inside the slot per the P063 record — gba-homebrew ×2 (r6/r7),
> superbot ×2 (r8/r9), superbot-mineverse (r10), superbot-idle (r11),
> superbot-games (r12) — returns round 13 to **gba-homebrew**, undrawn since
> round 7 (P043), with pokemon-mod-lab excluded DARK/private per the
> standing Q-0260 rule-3 carve-out.)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline;
> the deliverable is a committed stdlib sim + a citable measured verdict — no
> lane build)
> **Grounding:** https://github.com/menno420/gba-homebrew@c0c688210bcb3db0004102e6c5b899943533f816 · fetched 2026-07-15T06:02:44Z
> (FIRSTHAND pin, public shallow clone read this session — the P039/P043/P063
> precedent; every Wickroad sentence and constant below was read directly at
> this pin, HEAD = "wickroad: growth cut 3 — the road itself (v0.4) (#144)".
> The sim itself is fully hermetic: zero repo/network reads at verdict time,
> every fixture constructed in-sim from the pinned constants in this file.)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous
pipeline) and ORDER 004 rule 3's rotation — round 13's third slot. The
harvested item is **Wickroad** (breadth game #11, `games/wickroad/`, v0.4
merged the morning of this harvest), whose committed concept doc and source
commit BOTH horns of an unpriced tension in the same tree:

- **The hook (CONCEPT.md § Pitch, verbatim):** "prices are only visible in
  the town you are standing in — everywhere else you see what you wrote down
  the last time you were there, stamped with how many days old the ink is.
  You navigate an economy you remember, not one you see; **every trip is a
  bet on your own stale information**." The § Sellability guess doubles
  down: "the **aging-ledger read is a genuinely ownable twist** worth
  testing."
- **The law (src/main.cpp, verbatim):** "Prices are a CLOSED FORM of (day,
  impact): price = clamp(base + tri12(day + phase) * step + impact), where
  tri12 is a triangle wave over a **12-day period**" — and the world is
  fixed: "The SAME world every run: the PRNG restarts at the fixed seed
  [0x5749434B] and is consumed only here, in a fixed order."

A bet needs an unpredictable outcome. A 12-day integer triangle wave is not
unpredictable — it is a clock. The committed law hands the committed hook
three exact structure theorems that decide what "stale" ink actually is, and
none of them is "a bet": ink of age 12 is a **photograph** (exactly current),
ink of age 6 is a **mirror** (every remembered deviation from a town's
normal price is exactly inverted — and the shipped 5-town line's longest
natural round trip, EMBERTON↔THORNBY, is exactly 6 days), and **two
consecutive mornings** in any town identify its (base, phase) pair exactly,
turning the rest of the run — and, at a fixed world seed, every future run —
into an open book. The lane's own witness infrastructure already knows half
of this ("the harness pins frames where **the ledger provably lies**",
CONCEPT.md § provable headlessly); what is unpriced is that at the map's own
natural revisit lags the ledger doesn't just sometimes lie — it lies
deterministically, in a direction and by an amount a player can compute, or
exploit, or be silently farmed by.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The folk belief** (the concept's own reading): an aging ledger creates a
genuine information asymmetry — old ink means risk, so every trip prices a
gamble on how far the market has drifted since you last saw it, and reading
ink ages well is the game's ownable skill.

**The mechanism:** information decay is a property of the (memory, process)
PAIR, not of memory alone. Against a mean-reverting or randomly-driven
price, old ink degrades gracefully and staleness is genuine risk. Against a
**deterministic periodic** price, ink does not decay — it ROTATES. The error
of age-`a` ink under the committed law is `|tri12(m+a) − tri12(m)| · step`,
which is itself a triangle in the lag: zero at a = 12 (T1), maximal and
exactly sign-inverting at a = 6 (T2, from the identity tri12(m+6) =
−tri12(m)), and — because the twelve consecutive-value pairs (tri12(m),
tri12(m+1)) are pairwise distinct — fully decodable from two dated
consecutive observations (T3). The ledger the game ships stamps every entry
with its ink age, so the player holds exactly the data T1–T3 need. Three
consequences, each exactly computable in the shipped world:

1. **The mirror band.** At revisit lags 5–7 every remembered nonzero
   deviation inverts (measured at drafting on the committed world, clamps
   included: I(5) = 240/240, I(6) = 300/300, I(7) = 240/240 — the census
   below). The map is a 5-town line; natural pendulum round trips are 2·d ∈
   {2, 4, 6, 8} days, so the flagship long route 0↔3 sits DEAD CENTER in the
   certain-inversion band: a player who trusts week-old ink is not taking a
   bet, they are being farmed — the town remembered as cheap is dear by
   exactly the amount that made it memorable.
2. **The photograph cadence.** A 12-day circuit (or any revisit at lag 12)
   makes every ledger word exactly current (T1) — "stale" ink at the right
   cadence carries zero risk, which is the opposite of "every trip is a
   bet."
3. **The two-morning decode.** Standing in a town for two consecutive dawns
   uniquely identifies that town's (base, phase) for every good whose
   readings don't clamp (T3) — after which the player navigates an economy
   they SEE, everywhere, for the rest of the run. And since the world seed
   is fixed ('WICK', committed), the decode survives across runs: for a
   returning player the information asymmetry is zero by construction. The
   in-run decode is the GENEROUS reading of the hook; the across-run fact
   deletes it entirely.

**What stays genuinely open (why this needs a sim, not just the theorems):**
whether the mirror/decode structure actually moves OUTCOMES in the shipped
game — the clamp bands (53/600 impact-free cells clamp at drafting) could
have broken the inversion census; market impact and the three authored decks
(rumors/contracts/hazards, all public-by-announcement) perturb the pure law;
and the value-of-information gradient needs a planner-controlled
measurement: does a law-inferring player actually collapse the gap to a
full oracle inside one 30-day run, and does an ink-trusting player actually
underperform? Drafting says yes on the shipped world (the numbers below) —
but the drafting scaffold showed the inference-collapse clause is
world-dependent (9/20 alternative worlds under the same greedy scaffold),
which is exactly the kind of knife-edge a pre-registered sim must pin
honestly rather than a drafter assert.

## Pinned model (measured at gba-homebrew c0c6882, then pinned as clean constants — all integers, exact arithmetic)

World (all from `games/wickroad/src/main.cpp`):

- 5 towns on a line (EMBERTON, GLASSMERE, SALTCOMBE, THORNBY, DUNWICK) ×
  4 goods (TALLOW, SALT, IRON, RESIN); `price_lo` = {6, 10, 22, 14},
  `price_hi` = {26, 34, 60, 44}, `drift_step` = {1, 2, 3, 2},
  `produce_gap` = {6, 8, 12, 10}.
- `tri12(m) = (m mod 12) ≤ 6 ? (m mod 12) − 3 : 9 − (m mod 12)` — the value
  track over one period is (−3, −2, −1, 0, 1, 2, 3, 2, 1, 0, −1, −2).
- `price(t, g, day) = clamp(base[t][g] + tri12(day + phase[t][g]) ·
  drift_step[g] + impact[t][g] + shock(t, g, day), price_lo[g],
  price_hi[g])`.
- World init: one xorshift32 (s ^= s<<13; s ^= s>>17; s ^= s<<5, 32-bit) at
  seed 0x5749434B, consumed in a fixed order — 20 base draws
  `base[t][g] = (lo[g]+hi[g])/2 − 3 + range(7)`, then 20 phase draws
  `range(12)`, then the produce/crave rotation `base[t][t mod 4] −=
  gap[t mod 4]; base[t][(t+2) mod 4] += gap[(t+2) mod 4]`. Resulting
  committed tables (drafting-computed, the F1 anchor; the sim re-derives):
  base = [[7,21,51,32],[17,16,43,39],[19,22,26,30],[19,33,43,19],
  [9,25,54,29]], phase = [[4,1,9,11],[0,8,11,4],[1,2,8,2],[8,6,3,11],
  [11,10,6,11]].
- Verbs: BUY one unit at price (impact +1 after, cap +9), SELL one unit at
  price − 1 (impact −1 after, cap −9), TRAVEL ±1 town (toll 2, a dawn),
  WAIT (lodging 1, a dawn). Impact decays 1 toward 0 everywhere at every
  dawn. Pack 8, start gold 60, target 300, pass closes at dawn 31. The
  ledger: standing in a town at a dawn writes ALL four of its prices in
  dated ink (`refresh_ledger`); other towns' ink ages.
- Decks (all fixed, authored, public by announcement lines): rumors
  {(announce 2, hit 5, GLASSMERE, IRON, +12), (8, 12, EMBERTON, SALT, −6),
  (14, 18, DUNWICK, RESIN, +9)}, window 3; contracts {(offer 2, 2 RESIN →
  THORNBY by day 8, pays 60), (offer 10, 2 IRON → GLASSMERE by day 14, pays
  70)}; hazards {(announce 13, arrival 15–16, leg 0, bandits, seize 12),
  (17, 19–22, leg 2, storm, +1 day), (23, 25–28, leg 3, bandits, seize
  15)}, guard fee 4 covers the next crossing.
- Committed lane pins (quoted for the F3 cross-check, not re-derived here):
  the proofs.sh P2 route wins in 13 days, gold 60 → 328, at the 5th iron
  sale; the stale-ink witness pair is (THORNBY, SALT) — whose pinned
  drafting track (impact/shock-free) is base 33, phase 6, days 1–12 =
  (34, 34, 33, 31, 29, 27, 29, 31, 33, 34, 34, 34) — the hi-clamp at 34
  visible on its own witness cell.

Exact drafting surfaces on the committed world (the sim re-derives all of
them from scratch; impact/shock-free core law, d0 ∈ {1..18} — 360 cells per
lag, deviations measured against each cell's clamped neutral base):

- Ink-error law E(a) = |price(d0) − price(d0+a)|: max 3a for a ≤ 6 (peak 18
  at a = 6, the IRON row), mirror-symmetric down to **0/360 exactly at
  a = 12**; exact sums (669, 1131, 1596, 1838, 2075, 2067, 2064, 1828,
  1591, 1127, 664, 0) for a = 1..12.
- Inversion census I(a) = #{ink_dev · true_dev < 0} / #{both ≠ 0}: a perfect
  staircase 0/240, 60/240, 120/240, 180/240, 240/240 for a = 1..5, then
  **300/300 at a = 6**, mirroring back down to 0/240 at a = 11 and 0/300 at
  a = 12 — the certain-inversion band spans lags 5–7, clamps included
  (53/600 impact-free (t,g,day) cells clamp over days 1–30 and the census
  is still total).
- Two-morning decode (T3): the 12 consecutive-value pairs are pairwise
  distinct (enumeration in the theorem gate), so any unclamped consecutive
  pair of dawn readings pins (base, phase) uniquely.

## The sim (stdlib python, sim-lab conventions — pre-registered)

**Arm A (decision, seedless, exact):** a byte-independent mirror of the
world init + price law + verb semantics above. Computes (1) the E(a)/I(a)
surfaces and their closed forms, (2) the theorem gates T1/T2/T3 over full
grids, (3) the four-arm planner census on the committed world: a SHARED
deterministic greedy day-planner (identical code path; solvency reserve
toll·dist + guard fee; plan = best positive believed profit-per-day
buy-here-sell-there pair, committed until the sell; guard hire on announced
hazard windows; contracts unused by all arms — held fixed, disclosed) where
arms differ ONLY in the belief function: **ORACLE** (the law, arrival-day
aware), **SCRYER** (candidate-set inference over (base, phase) from its own
dated ledger history — exactly the information the shipped UI gives a
player, plus arithmetic), **INKTRUTH** (ink read as today's truth — the
concept's own player model), **BLIND** (no memory: current town live,
midpoint elsewhere). Metrics: final gold at the close of day 30 (early-win
stop disabled for the scalar; first day gold ≥ 300 reported), SCRYER's
identified-cell timeline.

**Arm B (twin, seedless):** an independently-written literal day-walk
evaluator (unit-by-unit trade execution, dawn decay loop, no shared
formulas) that must reproduce every Arm-A number exactly — the P059–P065
twin discipline.

**Arm R (seeded, reporting-only, NO statistical gate):** 200 alternative
worlds — 32-bit init seeds drawn via `random.Random(20261590)` into the SAME
xorshift32 world generator — reporting the arm-ordering census and the
R2-clause replication rate (drafting at n = 20: 9/20 — the named
world-fragility axis); stability re-run 20261591; presentation sampling
20261592; aux 20261593 reserved and asserted NEVER read.

**Gates (INVALID if any fails):** F1 world identity (the base/phase tables
above re-derived from seed 0x5749434B; day-1 price table
[[9,19,48,26],[15,16,34,43],[18,22,26,30],[19,34,46,14],[6,21,60,23]]
matched; the witness-cell track above matched); F2 theorems (T1 period-12
identity ∀m; T2 anti-phase identity tri12(m+6) = −tri12(m) ∀m; T3 the
12-pair distinctness enumeration + unique (base,phase) recovery from every
unclamped consecutive pair over the full (base, phase) grid); F3 closed-form
anchors (the E sums and I staircase above, exact; E(12) = 0 and I(6) =
300/300 as identities of the committed world; the A-then-B round-trip net-0
edge at cap-free cells — the committed "hammering A/B in place always loses
gold" comment is measurably net-0, not negative, off-cap/off-clamp: a
disclosed micro-erratum, reporting-only); F4 hand world (2 towns × 1 good,
step 1, pencil E/I); F5 degeneracies (drift_step 0 → ink never lies, I
empty; lag 12k exactness for k = 1, 2, 3); F6 battery (twin exact-equality
on every number, byte-identical stdout + results.json across two process
runs, CPython minor pinned, aux seed never read via constructor registry).

**Decision rule (pre-registered, evaluated in this order):**

- **REJECT** ("the hook as committed is not a bet — it is a solved clock":
  the mirror is deterministic and the ledger decodable, so the aging-ledger
  read as shipped measures whether the player knows the period, not how
  well they price risk) — ALL of: **R1** I(6) = 1 exactly (den ≥ 250) AND
  I(12) = 0 exactly AND E(12) = 0 exactly, clamps included, on the
  committed world; **R2** SCRYER ≥ (9/10)·ORACLE final gold at the
  committed world under the shared scaffold (drafting: 1201/1309 ≈ 0.9175 —
  1.0194× over the line, knife-edge disclosed); **R3** T1/T2/T3 verified as
  exact identities (the theorem-gated conjunct, disclosed as such —
  falsifiability rides R1/R2).
- **INVALID** — any F1–F6 gate fails: report, no ruling.
- **APPROVE** ("the hook prices memory as a genuine gamble as shipped":
  clamps/decks/impact break the mirror in practice and inference cannot
  collapse the gap inside one run) — BOTH of: I(6) ≤ 1/2 AND SCRYER ≤
  (3/4)·ORACLE. Mutually exclusive with REJECT by arithmetic (1/2 < 1 on
  I(6); 3/4 < 9/10 on the ratio).
- **NULL** (anything else — pre-registered axes, each a finalized citable
  finding): (n1) partial mirror (1/2 < I(6) < 1 — the clamp-conditional
  census IS the finding); (n2) decodability straddle (3/4 < ratio < 9/10),
  or the greedy-nonmonotonicity overshoot (SCRYER > (11/10)·ORACLE — seen
  at drafting on the decks-OFF row, 1496/1237 ≈ 1.209: better beliefs are
  not monotone through a greedy scaffold, the named planner boundary);
  (n3) world fragility (the committed-world clauses hold but Arm R's
  200-world replication of R2 lands below 1/2 — the census ships with
  exact per-world rows); (n4) theorem failure without gate failure (the
  drafter's tri12 algebra is wrong — the corrected law is the finding).

**Expected landing, DISCLOSED per the P048–P066 closed-form-arm norm
(drafting prototype ran this session; the sim re-derives from scratch and
must not trust these):** REJECT on all three conjuncts — R1: I(6) = 300/300,
I(12) = 0/300, E(12) = 0/360, exact, clamps included; R2: 1201/1309 ≈
0.9175 ≥ 9/10 (knife-edge, 1.0194×, disclosed — and world-dependent: 9/20
alternative drafting worlds, the n3 axis armed); R3: all three theorems are
two-line integer identities. Full drafting table (decks ON, committed
world): ORACLE 1309 / SCRYER 1201 / INKTRUTH 898 / BLIND 0 final gold; all
three informed arms cross 300 by day 6 vs the committed route's day 13
(reporting row: the concept's own compounding proof is conservative);
SCRYER identifies 16/20 cells by day 30 on its own greedy trajectory —
identification is not even necessary for the collapse. Falsifiability is
real on every clause: clamps COULD have broken I(6) (53/600 cells clamp;
they did not — but a world with tighter lo/hi bands lands n1 exactly);
the R2 ratio moves with the scaffold and the world (9/20 alt-world
replication says a NULL-n3 landing is genuinely live); and INKTRUTH
finishing ABOVE BLIND (898 vs 0) shows the ledger is far better than
nothing — the REJECT is against the hook's RISK story, never against the
ledger having value.

**Boundaries (stated):** planner boundary (all gold numbers are properties
of the shared greedy scaffold, not of optimal play — the scaffold is held
identical across arms so only the belief axis varies; a full-DP upper bound
is the named free follow-up); deck boundary (contracts unused by all arms;
rumor/hazard decks ON at the decision cell as shipped, decks-OFF row
reported); impact boundary (beliefs are impact-free forecasts, execution is
impact-exact — shared across arms); magnitude boundary (the E/I surfaces
are theorem-backed; the gold gaps ride the committed seed's world, with the
Arm-R census as the honesty row); intent boundary (REJECT does not say the
game is bad — it says the committed hook SENTENCE mis-describes the shipped
mechanism; the consequence menu is where intent lives).

**Consequence, pre-registered** (routing is the manager's per Q-0260 — this
repo never edits gba-homebrew files; nothing here builds, publishes, or
spends; the ruling conditions on the committed v0.4 law — a later cut that
de-periodizes prices or varies the world seed means re-run, not reuse):
REJECT → paste-ready structured choice, recommendation first per Q-0263.2 —
**(a, recommended — zero new mechanics, lane-precedented):** per-run world
seed (the lane's own seeded-cave-runs recipe, already costed for Lumen
Drift: u32 seed as init offsets, seed 0 = byte-identity so every committed
proof carries verbatim, daily seed = published code) — deletes the
across-run memorization and re-arms the within-run read; **(b)** de-rig the
clock: co-prime per-good periods (e.g. 10/12/14/18) so no single revisit
lag sits in every good's mirror band and the anti-phase lag stops
coinciding with the map's natural round trips — one constant per good,
proofs re-pinned; **(c)** lean in: surface the decode as UI (after two
consecutive dawns in a town, the ledger row shows the forecast track) and
re-aim the hook at route optimization under known cycles — the honest
Taipan skill, an intent call the lane owner makes, never ruled here.
APPROVE → the hook sentence gains a measured basis and the witness words
already ship the risk meter. NULL → the named axis ships with its exact
census (n1's clamp map, n2's ratio, n3's per-world table) as the citable
number.

## Relations (adjacent heads — deliberately links, not duplication)

- **P043 (Brineward band necessity)** — same lane, different game, different
  object: P043 prices an ECONOMY claim (is band-2 necessary) via a policy
  grid; this head prices an INFORMATION claim (is stale ink a bet) via a
  belief-controlled planner + exact lag surfaces. Zero shared fixtures.
- **P063 (menu-width leverage inversion)** — nearest method kin (a game's
  own committed leverage sentence priced through its committed code path,
  REJECT predicted): different lane, different mechanism family
  (information decay vs action-surface truncation); the shared-scaffold /
  vary-one-axis design is its inheritance.
- **P059 (prestige-reset optimality)** — kin in "audit the engine's own
  committed claim", different claim class (optimality vs risk narrative).
- **P045 (mineverse stale-indicator threshold)** — shares only the word
  "stale": that head prices a data-feed staleness BADGE threshold; this one
  prices in-game information VALUE under a periodic law. Disclosed to
  pre-empt the collision read.
- **P066 (kill-clock anchor)** — the round's previous slot; kin only in the
  "(rule, process-shape) pair" moral: there a deadline against an arrival
  shape, here a memory against a price process. No shared fixtures.

## Model basis (declared model-dependence — the P024 discipline)

The E/I surfaces and T1–T3 are exact properties of the committed law —
model-free. The gold table is model-laden three ways, all disclosed: the
greedy scaffold (held identical across arms; only beliefs vary), the
impact-free belief convention (execution stays impact-exact), and the
committed fixed seed (the shipped world IS the decision cell — the game
commits "The SAME world every run" — with the Arm-R alt-world census as the
robustness row). No claim rides on magnitudes finer than the pre-registered
bands.

## Probe report (v0, 2026-07-15)

**1. What is this really?** A pre-registered audit of a committed game
hook's RISK story against the same tree's committed price law: three
integer theorems (photograph at lag 12, mirror at lag 6, two-morning
decode) plus a belief-controlled four-arm planner census on the shipped
world, deciding whether "every trip is a bet on your own stale information"
describes the mechanism or contradicts it.

**2. What is the possibility space?** (i) Don't run it — the hook sentence
stays unpriced and the lane iterates flavor on a mechanism whose core read
may be a solved clock; (ii) run exactly this (chosen); (iii) full-DP
optimal-play audit (costlier, planner-free — named follow-up); (iv) audit
across the growth-cut roadmap instead (wider map/mules — premature: v0.4 is
the committed surface).

**3. What is the most advanced capability reachable by the simplest
mechanism?** Two integer identities (tri12(m+12) = tri12(m), tri12(m+6) =
−tri12(m)) plus one 12-row enumeration decide the whole risk narrative of a
shipped game; the planner census then prices what the identities are worth
in gold. Nothing beyond stdlib integers is needed anywhere.

**4. What breaks it? (assumptions made explicit)** (a) Clamps could break
the mirror census — measured: they don't on the committed world (53/600
cells clamp, I(6) still 300/300), and if a re-tuned world breaks it the n1
axis IS the finding; (b) the R2 ratio is scaffold- and world-dependent
(knife-edge 1.0194×, alt-world 9/20 — n2/n3 axes armed, honestly the
likeliest NULL routes); (c) market impact perturbs the pure law — bounded
±9 with 1/dawn decay, shared identically across arms; (d) the decks add
public shocks — announced before they hit (2<5, 8<12, 14<18), so inference
stays exact; decks-OFF row reported.

**5. What does it unlock?** The lane gets a measured basis for its #11
game's core design decision BEFORE growth cuts 4–5 harden the hook (per-run
seeds vs co-prime periods vs lean-in are one-constant choices today, a
redesign after sprite art and audio land); the fleet gets the transferable
audit — every "fog of war" or memory mechanic over a DETERMINISTIC process
(idle-game offline projections, cached dashboards re-displayed as live,
any replay-from-memory read) inherits the same question: is the staleness a
risk or a rotation?

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external: all constants are pinned above from the FIRSTHAND clone; the sim
is hermetic, stdlib-only, fully deterministic (joint gate pass probability
for a correct implementation = 1 exactly — every decision clause is an
integer identity or a deterministic planner run; the only seeded arm is
reporting-only). Cheapest kill: a reviewer disproving T2 by evaluating
tri12 at one m — the theorems are two-line pencil checks.

**7. Which lane should build it — and what does it displace or interact
with?** sim-lab runs the verdict (this proposal); gba-homebrew consumes the
consequence menu via the manager (Q-0260). It displaces nothing in-lane —
Wickroad's own proofs.sh pins frames, not policy value; this head prices
what those witness frames are worth. Interacts with the seeded-cave-runs
parked head (option (a) reuses its exact recipe) — link, not duplication.

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib sim file (Arm A + Arm B twin + Arm R reporting), one fixtures.json
carrying every constant in § Pinned model verbatim, one results.json +
stdout byte-stable across two runs — the P059–P065 shape, nothing new.

**Recommendation: sim-ready**
