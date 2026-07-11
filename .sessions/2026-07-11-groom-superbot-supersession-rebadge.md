# Session — groom: superbot supersession re-badge sweep (index echoes + pointer census @ c77ee0d6)

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-11 ~11:22Z (worker slice, dispatched by the
> coordinator under continuous-chaining mode per Q-0265)

## Scope — the slice plan

The our-repo half of PR #160's recommendation (its 💡: adoption-record retirement
sweep): sweep superbot's supersession pointers against our link-indexed surface in
`ideas/superbot/`, flip every badge the pointers make MECHANICAL, report (not flip)
every judgment-laden one, and route the canonical-side half to the manager (Q-0260 —
this repo writes no superbot lane files). Plus the INDEX-ECHO class the sweep
surfaces on our own side: section-README bullets whose state token still reads bare
`parked` while the local idea file already carries a full terminal
`parked(<reason>)` state line (the #159/#160 flips echoed their own bullets; three
older parked bullets never got the echo).

Claim rode this branch's first commit per the #157/#159 precedent
(`control/claims/` re-read at origin/main `b627d12` at branch cut — empty except
README.md; no live claim on ideas/superbot). Claim cleared in the close-out commit.

## Pinned enumeration summary (established by the coordinator's sweep, trusted here)

Superbot enumerated at pinned live HEAD `c77ee0d662aeaff892623c445297c5f2952de34d`
(short `c77ee0d6`): **621 supersession-grammar hits** repo-wide, ~95 doc-level
pointers, of which **4 target `docs/ideas/`** (our link-indexed surface). Verdicts
per target:

1. `docs/planning/projects-eap-activation-plan-2026-07-07.md:7-8` supersedes ONLY
   the "next lifecycle step" of
   `docs/ideas/claude-code-projects-for-the-rebuild-2026-07-07.md` (partial;
   canonical Status still `ideas`). Our entry ALREADY parked(overtaken) via PR #160
   / merge `b627d12` — **no flip**.
2. `docs/ideas/central-admin-and-logging-guilds-2026-07-02.md:83-84` supersedes only
   "the destination question" in
   `docs/ideas/railway-deploy-alerts-discord-webhook-2026-07-02.md` (partial) —
   judgment-laden, **report only**.
3. `docs/ideas/superbot-fresh-rebuild-vision-2026-06-30.md` carries a
   superseded-IN-PART update block (extended by
   `docs/planning/fresh-rebuild-strategy-2026-07-02.md`; canonical Status still
   `ideas`) — judgment-laden, **report only**.
4. `docs/ideas/README.md` (target of an idea-roadmap-inventory banner) — canonical
   index, not an indexed idea — **n/a**.

Pointer-sweep mechanical yield: ZERO badge flips. The mechanical yield is the
index-echo class below.

## Planned flips (index-echo only; idea files untouched — already terminal)

Verified in this tree at branch cut (file `> **State:**` line vs README bullet):

- `rebuild-websites-cutover-role-2026-07-10.md` — file `parked(routed — …)` (flipped
  by PR #159, merge `03ace5f`); bullet (README line 189) bare `parked` → echo
  abbreviated `parked(routed — <short>)` per the #160 bullet-format precedent.
- `competitive-teardown-2026-07-10.md` — file `parked(reference — …)`; bullet
  (line 73) bare `parked` → echo the file's reason exactly (short enough).
- `wire-level-live-bot-loop-2026-07-10.md` — file `parked(contradicted-in-part by
  superbot canonical-plan F-4, PR #1770 — do not build as written)`; bullet
  (line 255) bare `parked` → echo exactly.

Read-only verifications for the report: claude-code-projects `parked(overtaken)`
both sides (line 59, #160); railway-deploy-alerts `captured` both — leave;
fresh-rebuild-vision `captured` both — leave; supersede-banner-integrity-checker +
fleet-manifest-freshness-checker `historical(…)` file / `historical` bullet — the
self-historical pair, leave.

**📊 Model:** fable-5 · docs-only grooming slice (3 index-bullet re-badges + card +
claim add/clear + heartbeat; no idea-file edits, no code)

## 💡 Session idea

**Index-echo drift is mechanically checkable — stop sweeping it by hand.** All three
of this slice's flips are the same defect: a file's `> **State:**` head token
drifted ahead of its section-README bullet's state token. A ~20-line addition to
`scripts/check_ideas.py` (or a `check_harvest` mode) that parses each indexed
bullet's state token and warns when it disagrees with the file's state-line head
token (`parked` vs `parked(...)` counts as agreement only bare-vs-bare) would have
caught all three at #159/#160 merge time — the same class of drift the canonical
side polices with `check_supersede_integrity.py`. Anchors:
`ideas/superbot/README.md` bullet grammar, `scripts/check_ideas.py` state-line
parser.

## ⟲ Previous-session review

PR #160 (`.sessions/2026-07-11-probe-claude-code-projects.md`, merge `b627d12`) —
verified against this tree at branch cut: the probe report append, the
captured → parked(overtaken) state flip, the Grounding pin at live `c77ee0d`, and
the section-README index echo (line 59) all land exactly as carded, and the #158
Self-review section survived verbatim on the heartbeat. What it did well: the
four-pin verify-first discipline (superbot `c77ee0d`, superbot-next `f87ffb0`, fm
roster `3150f0e`, websites `92c3dc6`, canonical doc byte-diffed against the harvest
pin) turned a plausible-looking live head into an honest "this WON already" park —
and its 💡 (adoption-record retirement sweep) is precisely the head this slice
executes on our side and routes canonical-side to the manager, so the card→slice
pipeline worked as designed. One nit: it echoed its OWN bullet but left the three
sibling parked bullets bare — an index-echo pass over the whole section costs one
grep and would have made this slice unnecessary; folded into this card's 💡 as a
checker so the class dies structurally.
