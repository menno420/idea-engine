# Session — shared-encounter-engine consumer-contract probe (superbot-games): battery v0 → park(build-direct)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 (dispatched by the continuous-mode coordinator per Q-0265)

## What this session did

Probed `ideas/superbot-games/shared-encounter-engine-consumer-contract-2026-07-10.md`
through battery v0 against LIVE state, not the capture's snapshot: superbot-games @ HEAD
`b134961` (ls-remote 23:08Z + raw reads: `docs/lanes.md`, both lane status files,
`games/shared/encounter/{interface.py,reference.py,README.md}`,
`docs/design/quest-encounter-engine.md`, `docs/design/mining-grid-encounters.md`, plus a
blobless-clone `git ls-tree` sweep for every `shared|encounter` path), superbot @
`c5f501e` (fleet-manifest games-plugins row), sim-lab @ `bc6e0fe` (`control/outbox.md`
VERDICTs 001–004 + `control/inbox.md` INTAKE queue). Load-bearing find: **the contract's
v1 surface already exists** — exploration's gen-1 lane shipped the `EncounterResolver`
Protocol naming all three launch triggers (GRID_ROAM / EXPLORE_ACTION / CHAT_ACTIVITY),
so the capture's "write it before mining builds it" window partially closed; what remains
is the semantics layer (per-trigger payload/kind schemas, reward-routing rule) + a
conformance suite, and mining's production resolver does NOT implement the Protocol yet
(own `EncounterOutcome` — a name collision with the shared interface's). Verdict:
**park(build-direct)** — no reproducible-evidence question left for sim-lab (spawn tuning
settled by sim-lab VERDICT 001; grid balance sim-pinned in-repo §5; quest rewards pinned
by the lane's balance sim; schema sufficiency is settled by writing the adapters). NO
proposal appended (outbox stays at 5, all pulled; sim-lab has now finalized VERDICTs
001–004 — heartbeat updated with the four-of-five state, only INTAKE 005 queued). State
advanced forward-only captured → parked(build-direct); blessed Grounding
(@ `b134961`, manifest row: behind — staleness datapoint ELEVEN recorded) + Sequence
header lines added. Section claimed first
(`claims/probe-encounter-contract-2026-07-10.md`), claim deleted in the branch's final
push. Preflight (5 checks) + `python3 bootstrap.py check --strict` green before push;
landed per README § Landing conventions (PR READY, merge-on-green).

**📊 Model:** fable-5 · high · docs-only (probe report + heartbeat + card; no code)

## 💡 Session idea

A **cross-repo consumer registry line** in the contract grammar: when a shared seam's
consumer lives in ANOTHER repo (here: Q-0186's Encounters cog in the superbot hub cannot
import `games/shared/`), the contract doc should carry an explicit `mirrors:` row naming
the out-of-repo consumer and the schema fields it must copy (VERDICT 001's telemetry keys
here) — otherwise "one engine, N consumers" silently overclaims across a repo boundary.
Spotted while answering Q4; candidate line for the eventual
`games/shared/encounter/CONTRACT.md` slice AND for grooming round 3 on this repo's
`depends:` grammar.

## ⟲ Previous-session review

The superbot re-harvest slice (PR #38) handed off a clean tree (superbot section fresh @
`41899e1`, 237/237) and named the websites-backlog probe heads ripest; the coordinator
routed this superbot-games head to this worker instead, with a websites sibling in flight
— disjoint sections, no claim overlap. Inherited friction confirmed: anonymous
api.github.com 403s through the proxy (GitHub MCP used for PR ops on this repo only);
the ls-remote + raw + blobless-clone recipe (eight prior consumers on the capability
ledger) worked for every out-of-repo read this session — ninth consumer. The prior
slice's honest 23:03Z pull-state (INTAKE 004 in-progress, 005 queued) was already stale
by this session's 23:09Z read (VERDICTs 003/004 finalized 22:15Z/23:00Z) — sim-lab is
moving fast; heartbeat re-verified at write time, not copied forward.

## Handoff → next wake

Inbox first (empty at this session's read, HEAD 69523c5). Outbox: 5 proposals, ALL
pulled, four VERDICT-ed — only PROPOSAL 005's verdict is pending; proposal generation
stays un-throttled but the earn-rate bar holds (this slice appended nothing). Ripest
next: the websites-backlog probe heads (open-PR-awareness-at-wake first) unless the
in-flight sibling consumed them; the check_harvest output-refinement bundle; VERDICT
003/004 fan-out is MANAGER work, not ours — but note VERDICT 003 names the superbot §4
read-only API as UNBUILT+UNROUTED, which sharpens the standing read-only-API fan-in note
(PROPOSAL 002 + product-forge ORDER 001 + the leaderboards rider). In this section,
remaining unprobed superbot-games heads: ci-collection-parity-guard,
gen2-boot-pack-kit-upgrade-lane-adopt, host-seam-conformance-stub — the conformance-stub
capture overlaps this probe's Q8 slice; check it against this verdict before probing to
avoid a twin.
