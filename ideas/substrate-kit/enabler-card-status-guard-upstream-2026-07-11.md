# Upstream the enabler card-status guard into substrate-kit

> **State:** parked(routed — substrate-kit lane build, scope-sharpened by v1.10.0's `session-card-hold`: the routed core is the gate-preflight config seam + badge-grammar single-sourcing, the arm guard demoted to opt-in defense-in-depth; verified un-adopted at live kit HEAD `09837de` — see probe report)
> **Class:** process · **Target:** `menno420/substrate-kit`
> **Grounding:** https://raw.githubusercontent.com/menno420/idea-engine/a4a376af0b1a89da4f79a906031982818323e909/.github/workflows/auto-merge-enabler.yml@a4a376a · fetched 2026-07-11T05:02:54Z
> **Grounding:** https://raw.githubusercontent.com/menno420/idea-engine/a4a376af0b1a89da4f79a906031982818323e909/.sessions/2026-07-11-automerge-arm-race-guard.md@a4a376a · fetched 2026-07-11T05:02:54Z
> *(pin annotation: the enabler as of the PR #86 merge — the `id: card` guard step plus its TWO in-file re-apply-duty comments (~lines 105 and 186) are the host customizations this capture prices)*

## Problem

KIT-OWNED workflow files ("hand edits are OVERWRITTEN" — any `bootstrap adopt`/
`upgrade` regenerates them) now carry TWO host customizations on this repo that
must be hand-re-applied after every regeneration. (1) The gate wake-preflight step
in `substrate-gate.yml` (added PR #18): silently dropped and re-applied live THREE
times (PRs #35, #54, #55), with the PR #36 self-check redding the preflight when it
goes missing. (2) The enabler card-status guard (PR #86, first Grounding pin): an
`id: card` step that lists the PR's changed files, parses each non-removed in-diff
`.sessions/*.md` card's `**Status:**` badge at the PR head SHA, and refuses to arm
auto-merge while any card is `in-progress` — proven live in actions run 29140112239
(logged `status=in-progress`, arm step conclusion `skipped`) and by PR #86's own
merge once its card flipped `complete` (second Grounding pin, live-fire section).
The re-apply debt compounds on every upgrade, and the in-file comments plus the
tripwire idea's extension-note ledger are the only thing keeping it honest.

## Idea

Upstream both as kit template features. **(a)** Ship the card-status guard in the
kit's enabler template, sourcing the badge regex from the kit's own grammar module
(`src/engine/grammar.py` `_BADGE_RE`) — three surfaces already parse the badge
independently (the kit's `_BADGE_RE`, substrate-gate's diff-scoped card pick, the
guard's hand-copied regex), so upstreaming collapses a triple-maintained regex into
the one writer-and-enforcer module (EAP §6.8). **(b)** Give the gate a config
carve-out — a `substrate.config.json` seam — so hosts declare a preflight command
instead of hand-editing the kit-owned gate; same seam family as the
host-checkers-one-gate capture below. Semantics note for fleet adopters: the guard
CHANGES enabler behavior as a template default — carded PRs no longer arm at open;
the `synchronize` re-run after the card flips `complete` is what arms them.

Cross-links (sibling captures in this section, indexed by link per section style):
[`host-checkers-one-gate-2026-07-10.md`](host-checkers-one-gate-2026-07-10.md)
(same class — a host customization needing a kit seam, checker edition) ·
[`kit-line-self-drift-local-check-2026-07-10.md`](kit-line-self-drift-local-check-2026-07-10.md)
(drift-detection sibling) · the re-apply ledger itself,
[`../fleet/branch-prefix-drift-tripwire-2026-07-11.md`](../fleet/branch-prefix-drift-tripwire-2026-07-11.md)
(its extension notes 1+2 record both enabler customizations).

**Why now:** PR #86 just made this the SECOND host customization carrying re-apply
debt on a KIT-OWNED file; the debt now compounds on every `bootstrap upgrade`, and
the changed arm-at-open semantics are exactly what a template should carry once —
rather than each host rediscovering the ~25s open→merge race (#64/#80) and
re-deriving the guard by hand.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/09837de9e787f07296767a54b5dedc4d4f5ff339/src/engine/adopt.py@09837de · fetched 2026-07-11T07:36Z
> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/09837de9e787f07296767a54b5dedc4d4f5ff339/src/engine/checks/check_session_log.py@09837de · fetched 2026-07-11T07:45Z
> *(pin annotation: kit live HEAD via `git ls-remote` 2026-07-11T07:34:56Z, read through a
> blobless clone at the pin. Batched with the sibling
> [`carveout-needles-config-2026-07-11.md`](carveout-needles-config-2026-07-11.md) as TWO
> FULL batteries sharing ONE verify-first sweep — the shape rationale and the shared
> release-wave evidence (v1.10.0 newest tag, `[Unreleased]` EMPTY, no feature in flight at
> HEAD) live in that report's pin annotation and verify-first paragraph; only the facts
> SPECIFIC to this head are restated below.)*

Single-pass battery v0 (no panel trigger: routing decision, docs-only diff).
**Verify-first, this head's specifics at `09837de`:** the kit's enabler template
(rendered in `src/engine/adopt.py`, the block under `AUTOMERGE_ENABLER_RELPATH`) carries
exactly TWO guard steps — "Refuse to arm unless the base branch requires status CONTEXTS"
and "Re-check the `do-not-automerge` label FRESH (stale-payload race guard)" — and ZERO
occurrences of "card": **the guard is not upstreamed**. No `extra_checks`/preflight
config key exists anywhere at the pin: **the gate seam (part b) is not built either**.
Two capture corrections found live: **(i)** `src/engine/grammar.py` EXISTS at HEAD (the
EAP §6.8 control-plane grammar module) but does NOT carry `_BADGE_RE` — the badge regex
lives at `src/engine/checks/check_docs.py:40`, and the parse the guard actually needs
(`status_in_progress()` + `IN_PROGRESS_TOKENS`) at `src/engine/checks/check_session_log.py:103`
— so "source from the grammar module" is one hop off: the badge/card grammar is not yet
one of grammar.py's surfaces, and upstreaming would either source from the checks modules
or move the badge grammar into grammar.py first. **(ii)** The MATERIAL post-capture
event: v1.10.0 (released today, `CHANGELOG.md` `[1.10.0]` "Born-red card-only loophole"
entry) shipped the **`session-card-hold`** — the GATE itself now reds while an ADDED card
declares in-progress, live-fired on this repo's own PR #125 hop (its card: the hold held
the gate red on the very PR that shipped it, while the local #86 guard skipped arming on
the same signal — belt and suspenders, confirmed compatible). An armed carded born-red PR
can no longer merge before its card flips, guard or no guard, wherever the gate is the
required context. **The guard's primary race (#64/#80, ~25s open→merge) is absorbed at
the required check; what the capture priced as the sole defense is now defense-in-depth.**
Not overtaken — neither ask exists upstream — but the scope moves: park(routed),
sharpened.

**1. What is this really?** Two distinct asks stapled by one debt class. (a) Template-
default the enabler card-status arm guard — post-v1.10.0, a SECOND belt over the gate's
own hold. (b) A config seam so hosts declare the gate's wake-preflight step instead of
hand-editing the kit-owned gate — the debt that remains fully unaddressed and is the
OLDEST recurring re-apply duty on this repo (dropped and re-applied live on PRs
#35/#54/#55, re-applied INTO a changed template on #125). The capture's real center of
gravity, post-correction, is (b) plus the badge-grammar single-sourcing; (a) is residue.

**2. What is the possibility space?** For (a): template-default verbatim (the capture's
ask — but it changes arm-at-open semantics for every adopter); opt-in via a config flag;
or retire-don't-upstream, letting the gate hold carry the class and the template merely
DOCUMENT the arm-then-hold semantics (the honest new option the capture predates). For
(b): an `extra_checks`-style config key the gate template renders into a step; or a
kit-blessed SEPARATE host workflow (the kit's own file-header advice) — which cannot be
the required context without re-creating the never-reports jam the gate's fast lane
exists to prevent; or the sibling needles config making the hand-edit survivable rather
than unnecessary. The needles path composes with either: it is the floor, (b) is the fix.

**3. What is the most advanced capability reachable by the simplest implementation?**
The (b) seam: one config key (host-declared preflight command) + ~10 lines of gate
template rendering + one test kills the three-live-drops re-apply duty for every adopter
that declares — and this repo's gate customization reduces to one config line. For (a),
the simplest honest move is documentation-plus-opt-in: the template gains the guard
behind a config flag defaulting OFF, sourced from the kit's own badge parse, collapsing
the hand-copied regex without changing any adopter's semantics unasked.

**4. What breaks it?** (a) Redundancy is now the base case: the v1.10.0 hold covers the
merge race for ADDED in-progress cards wherever the gate is required — the guard's
residual value is narrow (a MODIFIED-not-added in-progress card in the diff, which the
hold's added-card lane does not grade; a repo whose required context is not the gate).
A template DEFAULT that stops arming carded PRs at open changes every adopter's landing
behavior for that narrow residue — the strongest argument for opt-in. (b) A config-
rendered step executes host-declared commands inside a kit-owned required check — a
trust/injection surface the kit must scope deliberately (the checks-not-commands variant:
the key names scripts under the host's own `scripts/`, the template pins the interpreter
— same shape as this repo's `interpreter` key). (c) The badge-grammar move: three
independent badge parsers exist TODAY (`check_docs.py:40`, the gate's diff-scoped card
pick, this repo's hand-copied guard regex) — upstreaming the guard WITHOUT first homing
the badge grammar in `grammar.py` adds a fourth copy; sequencing matters.

**5. What does it unlock?** Retires two of this repo's three re-apply duties at their
seam ((b) kills the gate-step duty; (a)-as-template or the sibling's needles kill the
guard duty), leaving only the provenance `--body` edit — the sibling's first declared
needle; collapses the badge-regex triple-parse into the one writer-and-enforcer module
(the exact EAP §6.8 doctrine grammar.py already implements for the control-plane
grammar); ends per-host rediscovery of the arm race and its guard.

**6. What does it depend on?** The kit lane (templates, config schema, grammar module
are all kit-owned); the v1.10.0 session-card-hold semantics it must compose with
(shipped; composition proven live on PR #125 — belt and suspenders compatible); the
badge grammar moving into `grammar.py` (exists at HEAD, badge surface not yet in it);
the sibling `carveout_needles` key for whatever residue stays host-local. Nothing
sim-shaped — no verdict gate.

**7. Which lane should build it?** substrate-kit — every artifact is kit-owned. The
honest fork per verify-first is **park(routed), NOT parked(overtaken)**: neither (a) nor
(b) exists at `09837de` (card-less enabler template, no gate config seam, empty
`[Unreleased]`), and the kit's own backlog carries no matching entry. But route it
scope-sharpened: the ORDER-worthy core is (b) + badge-grammar single-sourcing, with (a)
as opt-in defense-in-depth — v1.10.0's hold, not this guard, now owns the primary race.
Same fan-in bundle as the sibling and `kit-line-self-drift-local-check`: three routed
heads, one lane, one config/check seam family — one manager ORDER could carry all three.

**8. What is the smallest shippable slice?** The (b) seam alone: one config key
(host-declared gate preflight command, script-path-shaped per Q4b) + gate template
rendering + one test; this repo migrates its wake-preflight step into the key and
deletes the oldest re-apply duty. The badge-grammar homing and the opt-in guard ride
later slices — or the guard simply retires here once the hold has one more clean cycle
(its own #125 promotion logic, inverted).

**Recommendation: park** — routed(substrate-kit lane build, scope-sharpened): un-adopted at live kit HEAD `09837de` (no card guard in the enabler template, no gate config seam, empty `[Unreleased]`), but v1.10.0's `session-card-hold` — shipped post-capture, live-fired on this repo's #125 — absorbed the guard's primary race, so the routed ask is the gate-preflight config seam + badge-grammar single-sourcing with the arm guard as opt-in; no simulator question (template features are proven by their own red/green — the #114 precedent).
