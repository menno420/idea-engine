# Shared encounter engine — write the consumer contract before mining builds it

> **State:** parked(build-direct — the contract's v1 surface ALREADY EXISTS at lane HEAD `b134961`: `games/shared/encounter/interface.py` ships the EncounterResolver Protocol naming all three launch triggers, so the capture's headline ask is overtaken; what remains is a lane-sized claim-first slice — pin the per-trigger payload/kind schemas + reward-routing rule + an executable conformance suite — with no parameter question left for sim-lab: spawn tuning is settled by sim-lab VERDICT 001, grid balance is sim-pinned in-repo, quest rewards are pinned by the lane's own balance sim; manager routes it to the superbot-games mining Project as a gen-2 slice)
> **Class:** product · **Target:** `menno420/superbot-games`
> **Grounding:** https://github.com/menno420/superbot-games@b134961ef5dddf8a1cc15d97c11704629d81989a · fetched 2026-07-10T23:09Z (manifest row: behind)
> **Sequence:** after the gen-1 shared seam shipped (the capture's "before mining builds it" window PARTIALLY closed: `games/shared/encounter/` v1 landed gen-1 with a reference resolver, and mining's production grid resolver landed OUTSIDE the Protocol in lane PR #11) — but before the gen-2 production-resolver swap, which is the standing mining backlog item the remaining contract slice must precede

## Problem

`docs/lanes.md` @ `adb5f9b` rules: "Mining implements the shared encounter engine first;
exploration consumes it." But the engine's first real consumers are already owner-ruled
and live in *another repo's* backlog: **wild encounters** (activity-debounced channel
spawns — owner decision **Q-0186: build FIRST**) and **grid encounters** (depth-gated
sparse events — owner decision **Q-0198: loot/flavour first, combat fast-follow**), both
harvested into `ideas/superbot/` @ superbot `fd638e3`. Nothing in superbot-games names
them. A mining Project building "the shared encounter engine" from its own founding plan
alone will build a grid-shaped engine, and the activity-spawn consumer (plus
exploration's quest/encounter engine) will each need a retrofit — in a claim-first shared
path where interface changes cost a both-lanes announcement every time.

## Idea

One capture-level contract doc for `games/shared/` (this is that capture): the engine
takes a **spawn source** abstraction (activity counter · grid step · quest beat), a
**deterministic resolution seam** (loot/flavour first per Q-0198; combat delegated to the
creature engine as fast-follow), and **reward routing through the existing audited
seams** (Q-0186's own condition) — with wild encounters, grid encounters, and
exploration's quest engine named as the three launch consumers the public surface must
satisfy before it freezes.

## Grounding

- `https://raw.githubusercontent.com/menno420/superbot-games/main/docs/lanes.md` @
  `adb5f9b` (mining-implements/exploration-consumes rule; claim-first + interface-change
  announcement cost).
- `ideas/superbot/wild-encounters-activity-spawning-2026-07-10.md` and
  `ideas/superbot/mining-grid-encounters-2026-07-10.md` — link indexes pinned @ superbot
  `fd638e3` carrying the Q-0186 (BUILD FIRST) and Q-0198 (loot-first) owner rulings.
- `control/status.md` prior heartbeat: wild-encounters flagged among the harvest's
  ripest probe candidates.

**Why now:** the engine is the first shared-path code the cohabitation experiment will
stress; shaping its surface costs one doc today and a two-lane renegotiation later.

## Probe report (v0, 2026-07-10)

*Probed against live state, not the capture's snapshot: superbot-games @ HEAD `b134961`
(ls-remote 2026-07-10T23:08Z; the capture was grounded @ `adb5f9b`, and the tree moved),
superbot @ `c5f501e`, sim-lab @ `bc6e0fe`. The load-bearing live find: the contract this
capture asks for now PARTIALLY EXISTS — exploration's gen-1 lane shipped
`games/shared/encounter/interface.py` + `reference.py` (announced as the standing shared
interface in `control/status-exploration.md` @ `b134961` per the docs/lanes.md both-lanes
rule), naming ALL THREE launch triggers this capture wanted named: `EncounterTrigger =
{GRID_ROAM, EXPLORE_ACTION, CHAT_ACTIVITY}`. Where something is not verified, it says so.*

**1. What is this really?**
A freeze-order instrument: it does not add a feature, it fixes WHO the shared engine's
public surface must serve before that surface hardens. At capture time the ask was "write
the contract before mining builds a grid-shaped engine." Live state has already split that
in two: the *shape* half shipped (the `EncounterResolver` Protocol —
`EncounterRequest(trigger, player_id, world_seed, context)` →
`EncounterOutcome(encounter_id, kind, payload, seed)` — deterministic by invariant, with a
dependency-free reference impl so exploration is unblocked now, per
`games/shared/encounter/README.md` @ `b134961`), while the *semantics* half did not: both
`context` and `payload` are `Mapping[str, object]`, so the Protocol binds no per-trigger
keys, no kind vocabulary beyond the reference's `{none, creature, cache, event}`, and no
reward-routing rule. What this idea really is NOW is that unwritten semantics layer plus
the conformance proof that mining's production core honors it.

**2. What is the possibility space?**
Three axes. **Contract depth:** thin Protocol as-is → documented per-trigger context/payload
key schemas → an executable conformance suite any resolver impl must pass → a versioned
engine surface with capability negotiation. **Consumer set:** the three launch consumers
(grid encounters Q-0198 — mining's `games/mining/core/encounters.py`, shipped lane PR #11;
exploration's quest engine — already consuming the reference resolver via
`docs/design/quest-encounter-engine.md` §6/§8 and `test_encounter_reference.py`; wild
encounters Q-0186 — the CHAT_ACTIVITY trigger, whose spawn-source tuning sim-lab VERDICT
001 just settled) → the superbot hub's Encounters cog (cross-repo) → future superbot-next
game plugins registering their own encounter types. **Reward routing:** payload-only
(host's audited workflow layer is the sole writer — the current de-facto rule, matching
Q-0186's own condition) → a shared reward vocabulary in the contract → engine-computed
capped bundles like the quest catalog's `TIER_CAPS`.

**3. What is the most advanced capability reachable by the simplest implementation?**
One contract page + one parameterized conformance test. A `games/shared/encounter/`
contract doc naming the three launch consumers with per-trigger context/payload key
tables, plus a test suite parameterized over resolver implementations (determinism as a
pure function of `(world_seed, player_id, trigger, sorted context)`, kind vocabulary,
required payload keys per trigger, no spend/purchase lever — the mining slice already
proves that last invariant for its own resolver), buys the whole strategic point: mining's
production swap becomes a no-consumer-change event BY PROOF rather than by the Protocol's
vacuous satisfiability; the lanes.md "interface change" announcement rule gets an
executable definition of what the public surface IS; and VERDICT 001's telemetry fields
(per-spawn / per-claim / per-channel mint) land as named payload keys so the hub's
CHAT_ACTIVITY consumer and the reward-inflation follow-up read the same schema.

**4. What breaks it?**
- **The cross-repo consumer.** Q-0186's Encounters cog builds in the superbot hub (owner
  ruling; every seam it routes through — `economy_service`, `game_xp`, the audited
  `*_workflow` writes — lives there), and the hub cannot import `games/shared/`. The
  contract can bind shape cross-repo, not code; claiming "one engine, three consumers"
  literally is a fork by construction until superbot-next hosting converges them. The
  honest scope is one engine for the two in-repo consumers + a schema the hub mirrors.
- **Vacuous satisfiability.** `Mapping[str, object]` context/payload means any resolver
  satisfies the Protocol; a contract that fails to pin keys certifies nothing — the
  retrofit risk the capture named, reborn one level down.
- **The name collision.** Mining's `games/mining/core/encounters.py` defines its OWN
  `EncounterOutcome` (kind · resolution · narration · rewards · damage_taken ·
  energy_cost; signature `(seed, cell, stats, energy, rng)`) — same name, different shape
  as the shared interface's. The production resolver does NOT implement the Protocol
  today; the swap is standing gen-2 backlog (`control/status-mining.md` next-items;
  README "mining's production core replaces it via the Protocol"). Unreconciled, the
  contract doc would describe a surface its owning lane's real engine ignores.
- **Clockless consumers.** Both gen-1 lanes are closed and the relaunch is un-armed
  (manifest games-plugins row: ORDER 002 self-arm unexecuted, "relaunches clockless";
  ORDER 001 P0 CI-collection pending — boot-gating). A contract slice routed now may sit
  unread until an externally-fired gen-2 boot; that argues for routing it WITH the boot
  order, not for skipping it.

**5. What does it unlock?**
The gen-2 mining queue in its intended order: the production-resolver swap lands against a
proved conformance suite instead of a thin Protocol; the Q-0198 build-out (three
depth-band archetypes, multi-turn combat fast-follow) extends a contracted surface; the
superbot-next Layer-3 host adapter wires one documented seam instead of two divergent
outcome types; and VERDICT 001's UNSETTLED half (reward inflation — no live earn-rate
baseline exists) gets its telemetry keys standardized where every consumer can log them.

**6. What does it depend on?**
All shipped, verified at pin: `games/shared/encounter/{interface,reference}.py` +
`games/exploration/quest/**` (`DetRng`/`derive_seed` determinism plumbing) +
`games/mining/core/encounters.py` with its sim-pinned balance table
(`docs/design/mining-grid-encounters.md` §5, 276,480-action sweep) — all @ `b134961`.
Decisions: Q-0186 (wild encounters BUILD FIRST; rewards through existing audited seams)
and Q-0198 (grid: loot/flavour first, combat fast-follow) — both owner-ruled, cited in
the tree itself (the interface docstring and the grid design doc). Evidence: sim-lab
VERDICT 001 (finalized 21:20Z, sim-lab `control/outbox.md` @ `bc6e0fe`) — spawn defaults
threshold=24 / debounce=30s / cooldown=900s + guardrails SETTLED for the CHAT_ACTIVITY
source; reward VALUES provisional pending named telemetry. Deferred-by-design: the
audited workflow layer (grid design §7) — where reward routing actually executes.

**7. Which lane should build it?**
`menno420/superbot-games`, claim-first on `games/shared/**` per `docs/lanes.md` — and
specifically the MINING Project, since it owns the production resolver whose swap the
contract gates, with the mandatory interface-change announcement in both status files.
Not sim-lab (no reproducible-evidence question remains — see below), not the superbot hub
(it owns the cog consumer, not this repo's shared surface), not this repo (we write no
other repo's files).

**8. What is the smallest shippable slice?**
One lane PR: (a) `games/shared/encounter/CONTRACT.md` (or a README § growing into it)
naming the three launch consumers and pinning per-trigger context/payload key tables, the
kind vocabulary, and the reward-routing rule (payload carries reward INTENTS; the host's
audited workflow op is the sole writer — Q-0186's condition verbatim); (b) a conformance
suite parameterized over resolver impls (determinism, vocabulary, required keys, no-spend
lever), green on `ReferenceEncounterResolver` day one; (c) a flagged note on the
`EncounterOutcome` name collision with the migration rule for mining's swap. Nothing else
— archetypes, combat depth, and host wiring stay in their own slices.

**Recommendation: park** — build-direct: the contract's v1 surface already exists at lane
HEAD (`games/shared/encounter/interface.py` @ `b134961` names all three launch triggers),
and every remaining question is settled by writing the lane slice itself — spawn tuning
settled by sim-lab VERDICT 001, grid balance sim-pinned in-repo (§5 table), quest rewards
pinned by the lane's balance sim, and "does one payload schema serve all three consumers
without forks" is answered by the conformance suite + adapters, not by simulation — so
route it to the superbot-games mining Project (claim-first, both-status-files
announcement) sequenced BEFORE the gen-2 production-resolver swap, ideally riding the same
boot that executes ORDER 001.
