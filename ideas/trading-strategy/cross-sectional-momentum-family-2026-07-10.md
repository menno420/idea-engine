# Cross-sectional momentum family — the first post-holdout hypothesis class

> **State:** captured
> **Class:** product · **Target:** `menno420/trading-strategy`

## Problem

The lane has honestly falsified its opening hypothesis class: single-instrument
technical rules on the 8 committed tickers. P4 ran all 13 P2 subjects
cross-instrument with frozen params — **13/13 TRANSFER-FAILED** (13/99 pairs beat
B&H) — and ORDER 007's significance bar demoted the sole promotion (AAPL-donchian,
t = 0.42 < 1.64 at the most lenient K) to candidate, leaving **no candidate holding a
finding label**. After P5 spends the holdout, the roadmap is empty: more variants of
the falsified class would be p-hacking with extra steps, but the lane has no next
hypothesis class queued.

## Idea

A cross-sectional (relative) momentum family: rank the 8 committed tickers by
trailing return each rebalance, hold the top-k, vs. equal-weight buy-and-hold of the
same universe. This is a genuinely different hypothesis class — the signal is the
cross-section, not any single name's path, so the 13/13 single-name transfer failure
does not pre-judge it — and it is the most-replicated anomaly class in the
literature, exactly what an honest lab should test next. It needs one real engine
extension (portfolio-level positions across instruments; the current engine
backtests per-instrument), which is itself the capability every future multi-asset
family reuses. Variant count stays small and pre-declared (lookback × k ×
rebalance), run under the existing walk-forward + costs + ORDER 007 significance
discipline, on post-re-seal data only.

## Grounding

- Lane reality @ [`e713abb`](https://github.com/menno420/trading-strategy/tree/e713abb125766db2b1562980369a11290b8772b9):
  `docs/p4-transfer-results.md` via `docs/succession/QUEUE.md` item 7 (13/13
  TRANSFER-FAILED, pre-registered verdict rule), `control/status.md` (AAPL-donchian
  demotion math; "no candidate currently holds a finding label"),
  `docs/current-state.md` (per-instrument engine scope: config/data/engine/
  strategies are single-name).
- Manifest trading-strategy row: "P1–P5 prep DONE, PARKED GREEN"
  ([superbot @ `6f283b9`](https://raw.githubusercontent.com/menno420/superbot/6f283b91160546af2864a0fd30b6e2d81b148a8f/docs/eap/fleet-manifest.md), fetched 2026-07-10).

**Why now:** the lane goes idle the day P5 completes — queuing the next hypothesis
class now (and pre-declaring its variant budget before any new data is seen) is what
keeps the anti-overfitting discipline unbroken across the generation boundary.
