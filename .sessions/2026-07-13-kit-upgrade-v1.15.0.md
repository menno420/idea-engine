# 2026-07-13 — kit upgrade v1.15.0 (distribution)

> **Status:** `complete`

Started as the full substrate-kit 1.10.0 → 1.15.0 distribution upgrade (ORDER 019
item 3 residual). Mid-session, parallel PR #366 landed the first upgrade command on
main; this session's PR #367 was repurposed to carry the missing second command of
the v1.13.0+ two-command flow — `upgrade --apply-docs`.

## What shipped (PR #367)

- Applied the 4 template-improved, consumer-untouched docs main still owed:
  `CONSTITUTION.md`, `docs/collaboration-model.md`, `docs/question-router.md`,
  `.claude/CLAUDE.md` (via `python3 bootstrap.py upgrade --apply-docs`, v1.15.0
  engine); `.substrate/state.json` hashes re-recorded; post-apply-docs
  `.substrate/upgrade-report.md` kept over #366's pre-docs-pass report.
- Kept from main unchanged: #366's upgrade (engine, regenerated gate incl. the
  re-applied wake-preflight host step — both sessions' regens byte-identical —
  SKILLS/ROUTINES/seat-digest plants, capability-seed fence, orientation wiring)
  and #366's `claude/*` enabler-allowlist addition.
- Distribution rails held: live `.github/workflows/auto-merge-enabler.yml`
  byte-identical to main (the engine's kit-owned regen of it was reverted);
  no `ideas/**` / `control/**` / `.claude` settings-or-hooks touches.

## Verify evidence

- Release assets sha256-verified before upgrade: bootstrap.py
  `25d22af9…c650e` (828,825 B), release.json `90f8ae75…da26` (449 B).
- `python3 bootstrap.py check --strict` on the merged tree: exit 0,
  `check: all checks passed.` (one pre-existing, never-exit-affecting
  `owner-action-fields` advisory on control/status.md).
- Tree markers: `bootstrap.py:93 KIT_VERSION = "1.15.0"`,
  `substrate.config.json:60`, `.substrate/state.json` kit_version 1.15.0.

## Guard recipe (deferred observation)

The duplicate-upgrade race (this PR vs #366) burned a lane: the claim (#365)
was on main before this session branched, but the claim named the SAME work
both sessions were dispatched for. Cheapest guard: before branching for an
upgrade, check open PRs AND fresh main history for the upgrade itself, not
just the claim's existence (`git log --oneline -5 origin/main` grep
"kit upgrade").

💡 Session idea: the upgrade engine could refuse to write "safe to apply with
`upgrade --apply-docs`" report rows without also printing a loud final-line
reminder (or the check gaining an advisory `apply-docs-owed` finding) — #366
skipped the second command silently; a strict-visible nudge would have made
the miss impossible to land green. Worth proposing upstream to the kit.

⟲ Previous-session review: the previous session (PR #366 lane) landed a clean
first-command upgrade — gate host step correctly re-applied, enabler correctly
left alone, orientation wired — but missed the mandatory `--apply-docs` second
command (v1.13.0+ doctrine), leaving 4 template-improved docs and their state
hashes stale on main. System improvement: the wave doctrine "two-command
upgrade is MANDATORY" lives only in agent memory + kit report prose; see the
💡 above for the enforcing version.

📊 Model: Claude Fable 5 (family-level)
