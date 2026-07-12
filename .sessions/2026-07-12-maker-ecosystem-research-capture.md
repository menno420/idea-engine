# Session — capture slice: maker ecosystem research dossier (venture-lab)

> **Status:** `complete`

- **📊 Model:** fable-5 · capture slice (one new `ideas/venture-lab/` head + index row +
  this card; no code, no probe — capture only)

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this card's
born-red first commit carries the `ideas/venture-lab/` collision flag per the
PR #222/#225/#243/#244 workflow convention. Scope: ONE new head —
`ideas/venture-lab/maker-ecosystem-research-2026-07-12.md` — plus the
venture-lab README index row and this card.

## What this session did

Captured the external-ecosystem RESEARCH companion for the maker gift repo:
the owner is gifting a friend a GitHub repo seeded with substrate-kit + ideas
+ starter projects; the friend has two 3D printers (one small, one larger
3-color) and a generic 6DOF/6-servo arm kit (Amazon.nl, no controller
included, MG996R-class servos) plus general Arduino tinkering, and will drive
the repo with his own Claude. The head is explicitly a **reference dossier,
not a build proposal** (stated in its first paragraph); class is `venture`
per the README grammar — no `reference` class exists and none was invented.

Content: six research sections merged from three dispatched research passes
plus a supplemental generic-6DOF arm control-stack pass delivered mid-slice
(folded into section 4 as a dedicated subsection: PCA9685 + external power,
MG996R clone caveats, servo easing, per-joint calibration, IK with measured
links, serial/G-code protocols). Entry format kept throughout (name — link —
what — how-it-helps-him); every link and every "couldn't verify" flag
preserved. Final section: a TOP 10 highest-leverage list distilled across all
entries, re-weighted after the arm supplement (the arm ships with no
controller, so the PCA9685/easing/calibration stack displaced Spoolman from
the list; Spoolman stays referenced in item 9 and in section 2).

Dedup: recon grep found no real maker/3d-print/arduino/gift content anywhere
in `ideas/` (only "pacemaker" false positives). Overlap seams handled by
reference, not restatement: the gift-repo/kit-packaging seam cross-links
`substrate-kit-agent-fleet-starter-2026-07-11.md` in the dossier intro. The
companion blueprint head `maker-gift-repo-blueprint` did not exist at branch
time — cross-linked BY NAME ONLY with an in-flight note (its sibling branch
`slice/maker-gift-repo-blueprint` appeared remotely mid-slice, confirming the
sibling is live; no live relative link that would break pre-land).

## Close-out

**Evidence:**

- ideas touched (2): `ideas/venture-lab/maker-ecosystem-research-2026-07-12.md`
  (NEW — state `captured`, class venture, target menno420/venture-lab),
  `ideas/venture-lab/README.md` (index row added)
- sessions touched (1): this card
- code touched: none · control touched: none (dispatch boundary)
- git: branch `harvest/maker-ecosystem-research` off origin/main `949fc0b`,
  born-red card first commit (`f073fa2`), capture commit follows (`6994a17`);
  draft PR #265 flipped ready on green — never merged by this slice,
  auto-merge never armed by this slice.
- verify: `python3 scripts/preflight.py` PASS all 10 checks, exit 0, before
  each push; `python3 bootstrap.py check --strict` red only on this card's
  own designed born-red HOLD pre-flip (the designed exception), re-run green
  after the flip. Gate-hook telemetry appends to
  `.substrate/guard-fires.jsonl` restored to pre-run bytes before every
  commit; `.substrate/` never staged.

**Judgment (the half only the session knows):**

- Decisions made: (1) Class `venture`, not an invented `reference` class —
  README grammar allows product|process|venture only; the reference-dossier
  nature is carried in the title and first body paragraph. (2) TOP 10
  re-weighted after the supplemental arm research: the
  PCA9685+power+easing+calibration stack is mandatory to make the
  no-controller arm move at all, so it outranks Spoolman for this friend.
  (3) Arm cited only as "generic 6DOF/6-servo kit (Amazon.nl, no controller
  included)" per mid-slice correction; branded arm ecosystems excluded.
- Next session should know: the dossier is intentionally content-disjoint
  from the fleet-starter head (kit packaging) and the gba-homebrew head
  (template-for-a-hobbyist-scene); if the blueprint head lands under a
  different final filename than `maker-gift-repo-blueprint`, the dossier's
  by-name cross-links (intro + Sequence line) need a one-line touch-up.

## 💡 Session idea

Cross-linking an in-flight sibling head by bare name is convention, but
nothing ever re-checks that the name resolved: a `check_ideas` advisory that
greps idea bodies for backticked head-names matching the idea-filename
grammar plus "in flight"/"sibling" markers, and warns when no file with that
stem exists after N days, would turn dangling forward-references into a
report-only lint line instead of silent rot.

## ⟲ Previous-session review

previous-session review: this slice's shape precedent,
`.sessions/2026-07-12-verdict-inheritance-guard-capture.md`, held up on every
claim this slice reused: its harvest/* prefix rationale matches
`substrate.config.json` `automerge.branch_patterns` as checked out at
`949fc0b` (no `capture/` pattern exists — verified in-tree); its "born-red
hold is the designed exception" wording reproduced verbatim by this slice's
own strict-gate run; its draft-PR-flipped-ready-on-green dispatch convention
was followed. Its captured head
`ideas/fleet/carried-watch-verdict-inheritance-guard-2026-07-12.md` exists at
this branch's base with state `captured` and its index row in
`ideas/fleet/README.md`, exactly as the card claims. One drift noted, not a
defect: recon predicted the container-local kit auto-draft
`.sessions/2026-07-12-session.md` reds local strict runs; on this slice's
runs the strict checker surfaced only this slice's own born-red card, so the
auto-draft noise did not reproduce as described (untracked file, never rode
any branch either way).

## Handoff → next wake

Facts for the coordinator heartbeat (NOT written here — control/ is
coordinator-only): ONE new venture-lab head captured
(`maker-ecosystem-research-2026-07-12.md`, captured, reference dossier for
the maker gift repo); companion blueprint `maker-gift-repo-blueprint` was in
flight in a sibling session at close-out (remote branch
`slice/maker-gift-repo-blueprint` observed) — when it lands, verify the
by-name cross-links resolve; PR #265 left ready-for-review, never merged,
auto-merge never armed by this slice.
