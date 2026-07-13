# Session — PROPOSAL 044: checkout pooling folk law (COMPLETELY-UNRELATED slot, round 7)

> **Status:** `complete`
> **Model/time:** Claude Fable · 2026-07-13T19:42:00Z (Ideas Lab worker slice — draft the
> round-7 COMPLETELY-UNRELATED-domain rotation head + PROPOSAL 044 outbox append; card
> born in-progress as the designed gate hold, flipped complete in this PR's final commit
> at 2026-07-13T19:49:52Z)

## Scope

Draft a genuinely new fleet-external idea under standing owner ORDER 003 ("continue
coming up with new ideas, that is your main purpose") in the ORDER 004 rule-3
rotation (fleet backlogs → venture → game mechanics → COMPLETELY UNRELATED) —
round 7: P041 (#331) served fleet backlogs, P042 (#333) served venture, P043 (#337)
served game mechanics, so this head closes the round at the unrelated slot. Domain:
**stochastic service operations / queue-discipline design** — the supermarket
checkout pooling folk law ("ONE shared line for all registers beats a line per
register — dramatically") — a SEVENTH fleet-external domain after P017's social
choice, P024's congestion routing, P028's tournament seeding, P032's pattern races,
P036's optimal stopping, and P040's spatial self-organization. Priced as a
pre-registered hermetic discrete-time common-random-numbers sim (3 registers,
pinned integer service pmf, Bernoulli-per-tick arrivals, POOLED vs SPLIT-RANDOM
decision pair + SPLIT-JSQ reporting-only, drain-to-empty so every wait is measured
exactly, REJECT-first bands on the median per-run wait ratio at ρ = 9/10). Files:
this card (born in-progress), the claim (`control/claims/`),
`ideas/fleet/checkout-pooling-single-line-2026-07-13.md`, an `ideas/fleet/README.md`
index row, and the PROPOSAL 044 append to `control/outbox.md`. Seeds 20261313–316,
strictly above the P043 high-water 20261312 (re-swept tree-wide at HEAD `3e47fad`:
`rg -o -g '!bootstrap.py' -g '!.substrate' '202613[0-9][0-9]'` maxes at 20261312).

**📊 Model:** `fable-5` (family-level self-report from this session's own harness,
per ORDER 001 / Q-0262 — never copied from a schedule surface) · content + outbox
proposal only (idea file, card, index row, claim, outbox append; no product code,
no control/status.md or control/inbox.md writes; no sim-lab writes — the V054
verdict session runs parallel there and its claim
`control/claims/2026-07-13-verdict-054-brineward.md` is untouched)

## 💡 Session idea

**control/outbox.md needs a blessed lifecycle before it outgrows its own tooling —
a rollover convention for CLOSED blocks, groomed as an idea head because it touches
the append-only doctrine.** Measured this slice, not speculated: three days into
operation the outbox is 360,124 bytes over 375 lines (single field lines up to
7,690 chars), and this session's own first read of it FAILED — the harness Read
tool's 256 KB ceiling rejected the whole file ("File content (351.7KB) exceeds
maximum allowed size (256KB)"), forcing the grep-headers + `cut -c` field-slicing
workaround every future consumer will now need. The slice-sized form: an idea head
proposing `control/outbox-archive/YYYY-MM.md` rollover for blocks whose lifecycle
is CLOSED (proposals with finalized verdicts, served asks, posted tallies), each
leaving a one-line pointer stub, with the live file holding only open items — run
through the pipeline as a proposal precisely BECAUSE "append-only, never edit
existing blocks" is standing doctrine and a unilateral archive edit would violate
it; the verdict decides where closed-block custody lives. Dedup (this slice, at
HEAD `3e47fad`): the P033 card 💡 is an outbox DIGEST (a derived summary view —
complementary: a digest adds a read surface, rollover manages the source file's
lifecycle); the P035 💡 is a seed registry, P036 a domain ledger, P042 claims
pruning, P043 alternative-pass expiry — none touches outbox source-file growth or
the Read-ceiling wall; `rg -i 'rollover|outbox-archive' -g '!bootstrap.py' -g
'!.substrate'` at drafting HEAD: zero hits.

## ⟲ Previous-session review

Newest predecessor card (`.sessions/2026-07-13-proposal-043-brineward-band-necessity.md`,
worker slice ~19:07Z): closed clean, and two of its rituals transferred verbatim to
this slice — the blob-pinned `idea:` link discipline (P044's outbox append pins the
`3f38420` idea-doc commit exactly as P043 pinned `8e87238`) and the seed-high-water
tree-wide re-sweep (carried forward, found 20261312, allocated 20261313–316 above
it). Its 💡 (alternative-pass reasons are dated claims that expire — re-verify them
at live HEAD before hunting new sources) generalizes beyond the game slot and was
applied here in its unrelated-slot form: P040's "runners-up weighed and dropped on
merit" list was re-read before choosing this head, and each drop reason still holds
at today's HEAD (epidemic thresholds stays dropped for P024-adjacency — reasoning
recorded in P040 and honored rather than silently re-litigated). One thing visible
only from here: P043's own claim file
(`control/claims/claude-proposal-043-brineward-band-necessity.md`) still sits in
control/claims/ after PR #337 merged — meanwhile P041's and P042's were pruned by
dedicated prune branches, so the corpse census is backfill + P043 (n = 2): the
prune advisory the P042 💡 proposed is being served, but always one slice behind —
evidence for making the prune a standing step of the NEXT same-lane claim commit
rather than its own follow-up branch.

## Close-out

All pieces landed before this flip: card born in-progress @ `e7cd512`, claim @
`675e4fd` (de-noised @ `7642c4b` after a false claims-duplicate advisory keyed on
the shared backticked date-u token — advisory-only, fixed anyway), idea doc +
fleet index row @ `3f38420`, PROPOSAL 044 outbox append @ `551df24` (idea: link
pinned to the `3f38420` blob), PR #339 opened READY immediately after the push
(never draft; merge left to the enabler workflow, no agent merge). Rotation
verified at HEAD before drafting: P041/P042/P043 blocks each self-declare round 7
fleet/venture/game, ORDER 004 rule 3 names COMPLETELY-UNRELATED as the fourth
slot. Collision checks before claiming: control/claims/ listed (only the parallel
V054 sim-lab claim live — untouched), zero open PRs, no proposal-044 branch at
origin. Final verification on this tree at the flip:
`python3 scripts/check_ideas.py --outbox` exit 0 ("OK — outbox proposals and
sim-ready ideas are consistent"); `python3 bootstrap.py check --strict` red ONLY
on this card's designed born-red hold before this flip, green after. No
control/status.md, control/inbox.md, or sim-lab writes; timestamps from real
`date -u` throughout.
