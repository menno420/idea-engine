# Host-declared carve-out needles — close the scan's step-blindness class

> **State:** captured
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
