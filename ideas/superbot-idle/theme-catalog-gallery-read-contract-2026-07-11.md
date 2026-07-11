# Theme-gallery read contract — the committed catalog index the website's shop window renders from

> **State:** captured
> **Class:** product · **Target:** `menno420/superbot-idle`
> **Grounding:** https://github.com/menno420/superbot-idle@f11c71a52d4d2adf88b2bf11f5d1134bad495be2 · fetched 2026-07-11T03:31Z (manifest row: behind)
> *(pin annotation: roster row @ fleet-manager `93d3a4d` records lane HEAD `97bfff2`; live HEAD `f11c71a` is 3 PRs ahead. Consumer-side verified separately: websites @ HEAD `d4ed380` (ls-remote 03:34:07Z, blobless clone) carries ZERO idle/setup-code/gallery surface — `git grep -i 'IDLE1-|setup.code|superbot-idle|theme gallery'` empty outside kit internals.)*
> **Sequence:** before the websites lane builds the selector/gallery UI (§3's target flow) — nothing consumes the read path yet, so the contract can still be published ahead of its first consumer instead of reverse-engineered from one.

## Problem

The directive's §3 makes a **live theme gallery "rendered from the committed theme
packs"** the shop window of website-first onboarding (superbot @ `41899e1`). The WRITE
path is contract-complete at lane HEAD: SETUP-CODE FORMAT v1 names the websites lane as
the encoder and ships 150 cross-language test vectors so a foreign implementation can
prove itself (`docs/provisioning.md` § Consumers; `tests/vectors/setup-codes.v1.json`,
regenerate-or-red). The READ path has **no machine surface at all**: a gallery renderer
today must parse 12 YAML packs and re-derive schema semantics by hand — which optional
blocks are present (= which features are skinnable, exactly what
`validate_against_catalog` will later enforce against the code it encodes), `labels`
optionality with pinned neutral fallbacks, string budgets. That is loader-logic
duplication in another repo against a schema that is additive-within-v1 — drift by
construction, the exact failure class the lane's own md↔json parity tests exist to
prevent inside the repo. Verified absence both sides: no catalog/gallery export
anywhere in the lane tree @ `f11c71a` (ls-tree scan), no consumer started @ websites
`d4ed380`.

## Idea

A committed, **regenerate-or-red catalog index** — e.g. `themes/catalog.v1.json`,
generated from the real loader by a `tools/gen_setup_vectors.py`-shaped script: one
entry per pack (id, name, emoji, embed_color, description, schema_version, skinnable
feature blocks present) plus catalog-level ordering. The gallery then renders from ONE
committed file, and the setup codes it encodes are valid against the same catalog by
construction — §3's read and write halves close over committed artifacts with no hosted
backend, exactly the phase-1 shape the owner decided (§7 item 2). v1's renderable
surface is small and complete (no art slot exists in schema v1 — name/emoji/color/
description + feature presence IS the gallery data), so the export is bounded and the
discipline is one the lane has already proven twice (schema md↔json parity; setup-code
vectors).

## Grounding

- Write-path contract + consumer naming: lane `docs/provisioning.md` @ `f11c71a`
  (§ Consumers — "Encoder — the websites lane"; § Cross-language test vectors).
- Renderable surface + additive-v1 + neutral-fallback semantics: `docs/theme-schema.md`
  @ `f11c71a` (fields table, budgets, `labels` optionality); 12 packs in `themes/`.
- Gallery-as-shop-window + pre-invite selection: superbot @ `41899e1` §3.
- Consumer not started: websites @ `d4ed380` (clone-grep, 03:34Z — see pin annotation).

**Why now:** publishing the read contract BEFORE the first gallery render is the cheap
moment — once a scraper exists, its parsing assumptions harden into a de-facto contract
nobody registered (the reachability discipline: pattern-exists is not
pattern-can-produce, and here the producer, its tooling shape, and the data's location
are all verified at pin).
