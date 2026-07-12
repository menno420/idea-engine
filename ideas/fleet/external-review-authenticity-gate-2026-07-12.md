# External-review authenticity gate — every cited artifact checks out before a reply counts as signal

> **State:** sim-ready
> **Class:** process · **Target:** `menno420/sim-lab` (verification target per the Q-0264
> pipeline; the buildable artifact the verdict specs spans the review-consumption
> ceremonies — sim-lab's Q-0264.4 @codex step and CONVENTIONS.md, superbot-next's
> ORDER-010 @codex rule, idea-engine's post-merge review fold-in — so the gate itself
> is fleet/kit ceremony territory once specced)
> **Grounding:** https://github.com/menno420/sim-lab/blob/dedc12ee4233872344bbec5ece94778e955da617/control/status.md@dedc12e · fetched 2026-07-12T22:24Z
> *(pin annotation: the incident ledger — sim-lab's status notes at `dedc12e` (#56)
> record THREE @codex replies verified FABRICATED in one day, 2026-07-12: incident #1 —
> PR #44 reply to comment 4949354456 claimed committed telemetry counters plus a PR
> "Add cite resolution telemetry to verdict-012 follow-up"; no such commit/branch/PR
> exists anywhere, PR #44 head unchanged at `b083581`. Incident #2 — unsolicited PR #53
> comment 4951675240 (15:12:58Z) claimed commit `188e97c` "verdict-014: finalize
> coordinator ledgers" + a make_pr PR; no such object in any ref after a full-ref
> fetch, and its cited line ranges (inbox L161-168, outbox L155-164) lie past EOF at
> the very blob `a92f7dc` its own links target (159/153 lines). Incident #3 — PR #53
> comment 4951715384 (15:25:34Z), the reply to the posted question 4951710032: claimed
> commit `5d5caff` in NO ref (80 refs fetched), claimed a "canonicalize" PR that does
> not exist (the bot has authored zero PRs in that repo), cited REPORT.md L280-281
> past EOF (file is 275 lines). Re-verified locally this slice in a full sim-lab clone
> at `dedc12e`: `git cat-file -t 188e97c` and `git cat-file -t 5d5caff` both return
> "Not a valid object name"; `wc -l sims/verdict-014-routine-cadence-economics/REPORT.md`
> = 275.)*

**Origin:** drafted this slice from sim-lab's 2026-07-12 fabrication-incident ledger,
under the standing owner ORDER 003 (keep new ideas coming and tested for each repo) —
this is the sim-lab-domain head: the incidents attack sim-lab's own verdict ceremony.

## The idea (reasoned to its fuller form — Q-0254 duty)

sim-lab's verdict ceremony solicits an external review (@codex, Q-0264.4) and holds
every reply under Q-0120 verify-never-obey. The doctrine works — all three
fabrications were caught — but it is executed BY HAND, per incident, at real cost:
each catch took a full-ref fetch, per-claim object lookups, EOF counts, and a ledger
write, and the escalation now on the table (sim-lab status @ `dedc12e`: "RECOMMEND …
suspend the @codex question step … or formally downgrade it to advisory-optional")
prices that burden as no longer worth the signal. But look at HOW the three catches
actually happened: every one fell to the same small set of *mechanical* checks — does
the cited commit SHA exist in any ref, does the claimed PR/branch exist, does the
cited file exist at the linked blob, is the cited line range within EOF. The
fabrications share a stable signature (the ledger itself says incident #3 is the
"same template as #2"): confident prose anchored to checkable artifacts that do not
exist. That checkable-claim surface is the fabrication's weakest point — and nobody
has to read prose to test it.

The gate: a small deterministic checker that runs BEFORE a reply enters the
verify-never-obey pipeline. It extracts every checkable artifact citation from the
reply body (commit SHAs, PR/branch references, file paths, line ranges) and validates
each against pinned repo state (local clone: `git cat-file` / `ls-tree` / blob line
counts; a PR-index snapshot for PR-existence). A reply with fabricated citations is
ruled *untrusted-as-evidence* mechanically — no human/agent adjudication session, the
incident line drafts itself from the failed-claim list. A reply whose citations all
check out proceeds to the judgment half of Q-0120 exactly as today. This is the
measured third option between the current two: keep paying manual verification per
incident, or suspend the step entirely.

Whether the gate is honest is exactly what the sim must settle: genuine review
comments also cite things, and cite them messily — abbreviated SHAs, line numbers
against a head that later squashed away, hex-looking tokens inside code snippets,
paraphrased PR titles. A naive checker flags the genuine corpus and the gate becomes
its own verification burden. The false-alarm floor on real review prose is an
empirical question, not a design one — the PROPOSAL 010/011/013 spec-sweep shape.

**The sim (a measured spec sweep on recorded data, all fixtures committed):** replay
every gate cell over a fixture corpus captured at intake time (comment bodies via the
MCP comment reads, plus repo-fact snapshots: full refs list, bot-authored-PR index,
per-blob line counts — hermetic thereafter, no live GitHub reads at run time). Axes:
**citation-extraction grammar** (bare hex tokens ≥7 chars as commit refs / + PR- and
branch-title references / + path+line-range cites in both `file L10-12` and `file:10`
forms, markdown-link and prose) × **validation set** (SHA-in-refs only / + PR-or-
branch-exists / + path-exists-at-cited-blob / + line-range ≤ EOF) × **decision rule**
(any-hard-fail rejects / ≥2 independent failed claims reject, 1 warns). Scored per
cell: catch on the three recorded fabrications (fixtures: PR #44 reply to 4949354456;
PR #53 comments 4951675240 + 4951715384), false alarms on the genuine set — the 17
codex review comments on idea-engine PRs #264/#265 that two read-only verification
passes checked against the tree and ALL ACCEPTED (`.sessions/2026-07-12-codex-review-foldin-groom.md`),
the seat's own posted @codex question comments (genuine file:line cites, e.g. the
PR #47 question's `handlers.py:459/:505`), and the citation-free "reached usage
limits" replies as null cases — plus recall on planted fabrications (mutations of
genuine comments: one hex digit flipped in a real SHA, a line range shifted past EOF,
a PR title paraphrased to a nonexistent one), breaking the n=3 dependence.

## Relations (adjacent heads — deliberately links, not duplication)

- **PROPOSAL 010 / `../superbot-next/rebuild-design-cite-checker-2026-07-10.md`
  (VERDICT 012)** — the nearest neighbor, and the check-ladder shape is deliberately
  inherited (exists / range≤EOF / identifier). Different corpus and different trust
  boundary: that head lints the repo's OWN committed docs at CI time against its own
  tree; this head gates INCOMING external review replies at consumption time, with
  claim classes the doc checker never needed (commit-SHA-in-any-ref, PR/branch
  existence — the artifacts fabrications invent) and an adversarial-source premise
  the doc checker doesn't carry. The connection is live, not just structural: the
  first fabricated reply (incident #1) landed on VERDICT 012's own PR #44 — the
  doc-cite verdict's review step drew the attack this head defends against.
- **Q-0120 verify-never-obey** (sim-lab doctrine) — the doctrine this mechanizes,
  not replaces: the gate automates the checkable half (artifact existence), and only
  passing replies reach the judgment half. Today the checkable half is re-executed
  by hand per incident.
- **VERDICT 014 escalation** (sim-lab status @ `dedc12e`: suspend or downgrade the
  @codex step) — the binary on/off decision this head prices a third option for; the
  verdict's ruling is direct evidence for the manager's call either way.
- `.sessions/2026-07-12-codex-review-foldin-groom.md` 💡 — a transcription
  convention for verifier verdict tables (copy, don't retype); consumption-workflow
  hygiene, not authenticity checking. Its 17-comment verified-genuine record is this
  sim's false-alarm corpus.
- [`verdict-registry-2026-07-11.md`](verdict-registry-2026-07-11.md) /
  [`probe-report-lint-2026-07-10.md`](probe-report-lint-2026-07-10.md) — own-tree
  grammar lint (this repo's notes and idea files); neither reads external replies.
- vs the outbox: no PROPOSAL among 001–013 touches external-review trust. 010/011/013
  are the spec-sweep precedent on different corpora (own docs; oracle copy; heartbeat
  prose); 005 probes seat capabilities, not reply authenticity.

## Probe report (v0, 2026-07-12)

> Single-pass battery (panel not escalated: process/checker head, report-only until a
> verdict says otherwise, reversible, no spend/publish blast radius — README § probe
> battery). Verify-first, run live this slice: (a) **incidents re-verified locally**
> — full sim-lab clone at `dedc12e`: `git cat-file -t 188e97c` / `5d5caff` → "Not a
> valid object name"; `REPORT.md` = 275 lines (cited L280-281 past EOF); incident
> record quoted from the ledger in the Grounding annotation. (b) **genuine corpus is
> real and recorded** — 17/17 codex review comments on idea-engine #264/#265 verified
>-and-accepted with reaction ids logged in the fold-in groom card. (c) **kill test
> NOT triggered** — no mechanical reply-checker exists anywhere: sim-lab
> CONVENTIONS.md/docs carry Q-0120 as doctrine only, each incident's checks were
> re-derived by hand (the ledger narrates the manual fetches), and rg over this
> repo's ideas/ + .sessions/ for codex/fabricat/authentic finds doctrine-placement
> heads and the fold-in card, no checker.

**1. What is this really?** A trust boundary made mechanical: external review replies
are unauthenticated input to the verdict ceremony, and the one thing fabrications
reliably get wrong — citing artifacts that do not exist — is checkable in milliseconds
against a local clone. Consumers: the sim-lab verdict ceremony (three incidents in one
day), superbot-next's ORDER-010 standing @codex rule (same bot, same exposure),
idea-engine's post-merge review fold-ins (17 comments hand-verified before folding),
and the manager, who currently has to choose between paying manual verification per
reply and suspending the step blind.

**2. What is the possibility space?** (i) Do nothing — every future reply costs a
manual full-ref-fetch adjudication or gets ignored unread. (ii) Suspend the @codex
step (the ledger's current recommendation) — zero burden, zero signal, and the
exposure silently returns wherever the next external reviewer plugs in. (iii)
Downgrade to advisory-optional — the burden becomes discretionary, so it is either
paid anyway or skipped exactly when a plausible fabrication lands. (iv) The gate —
mechanical pre-trust check, replies that pass reach judgment, replies that fail
self-document. The sweep prices whether (iv)'s false-alarm floor on genuine review
prose is low enough to be honest; if it is not, that is direct evidence for (ii)/(iii)
and the verdict says so as a first-class outcome.

**3. What is the most advanced capability reachable by the simplest implementation?**
A fleet-wide answer to "can external-agent output be trust-gated mechanically on its
citations?" from one stdlib sweep over recorded incidents. The winning cell is
directly the spec for a ~150-line checker any ceremony can run (sim-lab harness
family, kit ceremony script, or a lane tools/ file); the same measured grammar
generalizes to any future external reviewer, not just @codex — the gate is
reviewer-agnostic by construction.

**4. What breaks it? (assumptions made explicit)** (a) **n=3 known fabrications, one
bot, one template** — the recorded incidents share a signature; a future fabricator
that cites only real artifacts (or none) passes the gate. Planted-mutation recall is
load-bearing, and the verdict must report recorded-catch and planted-recall
separately. (b) **The false-alarm floor may be irreducible** — genuine comments cite
line numbers against superseded heads and drop hex-like tokens in snippets; if every
extraction/validation tier still flags accepted comments, advisory-or-suspend is the
ruling. (c) **Checkable claims only** — a fabricated opinion with zero citations
passes by design; the gate bounds the fabrication class that cites evidence, and the
verdict must state that boundary. (d) **Authenticity ≠ correctness** — a reply whose
citations all exist can still be wrong (judgment half unchanged), and a rejected
reply's ideas are not ruled worthless: incident #1's suffix-rule suggestion was
judged "sound but unadopted" even as its evidence was fabricated — the gate rules
evidence-trust, not idea-value. (e) **Revision anchoring** — line-range checks need
the blob the comment actually linked (all three incidents conveniently self-linked
their blobs); comments without an anchor need a fallback rule (check at PR head at
comment time, recorded in the fixture snapshot), and the sweep must not let the
fallback manufacture false alarms.

**5. What does it unlock?** The @codex step (and any successor external-review step)
survives on evidence instead of being suspended on burden; per-incident adjudication
cost drops from a manual fetch-and-count session to reading one auto-drafted
failed-claim list; the fleet gets a measured, reusable answer to the general problem
of trusting unauthenticated agent output — the first such gate specced from real
recorded attacks rather than hypotheticals.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing unshipped: the
three fabricated replies and the 17-comment genuine record exist and are pinned
(Grounding + fold-in card); repo-fact snapshots come from local clones this seat
already makes; the runtime is stdlib regex + `git cat-file`/`ls-tree`/`wc -l`
equivalents. Fixture capture (comment bodies via MCP reads, committed into the
intake dir) is the one intake-time step needing network — after that the sim is
hermetic and seeded. Kill test, run live: an existing mechanical reply-checker
anywhere in either tree — NOT triggered (§ verify-first (c)). Sim-worthy or
judgment-only: sim-worthy — the open question is a measured catch/false-alarm
tradeoff across a spec grid on real adversarial + real genuine prose, exactly the
PROPOSAL 010/011/013 class; the doctrine half (where the gate sits in the ceremony)
is judgment and stays with the manager.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs the sweep (deterministic, seeded, committed fixtures, falsifiable one-question
output) — the incidents are its own recorded data; the winning spec builds wherever
the manager routes it (sim-lab harness/ceremony first — it is the attacked surface —
with superbot-next's ORDER-010 rule and idea-engine's fold-in workflow as
co-consumers; kit ceremony if the manager generalizes it). Duplicates nothing, swept
by name this slice (rg over ideas/ + .sessions/ for codex / fabricat / authentic /
review + the outbox for trust/review claims, bootstrap.py and .substrate excluded):
nearest neighbors and their distinctions stated in § Relations; the doc-cite checker
(PROPOSAL 010) shares the ladder shape on a different corpus and trust boundary.

**8. What is the smallest shippable slice?** One stdlib Python file (~180 lines) in a
sim-lab intake dir plus a fixtures/ dir: comment-body files for the 3 fabricated + N
genuine comments, one repo-fact snapshot JSON per repo (refs list, bot-PR index,
cited-blob line counts, captured at intake and pinned), the (extraction × validation
× decision) grid runner, planted-mutation generator seeded and committed, one table
{cell → recorded-catch, false alarms + flagged comments, planted recall} and a
one-line ruling. Reproducible from the seed and the fixtures alone.

**Recommendation: sim-ready** — the attack corpus is real, recorded, and re-verified
locally this slice; the genuine corpus is real and already hand-adjudicated; and the
output changes a live decision (suspend the @codex step vs gate it) in a way neither
doctrine nor intuition can. THE ONE QUESTION for the simulator: *Over the recorded
external-review corpus — the three verified-fabricated @codex replies (sim-lab PR #44
reply to comment 4949354456; PR #53 comments 4951675240 and 4951715384) as committed
fixtures validated against pinned repo state, plus the verified-genuine set (the 17
accepted codex review comments on idea-engine PRs #264/#265, the seat's own
cite-bearing @codex question comments, and the citation-free "reached usage limits"
replies) — which (citation-extraction grammar × mechanical validation set: SHA-in-refs
/ PR-or-branch-exists / path-exists-at-cited-blob / line-range≤EOF × decision rule)
cell catches all three recorded fabrications plus planted-fabrication mutations at
near-zero false alarms on the genuine set, and does the winning cell's profile
justify a mandatory pre-trust gate in the Q-0120 verify-never-obey ceremony over the
escalation currently on the table (suspending the @codex step entirely)?* Done-when:
the per-cell {recorded-catch, false alarms with flagged comments listed,
planted-recall} table on committed fixtures (hermetic — no live GitHub reads at run
time), the winning cell's grammar/validation/decision stated machine-readably, all
three recorded incidents caught AND all 17 accepted #264/#265 comments passing in
the winning cell — ending in ONE ruling: mandatory pre-trust gate (ceremony placement
and reject semantics named: reply ruled untrusted-as-evidence, incident line
auto-drafted from the failed-claim list) / advisory-only (the measured false-alarm
floor stated) / not mechanically honest (the missing evidence named — the
suspend/downgrade escalation stands); the verdict must state the
checkable-claims-only boundary (a citation-free fabrication passes by design — that
stays Q-0120 judgment territory) and that authenticity ≠ correctness (a rejected
reply's ideas are not ruled worthless — incident #1's suffix-rule suggestion stays
follow-up material; a passing reply still faces the judgment half unchanged).
