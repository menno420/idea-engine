# Session — ORDER 008 housekeeping pass: stale-claim prune, heartbeat re-stamp, verdict-ledger echo, current-state stub fill

> **Status:** `in-progress`
> **Model/time:** Fable-class · 2026-07-13T22:46:35Z (dispatched worker slice for the
> Ideas Lab coordinator — ORDER 008 EAP final-night worklist, items 1/3/4/6. Card born
> in-progress as the designed born-red gate hold; flipped complete in this PR's final
> commit)

## Scope

Housekeeping pass over ORDER 008 (control/inbox.md, 2026-07-13T22:14Z — fm ORDER 045
relay, EAP final-night worklist; prior sweep @ `2808b16`; this slice cut at HEAD
`f7841ec`). Items worked this PR:

- **Item 1 (stale-claim prune):** `git rm control/claims/claude-ideas-link-backfill-p037-p038.md`
  — its work merged as PR #318 (squash `8e588f0`, 2026-07-13T15:56:43Z), session
  terminal. The other listed claim (`claude-proposal-047-creature-rarity-counter.md`)
  was already pruned by #354 @ `ed4429f`. Live claims untouched: the P049 drafter claim
  (V060 in flight) and the sim-lab kit-upgrade claim (kit still v1.7.0 there).
- **Item 3 (heartbeat re-stamp):** wholesale overwrite of `control/status.md`
  (coordinator grammar preserved), monotonic past the stale 2026-07-13T20:06:20Z stamp
  that knew only through V053/P044.
- **Item 4 (verdict-ledger echo):** ledger echoed through V059 in the heartbeat LOOP
  STATE (canonical ledger sim-lab control/outbox.md @ `94cdfba`).
- **Item 6 (current-state stub fill):** populate the three empty stub sections of
  `docs/current-state.md` (Stability baseline / In flight / Recently shipped) with
  verified facts, each pointing at `control/status.md` as the living record.
- **Item 5 PARKED:** ASK 004 (outbox archival convention) verified unanswered at
  fleet-manager HEAD `eff4c7d` (checked 2026-07-13T22:37Z); the archival split is
  gated on the answer per the ask itself.
- **Item 2 recorded ALREADY DONE pre-order:** round 8 closed at P048 (V059 approve);
  round 9 opened at P049 via #358.

Does NOT touch control/inbox.md or control/outbox.md.

**📊 Model:** `Fable-class` (family-level self-report per ORDER 001 / Q-0262 — never an
exact model ID anywhere in the repo) · control + docs housekeeping only (this card, one
claim add + one claim deletion under control/claims/, control/status.md wholesale
heartbeat overwrite, docs/current-state.md stub fill; no ideas/ content, no inbox/outbox
writes).

## 💡 Session idea

**A housekeeping order's per-item dispositions belong IN the heartbeat's `orders:` line,
not scattered across cards** — ORDER 008 arrived as a 6-item worklist and the honest
states diverged immediately (done-this-PR / already-done-pre-order / parked-on-ask /
done-elsewhere-#354). Writing the per-item disposition into `control/status.md` itself
(item N DONE/PARKED + citation) makes the heartbeat the single query surface a successor
needs, instead of forcing a card archaeology pass to learn that e.g. item 2 was served
by #353/#358 before the order even landed.

## ⟲ Previous-session review

Newest predecessor card (`.sessions/2026-07-13-proposal-049-magnet-press-fit-band.md`,
worker slice ~22:22Z): closed clean — claim-in-first-commit, born-red card, PR #358
opened READY and enabler-merged at 22:30:14Z; its 💡 (second-tap dedup inversion: read
the prior head's dropped runners-up FIRST) is drafting-lane doctrine and doesn't bind a
housekeeping slice, so no application here beyond noting it transferred to the round-9+
steady state. Carried flag it surfaced (FOUR cards deep): the two coexisting
claim-landing patterns (fast-lane control-only PR vs claim-in-first-commit) remain
undocumented — this slice again used claim-in-first-commit per its orders; the flag
rides to the manager sweep unchanged. Honest nit on the predecessor: none material —
its close-out enumerated every landed SHA, which this card mirrors.

## Close-out

(Filled at flip.)
