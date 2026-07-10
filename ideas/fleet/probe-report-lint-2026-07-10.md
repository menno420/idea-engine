# Probe-report lint — idea-grammar checker for the ideas tree

> **State:** park(built-here — `scripts/check_ideas.py`, this PR)
> **Class:** process · **Target:** `menno420/idea-engine` (this repo's own tree — built here, see report Q7)

**Origin:** the first probe session's 💡 (`.sessions/2026-07-10-first-probe.md`) — that
session's own probe named "confident padding" as the battery's failure mode and proposed
a shape-checker as the cheapest guard; the section-sync-checker probe (Q2/Q5,
`ideas/fleet/section-sync-checker-2026-07-10.md`) named this idea as the sibling that its
`scripts/` pattern sets up.

**The idea:** a stdlib-only `scripts/check_ideas.py` that lints `ideas/` against the
README idea grammar (README § Idea file grammar + § The probe battery). Checks, grounded
in the tree at capture time (240 idea files across 10 sections):

- **filename** — `ideas/<section>/<slug>-YYYY-MM-DD.md` (section `README.md` exempt);
- **state line** — present, and one of the legal states: `captured | probed | sim-ready |
  parked(<reason>) | park(built-here — <what shipped>) | rejected(<reason>) |
  historical(<merged PR>)` (the park(built-here) form per PR #6's grammar addition,
  reference use in PR #2);
- **probe reports** — a file carrying a `## Probe report` section must answer all 8
  battery questions and end in exactly ONE legal recommendation
  (`sim-ready / park / reject / needs-more-grooming`, park optionally `(built-here — …)`);
  and a state of `probed`/`sim-ready` without a probe report is the half-probe the
  first-probe 💡 was aimed at;
- **harvested link-index entries** — a file declaring a canonical idea elsewhere must
  carry the canonical `https://github.com/…` link (README § Idea file grammar: indexed by
  link, never mass-copied).

Report-only, exit 1 on violations, usable as a wake preflight next to
`scripts/check_sections.py`.

## Probe report (v0, 2026-07-10)

**1. What is this really?**
A shape-checker for the pipeline's core artifact. Every downstream hop — outbox proposal,
sim-lab pull, manager routing — consumes idea files and trusts their state lines; the
grammar is currently enforced by nothing but session discipline. This is the same move as
`check_sections.py` one level down: that script guards the *partition* (directories), this
guards the *contents* (files). It cannot judge honesty (a fluent fabricated answer passes),
but it kills silent half-probes: a `sim-ready` state with no probe report, a probe report
missing questions, or two recommendations in one report.

**2. What is the possibility space?**
Four axes: **strictness** (shape-only → cross-checks like "sim-ready idea must have an
outbox PROPOSAL naming it" → semantic lint via an agent pass); **integration** (manual
script → wake-preflight convention → CI gate step in `substrate-gate.yml` → a
`bootstrap.py check` seam); **scope** (this repo's grammar → parameterized grammar for any
fleet repo with an ideas dir — a substrate-kit graduation candidate, same as
`check_sections.py` Q2 noted); **coverage** (state+filename+probe+link today → Class/Target
line, section README index completeness, outbox↔idea link integrity later). Each later
axis point is its own idea; none blocks the first.

**3. What is the most advanced capability reachable by the simplest implementation?**
A ~150-line stdlib script gives every wake (and CI, if wired) a one-command answer to "does
the whole tree still parse as the contract says?" — across 240 files, which no prose
review re-reads. The most advanced part is cheap because the grammar is already rigid:
state lines have one byte-form (`> **State:** …`), battery questions are numbered 1–8, the
recommendation has one bold form. Regexes over that are near-zero ambiguity — the
convention was born checkable, this just collects the check.

**4. What breaks it?**
- **Grammar drift without co-edit** — README grammar changes (a new state, a battery v1
  with 9 questions) silently red the linter or, worse, a loosened regex silently passes
  new violations. Mitigation: the legal-state list and question count live as loud
  constants at the top of the script, one edit per grammar change.
- **Shape ≠ substance** — it validates form only; "confident padding" (the battery's own
  named failure mode) passes untouched. Honesty stays enforced downstream (sim-lab,
  manager) — this is a floor, not a judge.
- **Heuristic link-index detection** — "is this file a harvested link-index?" is inferred
  from the `Canonical idea` marker text; a harvest that phrases it differently escapes the
  canonical-link check (fail-open on that one check, loud on the other three).
- **False positives on legitimate prose** — a probe report *quoting* a recommendation line
  verbatim would double-count; the tree today has none, and the check counts only the
  exact bold byte-form at line start.

**5. What does it unlock?**
Trustable state lines for the outbox → sim-lab → manager flow (a `sim-ready` in the tree
becomes machine-checked to at least carry a full probe); a wake preflight pair
(`check_sections.py` + `check_ideas.py` = partition + contents) that makes "is the tree
sane?" a two-command ritual; and the precondition for any future auto-indexing or
outbox-integrity checker (you can only cross-check files that parse).

**6. What does it depend on?**
The README grammar staying byte-stable in its markers (`> **State:**`, `## Probe report`,
`**N.` question numbering, `**Recommendation:`) — all six existing probe/report artifacts
already conform; python3 stdlib (the kit interpreter, `substrate.config.json`); no network
(unlike `check_sections.py` it reads only this tree, so it runs offline and in CI free).

**7. Which lane should build it?**
**idea-engine — this repo, directly.** It lints this repo's own tree against this repo's
own README, and only this repo's sessions write here (Q-0260); no other lane can even land
a fix it reports. Not substrate-kit yet: the grammar is this repo's contract; the
parameterized version (Q2's scope axis) could graduate later as its own idea.

**8. What is the smallest shippable slice?**
`scripts/check_ideas.py`, report-only, exit 1 on violations — ~150 lines, stdlib only,
mirroring `check_sections.py`'s shape. Cheaper to build than to route (the
README § probe-battery shortcut, first used by PR #2), so it ships **in this same PR**,
run over the full 240-file tree with real output in the session card.

**Recommendation: park(built-here — `scripts/check_ideas.py`, shipped in this PR)** —
rationale: repo-internal PROCESS tooling whose smallest slice is a trivial stdlib
reporter; nothing routes to sim-lab (no reproducible question exists worth a sim cycle —
the script's correctness is settled by running it, which this PR does), so per the README
shortcut the state advances to `historical(<this PR>)` on merge. Proposal deferred —
outbox backpressure (moot here: built-here routes nothing to the outbox by design, and
outbox depth is 3 with zero sim-lab pulls, so no proposal is appended either way).
