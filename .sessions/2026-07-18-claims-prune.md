# Claims prune — sweep terminal control/claims/ backlog (ORDER 018 hygiene slice)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · review/verify

Born red by design: this card lands `in-progress` in the branch's FIRST commit, holding the substrate-gate born-red HOLD red while the prune is executed and audited. The LAST commit flips it to `complete`, clearing the HOLD. The diff is control-only (`control/claims/**`) plus this card — no ideas/, no heartbeat, no inbox/outbox.

## Objective
Prune the accumulated terminal claim files in `control/claims/` behind the advisory `claims-duplicate` / `claims-format` nags. Delete ONLY claims whose branch/PR is verifiably terminal (merged/closed PR + content on origin/main); keep anything possibly-live. `README.md` stays.

## GROUNDING (verified at HEAD `3c4d3ba`)
- Claims convention — https://github.com/menno420/idea-engine/blob/3c4d3bab7a141b5ab2fe8660aa73673a54dc2635/control/claims/README.md — successor-prune of terminal claims down to `README.md` is the sanctioned lifecycle (a claim rides its work PR, stays on main at close, and the successor prunes it once that PR is verified terminal).
- Audit basis — `git ls-remote --heads origin 'claude/*'` + `list_pull_requests` (state=all/open): the repo's only open PR is #527 (the V126 two-choices-routing-cliff born-red mirror), whose work claim `verdict-126-two-choices-routing-cliff.md` lives on its own branch and is NOT on main, so it is not in this sweep's tree and cannot be pruned here; every claim actually present in the tree at branch time has a merged PR and its content (proposal verifiers + verdict blocks in `control/outbox.md`, through V154) confirmed present on origin/main.

## Constraints honored
- Model line family-level (PL-004), task class review/verify.
- Delete only verifiably-terminal claims; conservative KEEP on any doubt. 76 deleted, 0 live-at-branch.
- Control-only diff (`control/claims/**` deletions + this card). `control/status.md` heartbeat, `control/inbox.md`, `control/outbox.md`, all `ideas/` and other sessions' `.sessions/` files untouched.
- born-red card FIRST commit holds the HOLD; flip `complete` LAST.

## Audit outcome
76 non-README claim files audited against live GitHub at HEAD `3c4d3ba`. Every one is terminal: a merged PR exists and its content is confirmed on origin/main. The repo's one open PR (#527, the V126 born-red mirror) touches a claim file that is not on main, so it does not intersect this sweep. **76 DELETE, 0 KEEP.** The malformed `proposal-099-shop-reroll-ruin.md` (self-declared "LIVE (PR open)") is terminal in ground truth — PR #490 merged, branch gone, verifier on main — so it too is pruned; its stale self-report is exactly why the rule verifies against live git/PR state. No claim was kept — every non-README claim in the tree at branch time was verifiably terminal. A claim landing after this branch point simply survives to the next successor-prune.

## ⟲ Previous-session review
Prior session on origin/main landed the latest verdict mirror (V154) — APPROVE. That loop, like the ~35 verdict/proposal loops before it, left its claim file on main for a successor to prune — exactly the backlog this slice clears. No prior `claims-prune` session precedes this one.

## 💡 Session idea
The `claims-duplicate` advisory keys on the bare ISO **date** token, so every claim that lands on a single day collapses into one "same-lane" collision even though branch and scope differ — the warning count tracks daily throughput, not real contention. A cheap kit refinement: have the duplicate scan key on the full claim bullet (branch token or ISO8601 timestamp) rather than the date-only prefix, so it flags genuine same-branch collisions and stays quiet on distinct same-day claims. Until then, successor-prune-on-terminal (this slice) is the standing remedy — a recurring hygiene lane worth a scheduled sweep.

## Outcome — pruned (76 terminal claims removed)
Executed `git rm` of all 76 verified-terminal claim files; `control/claims/` now holds `README.md` only. `python3 bootstrap.py check --strict` → all checks passed; the claims advisory warnings (claims-format + claims-duplicate) are cleared (residual advisories named here are pre-existing and out of scope: `owner-action-fields` on `control/status.md`, `seat-digest-stale` on `docs/seat-digest.md`). PR #587. This flip is the card's LAST commit, clearing the born-red HOLD so the auto-merge-enabler lands on green.
