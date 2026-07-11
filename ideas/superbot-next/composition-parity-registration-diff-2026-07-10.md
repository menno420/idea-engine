# Composition-parity registration diff — kill the BUG-A class before band-6 trips on it live

> **State:** parked(lane-self-served — the lane landed exactly the prescribed test itself, pre-band-6: PR #114 (merge `385df11`, 2026-07-10T21:33:42+02:00) ships `tests/unit/invariants/test_composition_parity.py` — a generic both-roots ref-set diff over ALL ref kinds — AND fixes the two named latent carriers (blackjack + rps register at import) in the same PR, plus the burn-down ledger this capture asked for ("find the instances nobody eyeballed"): `_KNOWN_ENSURE_ONLY` captured 99 refs across 8 subsystems at landing, 45 at HEAD `910c44e`, may only shrink by its own docstring contract)
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://github.com/menno420/superbot-next@910c44ebeb85c0d0db2bd6e5455176d52a023dcc · fetched 2026-07-11T08:13:45Z
> *(pin annotation: verify-time re-check pin — capture pin was `ec2bcf2` (2026-07-10, lane PR #117's merge); lane live HEAD via `git ls-remote` 2026-07-11T08:13:45Z = `910c44e`, re-confirmed UNMOVED 08:42:15Z at authoring time; tree reads via read-only blobless clone at the pin — 50 commits past `ec2bcf2` in ~24h)*

## Problem

The costliest live bug of the band-5 live-drive lane (BUG A, fixed in #111) was a
*composition* gap, not a logic gap: role pending terminals were registered only inside
`ensure_handler_refs()`, and the live composition root never ran ENSURE_REFS with zero
plugins — so the live bot booted without handlers the test root had. The lane's own
close-out notes verify the same latent pattern still sits in **blackjack**
(`sb/domain/blackjack/handlers.py`) and **rps** (`sb/domain/rps/handlers.py`):
`_register()` runs at module import, but their `pending_handler` registrations live only
inside `ensure_handler_refs()`. The declared next lane is **band-6 (games — "highest
state-machine risk")** — exactly the subsystems carrying the pattern. Each instance is
one PR to fix; the *class* costs a live debugging lane every time it recurs.

## Idea

One composition-parity test, landed **before** band-6 starts: build both composition
roots the way the test suite and the live entrypoint respectively build them, and diff
their registered ref sets — handler refs, pending handlers, compensator refs —
asserting set equality (or an explicitly listed, justified delta). This extends the
shape of #111's compensator-invariant test ("every declared compensator ref resolves to
a registered leg") one level up: not just *declared refs resolve*, but *both roots
register the same refs*. The lane already proposed the kernel of this in its own notes;
the capture adds priority (pre-band-6, not "next session sometime") and scope (all ref
kinds, not only the two known carriers — the test must find the instances nobody has
eyeballed).

## Grounding

- Lane status @ [`ec2bcf2`](https://raw.githubusercontent.com/menno420/superbot-next/ec2bcf21d7517284df33f56d1082db0c8dcb9007/control/status.md)
  (fetched 2026-07-10): phase line, BUG A record ("the live root never ran ENSURE_REFS
  with zero plugins"); `notes:` item (1) naming blackjack + rps as verified latent
  carriers and sketching "a composition-parity test diffing both roots' registered ref
  sets"; "▶ NEXT LANE: band-6 (games — highest state-machine risk)".
- Manifest superbot-next row @ [`6f283b9`](https://raw.githubusercontent.com/menno420/superbot/6f283b91160546af2864a0fd30b6e2d81b148a8f/docs/eap/fleet-manifest.md):
  gen-1 MID-MISSION band 5 — the band that paid for this lesson live.

**Why now:** band-6 is the named next lane and two of its subsystems are already
verified carriers — the test costs one session now vs. another live-bug lane later.

## Verify-and-park (2026-07-11)

*Verify-first per README § The probe battery (a captured head whose premise a live
lane-state read can settle gets a verify-and-park FIRST, keyed on the capture's
INVARIANT — escalating to a full battery pass only if the live check finds the gap
still open; the PR #66/#131 form). The live check found the head SELF-SERVED by its
own lane, so no battery pass runs and no `**Recommendation:` line is written — that
token belongs to probe reports.*

**Invariant keyed on:** "one composition-parity test diffing both roots' registered
ref sets must land **before** band-6 starts, scoped to ALL ref kinds — the test must
find the instances nobody has eyeballed."

**Verified, with citations (blobless clone at `910c44e`):**

- **The exact prescribed test EXISTS** — lane PR #114, merge `385df11`
  ("fix: blackjack/rps pending terminals register at import + composition-parity
  class-killer (BUG A)", 2026-07-10T21:33:42+02:00):
  `tests/unit/invariants/test_composition_parity.py` diffs the two composition
  roots' ref sets generically — its own docstring: the LIVE root "NEVER runs the
  `ENSURE_REFS` hooks when zero plugins are admitted … This test diffs the two
  roots' ref sets generically — a NEW plugin whose pending terminals (or any refs)
  live only inside its ensure hook fails CI here, before band-6 trips on it live."
  Both-roots, clean-subprocess, all ref kinds — the capture's full scope, not just
  the two known carriers.
- **The two named carriers were fixed IN THE SAME PR** — blackjack + rps pending
  terminals register at module import (the `sb/domain/role/handlers.py` pattern
  from #111), per the #114 merge subject and the test docstring ("Blackjack and rps
  were the two known carriers when this landed; both were fixed in the same PR").
- **The pre-band-6 sequencing HELD** — #114 was band-6's lane slice 1 (lane
  heartbeat @ `910c44e`: the band-6 record opens "#114 … the composition-parity
  class-killer"); every subsequent band-6 game port ran with the invariant in CI.
- **The "instances nobody eyeballed" clause was honored beyond the ask** —
  `_KNOWN_ENSURE_ONLY` is a committed BURN-DOWN list ("not an exemption policy:
  every entry is a standing live defect of exactly this class … Entries may only be
  REMOVED"), captured at 99 refs across 8 subsystems when the invariant landed,
  measured 45 at HEAD `910c44e` (mining 28, fishing 15, creature 1, role 1) —
  re-counted from the file at the pin during this sweep; the lane's heartbeat
  tracks the burn-down per-sha (99 → 76 → 66 → 65 → 45).

**Verdict: verify-and-park** — state flipped forward-only captured →
`parked(lane-self-served)`. The lane executed the capture's exact slice (right
test, right scope, right sequencing) before this repo's probe cycle reached it;
nothing remains to queue, route, or simulate — the residual is the lane's own
burn-down ledger, which shrinks by its own contract.
