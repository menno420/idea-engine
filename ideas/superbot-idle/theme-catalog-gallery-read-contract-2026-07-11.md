# Theme-gallery read contract — the committed catalog index the website's shop window renders from

> **State:** parked(build-direct — a one-PR lane export slice generated from the lane's own loader, no sim question; window verified open at websites `7da9fbf`)
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

## Probe report (v0, 2026-07-11)

*Single-pass battery per the README panel default (sim-lab VERDICT 002): a committed
JSON export with a regenerate-or-red test is reversible, low-blast-radius surface, and
the verify-first read below did not disagree with the capture. Expiry-aware head
(Sequence: before the websites lane builds the selector/gallery UI), so verify-first ran
FIRST, both sides of the seam. Producer side: lane HEAD moved `f11c71a` → `1b3a211`
since capture, but the delta (PRs #47–#49) is ORDER-001 model-attribution only — zero
product change; a full ls-tree at `1b3a211` shows NO `themes/catalog*.json`, no export
tool beyond `tools/gen_setup_vectors.py` + `tools/theme_gate.py`, `themes/` = README +
12 yaml packs, and `tests/test_theme_catalog.py` is in-repo schema-proving, not an
export; `git grep -i 'catalog.v1|gallery'` outside `.sessions/`/`.substrate/` returns
zero product hits. The capture premise HOLDS at live HEAD. Consumer side: websites @
HEAD `7da9fbf` — zero hits for `IDLE1-|superbot-idle|theme gallery|setup code`; the
selector/gallery UI is NOT started. **Window open.** All lane citations below read at
`1b3a211` unless marked otherwise.*

**1. What is this really?**
A contract publication, not a design. The truth the gallery needs already exists in
exactly one place — the lane's loader plus 12 committed packs — and the lane has already
proven, twice, the discipline that exports such truth (schema md↔json parity tests;
`tools/gen_setup_vectors.py` + `tests/vectors/setup-codes.v1.json`, regenerate-or-red).
This idea is the third instance of that same move, pointed at the READ side of §3: one
generated `themes/catalog.v1.json` so a foreign renderer never re-implements loader
semantics. Nothing here invents schema surface; it re-serializes surface that
`docs/theme-schema.md` @ `1b3a211` already pins (fields, budgets, `labels` optionality
with neutral fallbacks, additive-within-v1).

**2. What is the possibility space?**
Ascending: (i) a hand-committed JSON index — rejected by the lane's own drift doctrine
(hand-copies are the failure its parity tests exist to kill); (ii) the capture's shape —
a `gen_setup_vectors.py`-shaped generator reading the REAL loader, output committed,
regenerate-or-red test (the floor that already carries everything the gallery needs);
(iii) + catalog-level ordering/metadata as explicit fields rather than array accident;
(iv) + wiring the future `validate_against_catalog` to consume the SAME file, closing
read and write over one artifact; (v) a hosted catalog API — rejected by the decided
phase-1 shape (no hosted backend, superbot @ `41899e1` §7 item 2). The null alternative
is the status quo the capture prices: the websites lane parses 12 YAMLs and re-derives
schema semantics by hand — drift by construction against an additive-within-v1 schema.

**3. What is the most advanced capability reachable by the simplest implementation?**
One generated file + one parity test turns the gallery into a static-render problem: a
consumer that never imports the loader still renders the complete v1 surface (id, name,
emoji, embed_color, description, schema_version, skinnable feature blocks, ordering) —
and because schema v1 has no art slot, that small export is not a preview of the gallery
data, it IS the gallery data, complete. By construction the catalog and the setup codes
it must validate against derive from the same loader at the same commit, so §3's read
and write halves agree without any runtime coordination.

**4. What breaks it?**
- **Ordering is not pre-registered anywhere.** "Catalog-level ordering" appears in this
  capture, but no lane doc @ `1b3a211` pins what gallery order MEANS (insertion?
  alphabetical? curated?). If the generator just serializes loader iteration order, an
  incidental dict order becomes de-facto contract — the exact failure class the idea
  exists to prevent, one level up. The lane must decide ordering explicitly in the slice
  (a one-line product decision, not an experiment).
- **Additive-within-v1 churn.** Every new optional block and every catalog wave (QUEUE
  @ `1b3a211` carries `ON-DEMAND: catalog wave 4+`) changes the file; regenerate-or-red
  covers this — it is the mechanism working, not breaking — but only if the test lands
  WITH the file, not after.
- **No buyer yet.** Websites @ `7da9fbf` has not started the consumer; if the gallery
  never gets built the file is unread ballast. Bounded downside: one generated file +
  one test, and the §3 directive names the gallery as the shop window, so the buyer is
  decided even though its lane hasn't started.
- **Schema v2.** The versioned filename (`catalog.v1.json`) already prices this; a v2
  ships a sibling file, never mutates v1 semantics.

**5. What does it unlock?**
The websites gallery renders from ONE committed file instead of a YAML-scraping fork of
the loader; the future `validate_against_catalog` and the gallery close over the same
artifact, so a setup code encoded from gallery state is valid by construction; any later
consumer (docs site, bot-side theme preview, the manager's roster tooling) gets the same
machine surface free; and the contract is registered BEFORE the first scraper hardens
its guesses into one nobody registered — the capture's whole "why now".

**6. What does it depend on?**
Producer side, all verified present @ `1b3a211`: the real loader, 12 packs in
`themes/`, `docs/theme-schema.md` semantics, and the twice-proven regenerate-or-red
pattern (`tools/gen_setup_vectors.py` as the template; `tools/theme_gate.py` as CI
precedent). Write-path contract it must stay consistent with: SETUP-CODE FORMAT v1
(`docs/provisioning.md` § Consumers, 150 vectors) — same repo, same loader, so
consistency is by construction. Non-dependencies worth stating: the lane's only standing
upstream block, PLUG-001 (plugin contract, 404 upstream), touches plugin surface, not
themes; SIM-001 is lifted (sim-lab VERDICT 006 approve) — nothing upstream blocks this
slice. Consumer side: deliberately none — publishing ahead of the first consumer is the
point (Sequence window verified open at websites `7da9fbf`).

**7. Which lane should build it?**
**superbot-idle — direct lane build; nothing here is a simulator's.** The catalog is
generated FROM the lane's own loader against the lane's own schema, and its correctness
is settled by running the generator and its parity test in lane CI — deterministic,
reproduced on every push, no empirical question left over. The one open question the
probe found (Q4 ordering) is a product decision, not evidence a sim could produce.
Routing a deterministic export through sim-lab would spend a verdict cycle to learn what
`python3 -m pytest` already proves. The lane is also positioned to take it: QUEUE @
`1b3a211` already carries ON-DEMAND catalog work, and its only live upstream block
(PLUG-001) is unrelated. No outbox proposal — park(build-direct) routes nothing to
sim-lab; the head stays indexed for the manager's sweep / lane pickup, the same shape as
the mineverse `snapshot-contract` precedent.

**8. What is the smallest shippable slice?**
One lane PR: `tools/gen_theme_catalog.py` (shaped like `gen_setup_vectors.py`, reading
the real loader) + committed `themes/catalog.v1.json` (per-pack id, name, emoji,
embed_color, description, schema_version, skinnable blocks present; catalog-level
schema_version + an EXPLICIT ordering decision) + a regenerate-or-red test (new, or an
extension of the existing in-repo `tests/test_theme_catalog.py`). Zero new schema
semantics; the slice is the export plus the drift gate that keeps it honest.

**Recommendation: park** — build-direct: a one-PR lane export slice generated from the
lane's own loader whose correctness is settled by its own regenerate-or-red CI, leaving
no empirical question a sim can settle (the sole open point, gallery ordering, is a
product decision); the Sequence window is verified open (websites @ `7da9fbf` has no
gallery started), so the lane can still publish the read contract before its first
consumer exists.
