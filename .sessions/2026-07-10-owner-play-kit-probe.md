# Session — lumen-drift-owner-play-kit probe (gba-homebrew): battery v0 → park(build-direct)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 (worker slice, dispatched by the coordinator under
> continuous-chaining mode per Q-0265)

## What this session did

- Claimed `ideas/gba-homebrew/` (`claims/probe-gba-homebrew-owner-play-kit.md`, flat
  filename per `claims/README.md`; cleared in this branch's final commit).
- **Live-state verification FIRST** (the PR #25/#27/#30 discipline): lane HEAD still
  `16e64d7` (`git ls-remote`, 22:21Z — unchanged since PR #30's 22:05Z audit, so its delta
  finding carries: only kit-upgrade commits since the capture pin `bc73da7`). Verified at
  HEAD via read-only blobless clone + full `ls-tree -r`: **the play kit does not exist**
  (no `docs/play/`, no committed `.gba`; `.gitignore` ignores `games/*/*.gba`), and —
  stronger than the capture claims — NO CI surface carries the ROM either: the required
  "ROM builds" check uploads no artifact and `headless-boot.yml` (workflow_dispatch only)
  uploads PNGs only. Playing today genuinely requires a local devkitARM toolchain; the
  capture UNDERSTATED its own problem. Lumen Drift still SCOPE-COMPLETE / polish list
  EXHAUSTED / ⚑ concept-pick ask open (lane heartbeat @ HEAD, the 07:14:30Z session-7
  write); concept doc still "awaiting owner pick"; publish rail confirmed verbatim at HEAD
  README. Cross-link cross-checked: `ideas/venture-lab/games-adjacent-candidate-three`
  (state `captured`) sequences the itch.io listing strictly post-EAP behind this same
  owner sitting and names this artifact as its upload. Manifest row @ superbot HEAD
  `c06e9a2` still records `b607365`/v1.6.0 vs real `16e64d7`/v1.7.1 — staleness
  datapoint 9.
- **Probed (battery v0):**
  `ideas/gba-homebrew/lumen-drift-owner-play-kit-2026-07-10.md` — committed `docs/play/`
  kit: checksummed `lumen-drift.gba` + 2-minute how-to page, drift-proofed by a ~5-line
  rebuild-and-compare step in the existing required check (which already rebuilds every
  ROM per-PR in <60s warm).
- **Verdict: park(build-direct)** — worth building, nothing to simulate: a lane-local
  packaging slice the standing default already authorizes; the one empirical unknown
  (build byte-reproducibility under the pinned toolchain) is settled by the kit PR's own
  first CI run, and the how-to page's validation event is the owner sitting itself.
  Smallest slice (Q8): ROM + sha256 sidecar in `docs/play/` at the pinned toolchain sha,
  the drift assert in "ROM builds", one how-to page carrying the concept-pick fork and
  the publish-rail reading, ⚑ ask updated to lead with the kit. State advanced
  forward-only captured → parked(build-direct — …); Grounding (@ `16e64d7`, manifest row:
  behind) + Sequence header lines added in the blessed byte-form; section README index
  updated.
- **No PROPOSAL appended:** not sim-ready — the PR #25/#27/#29/#30 discipline; the
  manager reads the verdict on the idea file and this heartbeat's fan-in note (now a
  THREE-head build-direct queue for one lane: anchor → pack → play kit, the kit alone
  carrying a hard calendar bound).

**📊 Model:** fable-5 · high · docs-only (probe report + index line + card + heartbeat; no code)

## 💡 Session idea

Q4's sharpest finding generalizes: a lane can prove an artifact exhaustively in CI and
still leave it unreachable by the one human it gates on — "no surface carries the
artifact" is a distinct failure class from "artifact unproven", and it is invisible to
every green check. A cheap standing probe for any owner-gated playtest/review ask:
enumerate the surfaces the owner can reach with zero toolchain (tree, release assets,
persistent artifacts) and require the ask's object to exist on at least one. Candidate
grooming-round-3 line for the capture checklist: an idea that prices an owner action
should verify where the action's object actually lives.

## ⟲ Previous-session review

Consumed the PR #30 card + heartbeat handoff: it named this exact head as ripest
("owner-play-kit feeds the 2026-07-14 EAP sitting and could be probed next if the pick
still hasn't landed") — dispatched while the pick window is still open; the window held
(pick-relevant surfaces unchanged at the same HEAD `16e64d7` PR #30 audited, re-verified
by ls-remote at 22:21Z rather than assumed). Reused both of its capability recipes
as-documented: ls-remote for out-of-scope HEAD verification and the blobless clone for
tree/blob reads where the raw path can't enumerate — this session extended the latter
from commit enumeration to full-tree existence proofs (`ls-tree -r` for "no .gba
anywhere"). Friction inherited and confirmed unchanged: GitHub MCP scoped to
`menno420/idea-engine`, `api.github.com` proxy-walled, lane Actions unreadable (CI-green
therefore inferred from merged-through-required-checks + the lane's recorded green run,
stated as inference in the report). Its manifest-staleness list grows to nine datapoints
(same row, THIRD consecutive superbot HEAD — `655e0fe`, `9624c53`, now `c06e9a2` — still
recording `b607365`/v1.6.0).

## Handoff → next wake

Inbox first (verified still empty at origin/main HEAD `d73d91a` at claim time). Outbox
depth unchanged (4 proposals; this probe parked, nothing appended). gba-homebrew now
carries THREE build-direct heads racing one owner window — the fan-in note asks the
manager for one sequenced bundle (anchor → pack → play kit; the kit is the only head
with a hard calendar bound, EAP window ends 2026-07-14, and is independent of the
anchor↔pack coupling so it can ship first). Of the section's captured heads only
`seeded-cave-runs` remains unprobed — it is pick-gated by construction (the concrete
"keep investing" arm), so probing it before the pick adds little; deprioritize until the
pick lands. Ripest next slices: second-lane harvest, freshest-wins one-liner (grooming
round 3), `check_harvest --emit-entries` (PR #26 card 💡), cross-link state-echo lint
(PR #29 card 💡).
