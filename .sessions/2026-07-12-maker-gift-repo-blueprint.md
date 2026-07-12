# Session — capture slice: maker gift-repo blueprint (venture-lab)

> **Status:** `complete`

- **📊 Model:** fable-5 · capture slice (one new venture-lab idea file + the
  section README index bullet + this card; no code, no probes)

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this card's
born-red first commit carries the `ideas/venture-lab/` collision flag per the
PR #222/#225/#243/#244 workflow convention. Scope: ONE new file —
`ideas/venture-lab/maker-gift-repo-blueprint-2026-07-12.md` — plus the
venture-lab section README index bullet and this card. A SIBLING session is
writing `ideas/venture-lab/maker-ecosystem-research-2026-07-12.md` in
parallel (disjoint file, uniquely named — no collision; cross-linked by name,
never blocked on).

## What this session did

Captured the owner-requested (2026-07-12) **maker gift-repo blueprint**: a
complete plan for a GitHub repo the owner will gift to a friend (two 3D
printers — one small, one 3-color — plus an Arduino robot arm), pre-seeded
with substrate-kit machinery, a starter idea backlog, and finished projects,
so the friend discovers Claude+GitHub workflows with his own Claude account
from day one. Seven sections: repo skeleton with a defended kit cut list
(checks + simplified cards YES; control/ plane, claims, fleet sync, panel
mode, born-red hold NO — each cut justified item by item), a beginner
CLAUDE.md outline with hard print/arm safety rules and a literal worked
bracket prompt, five pre-built starter projects each with 2–4 acceptance
criteria, a 14-head starter ideas backlog (six arm+printer crossovers), a
fleet reuse inventory with per-row citations and adaptations, a 7-day
one-feature-per-day discovery curriculum, and a routed 5-slice delivery plan
ending in a one-line six-field OWNER-ACTION (recommended: name=makerbench,
private, all five projects, optional PCA9685 shopping-list add-on).

Mid-slice coordinator context update, folded in before ship: the friend's
arm is a generic 6DOF/6-servo kit (Amazon.nl, no controller included) — the
arm starter (project c) was retargeted at exactly that hardware (friend's own
Arduino + PCA9685 servo driver, conservative travel limits + slow easing for
unbranded 180° servos, per-joint calibration routine as the FIRST arm project
writing `arm/calibration.json` — deliberately first-PR material), the
external 5–6 V servo-power rule was added to the CLAUDE.md safety outline,
and the owner ask gained the PCA9685 shopping-list line.

Grounding discipline: external pins are real `git ls-remote` HEAD pins taken
this session — substrate-kit `0801be9` (HEAD v1.15.0 measured vs the ~v1.14.0
recon expectation; lanes run v1.14.0 per the roster — both stated in-file),
fleet-manager roster `54a9588` (gen #17), superbot `5c84ce2` (the 8-question
probe-battery source) — with the cited files fetched at those exact SHAs via
raw.githubusercontent.com. Local cites @ `949fc0b`. No invented SHAs.

Dedup: `ls ideas/venture-lab/` + the gift/maker/printer/arduino/starter grep;
nearest head `substrate-kit-agent-fleet-starter-2026-07-11.md` READ IN FULL —
the new file states the relation explicitly (PERSONAL-GIFT instance of that
family, not the commercial starter; neither supersedes the other) and reuses
its gap-5 tagged-release pinning rule.

## Close-out

**Evidence:**

- ideas touched (2): `ideas/venture-lab/maker-gift-repo-blueprint-2026-07-12.md`
  (NEW, state `captured`) and `ideas/venture-lab/README.md` (one index bullet
  appended, state echo `captured` matches)
- sessions touched (1): this card
- code touched: none · control touched: none (dispatch boundary) — the
  pre-existing unstaged `.substrate/` telemetry noise in the worktree was
  deliberately NOT staged (not this slice's change)
- git: branch `slice/maker-gift-repo-blueprint` off main `949fc0b` (an
  enabler-allowlisted prefix — the #253 lesson applied at dispatch), born-red
  card first commit `507deae`, capture commit `9550899`, card flip last; draft
  PR flipped ready on green per dispatch.
- verify: `python3 bootstrap.py check --strict` and
  `python3 scripts/preflight.py` run green before push (born-red hold on this
  card pre-flip is the designed exception).

**Judgment (the half only the session knows):**

- Decisions made, decide-and-flag: (1) the kit cut list takes a POSITION
  (solo human+Claude wants checks + cards, NOT fleet coordination machinery)
  rather than deferring it to the build — the owner works in fragments and
  expects agents to complete the thought (Q-0254), and every cut is reversible
  at slice 1; (2) `Target:` kept `menno420/venture-lab` per section convention
  even though the build target is a not-yet-existing gift repo — the delivery
  plan names the boundary explicitly; (3) the sibling dossier is cross-linked
  by name while not yet on main — flagged in-file ("do not treat a red link
  as drift") rather than omitted, so neither session blocks the other.
- Next session should know: the blueprint's tool picks (OpenSCAD-first,
  arduino-cli, pyserial, Spoolman upgrade path) defer to the companion
  dossier's findings at build time by explicit in-file rule — a groom pass
  after the dossier lands should reconcile any contradictions rather than
  treating them as drift.

## 💡 Session idea

The venture-lab index bullets have grown into multi-line paragraphs that
restate half the idea file (this slice's own bullet included — it follows the
section's established register). A `check_ideas` advisory leg that warns when
an index bullet exceeds ~N words would push the index back toward its real
job — a scan surface, not a shadow copy; the STATE-ECHO checker already
proves per-bullet linting is cheap (`scripts/check_ideas.py`@949fc0b,
`check_state_echoes`). Warn-first per the repo's checker-authoring doctrine.

## ⟲ Previous-session review

The story-window-recheck card (`.sessions/2026-07-12-story-window-recheck.md`)
held up as the workflow precedent this slice leaned on: born-red ceremony
shape, the dispatch-boundary section-collision flag (no claim file when
barred from `control/`), and the draft-PR-flipped-ready-on-green landing —
all three re-executed here unchanged. Its load-bearing facts were not
consumed by this slice (different section, no shared pins); its handoff's
watch conditions (story-shaped websites orders, the fifth backlog re-pin)
remain open for the next groom/harvest slice — untouched and unclaimed here.

## Handoff → next wake

The blueprint stands `captured` with a paste-ready owner ask in-file
(§7 — one line answers name + visibility + project cut). Watch conditions:
(1) the companion dossier `maker-ecosystem-research-2026-07-12.md` landing —
a groom pass should reconcile tool picks against it; (2) the owner's one-line
reply — on arrival, the 5-slice build routes via the manager (this seat
writes no other repo); (3) if the gift repo materializes, it becomes the
kit's first single-human adopter datapoint — evidence the parked commercial
starter head explicitly lacks (feed it back into that file's re-open case).
