# Host-seam conformance stub — an executable stand-in for the in-flight plugin contract

> **State:** parked(build-direct — sequenced: the seam's SHAPE is superbot-next's to define (its inbox ORDER 002 item 4 — "docs: the plugin contract … which kernel seams a plugin gets" — live-verified `status: new` @ `c3f7a02`), so a stub the games lane invents today is a second source of truth guessing the host's shape; the buildable slice is a schema-MIRROR host-seam stub + package conformance test in superbot-games AFTER the host's contract doc (or its manifest types) lands, ordered behind the PR #39-routed encounter-contract slice on the same claim-first `games/shared/**` path, with the fake reward seam deferring to that contract's payload-INTENTS rule — no sim question; manager sequences)
> **Class:** product · **Target:** `menno420/superbot-games` (cross-lane dependency:
> `menno420/superbot-next` plugin/manifest contract, its inbox ORDER 002)

## Problem

The lane README @ `adb5f9b` is explicit: games ship as plugin packages consumed by
`superbot-next` via a manifest/plugin contract that "is in flight there (superbot-next's
inbox ORDER 002); until it lands, all work here stays plugin-side … with the host-facing
seams left open." Today those open seams exist only as prose in two founding plans. Two
autonomous Projects building against prose seams for weeks means the seams drift apart,
and the eventual cutover to the real contract becomes an archaeology job instead of a
diff — while superbot-next itself is still mid-mission (manifest: gen-1 band 5, ORDERs
008/009 pending), so the wait is not short.

## Idea

A tiny **stub host** under `games/shared/` (claim-first path per `docs/lanes.md`): one
module that fake-implements each open host-facing seam (registration/manifest handshake,
command surface mount, persistence handle, audited reward routing) plus a conformance
test both lanes run — "my package loads, mounts, and round-trips against the stub."
The stub is the seam's single executable definition; when superbot-next's real contract
lands, cutover = point the conformance test at the real contract and fix exactly the
failures it prints. Interface changes announce in both lane status files per lanes.md.

## Grounding

- `https://raw.githubusercontent.com/menno420/superbot-games/main/README.md` @ `adb5f9b`
  (contract-in-flight paragraph, quoted above) and `docs/lanes.md` @ `adb5f9b`
  (`games/shared/**` claim-first; both-status-files interface rule).
- Fleet manifest superbot-next row (`https://raw.githubusercontent.com/menno420/superbot/main/docs/eap/fleet-manifest.md`,
  fetched 2026-07-10): mid-mission, self-arm ORDER unexecuted — the contract's ETA is
  genuinely uncertain.

**Why now:** both gen-1 lanes just closed green — gen-2's first plugin work starts
against these seams, and a stub is cheapest before either lane has code shaped around a
private guess.

## Probe report (v0, 2026-07-10)

> **Grounding:** https://github.com/menno420/superbot-games@b134961ef5dddf8a1cc15d97c11704629d81989a · fetched 2026-07-10T23:52Z (manifest row: behind)
> **Grounding:** https://github.com/menno420/superbot-next@c3f7a02e8607d6b1d9edfcd99f92039f8d09592a · fetched 2026-07-10T23:52Z
> **Sequence:** after superbot-next inbox ORDER 002 item 4 (the host's contract doc — live-verified `status: new`, acked-not-done, at the pin above) and behind the PR #39-routed encounter-contract slice — both slices live under claim-first `games/shared/**` and ride the same externally-fired gen-2 boot, so they share one claim and must be ordered: encounter contract doc first, host-seam stub second

*Probed against live state, not the capture's snapshot: superbot-games @ HEAD `b134961`
(ls-remote 23:52Z — the capture's `adb5f9b` pin is one commit behind; the tree has not
moved since PR #39's read), superbot-next @ HEAD `c3f7a02` (ls-remote 23:52Z;
`control/inbox.md` ORDER 002 raw-read at that pin: `status: new`, and the lane's
`control/status.md` shows 002 acked, NOT in `done=` — the plugin contract is genuinely
still unbuilt, so the capture's core premise holds). One staleness flag the capture
needs: "those open seams exist only as prose" is no longer fully true — the encounter
seam has executable shape (`games/shared/encounter/{interface,reference}.py` @
`b134961`, PR #39's load-bearing find); the four HOST-facing seams this capture names
(registration/manifest handshake, command surface mount, persistence handle, audited
reward routing) are indeed still prose. Twin-check: this is NOT PR #39's remainder —
that probe's Q8 fences "host wiring stays in their own slices" and its Q4 rules the
cross-repo plane binds shape, not code; this idea is exactly that fenced-off plane.*

**1. What is this really?**
A drift-prevention instrument for the host/plugin seam —
but split it honestly and it is two different things wearing one name. Half (a): a
games-lane discipline — shape both lanes' plugin packages so "loads, mounts,
round-trips" is CI-provable rather than asserted; that is genuinely superbot-games
work. Half (b): an executable DEFINITION of the host seam itself — and that definition
is chartered elsewhere: superbot-next's ORDER 002 item 4 is verbatim "docs: the plugin
contract (what a plugin may declare, which kernel seams it gets — economy, game-XP,
EffectiveStats, panels — and what stays host-owned)." A stub written by the games lane
today does not stand in for that contract; it PREEMPTS it with a guess. What this idea
really is: half (a) built against half (b)'s output — not before it.

**2. What is the possibility space?**
Three axes. **Stub fidelity:** no-op fakes that
only prove import/mount → round-trip fakes with recorded interactions a conformance
test asserts → a schema MIRROR whose seam signatures are copied-with-pins from
superbot-next's published contract doc/manifest types (the PR #39 Q4 cross-repo rule:
bind shape, not code) → vendoring the real `sb.spec`/manifest types once ORDER 002
item 1 ships an installable path. **Ownership:** games invents the shapes (cheapest
now, structurally divergent later) → games mirrors host-published shapes by schema
(cutover = re-pin + rerun) → the host ships a plugin-SDK stub both lanes consume (the
converged end-state; ORDER 002 items 1–3 are most of it). **Seam coverage:** handshake
only (an exported `SubsystemManifest` the stub loads and hash-pins the way ORDER 002
item 2 says the host will) → +command mount → +persistence handle → +reward routing —
where this capture must DEFER rather than define: PR #39's probe already pinned
audited reward routing as payload INTENTS inside the encounter contract, with the
host's audited workflow op as sole writer (Q-0186's condition verbatim); a stub reward
seam that fake-IMPLEMENTS routing would be a second definition of an already-pinned
rule.

**3. What is the most advanced capability reachable by the simplest implementation?**
One mirrored stub module + one parameterized conformance test, built AFTER the host's
contract doc exists: `games/shared/` gains a stub whose seam signatures cite
superbot-next's doc @ its SHA (schema-mirror, never invention), and a test
parameterized over plugin packages asserts loads/mounts/round-trips against it. That
buys the capture's whole strategic point — cutover to the real host becomes "re-point
the conformance test, fix exactly the printed failures" — because the failures are
then guaranteed shape-compatible: the stub and the real contract share an upstream
definition. Built BEFORE that doc, the same code buys almost nothing durable: the
simplest honest pre-doc slice shrinks to the handshake seam alone (ORDER 002's own
wording already pins "an installed plugin exports its SubsystemManifest; host compiles
+ hash-pins it"), and even that mirrors an inbox order's prose, not a contract.

**4. What breaks it?**
**Second source of truth — the big one.** A stub invented
unilaterally by the games lane is the seam's "single executable definition" only
inside this repo's fiction; superbot-next's ORDER 002 keeps its own charter regardless.
When the real contract lands, the diff is plausibly STRUCTURAL, not cosmetic — item 1
is a packaging/import strategy (installable `sb` package vs git-dependency), item 2
has the host compile + hash-pin the manifest (a dynamic fake cannot honestly stand in
for a hash-pinned compile), item 4 decides which kernel seams a plugin gets AT ALL —
and the capture's cutover promise ("fix exactly the failures it prints") silently
assumes shape-compatible failures. Divergence turns the conformance suite into a
certificate of conformance to a guess. **Cross-repo import wall:** the superbot hub
cannot import `games/shared/` (PR #39 Q4) and neither can superbot-next — the stub
binds games-side code only; it never constrains the host, which is the party whose
shape is uncertain. **Reward-routing collision:** defined here AND in the encounter
contract, the two definitions drift inside one repo — this stub must consume PR #39's
payload-INTENTS rule, not restate it. **Clockless consumers + shared claim path:**
superbot-games is relaunch-gated (its own self-arm ORDER unexecuted; manifest row
still `behind` at `adb5f9b`), so the stub sits unread until an externally-fired gen-2
boot — the same boot PR #39's contract slice rides, on the same claim-first
`games/shared/**` path: unsequenced, the two slices are a live claim collision.

**5. What does it unlock?**
Sequenced right, the gen-2 plugin wave starts against
executable seams instead of prose: both lanes' packages become CI-provable plugin
citizens before the host ever loads them; the cutover to superbot-next's real contract
becomes a diff instead of archaeology (the capture's own framing — true once the stub
mirrors rather than guesses); superbot-next gets a free live fixture — ORDER 002 item
3's "hello-world plugin from a separate repo" could simply BE a games package that
already passes the conformance test, collapsing the host's done-when demo and the
lanes' readiness proof into one artifact; and the lanes.md both-status-files
announcement rule gets an executable subject for the host seam, as PR #39's slice
gives it one for the encounter seam.

**6. What does it depend on?**
**The hard dependency is unbuilt and owned elsewhere:**
superbot-next ORDER 002 — item 4's contract doc (and item 1's manifest types) is the
upstream this stub must mirror; live-verified `status: new` / acked-not-done @
`c3f7a02`, and the lane is mid band-6 with ORDER 002 at P2 ("do NOT let it derail
live-testing"), so the ETA is genuinely uncertain — the capture is right about the
wait, wrong about the remedy. Shipped and verified: `games/shared/encounter/` @
`b134961` (the one executable seam; its contract-doc slice is PR #39's routed
remainder), `docs/lanes.md`'s claim-first + both-status-files rules. Decisions:
Q-0186's reward condition (audited seams, sole writer) as pinned into the encounter
contract by PR #39's probe. Process: the externally-fired gen-2 boot (lane ORDER 001
P0 CI-collection is boot-gating; self-arm ORDER 002 unexecuted) — the delivery vehicle
for ANY `games/shared/**` slice.

**7. Which lane should build it?**
Split by the two halves of Q1. The stub CODE is
superbot-games' (it lives under `games/shared/**`, claim-first, both-status-files
announcement — same claim discipline as PR #39's slice, so the manager should route
them as ONE ordered bundle on the same boot: encounter contract doc first, host-seam
stub second). The seam SHAPE is superbot-next's — ORDER 002 item 4 is exactly this
contract; the correct cross-lane move is a manager nudge that raises that item's
priority (or extracts a minimal manifest-types/contract-doc pre-slice from it), not a
games-side preemption. Not this repo (writes no lane code); not sim-lab — the open
questions are ownership and sequencing, which routing settles, not simulation.

**8. What is the smallest shippable slice?**
Two-step, in dependency order. **Step 0
(superbot-next, unblocks everything):** land ORDER 002 item 4's contract doc — even a
minimal committed page pinning the manifest export shape and the four seam signatures
is sufficient upstream. **Step 1 (superbot-games, one lane PR on the gen-2 boot):**
`games/shared/host_stub/` mirroring the doc's seam signatures @ its SHA (schema-mirror
rule, PR #39 Q4) + a conformance test parameterized over plugin packages ("loads,
mounts, round-trips"), green on one existing package day one; the reward seam routes
payload INTENTS per the encounter contract's rule (consume, don't redefine); interface
announcement in both lane status files per lanes.md. Explicitly NOT in the slice: any
games-invented seam shape (the Q4 failure mode), and nothing before step 0 beyond at
most a prose seam-inventory page naming the four seams and the pin-and-mirror rule.

**Recommendation: park** — build-direct but sequenced: no reproducible-evidence
question exists for sim-lab (the uncertainty is contract ownership and timing, settled
by routing, not simulation) — the seam's shape belongs to superbot-next's ORDER 002
item 4 (live-verified still unbuilt @ `c3f7a02`), so the manager should nudge that
contract doc FIRST, then route the stub to superbot-games as a schema-mirror +
conformance slice bundled behind the PR #39 encounter-contract slice on the same
claim-first `games/shared/**` path and gen-2 boot, its reward seam deferring to that
contract's payload-INTENTS rule.
