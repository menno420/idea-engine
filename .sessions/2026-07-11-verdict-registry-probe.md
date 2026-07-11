# Session — verdict-registry capture+probe: hermetic `## Sim verdict` note lint

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Captured + probed the committed-verdict-registry idea (the V005 fan-in card's 💡,
`.sessions/2026-07-11-verdict-005-superbot-fanin.md` § "💡 Session idea" @ PR #81
`a1b320a`; ARMED by V006's ruling-field drift — VERDICT 006 shipped no `ruling:`
field, operative text in `recommendation:`, deviation recorded in PR #121, verified
via the PR object: merged 2026-07-11T06:57:33Z, merge `d90f9c5`) as
`ideas/fleet/verdict-registry-2026-07-11.md`, and shipped its built-here half in the
same PR per the README battery shortcut (PR #2/#11 lineage):

- **`scripts/check_ideas.py` — new SIM-VERDICT category** (stdlib, constants in the
  loud co-edit block): every `## Sim verdict` note is linted against the PINNED
  field set — heading `(YYYY-MM-DD)` · `**VERDICT <nnn> · finalized <time> ·
  <token>**` marker · sim-lab `control/outbox.md` @ sha source pin · "State stays"
  closer (hard everywhere — the invariant core ALL six live notes already carry);
  the inline numbering cross (`= this repo's PROPOSAL <nnn>`) + a gate mention are
  date-gated hard from 2026-07-11 (the PR #121 day) and advisory WARN before (the
  PR #24 forward-only pattern); a cross naming a PROPOSAL absent from the LOCAL
  `control/outbox.md` is ALWAYS hard — the PROPOSAL↔VERDICT cross is now
  machine-checked hermetically, zero network; duplicate VERDICT numbers WARN.
  Zero wiring change: preflight CHECKS entry 2 already runs this checker —
  `scripts/preflight.py` and both workflows untouched (kit-v1.10.0 sibling claim
  respected).
- **Registry FILE judged overkill and NOT built** (the origin 💡's file-shaped
  half, reasoned rejection on the idea's Q4): a committed
  `control/verdict-registry.md` is a hand-edited shared index (the claims-README
  measured anti-pattern) duplicating facts the notes already carry — the notes +
  the local outbox ARE the registry.
- **Sim-lab half routed, not built** (idea Q7): pinning sim-lab's verdict-entry
  grammar (`ruling:`-or-`recommendation:` explicit, ideally a `proposal:` cross
  field) is a sim-lab change; routed to the MANAGER via this slice's heartbeat
  notes as an ORDER-worthy fan-in line, evidence attached (fetched RAW at the
  pinned `d89303e`: `ruling:` in only 2/6 verdict entries — V003+V005; no
  machine-readable proposal cross anywhere sim-lab-side).
- Survey (core evidence, tabulated on the idea file): 6 notes grepped; all six
  carry the invariant core; inline cross only 3/6 (all three misses dated
  2026-07-10 — their crosses live on the fan-in cards); finalized-time drifted
  time-only → full-ISO, pin form 40-hex → short sha, V004's gate token drifted
  position (rides its SETTLED line, not the source parenthetical).

Probe verdict (exact line on the idea file):
`park(built-here — SIM-VERDICT note lint in scripts/check_ideas.py, this PR)` —
single-pass probe (no panel: repo-internal PROCESS tooling, reversible,
low-blast-radius); no outbox proposal (nothing sim-shaped — a contract check is
proven by its own red/green, the #114 precedent).

Claim ritual honored: `control/claims/probe-verdict-registry-2026-07-11.md`
fast-laned FIRST as PR #124 (merged `c4285a5` by the enabler within the minute),
claims dir re-read at the recut — kit-v1.10.0 the only sibling claim live
(disjoint: kit surface incl. preflight.py; this slice touches neither preflight.py
nor any workflow), the #123 harvest claims cleared by its own merge. Claim file
deleted in this PR.

**📊 Model:** fable-5 · one checker extension + docs (idea file, fleet README
index bullet, card, heartbeat, claim clear)

## Live run + smoke test (both directions, real tree)

Live run over the real tree (also the preflight's check_ideas leg — all 7 green
on the final tree):

```
$ python3 scripts/check_ideas.py
warn: SIM-VERDICT ideas/superbot/explore-hub-federated-world-2026-07-10.md:72: no `= this repo's PROPOSAL <nnn>` numbering cross
warn: SIM-VERDICT ideas/superbot/idea-probe-brainstorm-simulator-2026-07-10.md:90: no `= this repo's PROPOSAL <nnn>` numbering cross
warn: SIM-VERDICT ideas/superbot/wild-encounters-activity-spawning-2026-07-10.md:100: no `= this repo's PROPOSAL <nnn>` numbering cross
check_ideas: OK — 299 idea files conform to the README grammar (3 warning(s), advisory)
exit=0
```

(the three warnings are exactly the surveyed legacy misses — V001/V002/V004,
advisory by the date gate, never exit-affecting.)

Smoke 1 — numbering cross broken (`PROPOSAL 006` → `096` in the V006 note),
hermetic cross-existence check fires hard:

```
SIM-VERDICT ideas/superbot-idle/idle-economy-sim-kernel-2026-07-11.md:197: numbering cross names PROPOSAL 096 but control/outbox.md carries no such proposal
check_ideas: FAIL — 1 violation(s) across 298 idea files (+3 warning(s), advisory)
exit=1
```

Smoke 2 — "State stays" closer removed, pinned-core check fires hard:

```
SIM-VERDICT ideas/superbot-idle/idle-economy-sim-kernel-2026-07-11.md:197: no "State stays" closer
check_ideas: FAIL — 1 violation(s) across 298 idea files (+3 warning(s), advisory)
exit=1
```

Both smokes restored via `git checkout --`; post-restore run exit 0. Outbox mode
unaffected (`check_ideas --outbox` OK).

## 💡 Session idea

The V006 deviation was caught by a HUMAN-shaped judgment call and recorded in PR
prose (#121) — this slice could only date-gate its lint at "the day the drift was
recorded" because that prose existed. The general pattern: when a fan-in/consumer
session survives an upstream grammar deviation by judgment, it should ALSO append
one machine-findable line (a pinned `deviation:` marker with sha + field name) to
the artifact it writes, so the next tooling slice can date-gate/pin against a
grep instead of an archaeology pass. Cheap discipline, compounding payoff — the
same move as the guard-recipe convention on cards.

## ⟲ Previous-session review

PR #123 (`harvest/websites-superbot-repin`, squash `3cf28e1`): verified against
the tree at my recut — both legs landed (websites re-pin section + two
forward-only outcome mirrors, superbot gist refreshes, both first
`.harvest-pin.json` records), BOTH its claim files deleted at close, card
complete with the Model line, heartbeat ⚑ OWNER-ACTION preserved verbatim. Its
last-shipped head is number-less ("this slice") per the rule — THIS session
stamps it #123 in the heartbeat overwrite (the #72/#79 precedent). Adopted from
it: the tree-diff-over-diffstat honesty norm (its 💡) shows up here as
fetch-RAW-at-the-pin before asserting sim-lab field facts, and its
claims-disjointness note pattern is copied for the kit-v1.10.0 sibling. One
inherited fact acted on: its heartbeat's notes carry the v1.10.0 hop as ripest
kit slice — this slice deliberately kept `scripts/check_ideas.py` OUTSIDE that
claim's expected-files list and verified the disjointness before building.

## Handoff → next wake

- The SIM-VERDICT lint is live in preflight from this merge (CHECKS entry 2 —
  no wiring change). Future fan-ins must carry the inline cross + gate mention
  (date-gated hard ≥ 2026-07-11); the three 2026-07-10 notes stay advisory
  warnings by design — do NOT retrofit them (forward-only).
- Guard recipe: grammar constants live in the `# Sim-verdict note grammar` block
  of `scripts/check_ideas.py` (`SIM_VERDICT_*`, `PROPOSAL_CROSS_RE`,
  `GATE_MENTION_RE`, `OUTBOX_PROPOSAL_ID_RE`); test = the two smokes on this
  card. If the README note blessing changes, co-edit that one block.
- The MANAGER fan-in (heartbeat notes): sim-lab verdict-entry field-set pin —
  `ruling:`-or-`recommendation:` explicit + a `proposal:` cross field; evidence
  PR #121 + 2/6 `ruling:` coverage at `d89303e`. If sim-lab adopts a cross
  field, a later slice can close the loop outbox→verdict (non-hermetic half,
  wake-time `check_harvest`-style — deliberately NOT built now).
- Friction for the ledger: anonymous `api.github.com` polling 403s through the
  proxy (use the GitHub MCP tools or authenticated git); a sibling landed
  mid-claim (#123) and moved main — recut + union-merge of
  `.substrate/guard-fires.jsonl` handled it forward-only.
- Ripest next unchanged from #123's handoff (five new-born websites heads, the
  websites #10 meta.md relay one-liner) plus the kit-v1.10.0 hop (claimed, in
  flight).
