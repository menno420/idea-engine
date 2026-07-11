# A `check_architecture` rule: settling game paths must adopt `SettleOnceMixin` — link index

> **State:** sim-ready
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/settle-once-architecture-guard-2026-06-24.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/settle-once-architecture-guard-2026-06-24.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/settle-once-architecture-guard-2026-06-24.md)).

A check_architecture rule that settling game paths must adopt SettleOnceMixin — the double-settlement race class recurred four times; the money leg was built (superbot PR #1454), the guard itself is the remainder.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/8214200aa0c00dda4156748617c9482dadc4277a/docs/ideas/settle-once-architecture-guard-2026-06-24.md@8214200 · fetched 2026-07-11T16:16Z
> *(pin annotation: superbot live HEAD S = `8214200aa0c00dda4156748617c9482dadc4277a` by `git ls-remote` 16:20:34Z (doc fetched via the /main/ raw path; main == S at the ls-remote instant). The canonical doc at S carries the "money leg BUILT (2026-06-25 dispatch run, PR #1454)" banner — Rule 6 `settle_once_adoption` in `check_consistency.py`, warn-first — and the DELIBERATE deferral of the broader "posts a terminal result" leg: "static 'settles via a result message reachable from on_timeout' detection is false-positive-prone, and a warn-clean rule must stay precise." Provenance Q-0089, the 2026-06-24 settle-once dispatch run, PRs #1444 + #1445.)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/8214200aa0c00dda4156748617c9482dadc4277a/scripts/check_consistency.py@8214200 · fetched 2026-07-11T16:22Z
> *(pin annotation: read via read-only blobless clone at S, the standing recipe. Rule 6 is LIVE and was WIDENED after the money leg: `_WAGER_SETTLE_CALLS = {settle_pvp, refund_pvp, payout_tournament, update_leaderboard}` (check_consistency.py:899-901) — the last two joined via commit `afec1f1` 2026-07-07 ("fix(games): settle-once guards for the three unguarded settlement paths (FINAL-REVIEW §6.3)", merged in PR #1781) after "the 2026-07-06 Gate-V Arm-D live run double-wrote through the unguarded `_DuelView`" (the rule's own comment, :890-892). Severity is still `"warning"` in the RULES registry (:1150) — NOT graduated; CI runs `check_consistency.py --mode strict` (`code-quality.yml:207`) which fails only on `error`-severity rules, so a Rule 6 finding never reds CI. DRIFT FOUND BY THIS PROBE: the rule function's default roots and docstring claim the 2026-07-07 widening put `cogs/` in scope ("the deathmatch human-duel view lives in cogs/ … so the cog layer is in scope", :1004-1008), but the registry entry passes `roots=("views/", "services/")` (:1151) and `main()` invokes `rule.fn(files, exceptions, rule.roots)` (:1185) — the cogs/ scope half of the widening is silently INERT. Latent, not live-failing: `disbot/cogs/deathmatch_cog.py::_DuelView` adopts `SettleOnceMixin` today (:100, claims at :162/:243) — but a NEW unguarded cogs-layer settle site, the exact Gate-V-recurrence shape, would ship unscanned while the docstring says otherwise. `scripts/check_architecture.py` at S carries NO settle rule (its "terminal" family is the Q-0194 dead-end-view checks) — the idea's literal `check_architecture` ask landed in `check_consistency` instead, as the canonical doc's banner records.)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-next/14e503769202e7ca38609c2063366d8db60bf2f0/docs/decisions.md@14e5037 · fetched 2026-07-11T16:24Z
> *(pin annotation: superbot-next live HEAD N = `14e503769202e7ca38609c2063366d8db60bf2f0` by `git ls-remote` 16:20:34Z. NO static settle-once checker exists at N: `tools/` holds 22 `check_*` checkers (ls-tree at N), none settlement-shaped. The rebuild's answer is architectural discipline, D-0042 ("Band 6 slice 1 … escrow-once wager lanes"): "the op owns the ONE txn … idempotency is DOUBLE-guarded exactly like shipped (once() fence + FOR-UPDATE row-consumption: a settle finding its escrow rows gone pays nothing)". The newest recurrence broke through exactly where that discipline has no row to consume: superbot-next PR #133, the blackjack-tournament consolation double-payout race ("no escrow rows to consume — two racing champion resolutions could both pay the consolation"; fixed as check-and-set keyed on the atomic row-deletion count, retrofit onto `rps.tournament_payout` too) — quoted with the fix shape in this repo's merged effect-arming probe, ideas/superbot-next/effect-arming-compensator-checklist-2026-07-10.md:58-61. N's heartbeat at HEAD ledgers "the settle-once + render-once guards" as band-6 PER-OP runtime fixes; nothing structural or CI-shaped shipped, and superbot's own Rule 6 comment names the same hole class at S: "`payout_tournament`'s free-reward leg has no escrow rows to consume, making the caller-side claim its ONLY guard" (check_consistency.py:887-889).)*

> Single-pass battery (panel not escalated: the idea is CI/process tooling — no
> live money moves in the diff it asks for — and the verify-first reads are
> decisive, no ambiguity signal; README § probe battery). Both queued
> verify-first 💡s were applied FIRST, per the karma card's handoff: the #180
> ledger grep at superbot-next (D-# nouns: hits D-0042/D-0045 discipline, no
> guard decision) and the #183-card folio/tree check at superbot
> (`disbot/` ls-tree for settle nouns: `utils/terminal_guard.py`, the Rule 6
> body, four settle-once test files, four .sessions cards — no
> docs/subsystems folio for settlement exists). One count correction against
> the briefed framing, evidence-first: the class has SIX documented instances,
> not five — (1) BUG-0013 (challenge view); (2)–(4) the three sites the
> 2026-06-24 by-hand run adopted the mixin in (RPS PvP, deathmatch bot-duel,
> blackjack PvP — PRs #1444/#1445, the canonical doc's provenance block);
> (5) the Gate-V Arm-D deathmatch W/L double-write through the then-unguarded
> `_DuelView` (2026-07-06 live run, fixed in the #1781 widening); (6)
> superbot-next #133's consolation double-payout — the first recurrence IN THE
> REBUILD, and the one that proves the class survives a from-scratch
> architecture designed to kill it.

**1. What is this really?**
A process idea (canonical superbot doc 2026-06-24, Q-0089): mechanize the
by-hand double-settlement hunt as a static CI rule. The verify-first read
splits it three ways. At superbot the money leg is BUILT (Rule 6, 2026-06-25,
promoting this very idea) and has since been WIDENED (#1781, two new sinks
after recurrence #5) — but it is still warn-only (never reds CI), its cogs/
scope widening is silently inert (the registry-roots drift this probe found),
and the structural "posts a terminal result" leg stays deliberately deferred
as false-positive-prone. At superbot-next — where all new settling paths are
being minted — NO guard exists at any layer above per-op discipline, and
recurrence #6 (#133) broke through that discipline exactly where it has no
consumable row. What remains of the idea is therefore not "build the rule"
(built, at the legacy tree) but a GUARD-DESIGN question with six real
datapoints: what contract must every settling path satisfy so the class
cannot recur, and can a checker enforce it without the false positives both
repos' own records warn about?

**2. What is the possibility space?**
(i) Superbot housekeeping: fix the one-line registry-roots drift, graduate
Rule 6 warn→error after its soak, optionally build the deferred structural
leg — all legacy-tree work whose value decays as the rebuild replaces it.
(ii) Rely on superbot-next's architectural discipline alone (D-0042 once()
fence + FOR-UPDATE row-consumption) — already breached by #133's
no-consumable-row leg, and superbot's own Rule 6 comment names the identical
hole (`payout_tournament`'s free-reward leg). (iii) A superbot-next static
checker on its proven `tools/check_*` CI seam mandating a settle-once
contract for every K7 money-moving op leg — the rebuild analog of Rule 6,
made MORE tractable by the K7 grammar (money moves only through declared
CompoundOpSpec legs, a closed enumerable set, vs AST-hunting arbitrary call
sites in disbot/). (iv) A runtime invariant instead — REJECTED by analysis
(derivation, not measured): INV-F-style reconciliation cannot see this class,
because a double-settle writes balance AND ledger consistently on BOTH legs,
so balance == Σ(ledger) stays green through a double payout. (v) Validate the
guard design against the six-instance corpus BEFORE building (iii) — the
sim-shaped half.

**3. What is the most advanced capability reachable by the simplest implementation?**
One static rule with the RIGHT contract makes the seventh recurrence
impossible-to-merge instead of caught-mid-flight: every money-moving op leg
must statically prove either consumable-row consumption (check-and-set on the
atomic deletion count — the #133 fix generalized) or an explicit atomic claim
(the Rule 6 / SettleOnceMixin shape) — checked at CI on the same seam as N's
22 existing checkers. The contract choice is the whole game: pick (b)-style
row-consumption alone and #133 recurs; pick a fuzzy structural rule and the
false-positive trap both repos deferred on fires; pick the right one and the
D-0043 successor ports (deep mining/fishing systems, creature battle engine,
blackjack/RPS tournament orchestration — the tournament orchestration is
literally the surface #133's race lived on) land born-guarded.

**4. What breaks it?**
False positives, above all — the reason superbot deferred the structural leg
TWICE (the canonical doc's §Open/cautions and the Rule 6 comment both insist
a warn-clean rule must stay precise); a noisy money-safety rule gets
allowlisted into meaninglessness. Scope drift, second — this probe's own
finding: a widening that edits the rule function but not the registry is
silently inert (the same silent-no-op class as this repo's branch_patterns
lesson, PR #55 card), so the checker contract must include its own
wiring-tripwire. Wrong-layer transplant, third: porting the SettleOnceMixin
AST shape verbatim to sb/ would miss — N has no views settling money; ops
do. And an unvalidated design pick re-admits the breach: mandating
row-consumption alone is refuted by instance #6, mandating universal claims
alone leaves the no-row legs' check-and-set undefined.

**5. What does it unlock?**
The queued new settling paths land guarded instead of vigilance-guarded: the
D-0043 deep-systems successor ports and the pending tournament orchestration
each mint money paths, and today their only net is per-PR review memory (the
effect-arming probe's finding that #133 was "caught mid-flight, not
pre-empted"). A validated contract also gives superbot's Rule 6 its
graduation evidence (warn→error), gives the effect-arming checklist's item
family a mechanical sibling, and closes the last open leg of this idea's
lineage — the 2026-06-24 run's "the manual hunt is the part worth
mechanizing" — at the tree where the hunt will otherwise be re-run by hand
for every new game.

**6. What does it depend on?**
The six-instance corpus, all documented and publicly readable (BUG-0013 +
PRs #1444/#1445 provenance at S; the #1781 widening; superbot-next #133's
recorded race + fix shape); superbot-next's `tools/check_*` CI seam and K7 op
grammar (D-0010) + wager-lane discipline (D-0042) as the enforcement
substrate; sim-lab's standing read access to both public repos for
reconstruction. No owner action anywhere on the path; superbot's one-line
roots fix and graduation call are the legacy lane's own (Q-0260).

**7. Which lane should build it? (honest routing)**
The checker itself: `menno420/superbot-next` — it owns the seam, the op
grammar, the queued settling paths, and the live recurrence risk; superbot's
Rule 6 residue (registry-roots one-liner, graduation) is superbot's own
housekeeping, routed by sweep flag, never from this seat. But the DESIGN is
not yet decided anywhere: S and N answered the same class two different ways
(caller-side static claim vs row-consumption discipline), each answer has a
documented breach or a documented false-positive fear, and six reconstructed
instances exist to measure against. That is a sim-shaped question in this
repo's own pipeline sense — a reproduced-evidence verdict (catch matrix +
false-positive count per candidate contract) settles with data what the lane
would otherwise pick by judgment on a money-safety class. PROPOSAL 009
routes exactly that; the lane build follows the verdict.

**8. What is the smallest shippable slice?**
Sim-lab: reconstruct the six instances as minimal replayable cases, run the
three candidate contracts against them — (a) universal caller-side atomic
claim (Rule 6 shape), (b) row-consumption alone (D-0042 shape), (c)
row-consumption + mandated check-and-set for no-row legs (the #133 fix
generalized) — and emit the catch matrix, the false-positive count on both
current trees, and ONE recommended contract. Lane afterwards (one PR each,
post-verdict): superbot-next `tools/check_settle_once.py` implementing the
winning contract warn-first (the lane's own Q-0105 posture); superbot's
one-line registry-roots fix. Red/green reference: the next tournament-family
port merging with the checker green and no mid-flight settle save in its PR
thread.

**Recommendation: sim-ready** — the guard's remainder is a design fork on a
money-safety class with six documented instances and a proven false-positive
trap: reproduced evidence (catch matrix + false-positive count per candidate
contract) beats judgment here, and PROPOSAL 009 routes that one question to
sim-lab before any lane builds the checker.

## Sim verdict (2026-07-11)

sim-lab **VERDICT 010 · finalized 2026-07-11T17:15:57Z · approve**
(= this repo's PROPOSAL 009 — sim-lab numbers by INTAKE order; sim-lab's own
VERDICT 009 is an unrelated OWNER-DIRECT superbot-next sim; lineage through
V008 on the V007 card). Source pin:
[sim-lab `control/outbox.md` @ `87ca0df`](https://github.com/menno420/sim-lab/blob/87ca0dfb562cb00a3da390c1c155d244fb4bb9b8/control/outbox.md)
(verdict PR #36 squash `e559a37`; triage/INTAKE PR #35 squash `41b26b5`;
report `sims/verdict-010-settle-once-architecture-guard/`). Like V006/V008
the entry carries no `ruling:` field — the operative ruling is the
`recommendation:` field, quoted: "adopt contract (c) — row-consumption +
mandated check-and-set for no-row legs." Catch matrix (4 contracts × 6
double-settlement instances, exhaustive interleaving sweep 6/90 per
instance, 72 self-checks 0 failed): (c) 6/6 0-missed WINNER; (b)
row-consumption alone — the current superbot-next D-0042 discipline — 1/6,
already breached by #133 at a no-escrow-row leg (the headline negative);
(a) caller-side atomic claim 3/6 as-shipped → 5/6 with the cogs/ roots-fix
(still cross-tree miss on #133). Gate: PASS (COMPARABLE bounded-structural ·
UNCORRUPTED 72 self-checks 0 failed, one real escrow-pot model bug caught by
self-check and fixed pre-finalization · ROBUST exhaustive interleaving +
retry-3 variant · REPRODUCIBLE one command byte-identical · LIMITS:
live-checker false-positive count NOT MEASURED — grep enforcement-surface
proxies only, an over-count upper bound). Build guardrails carried by the
verdict: the checker scope must enumerate EVERY money-moving root (the
cogs/ drift IS the failure mode), and the settle-flag must expose explicit
re-arm (`rearm_settlement`) or it false-positives legit multi-stage
tournament settlement. The probe's Rule 6 registry-roots finding is
CONFIRMED STILL LIVE by the sim (`check_consistency.py:1151` registers
`roots=("views/","services/")` while the docstring/default at
`:984`/`:1007` claim `cogs/`; 8 cogs/ guard-adopters outside the scanned
roots) — the done-when's drift question is answered: it moves contract (a)
from 3/6 to 5/6 but does not change the winner. Post-verdict routing is the
manager's per Q-0264 — targets superbot-next (`tools/check_*` settle-once
fence over the K7 op grammar D-0010, warn-first per Q-0105) + superbot
(one-liner `roots += "cogs/"`). State stays `sim-ready`, forward-only and
untouched — this note, not a new state, is the canonical verdict marker.
