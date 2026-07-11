# Session — pokemon-mod-lab post-EAP playtest-kit probe (DARK-lane, roster/manager-relayed)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~07:30Z (worker slice, dispatched by the coordinator under continuous-chaining mode per Q-0265)

## Scope

Probe `ideas/pokemon-mod-lab/post-eap-playtest-kit-2026-07-10.md` (seeded by PR #15's
first batch) through the battery v0, single-pass — the section's first probe, and a
TIME-BOUND head: the EAP window closes 2026-07-14 and the idea's Sequence is the same
owner sitting the Lumen Drift play kit (PR #34) targets. Section claimed first —
`control/claims/probe-pokemon-mod-lab-post-eap-playtest-kit.md` landed on main via
fast-lane PR #129 (merged 07:32:19Z by the enabler) before any build work; claims dir
re-read at the recut (HEAD `371f940`): one sibling claim live
(`probe-substrate-kit-clobber-family`), disjoint section, no collision. Claim file
deleted in this PR.

## Verify-first record (every load-bearing claim pinned)

- **The lane is still DARK** — re-verified three ways 2026-07-11T07:32Z: raw fetch 404
  on `control/status.md` AND `README.md`; `git ls-remote` auth wall ("could not read
  Username … terminal prompts disabled"); GitHub MCP scoped to idea-engine only.
  Corroborated manager-side: "Unauthenticated curl to the private pokemon repo 404s"
  (fm `control/status.md` @ `1afca50`). All lane facts are therefore roster/manager-
  relayed, shape-not-content, per the README DARK-lane recipe.
- **Registry read at live fleet-manager HEAD** `1afca50e171a33591f8481f0ac837b989c280425`
  (ls-remote 07:32:13Z; the raw-main `docs/roster.md` fetch at 07:31Z verified
  byte-identical to the HEAD blob via blobless clone). Roster gen #5 (generated
  2026-07-11T04:28Z, first machine generation) pokemon-mod-lab row: FRESH, heartbeat
  04:03:05Z, phase "Option A (Emerald QoL+ deepening, Q-0266 flagged reversible", kit
  v1.6.0 · check green · engaged yes, hourly wake `trig_01BTJjkMVMKtWPjuYe7643Hi`
  `30 * * * *`, evidence `297f67b` 04:13:49Z. The lane is UN-PARKED (gen #4 note:
  "pokemon UN-PARKED (Q-0266 decide-and-flag → Emerald QoL+; owner can override)") —
  the capture's "parked ender" premise is historical.
- **ORDER scan (fm surfaces @ `1afca50`):** lane-relayed orders visible = ORDER 002
  (hourly wake, roster row) + ORDER 004 (model-attribution, lane PR #19 `743525d`);
  ORDER 003 recorded "unconsumed" at roster gen #1. NO playtest-kit order anywhere —
  despite fm's own night review (`docs/findings/night-review-2026-07-10.md` Q4 +
  rec 12) prescribing exactly this kit and saying "that preparation session should be
  ordered now".
- **The owner ask exists, half-drafted:** fm `docs/owner-queue.md` item 3 @ `1afca50`
  (keep/tune/drop per patch; scope updated 2026-07-11 to the 12-patch #4–#8 train +
  session-012 QoL+ slice 2, pokemon PR #16 `aeaa4f7`); review-queue row pokemon#8 stays
  open SOLELY on the playtest feel half (sha1-chain half manager-verified, fm PR #61
  `5244a1c`). Its WHERE still names no artifact path, no notes page, no verdict form —
  the kit-shaped gap the capture priced is still open manager-side.

## Verdict

`park(build-direct)` — exact recommendation line on the idea file:
`**Recommendation: park**` — one lane PR (pinned artifact + tree-generated
player-visible notes + keep/tune/drop verdict form) plus a one-line fm owner-queue
WHERE fix; proven by the owner sitting, nothing sim-shaped, NO outbox proposal.
Owner-sitting-bound: same 2026-07-14 window as Lumen Drift — flagged in the heartbeat
so the manager routes it NOW (fm order or lane self-serve — the lane wakes hourly) or
explicitly lets it lapse. State line advanced forward-only to `parked(build-direct — …)`;
blessed Grounding/Sequence header lines added (forward-only additions), section README
badge flipped.

**📊 Model:** fable-5 · single-pass probe + docs (idea file append, section README
badge, card, heartbeat, claim add/clear; no scripts, no workflows, no proposal —
task-class: bounded DARK-lane probe)

## 💡 Session idea

A DARK lane's manager-relay surfaces disagree in freshness by construction — the
roster row, owner-queue item, review-queue row, and night-review each carried a
DIFFERENT slice of this lane's truth (the roster knew Q-0266/Option A; only the
owner-queue knew the scope grew to PR #16; only the review-queue knew the code half
was verified; only the night review knew a kit had been prescribed). A "manager-relay
freshest-wins" note in the README DARK-lane recipe — enumerate ALL manager surfaces
that mention the lane, cite each at the same fm pin, and let the newest stamped fact
win per surface — would make DARK-lane probes mechanical instead of archaeological.
This probe did it by hand (one fm blobless clone, four surfaces, one pin).

## ⟲ Previous-session review

PR #126 (`probe/verdict-registry-2026-07-11`, merge `186e8cc`) — the actual newest
card at my read (`.sessions/2026-07-11-verdict-registry-probe.md`; the dispatch
briefing named the mineverse first-batch card, which is 30+ merges older). Verified
against the tree: the SIM-VERDICT lint is live in `scripts/check_ideas.py` (my
preflight run rides it — same 3 advisory legacy warnings it documented, exit 0), the
idea file + fleet README index bullet exist as carded, its claim file is gone, and
its heartbeat landed with the ⚑ OWNER-ACTION preserved. Adopted from it: (a) the
`mergeable_state: dirty` → zero-check-runs jam recipe (watched for at my PR); (b)
its friction note "anonymous api.github.com polling 403s through the proxy — use
GitHub MCP or authenticated git" (this slice went straight to MCP + blobless clone,
zero 403 friction); (c) fetch-RAW-at-the-pin before asserting foreign-repo field
facts (applied to every fm citation above). Its handoff's "ripest next" (websites
new-borns + kit hop) was already partly consumed by siblings #125/#128 — stale
within two hours; window-bound heads like this one age even faster, which is why
this probe went out of briefing order.

## Handoff → next wake

- **The 2026-07-14 fan-in is the live item:** BOTH owner-sitting kits (Lumen Drift ⚑
  OWNER-ACTION + this playtest-kit park) now share the same closing window — the
  heartbeat flags them as one sitting; the manager's :30 sweep should route the
  pokemon kit (fm order or lane self-serve) before ~2026-07-13 or record the lapse.
- **Section follow-up, probably cheap:** `qol-plus-wave-2-option-board-2026-07-10.md`
  (same section, still `captured`) looks OVERTAKEN — Q-0266 un-parked the lane
  straight into "Option A (Emerald QoL+ deepening)" per the roster row, which reads
  like the option board's decision landed without the board. A five-minute
  verify-and-park at the fm pin is the next natural head here; `ruling-sync-first-boot`
  likely part-mooted the same way (the lane HAS booted).
- Guard recipe: DARK-lane probe fm-relay path = blobless clone of fleet-manager,
  `git grep -n -i '<lane>' HEAD -- ':!.sessions'`, then read roster row + owner-queue
  item + review-queue row + night-review at ONE pinned HEAD; cite fm@sha for every
  fact. Anonymous `api.github.com` 403s through the proxy — MCP or git only.
- Telemetry residue: this seat's hook-born `.substrate/guard-fires.jsonl` /
  `reflections.json` appends left uncommitted for the telemetry lane per the
  PR #32/#58/#62 precedent.
