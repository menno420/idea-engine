# Session — PROPOSAL 046: keyword tiling vs independent picks (venture rotation, round 8, books half)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-13T20:53:28Z (Ideas Lab worker slice — draft the
> VENTURE rotation round-8 head, BOOKS half, under standing owner ORDER 003. Card
> born in-progress as the designed gate hold; flipped complete in this PR's final
> commit at 2026-07-13T21:05:57Z)

## Scope

Draft a genuinely new sim-shaped idea for the VENTURE rotation slot, round 8
(BOOKS half), under standing owner ORDER 003 (continuous pipeline) and ORDER 004
rule 3's rotation. Round 8 opened at fleet backlogs with P045 (#343), so venture
is next; the slot's half-alternation from the actual sequence (P018 books →
P022/P026 trading → P030 books → P034 trading → P038 books → P042 products) puts
round 8 on the BOOKS half. Claim landed first via the fast-lane control/-only
PR #346 (`control/claims/claude-proposal-046-keyword-tiling.md`).

Harvest source: venture-lab's KDP keyword/category allocation map
(`docs/publishing/keyword-map.md` @ HEAD
`be6c75d4e3379efc108f27d17f2c8ff5adb9a74f`, read via the read-only clone) — the
14-title catalog's deliberate keyword TILING convention (first claim on main
wins; no two packets share a cell), adopted on the cannibalization theory and
never priced against independent per-packet greedy choice. Idea file
`ideas/venture-lab/keyword-tiling-vs-independent-picks-2026-07-13.md` (to be
probed single-pass this slice, sim-ready), then appended to `control/outbox.md`
as PROPOSAL 046. Seeds 20261321–324, strictly above the P045 high-water
20261320 (re-swept this session: outbox range notations + this tree +
/home/user/sim-lab; the only ≥20261321 hits are digit substrings inside
sim-lab results.json Fraction numerators, not allocations).

**📊 Model:** `fable-5` (family-level self-report from this session's own harness,
per ORDER 001 / Q-0262 — never copied from a schedule surface) · content + outbox
proposal only (idea file, card, section index row, fast-lane claim PR #346, outbox
append; no product code, no control/status.md or control/inbox.md writes; no
sim-lab writes — the V056 verdict session runs parallel there and its claim
`control/claims/2026-07-13-verdict-056.md` is untouched)

## 💡 Session idea

**Pin the canonical seed-sweep recipe — a digit-boundary regex plus the
range-notation companion plus a sim-results exclusion — because a naive numeric
grep now fails in BOTH directions, and this slice measured both live.** False
negative: P045's block writes "seeds 20261317–320" (range notation truncates the
literals), so a plain `20261[0-9]{3}` sweep maxes at 20261318 and misses the true
20261320 high-water — the dispatch-documented trap, confirmed real this slice.
False positive, NEW class: the same sweep over the sim-lab working copy returned
20261542/20261664/20261833 — digit substrings inside `results.json` exact-Fraction
numerators (42-digit integers) and one `se_rel` decimal, not allocations; as
verdicts accumulate, every future numeric sweep hits more of these. The fix is one
documented recipe: (1) digit-boundary match `(?<![0-9])20261[0-9]{3}(?![0-9])`
(kills the numerator aliases), (2) a companion range-notation grep
(`20261[0-9]{3}\s*[–-]\s*[0-9]+`, expand by hand), (3) exclude sim results
artifacts (`results.json`) from the numeric pass — one line in the seed-allocation
convention doc, zero new tooling. Dedup (this slice, at HEAD `fda76a7`): P035's 💡
is a seed REGISTRY (where allocations are recorded); P045's 💡 is
harvest-by-hedge-marker; this is the sweep RECIPE (how the high-water is verified)
— no prior 💡 or head pins it, and the two failure classes it addresses were both
observed, not speculated.

## ⟲ Previous-session review

Newest predecessor card (`.sessions/2026-07-13-proposal-045-snapshot-stale-threshold.md`,
worker slice ~20:26Z): closed clean, and its rituals transferred verbatim here —
the blob-pinned `idea:` link (P046's outbox append pins the `ae779cc` idea-doc
commit) and the seed re-sweep, which its own range notation made harder in an
instructive way: its block's "seeds 20261317–320" is exactly the truncated-literal
trap this card's 💡 now names, while its idea file (listing all four seeds in
full) is what made the 20261320 high-water recoverable at all. Its outbox-rollover
escalation (368,007 bytes then, "nearing the 256KB-Read-limit pain it predicted")
kept compounding on schedule: control/outbox.md is 390,738 bytes after this
slice's append and every read here was shell-sliced — ASK 004 remains the right
fix and remains unserved. Its ⟲ claim-corpse note also aged as predicted:
`control/claims/` still holds the P045 claim post-merge (#343) plus the backfill
corpse, and this scope-limited slice pruned nothing either (decide-and-flag:
noted, not expanded into this worker diff).

## Close-out

All pieces landed before this flip: fast-lane claim PR #346 (control/-only,
opened ready, merge left to the enabler), card born in-progress @ `71c1421`,
idea doc + section index row @ `ae779cc`, PROPOSAL 046 outbox append @ `68e4acb`
(idea: link pinned to the `ae779cc` blob; `scripts/check_ideas.py --outbox` exit
0 verified after the append), work PR #348 opened READY immediately after the
push (never draft; merge left to the enabler workflow, no agent merge). Rotation
verified at HEAD before drafting: round 8 opened at fleet backlogs with P045
(#343), venture next per ORDER 004 rule 3, BOOKS half per the slot's actual
P018→P042 half sequence. This flip is the branch's last commit; both checkers
(`python3 bootstrap.py check --strict`, `python3 scripts/check_ideas.py
--outbox`) run green at flip time or this commit does not push.
