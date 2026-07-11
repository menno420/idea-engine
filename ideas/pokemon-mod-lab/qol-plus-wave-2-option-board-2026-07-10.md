# QoL+ wave-2 option board — reseed the exhausted patch queue under the ruled concept

> **State:** parked(overtaken-by-events — the lane un-parked straight into "Option A (Emerald QoL+ deepening)" WITHOUT waiting for this board: Q-0266-labeled decide-and-flag pick fm-side, hourly wake live `30 * * * *`, heartbeat fresh and mid-wave-2 at verify time — the "parked lane, zero runway, externally-fired first boot" premise is historical)
> **Class:** product · **Target:** `menno420/pokemon-mod-lab`
> **Grounding:** https://github.com/menno420/fleet-manager@1afca50 · fetched 2026-07-11T07:49:14Z
> *(pin annotation: verify-time re-check pin — the capture's grounding was manifest-relayed @ superbot `53fb5ef` (2026-07-10; the manifest has since been retired to a pointer stub, fm roster canonical); the lane repo stays private/DARK from here, so every verify fact is roster/manager-relayed at the fm pin per the README DARK-lane recipe; fm HEAD via `git ls-remote` 2026-07-11T07:49:14Z (re-confirmed unmoved 07:56:38Z), tree reads via read-only blobless clone at that pin; the Q-0262.7 ruling text re-verified live at superbot HEAD `58040c6`, same ls-remote batch)*

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

## Verify-and-park (2026-07-11)

*Verify-first per README § The probe battery (a captured head whose premise a live
lane-state read can settle gets a five-minute verify-and-park FIRST, keyed on the
capture's INVARIANT — escalating to a full battery pass only if the live check finds
the gap still open; the PR #66/#131 form). The live check found the premise
OVERTAKEN, so no battery pass runs and no `**Recommendation:` line is written — that
token belongs to probe reports. The lane is DARK (private) from this repo, so all
lane facts below are roster/manager-relayed at ONE fleet-manager pin, `1afca50`
(`git ls-remote` 2026-07-11T07:49:14Z; re-confirmed unmoved 07:56:38Z), per the
README DARK-lane recipe; the DARK wall itself is the standing capability finding,
re-verified three ways the same day by the #131 probe (raw 404 ×2, ls-remote auth
wall, MCP scoped here — `.sessions/2026-07-11-pokemon-playtest-kit-probe.md`), not
re-attempted here.*

**Invariant keyed on:** "the externally-fired first relaunch session arrives with a
mandate but ZERO runway — no next patch named anywhere the fleet can see — so it
must reseed the queue (as an option board) before building."

**Verified, with citations (all @ fleet-manager `1afca50` unless noted):**

- **The lane is UN-PARKED and AWAKE** — fm `control/status.md` (roster gen #4
  lane-notes block): "pokemon-mod-lab — **UN-PARKED** (Q-0266 decide-and-flag →
  Emerald QoL+; owner can override); hourly wake `30 * * * *` (fresh-session mode);
  private re-verified 01:35:50Z." No externally-fired first boot is pending — the
  boot happened, and the wake is standing.
- **The lane has DIRECTION and is already building under it** — fm `docs/roster.md`
  (GENERATED, gen #5, generated-at 2026-07-11T04:28Z) pokemon-mod-lab row: FRESH,
  heartbeat `updated:` 2026-07-11T04:03:05Z (~24m at generation), phase "Option A
  (Emerald QoL+ deepening, Q-0266 flagged reversible", kit v1.6.0 · check: green ·
  engaged: yes, hourly wake `trig_01BTJjkMVMKtWPjuYe7643Hi` `30 * * * *`, evidence
  `297f67b` 04:13:49Z. The phase's own "Option A" token shows a direction pick
  landed and stuck; scope meanwhile GREW to a 12-patch #4–#8 train + session-012
  QoL+ slice 2 (fm `docs/owner-queue.md` item 3 at the same pin, citing pokemon
  PR #16 `aeaa4f7` — manager-relayed; same read as the #131 card).
- **The exact overtaking is RECORDED manager-side** — fm
  `docs/findings/manifest-parallel-run-2026-07-11.md` pokemon row: manifest said
  "'**none** — first relaunch must be externally fired'; LANE PARKED" vs live
  "**hourly wake LIVE** `trig_01BTJjkMVMKtWPjuYe7643Hi` `30 * * * *` (created
  01:37:07Z, fresh-session mode); lane **UN-PARKED** — Q-0266 pick = Emerald QoL+
  (the manifest's own recommendation, now taken)", citing lane `control/status.md`
  @ `c692130`. This capture's grounding row and its overtaking sit in the same
  table.
- **Ruling-label honesty note:** the superbot question-router @ HEAD `58040c6` has
  NO pokemon entry under Q-0266 — its Q-0266 is the volume-first founding doctrine.
  The concept ruling behind the pick is **Q-0262.7** ("Pokemon concept pick = QoL+
  … takes effect when the games program boots post-core", re-verified verbatim at
  `58040c6`); "Q-0266" is the fm-side label on the decide-and-flag Emerald/Option-A
  pick (owner can override). The id mismatch is recorded here, not resolved — it is
  fm's ledger to fix.
- **Not measured:** whether the lane formally drafted a 3-direction board before
  the pick (lane tree unreadable — DARK). It does not bear on the verdict: the
  premise this capture priced (parked lane + zero runway + a first boot that burns
  its slice rediscovering direction) is gone whichever way the board happened.

**Verdict: verify-and-park** — state flipped forward-only captured →
`parked(overtaken-by-events)`. The shape this capture fixed (options + recommend +
proceed, Q-0259 r.5) was consumed by events at pick time; nothing to queue, route,
or simulate — the lane is awake, directed, and mid-wave-2 on an hourly cadence.
