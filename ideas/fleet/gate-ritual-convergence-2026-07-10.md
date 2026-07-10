# Gate↔ritual convergence — substrate-gate runs the same preflight the wakes run

> **State:** historical(#18 — probed + built in the same PR, `substrate-gate.yml` non-control lane → `scripts/preflight.py`)
> **Class:** process · **Target:** `menno420/idea-engine` (this repo's own CI gate — built here, see report Q7)

**Origin:** the PR #16 session card's 💡 (`.sessions/2026-07-10-preflight-wrapper.md`
@ `68c3d2a`, "Gate↔ritual convergence") — flagged the moment `scripts/preflight.py`
existed: the wrapper probe's Q4 named list-drift as the failure mode, and its Q5/Q2
named CI convergence as the unlock. Battery reference: superbot
`docs/ideas/idea-probe-brainstorm-simulator-2026-07-10.md` (cited by path; read-only
lane) + README § The probe battery.

**The idea:** `.github/workflows/substrate-gate.yml` and the wake/pre-push ritual
should converge on `scripts/preflight.py` as the **single source of truth for the
check list**. Today the wakes run four checks through the wrapper
(`check_sections` · `check_ideas` · `check_ideas --outbox` · `bootstrap check
--strict --status-only`), but the gate's non-control lane runs only the kit check —
a PR that breaks the section partition or the idea grammar can merge green, and any
future fifth check must be added in two places or the lists drift. Fix: the gate's
non-control lane runs `python3 scripts/preflight.py` (one loud list,
`scripts/preflight.py::CHECKS`), keeping its existing session-card gate — the full
`check --strict --require-session-log` leg the wrapper deliberately does not subsume
— and keeping the control-only fast lane exactly as is.

## Probe report (v0, 2026-07-10)

**1. What is this really?**
De-duplication of authority, not new checking: the ritual already exists
(`scripts/preflight.py`, PR #16) and the gate already exists (kit-planted
`substrate-gate.yml`); this makes the gate *call* the ritual instead of maintaining
its own private notion of "the checks". After it, "what does CI check?" and "what
does a wake check?" have the same answer by construction — the wrapper's `CHECKS`
constant becomes the one place the ritual is defined.

**2. What is the possibility space?**
Three axes: **coverage** (today: non-control lane runs the wrapper → later: the
control fast lane could also route through a `preflight --status-only` flag instead
of naming `bootstrap.py` directly → later still: the card gate itself joins the
wrapper behind a `--ci` flag); **direction** (this repo's gate calls this repo's
wrapper → the pattern graduates to substrate-kit so every adopter's gate calls a
lane-local preflight seam — same graduation path the wrapper probe's Q2 named);
**reporting** (per-check PASS/FAIL lines in the CI log → step-summary markdown →
matrix-per-check for parallel CI). Each later point is its own idea; the first point
alone kills the drift.

**3. What is the most advanced capability reachable by the simplest implementation?**
A one-step YAML insertion makes every future checker CI-enforced *by default*: add a
check to `preflight.py::CHECKS` (one edit, the constant's own co-edit comment) and
both the wakes and the required merge gate pick it up with zero workflow edits. The
enforcement surface grows for free forever after a ~10-line diff.

**4. What breaks it?**
- **KIT-OWNED overwrite** — `substrate-gate.yml`'s own header says adopt/upgrade
  regenerates it in place; a `bootstrap upgrade` will clobber the preflight step.
  Known, accepted, and guarded: the loss mode is loud (the next gate↔ritual drift is
  visible in the workflow diff of the upgrade PR itself), and the re-apply is this
  same one-step insertion. Guard recipe recorded in this slice's session card; the
  durable fix is the Q2 graduation (kit ships the seam natively).
- **Network leg in CI** — `check_sections.py` fetches the live manifest
  (raw.githubusercontent.com, 30s timeout); a raw-path outage reds the gate on
  infrastructure, not tree state. Same exposure the wakes already carry; the
  `--manifest` escape hatch exists unplumbed (possibility space, not day-0).
- **Double status check** — the wrapper's `--status-only` leg re-runs what the card
  gate's full `check --strict` also covers; harmless (seconds, report-only) but a
  reader could think the lanes differ more than they do — the step comment names it.
- **Semantics widening on push-to-main** — the push run now also reds if the
  manifest sprouts a new active lane before the section exists; that is *intended*
  (the partition invariant becomes enforced, not just observed), but main can go red
  through no fault of the merged PR. Acceptable: that red is exactly the signal the
  next wake needs.

**5. What does it unlock?**
The gate stops under-running the ritual (grammar/partition/outbox violations become
merge-blocking instead of wake-time-only); list drift between CI and ritual becomes
structurally impossible while the step survives; and every future checker lands
CI-enforced with one edit (Q3). It also produces the first live proof that the
wrapper is CI-clean — evidence the Q2 kit graduation will want.

**6. What does it depend on?**
`scripts/preflight.py` on main (merged, PR #16); its children keeping clean 0/1/2
exits (verified live in PR #16); Actions runners reaching raw.githubusercontent.com
(already true — the runner fetches the repo itself from github.com); the
owner-configured required context staying `substrate-gate` / job `substrate-gate`
(this slice renames NOTHING). Nothing cross-lane, nothing sim-checkable.

**7. Which lane should build it?**
**idea-engine — this repo, directly.** It wires this repo's own workflow to this
repo's own wrapper; only this repo's sessions write here (Q-0260). Not substrate-kit
yet: the kit-owned-file tension (Q4) is real, but graduating the seam upstream is a
separate, larger idea — the local convergence is needed now and proves the pattern.

**8. What is the smallest shippable slice?**
One workflow step: in `substrate-gate.yml`'s non-control lane, insert
`run: python3 scripts/preflight.py` between `setup-python` and the session-card gate
step — preserving the workflow name, the job id, both triggers, the control fast
lane, and the card gate verbatim — plus this idea file and its card. Test: the PR
carrying the change must itself run the reworked gate green on its own
`pull_request` event (live-fire, recorded in the card). Cheaper to build than to
route, so it ships **in this same PR** (README § probe-battery shortcut, first used
by PR #2).

**Recommendation: park(built-here — substrate-gate.yml non-control lane now runs `scripts/preflight.py`, shipped in this PR)** —
rationale: repo-internal PROCESS wiring whose smallest slice is a one-step YAML
insertion, self-proving on its own PR's gate run; nothing routes to sim-lab (its
correctness is settled by the required check going green on this very PR — and
backpressure holds regardless: outbox depth 3, zero pulls, no proposal appended), so
per the README shortcut the state advances to `historical(<this PR>)` on merge.
