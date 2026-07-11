# Session — docs+lint slice: contract grooming round 3 (the PR #19–#48 era's contract 💡s encoded)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (dispatched by the continuous-mode coordinator per
> Q-0265; harvest ran as a separate agent, this slice applies+ships)

## What this session did

Encoded the heartbeat's seven grooming-round-3 seeds plus the card-flagged lint
follow-ups (PR #47's `[[fill:` tripwire, PR #24's part-b date-gate) as minimal
in-place amendments to the contract docs and one bounded `scripts/check_ideas.py`
diff — grooming to match practice, not a redesign (PR #6/#21 shape). Every seed's
source card was re-verified verbatim before encoding; a completeness sweep over the
era's other card-flagged seeds produced deliberate skips (each with its reason,
below). No claim: root contract docs are not a section (PR #21 precedent); zero
overlap with the sibling in flight at branch time (`probe/own-heartbeat-parse-self-check`,
websites tree). Inbox read first — still empty; `orders: acked= done=` unchanged. No
outbox entry: non-proposal-generating by design (earn-rate bar).

**Encoded — each seed → its amendment (all one-sentence-or-bullet, in place):**

1. **Freshest-wins citation rule** — PR #19 card 💡, evidence base twelve live
   manifest-staleness datapoints (the sharpest: a manifest row prescribing a fix its
   lane had deliberately archived) → README § Idea file grammar, one sentence
   extending the Grounding-line paragraph (manifest row < lane heartbeat < lane
   HEAD/tree-scan, freshest wins).
2. **Pin-annotation blessing** (`> *(pin annotation: …)*` below the pin, never inside
   it) — PR #28 card 💡, four live instances, zero drift → same README paragraph, one
   sentence. Per the card's own guard recipe, NO check_ideas shape check yet ("only if
   drift is ever observed").
3. **Foreign-order dependency token, doc half** (`<repo>#ORDER-<nnn>` in the Sequence
   body) — PR #44 card 💡 → same README paragraph, one sentence extending the
   Sequence-line rule (forward-only; the one live prose-form instance is exempt).
4. **`## Sim verdict (<date>)` section blessed as the canonical post-verdict marker**
   — PR #41 card 💡 option A + PR #43 card endorsement, four live instances — WITH the
   PR #43 card's lived numbering-cross practice folded in (`VERDICT <n> = PROPOSAL <m>`;
   sim-lab numbers by intake order) → README § Idea file grammar, one new paragraph.
   States stay forward-only and untouched: the note, not a new state, says "verdict
   received".
5. **Producer-reachability check** — PR #45 card 💡 fused with the PR #34 card's
   convergent line ("no surface carries the artifact" is invisible to green CI) →
   README § The probe battery, one bullet after the battery list (Q4/Q6 discipline:
   pattern-exists is not pattern-can-produce).
6. **Expiry-aware probe ordering** — PR #48 card 💡 fused with the PR #25 card's
   time-boxed-capture escalation rule (one capture missed its window by ~4 h, another
   was mooted overnight) → README § The probe battery, one closing paragraph (the
   card said "section README"; encoded at main-README altitude because the rule is
   section-agnostic — interpretation noted for the coordinator).
7. **ORDER `anchor:` field / stale-pointer executor duty** — PR #46 card 💡,
   vindicated live by superbot-games ORDER 001 → control/README.md § inbox.md order
   format, one paragraph under the format block. Executor-side half only: the field
   itself becomes real when the kit/manager adopts it; the verification duty is the
   part this repo owns (clearly additive to the local copy — the claiming-an-order
   graduation precedent).
8. **check_ideas.py, one bounded diff (two card-named tests):** (a) `[[fill:`
   unfilled-stub tripwire — PR #47 card 💡 — new UNFILLED hard-violation class with a
   `(?<!` + backtick + `)` guard so the three live backtick-quoted prose mentions of
   the slot grammar stay green (a real slot is never backtick-wrapped); (b) date-gate
   tightening `>` → `>=` on `OPTIONAL_LINE_GRAMMAR_DATE` — PR #24 card 💡 part b,
   deliberately deferred by PR #28, precondition verified (boundary day clean at 0
   warnings). Acceptance: live tree still `OK — 281 idea files conform`, 0 warnings;
   planted unquoted `[[fill:gist]]` → 1 UNFILLED violation exit 1; planted backticked
   mention → clean; planted malformed Grounding in a 2026-07-10-dated scratch file →
   flips warn→violation; in a 2026-07-09-dated file → stays WARN.

**Skipped — judged not encodable this round (with reasons):**

- **Verdict-vs-note lint, code half** (PR #43 card 💡) — the diff's left side
  ("proposals with finalized verdicts") lives in sim-lab's `control/outbox.md`,
  out-of-repo; check_ideas is hermetic/offline by design (PR #22 Q4 rule). The doc
  half (encode 4) is the enabling move and fixes the byte-shape a future lint needs;
  the lint stays a lint-slice head.
- **Foreign-order token lint, code half** (PR #44 card 💡) — `SEQUENCE_BODY_RE`
  already accepts the token form unchanged; one live prose-form pre-bless instance,
  nothing to enforce yet.
- **Q0 reality check** (PR #23 card) — absorbed by encode 6's live-state-first rule
  plus universal practice since PR #39; a battery-v1 restructure is bigger than a
  grooming bullet.
- **"Fix's clothes" Q4 rule** (PR #27 card) — the card routes it to a future capture
  ("capture in a future generate slice if still believed"), not to grooming; routing
  honored.
- **Joint sequenced routing for coupled build-direct heads** (PR #30 card) —
  self-gated on recurrence ("if the pattern recurs"); one instance so far.
- **Cross-repo consumer `mirrors:`/`depends:` row** (PR #39 card) — zero live outbox
  instances to shape against (all 5 proposals pre-date it) and the outbox is
  append-only/forward-only; encode when the next `depends:`-carrying proposal needs
  it. Not in the heartbeat's seven.
- **Merged-branch pruning close-out line** (PR #42 card) — practice already holds
  (zero stale non-main heads at harvest sweep); the heartbeat routes it under the
  open-work/advisory-fatigue thread, not round 3; cheap to add later if noise appears.

Preflight per README § Landing conventions: `python3 scripts/preflight.py` (6 checks)
plus full `python3 bootstrap.py check --strict` green before push; heartbeat overwrite
as the deliberate LAST content step (Q-0265 cutover record, MANAGER fan-in notes,
datapoint 12, and the superbot-games section-complete milestone preserved verbatim;
the seven-seeds tracker updated to encoded/dispositioned).

**📊 Model:** fable-5 · high · docs + one bounded lint diff (contract prose + check_ideas + card + control ceremony)

## 💡 Session idea

**Grooming rounds should end by re-pointing the trackers that fed them** — this round's
seven-seeds enumeration lived only in the heartbeat's ripest-next list, and the encode
work would have silently invalidated it (the heartbeat would keep claiming seeds
"unencoded" after they landed). The overwrite-own heartbeat makes this self-healing
ONLY if the grooming slice treats tracker-reconciliation as a required close-out step,
which nothing writes down. Candidate round-4 line for README § Coordination or the
grooming-card template: a grooming slice's heartbeat overwrite must re-state every
standing-seed tracker it consumed (encoded → where; skipped → why), so no future
harvest re-derives a stale list. Cost: one sentence; test: the next harvest finds zero
already-encoded seeds still tracked as pending.

## ⟲ Previous-session review

PR #48's card (gen2-boot-pack probe) handed off "grooming round 3 (now seven seeds —
this card adds expiry-aware probe ordering)" — consumed here in full: its 💡 is encode
6, and its enumeration pointer (the heartbeat's ripest list) was accurate; all seven
seeds traced to real card quotes at the cited lines, zero dead references. Its
convergence claim (pairing with the PR #46 `anchor:` seed as "verify the
pointer/premise still exists at HEAD" moves) held up — encodes 6 and 7 are one family
in the final prose. One asymmetry its handoff didn't flag, found at harvest: the
seventh seed ("verdict-vs-note diff / lintable `## Sim verdict` variant") bundles a
doc half and a code half with opposite feasibility — the doc half landed (encode 4)
while the code half is structurally blocked by check_ideas hermeticity (needs sim-lab's
outbox at lint time), so the seed splits rather than closes; recorded in the skip list
so the tracker doesn't re-open it whole. Round-2 precedent (PR #21 card) followed on
ceremony: no claim on root docs, minimal in-place amendments, skips listed with
reasons.

## Handoff → next wake

Nothing to babysit: no outbox proposal, no claim to clear, amendments land with this
PR. Round 3 CLOSED: all seven heartbeat seeds encoded or dispositioned (see the two
lists above), plus the `[[fill:` tripwire and the `>=` date-gate shipped as one lint
diff. Sibling `probe/own-heartbeat-parse-self-check` was open at branch time
(websites tree — disjoint; forward-merge recipe ready if it lands mid-flight).
Remaining lint-slice heads unchanged and untouched: cross-link state-echo (PR #29
card 💡), recommendation-vocabulary (PR #33 card 💡), step-anchor drift (PR #36 card
💡), `check_harvest --states` depth (PR #22 card). Round-4 seed candidates already
visible: the tracker-reconciliation line (💡 above), the verdict-registry question
(what committed surface would let the verdict-vs-note lint run hermetically), and the
`mirrors:`/`depends:` row when the next depends:-carrying proposal lands.
