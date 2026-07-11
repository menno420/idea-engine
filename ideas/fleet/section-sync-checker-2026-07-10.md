# Manifest-derived section sync checker

> **State:** historical(#2)
> **Class:** process · **Target:** `menno420/idea-engine` (this repo's own tree — built here, see report Q7)

**Origin:** the seed session's 💡 (`.sessions/2026-07-10-seed.md`) — the section convention
(README § Sections: one `ideas/<section>/` per active fleet lane) shipped as prose-only at
seed, which is exactly the drift class superbot documented (#880→#882: a convention without
its checker drifts before the next session reads it).

**The idea:** a tiny stdlib-only `scripts/check_sections.py` that diffs the `ideas/<section>/`
directories against the **active lane rows of the fleet manifest** (superbot
`docs/eap/fleet-manifest.md`, read-only via the public raw path per Q-0260) and reports
drift both ways: **missing** sections (active lane, no directory) and **orphan** sections
(directory, no active lane). Grounded in the real manifest at capture time: a 14-row
`| Project | Repo(s) | … |` table where activity is textual (three `Project CLOSED` rows,
one `repos NOT created` row) and row names ≠ repo names (`manager`→fleet-manager,
`games-plugins`→superbot-games, `kit-lab`→substrate-kit) — so section derivation must come
from the Repo(s) cell, with the manager row excluded (control chair, not a build lane) and
`fleet` always expected (README-mandated cross-cutting section, not a manifest row).

## Probe report (v0, 2026-07-10)

**1. What is this really?**
A drift detector for a cross-repo convention: it turns README § Sections' prose rule ("a
new active lane row in the manifest → the wake that spots it creates the section; never
invent a section ad hoc") into a one-command checkable invariant. The section tree is this
repo's collision-avoidance mechanism for parallel agents (claims assume the partition is
authoritative), so this is really a guard on the repo's concurrency model, not a tidiness
tool.

**2. What is the possibility space?**
Four axes: **action** (report-only → scaffold the missing section README automatically →
open the PR itself); **integration** (manual script → routine-wake preflight step → a
`bootstrap.py check` seam → CI gate step); **source format** (parse today's hand-maintained
markdown table → consume the proposed generated-from-heartbeats roster when fleet-manager
ORDER 009 lands — the manifest header itself says the current file is slated to die);
**generalization** (any repo whose directory tree mirrors an external manifest — a
substrate-kit candidate pattern, cf. the probe-report lint idea in
`.sessions/2026-07-10-first-probe.md` §💡).

**3. What is the most advanced capability reachable by the simplest implementation?**
A ~130-line stdlib script gives every wake a one-command answer to "is my section tree
current?", including the case prose review essentially never catches: a lane *closing*
(its section silently becoming an orphan). It also makes the derivation rules — which
manifest rows count, how a row maps to a section name — explicit, loud code instead of
seed-session folklore; the special cases (manager row, `fleet`, textual CLOSED markers)
are now written down where they execute.

**4. What breaks it?**
- **Manifest format drift** — the source is a hand-maintained living ledger whose header
  already announces its replacement (generated roster, ORDER 009). The parser fails LOUD
  (exit 2 on zero parsed rows) because a false clean is worse than a crash, but a format
  change that still parses (e.g. column reorder keeping a `|` table) could misread rows.
- **Activity heuristics** — "active" is inferred from text (`Project CLOSED`, presence of
  a `menno420/<repo>` in the Repo(s) cell). A new closure phrasing would count a dead lane
  as active (drift noise, fail-safe direction) — acceptable for a reporter, wrong if it
  ever auto-scaffolds.
- **Mapping ambiguity** — the manager-row exclusion and the `fleet` add-on are judgment
  calls encoded as constants; if the fleet reorganizes (e.g. the manager grows a lane),
  the constants silently mislead until edited.
- **Network dependence** — default path fetches the raw URL; `--manifest FILE` covers
  offline/CI runs. It is a read of another repo at HEAD, so a mid-rewrite manifest can be
  transiently inconsistent.

**5. What does it unlock?**
Honest partitioning for parallel agents (the claims protocol rests on the section tree
being right); the repo's first `scripts/` entry, setting the pattern for the sibling
probe-report lint idea; and the precondition for any future auto-scaffolding wake step
(you can only auto-create sections once detection is trusted).

**6. What does it depend on?**
Public raw availability of superbot's manifest (or a saved copy via `--manifest`); the
manifest keeping a parseable `| Project | Repo(s) |` table until the generated roster
replaces it (then: update `active_sections()`); the `ideas/<section>/` layout convention;
python3 stdlib (already the kit interpreter, `substrate.config.json`).

**7. Which lane should build it?**
**idea-engine — this repo, directly.** It checks this repo's own tree, and only this
repo's sessions write here (Q-0260); no other lane can even land the fix. Not
substrate-kit: the kit is fleet-generic, this is fleet-manifest-specific (the
generalized "tree mirrors external manifest" pattern in Q2 could graduate to the kit
later, as its own idea).

**8. What is the smallest shippable slice?**
`scripts/check_sections.py`, report-only, exit 1 on drift, `--manifest` for offline —
about 130 lines, stdlib only. Cheaper to build than to route: it shipped **in this same
PR** and ran green against the live manifest and the seeded 10-section tree (smoke output
in `.sessions/2026-07-10-section-sync-checker.md`).

**Recommendation: park** — rationale (build-here deviation, flagged): the battery's four
labels have no "build directly in this repo" outcome and the README grammar admits exactly
one of the four, so `park` is the closest label in routing terms — *nothing goes to
sim-lab* (a trivial stdlib reporter is cheaper to build than to simulate; no reproducible
question exists worth a sim-lab cycle) — while the true disposition is BUILT: the slice
ships in this PR and the state line advances to `historical(#2)` on merge, which the idea
grammar does permit.

## Extension note (2026-07-11, appended — probe report and state untouched)

The checker's own anticipated failure mode fired live: the hand-maintained fleet
manifest was SUPERSEDED mid-day by the fleet-manager GENERATED roster
(`docs/roster.md`, regenerated each manager wake — fleet-manager PR #59, merge
`b0639a9`; the manifest's table was REMOVED, leaving only the supersession banner),
so the manifest parse hit its fail-loud path exactly as designed ("no table rows
parsed — manifest format changed? (it is slated to be replaced by a generated
roster; update this parser, do not trust this run)") and redded every non-control
PR's gate in this repo. The parser was updated the same session, per its own error
message:

- **Canonical source flipped to the roster** (`fleet-manager docs/roster.md` raw
  path; format auto-detected by table header — `| Lane |` = roster, legacy
  `| Project |` manifest parse retained for offline copies of the historical file).
- **Roster row semantics, fail-loud preserved:** Lane-cell display decorations
  stripped (`**bold**`, `(hub)`, `(NEW)`, `· Seat A`); registry-only seats skipped
  only when the Lane CELL declares "NO repo" (a full-row substring match
  false-positived on superbot's "No repo wake trigger" prose — caught live in the
  first run); wound-down lanes skipped ("wound down"/"wind-down complete" markers);
  an unreducible lane cell RAISES (never a silent skip); zero rows RAISES.
- **NON_LANE_REPOS extended** with loud comments: `sim-lab` (the pipeline's verdict
  stage per Q-0264, not a build lane — no section has ever existed) and
  `idea-engine` (this repo itself — its process ideas live in `ideas/fleet/`,
  established practice) join `fleet-manager`.
- **Three new sections seeded** per README § Sections (the wake that spots a new
  active lane creates the section, README stub first): `ideas/product-forge/`,
  `ideas/superbot-idle/`, `ideas/superbot-mineverse/` — the roster surfaces live
  lanes the stale manifest never rowed. Post-fix run: 13 sections in sync.
