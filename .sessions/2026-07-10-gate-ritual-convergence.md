# Session — fleet slice: gate↔ritual convergence (substrate-gate runs preflight.py, PR #18)

> **Status:** `complete`
> **Model/time:** 2026-07-10 ~21:00Z (worker slice; idea origin: PR #16 session card 💡,
> `.sessions/2026-07-10-preflight-wrapper.md` @ `68c3d2a` — "Gate↔ritual convergence")

## What this session did

- Claimed `ideas/fleet/` + the gate workflow (`claims/slice-gate-ritual-convergence.md`,
  flat filename per `claims/README.md`; cleared in this close-out commit).
- **Captured + probed (battery v0):** the PR #16 card's standing gate↔ritual-convergence
  candidate → `ideas/fleet/gate-ritual-convergence-2026-07-10.md`. Verdict:
  **park(built-here — `substrate-gate.yml` non-control lane → `scripts/preflight.py`,
  this PR)** — repo-internal PROCESS wiring, smallest slice is one YAML step, cheaper
  to build than to route (README § probe-battery shortcut, first used by PR #2);
  state advanced to `historical(#18)` in this close-out, nothing routed to sim-lab.
- **Built the slice:** ONE step inserted in `substrate-gate.yml`'s non-control lane —
  `run: python3 scripts/preflight.py`, between `setup-python` and the session-card
  gate step. The gate previously ran ONLY the kit check on non-control diffs; now it
  runs the same four-check wrapper the wakes run, so `scripts/preflight.py::CHECKS`
  is the single source of truth for the check list. Preserved verbatim: workflow
  name `substrate-gate` + job id `substrate-gate` (the owner-configured required
  check context — renamed NOTHING), both triggers (`pull_request` + push-to-main),
  the control-only fast lane (still short-circuits green after
  `check --strict --status-only`), and the session-card gate step (the wrapper
  deliberately does not subsume `--require-session-log`; its `--status-only` leg
  harmlessly overlaps the full `check --strict`).
- **CI-cleanliness check on the wrapper:** stdlib-only, report-only, no git-state or
  interactive input; the one network leg is `check_sections.py`'s manifest fetch
  (raw.githubusercontent.com, 30s timeout) — reachable from Actions runners, same
  exposure the wakes already carry. No adaptation needed.
- **Live-fire:** this PR is the test — the reworked gate ran on this PR's own
  `pull_request` event (result recorded in the PR checks; merge was on-green per
  README § Landing conventions, PR READY, never draft, no review wait).
- **No outbox entry, no new proposal** — backpressure holds (depth 3, zero sim-lab
  pulls); non-proposal-generating by design.

### Local pre-push run (real output)

```
$ python3 scripts/preflight.py
check_sections: OK — 10 sections in sync with the manifest
preflight: PASS — check_sections (exit 0)
check_ideas: OK — 263 idea files conform to the README grammar
preflight: PASS — check_ideas (exit 0)
check_ideas: OK — outbox proposals and sim-ready ideas are consistent
preflight: PASS — check_ideas --outbox (exit 0)
check: control-status check passed (--status-only).
preflight: PASS — bootstrap check --strict --status-only (exit 0)
preflight: OK — all 4 checks green
(exit 0)
```

- **📊 Model:** (worker slice, model id withheld per coordinator directive) · high ·
  one workflow step + idea capture/probe + docs

## 💡 Session idea

**Preflight seam graduation to substrate-kit** — the convergence step lives in a
KIT-OWNED file (`substrate-gate.yml`'s own header: adopt/upgrade regenerates it in
place), so every `bootstrap upgrade` will clobber it and the upgrade session must
re-apply one step. Guard recipe (until graduated): after any `bootstrap upgrade`,
diff `substrate-gate.yml` for the `wake preflight` step and re-insert it between
`setup-python` and the card-gate step (anchors: `scripts/preflight.py::CHECKS`, the
step comment names the idea file); test = the upgrade PR's own gate run must show
the preflight step executing. Durable fix: the kit's planted gate grows a native
"lane-local preflight" seam (run `scripts/preflight.py` if it exists) — that is a
substrate-kit PROCESS idea (the wrapper probe's Q2 graduation axis), proposal-shaped,
so it waits out backpressure.

## ⟲ Previous-session review

The PR #16 card's 💡 scoped this exact slice; its guard recipe — point the gate's
non-control lane at `python3 scripts/preflight.py` plus its existing
`--require-session-log` full check, anchors `scripts/preflight.py::CHECKS` + the
gate's run steps, test = a PR that reds exactly one wrapped check must red the gate —
was consumed as written, zero re-derivation. One scoping delta, resolved forward: the
💡's test (plant a violation, watch the gate red) was replaced by the cheaper
equivalent live-fire this PR gives for free — the reworked gate running green on its
own `pull_request` event proves the wire; the red path was already proven locally by
the wrapper's own synthetic-violation run (PR #16 card) and the gate step inherits
its exit code mechanically (`run:` fails on nonzero). One discovered fact worth the
record: the gate was not *duplicating* the wrapper's check list — it was
under-running it (only the kit check gated merges); convergence therefore *added*
enforcement rather than de-duplicating commands.

## Handoff → next wake

Nothing to babysit: no outbox proposal (backpressure), claim cleared, gate converged
once #18 merges. Post-merge, the push-to-main gate run executes the wrapper on every
merge commit — a manifest change adding an active lane now reds main until the
section exists (intended; that red is the next wake's work order). Next wake: normal
loop — inbox first; ripest non-proposal slices remain substrate-kit first batch,
harvest freshness checker, second-lane harvest, contract-grooming micro-slice, or
the 💡 above once backpressure lifts.
