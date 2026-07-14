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
> **Grounding:** https://github.com/menno420/superbot-games/blob/e3930f134119dd36d9e7f37a7dccb4f4b33e3805/games/dnd/core/resolver.py · fetched 2026-07-14T11:31:51Z
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

- **Dedup:** no proposal 001–062 and no sim-lab verdict V001–V073 touches
  menu width, option ordering, prefix truncation, or the message-XP
  leverage axis (local outbox + rolled archive swept for
  leverage/menu/width/prefix/dnd terms; nearest kin listed in Relations —
  P031/P035 rate-constants, ORDER 006 (6)/(7) escort-accounting and
  cap-size, all disjoint by constant and by file).
- **Firsthand:** superbot-games shallow clone @
  `e3930f134119dd36d9e7f37a7dccb4f4b33e3805`, fetched 2026-07-14T11:31:51Z,
  `git log -1` verified. All eight companion files read at that pin; every
  constant above traced to its defining line.
- **Closed form:** the drafting-time landing (F2 rationals, the {0, 1/2}
  partition, the B2/B4 headline cells) computed this slice in exact
  `fractions.Fraction` from the role graph; committed to this file BEFORE
  the sim exists — the harness confirms or refutes, it does not discover.
- **Seeds:** 20261389–392, strictly above the V073 high-water 20261388;
  boundary-aware re-sweep at drafting HEAD `8e171bd` (regex
  `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)`, bootstrap.py/.substrate excluded)
  found no genuine allocation above 20261388; the standalone numerals
  20261542/20261664/20261833 are the documented Fraction-numerator
  data-not-seed specimens.
- **Hermeticity:** verdict-time sim reads NOTHING outside its own fixture
  (constructed from this file's pinned constants) — the FIRSTHAND read is
  drafting-time grounding, per the venture-slot/game-slot split the P061
  card asked to be stated per-slot: the GAME slot harvests firsthand at
  drafting and sims hermetically at verdict.
