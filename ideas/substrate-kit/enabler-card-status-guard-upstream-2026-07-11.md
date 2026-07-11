# Upstream the enabler card-status guard into substrate-kit

> **State:** captured
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
