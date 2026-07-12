# Session — single-pass probe: superbot-next oracle-copy punctuation-drift sweep

> **Status:** `in-progress`

## What this session did

Single-pass probe (battery v0, no panel triggers) of
`ideas/superbot-next/oracle-copy-punctuation-drift-sweep-2026-07-12.md` —
harvested 2026-07-12 from superbot-next at lane pin `80464ab` (idea-engine PR
#235): a cheap sweep comparing the rebuild's user-copy string literals against
oracle copy to catch punctuation-level drift in golden-uncovered refusal paths.

Verify-first, live: N = superbot-next HEAD `af985c1`, S (oracle) = superbot
HEAD `1ecc211` (both `git ls-remote`-resolved; N tree scanned via the standing
read-only blobless `--no-checkout` ls-tree recipe, all file contents fetched
via raw at the pinned SHAs; S read via raw only). Decisive findings: (a) the
known drift instance is STILL LIVE at N HEAD — `sb/domain/rps/tournament.py:153`
returns `"You're already registered."` where the oracle says
`"You're already registered!"` (S `disbot/views/rps/registration.py:49` and
`disbot/utils/tournaments.py:44`, both @ `1ecc211`); (b) golden-uncovered
confirmed mechanically — `parity/goldens/rps_tournament/sweep_rpsregister.json`
@ `af985c1` contains ZERO "registered" strings; (c) NO sweep/drift tool exists
at N HEAD — 23 `tools/check_*.py`, none copy/drift-shaped (`check_intent_survival`
= manifest slash-survivability, `check_verified_live` = V-5 registry gate,
headers read); (d) the capture's "search_code fragments" framing was a
seat-specific constraint — the oracle repo is publicly raw-readable at a
pinnable SHA, BUT N's own boundary doctrine ("this repo never imports the old
bot" — `tools/compute_corpus.py` header) means oracle-derived inputs arrive as
committed artifacts, which shapes the smallest slice.

Verdict: **recommendation sim-ready** (state advanced captured→probed here;
the sim-ready STATE flip is outbox-coupled by `check_ideas --outbox` and
control/ is coordinator-only for this slice, so flip + PROPOSAL append ride
the coordinator's slice together) — same family as VERDICT 012's cite-checker sweep
(deterministic corpus diff, real grammar × normalization × gating parameter
space, two real pinned corpora), and the spec questions are genuinely open:
which AST contexts count as user copy across 528 `sb/**.py` files, what match
normalization catches drift without flooding on deliberate divergences (the
disposition classes: kernel-surface-drift, xp-coins-alias, …), and red vs warn
under N's red-gating convention. Sim question named in the probe report.

Dedup swept (rg over ideas/superbot-next/ + ideas/superbot/, kit machinery
excluded): `rebuild-design-cite-checker` (sim-ready, VERDICT 012 approve —
same sweep-pattern FAMILY, different corpus + comparison; harness reuse yes,
one-tool-serves-both no — compared in probe Q7); `golden-recapture-on-bugfix`
(parked(routed) — golden freshness, adjacent not duplicate);
`parity-flip-cadence` (parked(overtaken) — golden coverage cadence, adjacent);
`rebuild-critical-review-checkers` (parked(routed) — checker backlog, no
copy-sweep item); `warn-first-checker-authoring-kit` probe (PR #230) checker
census re-used: N's 23-checker fleet confirmed sweep-less. No duplicate idea
file.

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this card's
born-red first commit carries the `ideas/superbot-next/` collision flag per
the PR #222/#225/#226/#228 workflow convention.

## Close-out

**Evidence:**

- ideas touched (2): `ideas/superbot-next/oracle-copy-punctuation-drift-sweep-2026-07-12.md`
  (state flip captured→probed + probe report v0 append; sim-ready flip is
  coordinator-side, outbox-coupled),
  `ideas/superbot-next/README.md` (index bullet re-badge, PR #192 card
  convention)
- sessions touched (1): `.sessions/2026-07-12-oracle-copy-drift-sweep-probe.md`
- code touched: none · control touched: none (dispatch boundary; READ-ONLY
  reads of `control/status.md` and `control/outbox.md` for VERDICT 012 /
  proposal-grammar context)
- git: branch `probe/oracle-copy-drift-sweep` off main `d68ac2d`, born-red
  card first commit, probe+close-out commit follows; draft PR flipped ready
  on green per dispatch instructions.
- verify: `python3 bootstrap.py check --strict` and
  `python3 scripts/preflight.py` run before every push.

**Judgment (the half only the session knows):**

- Decisions made: no D-entry — probe verdict only (recommendation
  sim-ready, state probed pending the coordinator's outbox-coupled flip). One
  evidence-over-claim call, declared: the capture frames the oracle side as
  "search_code fragments" because the SOURCE seat had direct oracle reads
  denied; this probe verified the denial is seat-specific (raw reads at
  `1ecc211` succeeded) AND that N's committed-artifact boundary doctrine
  makes the fetch-vs-snapshot question a spec input, not a wall — the probe
  report carries the corrected framing rather than the capture's.
- Next session should know: the outbox PROPOSAL for this head is
  coordinator-side (control/ is coordinator-only for this slice) — the
  paste-ready proposal body sits at the end of the probe report's verdict
  paragraph (question + done-when). The sim harness precedent is sim-lab
  `sims/verdict-012-doc-cite-checker-spec/cite_checker_sweep.py` (pinned
  corpora fetch-on-run, labeled cells, per-variant TC/FP) — reuse the
  harness shape, not the grammar.

## 💡 Session idea

A capture that inherits its SOURCE seat's access constraints as if they were
facts of the world ("oracle reachable only via search_code fragments") will
mis-price every design that depends on the access path. Cheap fix at harvest
time: when a source card names a DENIED capability, badge it as
seat-scoped-until-reverified — one probe-side `ls-remote`/raw attempt
(CAPABILITIES discovery rule) either confirms the wall or, as here, dissolves
it and changes the smallest shippable slice.

## ⟲ Previous-session review

PR #230 (warn-first-checker-authoring-kit probe): adopted wholesale — (a)
live-HEAD-first discipline (N moved `80464ab`→`af985c1` since harvest; the
still-live drift instance and still-absent sweep tool are the probe's
premise); (b) the born-red-card collision flag under the dispatch boundary
used verbatim; (c) its checker census (N: 23 `tools/check_*.py`) consumed
directly instead of re-derived. Improvement carried: #230's card noted the
stop-hook auto-draft diffs against the wrong base — this card was
hand-written from the first commit and the auto-drafted `2026-07-12-session.md`
stray was left uncommitted.

- **📊 Model:** worker slice · single-pass battery (no panel triggers) ·
  docs-only probe (one probe append + state flip + index re-badge + card;
  no code)

## Handoff → next wake

Coordinator: this head's recommendation is sim-ready — BOTH the
probed→sim-ready state flip AND the outbox PROPOSAL append are yours
(control/ boundary; `check_ideas --outbox` couples them, so do both in one
slice). Question + done-when are paste-ready in the probe
report's verdict. The idea's grounding pins to carry into the proposal:
superbot-next @ `af985c17def5ff2478103cb363ebb150cb583a97`, superbot (oracle)
@ `1ecc21138fe0a1eb672d03b66bd319164c29d55f`.
