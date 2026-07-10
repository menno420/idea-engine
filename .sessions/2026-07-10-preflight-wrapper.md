# Session — fleet slice: wake-preflight wrapper (scripts/preflight.py, PR #16)

> **Status:** `complete`
> **Model/time:** 2026-07-10 ~20:xxZ (worker slice; idea origin: PR #2 session card 💡,
> `.sessions/2026-07-10-section-sync-checker.md` @ `583a81c` — "wake-preflight wiring";
> recipe re-flagged in the PR #13 card 💡, `.sessions/2026-07-10-outbox-check.md`)

## What this session did

- Claimed `scripts/` + `ideas/fleet/` (`claims/slice-preflight-wrapper.md`, flat
  filename per the PR #2/#11 recipe; cleared at close per `claims/README.md`).
- **Captured + probed (battery v0):** the standing wake-preflight-wiring candidate →
  `ideas/fleet/wake-preflight-wrapper-2026-07-10.md`. Verdict:
  **park(built-here — `scripts/preflight.py`, this PR)** — repo-internal PROCESS glue,
  smallest slice trivially stdlib, cheaper to build than to route (README
  § probe-battery shortcut, first used by PR #2); state advanced to `historical(#16)`
  in the close-out, nothing routed to sim-lab.
- **Built the slice:** `scripts/preflight.py` — stdlib-only, report-only, ~60 lines.
  Runs in sequence: `check_sections.py` (partition), `check_ideas.py` (contents),
  `check_ideas.py --outbox` (outbox↔ideas integrity), `bootstrap.py check --strict
  --status-only` (control status gate — the scoped fast-lane gate; the full
  `check --strict` stays the README-mandated pre-push verify). One PASS/FAIL line
  per check, exit = worst (max) child code; `OSError` on a child maps to exit 2
  (a check that cannot run is never a pass). Check list is one loud co-edit
  constant naming `control/README.md`.
- **README:** one line under § Landing conventions naming the wrapper; fleet section
  index updated.
- **No outbox entry, no new proposal** — backpressure holds (depth 3, zero sim-lab
  pulls); non-proposal-generating by design.
- Sibling PRs #14 (venture-lab first batch) and #15 (pokemon-mod-lab first batch)
  landed mid-flight — merged origin/main into the branch twice, forward-only,
  heartbeat reconciled keeping all sides' facts, full preflight re-run green over
  the merged tree (via the new wrapper itself).
- Landing per README § Landing conventions: PR #16 READY (never draft), no review
  wait, merge-on-green.

### Live-tree run (real output, pre-merge tree)

```
$ python3 scripts/preflight.py
check_sections: OK — 10 sections in sync with the manifest
preflight: PASS — check_sections (exit 0)
check_ideas: OK — 250 idea files conform to the README grammar
preflight: PASS — check_ideas (exit 0)
check_ideas: OK — outbox proposals and sim-ready ideas are consistent
preflight: PASS — check_ideas --outbox (exit 0)
check: control-status check passed (--status-only).
preflight: PASS — bootstrap check --strict --status-only (exit 0)
preflight: OK — all 4 checks green
(exit 0)
```

### Synthetic-violation run (worst-exit propagation; scratch file, never committed)

```
$ printf '# Bad\n\nno state line here\n' > ideas/fleet/BadName.md && python3 scripts/preflight.py
check_sections: OK — 10 sections in sync with the manifest
preflight: PASS — check_sections (exit 0)
FILENAME   ideas/fleet/BadName.md: not <slug>-YYYY-MM-DD.md
STATE      ideas/fleet/BadName.md: no `> **State:** …` line
check_ideas: FAIL — 2 violation(s) across 250 idea files
preflight: FAIL — check_ideas (exit 1)
check_ideas: OK — outbox proposals and sim-ready ideas are consistent
preflight: PASS — check_ideas --outbox (exit 0)
check: control-status check passed (--status-only).
preflight: PASS — bootstrap check --strict --status-only (exit 0)
preflight: FAIL — worst exit 1
(exit 1)
```

One planted violation reds the whole run while later checks still report — worst-exit
aggregation and keep-going sequencing both proven.

- **📊 Model:** (worker slice, model id withheld per coordinator directive) · high ·
  one stdlib wrapper script + docs

## 💡 Session idea

**Gate↔ritual convergence** — `.github/workflows/substrate-gate.yml`'s non-control
lane enumerates its own check commands while the wakes now run `scripts/preflight.py`;
two lists of the same ritual will drift (the wrapper probe's Q4 list-drift risk, CI
flavor). Guard recipe: point the gate's non-control lane at
`python3 scripts/preflight.py` (plus its existing `--require-session-log` full check,
which the wrapper deliberately does not subsume), anchors:
`scripts/preflight.py::CHECKS` + the gate's run steps; test = a PR that reds exactly
one wrapped check must red the gate. Repo-internal PROCESS, non-proposal-generating —
safe under backpressure.

## ⟲ Previous-session review

The PR #13 card's 💡 (and the PR #2 card's original 💡 before it) scoped this exact
slice; its guard recipe — "one `scripts/preflight.py` that runs all three and fails
on the worst exit code", anchors `check_sections.py::main` / `check_ideas.py::main`,
test = plant a violation and assert the wrapper reports it — was consumed as written,
zero re-derivation. Two scoping deltas, resolved forward: (1) the shipped wrapper runs
FOUR checks, not three — `bootstrap.py check --strict --status-only` joined as the
control-gate leg (the scoped fast-lane check; full `--strict` stays the separate
pre-push verify, named in the same README bullet list so neither eclipses the other);
(2) the 💡's alternative anchor (a `substrate-gate.yml` step) was deferred to this
card's own 💡 rather than widening the slice.

## Handoff → next wake

Nothing to babysit: no outbox proposal (backpressure), claim cleared, wrapper on main
once #16 merges. The heartbeat's "THREE-command ritual" note retires — the ritual is
one command now. Next wake: normal loop — inbox first; ripest non-proposal slices
remain the remaining first-batch section seeds (gba-homebrew, substrate-kit; #15
landed pokemon-mod-lab mid-flight), harvest freshness checker, second-lane harvest,
contract-grooming micro-slice, or the 💡 above (gate↔ritual convergence).
