# Creature-PvP rarity vs skill — does the committed level-normalized ruleset actually let a Common team counter an Epic, or is collection grind the pay-to-win side door?

> **State:** sim-ready
> **Class:** game-mechanics (pipeline rotation — the standing ORDER 003
> GAME-MECHANICS slot, round 8; rounds 1–7 were P020 casino odds → V022 reject,
> P023 entry fee → V025 reject, P027 comp/stipend → V029 null, P031 explore
> pacing → V033, P035 mining booster throttle seal → V046 null, P039 Gloamline
> survival ceiling → V050 approve, P043 Brineward band necessity → V054) ·
> **Target:** `menno420/superbot` (the hub — owns the creature battle engine,
> the catalog, and the eventual ranked-PvP surface this verdict prices; routing
> is the manager's per Q-0260, this repo never edits superbot files);
> verification target `menno420/sim-lab` per the Q-0264 pipeline
> **Grounding:** https://github.com/menno420/superbot@1cc553651a19016a4b1439f048b49e7baa28dfb1 · fetched 2026-07-13T21:25:33Z
> (shallow clone at drafting, HEAD committed 2026-07-13T21:53:48+02:00; every
> constant below quoted from `disbot/utils/creatures/battle.py`,
> `disbot/utils/creatures/creature.py`, `disbot/utils/creatures/encounters.py`,
> and `disbot/data/creatures/creatures.json` — all at that pin; subject sourced
> via the fleet game repos, pokemon-mod-lab DARK, skipped per the reading
> path's rule)

**Origin:** drafted under standing owner ORDER 003 ("continue coming up with new
ideas, that is your main purpose") in the ORDER 004 rule-3 rotation — round 8:
P045 served fleet-backlogs (#343), P046 served venture (#348), so this head is
the round's GAME-MECHANICS slot. The last two game rounds (P039, P043) both
drew from gba-homebrew, so round 8 rotates the SOURCE to the hub's own creature
game — deliberately outside the nine queued SIM-REQUEST domains (local ORDERs
005/006 cover venture pricing ×4, superbot-idle economy, and superbot-games
mining/fishing/dnd/exploration; creature battle balance is in none of them).

## The idea

superbot's creature PvP engine (`disbot/utils/creatures/battle.py` @ `1cc5536`)
was built around one owner-ratified fairness rule: ranked PvP normalizes every
creature to a flat level (`NORMALIZED_LEVEL = 50`) because raw levels make a
1v1 deterministic — the pay-to-win outcome Q-0039 forbids. The module carries
two load-bearing lines, neither ever cross-rarity-tested:

1. *"Total stat budget per rarity — rarer = stronger, but level + type + move
   choice still let a Common counter an Epic."* (the `RARITY_BUDGET` comment)
2. *"Flat-level PvP makes **types + team-building + ordering + move choice**
   decide, so it rewards *skill*, not *time spent*."* (module docstring)

Level normalization killed the LEVEL grind axis. But rarity is the OTHER
time-spent axis, and it is raw stats: `RARITY_BUDGET = {Common: 200, Uncommon:
230, Rare: 260, Epic: 300}` — an Epic carries **1.5× a Common's entire stat
budget at the same level**, and the committed catch economy prices that budget
in grind (`RARITY_ENCOUNTER_WEIGHT = {100, 45, 18, 6}`, `RARITY_CATCH_BASE =
{0.90, 0.65, 0.40, 0.20}` @ `creature.py`). The in-repo design simulator
(`tools/game_sim/creature_battle_sim.py`) that stamped the ruleset PLAYABLE
checked type balance, raw-level dominance, normalized fairness, skill impact,
status-move value, and catch grind — **every battle check on same-rarity or
randomly-mixed rosters; it never once put a Common team across the table from
an Epic team**. So whether the type chart (`1.5×/0.67×`), move choice
(Normal 9 vs element 12), lead ordering, and setup buffs can actually climb a
committed 200-vs-300 budget wall is an open arithmetic question about
committed constants. Sharper still: in ranked PvP the comment's "level" lever
is normalized away by the engine's own rule — only type + team-building +
ordering + move choice remain. If they cannot counter, collection rarity is a
pay/time axis in ranked PvP and the P2W shape re-enters through the side door
the normalization was adopted to kill; if they can, both lines deserve their
numbers before a ranked surface is built on them.

The catalog makes the question concrete and unique: at `1cc5536` there is
**exactly one Epic per element** — Infernox (Ember, tank), Abysscale (Tide,
balanced), Verdankor (Bramble, speedster), Stormfang (Spark, attacker),
Tectonix (Stone, balanced), Tempestra (Gust, speedster) — so THE all-Epic
"one of each element" team is a single committed artifact, not a modeling
choice. Commons come exactly two per element (one `balanced`, one `attacker`).

## The model (committed constants quoted @ `1cc5536`; the engine re-implemented verbatim, hermetic)

**Combat (all committed):** 6 elements on `ELEMENT_CYCLE = (Ember, Tide,
Bramble, Spark, Stone, Gust)`; an element is strong (×1.5) vs the next two,
weak (×0.67) vs the previous two, neutral vs its opposite; `Normal` always
×1.0. Stats derive from `round(budget · weight / 4)` with `ARCHETYPE_WEIGHTS`
attacker (0.9, 1.3, 0.7, 1.1) / tank (1.3, 0.8, 1.3, 0.6) / balanced (1, 1, 1,
1) / speedster (0.8, 1.2, 0.7, 1.3) over (hp, atk, def, spd) — Python-3
banker's rounding faithfully reproduced and disclosed (tank Epic derives
(98, 60, 98, 45), total 301 — the committed overshoot). Level 50 scaling: HP
×(1 + 0.06·49) = ×3.94, ATK/DEF/SPD ×(1 + 0.035·49) = ×2.715 — the off-mult
cancels in every atk/df ratio, so damage is level-invariant and HP pools grow;
both facts gate-checked. Four moves each: Strike (Normal, power 9), the
element signature (power 12, type chart applies), Bulwark (+DEF), Onslaught
(+ATK); buffs step +0.25 capped +0.50. Damage = `max(1, round((atk /
max(1, df)) · power · mult · jitter))`, jitter ~ uniform(0.85, 1.0). 6v6
lead-until-faint; each turn both leads act in SPD order (exact tie: one
`rng.random() < 0.5` coin flip); a KO denies the victim's action that turn;
stall guard 5000 (any battle reaching it invalidates the run — unmodeled
territory). All of it re-implemented from these quoted formulas in the
committed sim; zero imports from superbot at verdict time.

**Teams (pinned from the committed catalog):** the Epic side is THE committed
all-Epic team above, pre-ordering pinned to `ELEMENT_CYCLE` order. The Common
side sweeps three pinned element-complete compositions: **BAL** (the six
`balanced` Commons: Cindling, Rippling, Sproutle, Voltkit, Pebblet, Zephyrl),
**ATK** (the six `attacker` Commons: Emberpaw, Splashfin, Thornkit, Sparkpup,
Gravelpup, Gustling), **MIX** (balanced on even `ELEMENT_CYCLE` indices —
Ember, Bramble, Stone — attacker on odd — Tide, Spark, Gust). All combatants
at `NORMALIZED_LEVEL = 50`, fresh per trial (`fresh_team` semantics: full HP,
no buffs).

**Skill levers (all committed engine code):** the Common side always plays
MAX-SKILL — `order_type_aware` (stable-sort the team by descending
effectiveness vs the opponent's pre-ordering lead) + `policy_setup` (best
expected-damage move; finish a kill rather than buff; one opening +ATK when
un-buffed, ≥ 60% HP, and not slower). The Epic side's pilot is the grid's
second axis: **BEGINNER** (`policy_naive_element` — always the signature move,
even into a 0.67 resist — with the pinned `ELEMENT_CYCLE` lead order),
**MID** (`policy_best_damage`, pinned lead order), **SKILLED** (`policy_setup`
+ `order_type_aware`). Both type-aware orderings resolve against the
opponent's PRE-ordering lead, applied simultaneously (pinned, disclosed —
the engine itself gives ordering no second-mover privilege). Grid: 3 Common
compositions × 3 Epic pilots = **9 cells**, decision rows BEGINNER and
SKILLED, MID reported.

**Arm S (the DECISION arm — seeded MC, the P044 precedent):** the engine's
float math admits no closed form, so the decision arm is seeded MC with exact
per-run tallies: `random.Random(20261325)`, cells in pinned order
(composition outer, pilot inner), N = 20,000 battles per cell, one battle =
one pinned-order stream of jitter + tie-flip draws; `W(cell)` = Common-side
wins / N as an exact `fractions.Fraction`. SE at N = 20,000 is ≤ 1/283 —
the decision bands sit ≥ 14 SE from each other (2/5 vs 1/2), pre-checked.
Reporting legs on the same seed, pinned order after the grid: mirror-match
calibration (BAL vs BAL, both MAX-SKILL — W must land within 1/50 of 1/2,
an anomaly gate); naive-vs-naive BAL vs Epic (the raw wall, no skill
anywhere); the Rare gradient (BAL vs the committed all-Rare team — Magmaul,
Coralisk, Thornmaw, Arcwing, Boulderon, Galeon — BEGINNER and SKILLED
pilots). Stability leg: seed **20261326**, the 9-cell grid at N = 5,000, must
reproduce the ruling class through both twin evaluators. Sensitivity legs
(reporting-only, seed **20261327**, 9-cell grid at N = 5,000 each): jitter
uniform(0.7, 1.0); jitter degenerate ≡ 0.925 (the expected-damage constant);
`BUFF_CAP = 0.75`; level 5 instead of 50 (the docstring calls the normalized
value cosmetic — this prices that claim: the off-mult cancels exactly, only
HP rounding and pool depth move). Aux seed **20261328** is never read by any
decision number. Seeds **20261325–20261328** sit strictly above the P046
registry high-water **20261324** (re-swept at drafting: digit-boundary regex
`(?<![0-9])20261[0-9]{3}(?![0-9])` + the range-notation companion over this
tree at HEAD `bb6afe7` and the sim-lab working copy at `c7fc1a0` — sim-lab
allocates none; its fishing-robustness block 20260881–1280 sits below the
proposal series' floor; the parallel V057 session consumes P046's 20261321–324
and allocates none).

**Arm E (exact stakes arm — seedless `fractions.Fraction` throughout):** the
committed catch economy priced exactly. Per encounter, P(catch specific
creature c) = (weight_c / 1884) · catch_c at pinned player level 50 (catalog
weights: 12 Commons ×100 + 12 Uncommons ×45 + 6 Rares ×18 + 6 Epics ×6 = 1884;
catch = min(0.95, base + min(0.20, 0.02 · 50)): Common 19/20, Rare 3/5, Epic
2/5). Expected encounters to complete a specific 6-creature team by max–min
inclusion–exclusion, `E[max] = Σ_{∅≠S} (−1)^{|S|+1} / Σ_{c∈S} p_c` (exact
regardless of the per-encounter exclusivity — one creature per encounter),
hand anchors gate-checked: a single specific Epic costs exactly **785**
encounters (p = (6/1884) · (2/5) = 1/785); six equal-p targets cost
(1/p) · 49/20. Output: E_epic (the committed all-Epic team), E_common (BAL),
and the **time-premium ratio TP = E_epic / E_common** — the exact grind
multiple the Epic team costs. TP is reporting-only for the decision but is
the verdict's stakes line: the ruling says whether that multiple buys
unanswerable ranked power (hand span: TP ≈ 39.6, exact Fraction printed by
the arm; the two hand anchors are the gates, the headline is the sim's).

**Gates (run invalid on any failure):** F1 effectiveness matrix — the full
7×6 hand table exact (incl. Normal row ≡ 1.0, opposite-element ≡ 1.0); F2
derived-stats hand table for all six used (rarity, archetype) pairs with
banker's-rounding values pinned (balanced Common (50, 50, 50, 50); attacker
Common (45, 65, 35, 55); tank Epic (98, 60, 98, 45); balanced Epic (75, 75,
75, 75); attacker Epic (68, 98, 52, 82); speedster Epic (60, 90, 52, 98));
F3 level-50 identities — HP mult 3.94 and off mult 2.715 exact, balanced
Common max_hp = 197, tank Epic max_hp = 386, and level-invariance of every
atk/df ratio asserted symbolically (60/50 = 1.2 at any level); F4 the
deterministic hand-traced 1v1 fixture — Cindling vs Infernox, both
`policy_best_damage`, jitter pinned ≡ 0.925 (fixture-only hook): Cindling
acts first (135.75 > 122.175 spd), per-turn damages exactly 6 (round(12 ·
0.925 · 135.75/266.07)) and 13 (round(12 · 0.925 · 1.2)), Infernox KOs on its
16th action with Cindling having dealt 96 ≤ 386 — the full event log
reproduced exactly; F5 theorem/anomaly gates — mirror match within 1/50 of
1/2; naive-vs-naive W < 1/2 expected-direction (loudly flagged, not
invalidating); zero stall-guard hits (invalidating); RARITY_BUDGET spread
300/200 = 3/2 asserted from the pinned table; F6 Arm E anchors — 785 exact,
the 49/20 equal-p identity exact, and a Markov-chain twin computation of
E_epic agreeing with inclusion–exclusion at exact equality; per-leg draw-count
sentinels (jitter draws ≡ damage events, tie-flip draws ≡ recorded ties);
twin independently-written decision evaluators; stdout + results.json
byte-identical across two process runs (Arm E platform-independent exact
Fractions; the battle arm pinned to a stated CPython minor version).

## Decision rule (pre-registered; evaluated in this order, REJECT first)

Decision numbers: W(c, pilot) = P(Common side wins) per grid cell, exact
Fractions from the main leg.

- **REJECT** ("the promise fails — the budget wall stands and collection
  grind is the ranked-PvP side door"): W(c, BEGINNER) < **2/5** in **≥ 2 of
  3** Common compositions. Even max-skill Common play loses 3-in-5+ to a
  beginner-piloted Epic team — type, ordering, move choice, and setup cannot
  climb 200-vs-300. Checked FIRST: the costly error is the lane building a
  ranked surface (and 2.0 inheriting a parity-locked engine, superbot-next
  #226) on "rewards skill, not time spent" while the committed catch economy
  sells the counter-proof at TP× the grind — exactly the Q-0039 shape the
  normalization was adopted to kill.
- **APPROVE** ("the two-sided design holds: rarer = stronger AND skill
  counters"): W(c, BEGINNER) ≥ **1/2** in **all 3** compositions (a max-skill
  Common collection is at least even money against a lazy Epic one) **AND**
  W(c, SKILLED) < 1/2 in **≥ 2 of 3** (under equal max skill the Epic budget
  still leads — "rarer = stronger" retains meaning) **AND** the seed-20261326
  stability leg reproduces the ruling through both twin evaluators.
  Mutually exclusive with REJECT by arithmetic (all 3 ≥ 1/2 leaves 0 below
  2/5). Consequence: both harvested lines gain their measured numbers routed
  lane-side per Q-0260 (the comment cites the measured beginner-row floor;
  the docstring cites the equal-skill Epic edge as the surviving, priced
  meaning of rarity).
- **NULL** (anything else — a legitimate reportable outcome with
  pre-registered axes, each a citable finding, never a re-run request):
  (i) **composition-straddle** — the BEGINNER row mixes ≥ 1/2 and < 2/5
  across Common compositions: the counter exists but only for specific
  archetype builds, naming the catalog's per-element Common archetype rows
  as the knob (team-building matters MORE than the line promises — the
  finding is which builds); (ii) **margin-band** — the BEGINNER row lives in
  [2/5, 1/2): the Common side is close but never even money; the measured
  band is the retune target and `ELEMENT_POWER`/`STRONG_MULT` the named
  one-constant levers; (iii) **budget-inert** — W(c, SKILLED) ≥ 1/2 in ≥ 2 of
  3: skill parity ERASES rarity, the "rarer = stronger" half fails, and
  `RARITY_BUDGET`'s 230/260/300 spread is dead weight the catch economy
  still charges TP× for — the knob is the spread itself; (iv) **stability
  non-reproduction**; (v) **sensitivity straddle** — a reporting leg (jitter,
  buff cap, level) flips what the main leg ruled: names the axis, never
  flips the decision.

**Boundaries (stated in the verdict, each with its direction):** the policy
family is the engine's own committed skill ceiling (its four policies + the
one committed ordering lever; there is no mid-battle switching in the engine
to model) — a cleverer in-engine policy could only RAISE the Common side's
numbers, so a REJECT is conservative in the one direction that matters and an
APPROVE is not weakened (direction stated). Teams are the owner's 6v6
element-complete standard; off-meta stacking (six of one element) is out of
registered scope. The comment's "level" lever is normalized away in ranked
PvP by the engine's own `NORMALIZED_LEVEL` rule — this head prices the
sharper surviving claim; raw-level PvE counters are explicitly out of scope
(the docstring itself routes raw levels to "PvE/collection prestige").
APPLICATION GUARD: the verdict conditions on the 36-row catalog @ `1cc5536`
(exactly one Epic per element, two Commons per element) and the quoted
engine constants — a catalog reshuffle or a re-tuned engine means re-run,
not reuse. Trading/gifting economies don't exist in the engine; TP prices
self-caught grind only (stated).

## Dedup (swept at drafting, HEAD `bb6afe7`)

Tree-wide `rg -i -g '!bootstrap.py' -g '!.substrate' "creature|rarity"`:
every prior hit is spawn/encounter pacing (P003 → V001 spawn tuning, P016 →
V018 cooldown coexistence — the latter's own depends line notes "the only
encounter code is the pure creature-game catch roll"), websites data-story
listings, or fishing/mining rarity WEIGHTS (V042/V043 price faucet curves
keyed on `rarity_weight` — sell values, not battle power). **No proposal
P001–P046 and no sim-lab verdict through V056 (outbox re-read at `c7fc1a0`;
V057 in flight consumes P046 — keyword tiling, zero overlap) crosses rarity
tiers in battle or touches creature battle balance at all.** Nearest by SLOT:
P039 → V050 and P043 → V054 (gba-homebrew — survival-frames census / band-
routing economy; different repo AND different question class: PvE
economy/pacing vs PvP fairness under asymmetric assets). Nearest by SHAPE:
the casino family P020/P023/P027 → V022/V025/V029 (bankroll ruin under house
take levers — a wagering wallet; here nothing is wagered: the contested
resource is committed stat budget and the lever is the opponent's skill).
Nearest by CONSUMER: P016 → V018 (same hub, same creature game, but spawn
cooldown namespaces — zero shared fixture, metric, or constant). Nearest by
MOVE: the in-repo design sim itself — this head runs exactly the one check
its PLAYABLE stamp skipped (its fairness legs are all same-rarity or
random-mixed rosters), with its own graduated constants quoted back at it.

**Alternatives passed on merit:** the catch-grind faucet alone (already half-
covered by V001's spawn-pacing world and it prices time, not the P2W claim);
a type-chart balance census (the design sim already checks element win-rate
spread on same-rarity teams — no committed claim is unpriced there); the
superbot-games shared-encounter contract head (parked gen-2, build-shaped
not sim-shaped); Uncommon/Rare intermediate rungs as decision cells (kept
reporting-only via the Rare gradient — the harvested line names Common vs
Epic, so the decision stays on the claim's own endpoints).

## Probe report (v0, 2026-07-13)

**1. What is this really?** A pre-registered cross-rarity fairness sim for a
shipped PvP ruleset's own never-tested promise: can the committed skill
levers (type-aware ordering, move choice, setup buffs) lift a 200-budget
Common team to even money against the catalog's unique 300-budget Epic team
at the engine's own normalized level — pricing whether "rewards skill, not
time spent" survives the one axis level normalization left standing.

**2. What is the possibility space?** Trust the comment by vibes (the status
quo — a ranked surface ships on an unpriced fairness claim); re-run the
in-repo design sim as-is (it never crosses rarity tiers — the gap IS the
head); wait for live ranked data (needs the surface built first, the wrong
order); or this head: re-implement the pure committed engine hermetically,
sweep the pinned 9-cell composition × pilot grid, and register what each
landing means before the build.

**3. Most advanced capability from the simplest implementation?** One stdlib
sim + fixture JSON: the engine is already pure, seeded, and stdlib-only, so
the whole combat model re-implements from quoted constants in ~200 lines;
exact-Fraction win rates, an exact inclusion–exclusion catch-economics arm,
a deterministic hand-traced fixture battle, and a 9-cell decision grid — all
byte-reproducible.

**4. What breaks it?** The policy family understates the true skill ceiling
(disclosed: it is the engine's own committed ceiling, and the bias direction
makes REJECT conservative); float damage math ties reproducibility to a
pinned CPython minor (the P017+ Arm-S convention, stated); the catalog could
reshuffle (application guard: re-run, not reuse); banker's rounding in stat
derivation is subtle and therefore gate-pinned per archetype (F2).

**5. What does it unlock?** The hub's ranked-PvP fork decided on evidence
before it is built: a ratified two-sided design with numbers, or a named
retune (RARITY_BUDGET spread / ELEMENT_POWER / STRONG_MULT — one-constant
knobs) shipping BEFORE leaderboards, plus the exact TP grind-premium number
the catch economy currently charges; superbot-next inherits the same numbers
through its parity-locked port (#226) before its own ranked build.

**6. What does it depend on?** Nothing at verdict time — fully hermetic:
every committed constant and all 18 used catalog rows quoted into the fixture
at drafting @ `1cc5536`, zero repo/network reads in the verdict session.
Consumers: superbot hub owns the engine, catalog, and ranked surface (routing
is the manager's per Q-0260); superbot-next co-consumes via creature parity;
sim-lab owns the method precedent.

**7. Which lane should build it?** sim-lab (the hermetic pre-registered
seeded-MC + exact-arm discipline is the P017–P046 committed precedent;
nearest method kin P044's pure-seeded decision arm with exact per-run
Fractions and hand fixtures, P043's committed-tables game-economy pin). The
verdict consumer is the superbot lane via the manager sweep. Dedup argued
line-by-line above — no prior proposal or verdict crosses rarity tiers in
battle.

**8. What is the smallest shippable slice?** The committed sim + fixture
reproducing the 9-cell W grid, the mirror/naive/Rare-gradient reporting rows,
the sensitivity legs, both Arm E outputs with TP, and every gate
byte-identically per the done-when in the outbox block — one PR in sim-lab,
no lane build. On NULL, the cheapest live probe is the engine's OWN test
seam at zero new tooling: `resolve_battle` is pure and seeded, so the named
boundary cell (or the candidate knob value) replays as a lane-side unit test
with the fixture's exact teams and seeds.

**Recommendation: sim-ready**
