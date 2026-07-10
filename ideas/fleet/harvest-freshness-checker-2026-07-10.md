# Harvest freshness checker

> **State:** probed
> **Class:** process · **Target:** `menno420/idea-engine` (this repo's own tree — built here, see report Q7)
> **Grounding:** https://github.com/menno420/superbot @ fd638e3c0693687a62093aa6bd75954e238fa58d · fetched 2026-07-10 (harvest pin; live HEAD checked this session)

**Origin:** the PR #7 session card 💡 first flagged it (a link-index harvest is a snapshot,
and snapshots rot); dispatched via the PR #21 card
(`.sessions/2026-07-10-grammar-grooming.md` § Handoff), which names it head of the ripest
non-proposal next-slice list.

**The idea:** a report-only drift checker for link-index sections harvested from a
canonical repo. `ideas/superbot/README.md` link-indexes superbot's entire `docs/ideas/`
backlog (233 docs) pinned @ superbot `fd638e3` — a point-in-time snapshot of a repo that
keeps moving. Nothing today tells a wake whether that pin is stale, how MANY new upstream
docs have appeared since the harvest, or whether an indexed doc was deleted upstream (a
dead link in the partition surface parallel agents trust). The checker parses each
harvested section README for its pin and its indexed canonical paths, asks the canonical
repo (public raw/API path, Q-0260 read-only) for its live HEAD and current doc listing,
and reports three drift classes: HEAD moved past the pin · NEW upstream docs not indexed ·
indexed docs DELETED upstream. The drift COUNT sizes the next re-harvest slice — drift is
information, not failure.

## Probe report (v0, 2026-07-10)

**1. What is this really?**
A staleness detector for the harvest-by-link convention (README § Idea file grammar:
"harvested lane-born ideas are indexed by link, never mass-copied"). The link index is a
promise — "this section reflects the lane's backlog" — that silently decays the moment the
canonical repo moves. This turns the pin (`@ fd638e3`) from decoration into a checkable
claim: the same drift class as the section-sync checker (#2), one level up — sections
mirror the manifest; a harvested section's CONTENTS mirror a canonical directory.

**2. What is the possibility space?**
Four axes: **action** (report-only → emit a ready-to-paste index stub per new doc → open
the re-harvest PR itself); **scope** (one section today → every harvested section via the
SECTIONS table → cross-repo generic, a substrate-kit candidate like Q2 of the #2 probe);
**depth** (existence-only diff → per-doc content drift via blob shas → state drift: an
indexed `captured` whose canonical doc advanced to built); **integration** (wake-time
manual → scheduled routine step — but NEVER preflight/CI, see Q4).

**3. What is the most advanced capability reachable by the simplest implementation?**
One `git ls-remote` + one GitHub contents-API call gives every wake a live, quantified
answer to "how stale is the harvest?" — including the two cases prose review essentially
never catches: upstream deletions (dead canonical links) and the real NEW-doc count (the
next harvest slice gets sized by data, not vibes). A second harvested lane is a one-line
SECTIONS-table addition.

**4. What breaks it?**
- **Network dependence — therefore it must NOT join `scripts/preflight.py`.** CI stays
  hermetic: preflight gates PRs, and a GitHub API blip must never red a PR that changed
  nothing. This is wake-time tooling, run by hand or by a routine wake, explicitly outside
  the preflight ritual (the one existing network check, `check_sections.py`, has a
  `--manifest FILE` offline seam; this checker's whole POINT is the live comparison, so it
  takes exit 2 = could-not-run instead of an offline mode).
- **Index-entry format drift** — it parses the section README's pin line and
  `canonical: <repo> \`<path>\`` entries; a reformatted index parses to zero entries. Fail
  LOUD (exit 2 on zero parsed entries / no pin), never a false clean.
- **GitHub raw/API unreachable or rate-limited** — unauthenticated API is 60 req/h per IP;
  one request per run is fine, a tight loop is not. Found live at build time: this
  session's egress proxy walls `api.github.com` per-repo (403) while git egress stays
  open — so the shipped checker falls back from the contents API to a blobless
  no-checkout shallow clone + `git ls-tree` (~1s, trees only). Both paths dead → exit 2.
- **Canonical repo goes private/DARK** — the pokemon-mod-lab precedent (PR #15 card): raw
  path 404s look identical to deletion. `ls-remote` failing while the API 404s is the
  DARK signature; the checker reports could-not-run, and grounding falls back to
  manifest-relay per the README's DARK-lane rule.

**5. What does it unlock?**
Scheduled re-harvest slices sized by real drift counts (the wake sees "N new upstream
docs" and dispatches a bounded harvest, not a full 233-doc re-scan); dead-link detection
for the trail (deleted canonical docs); and the pattern for every future harvested lane —
the second-lane harvest (already on the ripest list) lands pre-instrumented.

**6. What does it depend on?**
The harvested README keeping its pin line (`pinned @ … (\`<full-sha>\`)`) and entry format
(`canonical: superbot \`docs/ideas/<file>.md\` @ …`); `git ls-remote` egress to github.com
and the unauthenticated contents API (both proxied fine in this environment); the
canonical repo staying public (Q4); python3 stdlib + git (both already required here).

**7. Which lane should build it?**
**idea-engine — this repo, directly.** It checks this repo's own harvested sections
against a repo this repo already reads read-only (Q-0260); only this repo's sessions
write here. Not substrate-kit today: the index grammar is this repo's, though the
generic "committed snapshot of an external directory" pattern could graduate later as
its own idea (same routing as the #2 probe's Q7).

**8. What is the smallest shippable slice?**
`scripts/check_harvest.py` — stdlib-only, report-only, ~170 lines: parse the section
README (pin + indexed canonical paths), `git ls-remote` the canonical HEAD
(MOVED/UNMOVED), one contents-API call (blobless `ls-tree` fallback, see Q4) to
enumerate live `docs/ideas/*.md`, print NEW/UNMARKED/DELETED/HEAD-moved findings.
Exit 0 whenever the check RAN (drift is information, not failure); exit 2 = could
not run. Cheaper to build than to route: it ships **in this
same PR** per the PR #2 precedent (README § probe battery blesses the shortcut for
trivial repo-internal PROCESS tooling) and ran green live against the moved superbot
HEAD (output in `.sessions/2026-07-10-harvest-freshness-checker.md`).

**Recommendation: park(built-here — scripts/check_harvest.py, report-only wake-time drift checker)** —
rationale: trivial repo-internal PROCESS tooling per the blessed same-PR shortcut (first
used by PR #2; deviation-from-routing flagged exactly as there) — nothing routes to
sim-lab (no reproducible question worth a cycle; the checker's own live run IS the
evidence), and the state advances to `historical(<merged PR>)` on merge.
