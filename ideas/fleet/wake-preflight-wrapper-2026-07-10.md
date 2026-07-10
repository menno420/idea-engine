# Wake-preflight wrapper — one command for the whole preflight ritual

> **State:** park(built-here — `scripts/preflight.py`, this PR)
> **Class:** process · **Target:** `menno420/idea-engine` (this repo's own wake ritual — built here, see report Q7)

**Origin:** the PR #2 session card's 💡 (`.sessions/2026-07-10-section-sync-checker.md`
@ `583a81c`, "Wake-preflight wiring") — flagged the moment `scripts/check_sections.py`
existed; re-flagged with a full guard recipe once the ritual grew to three commands
(PR #13 card 💡, `.sessions/2026-07-10-outbox-check.md`, and the standing heartbeat
`notes:` line "wake-preflight wiring").

**The idea:** a stdlib-only `scripts/preflight.py` that runs the whole wake/pre-push
preflight in sequence — `check_sections.py` (partition), `check_ideas.py` (contents),
`check_ideas.py --outbox` (outbox↔ideas integrity), `bootstrap.py check --strict
--status-only` (control status gate) — printing one PASS/FAIL line per check and
exiting with the worst (max) exit code. The ritual is currently enforced by nothing
but session discipline across four separate commands; the wrapper makes "is the tree
sane?" a one-command answer.

## Probe report (v0, 2026-07-10)

**1. What is this really?**
Glue, honestly — four already-green checkers behind one entry point. Its value is not
new checking but ritual compression: every wake and every pre-push now has a single
command whose exit code aggregates the whole preflight, so "I ran the ritual" stops
meaning "I remembered all four commands". The same move as `check_sections.py` →
`check_ideas.py` one level up: those collect checks, this collects the checkers.

**2. What is the possibility space?**
Four axes: **membership** (today's four checks → future checkers auto-join by editing
one loud list → discovery by convention, e.g. every `scripts/check_*.py`); **surfaces**
(manual wake command → the `substrate-gate.yml` non-control lane calls the wrapper
instead of enumerating checks → a `bootstrap.py check` seam); **reporting** (PASS/FAIL
lines → `--quiet` summary-only → machine-readable JSON for a fleet-manager sweep);
**parameterization** (this repo's hardwired list → a kit-graduated generic runner —
same graduation path `check_sections.py`'s probe Q2 named). Each later point is its
own idea; none blocks the first.

**3. What is the most advanced capability reachable by the simplest implementation?**
A ~60-line stdlib wrapper turns the preflight from a discipline into an invariant:
worst-exit aggregation means one red check reds the whole run — a partial ritual can
no longer look green. Cheapest possible because the checkers were born composable
(clean 0/1/2 exits, no shared state); the wrapper just sequences and maxes.

**4. What breaks it?**
- **List drift** — a fifth checker lands and nobody adds it to the wrapper; the ritual
  silently shrinks back to discipline for that check. Mitigation: the check list is one
  loud constant at the top with a co-edit comment naming `control/README.md`.
- **Scoped bootstrap leg** — the wrapper runs `--status-only` (the control fast-lane
  gate), not the full `check --strict`; the full-suite verify before push stays its own
  README-mandated command. A session that treats the wrapper as covering the full kit
  check over-trusts it — the README line added in this PR keeps both named.
- **Child crash ≠ pass** — a checker that cannot even start must not vanish; the
  wrapper maps `OSError` to exit 2, fail-loud.
- **Network leg** — `check_sections.py` fetches the live manifest; offline wakes red
  the wrapper on infrastructure, not tree state (that check's own `--manifest` escape
  hatch exists, unplumbed here — possibility-space, not day-0).

**5. What does it unlock?**
Every future wake (and any sibling worker's ship ceremony) preflights in one command
with one honest exit code; the standing heartbeat `notes:` reminder about the
"THREE-command ritual" retires; and CI convergence becomes possible — the gate
workflow can one day call the same wrapper the wakes run, killing enumeration drift
between CI and ritual (Q2's surfaces axis).

**6. What does it depend on?**
The four checkers keeping their clean 0/1/2 exit contract (all do today — verified
live in this PR); python3 stdlib `subprocess` only; the same network reachability
`check_sections.py` already needs. Nothing cross-lane, nothing sim-checkable.

**7. Which lane should build it?**
**idea-engine — this repo, directly.** It sequences this repo's own scripts against
this repo's own ritual; only this repo's sessions write here (Q-0260). Not
substrate-kit yet: the check list is this repo's contract (same reasoning as both
prior scripts/ probes); the generic runner (Q2) could graduate later as its own idea.

**8. What is the smallest shippable slice?**
`scripts/preflight.py` exactly as described — ~60 lines, stdlib only, hardwired
four-check list, worst-exit aggregation, one PASS/FAIL line per check — plus one
README line naming it. Cheaper to build than to route, so it ships **in this same
PR** (README § probe-battery shortcut, first used by PR #2), run live over this tree
with real output in the session card.

**Recommendation: park(built-here — `scripts/preflight.py`, shipped in this PR)** —
rationale: repo-internal PROCESS glue whose smallest slice is a trivial stdlib
sequencer; nothing routes to sim-lab (its correctness is settled by running it, which
this PR does — and backpressure holds regardless: outbox depth 3, zero pulls, no
proposal appended), so per the README shortcut the state advances to
`historical(<this PR>)` on merge.
