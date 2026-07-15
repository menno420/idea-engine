# Session — PROPOSAL 075: the hint that hides — mineverse's world views treat the OPTIONAL max_depth envelope hint as an unvalidated visibility gate (14 of 80 valid lattice cells render a miner NOWHERE while the same document ranks them #1 on two boards), and the Deep Diver badge's exact-equality law is non-monotone — digging past the hint LOSES it (game slot, round 15, superbot-mineverse)

> **Status:** `in-progress`
> **Model/time:** fable · 2026-07-15T11:03:46Z (Ideas Lab worker slice — draft the
> round-15 GAME-MECHANICS rotation slot under standing owner ORDER 003/004; round
> 15 opened at fleet backlogs with P073 (#437, merged 2026-07-15T09:59:51Z) and
> served venture with P074 (#438, merged 2026-07-15T10:32:39Z by
> github-actions[bot]), so game mechanics is next per ORDER 004 rule 3. Slot
> spacing history confirmed: P020 … P067, P071 → P075 (spacing 4). Source rotation
> inside the slot per the P063/P067/P071 committed records (gba r6/r7, superbot
> r8/r9, mineverse r10, idle r11, games r12, gba r13, superbot hub r14): round 15
> returns to superbot-mineverse, undrawn in the slot since round 10;
> pokemon-mod-lab excluded per the Q-0260 rule-3 carve-out.)

- **📊 Model:** fable-class · high · idea/planning

*(card born in-progress at 2026-07-15T11:03:46Z as the designed session-gate
hold; flips complete in this PR's final commit.)*

## Scope

Draft a genuinely new sim-shaped idea for the GAME-MECHANICS rotation slot,
round 15, source superbot-mineverse, under standing owner ORDER 003 (continuous
pipeline) and ORDER 004 rule 3. Game priors re-read this session: P055 (mineverse
badge calibration → V066), P059 (idle prestige → V071), P063 (games menu prefix
→ V074), P067 (gba stale-ink → V080), P071 (superbot fishing trophy quantization
→ V084); mineverse non-game priors P045 (staleness constant → V056) and P073
(write-contract rate tiers, this round, in flight).

Head: **the max_depth trust lattice.** The v1 snapshot schema commits
`max_depth` as an "OPTIONAL world-shape hint … Consumers must fall back
gracefully when absent" (schema:24-25 @ b9ade33) and bounds miner
`depth`/`record_depth` 0–3 INDEPENDENTLY — zero cross-field applicators anywhere
in the schema (keyword-swept at drafting). The committed views treat that hint
as a hard gate three ways: `build_ladder`/`build_minimap` render bands
`range(max_depth + 1)` only (views.py:216, 316 — schema fallback 3 ONLY when
absent, :633-634), and `deep_diver` is `record_depth == max_depth` exact
equality (:446-448). Four exact theorems, every registered numeral RAN live
against the ACTUAL committed views.py + snapshot_validation.py (scratchpad
`draft_p075.py`, ALL PASS, exit 0; the committed validator ACCEPTED all 80
lattice cells): **T1** fully-invisible census (3−m)² per present hint — 14/80
cells where a miner has no ladder row, no minimap point, not even `unplotted`
(against the same file's committed "listed honestly, never silently dropped");
minimap-invisible 24, ghost-chip-only 10; **T2** deep_diver ⇔ r == m_eff — 12
non-monotone flip cells (r = m → m+1 loses "deepest"), 24 overshoot denials, and
the m=0 inversion (never-dug newcomer earns, r=3 explorer denied); **T3** one
validator-ACCEPTED witness where the #1 miner on BOTH depth and coins boards
renders nowhere and the badge inverts, and omitting the hint flips all three;
**T4** hint domination — the optional field can only hide (strict on exactly the
14 cells). Repair worlds RAN: conformance applicator → 46-cell lattice, all
censuses zero; overflow bands → 0/80; deep_diver `>=` → zero flips,
byte-identical to committed behavior at m_eff = 3.

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/superbot-mineverse/max-depth-hint-visibility-clip-2026-07-15.md` + the
`ideas/superbot-mineverse/README.md` index row, the `control/outbox.md` PROPOSAL
075 append (append-only, real `date -u`, status sim-ready), and ONE terminal
claim prune (the P074 drafter — PR #438 verified merged at live GitHub
2026-07-15T10:32:39Z, merged_by github-actions[bot], this session before
deletion). Seeds 20261670–673 — allocated from 20261670 (20261660–663 are
P074/V087's registered set; 20261664 is a standalone DATA numeral per the
recorded discrimination rule, NOT a seed; the gap 20261665–669 is the disclosed
in-flight buffer). Arm R reporting-only seeded 20261670/671/672, aux 20261673
never read.

## Constraints honored

- control/inbox.md untouched (manager-written); control/status.md untouched
  (coordinator-only heartbeat). Newest inbox ORDER at HEAD is ORDER 015
  (2026-07-15T03:37:08Z, EAP extended to 2026-07-21) — no ORDER newer than 015
  (checked at sync, 2026-07-15T10:43:32Z); the continuous-pipeline duty
  (ORDER 003/004) is the standing authority for this slice.
- Outbox: PROPOSAL 075 appended via shell (append-only, real `date -u`); the
  live file is under the 200KB rollover threshold — no roll this append. Both
  dated archives untouched (rolled, terminal).
- Claim prune is TERMINAL-only: PR #438 verified merged at live GitHub (mcp
  pull_request_read: merged 2026-07-15T10:32:39Z, merged_by github-actions[bot])
  before deletion; zero open PRs at drafting (list_pull_requests state=open →
  []).
- Numbering verified at HEAD c1b97be: newest PROPOSAL = 074 (live outbox tail +
  both dated archives swept); `PROPOSAL 075`/`proposal-075` collision-grepped
  clean; zero open PRs.
- Grounding FIRSTHAND (Q-0272 git transport): superbot-mineverse read-only
  public-HTTPS shallow clone at live HEAD
  b9ade33ae6019eff45195684fa6fd6f02da4bee0 (fetched 2026-07-15T10:45:57Z — the
  SAME pin P073 grounded at this morning; the lane has not moved) — every
  harvested sentence and constant quoted verbatim with file:line in the idea
  file. The verdict session is fully hermetic (the P017–P074 precedent). This
  repo edits no other repo (Q-0260).
- sim-lab dedup-swept READ-ONLY on a shallow clone @ 9e22abb (fetched
  2026-07-15T10:57:11Z, newest VERDICT 086): no verdict prices a cross-field
  visibility lattice, an optional-field trust boundary, or a non-monotone badge
  law; P055's V066 contact is a static saturation reporting row, argued in the
  idea file's Dedup.
- Seed sweep boundary-aware at HEAD c1b97be: genuine in-tree high-water 20261663
  (P074/V087's registered set 20261660–663); 20261664/20261833 re-confirmed
  DATA-not-seed by the recorded discrimination rule. Allocation starts at
  20261670 per the coordinator relay, strictly above the registered set and the
  disclosed gap 20261665–669.
- Drafting-time verification discipline (V080 live-verify + V084
  NO-DERIVED-LITERALS): every numeral registered in the idea file was PRODUCED
  by the drafting script this session (`draft_p075.py`, ALL PASS, exit 0,
  importing the ACTUAL committed modules) — the 80-cell acceptance sweep, the
  censuses {14, 24, 10} with closed forms (3−m)²/4(3−m)/(3−m)(m+1), the badge
  censuses {20, 12, 24} + the m=0 inversion, the T3 witness and its absent-hint
  triple flip, T4 domination (strict on exactly 14), the G5 hand world, the
  three G6 repair worlds {46, 0, 44/0/byte-identical}, and the frontend meter
  rows (150%, 300%, falsy-0). One drafting-run hand-fact correction disclosed in
  the idea file (the ghost law's per-band `elif`). Zero hand-derived or scaled
  numerals anywhere in the registered set.
