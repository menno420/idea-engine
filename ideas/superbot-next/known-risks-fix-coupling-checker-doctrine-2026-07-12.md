# KNOWN_RISKS→fix coupling as checker doctrine — ledgered bugs whose rows the fixing PR must delete

> **State:** parked(routed — lane build-direct: one KNOWN_RISKS-disposition subsection folded into the SAME `docs/collaboration-model.md` doc-only lane slice already routed for the band-binding + effect-arming heads (three sections, one lane PR, could ride ONE lane ORDER) — probed 2026-07-12 at live N `39bf226`: the coupling is self-enforcing ONLY where instantiated — exactly 1 of 23 checkers carries the two-ledger idiom (`tools/check_money_race.py`; lifetime ledger history: 1 row minted #221, 1 deleted coupled-to-fix #223, 0 drifted — ledger now EMPTY), the sibling fences hold bare ALLOWED_* frozensets (no per-row justification, no stale-row guard), and the rule is encoded in NO doctrine surface (collaboration-model.md carries only @codex + "Friction → guard"; decisions.md greps zero; the routed sibling doc slice UNLANDED, inbox ORDERs 001–013 carry no doctrine order) — adoption is convention-by-imitation, the exact one-rotation-from-drop surface the lane's own ORDER 010 "ENCODE THE RULE DURABLY" precedent names; live contrast datapoint: the #194 prose-ledgered latent bug (`sb/domain/btd6/service.py:274-275`) still unfixed at N, uncoupled; a queued consumer exists (the routed recapture-disposition warn-first checker slice); nothing sim-shaped — a doc paragraph encoding a proven practice, red/green = the next checker mint's baseline disposition citing it)
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://github.com/menno420/superbot-next@80464ab39f86d55cede1e38b4780e7b1cc4a1777 · fetched 2026-07-12T01:34:18Z

Generalize the lane's just-proven #221→#223 pattern into standing checker doctrine: any
"suspected real bug" a committed checker surfaces lands as a loud KNOWN_RISKS ledger
row (reported on every run, never called safe) whose DELETION is mechanically coupled
to the fixing PR by a stale-row guard — fix-without-delete reds the checker — so
checker findings can't silently rot. Live proof at the pin: `tools/check_money_race.py`
(PR #221) ledgered the tournament-entry race as its single KNOWN_RISKS row, and the
stale-row guard forced the fixing PR #223 to ship fix + row deletion in one PR ("worked
exactly as designed", the fix session's own words). Adjacent but distinct in scope to
[`ideas/superbot/warn-first-checker-authoring-kit-2026-07-10.md`](../superbot/warn-first-checker-authoring-kit-2026-07-10.md)
(superbot-side checker AUTHORING ergonomics; this head is the finding-LIFECYCLE
coupling rule for this lane's checker fleet). Source: lane session card
[`.sessions/2026-07-12-tournament-entry-race-fix.md` § "💡 Session idea"](https://github.com/menno420/superbot-next/blob/80464ab39f86d55cede1e38b4780e7b1cc4a1777/.sessions/2026-07-12-tournament-entry-race-fix.md)
@ `80464ab` ([raw](https://raw.githubusercontent.com/menno420/superbot-next/80464ab39f86d55cede1e38b4780e7b1cc4a1777/.sessions/2026-07-12-tournament-entry-race-fix.md));
the pattern is also described at the lane heartbeat,
[`control/status.md`](https://github.com/menno420/superbot-next/blob/80464ab39f86d55cede1e38b4780e7b1cc4a1777/control/status.md)
(the #223 and #221 slice records) @ `80464ab`.

## Probe report (v0, 2026-07-12)

> **Grounding:** https://github.com/menno420/superbot-next@39bf226b98b48083f9b9d1b1cc8a644cd3dae9e3 · fetched 2026-07-12
> *(pin annotation: N = superbot-next live HEAD by `git ls-remote` this session =
> `39bf226b98b48083f9b9d1b1cc8a644cd3dae9e3` — three commits past the harvest pin
> `80464ab` (#227 four_twenty flip, #225 btd6 freeplay MOAB scaling, #226 creature
> flip). Every probe-relevant file is byte-identical across the gap (`git diff
> --stat 80464ab..HEAD` over the source card, `tools/check_money_race.py`,
> `docs/collaboration-model.md`, `docs/decisions.md`, `control/inbox.md` is
> EMPTY), so harvest-pin citations carry to HEAD unchanged. Tree scans via
> read-only blobless clone at N; file reads via raw at N.)*

> Single-pass battery (panel not escalated: doc-routing decision, reversible,
> no security/data/spend/public blast radius — README § probe battery).
> Verify-first at N: the pattern is LIVE and its one lifecycle is complete —
> [`tools/check_money_race.py`](https://raw.githubusercontent.com/menno420/superbot-next/39bf226b98b48083f9b9d1b1cc8a644cd3dae9e3/tools/check_money_race.py)
> defines the two-ledger idiom in its docstring (lines ~52–63: ALLOWLIST =
> verified-safe with per-row justification; KNOWN_RISKS = "REAL members of the
> defect class … Printed loudly on every run, NOT red — but never called safe.
> Fixing the site without deleting its row reds the checker"), its
> `KNOWN_RISKS` dict (line 118) is now `{}` with the cleared-row comment
> ("enter_tournament_in_txn's row cleared 2026-07-12"), and the stale-row red
> fires at lines 594–595. **But it is codified NOWHERE**:
> `docs/collaboration-model.md` @ N carries only the ORDER-010 @codex rule and
> the "Friction → guard" section (enforce-don't-exhort — no finding-disposition
> rule); `docs/decisions.md` @ N greps ZERO for
> `known_risk|known-risk|money_race|fix-coupl`; lane inbox ORDERs 001–013 carry
> no doctrine order; and the routed band-binding/effect-arming doc slice
> (`band-binding-doctrine-encoding-2026-07-10.md`,
> `effect-arming-compensator-checklist-2026-07-10.md` — both parked(routed —
> lane build-direct) toward the SAME doc) has NOT landed at N — the carrier is
> still open.

**1. What is this really?** A finding-LIFECYCLE disposition rule for the lane's
checker fleet, generalized from one complete, working instance: when a
committed checker's baseline sweep (or a later widening) surfaces a finding the
author judges a REAL member of the defect class but out of the lint PR's scope,
the ONLY legal disposition is a loud KNOWN_RISKS ledger row — keyed
(file, function, rule), justified, reported on every run, never called safe —
whose deletion the stale-row guard mechanically couples to the fixing PR.
Never allowlisted-as-safe (a lie), never a prose TODO (uncoupled). Live proof
at N: the #221 lint ledgered `enter_tournament_in_txn` as its single
KNOWN_RISKS row; the fixing PR #223 was FORCED to ship fix + row deletion in
one PR ("worked exactly as designed" — the fix card's own words,
[`.sessions/2026-07-12-tournament-entry-race-fix.md` § 💡](https://raw.githubusercontent.com/menno420/superbot-next/39bf226b98b48083f9b9d1b1cc8a644cd3dae9e3/.sessions/2026-07-12-tournament-entry-race-fix.md);
heartbeat records at
[`control/status.md`](https://raw.githubusercontent.com/menno420/superbot-next/39bf226b98b48083f9b9d1b1cc8a644cd3dae9e3/control/status.md)
lines 6/19/23/28/31). Who it's for: the next N seat that mints or widens a
checker and hits a real bug it can't fix in the same PR.

**2. What is the possibility space?** (i) Do nothing — the idiom lives in one
checker's docstring + heartbeat prose + a session card; the next checker author
may imitate it (N checkers demonstrably copy prior checkers' idioms —
check_money_race's own docstring cites "check_egress / check_no_skip
precedent"), or may not. (ii) One standalone doctrine PR — over-weight for a
paragraph. (iii) **Fold one subsection into the SAME `docs/collaboration-model.md`
doc-only slice already routed for band-binding + effect-arming** (three
sections, one lane PR/ORDER) — the value peak: marginal cost ≈ one paragraph
riding an already-routed carrier, homed beside "Friction → guard" (the rule is
that section's missing second half: friction→guard says BUILD the checker;
this says what the checker's REAL-bug findings must do). (iv) A meta-checker
asserting every `tools/check_*.py` with a warn-class ledger carries a stale-row
guard — over-mechanized for a 1-member family; YAGNI until the family grows.
(v) Kit-level (substrate-kit PL-register) — premature at n=1 lifecycle and one
lane; the fleet-wide generalization is the manager's call, not this probe's.

**3. What is the most advanced capability reachable by the simplest
implementation?** One doc paragraph makes the disposition DEFAULT instead of
one seat's style: every future checker mint/widening at N inherits
"suspected-real-bug ⇒ loud coupled row" without re-deriving it, and the #221
card's own under-specification lesson rides along free (the ⟲ section:
"Future ledger rows should carry the oracle citation for the intended
semantics up front" — a row-content rule only a doctrine surface can carry
forward). The crux fact the verdict turns on: **the mechanism is
self-enforcing per instance, but adoption is NOT self-propagating** — exactly
1 of 23 checkers at N carries the two-ledger idiom (blobless-clone grep:
`KNOWN_RISKS` hits only `tools/check_money_race.py`); the sibling fences
(`check_egress.py`, `check_no_skip.py`) hold bare `ALLOWED_*` frozensets with
no per-row justification and no stale-row guard. An uncodified convention
under continuous mode's fresh seats is the exact "one rotation from silent
drop" surface the lane's own ORDER 010 diagnosed and fixed for the @codex rule
("ENCODE THE RULE DURABLY: write it into the working doctrine every Builder
session boots from … so it survives inbox rotation").

**4. What breaks it?** (a) The reject case, weighed honestly: at n=1 lifecycle
(1 row minted, 1 deleted coupled-to-fix, 0 drifted — "not measured" beyond
that because no more rows have ever existed) one could rule the pattern
already terminal. What defeats the reject: the failure mode the doctrine
prevents is ALIVE at N in its uncoupled form — the #194 session prose-ledgered
latent bug (`sb/domain/btd6/service.py:274-275`, `_run_op` reads `result.ok` /
flat `result.after`) is STILL live at N, file untouched since #144, no
coupling forcing a fix (honest note: session-found not checker-found, and
judged unreachable via golden-driven lanes — deliberate deferral, but it
demonstrates prose rows have no lifecycle guard). (b) Timing: the next checker
author may imitate check_money_race anyway — then the doc's marginal value
drops to the citation/row-content function (still nonzero, near-zero cost).
(c) Mis-homing: if the routed band-binding/effect-arming slice lands before
this relays, the fold-in becomes a trivial follow-up to the same doc — the
carrier choice degrades gracefully. (d) Scope inflation: writing it as a
mandatory idiom for ALL 23 checkers would be wrong — the pure structural
fences (egress/no_skip) red on any finding and need no risk ledger; the rule
binds only checkers whose findings can be judged real-but-out-of-scope.

**5. What does it unlock?** Checker findings that cannot silently rot,
fleet-wide by default; the #221→#223 coupling repeatable by rule rather than
memory; and the row-content lesson (oracle citation up front) delivered to the
next row author. Downstream: a clean precedent the manager can lift to the
substrate-kit PL-register if a second lane grows a judgment-class checker.

**6. What does it depend on?** Nothing unshipped: the exemplar checker, the
fix card, and the doctrine doc all exist at N; the routed carrier slice
(band-binding + effect-arming, same doc) is verified UNLANDED at N so the
ride-along is still open. Cheapest confirm/kill evidence, priced: this probe's
confirm cost was one `git ls-remote` + one blobless clone + ~6 raw reads
(decisive facts: 1/23 adoption; ledger lifecycle 1-minted/1-coupled-deleted/
0-drifted; zero doctrine encoding; carrier unlanded). The build-time red/green
is judgment-shaped but cheap: the NEXT checker mint at N whose baseline sweep
finds a real bug either cites the section and ships a coupled row (green) or
ships a prose TODO/safe-allowlist (red — and the doc gives the reviewer the
citation to demand the row).

**7. Which lane should build it — and what does it displace or duplicate?**
**superbot-next** — build-direct: it owns the doc, the checker, and the
proof case; the slice is one paragraph riding the already-routed doc-only PR.
Not sim-lab: nothing to measure — a doc encoding of a proven practice, the
same nothing-sim-shaped ruling as the band-binding and effect-arming heads
(and unlike `rebuild-design-cite-checker`, there is no grammar × gating
parameter space to sweep: the mechanism is already built and proven). Dedup
findings, named:
[`ideas/superbot/warn-first-checker-authoring-kit-2026-07-10.md`](../superbot/warn-first-checker-authoring-kit-2026-07-10.md)
(probed 2026-07-12, PR #230, parked trigger-misfire) — **adjacent, not
overlapping**: authoring ERGONOMICS (scaffold + shared AST lib for superbot's
warn-first family) vs finding LIFECYCLE at N; its census is this probe's
baseline (23 checkers at N, red-gating convention, no shared lib) and its
park confirms no kit will carry this rule — a doctrine doc is the only
carrier on offer. [`band-binding-doctrine-encoding-2026-07-10.md`](band-binding-doctrine-encoding-2026-07-10.md)
+ [`effect-arming-compensator-checklist-2026-07-10.md`](effect-arming-compensator-checklist-2026-07-10.md)
— same CARRIER (one `docs/collaboration-model.md` slice), disjoint content;
this head is the third section on that ride, not a duplicate.
[`oracle-copy-punctuation-drift-sweep-2026-07-12.md`](oracle-copy-punctuation-drift-sweep-2026-07-12.md)
(sim-ready, PROPOSAL 011) — same source card's OTHER 💡 half, disjoint.
`ideas/superbot/golden-recapture-on-bugfix-2026-07-10.md` (parked routed —
superbot-next recapture-disposition ledger + warn-first checker slice) — the
QUEUED CONSUMER: that routed checker mint is precisely a
judgment-class/ledgered checker whose baseline disposition this doctrine
binds. `ideas/fleet/lint-bundle-2026-07-11.md`, superbot
`rebuild-critical-review-checkers` / `settle-once-architecture-guard` /
`audit-seam-coverage-checker` — checker-family heads, other repos/surfaces,
no lifecycle-rule overlap. No duplicate idea file.

**8. What is the smallest shippable slice?** One subsection (~a paragraph) in
the routed `docs/collaboration-model.md` lane PR, beside "Friction → guard":
a committed checker's finding judged a REAL class member lands as a loud
KNOWN_RISKS row — keyed, per-row justified, carrying the oracle/intended-
semantics citation up front (the #223 card's ⟲ lesson), reported every run,
never called safe — under a stale-row guard so fix-without-delete reds the
checker; verified-safe sites go to ALLOWLIST with justification; prose TODOs
and safe-allowlisting of suspected bugs are banned dispositions. Cite
`tools/check_money_race.py` as the reference implementation and #221→#223 as
the proof case. Cost: one paragraph on an already-routed doc slice; zero
code, zero behavior change. This-repo-side: this probe + park (nothing to
build here, Q-0260).

**Recommendation: park** — routed (lane build-direct: fold the KNOWN_RISKS
disposition subsection into the same `docs/collaboration-model.md` doc-only
slice already routed for band-binding + effect-arming — verified UNLANDED at
N `39bf226`, so the ride is open). Rationale: the coupling mechanism is
self-enforcing only where instantiated (1 of 23 checkers; lifecycle history
exactly 1 row, coupled-deleted, 0 drifted) and adoption-by-imitation is the
lane's own diagnosed one-rotation-from-drop failure mode (ORDER 010), so a
one-paragraph codification on an already-routed carrier buys the default at
near-zero marginal cost — while a standalone doctrine PR would over-weight an
n=1 pattern, and a full reject would leave the #194-class uncoupled
disposition as the unstated default.
