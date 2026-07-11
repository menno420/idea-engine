# Band-binding doctrine encoding — make the ORDER-004 bindings survive inbox rotation

> **State:** parked(routed — lane build-direct: one doc-only lane slice writing the three ORDER-004 bindings into `docs/collaboration-model.md` beside the ORDER-010 @codex rule, codifying the walking-skeleton test convention bands 6–7 already proved as the bindings' canonical evidence form — probed 2026-07-11: ORDER 004 still acked-NOT-done at the lane heartbeat @ `910c44e` and the bindings encoded in NO doctrine doc (grep-verified), while bands 6–7 carried them anyway via emergent practice (`tests/unit/band6/` skeleton tests riding every band-6 port PR; `tests/unit/band7/*_walking_skeleton.py`, 5 files at HEAD; per-slice live-drive proof records for #144/#148/#151/#160) — practice without encoding is one seat-rotation from silent drop, and 004's `done=` flip needs a citable section; nothing sim-shaped)
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://github.com/menno420/superbot-next@910c44ebeb85c0d0db2bd6e5455176d52a023dcc · fetched 2026-07-11T08:13:45Z
> *(pin annotation: probe-time re-check pin — capture pin was `ec2bcf2` (2026-07-10); lane live HEAD via `git ls-remote` 2026-07-11T08:13:45Z = `910c44e`, re-confirmed UNMOVED 08:42:15Z at authoring time; tree reads via read-only blobless clone at the pin; the shared verify-first sweep for this section's four heads lives in [`composition-parity-registration-diff-2026-07-10.md`](composition-parity-registration-diff-2026-07-10.md)'s pin annotation — only the facts SPECIFIC to this head are restated below)*

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

## Probe report (v0, 2026-07-11)

Single-pass battery v0 (no panel trigger: routing decision, docs-only diff lane-side).
**Verify-first, this head's specifics at `910c44e`:** ORDER 004 is **still acked, NOT
done** — the lane's own heartbeat: `orders: acked=001,…,012 done=003,005,…,012`, with
the verbatim reason "still NOT marking done=004 — its done-when reads 'bands 3-9
orders carry the two binding steps' and item 5's demo rule binds every future demo"
(bands run as ordered lanes; band-7 was mid-flight at the pin, 5 slices, bands 8–9
pending). The bindings are encoded in **NO doctrine doc** — `docs/collaboration-model.md`
at the pin carries ONLY the ORDER-010 "Standing @codex review" rule (line 54ff);
zero walking-skeleton/classify-or-fix hits in any doctrine doc (grep at the pin:
hits only in retro/status/ideas). **The weakening fact, recorded honestly:** bands
6–7 carried both bindings anyway, unencoded — the lane heartbeat states "band-6 now
demonstrably carries BOTH bindings (item 3: walking-skeleton CI tests in
tests/unit/band6/ ride every band-6 port PR #117/#120/#124/#130/#133/#138 +
classify-or-fix in each testing-report)", and band-7 named the convention explicitly
(`tests/unit/band7/test_band7_{ai,ai_review,ai_settings_mutation,btd6,projmoon}_walking_skeleton.py`,
5 files at HEAD) with live-drive proof recorded per port slice
(#144/#148/#151/#160 — the heartbeat's #144 record: "ORDER 004 walking-skeleton
LIVE-DRIVE done for real: real composition root booted … four real `!btd6` posts …
through the live prefix entrypoint"). **Not overtaken — the gap is narrower than
captured, but open.**

**1. What is this really?** The battery's crux question, put plainly: is the
committed skeleton-test convention already de-facto durable encoding, or is the
one-doc PR still the missing piece? Answer: the convention is durable *evidence*
but not durable *doctrine*. What bands 6–7 built survives in the tree (test files
outlive seats), and a fresh seat porting band-8 will probably imitate the visible
`tests/unit/band7/*_walking_skeleton.py` pattern. But imitation is not binding:
nothing tells a fresh seat the pattern is REQUIRED (vs. one prior seat's style),
nothing names the classify-or-fix and demo-rule halves (which live only in test
reports and PR bodies, not in any file a seat boots from), and — decisively —
ORDER 004's `done=` flip needs something a close-out can *cite*. The lane's own
precedent (ORDER 010: "ENCODE THE RULE DURABLY: write it into the working doctrine
every Builder session boots from … so it survives inbox rotation") was executed for
@codex and is sitting there as the template.

**2. What is the possibility space?** (i) Do nothing — bands 8/9 probably imitate
band-7's convention; 004 stays open on a technicality or closes on a judgment call
without citable evidence. (ii) The captured one-doc PR — write the three bindings
into `docs/collaboration-model.md` beside the @codex rule, now CHEAPER and
BETTER-GROUNDED than at capture time: it codifies a practice two bands already
proved, naming the skeleton-test convention as the item-3 binding's canonical form
(the doc describes what the tree already does — zero behavior change, pure
encoding). (iii) Encode in the inbox only (status quo the capture already
diagnosed: one rotation from silent drop). (iv) A CI check enforcing a
`*walking_skeleton*` test per newly ported band — over-mechanized: the demo rule
and classify-or-fix halves are not lintable, and the parity gate already enforces
the golden half. The value peak is (ii).

**3. What is the most advanced capability reachable by the simplest
implementation?** One doc section (~a page) closes a P0 order: band-8/9 close-outs
cite the section, the manager sees "bands 3-9 orders carry the two binding steps"
satisfied by reference to committed doctrine plus the visible per-band test files,
and 004 — the four-reviewer audit's quality band, open since bands 3–5 — flips
`done=` on evidence instead of institutional memory. The doc also retroactively
names what bands 6–7 did, so the evidence trail is continuous.

**4. What breaks it?** Timing: bands 8/9 could run before any relay lands (the lane
merged 50 commits in ~24h; band-7 was mid-flight at the pin) — if they carry the
bindings by imitation anyway, the doc's marginal value drops to the citation
function alone (still the thing 004's flip needs). Mis-homing: if the lane's real
boot doctrine is a different doc, the section must follow the @codex rule's home,
not this capture's guess — the builder verifies at build time. Scope creep: folding
the (separately probed) effect-arming checklist into the same PR is tempting and
fine, but the two must stay separately citable sections.

**5. What does it unlock?** ORDER 004's `done=` flip on evidence at bands 8/9; a
named, citable convention for every future band seat under continuous mode
(Q-0265's fresh seats are the exact population ORDER 010's precedent worried
about); and closure of this repo's last superbot-next process head.

**6. What does it depend on?** The lane's doctrine doc being the real boot surface
(verified: `docs/collaboration-model.md` is where ORDER 010 landed); the bindings'
text (already written — ORDER 004 items 3+5 in the lane inbox, plus the live
convention to name); nothing external, no owner action, nothing sim-shaped — a
doctrine section is proven by the next band close-out citing it.

**7. Which lane should build it?** `menno420/superbot-next` — build-direct: it owns
the doc, the order, and the convention; the slice is one doc-only PR a band seat or
the lane coordinator lands between slices. Not idea-engine (this repo writes only
itself); no sim-lab question (nothing to simulate in a doc encoding an existing
practice). Routing = this section README's index + the heartbeat notes for the
manager's :30 sweep — pairs with the effect-arming checklist head (same doc, same
sweep, could ride ONE lane ORDER).

**8. What is the smallest shippable slice?** One lane doc-only PR:
`docs/collaboration-model.md` gains a "Band bindings (ORDER 004, standing)" section
beside the @codex rule — (a) walking-skeleton live-drive per band before merge
(canonical form: the `tests/unit/bandN/` skeleton-test convention + live-drive
proof in the port PR body, exactly as bands 6–7 did), (b) classify-or-fix on every
red golden replay, (c) known-red classes named in any owner-visible demo invitation
— with one line telling band close-outs to cite the section. Red/green reference:
the band-8 close-out citing it, and 004 flipping `done=` at band-9's.

**Recommendation: park** — routed (lane build-direct): the gap is real but narrower
than captured — bands 6–7 carried the bindings as emergent practice, so the one-doc
slice is now codification plus the citation hook 004's `done=` flip requires, not a
rescue; one doc-only lane PR, nothing sim-shaped, sequenced whenever the lane
breathes between waves (before band-8's close-out to get full value).
