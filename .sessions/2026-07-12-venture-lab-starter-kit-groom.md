# Session — grooming pass: venture-lab substrate-kit agent-fleet starter

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-12 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

One grooming pass (the probe's `needs-more-grooming` follow-through) on
`ideas/venture-lab/substrate-kit-agent-fleet-starter-2026-07-11.md` — reasoned the
partial idea to its fuller form per the maintainer profile (superbot Q-0254),
closing each probe-named gap by name in a dated `## Grooming pass (2026-07-12)`
section: (1) the false "pure packaging, two clicks" costing replaced with the
honest four-owner-decision + curation-slice ledger; (2) the open-core boundary —
absent from every tree at probe time — drafted as a paste-ready 3-option owner
choice, recommendation first (Q-0263.2); (3) the kit-lane vs venture-lab ownership
split recommended and flagged for the manager sweep; (4) the smallest shippable
slice re-scoped (the zero-gate slice was the boundary draft itself — this pass IS
it); (5) a pin-to-tagged-release rule for the moving kit target; (6) the
public-status anomaly routed to the kit-lane head.

Grounding refreshed, not reused: `git ls-remote` re-pinned substrate-kit main at
`8a544a6` (v1.12.1, one release since the probe's `fa921f4`/v1.12.0) and the
pending-owner-action ledger re-read at that ref confirmed all three kit-side gates
(settled name, P8, P11/P13) still open — the park is grounded at a fresh pin.

State advanced forward `probed` → `parked(owner-gated — behind kit
public-readiness…)` with the re-open trigger carried into the index badge (PR #192
card convention); a `Sequence: behind …` header line stamped (the probe-derived
ordering constraint, README optional-line grammar). Dedup sweep recorded in-file:
no true duplicate; one NEW overlap found and bounded (the rank-5 playbook e-book's
Gumroad channel vs this head's doctrine bundle — files-vs-narrative split).

Files touched: the idea file (state flip + Sequence line + grooming pass append),
`ideas/venture-lab/README.md` (index bullet re-badge), this card. No code.

Coordinator-imposed deviations, declared (mirroring the PR #222 slice): PR opened
DRAFT (not READY-at-open) and never self-merged; NOTHING under `control/` written
by this slice (no claim file, no heartbeat) per its dispatch boundary —
section-collision risk declared in this card's born-red first commit instead of a
claim file, and the gap-3 ownership flag for the manager rides the idea file +
this card, not a heartbeat line. Read-only side check recorded for the
coordinator: `control/inbox.md` carries ORDER 001 and ORDER 002 only — no ORDER
003+ at branch time (main `5e50274`).

- **📊 Model:** fable-5 · docs-only grooming slice (one grooming-pass append +
  state flip + Sequence line + index re-badge + card; no code)

## 💡 Session idea

A probe that ends `needs-more-grooming` should name its gaps as a NUMBERED list in
the recommendation rationale, not as prose spread across Q1–Q8: this pass spent
its first read reconstructing "which gaps exactly?" from four battery answers.
A `gaps: 1) … 2) …` line at the recommendation would make the follow-up grooming
slice mechanical — same shape as the fired-trigger badge rule (PR #192), applied
to the probe→groom seam.

## ⟲ Previous-session review

PR #222's card (fleet-program-pulse-feed probe) is the newest sibling with the
same dispatch boundary (draft PR, no `control/` writes) — its
declare-collision-risk-in-the-born-red-card workaround was adopted here verbatim,
and its verify-at-LIVE-HEAD discipline paid off again: the kit had released
v1.12.1 overnight, and re-pinning (rather than reusing the probe's fa921f4)
turned "the gates were pending yesterday" into "the gates are pending today",
which is the fact the park actually stands on. Its auto-draft close-out needed
hand-correction against a wrong diff base; this card was written by hand from the
start.

## Handoff → next wake

The gap-3 ownership flag (kit-lane public-readiness head vs venture-lab sale
head) needs a coordinator heartbeat line to reach the manager's sweep — this
slice could not write one. Re-open triggers to watch on future kit re-pins:
the distribution name losing its "placeholder" comment in pyproject.toml, P8/P11
leaving the pending ledger in `docs/current-state.md`, or a manager ownership
ruling. Guard recipe: re-pin via `git ls-remote https://github.com/menno420/substrate-kit.git main`,
then `rg -in 'P8|P11|placeholder' docs/current-state.md pyproject.toml` at the new
ref; test target `python3 scripts/preflight.py`.
