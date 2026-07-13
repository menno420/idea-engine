# Brineward band-2 necessity — does the committed loot/price ladder actually force the deeps, or is shallow grinding a viable route to the full upgrade ladder?

> **State:** sim-ready
> **Class:** game-mechanics (pipeline rotation — the standing ORDER 003
> GAME-MECHANICS slot, round 7; rounds 1–6 were P020 casino odds → V022 reject,
> P023 entry fee → V025 reject, P027 comp/stipend → V029 null, P031 explore
> pacing → V033, P035 mining booster throttle seal → V046 null, P039 Gloamline
> survival ceiling → V050 approve) ·
> **Target:** `menno420/gba-homebrew` (the Game Lab lane — owns the Brineward
> band tables, the upgrade ladder, and the charted-score/save-ledger surface
> this verdict prices; routing is the manager's per Q-0260, this repo never
> edits gba-homebrew files); verification target `menno420/sim-lab` per the
> Q-0264 pipeline
> **Grounding:** https://github.com/menno420/gba-homebrew@8bac80a70c82096828663d501af5f2790acbccc4 · fetched 2026-07-13T18:58:31Z
> (shallow clone at drafting, HEAD committed 2026-07-13T18:51:09Z; every
> constant below quoted from `games/brineward-nds/source/bw_sim.h`,
> `games/brineward-nds/source/bw_sim.c`, `games/brineward-nds/source/main.c`,
> and `docs/concepts/brineward-concept.md` — all at that pin; subject sourced
> via the fleet game repos, pokemon-mod-lab DARK, skipped per the reading
> path's rule)

**Origin:** drafted under standing owner ORDER 003 ("continue coming up with new
ideas, that is your main purpose") in the ORDER 004 rule-3 rotation — round 7:
P041 served fleet-backlogs (#331), P042 served venture (#333), so this head is
the round's GAME-MECHANICS slot. It is the second game-mechanics head sourced
from the Game Lab repo but the first from its **Brineward** arc — the sibling
game P039's own alternatives line passed on verbatim ("concept tree mid-build,
no committed score surface yet"). Nine slices have shipped since that pass: at
`8bac80a` the danger bands, the upgrade ladder, the hold cap, the
sink-forfeits-hold rule, and the pier-repair price are all committed
one-constant tables, and the arc's charted score ("deepest band ever sailed")
plus the slice-9 save ledger already persist on the depth premise this head
prices.

## The idea

Brineward's whole economy hangs on two lines of its own committed concept doc
(`docs/concepts/brineward-concept.md` @ `8bac80a`), both load-bearing, neither
ever quantified:

1. *"Tier prices roughly triple per step so band-2 runs stay necessary, never
   optional."* (§ Progression / economy sketch)
2. *"deep-water salvage is worth more per crate, so greed has a shape: one more
   fight or turn for home?"* (§ Core loop, Loot bullet)

The constants those lines gesture at are now all in-tree
(`games/brineward-nds/source/bw_sim.c` + `bw_sim.h` @ `8bac80a`): crate value
per band `BW_BAND_LOOT_VALUE_OF = {5, 12, 25}`; upgrade price INTO tier
`BW_UP_COST = {0, 15, 45}` per track × 3 tracks → **the full ladder costs
exactly 180g**; `BW_LOOT_DROPS = 3` crates per sunk rum-runner;
`BW_HOLD_CAP = 8`; `BW_REPAIR_PER_GOLD = 4`; enemy hull per band
`{100, 130, 160}` and enemy reload `{150, 120, 100}` (vs `BW_RELOAD_PLAYER`
90, 3-ball rakes, `BW_MAW_HULL` 120 ≈ "two clean rakes of the tier-0 battery"
→ one clean rake ≈ 60 hull). The movement rules are equally committed
(`main.c` @ `8bac80a`): SELECT from a won water descends one band (carrying
hold, dents, and tiers); START stays in the band; the pier is IN every water —
banking is a detour, not a voyage home; sinking forfeits the unbanked hold and
respawns at port in band 0 with a free full refit.

So "band-2 runs stay necessary" is now an arithmetic claim about committed
numbers plus one honest unknown — **how dangerous a deeper duel actually is**.
Neither direction is pre-computable. For necessity: a band-2 crate is worth 5×
a band-0 crate while the deepest enemy has only 1.6× the hull. Against it: the
committed hold cap bites exactly at depth (a 2-band descent already yields 6 of
8 hold slots before the first band-2 wreck breaks up), deeper crews fire
faster on heavier hulls (committed reload/hull tables), reefs `{0, 3, 5}` and
one-level-worse weather tax the deeps, and a sink hands back the WHOLE unbanked
hold — the richer the hold, the bigger the forfeit. If shallow grinding reaches
the 180g ladder at comparable speed, "never optional" is false, and the lane is
building depth chrome (charted score, save ledger) on an unpriced premise; if
depth genuinely dominates at honest risk, both doc lines deserve their numbers.

## The model (committed constants quoted @ `8bac80a`; invented constants pinned with sensitivity)

**World, per water (the game's own unit — one rum-runner duel, then salvage):**
in band `b ∈ {0, 1, 2}` a fought water either **sinks the player** (forfeits
the unbanked hold, respawn port band 0, full free refit — `begin_duel`'s
`carry_hull <= 0` branch) or is **won**, dropping 3 crates worth
`v_b ∈ {5, 12, 25}` each (committed). Scooping is pinned always-scoop,
chronological, hold-capped at 8 (excess crates wasted — the committed cap).
Banking = pier detour inside the water (committed `bw_dock_step`), pinned to
include full repair at `ceil(missing_hull / 4)` gold (committed
`BW_REPAIR_PER_GOLD = 4`, "rounded against the player").

**Duel outcome (the honest unknown, pinned with committed-derived ratios):**
per-duel hull damage is drawn from the 5-point support
`{0, ⌊D_b/2⌋, D_b, D_b + ⌈D_b/2⌉, 2·D_b}` with pmf
`{1/8, 1/4, 1/4, 1/4, 1/8}` (mean exactly `D_b`). The player sinks iff
cumulative damage since the last full repair reaches 100 (`BW_HULL_MAX`,
tier 0); the sinking draw resolves BEFORE the win (pinned). The band scaling of
`D_b` is committed-derived, not invented: rakes-to-kill at tier 0 =
`ceil(EHULL_b / 60) = {2, 3, 3}` → pinned duel time `t_b = {1, 3/2, 3/2}`
water-units; enemy rake pressure ∝ `t_b / ERELOAD_b` → damage ratio
`r_b = {1, 15/8, 9/4}` exactly. Only the BASELINE is invented:
`D_0 ∈ {20, 35, 50}` (the risk axis), giving pinned integer tables (round half
up): `D0=20 → {20, 38, 45}`, `D0=35 → {35, 66, 79}`, `D0=50 → {50, 94, 113}`.
The other axis is the banking overhead `T_dock ∈ {1/2, 1, 2}` water-units per
pier detour (invented, pinned) — **9 cells**, central cell `(35, 1)`. Time on a
sinking water = `t_b / 2`; SELECT transition and post-sink restart = 0
(pinned; both flatter depth — direction stated below).

**Policy family (pre-registered, 18 policies):** `GRIND(b, m)` for
`b ∈ {0, 1, 2}`, `m ∈ {1, 2, 3}` — descend by winning one water per band
`0..b−1` (scooping en route), pier-bank + repair at descent end, then loop
{fight `m` waters in band `b`, pier-bank + repair}; sinking restarts the
descent. Plus `GRIND-H(b, m)` — identical, but banks + repairs early whenever
hull ≤ 50 after a won water (θ = 50 pinned; the "turn for home" verb).
Hold arithmetic is exact: a `b=2` descent banks 6 crates = 3·5 + 3·12 = 51g;
an `m=3` band-2 loop segment banks `min(9, 8) = 8` crates = 200g with one 25g
crate wasted — the committed cap bite, surfaced as its own reported column.

**Arm A (the DECISION arm — seedless exact enumeration):** segments are iid
(every bank repairs to full), each segment ≤ 3 duels → ≤ 125 outcome paths of
exact `fractions.Fraction` mass; the long-run gold rate `G(policy; cell)`
follows from renewal-reward over the sink-to-sink cycle in closed form
(geometric composition over segment sink probabilities; the zero-sink branch —
possible by construction at `D0=20`, band 2, `m=1`, max cumulative damage
90 < 100 — is handled exactly as the pure loop rate, stated). Decision
numbers: `G*(≤1) = max G` over policies with `b ≤ 1`; `G*(all)` over all 18;
**`NEC(cell) = G*(all) / G*(≤1)`** — how much the deeps beat the best shallow
grind, which is exactly the time ratio to ANY banked-gold target including the
180g ladder. Reported: the full 18-policy × 9-cell `G` table, `NEC0`
(vs band-0-only), `T180 = 180/G` per cell (renewal-smoothed, discreteness
disclosed), per-cell argmax policy, the m-curve per band (the greed dial), the
wasted-crate column, and per-segment sink probabilities.

**Arm S (seeded MC confirmation):** `random.Random(20261309)`, cells in pinned
order (`D0` outer, `T_dock` inner), policies in pinned order, 100,000 waters
per (cell, policy) leg, one damage draw per water in pinned draw order;
`G_S = total banked / total time`; agreement gate
`|G_S − G_A| / G_A ≤ 1/50` on EVERY leg (pre-checked ≥ 4 SE headroom at the
pinned leg length), any breach invalidating the run. Stability leg: seed
**20261310**, 20,000 waters per leg, widened gate ≤ 1/20, must reproduce the
ruling class through both twin evaluators. Sensitivity confirmations: seed
**20261311**. Aux seed **20261312** is never read by any decision number.
Seeds **20261309–20261312** are allocated strictly above the P042 registry
high-water **20261308** (re-swept at drafting: tree-wide
`rg -g '!bootstrap.py' -g '!.substrate' -o '202613[0-9][0-9]'` at HEAD
`e52f212` maxes at 20261308; sim-lab's outbox at drafting carries nothing
above 20261304 — verdicts consume proposal seeds, they allocate none).

**Sensitivities (reporting-only, never decision-flipping):** duel time
hull-proportional `{1, 13/10, 8/5}` instead of rakes-derived; 7-point damage
support `{0, D/2, 3D/4, D, 5D/4, 3D/2, 2D}` pmf
`{1/16, 1/8, 1/8, 3/8, 1/8, 1/8, 1/16}` (mean exactly `D`, quarter terms
floored, disclosed); `m = 4`; `θ ∈ {30, 70}`; post-sink restart overhead
`= T_dock` instead of 0.

**Gates (run invalid on any failure):** F1 ladder-total identity
`(15 + 45) × 3 = 180` asserted from the committed table; F2 hold arithmetic —
descent bank 51g, band-2 `m=1` bank 75g, `m=3` bank 200g + one 25g crate
wasted, exact; F3 zero-damage fixture cell (`D0 = 0`, `T_dock = 1`, NOT in the
decision grid): rate = loop rate exactly (no sinks → descent amortizes to
zero), hand values `G(GRIND(2,2)) = 150/4 = 75/2`, `G(GRIND(1,2)) = 72/4 =
18`, `NEC = 25/12`; F4 damage-pmf mean identity (mean `= D_b` exactly, every
band and axis point, both supports); F5 exact monotonicity — `G(policy)`
non-increasing in `D0` under shared enumeration/common random numbers,
`NEC ≥ 1` by class nesting, per-segment sink probability non-decreasing in `m`
and in band at fixed `D0` (theorems; any violation is an implementation
defect); F6 repair identities — zero-damage segment pays 0, hull `100 − h`
pays `ceil(h/4)` (spots: h=1 → 1g, h=48 → 12g); per-leg draw-count sentinels;
twin independently-written decision evaluators; stdout + results.json
byte-identical across two process runs (Arm A platform-independent exact
Fractions; Arm S pinned to a stated CPython minor version).

## Decision rule (pre-registered; evaluated in this order, REJECT first)

- **REJECT** ("'never optional' collapses — the committed value/price ladder
  does not force the deeps at honest duel risk"): `NEC(cell) < 5/4` in **≥ 5
  of 9** cells. Checked FIRST — the costly error is the lane continuing to
  build depth chrome (the charted score and the slice-9 save ledger already
  persist "deepest band sailed" as THE score) and future band tuning on an
  economy that doesn't actually send anyone deep. Consequence: the quantified
  retune signal routes lane-side via the manager (Q-0260) — the band loot
  values, prices, and hold cap are the header's own self-described
  "one-constant owner-tunables", and the doc line retires or gains its
  precondition.
- **APPROVE** ("band-2 runs are necessary AND greed has a shape"):
  `NEC(cell) ≥ 3/2` in **≥ 7 of 9** cells (mutually exclusive with REJECT by
  arithmetic: ≥ 7 cells at ≥ 3/2 leaves ≤ 2 below 5/4) **AND** the central
  cell's argmax policy is neither the timid pole `GRIND(b*, 1)` nor the
  maximal-greed pole `GRIND(b*, 3)` — i.e. it is `GRIND(b*, 2)` or a `GRIND-H`
  variant, the greed dial's interior answer — **AND** the seed-20261310
  stability leg reproduces the ruling. Consequence: both doc lines gain their
  numbers routed lane-side per Q-0260 ("never optional" cites the measured NEC
  floor; "one more fight or turn for home?" cites the measured banking cadence
  m* and the hull-aware trigger's value).
- **NULL** (anything else — a legitimate reportable outcome with pre-registered
  axes, each a citable finding, never a re-run request): (i) **band-1-carries**
  — the argmax band is 1 in ≥ 5 cells while `NEC0 ≥ 3/2`: "necessary" fails
  specifically to the middle rung, naming `BW_BAND_LOOT_VALUE_OF[1] = 12` as
  the knob; (ii) **hold-cap bind** — the committed 3-drop × cap-8 arithmetic,
  not duel risk, prices depth (the wasted-crate column is the evidence and
  `BW_HOLD_CAP` the knob); (iii) **risk-straddle** — the ruling flips across
  `D0` with the flip boundary `D0†` as the citable pin; (iv) **dock-straddle**
  — flips across `T_dock`; (v) **margin-thin** — deciding cells live between
  5/4 and 3/2; (vi) **arm disagreement**; (vii) **sensitivity straddle**
  (reporting legs name the axis, never flip the decision).

**Boundaries (stated in the verdict, each with its direction):** the Maw is
out of decision scope by the game's own clock — it stirs only after
`BW_MAW_PATIENCE = 600` quiet salvage frames and never enters
`BW_MAW_HARBOR`, and every policy here banks or puts out promptly (omitting
its bites AND its richer `{15, 30, 50}` crates; both directions named, the
tax and the bonus roughly oppose). Reefs `{0, 3, 5}` per band and
one-level-worse weather are NOT separately modeled — omitting deep-band
hazards flatters band 2, so it is GENEROUS TO APPROVE and a REJECT is robust
against it. Zero SELECT/restart overhead flatters depth the same direction.
The policy family brackets bounded play — mid-duel flight to the pier (the
committed "running for the pier IS the 'turn for home' choice") is
approximated only by GRIND-H's segment-level trigger, so deep-band viability
is a lower bound in that one respect (direction: against REJECT's robustness,
stated — GRIND-H is in the family precisely to shrink it). Upgrades feed back
on none of this (tier-0 sloop throughout; the ladder is the TARGET, not a
lever — the doc's claim is about reaching it, stated). `D0` and `T_dock`
carry no bench measurement anywhere in the fleet — the sweeps bracket scale,
and the NULL probe below turns both into measurements.

## Dedup (swept at drafting, HEAD `e52f212`)

Tree-wide `rg -i -g '!bootstrap.py' -g '!.substrate'
"brineward|danger.band|band.2|push.your.luck|hold.cap|charted"` : zero hits
outside this head's own files except P039's Gloamline block quoting the arc's
NAME in its alternatives line — the pass this head answers. No outbox proposal
P001–P042 cites Brineward; verdicts V001–V052 (sim-lab outbox re-read at
drafting) touch neither the arc nor band-choice routing; V053 (in flight,
parallel session) consumes P042 — venture channel allocation, zero overlap.
Nearest by SLOT: P039 → V050 (same repo, the Gloamline game — a
survival-frames census over a byte-reused engine mirror; different game,
different question class: survivability vs economy routing, frames vs gold
rate, difficulty backlog vs band tables). Nearest by SHAPE: the casino family
P020/P023/P027 → V022/V025/V029 (bankroll-ruin grids under HOUSE levers — a
wagering wallet against take rates; here no wager and no house exist: the
risked resource is hull, the objective is a time RATE to a committed price
ladder, and the lever is the player's routing). Nearest by METHOD:
P041/P042 (exact-Fraction decision arm + seeded confirmation with
invented-but-pinned constants and committed-derived ratios) — method
precedent only, different worlds. P031 → V033 / P035 → V046 / V042–V045
(superbot-games pacing/economy) — different repo, machinery, and consumer.
The four parked 2026-07-10 gba-homebrew heads are all build-direct process
slices, none sim-shaped, none Brineward.

**Alternatives passed on merit:** the Gloamline oil-economy dynamic
sustainability head (P039's own named runner-up — still smaller stakes, the
static margin is 2×); a Brineward duel-geometry census over `check-brine.py`
(the V050 method transplanted — real, but it prices the COMBAT skill surface
the lane's 28-assert proof set already brackets, while nothing anywhere prices
the economy routing the score system builds on; it is the named follow-up if
this head's invented `D0` proves load-bearing); a mineverse browser-game
difficulty pin (still no committed pure mirror there; V042's family already
prices that economy shape).

## Probe report (v0, 2026-07-13)

**1. What is this really?** A pre-registered band-routing economy sim for a
shipped game's committed loot/price ladder: does "band-2 runs stay necessary,
never optional" survive honest duel risk, measured as the exact gold-rate
ratio between the best unrestricted and best shallow-restricted policies in a
pinned family — pricing the depth premise the arc's score and save surfaces
already build on.

**2. What is the possibility space?** Trust the doc line by vibes (the status
quo — depth chrome ships on an unpriced economy); hand-tune band values
lane-side without evidence; wait for owner playtests (slow, n=1, unrecorded);
or this head: enumerate a pinned policy family over the committed tables with
the one honest unknown swept as a pre-registered axis, and register what each
landing means for the lane's next slice.

**3. Most advanced capability from the simplest implementation?** One stdlib
sim + fixture JSON: committed tables quoted verbatim, segments of ≤ 125 exact
paths, closed-form renewal rates, an 18 × 9 policy table, the greed-dial
m-curve, and the hold-cap waste column — all byte-reproducible, no engine
stepping needed.

**4. What breaks it?** The invented duel-damage baseline `D0` is the disclosed
weakest joint (bracketed as the decision axis; its band SCALING is
committed-derived, and the NULL probe converts it to a measurement); the
policy family brackets bounded play (GRIND-H covers the flee direction only at
segment level, direction stated); Maw/reefs/weather omissions all named with
directions — the hazard omissions flatter depth, so REJECT is robust to them.

**5. What does it unlock?** The lane's band-tuning fork decided on evidence:
retune signal vs ratified ladder with numbers vs a named conditional (band-1
knob / hold-cap bind / risk boundary `D0†`); plus reusable art — a
band-routing renewal kernel any loot-ladder game with committed tables can
inherit (superbot's mining depth tiers are the obvious transfer surface).

**6. What does it depend on?** Nothing at verdict time — fully hermetic: every
committed constant quoted into the fixture at drafting @ `8bac80a`, zero
repo/network reads in the verdict session. Consumers: gba-homebrew owns the
tables and the depth-score surface (routing is the manager's per Q-0260);
sim-lab owns the method precedent.

**7. Which lane should build it?** sim-lab (the hermetic pre-registered
exact-arm + seeded-confirmation discipline is the P017–P042 committed
precedent). The verdict consumer is the gba-homebrew lane via the manager
sweep. Dedup argued line-by-line above — no prior proposal or verdict touches
Brineward, band-choice routing, or a banked-vs-unbanked loot economy.

**8. What is the smallest shippable slice?** The committed sim + fixture
reproducing the 18 × 9 tables, the NEC/NEC0 rows, the greed-dial curve, the
waste column, and every gate byte-identically per the done-when in the outbox
block — one PR in sim-lab, no lane build. On NULL, the cheapest live probe is
the lane's own committed tooling at zero new work: the `bands-*-keys.txt`
recorded routes + `bw_telemetry` headless replays measure real tier-0 duel
damage and duel time per band, turning `D0` and `t_b` into bench numbers
before the band is re-litigated.

**Recommendation: sim-ready**
