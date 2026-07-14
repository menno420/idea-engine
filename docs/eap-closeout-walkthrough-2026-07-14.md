# Ideas Lab seat — EAP close-out walkthrough (2026-07-14)

> **Status:** `owner-guidance`
>
> The seat-level EAP close-out walkthrough ordered by inbox ORDER 012 item
> (b) / ORDER 013 STEP 2 (`control/inbox.md` @ `6d6735f`, both landed
> 2026-07-14). Covers BOTH repos of the Ideas Lab seat —
> [menno420/idea-engine](../README.md) (ideation) and
> [menno420/sim-lab](https://github.com/menno420/sim-lab) (verdicts). This
> doc is the OWNER's path through the seat: what shipped (§A), what works
> right now and how to verify it (§B), everything Menno must personally do
> (§C), a 5-minute tour (§D), and the handoff for the next phase (§E). For
> measured depth (walls, denials, friction, asks) read the companion audit,
> [docs/audits/eap-project-audit-2026-07-14.md](audits/eap-project-audit-2026-07-14.md)
> (PR #413 @ `8162d1e`) — this walkthrough links it, never restates it.
> sim-lab's own walkthrough is the parallel deliverable:
> [sim-lab docs/eap-closeout-walkthrough-2026-07-14.md](https://github.com/menno420/sim-lab/blob/main/docs/eap-closeout-walkthrough-2026-07-14.md).

Written 2026-07-14T12:45Z at idea-engine HEAD `6d6735f` (PR #419 merge) and
sim-lab HEAD `9aaf72b` (PR #140 merge); open-PR counts verified live via
GitHub MCP at 12:36Z (both repos: zero).

## A. What this seat did

**The seat and window.** Ideas Lab = one coordinator + dispatched workers
operating idea-engine (fleet ideation: `ideas/` for 13 lanes, `control/`
coordination bus, no product code) and sim-lab (reproduced-evidence verdicts).
Active window 2026-07-10 → 2026-07-14, ≈3.6 days. Measured scale (audit §1,
measurement snapshot 08:39–08:54Z): **288 session cards, 545 PRs opened**
across the pair; today's post-snapshot tail brought the pair to #420 (this
PR) and #140 respectively.

**The pipeline product — 63 proposals, 76 verdicts.** idea-engine drafted
PROPOSALs 001–063 (every one a probe-batteried, seed-registered,
closed-form-first sim question harvested from a live fleet repo, rotated
across lanes per standing ORDERs 003/004); sim-lab returned VERDICTs 001–076
(V074 = P063 at the standing +11 offset; V075/V076 served the
superbot-games SIM-REQUESTs simreq-010/011, not idea-engine proposals).
Final-day highlights, all merged today:

- **V074 on P063 — REJECT-REORDER** (sim-lab #140 @ `9aaf72b`): the D&D
  menu-width leverage inversion. Certified the width-2 mint partition is
  exactly {0, 1/2} — MONOTONE + POSITIVE-FLOOR are jointly unsatisfiable by
  ANY data-only reorder; the SHIPPED ordering's inversion certified 1/2→1/3
  (E[mints, T=20] −35.1%), matching the pre-registered prediction in the
  idea file. Idea: [ideas/superbot-games/menu-width-leverage-inversion-2026-07-14.md](../ideas/superbot-games/menu-width-leverage-inversion-2026-07-14.md)
  (PR #419 @ `6d6735f`).
- **V076 — APPROVE-WITH-CONSTANTS** (sim-lab #139 @ `d0a5a75`): fishing
  cook-leg constants P*=12 (cook energy minnow 1 / bass 1 / pike 2 /
  legend_carp 7), plus the bonus F-FLAT30 finding: the committed flat
  "cooked fish": 30 is perpetual motion — supersede before wiring.
- **V075 — NULL** (same PR): fishing full-roster band-straddle; the honest
  no-verdict, with the three-way reframing fork named for the next phase.

**Shipped systems (idea-engine).** The idea grammar + checker suite
(`scripts/check_ideas.py` — 8-question probe battery, exactly-one
recommendation, grounding/sequence line grammar, sim-verdict note pinning;
`scripts/check_sections.py` — lane partition vs the fleet manifest;
`scripts/preflight.py` — the one-command ritual, CI-converged into the
substrate gate); the append-only outbox proposal bus with the fm rollover
convention (ORDER 010, PRs #400/#401); claims discipline (claims/ ends the
EAP EMPTY — prunes #414 @ `6626767`, #415 @ `7dc095c`, and this PR's P063
claim deletion); the born-red session-card ceremony; the coordinator-only
heartbeat (`control/status.md`, last stamp 09:31:52Z via #416 @ `4661145`).

**Shipped systems (sim-lab).** The fixtures-before-runner verdict ceremony
(constants registered and committed before any run; byte-identical double
runs; named-anomaly discipline), the simharness second product, and the
INTAKE/VERDICT ledger in sim-lab `control/outbox.md` (through V076 via #137
@ `fa1ae2d`, #139 @ `d0a5a75`, #140 @ `9aaf72b`; ORDER 008 consumed via #138
@ `d4ff3c8`).

**Close-out trail (today).** Audit #413 @ `8162d1e` · prunes #414/#415 ·
heartbeat #416 @ `4661145` · ORDER 012 landing #417 @ `24195f8` · ORDER 013
landing #418 @ `8e171bd` · P063 #419 @ `6d6735f` · this walkthrough (#420).

## B. Current state — what works, how to verify

**Works right now.**

- Both repos are green at HEAD. Per repo:

  ```
  git clone https://github.com/menno420/idea-engine && cd idea-engine
  python3 bootstrap.py check --strict     # exit 0 = the whole kit gate
  python3 scripts/preflight.py            # the full wake ritual, one command
  ```

  (same two commands in a sim-lab clone; both exit 0 at the HEADs above).
- **Heartbeat:** open
  <https://github.com/menno420/idea-engine/blob/main/control/status.md> —
  one screen: `updated:` stamp, `phase:` (routine disposition + LOOP STATE +
  NEXT-2 baton), `orders:`, `⚑ needs-owner:`. This is the seat's single
  source of session truth.
- **Proposal bus:** `tail -60 control/outbox.md` in idea-engine (or
  <https://github.com/menno420/idea-engine/blob/main/control/outbox.md>) —
  newest blocks: PROPOSAL 063 and this slice's CLOSE-OUT 001 report.
- **Verdict ledger:** sim-lab
  <https://github.com/menno420/sim-lab/blob/main/control/outbox.md> —
  INTAKE/VERDICT blocks through V076; each verdict's evidence lives under
  `sims/verdict-NNN-*/` (fixtures.json → runner → results.json → REPORT.md).

**Pipeline state — honest.** The pipeline is **DRY at EAP close**: P063 was
drafted AND verdicted the same day (V074), so no unverdicted proposal
exists. Standing ORDER 003's "≥1 in flight at all times" duty was satisfied
to the last hour; whether the duty continues is the next phase's first
decision (§E).

**In progress / parked — each with its citation.**

| Item | Where parked | Waits on |
|---|---|---|
| ASK 005 — roster-generator registry-only-row contract | `control/outbox.md` § ASK 005 (live, status: new) | fleet-manager answer |
| Kit ASKs 001–003 (enabler prefix, local=CI gate, card selection) | ACCEPTED upstream per inbox ORDER 010; evidence standard: the NEXT kit-upgrade PR retains the `claude/*` allowlist line | substrate-kit lane |
| Owner three-item bundle | ⚑ block @ [`ff0b1cb` control/status.md](https://github.com/menno420/idea-engine/blob/ff0b1cb5750808ddd2db4eb6c287c1ebde484f77/control/status.md) | owner sitting (§C-1) |
| makerbench build | ORDER 004 rule 4 verbatim: "Do NOT build makerbench — it waits on my tweak reply" (`control/inbox.md`) | owner reply (§C-2) |
| Audit §9 pains 2–5 | [audit §9](audits/eap-project-audit-2026-07-14.md) — MCP repo-scoping, branch-delete 403, scheduling opacity, policy opacity | Anthropic asks ride the fm feedback-email synthesis; pain 3 has an owner click (§C-3) |
| sim-lab OA-002 / OA-003 / OA-004 | sim-lab `docs/retro/archive-ready-2026-07-11.md` § Open owner-actions (+ CAPABILITIES walls fence @ `b10ffce`) | owner clicks (§C-4) |

## C. OWNER ACTIONS — one sitting

Merge clicks: **NONE** — verified 0 open PRs on both repos at 2026-07-14T12:36Z (GitHub MCP `list_pull_requests state=open`: idea-engine `[]`, sim-lab `[]`); this walkthrough's own PR #420 auto-merges on green via the enabler and needs no click.

- [ ] **1.** <https://github.com/menno420/idea-engine/blob/ff0b1cb5750808ddd2db4eb6c287c1ebde484f77/control/status.md> — the standing three-item ⚑ bundle: (1) the four-decision sitting (Lumen Drift itch.io go/no-go · pokemon playtest verdicts · gba concept pick · post-EAP routine posture), (2) websites cutover, (3) gift-repo naming/visibility/cut. **Recommendation: clear the whole bundle in one reply using the three RECOMMENDED one-liners already written in that block** (post-EAP routines Option A · websites cutover Option A · gift repo = makerbench, private + friend as collaborator, all five projects). VERIFY: the next fleet-manager owner-queue sweep marks all three consumed and the ⚑ block drops from the next idea-engine `control/status.md` stamp.
- [ ] **2.** <https://github.com/menno420/idea-engine/blob/main/ideas/venture-lab/maker-gift-repo-blueprint-2026-07-12.md> — the makerbench tweak reply. The build is deliberately NOT started: your standing ORDER 004 rule 4 verbatim "Do NOT build makerbench — it waits on my tweak reply; keep custody current." (`control/inbox.md`). **Recommendation: send the blueprint's paste-ready reply line as-is** — one reply unblocks build slice 1. VERIFY: the next Ideas Lab wake opens the makerbench slice-1 build PR instead of re-parking it.
- [ ] **3.** <https://github.com/menno420/idea-engine/settings> and <https://github.com/menno420/sim-lab/settings> — under General → Pull Requests, tick "Automatically delete head branches" (audit §9 pain 3: 389 merged-but-undeleted branches accumulated in 3.6 days; agents get HTTP 403 on every branch-delete path). **Recommendation: enable on both repos** — two clicks total; already-merged stale branches stay until bulk-deleted from each repo's /branches page (optional). VERIFY: merge any later PR and its head branch disappears from <https://github.com/menno420/idea-engine/branches> within seconds.
- [ ] **4.** sim-lab owner clicks OA-002/OA-003/OA-004 (<https://github.com/menno420/sim-lab/blob/main/docs/retro/archive-ready-2026-07-11.md> § Open owner-actions): OA-002 Codex usage-cap raise/reset · OA-003 review-site deploy · OA-004 harness tag push (agents are 403-walled on `refs/tags/*`). **Recommendation: do OA-004 now from any clone — `git tag harness-v0.1.0 && git push origin harness-v0.1.0` — and take OA-002/OA-003 only if you still want the Codex fold-in and the reviewer site live post-EAP.** VERIFY: <https://github.com/menno420/sim-lab/tags> shows `harness-v0.1.0`; OA-002/003 verify in their own consoles.
- [ ] **5.** Honest null — nothing else is owner-click-shaped: audit §9 pains 2/4/5 (GitHub-MCP repo-scoping, scheduling opacity, policy-boundary opacity) are ANTHROPIC-ask-shaped and ride the fleet-manager's synthesis into the final feedback email; your only touch is sending that email when the fm serves it. VERIFY: the fm close-out synthesis quotes the audit's §9 asks verbatim.

## D. 5-minute tour

1. **The audit** — [docs/audits/eap-project-audit-2026-07-14.md](audits/eap-project-audit-2026-07-14.md):
   §1's measured table (288 cards / 545 PRs / 3.6 days), then §9's ranked
   pains. Two minutes; everything else in this doc hangs off it.
2. **One idea, end to end** — [ideas/superbot-games/menu-width-leverage-inversion-2026-07-14.md](../ideas/superbot-games/menu-width-leverage-inversion-2026-07-14.md):
   the last proposal (P063). See the 8-question probe battery, the
   pre-registered closed-form prediction ({0, 1/2} partition), and the one
   recommendation line — the grammar every one of the 63 ideas passed.
3. **Its verdict, same day** — [sim-lab V074 REPORT.md](https://github.com/menno420/sim-lab/blob/9aaf72b091a378a59f5ed165f9cb01a005ed5e33/sims/verdict-074-menu-width-leverage/REPORT.md):
   REJECT-REORDER; the prediction confirmed, fixtures committed before the
   runner, byte-identical double run, the 59 flagged self-checks disclosed
   as named anomaly A1.
4. **A verdict you can wire tomorrow** — [sim-lab outbox @ `d0a5a75` — VERDICT 076](https://github.com/menno420/sim-lab/blob/d0a5a756b9d3c57bc5f77a93af5bf29e32bc6ed2/control/outbox.md):
   APPROVE-WITH-CONSTANTS P*=12 (minnow 1 / bass 1 / pike 2 / legend_carp 7)
   and the F-FLAT30 perpetual-motion catch.
5. **The heartbeat** — [control/status.md](https://github.com/menno420/idea-engine/blob/main/control/status.md):
   how the seat kept itself honest — one overwritten screen: phase, loop
   state, orders 001–013, the ⚑ block that is your §C item 1.

## E. Handoff — for the next session/phase

**Boot set, in order** (per `.claude/CLAUDE.md`): HARD-SYNC
(`git fetch origin main && git reset --hard origin/main`) → CLAUDE.md →
`HANDOFF.md` (if present) → `docs/current-state.md`; then route via
`docs/AGENT_ORIENTATION.md` as tasks demand. Verify with
`python3 bootstrap.py check --strict` before every push, both repos.

**Batons.**

- `control/status.md` NEXT-2 baton + the proposed next stamp (below).
- ORDER 012/013 done-when: satisfied by this PR (walkthrough on main +
  OWNER ACTIONS surfaced via outbox CLOSE-OUT 001 + claims/ empty).
- ASK 005 watch: live in `control/outbox.md`, awaits the fleet-manager.
- Kit ASKs 001–003 evidence standard: the next kit-upgrade PR must retain
  the `claude/*` enabler allowlist line — check it at upgrade time.
- Pipeline DRY at close (P063→V074 same-day). The next phase's first
  decision: does standing ORDER 003's ≥1-in-flight duty continue? If yes,
  round 13 opens at the fleet-backlogs rotation slot (ORDER 004 rule 3).
- Fleet seed high-water: **20261562** (V074 registration, seeds
  20261559–62, sim-lab #140 @ `9aaf72b`). Allocate strictly above.

**Proposed next `control/status.md` stamp** — written here because the
heartbeat is coordinator-only; this PR does NOT touch it. Coordinator: apply
via the normal wholesale overwrite with a fresh `date -u`, filling the two
`<...>` slots from this PR's merge:

```
updated: <date -u at write> · seat: Ideas Lab coordinator · model family: fable-class
phase: EAP CLOSED. Walkthrough landed: docs/eap-closeout-walkthrough-2026-07-14.md via PR #420 @ <merge sha>; audit @ 8162d1e (#413). ROUTINE DISPOSITION: unchanged from the 09:31:52Z stamp pending the owner's post-EAP posture reply (⚑ item 1d). LOOP STATE: pipeline DRY at close — 63 proposals / 76 verdicts, newest P063 → V074 REJECT-REORDER (sim-lab#140 @ 9aaf72b); claims/ EMPTY (P063 claim pruned in #420). Fleet seed high-water 20261562 (V074, seeds 20261559–62). NEXT-2 BATON: (1) next phase rules on standing ORDER 003's ≥1-in-flight duty — if it stands, round 13 opens at the fleet-backlogs slot; (2) standing watches: ASK 005 awaiting fleet-manager; kit ASKs 001–003 evidence standard = next kit-upgrade PR retains the claude/ line.
health: green — python3 bootstrap.py check --strict exit 0 on this tree immediately before push.
kit: v1.15.0 · check: green · engaged: yes
last-shipped: EAP close-out walkthrough PR #420 @ <merge sha> (doc + P063 terminal-claim prune + outbox CLOSE-OUT 001); 0 open PRs at this write.
blockers: none.
orders: 001–013 ALL done — 012(b)/013 STEP 2 closed by PR #420; owner-actions checklist surfaced via outbox CLOSE-OUT 001.
⚑ needs-owner: unchanged — the three-item bundle @ ff0b1cb, plus the walkthrough §C checklist (docs/eap-closeout-walkthrough-2026-07-14.md).
notes: control-only heartbeat. Successor reading order: this file → docs/eap-closeout-walkthrough-2026-07-14.md → docs/audits/eap-project-audit-2026-07-14.md.
```

**Open threads that live elsewhere:** sim-lab's V075 reframing fork (its
walkthrough + REPORT name the three options); the F-FLAT30 supersession duty
(superbot-games side, before wiring V076 constants); the fm feedback-email
synthesis consuming audit §9.
