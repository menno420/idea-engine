# Session — docs slice: contract grooming round 2 (💡 harvest of the PR #8–#17 era encoded)

> **Status:** `in-progress`
> **Model/time:** 2026-07-10 ~21:5xZ (worker slice, dispatched by the coordinator under
> continuous-chaining mode per Q-0265; fifteenth slice of the repo)

## What this session did

Harvested every session card of the PR #8–#17 era (all 16 cards re-read, seed included,
to be safe on era boundaries) for contract-level 💡s, deviations, and friction, then
encoded the worthwhile ones as minimal in-place amendments to the three contract docs —
grooming to match practice, not a redesign (PR #6 shape). No claim: root contract docs
are not a section (`claims/README.md` scope, PR #6 precedent). No outbox entry —
Q-0265 backpressure holds (depth 3, zero sim-lab pulls); this slice is
non-proposal-generating by design.

**Encoded — each 💡/lesson → its amendment (all one-sentence-or-bullet, in place):**

1. **Grounding-pin line** (`> **Grounding:** <url>@<sha> · fetched <time>`) — PR #8
   card 💡, re-shaped by the #10/#12/#14/#15/#17 cards (five hand-rolled instances) →
   README § Idea file grammar, new optional-lines paragraph.
2. **Sequence line** (`> **Sequence:** <before|after|behind> <event/order/claim>`) —
   PR #10 card 💡, re-evidenced by #12 ("every capture sequenced before band-6") →
   same README paragraph.
3. **Manifest-staleness flag** (`(manifest row: behind|matches|ahead)` on the pin) —
   PR #14 card 💡 (lane pin `ce22315` was AHEAD of the row's `af11bdb` note and it
   reshaped two captures) → folded into the grounding-pin sentence, same paragraph.
4. **DARK-lane grounding recipe** — PR #15 card 💡 (private lane, blackout verified
   three ways, captures scoped shape-not-content) → same README paragraph, one
   sentence.
5. **Cross-links subsection shape** — PR #17 card 💡 (sibling-section dedup for the
   Lumen Drift itch.io capture) → README § Idea file grammar, one sentence extending
   the harvest-by-link rule.
6. **Arm auto-merge only once the branch is FINAL** — the PR #2/#3 lesson (~16s merge
   loop out-races later commits), recorded in the PR #6 card and practiced by every
   card since → README § Landing conventions, one sentence appended to the
   lands-its-own-PRs bullet.
7. **Sibling-conflict forward-only recipe** — practiced across PRs #10–#17 (e.g. the
   #16 card's two mid-flight merges, the #17 card's reconciled heartbeat) but written
   down nowhere → README § Landing conventions, one new bullet (merge origin/main,
   never rebase; reconcile the heartbeat keeping both sides' facts; rerun preflight;
   push again).
8. **Never pre-write a PR number; stamp real wall-clock time** — commit `7ce1607`
   ("heartbeat fixup: PR number is #12 (created as #12, heartbeat predicted #11)")
   plus the PR #15 card §⟲ (the prior heartbeat's `updated:` was ahead of wall-clock,
   breaking the manager's staleness math) → `control/README.md` § status.md format,
   one sentence after the format block.
9. **Claim-filename flattening** (`/` → `-`) — PR #1 card §⟲ guard recipe, consumed
   by every claim since #2 but never written into the convention it patches →
   `claims/README.md`, one sentence.

**Skipped — judged not worth encoding here (with reasons):**

- **Contract-amendment "consumed flags" ledger** (PR #6 card 💡) — natural home is
  `.sessions/README.md`, not a contract doc; the convention self-applies (this card
  names its consumed flags, as #6's did); follow-up one-liner if it recurs again.
- **Gate↔ritual convergence** (PR #16 card 💡) — a build slice touching
  `.github/workflows/substrate-gate.yml`, which a sibling session is editing this
  window; standing candidate, untouched here.
- **Harvest freshness checker** (PR #7 card 💡) — a script build slice, not contract
  prose; remains a standing non-proposal candidate.
- **Earn-rate budget doc** (PR #9 card 💡) — a superbot-targeted capture candidate
  for a future generate slice, not this repo's contract.
- **Blobless-clone history recipe** (PR #17 card §⟲) — operational fetch tactic,
  already recorded in the heartbeat notes for reuse; not grammar.
- **Already-consumed 💡s** — section-sync checker (built, #2); park(built-here) +
  `depends:` + cadence ruling (encoded, #6); probe-report lint (built, #11);
  outbox↔idea integrity (built, #13); wake-preflight wiring (built, #16) — landed,
  nothing to encode.

Preflight per README § Landing conventions: `python3 scripts/preflight.py` plus full
`python3 bootstrap.py check --strict` green before push; heartbeat overwrite as the
deliberate LAST step (Q-0265 cutover record, fan-in notes, and backpressure line
preserved).

- **📊 Model:** (worker slice, model id withheld per coordinator directive) · high ·
  docs-only (contract prose + card + control ceremony)

## 💡 Session idea

**Optional-line lint coverage** — `scripts/check_ideas.py` now trails the grammar it
enforces: the newly blessed optional `> **Grounding:**` / `> **Sequence:**` lines are
invisible to it, so a malformed pin (no `@<sha>`, no fetch time) passes silently and
the machine-readability the lines were blessed FOR never gets guaranteed. Guard
recipe: extend the grammar constants atop `scripts/check_ideas.py` with
optional-but-well-formed checks for both lines (fire only when the line is present);
test = plant a `> **Grounding:**` line missing its `@<sha>` in a scratch tree.
Repo-internal PROCESS, park(built-here)-eligible, non-proposal-generating — safe
under backpressure.

## ⟲ Previous-session review

The gba-homebrew card (`.sessions/2026-07-10-gba-homebrew-first-batch.md`, PR #17)
and the standing heartbeat both named the contract-grooming micro-slice as overdue
("evidenced across PR #8/#10/#12/#14/#15 + this slice's cards") — consumed here in
full; all five grounding-line 💡s plus the cross-link 💡 land as one grammar
paragraph, zero re-derivation. Deviations: one — the harvest also encoded two
ritual lessons the dispatch's cards carried outside 💡 lines (the pre-written-PR-number
fixup, found in commit history not a card body; the wall-clock stamp, a §⟲ aside) —
judged in-scope because both are exactly the "ceremony lessons" class this slice
exists to write down. Friction found: the era's cards never say their own PR number
in a stable place (deliberately, post-#16), so mapping cards→PRs required the
heartbeat's `last-shipped:` trail — the mapping is recorded above so no future
harvest re-derives it.

## Handoff → next wake

Nothing to babysit: no outbox proposal (backpressure), no claim to clear, amendments
land with this PR. Substrate-kit remains the last stub-empty section (first-batch
seed). Ripest non-proposal slices: substrate-kit first batch, harvest freshness
checker, optional-line lint coverage (💡 above), second-lane harvest. Gate↔ritual
convergence stays parked until the sibling's substrate-gate.yml window closes.
