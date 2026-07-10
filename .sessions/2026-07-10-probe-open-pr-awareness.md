# Session — fleet slice: open-PR-awareness probe (websites)

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-10 ~23:15Z (worker slice, dispatched by the
> continuous-mode coordinator per Q-0265)

## Scope

Probe `ideas/websites/open-pr-awareness-at-wake-2026-07-10.md` (the ripest websites
head per the PR #37 handoff and the heartbeat's held priority): full battery, verdict
landed on the file, state advanced forward-only, fleet-generic routing cross-linked to
substrate-kit. No outbox append expected (probe first, earn second).

## What this session did

- Claimed the surface (`claims/slice-probe-open-pr-awareness.md`, flat filename per
  `claims/README.md`; cleared in this close-out commit).
- **Probed** open-pr-awareness-at-wake — the FIRST websites-section probe. Verdict:
  **park(build-direct)** — no simulator question (a wake-ritual read step is proven by
  lived usage plus one golden classifier table; the one genuinely open question,
  per-seat PR-tooling variance, is already PROPOSAL 005's battery, queued at sim-lab
  as INTAKE 005), and the build belongs to lanes this repo does not write. State
  advanced forward-only `captured → parked(build-direct — …)`; report appended, header
  and body untouched.
- **Grounding re-verified live first** (the PR #25 lesson): websites HEAD
  `8dc5ec2f2c28904423ab046e5eaff17870c194b5` via `git ls-remote refs/heads/main` at
  23:04Z — AHEAD of the harvest pin `144dfce`, canonical doc byte-identical at both
  SHAs (equal sha256, `d4e4c2a6…`), so the Grounding pin cites HEAD faithfully. Both
  cited lived failures transport-verified at HEAD: PR #63's merge commit `507be5a` in
  main history; the stale "Not yet merged" ledger passage recoverable verbatim at
  `docs/planning/queue-state-2026-07-09-winddown.md@507be5a` with its 20:00Z
  correction (PR #64) at HEAD. Gap confirmed live: the wake ritual
  (`docs/project/routine-prompt.md` WAKE line, `project-instructions.md`
  § ROUTINE-FIRED) still carries NO open-PR step, while three `claude/*` branches plus
  `manager/control-plant` sit with commits not on main.
- **Routing split (PR #29-shaped, weight on the lane):** websites builds its own
  ritual step build-direct (manager fan-in relay via the heartbeat notes; lane can
  self-serve at its next wake); substrate-kit owns the fleet-generic convention — the
  kit-planted `control/README.md` wake ritual's missing third leg (orders → sections →
  branches), NOT the zero-network `session-start` hook. Third Cross-links entry landed
  on `ideas/substrate-kit/README.md` (PR #17 rule).
- **Sim-lab pull recorded (backpressure released):** PROPOSALs 004+005 pulled at
  22:35Z — INTAKE 004/005 at sim-lab HEAD `bc6e0fe`; VERDICT 004 already finalized
  (needs-more-evidence: phi=0 rate-only invariant gate-PASS, magnitude pending
  telemetry; sim-lab PR #13, merge `4d84037`); INTAKE 005 (capability self-awareness)
  queued next, EAP window ends 2026-07-14. Outbox: 5 proposals, ZERO unpulled. This
  slice appended nothing (earn-rate bar held).
- **No outbox append, no proposal** — the verdict is park.
- **📊 Model:** fable-5 · high · one probe + cross-link + docs ceremony (no code
  changes, no proposal — park verdict)

## 💡 Session idea

**Idea-engine should adopt the open-work sweep itself.** This very session discovered
sibling PR #38 (superbot re-harvest) only via an ad-hoc `git ls-remote` — the exact
ad-hoc move the probed idea wants ritualized. The built-here-sized version of the idea
just probed: ONE line in the wake ritual (or a sixth report-only preflight `CHECKS`
entry listing remote branches ahead of main — anchors: `scripts/preflight.py::CHECKS`
constant plus a small `--open-work` self-invoked mode per the `--gate-wiring` pattern;
test = branch a throwaway ref, confirm it lists). A one-line capture, distinct from
the websites/kit builds routed by the probe.

## ⟲ Previous-session review

PR #36 (gate-wiring self-check; card `.sessions/2026-07-10-preflight-gate-selfcheck.md`)
promised: a fifth `CHECKS` entry `--gate-wiring` that REDs when the kit-owned gate
loses the PR #18 wake-preflight step, worst-exit conventions honored, gate file
byte-untouched. Verified on this tree: `python3 scripts/preflight.py` runs green with
ALL FIVE checks PASS including `gate-wiring: OK — .github/workflows/substrate-gate.yml
non-control lane runs scripts/preflight.py`, and the gate file still carries the PR
#18 step at the PR #18 position (`run: python3 scripts/preflight.py` guarded by
`if: steps.lane.outputs.control_only != 'true'`, lines 84–96) — both byte-anchors the
tripwire matches are intact. Its 💡 (step-anchor drift lint: the byte-anchors must
co-edit with any deliberate gate-step rewording) remains a captured follow-up in the
heartbeat's ripest list — not consumed here (this slice is a probe, disjoint surface).
Its handoff named superbot re-harvest among ripest slices — consumed by sibling PR #38
(merged to main before this branch cut). All checks out; nothing contradicted.

## Handoff → next wake

Claim cleared, no proposal in flight, nothing to babysit. Manager fan-in material now
on the heartbeat: open-pr-awareness parked(build-direct) routing (websites ritual step
+ kit-planted convention) and VERDICT 004 (needs-more-evidence, sim-lab PR #13
`4d84037`). Ripest next: websites remaining heads (own-heartbeat parse self-check,
review-queue row auto-check), public-leaderboards probe, freshest-wins one-liner,
`upgrade --apply-docs` follow-up, and this card's 💡 (the built-here open-work sweep).
