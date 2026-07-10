# Behind-stall auto-updater — close OWNER-ACTION 11's residual gap agent-side

> **State:** captured
> **Class:** product · **Target:** `menno420/substrate-kit`

## Problem

With "Require branches to be up to date" behaving as ON in the kit repo, a green,
armed-for-auto-merge PR stalls `behind` whenever a sibling merges first. Kit-lab has
partially closed this: the enabler's `synchronize` re-arm (its PR #111) means a
fix-*push* re-arms auto-merge — but a PR whose base moves AFTER its last push still
needs a manual `git merge origin/main` + push, an agent round-trip that burns a
2-hourly wake. The lane's own heartbeat files the remainder as owner work
(⚑ OWNER-ACTION 11: a repo-settings checkbox), and that checkbox has sat unclicked
in an eleven-item owner queue. Live evidence: PR #107 plus "later close branch
updates" sat `behind` with green checks until a manual branch update.

## Idea

The residual is closable with a **committed workflow file**, the same shape as the
existing `auto-merge-enabler.yml`: on `push` to `main`, enumerate open PRs that are
armed for auto-merge and `mergeable_state: behind`, and call the update-branch API
(`PUT /repos/{owner}/{repo}/pulls/{n}/update-branch`, plain `GITHUB_TOKEN`) on each.
The next gate run lands them with zero agent involvement. Guardrails: only touch
PRs with auto-merge armed (arming is the lane's explicit "branch is final" signal —
never refresh a branch someone is still building), and let merge-conflict responses
fall through loudly to the PR for a real reconcile. Ships first in the kit repo
where the stall is live-hit; graduates into the kit's staged CI examples as the
companion to the enabler, and OWNER-ACTION 11 demotes from "blocked on click" to
"optional nicety".

## Grounding

- The residual gap, named by the lane itself: ⚑ OWNER-ACTION 11 ("a PR that goes
  behind AFTER its last push still needs a manual `git merge origin/main` + push;
  the enabler `synchronize` fix (#111) is a partial, not a full, close") + blocker
  note 2 ("Require branches up to date" behaves as ON; live-hit #107) @
  [`7e600c6`](https://raw.githubusercontent.com/menno420/substrate-kit/7e600c6f4b9e0e685d7d5a11aed37d435d009dae/control/status.md).
- The mechanism precedent: `auto-merge-enabler.yml` — a committed `GITHUB_TOKEN`
  workflow is the proven lane-side answer to a session-dependent wall (same file,
  blockers note 1); same shape as the option-(b) capture that worked for venture-lab
  (`ideas/venture-lab/self-landable-merge-path-2026-07-10.md`, this repo).

**Why now:** kit-lab now runs a 2-hourly standing wake with parallel claimed lanes
(manifest kit-lab row @
[`dc19b1e`](https://raw.githubusercontent.com/menno420/superbot/dc19b1e8a5443101a1a4cadf9a2f4e65133f49a3/docs/eap/fleet-manifest.md))
— every behind-stall now costs a real fraction of a wake cycle, and the owner
checkbox shows no sign of jumping an 11-deep queue.
