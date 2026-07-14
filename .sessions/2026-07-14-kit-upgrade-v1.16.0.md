# 2026-07-14 — kit upgrade v1.16.0 (distribution)

> **Status:** `in-progress`

About to run the substrate-kit v1.15.0 → v1.16.0 distribution upgrade on this
repo: verify the release asset (sha256 three-way), run the mandatory
two-command flow (`python3 bootstrap.py.new upgrade` then
`python3 bootstrap.py upgrade --apply-docs`), verify
`bootstrap.py check --strict` green, and hold the Q-0261.3 rails — this
repo's host-customized `.github/workflows/auto-merge-enabler.yml` (wide
prefix allowlist) and `substrate-gate.yml` (wake-preflight carve-out step)
are restored byte-identical to origin/main if the regen touches them
(the #367 precedent). No `control/**`, `.claude/settings.json`, hooks, or
content-file touches. Heartbeat `kit:` line bump is lane-owed, noted not done.

Enabler note (recorded up front, sanctioned): this repo's live auto-merge
enabler arms on every synchronize push to an allowlisted-prefix PR and
merges on green after the card flip — the yield race is structurally
unwinnable (#367 precedent); enabler merge-on-green is the accepted landing
path for this PR.

📊 Model: Claude Fable 5 (family-level)
