# Replay start anchor — delete the bisected frame-offset class from the proof harness

> **State:** captured
> **Class:** process · **Target:** `menno420/gba-homebrew`

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
