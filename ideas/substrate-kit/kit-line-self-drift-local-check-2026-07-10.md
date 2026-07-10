# Local `kit:` self-drift check — kill the dominant DRIFT class at its source

> **State:** captured
> **Class:** product · **Target:** `menno420/substrate-kit`

## Problem

The kit's brand-new fleet scanner (`bootstrap currency`, shipped kit-lab PR #133)
just measured the fleet's version truth for the first time — and **7 of 10 registry
rows are DRIFT**, of which **5 are the exact same class**: the repo's heartbeat
`kit:` self-report lags its own tree after an upgrade (superbot-next, websites, and
gba-homebrew all claim v1.6.0 over a v1.7.0 tree; fleet-manager claims v1.4.0;
superbot-games' lane heartbeats claim v1.2.0). The contract already says "update it
in the same session as every `bootstrap upgrade`" (planted `control/README.md`,
§ status format) — it is hortatory, and measurably not happening. The fleet scan
catches it, but only agent-side, only on kit-lab's cadence, and only *after* the
stale claim has misled a manifest re-stamp or a coordinator read.

## Idea

Give every adopter a **zero-network local drift check**: a `check --strict` finding
(or Stop-hook advisory first, strict later) that compares the repo's OWN three
version artifacts against each other — vendored `bootstrap.py` stamped header
(primary truth), `substrate.config.json` `kit_version` pin, and the `kit: v<X.Y.Z>`
line in each declared heartbeat file. All three already exist in the committed tree
(`adopt` plants all of them — kit-lab's own finding, its 18:40Z heartbeat note 2),
so the check needs no fetch and runs under the same gate that already validates the
heartbeat. `bootstrap upgrade` completes the loop by printing the exact heartbeat
line to paste. The fleet scanner stays the cross-repo auditor; this makes the
dominant drift class impossible to *commit* rather than merely visible after the
fact.

## Grounding

- Generated registry + drift report (5 self-report-lag rows of 7 DRIFT) @
  [`7e600c6`](https://raw.githubusercontent.com/menno420/substrate-kit/7e600c6f4b9e0e685d7d5a11aed37d435d009dae/docs/adopters.md)
  (fetched 2026-07-10 ~20:55Z; scan generated 20:36:19Z the same day).
- The three-artifact finding + scanner design (tree = truth, self-report = claim) @
  [`7e600c6`](https://raw.githubusercontent.com/menno420/substrate-kit/7e600c6f4b9e0e685d7d5a11aed37d435d009dae/control/status.md)
  (kit-lab §6.3 close heartbeat, notes 2–3).
- The hortatory contract this would make enforcing: this repo's planted
  `control/README.md` § `status.md` format ("update it in the same session as every
  `bootstrap upgrade`") — and this repo's own in-sync `kit: v1.7.0` line as the
  existence proof that the check is satisfiable (`control/status.md`,
  `substrate.config.json`).

**Why now:** the currency checker made the class visible fleet-wide *today* — the
cheapest moment to close the loop is while the drift report is one slice old and
five repos would flip clean on their very next upgrade session.
