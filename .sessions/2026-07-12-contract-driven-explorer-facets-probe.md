# Session — single-pass probe: websites contract-driven-explorer-facets

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-12 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Single-pass probe (battery v0, no panel triggers) of
`ideas/websites/contract-driven-explorer-facets-2026-07-10.md` — the PROPOSAL 002
probe-Q4 fork made a capture: the phase-2 game-data explorer derives its browse
facets, table columns, and search fields from the versioned contract file itself
(fail-closed on unknown schema version), so each newly contracted family appears
with ZERO websites diff.

Verify-first, live (2026-07-12T00:31–00:33Z): superbot
`dashboard/data/dashboard_data_contract.json` fetched at live HEAD `1ecc211`
(ls-remote same fetch) — the version-1 contract is a THIN envelope: family list
+ per-family GUARANTEED FIELD-NAME lists (`"bug": ["id","title","status",
"summary"]`), NO types, NO facetable-dimension metadata, only `meta`+`bugs`
contracted. So columns+search are generatable from the v1 name lists TODAY;
facets need the contract format to grow field/type/facet metadata — superbot
work riding the fm ORDER 012/013 fan-in (the pinned-feed-contract head already
carries that seam). Websites `dashboard/data_source.py` at live HEAD `8f97654`
(byte-identical to the SHA PR #222's probe fully scanned): fail-closed
honest-unavailable doctrine live, nothing explorer-shaped in the tree, phase-2
explorer UNROUTED — the first-commit window this capture was filed to catch is
STILL OPEN.

Verdict: **parked(build-direct — first-commit design constraint on P002
phase-2)**, Sequence-pinned `before websites builds P002 phase-2 explorer UI #1`.
No sim question (deriving UI from a JSON contract is deterministic —
judgment/routing only, the PR #222 precedent). Best implementation found: the Q8
fold-in for the phase-2 explorer ORDER — generate columns+search from the live
v1 name lists now, extend the contract format with per-family field/type/facet
metadata (fm ORDER 012/013 fan-in) before or alongside facets, fail-closed on
version mismatch, zero-diff family landing proven by a fixture test. The
coordinator's re-rank alternative (park blocked-on-012/013) was weighed and
declined on this evidence: phase 2 can route any day without 012/013 (VERDICT
003), and the constraint must already be riding that ORDER when it does.

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; the born-red first
commit of this card carried the flag per the PR #222 workflow improvement.

Files touched: the idea file (state flip + Sequence line + probe report append),
`ideas/websites/README.md` (index bullet echo), this card.

## Close-out (auto-drafted 2026-07-12 — edit, don't author)

<!-- substrate:auto-draft -->

**Evidence (auto-collected — verify, then keep or correct; corrected: the
auto-draft listed `.sessions/2026-07-12-session.md` as touched — that card is
the coordinator's, untracked, NOT touched by this slice):**

- ideas touched (2): `ideas/websites/contract-driven-explorer-facets-2026-07-10.md`
  (state flip + Sequence pin + probe report append), `ideas/websites/README.md`
  (index echo)
- sessions touched (1): `.sessions/2026-07-12-contract-driven-explorer-facets-probe.md`
- code touched: none · control touched: none (dispatch boundary)
- git: branch `probe/contract-driven-explorer-facets` off main `5e50274`,
  born-red card first commit `4a26fe6`, probe+close-out commit follows; PR #225
  (draft, flipped ready on green).
- verify: `python3 bootstrap.py check --strict` → green for this slice's files;
  the one local HOLD is the coordinator's own untracked in-progress
  `2026-07-12-session.md` (designed hold, not this branch's — CI never sees the
  untracked file). `python3 scripts/preflight.py` → all 10 checks green.

**Judgment (the half only the session knows — resolve every slot):**

- Decisions made: no D-entry — probe verdict only (park, build-direct,
  first-commit design constraint, Sequence-pinned). One evidence-over-analysis
  call, declared: the coordinator's parallel re-rank suggested
  park(blocked-on-feed-contract-routing); the live contract fetch showed partial
  sufficiency (names yes, types/facets no), so the fold-into-phase-2-ORDER
  flavor won, with the format growth named as a dependency of FULL generation
  only.
- Next session should know: the phase-2 explorer ORDER is the constraint's only
  carrier — when the manager routes PROPOSAL 002 phase 2, the Q8 fold-in line
  must ride it (and if fm ORDER 012/013 routes first instead, the
  contract-format metadata growth can attach THERE via the
  pinned-feed-contract relay). Both parents verified unrouted at this session's
  pins.

## 💡 Session idea

A contract file that guarantees field NAMES but not types/facets sits in an
uncanny middle: consumers can generate SOME UI from it, which makes hand-building
the rest feel cheap — and that is exactly how the two-lane per-family cost
sneaks back in. Contract-format design should decide "what can a consumer
GENERATE from this?" as an explicit version-1 question, not let generability be
an accident of which keys happen to exist.

## ⟲ Previous-session review

PR #222 (fleet-program-pulse-feed probe): its two exports were adopted wholesale
here and both paid off — (a) verify-first at live lane HEAD (the contract fetch
was this probe's decisive fact; the analysis-only view had it "blocked"), and
(b) declare the section-collision risk in the born-red card's first commit when
the dispatch boundary forbids a claim file. Workflow improvement to carry
forward: when two sibling captures watch the SAME first-commit window from
different phases (pulse-feed = phase 1, this = phase 2), their Sequence pins
should name each other — done here via Q7's same-shape-different-phase dedup
line, so whichever ORDER routes first surfaces both riders.

- **📊 Model:** fable-5 · single-pass battery (no panel triggers) · docs-only
  probe slice (one probe append + state flip + Sequence pin + index echo + card;
  no code)

## Handoff → next wake

The fold-in instruction (probe report Q8) is the whole deliverable — a
coordinator heartbeat line pointing the manager at it when PROPOSAL 002 phase 2
routes would strengthen it (this slice could not write one). Ripest related
follow-up when the contract format grows: `public-leaderboards-committed-feed`
(parked(routed)) becomes the first zero-diff arrival test case.
