# Post-holdout re-seal protocol — pre-register the NEXT holdout before the current one is spent

> **State:** captured
> **Class:** process · **Target:** `menno420/trading-strategy`

## Problem

The lane's single most valuable asset — its pre-registered one-shot holdout
(`HOLDOUT_START = 2025-01-09`, code-enforced at the loader and both ledger choke
points) — is about to be consumed: ORDER 008 (P0, Q-0262.2) authorizes the P5
evaluation now that ORDER 007's significance bar is done, and the manifest row shows
that exact 007→008 sequencing live. The moment P5 runs, every committed bar is
consumed data. The repo has **no doctrine for what becomes the next holdout** —
QUEUE.md's next-session brief says "No other undone roadmap items" — so the first
post-P5 experiment would either touch unsealed data or stall the lane.

## Idea

Pre-register the successor holdout **before** P5 executes, in the same
write-the-verdict-rules-before-the-numbers style as `docs/p5-holdout-protocol.md`:
new `HOLDOUT_START` = the current committed data end; caches extended forward only
under the new seal; the existing rails (the `load_ohlcv` filter, the
`data_end < HOLDOUT_START` ledger refusal, the CI audit over `experiments/index.jsonl`
— all already parameterized per `docs/holdout-enforcement.md`) re-pointed at the new
boundary in one PR. The protocol doc, not the code, is the deliverable: unlock
conditions, minimum accrual period before any future unlock, and how post-P5
subjects re-enter the pipeline.

## Grounding

- Manifest trading-strategy row: "holdout SEALED … with unlock ORDER 008 landed @ fd5e9fe (Q-0262.2, sequences AFTER ORDER 007); ORDER 007 … in flight"
  ([superbot @ `6f283b9`](https://raw.githubusercontent.com/menno420/superbot/6f283b91160546af2864a0fd30b6e2d81b148a8f/docs/eap/fleet-manifest.md), fetched 2026-07-10).
- Lane reality @ [`e713abb`](https://github.com/menno420/trading-strategy/tree/e713abb125766db2b1562980369a11290b8772b9):
  `control/status.md` (007 DONE, 008 acked-not-executed, "NEXT: ORDER 008 … FRESH dedicated session"),
  `docs/succession/QUEUE.md` item 8 + next-session brief ("No other undone roadmap items"),
  `docs/holdout-enforcement.md` (the rails to re-point).

**Why now:** pre-registration only counts before the numbers exist — the window to
seal the successor holdout closes the moment the ORDER 008 session runs P5.
