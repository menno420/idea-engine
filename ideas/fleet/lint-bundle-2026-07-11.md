# Lint bundle — five standing advisory lint heads, accumulated across session cards

> **State:** park(built-here — five advisory heads: RECOMMENDATION + STATE-ECHO in `scripts/check_ideas.py`, `--states` in `scripts/check_harvest.py`, `--step-anchor-drift` + `--heartbeat-keys` in `scripts/preflight.py`, this PR)
> **Class:** process · **Target:** `menno420/idea-engine`
> **Grounding:** https://github.com/menno420/idea-engine/blob/2aa4a4bb852e0b0dc17bfba4cf7cf9e4f85df6ea/.sessions/2026-07-11-contract-grooming-round-4.md@2aa4a4b · fetched 2026-07-11T09:26Z

**Origin:** five session-card 💡s that each named a small, hermetic-or-flag-gated lint
and were each deliberately deferred as "a build slice, not grooming" — accumulated on
the standing ripest list across rounds 3–4 and finally bundle-named by the PR #59 card
("pairs naturally with the PR #36/#29/#33 lint bundle if a lint slice ships") and the
PR #144 card's grooming ledger (item (c): the lint-bundle build slice). The five heads,
each with its source card:

1. **Step-anchor drift** — PR #36 card 💡
   (`.sessions/2026-07-10-preflight-gate-selfcheck.md`): the gate-wiring self-check
   matches its anchors as byte strings, so a deliberate gate-step rewording that
   forgets the `PREFLIGHT_RUN`/`NON_CONTROL_GUARD` co-edit either FALSE-reds later
   (reworded run line) or FALSE-greens (run line kept, guard semantics dropped —
   e.g. the guard bytes survive in a comment while the step's `if:` changed).
2. **Cross-link state-echo** — PR #29 card 💡
   (`.sessions/2026-07-10-seat-boot-harness-probe.md`): state echoes on
   index/cross-link lines in OTHER files are exactly the annotation class that rots
   when a state advances later; `check_ideas.py` already parses every idea's state
   line, so a small pass can diff any `— <state> ·` annotation against the linked
   file's actual current state (warn-first). Target set GROWN live by the PR #33
   card (three new echoes) — and this build's live run found six rotted echoes.
3. **Recommendation-vocabulary** — PR #33 card 💡
   (`.sessions/2026-07-10-capability-pair-probe.md`): a `**Recommendation:` line
   OUTSIDE any `## Probe report` block is never shape-checked (blocks split on
   `PROBE_HEADING_RE`), which that slice leaned on legitimately for a pointer
   disposition — but the same hole lets a malformed recommendation ride in prose
   unlinted; hold ANY such line file-wide to the legal vocabulary (warn-first
   outside probe blocks).
4. **`check_harvest --states`** — PR #22 card 💡
   (`.sessions/2026-07-10-harvest-freshness-checker.md`): the checker diffs
   EXISTENCE only; an indexed `captured` entry whose canonical doc has since
   advanced to built drifts invisibly. Fetch each indexed doc's canonical state
   marker at HEAD (batched via the same blobless clone, flag-gated — blobs needed)
   and diff against the entry's recorded state. `--re-badge` (PR #37 card, built by
   PR #47) bounded itself to front-matter built-outcome markers ONE direction; "the
   full `--states` depth stays unbuilt per the PR #22 card 💡" (PR #47 card,
   verbatim).
5. **Undeclared-heartbeat-key tripwire** — PR #59 card 💡
   (`.sessions/2026-07-11-contract-grooming-round-4.md`): extension keys accrete
   faster than out-of-repo parser runs happen, so the leak class is only ever
   measured one key behind (`routine:` was caught only at round-4's first live
   enforcement — a write-time tripwire would have caught the fold-in miss at
   write time). Parse the heartbeat's top-level `<key>:` tokens against the
   control/README format block's documented set — hermetic, advisory, never red.

**Dedup:** grep swept `ideas/fleet/` + `scripts/` before capture (rg, bootstrap.py and
.substrate excluded): no lint-bundle file exists; none of the five heads is built —
`check_ideas.py` checks recommendation vocabulary only INSIDE probe blocks and skips
README.md files entirely (no state-echo pass), `check_harvest.py` has `--re-badge` but
no `--states` (the PR #47 card names the depth unbuilt, verbatim above),
`preflight.py` has the binary `--gate-wiring` byte check but no anchor-drift advisory,
and no heartbeat-key check exists anywhere (`bootstrap.py check --strict --status-only`
gates presence/staleness/fields, not key declaration — the round-4 encode is prose
only). All five heads live.

## Probe report (v0, 2026-07-11)

**1. What is this really?**
Five deferred 💡s that are all the same move: a convention this repo already relies on
(gate anchors · index badges · recommendation grammar · outcome mirroring · heartbeat
key grammar) enforced by session discipline alone, each with a measured or lived rot
case, each turned into a checker the existing wrappers already run. Not five ideas —
one idea instantiated five times: "turn the contract sentence into a tripwire"
(the PR #59 card's own phrase). Bundling is the point: one PR, one claim, five
convention→checker conversions sharing the established advisory/exit conventions.

**2. What is the possibility space?**
Per head: severity (advisory → date-gated hard → hard), placement (check_ideas /
check_harvest / preflight / the kit's own `check` seam), and depth (byte-anchors →
semantic parse; family-compare → full-reason compare; one heartbeat file → all
declared `heartbeat_files`). Across heads: stay five local checks, or route the
fleet-generic ones upstream (heartbeat-keys and step-anchor-drift are both
kit-seam-shaped — the kit owns the heartbeat grammar and the gate template; the
substrate-kit section already carries the one-grammar/one-parser family:
`host-checkers-one-gate`, `heartbeat-ladder-field`, `own-heartbeat-parse-self-check`).
Terminal state: the kit's generator seam absorbs the gate-anchor class entirely
(`check_gate_wiring` and this advisory both retire — the PR #36 card said so of the
binary check already).

**3. What is the most advanced capability reachable by the simplest implementation?**
Every convention named above stops depending on memory THIS wake: ~230 lines of
stdlib across three existing scripts, zero new files, zero workflow edits (preflight
CHECKS is the one wired list — two new advisory entries ride the existing gate step),
zero network added to any default run (`--states` is flag-gated behind the same
blobless-clone batch `--re-badge` already pays). The live run proved the value at
build time: six rotted state echoes found (all six fixed in this PR) and one real
lifecycle divergence surfaced (`open-pr-awareness-at-wake`, deliberately parked
locally while the canonical doc records built — reported, judgment-laden, NOT
auto-fixed: exactly the suggestion-pass honesty `--re-badge` established).

**4. What breaks it?**
- **Echo-position ambiguity** — index entries carry state words in gist prose
  ("probed 2026-07-10", "still `captured` @"); the echo regex anchors on `— `/`· `
  position and takes the FIRST hit after the link, calibrated against all 310 live
  entries (303 ok · 6 true mismatches · 1 echo-less). A future entry form could
  still dodge it — advisory severity makes that a missed warning, never a false red.
- **Family-compare blindness** — `parked(routed)` echoing a file that moved to
  `parked(build-direct …)` passes (same family). Deliberate: the rot class is a
  family advance; reason-detail drift is judgment territory.
- **Canonical marker vocabulary drift** — `--states` maps
  `state:/status:/shipped_pr:` onto three lifecycle stages; a canonical repo
  inventing a new token lands in "open" silently. Mitigated: the stage map is a loud
  co-edit constant block, and the finding text quotes the marker verbatim.
- **Anchor-advisory self-reference** — `--step-anchor-drift` shares the constants it
  polices; a co-edit that changes BOTH constants wrongly stays green. The gating leg
  (`--gate-wiring`) and CI's real behavior remain the backstop.
- **Advisory fatigue** — five more warn-lines per wake if findings accrete unfixed;
  the fix cost is one badge edit each, and the live run lands at zero warnings.
- **Kit regen** — none of the five touches a KIT-OWNED file; preflight/check_ideas/
  check_harvest are host-owned scripts. No new re-apply duty created.
- **`--states` false drift on deliberate divergence** — the open-pr-awareness case:
  a lane self-serving a slice does not always flip the local park verdict. That is
  why the head is a suggestion pass (report-only, harvester judges), never an
  auto-editor.

**5. What does it unlock?**
Index badges, prose recommendations, gate-anchor co-edits, outcome mirroring, and
heartbeat key grammar all become machine-checked the same wake they drift — the
five recurring by-hand sweeps the cards each priced retire. The heartbeat-keys head
additionally arms the round-4 contract sentence (fold-in over declare) as a
tripwire, and both preflight heads produce the working reference implementations the
substrate-kit routed heads can absorb (the `--branch-prefix-drift` → kit-check
precedent, verbatim).

**6. What does it depend on?**
This tree only, for four heads (stdlib, local files, the existing advisory/exit
conventions); `--states` additionally depends on the canonical repos' git transport
(the same ls-remote + blobless-clone recipe `check_harvest` already uses — network
walls degrade to exit 2 could-not-run, never a false clean) and on canonical
front-matter markers staying in the `state:/status:/shipped_pr:` family. No kit
change, no workflow edit, no new wiring (preflight CHECKS is the single edit point,
per its own loud comment).

**7. Which lane should build it?**
idea-engine, this repo, this PR — all five lint this repo's own artifacts against
this repo's own contracts, and only this repo's sessions can land the fixes they
report (the check_ideas/check_sections/preflight precedent, three times over). The
fleet-generic residues (heartbeat-key declaration and gate-anchor survival as KIT
checks) are already routed on the substrate-kit section's existing heads
(`own-heartbeat-parse-self-check` cross-link · `host-checkers-one-gate`) — nothing
new to route, this build adds the reference implementations those heads cite.

**8. What is the smallest shippable slice?**
Exactly this PR: RECOMMENDATION (outside-block vocabulary, warn) + STATE-ECHO
(README index/cross-link family diff, warn) in `scripts/check_ideas.py`;
`--states` (flag-gated, both-direction lifecycle-stage suggestion pass) in
`scripts/check_harvest.py`; `--step-anchor-drift` (both drift legs, advisory) +
`--heartbeat-keys` (declared-set tripwire over `heartbeat_files`, advisory) as
ninth/tenth CHECKS entries in `scripts/preflight.py`; six rotted index badges
re-badged (the live findings); planted-violation smoke per head (all five fired,
plants removed). ADVISORY-first throughout — nothing new can red a legacy file
(the PR #24 date-gate pattern's spirit; here every head is warn-only because
READMEs/heartbeats/gates carry no filename date to gate on, and the outside-block
recommendation is a legitimate pattern to warn on, not red).

**Recommendation: park(built-here — five advisory lint heads across check_ideas.py, check_harvest.py, preflight.py, this PR)** —
rationale: repo-internal PROCESS tooling whose smallest slice is a bounded stdlib
extension of three existing checkers, proven by its own live run + five planted
violations in this same PR (the README battery shortcut, PR #2/#11/#16 lineage);
nothing sim-shaped, so no outbox proposal — a contract check is proven by its own
red/green (the #114 precedent).
