# Parity-flip cadence — one pending→ported flip per band, or a named blocker

> **State:** parked(overtaken — the lane built a STRONGER mechanism than the captured rule: a dedicated continuous-mode parity-flips lane (Q-0265) ran waves 1–6 and flipped 22 subsystems pending→ported in ~24h (`ec2bcf2..910c44e`; `parity/parity.yml` @ `bd211e9` = 23/49 ported, gate GREEN 151/151 goldens, #163) — the idling-gate risk class this capture priced is dead; honesty note: no cadence *rule* was ever written into any close-out ritual, and the mechanism moots the need)
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://github.com/menno420/superbot-next@910c44ebeb85c0d0db2bd6e5455176d52a023dcc · fetched 2026-07-11T08:13:45Z
> *(pin annotation: verify-time re-check pin — capture pin was `ec2bcf2` (2026-07-10); lane live HEAD via `git ls-remote` 2026-07-11T08:13:45Z = `910c44e`, re-confirmed UNMOVED 08:42:15Z at authoring time; tree reads via read-only blobless clone at the pin; the shared verify-first sweep for this section's four heads lives in [`composition-parity-registration-diff-2026-07-10.md`](composition-parity-registration-diff-2026-07-10.md)'s pin annotation — only the facts SPECIFIC to this head are restated below)*

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

## Verify-and-park (2026-07-11)

*Verify-first per README § The probe battery (the PR #66/#131 verify-and-park form —
invariant-keyed live check first, battery only if the gap survives). The live check
found the risk class this capture priced DEAD, killed by a stronger mechanism than the
one it prescribed, so no battery pass runs and no `**Recommendation:` line is written.*

**Invariant keyed on:** "without a cadence rule the golden-parity gate can sit at 1/49
non-vacuous coverage indefinitely while bands push forward."

**Verified, with citations (blobless clone at `910c44e`):**

- **The gate did not idle — it converged 22 flips in ~24h.** `parity/parity.yml` @
  `bd211e9` (#163, the newest flip at the pin) counts **23/49 subsystems ported**
  (was 1/49 at the capture's `ec2bcf2` pin — 22 pending→ported flips across
  `ec2bcf2..910c44e`, 26 `parity:` commits total in the range); gate GREEN —
  "151/151 goldens across the 23 ported subsystems replay clean at `bd211e9`" (lane
  heartbeat @ `910c44e`, citing gate job 86525137517 in run 29145082777); report leg
  191/465 goldens green, was 15/465.
- **The operative mechanism is a dedicated lane, not a per-band tail.** The lane
  heartbeat @ `910c44e` records a standing **parity-flips lane** under continuous
  mode (Q-0265): "two waves shipped (wave 1 #118/#119/#121/#123/#125, wave 2
  #128/#129/#131/#132) PLUS post-wrap wave-3 sibling flips", then wave-4
  (#143/#145), wave-5 (#152/#154/#157), wave-6 (#163) — flips ride the A-16 door
  exactly as this capture prescribed (per-flip golden counts in every merge
  subject), but on a dedicated always-on cadence that converges far faster than
  one-flip-per-band-close-out ever could.
- **Honesty note — the captured RULE was never written.** No band close-out ritual
  doc carries a parity-tail clause (grep at the pin: cadence/close-out hits only in
  retro/status/ideas, not in any doctrine doc). The lane leapfrogged the rule: a
  standing lane that does nothing but flip rows makes a "at least one flip per band"
  floor moot — the floor was priced against build-lane-only bands, a world that no
  longer exists under Q-0265.
- **The capture's other half was consumed independently** — "pairs naturally with
  the ORDER-004 binding encoding (same doctrine doc)": that half lives on as this
  section's [`band-binding-doctrine-encoding-2026-07-10.md`](band-binding-doctrine-encoding-2026-07-10.md),
  probed separately this same sweep (full battery — its gap survives).

**Verdict: verify-and-park** — state flipped forward-only captured →
`parked(overtaken)`. The risk class (idling gate) is dead by measurement, the
mechanism that killed it is stronger than the prescribed rule, and writing the rule
now would ritualize a floor the lane's real cadence exceeds by an order of
magnitude; nothing to queue, route, or simulate.
