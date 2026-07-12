# Merge holds announced in a file at HEAD — link index

> **State:** parked(routed — kit/manager layer, one fleet-wide shape per the canonical doc's own routing half: a substrate-kit slice adding (a) a `HOLD-<scope>.md` grammar paragraph + `lift-when:` line to the planted `control/claims/README.md`, (b) a hold-aware carve-out in `check_claims` (a >72h HOLD must NOT get the work-claim "delete it" prune-on-sight advice — today it would, measured against `bootstrap.py` `_work_claim_findings`), (c) one before-merging ritual line in the planted `control/README.md`, and (d) the enforcement half that makes it more than a sticky note: a hold-aware step in the kit-owned gate workflow so armed auto-merge is machine-blocked, since NO current merge automation reads claims/ (probe Q4's enumeration) — probed 2026-07-12: incident transport-verified in websites main history (#143 `ebef8bd`, #146 `31cfd9f` in-hold; #141 owner-merged later as `0545906`), idea NOT self-served at websites HEAD `8f97654` (= harvest pin, lane PARKED — self-serve will never come, routing must go via the manager sweep), and a bare `HOLD-*.md` is ALREADY legal in the kit's claim scan today (grammar-compatible, stale-nag free) so the convention halves are cheap; nothing sim-shaped — deterministic file-at-HEAD mechanics the first live hold settles; manager-sweep flag rides this file + the session card, dispatch boundary)
> **Class:** process · **Target:** `menno420/websites`
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8f9765483a7df57ce426e7d11d200f10b5495ed7/docs/ideas/merge-hold-at-head-2026-07-11.md@8f97654 · fetched 2026-07-12T01:47Z

**Canonical idea (stays in websites — indexed by link, never copied):**
[`menno420/websites → docs/ideas/merge-hold-at-head-2026-07-11.md`](https://github.com/menno420/websites/blob/8f9765483a7df57ce426e7d11d200f10b5495ed7/docs/ideas/merge-hold-at-head-2026-07-11.md)
— harvested 2026-07-12 by the websites fourth re-harvest slice, pinned @ websites `8f97654`
([raw](https://raw.githubusercontent.com/menno420/websites/8f9765483a7df57ce426e7d11d200f10b5495ed7/docs/ideas/merge-hold-at-head-2026-07-11.md)).

Announce a repo-wide merge hold as a file **at origin/main HEAD** — one
`control/claims/HOLD-<scope>.md` per hold (created when the hold starts, deleted
when it lifts; weaker fallback: a `hold:` heartbeat line) — so every session's
mandatory session-start pull sees the hold mechanically, instead of coordinating
holds by session messages, which only reach sessions alive at send time. The
canonical doc grounds it in a MEASURED failure, not vibes: the 2026-07-11 hold
protecting websites PR #141 failed twice — routine-fired 4-hourly wakes boot with
zero chat context, and websites #143/#146 were merged mid-hold by sessions that
never saw it (websites PR #148's body records #141 knocked to
`mergeable_state: behind` by exactly those merges). Same insight that makes
`control/claims/` work for work-claims, and the claim checker's existing
parse/stale machinery could nag on a stale HOLD file for free. Routing half named
in the canonical doc: the convention belongs to the kit/manager layer — one
fleet-wide shape, not per-repo forks (born in the lane's archive-prep capture,
websites #154; source retro: websites `docs/retro/archive-ready-2026-07-11.md`
§3). Dedup at capture: zero prior hold-coordination capture anywhere in this
repo's `ideas/` tree (nearest misses are the kit's `session-card-hold` gate
mechanics and superbot-idle's sim-hold queue states — different objects).

## Probe report (v0, 2026-07-12)

> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8f9765483a7df57ce426e7d11d200f10b5495ed7/docs/ideas/merge-hold-at-head-2026-07-11.md@8f97654 · fetched 2026-07-12T02:24Z
> *(pin annotation: websites live HEAD verified = the harvest pin
> `8f9765483a7df57ce426e7d11d200f10b5495ed7` by `git ls-remote` + a read-only
> blobless clone this session — the lane is PARKED and has not moved since its
> own #156; harvest citations ARE HEAD citations, zero drift. Canonical doc and
> its source retro `docs/retro/archive-ready-2026-07-11.md` both raw-fetched at
> the pin.)*

> Single-pass battery (panel not escalated: doc-convention head, reversible,
> no security/data/spend/public blast radius — README § probe battery).
> Verify-first, live: (a) **not self-served** — `control/claims/` at websites
> HEAD holds `README.md` ONLY (tree `4177361`), websites `control/README.md`
> greps zero for any hold ritual, and `git log ebef8bd..HEAD -- control/README.md
> docs/project/` is EMPTY — no hold convention shipped since the incident;
> (b) **the measured incident is transport-real**: websites main history carries
> #143 (`ebef8bd`) and #146 (`31cfd9f`) — the two mid-hold merges — plus #148
> (`7d1ff88`), the catch-up heartbeat #150 (`9775697`, subject: "hold window
> resolved; held queue landed"), and #141 itself finally landed as `0545906`
> (the owner squash-merge the hold was protecting); (c) the retro that birthed
> the idea (`docs/retro/archive-ready-2026-07-11.md` §3 @ `8f97654`) records the
> failure verbatim: "routine-fired wakes boot with no chat context: #143 and
> #146 were merged mid-hold by sessions that never saw the hold". One citation
> honestly SHORT of verification: PR #148's BODY (the `mergeable_state: behind`
> quote) is unreachable from this seat — GitHub MCP is scoped to idea-engine
> (access-denied captured this session) and `api.github.com` is walled
> (`docs/CAPABILITIES.md:53`) — **reported-not-verified**, corroborated by the
> retro's quote of it and by the verified merge sequence around it.

**1. What is this really?** A negative work-claim — "nobody land anything on
`<scope>` until this lifts" — carried on the ONE channel a zero-context wake
provably reads: the tree at origin/main HEAD. Session-message holds reach only
sessions alive at send time; the measured failure (twice in one afternoon) is
exactly the sessions that did not exist yet. Who it's for: every fleet repo
running routine-fired wakes — which since Q-0265 continuous-chaining is this
repo too, with the same 4-hourly-wake shape that produced the websites
incident. One honest scope note the canonical doc's framing invites but the
retro corrects: the hold protects a bounded WINDOW; for the indefinite
owner-click wait that followed (#141 stayed owner-merge-only because it adds
workflow files — retro §2(c)), the lane's standing remedy was the
drift-watchdog (update-branch + re-green loop, retro §3), and post-hold merges
(#147/#148/#150/#145) went on knocking #141 behind BY DESIGN. The HOLD file
complements the watchdog; it does not replace it.

**2. What is the possibility space?** (i) Do nothing — next hold gets
coordinated by messages again and fails the same way at the next zero-context
wake. (ii) The canonical doc's weak fallback: a `hold:` heartbeat line —
rejected as primary by the incident's own repo shape: `control/status.md` is
coordinator-only and overwritten every wake (staleness + one-writer
contention), and websites' phase line "carried it late in the day" only after
the damage. (iii) The captured shape: `control/claims/HOLD-<scope>.md`, same
one-file-per-claim grammar (backticked scope token + ISO date + `lift-when:`),
created at hold start, deleted at lift. Measured-cheap to make legal: the kit
claim scanner already reads EVERY `control/claims/*.md` except README
(`bootstrap.py` `_work_claim_findings`), so a bullet-conformant HOLD file
parses TODAY and inherits `claims-stale` nagging for free — the canonical
doc's "parse/stale machinery for free" claim verified TRUE with one wrinkle
(Q4.iv). (iv) (iii) plus the enforcement half: a hold-aware step in the
kit-owned gate workflow (`substrate-gate.yml` shape) that reds a PR when a
`HOLD-*.md` at the merge-base names its scope — turning the hold from
agent-etiquette into a machine-blocked state, because a red required check is
the one thing GitHub auto-merge waits on. (v) GitHub-native levers instead —
priced in Q7; all owner/admin-gated or wrong-shaped. Value peak: (iii)+(iv)
as ONE kit slice; (iii) alone is real but leaves the auto-merge hole open.

**3. What is the most advanced capability reachable by the simplest
implementation?** Fleet-wide hold coverage from one kit PR: a grammar
paragraph in the planted `control/claims/README.md`, one before-merging ritual
line in the planted `control/README.md` ("`ls control/claims/` — a `HOLD-*`
naming your target's surface means stand down"), a hold-aware carve-out in
`check_claims`, and a ~10-line gate-workflow step. Every kit adopter inherits
all four at its next `bootstrap upgrade` — the same one-template-many-lanes
economics the open-pr-awareness probe priced for the wake sweep. The
convention needs zero new machinery to be VISIBLE (session-start pull + `ls`),
and the gate step makes it BINDING against the exact automation that never
reads etiquette (Q4).

**4. What breaks it?** The coordinator's sticky-note test, answered surface by
surface — which merge paths would honor a HOLD file today, unbuilt:
(i) **GitHub auto-merge armed at PR creation** (this repo's own landing
convention arms it where checks can go pending): fires on green with NO agent
in the loop, reads no files — a hold landing at main HEAD after a sibling PR's
checks are already green does NOT re-trigger checks, so the armed PR merges
anyway. Convention-only loses here; only the gate step (Q2.iv) plus a
hold-start sweep of already-armed open PRs (disarm, or update-branch to force
a fresh gate run against the now-held base) closes it. (ii) **REST
merge-on-green loops** (PRIMARY on born-red here): agent-driven — honors the
hold exactly if the ritual line exists and the agent re-lists claims before
the merge call; zero-context wakes get this from the session-start pull, which
is the half the idea actually fixes. (iii) **The kit gate workflow**: required
check, blocks auto-merge when red — the enforcement hook EXISTS but reads
cards + inbox purity today, never `claims/`. (iv) **The kit claim checker**:
a >72h hold triggers `claims-stale` whose finding text prescribes
prune-on-sight ("likely an orphan; delete it") — for a legitimate long hold
that advice is actively inverted; the kit slice must carve HOLD files out of
the work-claim wording or a compliant agent DELETES the hold. (v) **Scope
grammar ambiguity**: "names your target's surfaces" needs a deterministic
match rule (repo-wide `HOLD-main.md` vs path-scoped) or agents will
judgment-call their way through it — v1 should ship repo-wide holds only.
(vi) **Owner-side merges**: the owner clicking squash-merge reads no claims
dir either; a hold that must bind the owner is a chat message to the owner,
out of scope by design.

**5. What does it unlock?** The next protect-a-window hold costs one fast-lane
claim PR instead of a failed message relay plus an afternoon of drift-watchdog
repair; zero-context wakes become hold-safe BY the mechanism that makes them
zero-context-safe for sections and orders already (the bus, not the chat); and
the claims directory completes its grammar family — positive claims (work),
negative claims (holds) — one convention, one scanner, every adopter. For this
repo specifically: continuous-chaining (Q-0265) plus armed auto-merge is
exactly the websites failure shape; the fleet's ideation hub is currently as
hold-blind as websites was on 2026-07-11.

**6. What does it depend on?** Nothing unshipped for the convention halves:
the claims dir + scanner exist at every kit adopter (v1.8.0+), and a
grammar-conformant `HOLD-*.md` parses today (verified against
`_work_claim_findings` this session). The enforcement half depends on the
kit-owned gate workflow (substrate-kit's surface) and on the hold-start sweep
having PR tooling to see armed siblings — the same per-seat variance the
open-pr-awareness probe named decisive (degrade honestly: file + ritual
always; gate step wherever the kit gate runs; armed-PR sweep where the seat
can). Cheapest confirm/kill evidence, priced: this probe's confirm cost was
two raw fetches + one `ls-remote` + one blobless clone (decisive facts: not
self-served, lane parked, incident transport-real, HOLD grammar-legal today).
The build-time kill-test is deterministic and cheap: land a `HOLD-main.md` on
a scratch adopter, open a sibling PR with auto-merge armed — un-gated it
merges (the failure, reproduced); with the gate step it sits red until the
hold file is deleted, then greens and lands. One CI run settles it.

**7. Which lane should build it — and what does it displace or duplicate?**
**substrate-kit, via the manager sweep** — the canonical doc's own routing
half names the kit/manager layer ("one fleet-wide shape, not per-repo forks"),
and the probe confirms the routing is FORCED, not just preferred: the websites
lane is PARKED at `8f97654`, so the self-serve path that executed
open-pr-awareness (websites#90) will never fire here, and idea-engine writes
only itself (Q-0260). This slice cannot write `control/` (dispatch boundary) —
the manager-sweep flag rides this file + the session card for the
coordinator's next heartbeat. Displaces/duplicates, named: **this repo's
`control/claims/` grammar** (`control/claims/README.md`) — the direct
substrate, NOT a duplicate: HOLD is a new claim CLASS (negative claim) reusing
the measured 0%-conflict one-file-per-claim layout; the grammar gap is
`lift-when:` + the stale-wording carve-out (Q4.iv). **The kit's
`session-card-hold` / born-red HOLD** (`bootstrap.py:1759`
`BORN_RED_HOLD_MESSAGE`, gate workflow) — nearest miss, different object: a
per-PR hold on the PR's OWN card state, not a repo-wide cross-PR hold; no
overlap in mechanism, and its gate step is the PATTERN the enforcement half
copies. **`open-pr-awareness-at-wake`** (this section, parked; lane
self-served as websites#90) — the discovery dual: it surfaces others' IN-FLIGHT
work at wake, this surfaces a declared CONSTRAINT at wake; complementary, and
its still-unbuilt substrate-kit fleet-generic half (planted `control/README.md`
wake-sweep paragraph) is the SAME kit surface — one kit slice should carry
both ritual lines (concrete bundling finding for the manager).
**`ideas/fleet/open-work-preflight-sweep-2026-07-10.md`** — same wake-sweep
family, branches/PRs not holds. **`ideas/fleet/
coordinator-archive-handoff-ceremony-2026-07-11.md`** (captured; the fifth
mint's rejected kit-lane bundle candidate) — overlapping ROUTING TARGET
(kit-blessed coordination ceremony docs), zero mechanism overlap; a hold's
lifecycle (start → sweep armed PRs → lift → delete) is ceremony-shaped and can
ride the same kit doc bundle. **`ideas/fleet/gate-ritual-convergence`** —
supplies the make-the-ritual-merge-blocking doctrine Q2.iv applies.
**GitHub-native mechanisms**, and why they were not the incidents' answer:
branch-protection lock is an owner/admin mutation (the holding sessions were
agents, which the platform demonstrably fences — retro §2(c) records agents
platform-denied even from MERGING workflow-file PRs) and is blunt: locking
main also stops the control fast lane (claims/heartbeats) AND the hold file's
own landing; a merge queue serializes merges but holds nothing; draft-flipping
sibling PRs needs PR tooling many seats lack and cannot cover PRs born
mid-hold. All reported-context on the incident side (the hold itself lived in
chat, unreadable from any seat); the platform-fence datapoint is the retro's,
cited above. Superbot-idle's sim-hold queue states — different object
(capture's dedup, re-confirmed: sim scheduling, not merge coordination). No
duplicate idea file anywhere in `ideas/` (rg sweep over
hold/claim/lock/merge-queue/auto-merge/branch-protection this session).

**8. What is the smallest shippable slice?** One substrate-kit PR, four
touches: (1) planted `control/claims/README.md` gains a "Hold claims" section
— `HOLD-<scope>.md`, the existing bullet grammar plus a `lift-when:` line,
repo-wide scope only for v1, delete-to-lift; (2) `check_claims` gains the
HOLD carve-out — hold-aware stale wording (nag "is this hold still live?
confirm or lift", never "delete it") — the ~10-line diff to
`_work_claim_findings` plus its test; (3) planted `control/README.md` gains
the one before-merging ritual line (bundled with the open-pr-awareness wake
paragraph if the manager takes the bundling finding); (4) the kit gate gains
the hold step: red with a HOLD-by-design banner when `control/claims/HOLD-*.md`
exists at the merge-base, exempting the PR the hold file itself names.
Hold-START ritual documents the armed-PR sweep (Q4.i) with the honest per-seat
degradation. Cost: one kit PR, ~50–100 lines including tests, zero runtime
code, adopters inherit at next upgrade. What must NOT ship: hold state on the
heartbeat as primary (one-writer + overwrite staleness), path-scoped hold
matching in v1 (Q4.v), or any hand-edited hold index (the 0%-conflict rule).

**Recommendation: park** — routed (kit/manager layer: the Q8 four-touch
substrate-kit slice; manager-sweep flag rides this file + the session card
since this slice cannot write `control/`). Rationale: the twice-measured
failure is transport-verified and the fix is real, but nothing here is
sim-shaped — a HOLD file either is at HEAD and honored by the ritual/gate or
it is not, the Q6 red/green kill-test settles enforcement in one CI run, and
the build surface belongs to a lane this repo does not write while the
canonical lane (websites) is PARKED and cannot self-serve.
