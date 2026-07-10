# Session — fleet slice: outbox↔ideas link-integrity mode for check_ideas.py (PR #13)

> **Status:** `complete`
> **Model/time:** 2026-07-10 ~21:xxZ (worker slice; idea origin: PR #11 session card 💡,
> `.sessions/2026-07-10-probe-report-lint.md` — the linter's Q2 coverage axis)

## What this session did

- Claimed `scripts/` + the `ideas/fleet/` note surface (`claims/slice-outbox-check.md`,
  flat filename per the PR #2/#11 recipe; cleared at close per `claims/README.md`).
- **Extended the historical fleet idea probe-report-lint (`historical(#11)`) without
  reopening it** — probe reports append-only, states forward-only, so the extension
  landed as a brief appended `## Extension note` in
  `ideas/fleet/probe-report-lint-2026-07-10.md` (probe report and state line untouched,
  citing this PR) — plus this card. No new idea file, no re-probe: the probe's own Q2
  already scoped this axis ("outbox↔idea link integrity later"), and the PR #11 card's
  💡 carried the guard recipe consumed here verbatim.
- **Built the slice:** `scripts/check_ideas.py --outbox [FILE]` (default
  `control/outbox.md`) — stdlib-only, report-only, exit 0/1/2 matching the existing
  modes (2 = missing outbox/tree, never a false clean). Checks per README § The outbox:
  - **PROPOSAL** — heading is `## PROPOSAL <nnn> · <ISO8601> · status: sim-ready`; all
    required fields present (`target:` / `idea:` / `question:` / `done-when:`);
    `depends:` OPTIONAL (PR #5 grammar).
  - **LINK** — every `idea:` link carries a this-repo `ideas/…` path (blob or raw form)
    that resolves to an existing file whose state is `sim-ready` — `historical(…)` also
    legal, because the outbox is append-only and states move forward only, so a proposal
    outlives its idea's advance to built.
  - **UNPROPOSED** — reverse pass: every `sim-ready` idea in the tree must be named by
    some proposal (kills the silent "sim-ready verdict that never reached the sim-lab
    pull surface").
  Grammar constants live at the top of the script under the same loud co-edit comment as
  the idea-grammar ones. `--ideas-dir` composes with `--outbox` for scratch-tree tests.
- **No outbox entry, no new proposal** — backpressure holds (depth 3, zero sim-lab
  pulls); this slice was chosen non-proposal-generating by design.
- Landing per README § Landing conventions: PR #13 READY (never draft), no review wait,
  merge-on-green.

### Live-tree run (real output)

```
$ python3 scripts/check_ideas.py --outbox
check_ideas: OK — outbox proposals and sim-ready ideas are consistent
(exit 0)
```

**Zero violations** — the 3 outbox proposals (001–003) all parse against the grammar,
each `idea:` link resolves to an existing idea file in state `sim-ready`, and the tree's
3 sim-ready ideas are exactly the 3 proposed ones. The reverse pass also confirms the
PR #11 built-here idea (`historical(#11)`) correctly has no proposal.

### Synthetic-violation smoke (every check fires; scratch tree, not committed)

```
$ python3 scripts/check_ideas.py --outbox <scratch>/outbox.md --ideas-dir <scratch>/ideas
PROPOSAL   PROPOSAL 002: heading not `## PROPOSAL <nnn> · <ISO8601> · status: sim-ready`
PROPOSAL   PROPOSAL 002: missing required field `done-when:`
LINK       PROPOSAL 003: linked idea file ideas/fleet/missing-idea-2026-07-10.md does not exist
LINK       PROPOSAL 004: linked idea ideas/fleet/not-ready-2026-07-10.md state 'captured' is not sim-ready (or historical(…))
UNPROPOSED ideas/fleet/orphan-simready-2026-07-10.md: state 'sim-ready' but no outbox PROPOSAL names it
check_ideas: FAIL — 5 outbox↔ideas violation(s)
(exit 1)
```

Planted: a malformed proposal (bad heading + missing `done-when:`), a proposal linking a
missing idea file, a proposal linking a `captured` idea, and an unproposed `sim-ready`
idea — all four classes fire. Missing-outbox path verified separately: exit 2 with
`check_ideas: no outbox file at …` on stderr.

### Preflights (green before push)

```
$ python3 scripts/check_sections.py
check_sections: OK — 10 sections in sync with the manifest
(exit 0)

$ python3 bootstrap.py check --strict
check: all checks passed.
(exit 0)

$ python3 scripts/check_ideas.py
check_ideas: OK — 245 idea files conform to the README grammar
(exit 0)

$ python3 scripts/check_ideas.py --outbox
check_ideas: OK — outbox proposals and sim-ready ideas are consistent
(exit 0)
```

- **📊 Model:** (worker slice, model id withheld per coordinator directive) · high · one
  stdlib script extension + docs

## 💡 Session idea

**Wake-preflight wiring** — the preflight is now a THREE-command ritual
(`check_sections.py` + `check_ideas.py` + `check_ideas.py --outbox`) enforced only by
session discipline. Guard recipe: one `scripts/preflight.py` (or a `substrate-gate.yml`
step) that runs all three and fails on the worst exit code — anchors:
`check_sections.py::main`, `check_ideas.py::main` (both already return clean 0/1/2), the
gate's non-control lane in `.github/workflows/substrate-gate.yml`; test = plant one
violation per script in a scratch tree and assert the wrapper reports all three.
Repo-internal PROCESS, non-proposal-generating — safe under backpressure.

## ⟲ Previous-session review

The PR #11 card's 💡 and the standing heartbeat both named this exact slice ("outbox↔idea
link-integrity extension of check_ideas.py (PR #11 card 💡)") — consumed as scoped, zero
re-derivation; the 💡's guard recipe (extend with `--outbox`, parse `## PROPOSAL` blocks'
`idea:` lines, test = plant a sim-ready idea with no proposal in a scratch tree) was
followed verbatim and all its named tests fire. One scoping delta, resolved forward: the
💡 offered a "proposal deferred — outbox backpressure" note as an alternative reverse-pass
exemption; the shipped check flags ALL unproposed sim-ready ideas unconditionally — the
simpler contract, and the live tree needed no exemption (deferred-by-backpressure ideas
so far took the built-here path instead). If a deferred-note exemption is ever needed, add
it at `check_outbox()`'s reverse pass with its own loud constant.

## Handoff → next wake

Nothing to babysit: no outbox proposal (backpressure), claim cleared, `--outbox` on main
once #13 merges. Next wake: normal loop — inbox first; ripest non-proposal slices remain
harvest freshness checker, second-lane harvest, superbot-next section seed, or the 💡
above (preflight wiring — glue over three existing green scripts).
