# Revenue-ingestion owner relay — close the return-on-agent-labor loop before the first sale

> **State:** captured
> **Class:** process · **Target:** `menno420/venture-lab`

## Problem

The lane's mission metric is measurable return-on-agent-labor: every candidate
carries a running token-cost line (candidate #1 ≈1.x build sessions, #2 ≈1,
packaging/distribution ≈1 — banked in the heartbeat), and Q-0259's venture mandate
demands conservative, never-overstated economics. But the **revenue side of that
ledger has no ingestion path**: sales will happen entirely inside owner-owned
marketplace accounts (Gumroad / Lemon Squeezy, per ⚑B/⚑D), which agents can neither
create nor read (lane hard rail: no account creation). The heartbeat already flags
the gap — "return-on-agent-labor pending first sale (owner-gated on ⚑B/⚑D)". The
day the listings go live, the ledger goes silently stale and the lane is blind on
its own scoreboard.

## Idea

Define the relay protocol BEFORE first revenue: a `docs/ledger/` sales-inbox
convention where the owner periodically pastes the marketplace's sales CSV export
(or receipt summaries) — one paste per period, zero new accounts, zero spend. The
lane parses it into per-candidate revenue lines sitting next to the token-cost
lines, **net of marketplace fees**, so return-on-agent-labor becomes a computed
number instead of vibes. Includes the empty-period entry ("0 sales this week") so
absence of data is a recorded observation, not a gap — Q-0259: expect bad results,
report them honestly.

## Grounding

- Lane reality @ [`ce22315`](https://github.com/menno420/venture-lab/tree/ce223152719705e22a386b6fdc6d03508a0661c1):
  `control/status.md` token-cost line + "return-on-agent-labor pending first sale";
  README hard rails (no account creation → agents cannot poll the marketplace);
  ⚑B/⚑D publish asks name Gumroad / Lemon Squeezy as the channels.
- Venture mandate Q-0259 r.4 — profitable to fund the fleet, conservative
  expectations, never overstate (superbot
  [`docs/owner/maintainer-question-router.md` @ `6f283b9`](https://raw.githubusercontent.com/menno420/superbot/6f283b91160546af2864a0fd30b6e2d81b148a8f/docs/owner/maintainer-question-router.md), § Q-0259).
- Q-0259 fit: lane-internal ledger doctrine; no games/rebuild resources touched.

**Why now:** the format is cheapest before sales exist — defined after launch, the
first weeks of revenue history get reconstructed from owner memory or lost.
