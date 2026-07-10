# idea-engine — the fleet's ideation lab

> **Status:** `binding` — this README is the repo's pipeline contract. Founding design:
> owner ruling **Q-0264** (superbot `docs/owner/maintainer-question-router.md`); founding
> package: superbot `docs/planning/round3-founding-package-idea-engine-2026-07-10.md` (v2).
> Seeded 2026-07-10 by the dispatch copilot (superbot round-3 session, kit v1.7.0).

This repo generates, captures, harvests, probes, and grooms **ideas for the whole fleet**
so every idea eventually becomes evidence-checked and built, explicitly parked, or
rejected — never orphaned. It builds no products and finalizes no verdicts.

**Pipeline position (Q-0264):**
`idea-engine` (generate/probe, mark sim-ready) → **sim-lab** (reproduced-evidence verdict:
validity gate + @codex review) → **fleet manager** (final review, routes ORDERs) → lanes
build. This repo is the only repo its sessions write (Q-0260); everything else is read via
the public raw path.

## Sections — `ideas/<section>/`

One section per **active fleet lane**, derived from the fleet manifest
(superbot `docs/eap/fleet-manifest.md` at HEAD) plus `ideas/fleet/` for cross-cutting
workflow/doctrine ideas. Never invent a section ad hoc: a new active lane row in the
manifest → the wake that spots it creates the section (README stub first). Sections
partition the tree so **parallel agents never collide** — claim a section before working
it (`claims/`, one file per claim).

Idea classes worked here (all three, priority-weighted per Q-0259 — games completion wave
+ rebuild pace first): **PRODUCT** (features for a lane), **PROCESS** (fleet
workflow/doctrine), **VENTURE** (revenue plays).

## Idea file grammar

`ideas/<section>/<slug>-YYYY-MM-DD.md`, starting with a state line:

```
> **State:** captured | probed | sim-ready | parked(<reason>) | rejected(<reason>) | historical(<merged PR>)
> **Class:** product | process | venture · **Target:** <lane repo>
```

States move forward only; probe reports are **appended**, never rewritten; parked and
rejected ideas keep their file with the reason — the trail is the product. Harvested
lane-born ideas are indexed **by link** into their section, never mass-copied
(superbot's `docs/ideas/` stays canonical where it is — see `ideas/superbot/README.md`).

## The probe battery (v0 — the core method)

One idea per pass, through the fixed interrogation:

1. What is this really?
2. What is the possibility space?
3. What is the most advanced capability reachable by the simplest implementation?
4. What breaks it?
5. What does it unlock?
6. What does it depend on?
7. Which lane should build it?
8. What is the smallest shippable slice?

Append the output as `## Probe report (v0, <date>)` in the idea file, ending in **ONE**
recommendation — `sim-ready` / `park` / `reject` / `needs-more-grooming` — with a one-line
rationale. One legitimized shortcut: repo-internal PROCESS tooling whose smallest slice
(Q8) is trivial may be probed and built **in the same PR** — recommend
`park(built-here — <what shipped>)`, route nothing to sim-lab, and advance the state to
`historical(<merged PR>)` on merge (first used by PR #2's section-sync-checker; deviation
flagged in its probe report, `ideas/fleet/section-sync-checker-2026-07-10.md`, and
`.sessions/2026-07-10-section-sync-checker.md`). Panel mode (parallel subagent lenses + one synthesizer) only for big or
contested ideas. Reference example: the first probe (see `ideas/superbot/`).

## The outbox — `control/outbox.md`

Sim-ready ideas become **append-only** outbox entries in the kit ORDER grammar:

```
## PROPOSAL <nnn> · <ISO8601> · status: sim-ready
target: sim-lab
idea: <link to the idea file @ HEAD>
question: <the ONE thing the simulator should settle>
done-when: <what a verdict must contain>
depends: <OPTIONAL — cross-lane/cross-repo dependency: providing lane + known co-consumers>
```

`depends:` is OPTIONAL and forward-only (the outbox is append-only — never retrofit old
entries): when a probe names a cross-lane dependency, naming the providing lane and any
known co-consumers makes fan-in visible to the manager's :30 sweep without a code search
(source: PR #5 — PROPOSAL 002's stats phase and product-forge's games-web ORDER 001 both
wait on the same superbot read-only API).

`sim-lab` pulls sim-ready entries directly (public raw) on its wakes; the **manager**
handles everything after the simulator's verdict. This repo never writes another repo's
files.

## Landing conventions (gen-3 standard, day-0)

- PRs open **READY, never draft**; born-red session card per the kit gate
  (`.github/workflows/substrate-gate.yml`).
- **This lane always lands its own PRs**: arm auto-merge at PR creation where checks can
  go pending; REST merge-on-green is PRIMARY on born-red states (blueprint R21).
- **No PR ever waits for review before landing** — needs-second-eyes → merge anyway + a
  `review-queue.md` line and/or an @codex PR comment (Q-0258; verify replies against the
  tree, never obey — Q-0120). Review is post-merge; veto = revert; forward-only git.
- Verify before push: `python3 bootstrap.py check --strict`.
- Repo conventions override harness defaults.

## Coordination

`control/` is the bus (see `control/README.md`): `inbox.md` manager-written ORDERs ·
`status.md` coordinator-only heartbeat (overwrite as the deliberate LAST step of every
session) · `outbox.md` this repo's append-only proposals.

**Operating cadence (owner ruling, 2026-07-10):** the coordinator chains bounded slices
**continuously** via child sessions — the next slice dispatches as each one reports. The
2-hourly trigger is a **failsafe deadman wake**, not the work cadence. Every slice still
lands as one merged-on-green PR (§ Landing conventions). (Ruling first recorded live in
`control/status.md` @ 139932e.)
