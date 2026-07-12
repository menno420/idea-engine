# Session — superbot-next harvest sweep (lane-born 💡s + backlog link-index @ 80464ab)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-12 ~01:34Z (write-worker slice, dispatched by the
> coordinator on a recon pass's verified findings)

## Scope

Harvest pass over `menno420/superbot-next` from the section's last watermark — lane pin
`910c44e` @ 2026-07-11T08:13:45Z (the four-head verify sweep,
`.sessions/2026-07-11-superbot-next-four-head-verify-sweep.md`) — to the live lane HEAD
`80464ab39f86d55cede1e38b4780e7b1cc4a1777` (`git ls-remote` 2026-07-12T01:34:18Z,
re-verified unmoved from the recon pass's read). Five idea-shaped candidates surfaced in
the lane's session cards and heartbeat since the watermark → 3 captured as new
`ideas/superbot-next/` files + 2 skipped with reasons; separately, 3 lane-own backlog
docs (`docs/ideas/` at the pin) that were never indexed here got link-only index rows.

## What this session did

**3 captured** (state `captured`, class process, grounding pinned @ `80464ab` · fetched
2026-07-12T01:34:18Z; one-paragraph summary + source citation each, never copying the
lane card beyond the summary):

- `ideas/superbot-next/registry-shrinkage-sentinel-fixture-2026-07-12.md` — the
  session-scoped autouse `ref_inventory()`/`provider_names()` no-shrinkage sentinel
  ("the world a suite finds is the world it leaves"); source lane card
  `.sessions/2026-07-12-canonical-order-flake-fix.md` § 💡 @ `80464ab`.
- `ideas/superbot-next/known-risks-fix-coupling-checker-doctrine-2026-07-12.md` — the
  #221→#223 KNOWN_RISKS→fixing-PR coupling (stale-row guard) generalized to checker
  doctrine; source lane card `.sessions/2026-07-12-tournament-entry-race-fix.md` § 💡 +
  heartbeat @ `80464ab`; adjacency (distinct scope) noted to
  `ideas/superbot/warn-first-checker-authoring-kit-2026-07-10.md`.
- `ideas/superbot-next/oracle-copy-punctuation-drift-sweep-2026-07-12.md` — grep
  rebuild user-copy literals vs oracle search_code fragments for punctuation-level
  drift in golden-uncovered refusal paths (live datapoint: "You're already registered."
  vs oracle "…!", `sb/domain/rps/tournament.py:153`); source same lane card § 💡,
  second half, @ `80464ab`.

**3 link-indexed** (new "Lane backlog (by link)" block in
`ideas/superbot-next/README.md` — link + one-line honest gist + lane-side state, no new
files; exact filenames verified against the lane's `docs/ideas/README.md` @ `80464ab`):
`port-the-small-four-2026-07-10.md` (utility/general ported; anomaly flagged — paragon
has NO row in `parity.yml` at the pin) · `blackjack-remaining-surface-2026-07-10.md` ·
`rps-tournament-remaining-surface-2026-07-10.md` (both: PvP/tournaments shipped
#124/#130/#133; remainder unpinned polish).

**2 skipped on purpose** (recorded here, not as idea files): the btd6 `_run_op`
latent-bug guard — a ledgered bug + guard recipe, not idea-shaped; and the kernel-band
golden mint — a named follow-up work item the lane already tracks (`parity.yml` lines
113–116 at the pin), not a harvestable idea.

**Dedup verdicts:** D-0027/D-0048 advisor deferrals and the D-0056 plugin contract —
already covered by existing heads, no new capture; the lane's
`docs/ideas/ensure-only-registration-gaps-2026-07-10.md` deliberately NOT link-indexed
(already tracked by
`ideas/superbot-next/composition-parity-registration-diff-2026-07-10.md`).

Coordinator-imposed deviations, declared (the PR #222-family dispatch boundary):
NOTHING under `control/` written by this slice (no claim file, no heartbeat) —
section-collision risk was declared in this card's born-red first commit instead; PR
opened DRAFT, parked READY on green, never self-merged (the kit-owned auto-merge
workflow lands it).

Files touched: 3 new idea files, `ideas/superbot-next/README.md` (3 index rows + the
lane-backlog block), this card. No code, no `control/`.

## Verification (real runs, this tree)

`python3 bootstrap.py check --strict` green and full `python3 scripts/preflight.py`
(10/10 checks) green immediately before push, after this card's complete-flip (the
three SIM-VERDICT numbering-cross warnings are the known deliberate legacy advisories).
The kit auto-draft `.sessions/2026-07-12-session.md` and the
`.substrate/guard-fires.jsonl` hook residue stay uncommitted (session machinery /
telemetry lane, per the phase-1 handoff precedent).

**📊 Model:** fable-5 · medium · bounded harvest write slice (3 captures + section
index + link-index block + card; no scripts, no workflows, no proposal — task-class:
recon-directed harvest write)

## 💡 Session idea

**A harvest watermark should live in a machine-readable place, not in a prior card's
prose.** This sweep's watermark (`910c44e` @ 2026-07-11T08:13:45Z) had to be excavated
from lines 29–31 of the previous session card — a re-derivation cost every future
sweep of every lane section will pay again. One `.harvest-watermark` line per section
(or a row in the existing `.harvest-pin.json` mechanism `check_harvest.py` already
owns for canonical-dir sections) would make "what's new since last harvest?" a diff
command instead of an archaeology pass — and `check_harvest.py`'s SECTIONS table shows
the shape: superbot-next isn't even registered there because its harvest source is
session cards + heartbeat, not a canonical `docs/ideas` dir; a watermark record is the
lighter-weight equivalent for card-sourced lanes.

## ⟲ Previous-session review

Reviewed: `.sessions/2026-07-11-superbot-next-four-head-verify-sweep.md` (this
section's predecessor slice). Its verify-first discipline (one `ls-remote` sweep
serving all reports, re-confirmed unmoved before authoring) was adopted here verbatim
— the pin was re-verified live at 01:34:18Z rather than trusting the recon pass's
read. Its card also carried the watermark this sweep needed, which worked but only as
prose (see 💡 above). One workflow improvement over it: this slice split born-red card
/ content / complete-flip into three logical commits, so the in-flight window is
visible commit-by-commit rather than landing as one opaque squash-side diff.

## Handoff → next wake

New watermark for the NEXT superbot-next harvest sweep: lane pin `80464ab` @
2026-07-12T01:34:18Z. The section now carries 3 fresh `captured` heads (this sweep) +
4 parked (the 2026-07-11 verify sweep) — the captured heads are probe-eligible; the
lane's fast cadence (verified again: #221/#223 shipped within a day of each other)
argues for verify-first at the then-live HEAD before any battery, per the predecessor
card's vindicated rule. The paragon-missing-from-parity.yml anomaly flagged on the
port-the-small-four link row is lane-side information the manager's sweep may want to
relay. Skipped-on-purpose items (btd6 `_run_op` guard, kernel-band golden mint) need
no follow-up here — both live lane-side.
