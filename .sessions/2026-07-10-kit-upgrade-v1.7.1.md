# Session — fleet slice: substrate-kit self-upgrade v1.7.0 → v1.7.1 (gate preflight re-applied)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 ~22:30Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

Consume the heartbeat's standing self-upgrade candidate (named a ripest next slice
since the PR #30 window): move the vendored kit from v1.7.0 to v1.7.1 via the kit's
own documented path, and execute the PR #18 card's standing guard — re-apply the
`wake preflight` step after the (now kit-owned) `substrate-gate.yml` regeneration.

## What this session did

- Claimed the kit surface (`claims/kit-upgrade-v1.7.1.md`; cleared in this close-out).
- **Fetched the v1.7.1 dist via the raw path** — GitHub release-asset downloads are
  walled from this seat (the `releases/download/` URL 403s "not enabled for this
  session", same class as the repo-walled MCP), but the kit COMMITS its dist:
  `substrate-kit@v1.7.1:dist/bootstrap.py` (raw 200) → saved as `bootstrap.py.new`,
  header `v1.7.1`, self-reported `--version` 1.7.1, sha256
  `2aa4feddf7de7e20b00f46866826985ca8fd11f40bc51ebe261bbdef3118486d`. `release.json`
  is a release-asset only (raw 404 at the tag) — the upgrade verb's self-verification
  step noted the skip, per its documented contract (upgrade docstring step 1).
- **Ran the documented flow:** `python3 bootstrap.py.new upgrade` (the
  `release.json.upgrade_steps` consumer flow quoted in the verb's own docstring).
  Result: archived-first (exactly ONE dist banked — `bootstrap-1.7.0.py`, already
  tracked from seed; the v1.7.1 spurious-backup fix verified live: no
  `bootstrap-1.7.1.py` appeared), 19 planted docs classified (15 unchanged ·
  2 template-improved: `docs/repo-navigation-map.md` + `docs/AGENT_ORIENTATION.md`,
  NOT applied — `--apply-docs` left for a future slice · 2 consumer-edited kept),
  staged `.substrate/` artifacts regenerated, `kit_version` recorded 1.7.1 in both
  `substrate.config.json` and `.substrate/state.json`, report at
  `.substrate/upgrade-report.md`, inputs self-cleaned.
- **The predicted clobber happened — and v1.7.1's carve-out protection caught it:**
  the kit-owned gate regen dropped the PR #18 `wake preflight` step, but detected it
  (`carve-out: … host-added step 'wake preflight …' in job 'substrate-gate'`), banked
  the full pre-regen gate at `.substrate/backup/substrate-gate.pre-regen-457b2c6d.yml`,
  and surfaced it in the upgrade report's ⚠️ section — never a silent drop (the
  changelog's superbot-games #16 lesson, verified live here).
- **RE-APPLIED the preflight step per the PR #18 recipe, verbatim:** inserted between
  `setup-python` and the session-card gate step, anchors intact
  (`scripts/preflight.py::CHECKS`, comment names the idea file). Post-re-apply diff vs
  the pre-upgrade gate: the ONLY delta is the new (additive) `inbox append-only gate`
  step — v1.7.1's `--inbox-base` wiring, which was LATENT on every adopter until this
  release. Workflow name `substrate-gate` + job id `substrate-gate` byte-unchanged
  (the owner's required-check context — renamed NOTHING). The kit's own guidance
  (move carve-outs to a separate workflow) was deliberately NOT followed: a separate
  workflow is a separate check context outside branch protection's required set, so
  the step would stop gating merges — the in-gate re-apply stays correct until the
  kit grows the native lane-local preflight seam (the PR #18/#19 graduation idea).
- **Interview-slot churn: NONE** — `bootstrap ask` post-upgrade: "no pending
  questions — all slots filled." No render needed (no UNRENDERED banners; the two
  template-improved docs are classified, not pending slots).
- **What v1.7.1 is** (CHANGELOG.md @ v1.7.1, fetched via raw): PATCH fix-and-hardening
  shipping the v1.7.0 distribution-wave findings (#137) — the spurious upgrade-backup
  fix, the `--inbox-base` gate wiring, gate-refresh carve-out protection — riding with
  the kit-owned `substrate-gate.yml` regeneration (#130), the kit-upgrade currency
  checker + generated `docs/adopters.md` (#133, `bootstrap currency`), the F-5
  Reading-A ruling record (#128), and the superbot-coordinator succession close-out.
  Release marker: `breaking=false state_migration=false min_upgrade_from=1.0.0`.

### Local pre-push runs (real output)

```
$ python3 bootstrap.py check --strict
check: all checks passed.

$ python3 scripts/preflight.py
check_sections: OK — 10 sections in sync with the manifest
preflight: PASS — check_sections (exit 0)
check_ideas: OK — 274 idea files conform to the README grammar
preflight: PASS — check_ideas (exit 0)
check_ideas: OK — outbox proposals and sim-ready ideas are consistent
preflight: PASS — check_ideas --outbox (exit 0)
check: control-status check passed (--status-only).
preflight: PASS — bootstrap check --strict --status-only (exit 0)
preflight: OK — all 4 checks green
```

`scripts/check_harvest.py` (report-only): DRIFT — superbot pin 655e0fe vs HEAD
41899e1, 1 new upstream doc (`games-theme-engine-website-first-2026-07-10.md`), exit 0
— sizes the next re-harvest slice, not this one's problem.

**📊 Model:** fable-5 · high · kit payload (vendored dist + config/state + staged
artifacts + gate regen/re-apply; no idea-tree changes, no proposal — backpressure)

## 💡 Session idea

**Preflight-step re-apply as a checkable invariant** — the standing guard is still
human-memory-shaped: nothing REDS if an upgrade ships without re-applying the step
(this slice caught it because the card said to look). One line in
`scripts/preflight.py` (or `check_ideas.py`'s home) could assert the live gate
contains `run: python3 scripts/preflight.py` in the non-control lane — self-healing
loop: the wrapper CI-checks its own CI wiring, red the moment a regen drops it.
Anchors: `scripts/preflight.py::CHECKS`, `.github/workflows/substrate-gate.yml`, the
banked pre-regen copies under `.substrate/backup/`. Complements (not replaces) the
kit-side graduation idea (`ideas/substrate-kit/host-checkers-one-gate-2026-07-10.md`).

## ⟲ Previous-session review

PR #33 (capability-pair probe; merge `cd7251e`) promised: combined battery on
`project-capability-self-awareness` → sim-ready + PROPOSAL 005 appended, sibling
`session-start-capability-self-probe` → parked(folded) via pointer disposition,
substrate-kit Cross-links entry, MANAGER note on the heartbeat, dirty-PR CI bullet in
`control/README.md` — ALL verified on this tree pre-upgrade: PROPOSAL 005 present in
the outbox (1 match), both state lines read exactly as promised, the Cross-links
entry exists, the `mergeable_state: dirty` bullet is `control/README.md:171`, and
`claims/` carried only README.md at branch time. Its heartbeat named this exact slice
("kit v1.7.0→v1.7.1 self-upgrade (re-apply the gate preflight step)") among the
ripest — consumed as written, zero re-derivation; the PR #18 recipe held verbatim
(anchors unmoved, step re-inserted at the named position). One upstream delta worth
the record: v1.7.1 made the clobber DETECTED (carve-out lines + banked pre-regen
copy), so the recipe's riskiest failure mode — a silent drop nobody notices — is now
structurally impossible; the re-apply itself is still manual (this card's 💡).

## Handoff → next wake

Inbox first, as always. Kit line now v1.7.1 — keep the heartbeat `kit:` line in sync
(done this slice). The two template-improved docs (`repo-navigation-map`,
`AGENT_ORIENTATION`) are a one-command follow-up (`upgrade --apply-docs`) if wanted.
check_harvest names the next re-harvest (superbot 655e0fe → 41899e1, 1 new doc);
websites lane-backlog harvest remains the ripest capture slice; the new inbox
append-only gate step live-fires on the next inbox-touching PR — nothing to babysit.
