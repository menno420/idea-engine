# Idea — "audited per-user score" subsystem scaffold + parity guard — link index

> **State:** parked(routed — trigger already fired: karma hand-built the six-piece shape 2026-06-22; general half built at superbot PR #1346; score half structurally superseded at superbot-next D-0005/D-0038; the remaining RankProvider parity guard is superbot's own one-file lane-side test, flagged for fleet-manager routing)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/audited-score-subsystem-scaffold-2026-06-22.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/audited-score-subsystem-scaffold-2026-06-22.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/audited-score-subsystem-scaffold-2026-06-22.md)).

Economy, XP, and karma are the identical six-piece per-user-score shape (DB seam, audit table, service write seam, catalogue entry, INV test, rank provider); scaffold it plus a parity guard so new score subsystems are stamped out consistently. Partially implemented (superbot PR #1346).

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/1eeedb03b8a29992e438544e5e3c0e1ef51d35b0/docs/ideas/audited-score-subsystem-scaffold-2026-06-22.md@1eeedb03b8a29992e438544e5e3c0e1ef51d35b0 · fetched 2026-07-11T17:01:06Z
> *(pin annotation: superbot live HEAD S = `1eeedb03b8a29992e438544e5e3c0e1ef51d35b0` by `git ls-remote` 2026-07-11T16:50:48Z — S moved past the capture pin `fd638e3`. The canonical doc's own 2026-06-23 update names WHICH half "partially implemented" means: PR #1346 (merged 2026-06-23, merge `36aa35a76dc0dfd979a1b449f97ff19bae813084`) "closed the checker's blind spots" of the pre-existing GENERAL scaffold (`scripts/new_subsystem.py` + the `/new-subsystem` skill — three new checks: config.py extension-loading, extension_roles.yaml overlay, sector-folio homing, each with a test) rather than minting a parallel score-only generator; "**Still open:** the **score-specific** half … the `RankProvider` parity guard (item 6), which the general checker does not cover because it's leaderboard-specific." Invocation-site verify (the #186 card 💡, not body greps): `scripts/new_subsystem.py@1eeedb0` is a manual CLI (argparse mode ∈ check|scaffold; scaffold PRINTS paste-ready snippets, "deliberately edits nothing"), invoked by the skill's :47/:58 lines and LOGIC-pinned in CI via `tests/unit/scripts/test_new_subsystem.py` under `code-quality.yml:275` pytest — but NO CI step runs new_subsystem.py itself (full grep of the workflow's run: lines). Score half ABSENT at S: `scripts/new_score_subsystem.py` → 404; zero rank/RankProvider handling in new_subsystem.py; no parity rule in `scripts/check_consistency.py`; no tables↔`_PROVIDERS` cross-check in `tests/unit/services/test_rank_providers.py` (627 lines, provider unit tests only) nor among the 68 `tests/unit/invariants/` files. Karma's item 6 was hand-done: `KarmaProvider` at `disbot/services/rank_providers.py:587`, registered in `_PROVIDERS` :627/:641, aliases rep/reputation/karmalb :671-673.)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-next/4024624d3258aa982bac466acb16a51b17bbc6df/docs/decisions.md@4024624d3258aa982bac466acb16a51b17bbc6df · fetched 2026-07-11T17:01:07Z
> *(pin annotation: superbot-next live HEAD N = `4024624d3258aa982bac466acb16a51b17bbc6df` by the same ls-remote pass. Full D-0001–D-0073 ledger: ZERO hits for audited-score/new_subsystem/new_score/scaffold — the idea never crossed to the rebuild because the rebuild answers "stamp out subsystems consistently" STRUCTURALLY: D-0005 (decided 2026-07-08) makes every subsystem a declared manifest compiled through the K2 9-pass gate (`tools/manifest_compile.py` P1–P9, A-2 schema-growth ledger, boot gate) — a scaffold script has no role in that architecture; D-0038 (decided 2026-07-09) ports the provider REGISTRY (`sb/domain/community/rank_providers.py`) with "band 6 adds game categories BY REGISTERING PROVIDERS (the shipped 'never edit a consumer' invariant, test-pinned)" and a provider-fed category selector — the parity property the guard half wants, held by construction+test at N. Karma context: D-0037 ported the hand-built karma verbatim; D-0061 fixed its clock split.)*

> Single-pass battery (panel not escalated: verify-first is decisive at both live
> pins, no ambiguity signal, no security/data/spend/public blast radius — README
> § probe battery). The re-priced live question from the #183/#186 handoffs —
> "scaffold value for the NEXT score subsystem" — was premise-verified FIRST at
> invocation/registration sites per the #186 card 💡, and answered: no next score
> subsystem is queued at S (its docs/roadmap horizon is fix-phase + rebuild-parallel;
> no score-shaped idea in its backlog index is promoted), and at N the next score
> subsystem arrives as a manifest + registered provider, not as six hand-copied
> files. Orthogonality note (stated here deliberately, no Sequence line — the
> Sequence grammar only speaks before/after/behind an event, and there is no
> ordering relation to encode): this head is NEITHER a dependency NOR a consumer
> of PROPOSAL 009 (settle-once guard matrix). The scaffold's pieces 1–3 (audit
> table + single write seam) are the substrate settle-once discipline rides on,
> but that substrate is built three times over (economy/XP/karma); the remaining
> parity-guard half touches leaderboard registration, not money-moving legs, and
> PROPOSAL 009's checker targets N's tools/check_* seam for settle legs. Shared
> pattern only (a static checker at a CI seam); neither blocks nor feeds the other.

**1. What is this really?**
A process idea captured BY the karma planning session (2026-06-22): economy, XP,
and karma repeat an identical six-piece per-user-score shape by hand, so build
(i) a score-subsystem scaffold and (ii) a RankProvider parity guard. Verify-first
re-prices it as a SPLIT head: the general half is built and consumed (PR #1346
closed the existing checker's three blind spots the karma build revealed —
test-pinned in CI, skill-invoked on demand), and the score-specific half
(generator + parity guard) is dormant-but-open at S only, with its own trigger
("the moment the next karma-like build starts") already in the past tense —
karma hand-stamped all six pieces the same day the idea was captured.

**2. What is the possibility space?**
(a) The score-only generator `scripts/new_score_subsystem.py` — absent at S
(404 @ `1eeedb0`), and the canonical doc's own 2026-06-23 update argues AGAINST
minting it ("rather than mint a parallel score-only generator"), leaving only an
extend-the-skill variant; disposable by its own Q-0105 clause. (b) The
RankProvider parity guard — a one-file test cross-checking leaderboard-worthy
score tables against `_PROVIDERS` plus an allow-list; absent at S (no rule in
check_consistency.py, no test in test_rank_providers.py or the 68 invariants
files). (c) CI-wiring new_subsystem.py itself (today it is logic-pinned by
pytest but never executed by a CI step) — a superbot hygiene call, not this
idea's ask. (d) At N: nothing — D-0005's manifest compiler and D-0038's
test-pinned provider registry hold both halves' properties by construction.

**3. What is the most advanced capability reachable by the simplest implementation?**
For the general half: already reached, by the simplest means available — +98
lines extending the existing checker instead of a new generator (PR #1346). For
the still-open score half: one lane-side pytest file (tables↔`_PROVIDERS`
set-difference with an explicit allow-list) delivers the entire remaining value —
"shipped a new scoreboard with no leaderboard category" becomes structurally
impossible at S. No generator needed for that; the canonical doc itself ranks
the guard as "the higher-value half [that] should outlive the generator."

**4. What breaks it?**
The trigger's absence: the idea's activating event already fired (karma,
2026-06-22, hand-built — `KarmaProvider` registered at
`disbot/services/rank_providers.py:587/:627/:641`), and no next score subsystem
is queued at S, so a generator built now would sit unused — exactly the
friction-vs-copy-paste failure its own Q-0105 disposal clause anticipates. At N
the whole idea is structurally superseded: a manifest-compiled subsystem cannot
skip its provider registration (D-0038's never-edit-a-consumer invariant is
test-pinned), so porting either half there would re-solve a solved problem. The
parity guard alone has no real break mode beyond allow-list upkeep — which is
why it survives as the routed remainder.

**5. What does it unlock?**
The parity guard closes the "scoreboard with no leaderboard category" gap class
at S for the live bot's remaining life (the exact gap karma would have had if
its provider were forgotten) and hardens the seam the #186 probe showed is
where drift hides — registration sites, not bodies. The generator unlocks
nothing until a next score subsystem is queued (none is). Closing this head also
retires TOP-5 item 4 and promotes item 5 (wager-flow-map) to ripest.

**6. What does it depend on?**
Nothing open. The templates it would stamp from (economy/XP/karma) and the
registry it would guard (`_PROVIDERS` + migrations) all live at S today. It does
NOT depend on PROPOSAL 009, and PROPOSAL 009 does not consume it — orthogonal
heads (per the preamble note: shared static-checker-at-CI-seam pattern only; the
guard half touches leaderboard registration, never a money-moving leg). No owner
decision is required: the canonical doc already made the design calls (guard
over generator; allow-list for intentional exclusions).

**7. Which lane should build it? (honest routing)**
superbot itself, for the parity guard only — a one-file test in its own
`tests/unit/` tree against its own `disbot/services/rank_providers.py`;
canonical-side work is superbot's own per Q-0260 (this repo writes no lane
files), so the routing is a fleet-manager sweep flag, not an idea-engine build.
NOT sim-lab: there is no evidence question — no design fork (the doc already
chose guard-over-generator and the allow-list mechanism), no parameters to
sweep, and the catch set is derivable statically by running the test; a
simulation would re-derive what one pytest run answers. NOT superbot-next:
superseded there (D-0005/D-0038). NO PROPOSAL — the honesty guard outranks
feeding sim-lab's queue (the #180/#183 precedent), and PROPOSAL 009 stays
untouched as the orthogonal settle-once head.

**8. What is the smallest shippable slice?**
At the owning lane: `tests/unit/invariants/test_rank_provider_parity.py` (or a
check_consistency.py rule) — every table with a leaderboard-worthy per-user
score column has a `RankProvider` in `_PROVIDERS` OR is on an explicit
allow-list; nearest-neighbor precedent already in that directory
(`test_world_registry_parity.py`). For THIS repo the smallest slice is exactly
this probe: state flip + the S-side parity-guard hole flagged on the heartbeat
for fleet-manager routing. Nothing else to build here.

**Recommendation: park** — the trigger event already fired (karma hand-built
the six-piece shape 2026-06-22) and no next score subsystem is queued at
superbot; the general half shipped as PR #1346 and the idea is structurally
superseded at superbot-next (D-0005 manifest gate + D-0038 test-pinned provider
registry); the remaining S-side RankProvider parity guard is a one-file
lane-side test (routed via the heartbeat's manager sweep flag, Q-0260), not a
sim evidence question — no proposal.
