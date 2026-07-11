# Session — substrate-kit capture: carveout-needles config (kit carve-out scan, de-step-blinded)

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Captured — capture ONLY, deliberately not probed (the head goes into the section
backlog for a later battery pass) — the #125 card's 💡 kit-seam half as
`ideas/substrate-kit/carveout-needles-config-2026-07-11.md`: a host-declared
`carveout_needles` key in `substrate.config.json` (kit-owned file → list of literal
byte-needles) so the kit's OWN carve-out scan checks declared host edits explicitly
and reports a dropped needle even when it lives INSIDE a kit-owned step, instead of
being step-blind.

Evidence lineage pinned per the Grounding grammar (both raw fetches 200 at
2026-07-11T07:22:00Z):

- **Two-hop miss, same class:** the scan missed the enabler's in-step `Head-ref:`
  `--body` provenance edit on BOTH the v1.9.0 hop (PR #120, squash `f417a1f` — its
  survival table records "DROPPED — NOT named by the carve-out scan (in-step edit,
  step-blind scan)") AND the v1.10.0 hop (PR #125, squash `b11fe68` — its card:
  "NOT named — step-blind, exactly as on the v1.9.0 hop"). Both times only the #86
  card's manual-diff duty caught it.
- **The stopgap, cited as stopgap:** `scripts/preflight.py --enabler-anchors`
  (`ENABLER_ANCHORS` + `check_enabler_anchors`, ~lines 322–379 @ `b11fe68`) —
  REPORT-ONLY advisory, exit 0 unconditionally, promotion-to-gating condition
  recorded on the #125 session card (flip after one clean regen cycle). One host,
  two hard-coded needles; the durable fix belongs upstream in the kit's scan.

Cross-linked same-family per the section's linking convention:
`enabler-card-status-guard-upstream-2026-07-11.md` (host customizations on
kit-owned files — the guard upstream absorbs one needle's subject, this config
covers the residue and every future in-step edit) and
`host-checkers-one-gate-2026-07-10.md` (the config-seam sibling). Section index
row added to `ideas/substrate-kit/README.md` matching the existing format.

Files touched: the new idea file, `ideas/substrate-kit/README.md` (index row),
this card, `control/status.md` (heartbeat, LAST — kit-lane fan-in line for the
manager), claim `control/claims/seed-carveout-needles.md` deleted per convention.

Claim ritual honored: claim fast-laned FIRST as PR #127 (control-only, merged
`e1c6955` by the enabler within the minute), claims dir re-read at origin/main
HEAD after the merge — no competing claim on the substrate-kit section (the #126
verdict-registry sibling's claim cleared with its own merge, which landed
mid-flight and was forward-merged into this branch, never rebased). Claim file
deleted in this PR. Inbox re-read FIRST at branch time and again post-merge:
ORDER 001 (model-attribution standing rule) is the only order, already `done=` —
this card's `📊 Model:` line satisfies it for this wake too.

**📊 Model:** fable-5 · docs-only (one new capture + index row + card + heartbeat
+ claim clear; no code, no workflow edits, no outbox append)

## 💡 Session idea

A stopgap that names its own successor should carry a machine-findable pointer to
it: `--enabler-anchors`' docstring says "promote to gating after a clean cycle"
but nothing links the advisory to the upstream idea that would RETIRE it. A
one-line `supersedes-when:` marker on stopgap checks (naming the idea file / the
upstream seam) would let the next kit hop grep for retire-ready stopgaps instead
of re-deriving the lineage from three session cards — the same
guard-recipe-over-symptom move, applied to check lifecycles.

## ⟲ Previous-session review

PR #126 (`probe/verdict-registry-2026-07-11`, squash `186e8cc`) — the freshest
card at this slice's dispatch, verified against the tree at the forward merge:
the SIM-VERDICT lint landed in `scripts/check_ideas.py` with both smokes on its
card, its claim file gone at my claim-time re-read, card complete with the Model
line, heartbeat numbered #126 at its own write time ✓. Its mid-flight-reconcile
section (dirty PR, zero check runs, forward merge per the README recipe) is the
exact playbook this slice pre-armed for — and needed only the mild version of
(sibling landed between my claim push and build; forward-merged clean). Adopted
from it: fetch-RAW-at-the-pin before asserting field facts (both Grounding pins
curl-verified 200 this session) and the disjointness note pattern for sibling
claims. Also reviewed per dispatch, `2026-07-11-venture-lab-revenue-relay-probe.md`
(PR #104): its verify-first-at-live-HEAD discipline and "card complete BEFORE
push so the enabler arms at open" are both honored here; its handoff's
watch-item (venture-lab ledger fan-in) is untouched by this slice — disjoint
sections, shared heartbeat only, its ⚑ OWNER-ACTION preserved verbatim in this
overwrite.

## Handoff → next wake

- The capture is deliberately UN-probed: when the section is next worked, run the
  battery on `carveout-needles-config-2026-07-11.md` — expiry-aware note: the
  natural probe window is BEFORE the next kit hop (the promotion moment for
  `--enabler-anchors` per the #125 card; a kit-side `carveout_needles` adoption
  would change that promotion from "flip local check to gating" to "retire it").
- It composes with the still-captured `enabler-card-status-guard-upstream` head —
  a future probe could batch the two (same family, same target lane).
- Kit-lane fan-in line is on the heartbeat for the manager's :30 sweep: adopt
  needles config upstream; our enabler-anchors advisory is the interim.
- Friction for the ledger: none new — anonymous api.github.com still 403s via the
  proxy (GitHub MCP used, per the #126 card's note); one sibling (#126) landed
  mid-flight, forward-merged clean.
