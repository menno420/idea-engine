# Idea — rebuild schema-growth ledger (enforce the second-consumer rule mechanically) — link index

> **State:** historical(built-at-target — D-0005 @ `2f4b2c3`)
> **Class:** process · **Target:** `menno420/superbot-next`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/rebuild-schema-growth-ledger-2026-07-03.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-schema-growth-ledger-2026-07-03.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-schema-growth-ledger-2026-07-03.md)).

Enforce the second-consumer rule mechanically: every schema-field addition to the rebuild grammar carries a same-PR ledger entry naming the ≥2 consumers that justified it, with a CI checker diffing grammar fields against the ledger.

## Verify note (2026-07-11) — built at target, flipped historical

> **Grounding:** https://github.com/menno420/superbot-next@2f4b2c3dcf4a13f32dd1e758908a886cc5b1d704 · fetched 2026-07-11T17:57:33Z

PR #194's mint-time ledger check priced this head out of the third TOP-5 as built at
N (D-0005, then @ `870a16c`) and flagged the verify-and-flip micro-slice. This slice
VERIFIED at the target — reading the artifact itself and its invocation sites, not
just greps — via per-file raw reads at the pinned live HEAD
`2f4b2c3dcf4a13f32dd1e758908a886cc5b1d704` (N by `git ls-remote`, 17:57Z; NO probe
battery — nothing left to interrogate):

- `docs/decisions.md:42` — **D-0005**: "A-2 schema-growth ledger (baseline = the 8
  s2.1 seed fields) + check_schema_growth … inside the manifest-validate gate."
- `docs/planning/schema-growth-ledger.yml` — the ledger ITSELF (1143 lines, read
  whole): `version: 1`; `baseline:` = exactly the 8 §2.1 seed fields
  (`SubsystemManifest.key/version/commands/panels/settings/stores/events/capabilities`,
  frozen pre-A-2 and exempt); live `entries:` rows each carrying `consumers:` (≥2 —
  the Q-0219 second-consumer rule), `rejected_alternative:`, and `minted:` — exactly
  the capture's "same-PR ledger entry naming the ≥2 consumers". The ledger is
  actively consumed at band pace: `PanelActionSpec.reply_visibility` (line 378) and
  `CommandSpec.reply_visibility` (line 854) were minted by the D-0071-era grammar
  growth.
- `tools/check_schema_growth.py` — the CI checker, read whole: diffs the registered
  grammar field set (`sb.spec.roles.snapshot_field_roles()` after importing every
  `sb.spec` module) against the ledger; reds on (a) a registered field with no
  baseline/entry row, (b) an entry with <2 `consumers` (Q-0219), and (c) stale
  ledger/baseline rows naming unregistered fields.
- Invocation sites READ, not grepped: `.github/workflows/named-gates.yml:62-63` —
  step "Schema-growth ledger (A-2)" runs `python3 tools/check_schema_growth.py`
  inside the `manifest-validate` named gate (§6 gate 2, per D-0034's gate map);
  `.github/workflows/ci.yml:54` — `check_schema_growth` in the committed
  19-checker fleet loop.

Every element of the capture — same-PR ledger entry, ≥2 named consumers, a CI
checker diffing grammar fields against the ledger — is live and wired at the
target. State flipped `captured` → `historical(built-at-target — D-0005 @
2f4b2c3)`; nothing remains to probe or route.
