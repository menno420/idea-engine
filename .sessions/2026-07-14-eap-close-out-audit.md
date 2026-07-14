# Session — EAP close-out project audit (ORDER 011): the Ideas Lab seat's definitive what-worked/what-walled ledger, both repos

> **Status:** `complete`
> **Model/time:** fable · 2026-07-14T09:02:52Z (Ideas Lab worker slice — land the
> owner's EAP CLOSE-OUT AUDIT directive as inbox ORDER 011, then the audit
> doc `docs/audits/eap-project-audit-2026-07-14.md` covering BOTH repos
> (idea-engine + sim-lab). Card born in-progress as the designed gate hold;
> flipped complete in this PR's final commit at 2026-07-14T09:14Z. PR #413.)

**📊 Model:** fable-family · docs+control slice (this card, the claim file,
control/inbox.md ORDER 011 append, docs/audits/eap-project-audit-2026-07-14.md,
docs/AGENT_ORIENTATION.md router link; no control/status.md writes, nothing
in sim-lab, no other session's claims/PRs touched)

## Scope

Land the owner's EAP close-out audit directive (given live in the coordinator
chat) verbatim as `control/inbox.md` ORDER 011, then ship the deliverable it
names: the seat's definitive EAP audit — what this project used, what it
couldn't use, where it lost time, what it fixed, what still hurts — every
finding dispositioned FLEET-FIX / ANTHROPIC / ACCEPTED, sections 1–11 exactly
per the directive, both repos covered, every claim cited (path@SHA / PR # /
verbatim denial), numbers measured not estimated.

STEP 0 (finish in-flight work first) was completed by a sibling slice before
this session began: idea-engine PR #361 closed-as-superseded with a cited
evidence comment; sim-lab ORDER 006 outbox rollover landed via sim-lab PR
#134 → main 5356b2a; sim-lab ORDER 007 walls→capability-seed-fence fold
landed via sim-lab PR #136 → main b10ffce. Nothing parked at STEP 0; the one
in-flight item at audit time (sim-lab V073 build, PR #135, open) is reported
in the audit's §11 and deliberately NOT interfered with.

## Constraints honored

- control/inbox.md append-only: ORDER 011 appended via shell after the
  existing bytes; no existing block touched.
- control/status.md untouched (coordinator-only).
- sim-lab untouched entirely (V073 session live there — PR #135 is theirs).
- Other sessions' claims untouched (order-008 housekeeping, P062 drafter,
  V073 builder claims all left as found).
- No merge/arm calls on this PR — merge-on-green owns the landing.
- All timestamps from real `date -u`.

## Deviations, disclosed

- The tasking asked for the audit doc's Status badge to read `complete`; the
  repo's `[badge]` checker rejects that token for docs (allowed:
  archive/audit/binding/historical/ideas/living-ledger/owner-guidance/plan/
  reference — verbatim finding captured pre-fix). Badge shipped as `audit`
  with a FINISHED line in the doc header. The checker's grammar wins over a
  prose instruction — that is the doc-vs-source rule applied to tasking.

## 💡 Session idea

**An audit's §11 is where its credibility is priced — and the cheapest way to
fund it is to write down what you COULDN'T measure at the moment you fail to
measure it, not at synthesis time.** This audit's honest-gaps section cost
minutes because every mining pass had already recorded its own nulls inline
("not measured", "verbatim text lost to a PR body", "0 hits — honest null");
the sections that would have been expensive to reconstruct (owner-click vs
PAT ambiguity, the live-sibling measurement holes) were free because the
measurement notes carried their own caveats. The durable pattern for any
multi-worker synthesis: require each upstream report to ship a "couldn't
measure + why" trailer, and the final document's hardest section assembles
itself — the alternative is a synthesis-time archaeology pass that either
burns a session or, worse, silently omits the gaps.

## ⟲ Previous-session review

Previous session in this seat's chain: the ORDER 006/007 close-out (sim-lab
PRs #134 → main `5356b2a` and #136 → main `b10ffce`). Re-verified its central
claims against sim-lab origin/main at this session's HEAD rather than taking
its report on faith: live `control/outbox.md` is **41,974 B exactly** as the
session reported (< the 200 KB fm threshold), `control/outbox-archive-2026-07.md`
exists at **1,071,719 B exactly**, the live file carries **128** "ROLLED
2026-07-14" pointer stubs matching the claimed 128 rolled terminal blocks,
`grep -c '^## VERDICT '` parity = 72 holds, and the `substrate-kit:capability-seed`
fence is present and non-empty in `docs/CAPABILITIES.md` (lines 19–142) with
the walls digest section rendering in `docs/seat-digest.md` — five for five,
byte-exact. Two things it did notably right: it read the fm convention doc AT
SOURCE via the raw.githubusercontent bypass instead of trusting the ORDER's
summary (catching that the archive is per-MONTH, not per-day — the prompt's
guessed filename was wrong), and it disclosed the fence trade (lane rows
inside the kit-owned fence will make the next kit upgrade report it
consumer-edited) next to the work instead of leaving it for the upgrade
session to discover. One nit forward: its new-wall entry (fleet-manager MCP
denial + raw bypass) is recorded in sim-lab's CAPABILITIES append log but the
twin ledger here in idea-engine was left untouched — the same wall binds this
repo's sessions, and the venue doctrine ("a flat CAN/CANNOT ledger is wrong
somewhere by construction") cuts both ways; whoever next touches
`docs/CAPABILITIES.md` should mirror the entry with its scope noted.
