# Parity-flip cadence — one pending→ported flip per band, or a named blocker

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot-next`

## Problem

Parity stands at **1/49 subsystems ported, 15/465 report goldens green** (replayable
465/465). The one flip that exists — `help`, PR #112 — was individually *ordered*
(ORDER 004 item 2, "the first green golden row"); no standing rule orders the second.
The named next lane is band-6 + live EFFECT ports, all build work: without a cadence
rule the golden-parity gate can sit at 1/49 non-vacuous coverage indefinitely while
bands push forward — which is structurally the "trust our classification" state the
four-reviewer audit called out, re-accumulating one band at a time. Meanwhile #112 just
made flips *cheap*: the A-16 door is proven end-to-end and the disposition machinery
(`apply_dispositions` incl. symmetric `<msg:N>` ref renumbering, the ratchet row format,
the documented disposition classes) is reusable.

## Idea

A standing per-band parity tail, written into the band close-out ritual: each band's
close-out either (a) drives at least one of that band's subsystems' goldens to
byte-green and flips its `parity/parity.yml` row through the A-16 door (100% declared
surface, zero exemptions, ratchet row — the #112 recipe), or (b) records a *named*
blocker class explaining why no row in the band is flippable yet. The ratchet stays
monotone by construction and the red-by-design report dashboard converges band by band
instead of waiting for a terminal parity push. Pairs naturally with the ORDER-004
binding encoding (same doctrine doc, same PR if convenient).

## Grounding

- Lane status @ [`ec2bcf2`](https://raw.githubusercontent.com/menno420/superbot-next/ec2bcf21d7517284df33f56d1082db0c8dcb9007/control/status.md)
  (fetched 2026-07-10): health line — "Parity: 1/49 subsystems ported; report leg
  15/465 goldens green (replayable 465/465; help 3/3 — verified in #112's report job,
  run 29116678733)"; phase line — the #112 flip record incl. the A-16 door criteria and
  the disposition classes that bit.
- Lane inbox @ [`ec2bcf2`](https://raw.githubusercontent.com/menno420/superbot-next/ec2bcf21d7517284df33f56d1082db0c8dcb9007/control/inbox.md):
  ORDER 004 item 2 ordered exactly one flip; nothing orders a cadence.
- Lane README @ [`ec2bcf2`](https://raw.githubusercontent.com/menno420/superbot-next/ec2bcf21d7517284df33f56d1082db0c8dcb9007/README.md):
  the `report` job is red-by-design "until full parity" — the dashboard only earns its
  keep if the number under it moves.

**Why now:** the flip machinery is one day old and its marginal cost will never be
lower; band-6 is the first band that can either adopt the cadence or set the precedent
of skipping it.
