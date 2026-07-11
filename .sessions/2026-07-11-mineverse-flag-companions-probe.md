# Session — batched probe: the two mineverse FLAG companions (snapshot-contract-shared-constant + shim-replay-determinism-harness)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

The two expiry-aware heads named by the #92 card's handoff, executed as ONE batched
slice (both single-pass battery v0, no panel triggers): probes of
`ideas/superbot-mineverse/snapshot-contract-shared-constant-2026-07-11.md` +
`ideas/superbot-mineverse/shim-replay-determinism-harness-2026-07-11.md` — the FLAG 1
and FLAG 2 companions. Two FULL batteries, no pointer-disposition: these are sibling
ideas on different surfaces (a constants module vs a property test), so neither folds
into the other — the #87 pointer precedent was for one-surface pairs.

Verify-first at build time (05:34:43–05:35:57Z, live): `git ls-remote` —
superbot-mineverse HEAD still `2b1bd0b`; its control/status.md (04:27Z) still carries
both FLAG blocks as unpicked externally-blocked specs; superbot-next's queue (05:01Z)
is Discord parity ports, zero mineverse/FLAG work; roster gen #5 (04:28Z) shows no
pickup — **window open**, probes live. All three pinned contract files re-fetched at
BOTH pins: `tests/test_snapshot.py` + `schemas/mining_snapshot.v1.schema.json` +
`tests/test_actions.py` each byte-identical 510fa3e↔2b1bd0b; `snapshot_contract.py`
404 at main (nobody built it). One capture correction: 35 `def test_` functions, not
"34 cases" — counting method, not drift.

Verdicts: BOTH **parked(build-direct)**. (1) snapshot-contract-shared-constant — a
scope promotion, not new validation: the schema-derived constant ALREADY lives
in-test (test_snapshot.py line 22); the slice is a ~20-line importable module + a
two-line test edit; no sim question; sequenced with the pending seam ruling / FLAG 1
pickup so the constant lands in its final home. (2) shim-replay-determinism-harness —
one committed-seed property test, zero new deps, portable to the real endpoint via
the `make_shim_server` base-URL fixture seam; a property harness is proven by its own
runs, and the only sim-shaped question (shim-vs-real divergence classes) needs the
not-yet-existing FLAG 2 endpoint. No PROPOSAL — outbox tail stays 006, untouched.

Claim: fast-laned first as PR #98 (squash `18e5a54`), claims dir re-read at HEAD (only
this claim live — the venture-lab sibling's claim cleared in its own #97), claim file
deleted in this PR per convention (#89-cleared-in-#92 precedent).

**📊 Model:** fable-5 · docs-only (two probe appends + state flips + index flips +
claim clear + heartbeat + card; no code)

## 💡 Session idea

Batched probing of sibling companions bought exactly one thing: ONE shared
verify-first pass amortized over two expiry-aware heads (the window check + pin
re-fetch is the expensive, perishable part; the batteries themselves are cheap and
independent). Cheap codification: when two captured ideas share the same window event
and the same grounding pins, batch them under one claim and stamp one verify-first
header both reports cite — but keep the batteries FULL and separate; the batch is a
verification economy, never a disposition shortcut.

## ⟲ Previous-session review

PR #92 (`probe/snapshot-field-parity-audit`, squash `a693946`) + the #93 fix slice
(`fix/card-slot-post-90`, squash `466ccdd`): verified against the tree — #92's probe
report + state flip + index re-badge landed clean, its claim `probe/
snapshot-field-parity-audit.md` is gone, and its card is `complete`. The prior
heartbeat's "this slice" last-shipped entry was still number-less ("number written
only after the PR exists") — THIS session performs its #92 stamp in the heartbeat
overwrite, per the #72/#79 precedent. #93's cleanup (literal fill-token dropped from
the #90 card + 3 stop-advisory guard fires flushed) verified present; the follow-on
telemetry flushes #95/#96 landed after it, so guard-fire residue is being kept
current by siblings — this branch cut clean with no dirty `.substrate/` state to
carry. Workflow kept from #92: card flipped `complete` before the single final push
so the enabler arms with the branch already FINAL.

## Handoff → next wake

All three pre-staged mineverse companions are now dispositioned (parity-audit
MEASURED + these two PROBED parked(build-direct)) — the section's captured backlog is
`heartbeat-ladder-field-2026-07-11.md` (process, → fleet-manager) only. Nothing
further from this repo on the FLAG family until the manager's seam ruling or a FLAG
pickup; when FLAGs 1/2 are picked up, both parked files are ready-to-build one-file
lane specs (each probe's Q8 names the exact slice). Ripest next heads: the
heartbeat-ladder-field capture (non-expiring), and the PR #85 stale-card conflict
remains a coordinator hygiene item.
