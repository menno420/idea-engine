# 2026-08-13 — substrate-kit v1.20.1 → v1.21.0 (distribution wave, phase 3)

> **Status:** `complete` — branch `claude/substrate-kit-v1-21-0`, PR #899. This
> flip releases the born-red hold; the reviewed head is `320267e` and after it
> came only the one-line stub-path fix the round-2 dispositions name (`1dc11a5`)
> and this flip.

- **📊 Model:** fable-5 · high · mechanical refactor

## previous-session review

The previous card (2026-07-21 closeout) left the loop at rest; nothing it
recorded contradicted this session's tree (vendored v1.20.1, pin v1.20.1,
`kit: v1.20.1`). One thing it could not know: the required gate has been
structurally red since the roster froze with `shiftlife` listed active and no
matching section directory existed — measured on this PR's card-only head.

## Shipped

- Vendored dist v1.20.1 → v1.21.0 (sha256 `8807a00e…9cc7356` four ways), pin →
  1.21.0, `control/status.md` `kit:` line → v1.21.0.
- Rollback banked byte-identical: `.substrate/backup/bootstrap-1.20.1.py`.
- Carve-outs: gate regen KEPT with the host wake-preflight step re-applied in
  place (fm #833 precedent; this repo's preflight reds without it); enabler
  regen REVERTED byte-identical to main (dropped card guard — sbn #606
  lesson). Pre-regen copies banked.
- `ideas/shiftlife/` section created (partition vs the roster frozen at
  retirement); stub points at `control/claims/`.
- Two v1.21.0-new false-wall false positives on anti-wall text: one cured by
  rewording the CAPABILITIES aside ("phrasing note"), one allowlisted with
  reason (CONSTITUTION.md's own anti-wall instruction) — **accepted-scope
  exception**: `apply_allowlist` matches path+kind only, so the entry is
  file-wide; occurrence-level matching is the upstream gap, named on the kit
  worklist.

## Verify

- `python3 bootstrap.py check --strict` → exit 1 on exactly the designed hold;
  `scripts/preflight.py` → exit 0 (check_sections 14/14 in sync; gate-wiring
  OK after the splice, confirmed in the CI venue too).
- Codex: two rounds, 12 findings — 2 adopter-side conceded+fixed, 1 declined
  `[survived]` with grounds, 9 dist-routed to fleet-manager's followups
  worklist (rows 18–22 among them). Cap reached, opens named.

💡 The gate's new claims-only guard has a mixed-control hole (row 22) — but
this repo's pre-upgrade gate had no claims guard at all, which means every
adopter that never upgraded past v1.20.x has been running with zero card-less
fast-lane protection the whole time; the wave is the first time that gap
narrows.
