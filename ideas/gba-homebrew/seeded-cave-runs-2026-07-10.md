# Seeded cave runs — one parameter multiplies the endless cave into infinite caves

> **State:** captured
> **Class:** product · **Target:** `menno420/gba-homebrew`

## Problem

Polish pass 3 rebuilt the world so every row is a **pure function of the world
row** — an endless deterministic cave through a sliding 4KB window. Endless, but
singular: there is exactly ONE cave, forever. Past mastery every run replays the
same layout, echo bands cycle the same three section looks, and score-as-depth
converges on route memorization — the arcade loop's replay value has a ceiling the
architecture no longer requires.

## Idea

Thread a **run seed** through the pure row functions (phase/feature/waveform
offsets keyed by seed): one small parameter, multiplicative content. Unlocks in
rising order of ambition — seed shown on the death card and enterable on the title
screen (share a brutal cave with a friend), per-seed BEST in the existing SRAM
save, and a daily seed for a comparable community score. Determinism is preserved
per seed, so the entire proof harness keeps working: the canonical and deep-run
replays pin seed 0 (today's cave, byte-identical), and CI optionally adds one
assert on a second seed to prove divergence. Sequencing is explicit: this is
**new scope**, and the lane's ⚑ says new Lumen Drift scope needs owner say-so —
this capture exists so the "keep investing" arm of the pick is a concrete option,
not a blank. If the itch.io publish happens (venture-lab capture,
[`games-adjacent-candidate-three-2026-07-10.md`](../venture-lab/games-adjacent-candidate-three-2026-07-10.md)),
daily seeds are the natural retention hook for a PWYW listing.

## Grounding

- The pure-function rewrite that makes this nearly free ("every row is a pure
  function of the world row … endless deterministic cave"; rows 0-61 byte-identical
  to the committed layout): lane
  [`control/status.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/control/status.md)
  and PR #23 row in
  [`docs/review-queue.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/docs/review-queue.md)
  (the same row warns any edit to `layout_of_row`/`row_solid`/`row_features`
  rewrites the whole cave — a seed parameter is the disciplined way to vary them).
- New-scope gate ("keep investing in Lumen Drift (new scope needs owner say-so)"):
  ⚑ needs-owner in the same status pin.
- SRAM save slot + title screen already exist to carry per-seed BEST and seed
  entry: concept-doc polish-pass-1 entry,
  [`docs/concepts/session-1-concepts.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/docs/concepts/session-1-concepts.md).

**Why now:** the owner is about to make the concept pick — the fork's
"more Lumen Drift" arm should name its best concrete option before he chooses,
and the PR #23 architecture is the moment this became a small change instead of a
rewrite.
