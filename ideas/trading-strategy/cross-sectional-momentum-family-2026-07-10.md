# Cross-sectional momentum family — the first post-holdout hypothesis class

> **State:** parked(overtaken-by-events — the lane self-served the exact family: Research Round 2 pre-registered it 2026-07-10 (PR #46, `8d0270f`) and executed it as R3 `xsec_momentum` the same day (PR #49, merge `9b13b8a`) — first portfolio lane, 3 KEEP dev-candidates / 3 KILL of 6; any path past dev-candidate is owner-gated by the round's own banner)
> **Class:** product · **Target:** `menno420/trading-strategy`
> **Grounding:** https://github.com/menno420/trading-strategy@6799a4c7d4f59cefd60cefd88eaadab944155db7 · fetched 2026-07-11T01:08:54Z (manifest row: behind)
> *(pin annotation: probe-time re-check pin — capture pin was `e713abb` (2026-07-10); manifest row @ superbot `4ccb631` still reads "P1–P5 prep DONE, PARKED GREEN … holdout SEALED … ORDER 007 … in flight; kit v1.1.0 (oldest pin)" while lane reality is holdout SPENT, orders 001–008 done, kit v1.7.1, paper lane operational, Research Round 2 pre-registered+executed+CLOSED — a full program-phase-plus behind; freshest wins: lane HEAD)*
> **Sequence:** after trading-strategy ORDER 008 (P5 spend) — constraint MET but the slot it guarded is CONSUMED: the lane pre-registered and ran this family itself (PRs #46–#50) between this capture and this probe.

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

## Probe report (v0, 2026-07-11)

*Probed 2026-07-11T01:09Z, single-pass per the README panel default (sim-lab VERDICT 002
— no ambiguity signal, no irreversible surface). Live-state recon FIRST, per the
expiry-aware ordering rule and the PR #25 lesson — this capture's "Why now" was a window
("the lane goes idle the day P5 completes"), so the probe's first act was a lane-HEAD
check. Lane HEAD `6799a4c` (ls-remote 2026-07-11T01:08:54Z), ahead of the capture pin
`e713abb`; superbot HEAD `4ccb631`. The re-check is the probe's decisive input: the lane
did NOT go idle — it pre-registered and executed this exact hypothesis class itself,
same day. This is the third live datapoint of the lane-self-served class (after
websites PR #79 / this repo's PR #49 card 💡, whose pre-probe live-check rule this probe
followed), and the second in this very section (post-holdout-reseal, PR #25).*

**Live state, with citations (all @ trading-strategy `6799a4c` unless noted):**

- **P5 holdout outcome** — `control/status.md`: "holdout: **SPENT** … The one-shot was
  consumed 2026-07-10 (run stamps 2026-07-10T1647Z); all 13 ledger rows carry
  `holdout_unlocked=true`"; verdict line: "primary donchian×AAPL×daily CONFIRMED by the
  mechanical §5 rule (Sharpe 0.759 > B&H 0.740) but t = 0.02 → remains a RULE-PASS
  candidate under the ORDER 007 significance rule, NOT a finding; secondaries 2/12
  HOLDOUT-BEAT (S5, S6) — chance-level vs the pre-registered null; 0 of 13 clears the
  significance bar even at the most lenient K=1." Program complete, final report on
  main as `ffdd6f6`.
- **ORDER 007 / ORDER 008** — `control/status.md`: "orders: acked=001–008,
  done=001–008 — unchanged this session. Inbox re-read at origin/main HEAD (9b13b8a)
  2026-07-10T23:08Z … no order newer than 008." Both done; the inbox carries nothing
  newer.
- **Successor hypothesis slot: CONSUMED** — `control/status.md`: "research round 2:
  CLOSED — pre-registered → executed → closed, all merged-on-green: #46 pre-registration
  docs/research-round-2.md (BINDING, merged before any Round 2 number existed,
  `8d0270f`), #47 R1 vol_filtered_trend (0 KEEP / 4 KILL of 48…), #48 R2
  keltner_breakout (2 KEEP / 2 KILL of 24…), #49 R3 xsec_momentum (3 KEEP / 3 KILL of
  6, first portfolio lane, `9b13b8a`), plus #50 R4 close-out." R3 IS this idea:
  `docs/research-round-2.md` §3c — "First portfolio-level lane. One strategy over all
  9 cached daily instruments as a single portfolio: rank instruments by trailing total
  return over lookback L, hold the top-k equal-weight, rebalance every 21 bars …
  Benchmark: equal-weight buy & hold of the 9-instrument basket, same window, same
  costs." Grid frozen pre-run: L ∈ {63, 126, 252} × k ∈ {2, 3}.
- **Promotion state** — `docs/research-round-2.md` banner: "**Promotion is CLOSED for
  this round.** … Genuine OOS validation of any Round 2 survivor requires a **NEW,
  owner-gated, pre-registered protocol on post-2026 data**. That is an **OWNER-ACTION**:
  agents may flag it as a proposal but must not schedule, initiate, or run it."
- **Manifest divergence** (freshest-wins) — superbot `docs/eap/fleet-manifest.md` @
  `4ccb631`: the trading-strategy row still reads "P1–P5 prep DONE, **PARKED GREEN** …
  **holdout SEALED** … ORDER 007 … in flight; kit v1.1.0 (oldest pin)" — a full
  program-phase-plus behind the lane heartbeat and HEAD; every citation above uses the
  lane's own tree (manifest staleness datapoint 13, same row as datapoints 5–6).

**1. What is this really?**
A correctly-aimed succession capture that its own target lane outran. The capture
proposed three things: (a) queue cross-sectional (relative) momentum as the first
post-holdout hypothesis class; (b) build the one engine extension it needs
(portfolio-level positions across instruments); (c) pre-declare the variant budget
(lookback × k × rebalance) before any new data is seen. The lane did all three on
2026-07-10, hours after the capture merged: Research Round 2 pre-registration (frozen
grids, hard cap 100, rebalance interval frozen at 21 bars and not swept) landed as
lane PR #46 (`8d0270f`) BEFORE any outcome existed, the first portfolio lane was built,
and R3 ran the 6-config sweep (lane PR #49, `9b13b8a`). Verdicts: L=63/k=2 (stitched
OOS Sharpe 1.627 vs basket 1.147), L=63/k=3 (1.631), L=252/k=3 (1.277) KEEP as
dev-candidates only; L=126 failed both arms and L=252/k=2 failed
(`docs/research-round-2-results.md` §R3). What remains of the capture is not a
hypothesis to queue but a state to record.

**2. What is the possibility space?**
Post-self-serve, four residual branches. (i) **OOS validation of the three xsec
dev-candidates** — the only branch that converts a dev-candidate into a claim, and it
is explicitly owner-gated ("NEW, owner-gated, pre-registered protocol on post-2026
data"; agents flag, never run). (ii) **More variants** — 22 contingency configs exist
but are "unusable without a committed amendment … BEFORE running"; sweeping further
lookbacks/k on the same dev bars is exactly the variant-inflation the lane's own
discipline exists to stop. (iii) **A second paper-lane protocol** carrying an xsec
rule forward on genuinely-new bars — the live paper lane is pre-registered for
donchian(15,5) only (`docs/paper-lane-protocol.md`, ledger record paper-0001 WATCH);
adding a portfolio strategy means a new pre-registration, same owner gate (protocol
§8 names promotion paths owner-gated). (iv) **Other multi-asset families** reusing
the now-existing portfolio engine (cross-sectional mean-reversion, vol-weighted
baskets…) — future captures, each a new burden-budget negotiation, none queued here.

**3. What is the most advanced capability reachable by the simplest implementation?**
Already reached — by the lane. The capture's "one real engine extension … the
capability every future multi-asset family reuses" now exists (aligned common date
index across 9 instruments, 2,595 bars; per-rebalance per-side costs; walk-forward on
the aligned index — results doc §R3 protocol block). The simplest implementation that
adds anything NEW today is a one-page owner PROPOSAL naming the three xsec
dev-candidates (plus keltner's two) as pre-declared subjects of the next protocol —
paperwork, not code, and the decision it needs is reserved to the owner.

**4. What breaks it?**
- **Already broken by timing** — the lane self-served between capture (PR #10, merged
  2026-07-10 ~20:0xZ) and probe: pre-reg `8d0270f` and execution `9b13b8a` both landed
  2026-07-10. A probe dispatched a few hours earlier would still have found the
  pre-registration merged. Nothing here was wasted — capture and lane converged
  independently on the same next class — but the queue-it-now value is gone.
- **The "post-re-seal data" premise never materialized.** The capture assumed a
  successor holdout seal (its sibling capture, parked @ PR #25) would provide fresh
  evaluation data; instead the lane ran on the dev rail (bars < 2025-01-09, "zero new
  `holdout_unlocked` rows — the count stays exactly 13") with promotion CLOSED. The
  honest evaluation data the capture priced does not exist yet anywhere: the paper
  rail serves only bars ≥ 2026-07-11 and "zero lane bars exist yet."
- **Universe drift, minor:** the capture says "the 8 committed tickers"; the lane's
  cached daily universe is 9 (incl. BTC-USD) and R3 used all 9.
- **Routing hazard:** any idea-engine push of this family to sim-lab now would
  re-backtest the same dev bars with WEAKER provenance than the lane's own
  pre-registration (which was committed before any number existed), and would route
  around an explicitly reserved OWNER-ACTION. Producer-reachability check (README
  battery rule): the named producer (the trading lane) demonstrably reaches everything
  this idea prices — data (cached snapshot via the `load_ohlcv` default rail), engine
  (portfolio lane shipped), discipline (pre-registration) — evidenced by the committed
  sweep artifact `experiments/sweeps/r2-xsec_momentum/xsec_momentum__XSEC-9.json`;
  conversely NO agent-reachable producer can supply the post-2026 evaluation bars the
  residual question needs — pattern-exists is not pattern-can-produce, and here the
  missing producer is time itself plus an owner signature.

**5. What does it unlock?**
Nothing left to unlock by acting — the engine extension exists and three named
dev-candidates sit in the lane's results doc with full denominators (6 this family /
78 Round-2 / 668 program). Residual value of the capture: it independently predicted
the lane's actual next move hours ahead (evidence the capture heuristic — "next
hypothesis class after honest falsification" — aims true), and its file now carries
the cross-repo trail from the 13/13 P4 falsification to the R3 dev-candidates.

**6. What does it depend on?**
Consumed: it depended on the post-holdout hypothesis slot being OPEN; Research Round 2
consumed that slot with this very family (pre-reg `8d0270f` → close-out PR #50). Any
revival depends on (a) the owner authorizing the new pre-registered protocol on
post-2026 data (research-round-2.md banner; the lane deliberately keeps this a
"decision, not a click" — NOT a ⚑ item, per its status), and (b) genuinely new bars
accruing (paper lane opened 2026-07-11; first evaluable signal ~early Aug 2026 per the
lane's warm-up math). No idea-engine dependency remains.

**7. Which lane should build it?**
`menno420/trading-strategy` itself, through its own pre-registered research rounds and
paper-lane infrastructure — not sim-lab, and this is now proven rather than argued:
the lane already built and ran the family under provenance (pre-registration merged
before any outcome, frozen grids, burden denominators on every number) that a sim-lab
reproduction of the same dev bars could only weaken. The one open question — do the
three dev-candidates survive genuinely new data — is answerable only by the lane's
paper/OOS machinery on post-2026 bars under an owner-gated protocol; sim-lab has no
data the lane lacks and no discipline the lane hasn't already exceeded. idea-engine's
role ends at recording the state and handing the manager the routing fact.

**8. What is the smallest shippable slice?**
For idea-engine: exactly this PR — state flip + probe + section-index row; no
proposal (outbox tail verified at PROPOSAL 005; appending one would route around the
owner reservation). For the lane, IF the owner authorizes follow-on research: a
one-doc pre-registered protocol on post-2026 data naming the five Round-2
dev-candidates (three xsec, two keltner) as its pre-declared subjects — the lane's own
status already carries this as "flagged as proposal only, never scheduled/initiated/
run by agents." Watch item, no action: first paper-lane grading pass
(next-update-by 2026-07-17 in the lane heartbeat).

**Recommendation: park** — overtaken-by-events: the lane pre-registered (`8d0270f`) and
executed (`9b13b8a`, R3 `xsec_momentum`, 3 KEEP dev-candidates / 3 KILL) this exact
hypothesis class on 2026-07-10, and every path beyond dev-candidate is an owner-gated
new protocol on post-2026 data that agents must not schedule.
