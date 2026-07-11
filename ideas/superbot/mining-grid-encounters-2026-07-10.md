# Mining grid encounters — depth-gated sparse events (2026-06-22) — link index

> **State:** sim-ready
> **Class:** product · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/mining-grid-encounters-2026-06-22.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/mining-grid-encounters-2026-06-22.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/mining-grid-encounters-2026-06-22.md)).

Sparse, depth-gated random encounters on the grid-Mine navigator (fight/flee/loot buttons, resolved through the audited mining seam). Owner decision Q-0198: build loot/flavour-only first; combat is a fast-follow reusing the creature engine.

## Probe report (v0, 2026-07-11)

> Single-pass battery (panel not escalated: reversible game-feature surface, no
> security/data/spend/public blast radius — README § probe battery, VERDICT 002 default).
> Verify-first grounding, live at probe time: canonical doc re-read at superbot HEAD
> `e1090dbcfdf63ffd955399dc2325b9ad1a2f8c8d` (ls-remote 2026-07-11T~12:05Z) — the Q-0198
> owner-decision banner is live ("build the encounters, loot/flavour-only first …
> depth/chance/cooldown … sim-tunable at build time"), doc status still `ideas`; superbot
> `docs/current-state.md` @ the same HEAD contains ZERO "encounter" occurrences and its
> 43rd reconciliation pass records band #1951–#1980 as "entirely docs/tooling, zero
> `disbot/` runtime" — the build has not started, the premise is live.

**1. What is this really?**
The owner-named, owner-ruled second half of a two-trigger encounter architecture. The
sister idea (wild-encounters, chat-activity-triggered) got sim-pinned spawn defaults in
sim-lab VERDICT 001 (= PROPOSAL 003 by intake cross; threshold=24 msgs, debounce=30s,
cooldown=900s — recorded in `wild-encounters-activity-spawning-2026-07-10.md` § Sim
verdict); THIS is the exploration-triggered half — sparse, depth-gated events on the
shipped grid-Mine navigator, loot/flavour-only first (Q-0198), resolved through the
audited `mining_workflow` seam. The canonical doc itself names the deeper truth: both
triggers should share ONE encounter-resolution engine, designed once.

**2. What is the possibility space?**
Loot/flavour events (ruled first scope) → light combat fast-follow reusing the
creature/deathmatch engine (ruled: never a third combat model) → a shared
encounter-resolution engine serving both triggers (grid per-action + channel
activity-spawn) → depth bands as a real risk/reward ladder → encounter content as
swappable data tables (the exact noun-out-of-logic shape superbot-games just executed for
mining in its theme-leak R2 pass — fm roster @ `7b46bd1`, superbot-games row), making
encounter packs theme-engine-compatible later. Adjacent, unclaimed: hint/rumor items that
bias encounter odds (a sink), and per-depth telemetry as the tuning feedback loop.

**3. Most advanced capability reachable by the simplest implementation?**
A pure table + roll function (`utils/mining/encounter.py`, stdlib) keyed on depth band,
called from the EXISTING move/`Mine here` action path, resolving through ONE new audited
workflow op; rewards ride the existing `economy_service`/`update_mining_item`/`game_xp`
seams. Loot-only needs no new persistent state beyond a per-player cooldown stamp — yet
this already delivers the depth risk/reward curve, deterministic testability, AND the
engine seam the wild-encounters build can share. The advanced capability (one engine, two
triggers) costs nothing extra if the resolution function is trigger-agnostic from day one.

**4. What breaks it?**
- **Mis-tuned sparsity.** The owner's whole spec is "after a certain depth … not too
  many" — interrupt-spam kills the grid's calm roaming and violates Q-0087
  (never-mandatory). This is a pure parameter question, currently unpinned: Q-0198 left
  depth/chance/cooldown "sim-tunable at build time" and no sim has run.
- **Reward inflation, unmeasurable pre-live.** VERDICT 001's UNSETTLED half applies
  verbatim here: no live fishing/mining earn-rate baseline exists, so loot values stay
  provisional and the slice must log the same named telemetry.
- **Engine fork by sequencing.** If the channel Encounters cog (build owner-ruled Q-0186,
  defaults already sim-pinned) ships its own resolution path first, grid encounters builds
  a second one later — the shared-engine window closes at whichever build lands first.
- **Roll-farming via action rate.** Per-action chance × `!fastmine` (shipped, S1 ledger)
  = grinders farm rolls; the cooldown must be per-player (not per-cell), and the sweep
  must include a fastmine-grinder trace or the defaults are tuned for a player who
  doesn't exist.

**5. What does it unlock?**
A reason to descend (the depth ladder currently pays only richer ore — current-state S1:
deeper ladders shipped, MAGMA reachable, no event layer); the shared encounter engine that
makes the Q-0186 wild-encounters build cheaper and consistent; the combat fast-follow
slot (creature-engine reuse); an encounter-content surface shaped for the games program's
theme-pack data tables; and the earn-rate telemetry both verdicts need before any reward
scaling.

**6. What does it depend on?**
Shipped grid navigator (`views/mining/grid_mine_view.py`, shipped encounter-free by
explicit Q-0173 deferral — the doc's origin note); the audited `mining_workflow` seam
(RS02/Q-0071) + `economy_service`/`game_xp`; Q-0198 ANSWERED (it is — loot-first, live
roll, navigator-button resolution, 2026-06-28 banner); tuning defaults, the one open
dependency — "sim-tunable at build time" with no sim run yet; and (soft) the VERDICT 001
guardrail/telemetry set, which a shared engine should inherit rather than re-derive.

**7. Which lane should build it? (honest routing)**
superbot, the hub — this is `disbot/` runtime (cog/view/workflow territory) and the grid,
the mining seams, and the creature engine all live there. No standing hub seat exists
(Q-0264), so the builder is the next hub-touching runtime session, sequenced with (ideally
the same session as) the Q-0186 Encounters-cog build so the resolution engine is designed
once. NOT the games lanes (superbot-games/idle/mineverse carry no disbot runtime) and
nothing for idea-engine to build.

**8. Smallest shippable slice?**
Config-driven depth threshold + per-action chance + per-player cooldown wired into the
existing move/mine-here path; 3–5 loot/flavour events drawing from the existing
mining item pool + small coins via the audited seams; one trigger-agnostic
`resolve_encounter` workflow op; navigator-embed resolution buttons (loot/leave); OFF
above the threshold and default-on below it only after tuning; telemetry from day one
(rolls, fires, resolutions, mint per depth band + the mine_here earn-rate baseline —
VERDICT 001's named gap). Combat excluded (Q-0198 fast-follow).

**Recommendation: sim-ready** — the build is already owner-ruled (Q-0198) and explicitly
waits on sim-tunable depth/chance/cooldown defaults; that is a parameter-sweep question a
simulator can settle against synthetic traversal traces exactly the way VERDICT 001
settled the sister trigger's spawn defaults, and pinning it now (before the Q-0186 cog
build hard-codes an engine) keeps the one-engine-two-triggers design open.

## Sim verdict (2026-07-11)

sim-lab **VERDICT 008 · finalized 2026-07-11T13:01:19Z · needs-more-evidence**
(= this repo's PROPOSAL 008 — coincidental alignment, sim-lab numbers by intake
order; lineage on the V007 card: V001=P003 · V002=P001 · V003=P002 · V004=P004 ·
V005=P005 · V006=P006 · V007=P007). Like V006 and unlike V007, this entry
carries NO `ruling:` field — the operative ruling is the `recommendation:`
field, quoted from the pin below. SETTLED half: gating is structural — "the
per-PLAYER cooldown analytically caps encounters at 3600/cooldown enc/hr for
EVERYONE including the !fastmine grinder (grinder-vs-honest RATE ratio bounded,
shrinking toward ~1.15 as chance rises; grinder rolls-per-encounter 2-4x the
honest player's, so reward-per-action collapses)". Recommended defaults
**threshold=15 (or 20 for a silent surface) · chance=0.02 · cooldown=600s**
(cap 6.00 enc/hr: casual ~0.2, honest deep-runner ~2.8, grinder ~5.2). Ship-with
guardrails: **per-PLAYER (not per-cell) cooldown + one-live-encounter-per-player
+ audited-seam resolution** (`economy_service`/`update_mining_item`/`game_xp`
via `mining_workflow` RS02/Q-0071) — exactly the probe's Q4/Q8 guardrail set,
now sim-pinned. UNSETTLED half, COUPLED: the loot faucet's ABSOLUTE VALUE — no
live earn-rate baseline exists, so loot values stay provisional and
farm-unprofitability is settled in RATE terms, not VALUE terms (the owner-vague
"rare-but-present" numeric target stays open); the slice MUST log the named
telemetry: per-action encounter fire rate per playstyle depth-band, per-player
cooldown-hit rate, encounter-loot coin value vs `mine_here` coin value,
real-player depth distribution — VERDICT 001's unsettled-half form, restated
verbatim as PROPOSAL 008's done-when demanded. Post-verdict HARDENING (sim-lab
heartbeat @ the same pin): a wider-variation robustness pass (sim-lab PR #32,
merge `0235679`, module `robustness_wide.py`, 811 self-checks 0 failed)
answered the @codex STRUCTURAL-vs-artifact question as **STRUCTURAL** — the
3600/cooldown cap survives bot-speed cadence, boundary-timing burst farming,
and a wider cd×chance grid; the boundary farmer PINS to the cap (6.00 at
cd=600s) but never exceeds it; verdict unchanged. Shares the
encounter-resolution engine with VERDICT 001 (Q-0186 wild-encounters) —
whichever build lands first fixes it. Source:
[sim-lab `control/outbox.md` VERDICT 008 @ `b639ef0`](https://github.com/menno420/sim-lab/blob/b639ef0d6d2f082829ddf03acc4803d515940d2d/control/outbox.md)
(gate PASS; evidence: simulation — sim PR #30, 7723 self-checks 0 failed,
byte-identical re-runs; verdict block re-read RAW at the live-HEAD pin at write
time, byte-identical to the orientation read). State stays `sim-ready` — the
grammar has no post-verdict state; `historical(<merged PR>)` is a build-time
move (post-merge routing is the manager's).
