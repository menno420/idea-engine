# ideas/substrate-kit

> **Target lane:** `menno420/substrate-kit` (manifest-derived section — see README.md § Sections).

Ideas FOR this lane: files per the idea grammar, harvested lane-born ideas indexed by
link below. Claim this section (`claims/`) before working it.

## Index

- [`kit-line-self-drift-local-check-2026-07-10.md`](kit-line-self-drift-local-check-2026-07-10.md) — captured · product: zero-network `check --strict` finding comparing a repo's OWN three version artifacts (vendored dist header · config pin · heartbeat `kit:` line) — makes the fleet scan's dominant DRIFT class (5 of 7 rows @ adopters.md 7e600c6) impossible to commit instead of merely visible after the fact
- [`parallel-session-heartbeat-reconcile-2026-07-10.md`](parallel-session-heartbeat-reconcile-2026-07-10.md) — captured · process: the one-writer rule never named same-lane parallel sessions — codify the forward-only heartbeat-reconcile recipe (proven here across PRs #12/#15) in the planted control/README + a non-monotonic-stamp advisory, before continuous chaining spreads fleet-wide
- [`behind-stall-auto-updater-2026-07-10.md`](behind-stall-auto-updater-2026-07-10.md) — captured · product: committed `GITHUB_TOKEN` workflow (auto-merge-enabler's sibling) that update-branches armed-but-`behind` PRs on push to main — closes the residual the kit's own ⚑ OWNER-ACTION 11 files as an unclicked owner checkbox
- [`host-checkers-one-gate-2026-07-10.md`](host-checkers-one-gate-2026-07-10.md) — captured · product: `substrate.config.json` `extra_checks` seam so host checkers (this repo's three-command preflight ritual) run under the KIT-OWNED gate's one `check --strict` — one-gate doctrine at the host boundary, zero gate hand-edits

## Cross-links

Sibling-section ideas indexed **by link** (README § Idea file grammar — never duplicated;
rule source: PR #17 card):

- [`../superbot/seat-boot-verification-harness-2026-07-10.md`](../superbot/seat-boot-verification-harness-2026-07-10.md) — parked(routed) · probed 2026-07-10: the seat-boot `check_seat.py` harness parses the KIT-OWNED heartbeat grammar, so its probe's Q7 puts the parsing core on this lane (a remote-tree/heartbeat-parse seam — one grammar, one parser, kit-versioned; rhymes with `host-checkers-one-gate`) with only a thin operator wrapper in superbot `scripts/`; routing relayed to the manager via the idea-engine heartbeat notes — no sim-lab proposal (no simulator question)
- [`../superbot/project-capability-self-awareness-2026-07-10.md`](../superbot/project-capability-self-awareness-2026-07-10.md) — sim-ready · probed 2026-07-10 (batched with `session-start-capability-self-probe`, its agent-plane half): the fleet-internal mitigation is a kit-owned `bootstrap.py capabilities --probe` — this lane already plants the ledger it would regenerate (`adopt.py:66` CAPABILITIES.md.tmpl @ kit HEAD `415c37e`) and its `session-start` injection is the natural carrier for the agent-plane checklist (same one-grammar/one-parser logic as the seat-boot routing above); build gated on PROPOSAL 005's sim-lab verdict (is probe-regenerated capability truth honest across seat types → decides regenerate-whole-file vs annotate-per-seat schema)
