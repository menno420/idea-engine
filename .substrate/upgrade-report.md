# substrate-kit upgrade report — v1.17.0 → v1.20.1

> Generated 2026-07-20 by `bootstrap.py upgrade`. Rollback: `python3 bootstrap.py upgrade --rollback`.

**Docs:** consumer-edited: 4 · diverged: 3 · template-improved: 3 · unchanged: 15

| planted doc | class | note |
|---|---|---|
| CONSTITUTION.md | template-improved | consumer-untouched + template improved — safe to apply with `upgrade --apply-docs` |
| docs/decisions.md | unchanged | template identical across versions |
| docs/architecture.md | unchanged | template identical across versions |
| docs/ownership.md | unchanged | template identical across versions |
| docs/runtime_contracts.md | unchanged | template identical across versions |
| docs/repo-navigation-map.md | unchanged | template identical across versions |
| docs/helper-policy.md | unchanged | template identical across versions |
| docs/collaboration-model.md | unchanged | template identical across versions |
| docs/ai-project-workflow.md | unchanged | template identical across versions |
| docs/owner-profile.md | unchanged | template identical across versions |
| docs/AGENT_ORIENTATION.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| docs/current-state.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| docs/question-router.md | unchanged | template identical across versions |
| docs/CAPABILITIES.md | diverged | both the template and the doc moved — manual merge |
| docs/SKILLS.md | template-improved | consumer-untouched + template improved — safe to apply with `upgrade --apply-docs` |
| docs/ROUTINES.md | unchanged | template identical across versions |
| docs/reading-path.md | unchanged | template identical across versions |
| docs/ideas/README.md | template-improved | consumer-untouched + template improved — safe to apply with `upgrade --apply-docs` |
| .session-journal.md | unchanged | template identical across versions |
| control/README.md | diverged | both the template and the doc moved — manual merge |
| control/inbox.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| control/status.md | diverged | both the template and the doc moved — manual merge |
| control/claims/README.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| scripts/env-setup.sh | unchanged | template identical across versions |
| .claude/CLAUDE.md | unchanged | template identical across versions |

## ⚠️ Gate carve-outs (host additions the kit-owned regen could not keep)

- carve-out: .github/workflows/substrate-gate.yml — host-added step 'wake preflight (gate↔ritual convergence — scripts/preflight.py is the ONE check list)' in job 'substrate-gate'
- carve-out: full pre-regen gate banked at .substrate/backup/substrate-gate.pre-regen-0c855c92.yml — host additions were NOT carried into the regenerated kit-owned gate; move them into a separate workflow file (e.g. .github/workflows/host-ci.yml) and commit that before shipping this upgrade/adopt PR.
- carve-out: .github/workflows/auto-merge-enabler.yml — host-added step 'Skip arming while the PR's own in-diff session card is in-progress' in job 'enable-auto-merge'
- carve-out: full pre-regen enabler banked at .substrate/backup/auto-merge-enabler.pre-regen-e3275f45.yml — host additions were NOT carried into the regenerated kit-owned enabler; move them into a separate workflow file (e.g. .github/workflows/host-ci.yml) and commit that before shipping this upgrade/adopt PR.

## Carve-out scan

- carve-out scan: 4 carve-out line(s) reported above (see the ⚠️ section).

## Capability-ledger seed refresh

- capability-seed: NOT refreshed — the fenced seed block in docs/CAPABILITIES.md differs from the kit-form fence (edited inside the fence, or the old templates are unavailable). The fence is kit-owned: move your own findings BELOW the fence into the append log, restore the block between the BEGIN/END markers to kit form (copy it from the new template render), and the next upgrade refreshes it automatically.

This upgrade ships the venue-scoped capability ledger (grounded-skills §4.2): entries carry a venue token (owner-live · autonomous-project · routine-fired · subagent · any) and the ledger's kit-owned seed block carries the posture decision rule. If this repo carries a local prose copy of the boot-triad/venue-posture rule (superbot Q-0270), that copy is now superseded by docs/CAPABILITIES.md's posture rule — collapse the local copy into a pointer.

## Seat-digest refresh

- seat-digest: regenerated docs/seat-digest.md (derived render — skills index + venue-filtered walls re-rendered from the current tree; venue filter preserved from the committed doc).

## Applied (--apply-docs)

- applied: CONSTITUTION.md (template@new, hash re-recorded)
- applied: docs/SKILLS.md (template@new, hash re-recorded)
- applied: docs/ideas/README.md (template@new, hash re-recorded)

## Template deltas for diverged docs

### docs/CAPABILITIES.md

```diff
--- docs/CAPABILITIES.md (template@old, current slots)
+++ docs/CAPABILITIES.md (template@new, current slots)
@@ -84,12 +84,16 @@
   console — queue them as structured owner asks, never wait silently.
   Routine/schedule creation is NO LONGER a blanket wall: `create_trigger`
   arms routines agent-side (proven 2026-07-11); the console-only knobs
-  (model class, branch-push, auto-fix PRs) remain owner-only.
-  — LAST-VERIFIED: 2026-07-11
-- `subagent` · **Self-merge classifier**: sessions can be refused merging
-  owner-gated PRs while their other capabilities work — and the boundary
-  differs by venue (a child session was refused where a coordinator was
-  not). Record which venue hit which boundary. — LAST-VERIFIED: 2026-07-10
+  (model class, plan/seat settings) remain owner-only. **Branch creation
+  and commit-pushes work agent-side** — only ref *deletion* is walled (see
+  Branch deletion above). — LAST-VERIFIED: 2026-07-18
+- **Merging works agent-side — NOT a wall.** Agents flip drafts to ready,
+  arm auto-merge, and merge their own or a sibling's PR (MCP/REST) once CI
+  is green — verified 2026-07-18 by a direct MCP merge. There is **no
+  standing self-merge/owner-gated-merge wall**; do not record one. If a
+  *specific* merge/arm call is refused, that refusal is specific to that
+  call, venue, and the session's permission mode — note it as a dated,
+  verbatim one-off, never generalize it into doctrine. — LAST-VERIFIED: 2026-07-18
 - `any` · **GraphQL API quota**: tight — batch queries and prefer the
   REST-backed MCP tools for bulk reads. — LAST-VERIFIED: 2026-07-10
 - `routine-fired` · **Silent prompt-stalls**: a permission prompt in an
```

### control/README.md

```diff
--- control/README.md (template@old, current slots)
+++ control/README.md (template@new, current slots)
@@ -41,6 +41,42 @@
   `bootstrap adopt --lane <name>`: it plants `control/status-<name>.md` (skip-if-exists),
   declares it in `heartbeat_files`, and leaves `inbox.md`/`README.md` single — a second lane
   never re-plants the first Project's files (the double-adoption fix).
+
+## Delegated tally — coordinator-written heartbeats (multi-repo seats)
+
+A coordinator seat that spans several repos may legitimately write the authoritative
+tally in ITS status file, leaving the member repos' own heartbeats stale **by design**
+(live precedent: the 2026-07-12→13 night run — the mineverse coordinator wrote the whole
+SuperBot World tally while the member seats' heartbeats sat hours stale, and a
+staleness-only sweep would have misclassified shipping seats as stalled). Two conventions
+keep the delegation legible instead of looking like a dead lane:
+
+1. **The delegated write is MARKED.** A coordinator overwriting a member repo's status
+   (or carrying its tally) states so on the heartbeat it writes, first line after
+   `updated:`:
+
+   ```markdown
+   COORDINATOR-DELEGATED heartbeat write — the coordinator seat authorized this status
+   overwrite; authoritative tally for this repo lives here.
+   ```
+
+   One-writer-per-file is preserved as *one writer at a time*: the delegation line names
+   the current writer, so a sweep never sees two silent writers.
+
+2. **The member repo POINTS to its live tally.** A seat whose tally is delegated keeps
+   its own `status.md` from going silently stale by carrying a standing pointer in
+   `notes:` (or directly under `updated:`):
+
+   ```markdown
+   notes: tally DELEGATED to the coordinator seat — live status lives in
+   <coordinator-repo> control/status.md; this heartbeat updates only on this seat's own
+   sessions.
+   ```
+
+**Sweep rule (for managers and roll-up readers):** classify a seat by its **PR record +
+the coordinator's status file**, never by seat-heartbeat staleness alone. A stale member
+heartbeat carrying the delegation pointer is a healthy delegated lane; a stale heartbeat
+with no pointer and no PR activity is the actual dark-lane signal.
 
 ## Per-session ritual (every session, and every routine wake)
 
```

### control/status.md

```diff
--- control/status.md (template@old, current slots)
+++ control/status.md (template@new, current slots)
@@ -17,4 +17,6 @@
 does NOT parse and the fleet registry reads it as no `kit:` line at all (grammar + the valid
 bold-label-before-plain-token shape: `control/README.md` § "status.md format"). And this line is
 a self-report, not version truth — self-reports chronically lag; the kit repo's generated
-`docs/adopters.md` and your committed tree are the version truth to defer to.
+`docs/adopters.md` and your committed tree are the version truth to defer to. If this seat's
+tally is written by a coordinator seat elsewhere (multi-repo lanes), mark it — the delegated-write
+convention and the sweep rule live in `control/README.md` § "Delegated tally".
```

