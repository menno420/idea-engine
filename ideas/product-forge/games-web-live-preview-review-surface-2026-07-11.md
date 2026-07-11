# games-web live preview is the owner's review-after surface — make "live" a verified fact

> **State:** captured
> **Class:** product · **Target:** `menno420/product-forge`
> **Grounding:** https://raw.githubusercontent.com/menno420/product-forge/0a6efe96ef8021679b9f8a6ee63a617cd9d61ffc/control/status.md@0a6efe9 · fetched 2026-07-11T03:31:46Z
> **Sequence:** after OA-003 (owner enables GitHub Pages on product-forge — the ask already lives on the LANE's own heartbeat, deliberately not duplicated here)

## Problem

The owner's merge grant (verbatim on the lane heartbeat @ `0a6efe9`: "I review
afterwards when the whole product is finished") makes **review-after** the forge's
operating model — so the review surface is not the diff, it is the *running product*.
For games-web that surface is the GitHub Pages preview, which is prepped but **dark**:
deploy run 29126980391 failed at `actions/configure-pages@v5` ("Get Pages site
failed… Not Found") because Pages is not enabled — the lane's OA-003, one owner
click. When that click lands, the workflow deploys on the next push — and nothing
anywhere *verifies* the published site actually serves the product: a dark or stale
preview would sit silent while the owner's eventual whole-product review depends on
it.

## Idea

One small games-web slice, waiting ready for the click: (1) a **post-deploy smoke
step** in `deploy-pages.yml` — fetch the published URL after deploy, assert HTTP 200
and that the served payload/page carries the committed contract stamp
(`games-web.character-sheet` + the tree's `schema_version`), so a dark deploy or a
stale artifact reds the workflow instead of nothing; (2) the product README's honest
state line gains the preview URL + a last-verified stamp, so "live preview" is a
claim with evidence attached. Zero new surface: the contract const and version
already exist in `data/schema/game-state.schema.json`; the workflow already exists.

**Honesty caveat (verify-first duty):** this is maintenance-shaped work aimed at a
LIVE lane — the class the probe battery's verify-first rule exists for (five
lane-self-served datapoints). The probe verifies the INVARIANT at lane HEAD first —
*does anything verify the served preview, not merely deploy it?* — and parks as
self-served if the lane got there first.

**Why now:** the games completion wave is the stated priority (Q-0259), the owner's
review of its first product happens on exactly this surface, and OA-003 can land any
wake — the verification should be waiting when it does.
