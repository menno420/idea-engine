# Wager / money-flow map — generated trace of game coin paths — link index

> **State:** parked(routed — superbot's own read-only tooling slice per Q-0260: the AST tracer at its `disbot/services/game_wager_workflow.py` seam; sequence-sensitive — cheapest built BEFORE the V001/V008 loot-faucet landings, which are sim-green-lit but NOT landed at S=2c7d2de; no distinct sim question next to pending PROPOSAL 009)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/wager-flow-map-2026-06-12.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/wager-flow-map-2026-06-12.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/wager-flow-map-2026-06-12.md)).

A generated wager/money-flow map tracing game coin paths: hand-tracing where game money moves (four files per game, fees hidden in unrelated helpers) was the single biggest cost of the money-safety session.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/2c7d2de770fee76008b4561ef8165f1d97d78a52/docs/ideas/wager-flow-map-2026-06-12.md@2c7d2de770fee76008b4561ef8165f1d97d78a52 · fetched 2026-07-11T17:24:25Z
> *(pin annotation: superbot live HEAD S moved MID-SESSION — recon ls-remote earlier
> 2026-07-11 read `448584e`, the pre-work re-check read
> `2c7d2de770fee76008b4561ef8165f1d97d78a52` (ls-remote 17:23Z) — so every claim below
> was RE-verified at `2c7d2de`, not carried from the recon pin. Canonical doc
> byte-identical at both pins (diff clean). Invocation-wiring check FIRST, the #186
> card 💡 applied as idea-exists-is-not-idea-built: `scripts/wager_flow_map.py`,
> `scripts/coin_flow_map.py`, `scripts/economy_map.py`, `docs/economy/coin-flow-map.md`,
> `docs/wager-flow-map.md` ALL 404 at S=`2c7d2de`; superbot `scripts/` tree (~130 files)
> carries zero wager/coin/money/economy/flow/map filenames (recon census @ `448584e`);
> superbot-next `tools/check_settle_once.py` 404 at its main `e81bc9e`. The seam the
> tracer would read is ALIVE at S: `disbot/services/game_wager_workflow.py` → 200
> (note: the canonical doc says `services/` — the doc's path is already one directory
> move behind the tree, exactly the annotation-rot a GENERATED map is immune to).
> Faucet status at S: NO encounters cog (`cogs/encounters.py` + `disbot/cogs/encounters.py`
> both 404) and `docs/current-state.md` @ `2c7d2de` has zero encounter/loot-faucet hits —
> the V001/V008 builds have NOT landed.)*
> **Sequence:** before superbot V001/V008 loot-faucet landings (wild-encounters + mining-grid encounters — both sim-green-lit needs-more-evidence, neither landed at S=2c7d2de; faucets that land first are born untraced)

> Single-pass battery (panel not escalated: verify-first is decisive at the live pin,
> no ambiguity signal, no security/data/spend/public blast radius — README § probe
> battery). PROPOSAL 009 note, stated honestly: 009 (settle-once guard-contract catch
> matrix, appended 2026-07-11T16:36:50Z) is PENDING — sim-lab @ its live HEAD `e559a37`
> has NOT intaken it (its control/status.md, updated 15:16:50Z, says "no PROPOSAL
> 009+"; its own VERDICT 009 is an unrelated OWNER-DIRECT superbot-next sim). The
> six-instance double-settlement corpus 009 interrogates (this repo's
> settle-once-architecture-guard-2026-07-10.md:31-39, the #186 probe) lives on the
> SAME coin paths this map would trace — co-consumable evidence, DISTINCT questions:
> the map is a deterministic tracer (run it, read the output), 009 is a
> contract-choice evidence question (which guard contract catches the corpus at what
> false-positive cost). Neither blocks the other; a landed map would make 009's
> catch-matrix reconstruction cheaper by handing the verdict writer the per-game legs
> as a lookup instead of an archaeology dig.

**1. What is this really?**
A process/tooling idea captured by superbot's P0-1 wager-money-safety session
(Q-0089, PR #748): a read-only, offline AST tracer — `scripts/wager_flow_map.py`,
mirroring the existing `command_surface_dump.py` / AST-fence pattern — that finds
every call site of the six `game_wager_workflow` ops (`open_pvp_wager`,
`settle_pvp`, `refund_pvp`, `enter_tournament`, `payout_tournament`,
`recover_escrow`) plus every `*_escrow` / entry `game_state` constant, and emits a
per-game **accept → escrow → settle/refund** and **entry → payout** map with
file:line for each leg. The lived gap: hand-tracing where game money moves was the
single biggest cost of that session — four files per wagered game, and the
tournament fee debit hidden in `utils/tournaments.deduct_fees`, a shared helper
named nothing like "money". Verify-first: nothing of it is built anywhere (the
five-path 404 sweep + filename census in the pin annotation above).

**2. What is the possibility space?**
(a) The v0 map generator (six-op call-site resolution + per-game leg emission,
`--json` mode). (b) A `--check` drift mode asserting every escrow subsystem has a
matching settle AND a recovery path — a future game that escrows but forgets to
refund becomes structurally catchable. (c) The human-readable companion to the AST
fence `test_game_wager_write_boundary` — the fence proves no money leaks OUT of the
workflow, the map shows what flows THROUGH it. (d) The canonical doc's own
extension: mining shares the same `*_workflow` seam, so the tracer generalizes to a
unified "where does the economy move?" map — which is also where V008's
audited-seam encounter resolution (`mining_workflow` RS02/Q-0071) would surface in
the output. (e) Downstream, not built here: cheaper PROPOSAL 009 verdict work (the
preamble's co-consumable note).

**3. What is the most advanced capability reachable by the simplest implementation?**
The whole idea is already the simplest implementation: one stdlib-AST read-only
script, no runtime, no bot, CI-safe (the disposable-guard discipline Q-0105 applies
by the doc's own citation). The most advanced capability on that same walk is the
`--check` mode — escrow-without-settle / escrow-without-recovery becomes a CI
assertion, not a code-review hope — and it reuses the identical op/constant
resolution the plain map needs; the delta between "map" and "drift guard" is an
output formatter versus a set-difference.

**4. What breaks it?**
Timing, mostly. The map is cheapest while every wagered move is converged on the
single seam AND before new faucets land: V001 (wild-encounters, threshold=24/
debounce=30s/cooldown=900s defaults) and V008 (mining-grid encounters,
threshold=15-20/chance=0.02/cooldown=600s, per-player cooldown, audited-seam
resolution) are both green-lit needs-more-evidence and both mint coins on these
paths — each one that lands before the tracer is born untraced and becomes
retrofit archaeology (the exact cost the idea exists to kill). Second break mode:
staleness — a map generated once and committed rots like any folio; the `--check`
CI mode is what keeps it honest (Q-0105). Third: path drift is real and already
observable — the canonical doc's `services/game_wager_workflow.py` is one
directory move behind the live tree's `disbot/services/` — which cuts FOR
generation over hand-maintenance.

**5. What does it unlock?**
Turns the money-safety session's single biggest cost into a one-command lookup for
every future "touch a wager path" session; lets the V001/V008 faucet builds land
born-traced (their new mint legs appear in the map the day they merge); gives
PROPOSAL 009's eventual verdict writer the per-game leg inventory for the
six-instance corpus as a lookup; and extends naturally to the unified economy map.
Lane-side here: closes standing TOP-5 item 5 — the TOP-5 is now fully consumed
(items 1-5), so the next groom re-ranks.

**6. What does it depend on?**
Nothing open. The seam it reads exists and answers at S
(`disbot/services/game_wager_workflow.py` → 200); the six op names and the AST
fence it complements shipped with P0-1; the patterns it mirrors
(`command_surface_dump.py`, the fence) are live precedent in the same tree. It
does NOT depend on PROPOSAL 009 (pending, not intaken — preamble pin), and 009
does not depend on it; the only coupling is that a landed map cheapens 009's
verdict reconstruction. No owner decision required: the canonical doc already made
the design calls (read-only, offline, disposable-guard discipline).

**7. Which lane should build it? (honest routing)**
superbot itself — canonical-side, read-only tooling in its own `scripts/` tree per
Q-0260 (this repo writes no lane files). The canonical doc already routes it:
"quick-win, read-only tooling — not auto-promoted. Build it the next time a
wager/economy path is touched" — and the V001/V008 faucet builds ARE that next
touch, so the routing ask is pure sequencing: land the map slice first (or as the
first commit of the first faucet PR), flagged on the heartbeat for fleet-manager
routing. NOT sim-lab: no genuine evidence question survives here distinct from
PROPOSAL 009 — a tracer is deterministic (build it, run it, read the output; there
is no parameter space, no design fork the canonical doc left open), and the one
sim-shaped question on these coin paths is already 009's. NOT superbot-next: its
economy is manifest-compiled from scratch and its settle-once question is 009's
scope, not a retrofitted tracer's.

**8. What is the smallest shippable slice?**
At the owning lane: `scripts/wager_flow_map.py` v0 that ONLY resolves the six
workflow ops' call sites across `views/` + `cogs/` and prints the per-game legs
(file:line) — no `--json`, no `--check`, no mining extension; that alone replaces
the archaeology dig, and both extras ride the same AST walk later. For THIS repo
the smallest slice is exactly this probe: state flip + the sequencing flag on the
heartbeat (map before faucets) for fleet-manager routing. Nothing else to build
here.

**Recommendation: park** — routed: superbot's own lane doc/tool slice (a read-only
tracer in its `scripts/` tree at the `disbot/services/game_wager_workflow.py` seam,
Q-0260 canonical-side; the canonical doc's own routing — "build it the next time a
wager/economy path is touched" — makes the sim-green-lit V001/V008 faucet builds
the trigger), sequence-sensitive: cheapest landed BEFORE those faucets so they are
born traced, not retrofitted; no distinct sim evidence question next to pending
PROPOSAL 009 (the map is a deterministic tracer; 009 owns the contract-choice
question on these same coin paths) — no proposal.
