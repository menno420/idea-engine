# Composition-parity registration diff — kill the BUG-A class before band-6 trips on it live

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot-next`

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
