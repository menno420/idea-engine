# Session — PROPOSAL 071: the personal best is a finite resource — the committed 2-decimal weight grid caps every species' trophy ladder, the modal catch's chase completes in ~148 casts, and no committed rod/weather/bait knob can extend it (game rotation, round 14, superbot hub fishing)

> **Status:** `in-progress`
> **Model/time:** fable · 2026-07-15T08:46:47Z (Ideas Lab worker slice — draft the
> round-14 GAME-MECHANICS rotation slot under standing owner ORDER 003/004;
> round 14 opened at fleet backlogs with P069 (#432) and served venture with
> P070 (#434, merged 2026-07-15T08:16:04Z), so game mechanics is next per
> ORDER 004 rule 3. Source rotation inside the slot per the P063/P067 records
> (gba ×2 r6/r7, superbot ×2 r8/r9, mineverse r10, idle r11, games r12,
> gba r13) returns round 14 to the superbot hub — undrawn since round 9,
> pokemon-mod-lab excluded DARK/private per the standing Q-0260 rule-3
> carve-out.)

- **📊 Model:** fable-class · high · idea/planning

## Scope

Draft a genuinely new sim-shaped idea for the GAME-MECHANICS rotation slot,
round 14, under standing owner ORDER 003 (continuous pipeline) and ORDER 004
rule 3 ("fleet backlogs → venture's book/product space → game mechanics →
COMPLETELY UNRELATED domains"). Slot spacing history confirmed: P020, P023,
P027, P031, P035, P039, P043, P047, P051, P055, P059, P063, P067 → P071
(spacing 4). Source: the superbot hub (least-recently-drawn since r9; r10–r13
drew mineverse, idle, games, gba), on a mechanic DISJOINT from the hub's prior
draws — P047 creature battle (V058), P051 chicken farm (V062), P020/P023/P027
casino (V022/V025/V029), P003/P016 encounter spawns.

Head chosen: **the trophy-record quantization ceiling** — the hub fishing
game's shipped "trophy records per species (biggest caught)" retention hook
(weight.py's own header: "a cheap long-tail retention goal"; the design doc:
"a fresh record celebrates with '🏅 New personal best!' … 'personal best'
beats raw counts for retention") rides a committed weight law
`max(0.01, round(nominal × U(0.65, 1.55), 2))` whose 2-decimal rounding gives
every species a FINITE record ladder with a REACHABLE ceiling — and the
committed strict-> PB comparison (fishing_workflow.py:267) makes the chase
provably terminating. Live drafting census (every registered number verified
by enumeration this session, the V080 lesson): the minnow — the MODAL catch
under the committed inverse-size mix at every rod tier — has exactly 17
atoms, ceiling probability exactly 2/81 (E[catches to ceiling] = 40.5,
≈ 147.6 casts at the bare-rod level-7 mix), and an exact lifetime-PB law
E[lifetime PBs] = Σ_k p_k / P(X ≥ v_k) = 11736310749428605/3026966925030048
≈ 3.877 celebrations EVER; all 21 species sum to ≈ 153.38 lifetime PBs
against a continuous benchmark that diverges (harmonic law, distribution-free
P(PB at t) = 1/t); the strict-record law P(PB at t) < 1/t holds from t = 2 on.
Invariance grounded: roll_weight's only caller passes (species, rng) — no
rod (rarity_pull ≤ 1.70), weather (rarity_mult ≤ 1.30), bait, or venue knob
touches the atoms, so the entire committed progression ladder can only change
the SPEED of ladder depletion, never extend it.

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/superbot/fishing-trophy-record-quantization-ceiling-2026-07-15.md` +
the `ideas/superbot/README.md` index row, the `control/outbox.md` PROPOSAL
071 append (append-only, real `date -u`, status sim-ready), and ONE terminal
claim prune (the P070 drafter — PR #434 verified merged at live GitHub
2026-07-15T08:16:04Z, merged_by github-actions[bot], this session before
deletion). Seeds 20261630–633 — allocated from 20261630 per the coordinator
relay (20261620–623 are P070/V083's registered set; the gap 20261624–629 is
the disclosed in-flight buffer). Arms F/R reporting/fidelity seeded, aux
20261633 never read.

## Constraints honored

- control/inbox.md untouched (manager-written); control/status.md untouched
  (coordinator-only heartbeat). Newest inbox ORDER at HEAD is ORDER 015
  (2026-07-15T03:37:08Z, EAP extended to 2026-07-21) — no ORDER newer than
  015; the continuous-pipeline duty (ORDER 003/004) is the standing authority
  for this slice.
- Outbox: PROPOSAL 071 appended via shell (append-only, real `date -u`); the
  live file is ~114 KB pre-append, under the 200KB rollover threshold — no
  roll this append. Both dated archives untouched (rolled, terminal).
- Claim prune is TERMINAL-only: PR #434 verified merged at live GitHub (mcp
  pull_request_read: merged 2026-07-15T08:16:04Z, merged_by
  github-actions[bot]) before deletion; zero open PRs at drafting.
- Numbering verified at HEAD d165876: newest PROPOSAL = 070 (live outbox +
  both dated archives swept); `PROPOSAL 071`/`proposal-071` collision-grepped
  clean (0 hits in live outbox, both archives, ideas/, docs/), zero open PRs.
- superbot READ-ONLY (fleet READ standing-authorized, git transport —
  `git clone https://github.com/menno420/superbot.git`, shallow, origin/main
  @ f8e2313a087e18cb32e88269d468b0b30a41fad9 fetched 2026-07-15T08:34:14Z);
  this repo edits no other repo (Q-0260). Every measured constant in the idea
  file is read from superbot's committed files at that pin and cited
  file@sha; every model convention is declared in the idea file.
- Seed sweep boundary-aware at HEAD d165876: numerals ≥ 20261620 in-tree are
  20261620–623 (P070/V083's registered set + its disclosure text) and the
  standalone data numerals 20261664/20261833 matching the recorded
  discrimination rule (Fraction numerators in results-quoting text — data,
  not seeds); allocation starts at 20261630, strictly above the registered
  set and the disclosed gap 20261624–629.
- Drafting-time verification discipline (the V080 lesson, the P068/P069/P070
  norm): every theorem registered below RAN LIVE this session — the exact
  atom census (17/52/…/2462, probabilities summing to 1 per rank), the
  rank-1 atom law (4/81 + 15×5/81 + 2/81), the ceiling law 2/81, the exact
  lifetime-PB rational, the strict-record inequality at t ∈ {2,3,5,10,41},
  the composite career table, AND a fidelity check importing the actual
  committed module (support identity on ranks 1/2/21; ceiling frequency
  0.0249 vs 2/81 within MC noise at 400k draws). One discovered drafting
  hazard disclosed in the idea file: exact lifetime-PB rationals for ranks
  ≥ ~7 exceed CPython's default 4300-digit int-print limit — the fixture
  registers printable exact anchors for ranks 1–3 and gates large ranks by
  in-memory Fraction equality, never by printing.

## 💡 Session idea

*(placeholder — filled at the complete-flip; the born-red hold is exactly
this line per the session gate)* [[fill:session-idea]]

## ⟲ Previous-session review

*(placeholder — filled at the complete-flip)* [[fill:previous-session-review]]
