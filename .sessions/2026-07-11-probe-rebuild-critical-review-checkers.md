# Session — TOP-5 item 3 probe (rebuild-critical-review-checkers)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~19:20Z (worker slice, coordinator-dispatched
> under continuous-chaining mode per Q-0265)

## Scope

Probe TOP-5 item 3 (`ideas/superbot/rebuild-critical-review-checkers-2026-07-10.md`
— mechanize the critical-review rubric's checkable classes, the "enforce, don't
exhort" arm of Q-0233's ten-class review lens). Section claim rode fast-lane FIRST
as PR #207 `becbf39` (`control/claims/probe-rebuild-critical-review-checkers.md`;
claims dir re-read at branch time — the two live venture-lab claims #208/#209 are
disjoint sections, no collision; this claim file deleted in this PR). Branch
`probe/rebuild-critical-review-checkers`.

## What this session did

**Full battery probe (single-pass)** on the checker backlog. Verdict, exact line
on the file: `**Recommendation: park** — routed (superbot lane build: the class-4
staleness-extension one-file slice; …)`. State flipped `captured` →
`parked(routed — superbot lane build: the class-4 un-anchored-NN% staleness-extension
one-file slice; …; probe 2026-07-11)`, index re-badged with the built-half/open-half
split (the PR #189 badge duty). **NO outbox proposal** (park verdict; nothing has a
parameter space or corpus for sim-lab — outbox tail stays PROPOSAL 009).

The probe's verify-first, read at invocation sites not doc claims, per rubric class
at N HEAD:

- Classes 11/12/13 BUILT + CI-WIRED (D-0014 mechanics, D-0033 lens adoption;
  `tools/check_cost_posture.py`, `check_metric_cardinality.py`,
  `check_data_lifecycle.py`, `check_egress.py`; red-gating in
  `.github/workflows/ci.yml:50-56` — an 18-checker fleet, 22 `tools/check_*.py`
  on disk). Class 10 built by construction (`check_namespace.py` +
  `check_symbol_shadowing.py`). Class 8 mechanized STRONGER than the ask
  (`check_verified_live.py` V-5 signed registry + parity door). Class 9's nav
  golden exists (`tests/unit/navigation_golden/test_navigation_completeness.py`,
  the D-0020 A-3 golden — residual half stays the separate TOP-5 exclusion).
- The audit-coverage AST addendum substantially closed: `check_egress.py` is a
  real `ast` fence A-5-widened to raw Discord state mutations (the canonical
  doc's "PENDING (RC-21/Q-D26)" is STALE); `check_atomic_db_only`
  (`sb/kernel/workflow/compile.py:118`) scans every armed DB-leg handler's
  source for banned I/O.
- Classes 1/3/5 NOT built and CARRIER-LESS — `SubsystemManifest`
  (`sb/spec/manifest.py:23-33`) declares no `depends_on`/risk field; class 1's
  premise mooted (build order fully executed, rebuild in band live-testing).
  Classes 2/6/7 human by design. Lens self-application fenced by Q-0233
  ("never self-applied" — the rubric-v2 doc header verbatim).
- Class 4 = the ONE unbuilt named-now slice: superbot
  `scripts/check_plan_staleness.py` @ S HEAD carries only its three original
  rules (127 lines, warn-first) — NO un-anchored-`NN%` rule. Routed as the park.

**Honesty corrections on the file:** the TOP-5 framing "enforcement still manual"
is OVERBROAD (mechanized-class enforcement is CI-wired red at N; what stays manual
is the review PASS — deliberately — and the un-mechanized classes); the canonical
doc's audit-coverage addendum understates N (state-mutation fence live, not
pending); the rebuild-arm checker list is two-thirds consumed.

## Probe evidence (pins on the idea file)

- S = superbot `050ba69` (`050ba693d507af5b74a8d7348c7c6b612a8b6ad7`, ls-remote
  pin + raw per-file reads) and N = superbot-next `81b04bc`
  (`81b04bcbbf80dedac0fa26a9295138cea092f513`, blobless-clone HEAD,
  ls-remote-confirmed). Canonical idea doc byte-identical at S HEAD vs the
  `fd638e3` harvest pin (md5 match).
- Read at N: `docs/decisions.md` D-0014/D-0033 in full + the D-tail through
  D-0074 (rubric grep: 6 hits, all D-0014/D-0033-adjacent — no newer review-
  checker decision); `docs/planning/rubric-v2-classes-11-12-13.md` (header
  `binding — ADOPTED`); `tools/` inventory + `check_egress.py` body +
  `check_atomic_db_only` body + `check_symbol_shadowing.py`/`check_verified_live.py`
  docstrings; `.github/workflows/ci.yml` checker loop; `sb/spec/manifest.py` +
  `sb/spec/settings.py:147`; `control/inbox.md` ORDERs 001–010 (no order touches
  review checkers).
- Read at S (raw @ `050ba69`): `scripts/check_plan_staleness.py` full body;
  `docs/planning/rebuild-critical-review-rubric-2026-07-03.md` (ten classes +
  mechanization roadmap); the canonical idea doc.
- Panel not escalated: process head, reversible park, no security/data/spend/
  public surface (README battery panel rule).

## Verification

`python3 bootstrap.py check --strict` green on the final tree immediately before
push (heartbeat rides the follow-up PR per the arm-at-open race recipe, so this
slice's tree is final at push). Claim PR #207 merged on green via the armed
auto-merge enabler (opened 19:08:13Z, merged 19:08:25Z — arm-at-open working as
wired). PR number stamped post-open per the never-guess rule (the
#181/#184/#187/#190/#193/#195/#198/#201 follow-up recipe).

**📊 Model:** fable-5 · one idea-file probe append + state flip + one index
re-badge + card + claim clear (+ follow-up heartbeat); no code, no outbox append,
no lane-file writes (Q-0260)

## 💡 Session idea

**`git ls-remote <url> main` is the cheapest SHA pin and it is not in the
capability ledger.** This probe pinned BOTH lanes' HEADs in one round-trip each
with zero clone cost (`ls-remote` worked through the proxy for both repos), and
cross-confirmed the blobless clone. The commits/main.atom recipe (still un-promoted
from the #200 card's 💡) FAILED this session for superbot ("GitHub access to this
repository is not enabled for this session" — github.com HTML/atom surface is
session-gated where git-protocol and raw.githubusercontent.com are not). Ledger
candidates for `docs/CAPABILITIES.md`: (a) ls-remote = verified SHA-pin route,
(b) the atom feed is NOT reliable from a worker seat — supersede the #200
suggestion with this stronger datapoint.

## ⟲ Previous-session review

Reviewed card (per dispatch): `.sessions/2026-07-11-wire-automerge-enabler.md`
(the enabler-wiring slice; note the factually newest card at branch time is
`2026-07-11-probe-leaderboard-row-avatars.md` — spot-checked too, no corrections).
The enabler card's claims verified against reality, ~18 h and ~150 PRs later:
(1) its core promise — "every matching-prefix READY PR self-arms at open and
merges when substrate-gate goes green" — held LIVE on this very slice's claim
PR #207 (opened 19:08:13Z, auto-merged 19:08:25Z, `merged_by` the enabler's arm);
(2) its 13-pattern `branch_patterns` set survives at `substrate.config.json`
(probe/* rode it here); (3) its predicted failure mode became a real recurring
class — the arm-at-open squash exiling later commits — confirmed by the #62/#64/
#80 instances in the Self-review section and fixed by PR #86's race guard, and
this slice PLANS for it (heartbeat rides a follow-up PR by design, the #198/#201
recipe); (4) its gate-clobber vigilance aged well — the PR #36 tripwire caught
clobbers a fourth and fifth time at #120/#125 (Self-review, cited). One honest
delta: the card's 💡 (branch-prefix drift tripwire) is STILL-OPEN grooming — no
`scripts/preflight.py` check compares merged-branch prefixes against
`automerge.branch_patterns` at this wake; flagged rather than silently dropped.

## Handoff → next wake

- Inbox first, as always (read FIRST this session at wake HEAD `37d2592`: ORDER
  001/002 only, nothing beyond 002). TOP-5 item 3 is CONSUMED (parked/routed this
  slice). **Ripest next: TOP-5 item 4**
  (`rebuild-design-cite-checker-2026-07-10.md` — zero cite validation at N; the
  LAST open TOP-5 head) — then the slice after re-ranks (the #204 card's 💡 names
  the grooming inputs: the 4 websites heads, fired mint-time-exclusion triggers).
- Manager sweep flag added by this slice (heartbeat notes): critical-review-
  checkers routing (ORDER-worthy — superbot lane build, one warn-first file
  slice: rule 4 in `scripts/check_plan_staleness.py`, the un-anchored-`NN%`/
  "complete" rule with the Q-0105 delete-if-noisy header; evidence pins
  S=`050ba69` / N=`81b04bc`).
- PROPOSAL 009 verdict fan-in when sim-lab finalizes (outbox tail stays 009;
  two venture-lab claims #208/#209 in flight may append 010/011 — reconcile
  numbering at their merge, not here).
- Standing watches otherwise unchanged (golden-recapture + release-testing +
  leaderboard-avatars routing, map-before-faucets, RankProvider parity-guard,
  Rule 6, adoption-record sweep, contract-shape attach, effect-arming
  third-dependent; theme-schema half-fired; superbot-idle V006 guardrails).
- Friction for the ledger: local main had diverged at wake with the SAME stray
  pre-force-push seed commit `df64aab` as last slice — backed up
  (`backup/stray-main-2026-07-11-probe`) and realigned via `git reset --keep`;
  github.com atom feed refused for superbot from this seat (verbatim error in 💡
  above) — `git ls-remote` + raw reads covered everything; otherwise clean.
