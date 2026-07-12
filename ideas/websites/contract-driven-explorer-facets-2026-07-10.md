# Contract-driven explorer facets — the game-data explorer derives its UI from the versioned contract

> **State:** parked(build-direct — first-commit design constraint on P002 phase-2, not an independent build surface; fold "generate facets/columns/search from the versioned contract, fail-closed on unknown version — extending the contract format with per-family field/type/facet metadata first, which rides the fm ORDER 012/013 contract fan-in" into the phase-2 explorer ORDER when the manager routes it — see probe report)
> **Class:** product · **Target:** `menno420/websites`
> **Sequence:** before websites builds P002 phase-2 explorer UI #1
> **Grounding:** https://raw.githubusercontent.com/menno420/idea-engine/698fd93869f8a05200f26fde45bbd71596323e6a/ideas/websites/superbot-site-stats-data-story-2026-07-10.md@698fd93 · fetched 2026-07-10T22:08Z
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/0cd08d2da1580fffff1595a6f4119b6d98a8b4b3/dashboard/data_source.py@0cd08d2 · fetched 2026-07-10T22:08Z

## Problem

PROPOSAL 002's phase-2 explorer rides the live committed-feed pattern, but the
probe's Q4 names its real break: only families `meta`+`bugs` are contracted at
version 1, the game corpora (BTD6 towers/upgrades/bosses, mining items/recipes,
fish, creatures) are not contracted families at all, and "an explorer built on
un-contracted exports inherits the BUG-0022 silent-desync class … B's real cost
is contract extension, not UI." Built the obvious way, every new family costs
TWICE: a superbot-side contract/export extension AND a websites-side hand-built
facet/column/search UI — two lanes paying per family, forever, with the UI copy
free to drift from the contract it renders.

## Idea

Make the contract the explorer's only UI source of truth: the explorer reads the
versioned contract file itself (family list, field names/types, which dimensions
are facetable) and *generates* its browse facets, table columns, and search
fields from it — fail-closed on an unknown schema version, exactly the checker
doctrine the feed already lives by ("never fake data", honest-unavailable
banners, `dashboard/data_source.py`). Result: when superbot contracts a new
family, the family appears in the explorer with ZERO websites diff — the
per-family cost halves to one lane, the UI *cannot* desync from the contract,
and the probe's Q5 flywheel ("forces the #1920 contract to grow
family-by-family — hardening every other consumer of the same feed for free")
spins without a websites session per turn. The `leaderboards` family (sibling
capture, this section) would be its first zero-diff arrival if both land.

**Why now:** phase 2 is routable now without the sim verdict (probe
recommendation), and schema-driven vs hardcoded is a first-commit fork —
retrofitting generation under two or three hand-built family UIs is the
expensive path, choosing it before UI #1 exists is nearly free.

## Probe report (v0, 2026-07-12)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/1ecc21138fe0a1eb672d03b66bd319164c29d55f/dashboard/data/dashboard_data_contract.json@1ecc211 · fetched 2026-07-12T00:32Z
> *(pin annotation: superbot live HEAD by `git ls-remote refs/heads/main` same
> fetch = `1ecc21138fe0a1eb672d03b66bd319164c29d55f`, so the pinned URL is what
> was read — the version-1 contract file itself, quoted in the timeliness block.)*
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8f9765483a7df57ce426e7d11d200f10b5495ed7/dashboard/data_source.py@8f97654 · fetched 2026-07-12T00:33Z
> *(pin annotation: websites live HEAD by `ls-remote` same fetch = `8f97654` —
> BYTE-IDENTICAL to the HEAD the pulse-feed probe (PR #222) blobless-cloned and
> fully scanned 2026-07-11T23:57Z, so that probe's whole-tree findings — nothing
> explorer-shaped, inbox ORDERs 001–011 none story/explorer-shaped — carry over
> to this exact commit without a re-clone.)*
> **Sequence:** before websites builds P002 phase-2 explorer UI #1 — schema-driven
> vs hardcoded is decided at the explorer's first commit; retrofitting generation
> under hand-built family UIs is the expensive path

> Single-pass battery (panel not escalated: docs/design-constraint surface,
> reversible, no security/data/spend/public blast radius — README § probe
> battery). Verify-first grounding live this probe (2026-07-12 ~00:31–00:33Z),
> pins above; sim-lab VERDICT 011 (owner-002 four-websites audit, 243 self-checks,
> @ sim-lab HEAD `0622118`) and websites inbox state cited via the sibling probe's
> same-session fetches at the identical websites SHA
> ([`fleet-program-pulse-feed-2026-07-10.md`](fleet-program-pulse-feed-2026-07-10.md)
> probe report, PR #222 / commit `9980356`).

*Timeliness verified live FIRST (the PR #25 lesson). The decisive live finding,
at superbot HEAD `1ecc211`: the version-1 contract is a THIN envelope, not a UI
schema. Quoted structure, in full apart from its `_comment`: `{"version": 1,
"contracted_families": ["meta", "bugs"], "meta": ["generated_at", "build",
"counts", "schema_version"], "bug": ["id", "title", "status", "summary"]}` — a
per-family list of GUARANTEED FIELD NAMES ("values may be null"), with NO types
and NO facetable-dimension metadata. So the capture's generation target is
PARTIALLY reachable today: table columns and search fields are generatable from
the name lists as-is, but facets need the contract format to GROW per-family
field/type/facet metadata — and the game corpora the explorer exists for (BTD6
towers/upgrades/bosses, mining, fish, creatures) are among the 11/13 families
still uncontracted (the pinned-feed-contract probe's live census). Meanwhile at
websites `8f97654` the consumer doctrine the capture leans on is live and
unchanged — `dashboard/data_source.py` "never fake data", honest
"data temporarily unavailable" banners — and NOTHING explorer-shaped exists in
the tree; the phase-2 explorer is UNBUILT and UNROUTED (inbox ORDERs 001–011,
none story/explorer-shaped) despite VERDICT 003's explicit "phases 1–2 … do NOT
wait". The first-commit window this capture was filed to catch is therefore
STILL OPEN — the exact window the pulse-feed sibling watched half-close.*

**1. What is this really?**
A first-commit DESIGN CONSTRAINT on someone else's routed work, not a build item:
when the manager routes PROPOSAL 002 phase 2 (the game-data explorer), its first
commit must derive facets/columns/search from the versioned contract file and
fail closed on an unknown `meta.schema_version` — instead of hand-building
per-family UI that is free to desync (the BUG-0022 class the contract exists to
kill, per the parent probe Q4: "B's real cost is contract extension, not UI").
Who it is for: the websites lane (per-family UI cost drops to zero diffs), the
superbot lane (its contract growth instantly surfaces publicly — the parent
probe Q5 flywheel), and every family that lands after UI #1 — the `leaderboards`
sibling would be the first zero-diff arrival.

**2. What is the possibility space?**
- **UI source of truth:** hardcoded per-family templates (the default the lane
  will drift into) → contract-derived columns+search only (reachable at contract
  version 1 as measured — the name lists suffice) → fully contract-derived
  facets/columns/search (needs the format to grow field/type/facet metadata) →
  contract + per-family display hints (labels, sort order) as a versioned
  overlay. The capture wants tier 3; tier 2 is free today.
- **Where the metadata lives:** grown inside `dashboard_data_contract.json`
  (one source of truth, rides the existing version bump + fail-closed checker) ·
  a separate websites-side view-config (rejected: reintroduces the two-lane
  per-family cost and the drift the capture kills) · inferred at render time
  from the data itself (rejected: inference on uncontracted shapes IS the
  silent-desync class).
- **Assumptions, named:** the explorer stays on the committed-feed path (VERDICT
  003 phases 1–2, no API); the contract format's growth is superbot-lane work
  inside the fm ORDER 012/013 fan-in; fail-closed means the explorer renders the
  honest-unavailable banner on version mismatch, never a guessed UI.

**3. What is the most advanced capability reachable by the simplest implementation?**
One render-time loop over `contracted_families` — columns from the field-name
list, search over the same names, a version gate on `meta.schema_version` — is
buildable against the LIVE version-1 contract with zero superbot work, proving
the mechanism on `meta`+`bugs` while the game families are still uncontracted.
The advanced capability arrives when the contract grows typed/facetable field
metadata: every subsequent family (leaderboards, mining, fish, creatures) then
lands as a superbot-side contract PR with ZERO websites diff, and the UI cannot
desync from the contract because it has no other input. Measured caveat, not
guessed: facet QUALITY (which dimensions are worth faceting) is judgment the
contract must encode — generation makes it cheap, not automatic.

**4. What breaks it?**
- **Sequencing (decisive):** the constraint is worthless the day after the lane
  hand-builds family UI #1 — the pulse-feed sibling's window half-closed exactly
  this way, on a page nobody watched. The Sequence pin above is the guard, and
  the phase-2 ORDER is the only carrier that reaches the lane in time.
- **Contract-format gap (measured, this probe):** version 1 carries no
  type/facet metadata — full generation needs the format to grow, which is
  superbot-lane work that only moves inside the fm ORDER 012/013 providing ORDER
  (decided, verified unrouted/owner-held by the pinned-feed-contract probe). If
  phase 2 routes FIRST, the fold-in must say "columns+search from the v1 name
  lists now; facets when the format grows" — not wait.
- **Cheapest confirm/kill evidence, priced:** this probe's single raw fetch of
  the contract file settled the load-bearing question (metadata sufficiency) for
  the cost of one HTTP GET; the kill-test for the folded constraint is equally
  cheap — a contracted-family fixture with a bumped version must render
  fail-closed, a new family entry must appear with zero websites diff.
- **Overlay creep:** display hints (labels, ordering, units) leaking back into
  websites code re-opens the two-lane cost by the back door; they belong in the
  contract or nowhere.

**5. What does it unlock?**
The parent probe Q5 flywheel without a websites session per turn: every family
superbot contracts is instantly browsable public UI, which makes contract growth
visibly rewarding and hardens every other consumer of the same feed for free.
Plus the per-family cost halving (one lane instead of two), the structural
impossibility of UI/contract desync, and a zero-diff landing slot for the
`leaderboards` family (sibling capture, this section) if both land.

**6. What does it depend on?**
- The manager routing PROPOSAL 002 phase 2 to websites (VERDICT 003 cleared
  phases 1–2 explicitly; verified still unrouted at websites inbox @ `8f97654`)
  — the constraint's only carrier.
- For FULL generation (facets): the contract format growing per-family
  field/type/facet metadata + the game families getting contracted at all —
  both superbot-lane moves inside the fm ORDER 012/013 fan-in (decided,
  unrouted, owner-held per the pinned-feed-contract probe's live pins).
- NOT a dependency: auth, databases, the read-only API, any new service — the
  committed-feed path end to end.
- Cost, priced honestly: as a folded constraint, ~zero — one instruction line in
  the phase-2 ORDER plus the generation loop being the FIRST implementation
  instead of a retrofit; this probe itself was docs-only (one contract fetch,
  one consumer fetch).

**7. Which lane should build it — and what does it displace or duplicate?**
**websites** implements the generation loop (inside the phase-2 ORDER);
**superbot** owns the contract-format growth (inside the fm ORDER 012/013
providing ORDER); **nobody** builds anything from THIS file — it is a constraint
rider. Dedup findings, named:
- PARENT, NOT DUPLICATE: [`superbot-site-stats-data-story-2026-07-10.md`](superbot-site-stats-data-story-2026-07-10.md)
  (PROPOSAL 002) — this capture is a design constraint on its phase 2; the
  parent's probe Q4 is this file's founding quote.
- SAME SHAPE, DIFFERENT PHASE: [`fleet-program-pulse-feed-2026-07-10.md`](fleet-program-pulse-feed-2026-07-10.md)
  — parked(build-direct) riding the phase-1 story-page routing (PR #222); this
  file is the phase-2 twin of that ride-the-routing move, and its half-closed
  first-commit window is the cautionary precedent the Sequence pin encodes.
- SUPPLY SIDE, NOT DUPLICATE: [`../superbot/pinned-feed-contract-for-dashboard-json-2026-07-10.md`](../superbot/pinned-feed-contract-for-dashboard-json-2026-07-10.md)
  — parked(routed) into the fm ORDER 012/013 fan-in; it grows WHICH families are
  contracted, this file makes the contract also carry HOW they render. Its probe
  already names "websites stats/explorer" as a blocked consumer.
- FIRST CUSTOMER: [`public-leaderboards-committed-feed-2026-07-10.md`](public-leaderboards-committed-feed-2026-07-10.md)
  — parked(routed); the `leaderboards` family is the first zero-diff arrival if
  both land.
- Dedup scan of `ideas/` for facet/contract-driven/schema-derived UI mechanisms:
  no duplicate found (repo-wide grep, kit machinery excluded, this session).

**8. What is the smallest shippable slice?**
No independent slice ships from this file. The deliverable is ONE instruction
folded into the manager's phase-2 explorer ORDER when it routes: "derive the
explorer's facets, table columns, and search fields from
`dashboard_data_contract.json`; fail closed (honest-unavailable banner) on an
unknown `meta.schema_version`; columns+search generate from the version-1
field-name lists TODAY — extend the contract format with per-family
field/type/facet metadata (superbot lane, fm ORDER 012/013 fan-in) before or
alongside facets; new families must land with zero websites diff, proven by a
fixture test." A coordinator-analysis alternative was weighed and declined on
this probe's evidence: parking blocked-on-012/013 would idle the constraint
behind the WRONG dependency — VERDICT 003 lets phase 2 route any day without
012/013, and if it routes first the constraint must already be riding it; the
metadata gap is a named dependency of full generation, not of the fold-in.

**Recommendation: park** — build-direct, as a first-commit design constraint on
P002 phase 2: no simulator question exists (deriving UI from a JSON contract is
deterministic and trivially demonstrable at build time — judgment/routing only,
the PR #222 precedent), the first-commit window is verified still open (nothing
explorer-shaped at websites `8f97654`, phase 2 unrouted), and the best
implementation found is the Q8 fold-in — generate columns+search from the live
version-1 name lists now, grow the contract format (fm ORDER 012/013 fan-in) for
facets, fail-closed on version mismatch — recorded with a Sequence pin so the
constraint lands before explorer UI #1 exists.
