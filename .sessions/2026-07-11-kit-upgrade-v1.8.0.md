# Session — fleet slice: substrate-kit self-upgrade v1.7.1 → v1.8.0 + claims-dir reconcile

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~02:00Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

Consume the heartbeat's named ripest slice (the PR #52 card's 💡): move the vendored
kit v1.7.1 → v1.8.0 via the kit's own documented path, execute the PR #18/#35 standing
guard (re-apply the `wake preflight` step after the kit-owned gate regen), AND resolve
the one reconcile question the v1.7.1 upgrade never had — kit-planted `control/claims/`
vs this repo's hand-made root `claims/` (one convention, not two).

## What this session did

- Claimed the kit surface FIRST commit (`claims/upgrade-substrate-kit-v1.8.0.md` —
  taken in the then-live root home; migrated to `control/claims/` by this same slice's
  reconcile; cleared at close-out).
- **Fetched the v1.8.0 dist via the raw path** (the PR #35 wall unchanged:
  `releases/download/` 403s from this seat; `release.json` raw-404s at the tag —
  asset-only). `substrate-kit@v1.8.0:dist/bootstrap.py` → `bootstrap.py.new`, header
  v1.8.0, self-reported `--version` 1.8.0, sha256
  `28c5dcb64b713dde8d64a513a9a1aa860b4a07bf17d832686f0009932dc89b9b` —
  **byte-identical to websites' vendored copy @ `8abfe0a`** (its PR #85 verified that
  copy against the release asset's sha256, so the skip-noted self-verification step
  has independent cross-repo provenance this time).
- **Ran the documented flow:** `python3 bootstrap.py.new upgrade`. Result:
  archived-first (`bootstrap-1.7.1.py` banked — exactly one, no spurious backup;
  the new #156 hash-verified collision-banking had nothing to dedup), 21 planted docs
  classified (15 unchanged · 1 consumer-edited kept (`control/status.md`) ·
  1 **diverged** (`control/README.md` — both template and doc moved, manual merge; done
  this slice, see below) · 2 template-improved NOT applied (`repo-navigation-map`,
  `AGENT_ORIENTATION` — `--apply-docs` still a future slice, now two versions' worth) ·
  2 **missing → planted**: `control/claims/README.md` + `scripts/env-setup.sh`),
  staged `.substrate/` artifacts regenerated **plus one NEW staged artifact**
  `.substrate/ci/auto-merge-enabler.yml` (staged ONLY — installed live only by
  `adopt --wire-enforcement`; not wired this slice), `kit_version` 1.8.0 recorded in
  `substrate.config.json` + `.substrate/state.json`, and two NEW config keys written:
  `automerge` (`branch_patterns: ["claude/*"]`, `required_context: substrate-gate`)
  and `claims_dir: control/claims`. Report at `.substrate/upgrade-report.md` — which
  now carries the #156 explicit `## Carve-out scan` section (2 lines reported, never
  silent). Inputs self-cleaned.
- **The predicted clobber happened again, detected again:** the gate regen dropped the
  PR #18 `wake preflight` step; carve-out protection named it and banked the full
  pre-regen gate at `.substrate/backup/substrate-gate.pre-regen-048ca4a2.yml`.
  **RE-APPLIED verbatim per the PR #18 recipe** (between `setup-python` and the
  session-card gate step, anchors intact). Post-re-apply diff vs the pre-upgrade gate:
  the ONLY delta is v1.8.0's **mid-PR gate hold-tightening fix** (venture-lab #14 —
  a PR that ADDS a card AND touches the gate file routes the added card through the
  FULL locked door; this very PR live-fires that shape, which is why this card is
  flipped `complete` before push, not merely born-red). Workflow name
  `substrate-gate` + job id `substrate-gate` byte-unchanged (the owner's
  required-check context — renamed nothing). In-gate re-apply kept deliberately
  (NOT the kit's separate-workflow guidance): a separate workflow is a separate check
  context outside the required set — unchanged reasoning from the PR #35 card.
- **Claims reconcile — `control/claims/` WON; root `claims/` removed.** Decision
  basis (kit's own v1.8.0 text, not preference): the changelog frames root `claims/`
  as a **legacy home in a migration/compat window** with a `claims-legacy-location`
  nudge ("move them here, or pin your deliberate location via `claims_dir`"), and —
  decisive — `ADOPT_PLAN` plants `control/claims/README.md` at a **fixed path**
  (dist line 9119) with upgrades replanting it when missing, so pinning
  `claims_dir: claims` would still leave TWO claims directories after every future
  upgrade (or a per-upgrade delete chore). One convention, not two: root `claims/`
  deleted (`git rm claims/README.md`), the live claim file `git mv`'d across,
  repo-specific rules (section claims · flatten `/`→`-` filename rule ·
  pre-resolved-at-seed note) migrated into a HOST-OWNED trailing section of the
  planted `control/claims/README.md`, and `README.md` § Sections re-pointed.
- **`control/README.md` diverged-doc manual merge** (the upgrade report's named
  manual-merge item, done from its own template delta): added the new
  `## Claiming work (not an ORDER)` section + the three `Grammar source of truth`
  pointer lines (status/⚑/ORDER formats → the kit's `src/engine/grammar.py`, EAP
  §6.8) while keeping every consumer edit (the `anchor:` paragraph, the dirty-PR CI
  bullet, the claiming-an-order section).
- **Interview-slot churn: NONE** — `bootstrap ask`: "no pending questions — all slots
  filled" (shell plants are slot-free by design; the two template-improved docs are
  classified, not pending).
- **What v1.8.0 is** (CHANGELOG.md @ v1.8.0, raw): CAPABILITY MINOR shipping the EAP
  program-review §6 kit-owned band — the unified work-claim convention +
  `check_claims` claims-directory scan (#144, all advisory), the planted
  `scripts/env-setup.sh` setup-script contract + `check_setup_script` (#147,
  advisory), the kit-owned control-plane grammar module `engine/grammar.py` with
  writer↔enforcer agreement tests (#150, no behavior change), the kit-planted
  auto-merge enabler workflow + repo-settings checklist (#153, staged-only here),
  and the four #156 fixes (explicit-when-clean carve-out reporting ·
  hash-verified backup collision-banking · mid-PR gate hold-tightening ·
  code-span-aware unrendered-slot scan + control-fast-lane scan close). Release
  marker: `breaking=false state_migration=false min_upgrade_from=1.0.0`.

### Local pre-push runs (real output)

```
$ python3 bootstrap.py check --strict
check: all checks passed.

$ python3 scripts/preflight.py
preflight: PASS — check_sections (exit 0)
preflight: PASS — check_ideas (exit 0)
preflight: PASS — check_ideas --outbox (exit 0)
preflight: PASS — bootstrap check --strict --status-only (exit 0)
gate-wiring: OK — .github/workflows/substrate-gate.yml non-control lane runs scripts/preflight.py
preflight: PASS — gate-wiring self-check (exit 0)
preflight: PASS — open-work advisory (report-only, never gates) (exit 0)
preflight: OK — all 6 checks green
```

(The PR #36 tripwire is the proof the re-apply landed: `gate-wiring: OK` on the
regenerated file. Both runs re-executed green after the heartbeat overwrite,
immediately before push.)

**📊 Model:** fable-5 · high · kit payload (vendored dist + config/state + staged
artifacts + gate regen/re-apply + claims-dir migration + two planted docs + one
diverged-doc manual merge; no idea-tree changes, no proposal — backpressure)

## 💡 Session idea

**The auto-merge enabler is staged and one flag from live — decide, don't drift.**
v1.8.0 banked `.substrate/ci/auto-merge-enabler.yml` (the Q-0123 arm-at-open pattern,
`claude/*` branches, required-context refuse-to-arm guard) but it only goes live via
`adopt --wire-enforcement` + the owner's repo-settings checklist ("Allow auto-merge"
ON). This repo's landing convention already arms auto-merge by hand per PR — the
enabler would make that structural, but its default `branch_patterns: ["claude/*"]`
matches ZERO of this repo's branch names (`upgrade/*`, `probe/*`, `groom/*`…), so
wiring it as-is would be a silent no-op: the slice is (1) set `automerge.branch_patterns`
to this repo's real prefixes, (2) `adopt --wire-enforcement`, (3) verify the
refuse-to-arm guard against the branch-protection rules API from this seat. Anchors:
`substrate.config.json::automerge`, `.substrate/ci/auto-merge-enabler.yml`,
`docs/operations/auto-merge-guards.md` (kit repo) § "The kit-planted enabler".

## ⟲ Previous-session review

PR #52 (review-queue row auto-check probe + websites re-pin rider; merge `7be9a1f`)
promised: new sibling entry + section-README index row + lane-backlog `## Re-pin`
section + substrate-kit Cross-links row + claim cleared — ALL verified on this tree
pre-upgrade: `ideas/websites/review-queue-row-auto-check-2026-07-11.md` exists,
`ideas/websites/README.md:24` carries the index row, `lane-backlog-2026-07-10.md`
has the Re-pin section (1 match), `ideas/substrate-kit/README.md:24` carries the
cross-link, and `claims/` held only README.md at branch time. Its card's 💡 sized
THIS slice exactly — including the claims-dir reconcile question and its "one
convention, not two" framing, both consumed as written. Two things it could not have
known that this slice adds to the record: (1) the kit answers its reconcile question
STRUCTURALLY — the fixed-path plant makes "keep root claims/" the strictly worse
branch (two dirs after every upgrade), so the decision was read off the dist, not
judged; (2) its observation that websites' delta was "kit-upgrade-only" gave this
slice free provenance — the same bytes it clone-diffed became the sha256
cross-check that stood in for the walled release.json. The PR #35 card's recipe held
end-to-end a second time (fetch-raw → upgrade → carve-out banked → re-apply →
tripwire green); its 💡 (make the re-apply checkable) was already BUILT as PR #36's
gate-wiring check, and this slice is the first upgrade to run UNDER that tripwire —
it fired green post-re-apply, exactly as designed.

## Handoff → next wake

Inbox first, as always (verified empty at origin/main `7be9a1f` at branch time).
Kit line now v1.8.0 — heartbeat `kit:` line updated this slice. NEW this upgrade:
work claims live in `control/claims/` (root `claims/` is GONE — the checker would
nudge any resurrection as legacy); `scripts/env-setup.sh` exists (kit-planted
archetype contract — put repo-specific provisioning in its host-owned section);
the auto-merge enabler is STAGED ONLY (see 💡 — branch_patterns must change before
wiring is meaningful). `upgrade --apply-docs` follow-up now covers two versions of
template improvements for the same 2 docs. The four grooming-round-4 seeds queued on
the heartbeat are unchanged; trading-strategy kit-oldest-pin probe may be in flight
as a sibling (expect a status.md reconcile).
