# Session — ideas-link backfill for PROPOSAL 037 + 038 (healing the latent outbox LINK red)

> **Status:** in-progress
> **Model/time:** fable · 2026-07-13T15:50:00Z (repair worker slice — card born
> in-progress as the designed gate hold; flips complete in this PR's final commit
> once both checkers verify green and the 💡 slot resolves)

**📊 Model:** fable · repair + backfill only (two idea files, two section-README
index rows, two append-only correction lines inside the P037/P038 outbox blocks,
claim file, two stale drafter-claim deletions, this card; no control/status.md or
control/inbox.md writes, no checker or script changes, nothing in sim-lab)

## Scope

Heal the latent red gate found at HEAD `2b43de2`: `python3 scripts/check_ideas.py
--outbox` FAILS on main with two LINK violations — PROPOSAL 037 and PROPOSAL 038
carry no `menno420/idea-engine` `ideas/` link in their `idea:` lines (both were
control-only fast-lane slices that disclosed "no local idea file is committed" as a
deviation from the P017–P036 idea-file convention). The fast lane short-circuits CI
green on control-only diffs, so the violation is latent: the NEXT non-control PR's
preflight goes red on someone else's work. This slice (1) backfills minimal local
idea docs for both proposals under their correct sections, sourced verbatim from
the outbox blocks; (2) appends one correction `idea:` line INSIDE each block (the
checker's fields parser takes the last `idea:` match per block; no existing line is
edited — append-only preserved); (3) prunes the two stale drafter claims whose work
is terminal (P036 drafted via PR #313 MERGED, P037 via PR #315 MERGED — verified
live via the GitHub API this slice); (4) verifies both `python3 bootstrap.py check
--strict` and `python3 scripts/check_ideas.py --outbox` exit 0 before push.
