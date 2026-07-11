# Ruling-sync at first boot — reconcile decisions that landed while the lane was parked

> **State:** parked(overtaken-by-events — the lane BOOTED and the rulings blackout is over: un-parked into Option A on a standing hourly wake (ORDER 002 consumed per the roster row's own label), heartbeat fresh, no stale concept-pick ask visible on any manager surface at the pin; the pokemon-specific instance is fully mooted — the residual kernel "park-time is a rulings blackout" survives as a one-line fleet convention whose home is the kit's control/README wake ritual, see verify note)
> **Class:** process · **Target:** `menno420/pokemon-mod-lab`
> **Grounding:** https://github.com/menno420/fleet-manager@1afca50 · fetched 2026-07-11T07:49:14Z
> *(pin annotation: verify-time re-check pin — the capture's grounding was manifest-relayed @ superbot `53fb5ef` (2026-07-10; manifest since retired to a pointer stub, fm roster canonical); the lane repo stays private/DARK from here, so every verify fact is roster/manager-relayed at the fm pin per the README DARK-lane recipe; fm HEAD via `git ls-remote` 2026-07-11T07:49:14Z (re-confirmed unmoved 07:56:38Z), tree reads via read-only blobless clone at that pin; Q-0262.7 ruling text re-verified live at superbot HEAD `58040c6`, same ls-remote batch)*

## Problem

The lane parked at **07:49Z** (session-008 ender, manifest row @ 53fb5ef) with "concept
pick" as an open owner ask. The pick was then RULED the same day while the lane slept:
**Q-0262.7, concept = QoL+** (blanket application of the round-3 recommendations, live
dispatch session). The manifest row now carries both facts side by side — "owner:
playtest verdict + concept pick (rec: Emerald QoL+, effective post-core per Q-0262.7)"
— i.e. a **stale owner ask standing next to its own answer**. A first relaunch session
that trusts the parked ender will re-ask an answered question, which is exactly the
drift the control protocol bans ("expire or withdraw stale asks every session") and
which costs the scarcest resource in the program, owner attention.

## Idea

Make **ruling reconciliation a named first-boot step** for this lane (and a reusable
pattern for any parked lane): before resuming work, the first relaunch session diffs
its parked ender's open asks against rulings younger than the park — here, fetch the
question-router entries stamped after 07:49Z (Q-0262 at minimum), mark the concept-pick
ask **answered (QoL+)** in its status overwrite, and consume pending inbox ORDERs
002/003 in the same pass (the manifest names them "consumable at first boot"). Output
is one status.md whose ⚑ list contains only genuinely-open items. The generalizable
kernel: *park-time is a rulings blackout* — any lane without a standing wake must treat
"asks older than my park" as unverified until diffed against the router.

## Grounding

- Manifest pokemon-mod-lab row @ [`53fb5ef`](https://raw.githubusercontent.com/menno420/superbot/53fb5ef9a294ab304b679dedd44ead55849295d5/docs/eap/fleet-manifest.md)
  (fetched 2026-07-10 ~20:35Z): status 07:49Z session-008 ender; "ORDERs 002/003
  pending, consumable at first boot"; the owner-ask line carrying its own answer.
- Q-0262.7 (the ruling that answered the parked ask) @
  [`53fb5ef`](https://raw.githubusercontent.com/menno420/superbot/53fb5ef9a294ab304b679dedd44ead55849295d5/docs/owner/maintainer-question-router.md).
- Stale-ask hygiene rule: idea-engine `control/README.md` § ⚑ needs-owner ("expire or
  withdraw stale asks every session") — the fleet-wide contract this capture applies to
  the parked-lane case.

**Why now:** the first relaunch must be externally fired (no standing wake, ORDER 002
pending) — whoever fires it can hand this step in the wake prompt, and the concept-pick
discrepancy is live in the manifest today.

## Verify-and-park (2026-07-11)

*Verify-first per README § The probe battery, same pass and same single pin as the
sibling park (`qol-plus-wave-2-option-board-2026-07-10.md` — one fm blobless clone
at `1afca50` served both verify notes; the #131 card's DARK-lane recipe). Premise
found part-mooted; judged honestly below: instance MOOTED, kernel SURVIVES. No
battery pass, no `**Recommendation:` line — that token belongs to probe reports.*

**Invariant keyed on:** "before resuming work, a first relaunch session diffs its
parked ender's open asks against rulings younger than the park — the ⚑ list it
publishes contains only genuinely-open items."

**Verified, with citations (all @ fleet-manager `1afca50` unless noted):**

- **The first-boot moment PASSED** — the lane is UN-PARKED on a standing hourly
  wake: fm `control/status.md` gen-#4 lane-notes block ("pokemon-mod-lab —
  **UN-PARKED** (Q-0266 decide-and-flag → Emerald QoL+; owner can override);
  hourly wake `30 * * * *` (fresh-session mode)"); roster gen #5 row: FRESH,
  heartbeat 2026-07-11T04:03:05Z, phase "Option A (Emerald QoL+ deepening…",
  evidence `297f67b` 04:13:49Z. There is no pending externally-fired first boot
  left for this step to ride, and no "no standing wake" lane state left to guard.
- **ORDER 002 was consumed** — the roster row itself labels the live trigger
  "**pokemon-mod-lab hourly wake (ORDER 002)** `trig_01BTJjkMVMKtWPjuYe7643Hi`" —
  the wake-arm order this capture said to consume at first boot is the standing
  wake now.
- **The stale-ask discrepancy this capture priced is GONE from the visible
  surfaces** — the capture's trigger artifact was a manifest row carrying "a stale
  owner ask standing next to its own answer"; that manifest is retired (pointer
  stub; fm roster canonical since 2026-07-11, this repo's PR #66 re-point), and at
  `1afca50` no manager surface carries a stale concept-pick ask: fm status keeps
  pokemon visible ONLY as "pokemon#8 open on owner playtest only", and the ruling
  is being EXECUTED, not re-asked (Option A = Emerald QoL+ deepening; Q-0262.7
  re-verified verbatim at superbot `58040c6`: "Pokemon concept pick = QoL+ …
  takes effect when the games program boots post-core").
- **ORDER 003 residue: NOT MEASURED** — fm `control/inbox.md` (roster gen #1 ✅DONE
  block) recorded "pokemon ORDER 003 unconsumed"; roster gen #5's pokemon Orders
  column reads "—" (lane DARK, orders line not machine-visible). Whether 003 was
  since consumed is unknowable from here; that watch belongs to the manager's
  roster sweep, not to a first-boot step whose moment has passed.

**Judgement — what is mooted, what survives, and where it should live:**

- **MOOTED (the instance):** the pokemon-specific first-boot reconciliation. The
  lane booted, the blackout ended, the answered ask is nowhere visible, and the
  wake-arm order is consumed. Nothing here is buildable for this lane anymore.
- **SURVIVES (the kernel):** *park-time is a rulings blackout — a lane resuming
  from park treats asks older than its park as unverified until diffed against
  rulings younger than the park.* This is NOT yet written anywhere reusable:
  `control/README.md` ⚑ hygiene ("expire or withdraw stale asks every session")
  covers RUNNING lanes' wakes, not the park-resume case, and the roster's >24h
  kill-switch covers roster staleness, not ask staleness. The class shrank by
  construction (roster gen #4: "ZERO triggerless live lanes" — every live lane now
  wakes on cron) but did not die: parks still exist fleet-wide (codetool-lab*
  rows are STALE-BY-DESIGN; this very lane was parked days ago), so the kernel
  stays cheap and true.
- **Where it should live:** ONE sentence in the kit's planted `control/README.md`
  per-session ritual (park-resume clause) — a substrate-kit lane change, so every
  adopter inherits it. Graduation path: a one-line `ideas/substrate-kit/` capture
  (that section was under a sibling claim when this pass started; the park note
  and the session-card handoff carry the kernel so it is not orphaned). Not
  routed from here this slice — this PR stays inside its claimed section.

**Verdict: verify-and-park** — state flipped forward-only captured →
`parked(overtaken-by-events)`, kernel recorded above. Nothing sim-shaped: the
instance is dead by evidence, and the surviving kernel is a one-sentence doctrine
line proven by the four datapoints already cited, not by a simulator.
