# Session — PROPOSAL 043: Brineward band-2 necessity (game-mechanics slot, round 7)

> **Status:** `complete`
> **Model/time:** Claude Fable · 2026-07-13T19:07:52Z (Ideas Lab worker slice — draft the
> round-7 GAME-MECHANICS rotation head + PROPOSAL 043 outbox append; card born
> in-progress as the designed gate hold, flips complete in this PR's final commit)

## Scope

Draft a genuinely new game-mechanics idea under standing owner ORDER 003
("continue coming up with new ideas, that is your main purpose") in the ORDER 004
rule-3 rotation (fleet backlogs → venture → game mechanics → unrelated) — round 7:
P041 (#331) served fleet backlogs, P042 (#333) served venture, so this head is the
round's GAME-MECHANICS slot. Subject: gba-homebrew's **Brineward** arc (the sibling
game P039 explicitly passed on when it had "no committed score surface yet" — nine
slices have shipped since, at drafting HEAD `8bac80a` the band/price/hold tables are
all committed constants), priced as a pre-registered hermetic band-routing economy
sim: does the concept doc's own load-bearing line "tier prices roughly triple per
step so band-2 runs stay necessary, never optional" survive honest duel risk, and
does "greed has a shape: one more fight or turn for home?" have a measurable
interior answer? Expected files: this card (born in-progress), the claim
(`control/claims/`), `ideas/gba-homebrew/brineward-band-necessity-2026-07-13.md`,
an `ideas/gba-homebrew/README.md` index row, and the PROPOSAL 043 append to
`control/outbox.md`. Seeds 20261309–312, strictly above the P042 high-water
20261308 (re-swept at HEAD `e52f212` + sim-lab outbox at drafting).

**📊 Model:** Claude Fable · content + outbox proposal only (idea file, card, index
row, claim, outbox append; no product code, no control/status.md or
control/inbox.md writes; no sim-lab writes — a V053 verdict session runs parallel
there and its files are untouched)

## 💡 Session idea

**"Alternatives passed on merit" entries need an expiry check — a pass reason is
a dated claim about a MOVING repo, so the next same-slot drafter's FIRST move
should be re-verifying each named alternative's pass reason at live HEAD before
hunting a new source.** This slice's entire subject came from exactly that move:
P039 (drafted ~16:33Z against gba-homebrew `d87f9ad`) passed on Brineward with
"concept tree mid-build, no committed score surface yet" — and by this slice's
drafting clone (~18:58Z, HEAD `8bac80a`) NINE Brineward slices had shipped,
turning the pass reason false within hours and leaving a 5×-value-gradient
economy head sitting fully committed and unmined. The slice-sized form: the
rotation slot's drafting ritual records each pass reason WITH the HEAD it was
true at (P039 already does this implicitly — its clause quotes no SHA), and the
next drafter greps the previous slot head's "Alternatives passed on merit"
section and re-checks each reason against a fresh `ls-remote` HEAD before
surveying new repos — the cheapest new head is often a previously-passed one
whose pass reason expired. Dedup (this slice, at HEAD `e52f212`): the P036 card
💡 is a per-round DOMAIN ledger (which repo, read-cost), the backfill card 💡 is
fast-lane check coverage, the P042 card 💡 is claims pruning, the P035 💡 a seed
registry, the P033 💡 an outbox digest — none touches alternative-pass staleness
or re-probe ordering; `rg -i "passed on merit|pass reason" -g '!bootstrap.py'
-g '!.substrate'` hits only the slot heads' own sections, no process capture.

## ⟲ Previous-session review

Newest predecessor card (`.sessions/2026-07-13-proposal-042-channel-concentration.md`,
worker slice ~18:26Z): closed clean and unusually load-bearing — its Scope
section documents the pre-claim collision check file-by-file (four residual
claims manually classified), which is exactly the evidence its own 💡 (a
landed-claim prune advisory) needs to justify itself, and its seed-high-water
ritual (tree-wide `rg` sweep + explicitly naming control/status.md's
"20261300" line as stale prose, not an allocation) transferred verbatim to
this slice — carried forward, found 20261308, allocated 20261309–312 above
it. One thing visible only from here: its claim file
(`control/claims/claude-proposal-042-channel-concentration.md`) still sits in
control/claims/ after PR #333 merged — the corpse class its own 💡 names,
now n=3 (backfill, P041 pruned at #335, P042 pending) — so the prune-advisory
idea has grown its own evidence base and deserves a build slot soon.

## Close-out

All pieces landed before this flip: card + claim @ `0f51c04` (PR #337 opened
READY immediately after — never draft; auto-merge left to the enabler, no agent
merge), idea doc + gba-homebrew index row @ `8e87238`, PROPOSAL 043 outbox
append @ `e1df9fc` (idea: link pinned to the `8e87238` blob). Final
verification on this tree at the flip: `python3 scripts/check_ideas.py
--outbox` exit 0 ("OK — outbox proposals and sim-ready ideas are consistent");
`python3 bootstrap.py check --strict` red ONLY on this card's designed
born-red hold before this flip, green after. No control/status.md,
control/inbox.md, or sim-lab writes; timestamps from real `date -u`
throughout; V053's parallel claim untouched.
