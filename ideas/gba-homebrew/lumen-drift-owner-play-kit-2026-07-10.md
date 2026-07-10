# Lumen Drift owner play kit — make the 15-minute playtest cost 15 minutes

> **State:** parked(build-direct — a lane-local packaging slice (committed checksummed ROM + how-to page + a ~5-line drift assert in the existing required check) the lane's standing default already authorizes; no reproducible-evidence question for sim-lab — the one empirical unknown, build byte-reproducibility, is settled by the lane's own first CI run; manager routes it to the lane before the owner's EAP sitting, window ends 2026-07-14)
> **Class:** product · **Target:** `menno420/gba-homebrew`
> **Grounding:** https://github.com/menno420/gba-homebrew@16e64d7c92ff8fd1ee96eeb3194fae26b14b86ee · fetched 2026-07-10T22:21Z (manifest row: behind)
> **Sequence:** before the owner's EAP playtest sitting (window ends 2026-07-14) — verified still ahead at probe time: no play kit exists at lane HEAD `16e64d7` (no `docs/play/`, no committed `.gba` anywhere in the tree) and the ⚑ playtest+pick ask is still the lane's open needs-owner; partial decay only — the checksummed artifact still serves venture-lab's post-EAP itch.io upload even if the sitting passes first

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

## Probe report (v0, 2026-07-10)

*Probed 2026-07-10T22:21Z. Live-state verification FIRST (the PR #25/#27/#30 discipline):
lane HEAD is STILL `16e64d7` (`git ls-remote`, 22:21Z) — unchanged since PR #30's 22:05Z
audit, so that audit's delta finding carries: only lane PR #27's kit upgrade
(`979b161`/`962cdfe`/`64a81d8`, v1.7.0 → v1.7.1) sits between the capture pin `bc73da7`
and HEAD, and the pick-relevant surfaces are byte-identical. Verified at HEAD via a
read-only blobless clone (full `git ls-tree -r`): the play kit does NOT exist — no
`docs/play/`, no committed `.gba` anywhere; `.gitignore` ignores `games/*/*.gba` build
output. Stronger than the capture claims: the per-PR required "ROM builds" check
(`.github/workflows/rom-builds.yml`) builds every ROM but uploads NO artifact, and the
workflow_dispatch-only `headless-boot.yml` uploads only PNGs (`boot-proof`,
`lumen-drift-proof`) — so even "fishing a build out of Actions runs" yields screenshots,
never the ROM; playing today genuinely requires a local devkitARM toolchain. The capture
UNDERSTATED its own problem. Lumen Drift is still finished and gated: lane heartbeat @
HEAD (the 07:14:30Z session-7 write) says SCOPE-COMPLETE, polish list EXHAUSTED, ⚑
concept-pick ask open; `docs/concepts/session-1-concepts.md` still "awaiting owner pick";
CI-green inferable from lane PRs #26/#27 merging through the required checks at
`bc73da7`/`16e64d7` plus the recorded green headless run 29076028307 on `f502147`
(Actions unreadable from here — GitHub MCP is scoped to this repo). Publish rail
confirmed verbatim at HEAD README: "External publishing of Track B (itch.io, forums,
anywhere) still requires an owner action." Cross-link cross-checked:
[`ideas/venture-lab/games-adjacent-candidate-three-2026-07-10.md`](../venture-lab/games-adjacent-candidate-three-2026-07-10.md)
(state `captured`) sequences the itch.io listing strictly post-EAP behind this same
owner sitting and names this artifact as its upload — built once, used twice. Manifest
row @ superbot HEAD `c06e9a2` STILL records lane HEAD `b607365`/kit v1.6.0 (behind —
staleness datapoint 9).*

**1. What is this really?**
Last-mile artifact logistics: the lane proved the ROM (built, replay-asserted, checksummed
toolchain), then left it on the far side of the toolchain wall from the one human whose
click gates the whole track. The kit moves the already-proven build product to where the
owner's ~15 minutes actually are — a committed, checksummed `lumen-drift.gba` plus a
2-minute how-to page — converting a CI-internal build product into an owner-facing
artifact. Deeper: it re-prices the fleet's single most expensive pending action. The
manifest budgets the playtest at ~15 minutes; at HEAD it costs a devkitARM install,
because no surface — tree, Actions artifacts, releases — carries the ROM at all. And it
is dated: the playtest feeds the owner's EAP sitting before 2026-07-14.

**2. What is the possibility space?**
Five axes. **Artifact placement:** committed file in `docs/play/` (stable raw URL,
zero-click, survives forever) vs Actions artifact upload (expires, needs a logged-in
fishing trip) vs GitHub Release asset (needs a tag ceremony the lane has never run) —
committed file dominates for a single small ROM. **Drift-proofing:** none (committed
binary rots — the classic objection) vs a checksum sidecar vs rebuilding in the existing
required check and comparing — the last is nearly free here because "ROM builds" already
rebuilds every ROM per-PR in <60s warm. **Kit depth:** bare ROM + mGBA link vs a
how-to-play page vs a full playtest script that maps what-to-look-for onto the
concept-pick criteria the sitting must feed — thin page + pick pointer is the sweet spot.
**Scope:** Lumen Drift only vs also the skeleton ROM (no owner value — skip).
**Browser embed:** an in-repo HTML emulator page would creep toward the publishing rail
and duplicates what itch.io provides later — out of scope, venture-lab owns that path.

**3. What is the most advanced capability reachable by the simplest implementation?**
A ~5-line addition to the existing required check (build, then `sha256sum -c` /`cmp`
against the committed copy) makes the committed binary structurally drift-proof — the
standard reason never to commit build products is deleted by CI the lane already runs on
every PR, warm-cached under its 60s budget. On top of that one page buys: (a) the gating
playtest actually costing its budgeted 15 minutes (download ROM + mGBA, one-button
controls, what to look for: light-radius pressure, three sections, the endless deep);
(b) the pick fork wired in — the page points at `session-1-concepts.md` and the ⚑ ask so
the sitting produces the pick, not just impressions; (c) venture-lab's itch.io upload
pre-staged with a hash that provably matches reviewed source at a pinned sha — the
publish candidate inherits a verified artifact for free.

**4. What breaks it?**
- **Build nondeterminism.** If the devkitARM/Butano link embeds timestamps or paths, the
  CI comparison flakes. The toolchain is checksum-pinned (lane PR #13;
  `tools/setup-toolchain.sh` is the pin manifest and the cache key), which bounds the
  environment, but byte-reproducibility must be verified in the kit PR's own first CI
  run; fallback is a recorded checksum without a hard rebuild-compare — weaker, still
  honest.
- **The gitignore trap.** `games/*/*.gba` is ignored — the committed copy must live
  outside `games/` (hence `docs/play/`); a naive `git add` of the build output silently
  stages nothing.
- **Rail-reading contest.** The repo is public, so a committed ROM is downloadable by
  anyone; a broad reading of "external publishing … anywhere" could object. The capture's
  answer holds — the source is already public and publish-safe by construction, the kit
  adds no new venue — but the lane PR should state that reading explicitly so the owner
  can veto by revert (forward-only git).
- **The window race, softened.** The EAP sitting ends 2026-07-14 — the same clock the
  other two build-direct heads race — but decay is only partial: the artifact still
  serves venture-lab's post-EAP upload even if the sitting happens without it. What is
  lost unrecoverably is the 15-minute playtest price at the moment it gates the pick.
- **What it cannot fix.** The owner still installs mGBA locally (a 2-minute download the
  page links, not removable), and a kit nobody points him at changes nothing — the ⚑
  ask must be updated to lead with the kit, or the artifact is buried one layer up.

**5. What does it unlock?**
The pick gate becomes clickable at its advertised price — and the pick gates every
remaining Track B session plus ORDER 001's joint done-when with Track A. Venture-lab's
candidate #3 gets its upload artifact and provenance hash for free (built once, used
twice — the cross-link's own words). The fleet gets the pattern: every future finished
game ships a play kit as last-mile packaging, so no gating playtest ever silently costs
an evening again. And the EAP sitting before 2026-07-14 gets one more of its inputs
staged in advance (alongside the bring-up pack, which stages the post-pick side).

**6. What does it depend on?**
- The owner sitting still being ahead (hard calendar bound 2026-07-14) — verified ahead
  at probe time; owner-controlled.
- Lane CI green + the pinned toolchain reproducing the build (checksum pins, warm cache
  keyed on the pin manifest) — the drift assert stands on both.
- Lane capacity under the standing default ("groom the backlog — never idle") — no new
  ORDER strictly required.
- No cross-lane build dependency: everything it touches lives in `menno420/gba-homebrew`.
  Downstream co-consumer, not dependency: venture-lab's candidate-three consumes the
  artifact post-EAP behind the owner's itch.io clicks.
- Sequencing interplay with the lane's other two build-direct heads: independent of the
  anchor↔pack coupling (the kit touches no harness timing), so it can ship first or in
  the same joint lane session — and of the three heads it is the only one with a hard
  calendar bound.

**7. Which lane should build it?**
`menno420/gba-homebrew`, alone: it owns the ROM source, the pinned toolchain, and the
required check the drift assert extends; this repo cannot write lane files (Q-0260). Not
venture-lab — the kit is upstream of the venture play, inside the lane's own rails, and
venture-lab cannot build the ROM. Not sim-lab: there is no reproducible-evidence question
to settle — the only empirical unknown (is the build byte-reproducible under the pinned
toolchain?) is answered by the kit PR's own first CI run in minutes, and "does a
committed how-to page make a playtest cheaper" has no simulator; its validation event is
the owner sitting itself.

**8. What is the smallest shippable slice?**
One lane PR under the standing default: (1) `docs/play/lumen-drift.gba` +
`docs/play/lumen-drift.gba.sha256`, built at the pinned toolchain sha; (2) the required
"ROM builds" check gains a rebuild-and-compare step (drift = red; if the first run proves
the build nondeterministic, fall back to the recorded-checksum form and say so in the
page); (3) `docs/play/README.md` — mGBA download link, the one-button control scheme,
what to look for (light-radius pressure, the three sections, the endless deep), and the
concept-pick fork the playtest feeds (links to `docs/concepts/session-1-concepts.md` and
the ⚑ ask), with the publish-rail reading stated (in-repo only; external publishing stays
owner-gated, venture-lab owns that path); (4) the lane heartbeat's ⚑ ask updated to lead
with the kit. Done-when: kit merged + the required check proving the committed ROM
matches source + ⚑ pointer live before the owner sitting.

**Recommendation: park** — build-direct: a lane-local packaging slice (committed
checksummed ROM + how-to page + a ~5-line drift assert in the check the lane already
runs per-PR) the standing default already authorizes, with no reproducible-evidence
question for sim-lab; the manager should route it to `menno420/gba-homebrew` now,
alongside the anchor→pack pair — of the lane's three build-direct heads this is the only
one with a hard calendar bound (the owner's EAP sitting, window ends 2026-07-14).
