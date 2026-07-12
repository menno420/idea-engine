# Session — websites re-harvest round 4 (close-out wave + first new standalone doc)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-12 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

One harvest sweep of the websites lane, pinned at live HEAD `8f97654`
(`8f9765483a7df57ce426e7d11d200f10b5495ed7`, `git ls-remote` re-resolved
2026-07-12T01:46Z — byte-identical to the HEAD the three P002-family probes
PRs #222/#225/#233 verified, no move). Watermark: the round-3 re-harvest
(2026-07-11, PR #151-era card `2026-07-11-websites-round-3-reharvest.md`),
websites pin `c81ce76` (its `f7f07e7` tail-move was verified moved-only there).

Sweep surfaces at the pin (shallow clone in the scratchpad, read-only; gh absent
and anonymous api.github.com 403s via the proxy — the standing recipe):
`docs/ideas/` (checker-sized: 1 CHANGED + 1 NEW), the 51 post-watermark commits
`c81ce76..8f97654`, `control/status.md` (final parked-chain heartbeat @ #153-era),
docs TODO/FIXME/DEFERRED markers (all owner-deferred items already flagged, none
idea-shaped-and-unflagged), `review/gen_snapshot.py` + `review/story.py` headers
(architecture prose, no seed markers), and the post-close-out session cards
(archive-prep, v1.12.1 — both 💡s verified folded into backlog.md).

Findings → actions:

1. **ONE genuine new find indexed by link:**
   [`ideas/websites/merge-hold-at-head-2026-07-11.md`](../ideas/websites/merge-hold-at-head-2026-07-11.md)
   — the section's first NEW standalone canonical doc since the first harvest
   (born in the lane's archive-prep capture, websites #154). `captured`,
   mirroring the canonical front-matter. Dedup: zero hold-coordination capture
   anywhere in `ideas/` (`rg` stem sweeps; nearest misses named in the entry);
   no overlap with the #222/#225/#233 probe family (pulse-feed, explorer-facets,
   story-bubble — different objects).
2. **Fourth re-pin section** appended to
   [`lane-backlog-2026-07-10.md`](../ideas/websites/lane-backlog-2026-07-10.md):
   backlog blob `0897a6f` → `e14bb15`, +194/-30 by `check_harvest
   --bullet-drift` (the pin record's second live CHANGED catch). Lifecycle
   14 captured / 31 built / 6 retired (was 6/24/5): 2 flips, 1 bullet REPLACED
   in place (route clock freeze shipped PR #130 with no Built entry — the
   backlog's first bullet deletion, honesty-noted), 5 born-Built, 1
   born-Retired, 11 new-born captured, 3 survivors. Per section convention the
   backlog's bullets ride the link entry — none promoted to standalone files
   without a probe.
3. README index re-badged (lane-backlog bullet + harvest paragraph incl. its
   leading pin sentence — the line `check_harvest` actually parses, caught live
   when the first post-edit run reported a STALE record + new merge-hold
   entry); `.harvest-pin.json` re-recorded at `8f97654` by hand
   (websites section only — the checker's `--write-pins` is all-sections and the
   superbot pin is stale with 2 NEW upstream docs, ANOTHER lane's sweep; exactly
   the per-section-selector gap the round-3 card's 💡 named, lived again).

Deduped-not-indexed (named, per the honest-nulls bar): the sanitized `guilds[]`
export ask — already a flagged manager item on the lane heartbeat @ `8f97654`
AND a backlog bullet (rides the link entry); the ten other new backlog bullets —
lane work items/routed asks covered by the re-pin section; all built/retired
flips — outcomes, not ideas. VERDICT 011 fallout checked: no lane-side idea
notes exist for the dead-link families or the review-service non-deploy at the
pin (the latter is owner-ask #4 on the heartbeat, not an idea seed) — grep
`verdict|dead.?link` across the lane's docs/control returned only unrelated
retro/ledger prose.

Coordinator-imposed deviations, declared (mirroring the PR #222/#238 slices):
PR opened DRAFT then flipped ready (not READY-at-open) and never self-merged;
NOTHING under `control/` written by this slice (no claim file, no heartbeat) per
its dispatch boundary — section-collision risk declared in this card's born-red
first commit instead of a claim file. Read-only side check recorded for the
coordinator: `control/inbox.md` @ main `4f50cce` carries ORDER 001 and ORDER 002
only — no ORDER 003+ at branch time.

- **📊 Model:** fable-5 · harvest docs only (one new link-index entry + fourth
  re-pin section + README re-badge + pin record + this card; no code)

## 💡 Session idea

A backlog bullet REPLACED in place (shipped work absorbed, residue re-captured
under a new title, no Built entry) is invisible to every drift class the checker
has — filename-set, blob-compare, and `--states` all see "content changed", and
only a human diff caught that a bullet VANISHED. One-paragraph grooming seed:
teach `--bullet-drift` to diff the bullet TITLE SET (the `- **…**` heads) inside
a CHANGED doc and report `BULLET DELETED (title gone)` alongside the line
counts — the same trail-is-the-product rule the doc-level DELETED class already
enforces, one level down.

## ⟲ Previous-session review

The round-3 card (`2026-07-11-websites-round-3-reharvest.md`) held up as the
watermark on every load-bearing fact: its `c81ce76` pin, its `f7f07e7`
moved-only verdict, and its `.harvest-pin.json` record all reconciled exactly
against live HEAD — and its 💡 (per-section `--write-pins` selector) fired
again verbatim this session: the superbot pin is stale, so the all-sections
writer could not be used and the websites record was hand-edited. Two harvests
have now paid the same tax; the selector seed is ripe. One gap: its handoff
flagged the kit-shaped quality.yml bullet for a substrate-kit cross-link, which
this sweep confirms is MOOT — the lane self-served the fold (PR #120) before
any cross-link landed; the lane-self-serve lesson eats another routed idea.

## Handoff → next wake

The merge-hold capture is probe-ready and cheap to verify (self-serve-aware:
budget the five-minute check FIRST — `git ls-remote` the lane, then
`rg 'HOLD-' control/` in a shallow clone; the lane self-serves within hours,
six datapoints). The superbot section carries 2 NEW upstream docs + a moved
pin (checker-sized this session, out of this one-lane slice's scope) — the
next superbot harvest should take them with a fresh sizing. Checker seed to
groom: bullet-title-set diff (this card's 💡) + the twice-lived per-section
`--write-pins` selector.
