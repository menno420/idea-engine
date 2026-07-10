# Pre-publish conservative forecast — the Q-0259 hard-protocol attachment for every money click

> **State:** captured
> **Class:** venture · **Target:** `menno420/venture-lab`

## Problem

Q-0259's venture mandate carries a hard protocol: any step that needs the owner to
do/enable/buy something ships with **exactly what the owner must do, a conservative
earnings expectation, and a payback-time estimate — expect bad results, never
overstate**. The lane's queued money clicks (⚑B publish membership-kit at $49, ⚑D
publish template-packs at $19 PWYW, plus the $59 bundle note) fully satisfy the
first leg — click paths and paste-ready copy are excellent — but carry **no earnings
expectation and no payback estimate** against the banked token-cost lines. Both
clicks are currently FROZEN pending ORDER 003 (the P0 real-Stripe-path fix), which
means the unfreeze relay to the owner queue is a known, dated future event that the
protocol attachment must precede.

## Idea

One page per listing, shipped before the unfreeze is requested: a conservative
sales-range with its stated basis (marketplace-baseline honesty — most unlaunched
boilerplate listings sell ≈0–few units without an audience), fee-adjusted net per
unit, payback expressed in build-sessions recovered (the ledger's own currency), and
the explicit expect-bad-results line. The doc doubles as the reusable template every
future ⚑ money-click must attach — turning the Q-0259 hard protocol from prose into
a lane convention with a file shape.

## Grounding

- Q-0259 r.4 ruling text (verbatim-in-substance: "a plan showing exactly what the
  owner must do/enable/buy, plus a conservative earnings expectation and
  payback-time estimate — expect bad results, never overstate"): superbot
  [`docs/owner/maintainer-question-router.md` @ `6f283b9`](https://raw.githubusercontent.com/menno420/superbot/6f283b91160546af2864a0fd30b6e2d81b148a8f/docs/owner/maintainer-question-router.md), § Q-0259.
- Lane reality @ [`ce22315`](https://github.com/menno420/venture-lab/tree/ce223152719705e22a386b6fdc6d03508a0661c1):
  ⚑B/⚑D ask blocks (click paths present, forecasts absent); token-cost lines in
  `control/status.md`; freeze + unfreeze path in `control/inbox.md` ORDER 003
  ("done-when … ⚑B/⚑D unfreeze requested").
- Q-0259 fit: this IS the mandate's own compliance artifact; zero games/rebuild load.

**Why now:** ORDER 003 is the unfreeze trigger and it is a P0 already in the lane's
inbox — the forecast only does its job if it exists before the unfreeze relay
reaches the owner.
