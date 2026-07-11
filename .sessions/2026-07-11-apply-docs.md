# Session — fleet slice: apply pending kit doc-template updates (upgrade --apply-docs)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~02:02Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

Consume the queued follow-up the heartbeat has carried since the v1.8.0 upgrade:
two planted docs (`docs/repo-navigation-map.md`, `docs/AGENT_ORIENTATION.md`) were
classified `template-improved` (consumer-untouched by hash match) across TWO skipped
apply passes (v1.7.0 → v1.7.1 → v1.8.0). Run the kit's documented catch-up path —
`python3 bootstrap.py upgrade --apply-docs` (post-hoc: loads the old templates from
the newest banked archive under `.substrate/backup/`, only ever writes
consumer-untouched kit-form docs, re-records hashes, idempotent) — and ship the
synced docs as one merged-on-green PR.

## What this session did

- **Branched `upgrade/apply-docs-v180`** from origin/main `5b8fca7` (the PR #55
  merge — re-fetched and verified HEAD unmoved at branch time). Prefix `upgrade/*`
  matches the auto-merge enabler's live branch_patterns, so this PR is expected to
  self-arm at open. Inbox verified EMPTY at `5b8fca7` at branch time.
- **No-claim decision (decide-and-flag):** `control/claims/` verified README-only at
  branch time — no competing claim. Scope is 2 kit-form docs + `.substrate/`
  bookkeeping: not a section, uncontested, and disjoint from the one sibling in
  flight (trading-strategy wake-resilience probe — different repo surface entirely).
  Same no-claim shape as the PR #50 root-contract and PR #55 kit/config precedents.
  Proceeded without a claim file; this paragraph is the flag.
- **Ran `python3 bootstrap.py upgrade --apply-docs`** (docs snapshotted to scratchpad
  first). Full output, verbatim:

  ```
  upgrade: applied: docs/repo-navigation-map.md (template@new, hash re-recorded)
  upgrade: applied: docs/AGENT_ORIENTATION.md (template@new, hash re-recorded)
  upgrade: report: .substrate/upgrade-report.md
  ```

- **Diff character (verified per file, not assumed):**
  - `docs/repo-navigation-map.md` — ONE line: the "## Documentation roots" body
    expanded from `docs` to `docs/ (kit contracts) + ideas/ (the product: per-lane
    idea sections) + control/ (coordination)`. Nothing else in the file moved.
  - `docs/AGENT_ORIENTATION.md` — ONE line: the same "Documentation root(s):"
    expansion under "## Where things live". The router's planted-doc list, task
    routing table, and every other section byte-unchanged.
  - **Host-content outcome: NOTHING host-authored was deleted.** Both docs were
    consumer-untouched (hash-verified by the classifier AND confirmed by eyeball on
    the diffs — single kit-owned line each, purely additive replacement; no section
    anchors, contract rules, or grooming-round edits live in these two files). No
    revert needed.
  - `.substrate/state.json` — exactly the 2 `planted_doc_hashes` entries re-recorded.
  - `.substrate/upgrade-report.md` — **honest delta:** the kit REGENERATED the report
    rather than purely appending the documented `## Applied (--apply-docs)` section.
    Classifications refreshed (control/claims/README.md + scripts/env-setup.sh no
    longer "missing"; a .claude/CLAUDE.md row appeared) and the old ⚠️ gate
    carve-out section was REPLACED by the Applied section. Nothing is lost — the
    carve-out it described was already resolved (the gate ships with the PR #18 step
    intact since the PR #55 verbatim-restore; PR #36 tripwire green on this tree)
    and the banked pre-regen gate files remain under `.substrate/backup/` — but the
    report is NOT the append-only ledger its "appends" description implies. See 💡.
- **Gate watch (the standing clobber class): NO fourth occurrence.**
  `git diff --stat HEAD -- .github/workflows/substrate-gate.yml` EMPTY;
  `.github/workflows/auto-merge-enabler.yml` and `substrate.config.json` also
  untouched — apply-docs' post-hoc path writes docs only, as documented.
- **Not touched:** no idea-tree changes, no proposal (outbox stays at 5, all
  pulled — bookkeeping slice, nothing earned an append), stash@{0} (pre-existing
  local mods, not this slice's) left untouched.

### Local pre-push runs (real output)

```
$ python3 scripts/preflight.py
preflight: PASS — check_sections (exit 0)
preflight: PASS — check_ideas (exit 0)
preflight: PASS — check_ideas --outbox (exit 0)
preflight: PASS — bootstrap check --strict --status-only (exit 0)
gate-wiring: OK — .github/workflows/substrate-gate.yml non-control lane runs scripts/preflight.py
preflight: PASS — gate-wiring self-check (exit 0)
preflight: OK — all 6 checks green

$ python3 bootstrap.py check --strict
check: all checks passed.
```

(Both re-run green after the heartbeat overwrite, immediately before push. This card
is written before push per the honest-stamps rule — no merge outcome is claimed here
for this slice's own PR.)

**📊 Model:** fable-5 · doc-sync payload (2 planted docs one line each,
state.json hash re-record, regenerated upgrade-report, card, heartbeat; no
idea-tree changes, no proposal)

## 💡 Session idea

**apply-docs report regeneration is lossy — the "append" contract isn't one.**
The kit's `--apply-docs` path is described (and heartbeat-tracked here) as
*appending* `## Applied (--apply-docs)` to `.substrate/upgrade-report.md`, but the
observed behavior is a full report REGENERATION: prior sections (this run: the ⚠️
gate carve-out section naming the banked pre-regen gate file) are dropped, and
classifications silently refresh. Harmless this time only because the carve-out was
already consumed — but a consumer who treats the report as an append-only ledger of
outstanding manual work loses warnings the moment they run the catch-up command.
Kit-seam candidate (cross-link shape, per the PR #29/#40 precedent →
`ideas/substrate-kit/README.md`): either preserve non-kit-owned/⚠️ sections across
regeneration, or write applied-records to a separate append-only ledger file and
leave the report immutable between upgrades.

## ⟲ Previous-session review

PR #55 (auto-merge enabler wired live + branch_patterns fixed; merge `5b8fca7`) —
its card honestly stopped at "arm result verified in the PR thread post-push" and
never recorded the outcome. **Recorded now, with evidence** (GitHub API read
2026-07-11T02:02Z): PR #55 `merged: true`, `merged_by: github-actions[bot]`,
created 2026-07-11T01:48:20Z → merged 2026-07-11T01:53:38Z. Merged FIVE MINUTES
after open by the Actions bot — exactly the enabler's arm path (`gh pr merge --auto
--squash` under the workflow's own token; a hand-merge would show the owner login as
merged_by). **The live-fire PASSED end-to-end:** the enabler armed on the very PR
that shipped it, and GitHub-native auto-merge executed the squash the moment
substrate-gate went green. Corollaries verified: the refuse-to-arm guard did NOT
refuse, so the owner-UI inertness preconditions its card flagged ("Allow auto-merge"
ON + a required substrate-gate context) are confirmed set — the ⚑ owner-action
contingency is dead; and `substrate.config.json` at this tree carries `upgrade/*`
among the 13 patterns, which THIS slice's branch relies on for its own arm. One
residue its card predicted correctly: the by-hand arming convention is now
structural — this slice ships with zero hand-arming planned.

## Handoff → next wake

Inbox first, as always (verified empty at `5b8fca7` at branch time). The planted-doc
set is now FULLY kit-current at v1.8.0 — the "two template versions deep" debt is
cleared; a future `upgrade --apply-docs` re-run is a no-op by hash. Still queued:
branch-prefix drift tripwire (PR #55 card 💡), grooming round 4 seeds (see
heartbeat ripest list — unchanged by this slice), and this card's 💡 (apply-docs
report-regeneration lossiness → kit seam). The trading-strategy wake-resilience
sibling may land mid-flight or after; its scope never touched these files.
