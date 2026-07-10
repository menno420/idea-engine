# Concept-pick bring-up pack — pre-stage day-0 plans so the pick converts to build the same session

> **State:** parked(build-direct — a lane-local docs pack the lane's standing default already authorizes; no reproducible-evidence question for sim-lab — the validating event is the post-pick build session itself; manager routes it to the lane while the pick window is open)
> **Class:** process · **Target:** `menno420/gba-homebrew`
> **Grounding:** https://github.com/menno420/gba-homebrew@16e64d7c92ff8fd1ee96eeb3194fae26b14b86ee · fetched 2026-07-10T22:05Z (manifest row: behind)
> **Sequence:** before the ORDER 001 concept pick lands (any signal) — window verified OPEN at probe time: the pick is still the lane's open ⚑ needs-owner @ HEAD `16e64d7`, only kit-upgrade commits since the capture pin `bc73da7`; the pack is worthless the session after the pick

## Problem

The lane's next build target is owner-gated (⚑ concept pick: keep investing in
Lumen Drift vs start Clockwork Courier vs Shoal), and the pick "can land as any
signal (inbox order or PR comment)" — i.e. at an arbitrary moment, into a lane
that wakes cold. The concept doc's scope estimates date from session 1, **before**
seven sessions built the transferable scaffolding (`games/common/` input /
kinematics / collision / run-state / stage / save / light-window / audio-hook
headers plus the harness scripting, text/watch assertions, savefile persistence,
and route recording). When the pick lands, the first session burns on re-planning:
which estimates still hold, what the scaffolding already covers, what increment 1
actually is now.

## Idea

One committed bring-up pack, one page per fork arm, written **while the pick is
pending**: for Clockwork Courier and Shoal, a day-0 increment-1 plan against the
scaffolding as it exists (which common headers apply unchanged, which harness
proofs run on day 0, what is genuinely new per concept, revised
sessions-to-first-playable); for the keep-investing arm, the concrete
new-scope-needs-owner-say-so options (e.g. the seeded-cave capture,
[`seeded-cave-runs-2026-07-10.md`](seeded-cave-runs-2026-07-10.md)). The pick then
converts to build work the same session with zero re-planning — pure rebuild pace
under Q-0259. Fits the lane's own standing default ("groom the backlog — never
idle") for a between-orders session.

## Grounding

- ⚑ concept pick as a "pure fork" + the verbatim transferable-scaffolding list
  ("everything generic transfers …"): lane
  [`control/status.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/control/status.md).
- Session-1 estimates (Lumen Drift's later CONFIRMED at 2 sessions — evidence the
  format predicts well when refreshed against reality):
  [`docs/concepts/session-1-concepts.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/docs/concepts/session-1-concepts.md).
- Standing default ("advance … keep the loop honest, groom the backlog — never
  idle"): lane [`control/inbox.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/control/inbox.md).

**Why now:** with the polish list exhausted the lane has no queued build target —
this is the highest-value between-orders work precisely during the window before
the pick lands, and worthless the session after.

## Probe report (v0, 2026-07-10)

*Probed 2026-07-10T22:05Z. Timeliness FIRST (this capture names its own decay — "worthless
the session after" the pick lands — the exact PR #25 failure mode): the lane's HEAD has
MOVED since capture (`git ls-remote` = `16e64d7` vs the capture pin `bc73da7`), so the
delta was audited before judging. The only commits between the pin and HEAD are lane
PR #27's substrate-kit upgrade v1.7.0 → v1.7.1 (commits `979b161`/`962cdfe`/`64a81d8`,
21:49–21:53Z — `.substrate/`, `bootstrap.py`, `substrate.config.json` only); the four
pick-relevant surfaces — `control/status.md`, `control/inbox.md`,
`docs/concepts/session-1-concepts.md`, `docs/review-queue.md` — are byte-identical
between `bc73da7` and `16e64d7` (raw-path fetch + `cmp`). No pick has landed by any
commit-visible signal: no pick ORDER in the inbox @ HEAD, the concept doc still reads
"awaiting owner pick" / "the pick is still pending," and the ⚑ concept-pick ask is still
open in the lane heartbeat. Residual blindness stated honestly: a pick delivered as a PR
comment that the lane has not yet acted on would be invisible from this repo
(GitHub MCP is scoped to `menno420/idea-engine`; `api.github.com` is proxy-walled) —
every surface this repo CAN read says the window is OPEN.*

**1. What is this really?**
Latency-hiding by speculative planning: the owner's pick is a 3-arm fork whose per-arm
planning work is pick-independent, so the lane does that work inside the owner-latency
window instead of after the signal — a committed branch table mapping each arm to a
day-0 increment-1 plan against the scaffolding as it exists NOW (post-session-7), not as
of session 1. Pure process/docs artifact, zero game code. The deeper half: it repairs the
pick's own information. The owner is currently choosing on session-1 estimates that
predate the seven sessions that built `games/common/` and the proof harness; refreshed
sessions-to-first-playable per arm changes the cost side of the decision itself.

**2. What is the possibility space?**
Five axes. **Arm coverage:** the two transfer arms only, vs all three (the keep-investing
arm is cheap — enumerate the already-captured owner-say-so options, e.g.
`seeded-cave-runs-2026-07-10.md`). **Depth:** one thin page per arm (increment-1 plan +
revised estimate) vs full multi-session roadmaps — depth must stay thin because ≥2 of 3
arms die by construction. **Freshness protocol:** write-once vs pinned-at-scaffolding-sha
with a mandatory at-pick re-verify step (the pack must state what invalidates it).
**Placement:** new `docs/concepts/` bring-up pages vs appending to
`session-1-concepts.md` — the lane's call; either way the heartbeat's ⚑ pick ask should
point at the pack so the arriving signal converts immediately. **Generalization:** the
pattern — a pending-decision bring-up pack that pre-stages the decision-independent work
of every arm while an owner gate is pending — is fleet-reusable for any multi-arm ⚑ with
idle lane capacity; a future doctrine capture, out of scope here.

**3. What is the most advanced capability reachable by the simplest implementation?**
One between-orders lane docs PR (three thin pages + one heartbeat pointer) buys three
things at once: (a) pick→build conversion in the same session — the signal maps to a
committed increment-1 plan whose day-0 harness proofs are named in advance; (b) a
better-informed pick — per-arm costs refreshed against post-scaffolding reality, using an
estimate format with a live calibration datapoint (Lumen Drift's 2-sessions-to-playable
estimate CONFIRMED by measurement); (c) a scaffolding-transferability audit as a free
byproduct — "which common headers apply unchanged, which harness proofs run on day 0" is
the transfer contract of `games/common/` written down and checked per concept BEFORE any
transfer happens, including whether game 2 would inherit the boot-relative frame-offset
convention (the replay-start-anchor build-direct head).

**4. What breaks it?**
- **The window race.** Worthless the session after the pick lands (the capture's own
  words): probe→route→build is racing an arbitrary owner signal, and every step of
  routing latency risks total loss. Loss is bounded (one docs session) but real.
- **Staleness between pack-merge and pick.** Further lane sessions decay it — the routed
  replay-start-anchor slice in particular would change the harness contract the plans
  cite. The pack must be pinned at a scaffolding sha and carry an explicit at-pick
  re-verify step, or it becomes the same stale-estimates problem one layer up.
- **Speculative waste by construction.** At least 2 of 3 arm plans are discarded.
  Acceptable only because the arms number three, the pages stay thin, and the lane is
  otherwise idle between orders (standing default: "groom the backlog — never idle").
- **Confidently-wrong plans.** Clockwork Courier and Shoal have zero built code; day-0
  plans can misjudge the genuinely-new systems, and the estimate calibration is n=1 and
  same-game. Mitigation is honesty inside the pack (per-arm risk lines), not more
  planning.
- **Anchoring.** A committed plan can bias the post-pick session into executing a stale
  plan instead of re-verifying; the re-verify step must be part of the pack's own
  contract, not left to session discipline.

**5. What does it unlock?**
The lane's next N build sessions start one session earlier — pure rebuild pace under
Q-0259, which is the whole point of the games completion wave. The owner picks on current
costs instead of session-1 costs. The `games/common/` transfer contract gets its first
written per-consumer check. And the fleet gets its first live instance of the
pending-decision bring-up-pack pattern to learn from before anyone proposes it as
doctrine.

**6. What does it depend on?**
- The pick window staying open (Sequence line) — the sole hard dependency,
  owner-controlled, timing unknown.
- The scaffolding state at a pinned lane sha — the `games/common/` headers + harness
  features the lane heartbeat's transfer note names verbatim.
- Lane capacity under the standing default — already authorized between orders; no new
  ORDER is strictly required for the lane to self-serve this.
- Sequencing interplay, not dependency: if replay-start-anchor (park(build-direct), this
  repo's PR #27 probe) lands first, the packs cite the anchored harness contract and
  game 2 never inherits the offset class — writing the pack after (or jointly with) the
  anchor slice is strictly better ordering. No cross-lane dependency: everything it
  touches lives in `menno420/gba-homebrew`.

**7. Which lane should build it?**
`menno420/gba-homebrew`, alone: the plans must be written against the lane's own tree,
with the context of the sessions that built the scaffolding, and land as lane docs — this
repo cannot write lane files (Q-0260) and holds strictly less context than the lane. Not
sim-lab: there is no reproducible-evidence question to settle — plan quality has no
simulator, and its validation event is the post-pick build session itself (did
increment 1 land in roughly the planned session count?), which is real-world evidence no
simulation can pre-produce.

**8. What is the smallest shippable slice?**
One lane PR under the standing default: (1) per transfer arm (Clockwork Courier, Shoal)
one thin page — common headers that apply unchanged · harness proofs that run on day 0 ·
genuinely-new systems · revised sessions-to-first-playable in the lane's calibrated
estimate format; (2) the keep-investing arm as an options list (seeded-cave capture
linked), each option flagged new-scope-needs-owner-say-so; (3) every page pinned at the
scaffolding sha with an at-pick re-verify line; (4) the lane heartbeat's ⚑ concept-pick
ask updated to point at the pack so any pick signal converts immediately. Done-when:
pack merged + ⚑ pointer live while the pick is still pending.

**Recommendation: park** — build-direct: a lane-local docs slice the lane's standing
default already authorizes, with no reproducible-evidence question for sim-lab (its
validation event is the post-pick build itself); the manager should route it to
`menno420/gba-homebrew` now, sequenced jointly with the replay-start-anchor build-direct
head — both race the same open pick window.
