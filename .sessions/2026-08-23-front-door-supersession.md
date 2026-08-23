# 2026-08-23 — the front door said this repository was shut down; two owner directives say otherwise

> **Status:** `complete` — branch `claude/front-door-supersession`, opened
> against `main` in this repository. Flipped after
> `python3 bootstrap.py check --strict` returned a real exit 0 on this tree,
> read directly and never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

`docs/current-state.md` opened with **SEAT DORMANT — shut down for good by owner
order on 2026-07-14**, and said nothing else. A fleet-wide intent audit on
2026-08-23 probed this file for `standing asset`, `on-demand`, `R6` and
`resume`: **zero hits for all four.** So a session booting cold here read that
the repo was finished and had no reason to look further.

It is not finished. **Two owner directives dated 2026-07-26 — twelve days after
the shutdown — supersede it:** OD-4 keeps `idea-engine` and `sim-lab` as
standing assets, and OD-10 makes the Ideas Lab on-demand. The estate's
precedence rule is explicit that the owner's most recent instruction beats a
dated shutdown note, so the dates decide this and no judgement call is involved.

There is also **planned work**: program step R6 — *"make the two-era reality
legible from the front door … surface the 566-file idea corpus."* This banner is
a first slice of R6 by its own wording, since the front door was saying the
opposite of the truth.

## previous-session review

The previous card (`2026-08-13-kit-upgrade-v1.21.0.md`) took the kit to v1.21.0
and left the repo at rest. Nothing it recorded is contradicted here — the seat
really is retired. What no session had done is write the *second* half onto the
front page: the seat was retired **and** the repository was kept. Only the first
half was ever recorded here.

## What landed

One block at the top of `docs/current-state.md`, in the estate's era-banner
convention: the correction first, then the original section struck through,
re-badged HISTORICAL, and kept verbatim — its handoff pointer is still the real
revival record, so erasing it would cost more than it fixed.

The banner states what "on-demand" means in practice (no standing loop, no
invented cadence), quotes both directives with their dates, links the hub's
directive table, and records **why** the error persisted for a month: the
shutdown retired the *seat*, OD-4 kept the *repository*, and nothing joined the
two on the front page.

## What was checked, not assumed

- **The dates decide, and they were read, not recalled.** OD-4 and OD-10 are
  both stamped `07-26` in the hub's directive table; the shutdown order is
  `2026-07-14`. That ordering is the entire basis for this change.
- **R6's wording was read before being quoted**, not paraphrased from the
  audit's summary of it.
- **The zero-hit probe had a positive control**: the same probe form returns
  hits against other repositories' status docs, so the four nulls here are real
  absences rather than a broken query.

## Verify

`python3 bootstrap.py check --strict` → **exit 0**, read directly, never after a
pipe.
