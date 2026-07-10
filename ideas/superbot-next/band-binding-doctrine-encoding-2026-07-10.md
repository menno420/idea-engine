# Band-binding doctrine encoding — make the ORDER-004 bindings survive inbox rotation

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot-next`

## Problem

ORDER 004 (P0, the four-reviewer quality band) still cannot flip to `done=` — the lane's
own status says so explicitly: its done-when reads "bands 3-9 orders carry the two
binding steps", the item-3 binding (walking-skeleton live-drive + classify-or-fix) "has
ridden bands 3/4/5 … but bands 6-9 haven't run yet", and item 5's demo rule "binds every
future demo". Those bindings currently live **only in the inbox order text**. ORDER 010
already diagnosed this exact fragility for the @codex rule and mandated the fix:
"ENCODE THE RULE DURABLY: write it into the working doctrine every Builder session boots
from … not only in this inbox, so it survives inbox rotation and reaches every future
seat." Under continuous mode (Q-0265) bands 6-9 will be run by fresh seats; an
unencoded binding is one rotation away from being silently dropped — reopening the
audit gap ORDER 004 was filed to close.

## Idea

One doc-only PR: write the three ORDER-004 standing bindings into the same doctrine doc
the ORDER-010 rule went into (`docs/collaboration-model.md` or the boot-ritual doc —
wherever the @codex rule landed): every band-N session (a) live-drives a walking
skeleton through the real pipeline before merge, (b) replays the band's own goldens and
gives every red a named ledger class or a same-PR fix, (c) names known-red presentation
classes in any owner-visible demo invitation. Then the ORDER-004 `done=` flip stops
depending on institutional memory: band 6-9 close-outs cite the doctrine section, and
the order closes on evidence.

## Grounding

- Lane status @ [`ec2bcf2`](https://raw.githubusercontent.com/menno420/superbot-next/ec2bcf21d7517284df33f56d1082db0c8dcb9007/control/status.md)
  (fetched 2026-07-10): `orders:` line — the verbatim reasoning why 004 is acked, three
  items done, but not `done=`.
- Lane inbox @ [`ec2bcf2`](https://raw.githubusercontent.com/menno420/superbot-next/ec2bcf21d7517284df33f56d1082db0c8dcb9007/control/inbox.md):
  ORDER 004 items 3 + 5 (the bindings); ORDER 010's "ENCODE THE RULE DURABLY … so it
  survives inbox rotation" — the precedent, already executed for @codex (done=010).

**Why now:** band-6 is the first band that will run without the ORDER-004 author's
context in-session — the encoding must exist before that session boots, not after it
forgets.
