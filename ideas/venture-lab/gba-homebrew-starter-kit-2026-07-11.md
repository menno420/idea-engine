# GBA homebrew starter kit

> **State:** captured
> **Class:** venture · **Target:** menno420/venture-lab
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/main/docs/roster.md@6d5e3b3 · fetched 2026-07-11T18:54Z
> **Shortlist rank:** 3 of 5 · sellables brainstorm 2026-07-11 · [batch](sellables-brainstorm-batch-2026-07-11.md)
> **Sequence:** after the ⚑ 2026-07-14 EAP itch.io go/no-go (rides the same listing decision)

## What it is

Extract Lumen Drift's build scaffold — the Makefile/CI setup, the sprite pipeline, and the sha256-provenanced ROM dist pattern — into a clean, documented GBA project template sold to the homebrew scene. The gba-homebrew lane's toolchain is finished and working, and Lumen Drift v1.3 is the living proof it ships actual games; the starter kit is that same scaffold with the game removed and a setup guide added. Sell channel: itch.io PWYW, with a Gumroad mirror, cross-promoting the Lumen Drift listing that is already owner-gated in the ⚑ 2026-07-14 bundle.

## Why shortlisted

Three reasons. First, it is extraction from a finished game, not new construction — the toolchain, CI, and pipeline all exist and demonstrably work. Second, the marketing is proof-by-example: "the template that built Lumen Drift" is a claim backed by a shipped v1.3 ROM, which is the strongest pitch a tooling product can make to the homebrew scene. Third, it requires no new owner account — it rides the exact same itch.io go/no-go decision as the Lumen Drift listing itself, so the owner-click cost is already sunk into a decision being made anyway.

## Smallest shippable slice

A template repo containing a "hello world + one animated sprite" demo that builds green in CI, plus a setup guide. That single slice proves every load-bearing part of the product — toolchain install, build, sprite pipeline, CI — in the smallest possible surface.

## Honest effort / plausibility

Mostly extraction plus documentation; the code risk is low because nothing new is being engineered. The homebrew scene is small but active and does buy tooling — still, PWYW realistically nets a few dollars per paying download at low volume, so per Q-0259 r.4 this is a modest-trickle expectation, not a revenue line. The sequencing is the real constraint: nothing moves before the ⚑ 2026-07-14 EAP itch.io go/no-go, and a no-go there parks this too.

## Open questions

- Licensing for the toolchain pieces: which parts of the scaffold are fleet-original versus derived from third-party GBA tooling, and what license can the template legitimately carry?
- How much Lumen-specific code must be scrubbed? The extraction is only cheap if the scaffold separates cleanly from the game — a first pass should size the scrub before the slice is promised.
