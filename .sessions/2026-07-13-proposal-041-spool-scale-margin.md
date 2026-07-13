# Session — PROPOSAL 041: spool-scale go/no-go margin (FLEET-BACKLOGS rotation, round 7)

> **Status:** `complete`
> **Model/time:** fable · 2026-07-13T17:55:22Z (Ideas Lab worker slice — draft the
> FLEET-BACKLOGS rotation round-7 head under standing owner ORDER 003. Card born
> in-progress as the designed gate hold; flips complete in this PR's final commit
> once both checkers verify green and the 💡 slot resolves)

**📊 Model:** fable (Claude Fable family) · content + outbox proposal only (idea
file, card, fleet index row, claim file, outbox append; no control/status.md or
control/inbox.md writes; no checker or script changes; nothing in sim-lab)

## Scope

Draft a genuinely new sim-shaped idea for the FLEET-BACKLOGS rotation slot,
round 7, under standing owner ORDER 003 (continuous pipeline — "continue coming
up with new ideas, that is your main purpose") and ORDER 004 rule 3's rotation
("fleet backlogs → venture's book/product space → game mechanics → COMPLETELY
UNRELATED domains"). Round 6 closed fully served: P037 = fleet-backlogs
(fleet-manager review-queue N=50), P038 = venture (KU exclusivity fork),
P039 = game mechanics (Gloamline survival ceiling), P040 = unrelated (Schelling
tipping) — so round 7 opens at the fleet-backlogs slot. Slot rounds 1–6 and
their harvest SOURCES: P019 websites → V021 approve, P021 superbot → V023
reject, P025 substrate-kit claims doctrine → V027 reject, P029 substrate-kit
lease-renewal → V031 null, P033 superbot assign-at-merge → V035 null, P037
fleet-manager review-queue → (verdict pending at drafting). Round 7 rotates the
harvest source to a SIXTH repo, untapped by ANY prior proposal: curious-research
(the 9th seat, maker/3D-print research — public raw-readable per superbot
docs/fleet-reading-path.md §0/§2, raw-fetched this slice; pokemon-mod-lab DARK,
skipped per the path's own rule), read at live HEAD
`a9fd5faa6a10b4d1364d205dbeac7a8678e1bd73` (ls-remote-verified, shallow clone
this slice). The harvested head: the spool-weight-scale build's own honest-scope
contract ships an UNQUANTIFIED load-bearing default — "±5 g resolution …
'exactly enough to finish this print' is not [trustworthy] — leave yourself
margin" (projects/spool-weight-scale/README.md § Honest expectations @ a9fd5fa)
— with no number for the margin, plus the unmeasured comparative claim "Your own
measured empty weight beats the seeded table, every time" (same file, Stage 2).
PROPOSAL 041 prices both as a pre-registered hermetic error-budget sim: margin
grid × three tare-knowledge regimes, exact-enumeration decision arm + seeded
confirmation arm, REJECT checked first, seeds 20261301–304 strictly above the
P040/V051 high-water 20261300. Verified before claiming at HEAD `ee4fb76`: no
PROPOSAL 041 in control/outbox.md, no P041 claim in control/claims/, zero open
PRs on the repo, seed high-water still 20261300 (P040; sim-lab tree grepped —
the two larger numerals there are substring artifacts inside a fraction and a
float, not seeds), and the tree-wide dedup sweep `rg -i -g '!bootstrap.py'
-g '!.substrate' 'spool|filament|load.cell|tare|hx711'` returns only the
venture-lab makerbench gift-repo BLUEPRINT mentions (a repo plan, not a sim
head — no proposal prices any measurement-error decision rule). Idea file
`ideas/fleet/spool-scale-go-no-go-margin-2026-07-13.md` (probed single-pass
this slice, sim-ready), appended to `control/outbox.md` as PROPOSAL 041.
ORDER 004 rule 4 untouched: nothing here builds makerbench — this is
harvest → probe → outbox only.

## 💡 Session idea

**Commit the seed high-water as a machine-readable ledger line in the outbox
header — every drafter currently re-derives it by grepping numeric literals
across TWO repos.** This slice's step-2 recon had to (a) grep every
`20[0-9]{6,8}` literal across control/outbox.md, (b) shallow-clone sim-lab and
grep ITS tree, and (c) manually rule out two false positives there (a numeral
substring inside a results-JSON exact fraction and inside a float) before it
could honestly register 20261301–304. P040's card flagged the first half of
this cost (its 💡 cited P035's tail-readable ledger-line idea for THIS repo's
blocks); what only this slice's sweep surfaced is the cross-repo half and the
false-positive class: the high-water is defined over proposals AND sim-lab
verdicts, so a this-repo-only ledger line still leaves every drafter one
sim-lab clone + one substring-artifact judgment away from a collision. The
retiring fix is one convention line in the outbox header block (single-writer,
append-updated by each proposal slice: `seed-high-water: NNNNNNNN · PROPOSAL
nnn`), plus a check_ideas.py --outbox advisory that reds a NEW proposal block
registering seeds at or below the declared line — hermetic, no network, and
sim-lab's verdicts inherit it for free because verdicts consume pre-registered
proposal seeds and allocate none of their own (verified this slice across
V001–V051's tree: zero independent seed allocations found). Dedup: extends —
not repeats — P035's 💡 (tail ledger line, this repo only) and P040's 💡
(SHA-pin resolution, a different field class); no checker or header change
shipped this slice (content-only scope held).

## ⟲ Previous-session review

Newest predecessor card (`.sessions/2026-07-13-proposal-040.md`, the
unrelated-slot round-6 Schelling slice, flipped ~17:24Z): honest and thorough —
its close-out quoted both checker outcomes with the born-red hold correctly
framed, its seed registration prose named the re-check scope, and its 💡
(resolve this-repo SHA pins via `git cat-file -e` at lint time) is a real,
cheaply-buildable gap with the dedup done properly against four adjacent heads.
Two things visible only from here: first, its claim rode a separate fast-lane
claim PR (#324) while its card's own close-out had to explain that split — this
slice's dispatching coordinator ordered the claim onto the work branch instead,
which read cleaner end-to-end and cost one fewer PR; second, the P040 card's
high-water re-check ("re-checked across all prior blocks") was again
THIS-REPO-ONLY prose — it happened to be correct because sim-lab allocates no
seeds of its own, but nothing in the card evidences that the sibling tree was
ever swept, which is exactly the gap this slice's 💡 wants to retire
mechanically rather than by each drafter's diligence.

## Close-out

All pieces landed before this flip, in the dispatched born-red order: card born
in-progress @ `060aefd` (first commit on the branch, the designed gate hold);
claim + idea doc `ideas/fleet/spool-scale-go-no-go-margin-2026-07-13.md` +
fleet index row @ `8495c24`; outbox PROPOSAL 041 append (append-only, heading
stamp from real `date -u`, `idea:` blob link pinned at `8495c24`) @ `557031c`;
branch pushed; PR #331 opened READY (never draft; auto-merge left to the
enabler — no agent merge). Verification on this tree at the flip:
`python3 scripts/check_ideas.py --outbox` exit 0 ("check_ideas: OK — outbox
proposals and sim-ready ideas are consistent"); `python3 bootstrap.py check
--strict` exit 0 once this badge flipped — its only red before the flip was
the designed born-red hold on this very card, plus the pre-existing
never-exit-affecting owner-action advisory on control/status.md (predates and
is untouched by this slice). Rotation verified at HEAD `ee4fb76` against the
ORDER 003/004 threads verbatim before drafting (round 7 = fleet-backlogs;
ORDERs 005/006/007 read and confirmed non-superseding — SIM-REQUEST serving
and the night report, already marked done on the heartbeat, do not alter the
rotation). Seeds 20261301–304 registered strictly above the verified
high-water 20261300 (outbox + sim-lab tree both swept; 20261304 aux never read
by any decision number). Dedup sweep `rg -i -g '!bootstrap.py'
-g '!.substrate' 'spool|filament|load.cell|tare|hx711'` → only the makerbench
blueprint mentions at drafting HEAD. No control/status.md, control/inbox.md,
or sim-lab writes; V050/V051 parallel-session files and branches untouched;
timestamps from real `date -u` throughout.
