# Session — fleet slice: substrate-kit self-upgrade v1.8.0 → v1.9.0

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~06:50Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

Move the vendored kit v1.8.0 → v1.9.0 (released upstream TODAY — the exact slice the
PR #114 probe card's handoff named ripest: "this repo still runs v1.8.0 with all three
artifacts in sync — an upgrade slice is a natural next head"). Execute the standing
re-apply duty on BOTH kit-owned workflows: the PR #18 `wake preflight` gate step
(precedents #35/#54/#56 — clobbered on every regen, three for three) AND the enabler's
two host customizations (PR #86 card-status arm-race guard + the PR #62-lineage
`Head-ref:` squash provenance `--body` line), which no tripwire covers — manual diff
required.

## What this session did

- **Claimed FIRST** as fast-lane PR #117 (control-only, opened 06:44:08Z, auto-merged
  by github-actions[bot] 06:44:37Z — 29s, the enabler working as designed on a
  card-less `upgrade/*` claim). Claims dir re-read at HEAD `942b270` after the merge:
  only this claim live (the superbot-idle sibling's claim cleared with its #116 merge).
  Inbox re-read FIRST at branch time: ORDER 001 (model-attribution standing rule) is
  the only order, already `done=` — this card's `📊 Model:` line satisfies it for this
  wake too. Claim file deleted in this PR per convention.
- **Fetched the v1.9.0 dist via the raw tag path** (the PR #35 wall unchanged —
  `releases/download/` assets unreachable from this seat; `dist/bootstrap.py.sha256`
  raw-404s at the tag). `substrate-kit@v1.9.0:dist/bootstrap.py`: header v1.9.0,
  self-reported `--version` 1.9.0, 645448 bytes, sha256
  `55181082c796657c8e5e14750d248cea2df9e69a9aa896dd8a8c7f1adfb9cc90` —
  **byte-identical to BOTH websites' and gba-homebrew's vendored copies at their
  HEADs** (raw fetches this session; two independent adopters that upgraded in the
  v1.9.0 wave — cross-repo provenance in place of the walled release.json, the PR #54
  recipe).
- **Ran the documented flow:** `python3 bootstrap.py.new upgrade`. Result: 22 planted
  docs classified (17 unchanged · 4 consumer-edited kept (`control/*`,
  `control/claims/README.md`) · 1 **template-improved NOT applied**: `.claude/CLAUDE.md`
  — the v1.9.0 search-hygiene guidance note; deferred, see below), **2 NEW plants**:
  `.ignore` + `.gitattributes` (search-hygiene: vendored `bootstrap.py` +
  `.substrate/backup/` excluded from rg-family search and marked
  `linguist-generated` — merge-only append under a provenance marker, no host content
  existed to preserve), staged `.substrate/` artifacts regenerated (incl. the staged
  gate + enabler + `.substrate/claude/CLAUDE.md`), `kit_version` 1.9.0 recorded in
  `substrate.config.json` + `.substrate/state.json`, state schema v1 (no migration —
  release marker `breaking=false state_migration=false`). Report at
  `.substrate/upgrade-report.md` with the explicit `## Carve-out scan` section
  (4 lines reported). No `automerge.required_context` advisory fired (the new v1.9.0
  plant-time validation found `substrate-gate` among this repo's workflow contexts —
  silence is the pass). Interview churn: NONE (`bootstrap ask`: all slots filled).
- **The predicted clobber happened a FOURTH time, detected a fourth time — on BOTH
  workflows:**
  - `substrate-gate.yml`: regen dropped the PR #18 `wake preflight` step; carve-out
    banked the pre-regen gate at `.substrate/backup/substrate-gate.pre-regen-1ce5228e.yml`
    (hash-identical to the #56-era bank — the collision-banking dedup said "already
    banked" for the dist archive too). **RE-APPLIED verbatim** between `setup-python`
    and the session-card gate step, anchors intact. Post-re-apply diff vs HEAD: the
    ONLY delta is v1.9.0's **added-card grammar lint** (`--added-card "$card"` on the
    born-red advisory lane + its comment — the venture-lab #15 false-green class,
    adopted as-is: it only tightens). Workflow name AND job id `substrate-gate`
    byte-unchanged — the required-check context renamed nothing.
  - `auto-merge-enabler.yml`: regen dropped the PR #86 card-status guard step (named
    by the carve-out scan) AND the `Head-ref:` `--body` provenance customization
    (NOT named — it lives inside the arm step, invisible to the step-level scan;
    the manual-diff duty the #86 card's handoff prescribed is what caught it).
    Pre-regen bank at `.substrate/backup/auto-merge-enabler.pre-regen-78295b76.yml`.
    Since the v1.9.0 enabler template is otherwise UNCHANGED vs this repo's live file,
    restored via `git checkout HEAD -- .github/workflows/auto-merge-enabler.yml` —
    ships **byte-identical to HEAD, both customizations intact** (the #56 recipe;
    `git diff HEAD` on the file is empty).
- **Three version artifacts in sync at v1.9.0** (the exact drift class the PR #114
  probe verified live across 5 fleet repos — this upgrade is the moment the routed
  kit-side check would first pay off here):
  1. vendored dist header: `bootstrap.py` line 1 → `v1.9.0` (self-reported
     `--version`: 1.9.0)
  2. config pin: `substrate.config.json` → `"kit_version": "1.9.0"`
  3. heartbeat `kit:` line: `control/status.md` → `kit: v1.9.0 · check: green ·
     engaged: yes` (updated in this PR's final heartbeat commit — same session as the
     upgrade, per the control/README rule)
- **v1.9.0 features adopted vs deferred:**
  - ADOPTED (zero-risk, ships in this PR): SessionStart handoff push (engine-side,
    rides the vendored dist — no wiring needed); added-card grammar lint in the gate
    (regen, tighten-only); designed-hold signal on born-red reds (engine-side);
    plant-time `required_context` validation (ran clean this upgrade); `.ignore` +
    `.gitattributes` search-hygiene plants (append-only, host-content-preserving).
  - DEFERRED: `upgrade --apply-docs` for `.claude/CLAUDE.md` (the search-hygiene
    guidance note) — v1.9.0's `--apply-docs` has a KNOWN bug (fixed upstream in
    v1.10.0: the report rewrite drops the carve-out section — websites hand-restored
    theirs), and an `upgrade/apply-docs-v180` remote branch is already open (possible
    sibling in flight on the apply-docs surface); the model-attribution doctrine
    paragraph for `.sessions/README.md` — v1.9.0 only plants it into FRESH READMEs
    (`kept:` here), the retroactive append ships in v1.10.0's upgrade.
  - NOTE: **v1.10.0 released upstream the same day** (CHANGELOG @ kit main): the
    born-red card-only loophole gate fix (P1), the `--apply-docs` carve-out re-emit
    fix, the retroactive model-doctrine append, `check --simulate-added-card`, and the
    release runbook. This slice stays bounded at its assigned pin v1.9.0; the v1.10.0
    hop inherits all three deferred items above and is the natural next kit slice.

### Local pre-push runs (real output)

```
$ python3 bootstrap.py --version
substrate-kit 1.9.0

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
preflight: PASS — branch-prefix-drift advisory (report-only, never gates) (exit 0)
preflight: OK — all 7 checks green
```

(The `gate-wiring: OK` line is the PR #36 tripwire proving the wake-preflight
re-apply landed on the regenerated gate — fourth consecutive upgrade it has caught
the class. Both runs re-executed green after the heartbeat overwrite, immediately
before push.)

**📊 Model:** fable-5 · high · kit payload (vendored dist + config/state + staged
artifacts + gate regen/re-apply + enabler verbatim-restore + 2 search-hygiene plants;
no idea-tree changes, no proposal — kit surface only)

## 💡 Session idea

**Make the enabler re-apply checkable — the gate has a tripwire, the enabler has a
diff ritual.** The PR #36 gate-wiring check has now caught the wake-preflight drop
four upgrades running; the enabler's TWO customizations (card guard + Head-ref
provenance) rely on a human remembering to diff — and this upgrade proved the
carve-out scan only sees ADDED STEPS (it named the card guard but was blind to the
`--body`/env edit INSIDE the kit's own arm step). Lane-sized: extend
`scripts/preflight.py::check_gate_wiring` (or a sibling advisory) to assert the live
enabler contains both anchors — `steps.card.outputs.skip` in the arm-step `if` and
`Head-ref: $HEAD_REF` in the arm command — red when either vanishes. Kit-seam
cross-link: the upstream absorption of the card guard is already seeded
(`seed-enabler-card-guard-upstream` branch + `ideas/substrate-kit` head
`enabler-card-status-guard-upstream`); v1.10.0's gate-side `session-card-hold` fix
covers the RACE but not the PROVENANCE line, so the local tripwire stays worth
having even post-absorption.

## ⟲ Previous-session review

PR #114 (`probe/substrate-kit-kit-line-self-drift`, merge `5f4e201`) promised, and
this tree verifies: the idea file
`ideas/substrate-kit/kit-line-self-drift-local-check-2026-07-10.md` flipped
parked(routed — substrate-kit lane build) with the probe report appended ✓; the
section README index re-badged for that head only ✓; its claim cleared (claims dir
held only README.md at this slice's claim time) ✓; heartbeat ⚑ Lumen Drift block
preserved ✓. Its handoff named THIS slice ("an upgrade slice is a natural next
head") and its finding shaped this card's verification section: the three-artifact
sync it probed across the fleet is exactly what this upgrade must not break — shown
explicitly above, all three at v1.9.0 in the same PR. One delta its card could not
know: v1.10.0 landed upstream within hours carrying fixes for two of the classes
this slice hit live (`--apply-docs` carve-out drop, model-doctrine skip-if-exists) —
its "the exact moment the routed check would first pay off" framing now has a
second datapoint: the pace of upstream releases makes local artifact-sync checks
MORE valuable, not less. The PR #54 upgrade recipe held end-to-end a THIRD time
(fetch-raw → cross-repo sha256 → upgrade → carve-outs banked → re-apply →
tripwire green), and the #86 card's manual-diff duty for the enabler proved
load-bearing exactly as written.

## Handoff → next wake

Inbox first, as always. Kit line now v1.9.0 — all three artifacts in sync (dist
header · config pin · heartbeat `kit:` line). The re-apply duty is UNCHANGED for
future upgrades: gate wake-preflight step (tripwire-covered) + enabler card guard
AND Head-ref `--body` line (manual diff — the carve-out scan is step-blind to the
latter; see this card's 💡 for the checkable fix). NEW surfaces: `.ignore` +
`.gitattributes` (kit-planted, append-only — put host search-hygiene entries ABOVE
the provenance marker). Queued: the v1.10.0 hop (gate P1 fix + the three deferred
items — apply-docs CLAUDE.md note, .sessions/README doctrine append, simulate-added-card);
`upgrade/apply-docs-v180` remote branch may be a sibling in flight on the apply-docs
surface — check before touching it.
