# Behind-stall auto-updater — close OWNER-ACTION 11's residual gap agent-side

> **State:** parked(routed — substrate-kit lane build, scope-sharpened by the GITHUB_TOKEN no-retrigger gotcha: updates pushed with plain `GITHUB_TOKEN` do not trigger workflow runs, so the naïve update-branch call the capture proposes trades a behind-stall for a checks-never-report stall — the routed build must pick an owner-provisioned PAT/App token or an explicit gate re-dispatch; ⚑ OWNER-ACTION 11's one checkbox stays the cleanest full close, this workflow is the agent-side fallback if it stays unclicked; verified un-adopted at live kit HEAD `be72c09` — see probe report)
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

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/be72c09ede329d01950ec764b409132a7eda007c/.github/workflows/auto-merge-enabler.yml@be72c09 · fetched 2026-07-11T08:14Z
> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/be72c09ede329d01950ec764b409132a7eda007c/control/status.md@be72c09 · fetched 2026-07-11T08:14Z
> *(pin annotation: kit live HEAD via `git ls-remote` 2026-07-11T08:13:45Z = `be72c09`; the
> shared verify-first sweep — release/tag/`[Unreleased]` state, the `c970f0a..be72c09`
> one-claim-file delta, batch-shape rationale, and the manifest-tombstone grounding-drift
> line — lives in the sibling
> [`parallel-session-heartbeat-reconcile-2026-07-10.md`](parallel-session-heartbeat-reconcile-2026-07-10.md)
> report's pin annotation and verify-first paragraph; only the facts SPECIFIC to this head
> are restated below.)*

Single-pass battery v0 (no panel trigger: routing decision, docs-only diff). **Verify-first,
this head's specifics at `be72c09`:** the kit's workflow set is exactly
`auto-merge-enabler.yml` · `auto-merge-disarm.yml` · `ci.yml` · `release.yml`, with **NO
update-branch machinery anywhere** (zero `update-branch`/`updateBranch`/`update_branch`/
`merge-when-green` hits across the workflows AND the planted-enabler generator
`automerge_enabler_workflow()`, `src/engine/adopt.py@37bd7e2` — `AUTOMERGE_ENABLER_RELPATH`
at `adopt.py:910`, the generator at `:948`); the only merge action in the set is
`gh pr merge --auto --squash` (native auto-merge arming). ⚑ OWNER-ACTION 11 is **STILL
OPEN** on the kit's own heartbeat (`control/status.md@5d0f59b`, `updated:`
2026-07-11T07:05:00Z, `kit: v1.10.0 · check: green`; same bytes re-read at `be72c09`): the
full six-field entry asking the owner to enable "automatically update branches",
VERIFIED-NEEDED citing #107 plus the manual branch updates that pre-empted it on
#144/#147/#150/#153, and the enabler `synchronize` fix (#111) named "a partial, not a
full, close" in so many words. No later status overwrite exists → inferred still
unclicked. The enabler's own trigger comment (`auto-merge-enabler.yml@0b6413d`, verbatim
at HEAD): re-arm on `synchronize` "does NOT fully close it — a PR that goes behind AFTER
its last push still needs the owner repo setting 'automatically update branches' (⚑ see
docs/CAPABILITIES.md)"; and `docs/CAPABILITIES.md@a03865c` carries both the live-hit
(#107: 3 required checks SUCCESS, sat unmerged, `mergeable_state: "behind"`) and the ⚑
RESIDUAL line. **Not overtaken — the capture's gap is real and open. But its mechanism is
wrong as written; see Q4.**

**1. What is this really?** An agent-side fallback for a one-checkbox owner action: a
committed workflow (the enabler's sibling shape) that, on push to main, refreshes armed
green PRs sitting `mergeable_state: behind` — closing the residual the kit's own heartbeat
files as ⚑ OWNER-ACTION 11 and its enabler comment names as not-fully-closed. It is
option-(b)-shaped (a committed `GITHUB_TOKEN` workflow as the answer to a
session-dependent wall, the enabler's own precedent) aimed at the last unautomated leg of
the landing pipeline.

**2. What is the possibility space?** (i) The owner checkbox (⚑ 11) — one click, zero
code, closes the class at the platform layer: the cleanest FULL close, and the kit's own
entry says so. (ii) The status quo per-wake recipe (`docs/CAPABILITIES.md@a03865c`: check
`mergeable_state` FIRST; if behind, `git merge origin/main` + push) — works, but burns an
agent round-trip per stall; #144/#147/#150/#153 each paid it. (iii) The captured workflow:
on push to main, enumerate open armed PRs with `mergeable_state: behind`, call
`PUT /repos/{owner}/{repo}/pulls/{n}/update-branch` — but the capture's "plain
`GITHUB_TOKEN`" premise fails, see Q4; the honest variants are (iii-a) an
owner-provisioned PAT/App token or (iii-b) plain token + explicit re-dispatch of the gate
workflow on each updated head. (iv) Do nothing and eat the wake cost. The value peak is
(i); (iii-b) is the best agent-side shape if (i) stays unclicked.

**3. What is the most advanced capability reachable by the simplest implementation?**
~30 workflow lines riding machinery the kit already ships: the enabler's own
event/permissions/concurrency scaffold + one `gh api` enumeration + the update-branch
call + (per Q4) one `workflow run dispatch`/`actions_run_trigger` re-kick of the gate on
each refreshed head. Guardrails come free from the capture: only touch PRs with
auto-merge ARMED (arming is the lane's explicit "branch is final" signal), and let
merge-conflict responses fall through loudly to the PR. Every green-behind PR then lands
with zero agent involvement — the 2-hourly wake stops being the merge scheduler.

**4. What breaks it? (the probe's sharpest finding — the capture's mechanism is wrong as
written.)** Two platform behaviors stack (flagged as platform behavior, kit-evidence-
consistent, not measured here): (1) GitHub's native auto-merge never updates a behind
branch itself — that is the whole stall class (`docs/CAPABILITIES.md@a03865c`, live-hit
#107). (2) Pushes and branch updates made with a workflow's own `GITHUB_TOKEN` do NOT
trigger new workflow runs — GitHub's recursive-workflow guard. So
`PUT /pulls/{n}/update-branch` called with plain `GITHUB_TOKEN` (exactly what the capture
proposes) creates the update commit, but CI never runs on the new head → the required
check never reports → the armed PR now sits in a **checks-never-report stall, strictly
worse because it looks like in-flight CI** (same failure family as this repo's
control/README "zero check runs" notes). The routed build must therefore pick: an
owner-provisioned PAT or App token (which reintroduces an owner action and weakens the
idea's own zero-owner premise) or an explicit re-dispatch of the gate workflow after each
update (plain token, `actions: write`, `workflow_dispatch` on the gate). Secondary risks:
update loops under sibling-merge trains (bounded by the armed-only guard + concurrency
group), and merge conflicts on update (deliberately loud, per the capture's guardrail).

**5. What does it unlock?** Green-behind PRs land unattended — each one currently costs a
wake round-trip on the kit's 2-hourly cadence (four evidenced manual updates in the #144–
#153 band alone); ⚑ OWNER-ACTION 11 demotes from "blocked on click" to "optional nicety";
and the kit's staged CI examples gain the enabler's missing sibling, so every adopter
inherits the full self-landing loop instead of re-deriving the recipe per repo.

**6. What does it depend on?** The kit lane (the workflow set, the enabler generator, and
the staged CI examples are kit-owned); the Q4 fork being decided in the build (PAT/App
token vs gate re-dispatch — the design's one real decision); ⚑ OWNER-ACTION 11's fate
(one click retires this head — the workflow is explicitly the fallback); the armed-only
guard semantics the enabler already establishes. Nothing sim-shaped — a workflow is
proven by its own live firing.

**7. Which lane should build it?** substrate-kit: the stall is live-hit in the kit repo
(#107, #144/#147/#150/#153), the enabler whose sibling this is ships from
`src/engine/adopt.py`, and the fix must compose with the kit's own required-check
topology. Joins the standing kit-lane fan-in bundle (carveout-needles-config +
enabler-card-status-guard-upstream(sharpened) + kit-line-self-drift +
parallel-session-heartbeat-reconcile + this head) — one manager ORDER could carry all
five, same config/template/check seam family. Not idea-engine (this repo writes only
itself); routing = this section README's index + the heartbeat notes for the manager's
:30 sweep.

**8. What is the smallest shippable slice?** One kit PR: the updater workflow in the
Q4-honest shape (armed-only enumeration + update-branch + explicit gate re-dispatch per
updated head, conflicts loud) + a header comment naming the no-retrigger gotcha so no
adopter re-ships the naïve variant + a CHANGELOG entry; ⚑ OWNER-ACTION 11 stays open as
the cleanest full close, with the workflow's own docs saying "click it and delete me".
Red/green reference: the next sibling-merge train in the kit repo — a green-behind PR
landing with zero agent involvement is the live green.

**Recommendation: park** — routed (kit lane build, scope-sharpened: the workflow must
solve the GITHUB_TOKEN no-retrigger gotcha — updates pushed with plain `GITHUB_TOKEN` do
not trigger workflow runs, so a naïve update-branch call trades a behind-stall for a
checks-never-report stall; ⚑ OWNER-ACTION 11's one checkbox remains the cleanest full
close, this workflow is the agent-side fallback if it stays unclicked) — verified
un-adopted at live kit HEAD `be72c09` (no update-branch machinery in any workflow or the
enabler generator; ⚑ 11 still open @`5d0f59b`; no v1.11.0, `[Unreleased]` empty), and no
simulator question exists — a workflow is proven by its own red/green (the #114
precedent, reaffirmed by #132).
