# Wild Encounters — activity-based spawning (2026-06-20) — link index

> **State:** sim-ready
> **Class:** product · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/wild-encounters-activity-spawning-2026-06-20.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/wild-encounters-activity-spawning-2026-06-20.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/wild-encounters-activity-spawning-2026-06-20.md)).

A new Encounters subsystem: channel activity accrues a debounced counter that spawns a wild encounter with a Claim button, rewards routed through existing audited seams. Owner decision Q-0186: the Pokétwo Lane A to build FIRST (feeds Collection/Quest/Shiny).

## Probe report (v0, 2026-07-10)

*Probed under owner ruling Q-0186 (2026-06-28): BUILD FIRST is already decided — this probe
does not re-litigate whether the idea is wanted; its job is to sharpen the spec into the one
question worth reproduced evidence before a runtime session commits tuning defaults. Grounded
in the canonical doc @ superbot `fd638e3`, its feature-mapping parent plan, the explore-hub
plan, and the fishing plan (same pin); where something is not measured, it says so.*

**1. What is this really?**
A passive engagement engine: a debounced per-channel activity counter that converts genuine
conversation into spawn events (embed + Claim button), with rewards routed through seams that
already exist — `economy_service` coins, fishing/mining items, `game_xp` under a new
`GAME_ENCOUNTERS` key. It is deliberately not a Pokémon clone (canonical doc § "The idea": no
roster, no battles, no new currency); its real substance is being the repo's first
*message-triggered* game event — every existing game is manual command-only (doc § Origin) —
i.e. a new trigger class over existing reward plumbing, not a new game.

**2. What is the possibility space?**
Four axes visible from the doc and its parent plan: **trigger** (flat message count →
activity-quality weighting → time/streak modifiers); **claim shape** (first-click → "name the
catch" hint-guess — doc open question 3); **reward surface** (existing fishing/mining items +
coins → dedicated encounter catalogue → shiny/variant layer); **reach** (one opted-in channel
→ per-guild config → other games registering their own encounter types through the same
spawner). The parent plan fixes the strategic shape: whatever encounters drop is the substrate
Lanes B (collection filters), C (quest engine), and D (shiny/variants) operate on (Q-0186
build order), so the reward-surface axis is the one that compounds.

**3. What is the most advanced capability reachable by the simplest implementation?**
One counter + one threshold + one embed with a Claim button, rewards through existing seams,
already yields: the repo's first passive engagement loop; stranger-grade participation
(capability re-check at callback, Q-0080); anti-P2W by construction (earned-only, Q-0039); a
`GAME_ENCOUNTERS` xp key that joins the global level for free (explore-hub plan: global level
= SUM of per-game xp); and — the compounding part — a live drop stream that is the exact data
substrate the next three owner-ordered lanes consume. The simplest slice is not a demo; it is
the foundation event source for the rest of the Pokétwo build order.

**4. What breaks it?**
- **Spawn-rate tuning.** The only number anywhere is the research report's "~24 messages"
  anecdote (doc open question 1 — config-driven, off by default). Too low → spawn spam that
  devalues rewards; too high → invisible in low-traffic channels. Not measured anywhere.
- **Paced-spam farming.** A debounced counter is still gameable by messages paced just under
  the debounce window; per-claimer cooldown and one-live-spawn-per-channel are proposed
  guardrails (doc open question 4) with unproven sufficiency. Nothing in the doc quantifies
  farmer-vs-honest yield.
- **Reward inflation.** Encounters mint free coins/items into `economy_service` with no new
  sink; if drops overlap the fishing/mining pool they undercut those games' earn rates
  (fishing v1's economy shipped in superbot #1033–#1041). No earn-rate baseline exists to
  check a new source against — not measured.
- **Claim atomicity.** First-valid-claimer under concurrent button clicks must be exactly-once
  through the audited workflow seam (Q-0071) or double-awards corrupt the economy audit trail.
  A known engineering constraint, not a design unknown.

**5. What does it unlock?**
The rest of the owner-ordered Pokétwo build: Lanes B/C/D all operate on encounter drops
(parent plan, Q-0186 build order). Secondarily: the world hub's first passive event (docks
into `world_registry`, merged in superbot #1156), and a proven activity-trigger pattern any
future subsystem can reuse.

**6. What does it depend on?**
All hard dependencies are shipped superbot seams: `economy_service` + `game_xp_service`
(per-game keys live), the fishing/mining item catalogue (fishing v1 shipped), `world_registry`
(superbot #1156 merged), audited `*_workflow` write seams (Q-0071), stranger-grade capability
checks (Q-0080). Soft dependencies: the four open design questions the doc routes to Q-0186
(threshold/debounce default, reward pool, claim shape, anti-abuse set) — of these,
threshold/debounce/anti-abuse are simulable; reward pool and claim shape are owner-taste calls
with cheap defaults (existing items; first-click).

**7. Which lane should build it?**
`menno420/superbot` (hub) — Q-0186 says a runtime session builds it in small PRs, and every
seam it routes through lives there. The games-plugins lane (`superbot-games`) is currently
boot-gated (fleet manifest @ superbot: ORDER 001 CI-collection pending) and holds none of the
economy/world seams; not a candidate for this.

**8. What is the smallest shippable slice?**
An off-by-default Encounters cog: per-channel opt-in command; config-driven threshold +
debounce; one live spawn per channel; embed + Claim button; first-click claim with capability
re-check at callback; reward = one existing fishing/mining item + small coins via
`economy_service` + `game_xp(GAME_ENCOUNTERS)`; per-claimer cooldown. No catalogue, no hints,
no shiny — and it should log spawn/claim telemetry (messages-per-spawn, time-to-claim, claimer
distribution) so the tuning defaults can be checked against reality.

**Recommendation: sim-ready** — build is already owner-ruled (Q-0186), so the one thing worth
reproduced evidence before a runtime session hard-codes defaults is the tuning/anti-farm
economics: which (threshold, debounce, cooldown) sets keep spawns rare-but-visible across
traffic tiers while making paced-spam farming unprofitable, and whether reusing the
fishing/mining reward pool materially undercuts those games' earn rates.
