# 2026-07-14 — kit upgrade v1.16.0 (distribution)

> **Status:** `complete`

substrate-kit v1.15.0 → v1.16.0 distribution upgrade (PR #422).

## What shipped

- Release asset sha256 three-way verified before running anything:
  downloaded bootstrap.py `bba34e21…9170` (980,026 B) == release.json
  `sha256` field == the wave's expected hash.
- Mandatory two-command flow, both run: `python3 bootstrap.py.new upgrade`
  then `python3 bootstrap.py upgrade --apply-docs`; the report carries
  `## Applied (--apply-docs)` with 4 applied lines (`CONSTITUTION.md`,
  `docs/collaboration-model.md`, `docs/SKILLS.md`, `docs/ROUTINES.md`).
  Capability-seed fence + seat-digest: already current, nothing refreshed.
- **Q-0261.3 rails held (the #367 precedent):** the regen DID overwrite both
  host-customized workflows; both were restored byte-identical to
  origin/main before push — `auto-merge-enabler.yml` sha256 `e3275f45…`
  (wide prefix allowlist + in-diff-card skip step preserved),
  `substrate-gate.yml` sha256 `0c855c92…` (wake-preflight carve-out step
  preserved). Pre-regen banks committed as audit artifacts
  (`.substrate/backup/substrate-gate.pre-regen-0c855c92.yml`; the enabler
  bank `e3275f45` was already tracked from the v1.15.0 wave).
- New v1.16.0 plant `docs/reading-path.md`: strict-red on arrival
  (`[reachable]` orphan + `[unrendered-banner]`). Cured in-session —
  **decide-and-flag:** the three fleet slots were answered from standing,
  derivable fleet doctrine rather than parked (dark repo =
  `pokemon-mod-lab`, per superbot Q-0272 doctrine; fleet-status command =
  none yet in this repo; sibling map derived from this repo's own `ideas/`
  sections + `control/` bus contract), then `render --live`; the orphan
  cleared with a minimal wiring hunk into the diverged
  `docs/AGENT_ORIENTATION.md` (fleet-manager #114/#123 standing pattern).
  If the owner wants different slot values, re-answer + re-render is a
  two-command reversible edit.
- New banked archive: `.substrate/backup/bootstrap-1.15.0.py`; all
  pre-existing banks byte-identical (git-verified). No `control/**`,
  `.claude/settings.json`, hooks, or content-file (`ideas/**`) changes.

## Verify evidence

- `python3 bootstrap.py check --strict`: both real findings cleared; the
  only exit-affecting item before this flip was the designed born-red hold
  on this card. Advisories (never exit-affecting): pre-existing
  `owner-action-fields` on control/status.md + 10 pre-existing
  `model-line-shape` on July-14 proposal cards — untouched, not this lane's.
- Tree markers: `bootstrap.py:98 KIT_VERSION = "1.16.0"`,
  `substrate.config.json:60`, `.substrate/state.json` kit_version 1.16.0.

## Lane-owed (noted, deliberately untouched per Q-0261.3)

- Heartbeat `kit:` line bump in `control/status.md` (chronic class).
- Diverged-doc template deltas preserved in `.substrate/upgrade-report.md`:
  `docs/CAPABILITIES.md` (fleet master-copy path fix),
  `control/claims/README.md` (the new `bootstrap claim` verb doctrine —
  control/** is out of distribution scope), and the remainder of the
  `docs/AGENT_ORIENTATION.md` delta beyond the applied reading-path hunk.

Enabler note (sanctioned, recorded up front): this repo's live auto-merge
enabler re-arms on every synchronize and merges on green after this flip —
enabler merge-on-green is the accepted landing path (#367 precedent); no
manual arm/label/merge from this session.

💡 Session idea: the v1.16.0 `reading-path.md` plant lands strict-red by
design on every adopter whose fleet slots are unanswered (orphan +
unrendered banner) — the kit's upgrade path could pre-answer
`fleet_dark_repos`/`fleet_siblings`/`fleet_status_command` from the fleet
manifest it already distributes (or plant the doc bannerless with a
follow-up ask), so a distribution wave doesn't have to make owner-flavored
interview calls to get its own gate green. Worth proposing upstream.

⟲ Previous-session review: the previous session (EAP close-out heartbeat
stamp, #421) left the tree clean and the claims dir empty, which made this
wave's collision check trivial — good. What it (and the #367 lane before
it) could have done better: the #367 card's guard recipe ("check open PRs
AND fresh main history before branching for an upgrade") is still only card
prose; this session benefited from doing it manually. System improvement:
that pre-branch duplicate-work check belongs in the kit's
upgrade-distribution skill checklist, not in per-repo card memory.

- **📊 Model:** fable-5 · high · kit payload (vendored engine + config/state
  + banks + applied docs + rendered plant + orientation wiring; workflows
  reverted byte-identical; no control/content changes)
