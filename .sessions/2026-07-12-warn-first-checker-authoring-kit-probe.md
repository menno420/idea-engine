# Session — single-pass probe: superbot warn-first-checker-authoring-kit

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-12 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session is doing

Single-pass probe (battery v0) of
`ideas/superbot/warn-first-checker-authoring-kit-2026-07-10.md` — TOP-5 #3 on the
fourth ledger (`control/status.md` @ `42f9642`): extract the shared scaffold +
AST/reachability lib so the third warn-first checker doesn't re-duplicate the
plumbing the first two (superbot #1747/#1748) copy-pasted.

Ledger trigger to verify at live HEADs: "third-checker trigger FIRED: PR #197
(golden-recapture checker seat at N) + PR #211 (class-4 check_plan_staleness at
S) each mint a warn-first checker; probe before both re-duplicate plumbing."

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this born-red
first commit carries the `ideas/superbot/` collision flag per the PR
#222/#225/#226/#228 workflow convention.

## Close-out

(pending — flips with the probe commit)
