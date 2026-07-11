# Pre-publish conservative forecast — the Q-0259 hard-protocol attachment for every money click

> **State:** parked(lane-self-served — venture-lab PR #20 shipped the conservative forecast before the PR #22 unfreeze; intake template now carries forecast+payback fields)
> **Class:** venture · **Target:** `menno420/venture-lab`
> **Grounding:** https://github.com/menno420/venture-lab@9f1b616 · fetched 2026-07-11T02:35:49Z
> *(pin annotation: verify-time re-check pin — capture pin was `ce22315` (2026-07-10); Q-0259 r.4 ruling text re-verified unchanged at superbot HEAD `a762384`, same ls-remote batch; both HEADs pinned via `git ls-remote` at 2026-07-11T02:35:49Z, tree reads via read-only blobless clone at those pins — anonymous api.github.com 403s through the proxy, so every SHA came from the git transport)*

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

## Verify-and-park (2026-07-11)

*Verify-first per README § The probe battery (the round-4 rule, encoded by PR #59: a
maintenance-shaped capture aimed at a LIVE lane gets a five-minute verify-and-park
FIRST at lane HEAD, keyed on the capture's INVARIANT — never its named artifact —
escalating to a full battery pass only if the live check finds the slice
unexecuted). The live check found it EXECUTED, so no battery pass runs and no
`**Recommendation:` line is written — that token belongs to probe reports. Pins:
venture-lab HEAD `9f1b616` and superbot HEAD `a762384`, both via `git ls-remote` at
2026-07-11T02:35:49Z; tree reads via read-only blobless clone at those pins
(anonymous api.github.com 403s through the proxy, so every SHA came from the git
transport — the standing capability recipe).*

**Invariant keyed on:** "a conservative forecast is attached before the owner sees
the money click." The ruling behind it re-verified verbatim-unchanged: Q-0259 r.4
(superbot `docs/owner/maintainer-question-router.md` § Q-0259 item 4 @ `a762384`)
still requires exactly what the owner must do PLUS a conservative earnings
expectation AND a payback-time estimate — expect bad results, never overstate.

**Verified, with citations (all @ venture-lab `9f1b616` unless noted):**

- **The freeze condition (ORDER 003) is DONE** — lane `control/status.md` reports
  003 DONE; the P0 real-Stripe-path fix merged as lane PR #16 (squash `912da3e`).
  The capture's "known, dated future event" arrived.
- **⚑B/⚑D are UNFROZEN** — lane PR #22 (`6fea90b`, 2026-07-11T01:58:35Z) flipped
  `docs/launch/membership-kit/owner-actions.md` to UNFROZEN (header confirms at
  `9f1b616`), with the honest caveat kept: "a live purchase is still unverified
  (⚑A)". Lane phase: launch-ready, orders 001–004 all done, awaiting the owner's
  publish clicks.
- **The lane SELF-SERVED the forecast BEFORE the unfreeze** — lane PR #20
  (`2021bab`, 2026-07-11T01:48:56Z, ~10 minutes before the PR #22 unfreeze flip)
  shipped `docs/launch/membership-kit/one-pager.md` § "Conservative revenue
  expectation" ("0–2 sales/month with no active distribution; the first month may
  well be $0. One sale ≈ $49 gross, ≈ $44 net after typical marketplace fees; the
  '$20K/7-days' headline is unproven") and `template-packs/one-pager.md` ("0–3
  PWYW downloads/month … $0–$20/month"); the owner-actions WHY lines carry the
  expectation inline; `docs/launch/README.md:23` cites "Q-0259.4: expect bad
  results, never overstate". The invariant was met, in substance, by the lane
  itself — sequencing included.
- **The reusable-template half self-served too** — the lane's candidate intake
  template (landed lane PR #25, `9253d86`, 2026-07-11T02:21:21Z) now carries
  binding "Conservative revenue estimate" + "Payback-time estimate" +
  "Token-cost line" fields (grep `payback` hits
  `candidates/{stripe-webhook-test-kit,agent-fleet-field-manual,cc-cost-lens}/INTAKE.md`)
  — the "turn the protocol into a lane convention with a file shape" half of this
  idea, executed as a forward-looking intake field set.
- **Residual sliver (observed gap, NOT routed from here):** the live ⚑B/⚑D pages
  carry a conservative earnings expectation but no payback-in-build-sessions line
  — Q-0259 r.4 requires BOTH. Fee-adjusted net per unit is present; payback in
  the ledger's own currency is not. Small lane doc task, owner-adjacent, not
  evidence-shaped; the lane's own `control/status.md` already notes
  "Return-on-agent-labor pending first sale". Recorded here so the trail carries
  it; the lane's next doc pass is its natural home.

**Verdict: verify-and-park** — state flipped forward-only captured →
`parked(lane-self-served — venture-lab PR #20 shipped the conservative forecast
before the PR #22 unfreeze; intake template now carries forecast+payback fields)`.
Fifth lane-self-served datapoint (first VENTURE-class instance; the class now
spans four sections, both arrival paths, and all three idea classes). Nothing to
queue, route, or simulate: a shipped forecast proves itself, and the ⚑B/⚑D
publish clicks already live six-field on the lane's own owner-actions surface.
