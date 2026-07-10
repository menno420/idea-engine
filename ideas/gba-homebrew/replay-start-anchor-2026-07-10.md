# Replay start anchor — delete the bisected frame-offset class from the proof harness

> **State:** parked(build-direct — a deterministic lane-harness slice the lane's own CI proves end-to-end on merge; no parameter/design question left for sim-lab to settle; manager routes it to the lane directly)
> **Class:** process · **Target:** `menno420/gba-homebrew`
> **Grounding:** https://github.com/menno420/gba-homebrew@bc73da70b5e46995dc63319cfd4b3bf997a886c9 · fetched 2026-07-10T21:46Z (manifest row: behind)
> **Sequence:** before the ORDER 001 concept pick converts to a game-2 harness transfer — window OPEN at probe time (the pick is still the lane's ⚑ needs-owner @ `bc73da7`; fixing the offset class pre-transfer fixes it once, not per-game)

## Problem

Every scripted-input proof in the lane inherits a title-screen frame offset that is
**bisected, not derived** — and it has moved three times in three sessions (+4 at
the session-5 title screen, +5 when session-6 audio+window init grew the run-start
stall, back to +4 when session-7's sliding-window rebake got two frames faster).
The session-7 card adds a sharper warning: the bisect pass plateau is
**non-contiguous** (validate the full assert suite, never reason from lag alone),
and the per-frame deep-run script must be **re-recorded, not shifted**, on any
timing change. Net effect: every timing-adjacent PR pays a re-bisect tax, three
review-queue rows (#16, #20, #23) carry standing "re-verify the offset" duties, and
the harness — the explicitly transferable half of the lane — exports this tax to
every future game on the scaffolding.

## Idea

Replace boot-relative frame counting with an **event-anchored start sync**: the
harness already proves state via memory watches on the telemetry hook
(`gl_audio_hook` slots, exact-count and numeric-depth asserts in CI), so let the
replay runner wait for a "run started" telemetry value and begin script playback
at that frame instead of at boot+N. Init-time changes (audio, window, rebake speed)
then stop invalidating recorded inputs; the offset constant, the bisect procedure,
and the non-contiguous-plateau guard all become deletable. Canonical and deep-run
scripts re-anchor once and never move again.

## Grounding

- Offset history +4 → +5 → +4, all bisected; "the deep-run script … must be
  RE-RECORDED, not shifted, if timing changes"; non-contiguous plateau guard:
  lane [`control/status.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/control/status.md) (notes + last-shipped)
  and concept-doc polish-pass entries in
  [`docs/concepts/session-1-concepts.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/docs/concepts/session-1-concepts.md).
- Standing re-verify duties on the offset: rows #16, #20, #23 in
  [`docs/review-queue.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/docs/review-queue.md).
- Watch/telemetry infrastructure already in CI (hook slots 4–6 are a proof-surface
  contract): same status pin.

**Why now:** the offset moved on three consecutive sessions — and the concept pick
is about to transfer this harness to a second game; fixing the class before the
transfer fixes it once instead of per-game.

## Probe report (v0, 2026-07-10)

*Probed 2026-07-10T21:50Z. Timeliness first (the last probe head, PR #25, died on a
closed window): the lane's HEAD is STILL the capture pin — `git ls-remote` returns
`bc73da7` for `refs/heads/main` at 21:45Z, identical to the capture's grounding — so
every pinned citation below is also the live state. Live checks: the harness is still
pre-game-2 (the ORDER 001 concept pick is still the lane's open ⚑ needs-owner,
`control/status.md` @ `bc73da7`, 07:14:30Z write — "Lumen Drift SCOPE-COMPLETE …
UNBLOCKS: the next build target"); the offset class is still live (the canonical replay
was re-bisected +5 → +4 in lane PR #23 — status `notes:` + the offset-history comment
block in `.github/workflows/headless-boot.yml` @ `bc73da7`: "+3 and +5 drop the shard
grabs … +4 is the passing offset nearest the measured lag"); and review rows #16, #20,
#23 (`docs/review-queue.md` @ `bc73da7`) still carry the standing "offset is BISECTED —
re-verify on any timing-adjacent change" duties. The window the capture named is open.*

**1. What is this really?**
A harness-semantics change, not a game change: move the replay runner's time origin from
"emulator boot" to "the run actually started," using proof surfaces the CI already
watches. Today every script line is boot-absolute (`--keys 20-24:START`,
`--assert-watch 2261:hook:6:eq:95` — `headless-boot.yml` @ `bc73da7`), so any init-time
cost change shifts ALL of them at once, and the correction constant is bisected, not
derived (+4 → +5 → +4 across sessions 5/6/7). The telemetry to anchor on is already a
CI contract: `gl_audio_hook` slot 0 flips 0→1 exactly at run start (the workflow itself
asserts `15:hook:0:eq:0` then `30:hook:0:eq:1`), and slots 4–6 carry position/depth
(row #23 names them "a proof-surface contract"). This is deleting a bug class by
re-basing coordinates, the classic hardware-testbench trigger-on-event pattern.

**2. What is the possibility space?**
Three design axes. **Anchor event:** hook slot 0 (start-confirm trigger, fires once at
run start) vs depth-telemetry-validity (slots 4–6 leaving reset state) vs a dedicated
"run started" hook value the game writes — slot 0 exists today and is already asserted
in CI, so it is the zero-new-ROM-code option. **Anchor scope:** anchor only in-run input
(boot→START stays absolute — historically stable: "START press unchanged at frame 20"
across all three offset moves) vs multi-segment anchoring (each run in a multi-run
script gets its own anchor — the SRAM proof's two boots would each anchor
independently). **Syntax:** a runner flag (`--anchor hook:0:eq:1` rebasing every later
frame number) vs an in-script directive; the flag reuses the existing
`--watch`/`--assert-watch` grammar wholesale. Beyond the capture: the same mechanism
generalizes to any future game on `games/common/` scaffolding — the anchor becomes part
of the transferable harness contract instead of a per-game bisected constant.

**3. What is the most advanced capability reachable by the simplest implementation?**
One flag in `tools/headless-screenshot.py` — "wait until watched value satisfies
condition, then treat that frame as 0 for every subsequent `--keys`/`--shot`/
`--assert-text`/`--assert-watch`" — yields: (a) init-time changes (audio, window,
rebake speed — all three observed causes) stop invalidating recorded inputs; (b) the
offset constant, the bisect procedure, and the non-contiguous-plateau guard become
deletable prose; (c) the session-7 card's harshest rule — the per-frame deep-run script
"must be RE-RECORDED, not shifted, if timing changes" — collapses to "re-anchor once,
never again" for the init-drift class; (d) the harness transfers to game 2 with
"emit a run-start telemetry value" as its only per-game obligation. The runner already
reads watched memory every frame, so the mechanism is a comparison plus an offset
variable applied at frame-number lookup.

**4. What breaks it?**
- **Mid-run timing drift is NOT covered.** A start anchor kills init-relative drift —
  the class actually observed three times — but a future change that adds an in-run
  overrun still shifts every post-overrun frame. The lane already has the tripwire
  (loop-tick watch, slot 7: "lag is constant 19 from frame 24 to the end"); the report
  must not oversell the anchor as timing immunity.
- **Pre-anchor input still needs absolute frames.** The canonical script holds RIGHT
  from frame 4 and presses START at 20–24, all before any run-start event exists; the
  boot→START segment stays boot-relative (empirically stable so far) or gains its own
  title-visible anchor. A sloppy implementation that anchors EVERYTHING breaks the
  scripts it is meant to save.
- **One-frame ambiguity at the anchor.** Watches sample once per frame; "the frame where
  slot 0 first reads 1" vs "the frame after" is a fencepost that aliases exactly like
  the bisect plateau did. The convention must be written down once and asserted in CI
  (an anchored assert at the known first-input frame), or the bug class returns wearing
  the fix's clothes.
- **Anchor-surface renumbering.** Row #23 already warns hook-slot renumbering breaks CI;
  anchoring adds one more consumer of slot 0's meaning. Same contract, higher stakes.
- **Sunk re-anchor cost.** Existing scripts were recorded boot-absolute; the migration
  PR must re-express canonical + deep-run + SRAM scripts in anchored form and prove
  byte-identical behavior via the existing assert suites — a one-time cost the capture
  correctly prices as "re-anchor once and never move again."

**5. What does it unlock?**
Deletes a measured recurring tax: three re-bisects in three sessions, three standing
review-queue duties (#16/#20/#23 all carry "re-verify the offset"), and a documented
re-record obligation on the 2264-frame deep-run script. Unblocks clean harness transfer
at the concept pick — the explicitly transferable half of the lane stops exporting its
worst convention to game 2 (and to Track A, if the pokemon-mod-lab lane ever adopts the
runner). Secondary: recorded proofs become robust documentation — a future session
changing init code no longer needs the bisect ritual to keep CI green, which directly
cheapens every polish/perf slice the owner's pick commissions.

**6. What does it depend on?**
- The lane's existing telemetry/watch infrastructure — `gl_audio_hook` slots + the
  runner's per-frame watch sampling (`--watch hook:gl_audio_hook:4`/`:8` in CI today) —
  all shipped; slot 0 as run-start signal needs zero new ROM code.
- mGBA determinism under the pinned stack (mgba==0.10.2 + Butano 21.7.1) — the premise
  of the whole proof harness, already relied on by every committed script.
- The hook-slot proof-surface contract staying stable (review row #23) — the anchor
  becomes another consumer of it.
- Sequencing only: maximum value lands if it merges BEFORE the concept-pick transfer
  (Sequence line above; the pick is owner-gated, timing unknown, window open at probe
  time). No cross-lane dependency: everything it touches lives in `menno420/gba-homebrew`.

**7. Which lane should build it?**
`menno420/gba-homebrew`, alone — the runner (`tools/headless-screenshot.py`), the
workflow, the scripts, the telemetry hooks, and the review-queue duties it retires are
all lane-local, and the lane has self-merge + the dispatch-tier proof jobs to verify the
change end-to-end. Not sim-lab: there is no parameter to sweep and no contested design —
the only open choices (anchor event, fencepost convention) are settled by construction
during implementation, and reproducing the evidence would cost sim-lab the entire
devkitARM+mGBA toolchain to learn what the lane's own CI proves for free on the PR.

**8. What is the smallest shippable slice?**
One lane PR: (1) add `--anchor <name>:<idx>:<op>:<val>` to the runner (reusing the
`--assert-watch` condition grammar), rebasing all subsequent frame numbers to the first
frame satisfying it, with the fencepost convention documented in the flag's help; (2)
re-express the canonical, deep-run, and SRAM proof invocations anchored on
`hook:0:eq:1`, keeping the boot→START segment absolute; (3) prove it by the existing
assert suites passing unchanged in the dispatch job, plus one deliberate init-cost
perturbation build (add a frame of boot stall, show proofs still green) as the
class-kill demonstration; (4) delete the offset-history comment/constant and convert
rows #16/#20/#23's re-verify duties to "retired by anchor" notes. CI green on (3) IS the
acceptance test — no external evidence needed.

**Recommendation: park** — build-direct: the verdict is "worth building, nothing left to
probe or simulate" — a lane-local, self-proving harness slice (its own CI is the
acceptance test, Q8) with no parameter question for sim-lab; the manager should route it
to `menno420/gba-homebrew` directly, ideally sequenced before the concept-pick transfer
while the window is open.
