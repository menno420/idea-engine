# substrate-kit upgrade report — v1.15.0 → v1.16.0

> Generated 2026-07-14 by `bootstrap.py upgrade`. Rollback: `python3 bootstrap.py upgrade --rollback`.

**Docs:** consumer-edited: 4 · diverged: 3 · template-improved: 4 · unchanged: 14

| planted doc | class | note |
|---|---|---|
| CONSTITUTION.md | template-improved | consumer-untouched + template improved — safe to apply with `upgrade --apply-docs` |
| docs/decisions.md | unchanged | template identical across versions |
| docs/architecture.md | unchanged | template identical across versions |
| docs/ownership.md | unchanged | template identical across versions |
| docs/runtime_contracts.md | unchanged | template identical across versions |
| docs/repo-navigation-map.md | unchanged | template identical across versions |
| docs/helper-policy.md | unchanged | template identical across versions |
| docs/collaboration-model.md | template-improved | consumer-untouched + template improved — safe to apply with `upgrade --apply-docs` |
| docs/ai-project-workflow.md | unchanged | template identical across versions |
| docs/owner-profile.md | unchanged | template identical across versions |
| docs/AGENT_ORIENTATION.md | diverged | both the template and the doc moved — manual merge |
| docs/current-state.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| docs/question-router.md | unchanged | template identical across versions |
| docs/CAPABILITIES.md | diverged | both the template and the doc moved — manual merge |
| docs/SKILLS.md | template-improved | consumer-untouched + template improved — safe to apply with `upgrade --apply-docs` |
| docs/ROUTINES.md | template-improved | consumer-untouched + template improved — safe to apply with `upgrade --apply-docs` |
| docs/reading-path.md | unchanged | template identical across versions |
| docs/ideas/README.md | unchanged | template identical across versions |
| .session-journal.md | unchanged | template identical across versions |
| control/README.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| control/inbox.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| control/status.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| control/claims/README.md | diverged | both the template and the doc moved — manual merge |
| scripts/env-setup.sh | unchanged | template identical across versions |
| .claude/CLAUDE.md | unchanged | template identical across versions |

## ⚠️ Gate carve-outs (host additions the kit-owned regen could not keep)

- carve-out: .github/workflows/substrate-gate.yml — host-added step 'wake preflight (gate↔ritual convergence — scripts/preflight.py is the ONE check list)' in job 'substrate-gate' [carried from the previous upgrade report]
- carve-out: full pre-regen gate banked at .substrate/backup/substrate-gate.pre-regen-0c855c92.yml — host additions were NOT carried into the regenerated kit-owned gate; move them into a separate workflow file (e.g. .github/workflows/host-ci.yml) and commit that before shipping this upgrade/adopt PR. [carried from the previous upgrade report]
- carve-out: .github/workflows/auto-merge-enabler.yml — host-added step 'Skip arming while the PR's own in-diff session card is in-progress' in job 'enable-auto-merge' [carried from the previous upgrade report]
- carve-out: full pre-regen enabler banked at .substrate/backup/auto-merge-enabler.pre-regen-e3275f45.yml — host additions were NOT carried into the regenerated kit-owned enabler; move them into a separate workflow file (e.g. .github/workflows/host-ci.yml) and commit that before shipping this upgrade/adopt PR. [carried from the previous upgrade report]

## Carve-out scan

- carve-out scan: .github/workflows/substrate-gate.yml — ran, 0 found
- carve-out scan: .github/workflows/auto-merge-enabler.yml — ran, 0 found
- carve-out scan: 4 carve-out line(s) reported above (see the ⚠️ section).

## Capability-ledger seed refresh

- capability-seed: docs/CAPABILITIES.md fence already current — nothing to refresh.

This upgrade ships the venue-scoped capability ledger (grounded-skills §4.2): entries carry a venue token (owner-live · autonomous-project · routine-fired · subagent · any) and the ledger's kit-owned seed block carries the posture decision rule. If this repo carries a local prose copy of the boot-triad/venue-posture rule (superbot Q-0270), that copy is now superseded by docs/CAPABILITIES.md's posture rule — collapse the local copy into a pointer.

## Seat-digest refresh

- seat-digest: docs/seat-digest.md already current — nothing to refresh.

## Applied (--apply-docs)

- applied: CONSTITUTION.md (template@new, hash re-recorded)
- applied: docs/collaboration-model.md (template@new, hash re-recorded)
- applied: docs/SKILLS.md (template@new, hash re-recorded)
- applied: docs/ROUTINES.md (template@new, hash re-recorded)

## Template deltas for diverged docs

### docs/AGENT_ORIENTATION.md

```diff
--- docs/AGENT_ORIENTATION.md (template@old, current slots)
+++ docs/AGENT_ORIENTATION.md (template@new, current slots)
@@ -42,8 +42,9 @@
 `docs/repo-navigation-map.md` · `docs/ai-project-workflow.md` ·
 `docs/owner-profile.md` · `docs/current-state.md` · `docs/decisions.md` ·
 `docs/question-router.md` · `docs/CAPABILITIES.md` · `docs/SKILLS.md` ·
-`docs/ROUTINES.md` · `docs/ideas/README.md` — plus the root
-`CONSTITUTION.md` (the working agreement) and `.session-journal.md`.
+`docs/ROUTINES.md` · `docs/reading-path.md` · `docs/ideas/README.md` —
+plus the root `CONSTITUTION.md` (the working agreement) and
+`.session-journal.md`.
 
 Recurring action? **`docs/SKILLS.md`** — the skill index — names every
 kit-shipped skill and when to reach for it; check it before improvising a
@@ -54,6 +55,11 @@
 probe-not-record, scheduler-health signatures, pacing — read it before
 touching the trigger registry.
 
+Reading or acting across sibling repos in a fleet? **`docs/reading-path.md`**
+— the standing read authorization, the one-command fleet orient, the
+sibling/truth-file map, tiered depth, truth rules — read it before burning
+turns re-discovering what you may read.
+
 ## Verifying any change
 
 See the working agreement (`.claude/CLAUDE.md`) and its verify guidance
```

### docs/CAPABILITIES.md

```diff
--- docs/CAPABILITIES.md (template@old, current slots)
+++ docs/CAPABILITIES.md (template@new, current slots)
@@ -5,7 +5,7 @@
 > Generated by substrate-kit. What agent sessions in THIS environment can and
 > cannot do — **verified findings, never assumptions**. Read at session start
 > (it is in the orientation reading order); append at session close. Fleet
-> master copy: `menno420/fleet-manager` → `docs/capabilities.md` — sync new
+> master copy: `menno420/fleet-manager` → `docs/CAPABILITIES.md` — sync new
 > fleet-wide findings there via the manager when cross-repo access allows.
 
 ## Why this file exists
```

### control/claims/README.md

```diff
--- control/claims/README.md (template@old, current slots)
+++ control/claims/README.md (template@new, current slots)
@@ -37,12 +37,23 @@
    `check_claims` checker parses both; an unparseable claim is invisible to
    its duplicate scan.)
    Grammar source of truth: the bullet's regexes (backticked token + ISO date) are kit-owned constants in the kit's `src/engine/grammar.py` (EAP §6.8) — the SAME module `check_claims` consumes; agreement is pinned by the kit's `tests/test_grammar.py`.
+   **Don't hand-write it** — `bootstrap claim <slug> --scope "<scope>"
+   [--area "<files/area>"] [--order NNN]` renders the bullet from those same
+   constants (round-trip verified, current UTC date last; `--dry-run`
+   previews), so the claim can never be invisible to the duplicate scan.
+   **Serving an inbox ORDER? Pass `--order NNN`** — it renders the
+   structured ` · order NNN` segment the cross-branch overlap scan keys on,
+   and the verb REFUSES to write when another live claim on a different
+   branch already names that order (two branches building one ORDER is the
+   twin-execution waste this guard exists for; `--force` overrides for a
+   deliberate split of one order across branches).
 3. **Land the claim on main FAST** (claims are `control/**` traffic — they
    ride the CI control fast lane), then re-read this directory at HEAD before
    you build: if both lanes do this, the second claimer always sees the first.
-4. **Delete your own claim file at session close.** The durable record is the
-   PR and the living ledger — a claim is a whiteboard note, not an audit
-   trail.
+4. **Delete your own claim file at session close** — `bootstrap claim
+   <slug> --delete` (it refuses to touch a foreign claim). The durable
+   record is the PR and the living ledger — a claim is a whiteboard note,
+   not an audit trail.
 
 ## Arbitration + expiry
 
@@ -56,7 +67,10 @@
 
 `check` warns on: `claims-format` (no parseable bullet), `claims-stale`
 (older than the ~72h horizon), `claims-duplicate` (two files, one
-branch/scope token), and `claims-legacy-location` (claims living in a
+branch/scope token), `claims-order-collision` (two live claims on DIFFERENT
+branches naming the same `order NNN` / free-text `ORDER NNN` on the bullet
+— likely duplicate work; confirm one owner), and `claims-legacy-location`
+(claims living in a
 pre-unification home — `docs/owner/claims/` or root `claims/`; move them
 here, or pin your deliberate location via `substrate.config.json` →
 `claims_dir`).
```

