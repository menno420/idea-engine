# Session — pokemon-mod-lab verify-and-park pair (option-board + ruling-sync, both premises settled at one fm pin)

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-11 ~07:55Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

The #131 card's handoff named this exact pair as "the section's next natural head":
`ideas/pokemon-mod-lab/qol-plus-wave-2-option-board-2026-07-10.md` (likely OVERTAKEN —
the lane un-parked straight into Option A without the board) and
`ruling-sync-first-boot-2026-07-10.md` (likely part-mooted — the lane HAS booted).
Verify-and-park pair per README § The probe battery (verify-first rule; the PR #66/#131
form): no battery pass, no `**Recommendation:` token, one-line verdicts on evidence
pins. Section claimed first — `control/claims/probe-pokemon-mod-lab-verify-park-pair.md`
landed on main via fast-lane PR #133 (merged 711931b by the enabler) before any build
work; claims dir re-read at the recut: zero sibling claims live (the substrate-kit
clobber-family claim cleared when its PR #132 merged mid-window). Claim deleted in this
PR.

## Verify-first record (one sweep, one pin, both verdicts)

- **The lane is DARK** (private) — the standing wall, re-verified three ways the same
  day by the #131 probe (raw 404 ×2, `git ls-remote` auth wall, MCP scoped to
  idea-engine; `.sessions/2026-07-11-pokemon-playtest-kit-probe.md`), not re-attempted
  here per docs/CAPABILITIES.md (check-the-file beats re-paying a verified wall on the
  same day). All lane facts are roster/manager-relayed, per the README DARK-lane recipe.
- **fleet-manager pinned at `1afca50e171a33591f8481f0ac837b989c280425`** (`git
  ls-remote` 2026-07-11T07:49:14Z; re-confirmed unmoved 07:56:38Z; blobless clone,
  tree reads at HEAD) — the SAME pin the #131 card read ~20 min earlier, so its
  relayed evidence carried over without re-derivation. Surfaces read at the pin:
  roster gen #5 pokemon row (FRESH, heartbeat 04:03:05Z, phase "Option A (Emerald
  QoL+ deepening, Q-0266 flagged reversible", hourly wake
  `trig_01BTJjkMVMKtWPjuYe7643Hi` `30 * * * *` labeled "(ORDER 002)", evidence
  `297f67b` 04:13:49Z) · fm control/status.md gen-#4 note ("pokemon-mod-lab —
  UN-PARKED (Q-0266 decide-and-flag → Emerald QoL+; owner can override)") ·
  docs/findings/manifest-parallel-run-2026-07-11.md pokemon row (the overtaking
  recorded verbatim, lane status cited @ `c692130`) · control/inbox.md gen-#1 block
  ("pokemon ORDER 003 unconsumed") · docs/owner-queue.md item 3 (scope grown to the
  #4–#8 train + session-012 QoL+ slice 2, pokemon PR #16 `aeaa4f7`).
- **superbot router re-verified live at HEAD `58040c6`** (ls-remote same batch; raw
  fetch of `docs/owner/maintainer-question-router.md`): Q-0262.7 verbatim ("Pokemon
  concept pick = QoL+ … takes effect when the games program boots post-core").
  **Honesty finding:** the router's Q-0266 is the volume-first founding doctrine —
  there is NO pokemon entry under Q-0266; "Q-0266" is the fm-side label on the
  decide-and-flag Emerald/Option-A pick. The id mismatch is recorded in both park
  notes, not resolved (fm's ledger to fix).

## Verdicts

- `qol-plus-wave-2-option-board` → **parked(overtaken-by-events)**: the "parked lane +
  zero runway + externally-fired first boot" premise is historical — the lane
  un-parked straight into "Option A (Emerald QoL+ deepening)" on a standing hourly
  wake and is mid-wave-2 (scope grown per owner-queue item 3). Whether a formal
  3-direction board was drafted lane-side is NOT MEASURED (DARK) and does not bear on
  the verdict.
- `ruling-sync-first-boot` → **parked(overtaken-by-events)**, judged honestly as a
  split: the pokemon INSTANCE is fully mooted (lane booted, blackout over, ORDER 002
  consumed per the roster row's own label, no stale concept-pick ask visible on any
  manager surface at the pin; ORDER 003 residue NOT MEASURED — the manager's roster
  sweep owns that watch). The residual KERNEL survives: *park-time is a rulings
  blackout — a lane resuming from park treats asks older than its park as unverified
  until diffed against rulings younger than the park.* It is written nowhere reusable
  (⚑ hygiene covers running wakes, not park-resume); its home is ONE sentence in the
  kit's planted control/README.md per-session ritual (substrate-kit lane); graduation
  path = a one-line ideas/substrate-kit capture, deliberately NOT landed from this
  claimed-section slice.

No outbox proposal (both verdicts are parks; nothing sim-shaped). Section README
index re-badged for both rows.

## Section progress — ideas/pokemon-mod-lab after this pair

- post-eap-playtest-kit — parked(build-direct) @ PR #131 (owner-sitting-bound,
  2026-07-14 window).
- qol-plus-wave-2-option-board — parked(overtaken-by-events), this PR.
- ruling-sync-first-boot — parked(overtaken-by-events), this PR.
- **patch-only-egress-doctrine — the section's LAST open head, still `captured`**
  (state line verified in-tree this session): the private-flip lesson as doctrine +
  CI tripwire, "land before the first post-EAP egress event" — expiry-adjacent to
  the same 2026-07-14 window (an owner-verdict "keep" plausibly triggers the first
  patch egress). The section is 3/4 probed-or-parked; that head is the natural next
  claim here.

## Verification (real runs, this tree)

Full `python3 scripts/preflight.py` (all 8 checks) + `python3 bootstrap.py check
--strict` run green immediately before push, after the heartbeat overwrite (outputs
quoted in the PR). Telemetry residue: this seat's hook-born `.substrate/` appends
left uncommitted for the telemetry lane per the PR #32/#58/#62 precedent.

**📊 Model:** fable-5 · verify-and-park pair (2 verify notes + state lines + section
index re-badge + card + claim add via #133/clear via this PR + heartbeat; no scripts,
no workflows, no proposal — task-class: bounded DARK-lane verify pass)

## 💡 Session idea

**A Q-id is being reused across fleet surfaces with two meanings and nothing checks
it:** the router's Q-0266 is the volume-first doctrine, while fm's roster/status/
parallel-run all cite "Q-0266" as the pokemon Emerald-pick label — a consumer that
greps the router by the fm label lands on the WRONG ruling (this session did, and
only the verbatim-quote discipline caught it). Cheap fleet convention: any surface
citing a Q-id outside the router quotes ≥3 words of the entry's title alongside the
id (a "quote-anchored Q-id" rule); a checker can then verify id↔title agreement at
harvest time. Natural home: fm's roster generator + the kit's grammar notes;
fleet-section capture candidate.

## ⟲ Previous-session review

Reviewed: `.sessions/2026-07-11-substrate-kit-clobber-family-probe.md` (PR #132,
squash `02fc832`) — the actual newest card at my read; the dispatch briefing named
`2026-07-11-superbot-mineverse-first-batch.md`, which is ~30 merges older (same
briefing-lag the #131 card recorded — dispatch handoffs age within hours here).
Verified against the tree: both clobber-family probe reports exist as carded with
`parked(routed …)` state lines, the section README rows are re-badged, its claim
file is gone from control/claims/, and its heartbeat landed with the ⚑ block
preserved. Adopted from it: (a) its 💡 verify-first recipe — ls-remote for the pin,
blobless clone for topology, named-path checkout only, never grep a partial working
tree (this session's fm reads followed it verbatim, `git show HEAD:<path>` per
file); (b) "re-verify at the new HEAD before relaying" — applied as the double
ls-remote on fm (07:49 + 07:56) bracketing the evidence reads. Its handoff aged
accurately: it predicted this exact sibling slice ("the pokemon-mod-lab sibling
probe was in flight… reconciled forward at push time") — the reconciliation proved
unnecessary only because its own merge landed BEFORE this branch was cut.

## Handoff → next wake

- **Section closer:** `patch-only-egress-doctrine` is pokemon-mod-lab's last open
  head, window-adjacent (2026-07-14 sitting → possible first egress event) — probe
  or verify-and-park it BEFORE the sitting; after it, the section is fully
  probed-or-parked (would be the SIXTH complete section).
- **Kernel graduation (small, unclaimed):** one-line ideas/substrate-kit capture —
  park-resume ruling-sync clause for the kit's planted control/README.md ritual
  (evidence already pinned in ruling-sync-first-boot's verify note; the kit-lane
  fan-in is already three routed heads deep per the #132 card — this rides the same
  future ORDER).
- **Q-id label mismatch** (💡 above): cheapest as a one-line note in the fm relay
  the next time a slice talks to the manager; do not re-derive — both park notes
  quote the evidence.
- Guard recipe: DARK-lane verify path unchanged — blobless clone fm, `git grep -n
  -i '<lane>' HEAD -- ':!.sessions'`, read roster row + status lane-note +
  owner-queue + parallel-run at ONE pinned HEAD, cite fm@sha per fact; anonymous
  api.github.com 403s through the proxy — MCP or git transport only.
