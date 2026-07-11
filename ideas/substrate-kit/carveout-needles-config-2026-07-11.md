# Host-declared carve-out needles — close the scan's step-blindness class

> **State:** parked(routed — substrate-kit lane build, manager-ORDER-worthy: host-declared `carveout_needles` checked by the kit's OWN carve-out scan; verified un-adopted at live kit HEAD `09837de` — empty `[Unreleased]`, no v1.11.0 tag, `gate_carveouts` still step-granular in code — see probe report)
> **Class:** process · **Target:** `menno420/substrate-kit`
> **Grounding:** https://raw.githubusercontent.com/menno420/idea-engine/b11fe689c62838bde257dc37997bfba026b9e216/scripts/preflight.py@b11fe68 · fetched 2026-07-11T07:22:00Z
> **Grounding:** https://raw.githubusercontent.com/menno420/idea-engine/b11fe689c62838bde257dc37997bfba026b9e216/.sessions/2026-07-11-kit-upgrade-v1.10.0.md@b11fe68 · fetched 2026-07-11T07:22:00Z
> *(pin annotation: `b11fe68` IS the #125 squash — the v1.10.0 hop; the first pin is the
> stopgap this capture wants superseded (`ENABLER_ANCHORS` byte-needles + `check_enabler_anchors`,
> ~lines 322–379), the second is the card recording the SECOND step-blind miss, the
> advisory-mode decision, and the promotion condition)*

## Problem

The kit's carve-out scan (the `bootstrap upgrade`/`adopt` pass that names host
customizations about to be clobbered on KIT-OWNED files) is **STEP-granular: it names a
whole host-ADDED step but is blind to host edits INSIDE a kit-owned step** — so an
upgrade regenerates the file, silently drops the in-step edit, and nothing red points at
it. Evidenced on TWO consecutive hops of this repo's auto-merge enabler:

- **v1.9.0 hop (PR #120, squash `f417a1f`):** the scan named the PR #86 card-status
  guard step but NOT the `Head-ref:` `--body` squash-provenance edit inside the kit's
  own arm step — the PR's customization-survival table records it verbatim: "DROPPED —
  **NOT named by the carve-out scan** (in-step edit, step-blind scan); caught by the #86
  card's manual-diff duty".
- **v1.10.0 hop (PR #125, squash `b11fe68`):** step-blind AGAIN on the same edit — the
  regen "dropped the PR #86 card-status guard step (named by the carve-out scan) AND the
  `Head-ref:` `--body` provenance customization (NOT named — step-blind, exactly as on
  the v1.9.0 hop; the manual-diff duty caught it again)" (second Grounding pin, the hop's
  own card).

The stopgap shipped on that second hop is **host-side and host-shaped**:
`scripts/preflight.py --enabler-anchors` (first Grounding pin) hard-codes the two
byte-needles as `ENABLER_ANCHORS` and sweeps the enabler for them — REPORT-ONLY, exit 0
unconditionally, promotion-to-gating condition recorded on the #125 session card (flip
after one clean regen cycle). It protects ONE repo's two needles; every other adopter
re-lives the manual-diff duty, and every NEW in-step host edit here needs a hand-added
needle in a script the kit never sees.

## Idea

Give the kit a **host-declared needle list** — `substrate.config.json` →
`"carveout_needles": {"<kit-owned file>": ["<literal byte-needle>", …]}` — and have the
kit's OWN carve-out scan check each declared needle against the pre-regen and post-regen
bytes, reporting a dropped needle **even when it lives INSIDE a kit-owned step**, exactly
as it already reports whole added steps. Then the scan is no longer step-blind for any
host that declares its edits: the report's carve-out section lists the needle, the banked
pre-regen copy carries the restore source, and the re-apply duty becomes machine-checked
at the seam where the clobber HAPPENS (upgrade time) instead of downstream at preflight
time. This repo's `ENABLER_ANCHORS` list is the working reference implementation and the
first migration: on adoption, the two needles move into config and
`--enabler-anchors` reduces to a redundant local tripwire that can retire. Same
config-seam family as `extra_checks` (host-checkers-one-gate): hosts declare, the kit
enforces, zero hand edits to kit-owned machinery.

Cross-links (sibling captures in this section, indexed by link per section style):
[`enabler-card-status-guard-upstream-2026-07-11.md`](enabler-card-status-guard-upstream-2026-07-11.md)
(same family — host customizations on kit-owned files; upstreaming the guard absorbs one
needle's SUBJECT into the template, this config makes whatever residue remains — and any
future in-step edit on any adopter — declarable and scanned) ·
[`host-checkers-one-gate-2026-07-10.md`](host-checkers-one-gate-2026-07-10.md)
(the config-seam sibling — `extra_checks` for checkers, `carveout_needles` for bytes).
Seeded by the #125 card's 💡 (its "kit-seam half" names this exact shape and the
composition with the still-open guard-upstream seed).

**Why now:** two consecutive kit hops — same-day releases, v1.9.0 (PR #120 `f417a1f`)
and v1.10.0 (PR #125 `b11fe68`) — missed the SAME class of host edit, and only a manual
diff caught it both times; the `--enabler-anchors` advisory is an explicit stopgap (one
host, two hard-coded needles, report-only). The durable fix belongs upstream in the kit's
scan, where one config key closes the step-blindness class for every adopter before the
next release wave re-clobbers the fleet.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/09837de9e787f07296767a54b5dedc4d4f5ff339/src/engine/adopt.py@09837de · fetched 2026-07-11T07:36Z
> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/09837de9e787f07296767a54b5dedc4d4f5ff339/CHANGELOG.md@09837de · fetched 2026-07-11T07:36Z
> *(pin annotation: kit live HEAD via `git ls-remote` 2026-07-11T07:34:56Z; both files read
> at that pin through a blobless clone — the git protocol serving the same public bytes as
> the raw path. ONE shared verify-first sweep at this pin serves this report and the
> sibling's — batched as TWO FULL batteries, not primary+pointer: the #87 pointer shape is
> for one-surface pairs, and this pair targets two DISTINCT kit surfaces (the carve-out
> scan + config schema here, the enabler/gate templates there) with different failure
> modes and different smallest slices — the #102/#116 sibling-batteries precedent.)*

Single-pass battery v0 (no panel trigger: not contested, not high-blast-radius — a
routing decision over a docs-only diff). **Verify-first, release-wave-aware** (the kit
cut three same-day releases — v1.8.0/v1.9.0/v1.10.0 all dated 2026-07-11 in
`CHANGELOG.md` @ `09837de` — so overtaken-by-release was the live risk): the tag list at
ls-remote 07:34:56Z ends at **v1.10.0** (tag `eb1b6f3` → merge `1b5db16`, kit PR #178);
**no v1.11.0 tag, and `## [Unreleased]` is EMPTY** at HEAD (immediately followed by
`## [1.10.0] - 2026-07-11`) — nothing staged. Zero `carveout_needles`/byte-needle hits
anywhere in `src/`, `dist/bootstrap.py`, `docs/`, or `CHANGELOG.md` at the pin. The scan
is still step-granular IN CODE: `gate_carveouts()` (`src/engine/adopt.py:882`) compares
`_workflow_outline()` job/step NAME sets only, docstring verbatim — "Removals and edits
of kit content are NOT reported here: the regen restores those by design; only content
that exists in the live file and nowhere in the kit template is a carve-out." The kit's
own backlog (`docs/ideas/`, 29 entries) and `control/inbox.md` carry no
needles/step-blindness entry, and the post-v1.10.0 commits at HEAD (kit PRs
#179/#180/#182/#183) are release close-out + T5 bench re-scope, no scan work in flight.
**Not overtaken — the fork resolves park(routed).**

**1. What is this really?** A granularity extension to a reporting pass that already
exists, not a new subsystem: `gate_carveouts()` already diff-describes live-vs-template
at job/step granularity, and the regen path already banks the full pre-regen copy and
surfaces carve-outs in `upgrade-report.md` (`adopt.py:1130–1164`). The idea adds a third,
finer comparison the host DECLARES: literal byte-needles checked pre-regen vs post-regen.
Doctrinally it is the established declare-don't-edit config pattern — `heartbeat_files`,
`session_markers`, `automerge.branch_patterns` are all existing host-truth keys at HEAD;
this is the same shape aimed at the clobber seam.

**2. What is the possibility space?** Ascending: (i) report-only — a dropped declared
needle emits a `carve-out:` line exactly like a dropped host step does today; (ii) + the
restore pointer (the banked pre-regen copy already exists — the line names it as restore
source, zero new machinery); (iii) blocking — regen refuses / `check` reds until the
needle is re-applied or the declaration withdrawn; (iv) generalize past workflows to
every kit-owned regen surface (the config shape already keys by file path); (v) auto
re-apply (patch semantics). (v) is over the line — needles are literals, not patches;
(i)+(ii) is where the value/complexity curve peaks, matching the kit's own
observe-before-block doctrine (this repo's `--enabler-anchors` advisory-first wave, and
the v1.10.0 gate hold's own advisory→gating lineage).

**3. What is the most advanced capability reachable by the simplest implementation?**
A ~15-line loop in the existing regen path: for each declared needle of the regenerated
file — needle in pre-regen bytes AND absent from post-regen bytes → emit
`carve-out: <file> — host needle dropped: '<needle>' (restore source: banked pre-regen
copy)`. Zero new state, zero network, rides the existing report+bank machinery — and the
step-blindness class is closed for EVERY declaring adopter at EVERY future hop, at the
seam where the clobber happens (upgrade time) instead of downstream at each host's
preflight time.

**4. What breaks it?** (a) Nobody declares — the key defaults empty, so value only
materializes for hosts that adopt the discipline; migration #1 exists (this repo's two
`ENABLER_ANCHORS` needles, `scripts/preflight.py` @ `b11fe68` ~lines 322–379). (b) Stale
declarations: a kit template rewording that legitimately absorbs the host edit leaves a
needle that can never match — the check needs a DISTINCT "declared but absent pre-regen
too" message so a stale needle reads as hygiene, not as a drop. (c) Literal-match
brittleness: an edit spanning a YAML reflow breaks a single-string needle — the spec must
stay "literal bytes; picking a stable needle is the host's job" (proven workable: both
`ENABLER_ANCHORS` needles survived two hops as stable literals; normalization is the
ambition-creep failure mode). (d) House-style pushback: `grammar.py`'s D-7 note ("the kit
does not grow config knobs") — answered by (1): this is host-truth declaration, the
already-established key class, not grammar forking.

**5. What does it unlock?** Retires the manual-diff duty fleet-wide (the only thing that
caught the drop on BOTH evidenced hops); makes `upgrade-report.md` the single carve-out
surface (report + bank + needle); lets this repo demote `--enabler-anchors` to a
redundant tripwire and then delete it (the promotion condition on the #125 card inverts
into a retirement condition); makes every FUTURE in-step host edit on any adopter
declarable at edit time instead of discovered at loss time; and gives the sibling
guard-upstream head's residue (the `Head-ref:` `--body` provenance edit) its first
declared home.

**6. What does it depend on?** The kit lane building it (config schema key + the regen
loop + tests for drop/keep/stale-declaration); the existing bank/report machinery
(`adopt.py:1131` — present at the pin); adopters declaring (migration #1 is a one-config
edit here); nothing sim-shaped — no verdict gate.

**7. Which lane should build it?** substrate-kit — the scan, the config schema, and the
regen path are all kit-owned code; no host can close the class locally (the stopgap's
exact limit: one host, two hard-coded needles). The honest fork per verify-first is
**park(routed), NOT parked(overtaken)**: zero adoption evidence at `09837de` (empty
`[Unreleased]`, no v1.11.0 tag, no backlog entry, scan step-granular in code).
Manager-ORDER-worthy: the class is fleet-shaped, not host-shaped — the kit's adopter
registry counted 8 tree-current rows at the v1.9.0-wave regen (kit commit `78a69b5`),
`gate_carveouts`' own docstring cites a SECOND host's kit-owned-file customization
(superbot-games PR #16's in-gate pytest job), and this repo alone carries three
(gate wake-preflight step + enabler guard + enabler provenance edit); every row re-lives
the manual-diff duty on every release wave until the scan learns needles. One kit-lane
ORDER could carry this together with the two routed siblings (the guard-upstream head
and `kit-line-self-drift-local-check`) — three heads, one lane, one config/check seam
family.

**8. What is the smallest shippable slice?** `substrate.config.json` →
`"carveout_needles": {"<kit-owned file>": ["<literal>", …]}` in the config schema + the
Q3 loop inside the existing carve-out scan + one report line + three tests
(dropped/kept/stale-declaration) + a CHANGELOG entry; adopter migration = one config
edit here moving `ENABLER_ANCHORS`' two needles into the key.

**Recommendation: park** — routed(substrate-kit lane build, manager-ORDER-worthy): verified un-adopted at live kit HEAD `09837de` (empty `[Unreleased]`, no v1.11.0 tag, `gate_carveouts` step-granular at `adopt.py:882`), the two-hop-evidenced step-blindness class (`f417a1f` · `b11fe68`) closes for every adopter with one config key in the kit's own scan, and no simulator question exists — a scan feature is proven by its own red/green (the #114 precedent for this same lane).
