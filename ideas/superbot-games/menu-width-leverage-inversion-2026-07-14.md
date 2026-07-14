# Menu-width leverage inversion — does message-XP widen the D&D menu into FEWER rewards, and can a data-only reorder fix it?

> **State:** sim-ready
> **Class:** game-mechanics (pipeline rotation — the standing ORDER 003
> GAME-MECHANICS slot, round 12; round 12 opened at fleet backlogs with P061
> (#408) and served venture with P062 (#410), so game mechanics is next per
> ORDER 004 rule 3, confirmed against the slot's own spacing-4 history
> P020, P023, P027, P031, P035, P039, P043, P047, P051, P055, P059 → P063.
> Source rotation inside the slot: the six most recent draws were
> gba-homebrew ×2 (r6/r7), superbot ×2 (r8/r9), superbot-mineverse (r10),
> superbot-idle (r11), so round 12 returns to superbot-games — undrawn since
> round 5 (P031 explore pacing, P035 mining booster throttle);
> pokemon-mod-lab, the only never-drawn games lane, stays excluded as DARK.)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/superbot-games/blob/e3930f134119dd36d9e7f37a7dccb4f4b33e3805/games/dnd/core/resolver.py@e3930f134119dd36d9e7f37a7dccb4f4b33e3805 · fetched 2026-07-14T11:31:51Z
> (FIRSTHAND pin: read directly from a read-only shallow clone at the HEAD
> above, `git log -1` verified `e3930f1… control: work claim — ORDER 009 EAP
> closeout (#137)`. Companion reads at the same pin:
> `games/exploration/quest/leverage.py`, `games/dnd/core/models.py`,
> `games/dnd/data/scenes.py`, `games/dnd/core/effects.py`,
> `games/exploration/quest/catalog.py`, `games/dnd/sim/menu_sim.py`,
> `tests/dnd/test_resolver.py`. The sim itself is fully hermetic: zero
> repo/network reads at verdict time, every fixture constructed in-sim from
> the pinned constants in this file.)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous
pipeline) and ORDER 004 rule 3's rotation, on the EAP final day's close-out
dispatches (inbox ORDER 012 item (3): the pipeline went momentarily DRY at
P062 → V073 APPROVE; ORDER 013 STEP 1 names the fm list authoritative). The
game slot returns to superbot-games after seven rounds away, and the harvest
found a regime the lane's own sim deliberately steps around.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested surface, stated back.** The D&D walking skeleton is the
lane's bounded-authority showcase: the AI Dungeon Master only picks one
pre-approved button per turn, and chat-activity XP is "DM leverage" that
widens how MANY buttons may be surfaced — 2 at base, +1 per 500 message-XP,
hard-capped at 4 (`leverage.py`: `BASE_MENU_WIDTH = 2`, `MAX_MENU_WIDTH = 4`,
`XP_PER_EXTRA_OPTION = 500`) — "never the reward amounts, never the
outcomes." But the resolver implements the width cap as a PREFIX slice:
`_allowed_options` returns `scene.options[:limit]` (`resolver.py`, with
`limit = min(len(options), menu_width(xp), MAX_MENU_SIZE)`). So WHICH
options a low-XP table can legally reach is decided entirely by each scene's
option ORDER — plain data in `games/dnd/data/scenes.py`. And the shipped
data orders all three scenes the same way: the reward-or-progress option
first, the flavour option second, the safe no-op clamp default LAST
(`waystation_road` = advance_escort/scout_ahead/make_camp,
`waystation_gate` = enter_common_room/circle_to_treeline/rest_at_gate,
`treeline_watch` = signal_escort/hold_position/fall_back_camp; defaults
make_camp / rest_at_gate / fall_back_camp — index 2 in every scene).

Three consequences follow immediately, none simmed anywhere: (1) at width 2
the ENTIRE mint surface and the ENTIRE scene graph are already legally
reachable (both `escort_step` options and every edge sit at prefix indices
0–1), so the only thing leverage ever unlocks is the do-nothing button; (2)
adding a no-op to a uniform pick DILUTES the reward rate, so more message-XP
means FEWER expected mints — the leverage gradient points backwards; (3) at
width 2 the surfaced menu EXCLUDES the clamp default, while `models.py`
§4.1 promises the clamp target is "always ON the menu" — the invalid-input
path (`resolver.py` resolves `scene.option(scene.default_option_id)` on the
FULL scene) can pick an option the DM was never allowed to pick. The lane's
own balance sim never sees any of this: `games/dnd/sim/menu_sim.py` pins
rewards at `_FULL_MENU_XP = 5_000` — its own comment says the width clamp is
deliberately bypassed so "EVERY option is a genuine, surfaced choice" — and
`tests/dnd/test_resolver.py` checks the width-2 surface exists but never its
economy. The falsifiable core: **on the shipped constants, is the
message-XP → menu-width leverage reward-INVERTED (long-run mint rate
strictly falling as width grows), and can any within-scene reordering — a
pure data edit under the lane's own Q-0267 "re-skinning is a data-only
edit" doctrine — restore a monotone reward gradient without collapsing the
width-2 game to zero mints?** The drafting-time closed form (disclosed
below, per the P048–P062 norm) says the second half is IMPOSSIBLE — under
prefix truncation the width-2 mint rate is exactly 0 or exactly 1/2, nothing
between — which is precisely what makes this a genuine verdict: the sim
either certifies the impossibility partition (ordering cannot fix it; a
mechanic change is the recommendation) or falsifies my reading of the code.

**The model (fixed, fully pinned — every constant a decision of this file,
none left to the implementer; all decision arithmetic exact
`fractions.Fraction`).**

- **The width law (harvested verbatim @ `e3930f1`).**
  `menu_width(xp) = clamp(2 + max(0, xp) // 500, 2, 4)`; fixture table
  {0→2, 499→2, 500→3, 999→3, 1000→4, 5000→4}. Width axis w ∈ {2, 3, 4} ↔
  XP {0, 500, 1000}. Every scene has exactly 3 options, so **w=4 ≡ w=3** —
  a pinned identity (gate F3), not an assumption.
- **The role graph (the 3 scenes as data, harvested verbatim).** Roles per
  scene: **M** = the mint/progress option, **N** = the flavour option,
  **Z** = the safe no-op clamp default. `waystation_road`: M =
  advance_escort (mints, → waystation_gate), N = scout_ahead (no mint,
  → treeline_watch), Z = make_camp (no mint, stay).
  `waystation_gate` (no mint in scene): M-slot = circle_to_treeline (the
  progress edge, → treeline_watch), N = enter_common_room (stay), Z =
  rest_at_gate (stay). `treeline_watch`: M = signal_escort (mints, stay),
  N = hold_position (stay), Z = fall_back_camp (stay). Start scene
  `waystation_road` (the scenes.py docstring's walking-skeleton start).
  `treeline_watch` is absorbing at every width and every ordering (all
  three options stay) — the long-run regime is its menu composition.
- **The mint (harvested verbatim).** Each `escort_step` application runs
  `offer → accept → apply_event → grant_rewards` on a FRESH `safe_passage`
  instance and mints exactly `TIER_CAPS[RewardTier.I]` =
  RewardBundle(global_xp=5, game_xp=25, **currency=10**), ≤ GLOBAL_MAX
  (20, 120, 50) component-wise (`effects.py`, `catalog.py`). Two mint
  accountings, BOTH simmed: **PER-APP** (shipped semantics — every
  application mints; this includes the double-mint arc the
  DND-ESCORT-DOUBLE-MINT SIM-REQUEST asked about, inbox ORDER 006 item (6))
  and **ONCE** (mint-at-most-once per episode — that request's alternative
  ruling). Bands are evaluated on PER-APP; ONCE is the sensitivity leg, so
  this head stays decision-stable whichever way that verdict landed.
- **Policy family (6, pre-registered — the complete role-order set).** A
  policy is one of the 6 permutations of (M, N, Z) applied uniformly across
  all scenes as the within-scene option order: MNZ (**SHIPPED**), MZN, NMZ,
  NZM, ZMN, ZNM. Reordering is a data-only edit to `scenes.py` tuples —
  no resolver, effect, or reward change.
- **DM behaviour family (4, pre-registered).** B1 **UNIFORM** — uniform
  over the surfaced prefix (the model-agnostic baseline). B2
  **GREEDY-FARMER** — picks a surfaced mint, else a surfaced progress edge,
  else uniform (the revenue adversary). B3 **STORY-DM** — prefers N, then
  Z, then M (the flavour-first table). B4 **CLAMP-p** — B1 but with
  probability p ∈ {1/20, 1/4} returns an off-menu id and clamps to the
  full-scene default (the hallucination path — measures how much economy
  flows through the §4.1 gap). No behaviour reads reward amounts: B2/B3
  read only the role labels, mirroring what a real DM prompt would see.
- **Episode & metrics.** Start `waystation_road`, T ∈ {5, 20, 100} turns.
  Per (policy × behaviour × width × accounting) cell: expected mints,
  expected currency (10/mint at Tier I), P(≥1 mint), expected distinct
  scenes visited, no-op turns, and DEFAULT-IN-PREFIX(w) (boolean: is the
  clamp default legally surfaceable). Exact arm: forward distribution
  recursion over the 3-state chain in `fractions.Fraction` (T-step
  expectations + the absorbing-scene stationary mint rate). MC twin
  evaluator: seeded `random.Random`, 20,000 episodes/cell, seeds
  **20261389** (leg A) / **20261390** (independent twin leg B) /
  **20261391** (B4 clamp-stress leg) / **20261392** (holdout re-run);
  twin-vs-exact agreement within 3σ binomial tolerance per cell.

**Pre-registered bands (all four evaluated per policy, PER-APP, B-model as
stated):**

1. **MONOTONE** — B1 expected mints at T=20 non-decreasing w2 → w3 (and the
   w3 ≡ w4 identity holds).
2. **POSITIVE-FLOOR** — B1 long-run (absorbing-scene) mint rate at w=2
   ≥ 1/6 per turn (a width-2 table still earns SOMETHING).
3. **FARMER** — B2 currency at T=20, w=2 ≤ 3/4 × SHIPPED's same cell
   (width actually gates the farmer somewhere).
4. **CONFORM** — DEFAULT-IN-PREFIX(2) true (the §4.1 "always ON the menu"
   promise survives width capping).

**Decision rule (pre-registered):** **APPROVE-REORDER** iff ≥1 of the 6
policies passes all four bands — the verdict names the passing set and the
recommended data-only `scenes.py` reorder. **REJECT-REORDER** iff no policy
passes all four — the verdict certifies the impossibility partition (the
exact attainable (band-1..4) profile of all 6 policies is the citable
result) and the recommendation escalates from data edit to mechanic change:
width selection must stop being a prefix (e.g. per-option `min_width`
data, or width-indexed option sets — named for the lane, priced no further
here; intent stays the lane's per the V044/V046 posture). **NULL** iff gate
F1/F4 fails (the fixture does not reproduce the harvested constants — my
reading of resolver/scenes/effects is wrong, and the honest null names the
mismatching pin).

**Gates (fail-loud, all must pass before any cell is read):**

- **F1 identity** — fixture reproduces the width table above, the three
  scene role-tuples with defaults at the shipped positions, TIER_CAPS[I] =
  (5, 25, 10), GLOBAL_MAX = (20, 120, 50), and `_FULL_MENU_XP = 5000`
  (the dedup witness constant, asserted present so the fixture tracks the
  harvested tree, not a memory of it).
- **F2 inversion closed form** — exact arm reproduces SHIPPED × B1
  long-run mint rate = **1/2** at w=2 and **1/3** at w=3/4, and E[mints,
  T=20] = **9961473/1048576** (≈ 9.500) at w=2 vs **21502885715/3486784401**
  (≈ 6.167) at w=3 — the drafting-time closed form, committed as exact
  rationals.
- **F3 width identity** — w=4 ≡ w=3 in every cell (3-option scenes).
- **F4 hand world** — a by-hand 2-turn SHIPPED × B1 × w=2 trace (turn 1:
  1/2 mint-and-move-to-gate, 1/2 move-to-treeline; turn 2 conditional
  menus) matches the recursion cell-for-cell in exact arithmetic.

**Drafting-time landing (computed this slice, DISCLOSED per the
P048–P062 closed-form-arm norm; the sim's job is to confirm-or-refute on
the full grid, not to discover these):** the inversion is real and exact —
SHIPPED × B1 long-run mint falls 1/2 → 1/3 (−1/6 per turn absolute, −33%
relative; E[mints, T=20] −35.1%) when the table earns its first 500
message-XP, while SHIPPED × B2 mints every reachable turn at EVERY width
(19 mints / 190 currency at T=20 — width gates the farmer not at all) and
DEFAULT-IN-PREFIX(2) is FALSE (band 4 fails for SHIPPED, NMZ). Across all
6 policies the w=2 B1 long-run rate partitions as **{0, 1/2} and nothing
between** (rate = [M ∈ prefix(2)]/2), so MONOTONE (≤ 1/3 at w=2) forces
rate 0 — **no policy can pass MONOTONE and POSITIVE-FLOOR together**, and
the predicted verdict is REJECT-REORDER with the partition as the citable
number: NZM/ZNM buy monotonicity and full farmer-gating (B2 w=2 currency
0, −100%) at the price of a zero-mint width-2 game; every other ordering
keeps the inversion. If the harness reproduces this, the D&D lane gets a
measured, pre-priced case that its leverage design needs one mechanic
decision (what width SELECTS, not how much it counts), with the two
attainable orderings priced as the interim menu.

## Relations (adjacent heads — deliberately links, not duplication)

- **P031 → V033 (explore-action pacing)** and **P035 → V046 (mining booster
  throttle)** — the slot's two prior superbot-games draws; both price
  RATE constants of other games' faucets. This head prices menu
  COMPOSITION under the width law — no shared constant, no shared file.
- **Inbox ORDER 006 item (6) DND-ESCORT-DOUBLE-MINT** (served fleet-side as
  a SIM-REQUEST verdict) — asked whether ONE traversal completing the
  escort bundle TWICE (advance_escort@waystation_road +
  signal_escort@treeline_watch) is intended. This head does not re-ask it:
  both accountings ride as pre-registered arms (PER-APP/ONCE), so this
  verdict composes with either ruling. What that request never asked — and
  nothing else in the pipeline asks — is the WIDTH/ORDER question: which
  options are legally REACHABLE at a given XP, and what gradient leverage
  actually buys.
- **Inbox ORDER 006 item (7) EXPLORATION-REWARD-BANDS** — prices the SIZE
  of TIER_CAPS. This head holds TIER_CAPS fixed (any retune rescales
  currency linearly and moves no band — mint COUNTS drive all four bands).
- **`games/dnd/sim/menu_sim.py` @ `e3930f1`** — the lane's own economy pin,
  and this head's dedup witness: it proves per-option reward bounds at
  `_FULL_MENU_XP = 5000` and by its own comment steps around the width
  clamp. This head is the sim that file declines to be.
- **P059 (prestige reset-policy, r11 game slot)** — method kin only
  (absorbing-chain exact arithmetic); different repo, different constants.

## Model basis (declared model-dependence — the P024 discipline)

The world model is the shipped code read verbatim — graph, width law, mint
amounts, clamp semantics are all harvested constants, not assumptions. The
model-dependent layer is the DM behaviour family: real DMs are LLMs, not
B1–B4. The four behaviours are chosen as the decision-relevant envelope —
B1 the agnostic baseline, B2 the revenue adversary (upper envelope), B3 the
reward-averse floor, B4 the hallucination channel — and every band is
evaluated against a NAMED behaviour, never an average over them, so the
verdict never launders a behavioural assumption into a code claim. What no
behaviour model can settle: whether a zero-mint width-2 table is an
acceptable DESIGN (the NZM/ZNM price). That is an intent call and stays the
lane's; this sim's job is to hand it the exact price tag.

## Probe report (v0, 2026-07-14)

> Single-pass battery (panel not escalated: self-contained knowledge probe
> over pinned lane constants, sim is report-only evidence, no
> spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **source verified
> FIRSTHAND** — read-only shallow clone `git log -1`-verified at
> `e3930f134119dd36d9e7f37a7dccb4f4b33e3805` (fetched 2026-07-14T11:31:51Z);
> all eight companion files read at that pin, every constant above traced
> to its defining line (width law, prefix slice, scene tuples + defaults,
> escort mint path, TIER_CAPS/GLOBAL_MAX, `_FULL_MENU_XP`, the width-2
> resolver test). (b) **dedup** — PROPOSALs 001–062 (headers + summary
> lines, live outbox + rolled archive) and VERDICTs V001–V073 swept for
> menu/width/ordering/prefix/leverage/dnd terms before drafting; nearest
> kin argued distinct in Relations. (c) **kill test NOT triggered** — no
> prior head prices menu composition, option reachability, or the
> message-XP leverage gradient. (d) **feasibility + liveness arithmetic
> checked** — the drafting-time closed form was actually RUN in exact
> `fractions.Fraction` and its landing DISCLOSED (the 1/2 → 1/3 inversion,
> the {0, 1/2} width-2 partition, the B2/B4 headline cells — the
> P048–P062 norm), with the fixture-identity NULL named as the live escape.

**1. What is this really?** A pre-registered pricing of the D&D
bounded-menu engine's message-XP → menu-width leverage through the
resolver's prefix truncation: the complete 6-permutation within-scene
role-ordering family (SHIPPED = mint-first/default-last) × 4 DM behaviour
models (uniform / greedy farmer / story-DM / clamp-p) × widths {2,3,4} ×
both escort-mint accountings, judged against 4 bands fixed before any code
(MONOTONE, POSITIVE-FLOOR, FARMER, CONFORM), exact-Fraction forward
recursion as the primary arm with a seeded MC twin (20,000 episodes/cell,
seeds 20261389–392), on a 3-state absorbing scene graph harvested verbatim
@ `e3930f1`.

**2. What is the possibility space?** (i) Don't run it — the round-12 game
slot goes unserved and the lane's growth mechanic keeps an unpriced (and
closed-form-inverted) gradient. (ii) Serve the slot from the mining/fishing
economy surfaces — those are ORDER 006's served SIM-REQUEST territory
(items 4–7); re-asking them duplicates verdicts. (iii) A prose bug report
to the lane ("your leverage is inverted") — states the 1/2 → 1/3 fact but
prices no fix; the interesting half is that the obvious fix family
(reorder the data) is provably incomplete, which only the full-grid sim
certifies. (iv) Patch superbot-games directly — out of scope by this
repo's own contract (no product code here; intent stays the lane's).
(v) This head: hermetic, exact-arithmetic, pre-registered, with the
impossibility partition as its sharpest deliverable.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file + one fixture JSON yields: the exact
6×4×3×2 policy grid, the first quantified statement of what message-XP
leverage is WORTH in the shipped data (negative: −1/6 mint/turn long-run,
−35.1% E[mints, T=20] under the uniform DM), the certified {0, 1/2}
width-2 partition (no data-only reorder passes MONOTONE + POSITIVE-FLOOR
together — a closed impossibility over a discrete fix menu, a stronger
verdict shape than any single-fix test), the §4.1 CONFORM audit (the clamp
default is not legally surfaceable at width 2 under 2 of 6 orderings,
SHIPPED included), and a reusable pattern — prefix-capability meets
ordered list — that transfers to permission tiers, flag rollouts, and
every "unlock by rank" surface in the fleet.

**4. What breaks it? (assumptions made explicit)** (a) **The behaviour
family** — real DMs are LLMs, not B1–B4; the envelope design (agnostic /
adversary / averse / hallucinating) brackets the decision-relevant range
and every band is keyed to a NAMED behaviour, never an average; a logged
DM-choice trace from the lane is the free replacement measurement, named.
(b) **The role mapping at `waystation_gate`** (no mint in scene: M-slot =
the progress edge) — a mapping decision of this file, disclosed; the
alternative (N1/N2 arbitrary) changes no band because gate's options mint
nothing and only the edge placement moves. (c) **The scene graph is the
walking skeleton** — 3 scenes today; more scenes change the numbers but
not the partition argument (rate = [M ∈ prefix(2)]/2 holds per absorbing
menu regardless of graph size); the gate F1 pins the graph so growth
forces re-run-not-reuse. (d) **The double-mint ruling** (ORDER 006 item
(6), served fleet-side) — unknown here; both accountings ride as
pre-registered arms so no ruling direction invalidates a cell. None of
these is hidden; each is a named axis, a disclosed mapping, a pinned
fixture, or a dual arm.

**5. What does it unlock?** The lane's leverage mechanic stops being an
unpriced growth loop: either a data-only reorder is certified with its
exact price tag (the zero-floor menu NZM/ZNM, farmer-gating included), or
the lane gets a measured case that width must stop SELECTING by prefix —
one mechanic decision (per-option `min_width` data or width-indexed
option sets), arriving with the full grid attached. The pipeline gains
its first menu-composition verdict and its first certified-impossibility
verdict shape; the game slot's superbot-games line (P031 pacing → P035
throttle → P063 composition) now spans rate, bypass, and reachability.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external at verdict time — fully hermetic (the P017–P062 precedent); the
harvest grounding is one already-verified read-only clone pin (FIRSTHAND,
`e3930f1`). Cheapest kill BEFORE simming: a prior verdict on menu width or
ordering (none — swept), or a lane commit reordering `scenes.py` or
replacing the prefix slice after `e3930f1` (none at the pin; F1 makes any
later change a loud re-pin, not a silent stale verdict). Cheapest confirm
AFTER: run the lane's own `menu_sim.py` at xp ∈ {0, 500} instead of
`_FULL_MENU_XP` — the width-clamped rerun of their sim is the one-line
lane-side reproduction.

**7. Which lane should build it — and what does it displace or
duplicate?** sim-lab builds and runs the sim (the Q-0264 pipeline's verify
seat — this file is its intake spec); superbot-games consumes the verdict
as a `scenes.py` data decision or a width-mechanic decision on
`resolver.py`/`leverage.py`, routed by the manager per Q-0260; this repo
builds nothing. It displaces nothing in flight (no verdict session holds a
game head; the pipeline is otherwise drained at V073) and duplicates
nothing: `menu_sim.py` proves per-option reward BOUNDS at full width and
by its own comment bypasses the clamp; the served ORDER 006 items own
escort ACCOUNTING and cap SIZE; V018/V033 own cross-game pacing rates.

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib Python file (exact-Fraction forward recursion + stationary rates,
the four behaviour models, the MC twin evaluator + 3σ agreement check,
gates F1–F4), one fixture JSON (the width table, the 3 role-tuples with
shipped positions/defaults, TIER_CAPS[I]/GLOBAL_MAX, `_FULL_MENU_XP` as
dedup witness, 6 policies, 4 behaviours with p ∈ {1/20, 1/4}, T ∈ {5, 20,
100}, both accountings, the 4 band constants, 20,000 episodes/cell, seeds
20261389–392, the F2 rationals 9961473/1048576 and 21502885715/3486784401,
the F4 hand trace), one REPORT.md with the 6×4×3×2 grid, per-policy band
verdicts, the ruling, and the named lane-side reproduction line — the
standing INTAKE/VERDICT grammar, nothing else.

**Recommendation: sim-ready** — every constant pinned here, four bands
registered before any code, seeds 20261389–392 above the verified
high-water 20261388, fully hermetic at verdict time, the drafting-time
landing computed in exact arithmetic and disclosed (predicted
REJECT-REORDER via the {0, 1/2} partition); the honest next step is the
sim itself.
