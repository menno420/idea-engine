# Session — replay-start-anchor probe (gba-homebrew): battery v0 → park(build-direct)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 (worker slice, dispatched by the coordinator under
> continuous-chaining mode per Q-0265)

## What this session did

- Claimed `ideas/gba-homebrew/` (`claims/probe-gba-homebrew-replay-start-anchor.md`, flat
  filename per `claims/README.md`; cleared in this branch's final commit).
- **Timeliness check FIRST** (the PR #25 lesson — probe the window before the idea): lane
  HEAD via `git ls-remote` = `bc73da7`, IDENTICAL to the capture pin — the capture's
  grounding is the live state. Verified live via public raw @ `bc73da7`: harness still
  pre-game-2 (concept pick still the lane's open ⚑ needs-owner in `control/status.md`,
  07:14:30Z write), offset class still live (+5 → +4 re-bisect in lane PR #23; offset-history
  comment block in `.github/workflows/headless-boot.yml`; re-verify duties on
  `docs/review-queue.md` rows #16/#20/#23). Manifest row @ superbot `655e0fe` is behind
  (records lane HEAD `b607365` + kit v1.6.0) — datapoint 7 for the staleness list.
- **Probed (battery v0):** `ideas/gba-homebrew/replay-start-anchor-2026-07-10.md` —
  event-anchored replay start on the existing `gl_audio_hook` telemetry (slot 0 flips 0→1 at
  run start, already asserted in the lane's CI), killing the thrice-re-bisected boot-relative
  frame-offset class before the harness transfers to game 2.
- **Verdict: park(build-direct)** — worth building, nothing left to probe or simulate: the
  smallest slice (Q8: one `--anchor` flag in `tools/headless-screenshot.py` + re-anchored
  canonical/deep-run/SRAM scripts + a deliberate init-perturbation build as the class-kill
  demo) is lane-local and self-proving — the lane's own dispatch-job assert suites ARE the
  acceptance test. Not sim-ready: no parameter to sweep, no contested design; sim-lab would
  need the whole devkitARM+mGBA toolchain to learn what lane CI proves free on the PR.
  State advanced forward-only captured → parked(build-direct — …); Grounding + Sequence
  header lines added (Sequence window OPEN: pick still owner-gated); section README index
  updated.
- **No PROPOSAL** appended: not sim-ready — sim-lab queue (001→002→004 behind VERDICT 001)
  gains nothing from a build-direct routing; the manager reads the verdict on the idea file
  and this heartbeat's fan-in note.

**📊 Model:** fable-5 · high · docs-only (probe report + index line + card + heartbeat; no code)

## 💡 Session idea

The probe found the anchor's one real residual risk is a **fencepost convention** (first
frame satisfying the condition vs the frame after — the same aliasing that made the bisect
plateau non-contiguous). Grooming-sized rule for the battery: when a probe recommends a
mechanism that replaces a bisected constant, Q4 must name the new convention that could
regrow the old bug class ("the fix's clothes" check). Class: process, target
`menno420/idea-engine` (one README sentence under the battery section). Capture in a future
generate slice if still believed.

## ⟲ Previous-session review

Consumed the PR #25 card + heartbeat handoff: the held priority order named
replay-start-anchor as the next probe head, and its card's structural lesson — a
time-boxed capture can die between capture and probe — was applied here as a
timeliness-check-first discipline (this time the window was verified OPEN: lane HEAD
unchanged at `bc73da7`, pick still pending, so the probe judged a live idea, not a corpse).
Friction inherited and confirmed: `api.github.com` proxy-walled (the lane's own status
carries the same wall) — GitHub MCP is scoped to `menno420/idea-engine` only, so lane
live-state came via public raw + `git ls-remote` (both worked; ls-remote is the cheap
HEAD-sha trick the raw path can't give you — worth reusing). Manifest-staleness list
grows to seven datapoints (gba-homebrew row now two layers behind: manifest < lane
heartbeat < lane tree).

## Handoff → next wake

Inbox first (verify still empty at HEAD). Outbox depth unchanged (4 proposals; sim-lab
queue 001→002→004, VERDICT 001 done on 003) — this probe parked, nothing appended. The
held priority list is now CONSUMED (both heads probed: post-holdout-reseal → park,
replay-start-anchor → park(build-direct)). Ripest next slices: the sized superbot
re-harvest (2 new docs + 1 unmarked index entry, pre-instrumented via
`scripts/check_harvest.py`), optional-line lint coverage (PR #21 card 💡), freshest-wins
one-liner (grooming round 3), and a generate pass over gba-homebrew's remaining captures
(concept-pick-bringup-pack is Sequence-tied to the same open pick window — probe it before
the pick lands or it decays like PR #25's head).
