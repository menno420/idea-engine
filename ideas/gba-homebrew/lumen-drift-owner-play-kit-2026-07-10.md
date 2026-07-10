# Lumen Drift owner play kit — make the 15-minute playtest cost 15 minutes

> **State:** captured
> **Class:** product · **Target:** `menno420/gba-homebrew`

## Problem

The whole games wave now funnels through ONE human action: the manifest row names
the owner's next step as "play it (~15 min) + concept pick", and the lane's own
⚑ needs-owner says the pick gates every remaining Track B session. But at lane HEAD
there is **no owner-facing playable artifact**: the ROM is a CI build product, so
actually playing Lumen Drift means installing the devkitARM toolchain or fishing a
build out of Actions runs — the ~15-minute playtest silently costs an evening, which
is exactly how a gating click goes stale.

## Idea

One bounded lane slice that makes the built ROM a first-class committed artifact:
a `docs/play/` kit containing the checksummed `lumen-drift.gba` (rebuilt and
hash-verified by the existing CI so it can never drift from source) plus a
2-minute how-to-play page — mGBA download link, the one-button control scheme,
what to look for (light-radius pressure, the three sections, the endless deep),
and the concept-pick fork the playtest feeds. Rail-honest by construction: the
repo is public and the ROM is original-IP publish-safe, but this kit stays
**inside the repo** — external publishing (itch.io, forums, anywhere) remains the
owner-gated action, and the venture-lab capture already owns that path
(cross-link: [`ideas/venture-lab/games-adjacent-candidate-three-2026-07-10.md`](../venture-lab/games-adjacent-candidate-three-2026-07-10.md)).
The same artifact later becomes the upload for that listing — built once, used twice.

## Grounding

- Manifest gba-homebrew row: "**Lumen Drift SCOPE-COMPLETE** (session 7, close-out
  #24); public-by-design (no Nintendo-derived content); … owner: play it (~15 min)
  + concept pick" ([superbot @ `53fb5ef`](https://raw.githubusercontent.com/menno420/superbot/53fb5ef9a294ab304b679dedd44ead55849295d5/docs/eap/fleet-manifest.md), fetched 2026-07-10).
- Lane ⚑ needs-owner (concept pick, full click path) + "polish list is EXHAUSTED":
  [`control/status.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/control/status.md).
- Hard rail — "External publishing of Track B (itch.io, forums, anywhere) still
  requires an owner action": lane [`README.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/README.md).
- CI already builds + replay-proves the ROM headlessly (headless-boot.yml, deep-run
  asserts): lane status notes @ same pin.

**Why now:** the playtest is the dated gate — venture-lab's publish candidate is
sequenced behind this exact owner sitting (EAP window ends 2026-07-14), and every
session the artifact stays buried is a session the pick can't land.
