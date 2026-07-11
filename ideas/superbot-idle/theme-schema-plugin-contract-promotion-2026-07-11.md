# Theme-manifest schema promotion — carry v1's 12-pack evidence into the plugin-contract family when it is born

> **State:** parked(awaiting-arming-event — the promotion is already DECIDED (superbot §4/§7 item 3) and its evidence already exists, so nothing is sim-shaped; the arming event superbot-next#ORDER-002 has NOT fired at superbot-next HEAD `4c8c5b0` (002 `status: new`, acked-not-done, done-when hanging "ONLY on the owner-created separate repo"; every candidate contract-doc path 404) but is owner-click-distance from firing — un-park the moment a published plugin/manifest contract doc is fetchable anywhere in superbot-next OR ORDER 002 reaches done, then relay the adopt-with-evidence promotion to the manager; key the un-park check on the EVENT, never on the 404 path list — see probe report)
> **Class:** product · **Target:** `menno420/superbot-idle`
> **Grounding:** https://github.com/menno420/superbot-idle@f11c71a52d4d2adf88b2bf11f5d1134bad495be2 · fetched 2026-07-11T03:31Z (manifest row: behind)
> *(pin annotation: roster row @ fleet-manager `93d3a4d` records lane HEAD `97bfff2`; live HEAD `f11c71a` is 3 PRs ahead. The upstream absence is the LANE's own raw-probe evidence at the same pin, not this capture's assumption.)*
> **Sequence:** after superbot-next#ORDER-002 yields a published plugin/manifest contract — the promotion's arming event. At capture time the contract does NOT exist upstream: superbot-next publishes no plugin/manifest doc (`plugins.md` and `plugin-contract.md` both 404) and `superbot-plugin-hello` is an empty repo (lane PLUG-001 raw-probe evidence, `control/status.md` @ `f11c71a`).

## Problem

The directive decided (§4, re-affirmed §7 item 3, Q-0240 decide-and-flag): the
theme-manifest schema is **plugin-contract material** — drafted in the idle repo so the
games program never serializes behind the Builder, then **promoted into the contract
family later**. The draft half is done and over-delivered at lane HEAD: schema v1
frozen with a machine twin held field-for-field identical by tests, proven on 12
foreign packs across three catalog waves with ZERO schema pinches, and a gate whose
product property is "gate-green = safe to enable on a live server unreviewed"
(`docs/theme-schema.md` + `schema/theme.schema.json` + `tools/theme_gate.py` @
`f11c71a`). The promotion half has **no tracker anywhere**: the lane's QUEUE holds the
*adapter* on PLUG-001, not the schema promotion; the decided-and-flagged item lives
only as prose in a superbot planning doc. When the plugin contract is finally born,
nothing arms the promotion — the classic decided-and-flagged item that evaporates
between repos.

## Idea

This capture is that tracker, made greppable by the Sequence token above (one grep of
this tree surfaces every idea blocked on the same foreign order — README § Idea file
grammar). The promotion slice, when armed: schema v1 + theme-gate semantics + the
setup-code/provisioning contract move into the plugin-contract family **as one family**
— §4's "three versioned schemas, one discipline" (data API read · provisioning write ·
theme skin) — carrying the evidence trail (parity tests, 12 zero-pinch packs, exact
budget arithmetic, 150 cross-language vectors) as the draft's credentials. Promotion
should be adopt-with-evidence, not re-design: the contract family's theme chapter
already has a proven reference implementation, and re-drafting it upstream from scratch
would discard the only empirically-tested piece of the family.

## Grounding

- The decided split + promotion flag: superbot @ `41899e1` §4 ("the idle seat drafts v1
  in its own repo and flags it for promotion into the contract") and §7 item 3.
- Draft-half completeness: lane `docs/theme-schema.md`, `docs/current-state.md`
  § Stability baseline (schema v1, gate, 12 packs, parity tests) @ `f11c71a`.
- Upstream absence + the adapter-only hold: lane `control/status.md` § PLUG-001 and
  § QUEUE @ `f11c71a` (adapter evidence-blocked; schema promotion unmentioned).

**Why now:** both arming facts are fresh-verified this session (draft complete,
contract absent) and the capture costs one page; un-captured, the promotion duty gets
re-derived — or missed — whenever superbot-next's contract lands, by whoever happens
to notice.

## Probe report (v0, 2026-07-11)

*Single-pass battery per the README panel default (sim-lab VERDICT 002): a
tracker-disposition head has no irreversible/high-blast-radius surface, and the
verify-first sweep did not disagree with the capture. Expiry-aware read (README
§ probe order): the Sequence token is `after`, not `before` — this head does not
expire, but its arming event is imminent-but-unarmed (ORDER 002's done-when hangs
verbatim "ONLY on the owner-created separate repo" — one owner click), which is
exactly when the README's stale-grounding trap bites hardest; so every load-bearing
claim below was re-verified at LIVE HEADs this probe, not inherited from the
capture's pins. Two things moved since capture: the lane HEAD advanced
`f11c71a` → `1b3a211` (premise re-checked there, HOLDS), and sim-lab finalized
VERDICT 006 (a seam-adjacent non-event for this head — see Q6).*

**1. What is this really?**
A tracker being given its un-park condition — not a build, not a design, not an open
question. The promotion itself was decided by the owner directive (superbot @ `41899e1`
§4: "the idle seat drafts v1 in its own repo and flags it for promotion into the
contract"; re-affirmed §7 item 3; Q-0240 decide-and-flag). The draft half is done and
over-delivered at lane HEAD. What was missing — verified still missing at live lane
HEAD `1b3a211` — is any tracker for the promotion half: `git grep -i promot` across the
lane hits only kit internals, and the lane's `control/status.md` @ `1b3a211` tracks
PLUG-001 (the ADAPTER, "superbot-next plugin contract unavailable upstream",
`plugins.md` and `plugin-contract.md` both 404) with `plugin adapter (PLUG-001)`
ON HOLD-PENDING-UPSTREAM — the adapter is tracked, the promotion is not. This capture
IS the tracker; the probe's whole job is to verify the premise live (it holds), pin the
arming event's true state, and park the head with an un-park condition a future session
can execute without re-derivation.

**2. What is the possibility space?**
Two nearly-empty spaces, honestly split. **Disposition space (now):** probe-and-park
with an explicit un-park condition (this report) vs leave captured until the contract
lands (the README's stale-grounding trap: a `captured` head re-confirms a dead premise;
a `parked(awaiting-arming-event)` head names exactly what to re-check) vs route to
sim-lab (nothing to simulate — see Q7). **Promotion space (at fire time), pre-decided
by §4 but worth naming the forks a fire-time session must NOT take:** (a)
adopt-with-evidence — the contract family's theme chapter absorbs schema v1 +
theme-gate semantics + the setup-code/provisioning contract as ONE family, carrying the
evidence trail as credentials — this is the decided path; (b) upstream re-design from
scratch — discards the family's only empirically-tested member; (c) partial adoption
(schema without gate/provisioning) — breaks §4's "three versioned schemas, one
discipline"; (d) inversion — superbot-next merely links the lane's docs as canonical —
cheapest but leaves the contract family split across repos, and the family's whole
point is one home. The capture already encodes (a); the possibility space is
deliberately closed, which is itself the evidence this is park-shaped, not probe-fodder.

**3. What is the most advanced capability reachable by the simplest implementation?**
Already reached by the capture itself, and this report completes it: one page plus one
greppable Sequence token (`after superbot-next#ORDER-002`) means the fire-time session
— whoever notices the contract landed, in whatever repo they wake in — inherits via a
single tree-grep a paste-ready promotion brief with the draft's full credentials
(field-for-field parity tests, 12 foreign packs across three catalog waves with zero
schema pinches, exact budget arithmetic, 150 cross-language vectors) instead of
re-deriving the duty from prose in a superbot planning doc. The marginal implementation
this probe adds is exactly one line: the un-park condition in the State reason, keyed
on the event rather than on paths.

**4. What breaks it?**
- **Arming-event detection is passive.** Nothing polls superbot-next; the tracker fires
  only when an expiry-aware wake greps the Sequence token or reads this park reason.
  Mitigation is structural, not new work: README § probe order already prioritizes
  Sequence-carrying heads once their event is imminent, and this park reason states the
  event is owner-click-distance away — the strongest "re-check me early" signal the
  grammar has.
- **Path-keyed false negatives.** The 404 evidence enumerates four candidate paths
  (`docs/plugins.md`, `docs/plugin-contract.md`, `docs/plugin_contract.md`,
  `docs/plugins/README.md` — all 404 @ `4c8c5b0`); a contract landing at a fifth path
  (or in the owner-created separate repo ORDER 002's done-when names) would leave a
  path-keyed check reading "unarmed" forever. That is the README's #56-card lesson
  (verify the INVARIANT, not the named artifact) applied forward: the un-park condition
  is therefore keyed on the EVENT — any published plugin/manifest contract doc, or
  ORDER 002 reaching done — never on the path list.
- **Contract born incompatible.** The upstream family could define theme/provisioning
  shapes conflicting with v1. That degrades adopt-with-evidence to
  reconcile-with-evidence, not to nothing: 12 zero-pinch packs and parity tests are
  exactly the artifacts that win a reconciliation argument, and discarding them was the
  failure the §4 ruling pre-empted.
- **Conflation with PLUG-001.** The lane tracks the adapter; a fire-time session could
  mark this promotion satisfied when the adapter merely unblocks. They are distinct
  objects (adapter = lane consumes the contract; promotion = the contract absorbs the
  lane's schema family) — verified distinctly tracked/untracked at `1b3a211`, and this
  report says so out loud precisely so the confusion has to argue with a document.
- **Indefinite wait.** ORDER 002 has hung on one owner click since 2026-07-09; it may
  fire in an hour or never. A park tolerates that honestly; a sim-ready or
  needs-more-grooming disposition would not.

**5. What does it unlock?**
At fire time: the plugin-contract family is born with its theme chapter already
empirically proven — §4's "three versioned schemas, one discipline" (data API read ·
provisioning write · theme skin) starts life with its only tested member carried in
rather than re-drafted, and the games program keeps its founding property of never
serializing behind the Builder. Secondary: the lane's PLUG-001 adapter hold and this
promotion converge on one contract family instead of two half-tracked halves, and the
fleet gets a live demonstration that decide-and-flag items survive repo boundaries when
a tracker exists (the exact evaporation §4's flag would otherwise have suffered).

**6. What does it depend on?**
One hard dependency, verified un-fired: **superbot-next#ORDER-002**, whose deliverable
(4) is "docs: the plugin contract". Live state @ superbot-next HEAD `4c8c5b0`:
`control/inbox.md` reads `ORDER 002 · 2026-07-09T14:15Z · status: new`, P2; the lane's
own status shows 002 acked but NOT done (done list = 003,005,…,011) with the blocker
verbatim "ORDER 002 done-when still hangs ONLY on the owner-created separate repo"; all
four candidate contract-doc paths 404 at that HEAD. Provider side is ready and frozen:
the lane's draft half is complete at `1b3a211` (`docs/theme-schema.md` +
`schema/theme.schema.json` + `tools/theme_gate.py`, machine twin held field-for-field
by tests, 12 zero-pinch packs). One NON-dependency worth stating: sim-lab VERDICT 006
(= PROPOSAL 006 by the intake-order numbering cross) landed 2026-07-11T05:09:53Z as
approve (sim-lab `control/outbox.md` @ `d89303e`) — that lifts the lane's SIM-001
economy hold and unfreezes the ECONOMY surface, but themes carry no economy numbers and
the promotion is untouched by it; a fire-time session should not read the lane's
post-006 activity as movement on this head.

**7. Which lane should build it?**
Nobody yet — that is the point of the park. At fire time it is a cross-repo move the
manager routes: superbot-next (or the owner-created contract repo ORDER 002's done-when
names) ADOPTS; superbot-idle SUPPLIES the evidence trail; the manager writes the ORDER.
Not sim-lab: there is no reproduced-evidence question — the promotion is decided, and
its evidence (12 packs, parity tests, cross-language vectors) already exists; a sim
re-proving a frozen, test-enforced schema would re-measure the measured. Not this repo
(writes no lane code); this repo's contribution is exactly this tracker plus, at fire
time, the fan-in relay.

**8. What is the smallest shippable slice?**
Now: this report + the State flip to `parked(awaiting-arming-event …)` — ships in this
PR, zero lane surface touched. At fire time: one manager-routed promotion ORDER whose
substance the capture already wrote — the contract family absorbs
`docs/theme-schema.md` + `schema/theme.schema.json` + theme-gate semantics + the
setup-code/provisioning contract as one family chapter, evidence trail attached as the
draft's credentials, adopt-with-evidence never re-design. Explicitly NOT in any slice:
a lane-side pre-adaptation of the schema to a contract that does not exist yet (that
would be the host-seam stub mistake — guessing the host's shape preempts the chartered
definition).

### Grounding (probe-time pins — verify-first sweep, this probe session, 2026-07-11)

- Lane premise re-verified at LIVE superbot-idle HEAD `1b3a211` (moved from the
  capture's `f11c71a`): promotion tracker still ABSENT (`git grep -i promot` hits only
  kit internals); `control/status.md` @ `1b3a211` tracks PLUG-001 ("superbot-next
  plugin contract unavailable upstream", `plugins.md` + `plugin-contract.md` both 404)
  and holds `plugin adapter (PLUG-001)` ON HOLD-PENDING-UPSTREAM — adapter tracked,
  promotion untracked. Premise HOLDS at the live pin.
- Arming event @ superbot-next HEAD `4c8c5b0`: `control/inbox.md` `ORDER 002 ·
  2026-07-09T14:15Z · status: new`, P2, deliverable (4) "docs: the plugin contract";
  lane status 002 acked-not-done (done = 003,005,…,011); blocker verbatim "ORDER 002
  done-when still hangs ONLY on the owner-created separate repo"; contract-doc paths
  `docs/plugins.md` / `docs/plugin-contract.md` / `docs/plugin_contract.md` /
  `docs/plugins/README.md` all 404 at HEAD. NOT fired; owner-click-distance from firing.
- Seam note: sim-lab `control/outbox.md` @ `d89303e` — VERDICT 006 = PROPOSAL 006,
  landed 2026-07-11T05:09:53Z, approve (lifts the lane's SIM-001 economy hold; does not
  touch the theme surface).
- Decided split + promotion flag: superbot @ `41899e1` §4 and §7 item 3 (the capture's
  pin; a decided owner ruling, not a moving surface).
- This repo read at local main `c2d22cf`.

### Sequence (probe-time restatement)

- **after** superbot-next#ORDER-002 yields a published plugin/manifest contract — the
  arming event, verified NOT fired @ `4c8c5b0` this probe. Un-park condition, keyed on
  the event and never on the 404 path list: a plugin/manifest contract doc becomes
  fetchable anywhere superbot-next publishes (including the owner-created separate repo
  its done-when names), OR ORDER 002 appears in the lane's done list — then relay the
  adopt-with-evidence promotion to the manager via fan-in.

**Recommendation: park** — awaiting-arming-event: the promotion is already decided
(superbot `41899e1` §4/§7 item 3) and its evidence already exists, so nothing is
sim-shaped; the tracker premise holds at live lane HEAD `1b3a211` (adapter tracked,
promotion untracked) while the arming event superbot-next#ORDER-002 is verified
un-fired @ `4c8c5b0` yet owner-click-distance from firing — park with the un-park
condition keyed on the event (contract doc fetchable anywhere, or 002 done), then
relay the adopt-with-evidence promotion to the manager.
