# Session — ideas-link backfill for PROPOSAL 037 + 038 (healing the latent outbox LINK red)

> **Status:** complete
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

## 💡 Session idea

**Make the control-only fast lane run the local outbox↔ideas link check when
the diff touches `control/outbox.md`.** Root cause of this session's entire
existence: the fast lane short-circuits CI GREEN on control-only diffs (by
design — heartbeats must land fast), so the two PRs that INTRODUCED the LINK
violations (#315, #317) sailed green and the red landed latently on whichever
non-control PR came next. The slice-sized move: inside the gate's existing
control-only early exit, add ONE carve-out — if the control-only diff includes
`control/outbox.md`, also run `python3 scripts/check_ideas.py --outbox` (pure
local stdlib, no network, sub-second — the fast lane stays fast) and red on
its exit. The PR that introduces an outbox↔ideas violation then pays for it
itself; innocent successors inherit a green main. Dedup (this slice, at HEAD
`2b43de2`): `rg -i "fast.lane.*outbox|outbox.*fast.lane" -g '!bootstrap.py'
-g '!.substrate'` hits only this session's own backfill files; distinct from
the P036 card 💡 (rotation domain ledger — a read-cost index), the ender card
💡 (seam manifest grammar — close-out handoff), the P035 💡 (seed registry),
and the P033 💡 (outbox digest index) — none touches the fast-lane gate's
check coverage; the gate file is KIT-OWNED (README § Landing conventions), so
the head routes via the kit lane, not a local hand-edit.

## ⟲ Previous-session review

Newest predecessor card (`.sessions/2026-07-13-proposal-036.md`, worker slice
~14:37Z): closed clean and honest — rotation round-5 head drafted with the
band-liveness arithmetic run BEFORE registration and the loser candidates
named, and its 💡 (a one-line-per-round domain ledger for the rotation slot)
is genuinely slice-sized. One thing visible only from here: its drafter claim
(`control/claims/claude-proposal-036-secretary-rule.md`) was left in place
after PR #313 merged — the claims convention says delete at session close —
and the two fast-lane slices after it (P037/P038) skipped idea files entirely,
which together produced exactly the stale-claim debris and latent LINK red
this session existed to clean up.

## Close-out

All pieces landed before this flip: idea docs @ `3f41b42`, outbox correction
lines + claim prune @ `4616834` (P036 claim → PR #313 MERGED 14:42:14Z, P037
claim → PR #315 MERGED 15:10:59Z, both verified live via the GitHub API),
PR #318 opened READY (never draft; auto-merge left to the enabler — no agent
merge). Final verification on this tree at the flip:
`python3 scripts/check_ideas.py --outbox` exit 0 ("OK — outbox proposals and
sim-ready ideas are consistent"); `python3 bootstrap.py check --strict` exit 0
once this badge flipped (its only red before the flip was the designed
born-red hold on this very card). No control/status.md, control/inbox.md, or
sim-lab writes; timestamps from real `date -u` throughout.
