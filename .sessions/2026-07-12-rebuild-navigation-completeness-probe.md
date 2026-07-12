# Session — single-pass probe: rebuild-navigation-completeness-check (price the remaining half post-A-3-in-D-0020)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-12 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Single-pass probe (battery v0, panel not escalated — docs/process surface,
reversible park) of `ideas/superbot/rebuild-navigation-completeness-check-2026-07-10.md`
— the mint-time TOP-5 exclusion whose named trigger FIRED: "A-3 golden landed
inside D-0020 — price which half remains before it earns a slot"
(`control/status.md` notes @ `329547d`).

Answer, verified at superbot-next live HEAD N=`d3dba9b` (ls-remote + blobless
clone; invocation sites read, not doc claims): the capture asks for TWO asserts —
(a) the Back+Home golden over every node + re-render path, (b) a preset-coverage
assertion (every feature ∈ ≥1 preset). Half (a) is BUILT in stronger-than-asked
form inside D-0020 (superbot-next PR #19, `c7defbc`, 2026-07-08 — two days before
the harvest): `sim/navigation_walk.py` drives the REAL panel engine (reachability,
semantic-parent Back, static-table-bound Home, re-render stability) +
`tests/unit/navigation_golden/test_navigation_completeness.py` with
fixture-negative false-green proofs, red-gating via N `ci.yml:34`. Half (b)
REMAINS — but as a designed-in LOUD arm-later: `presets_checked=False`
(`sim/navigation_walk.py:56`) + `test_preset_leg_is_a_loud_arm_later`, blocked on
band-1's preset grammar which does not exist at N (zero `preset` hits in
`sb/spec/panels.py`). Priced: costs nothing here, earns its arming inside band-1 —
NO TOP-5 slot, NO sim proposal (boolean contract, no parameter space).

Shipped: probe report v0 appended to the idea file; state forward-only
captured → parked(half-built-at-target — …); section README index badge updated
naming built half AND open half per the badge duty; this card. Canonical doc
byte-identical at S HEAD `1ecc211` vs the `fd638e3` pin (md5 match) — capture
fresh, no re-pin needed. Dedup: sibling `rebuild-layout-success-simulator`
(same D-0020, different arm — scorer vs enforcer, no overlap consumed);
`rebuild-critical-review-checkers-2026-07-10.md:40-42` explicitly deferred this
half here; `no-dead-end-terminal-view-guard` / `ai-panel-inplace-navigation` /
`help-nav-attachment-seam` are legacy-superbot, no overlap. No control/ writes.

**📊 Model:** fable-5 (ORDER 001 standing rule; harness-reported family)

## 💡 Session idea

A "half remains" pricing probe should end by naming the EVENT that re-prices the
remainder, not a date: here the open half re-prices itself the day band-1 mints
the preset grammar — so the watch is "when band-1's preset grammar lands, verify
the reserved `presets_checked` leg actually armed" (body-exists is not
body-wired, the Rule-6 lesson). A fired-trigger exclusion consumed without naming
its successor event just mints the next stale exclusion.

## ⟲ Previous-session review

PR #221's card (check_sections roster sub-rows fix) closed with the
shape-classification handoff (roster gen #10+ may add new Lane-cell shapes) and
adopted the card-complete-BEFORE-push rule — adopted here too (card flips
complete pre-push; PR opens draft per dispatch, flipped ready on green). Its
slice unblocked `scripts/preflight.py` repo-wide, which this session relies on
for the verify step; no content overlap with this probe.

## Handoff → next wake

This consumes the "rebuild-navigation-completeness-check" mint-time exclusion
from the heartbeat's list (coordinator-side heartbeat edit — NOT done here,
control/ is coordinator-only). Forwardable watch for the manager sweep: when
superbot-next band-1 mints the preset grammar, verify the golden's preset leg
actually arms (flip of `presets_checked` + retirement of the loud test). Nothing
else in flight from this slice.
