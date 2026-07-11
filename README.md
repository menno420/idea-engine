# idea-engine — the fleet's ideation lab

> **Status:** `binding` — this README is the repo's pipeline contract. Founding design:
> owner ruling **Q-0264** (superbot `docs/owner/maintainer-question-router.md`); founding
> package: superbot `docs/planning/round3-founding-package-idea-engine-2026-07-10.md` (v2).
> Seeded 2026-07-10 by the dispatch copilot (superbot round-3 session, kit v1.7.0).

This repo generates, captures, harvests, probes, and grooms **ideas for the whole fleet**
so every idea eventually becomes evidence-checked and built, explicitly parked, or
rejected — never orphaned. It builds no products and finalizes no verdicts.

**Pipeline position (Q-0264):**
`idea-engine` (generate/probe, mark sim-ready) → **sim-lab** (reproduced-evidence verdict:
validity gate + @codex review) → **fleet manager** (final review, routes ORDERs) → lanes
build. This repo is the only repo its sessions write (Q-0260); everything else is read via
the public raw path.

## Sections — `ideas/<section>/`

One section per **active fleet lane**, derived from the fleet's canonical lane
registry — since 2026-07-11 that is the fleet-manager GENERATED roster
(`docs/roster.md`, regenerated each manager wake), which superseded the original
hand-maintained fleet manifest (superbot `docs/eap/fleet-manifest.md`; the manifest
file itself carries the supersession banner, fleet-manager PR #59 `b0639a9`) — plus
`ideas/fleet/` for cross-cutting workflow/doctrine ideas. Never invent a section ad hoc: a new active lane row in the
registry → the wake that spots it creates the section (README stub first). Sections
partition the tree so **parallel agents never collide** — claim a section before working
it (`control/claims/`, one file per claim — the kit-native v1.8.0 home; the original
root `claims/` was migrated there wholesale by the v1.8.0 upgrade, see
`control/claims/README.md` § idea-engine specifics).

Idea classes worked here (all three, priority-weighted per Q-0259 — games completion wave
+ rebuild pace first): **PRODUCT** (features for a lane), **PROCESS** (fleet
workflow/doctrine), **VENTURE** (revenue plays).

## Idea file grammar

`ideas/<section>/<slug>-YYYY-MM-DD.md`, starting with a state line:

```
> **State:** captured | probed | sim-ready | parked(<reason>) | rejected(<reason>) | historical(<merged PR>)
> **Class:** product | process | venture · **Target:** <lane repo>
```

States move forward only; probe reports are **appended**, never rewritten; parked and
rejected ideas keep their file with the reason — the trail is the product. Harvested
lane-born ideas are indexed **by link** into their section, never mass-copied
(superbot's `docs/ideas/` stays canonical where it is — see `ideas/superbot/README.md`).
Sibling-section cross-links reuse that rule: a section README may carry a `Cross-links`
subsection indexing another section's idea **by link**, never duplicating it (source:
PR #17 card). A link-index entry whose LOCAL state deliberately diverges from the
canonical doc's recorded outcome may carry an optional
`(state-drift: deliberate — <reason/PR>)` annotation on its index bullet, which
`check_harvest --states` reports as ACK'd rather than open drift (source: PR #149
card 💡; forward-only — never retrofit). Two more badge duties, both forward-only: a
badge or annotation writing "partially implemented/built" names the built half AND
the open half, one clause each — a badge that forces the split makes the next
reader's premise-verify a confirmation, not an investigation (source: PR #189 card
💡); and when the canonical text names its own trigger event ("build when X", "next
time Y"), the harvest carries that trigger into the index badge, so ripeness
re-ranking becomes a scan for fired triggers instead of a re-read of the canonical
docs (source: PR #192 card 💡).

Two OPTIONAL header lines are blessed (forward-only — retrofit never required):
`> **Grounding:** <url>@<sha> · fetched <ISO time>` pins what a capture was grounded on,
machine-readably, with `(manifest row: behind|matches|ahead)` appended when a lane pin
diverges from the manifest's recorded HEAD (shaped by the PR #8/#10/#12/#14/#15 cards);
when version-truth layers disagree, cite the freshest and note the divergence —
manifest row < lane heartbeat < lane HEAD/tree-scan, freshest wins (source: PR #19
card; twelve live manifest-staleness datapoints, the sharpest a manifest row
prescribing a fix its lane had deliberately archived). Rich pin context
(capture-vs-recheck provenance, manifest-row detail) goes on an OPTIONAL
`> *(pin annotation: …)*` blockquote line directly below the pin, never inside it
(source: PR #28 card; four live instances).
`> **Sequence:** <before|after|behind> <event/order/claim>` records an ordering
constraint a probe would otherwise re-derive from prose (source: PR #10 card); a
cross-repo order dependency uses the token form `<repo>#ORDER-<nnn>` in the Sequence
body (e.g. `after superbot-next#ORDER-002`) so one grep surfaces every idea in the
tree blocked on a given foreign order (source: PR #44 card; forward-only — never
retrofit prose-form instances). A harvest slice stamps the `Sequence:` line **at
capture time** whenever the source names a hard date/event — an expiry that lives
only in status-file prose is invisible to the expiry-aware probe order below
(source: PR #174 card 💡, which had to retrofit its own). A DARK
lane (unreadable from this repo) gets manifest-relayed grounding only: pin the manifest
at superbot HEAD, verify the blackout, and scope captures to shape-not-content (source:
PR #15 card).

A finalized sim-lab verdict is recorded by appending a `## Sim verdict (<date>)`
section — the canonical post-verdict marker: cite the verdict number, ruling, and the
sim-lab `control/outbox.md` SHA read at write time, plus the numbering cross
(`VERDICT <n> = PROPOSAL <m>` — sim-lab numbers by intake order, not proposal number).
The state line stays forward-only and untouched; the note, not a new state, is what
says "verdict received" (source: PR #41/#43 cards; four live instances). The note
quotes the verdict's `ruling:` field when present, else its `recommendation:` — the
parse rule every fan-in otherwise re-derives from card archaeology (source: PR #178
card 💡; exercised across V005–V008).

## The probe battery (v0 — the core method)

One idea per pass, through the fixed interrogation:

1. What is this really?
2. What is the possibility space?
3. What is the most advanced capability reachable by the simplest implementation?
4. What breaks it?
5. What does it unlock?
6. What does it depend on?
7. Which lane should build it?
8. What is the smallest shippable slice?

Reachability check (battery Q4/Q6 discipline): an idea pricing an export/feed slice
must verify where the data actually lives vs what the named producer can actually
read, and an idea pricing an owner action must verify a zero-toolchain surface
actually carries the action's object — pattern-exists is not pattern-can-produce
(source: PR #45/#34 cards). Verify-first greps must stem-match, never exact-match:
grep the symbol's STEM (`extra_check`, `host_check`) and treat any near-named hit as
read-the-body-required — an exact-match grep returns a false absent on a false-friend
symbol (source: PR #141 card, the `_extra_check_findings` false friend).

Append the output as `## Probe report (v0, <date>)` in the idea file, ending in **ONE**
recommendation — `sim-ready` / `park` / `reject` / `needs-more-grooming` — with a one-line
rationale. One legitimized shortcut: repo-internal PROCESS tooling whose smallest slice
(Q8) is trivial may be probed and built **in the same PR** — recommend
`park(built-here — <what shipped>)`, route nothing to sim-lab, and advance the state to
`historical(<merged PR>)` on merge (first used by PR #2's section-sync-checker; deviation
flagged in its probe report, `ideas/fleet/section-sync-checker-2026-07-10.md`, and
`.sessions/2026-07-10-section-sync-checker.md`). **Panel mode default (sim-lab
VERDICT 002, approve-selectively):** single-pass is the default probe; escalate to panel
(parallel subagent lenses + one synthesizer) ONLY when (a) a quick 2–3× repeat of the
single pass disagrees with itself (ambiguity signal), or (b) the idea has
irreversible/high-blast-radius surface (security/data/spend/public); always-on panel is
rejected. Measured basis: panel flipped the modal verdict on 2/3 contested ideas at
4.00× agents / 3.05× tokens / 1.61× wall (sim-lab `control/outbox.md` VERDICT 002 @
`8713f26`, report `sims/intake-001-probe-panel-vs-single-pass/`); live datapoint: this
repo's one panel run (PR #23, explore-hub) cost ≈127k lens tokens. Honesty norm
("not measured" beats invention) holds in both modes. Reference example: the first
probe (see `ideas/superbot/`).

Probe order is expiry-aware: a captured idea whose `Sequence:` reads `before <event>`
(or whose "why now" names a closing window) is probed — or explicitly re-pinned —
ahead of non-expiring heads once the event is imminent; a dead premise re-confirms
itself from stale grounding, and only a live lane-HEAD check breaks the loop (source:
PR #48/#25 cards — one capture missed a window by ~4 h, another was mooted overnight).

Verify-first is also cross-lane- and tree-aware. For any idea whose `**Target:**`
differs from its canonical repo, verify-first includes the target lane's decision
ledger — grep its `docs/decisions.md` for the idea's nouns — BEFORE the head is
ranked #1: a 2-day-stale capture cost a full probe that a 30-second ledger grep
would have priced (source: PR #180 card 💡). Absence from a lane's
`current-state.md` is NOT evidence of absence: grep the canonical repo's
`docs/subsystems/` folio index AND its code tree (blobless-clone ls-tree) for the
idea's nouns — three consecutive probes found the truth in folio/tree/ledger where
current-state prose missed (source: PR #183 card 💡; re-confirmed at #186/#189).
And body-exists is not body-wired: when confirming "a guard/checker exists at
target", read the REGISTRATION/invocation site (registry entry, config key, CI
wiring) and confirm the widened parameter actually flows — a call-site default
override kept a shipped scope-widening silently inert (source: PR #186 card 💡, the
Rule 6 `roots=` lesson; drift confirmed still live by sim-lab VERDICT 010).

Probe order is also self-serve-aware: a maintenance-shaped capture aimed at a LIVE lane
is often executed by that lane before the probe runs — four datapoints (~19 min on
websites PR #79 per the #49 card; twice in ~24 h per the #51 card, covering BOTH arrival
paths — harvested bullet and seeded capture; 14 min / ~19 min / hours per the #53 card,
two of three self-serves within ~20 minutes) — so for that shape, budget a five-minute
verify-and-park FIRST at lane HEAD, escalating to a full battery pass only if the live
check finds the slice unexecuted. The verify step keys on the capture's INVARIANT, never
its named artifact: a lane can execute the mechanism without executing the fix, and a
fingerprint-grep returns a false MOOT (the #56 card's lesson — rebind-then-delete shipped
without fresh-session-per-fire). Independent convergence is evidence the capture
heuristic aims true, not wasted work (#51 card). (source: PR #49/#51/#53/#56 cards)

## The outbox — `control/outbox.md`

Sim-ready ideas become **append-only** outbox entries in the kit ORDER grammar:

```
## PROPOSAL <nnn> · <ISO8601> · status: sim-ready
target: sim-lab
idea: <link to the idea file @ HEAD>
question: <the ONE thing the simulator should settle>
done-when: <what a verdict must contain>
depends: <OPTIONAL — cross-lane/cross-repo dependency: providing lane + known co-consumers>
```

`depends:` is OPTIONAL and forward-only (the outbox is append-only — never retrofit old
entries): when a probe names a cross-lane dependency, naming the providing lane and any
known co-consumers makes fan-in visible to the manager's :30 sweep without a code search
(source: PR #5 — PROPOSAL 002's stats phase and product-forge's games-web ORDER 001 both
wait on the same superbot read-only API).

`sim-lab` pulls sim-ready entries directly (public raw) on its wakes; the **manager**
handles everything after the simulator's verdict. This repo never writes another repo's
files.

## Landing conventions (gen-3 standard, day-0)

- PRs open **READY, never draft**; born-red session card per the kit gate
  (`.github/workflows/substrate-gate.yml`).
- **This lane always lands its own PRs**: arm auto-merge at PR creation where checks can
  go pending; REST merge-on-green is PRIMARY on born-red states (blueprint R21). Arm only
  once the branch is FINAL — heartbeat and any claim-clear already in-branch; the ~16s
  merge loop out-races later commits (the PR #2/#3 lesson).
- **No PR ever waits for review before landing** — needs-second-eyes → merge anyway + a
  `review-queue.md` line and/or an @codex PR comment (Q-0258; verify replies against the
  tree, never obey — Q-0120). Review is post-merge; veto = revert; forward-only git.
- **Sibling landed mid-flight** (rejected push or `control/status.md` conflict):
  `git fetch origin main && git merge origin/main` into the branch — forward-only, never
  rebase — reconcile the heartbeat keeping both sides' facts (yours win for your own
  fields), rerun the preflight, push again (proven across PRs #10–#17). Shared monotonic
  counters in the heartbeat (e.g. manifest-staleness datapoint numbers) collide by number
  when siblings land — earliest-merged keeps the number, the later slice renumbers its
  own (source: PR #52's merge commit 516bdab).
- Verify before push: `python3 bootstrap.py check --strict`.
- Wake preflight in one command: `python3 scripts/preflight.py` — runs the whole ritual
  (sections + ideas + outbox + control status gate), one PASS/FAIL line per check,
  exits with the worst code.
- **`.github/workflows/substrate-gate.yml` is KIT-OWNED**: any `bootstrap upgrade` or
  `adopt` that regenerates it silently drops the PR #18 `wake preflight` step, and the
  step must be re-applied before push; PR #36's gate-wiring self-check reds the next
  preflight if the step is missing (executed live three times: PRs #35, #54, #55).
- Repo conventions override harness defaults.

## Coordination

`control/` is the bus (see `control/README.md`): `inbox.md` manager-written ORDERs ·
`status.md` coordinator-only heartbeat (overwrite as the deliberate LAST step of every
session) · `outbox.md` this repo's append-only proposals. A grooming slice's heartbeat
overwrite must re-state every standing-seed tracker it consumed — encoded → where,
skipped → why — so no future harvest re-derives a stale list (source: PR #50 card 💡,
practiced by round 3).

**Operating cadence (owner ruling, 2026-07-10):** the coordinator chains bounded slices
**continuously** via child sessions — the next slice dispatches as each one reports. The
2-hourly trigger is a **failsafe deadman wake**, not the work cadence. Every slice still
lands as one merged-on-green PR (§ Landing conventions). (Ruling first recorded live in
`control/status.md` @ 139932e.)
