# Session — build: index-echo reason-presence drift check (STATE-ECHO extension)

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## Scope — the slice plan

The PR #161 card's 💡 executed: extend the STATE-ECHO pass in
`scripts/check_ideas.py` so a section-README bullet's state token that disagrees
with its idea file's `> **State:**` line on REASON PRESENCE warns — the exact
drift class PR #161 hand-fixed 3 instances of (bare `parked` bullets whose files
already carried full terminal `parked(<reason>)` states).

Verify-first overlap check (mandatory, done before writing code): PR #149's
STATE-ECHO pass (`.sessions/2026-07-11-lint-bundle-build.md` head 2) already
compares state FAMILIES — `parked` echo vs `parked(routed)` file counts as a
MATCH, so the #161 class passes silently. The lint-bundle idea's Q4 names this
deliberately ("family-compare blindness … reason-detail drift is judgment
territory") and the #161 card's 💡 carves the fix precisely: "`parked` vs
`parked(...)` counts as agreement only bare-vs-bare". Verdict: PARTIALLY covered
— EXTEND the existing pass with a reason-PRESENCE leg (never reason-DETAIL:
abbreviated echoes stay blessed per the #160 line-59 format precedent), no
parallel check.

Claim ritual honored: `control/claims/build-index-echo-reason-drift.md`
fast-laned FIRST as PR #162 (merged c3682dd by the enabler within the minute),
claims dir re-read at HEAD post-merge — empty except README.md and this claim.
Claim file deleted in this PR's close-out.
