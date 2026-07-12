# Idea: a shared `bytes | None` lazy-PIL contract guard for the card-render family — link index

> **State:** parked(routed — superbot lane build, ride the leaderboard-row-avatars ORDER; probe 2026-07-12)
> **Class:** process · **Target:** `menno420/superbot`
> **Sequence:** before superbot builds leaderboard-row-avatars (the `render_leaderboard_image` signature change — cheapest carrier for the guard; the guard stands alone if that ORDER stalls, see probe Q4)

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/pil-card-render-contract-guard-2026-06-22.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/pil-card-render-contract-guard-2026-06-22.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/pil-card-render-contract-guard-2026-06-22.md)).

A shared bytes|None lazy-PIL contract guard for the card-render family so every renderer honors the same 'return None when PIL is unavailable' contract without bespoke per-test scaffolding.

## Probe report (v0, 2026-07-12)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/1ecc21138fe0a1eb672d03b66bd319164c29d55f/disbot/utils/ux_patterns/image_builders.py@1ecc211 · fetched 2026-07-12
> *(pin annotation: S = superbot live HEAD by `git ls-remote` this session =
> `1ecc21138fe0a1eb672d03b66bd319164c29d55f`. Tree scans via the standing
> read-only blobless-clone recipe at S; file reads via raw at the pinned SHA.
> The canonical idea doc is byte-unchanged `fd638e3`→S (`git diff --quiet`),
> so the harvest pin content IS the HEAD content. The ledger's pin `d647b2e`
> (this repo's PR #204 avatars probe) is 21 commits behind S, but the render
> family is byte-unchanged across them: `git diff --stat d647b2e..S` over
> `disbot/utils` + `disbot/services` + `disbot/cogs/leaderboard_cog.py` +
> `tests/` touches ONLY `tests/unit/scripts/test_check_consistency.py`
> (+31/−5) — every PR #204 probe finding carries to S unchanged.)*
> **Sequence:** before superbot builds leaderboard-row-avatars — that ORDER's
> PR edits `render_leaderboard_image` (image_builders.py:90 @ `1ecc211`), a
> family member the per-module test net does NOT cover today (see Q4), so the
> guard is cheapest landed with/just before it.

> Single-pass battery (panel not escalated: read-only test tooling, reversible,
> no security/data/spend/public blast radius — README § probe battery).
> Verify-first at S: `git grep`/ls-tree over `disbot/utils/*_render.py`,
> `disbot/utils/ux_patterns/`, `disbot/utils/btd6/`, `tests/unit/utils/`,
> `tests/unit/views/`; `docs/decisions/` (8 ADRs, none render/guard-shaped by
> title — the PR #204 probe's zero-hit grep re-confirmed carrying via the
> byte-unchanged diff); superbot `control/inbox.md` @ S (ORDER 001 only).

**1. What is this really?** A ~25–40-line cross-cutting invariant test in
superbot (`tests/unit/utils/test_card_render_contract.py`): an explicit
registry of `(callable, sample_kwargs)` tuples covering every card-render
entrypoint, a forced `PIL` import failure (the `builtins.__import__`
monkeypatch already used verbatim at `tests/unit/utils/test_welcome_render.py:39-50`
@ `1ecc211`), and one assertion — each returns `None`, never raises. Who for:
the superbot lane's Pillow-less environments (sandbox runs degraded — the
canonical doc's motivating crash surface) and every FUTURE renderer author,
because the per-module test net only catches renderers that opted in. The
registry doubles as the family's one-place census, which does not exist today.

**2. What is the possibility space?** Minimal: the explicit registry + one
parametrized test (the canonical sketch's own preferred variant). Wider:
reflection-discovery of `def render_*`-shaped functions (canonical doc names it
and rejects it — signatures differ, reflection must guess valid inputs).
Wider still: graduate the guard into `scripts/check_consistency.py` as a
warn-first static rule (the settle-once precedent) — rejected here: the
contract is behavioral (`ImportError` → `None`), a static grep cannot prove it,
and a 15-line pytest can. Outer ring: the registry becomes the attach point
for future family-wide invariants (no-network assertion, theme-param
acceptance — the visual-card-engine vision's per-feature cards would inherit
each one on arrival).

**3. What is the most advanced capability reachable by the simplest
implementation?** One registry + one monkeypatch test locks the degrade-
gracefully contract across the ENTIRE family at once — measured at S as 9
modules / ~12 public entrypoints (`welcome_render`, `mining_render`
:84/:172, `character_render` :383/:427/:442, `role_menu_render`,
`rank_render`, `profile_render` :37, `card_render` canvas core,
`ux_patterns/image_builders` :90/:183, `btd6/ct_map_render` :100 — all
`-> bytes | None`; `btd6/freshness_render` and `views/setup/draft_render`
are embed/text builders, NOT family members) — and every future renderer
joins by adding one registry line, which a reviewer can demand by pattern.

**4. What breaks it?** (i) Nothing structural — but the canonical premise "the
gap is precisely a *new* renderer" has ALREADY FIRED at S, which the capture
does not know: since the 2026-06-22 four-module census, the without-pillow
net grew unevenly, and today **4+ entrypoints sit outside it** —
`character_render` (its `tests/unit/utils/test_character_render.py` @
`1ecc211` has NO without-pillow test), BOTH `image_builders` builders
(`render_leaderboard_image` :90, `render_event_poster` :183 — no unit-test
file at all; only `test_ux_patterns_registry.py` exists, while the module
docstring :10-11 CLAIMS "Same contract as ``utils/mining_render.py``: lazy
PIL import, ``bytes | None``"), and `btd6/ct_map_render` (its test gates on
`pillow_available()` — never forces the ImportError). A claimed-but-untested
contract is exactly the drift class. (ii) `test_card_render_structure.py` is
NOT this guard: it `skipif`-skips entirely without Pillow ("covered
separately", its own reason string) — layout goldens, wrong axis. (iii)
Sample-kwargs rot: renderers with rich specs (`CharacterSpec`, `CardSpec`)
make registry entries non-trivial; mitigated by reusing each module's existing
test fixtures. (iv) Timing dependency is soft, not hard: if the avatars ORDER
stalls, the guard still pays for the 4 already-uncovered entrypoints — riding
the ORDER is the cheapest carrier, not a precondition. (v) Cutover horizon:
superbot-next EXCLUDES image cards (D-0038 deviation 5, per the PR #204 probe
@ `d647b2e` = byte-carried to S), so the guard never ports — cheap and
disposable by design (canonical doc's own reversibility clause), no
build-twice cost.

**5. What does it unlock?** The avatars PR (TOP-5 #2's named window) lands
against a pinned contract instead of an untested docstring claim — its
signature change to the family's least-tested member becomes regression-proof
for free; every per-feature card the visual-card-engine vision spawns inherits
the contract on arrival; and the registry gives the lane its first one-place
family census (the canonical doc's secondary sell).

**6. What does it depend on?** Nothing unshipped: pytest + monkeypatch pattern
live at S in five test files; no store, no migration, no AI key, no owner
action (Q-0105 read-only test tooling — never gated). Cheapest confirm/kill
evidence, priced: this probe's confirm cost was one blobless-clone diff + six
raw file reads (the decisive facts: no `test_card_render_contract.py` in
ls-tree at S; `render_leaderboard_image` signature :90-96 still
rows/title/value_texts/theme, NO avatars param; superbot `control/inbox.md` @
S carries ORDER 001 only — avatars UNROUTED, window OPEN). The build-time
kill-test is the test file itself: it either reds on a contract violator or
passes — deterministic, self-evidencing, nothing for a simulator to settle.

**7. Which lane should build it — and what does it displace or duplicate?**
**superbot** (legacy live lane) — it owns `disbot/` + `tests/unit/utils/`, and
superbot-next defers image cards wholesale (D-0038 dev 5), so the rebuild has
no seat for it. Honest sim check: NO evidence question survives — the guard is
deterministic test tooling with no parameter space or corpus; sim-lab would
run pytest and report "it passes". No proposal; outbox tail unchanged. Dedup
findings, named: [`leaderboard-row-avatars-2026-07-10.md`](leaderboard-row-avatars-2026-07-10.md)
— parked(routed), the CARRIER, not a duplicate (its build PR edits the exact
uncovered entrypoint); [`visual-card-engine-vision-2026-07-10.md`](visual-card-engine-vision-2026-07-10.md)
— captured, future CONSUMER (each per-feature card joins the registry);
[`settle-once-architecture-guard-2026-07-10.md`](settle-once-architecture-guard-2026-07-10.md)
— sim-ready, same guard-an-honored-contract SHAPE on a different surface
(settlement, static rule) — precedent, not overlap. Repo-wide `rg` for
render/bytes-contract mechanisms (kit machinery excluded, this session): no
duplicate of this guard.

**8. What is the smallest shippable slice?** One superbot test-only PR (or a
commit riding the avatars build PR): add
`tests/unit/utils/test_card_render_contract.py` — an explicit
`(callable, sample_kwargs)` registry covering the ~12 entrypoints in Q3
(sample kwargs lifted from each module's existing tests), the
`test_welcome_render.py:39-50` monkeypatch, one parametrized
assert-returns-None. Zero runtime code touched; deletable in one revert if
noisy.

**Recommendation: park** — routed (superbot lane build, riding the
leaderboard-row-avatars ORDER the manager sweep already carries). Rationale:
the timing claim VERIFIED at live S `1ecc211` (avatars unlanded AND unrouted —
window open) and the premise is STRONGER than captured: 4+ entrypoints
including `render_leaderboard_image` itself already sit outside the
without-pillow net, so the guard pays even if the avatars ORDER stalls;
deterministic test tooling leaves nothing for sim-lab to settle. Best
implementation found: the Q8 explicit-registry test file, monkeypatch reused
from `test_welcome_render.py:39-50`, landed with/just before the avatars PR.
