# Claim remote-visibility scan — make claims travel without waiting for a merge — link index

> **State:** historical(shipped 2026-07-10 in superbot PR #1919 as `check_lane_overlap.py --remote`)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/claim-remote-visibility-scan-2026-07-08.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/claim-remote-visibility-scan-2026-07-08.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/claim-remote-visibility-scan-2026-07-08.md)).

Make parallel-lane claims visible before they merge: a tip-state ls-tree compare against sibling lanes' remote branches, plus a re-scan-after-your-own-claim-push protocol line.
