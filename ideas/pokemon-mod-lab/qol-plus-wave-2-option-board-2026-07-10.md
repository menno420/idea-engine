# QoL+ wave-2 option board — reseed the exhausted patch queue under the ruled concept

> **State:** captured
> **Class:** product · **Target:** `menno420/pokemon-mod-lab`

## Problem

The lane is PARKED at session 008 with its **patch queue exhausted**: PRs #2–#10
shipped 12 QoL patches and nothing is left to build (manifest row @ 53fb5ef). Meanwhile
the concept question the lane parked on has since been RULED: **Q-0262.7 picked QoL+**
("the lane's own recommendation; 12 patches form its foundation — takes effect when the
games program boots post-core"). So the first relaunch session — which must be
externally fired (no standing wake; ORDER 002 pending) — arrives with a mandate but
**zero runway**: no next patch is named anywhere the fleet can see.

## Idea

Reseed the queue as an **option board, not a flat list**, per the Q-0259 r.5 standing
instruction for the games program: "presenting a few options wherever that feels wise
rather than asking." Concretely: the first relaunch session drafts 3 candidate QoL+
wave-2 directions (each a coherent patch family that *extends* the 12-patch foundation
— e.g. deepening an existing patch family vs. opening a new QoL surface vs. optional
difficulty/convenience toggles), each with a per-patch effort estimate and a
recommendation, then **starts building the recommended one immediately** — the board
informs the owner's post-EAP playtest verdict, it does not wait for it (Q-0259 r.5: the
owner tests everything later; improvement rounds follow). The exact wave-2 contents are
the lane's call from its own tree — this capture fixes the *shape* (options + recommend
+ proceed) and the *priority* (first thing after boot ceremony), not the patch list.

## Grounding

- Manifest pokemon-mod-lab row @ [`53fb5ef`](https://raw.githubusercontent.com/menno420/superbot/53fb5ef9a294ab304b679dedd44ead55849295d5/docs/eap/fleet-manifest.md)
  (fetched 2026-07-10 ~20:35Z): "LANE PARKED at session 008 (PRs #2–#10, 12 QoL
  patches, queue exhausted)"; "ORDERs 002/003 pending, consumable at first boot";
  "owner: playtest verdict + concept pick (rec: Emerald QoL+, effective post-core per
  Q-0262.7)".
- Q-0262.7 + Q-0259 r.5 @ [`53fb5ef`](https://raw.githubusercontent.com/menno420/superbot/53fb5ef9a294ab304b679dedd44ead55849295d5/docs/owner/maintainer-question-router.md):
  concept pick = QoL+ (ruled); games program = continuously improve, present options.
- Lane repo itself is UNREADABLE from this repo (private since ~15:12Z per the manifest
  row; raw-read 404 verified this session — the Q-0260 rule-3 carve-out) — grounding is
  manifest-relayed, so wave-2 *content* is deliberately left to the lane.

**Why now:** the concept ruling landed AFTER the lane parked (status 07:49Z vs. the
same-day Q-0262 dispatch session) — without a reseeded queue the externally-fired first
boot burns its slice rediscovering direction instead of shipping patches.
