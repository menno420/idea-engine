# Session — coordinator first boot: probe battery v0 over one idea (walking-skeleton PR)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 ~18:0x–18:1xZ (coordinator seat, first boot —
> founding package §2 step 3 onward; seed handoff in `.sessions/2026-07-10-seed.md`)

## What this session did

- Claimed `ideas/superbot/` (`claims/probe-superbot-brainstorm-simulator-v0.md`; cleared
  at close per `claims/README.md`).
- **First probe (battery v0, README § The probe battery):** superbot's
  `docs/ideas/idea-probe-brainstorm-simulator-2026-07-10.md` — the battery probing itself.
  Link-index entry + probe report:
  `ideas/superbot/idea-probe-brainstorm-simulator-2026-07-10.md` (canonical stays in
  superbot, Q-0264.8). Verdict: **sim-ready** — mode 1 proven-by-use in the report itself;
  the open question is whether panel mode earns its cost. This report is the battery's
  reference example.
- **PROPOSAL 001** appended to `control/outbox.md` (target sim-lab; question = panel mode
  vs single-pass battery on real backlog ideas; done-when = reproduced-evidence ruling).
- Section index updated (`ideas/superbot/README.md`).
- Routine armed by the coordinator: "idea-engine 2-hourly standing wake", cron
  `0 */2 * * *` — details recorded in `control/status.md`.
- **Walking-skeleton proof:** this PR is the repo's first — branch → PR (READY, never
  draft) → `substrate-gate` → merge-on-green per README § Landing conventions. Verify
  ran before push: `python3 bootstrap.py check --strict` green.

- **📊 Model:** fable-5 · high · docs-only (probe + control + session ceremony)

## 💡 Session idea

**Probe-report lint** — a tiny stdlib checker (fits `bootstrap.py check` or a
`scripts/check_probe.py`) that verifies an idea file claiming `probed`/`sim-ready` state
actually carries a `## Probe report` section answering all 8 battery questions and ending
in exactly ONE of the four recommendations. Question 4 of this session's own probe named
"confident padding" as the battery's failure mode; a shape-checker is the cheapest guard
(it can't judge honesty, but it kills silent half-probes and battery drift between copies).

## ⟲ Previous-session review

The seed session (`.sessions/2026-07-10-seed.md`) left an accurate, immediately actionable
handoff — boot steps 1–2 done, start at step 3 — which this session executed without
re-derivation; that is what a good card buys. One friction inherited: the claims
convention says `claims/<branch>.md` but branch names contain `/` (this repo's own seed
used `probe/…`-style naming nowhere, this session chose `probe/superbot-…`); flattened the
slash to a dash rather than nesting a directory. Guard recipe: one clarifying line in
`claims/README.md` ("flatten `/` in branch names to `-`") — no code anchor needed,
prose-only fix.

## Handoff → next wake

PROPOSAL 001 sits in the outbox for sim-lab's pull; nothing to babysit. Next wake: normal
loop — inbox first (expect manager ORDERs eventually), then either a new probe from the
superbot backlog (`docs/ideas/README.md` index) or the seed card's section-sync-checker
idea as a first `ideas/fleet/` capture. Owner clicks still pending from the seed card:
required-check + auto-merge settings (this PR's gate run names the exact check string).
