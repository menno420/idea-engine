# substrate-kit upgrade report — v1.8.0 → v1.9.0

> Generated 2026-07-11 by `bootstrap.py upgrade`. Rollback: `python3 bootstrap.py upgrade --rollback`.

**Docs:** consumer-edited: 4 · template-improved: 1 · unchanged: 17

| planted doc | class | note |
|---|---|---|
| CONSTITUTION.md | unchanged | template identical across versions |
| docs/decisions.md | unchanged | template identical across versions |
| docs/architecture.md | unchanged | template identical across versions |
| docs/ownership.md | unchanged | template identical across versions |
| docs/runtime_contracts.md | unchanged | template identical across versions |
| docs/repo-navigation-map.md | unchanged | template identical across versions |
| docs/helper-policy.md | unchanged | template identical across versions |
| docs/collaboration-model.md | unchanged | template identical across versions |
| docs/ai-project-workflow.md | unchanged | template identical across versions |
| docs/owner-profile.md | unchanged | template identical across versions |
| docs/AGENT_ORIENTATION.md | unchanged | template identical across versions |
| docs/current-state.md | unchanged | template identical across versions |
| docs/question-router.md | unchanged | template identical across versions |
| docs/CAPABILITIES.md | unchanged | template identical across versions |
| docs/ideas/README.md | unchanged | template identical across versions |
| .session-journal.md | unchanged | template identical across versions |
| control/README.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| control/inbox.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| control/status.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| control/claims/README.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| scripts/env-setup.sh | unchanged | template identical across versions |
| .claude/CLAUDE.md | template-improved | consumer-untouched + template improved — safe to apply with `upgrade --apply-docs` |

## ⚠️ Gate carve-outs (host additions the kit-owned regen could not keep)

- carve-out: .github/workflows/substrate-gate.yml — host-added step 'wake preflight (gate↔ritual convergence — scripts/preflight.py is the ONE check list)' in job 'substrate-gate'
- carve-out: full pre-regen gate banked at .substrate/backup/substrate-gate.pre-regen-1ce5228e.yml — host additions were NOT carried into the regenerated kit-owned gate; move them into a separate workflow file (e.g. .github/workflows/host-ci.yml) and commit that before shipping this upgrade/adopt PR.
- carve-out: .github/workflows/auto-merge-enabler.yml — host-added step 'Skip arming while the PR's own in-diff session card is in-progress' in job 'enable-auto-merge'
- carve-out: full pre-regen enabler banked at .substrate/backup/auto-merge-enabler.pre-regen-78295b76.yml — host additions were NOT carried into the regenerated kit-owned enabler; move them into a separate workflow file (e.g. .github/workflows/host-ci.yml) and commit that before shipping this upgrade/adopt PR.

## Carve-out scan

- carve-out scan: 4 carve-out line(s) reported above (see the ⚠️ section).
