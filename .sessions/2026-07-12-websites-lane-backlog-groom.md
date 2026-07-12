# Session — groom slice: websites lane-backlog link index (fourth-re-pin reconciliation)

> **Status:** `complete`

- **📊 Model:** fable-5 · groom slice (one groom section appended to the
  lane-backlog head + this card; no code, no new idea files)

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this card's
born-red first commit carries the `ideas/websites/` collision flag per the
PR #222/#225/#243 workflow convention. Scope: ONE head only —
`ideas/websites/lane-backlog-2026-07-10.md` — plus this card.

## What this session did

Bounded grooming pass on `ideas/websites/lane-backlog-2026-07-10.md` (the
fourth re-pin landed by the PR #236 harvest), verify-everything mode — the
harvest card's claims were re-derived, not trusted:

1. **Tally reconciled — CONFIRMED 14/31/6, no correction.** The canonical
   backlog was re-fetched raw at the pin
   (`8f9765483a7df57ce426e7d11d200f10b5495ed7`) and the fetched bytes verified
   to hash to the claimed blob `e14bb15408b1f45de14eae72efe990024f0e548c` by
   `git hash-object` (prior-pin `c81ce76` fetch likewise verified to
   `0897a6f6a63a6e452689d94edd5919131e732ae1`; `git diff --no-index --numstat`
   between the fetches = +194/-30 exactly). Independent per-bullet
   classification of all 51 bullets: captured 14 (`captured` tokens); built
   31 = 3 `built` tokens + 28 `— shipped` entries; retired 6 = 3
   retired-in-place tokens + 3 `## Retired`-section `— retired` entries. One
   precision fix written into the head (number unchanged): the re-pin's
   stated granularity ("tokens plus `— shipped` entries") omits the
   `— retired` prose class — the literal stated rule reproduces retired=3,
   not 6. The reproducible count rule (state token OR em-dash outcome prose,
   section headings never) is now recorded in the groom section.
2. **Pin-integrity notes appended**, both anomalies verified against the
   prior blob with line numbers on both sides: the `## Built` heading GONE at
   `e14bb15` (heading set 10/441; was 10/90/277 at `0897a6f`), and the
   backlog's first bullet-replaced-in-place ("Route-level clock freeze",
   `0897a6f` line 80 → "Port the clock-freeze pattern", `e14bb15` line 188;
   shipped as `app/clock.py`, lane PR #130, no Built entry).
3. **Indexing rule decide-and-flag: link-index-only HOLDS.** Ten of the
   eleven new captured bullets are lane work items or asks whose routing half
   already exists (heartbeat flags per their own bullet text; the merge-hold
   pair is the probed sibling entry, PR #243). ONE candidate named, not
   captured: the **verdict-inheritance guard for carried heartbeat watches**
   — idea-shaped, fleet-relevant beyond the parked lane (heartbeat grammar is
   kit/manager territory, `/fleet` badge half spans lanes), and the only new
   bullet carrying no routing flag in its own text. No idea file created —
   named for a future probe/mint slot.
4. **Next step set: keep-as-index(re-pin cadence).** State stays `captured`
   — no disposition change, so the section README index needed no re-badge.

Read-only side check recorded for the coordinator: `control/inbox.md` at
branch time (main `f13933c`) carries ORDER 001 and ORDER 002 only — no
ORDER 003+.

## Close-out

**Evidence (auto-draft verified and corrected):**

- ideas touched (1): `ideas/websites/lane-backlog-2026-07-10.md` (groom
  section appended; grounding line conformed to the checker grammar after a
  live preflight catch — verification prose moved to the pin-annotation form)
- sessions touched (1): `.sessions/2026-07-12-websites-lane-backlog-groom.md`
  (the auto-draft's second listed card, `.sessions/2026-07-12-session.md`, is
  kit machinery's stray in-progress draft — untracked, not this slice's, left
  uncommitted)
- code touched: none · control touched: none (dispatch boundary) ·
  README/index: untouched — no state or disposition change to mirror
- git: branch `groom/websites-lane-backlog-2026-07-12` off main `f13933c`,
  born-red card first commit `a0289a0`, groom commit `3b2185e`, grammar-fix
  commit `c5e86d6`, card flip follows; draft PR #244 flipped ready per
  dispatch instructions — never merged by this slice, auto-merge never armed
  by this slice.
- verify: `python3 bootstrap.py check --strict` (red only on this card's
  designed born-red hold pre-flip; green at flip) and
  `python3 scripts/preflight.py` (10/10 PASS) run before each push.

**Judgment (the half only the session knows):**

- Decisions made: no D-entry — groom disposition only (keep-as-index). One
  judgment call, declared: the guilds[] export, provenance-token list, and
  pickup-latency bullets are all cross-lane ASKS but were NOT named as
  candidates because each already carries its routing flag (heartbeat/manager
  sweep) in its own bullet text or in the harvest card's dedup — naming them
  again would duplicate a live routing, exactly what the link-index rule
  exists to prevent.
- Next session should know: the reproducible count rule for this backlog now
  lives in the head's groom section — count state tokens OR em-dash outcome
  prose (`— shipped` / `— retired`), never section headings; three of the six
  retired entries are prose-classified. Guard recipe: any future
  `check_harvest --bullet-drift` bucket-count feature should implement that
  rule, not a heading-grouped count (`## Built` is gone at `e14bb15` and the
  head predicts heading-grouped over-counting until the lane restores it).

## 💡 Session idea

The lifecycle tally in this head is stated per re-pin as prose ("14 captured,
31 built, 6 retired") but the CLASSIFIER that produces it lived nowhere — this
groom had to reverse-engineer it, and the fourth re-pin's own stated
granularity turned out to reproduce only 3 of the 6 retired (the `— retired`
prose class under `## Retired` is invisible to the stated "tokens plus
`— shipped`" rule; the number was right anyway, the rule wasn't). Cheap
checker seed, same family as the harvest card's bullet-title-set 💡: teach
`check_harvest --bullet-drift` an optional `--lifecycle-tally` that applies
the now-written rule (state token OR em-dash outcome prose, headings never)
and prints the three-bucket count next to the line delta — a re-pin section
then QUOTES the checker instead of hand-counting, and a tally that cannot be
reproduced from the pinned blob fails loudly at harvest time instead of
surviving re-pins unverified.

## ⟲ Previous-session review

The fourth-reharvest card (`2026-07-12-websites-fourth-reharvest.md`, PR #236)
held up on every load-bearing claim under byte-level re-verification: both
blob SHAs (`0897a6f` → `e14bb15`) reproduced exactly by `git hash-object` on
raw fetches, the +194/-30 sizing reproduced exactly by `git diff --no-index`,
the 14/31/6 tally reproduced exactly by independent per-bullet count, and
both recorded anomalies confirmed with line numbers on both blobs. Its
deduped-not-indexed verdict on the eleven new bullets also held, with one
refinement this groom adds: the verdict-inheritance guard is the one bullet
of the eleven with NO routing flag anywhere (the card grouped it under "lane
work items/routed asks"), which is why it gets named as a candidate. Workflow
improvement, fed by the one gap found: a re-pin's tally sentence should state
a rule that reproduces its own numbers — this card's 💡 turns that into a
checker seed so the fix outlives prose.

## Handoff → next wake

The head's disposition is keep-as-index(re-pin cadence); the lane chain is
PARKED at `8f97654`, so the next re-pin fires on the first harvest sweep that
finds websites HEAD moved. For the coordinator: ONE candidate named for a
future probe/mint slot — verdict-inheritance guard for carried heartbeat
watches (fleet-relevant, no routing flag, lane self-serve never comes) — and
the inbox side check found no ORDER 003+ at main `f13933c`. Checker seeds now
queued in this family: bullet-title-set diff (harvest card 💡) +
lifecycle-tally reproduction (this card's 💡) — both land in the same
`--bullet-drift` surface if a kit slice ever picks them up together.
