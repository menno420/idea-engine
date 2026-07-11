# Gen-2 boot pack — kit v1.7.0 upgrade + `adopt --lane` heartbeat declaration

> **State:** parked(overtaken — the lane's gen-2 boot executed or dissolved every element of this capture's one bounded PR before the probe ran: kit already v1.7.1, two versions past the capture's v1.2.0→v1.7.0 target (lane PRs #22/#23); the two-writer heartbeat premise INVERTED by the Q-0267 single-seat unification (lane PR #24 — per-lane status files banner'd GEN-1 HISTORY, "do not resurrect the split", so `adopt --lane` today would re-plant what the lane deliberately archived); `heartbeat_files: ["control/status.md"]` verified MATCHING the unified reality at `9b09b99`; ORDER 001 executed in host-owned tests.yml, ORDER 002 done (wake routine armed — lane no longer clockless). No residual slice, no sim question)
> **Class:** process · **Target:** `menno420/superbot-games`

## Problem

superbot-games runs the fleet's oldest live kit pin (**v1.2.0**) and carries a flagged
**two-writer heartbeat ⚑**: its cohabitation contract already splits the heartbeat by
hand (`control/status-mining.md` / `control/status-exploration.md` are each lane's sole
property — `docs/lanes.md` ownership table @ `adb5f9b`), but a v1.2.0 kit predates
`heartbeat_files`, so the gate cannot see or enforce the per-lane files the repo actually
uses. Gen-2 relaunch is imminent and currently **clockless and boot-gated** (manifest:
ORDER 001 P0 pending, ORDER 002 self-arm wake landed-unexecuted) — booting two Projects
onto an undeclared heartbeat scheme re-runs the exact collision class the split exists to
prevent.

## Idea

One bounded PR at the lane's next boot: `bootstrap upgrade` to kit v1.7.0, then
`bootstrap adopt --lane mining` + `adopt --lane exploration` — v1.7.0's `adopt --lane` is
skip-if-exists (never re-plants the sibling's files, the double-adoption fix) and
declares both files in `substrate.config.json` → `heartbeat_files`, so the status checker
gates each lane independently and a missing/heartbeat-less lane goes strict-RED instead
of invisible. Honors the lane's "kit adoption ONCE / second Project verifies" rule.

## Grounding

- Fleet manifest games-plugins row (`https://raw.githubusercontent.com/menno420/superbot/main/docs/eap/fleet-manifest.md`,
  fetched 2026-07-10): "kit v1.2.0 (v1.7.0 `adopt --lane` is the fix for its two-writer ⚑)";
  ORDER 001 P0 boot-gating; ORDER 002 unexecuted.
- `menno420/superbot-games` @ `adb5f9b` — `docs/lanes.md` (per-lane status file ownership;
  "Kit adoption — ONCE") and `control` protocol mirrored in this repo's
  `control/README.md` § Multi-Project repos (`heartbeat_files`, `adopt --lane` semantics).

**Why now:** the fix ships in the kit today, and the lane's first gen-2 boot session is
the one moment it can land before the two-writer flag becomes a live incident.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://github.com/menno420/superbot-games@9b09b996f8d49c98a62f3be4e080b948d8a500f3 · fetched 2026-07-11T00:26Z (manifest row: behind)
> **Grounding:** https://github.com/menno420/superbot@7c6278ec990d9230aac439cb748465bf23bcec56 · fetched 2026-07-11T00:26Z
> **Sequence:** after the event it targeted — the capture was scoped "at the lane's next boot" and that boot EXECUTED 2026-07-10/11 before this probe: kit upgraded v1.2.0→v1.7.0→v1.7.1 (lane PRs #22/#23, merges `4493292`/`b134961`), ORDER 001 shipped (lane PR #24, merge `7d4c347`), single-seat unification landed (Q-0267, same PR), fishing skeleton on top (lane PR #25, merge `9b09b99`)

*Probed against live state, not the capture's snapshot — and the live state overtook
the capture wholesale. superbot-games moved `b134961` → `7d4c347` → `9b09b99` overnight
(HEAD even advanced BETWEEN this probe's ls-remote and its blobless clone — the lane is
actively shipping). Verified at `9b09b99`: `substrate.config.json` reads
`"kit_version": "1.7.1"` and `"heartbeat_files": ["control/status.md"]`; lane
`control/status.md` is the unified single-seat heartbeat ("Boot record: landed on
origin/main HEAD `b134961` (substrate-kit v1.7.1) … the per-lane
`control/status-mining.md` / `control/status-exploration.md` files are now GEN-1
HISTORY archives … do not resurrect the two-lane split"), `orders: acked=001,002
done=002` with its Orders section marking ORDER 001 **done** (merged lane PR #24) and
ORDER 002 **done** (routine `trig_019ZgWyL78Rx1sr6LhvL8NE3` armed 2026-07-10T23:47:02Z,
verified via list_triggers, Q-0265 supersession note recorded); `docs/lanes.md` carries
the "⟵ GEN-1 HISTORY … do not resurrect the split" banner (commit `dcc22c3`); the
ORDER 001 fix lives in host-owned `.github/workflows/tests.yml` (commit `0e5786b`:
collect `tests/` + `games/exploration/tests/`, count floor — raised 121→147 by lane
PR #25 commit `8b9f153` when the fishing suite landed). The lane's inbox at `9b09b99`
still shows ORDER 001/002 `status: new` — the manager's new→done flip is pending, the
normal post-execution lag (the lane reports done= in its status; the manager flips
after seeing it). Manifest games-plugins row @ superbot `7c6278e` still records lane
HEAD `adb5f9b`/kit v1.2.0/"ORDER 001 pending — boot-gating"/"v1.7.0 `adopt --lane` is
the fix" — now a full program-phase behind reality (datapoint 12 in the heartbeat's
staleness series).*

**1. What is this really?**
A boot-pack: maintenance work scoped to ride a specific one-shot event ("one bounded PR
at the lane's next boot") — kit upgrade v1.2.0→v1.7.0 plus `adopt --lane` ×2 to declare
the hand-split per-lane heartbeats to the gate. Probed at HEAD it is really a RACE the
boot won: the upgrade happened two versions past the capture's target (lane PRs
#22/#23), and the boot did not *declare* the two-writer split — it **dissolved** it
(Q-0267 single-seat unification, lane PR #24), which the capture's framing never
priced as an outcome.

**2. What is the possibility space?**
At capture time, three shapes: (a) as written — upgrade + `adopt --lane` ×2 declaring
both files in `heartbeat_files`; (b) upgrade-only, leaving the split undeclared (the
flagged two-writer ⚑ persists); (c) what actually happened — upgrade FIRST, then the
boot session unifies the seats instead, making the default
`heartbeat_files: ["control/status.md"]` correct with zero adopt-lane work. Post-boot
the space collapses: (a) is now actively WRONG (`adopt --lane mining` would plant
`control/status-mining.md` declarations for files banner'd "GEN-1 HISTORY … do not
resurrect"), (b) already happened without incident, (c) is live. The only residual
shape worth checking — a `heartbeat_files` misconfiguration left behind by the
unification — was checked: the config matches the unified reality. Nothing survives.

**3. What is the most advanced capability reachable by the simplest implementation?**
The null slice. At capture time: one `bootstrap upgrade` + two `adopt --lane` runs
bought gate-enforced per-lane heartbeat visibility (missing lane = strict RED). Today
the same capability — the gate seeing the repo's real heartbeat scheme — is ALREADY
delivered by a strictly simpler configuration: one seat, one status file, the kit
default. There is nothing left to implement; the most advanced remaining move is this
probe report making the expiry explicit so no future wake re-derives it.

**4. What breaks it?**
Time already did — three distinct breaks, worth naming because they are a class:
**(i) premise expiry** — "runs the fleet's oldest live kit pin (v1.2.0)" was falsified
by lane PRs #22/#23 hours after capture; **(ii) premise inversion** — the idea assumed
the two-writer split would persist into gen-2 and need declaring; the boot instead
archived it (Q-0267), flipping the proposed fix from protective to regressive; **(iii)
grounding staleness laundering** — the capture's manifest-row grounding ("kit v1.2.0
(v1.7.0 `adopt --lane` is the fix)") is STILL what the manifest says at superbot
`7c6278e`, so re-reading the capture's own source would re-confirm the dead premise —
only a direct lane read (ls-remote + clone at `9b09b99`) breaks the loop. A future
executor acting on the manifest row or this capture without a HEAD check would undo a
deliberate lane decision.

**5. What does it unlock?**
As captured: nothing anymore — its unlock (safe two-Project cohabitation on a declared
heartbeat scheme) was mooted when cohabitation itself ended. As a datapoint it unlocks
three cheap lessons: boot-pack ideas need expiry-aware probe ordering (probe
`before <event>` captures ahead of non-expiring heads once the event is imminent —
this idea sat ~12h and expired); the kit's host-carve-out protection worked in anger
(ORDER 001's fix landed in `tests.yml` and SURVIVES future upgrades by construction —
the PR #46 stale-anchor risk did not materialize); and the manifest staleness series
gains its sharpest instance yet (a row prescribing a fix for a state the lane exited a
program-phase ago).

**6. What does it depend on?**
Nothing open — every dependency resolved itself, and the ORDERING resolved correctly:
the kit upgrade (lane PRs #22/#23) landed BEFORE ORDER 001's execution (lane PR #24),
so the pytest step had already been relocated to the host-owned `tests.yml` carve-out
when the fix was written, and the fix landed there — NOT in the kit-owned
`substrate-gate.yml` where the order's stale anchor pointed and where any edit is
clobbered by the next `bootstrap upgrade` (the idea-engine PR #35 clobber lesson; the
v1.7.x carve-out relocation is the protection, per `tests.yml`'s own header). Had the
sequence run the other way — fix first at the stale anchor, upgrade second — the
upgrade would have silently deleted the P0 fix. The gen-2 boot (externally fired) and
ORDER 002's self-arm (routine live at 23:47:02Z) close the remaining dependencies.

**7. Which lane should build it?**
No lane — there is nothing to build. superbot-games already executed the superset and
made the capture's specific fix wrong-by-inversion. The only actor with residual work
is the **fleet manager**: flip the lane's inbox ORDER 001/002 new→done (the lane
reports both done), and refresh the manifest games-plugins row (still
`adb5f9b`/v1.2.0/boot-gating — datapoint 12); separately, the PR #46 census-parity
fold-in remains UNCONSUMED (the executor kept the hand-raised floor, already raised
once at 121→147 within hours — the predicted chore, lived), a lane follow-up the
manager may fold into its next games routing, not this idea's concern.

**8. What is the smallest shippable slice?**
This probe report and the forward-only state flip captured → parked(overtaken) — the
null slice, shipped as documentation so the section's trail records WHY the idea died
(the boot it targeted fired first) rather than leaving a captured head that a future
wake re-probes or, worse, executes against the manifest's still-stale prescription.
Explicitly NOT in any slice, anywhere: running `adopt --lane` on superbot-games.

**Recommendation: park** — overtaken: the lane's own gen-2 boot executed or dissolved
every element of the capture's one bounded PR before the probe ran (kit v1.7.1, split
archived by Q-0267 single-seat unification, `heartbeat_files` already matching, orders
executed), and the sole proposed mechanism (`adopt --lane`) would now resurrect the
exact scheme the lane deliberately retired.
