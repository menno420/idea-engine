# Own-heartbeat parse self-check in `quality` — link index

> **State:** parked(overtaken-by-events — the lane shipped this exact slice itself as websites PR #79 (`0f2cd17`, 2026-07-10T22:52:30Z), ~19 minutes after the PR #37 harvest pinned the bullet as captured; the fleet-generic extension-key residue is cross-linked to substrate-kit — see probe report)
> **Class:** process · **Target:** `menno420/websites`
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/backlog.md@144dfce · fetched 2026-07-10T22:33Z

**Canonical idea (stays in websites — indexed by link, never copied):**
backlog bullet #11 under
[`menno420/websites → docs/ideas/backlog.md` § Captured / planned](https://github.com/menno420/websites/blob/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/backlog.md#captured--planned-pick-highest-value-buildable-first)
— harvested 2026-07-10 inside the lane-backlog link index
([`lane-backlog-2026-07-10.md`](lane-backlog-2026-07-10.md), PR #37), pinned @ websites
`144dfce`; this sibling entry gives the bullet its own probe home
([raw](https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/backlog.md)).

Run the websites repo's own `control/status.md` through its `/fleet` parsers at PR
time, so a malformed heartbeat fails red in the required `quality` check instead of
rendering wrong on the live fleet page. The documented failure class (the bullet's
source citation, `.sessions/2026-07-10-heartbeat-enrichment.md` 💡): a heartbeat that
its own consumers can't parse fails SILENTLY — the pre-D-0028 `routine:` line leaked
into `blockers:` as a continuation and the live page showed
`blockers: none routine: ARMED …` for hours, with no red anywhere.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8c19e930f6dedd8b230538789a579cf1ce337f3c/docs/ideas/backlog.md@8c19e93 · fetched 2026-07-11T00:39Z (manifest row: behind)
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/7c6278ec990d9230aac439cb748465bf23bcec56/docs/eap/fleet-manifest.md@7c6278e · fetched 2026-07-11T00:35Z
> **Sequence:** after websites PR #79 (`0f2cd17`, 2026-07-10T22:52:30Z) — the lane built this exact slice itself between the PR #37 harvest fetch (22:33Z @ `144dfce`) and this probe

*Timeliness verified live FIRST (the PR #25 lesson). websites HEAD
`8c19e930f6dedd8b230538789a579cf1ce337f3c` transport-verified via `git ls-remote
refs/heads/main` at 2026-07-11T00:32Z — AHEAD of the harvest pin `144dfce`, and this
time the delta is decisive: commit `0f2cd17e37b9a6edea53c49a288bfa11dc52c4c0`
("Own-heartbeat parse self-check in quality + manifest-badge bullet retired (#79)",
authored 2026-07-10T22:52:30Z) added `tests/test_own_heartbeat.py` (103 lines, 5 tests;
suites 180 → 185 per the lane card `.sessions/2026-07-10-own-heartbeat-selfcheck.md` @
`0f2cd17`) and moved the backlog bullet to its Built section — at `8c19e93` it reads
"**Own-heartbeat parse self-check in `quality`** — shipped 2026-07-10 (continuous-mode
slice 7)". The idea is ALREADY BUILT by its own lane. Note for the harvest ledger: the
prior idea-engine slice's `check_harvest` run honestly reported websites `8c19e93` as
"HEAD MOVED (docs unchanged)" — that label means the doc FILENAME SET is unchanged;
the backlog's CONTENT changed underneath it (47 insertions / 31 deletions between the
pins, `git diff --stat 144dfce..8c19e93 -- docs/ideas/`), which is how a bullet
lifecycle flip stays invisible to the checker (measured here, flagged as a follow-up,
not fixed in this slice).*

**1. What is this really?**
A dogfood contract test: the lane runs its own committed heartbeat through the SAME
parser its consumers use (`app/fleet.py parse_status` / `freshness` /
`classify_health` / `parse_orders` / `classify_routine` / `classify_landing`), so
writer/parser drift reds at PR time instead of rendering wrong silently. It is the
websites-local instance of a fleet-wide contract — "the heartbeat and its parsers
must move together" — and websites is uniquely both WRITER of one heartbeat and
PARSER of everyone's (its `/fleet`, `/orders`, `/fleet.json` machine-read every
manifest lane's `control/status*.md`; `app/orders.py:179` @ `8c19e93`).

**2. What is the possibility space?**
- **Lane-local test (SHIPPED):** `tests/test_own_heartbeat.py` @ `0f2cd17` — required
  fields present, `updated:` parses (unparseable = dark lane to the manager),
  `health:` classifies, `orders:` machine-readable, optional `routine:`/`landing:`
  classify, and no enriched key leaks into `blockers:` (the pre-D-0028 class,
  regression-pinned).
- **Fast-lane enforcement (REJECTED by the lane, honestly documented):** heartbeat-only
  PRs ride the `control/**` fast lane and skip pytest by design, so a bad heartbeat
  reds the NEXT non-control PR — a standing floor, not same-PR enforcement; running
  just this file in the fast lane was considered and rejected (one enforced gate, no
  second logic path — the test file's own docstring).
- **Fleet-generic (the residue):** every OTHER lane writes a heartbeat no test parses.
  The kit already machine-reads slices of each repo's own `status.md`
  (`bootstrap check`: heartbeat presence/staleness; the `kit:` line) — a kit-owned
  grammar self-check finding is the one-grammar/one-parser home (the PR #29 seat-boot
  routing family), not N per-lane copies of websites' parser.
- **Degenerate corner (measured live, this probe):** parser-side key registries drift.
  websites' `KNOWN_KEYS` (`app/fleet.py` lines 48–64 @ `8c19e93`) is a hand-kept copy
  of the heartbeat grammar; any lane-invented extension key folds into the previous
  field as a continuation. Ran idea-engine's own `control/status.md` (@ this repo's
  `41c54b9`) through `fleet.parse_status` @ `8c19e93` locally (pure parser, network
  imports stubbed): it parses — `project=idea-engine`, `health:` classifies green,
  `updated:` fresh, `routine:` classifies armed — but this repo's two extension keys
  `mode:` and `BACKPRESSURE:` are not in `KNOWN_KEYS`, so BOTH fold into `phase`
  (9,551 chars), the exact leak class the lane's test guards; and
  `orders: acked= done=` (legitimately empty — no manager ORDERs yet) returns
  `parse_orders ok=False`, the honest free-text fallback.

**3. What is the most advanced capability reachable by the simplest implementation?**
Already reached, lane-side: one 103-line stdlib test file turns the live fleet page's
silent-misrender class into a red PR check, exercising the REAL committed artifact
through the REAL consumer code paths — zero new surface, zero network. Fleet-wide, the
simplest carrier for the same capability is the kit's existing `check` (it already
runs in every adopted repo and already reads the repo's own heartbeat for
staleness/kit-line): one added grammar-parse finding gives every lane the self-check
at its next kit upgrade, without any lane copying websites' parser.

**4. What breaks it?**
- **The fast-lane gap (accepted, documented):** a malformed heartbeat landed by a
  control-only PR stays green until the next non-control PR — delayed floor, by
  doctrine.
- **Extension keys (the live one):** the documented grammar (`control/README.md`
  status format) has no extension-key declaration seam, so every local invention —
  this repo's `mode:`/`BACKPRESSURE:`, websites' own D-0028 enrichment before
  `KNOWN_KEYS` learned it — leaks as a continuation in every KNOWN_KEYS-style parser.
  A strict self-check pinned to the documented grammar would conversely RED legitimate
  local extensions; the grammar needs a declaration story before strict enforcement is
  honest.
- **Parser-copy drift:** websites `KNOWN_KEYS`, the kit's heartbeat checks, and any
  future manager roster parser are three key lists with no shared source of truth —
  the kit-line-self-drift class, on the heartbeat itself.
- **Consumer gating hides latency:** idea-engine has NO row in the fleet manifest @
  superbot `7c6278e` (13 `menno420/` repo refs, none idea-engine — only the superbot
  row's prose "Idea Engine seat pending owner Project click") and no entry in
  websites' fallback `config.FLEET_LANES` (`app/config.py:196` @ `8c19e93`), so no
  mechanical consumer parses THIS repo's heartbeat today; `/fleet` auto-adds lanes
  when the manifest row appears (by design), and the leak goes live that same moment
  with nothing red anywhere.

**5. What does it unlock?**
Lane-side (already banked): heartbeats stay machine-readable as enrichment accretes;
the manager's staleness math and `/orders`' outstanding-work computation stay
trustworthy; the pre-D-0028 leak can't silently recur on websites' own heartbeat.
Fleet-side (if the kit residue is built): the same floor under all ~12 heartbeats the
fleet pages read, including the ones no lane test covers — and for idea-engine
specifically, this probe already cashed the first dividend: the `mode:`/`BACKPRESSURE:`
leak is now a KNOWN latent misrender, found by measurement before the manifest row
makes it live.

**6. What does it depend on?**
Lane-side: nothing — shipped and green (`quality` is the required check). Fleet-generic
residue: the kit-owned heartbeat grammar (`control/README.md` is kit-planted), the
kit's existing per-repo `check` as carrier, and a grammar decision on extension keys
(declare-then-parse vs known-set-only) — the same seam family as the PR #29 seat-boot
heartbeat-parser routing and the captured `kit-line-self-drift-local-check` idea, so
it composes with work substrate-kit already has indexed.

**7. Which lane should build it?**
- **websites: nothing left to build** — it built its own slice (PR #79) off its own
  backlog, exactly as the never-idle ladder intends; this section's verdict must not
  invent residual websites work where the lane already shipped.
- **substrate-kit owns the fleet-generic residue** (kit-owned grammar self-check in
  `check` + the extension-key declaration story) — routed as a Cross-links entry in
  `ideas/substrate-kit/README.md` (the PR #29/#40 precedent), NOT as a stretched
  websites verdict; no build ORDER is proposed from this probe.
- **idea-engine (self, no build):** whether to keep `mode:`/`BACKPRESSURE:` as
  undeclared extension keys or fold them into documented fields is a one-line
  heartbeat-format decision for a future grooming slice — noted, not executed here.

**8. What is the smallest shippable slice?**
Websites-side: NONE REMAINING — the smallest slice was the 5-test file plus backlog
hygiene, and PR #79 shipped precisely that. The residue's smallest slice is kit-side
and belongs to substrate-kit's queue, not this verdict: one advisory `check` finding
that parses the repo's own `status.md` against the planted grammar and WARNS on
unknown top-level keys (advisory first — strict only after the grammar grows an
extension-key declaration, per Q4).

**Recommendation: park** — overtaken by events: the websites lane shipped this exact
slice itself (PR #79, `0f2cd17`) ~19 minutes after the harvest pinned it as captured,
and the genuinely-open remainder (kit-grammar self-check + extension-key declaration)
is substrate-kit's seam, cross-linked per the PR #29/#40 precedent — no simulator
question anywhere (a contract test is proven by its own red/green run, and the leak
class was measured live in this probe, not simulated).
