# EXPLORE_ACTION pacing & the quest currency faucet — can the third trigger ride the shared K=4 window?

> **State:** sim-ready
> **Class:** game-mechanics · **Target:** `menno420/superbot-games` (exploration lane +
> the shared-engine CONTRACT slice) and `menno420/superbot` (the Q-0186 Encounters-cog
> build — the HOST whose gate would otherwise fix the constant by accident);
> verification target `menno420/sim-lab` per the Q-0264 pipeline
> **Grounding:** superbot-games live HEAD `5aec110834345e20ce47941266fe598f43804ea0`
> (anonymous blobless clone at drafting, 2026-07-13T07:3xZ) + sim-lab VERDICT 018
> committed report/fixtures @ local clone `b50fd06` (`sims/verdict-018-encounter-coexistence/`)

**Origin:** drafted under standing owner ORDER 003 (continuous pipeline — "continue
coming up with new ideas, that is your main purpose"). The ORDER 003 GAME-MECHANICS
rotation slot, round 4: rounds 1–3 were P020 (casino odds → V022 reject), P023
(entry fee → V025 reject), P027 (comp/stipend → V029 null) — the casino fairness
triage is CLOSED (all three routed levers priced), so round 4 rotates back to the
pipeline's other verdicted game-mechanics family, the encounter engine, following
its parent verdict's own excluded-trigger thread: VERDICT 018 (encounter
coexistence, P016 → approve) pinned the two-trigger contract row — per-source
clocks (CHAT_ACTIVITY 900 s, GRID_ROAM 600 s) + a MANDATORY combined per-player cap
K=4 per sliding 3600 s — and ruled the THIRD trigger out of its own sweep verbatim:
"**EXPLORE_ACTION inherits this rule by contract, not by this sweep** — its pacing
is lane-pinned" (`sims/verdict-018-encounter-coexistence/REPORT.md` @ sim-lab
`b50fd06`). The successor move is committed precedent (P023 ← V022's routed lever,
P026 ← V024's power half, P029 ← V027's routed slice, P030 ← V020's named
follow-up) — applied to the game slot's OTHER parent line for the first time.

## The window (verified live at drafting — and it is CLOSING)

VERDICT 018 deferred EXPLORE_ACTION pacing to "the lane's own balance sim". The
lane's own balance sim now exists at live HEAD and it **declares the constant
undefined**. superbot-games @ `5aec110` (head commit: "feat(exploration): finalize
— audited quest seam + `python -m games.exploration` + hub registration", PR #77)
ships `games/shared/sim/economy_sim.py`, whose module doc rules, verbatim:

> "the currency/xp faucets (dnd escort + exploration quests) are **host-gated
> per-completion (no in-domain cooldown)**, so their pinned domain-side quantity is
> a per-completion bundle."

So the lane pinned the bundle SIZE (`TIER_CAPS`, clamped to `GLOBAL_MAX = (20 gxp,
120 game_xp, 50 currency)` — `games/exploration/quest/catalog.py` @ `5aec110`) and
explicitly punted the RATE to "the host". The host is the superbot Q-0186
Encounters-cog build (BUILD FIRST, per V001's consumer line). Three owners each
believe another owns the pacing number: V018 says lane-pinned, the lane says
host-gated, and the host's build order says build first. The exploration lane just
FINALIZED (hub registration landed in the head commit) — the next consumer build
fixes the constant by accident, the exact pre-empt window P015/P016 were drafted
into. `grep -rn "cooldown\|rate_limit" games/exploration/ games/shared/encounter/`
at `5aec110` returns zero pacing surface; `EncounterTrigger.EXPLORE_ACTION` exists
in the seam interface with no clock.

## Why this is not just "V018 again with three surfaces" — the mint axis is NEW

The same economy sim pins the whole-world faucet map, and it makes the quest
faucet special: `ITEM_FAUCET_MINTS_NO_CURRENCY` rules that mining and fishing mint
**items only** (zero native currency/xp at the resolver layer — "mining coins
exist only downstream as an ore→sell conversion, a sink, not a mint"), with their
action pacing already energy-pinned in-tree (mining 360 digs/hr, fishing 180
casts/hr; observed ore 480–600/hr, fish 85–115/hr — the module's own pinned
bands). **The exploration quest bundle (with dnd's escort) is the world's
currency/xp faucet, and the quest half fires on exactly the trigger V018 left
unpaced.** Two consequences:

1. Every prior encounter verdict (V001/V008/V018) had to rule in RATE terms only
   because the item faucets' VALUE is unbaselined (the walled earn-rate baseline,
   restated in all three). The quest faucet is different in kind: its per-completion
   bundle is a committed in-tree integer (≤ 50 currency), so **per-player currency
   mint per hour is computable in absolute native units for the first time** — the
   wall does not apply to this faucet, and the verdict can say so explicitly while
   restating the wall for the item faucets.
2. V018's arbitrage finding gets a value dimension it could not see: under the
   committed row, a cross-surface farmer is rate-capped at K=4 combined/hr — but
   the three triggers are no longer value-symmetric. A farmer that STEERS its
   4/hr budget into EXPLORE_ACTION beats is farming the only currency faucet.
   Whether that is material is exactly a (c_E, B, K) arithmetic question.

## The idea (reasoned to its fuller form — Q-0254 duty)

Extend V018's committed composed machinery (its regression-pinned V001 chat machine
+ V008 grid gate + contract state machine) with the third surface, and sweep the
one free constant the contract row still lacks — the EXPLORE_ACTION per-source
cooldown c_E — jointly with the two model unknowns that decide whether any c_E
works: B (beats per quest completion; the catalog's own templates bracket it —
`supply_run` requires 3 delivery events) and the COUPLING between encounter
admission and quest progress (the design fork the build will otherwise decide
silently): **gated** (a quest beat advances only when the encounter engine admits
the fire — pacing can starve quests) vs **free** (quest progress is independent;
denied beats simply fire no encounter — pacing cannot starve quests, and only
FAIR/MINT bind). Score each cell against three pre-registered bands:

- **FLOW** — an honest quest-focused player is not starved: admitted-beat rate ≥
  80% of the cell's analytic ceiling min(3600/c_E, K, r_E)/hr, and completions/hr
  ≥ 0.8 · that ceiling/B.
- **FAIR** — the third surface does not silently retax V018's honest player: the
  mixed-triple-deep profile keeps combined chat+grid ≥ 2.375/hr (V018's committed
  K=4 mixed-deep 2.875/hr minus a 0.5/hr materiality allowance) AND still gets ≥
  1 admitted quest beat/hr.
- **MINT** — the currency faucet is not farmable: the beat-steering three-way
  farmer's currency/hr ≤ 2.0 × the honest quest-focused player's currency/hr
  (ARB_RATIO_MAX = 2.0, V018's committed materiality bound reused), with the
  ABSOLUTE currency/hr table (tier II 25 center, tier III 50 adversarial leg)
  shipped as the first native-unit mint pin regardless of ruling.

Chained anchors make it comparable, not parallel: regression legs must reproduce
V018's committed numbers exactly (mixed-deep 3.275 combined/hr uncapped / 2.875
at K=4 / honest cost 0.400/hr; farmer 8.875/hr under pure per-source, 4.000
pinned at the cap; V001's 0.93/3.00/4.38 + 4.00-claims/hr farmer; V008's
0.20/2.80/5.20) before any third-surface cell counts, and an empty-explore-surface
composition identity must equal the V018 machine event-for-event.

## Alternatives weighed for the round-4 slot (on the actual evidence, then passed)

- **Mining/fishing reward-pacing pins (candidate A):** superbot-games IS readable
  this session (blobless clone succeeded, HEAD `5aec110` pinned) and balance
  constants DID land — but they landed *pinned*: the item faucets' pacing is
  energy-model-pinned in-tree (360/180 per hour with tolerance bands in
  `economy_sim.py`) and their VALUE side still hits the V001/V008 earn-rate wall
  head-on (items only, no live baseline). Nothing open to sim; its verified
  constants ride HERE as grounding pins instead.
- **Idle T11+/prestige-cycle pacing (candidate B):** consumed lane-side — P015's
  own card records "Registering T11 WITH the mechanic's landing PR honors
  economy-v1.md's own verdict semantics"; V017 (conditional) already reshaped the
  purchase path. Not an open sim head.
- **Browser-game difficulty/session-length envelope (candidate D):** hermetically
  constructible (the P017/P024/P028 pattern) but chains to NO committed anchor —
  P027's drafting survey already measured this ("no committed in-tree baseline to
  chain to tonight"), and no Game Lab foundation order is visible in this repo's
  inbox at HEAD. A cold start loses on merit to a verdict-opened head whose build
  window is closing tonight.

## Sim spec (pre-registered)

**Model.** One player, THREE surfaces, merged event stream, 8 h window, V018's
5 committed seeds for the vendored parents plus fresh seeds for the explore layer.
Chat = V001 machine verbatim (med-tier honest / paced-farmer channels); grid =
V008 per-action gate verbatim (casual/deep/fastmine traces); explore = quest-beat
attempts as a Poisson stream at r_E/hr, each attempt requesting EXPLORE_ACTION
admission against (c_E clock, shared K-window); admitted beats advance the active
quest by 1 under GATED coupling (FREE coupling: progress advances on every
attempt, encounters fire only when admitted); quest completes at B beats, mints
the tier bundle, next quest offered immediately (chain — the engine's `offer` is
deterministic and instant at `5aec110`).

**Sweep (decision cells, K=4 binding).** c_E ∈ {0, 300, 600, 900} s × B ∈
{3, 5, 8} × coupling ∈ {gated, free} = 24 decision cells at K=4; the SAME grid at
K=6 runs reporting-only (V018 carved K to the owner and priced it — this sweep
reads the third trigger against both notches but re-pins nothing).

**Profiles.** Regression pairs (V018's, unchanged) · quest-focused (explore only,
r_E = 12/hr; sensitivity r_E ∈ {6, 30} reporting-only) · mixed-triple-casual
(med chat + casual grid + 6 beats/hr) · mixed-triple-deep (V018's mixed-deep +
12 beats/hr — the stress row) · three-way beat-steering farmer (paced-spam chat +
fastmine grid + saturating beat attempts, admission budget spent explore-first —
the value-steering adversary V018's rate-symmetric farmer could not express).

**Seeds.** 20260764 main / 20260765 stability (half-M, must reproduce the ruling)
/ 20260766 reporting / 20260767 aux self-check stream (never read by a decision
number) — allocated strictly above the P030 registry high-water 20260763.

**Gates (run invalid on any failure).** Exact regression to ALL of V018's
published numbers listed above; empty-third-surface composition identity to the
V018 machine event-for-event per seed; per-cell analytic ceilings (admitted
explore rate ≤ min(3600/c_E, K, r_E); farmer combined ≡ K exactly when saturated);
independent sliding-window re-audit of the K-cap; bundle-cap identity (currency/hr
≡ completions/hr × tier currency, tier ≤ GLOBAL_MAX component-wise); stdout +
results.json byte-identical across two process runs; CPython minor pinned.

**Decision rule (pre-registered order, REJECT checked first).**
- **REJECT** ("the third trigger cannot ride the shared window — carve it out
  before the cog build fixes it"): in GATED coupling at K=4, NO c_E passes
  FLOW+FAIR+MINT simultaneously in ≥ 2 of 3 B values. Consequence: EXPLORE_ACTION
  joins the combined K-window for its ENCOUNTERS but quest PROGRESS must not be
  admission-gated (the free coupling becomes the contract line); the lane pins
  quest pacing at the host gate per-completion (its own economy-sim frame), and
  the CONTRACT.md slice + Q-0186 build get the carve-out with the quantified
  starvation table.
- **APPROVE** ("the row completes — three triggers, one window"): ∃ c_E band of
  ≥ 2 consecutive grid values passing all three bands at K=4 in GATED coupling
  for ALL B ∈ {3, 5, 8}, stability-reproduced. Consequence: V018's contract row
  extends with the measured c_E band (namespace unchanged, K=4 unchanged, both
  parents' defaults untouched — nothing re-pins), plus the absolute
  currency-mint ceiling table as the row's new value line.
- **NULL** (anything else — legitimate and plausible): the flip axis named via
  per-axis pass shares — expected candidates B (at B=8 the K=4 window caps
  honest completions at 0.5/hr before c_E even binds — pure arithmetic) and the
  coupling fork itself; the citable finding is the CONDITIONAL rule (e.g. gated
  coupling viable only for supply_run-class 3-beat quests; multi-beat chains need
  free coupling), and the cheapest LIVE probe is named: the cog build ships
  V018's already-named combined-window telemetry EXTENDED with per-trigger
  admitted/denied beat counts + per-player quest currency/day — measuring r_E and
  the real coupling cost at zero new tooling.

**Boundaries (stated in the verdict).** Reward VALUE for the ITEM faucets stays
walled (V001/V008/V018's caveat restated verbatim — no live earn-rate baseline;
RATE terms only for chat/grid mint); the quest faucet's currency conclusions are
in native absolute units BY CONSTRUCTION (committed in-tree bundle integers) and
the verdict must state this asymmetry explicitly. dnd's escort bundle (the other
host-gated faucet) is out of scope — different trigger surface, named as the
natural follow-up if MINT binds. Tier selection is modeled as the {II center,
III adversarial} bracket, not swept. Real beat rates are a model dial (r_E swept
reporting-only) until the named telemetry lands.

## Dedup (explicit, against outbox 001–030 + verdicts V001–V031)

- **P016 → V018** (the parent, deliberately): its answered question — namespace +
  combined cap for the TWO live triggers — is settled and not re-asked; this head
  sweeps exactly the cell its report excluded by name ("not by this sweep"), on
  its machinery, with its numbers as chained regression anchors.
- **P003 → V001, P008 → V008** (grandparents): solo-surface pacing, settled;
  their defaults are held fixed here by V018's row.
- **P020/P023/P027 → V022/V025/V029**: the casino family — house-banked wager
  balance, zero shared trigger/fixture/metric; its triage is closed.
- **P015 → V017**: idle-engine purchase curve, different repo and loop entirely.
- **P009 → V010**: same games, correctness (settlement) never balance/pacing.
- `ideas/superbot-games/shared-encounter-engine-consumer-contract-2026-07-10.md`
  (parked build-direct): the CONTRACT-SLICE capture this verdict feeds — it
  states "quest rewards are pinned by the lane's own balance sim" for the bundle
  SIZE and carries no pacing question; this head supplies the row that slice
  will carry. No overlap: capture = contract prose, this = the measured constant.
- Tree-wide `rg -i "explore_action|quest.?beat|host.?gate" ideas/ control/
  .sessions/` (bootstrap.py/.substrate excluded) hits only V018's own
  inherits-by-contract lines, P016's out-of-scope clauses, and the contract
  capture above. No proposal 001–030 and no sim-lab verdict V001–V031 sweeps
  EXPLORE_ACTION pacing, quest-beat admission, or any currency-faucet mint bound.

## Pinned constants (quoted at drafting — fixture JSON copies these verbatim)

- superbot-games @ `5aec110834345e20ce47941266fe598f43804ea0`:
  `TIER_CAPS = {I: (5, 25, 10), II: (10, 60, 25), III: (20, 120, 50)}`,
  `GLOBAL_MAX = (20, 120, 50)` (`games/exploration/quest/catalog.py`);
  `supply_run` objective `required=3`; the host-gate quote and the
  mining-360/fishing-180 + ore-480–600/fish-85–115 pinned bands with
  `ITEM_FAUCET_MINTS_NO_CURRENCY` (`games/shared/sim/economy_sim.py`).
- sim-lab @ `b50fd06` (`sims/verdict-018-encounter-coexistence/REPORT.md` +
  `results.json`): the regression-anchor set listed under Gates, incl. the
  committed contract row (900 s / 600 s / K=4 per 3600 s) and ARB_RATIO_MAX 2.0.
