# Session — TOP-5 item 4 probe (rebuild-design-cite-checker)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~19:42Z (worker slice, coordinator-dispatched
> under continuous-chaining mode per Q-0265)

## Scope

Probe TOP-5 item 4 (`ideas/superbot/rebuild-design-cite-checker-2026-07-10.md` —
`check_doc_cites.py`: validate `path:line` source citations in analysis/design
docs; the LAST open TOP-5 head). Section claim rode fast-lane FIRST as PR #214
`702c894` (`control/claims/probe-rebuild-design-cite-checker.md`; this claim file
deleted in this PR). Branch `probe/rebuild-design-cite-checker`.

## What this session did

**Full battery probe (single-pass)** on the cite-checker head. Verdict, exact line
on the file: `**Recommendation: sim-ready** — unlike TOP-5 item 3 (one named rule,
nothing to sweep), this head has a real parameter space (grammar × scope × gating)
and two live corpora; … PROPOSAL 010.` State flipped `captured` → `sim-ready`,
**PROPOSAL 010 appended** to `control/outbox.md` (tail verified 009 at HEAD before
the append — the cite-grammar × scope × gating spec sweep over the two real doc
corpora, done-when sized so the superbot-next lane build is one file plus one
ci.yml loop word), index row re-badged sim-ready (the state-echo duty), claim
cleared.

## Probe evidence (pins on the idea file)

- N = superbot-next `2c62a09` (`2c62a099973a2ee384af51e9a33074d9cd411002`,
  ls-remote-confirmed) — the standing `81b04bc` pin +1 commit, checker surface
  unchanged (the delta touches no `tools/` or workflows). S = superbot `b2b7fe0`
  (`b2b7fe0ce02a2a68cc18eac5242ab160b7b4330f`).
- Verified at N: 22 `tools/check_*.py` by tree list; `.github/workflows/ci.yml`
  red-gates 19 of them in the `set -e` loop (lines 50-56 read in full); NONE
  validates `path:line` doc cites. `check_doc_cites.py` exists in NEITHER repo.
  Nearest mechanisms: the kit's `check --strict` dead-relative-link check and
  `tools/check_amendments.py` rule 4 (spec_ref resolution, registry-scoped —
  external `superbot:` corpus roots advisory-skipped).
- Verified at S: `scripts/check_plan_staleness.py` still carries exactly its 3
  original rules, header verbatim "Warn-first: not wired into CI"; the class-4
  un-anchored-NN% rule remains unbuilt. Canonical idea
  (`docs/ideas/rebuild-design-cite-checker-2026-07-04.md`, Status still `ideas`):
  motivating bug = an audit cited a `disbot/core/contracts.py:48-52`
  `WorkflowResult` class that does not exist, and the fabrication propagated into
  a design work-list.
- Panel not escalated: process head, reversible call (README battery panel rule).

## Verification

`python3 bootstrap.py check --strict` green on the final tree immediately before
push (branch FINAL at open — the heartbeat rides the follow-up PR per the
arm-at-open race recipe, the #198/#201/#206/#212 chain). PR number stamped
post-open per the never-guess rule.

**📊 Model:** fable-5 · one idea-file probe append (sim-ready flip + four
Grounding pins) + PROPOSAL 010 outbox append + one index re-badge + card + claim
clear (+ follow-up heartbeat); no code, no lane-file writes (Q-0260)

## 💡 Session idea

**Warn-first is where checkers go to sleep.** superbot's
`check_plan_staleness.py` has sat warn-only and un-CI-wired since 2026-07-03
(header verbatim at `b2b7fe0`: "Warn-first: not wired into CI"), and its class-4
extension is still unbuilt a week after being named — evidence that a NEW checker
should land with its gating decision already made, which is exactly what
PROPOSAL 010 buys: the sim pass rules warn-vs-red (with measured false-positive
rates) BEFORE the lane build, so `check_doc_cites.py` can ship red-gating on day
one instead of joining the warn-first graveyard.

## ⟲ Previous-session review

Reviewed card: `.sessions/2026-07-11-probe-rebuild-critical-review-checkers.md`
(the #211 slice) against today's live reads. (1) Its N pin `81b04bc` still the
checker-surface truth — CONFIRMED: today's N HEAD `2c62a09` is `81b04bc` +1
commit touching no `tools/` or workflows. (2) "Class 4 still unbuilt at S" —
CONFIRMED at `b2b7fe0`: `check_plan_staleness.py` carries exactly its three
original rules. (3) Honest delta: the card (and the standing status note) said
"18-checker fleet" in the CI loop, but today's ci.yml loop names 19 —
off-by-one, not load-bearing (22 `tools/check_*.py` on disk both days).

## Handoff → next wake

- **WRAP-UP MODE** (owner directive relayed by the coordinator 2026-07-11):
  project closing for archive. TOP-5 ALL FIVE heads now consumed (this slice
  consumed item 4, the last open head). NO follow-on slices from this session;
  the re-rank and close-out belong to the wrap-up session.
- Open externals: PROPOSAL 009 + PROPOSAL 010 verdict fan-in still owed by
  sim-lab.
