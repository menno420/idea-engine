# Session — superbot-next four-head verify sweep (the section's whole backlog through one battery pass)

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-11 ~08:43Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

The `ideas/superbot-next/` section carries exactly four captured heads, all captured
2026-07-10 against the same lane pin `ec2bcf2`: composition-parity-registration-diff ·
band-binding-doctrine-encoding · parity-flip-cadence · effect-arming-compensator-checklist.
This slice resolves all four in one pass — resolving them closes the section. Section
claimed first — `control/claims/probe-superbot-next-four-heads.md` landed on main via
fast-lane PR #139 (merged 08:29:16Z by the enabler) before any build work; the only
sibling claim at HEAD is `probe-substrate-kit-host-checkers-one-gate.md` (PR #140) — a
disjoint section, shared-heartbeat overlap only.

## Probe shape (stated per the batch precedent)

Mixed, chosen per head by the verify-first read (the PR #66/#131 verify-and-park form
escalating to full batteries only where the live check leaves the gap open): TWO
verify-and-parks (composition-parity — the lane self-served the exact prescribed test;
parity-flip-cadence — overtaken by a stronger lane-built mechanism) + TWO FULL battery-v0
reports (band-binding-doctrine-encoding + effect-arming-compensator-checklist — both
premises survive at the live pin). One shared verify-first sweep at one lane pin served
all four reports (the #102/#116/#132/#136-slice sibling-batteries precedent).

## Verify-first (one sweep, four reports)

- **superbot-next live HEAD `910c44e`** (`git ls-remote` 2026-07-11T08:13:45Z in the
  phase-1 sweep; re-confirmed UNMOVED at 08:42:15Z before authoring — blobless clone at
  the pin), **50 commits past the captures' shared `ec2bcf2` pin**: bands 2/3/4/6/7/8
  parity work shipped overnight, parity 1/49 → 23/49 subsystems ported, gate GREEN
  151/151 goldens at `bd211e9` (#163), report leg 191/465 (was 15/465). Kit v1.10.0.
- **Composition-parity head:** lane PR #114 (merge `385df11`) landed exactly the
  prescribed both-roots ref-set diff test (`tests/unit/invariants/test_composition_parity.py`)
  AND fixed blackjack/rps in the same PR, pre-band-6; burn-down ledger
  `_KNOWN_ENSURE_ONLY` 99 → 45 refs at HEAD (mining 28, fishing 15, creature 1, role 1;
  may only shrink by its own docstring contract).
- **Cadence head:** 22 pending→ported flips in ~24h (`ec2bcf2..910c44e`); the operative
  mechanism is the dedicated continuous-mode parity-flips lane (Q-0265, waves 1–6) —
  no cadence *rule* was ever written, and the mechanism moots the need.
- **Band-binding head:** ORDER 004 still acked-NOT-done at the lane heartbeat @
  `910c44e`; the bindings are encoded in NO doctrine doc (grep-verified —
  `docs/collaboration-model.md` carries only the ORDER-010 @codex rule); BUT bands 6–7
  carried both bindings anyway via the emergent walking-skeleton test convention
  (`tests/unit/band6/` riding every band-6 port PR; `tests/unit/band7/*_walking_skeleton.py`,
  5 files at HEAD) + per-slice live-drive proof records (#144/#148/#151/#160).
- **Compensator-checklist head:** "Still queued: role/proof_channel live EFFECT action
  ports (GuildRoleActions, ChannelPermActions still unarmed)" verbatim at the heartbeat
  @ `910c44e`; no arming-checklist doc exists (grep zero); lessons demonstrably
  re-litigated per-PR (#133 settle-once double-payout race caught mid-flight, #138
  render-once, #163 ad-hoc effect-leg sequencing); compensator allowlist deliberately
  EMPTY (re-asserted #145/#160/#163); more armings queued (the modal-arming slice +
  the owner-key-gated live-NL leg, OWNER-ACTION 5).

## Verdicts (one per idea)

- `composition-parity-registration-diff` → **parked(lane-self-served)** — PR #114
  (`385df11`) is the capture's exact slice, plus the burn-down ledger it asked for.
- `parity-flip-cadence` → **parked(overtaken)** — the parity-flips lane converges far
  faster than one-flip-per-band; the idling-gate risk class is dead.
- `band-binding-doctrine-encoding` → **parked(routed — lane build-direct)** — one-doc
  encoding slice in `docs/collaboration-model.md` beside the @codex rule, the piece
  that lets 004 close on evidence at bands 8/9; not simulation-shaped.
- `effect-arming-compensator-checklist` → **parked(routed — lane build-direct)** —
  one-page pre-arming checklist, same doc, landing BEFORE the role/proof_channel
  arming slice (the literal next queued item); not simulation-shaped.

No outbox proposal (nothing sim-shaped — doctrine text is proven by the next arming/band
close-out citing it, the #114 precedent family). Section README index re-badged for all
four rows. **SECTION MILESTONE: superbot-next 4/4 probed-or-parked — the EIGHTH complete
section** (after superbot-games, trading-strategy, superbot-mineverse, venture-lab,
superbot-idle, pokemon-mod-lab, and substrate-kit — whose host-checkers-one-gate probe
#141 landed mid-flight of this slice and took the seventh; forward-merged, never
rebased, heartbeat reconciled forward-only).

## Verification (real runs, this tree)

Full `python3 scripts/preflight.py` (all 8 checks) + `python3 bootstrap.py check
--strict` run green immediately before push, after the heartbeat overwrite (the three
SIM-VERDICT numbering-cross warnings are the known deliberate legacy advisories); a
pre-push `git fetch origin main` reconciles any mid-flight sibling forward-only per the
README recipe if main moves (the substrate-kit host-checkers-one-gate probe is in
flight, claim #140). The `.substrate/guard-fires.jsonl`/`reflections.json` hook residue
stays uncommitted for the telemetry lane, per the phase-1 handoff.

**📊 Model:** fable-5 · medium · batched verify sweep (2 verify-and-parks + 2 full
battery reports + state lines + section index + card + claim clear + heartbeat; no
scripts, no workflows, no proposal — task-class: bounded whole-section battery pass)

## 💡 Session idea

**A "lane-self-served half-life" datapoint series is accumulating and nobody owns it.**
This section's composition-parity head was self-served by its lane in under a day
(capture 2026-07-10, lane PR #114 merged the same evening, pre-band-6 exactly as
prescribed); trading-strategy's kit-upgrade head was self-served in 14 minutes; websites'
open-pr-awareness in ~19 minutes. The pattern: the sharper and more build-shaped a
captured head is, the more likely the lane ships it before this repo's probe cycle
reaches it — which argues for probing build-shaped captures within one wake of capture
(or capturing them WITH a routed ORDER attached), while reserving the slower battery
cadence for genuinely ambiguous heads. One `ideas/fleet/` capture could formalize the
triage rule from the measured datapoints.

## ⟲ Previous-session review

Reviewed: `.sessions/2026-07-11-superbot-mineverse-first-batch.md` (per the phase-1
handoff — the superbot-family predecessor slice). A fable-5 worker slice ~04:02Z shipped
the superbot-mineverse first batch — 5 captures + section index, grounded at lane HEAD
`510fa3e` / fm `dd8dc10`, claim-first via fast-lane PR #75, verification green (296
ideas, 13 sections, preflight 7 checks — now 8). Its handoff flagged the lane family's
fast cadence and prescribed "verify-first at lane HEAD before probing" — which this
slice's findings vindicate emphatically: at the live pin, two of this section's four
heads were already consumed lane-side (one self-served verbatim, one overtaken by a
stronger mechanism), and only the verify-first sweep kept those probes from prescribing
work the lane had already shipped.

## Handoff → next wake

The superbot-next section is CLOSED (4/4) — no captured heads remain anywhere in
`ideas/superbot-next/`. The two routed heads (band-binding one-doc encoding slice +
effect-arming pre-arming checklist slice) are both lane build-direct, SAME target doc
(`docs/collaboration-model.md`, beside the @codex rule), and could ride ONE lane ORDER —
the heartbeat notes say so for the manager's :30 sweep; sequencing matters on the second
(checklist BEFORE the role/proof_channel arming slice — the modal-arming slice was
already dispatched at the lane's last heartbeat, so the window is measured in wakes, not
days). Watch the lane's cadence: 50 commits in ~24h means any relay should re-verify at
the then-live HEAD before writing the ORDER. The substrate-kit host-checkers-one-gate
probe (claim #140) was in flight this session — it landed mid-flight as #141 (merged
`f71881c`), was forward-merged into this branch per the README recipe, and took the
seventh-section milestone (its heartbeat facts, including the kit-lane SIX-head fan-in
and its #138 stamp, are preserved under this slice's heartbeat chains).
