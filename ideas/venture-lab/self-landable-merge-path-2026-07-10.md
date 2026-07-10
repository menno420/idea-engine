# Self-landable merge path — commit the merge-on-green workflow the lane already specced

> **State:** captured
> **Class:** process · **Target:** `menno420/venture-lab`

## Problem

The lane cannot land its own PRs unattended. Its last heartbeat records the wall
verbatim: the auto-mode classifier walled the agent self-merge of PR #9 TWICE, and
there is no automated fallback — auto-merge cannot arm because PRs reach
`mergeable_state: clean` instantly with **0 branch-protection required checks**
(`substrate-gate` is not a required context), and the only workflow is the
enforcement gate itself, with no merge-on-green step. The lane filed this as a
systemic ⚑ needs-owner with two options: (a) make substrate-gate a required check
(owner clicks in Settings → Rules), or (b) add a server-side merge-on-green Actions
workflow (`GITHUB_TOKEN`, modeled on substrate-kit's auto-merge-enabler). Meanwhile
ORDERs 002/003/004 all sit pending and every one of them lands by PR — the fresh
boot session pays this wall on its first close.

## Idea

Option (b) is not actually owner-work: a merge-on-green workflow is a **committed
file**, and the lane already commits workflow files (`substrate-gate.yml` is in the
tree). Capture: the lane's next boot session ships `.github/workflows/` merge-on-green
(land green, non-draft PRs via `GITHUB_TOKEN` once `substrate-gate` reports success),
shrinking the systemic ⚑ from "pick and configure an option" to at most ONE residual
bootstrap click — merging the workflow-adding PR itself. Every later PR lands
unattended. Option (a) remains the belt-and-braces follow-up, not the gate.

## Grounding

- Manifest venture-lab row: ORDERs 002/003/004 all pending; no wake routine; lane
  ENDER-MISSING until ORDER 004
  ([superbot @ `6f283b9`](https://raw.githubusercontent.com/menno420/superbot/6f283b91160546af2864a0fd30b6e2d81b148a8f/docs/eap/fleet-manifest.md), fetched 2026-07-10).
- Lane reality @ [`ce22315`](https://github.com/menno420/venture-lab/tree/ce223152719705e22a386b6fdc6d03508a0661c1):
  `control/status.md` § BLOCKER (both classifier denials verbatim; "auto-merge cannot
  arm … 0 required checks"; "venture-lab has NO server-side auto-lander workflow") and
  its systemic ⚑ naming option (b) + the substrate-kit model to copy.
- Q-0259 fit: repo-internal lane plumbing — takes nothing from the games completion
  wave or the rebuild pace.

**Why now:** three pending ORDERs (one P0) are queued for the fresh boot and each
lands by PR — every session before this ships is a session that ends one owner-click
short of done.
