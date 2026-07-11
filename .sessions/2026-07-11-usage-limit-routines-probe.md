# Session — probe: usage-limit-aware-routines (superbot section, TOP-5 item 4)

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-11 ~14:20Z (worker slice, coordinator-dispatched)

## Scope

Battery v0 probe of `ideas/superbot/usage-limit-aware-routines-2026-07-10.md` —
TOP-5 item 4, expiry-bound (EAP window wraps 2026-07-14, decision needed
≤2026-07-13). Claim landed first via fast-lane PR #173 (claim file
`control/claims/probe-usage-limit-aware-routines.md`, deleted at this close-out).

## What this session did

*(filled at close-out)*

**📊 Model:** fable-5 · probe slice (idea-file battery + state flip + Sequence
retrofit + index re-badge + heartbeat; no product code)

## 💡 Session idea

**Stamp `> **Sequence:** before <event>` on expiry-bound captures at harvest
time.** This expiry-bound idea carried NO `Sequence:` line — its 2026-07-14
deadline lived only in status-file prose, invisible to any expiry-aware
ordering of the probe queue. Harvest slices should stamp the Sequence line on
capture whenever the source names a hard date/event, so the README's
expiry-aware probe ordering can actually key on it instead of relying on a
human-maintained TOP-5 note. This probe retrofits the line
(`> **Sequence:** before EAP-window-wrap-2026-07-14`); the harvest-time rule is
the generalization. Anchors: `scripts/check_ideas.py` (optional-line lint
already knows the `Sequence:` grammar), the harvest slices' capture template in
`ideas/*/README.md`.

## ⟲ Previous-session review

Newest prior card: `2026-07-11-wire-automerge-enabler.md` (status `complete`).
Its shipped work held up at HEAD `62aad8c`: `.github/workflows/auto-merge-enabler.yml`
is present with all 13 `startsWith` clauses materialized from
`substrate.config.json::automerge.branch_patterns` (verified this session:
13/13, `seed-*` slashless), the gate workflow still carries the required
`substrate-gate` context, and — the strongest evidence — the enabler
**live-fired on this very session's claim PR #173** (branch
`probe/usage-limit-aware-routines-claim` matches `probe/*`; an
`enable-auto-merge` check run started at PR open, exactly the arm-at-open
behavior the card promised as "structural" from its merge onward). The card's
honest-stamps discipline (claiming the live-fire result only post-push) proved
warranted and its prediction correct. This previous-session review found no
drift; its 💡 (branch-prefix drift tripwire) remains queued and was separately
captured as an idea card.

## Handoff → next wake

*(filled at close-out)*
