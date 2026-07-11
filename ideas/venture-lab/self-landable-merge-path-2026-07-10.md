# Self-landable merge path — commit the merge-on-green workflow the lane already specced

> **State:** parked(build-direct — lane wiring slice, owner-click-gated: the kit v1.9.0 enabler is already STAGED in the lane's own tree at `.substrate/ci/auto-merge-enabler.yml`; wiring = `adopt --wire-enforcement` + a `branch_patterns` fix, then two unverified owner toggles + one genuine-turn merge of the wiring PR)
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

## Probe report (v0, 2026-07-11)

Verify-first at live lane HEAD `9b504e8` (git ls-remote + raw fetches 2026-07-11T06:02–06:06Z; the lane moved past the capture's pin `ce22315`): the head is NOT overtaken — it MUTATED, and got cheaper. (a) Required checks: an owner statement dated 2026-07-11 says branch protection was updated (substrate-gate required + auto-merge; owner-statement event `a7bc924a`) but the lane's own ledger records "API verification NOT captured … required-check/auto-merge state on main remains unverified from an agent seat" (`docs/PLATFORM-LIMITS.md` @ `9b504e8`), and the same-day ORDER-004 arm denial explicitly cited "substrate-gate not required" — owner-claimed, agent-unverified. (b) Merge-on-green workflow: still NOT live — `.github/workflows/` carries only `substrate-gate.yml` (raw fetch 200); `auto-merge-enabler.yml`, `merge-on-green.yml`, `automerge.yml`, `auto-merge.yml`, `merge_on_green.yml` all 404 at `main` = `9b504e8`. BUT the kit v1.9.0 STAGED copy exists in the lane's own tree: `.substrate/ci/auto-merge-enabler.yml` @ `9b504e8` fetches 200, header verbatim "installed by `bootstrap.py adopt --wire-enforcement`" — the committed workflow the capture priced is one adopt command from live, not a hand-written file. `substrate.config.json` @ `9b504e8`: `kit_version` 1.9.0, `automerge.branch_patterns` still the kit default `["claude/*"]` (the exact wrong-default idea-engine fixed in its PR #55, squash `5b8fca7`), `required_context` `substrate-gate`. (c) Self-merge path: NONE from an agent seat, and the wall DEEPENED since capture — PLATFORM-LIMITS @ `9b504e8` records THREE terminal classifier denials on the lane's PR #15 (REST self-merge AND the auto-merge ARM from a child seat; "relayed authorization is never genuine in a child seat"); the proven working path is a coordinator-seat merge under the owner's genuine user turn (lane PRs #15/#16/#18 landed that way). Full battery below.

**1. What is this really?** A wiring slice, no longer a build: at capture time (PR #14) this was "commit a merge-on-green workflow file"; at `9b504e8` the lane already vendors kit v1.9.0, which STAGES the exact workflow (`.substrate/ci/auto-merge-enabler.yml`, planted by the kit's v1.8.0 automerge feature — substrate-kit CHANGELOG § [1.8.0] "Auto-merge enabler workflow planted by the kit", kit repo `main` @ `941be2e`). What remains is activation: `adopt --wire-enforcement` (or copying the staged file), one config line, and the repo-settings toggles the kit's own checklist names. The classifier wall the lane keeps hitting is an agent-SESSION wall; the enabler arms via `GITHUB_TOKEN` inside Actions — server-side, no agent session in the loop — which is precisely why the committed file dissolves the wall for every subsequent PR.

**2. What is the possibility space?** Minimal: copy staged → live, fix `branch_patterns` `["claude/*"]` → the lane's real prefixes, owner completes/verifies the two toggles, one genuine-turn merge of the wiring PR — every later green READY PR self-lands. Middle: adopt the idea-engine PR #86 card-status arm guard (squash `521aebf`) if the lane ever runs born-red session cards; verify the required-context count from inside the lane (the enabler's refuse-to-arm guard reads the rules API — a lane session can run the same query and close the "unverified from an agent seat" gap without owner help). Max: the kit template carries the #86 guard fleet-wide — already captured as `ideas/substrate-kit/enabler-card-status-guard-upstream-2026-07-11.md` (cross-link; that head covers the routed half, so THIS head need not).

**3. Most advanced capability by the simplest implementation?** Unattended self-landing of every future green PR — the lane's whole ORDER backlog lands without an owner click per PR — bought by ONE lane PR that mostly moves a file the kit already wrote. The refuse-to-arm guard means the same slice is safe under misconfiguration: with 0 required contexts it refuses rather than insta-merging (enabler header @ idea-engine `.github/workflows/auto-merge-enabler.yml`, same template).

**4. What breaks it?** (a) The owner toggles being absent after all: the guard counts required status CONTEXTS and refuses on zero — armed nothing, silent stall; and "Allow auto-merge" OFF makes the arm call fail (kit checklist names both; the trading-strategy adopter boundary in kit docs shows OFF is a real state). The owner's 2026-07-11 statement is UNVERIFIED — the wiring PR must verify, not assume (rules-API count from a lane session, or the enabler's own live log). (b) `branch_patterns` default `["claude/*"]`: if the lane's branches use other prefixes, the enabler never fires — survey merged branches first (idea-engine PR #55 found 13 real prefixes vs the same default; kit v1.9.0 validates `required_context` at plant time but NOT the patterns). (c) The bootstrap merge itself: the wiring PR cannot self-land (no enabler live yet) and a child seat must NOT attempt the merge or the arm (three verbatim denials @ `9b504e8`) — it lands via the proven coordinator+genuine-owner-turn path, the lane's documented working rule. (d) Kit-owned regeneration: hand edits to the live enabler are overwritten on upgrade — host customizations go in a separate workflow (the re-apply-debt class the substrate-kit capture prices).

**5. What does it unlock?** The lane's three pending ORDERs (002/003/004 at capture; every one lands by PR) stop paying a per-PR owner click; the systemic ⚑ shrinks from "pick and configure an option" to "verify two toggles once"; venture-lab joins idea-engine/websites in the self-landing gen-3 convention; and the lane's PLATFORM-LIMITS "agent-unlandable green PR" wall entry gets its closing annotation.

**6. What does it depend on?** Kit v1.9.0 staged enabler (present, verified 200 @ `9b504e8`); the owner's two repo-settings toggles ("Allow auto-merge" ON + a ruleset requiring `substrate-gate`) — claimed done 2026-07-11, UNVERIFIED, and the refuse-to-arm guard makes the required-check toggle a HARD dependency, not belt-and-braces; one genuine-owner-turn merge for the wiring PR itself (proven path, lane PRs #15/#16/#18); a branch-prefix survey of the lane's merged PRs for `branch_patterns`.

**7. Which lane should build it?** venture-lab, build-direct — the artifact is already in its tree and every remaining step is lane-local (`adopt --wire-enforcement`, config edit, PLATFORM-LIMITS annotation) plus owner toggles only the owner can click. NOT park(routed): the kit template work is DONE upstream (v1.8.0 planted the enabler, v1.9.0 added required-context validation — substrate-kit CHANGELOG @ `941be2e`); the one genuinely kit-shaped residue (the #86 card-guard upstream) is already captured at `ideas/substrate-kit/enabler-card-status-guard-upstream-2026-07-11.md` and needs no second head. Owner branch-protection click, stated explicitly for the fan-in: verify-or-complete on `menno420/venture-lab` — Settings → General → Pull Requests → "Allow auto-merge" = ON, and a default-branch ruleset REQUIRING the `substrate-gate` status check; the owner reported this done 2026-07-11 (event `a7bc924a`) but no agent seat has verified it, and the lane's wiring PR should verify from inside the lane before relying on it.

**8. What is the smallest shippable slice?** One venture-lab PR: run `python3 bootstrap.py adopt --wire-enforcement` (installs the staged enabler at `.github/workflows/auto-merge-enabler.yml`), set `substrate.config.json` → `automerge.branch_patterns` to the lane's observed merged-branch prefixes (survey first; drop the `claude/*` default if unused), and append the PLATFORM-LIMITS landing-path note ("enabler live as of this PR; arm is server-side, children still never merge/arm directly"). The PR lands via the coordinator+genuine-owner-turn path and verifies the required-context count live on its own head — if the count is zero, the PR's close-out re-raises the lane's existing ⚑ with the two toggles instead of declaring the path open.

**Recommendation: park** — build-direct (lane wiring slice, owner-click-gated): the workflow the capture wanted committed is already staged in the lane's own tree at `9b504e8`, so all that is left is a one-PR lane activation plus two unverified owner toggles and one genuine-turn bootstrap merge; nothing is evidence-shaped for sim-lab (the enabler pattern is live-proven on this repo — PRs #55/#86 — and the only unknown, the repo-settings state, is settled by a rules-API read, not a simulation).
