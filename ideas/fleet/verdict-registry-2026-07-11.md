# Verdict registry — hermetic `## Sim verdict` note lint + machine-checkable PROPOSAL↔VERDICT cross

> **State:** park(built-here — Sim-verdict note lint, SIM-VERDICT category in `scripts/check_ideas.py`, this PR)
> **Class:** process · **Target:** `menno420/idea-engine` (the lint half — built here, see report Q7; the sim-lab grammar half is NOT ours and routes via the manager, see Q7)
> **Grounding:** https://raw.githubusercontent.com/menno420/sim-lab/d89303e/control/outbox.md@d89303e · fetched 2026-07-11T07:12Z

**Origin:** the V005 fan-in card's 💡 (`.sessions/2026-07-11-verdict-005-superbot-fanin.md`
§ "💡 Session idea", landed PR #81 `a1b320a`): the blessed `## Sim verdict` lint (PR #50
round-3) stayed unbuilt as "hermeticity-blocked — `check_ideas --outbox` can't read
sim-lab's outbox at lint time", and the card proposed a committed registry
(`control/verdict-registry.md`) written by each fan-in so the lint becomes hermetic.
**Arming event:** V006 proved sim-lab's verdict field set is NOT stable — VERDICT 006
shipped **no `ruling:` field** (its verdict token is a plain `verdict: approve` and the
operative ruling text is its `recommendation:` field); the fan-in survived only on a
human judgment call about which field to quote. The deviation is recorded in **PR #121**
(merged 2026-07-11T06:57:33Z by github-actions[bot], merge commit `d90f9c5`; body:
"VERDICT 006 carries no separate `ruling:` field — … the operative ruling text is its
`recommendation:` field") and in the V006 card's 💡
(`.sessions/2026-07-11-verdict-006-fanin.md`).

**The idea:** make the verdict trail machine-checkable on THIS repo's side without
network: (a) pin the verdict-NOTE field set and lint every `## Sim verdict` note against
it in `scripts/check_ideas.py` (hermetic — reads only this tree); (b) validate the
PROPOSAL↔VERDICT numbering cross against the LOCAL `control/outbox.md` (the idea-engine
half of the cross — sim-lab numbers by intake order and its outbox carries no proposal
back-pointer field); (c) route the sim-lab half (pin sim-lab's verdict-ENTRY field set:
`ruling:`-or-`recommendation:` named explicitly + a machine-readable proposal cross
field) via the manager — this repo never writes another repo's files.

## Evidence survey (capture-time, all six live notes + the sim-lab pin)

De-facto field set of the six `## Sim verdict` notes in this tree (grep
`^## Sim verdict`, 6 hits):

| note (V=verdict) | heading date | VERDICT·finalized·token marker | sim-lab outbox pin | inline `= this repo's PROPOSAL n` cross | gate mention | "State stays" closer |
|---|---|---|---|---|---|---|
| V001 `ideas/superbot/wild-encounters-activity-spawning-2026-07-10.md` | 2026-07-10 | ✓ (`21:20Z`, time-only) | ✓ full 40-hex `8713f26…` | ✗ (cross lives on the fan-in card only) | ✓ | ✓ |
| V002 `ideas/superbot/idea-probe-brainstorm-simulator-2026-07-10.md` | 2026-07-10 | ✓ (token itself is prose: "approve — selectively (…)") | ✓ full 40-hex | ✗ (card only) | ✓ | ✓ |
| V003 `ideas/websites/superbot-site-stats-data-story-2026-07-10.md` | 2026-07-10 | ✓ (marker wraps a line; carries ", ruling buildable-with-named-changes") | ✓ full 40-hex | ✓ P002 | ✓ | ✓ |
| V004 `ideas/superbot/explore-hub-federated-world-2026-07-10.md` | 2026-07-10 | ✓ | ✓ full 40-hex | ✗ (card only) | ✓ (as "gate-PASS" on the SETTLED line — NOT in the source parenthetical, the only positional drift) | ✓ |
| V005 `ideas/superbot/project-capability-self-awareness-2026-07-10.md` | 2026-07-11 | ✓ (full ISO finalized) | ✓ short-SHA `f70fbea` | ✓ P005 | ✓ | ✓ |
| V006 `ideas/superbot-idle/idle-economy-sim-kernel-2026-07-11.md` | 2026-07-11 | ✓ (full ISO) | ✓ short-SHA `d89303e` | ✓ P006 | ✓ | ✓ |

Drift summary: the inline numbering cross is 3/6 (all three misses are 2026-07-10 notes;
both 2026-07-11 notes carry it); finalized-time form drifted time-only → full ISO; pin
form drifted 40-hex → short SHA; V004's gate token drifted position. The invariant core
carried by ALL six: heading date · VERDICT/finalized/token marker · sim-lab
`control/outbox.md` @ sha pin · "State stays" closer.

Sim-lab side (fetched RAW at the pinned SHA `d89303e`, all six verdict entries):
every entry carries `## VERDICT nnn · <ISO> · status: finalized` + `target:` +
`verdict:` + `evidence:` + `recommendation:` + `gate:`; **`ruling:` appears in only
V003 and V005** (2/6); `verdict:` tokens are free prose (V002:
"approve — selectively (…)"); **no field cross-references the idea-engine PROPOSAL
number** — the V=P cross exists nowhere machine-readable on sim-lab's side.

## Probe report (v0, 2026-07-11)

**1. What is this really?**
The last unbuilt half of the PR #50 round-3 blessing, un-blocked by a reframe. The
"registry" framing assumed the lint needs sim-lab's data at lint time (not hermetic) or
a committed mirror of it (a registry file). But every fan-in already writes a note that
QUOTES the verdict at a pinned SHA — the notes plus the local outbox ARE the registry.
What was actually missing: (a) a pinned note field set to lint against, and (b) the
observation that the PROPOSAL half of the numbering cross is validatable against
`control/outbox.md`, which is local. This is `check_ideas.py` growing one more category
(SIM-VERDICT), exactly like the PR #24 optional-line extension: lint the artifact the
convention already produces.

**2. What is the possibility space?**
Four axes. **Registry materialization:** none (lint the notes) → a committed
`control/verdict-registry.md` row per fan-in → per-idea structured verdict blocks with
machine fields. **Cross direction:** note→outbox only (hermetic, this slice) →
outbox→verdict completeness ("every proposal eventually verdicted" — NOT checkable
without sim-lab data, inherently non-hermetic) → wake-time network check à la
`check_harvest.py` (runs at wake, not in CI). **Grammar stabilization:** consumer-side
tolerance (quote whichever field is operative — status quo) → sim-lab pins its verdict
field set (`ruling:`-or-`recommendation:` explicit) → sim-lab adds a `proposal:` cross
field, making the V=P cross two-sided-machine-readable. **Enforcement:** advisory →
date-gated hard (this slice, the PR #24 pattern) → full hard after legacy notes are
grandfathered out.

**3. What is the most advanced capability reachable by the simplest implementation?**
A hermetic, CI-free-running guarantee that every verdict note in the tree carries the
pinned field set and that every inline numbering cross names a PROPOSAL that actually
exists in the local outbox — ~90 lines of stdlib regex in the checker the preflight
already runs (`scripts/preflight.py` CHECKS entry 2 — zero wiring change, preflight.py
untouched). The registry falls out for free: `grep -rn "^## Sim verdict" ideas/` +
the lint's guarantee IS the queryable registry, always exactly as fresh as the notes,
with no second writer surface to drift.

**4. What breaks it?**
- **A separate registry FILE would break itself** — it is a hand-edited shared index
  (the `control/claims/README.md` measured anti-pattern: shared-append ≈98% conflict
  vs 0% per-file) plus a second copy of note facts that can silently disagree with the
  notes it indexes. Judged overkill: dropped from the build, recorded here as the
  reasoned rejection of the origin 💡's file-shaped half.
- **Sim-lab grammar drift (the V006 class)** — the lint pins the NOTE shape, not
  sim-lab's entry shape; a future verdict with yet another operative field still needs
  the fan-in author's judgment. That half routes to the manager (Q7) — not fixable
  from here.
- **Verbatim-quote false positives** — a note QUOTING a broken marker in prose could
  satisfy the regex; mitigated as in the probe-report lint: markers are anchored
  byte-forms, and the check is a floor, not a judge.
- **Legal fan-out reads as duplication** — one verdict fanned into two ideas is legal
  but unprecedented; duplicate VERDICT numbers WARN (advisory) rather than red.
- **Grammar co-edit drift** — the same standing risk as every checker here: README
  grammar changes without the loud constants block changing; mitigated by the
  co-edit comment convention (constants live in one block, PR #11 pattern).

**5. What does it unlock?**
The `## Sim verdict` convention stops depending on session discipline: a fan-in missing
its cross, its pin, or its closer reds preflight the same wake it lands. The V=P cross
becomes grep-plus-lint queryable (the exact by-hand query the V005 card named as the
recurring cost — five hand-executed fan-ins to date). And it hands the manager a
concrete, evidence-backed ask for sim-lab (Q7): 2/6 `ruling:` coverage and a
nowhere-machine-readable cross, measured at a pinned SHA.

**6. What does it depend on?**
This tree only: the six live notes (all already conform — live run green, 3 advisory
legacy warnings by design), `control/outbox.md` (local, the hermetic cross target),
python3 stdlib, and the date-gate precedent (PR #24) for forward-only enforcement.
No network, no sim-lab cooperation, no kit change, no preflight/workflow edit.

**7. Which lane should build it?**
Split verdict. **Lint half: idea-engine, this repo, this PR** — it lints this repo's
own artifact against this repo's own README blessing; only this repo's sessions can
land fixes it reports (the `check_ideas.py` precedent verbatim). **Sim-lab half:
NOT ours regardless** — stabilizing sim-lab's verdict-entry grammar (explicit
`ruling:`-or-`recommendation:`, ideally a `proposal:` cross field) is a sim-lab-repo
change; this repo never writes another repo's files, sim-lab has no `ideas/<section>`
(sections mirror active fleet lanes; sim-lab is pipeline, not lane), and README § the
pipeline contract routes everything post-verdict through the **manager** — so the ask
rides this slice's heartbeat notes as an ORDER-worthy fan-in line for the manager's
:30 sweep (the same routing surface the trading-strategy and venture-lab fan-ins
used), citing PR #121 + the 2/6 `ruling:` survey above as evidence.

**8. What is the smallest shippable slice?**
The SIM-VERDICT category in `scripts/check_ideas.py` (stdlib, constants in the loud
co-edit block, ~90 lines): pinned-core checks hard everywhere (heading date ·
VERDICT/finalized/token marker · sim-lab outbox pin · "State stays" closer),
numbering cross + gate mention date-gated hard from 2026-07-11 (the PR #121 day) and
advisory before, cross-existence vs local outbox always hard, duplicate-verdict WARN.
Cheaper to build than to route (the README battery shortcut, PR #2/#11 lineage) — it
ships **in this same PR**, live-run green over the real tree with a two-direction
smoke test on the session card. No registry file (Q4), no preflight/workflow edit
(entry 2 of CHECKS already runs the checker).

**Recommendation: park(built-here — SIM-VERDICT note lint in scripts/check_ideas.py, this PR)** —
rationale: the idea-engine half is repo-internal PROCESS tooling whose smallest slice
is a trivial stdlib extension of the existing checker, settled by running it (this PR
does, both directions); nothing here is sim-shaped, so no outbox proposal — the
sim-lab grammar half is deliberately NOT built here and routes to the manager via this
slice's heartbeat fan-in note (Q7), with the registry FILE explicitly judged overkill
(Q4: the notes + local outbox are the registry).
