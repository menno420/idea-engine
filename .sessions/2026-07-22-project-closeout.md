# Project closeout — write the permanent final record: docs/PROJECT-CLOSEOUT.md, link it from the docs index, and true up control/status.md at the close of the run

> **Status:** in-progress

> **📊 Model:** Claude Opus 4 family · high · docs/closeout
started: 2026-07-22T00:00:00Z

💓 Heartbeat:
- round/slot: closeout — permanent final record for the generate-and-verify loop
- lane: docs/PROJECT-CLOSEOUT.md (new) + docs/current-state.md link + control/status.md true-up
- branch: claude/project-closeout
- state at close: proposal high-water P261 (sim-ready), verdict high-water V274 (ruled APPROVE); loop caught up / at rest, no un-verdicted proposal pending
- gate: python3 bootstrap.py check --strict exits 0 on main (control fast lane for the true-up diff)

## What this session does
Writes the permanent project closeout record at `docs/PROJECT-CLOSEOUT.md`: what
the project was, everything it produced, the exact state it was left in, and how
to pick the work back up. Links the new record from the docs index
`docs/current-state.md`, and makes a surgical true-up of `control/status.md` so
the heartbeat reads accurately as of close (proposal high-water P261 sim-ready,
verdict high-water V274 ruled APPROVE, loop caught up / at rest, closeout in
progress with a pointer to the record). The routine-disposition block in
`control/status.md` is preserved byte-for-byte.

## Method
Born-red first commit lands this card with Status: in-progress to hold the PR
red behind the substrate-gate until the deliberate flip at the end. The second
commit adds the closeout doc, the docs-index link, and the status.md true-up.
`python3 bootstrap.py check --strict` is run before push. The card flips to
complete as the deliberate last commit, releasing native squash auto-merge on
green.

## ⟲ Previous-session review
The prior slice landed VERDICT 274 (P261 → V274, +13 offset) ruled APPROVE —
Morris approximate counting, base-2 counter estimator N̂=2^C−1 exactly unbiased
E[N̂]=n with exact variance n(n−1)/2, four gates PASS, appended to
`control/outbox.md` and stamped in `control/status.md`. With P261/V274 landed the
loop is caught up and at rest; this session writes the permanent closeout record
rather than pulling a new idea.

## 💡 Session idea
A single definitive closeout record, written for two cold readers — the owner and
any future session opening the repository fresh — collapses the scattered
heartbeat/ledger state into one linked, verifiable page and states exactly where
the work resumes if it is ever revived.
