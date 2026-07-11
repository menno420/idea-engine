# Patch-only egress doctrine — encode why the repo went private, before anything leaves it

> **State:** parked(build-direct — one lane doctrine PR: README egress-protocol paragraph — patch-format only against a named clean base for anything that ever leaves, repo private indefinitely, venture use permanently out of scope — plus a repo.private CI assert and an egress-scoped ROM/blob tripwire, never a tree-wide lint; nothing sim-shaped — doctrine text and a lint are proven by their own red/green; sequenced before any first post-EAP egress and routed with the 2026-07-14 owner-sitting bundle, same routing decision as the playtest-kit park)
> **Class:** process · **Target:** `menno420/pokemon-mod-lab`
> **Grounding:** https://github.com/menno420/fleet-manager@1afca50e171a33591f8481f0ac837b989c280425 · fetched 2026-07-11T08:09Z
> *(pin annotation: probe-time re-grounding — the capture's superbot fleet-manifest pin `53fb5ef` is a tombstone (superseded by the fm generated roster, fleet-manager PR #59 `b0639a9`); fleet state re-read at fleet-manager HEAD `1afca50` — the SAME pin the #131 and #134 probes read, third consecutive read, ls-remote 2026-07-11T08:08:14Z; surfaces: roster gen #5 pokemon row · `docs/playbook.md` R22 · `docs/dispatch-log.md` visibility-saga entries · `docs/owner-queue.md` items 3–4 · `docs/review-queue.md` pokemon#8 row · `docs/findings/night-review-2026-07-10.md` Q16 + remediation item 1 · `docs/proposals/instructions/game-lab.md`; superbot router re-read live at HEAD `58040c6` (Q-0260 rule 3, Q-0262.7); substrate-kit CHANGELOG read at its live HEAD `be72c09`; the lane repo itself is the standing DARK wall — re-verified three ways 2026-07-11T07:32Z by the #131 probe (raw 404 ×2, ls-remote auth wall, MCP scoped here) and not re-paid same-day per docs/CAPABILITIES.md — all lane facts below are roster/manager-relayed, shape-not-content)*
> **Sequence:** before the lane's first post-EAP egress event (none is planned on any manager surface at the pin — the 2026-07-14 owner sitting is the event most likely to generate the first share ask, and it bundles Lumen Drift's PUBLIC publish in the same sitting)

## Problem

The repo was flipped private **urgently** on 2026-07-10 — the manifest row records it
as "PRIVATE ✅ (API-verified ~15:12Z — the URGENT flip happened)". The urgency is the
tell: this lane's tree contains Nintendo-derived content that must not sit on a public
surface, in explicit contrast to gba-homebrew's "public-by-design (no Nintendo-derived
content)" row. The privacy flip fixed the *repo* surface, but the failure class —
IP-bearing bytes crossing to a public surface — re-arms every time the lane ships
anything outward: the pending owner playtest artifact, release assets, future public
docs. Nothing visible today encodes the boundary as doctrine; it lives only as the
memory of one urgent flip.

## Idea

One short lane PR that makes the boundary structural: (1) a **doctrine paragraph** in
the lane README — everything that leaves this repo (release artifact, playtest kit,
attachment, screenshot policy) is **patch-format only** (BPS/UPS/IPS against a named
clean base the owner supplies), never a ROM, never extracted assets; the repo itself
stays private indefinitely; (2) a **CI tripwire** — a check that fails on binary blobs
above a size threshold or known ROM extensions in the tree and in release-bound paths,
so the guard survives session turnover instead of relying on each agent remembering the
flip; (3) a one-line note that venture-class monetization is permanently out of scope
for this lane's outputs (derived IP), so no future venture sweep wastes a probe on it.

## Grounding

- Manifest pokemon-mod-lab row (URGENT private flip, API-verified ~15:12Z) and
  gba-homebrew row (public-by-design contrast) @
  [`53fb5ef`](https://raw.githubusercontent.com/menno420/superbot/53fb5ef9a294ab304b679dedd44ead55849295d5/docs/eap/fleet-manifest.md)
  (fetched 2026-07-10 ~20:35Z).
- Q-0260 rule 3 @ [`53fb5ef`](https://raw.githubusercontent.com/menno420/superbot/53fb5ef9a294ab304b679dedd44ead55849295d5/docs/owner/maintainer-question-router.md):
  "pokemon-mod-lab went private 2026-07-10" is already fleet-visible doctrine on the
  *read* side; this capture is its missing *egress* half.
- Verified live this session: raw-read of the lane 404s; only patch-shaped, clean
  artifacts could ever be fleet-shareable from here.

**Why now:** the post-EAP playtest (window closes 2026-07-14) is the first planned
egress event since the flip — the doctrine should exist before the first artifact
leaves, not be reconstructed after a second urgent fix.

## Probe report (v0, 2026-07-11)

*Probed 2026-07-11T08:05–08:25Z, single-pass (no panel: the SLICE is one doctrine
paragraph plus an advisory-first lint — reversible, no spend, no public surface; the
high-blast-radius event it governs — actual IP egress — is exactly what the doctrine
defers, so the panel trigger reads on the egress decision, not on encoding the ban).
DARK-lane recipe per README § Idea file grammar: the lane is the standing verified wall
(three-way check 07:32Z on the #131 probe — raw 404 ×2, `git ls-remote` auth wall, MCP
scoped to idea-engine — not re-paid same-day per docs/CAPABILITIES.md); every lane fact
is manager-relayed at fleet-manager HEAD `1afca50e171a33591f8481f0ac837b989c280425`
(ls-remote 08:08:14Z — the SAME pin the #131/#134 probes read, so their relayed evidence
carries over), the ruling layer re-read live at superbot HEAD `58040c6`, the kit layer at
substrate-kit HEAD `be72c09`. Verify-first found the capture's core premise
THREE-QUARTERS OVERTAKEN and one quarter INTACT. Already encoded, readable today: (1)
READ-side — superbot router Q-0260 rule 3 @ `58040c6` verbatim: "Private repos are the
carve-out to watch … pokemon-mod-lab went private 2026-07-10", DARK-by-privacy is fleet
doctrine; (2) VERIFICATION-side — fm playbook R22 (2026-07-10, "any lane whose rails
depend on repo visibility verifies ACTUAL visibility via the API at every session
start"), the exact-recipe CAN entry in fm `docs/capabilities.md`, and a dispatched lane
order (fm status @ `1afca50` line 698: "pokemon-mod-lab: ORDER 003 (visibility verify)
landed 12:56Z … unconsumed" at roster gen #1 — consumption at lane HEAD NOT MEASURED,
the lane is DARK); (3) the lane's own README carried a "no exceptions" PRIVATE rail
BEFORE the flip (night-review Q16: the breach was assertion-without-verification — 8 PR
bodies repeated "PRIVATE" while the repo was world-readable — not a missing rule), and
fm owner-queue item 3's WHERE now reads "(now PRIVATE — flipped by the owner 2026-07-10,
API-verified; the lane's rail says PRIVATE, never publish)". STILL MISSING — the intact
quarter: the EGRESS PROTOCOL. What may ever leave, and in what format (patch-only
BPS/UPS against a named clean base), is encoded nowhere deployed: its only statement is
fm `docs/proposals/instructions/game-lab.md` (IP RAILS block: Nintendo-derived bytes
"NEVER appear … in any release, gist, PR body, issue, artifact upload, or external
surface"; "Tier-1 CI lint that REDS any ROM/baserom/oversized-binary blob") — a
PROPOSED-not-deployed founding package for successor repos, header verbatim "PROPOSED,
not deployed" — plus this repo's own captures. And the machine guard is a verified debt:
night-review remediation item 1 prescribed "a substrate-gate step that fails when
`repo.private == false` in any repo declaring a PRIVATE rail … Builder: the
substrate-kit lane … ships in v1.8.0" — NOT shipped through v1.10.0 (kit CHANGELOG @
live HEAD `be72c09`: zero visibility-guard or IP-lint entries; v1.8.0/v1.9.0/v1.10.0
bands are claims/continuity/fixes). Egress-planning premise WEAKENED: the capture calls
the post-EAP playtest "the first planned egress event", but the playtest as planned is
IN-REPO — owner-queue item 3's WHERE is the private repo itself (PRs #4–#8 train), the
owner reads it directly, no bytes leave; no release/publish/distribution plan exists on
any fm surface at the pin, and the visibility saga (fm dispatch-log: flip → re-public
solely for the auto-merge toggle → counter → re-flip; "on this GitHub plan, private
repos cannot enable the auto-merge toggle at all") plus the game-lab draft's "the
emerald repo has NO release path by design" both point the same way: no egress surface
is even armed. The window-adjacency survives in weaker form: the 2026-07-14 sitting is
the event most likely to GENERATE the first share ask (a keep verdict → improvement
rounds → possible patch egress), and the SAME sitting publishes Lumen Drift publicly —
the moment of maximum cross-lane confusion about what may be published.*

**1. What is this really?**
The missing quarter of an already-three-quarters-encoded lesson. The private-flip's
read-side (Q-0260.3), verification-side (R22 + lane ORDER 003), and blanket rail
("PRIVATE, never publish" — the lane's own README, pre-dating the flip) all exist in
readable doctrine; what exists nowhere deployed is the egress PROTOCOL — the definition
of the ONE lawful outbound format (patch-only against a named clean base) plus its
machine guard. Honest reframe against the capture: this is doctrine-COMPLETION, not
doctrine-creation, and the patch-only clause is as much a RELAXATION valve as a
tightening — today's standing rule is a blanket never-publish, so the first legitimate
share request (post-playtest, community, fleet) currently has no lawful path and would
force exactly the kind of urgent ad-hoc ruling the flip was. Encoding the protocol
before that pressure arrives is the cheap half of the Q16 class.

**2. What is the possibility space?**
Four axes. **Where the doctrine lives:** lane README (binding where the bytes live, but
DARK — fleet-invisible) vs an fm-visible line (readable by every relay consumer, but fm
never writes lane files) vs the kit (generic, but the night review already assigned the
generic guard there and it hasn't shipped) — lane README paragraph + one fm-relay line
dominates; the kit inherits later. **Tripwire scope:** tree-wide blob/ROM lint (the
game-lab draft's shape for a BORN-CLEAN repo — WRONG here: this tree carries the vendored
decomp, upstream multiboot binaries and ~1.9MB screenshots by design per night-review
Q16, all rail-fine while private, so a tree lint is born-red on day 0) vs egress-scoped
(release-bound paths, artifact uploads, plus a `repo.private == true` assert per R22) —
egress-scoped wins structurally. **Guard owner:** lane-local CI step now (the lane owns
`substrate-gate` at kit v1.6.0 and `rom-builds.yml` — both real, fm-relayed homes) vs
waiting for the kit's generic Q16 guard (verified unshipped through v1.10.0) — lane
lands local now and becomes the kit's reference implementation, the enabler-anchors
pattern this repo already lived. **Venture note:** one line in the lane README plus this
section's index badge (the idea-engine half of it lands with this very probe — the index
row below says venture is permanently out of scope, so no future venture sweep prices
this lane).

**3. What is the most advanced capability reachable by the simplest implementation?**
One lane PR, three small pieces, two standing duties retired. (a) A README egress
paragraph — patch-format only (BPS/UPS against a named clean base the owner supplies),
repo private indefinitely, venture monetization permanently out of scope, citing
Q-0262.7 (NOT the fm-side "Q-0266" label — the #134 mislabel finding) and the 2026-07-10
flip as provenance — makes the boundary survive session turnover in the exact place
sessions boot. (b) A ~10-line CI step asserting `repo.private == true` converts ORDER
003's per-session ritual duty (R22) into structure: every PR re-proves the rail instead
of every session re-remembering it, and the assertion-without-verification class that
Q16 named becomes machine-impossible on this repo. (c) An egress-scoped ROM/blob lint on
release-bound paths prices near zero today (no release path exists by design) and arms
automatically the day one appears. The clean-base anchors are already committed: the
proof-bundle sha1 chain (`eec6d6af` → … → `805aeaee`, manager-verified fm PR #61)
gives every patch a named base for free.

**4. What breaks it?**
- **The tree-lint trap.** Copying the game-lab draft's tree-wide blob lint reds this
  repo on day 0 (vendored decomp is in-tree by design). Broken by construction unless
  the lint is egress-scoped — this probe's sharpest scope correction.
- **The DARK wall.** The lane may ALREADY carry a doctrine paragraph or lint invisible
  from here (a lane session read the companion capture's Q16 material independently —
  NOT MEASURED). First lane-side step is verify-own-tree; the fm-relay line is worth
  shipping in either branch.
- **Token visibility semantics.** Whether the Actions `GITHUB_TOKEN` on this GitHub plan
  returns `.private` for its own repo is NOT MEASURED from here (it should — same-repo
  read is standard — but the lane proves it in one run; advisory-first per the
  born-red-check doctrine if uncertain).
- **Doctrine rot.** A rule guarding a nonexistent event class can drift out of reading
  order; mitigated by being ONE paragraph in the README the lane's binding-docs ritual
  already opens, plus the CI assert that fires on every PR regardless.
- **Q-id mislabel propagation.** fm surfaces label the pick "Q-0266" (the router's
  Q-0266 is volume-first doctrine); a lane session grepping the router by the fm label
  lands on the wrong ruling — the doctrine text must cite Q-0262.7 (verified verbatim @
  `58040c6`: "Pokemon concept pick = QoL+ … takes effect when the games program boots
  post-core").

**5. What does it unlock?**
A lawful first-egress path the moment the owner's post-sitting reactions generate a
share ask — patch egress at zero marginal ruling cost instead of a second urgent flip.
Permanent venture-sweep savings (this section's index now says out-of-scope; the lane
README says it where lane sessions read). The fleet's generic Q16 guard gets its live
reference implementation — the substrate-kit debt (night-review item 1, verified
unshipped) inherits a proven egress-scoped shape instead of the born-red tree-wide one.
And section-locally: this closes pokemon-mod-lab's last open head — the SIXTH fully
probed-or-parked section.

**6. What does it depend on?**
- The lane being awake and able to land one PR — verified at the pin: roster gen #5 row
  FRESH, hourly wake `trig_01BTJjkMVMKtWPjuYe7643Hi` `30 * * * *`, kit v1.6.0 · check
  green, repo evidence `297f67b`.
- The repo actually being private NOW — verified from both sides: the raw 404 wall from
  here (the #131 three-way check) and fm's API-verified record ("private: true", R22
  end-state in the dispatch-log @ `1afca50`).
- Named clean bases for the patch format — already committed as the proof-bundle sha1
  chain, manager-verified (fm PR #61 `5244a1c`, review-queue pokemon#8 row).
- NO cross-lane build dependency. Co-consumers of the routing only: the playtest-kit
  park rides the same 2026-07-14 sitting bundle, and substrate-kit is the later
  generalization target, not a blocker.

**7. Which lane should build it?**
`menno420/pokemon-mod-lab` — it owns the README, the CI, and the tree the doctrine
binds; this repo cannot write lane files (Q-0260) and cannot read this one.
`fleet-manager` owns the routing (an ORDER alongside the playtest-kit item — one bundle,
same window) and the one-line fleet-visible relay note. `substrate-kit` owns the GENERIC
Q16 guard debt the night review already assigned it — verified unshipped through
v1.10.0, an evidence line for the manager's existing kit-lane bundle, not new scope.
NOT sim-lab: a doctrine paragraph and a lint are proven by their own red/green — no
reproducible-evidence question exists, so no outbox proposal rides this probe.

**8. What is the smallest shippable slice?**
One lane PR: (1) verify-own-tree first (doctrine text or lint may already exist —
DARK from every non-lane seat); (2) the README egress-protocol paragraph — patch-only
BPS/UPS against a named clean base, private indefinitely, venture permanently out of
scope, citing Q-0262.7 and the 2026-07-10 flip; (3) the `repo.private == true` CI
assert + the egress-scoped ROM/blob lint (advisory-first, promoted after one clean
cycle; proven red on a fixture, then the fixture removed). fm side: one ORDER routing
it with the 2026-07-14 sitting bundle. Done-when: the paragraph is at lane HEAD, the
guard has fired red-on-fixture once, and ORDER 003's per-session visibility duty is
structural.

**Recommendation: park** — build-direct: a one-PR lane doctrine slice (README
egress-protocol paragraph + repo.private CI assert + egress-scoped tripwire — never
tree-wide, the vendored decomp is in-tree by design) that completes the
three-quarters-encoded private-flip lesson with its missing egress quarter; nothing
sim-shaped, and the manager should route it in the SAME bundle as the playtest-kit park
(2026-07-14 owner sitting — the event most likely to generate the first share ask).
