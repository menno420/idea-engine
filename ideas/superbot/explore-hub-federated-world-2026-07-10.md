# The Explore hub — a federated open world (one world, each subsystem its own game) — link index

> **State:** sim-ready
> **Class:** product · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/explore-hub-federated-world-2026-06-19.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/explore-hub-federated-world-2026-06-19.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/explore-hub-federated-world-2026-06-19.md)).

Owner-directed framing: one federated open world (the Explore hub) that mining, fishing, pets, and RPG-survival all plug into — defining the shared world is the single design decision that homes four gated game lanes.

## Probe report (v0, 2026-07-10)

> **Mode:** panel (README § probe battery: big-or-contested → panel) — four parallel lenses (design/possibility-space, engineering/simplicity, adversarial/risk, dependencies/routing) + one synthesizer. Chosen because the harvest flagged this idea as "one shared-world decision homes four gated game lanes; highest design leverage per line."
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/explore-hub-federated-world-2026-06-19.md@fd638e3 · fetched 2026-07-10T21:23Z

**Reality check first (the probe's biggest finding):** the canonical doc (2026-06-19) predates its own partial build. Superbot carries a plan (`docs/planning/explore-hub-federated-world-plan-2026-06-19.md`) whose PR 1 — the Explore world hub + `world_registry` — is MERGED (superbot #1156: `disbot/services/world_registry.py`, `WorldEntry` key/label/emoji/description/opener/order + idempotent `register_world_entry`; CI parity invariant `tests/unit/invariants/test_world_registry_parity.py`), PR 3 (cross-game identity read card) is BUILT, and PR 2 (explicit global-vs-per-game XP split) is marked owner-gated ("requires owner design input on the two-track progression-balance model"). Mining, fishing, and farm already dock as registry entries; wild encounters (PROPOSAL 003) docks next. Any reading of this idea as a greenfield "single design decision" overstates remaining scope.

**1. What is this really?**
Not a game and not a feature: a **world-model contract** — a captured owner framing that fixes what is shared vs siloed across four superbot-internal gated game plans so each stops re-deciding it. Its decided core is three contracts: the three-XP-track table (Message / Global game / Per-game — "raw but decided"), the hybrid gear model (generalist loadout; auto-equip defaults OFF, never silent), and the invariant "loops are accelerators, never gates." Around that sit four explicitly owner-reserved questions — hub shape, survival-overlay attachment, docking topology, cross-game identity — marked "for the dedicated planning session — do not decide unprompted." The doc self-labels "Not a plan, not approval." Post-#1156 the "one decision homes four lanes" thesis is partially executed: federation's cheap contract shipped; what remains undecided is the progression/gear/overlay layer above it.

**2. What is the possibility space?**
Axes, minimal → maximal (doc-cited):
- **Hub representation:** flat HubView routing into each game (shipped as `ExploreWorldHubView`/`!world`) → map/location model with biome-gated reachability (open question 1).
- **Survival/adventure overlay:** invisible ("Easy ≡ today's game, byte-identical") → opt-in stakes → quests (open question 2).
- **Progression coupling:** 3-track structure fixed; the split is tunable — global "broad utilities (stamina, carry, luck, xp-gain)" vs per-game "signature mechanics"; minimal trickle → cold-start-softening global skills.
- **Gear sharing:** game-bound → encouraged generalist loadout → auto-equip-strongest (bounded: defaults OFF, toggle beside the memory controls).
- **Economy coupling:** isolated per-game economies → accelerator loops ("fish → food enabling deeper mining"); hard ceiling: gating loops forbidden.
- **Docking topology:** flat siblings → nested (mining-hub-redesign Option A sub-hubs under the Explore parent — open question 3).
- **Identity:** per-game profiles → single cross-game profile (open question 4; plan PR 3's read card is its first slice, BUILT).
- **Chat–AI fusion:** Message XP as "negotiation leverage vs the AI Dungeon Master" — the doc's only genuinely new mechanic.
Doc is silent on: multi-user shared-world state, persistence/data model, migration of existing player progress.

**3. Most advanced capability reachable by the simplest implementation?**
The registry-of-openers contract was exactly that — and it shipped (#1156): a flat ordered list of `WorldEntry` buttons; "a new world docks in by registering an entry, never by editing the hub." So the leverage point moves up a layer: the highest-leverage UNSHIPPED contract is plan PR 2's explicit global-vs-per-game XP split (`game_xp` as documented global pool + per-game adapter). Everything richer — skills, gear, survival overlay — reads through it; the map/biome model is the expensive fork both docs defer. Don't buy a location graph to get federation: federation is already bought.

**4. What breaks it?**
Ranked, most-likely-fatal first:
1. **Staleness** — planning against the 2026-06-19 text re-litigates a schema with running consumers (mining/fishing/farm registered; wild encounters docking). Mitigated by the reality-check above, now recorded in-file.
2. **Big-design-up-front** — every load-bearing remaining choice is owner-deferred, yet lanes demonstrably ship without waiting (fishing v1 economy #1033–#1041; wild encounters routed around it): the "one gating decision" claim is weaker than pitched, in both directions.
3. **Internal contradiction** — "per-game competence must never gate other games" vs open question 1's biome-gated reachability; biome gates are gates; unreconciled.
4. **Schema-ownership vacuum** — four plans writing one world model with no named owner/veto/migration process (doc silent — the silence is the finding).
5. **Economy inflation** — unified currency + shared global XP makes every subsystem a faucet into one pool with no earn-rate baseline (PROPOSAL 003 already found "not measured"); the hub multiplies that by four.
6. **Discord UX navigation tax** on the maximal map option (hypothesis — doc silent on interaction cost).
Rejected axis: retrofit cost — convergence is already in-flight (the doc "codifies the drift"; fishing Q-0175 already reuses `game_xp` + unified character), so retrofit is cheap.

**5. What does it unlock?**
- The four gated superbot plans get their home: fishing (Q-0175 — its shipped choices become sanctioned architecture), mining-hub-redesign (Option A sub-hubs get their parent), rpg-survival (attachment surface defined once at world level), pets-companions.
- Wild encounters (Q-0186, PROPOSAL 003): already paying rent — `GAME_ENCOUNTERS` xp "joins the global level for free"; the hub's first passive event.
- Every future game: the global pool applies "including games you haven't started yet" — cold-start leg-up by construction.
- Chat-AI lane: Message-XP-as-DM-leverage, the first chat↔games bridge.
- games-plugins (gen-2, GATED): a future plugin consumer of the registry once un-gated.

**6. What does it depend on?**
- **Shipped:** `game_xp` split · Message-XP · `world_registry` (#1156) · `economy_service` + audited `*_workflow` seams (Q-0071) · mining skill tree (the per-game-track prototype) · per-user config surface (hosts the auto-equip toggle).
- **In-flight:** fishing plan Q-0175 (live validation of the per-game mastery model).
- **Hard gate:** the four owner-reserved design questions — an owner planning session; explicitly "do not decide unprompted."
- **Plan PR 2's specific gate:** "owner design input on the two-track progression-balance model" — the one gate evidence can serve (see recommendation).
- **Adjacent:** PROPOSAL 003 co-cites the same world model ("global level = SUM of per-game xp"); it does not wait on this idea, but a planning session must read encounters as a live constraint.

**7. Which lane should build it?**
`menno420/superbot` (hub) — the only ACTIVE holder of every hard seam (`economy_service`, `game_xp`, `world_registry`). Correction to the harvest framing: the "four gated game lanes" are NOT fleet-manifest rows (the manifest has no fishing/pets/rpg-survival rows; its only other game lanes are games-plugins GATED and pokemon-mod-lab PARKED). They are four superbot-internal planning docs: `fishing-open-world-expansion-plan-2026-06-18`, `mining-hub-redesign-2026-06-15`, `rpg-survival-difficulty-design-2026-06-10`, `pets-companions-plan-2026-06-09`. Consumers = those four plans, plus games-plugins later.

**8. What is the smallest shippable slice?**
Plan PR 2 narrowed to its mechanical half: a per-game XP adapter over the existing `game_xp` table (namespaced per-game counters + slow-trickle write path: game event → fast per-game XP + small global XP), surfaced read-only on the existing PR-3 world card, shipped with placeholder config-constant ratios (no balance claims) so it does not stall on the owner gate. Zero-decision fallback: dock a fourth world (pets or wild-encounters entry) via `register_world_entry` — pure registry consumption, covered by the existing parity invariant.

**Recommendation: sim-ready** — the four owner-reserved questions stay with the owner — no sim should settle them — but plan PR 2's progression-balance gate is exactly the kind of input evidence can serve: sweep global-trickle ratios and global-skill effect sizes against the shipped mining/fishing earn shapes (plus PROPOSAL 003's `GAME_ENCOUNTERS` source) so the owner planning session ratifies an evidence-backed default instead of guessing one. (The risk lens returned needs-more-grooming on doc staleness; that ask is consumed by this report's reality-check section — state advances forward-only.)

Panel record: design lens → coordination value confirmed; simplicity lens → sim-ready (PR-2 slice identified); risk lens → needs-more-grooming (staleness; consumed in-report); deps lens → superbot confirmed as building lane, harvest framing corrected.
