# Session — harvest slice: websites lane backlog (5 docs link-indexed, second SECTIONS lane)

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-10 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## Scope

Second instance of the lane-backlog harvest (the PR #7/#26 recipe): link-index the
websites lane's own `docs/ideas/` docs — the backlog list plus its four standalone
idea files — into `ideas/websites/`, and register the section in
`scripts/check_harvest.py` SECTIONS (the one-line second-lane addition the heartbeat
has carried as a standing note since PR #22/#26). This is the exact follow-up the
PR #31 card's 💡 queued ("Lane-backlog harvest, second instance ready") and the
heartbeat names first in ripest-next. Ship as one merged-on-green PR.

Claimed with this first commit: `claims/harvest-websites-lane-backlog.md`
(inbox read first — verified still empty at origin/main HEAD `b251d56`; `claims/`
held only its README at claim time).
