# Oracle user-copy punctuation-drift sweep — grep rebuild literals against oracle fragments

> **State:** probed
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://github.com/menno420/superbot-next@80464ab39f86d55cede1e38b4780e7b1cc4a1777 · fetched 2026-07-12T01:34:18Z

One cheap sweep: grep the rebuild's user-copy string literals against oracle
`search_code` fragments to catch PUNCTUATION-LEVEL drift in refusal paths the golden
suites don't cover — the class the tournament-entry fix slice hit live and had to leave
out of scope. Live datapoint at the pin, recorded verbatim at the lane heartbeat: the
rebuild's in-memory guard copy in `sb/domain/rps/tournament.py:153` says "You're
already registered." where the oracle says "You're already registered!" —
golden-uncovered, found only because a fix slice happened to reconstruct the oracle
semantics by hand. Source: lane session card
[`.sessions/2026-07-12-tournament-entry-race-fix.md` § "💡 Session idea"](https://github.com/menno420/superbot-next/blob/80464ab39f86d55cede1e38b4780e7b1cc4a1777/.sessions/2026-07-12-tournament-entry-race-fix.md)
(second half) @ `80464ab`
([raw](https://raw.githubusercontent.com/menno420/superbot-next/80464ab39f86d55cede1e38b4780e7b1cc4a1777/.sessions/2026-07-12-tournament-entry-race-fix.md));
the noted-drift datapoint also rides
[`control/status.md`](https://github.com/menno420/superbot-next/blob/80464ab39f86d55cede1e38b4780e7b1cc4a1777/control/status.md)
(the #223 slice's ORACLE SEMANTICS bullet) @ `80464ab`.

## Probe report (v0, 2026-07-12)

> **Grounding:** https://github.com/menno420/superbot-next@af985c17def5ff2478103cb363ebb150cb583a97 · fetched 2026-07-12
> *(pin annotation: N = superbot-next live HEAD by `git ls-remote` at probe time
> — moved past the harvest pin `80464ab`; tree scanned via the standing
> read-only blobless `--no-checkout` ls-tree recipe, every file content fetched
> via raw at the pinned SHA. The drift instance is STILL LIVE at this pin, and
> NO sweep/drift tool has landed — verified below.)*
> **Grounding:** https://github.com/menno420/superbot@1ecc21138fe0a1eb672d03b66bd319164c29d55f · fetched 2026-07-12
> *(pin annotation: S = the oracle repo's live HEAD by `git ls-remote` — the
> SAME sha the source card's search_code fragments were indexed at, so the
> oracle side has not moved since the capture's reconstruction; oracle files
> read via raw at the pin.)*

> Single-pass battery (panel not escalated: process head, reversible verdict,
> no security/data/spend/public surface). Verify-first corrections below —
> the capture's oracle-access framing was seat-scoped, not a fact of the
> world, and it changes the smallest shippable slice.

**Verified live, both pins**

- **Drift instance still live at N `af985c1`:** `sb/domain/rps/tournament.py:153`
  is `return False, "You're already registered."` (period). Oracle byte-form
  verified at S `1ecc211`: `disbot/views/rps/registration.py:49` →
  `"You're already registered!",` and `disbot/utils/tournaments.py:44` →
  `return False, "You're already registered!"` — the punctuation drift is
  real, unfixed, and now double-cited from both trees rather than from
  search_code fragments.
- **Golden-uncovered confirmed mechanically:**
  `parity/goldens/rps_tournament/sweep_rpsregister.json` @ `af985c1` contains
  ZERO occurrences of "registered" — the guard copy lives on a path the
  rpsregister golden never drives. The premise class ("refusal paths the
  golden suites don't cover") holds on the motivating instance.
- **No sweep tool landed since harvest:** N's `tools/` @ `af985c1` = 23
  `check_*.py` + corpus/manifest/parity utilities (full ls-tree); no
  copy-drift / oracle-sweep / golden-checker-shaped file. The two
  nearest-by-name checkers read and ruled out: `check_intent_survival.py` is
  the S15 manifest slash-survivability gate, `check_verified_live.py` is the
  V-5 verification-registry gate. Self-serve check: negative — full battery
  warranted.
- **Access-path correction (load-bearing):** the source card reconstructed
  oracle semantics via `search_code` because "direct oracle file reads +
  list_commits DENIED for this seat" (N card
  `.sessions/2026-07-12-tournament-entry-race-fix.md` § Oracle semantics @
  `af985c1`). That denial is SEAT-scoped: the oracle repo is publicly
  raw-readable at a pinnable sha (both oracle files above fetched directly).
  BUT N's own boundary doctrine says the rebuild "never imports the old bot"
  — oracle-derived inputs arrive as committed artifacts, supplied JSON, not
  live reads (`tools/compute_corpus.py` module header @ `af985c1`; same
  pattern as `parity/goldens/`, 468 committed capture files). So the sweep's
  oracle side is a design choice the spec must settle: committed oracle-copy
  snapshot (doctrine-conformant, can go stale) vs pinned fetch-on-run
  (fresh, breaches the no-import boundary in letter).

**1. What is this really?** A cross-repo copy-equivalence linter for the ONE
   copy class the golden-parity gate structurally cannot see: user-facing
   string literals on paths no golden drives (in-memory guards, refusal
   branches, error copy). The rebuild pins copy to the oracle BY COMMENT
   CONVENTION (`# … verbatim` — sampled: 13 markers in
   `sb/domain/role/handlers.py`, 3 in `sb/domain/rps/tournament.py`, 1 each
   in `sb/domain/games/wager.py` / `sb/domain/economy/handlers.py`, all @
   `af985c1`), but a comment convention is a promise, not a check — the
   motivating drift sits three lines BELOW a "shipped … verbatim" marker.
   For: rebuild hardening sessions and the parity-flip lane, who today find
   this class only when a fix slice hand-reconstructs oracle semantics.
**2. What is the possibility space?** Axes: (i) rebuild-side enumeration —
   `verbatim`-comment-adjacent literals only / AST walk of refusal-tuple
   returns (`return False, "…"` and kin) / all user-reaching string literals
   (send/reply/embed args); (ii) oracle-side source — committed snapshot
   JSON at a pinned sha / fetch-on-run raw reads / search_code fragments
   (the capture's framing — strictly dominated now); (iii) match rule —
   byte-equal assertion on declared pairs / normalized-equal-but-byte-differ
   detection (punctuation/case/whitespace) / fuzzy wording similarity with a
   threshold; (iv) gating — red in the ci.yml `set -e` fleet loop (N's
   convention) / warn-first (S's graveyard) — with a deliberate-divergence
   allowlist either way, because intentional oracle divergences are a
   documented, named class at N (dispositions: kernel-surface-drift,
   xp-coins-alias, invoking-message-deletion — `control/status.md` phase
   line @ `af985c1`).
**3. What is the most advanced capability reachable by the simplest
   implementation?** One stdlib file in N's own pattern:
   `tools/check_copy_drift.py` + a committed
   `parity/oracle_copy.json` snapshot (byte-form fragments pinned
   `@<oracle-sha>`, the compute_corpus supplied-artifact shape). AST-walk
   `sb/` (528 py files) for refusal-tuple/message literals; for each, if a
   snapshot fragment matches under punctuation/case/whitespace
   normalization but differs in bytes → flag. Catches the entire motivating
   class (punctuation-level drift on golden-uncovered copy) with zero
   network in CI and zero new dependencies; re-finding tournament.py:153 vs
   registration.py:49 is the built-in acceptance test.
**4. What breaks it?** (a) Enumeration FP flood: log strings, exception
   messages, docstrings, and NEW-copy (no oracle counterpart) all look like
   literals — the grammar for "user copy" is the make-or-break spec choice,
   and it is NOT obvious across 528 files. (b) Deliberate divergences:
   normalized-match-but-byte-differ is exactly what an INTENTIONAL
   disposition also looks like; without a waiver/allowlist the red gate
   flags policy as drift (the VERDICT 012 waiver-token lesson, same shape).
   (c) Snapshot staleness: a committed oracle snapshot is only as honest as
   its pin; the oracle is frozen-ish (live HEAD unmoved since the capture's
   indexed ref) so decay is slow, but the spec must say who re-pins. (d)
   Fuzzy wording matching below punctuation level is judgment-shaped — if
   the sim shows the fuzzy tier is all-FP, the tool ships punctuation-only
   and the "wording" half of the capture dies. (e) One-instance risk: if
   the sweep finds ONLY tournament.py:153 on the real tree, a one-line fix
   beats a tool — the sim's true-catch count on the real corpora decides
   this, not intuition.
**5. What does it unlock?** The golden-parity gate's blind spot gets a
   fence: copy correctness on never-driven paths stops depending on a fix
   slice happening to wander past. Every future port/flip inherits the
   check for free (one loop word in ci.yml). The committed-snapshot pattern
   also gives later heads (e.g. embed-layout drift) a doctrine-conformant
   oracle-input precedent.
**6. What does it depend on?** (a) Oracle raw readability at a pinnable sha
   — VERIFIED (correction above). (b) An oracle-side snapshot format +
   re-pin owner — spec question. (c) N's AST-walkability of user copy —
   sampled true (refusal tuples are a stable convention:
   `tournament.py:141-165` returns detail-copy tuples; role/handlers same
   shape). (d) The disposition/waiver mechanism — exists as prose classes,
   needs a machine token (VERDICT 012 shipped exactly this for cites). (e)
   Nothing owner-shaped.
**7. Which lane should build it?** superbot-next (the declared Target): the
   copy, the goldens, the checker fleet, the ci.yml loop, and the
   committed-artifact doctrine all live there. NOT superbot — the oracle is
   the reference, not the patient. Displaces/duplicates: **VERDICT 012's
   `check_doc_cites.py`** (`ideas/superbot/rebuild-design-cite-checker-2026-07-10.md`,
   sim-ready, approve) is the same sweep-pattern FAMILY — stdlib file, one
   ci.yml loop word, grammar × scope × gating settled by a sim on real
   pinned corpora, inline waiver token — but a DIFFERENT corpus (markdown
   `path:line` cites vs python user-copy literals) and a DIFFERENT
   comparison (referent-exists/line-valid vs cross-repo byte-equivalence).
   One tool cannot serve both cores; what transfers is the sim HARNESS
   shape (sim-lab `sims/verdict-012-doc-cite-checker-spec/cite_checker_sweep.py`
   — pinned corpora fetch-on-run, variant cells, per-cell TC/FP, planted
   recall) and the waiver-token gating pattern. Building a shared
   "sweep kit" abstraction instead is the authoring-kit trap (PR #230's
   park: no queued third consumer). Also swept: `golden-recapture-on-bugfix`
   (parked(routed) — golden freshness, adjacent), `parity-flip-cadence`
   (parked(overtaken) — coverage cadence, adjacent),
   `rebuild-critical-review-checkers` (parked(routed) — no copy-sweep item
   in its backlog). No duplicate head.
**8. What is the smallest shippable slice?** `tools/check_copy_drift.py`
   (stdlib, AST-walk + normalize + compare) + `parity/oracle_copy.json`
   (committed snapshot, fragments pinned `@1ecc211`) + one word in the
   ci.yml checker loop — the sim-selected enumeration grammar,
   normalization tier, and gating; acceptance = re-finds tournament.py:153
   red, goes green when the period becomes `!`. This-repo-side: this probe
   + the coordinator's outbox PROPOSAL (control/ boundary).

**Recommendation: sim-ready** — same family as VERDICT 012 and it earns the
sim the same way: a real parameter space (enumeration grammar × match
normalization × gating/waiver) over two real, pinned, public corpora, where
the wrong grammar drowns the tool in log-string FPs and the wrong gating
flags deliberate dispositions as drift — and where the true-catch count on
the real tree (is tournament.py:153 alone, or one of many?) decides between
a tool and a one-line fix. Best implementation found: committed
oracle-copy snapshot + stdlib AST sweep at N (Q3/Q8), harness shape reused
from `cite_checker_sweep.py`. The ONE question the simulator should settle:
**which (user-copy enumeration grammar × match-normalization tier) cell
maximizes true drift catches at near-zero false positives on the real
corpora (superbot-next @ `af985c1` sb/ literals vs superbot @ `1ecc211`
disbot/ copy), and does the winning cell's true-catch count justify a
red-gating checker over a one-line fix?** Done-when: per-cell TC/FP on the
real corpora + planted-drift recall, the winning grammar + normalization +
gating/waiver spec stated machine-readably, and the tournament.py:153
instance caught by the winning cell.

*(State-flip note, dispatch boundary: this probe slice is barred from
`control/` writes, and the outbox↔ideas gate correctly couples a `sim-ready`
STATE to an outbox PROPOSAL naming the file — so the state line advances
`captured`→`probed` here, and the coordinator advances `probed`→`sim-ready`
in the same slice that appends the PROPOSAL (question + done-when are
paste-ready in the verdict paragraph above; grounding pins: superbot-next
`af985c17def5ff2478103cb363ebb150cb583a97`, superbot
`1ecc21138fe0a1eb672d03b66bd319164c29d55f`). Forward-only holds.)*
