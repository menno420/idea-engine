# games-web live preview is the owner's review-after surface — make "live" a verified fact

> **State:** parked(build-direct — lane workflow slice, owner-click-gated: one forge PR adds the post-deploy smoke + README last-verified line, inert-but-ready until OA-003; verified un-self-served at lane HEAD `43563dc`, nothing sim-shaped)
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

## Probe report (v0, 2026-07-11 — batched with `games-web-concept-evidence-pass-2026-07-11.md`, one shared verify-first sweep)

> **Grounding:** https://raw.githubusercontent.com/menno420/product-forge/43563dccc874c58946576444fbba38600bb45f86/control/status.md@43563dc · fetched 2026-07-11T09:10Z
> **Grounding:** https://raw.githubusercontent.com/menno420/product-forge/43563dccc874c58946576444fbba38600bb45f86/.github/workflows/deploy-pages.yml@43563dc · fetched 2026-07-11T09:10Z
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/3150f0e2b8096de7b497778189d3d85676e69ceb/docs/owner-queue.md@3150f0e · fetched 2026-07-11T09:12Z

*Verify-first ran FIRST (this head's own honesty caveat names the self-serve class):
NOT self-served at live lane HEAD `43563dc` (ls-remote 09:09:40Z, blobless clone at
the pin). `deploy-pages.yml` is byte-for-byte the same 4-step deploy the capture read
(checkout · configure-pages · upload-pages-artifact on `products/games-web` ·
deploy-pages) — ZERO verification steps; stem-greps across the tree (`smoke`,
`post-deploy`, `page_url`, `github.io`) hit only the workflow's own environment-URL
display and the product README's § Live preview block, whose state line still reads
"State: pending an owner settings click" with no last-verified mechanism. The
capture's premises all HOLD: OA-003 still open (pf status ⚑ verbatim + fm owner-queue
item 15 @ `3150f0e`), review-after grant intact (pf status § Merge grant, both owner
quotes), failed run 29126980391 still the last deploy verdict. Lane delta since
capture (0a6efe9 → 43563dc, PRs #14–#19: a11y pass · ORDER 002 · ORDER 003
heartbeat-UTC guard) touches nothing here — and adds evidence: `heartbeat-guard.yml`
+ `scripts/check-heartbeat.py` show repo-owned CI guards are the lane's house style.
One wall found and ledgered: `menno420.github.io` is proxy-blocked from this seat
(CONNECT 403, twice, 09:10Z) — Pages live-state concluded from committed surfaces,
not fetched; docs/CAPABILITIES.md append-log entry added this session.*

**1. What is this really?** A verification gap on the owner's actual review surface.
The review-after grant makes the RUNNING product the review artifact, and for
games-web that is the Pages site — but the pipeline ends at `deploy-pages` with
nothing asserting the published site serves the committed product. A dark or stale
preview fails silent exactly where the owner's whole-product review lands. The fix is
one workflow amendment plus one README line, not a feature.

**2. What is the possibility space?** (a) Post-deploy smoke inside the existing
deploy job — fetch `${{ steps.deployment.outputs.page_url }}`, assert HTTP 200 and
the committed contract stamp (`games-web.character-sheet` + the tree's
`schema_version` — both already in `data/schema/game-state.schema.json`); (b) a
scheduled freshness re-check (cron re-fetch — heavier, solves staleness between
pushes nobody has evidenced yet); (c) README § Live preview gains a last-verified
stamp (documentation of (a), or hand-carried — hand-carried rots); (d) do nothing
until OA-003 lands (loses the "waiting ready" property the capture bought). External
placement (a fleet-side monitor) has no owning surface today and would re-derive what
the deploy job already knows.

**3. Most advanced capability reachable by the simplest implementation?** (a)+(c):
~15 lines appended to the existing deploy job — curl the `page_url` with a small
retry loop (Pages CDN propagation), grep the served payload for the contract const
and `schema_version`, exit non-zero on miss — plus the README line pointing at the
smoke as the verification. Sequencing is self-arming: while Pages is disabled the
run already fails at `configure-pages` (run 29126980391), so the step is inert; the
moment OA-003 lands, the next push both deploys AND verifies. "Live preview" becomes
a claim with a green check attached.

**4. What breaks it?** (i) OA-003 never clicked — the step never executes; cost of
carrying it: zero (the workflow is already red pre-click). (ii) CDN propagation
lag — a naive immediate fetch flakes; the retry loop is load-bearing, not optional.
(iii) Asserting on the wrong payload — the smoke must fetch a file that actually
carries the stamp (the fixture JSON / schema ride the published artifact since the
whole `products/games-web` dir is uploaded; index.html alone might not embed the
version). (iv) Lane self-serve mid-relay — real risk class (five fleet datapoints)
but verified un-executed at `43563dc`, and the lane is order-starved idle ("the
forge needs new ORDERs to build", its own status), which cuts both ways: nobody is
about to self-serve it, and a relay lands on a lane begging for work.

**5. What does it unlock?** The owner's whole-product review happens on a
verified-live surface with zero manual checking; OA-003's click gets an immediate
green/red answer instead of silence; every future forge product inherits the
deploy+smoke pattern from product #1 (the forge is an incubator — patterns compound).

**6. What does it depend on?** OA-003 (owner, one click — the ask already lives on
the lane's own heartbeat and fm owner-queue item 15, deliberately NOT duplicated
here); the committed contract const + `schema_version` (exist at `43563dc`); nothing
cross-lane — the slice is entirely inside the forge's own tree.

**7. Which lane should build it?** product-forge — it owns `deploy-pages.yml`, the
product README, and the review-after obligation; its ORDER 003 work proves the
repo-owned-guard pattern is already house style. Nothing here is this repo's to
build (a foreign workflow), and nothing is sim-shaped (a smoke step is proven by its
own red/green — the #114 precedent).

**8. What is the smallest shippable slice?** ONE forge PR: the smoke step
(fetch-assert-retry) + the README § Live preview last-verified line. Relay shape for
the :30 sweep: a P3 lane ORDER naming this file; the lane is live, continuous-mode,
and idle on a DRY inbox — free throughput.

**Recommendation: park** — (build-direct — lane workflow slice, owner-click-gated):
premises verified intact and un-self-served at live lane HEAD `43563dc`; one forge
PR, inert until OA-003 then self-arming; nothing for sim-lab, relay-ripe for the
manager on an order-starved lane.
