# Carried-watch verdict-inheritance guard — a watch must not outlive the verdict that justified it

> **State:** parked(routed — kit/manager layer: fifth-touch rider on the merge-hold substrate-kit slice — carried-watch grammar (`WATCH: <claim> · verified <ISO> · per <pointer>`) + report-only `--watch-freshness` advisory; /fleet badge = manager rider — probed 2026-07-12: the precondition is UNIVERSAL in this repo's own heartbeat (14/14 inherited watch/flag entries in `control/status.md` @ main `6d40f6f` carry no `verified <ISO>` stamp; the fc0bab6 ten-flag carry-by-pointer is now seven overwrites deep; the two "from #157" watches crossed the a9b41f6→fc0bab6 coordinator generation handoff), the mechanism is measured at the source (a wrong "never delivered" cron verdict rode FIVE heartbeat overwrites at websites — backlog.md@`e14bb15` line 158, re-pinned byte-exact at probe time), the kill test did NOT trigger (live kit HEAD `8a544a6`: planted-contract template blob `71c9ce4` carries zero watch grammar, `docs/decisions.md` blob `f9b5d52` has no watch/stamp decision — nearest is D-0009's registry-layer "staleness reads as dark"), and nothing is sim-shaped — a deterministic lint over one file; manager-sweep flag (the fifth-touch bundling question) rides this file + the session card, dispatch boundary)
> **Class:** process · **Target:** `menno420/substrate-kit` (heartbeat-grammar + status-checker
> half is kit-planted territory every adopter inherits; the fleet-surface badge half is
> manager `/fleet` territory)
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8f9765483a7df57ce426e7d11d200f10b5495ed7/docs/ideas/backlog.md@e14bb15 · fetched 2026-07-12T02:57Z
> *(pin annotation: source bullet at line 158 of the pinned backlog — the fetch re-verified
> to blob `e14bb15408b1f45de14eae72efe990024f0e548c` by `git hash-object` this slice, the
> same pin-verify the PR #244 groom ran. The bullet's own canonical source is the websites
> chain-closeout card 💡 (`.sessions/2026-07-11-chain-closeout.md`, websites repo). Captured
> here because the PR #244 lane-backlog groom named it the ONE new bullet of eleven with no
> routing flag anywhere (`.sessions/2026-07-12-websites-lane-backlog-groom.md` § 3) and the
> websites lane chain is PARKED at `8f97654` — lane self-serve never comes.)*

**Origin:** websites backlog bullet (quoted verbatim): *"a watch claim copied across N
heartbeat overwrites (the 'never delivered' cron verdict rode five) should carry a
last-verified timestamp (`watch: <claim> · verified <ISO>`) so readers see staleness and
writers re-verify before copying; /fleet could badge watches whose verified-stamp lags the
heartbeat. Worth having because inheritance is how this chain's one durable wrong claim
propagated."*

## The idea

A **carried watch** is a heartbeat line one coordinator generation inherits from the
previous — copied verbatim or carried by pointer at each overwrite. This repo's own
`control/status.md` @ `ce2fab4` is a live gallery of the pattern: "SWEEP NOTES preserved:
theme-schema promotion park HALF-FIRED watch (from #157); superbot-idle V006 guardrails
watch (from #157 …)" and "MANAGER SWEEP FLAGS carried unchanged from fc0bab6 … full text at
fc0bab6 control/status.md notes, not re-copied here" (line 10), plus line 9's standing
entries "preserved VERBATIM from the prior overwrite". The failure mode is that inheritance
is *textual, not evidential*: every overwrite renews the file's `updated:` stamp, but the
watch's justifying verdict or evidence is never re-checked — a watch records where it came
from ("from #157") but nothing distinguishes *re-verified this wake* from *copied N times
since anyone last looked*, so an expired or wrong claim propagates exactly as durably as a
true one. That is not hypothetical: the websites chain's one durable wrong claim (a "never
delivered" cron verdict that had stopped being true) rode five overwrites on precisely this
mechanism, and the risk peaks at **generation handoff**, where a fresh coordinator inherits
the whole watch set by ceremony with zero context to doubt any line of it.

The guard puts teeth on the inheritance step, cheapest first. **Grammar:** a carried watch
names its justifying pointer and a last-verified stamp — the source's token,
`watch: <claim> · verified <ISO>`, generalized with a `· per <verdict/PR/sha>` evidence
half. **Carrier duty:** at each overwrite (and mandatorily at generation handoff) the
writer either re-verifies the claim and refreshes the stamp, or carries it with the OLD
stamp intact — visible staleness instead of silent renewal; what the guard forbids is a
watch whose apparent freshness is the heartbeat's, not its own. **Check:** a report-only
advisory in the existing status-checker/preflight family (always exit 0, like
`--heartbeat-keys` and `--open-work`) flagging watch-class lines with no `verified` stamp
or a stamp lagging the heartbeat by more than N overwrites/days; the manager's `/fleet`
badge is the same finding rendered fleet-wide. **Smallest testable version:** the token
plus one deterministic grep-shaped advisory over `control/status.md` — stdlib, no network,
demonstrable on this repo's own carried watches today. Expiry action is a probe question,
not a given: auto-drop is probably wrong (the merge-hold head's `claims-stale` "delete it"
lesson — stale advice that would kill a legitimate hold), so v0 nags and a human retires.

## Relations (adjacent heads — deliberately links, not duplication)

- [`../websites/merge-hold-at-head-2026-07-11.md`](../websites/merge-hold-at-head-2026-07-11.md)
  — **sibling failure mode, stated explicitly per the dispatch**: state written into
  coordination files that no automation enforces or re-validates. The hold's finding is
  spatial (a HOLD nothing *reads*, so armed auto-merge fires through it); this guard's is
  temporal (a watch everything *copies*, so staleness compounds). Same doctrine, two axes —
  a kit slice carrying its check_claims carve-out is a natural carrier for this advisory too.
- [`../substrate-kit/parallel-session-heartbeat-reconcile-2026-07-10.md`](../substrate-kit/parallel-session-heartbeat-reconcile-2026-07-10.md)
  — the complementary heartbeat hazard: concurrent overwrites LOSING sibling facts vs
  sequential overwrites KEEPING facts past their evidence; both land as advisories on the
  same kit status-checker surface.
- [`lint-bundle-2026-07-11.md`](lint-bundle-2026-07-11.md) — `--heartbeat-keys` is the
  syntactic leg (declared key-set presence); this adds the semantic-freshness leg in the
  same always-exit-0 family.
- [`coordinator-archive-handoff-ceremony-2026-07-11.md`](coordinator-archive-handoff-ceremony-2026-07-11.md)
  — the guard is the missing re-affirm step at exactly the seam that ceremony names; its
  trigger-disposition table (every carried trigger dispositioned, none inherited silently)
  is the precedent shape, applied to watches.
- Not dups, same family: `../websites/own-heartbeat-parse-self-check-2026-07-11.md`
  (parseability, not freshness), `../superbot-mineverse/heartbeat-ladder-field-2026-07-11.md`
  (whose probe found machine *regeneration-from-source* mooted verbatim carry at the manager
  roster — the strong-form fix this guard's stamp is the cheap form of),
  `../superbot/queue-slice-staleness-age-2026-07-10.md` and
  `../superbot/reconciliation-slot-carry-tracker-2026-07-10.md` (staleness-age for carried
  lane-internal artifacts, not fleet heartbeat grammar).

Captured awaiting probe — the claim here is the mechanism and its live instances, not a
verdict. Probe should verify what watch grammar (if any) the kit-planted `control/README.md`
prescribes at live kit HEAD, pick the checker's home (kit-side vs per-repo preflight), and
price the /fleet badge half.

## Probe report (v0, 2026-07-12)

> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8f9765483a7df57ce426e7d11d200f10b5495ed7/docs/ideas/backlog.md@e14bb15 · fetched 2026-07-12T03:49Z
> *(pin annotation: source re-pinned FRESH at probe time — the fetch hashed to blob
> `e14bb15408b1f45de14eae72efe990024f0e548c` by `git hash-object`, byte-identical to
> the capture's pin (the same pin-verify the PR #244 groom and the #247 capture ran),
> source bullet intact at line 158. Kit-side grounding, commit-pinned: substrate-kit
> live HEAD = `8a544a63d9b98bab41ac3ba0e31f8863216b7582` by `git ls-remote`
> (2026-07-12T03:55Z — the git transport is open; only anonymous `api.github.com` is
> walled, 403 captured live this session, so the merge-hold probe's ls-remote transport
> replaces its reported-not-verified fallback here); the planted-contract template
> `src/engine/templates/control-README.md.tmpl` (path discovered from the vendored
> engine — `bootstrap.py:14660` embeds `control-README.md.tmpl`; the kit README names
> `src/engine/templates/` as the planted-template home) fetched AT that commit = blob
> `71c9ce4d010f88a1ea86e31752b3609c07d62e45`, and the kit's `docs/decisions.md` at the
> same commit = blob `f9b5d525084b284040bad8dae9d29516af5c81d9`, both by
> `git hash-object`.)*

> Single-pass battery (panel not escalated: process/lint head, report-only advisory,
> reversible, no security/data/spend/public blast radius — README § probe battery).
> Verify-first, live: (a) **specimen check — the confirm evidence, measured this
> slice**: this repo's own `control/status.md` @ main `6d40f6f` carries **14 inherited
> watch/flag entries** across its two explicit carry blocks — the ten "MANAGER SWEEP
> FLAGS carried unchanged from fc0bab6" plus the four "SWEEP NOTES preserved" entries
> (status.md line 10) — and **zero carry a `verified <ISO>` stamp** (grep for
> `verified <ISO-8601>` over the file: no hits); every freshness token present is
> "preserved verbatim" / "preserved VERBATIM" / "carried unchanged" — explicit
> declarations of NON-re-verification. The fc0bab6 ten-flag carry-by-pointer ("MANAGER
> SWEEP FLAGS carried unchanged from fc0bab6 … full text at fc0bab6 control/status.md
> notes, not re-copied here", line 10) is now SEVEN overwrites deep (fc0bab6 #220 →
> 42f9642 #224 → 0595466 #229 → 4f50cce #234 → d68ac2d #237 → d7c74d1 #245 → f0ea577
> #248 → ef46497 #249 — `git log --follow control/status.md`, run this slice); the two
> "from #157" watches (line 10 SWEEP NOTES: theme-schema promotion HALF-FIRED,
> superbot-idle V006 guardrails) crossed the a9b41f6→fc0bab6 GENERATION HANDOFF
> (#219 "archive-ready close-out" → #220 "first wake of new coordinator") from the
> previous coordinator generation; and four further "Carried unchanged" mint-exclusion
> items (rebuild-amendment-registry; rebuild-invocation-ladder-centralization; standing
> decay lines; venture-lab gate — line 10) are bare names with no justifying pointer at
> all. (b) **kit template check**: the planted contract prescribes NO watch grammar and
> no per-line freshness/verified-stamp token — this repo's kit-planted
> `control/README.md` status format block (lines 119–130) defines nine fields whose
> only freshness token is the file-level `updated:` stamp (line 121: "heartbeat — stale
> = the manager treats the Project as dark"), staleness is enforced whole-heartbeat
> only (lines 57–59: "warns when the heartbeat goes stale"), and "watch" appears zero
> times as grammar (sole match: "watched PR", line 215, in the auto-merge notes); the
> LIVE kit HEAD template (blob `71c9ce4` @ commit `8a544a6`) is identical on this point
> — zero "watch" hits, and the only "verified" is the OWNER-ACTION `VERIFIED-NEEDED`
> field (template line 153). (c) **target decisions grep** (README rule — `Target`
> differs from the canonical repo): kit `docs/decisions.md` @ `8a544a6` (227 lines)
> grepped for watch/stamp/staleness/verified/heartbeat — NO decision prescribes or
> forbids a carried-watch freshness token; the hits are whole-heartbeat gating,
> staleness, and heartbeat-path config (lines 123–165 and D-0010), and the nearest
> doctrinal neighbor is D-0009's adopter registry: `last-seen` = the evidence date,
> "staleness reads as *dark*, never as wrong" (lines 183–186) — the SAME
> evidence-dated-stamp doctrine, already decided at the kit-lab REGISTRY layer, absent
> at the status-watch layer. Kill test NOT triggered on either leg.

**1. What is this really?** A freshness invariant for inherited coordination state: a
carried heartbeat watch must carry its OWN evidence timestamp, distinct from the
heartbeat's `updated:` stamp, so "re-verified this wake" and "copied N times since
anyone looked" become distinguishable — for overwriting coordinators (the writers),
status readers, and the manager's /fleet sweep. It is the temporal sibling of
merge-hold's spatial finding: state written into coordination files that nothing
re-validates; there the state isn't read (so armed automation fires through it), here
it's read and copied forever (so a wrong claim propagates exactly as durably as a true
one).

**2. What is the possibility space?** (i) Do nothing — every carried watch keeps
inheriting the heartbeat's apparent freshness, and the next wrong verdict rides
overwrites the way the websites "never delivered" cron verdict rode five. (ii) Grammar
only — the `· verified <ISO> · per <pointer>` token in the planted contract: staleness
becomes visible but nothing surfaces it. (iii) Grammar plus one deterministic
report-only advisory — the captured shape and the smallest testable version: a
grep-shaped, stdlib, always-exit-0 check (the `--heartbeat-keys`/`--open-work` family)
over `control/status.md`, flagging watch-class lines with no stamp or a stamp lagging
by N overwrites/days. Demonstrable today: it would flag 14 of 14 current carried
entries in this repo's own file (and the four bare-name carries besides). (iv) (iii)
plus the /fleet badge — the same finding rendered fleet-wide, manager territory.
Value peak is (iii) with (iv) as a rider.

**3. What is the most advanced capability reachable by the simplest implementation?**
Fleet-wide prohibition of SILENT freshness from one kit PR, priced by half: the grammar
half is one paragraph in the kit-planted `control/README.md` template plus adopter
re-render; the checker half is one small stdlib advisory (~60 lines) in the kit
status-checker family; the /fleet badge half is the same finding rendered fleet-wide —
manager territory, priced as a rider (small IF /fleet already parses per-repo
`status.md`; unknown until a manager slice). Every adopter inherits both kit halves at
its next `bootstrap upgrade` — the same one-template-many-lanes economics the
merge-hold probe priced. The dominant cost is not code but Q4(d): making watch lines
machine-identifiable changes every coordinator's writing habit, not just the checker.

**4. What breaks it? (assumptions made explicit)** (a) The stamp lives in the STATUS
GRAMMAR (the kit-planted `control/README.md` heartbeat rules), enforced only as a
report-only advisory — never a hard gate. (b) The overwriting coordinator re-verifies —
optionally at each overwrite, mandatorily at generation handoff; the guard never forces
refresh, it forbids only SILENT freshness (a watch whose apparent freshness is the
heartbeat's, not its own — carrying an OLD stamp intact stays legal and visible).
(c) "Justification" machine-checkably = the line parses as watch-class AND contains
`verified <ISO-8601>` AND a `per <PR#|sha|path>` pointer — the checker verifies
presence/parse/lag, never pointer truth; truth stays human (the merge-hold
`claims-stale` lesson: auto-action on staleness kills legitimate holds, so v0 nags and
a human retires). (d) The soft spot: watch-class line IDENTIFICATION — the current
watches are free prose inside two giant lines (status.md lines 9–10); v0 needs either
a keyword heuristic (WATCH/STANDING/"carried") or a grammar change to
one-watch-per-line / a `watch:` prefix, and that grammar change, not the checker, is
the real cost.

**5. What does it unlock?** The three consumer classes each gain the distinction the
current grammar cannot express: an overwriting coordinator sees which inherited lines
it owes a re-verify (mandatorily at the handoff seam — exactly where the #157 watches
crossed generations unexamined); a reader sees "verified 3 overwrites ago" instead of
a fresh-looking heartbeat; the manager's /fleet sweep gets a badgeable staleness signal
per watch instead of per file. The next wrong verdict dies at its first carry instead
of riding five overwrites. And it completes the kit's own staleness doctrine one layer
down: whole-heartbeat staleness (planted checker) and registry `last-seen` (D-0009)
exist; per-watch evidence freshness is the missing middle this supplies.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing unshipped: the
planted `control/README.md` template and the status-checker family exist at every
adopter, and the format's tokens are kit-owned constants in `src/engine/grammar.py`
(the grammar-source-of-truth rule, control/README.md line 132) — the token lands where
writer and enforcer cannot drift. Cheapest confirm/kill evidence — already in hand,
gathered this probe: the precondition is universal (14/14 unstamped, specimen check
above), the mechanism is measured at the source (a wrong "never delivered" cron verdict
rode FIVE heartbeat overwrites at websites — backlog.md@`e14bb15` line 158), and the
peak-risk seam is live (the #157 watches crossed a coordinator generation handoff).
Kill test, both legs run live this probe: a kit template that already prescribes a
freshness token — NOT triggered (blob `71c9ce4` @ `8a544a6`, zero watch grammar) — or
regeneration-from-source landing fleet-wide (heartbeat-ladder-field's strong form) —
NOT triggered: the ladder-field probe found regeneration mooted verbatim carry only at
the manager ROSTER layer, not status watches, so the cheap form stands. Sim-worthy or
judgment-only: judgment-only — a deterministic lint over one file, no stochastic
behavior, no user-facing surface, nothing a simulation adds beyond the specimen check
this probe already ran; sending it to sim-lab would be asking the simulator to confirm
a grep.

**7. Which lane should build it — and what does it displace or duplicate?**
substrate-kit builds the grammar + advisory; the manager /fleet badge is a rider.
Duplicates nothing, swept by name: `--heartbeat-keys` (syntactic key presence — this is
the semantic-freshness leg of the same always-exit-0 family),
own-heartbeat-parse-self-check (parseability, not freshness), the verdict-registry lint
(idea-file verdict cites, not heartbeat lines), harvest-freshness-checker #22 (the same
staleness doctrine on harvest pins — the built precedent this generalizes), and
heartbeat-ladder-field (the strong-form displacement risk — but its probe found
regeneration applies at the roster layer only; prose watches remain, so the cheap form
stands). Carrier question (#243 flagged one kit slice already carrying multiple ritual
lines): this head's grammar + checker halves edit the SAME kit surfaces as the
merge-hold four-touch slice — its touch (3) is the planted `control/README.md` (this
head's grammar paragraph lands in the same planted contract) and its touch (2) is a
kit-checker carve-out (this head's advisory joins the same checker engine) — so the
recommendation is to ride that slice as a FIFTH touch, with the explicit flag that if
the manager judges the slice saturated, this splits cleanly into its own kit slice (the
grammar paragraph + advisory are self-contained). The manager decides at bundling; this
probe only names the seam.

**8. What is the smallest shippable slice?** Kit-side, three touches: (a) one grammar
paragraph in the planted `control/README.md` template defining the carried-watch token
`WATCH: <claim> · verified <ISO> · per <pointer>` plus the handoff re-affirm duty;
(b) one report-only `--watch-freshness` advisory (always exit 0) flagging
unstamped/lagging watch lines; (c) a template note that /fleet may badge lagging stamps
(manager rider, not in slice v0). A per-repo shim in this repo's
`scripts/preflight.py` is possible but duplicates kit territory pre-adoption — skip.

**Recommendation: park** — routed (kit/manager layer: rider on the merge-hold-routed
substrate-kit slice as its fifth touch — carried-watch grammar + report-only
`--watch-freshness` advisory; the /fleet badge stays a manager rider; the manager-sweep
flag rides this file + the session card since this slice cannot write `control/`).
Rationale: the confirm evidence is already measured (14/14 carried entries unstamped in
this repo's own status.md; the websites incident rode five overwrites) and the
mechanism is a deterministic lint — nothing left for sim-lab to settle; routing, not
evidence, is the open question, and the kit owns the grammar.
