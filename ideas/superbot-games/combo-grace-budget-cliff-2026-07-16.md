# The combo grace window that hides one shared budget: a streak's per-action "any action ≤ G late is safe, forever" grace looks per-action-forgiving but actually spends from ONE shared grace budget whose cumulative depletion breaks the multiplier at a history-determined step floor(B0/ℓ)+1 — so the SMALLEST within-grace lateness rides the streak longest and loses the MOST multiplier when it silently snaps, and the strict "you only lose your streak on a real miss (ℓ > G)" contract is silent on every budget-depletion break

> **State:** sim-ready
> **Class:** game-mechanics (pipeline rotation — the standing ORDER 003
> GAME-MECHANICS slot, round 17; round 17 opened at fleet backlogs with P081
> (#448 → VERDICT 094 REJECT) and served venture with P082 (#450 → VERDICT 095
> REJECT), so game mechanics is next per ORDER 004 rule 3, confirmed against the
> slot's own spacing-4 history …P063, P067, P071, P075, P079 → P083. Source: the
> slot returns to superbot-games, LOCALLY READABLE firsthand — the P063
> precedent (fleet-slot taps live in the source lane's section when the verdict
> consumer is that lane); pokemon-mod-lab, the only never-drawn games lane,
> stays excluded as DARK (walled, docs/CAPABILITIES.md).)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build).
> Verdict consumer: menno420/superbot-games — the lane owns the pacing/throttle
> economy this head models (the shipped shared-budget precedent
> `games/mining/core/energy.py`) and would own the combo/streak multiplier this
> head prices as a DESIGN surface.
> **Grounding:** https://github.com/menno420/superbot-games@5db902a36b377d007b226445c2eb5bc20bf4d70f · fetched 2026-07-16T14:14:06Z
> *(pin annotation: FIRSTHAND, public shallow clone read this session — the
> P063 superbot-games precedent. HONEST SCOPE: the lane ships NO combo/streak/
> grace multiplier at this HEAD (`grep -rniE 'combo|streak|\bgrace\b' games/`
> returns only weight/yield/mine MULTIPLIERS, never a streak system). This is a
> DESIGN head: it transfers the STRUCTURE of the lane's shipped shared-budget
> pace surface — `games/mining/core/energy.py` (`MAX_ENERGY = 60`, `DIG_COST =
> 1`, `REGEN_SECONDS = 10` → the sim-pinned ~360-digs/active-hour throttle,
> `RESTORE_VALUES = {ration:25, energy drink:50, cooked fish:30}`, capped at
> `MAX_ENERGY`, settled from a stored `(value, timestamp)` pair) — a
> per-action-looking pace brake that is in fact ONE shared depleting budget with
> a cap and passive replenishment — onto a proposed combo-multiplier surface.
> Companion in-repo reads (readable here, cited not re-clone): the game-mechanics
> pacing corpus `ideas/superbot-games/explore-action-pacing-quest-mint-2026-07-13.md`
> (per-source cooldown × combined window) and
> `ideas/superbot-games/mining-booster-bypass-throttle-seal-2026-07-13.md`
> (restore-rate caps on the same 360/h throttle). The sim itself is fully
> hermetic: zero repo/network reads at verdict time, every fixture constructed
> in-sim from the pinned integer constants below.)*

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous
pipeline) and ORDER 004 rule 3's rotation — round 17 opened at fleet backlogs
(P081), served venture (P082), so this slice serves the GAME-MECHANICS slot. The
harvested object is the lane's pacing economy: the owner chose a shared
energy/regen BUDGET "instead of a per-dig cooldown" (energy.py header, 2026-06-22
balance note), and this head asks what happens when that same
shared-budget-behind-a-per-action-face pattern governs a combo/streak
MULTIPLIER instead of a dig faucet — the surface the lane's completion wave will
reach for the moment it wants "reward a hot streak, forgive the occasional slow
turn."

## The folk belief

The forgiving-streak design sentence, the one a player reads off the tooltip and
a designer writes in the balance doc: **"any action within the grace window is
safe — miss the ideal beat by up to G and your streak survives; you only ever
lose the multiplier on a REAL miss (an action later than G)."** Stated per
action, it is exactly the both-sided comfort of a per-dig cooldown: each action
is independently judged safe-or-not, so a player who is *consistently a little
late* (steady lateness ℓ ≤ G every action) reads themselves as permanently safe
— "I'm always inside the window, so I never break." The load-bearing corollary,
uninspected: that "inside the window forever" implies "streak survives forever."
It does not, the moment the grace is funded by ONE shared budget rather than
re-judged per action. A shared budget with replenish only on the CLEAN action
(ℓ ≤ 0) drains by exactly ℓ every within-grace action and is never refilled
while you lean on it; the per-action test "ℓ ≤ G?" stays TRUE at every step right
up to the step where the accumulated spend exceeds the budget, and then the
streak snaps — silently, because a budget-depletion break is not a "real miss"
(no single action was later than G) and the strict miss-contract never mentions
it. The comfort sentence is TRUE on its own grid (a genuine real miss, ℓ > G,
does break at once — registered), and INVERTED on the budget it never names.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Model the streak as a deterministic budget automaton, pinned verbatim in the
fixture. State per streak: a shared grace budget B (starts B0, capped Bmax) and a
multiplier m (starts 1, +1 per recognized action, capped M, reset to 1 on break).
Each action arrives with a lateness ℓ (ticks past the ideal period P). The
transition, evaluated in this order:

1. **Break check FIRST.** The streak breaks (m → 1) at the FIRST action where
   EITHER **(a)** the budget cannot cover the lateness — `B − ℓ < 0` — OR **(b)**
   the action is a real miss — `ℓ > G`. Either way the multiplier silently
   resets and the accumulated `m − 1` bonus is wiped.
2. **Otherwise the action is recognized:** `B ← min(Bmax, B − ℓ + R·[ℓ ≤ 0])` —
   spend ℓ from the budget, and replenish R only if the action was early/on-time
   (ℓ ≤ 0). `m ← min(M, m + 1)`.

For a player with STEADY constant lateness ℓ (the folk belief's own case — "I'm
always ℓ late"), the closed form is exact and the sim reproduces it to the step:

- **ℓ = 0** (on-time): every action replenishes R = 1 and spends 0, so
  `B ← min(Bmax, B + 1) = Bmax` forever — the budget never drains, the streak
  **survives indefinitely**. The folk belief is RIGHT here.
- **ℓ ∈ {1, 2, 3}** (within grace, ℓ ≤ G): no replenish (ℓ > 0), so
  `B` before action t is `B0 − (t−1)ℓ`, and the break fires at the first t with
  `B0 − (t−1)ℓ < ℓ`, i.e. **break_step = ⌊B0/ℓ⌋ + 1**. At B0 = 10 that is
  **ℓ=1 → step 11, ℓ=2 → step 6, ℓ=3 → step 4** — every within-grace steady
  pattern breaks at a FINITE, history-determined step. The folk belief is WRONG
  here, and the break is a budget break, not a real miss (ℓ never exceeds G).
- **ℓ > G** (e.g. ℓ = 4): break (b) fires at step 1 — the genuine real miss the
  contract does describe.

**The forgiveness inversion.** The multiplier silently wiped at the break is
`min(break_step − 1, M) = ⌊B0/ℓ⌋` (all within-grace losses are ≤ 10 < M = 25, so
the cap never binds): **ℓ=1 loses 10, ℓ=2 loses 5, ℓ=3 loses 3.** The loss is
STRICTLY DECREASING in ℓ. Per action, being ℓ = 3 late "feels" three times
riskier than ℓ = 1; at the STREAK level it is the exact opposite — the player
who leans LIGHTEST on grace each action (ℓ = 1) rides the longest streak and
therefore suffers the BIGGEST single-streak multiplier loss (10, more than 3× the
ℓ = 3 player's), while the per-action-riskiest within-grace player loses least.
The smallest habitual lateness is the most expensive habit, and nothing in the
per-action grace test tells the player so.

**The silent-break contract gap.** A budget-depletion break emits no "real miss"
signal — no single action was later than G — so a UI/telemetry surface that keys
on the miss-contract ("streak lost: you were ℓ > G late") never fires on any of
the within-grace breaks; the player watches a 10× multiplier vanish on an action
that was, per the tooltip, "safe." This is the streak analogue of the mining
energy surface's own design honesty: energy.py stores `(value, timestamp)` and
SETTLES on read precisely so the budget is legible; a combo multiplier that
hides the budget behind a per-action grace face removes exactly that legibility.

**Two priced repairs, both in-model:**
- **(a) grace-low warning** — fire a one-shot "grace running low" exactly when
  the NEXT action would break (`B_after − ℓ < 0`). For steady ℓ this fires
  exactly ONCE per streak, at step `break_step − 1` (ℓ=1 → step 10, ℓ=2 → step 5,
  ℓ=3 → step 3), and on the ℓ = 0 cohort it fires ZERO times (budget-after is
  always Bmax ≥ ℓ) — zero false positives, the legibility the silent break lacks.
- **(b) replenish-on-within-grace** at rate R' = 1 — refill on ANY within-grace
  action, not only the clean one. Net budget change per within-grace action
  becomes `−(ℓ − 1)`, so **ℓ = 1 survives forever (net 0 — the folk belief made
  true for the lightest habit)**, while ℓ ≥ 2 still drains: the break moves to
  `⌊(B0 − ℓ)/(ℓ − 1)⌋ + 2`, i.e. **ℓ = 2 → step 10 (exactly B0), ℓ = 3 → step 5**
  — a strict extension over the baseline (6 → 10, 4 → 5) that closes the ℓ = 1
  gap entirely but only DEFERS the rest. (a) buys legibility with zero state; (b)
  buys the lightest-habit survivor at the price of one changed constant and a
  partial fix — the structured choice the verdict routes.

Every registered numeral above was produced live this session by the drafting
script (V080 live-verify + V084 NO-DERIVED-LITERALS, scratchpad `draft_p083.py`,
stdlib-only): **35/35 checks PASS, exit 0**, sim == closed form on every steady
pattern, both repairs' break steps sim-verified against their closed forms.

## Pinned model (committed constants — all integers, all pinned)

- **Timing/grace:** ideal action period `P = 10` ticks (context for lateness ℓ;
  the budget law is ℓ-driven, P is not a free dial here); per-action grace
  threshold `G = 3` ("any action ≤ G late is individually safe").
- **Shared budget:** `B0 = 10` (start), `Bmax = 10` (cap), replenish `R = 1` per
  action with `ℓ ≤ 0`; a within-grace late action (0 < ℓ ≤ G) spends ℓ, no
  replenish.
- **Multiplier:** +1 per recognized action, cap `M = 25`, reset to 1 on break.
- **Break rule (checked BEFORE the budget update):** break at the first action
  with `B − ℓ < 0` (budget) OR `ℓ > G` (real miss); else
  `B ← min(Bmax, B − ℓ + R·[ℓ ≤ 0])`.
- **Registered census anchors (F3), exact:** steady break steps
  `{ℓ=0: ∞, ℓ=1: 11, ℓ=2: 6, ℓ=3: 4, ℓ=4: 1(miss)}`; steady multiplier losses
  `{ℓ=1: 10, ℓ=2: 5, ℓ=3: 3}` (= break_step − 1 = ⌊B0/ℓ⌋), strictly decreasing,
  max at ℓ = 1; repair-(a) warning steps `{ℓ=1: 10, ℓ=2: 5, ℓ=3: 3}`, ℓ=0 warns
  0; repair-(b) break steps `{ℓ=1: ∞, ℓ=2: 10, ℓ=3: 5}`.
- **Closed-form contacts (typed must-equal C1–C2):** **C1** steady sim break_step
  == `⌊B0/ℓ⌋ + 1` for ℓ ∈ {1,2,3}; **C2** repair-(b) sim break_step ==
  `⌊(B0 − ℓ)/(ℓ − 1)⌋ + 2` for ℓ ∈ {2,3}, and ℓ = 1 survives to horizon.
- **Arm R (seeded, REPORTING-ONLY):** per trace EXACTLY 3 `rng.randint` draws in
  registered order — lateness pattern ℓ ∈ [0, 4], horizon cap ∈ [5, 50], salt ∈
  [1, 1000] (drawn-and-logged, unused) — one `random.Random` per seed; classes
  {SURVIVE (ℓ=0), SILENT-BREAK (ℓ∈{1,2,3} budget), REAL-MISS (ℓ=4)}. N = 20,000
  on seed **20261726** (drafting preview census: SURVIVE **4,595** · SILENT-BREAK
  **11,427** · REAL-MISS **3,978**; draws exactly **60,000**; class-stream digest
  `3bfa073726f7`), stability N = 8,000 on **20261727** (preview 1,844 / 4,534 /
  1,622; draws **24,000**; digest `6f857d0afcf4`), presentation shuffle
  **20261728** (presentation legs only). NO statistical gate rides Arm R — its
  gates are the 3N draw sentinel and exact reproducibility. Aux seed **20261729**,
  reserved, NEVER read by any leg (the P054–P082 aux convention). Seeds
  20261726–729 allocated from 20261726 per the V095 heartbeat baton
  (20261722–725 are P082/V095's registered set).
- **Runtime disclosure:** the whole drafting battery (the steady census over
  ℓ ∈ {0,1,2,3,4}, both repairs, N = 28,000 seeded reporting traces, byte-identity
  check) runs in well under a second; every decision leg is deterministic integer
  arithmetic.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "the per-action grace contract is wrong as doctrine: 'within the
  window ⇒ safe forever' fails whenever the grace is funded by one shared budget —
  every steady within-grace lateness breaks the streak at a finite,
  history-determined step, and the break is silent under the strict miss-contract
  because no single action exceeded G": **(R1, the folk belief made precise)** the
  census over ℓ ∈ {0,1,2,3} lands `{ℓ=0 survives; ℓ=1,2,3 break at 11,6,4}` — NOT
  "all within-grace survive"; the ℓ > G control breaks at step 1 (the true real
  miss). **(R2, the cliff position)** steady sim break_step == `⌊B0/ℓ⌋ + 1` exact
  across the pinned grid (C1). **(R3, the forgiveness inversion)** the silent loss
  `= break_step − 1 = ⌊B0/ℓ⌋ = {10,5,3}` is strictly DECREASING in ℓ, max at
  ℓ = 1 (10 of M = 25) — the lightest per-action habit is the costliest streak.
  **(R4, the priced repairs)** repair (a) fires once per streak at break_step − 1
  with zero false positives on the ℓ = 0 cohort; repair (b) at R' = 1 makes ℓ = 1
  survive (net 0) and moves ℓ = 2 to step 10, ℓ = 3 to step 5, each == its closed
  form (C2). (Checked FIRST because the costly direction is a silently snapped
  streak: the player did exactly what the tooltip called safe and lost a
  history-long multiplier with no signal — a designed reward that punishes the
  most-compliant habit hardest.)
- **INVALID** (controls misbehaving — report, no ruling): any F1–F5 gate failure
  below.
- **APPROVE** — "the contract holds as doctrine: no steady within-grace pattern
  breaks the streak": every ℓ ∈ {1,2,3} survives to the horizon — arithmetically
  excluded by the ℓ = 1 cell (B0 = 10 is exhausted after 10 spends of 1, break at
  11 — F4a, pencil); mutually exclusive with REJECT.
- **NULL** — anything else; pre-registered axes: **model-semantics mismatch** (the
  verdict session's read of the transition contradicts a pinned clause — the
  break-before-update order, the replenish-only-on-clean rule, the `< 0` vs `≤ 0`
  budget test, or the checked-first miss rule; the corrected law + re-derived
  census is the finding, and this axis is LIVE: the `<` boundary in `B − ℓ < 0`
  moves every break step by one if misread as `≤`); **constant-convention axis**
  (the constants B0/G/R/M are a canonical DESIGN choice, not copied from a shipped
  combo system — none exists; if the census is asserted under a specific committed
  tuple and a different but defensible tuple flips a clause, the corrected tuple
  ships with the finding); **design-transfer axis** (the head transfers the
  energy-budget STRUCTURE to a multiplier the lane has not built — if the sim
  judges the transfer itself unsound as a model of any plausible combo mechanic,
  that is a finalized NULL naming the mismatch, never a re-run request).

GATE POWER, computed at registration: the sim is FULLY DETERMINISTIC in every
decision leg — each clause is an exact census over a finite steady grid or an
exact closed-form contact; the only seeded arm is reporting-only with NO
statistical gate (sole gates: the 3N draw sentinel and exact reproducibility,
pass probability 1 for a correct implementation); JOINT pass probability across
all gates for a correct implementation = 1 EXACTLY (the P059–P082
no-stochastic-gate precedent). MARGIN LEDGER, disclosed: every REJECT clause is
an exact equality — the registered surfaces are the break-step map
{11, 6, 4, 1}, the loss map {10, 5, 3}, the repair-(a) warning map {10, 5, 3}
with the ℓ = 0 zero, and the repair-(b) map {∞, 10, 5}; the one strict inequality
(loss decreasing in ℓ) carries margin ≥ 2 at every adjacent pair. A census
landing off these exact values is INVALID-or-NULL by the pre-registered axes,
never a "close enough."

## Gates (run INVALID on any failure)

- **F1 — model identities:** the break check is evaluated BEFORE the budget
  update on every step; `B ≤ Bmax` invariant holds; the multiplier reset wipes
  exactly `m − 1`; every steady trace is deterministic (two runs identical); the
  Arm-R draw counter == 3N exactly.
- **F2 — the structure results, exact:** (a) the steady census over
  ℓ ∈ {0,1,2,3,4} at the registered break steps; (b) the loss map and its strict
  monotonicity (R3); (c) repair-(a) once-per-streak at break_step − 1 + the ℓ = 0
  zero-false-positive; (d) repair-(b) break steps sim == closed form.
- **F3 — census anchors (reference values, exact):** the break-step map, the loss
  map, the repair maps, and the Arm-R previews/digests, verbatim from the Pinned
  model block.
- **F4 — the hand worlds (pencil):** (a) B0 = 10 is exhausted after 10 spends of
  ℓ = 1, so the ℓ = 1 streak breaks at step 11, not ∞ — APPROVE excluded by
  inspection; (b) ⌊10/3⌋ + 1 = 4 — the ℓ = 3 cliff by inspection; (c) at ℓ = 0 the
  clean-action replenish pins B at Bmax, so the budget never drains — the survive
  cell by inspection; (d) repair (b) net change at ℓ = 1 is `−1 + 1 = 0` — ℓ = 1
  survives by inspection.
- **F5 — degeneracy/convention controls:** the ℓ = 0 survivor and the ℓ > G
  immediate real-miss are both present (the contract's two TRUE cells registered
  as prominently as the silent ones); repair (a) fires zero times on the survivor
  cohort; repair (b) strictly EXTENDS survival vs baseline (never shortens); the
  Arm-R taxonomy is total on all N traces (SURVIVE + SILENT-BREAK + REAL-MISS ==
  N); stdout + results byte-identical across two process runs (deterministic
  parsing; Arm R pinned to a stated CPython minor).

## Expected landing (DISCLOSED per the P048–P082 exact-arm norm)

REJECT on all four conjuncts, at the drafter's exact values (the sim re-derives
everything from scratch and must not trust these; every number computed live at
drafting — `draft_p083.py`, **35/35 checks PASS, exit 0**): **R1** — the census
lands {ℓ=0 survives; ℓ=1,2,3 break at 11, 6, 4} with the ℓ > G control at step 1;
**R2** — steady break_step == ⌊B0/ℓ⌋ + 1 exact; **R3** — losses {10, 5, 3},
strictly decreasing, max at ℓ = 1; **R4** — repair (a) warns once at
break_step − 1 with zero ℓ = 0 false positives, repair (b) survives ℓ = 1 and
moves ℓ = 2 → 10, ℓ = 3 → 5. Falsifiability is real and named on three axes:
(i) the **model-semantics world** — one misread of the break-before-update order
or the `< 0` boundary moves every break step together, and the model-semantics
NULL prices exactly that; (ii) the **design world** — if the transfer from the
shipped energy budget to a hypothetical combo multiplier is judged an unsound
model of any real streak mechanic, the design-transfer NULL is a finalized
finding; (iii) the **constant world** — a defensible alternative (B0, G, R)
tuple that flips a clause ships the corrected tuple (the constant-convention
NULL). Disclosed sharpenings, reporting-only: the Arm-R census (random
ℓ ∈ [0,4] × horizon [5,50] sampled 20,000×) lands SILENT-BREAK **11,427 ≈ 57%**
(digest `3bfa073726f7`) — most random within-window players sit in the silent
regime; and the production color — the lane's shipped shared-budget precedent
(`games/mining/core/energy.py`, the 360-digs/hour throttle chosen "instead of a
per-dig cooldown") is the exact structure this head warns a future combo
multiplier will inherit, quoted per the realized-probe precedent as color, never
a fixture.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Verdict consumer: superbot-games — the lane owns the pacing/throttle economy this
head models and would own the combo/streak multiplier it prices. REJECT →
paste-ready structured choice, recommendation first per Q-0263.2: **(a,
recommended)** design the combo multiplier with the budget MADE LEGIBLE — carry
the grace budget as an explicit settled `(value, timestamp)`-style surface (the
energy.py pattern the lane already ships and unit-tests) AND fire the grace-low
warning of repair (a): zero new steady-state cost, one-shot per streak at
break_step − 1, zero false positives on the clean cohort, and it closes the exact
silent-break gap the strict miss-contract leaves — the player sees the cliff
coming instead of watching a 10× multiplier vanish on a "safe" action. **(b)**
replenish-on-within-grace (repair b, R' = 1) — makes the lightest habit (ℓ = 1)
truly survive-forever as the tooltip promises, at the price of one changed
constant and a still-silent (merely deferred) break for ℓ ≥ 2; pairs with (a)
rather than replacing it. **(c)** status quo + document — ship the shared-budget
combo but AMEND the tooltip/balance doc to state the budget explicitly ("your
grace is a shared reserve that refills only on an on-time action"), so the folk
belief is never sold. Known co-consumers of the verdict: the mining energy
surface (`energy.py` — the same shared-budget-behind-a-per-action-face pattern,
already legible via settle-on-read; the transfer runs BOTH ways — a combo built
this way should borrow energy's legibility), the two in-repo pacing heads
(explore action-pacing, mining booster throttle — each prices a DIFFERENT dial on
the same throttle economy; this head prices the streak-reward face of it), and —
the transferable audit — every fleet mechanic that presents a SHARED budget
behind a PER-ACTION test (rate limits, cooldown pools, retry budgets): a
per-action "am I under the limit?" check is silent on cumulative-budget
depletion, and the fix is to surface the budget, not to re-judge the action.

## Dedup

Tree-wide `rg -i 'combo|streak|grace|multiplier|budget.*deplet|shared.budget'`
(bootstrap.py/.substrate excluded): the superbot-games hits are the mining/
fishing/dnd WEIGHT and YIELD multipliers (bias dials, no streak state) and the
two pacing heads; no idea file or proposal prices a streak multiplier, a shared
grace budget, or a cumulative-depletion cliff. Nearest priors argued distinct:
**explore-action-pacing-quest-mint → P031** and **mining-booster-bypass-throttle-seal
→ P035** — the SAME throttle economy, zero shared machinery: both price a
per-source cooldown / restore-rate DIAL against admission or coin-profit bands,
taking each action's judgment as independent; this head prices a CUMULATIVE
shared-budget state whose per-action face hides a history-determined cliff — the
verdicts compose (a well-tuned cooldown can still hide a silent streak break).
**menu-width-leverage-inversion → P063** — the method kin (a shipped-mechanic
inversion priced by exact arithmetic with a data-only-vs-mechanic-change repair
fork), different object entirely: a menu-truncation leverage law over scene
orderings, no budget dynamics, no streak state, and its "inversion" is
rate-falls-as-width-rises, not loss-rises-as-habit-lightens. **P081 → V094
(guard-fires dedupe regime cliff)** — the closest DYNAMICS kin (a deterministic
automaton whose orbits are exactly computable, priced against its own comfort
comment with the true-sentence-survives move), but a different object class (a
windowed dedupe's tail-scan renewal vs a streak budget's single-cliff depletion —
no rotating alibi, no reads/parses bill here; a single monotone drain to one
history-determined break) and a different lane (substrate-kit vs superbot-games).
**P082 → V095 (owner-gate recognition cliff)** — the method sibling from the
prior slot (a shipped mechanism priced against its sold fail-safe sentence with
the disposition-grid-TRUE / everywhere-else-INVERTED structure and a priced
repair), but that head's object is a PARSER's single-edit recognition census with
no dynamics; this head's object is a temporal BUDGET whose break step is a closed
form in the history length. No proposal P001–P082 and no verdict V001–V095 prices
a streak/combo multiplier, a shared grace budget, or a cumulative-depletion
break. This head's own additions to the battery: a shared-budget-behind-a-
per-action-face automaton as the decision object, a FORGIVENESS INVERSION law
(streak loss strictly decreasing in per-action lateness), a silent-break contract
gap (the strict miss-contract blind to every budget break), and a design-transfer
grounding (a shipped shared-budget pace surface mapped onto an unbuilt reward
surface, with the transfer named as its own NULL axis).

## Model basis (declared model-dependence — the P024 discipline)

Four modeling commitments carry the verdict, each pinned and directional:
(1) the TRANSITION is a pinned deterministic automaton (break-before-update,
replenish-only-on-clean, checked-first miss) — carried with the model-semantics
NULL because the `< 0` boundary and the update order are each one misread from
moving every census cell; (2) the CONSTANTS (B0 = Bmax = 10, G = 3, R = 1,
M = 25, P = 10) are a canonical DESIGN choice, NOT harvested from a shipped combo
system (none exists at the grounding HEAD) — the constant-convention NULL prices
a tuple-driven clause flip, and the head says plainly that the lane ships no
streak multiplier; (3) the STEADY-lateness family is the folk belief's OWN case
("I'm always a little late") — a witness family, not a measure over all input
sequences: the claim is that within-grace steady patterns break (existential and
exact on the registered grid), and Arm R's random-sequence sampling is
reporting-only for exactly that reason; (4) the GROUNDING is a DESIGN TRANSFER —
the shared-budget STRUCTURE is read firsthand from the shipped `energy.py`
(`MAX_ENERGY`/`REGEN_SECONDS`/`RESTORE_VALUES`, settle-on-read), and the head
transfers that structure to a proposed multiplier surface, naming the transfer as
its own NULL axis rather than claiming a combo system the lane has not built. The
comfort sentence is priced against its own best formalization: the per-action
grace test where it is TRUE (the ℓ = 0 survivor and the ℓ > G real miss) is
registered as R1/F5, so the head cannot be read as a straw man.

## Probe report (v0, 2026-07-16)

> Single-pass battery (panel not escalated: self-contained mechanism probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep returned
> the mining/fishing/dnd weight-multiplier hits (no streak state) and the two pacing
> heads (per-action dials) as the only collisions; no prior head prices a shared grace
> budget or a streak cliff. (b) **kill test NOT triggered** — no recorded drop of this
> mechanism on any card; P031/P035 explicitly price DIFFERENT dials on the same throttle
> economy. (c) **feasibility + liveness arithmetic checked LIVE** — every registered
> numeral ran this session (draft_p083.py, 35/35 PASS, exit 0): the steady census, both
> repairs against their closed forms, and the seeded Arm-R previews with their 3N
> sentinels; expected landing DISCLOSED (REJECT), all rulings reachable, the
> model-semantics / design-transfer / constant falsifiability worlds named. (d)
> **grounding reachability** — the source lane was clonable firsthand this session
> (public shallow clone succeeded, `git rev-parse HEAD` = 5db902a3…); the HONEST scope
> (no shipped combo system) is stated in the pin annotation, not hidden.

**1. What is this really?** A pre-registered EXACT MEASUREMENT of a forgiving-streak
DESIGN contract — "any action within the grace window is safe forever; you only lose
the streak on a real miss" — taken on the contract's own most natural implementation
(one shared grace budget behind a per-action grace test, structurally the lane's shipped
energy budget): a steady-lateness census over a pinned budget automaton, with the two
cells where the contract is TRUE (the on-time survivor, the real miss) registered beside
the within-grace regime where it inverts, and the forgiveness inversion (loss decreasing
in per-action lateness) priced as its own clause.

**2. What is the possibility space?** (i) Don't run it — the round-17 game-mechanics
slot goes unserved. (ii) A different game-mechanics head — the lane's pacing dials are
priced through P031/P035; the streak-reward FACE of the same economy is unpriced and is
the surface the completion wave will reach for next. (iii) File a design note ("shared
budgets hide cliffs") — states the intuition without the laws; the exact treatment gives
the regime map: WHICH within-grace patterns break, at WHICH step, how much multiplier is
silently lost, and two repairs priced by their exact effect. (iv) A playtest — finds a
broken streak once without the closed form; here every decision cell is a registered exact
census and the random arm is demoted to reporting. (v) This head. (vi) Over-scope (model
the full reward economy, XP curves, the energy faucet itself) — each a named follow-up,
none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?** One
~150-line stdlib file: one budget-automaton step function, a steady-lateness driver, two
repair variants, and integer counters — that single kernel yields the steady census, the
loss map, the forgiveness inversion, both priced repairs, and the seeded reporting traces;
a verdict session runs it cold in under a second.

**4. What breaks it? (assumptions made explicit)** (a) **The transition is pinned, not
executed against a shipped system** — no combo system exists; the model-semantics and
design-transfer NULLs price a misread and an unsound transfer. (b) **The steady family is
a witness space** — prevalence rides only the reporting Arm R; the decision claim is
existential-and-exact on the registered grid. (c) **The constants are a design choice** —
registered explicitly; the constant-convention NULL prices a tuple-driven flip. (d) **Band
placement could cherry-pick** — every band is an exact value committed before the sim, the
landing is DISCLOSED, and the TRUE cells (the survivor, the real miss) are registered as
prominently as the silent breaks.

**5. What does it unlock?** A legible combo multiplier for the games completion wave (the
grace-low warning + the settled-budget surface, both zero-to-one-constant); the inversion
result that tells a designer the most-compliant habit is the costliest, so the reward
curve can be tuned deliberately instead of by accident; and the transferable audit for
every shared-budget-behind-a-per-action-test surface in the fleet (rate limits, cooldown
pools, retry budgets — a per-action limit check is silent on cumulative depletion).

**6. What is the cheapest experiment that decides it?** The whole head IS the cheapest
deciding experiment: a handful of deterministic steady-lateness walks of a 10-unit budget.
The single cheapest probe if a reader doubts it is pencil: B0 = 10 spent one unit at a
time survives 10 within-grace actions and breaks on the 11th — one line, no computer, and
APPROVE ("survives forever") is dead.

**7. What would make this a mistake to run?** If the exact treatment were unavailable (it
is not — every decision quantity is a finite deterministic census), if the object
duplicated a prior head (it does not — P031/P035 price per-action dials with the judgment
taken as independent; zero shared-budget/streak collisions), or if the disclosed REJECT
made the run theater. It does not: the value is the independent hermetic re-derivation
(the sim re-writes the automaton and must reproduce ⌊B0/ℓ⌋ + 1 from scratch), the honest
design-transfer scope (the sim can rule the transfer unsound as a finalized NULL), and
both non-REJECT rulings genuinely reachable (APPROVE is one boundary misread away; the
constant and design NULLs are one defensible-alternative away).

**8. How will we know it worked?** A committed sim-lab report with: the steady break-step
census, the multiplier-loss map + its monotonicity, the two priced repairs against their
closed forms, the F1–F5 gate results, the verdict token against the pre-registered bands,
Arm R's measured class census beside the exact grid (reporting-only, 3N draws asserted),
and a byte-identity note. A clean run reproduces the drafter's disclosed values (breaks
11/6/4, losses 10/5/3, repair-(b) 10/5) from scratch, or — the more interesting outcome —
DISAGREES and pins the drafter's misread, which the pre-registered rule then rules on
honestly (the model-semantics, constant-convention, and design-transfer NULL axes exist
for exactly that).

**Recommendation: sim-ready**
