# Session — public-leaderboards-committed-feed probe (battery v0, websites section)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 (dispatched by the continuous-mode coordinator per Q-0265)

## What this session did

Probed `ideas/websites/public-leaderboards-committed-feed-2026-07-10.md` — the PR #31
capture that fronts the owner's stats ask with a zero-auth `leaderboards` export family
— through battery v0, single-pass (README panel default: no repeat-disagreement signal,
no irreversible surface; the idea is docs/contract-shaped). Verdict:
**park(routed)** — no simulator question exists, and the probe REVERSED the capture's
front-run premise on live evidence.

The decisive live finding (all transport-verified this session, `git ls-remote` at
23:50Z + raw fetches ~23:55Z): at superbot HEAD `7c6278e`, BOTH committed feeds
(`dashboard/data/dashboard.json` — 13 families, all repo-derived, its `telemetry` is
agent-session telemetry; `botsite/data/console.json`) carry ZERO game runtime data;
`dashboard/data/leaderboards.json` 404s; the contract pins only `["meta","bugs"]` v1;
and the producer `scripts/export_dashboard_data.py` is a pure-stdlib STATIC REPO SCAN
that never touches the production Postgres. So the capture's "family, not API"
distinction dissolves: a leaderboards family needs a NEW production-DB egress — a
strict subset of the §4 read-only API's core (same per-server player rows, no auth,
public bounded top-N) — and therefore belongs INSIDE the batched superbot providing
ORDER as its zero-auth FIRST RUNG, not ahead of it. The websites half (render seam,
TTL cache, honest-degrade envelope, render-time contract pin — `dashboard/
data_source.py@98ce6c0`, live serving ~12 pages) is fully in hand and
order-independent; the page is build-direct once the family lands. VERDICT 003 re-read
raw at the sim-lab pin `8713f26` at write time (not copied forward): named change (4)
routes the §4 API as a superbot-lane ORDER FIRST — this probe hands the manager that
ORDER's internal sequencing (rung 1 committed feed → rung 2 token-scoped API) plus the
third consumer's exact needs-vs-haves split (probe Q6).

State moved forward `captured → parked(routed — …)`; probe report appended per the
lint shapes (8 questions, 3 Grounding lines + 1 Sequence line in blessed byte-form,
`**Recommendation: park**`). NO outbox entry — the grammar routes only sim-ready
proposals, and manufacturing a sim question (producer egress mechanism = design call
inside the providing ORDER; name-exposure policy = owner data-shape decision) would
violate the honesty norm. Claimed
`claims/probe-public-leaderboards-committed-feed.md` first (websites section, one idea
file), deleted before merge. Preflight (`python3 scripts/preflight.py`) + `python3
bootstrap.py check --strict` green before push; landed per README § Landing
conventions (PR READY, merge-on-green).

**📊 Model:** fable-5 · high · docs-only (one idea-file probe append + state line, card, heartbeat; no code)

## 💡 Session idea

A capture that names its own producer ("the existing exporter") is exactly where a
probe most needs the PR #34 lesson generalized: verify not just that the pattern
exists but that the pattern's MACHINE can reach the data — the exporter pattern was
live and still could not produce this family (no DB access anywhere in the committed
pipeline). Candidate grooming-round-3 checklist line alongside the PR #34 one: "an
idea pricing an export/feed slice should verify where the data actually lives vs what
the named producer can actually read."

## ⟲ Previous-session review

The deferred-VERDICT-003-note slice (PR #43, `.sessions/2026-07-10-verdict-003-websites-note.md`)
handed off cleanly and honestly: its `## Sim verdict` note on the stats/story idea is
byte-faithful to the verdict this session re-read at the same pin `8713f26` (ruling,
the four named changes, the phases-1–2 no-wait line all match the source), its
"re-verify at write time, don't copy forward" norm was adopted here directly, and its
handoff list named this exact probe second ("sharpens the batched superbot providing
ORDER that VERDICT 003 just made harder to defer") — an accurate priority call, since
the probe did materially change that ORDER's shape (rung structure + a reversed rider
premise). Verified against the tree: its claim is gone at HEAD `528f045`, the deferred
queue it declared EMPTY checks out (no remaining verdict lacking an idea-file note),
and the inbox it reported empty is still empty. One nit carried forward, not a defect:
its heartbeat `updated:` stamp (23:58:00Z) was slightly AHEAD of this session's branch
time (23:54Z) — a future stamp is the exact staleness-math hazard the control/README
warns about; this session's overwrite re-anchors to real wall-clock.

## Handoff → next wake

Inbox first. This probe consumed the "public-leaderboards probe" head from the standing
ripest list. Ripest next: the websites-backlog probe heads (own-heartbeat parse
self-check, review-queue row auto-check), the check_harvest output-refinement bundle
(PR #26/#37/#38 card 💡s, possibly probe-and-build-same-PR), grooming round 3 (now
carrying the verdict-tracking seeds + this card's producer-reachability checklist
line), the open-work-sweep merged-branch-pruning follow-up (PR #42 card 💡). For the
manager: the read-only-API fan-in note in the heartbeat is SHARPENED this slice — ONE
batched ORDER, three consumers, leaderboards as rung 1 (see notes).
