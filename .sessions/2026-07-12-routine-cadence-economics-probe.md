# Session — generate+probe slice: routine-cadence economics sim (fleet)

> **Status:** `complete`

- **📊 Model:** fable-5 · generate+probe slice (one new `ideas/fleet/` head reasoned
  to fuller form + single-pass v0 probe + index row + this card; no code, no
  control/ writes — dispatch boundary)

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this card's
born-red first commit carries the `ideas/fleet/` collision flag per the
PR #222/#225/#243/#244 workflow convention. Scope: ONE new head —
`ideas/fleet/routine-cadence-economics-sim-2026-07-12.md` — plus the fleet
README index row and this card.

## What this session did

Generated and probed **routine-cadence-economics-sim**: a seeded discrete-event
replay-and-sweep answering which wake policy (failsafe cron cadence × pacemaker
chain policy × event-driven wakes) minimizes worker-turns per caught trigger at
acceptable catch latency — calibrated on THIS seat's own first ~14h heartbeat
trail. Verify-first, all run live this slice:

- **Corpus verified locally**: 13 `control/status.md` heartbeat commits in
  `fc0bab6..531b109` (`fc0bab6` #220 first wake 2026-07-12T00:05:51Z →
  `531b109` #258 12:00Z sweep). Real latency datapoints extracted: sim-lab
  ORDER 003 fm-filed 08:30Z, caught+executed at the 10:00Z failsafe (`65cd284`
  #256, evidence merged 10:31:24Z — ~90 min); fm restructure merges
  03:15–03:28Z, priced at the 06:0x sweep (#253 honest null @ `38f8857` —
  ~2.5–3h); pacemaker chain alive per-turn (`42f9642` next-fire 00:43Z,
  `d7c74d1` next-fire 02:54Z), paused under the honesty guard (`0fd8b65` #252,
  `f92bd26` #257).
- **Consuming decision verified live**: fm `docs/owner-queue.md` @ `171e24f`
  (ls-remote + raw fetch 2026-07-12T14:13–14:16Z) line 589: "post-EAP routine
  posture — HARD deadline: decide ≤2026-07-13; RECOMMENDED Option A", id
  `OQ-SITTING-0714-DECISIONS`.
- **Live cadence edit already queued blind**: v3.2 spec `30 1-23/2 * * *` vs
  live `0 */2 * * *` residual flag, `control/status.md` @ `531b109` line 10.
- **As-given (not verified)**: fm trigger telemetry 783 triggers @ `4111da4`;
  cost proxies (1 worker-turn per re-arm, 1 recon-worker per sweep).

Dedup swept (`rg -g '!bootstrap.py' -g '!.substrate'` over all of `ideas/` for
cadence/cron/trigger/wake/routine/pacemaker/heartbeat/polling/economics) — no
duplicate. Nearest neighbor: `ideas/superbot/usage-limit-aware-routines-2026-07-10.md`
(parked(routed) into the SAME ≤07-13 decision, but it is the limit-deferral
MECHANISM; this head prices the CADENCE choice — complementary, zero mechanism
overlap). Also ruled not-dup: recon-cadence-boundary-jitter (marker jitter),
external-cron-trigger + wake-resilience-fresh-session-rebind (scheduler/binding
reliability), carried-watch guard + archive-handoff ceremony (heartbeat content
/ trigger disposition, not frequency), open-work-preflight-sweep (a per-wake
cost component), parity-flip-cadence (work-output cadence, different axis).

Probe verdict: **sim-ready** (single-pass battery, panel not escalated). The
kill test was applied honestly: the sim earns its keep only via a knee or a
dominated policy; a smooth-frontier null is itself cheap, decision-closing
evidence. THE ONE QUESTION is stated machine-readably in the head's
Recommendation block. State left at `probed` — advancing to `sim-ready`
requires the outbox PROPOSAL, which is coordinator territory this slice cannot
write.

## Close-out

**Evidence:**

- ideas touched (2): `ideas/fleet/routine-cadence-economics-sim-2026-07-12.md`
  (NEW — state `probed`, class process, target sim-lab; Grounding pinned to fm
  owner-queue @ `171e24f` with pin annotation; Sequence: before the ≤2026-07-13
  sitting), `ideas/fleet/README.md` (index row added, fleet-README entry form)
- sessions touched (1): `.sessions/2026-07-12-routine-cadence-economics-probe.md`
- code touched: none · control touched: none (READ-ONLY `control/status.md`
  history reads for corpus grounding)
- git: branch `probe/routine-cadence-economics-sim` off main `531b109`
  (allowlisted prefix per the #253 branch-prefix lesson)
- verify: `python3 bootstrap.py check --strict` + `python3 scripts/preflight.py`
  (10/10 green) run before push.

**Judgment (the half only the session knows):**

- Decisions made: no D-entry. Two judgment calls, declared: (1) the head's cost
  axis is stated in worker-turn UNITS, never tokens/dollars — the fm
  honest-nulls doctrine says real costs are not agent-visible, so the sim
  question demands relative dominance, not absolute spend; (2) the pacemaker
  window is cited only at its VERIFIED endpoints (00:3x–02:5xZ alive) rather
  than the dispatch's broader 00:11–04:16Z, which was not independently
  confirmable from the heartbeat revisions read.
- Next session should know: the head is `probed` with recommendation
  `sim-ready` — the coordinator's outbox PROPOSAL (and the state advance to
  `sim-ready`) is the open next step; the done-when is in the head's final
  paragraph. Highest-leverage window: before the ≤2026-07-13 sitting.

## 💡 Session idea

The heartbeat trail turned out to be a machine-recoverable trigger-arrival log
only by ACCIDENT of prose discipline — every wake record happened to name its
trigger and catch times. A one-line structured token in the heartbeat grammar
(`wake: <ISO> · cause: failsafe|chain|event|order · caught: <n>`) would make
every seat's cadence corpus greppable by design, turning this sim's
hardest-to-reproduce input (trace reconstruction from prose) into a `git log
-p` one-liner — the cheap instrumentation half of the fleet-wide telemetry
loop the probe's Q2(iv) priced as premature.

## ⟲ Previous-session review

The carried-watch capture+probe pair (#247/#251) held up as the format
exemplar this slice leaned on: its probe's verify-first block structure
(specimen check → template check → target-ledger grep) transplanted cleanly to
this head's corpus/decision/doctrine legs, and its "state the verified
endpoints, not the claimed range" discipline directly shaped this slice's
pacemaker-window citation. One workflow improvement: its Grounding pins used
`git hash-object` blob verification — this slice's owner-queue pin rests on
ls-remote + raw-fetch-at-SHA agreement instead, which is weaker (no byte-level
blob hash recorded); future probes grounding on a single external file should
record the blob hash too.
