# Ruling-sync at first boot — reconcile decisions that landed while the lane was parked

> **State:** captured
> **Class:** process · **Target:** `menno420/pokemon-mod-lab`

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
