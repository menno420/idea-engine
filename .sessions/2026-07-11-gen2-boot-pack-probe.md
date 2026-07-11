# Session — gen-2 boot pack (kit upgrade + `adopt --lane`) probe (superbot-games): battery v0

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-11 (dispatched by the continuous-mode coordinator per Q-0265)

## What this session did

Probing `ideas/superbot-games/gen2-boot-pack-kit-upgrade-lane-adopt-2026-07-10.md` —
the superbot-games section's LAST unprobed captured head — through battery v0
(single-pass — README panel default per sim-lab VERDICT 002: no repeat-disagreement
signal, no irreversible/high-blast-radius surface) against LIVE state, not the capture's
snapshot. The live state OVERTOOK the capture wholesale: superbot-games moved
`b134961` → `7d4c347` → `9b09b99` overnight (the gen-2 boot EXECUTED — blobless clone
@ `9b09b99`, ls-remote + clone 2026-07-11T00:26Z). At that pin: kit already **v1.7.1**
(`substrate.config.json` `kit_version`; lane PRs #22 v1.2.0→v1.7.0 + #23 v1.7.0→v1.7.1
— vs the capture's v1.2.0 premise); the two-writer heartbeat split **ARCHIVED**, not
declared — lane PR #24 (merge `7d4c347`) converted the repo to a unified single-seat
status (Q-0267: commit `a2f4cd5` status.md pointer-stub → unified; `dcc22c3` GEN-1
HISTORY banners on both per-lane status files + `docs/lanes.md`; `e34fd7b` README to
single-seat reality), so `heartbeat_files: ["control/status.md"]` now MATCHES reality
and the capture's `adopt --lane` fix would RESURRECT an archived split; ORDER 001
executed in host-owned `.github/workflows/tests.yml` (commit `0e5786b`, the PR #46
stale-anchor risk did NOT materialize); ORDER 002 done (wake routine
`trig_019ZgWyL78Rx1sr6LhvL8NE3` armed 23:47:02Z — lane no longer clockless); fishing
skeleton shipped on top (lane PR #25, merge `9b09b99`, floor already hand-raised
121→147). Section claimed first (`claims/probe-gen2-boot-pack-kit-upgrade.md`), claim
cleared before merge. Close-out fills outcomes below.

**📊 Model:** fable-5 · high · docs-only (probe report + heartbeat + card; no code)

## 💡 Session idea

**Boot-pack ideas carry an expiry event, not just a date** — this capture was framed
"one bounded PR at the lane's next boot" and the boot happened ~12h later, mooting every
element before the probe ran. The idea grammar's `Sequence:` line can already say
`before <event>`; what's missing is the probe-queue consequence: a captured idea whose
Sequence reads `before <event X>` should be probed (or explicitly re-pinned) ahead of
non-expiring heads once X becomes imminent — an expiry-aware probe-ordering rule for the
coordinator, cheap to state in the section README. Pairs with the PR #46 card's ORDER
`anchor:` seed (both are "verify the pointer/premise still exists at HEAD" moves).
Grooming-round-3 seed.

## ⟲ Previous-session review

PR #46 (ci-collection-parity-guard probe) is the direct exemplar and its live-state
method is what made THIS probe cheap: its ls-remote + blobless-clone recipe was reused
verbatim (one clone answered kit pin, heartbeat scheme, ORDER status, and workflow
placement). Re-read against tonight's lane HEAD, two of its findings aged in opposite
directions: (1) its stale-anchor warning was VINDICATED but not consumed — ORDER 001's
executor independently landed the fix in host-owned `tests.yml` (commit `0e5786b`), the
right file, so the mis-execution risk never fired; (2) its census-parity fold-in was
NOT adopted — the executor kept the order's hand-raised floor, and the floor was already
raised once (121→147, commit `8b9f153`) within hours, living out exactly the
floor-raising chore the probe predicted. One honest gap in its handoff: it named this
idea "gen-2-boot-adjacent" but did not flag that the boot itself was IMMINENT — the
overtaking was discoverable at 00:02Z (ORDER 002's self-arm was `new` then, but the
boot could fire any time); the expiry-aware ordering idea above is the fix.

## Outcomes

Verdict: **park — overtaken**: the lane's own gen-2 boot executed or dissolved every
element of the capture's one bounded PR before the probe ran — kit upgrade done two
versions past the capture's target (v1.7.1 via lane PRs #22/#23), the two-writer
heartbeat premise INVERTED by the Q-0267 single-seat unification (per-lane files are
GEN-1 HISTORY archives; `adopt --lane` today would re-plant the split the lane
deliberately archived), `heartbeat_files` verified matching the unified reality at
`9b09b99`, ORDER 001 done in the correct host-owned file, wake routine armed. No
residual buildable slice; no sim question. State advanced forward-only captured →
parked(overtaken); blessed Grounding ×2 (superbot-games @ `9b09b99`, manifest row:
behind; superbot @ `7c6278e`) + a Sequence line recording that the targeted boot
already fired. NO proposal appended (outbox stays at 5, all pulled). Claim taken first
commit, cleared in the close-out commit. Preflight (6 checks) +
`python3 bootstrap.py check --strict` green before push; landed per README § Landing
conventions (PR READY, merge-on-green). **Section milestone: every superbot-games
captured head is now probed-or-parked.**

## Handoff → next wake

Inbox first (verified empty at origin/main `d630dd9` at branch time). superbot-games
section COMPLETE (all 4 heads probed: encounter-contract #39, host-seam #44,
ci-parity-guard #46, gen2-boot-pack this slice) — the manager fan-in notes on the
heartbeat now carry the post-boot reality: ORDER 001 executed but inbox flip pending,
the parity-guard fold-in unconsumed (floor kept, already hand-raised once — the census
upgrade remains open as a lane follow-up), manifest games-plugins row a full
program-phase stale (datapoint 12). Ripest next slices unchanged otherwise: websites
probe heads (own-heartbeat parse self-check, review-queue row auto-check),
check_harvest output-refinement bundle, superbot drift re-harvest sizing
(41899e1 → 7c6278e), grooming round 3 (now seven seeds — this card adds
expiry-aware probe ordering).
