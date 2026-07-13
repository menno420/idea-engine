# Session — PROPOSAL 042: channel concentration vs diversification at fixed build budget (VENTURE rotation, round 7)

> **Status:** `complete`
> **Model/time:** fable · 2026-07-13T18:26:50Z (Ideas Lab worker slice — draft the
> VENTURE rotation round-7 head, non-books half, under standing owner ORDER 003.
> Card born in-progress as the designed gate hold; flips complete in this PR's
> final commit once both checkers verify green and the 💡 slot resolves)

**📊 Model:** fable (Claude Fable family) · content + outbox proposal only (idea
file, card, venture-lab index row, claim file, outbox append; no control/status.md
or control/inbox.md writes; no checker or script changes; nothing in sim-lab —
a parallel session owns the V052 claim there)

## Scope

Draft a genuinely new sim-shaped idea for the VENTURE rotation slot, round 7,
under standing owner ORDER 003 (continuous pipeline — "continue coming up with
new ideas, that is your main purpose") and ORDER 004 rule 3's rotation ("fleet
backlogs → venture's book/product space → game mechanics → COMPLETELY UNRELATED
domains"). Round 7 opened at fleet backlogs with P041 (spool-scale margin,
merged #331), so this slice serves the venture slot. Half selection: the slot's
own half-alternation, stated in P038's block verbatim ("r4 books → r5 trading →
r6 books due"), puts round 7 on the NON-BOOKS half — rounds 1–6 were P018
(books → V020 null), P022 (trading → V024 null), P026 (trading → V028 approve),
P030 (books → V032 reject), P034 (trading → V036 reject), P038 (books → V049
reject). Prior non-books rounds all served the half from TRADING; this round
takes the half from venture-lab's PRODUCTS lane deliberately — ORDER 004's
literal phrase is "venture's book/product space", and the products lane just
shipped the exact evidence this head prices (flagged in the idea doc's rotation
statement, decide-and-flag). The harvested head: venture-lab's own 2026-07-13
product ideation batch (docs/products/ideas-2026-07-13.md @
`be6c75d4e3379efc108f27d17f2c8ff5adb9a74f`, read via read-only clone this
slice) picks 3 BUILDs that its OWN batch-level Kill-Rule-2 critique says "all
ride the same saturated agent-ops/dev-article funnel that has produced 0
organic sales across 7 click-queued products so far — the batch does not
diversify channel risk, it deepens a channel whose first proof point (SWTK T+7
checkpoint, 2026-07-19) has not yet arrived". PROPOSAL 042 prices that
self-critique as a pre-registered hermetic channel-allocation sim: given the
0-organic-sales evidence, does CONCENTRATE (all builds in the incumbent
channel, cheaper per build — the ORDER 008 template thesis) beat SPLIT /
EXPLORE-THEN-COMMIT across untested channels at a fixed per-cycle token budget,
and under which prior-belief cells does the answer flip? Exact discrete-Bayes
enumeration arm + seeded MC arm, REJECT checked first, seeds 20261305–308
strictly above the P041 high-water 20261304. Verified before claiming at HEAD
`498a88e` (main advanced past the dispatch pin 65dcf3a by exactly the parallel
session's V052 claim — re-checked, no P042 collision): no PROPOSAL 042 in
control/outbox.md, no P042 claim in control/claims/, seed high-water 20261304
(tree-wide `rg -g '!bootstrap.py' -g '!.substrate' -o '202613[0-9][0-9]'` —
max hit 20261304 in P041's idea file; control/status.md's "20261300" line is
stale prose, not an allocation; sim-lab allocates no seeds of its own — its
verdicts consume pre-registered proposal seeds, per the P041-slice sweep of
V001–V051 — and the parallel V052 session consumes P041's 20261301–304), and
the topic dedup sweep `rg -i -g '!bootstrap.py' -g '!.substrate'
'channel.concentration|diversif|organic sale'` returns ZERO files. Idea file
`ideas/venture-lab/channel-concentration-vs-diversification-2026-07-13.md`
(probed single-pass this slice, sim-ready), appended to `control/outbox.md` as
PROPOSAL 042. Nothing here builds anything in venture-lab; routing of the
verdict's consequences is the manager's per Q-0260.

## 💡 Session idea

**Give control/claims/ a landed-claim prune advisory — a claim whose scoped
PROPOSAL already sits in the outbox is finished work squatting on the collision
surface.** This slice's collision check (the step every drafter runs before
claiming) had to manually classify FOUR residual files in control/claims/: two
stale merged claims (link-backfill, P041's) plus the parallel session's live
V052 claim, deciding file-by-file "is this a P042 collision or a corpse?" —
and the corpse class is growing, because claims now ride the work branch (the
P041 ordering, kept this slice: one fewer PR) which means NOTHING ever prunes
them: the old separate claims-prune control PRs (#282/#296/#301 in the night
report) were the pruning mechanism, and riding the work branch silently retired
it. The retiring fix is hermetic and one-file: an advisory (a `--claims` mode
on check_ideas.py or a tiny check_claims.py, always exit 0) that parses each
claim's `scope: PROPOSAL <nnn>` and nags when `## PROPOSAL <nnn>` already
exists in the local control/outbox.md — landed work, prunable claim; claims
whose proposal is absent stay silent (live work). Zero network, zero git
archaeology (the outbox is the landing ledger), and the venture-lab lane
already runs the pattern (its claim staleness/duplicate checkers, the
Advisory-Checker Pack #7 inventory @ be6c75d) — this imports it to the seat
where the collision check actually happens. Dedup: no prior card 💡 touches
claim lifecycle (P035 seed ledger tail-line, P036 domain ledger, P039 machinery
index, P040 SHA-pin resolution, P041 seed-high-water ledger — all
different surfaces); no checker change shipped this slice (content-only scope
held).

## ⟲ Previous-session review

Newest predecessor card (`.sessions/2026-07-13-proposal-041-spool-scale-margin.md`,
the round-7 fleet-backlogs slice, flipped ~18:10Z): thorough and honest — the
born-red order is documented commit-by-commit, both checker outputs are quoted
verbatim in the close-out with the designed hold correctly framed, the
cross-repo seed re-check names its false-positive class explicitly, and the
claim rode the work branch per the dispatching coordinator — which read cleaner
end-to-end than P040's separate fast-lane claim PR and cost one fewer PR (this
slice kept that ordering). Two things visible only from here: first, the
coordinator heartbeat still carries "fleet seed high-water 20261300" — stale
against P041's own 20261301–304 registration within the hour, which is exactly
the drift its 💡 (a machine-readable `seed-high-water:` ledger line + a
check_ideas advisory) wants to retire; the idea validated itself before its
proposer's PR was cold, and this slice had to route around the stale line by
re-sweeping the tree rather than trusting the heartbeat. Second, P041's claim
file sits un-pruned in control/claims/ post-merge — no fault of that slice
(pruning was never its scope), but riding the work branch removed the standing
prune vehicle, and the residue lands directly on the next drafter's collision
check; that gap is this card's 💡.

## Close-out

All pieces landed before this flip, in the dispatched born-red order: card born
in-progress @ `ca7f855` (first commit on the branch, the designed gate hold);
claim @ `00a65a9` (riding the work branch, the P041 ordering — its timestamp
was corrected to the real clock by amend BEFORE push, never after); idea doc
`ideas/venture-lab/channel-concentration-vs-diversification-2026-07-13.md` +
venture index row @ `8aad290`; outbox PROPOSAL 042 append (append-only,
heading stamp 2026-07-13T18:33:00Z from real `date -u`, later than P041's
18:01:18Z and ASK 003's 17:59:21Z; `idea:` blob link pinned at `8aad290`) @
`45884de`; branch pushed; PR #333 opened READY (never draft; auto-merge left
to the enabler — no agent merge). Verification on this tree at the flip:
`python3 scripts/check_ideas.py --outbox` exit 0 ("check_ideas: OK — outbox
proposals and sim-ready ideas are consistent"); `python3 bootstrap.py check
--strict` exit 0 once this badge flipped — its only red before the flip was
the designed born-red hold on this very card, plus the pre-existing
never-exit-affecting owner-action advisory on control/status.md (predates and
is untouched by this slice). Rotation verified before drafting: round 7 opened
at fleet backlogs (P041 #331), venture slot next per ORDER 004 rule 3;
non-books half per P038's block-verbatim half-alternation; served from the
PRODUCTS lane per ORDER 004's literal wording, both readings cited in the idea
doc (decide-and-flag). Seeds 20261305–308 registered strictly above the
verified high-water 20261304 (tree-wide `rg -g '!bootstrap.py'
-g '!.substrate' -o '202613[0-9][0-9]'` at HEAD `498a88e` maxes at 20261304;
control/status.md's 20261300 line is stale prose; sim-lab allocates no seeds
of its own — the parallel V052 session consumes P041's 20261301–304; 20261308
aux never read by any decision number). Dedup sweep `rg -i -g '!bootstrap.py'
-g '!.substrate' 'channel.concentration|diversif|organic sale'` → zero files
at drafting HEAD. No control/status.md, control/inbox.md, or sim-lab writes;
the V052 parallel-session claim and the two older stale merged claims in
control/claims/ untouched (out of scope — see 💡); timestamps from real
`date -u` throughout. Flip stamped 2026-07-13T18:35:19Z.
