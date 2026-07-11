# Webhook test-kit family — github + discord SKUs

> **State:** parked(awaiting stripe-kit validation signal)
> **Class:** venture · **Target:** menno420/venture-lab
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/main/docs/roster.md@6d5e3b3 · fetched 2026-07-11T18:54Z
> **Shortlist rank:** 2 of 5 · sellables brainstorm 2026-07-11 · [batch](sellables-brainstorm-batch-2026-07-11.md)

## What it is

Extend the launch-ready stripe-webhook-test-kit into a product family: a github-webhook-test-kit and a discord-webhook-test-kit, built on the same harness pattern the stripe kit already proves — realistic event fixtures plus a signature-verification harness — with new fixtures per platform and each shipped as its own SKU. Everything stays Python stdlib, matching how the stripe kit is built. Sell channel: Gumroad / Lemon Squeezy at $9–19 each, or bundled with the existing stripe SKU on its pending listing.

## Why shortlisted

Cheapest marginal effort on the entire list: the harness pattern, the packaging shape, and the listing all exist — only the fixtures are new work. Just as importantly, it validates the multi-SKU listing motion (one listing, several related SKUs, bundle pricing) on a low-stakes product before any bigger bet depends on that motion working. If the family sells even a little, it proves the channel; if it doesn't, the loss is a few fixture files.

## Smallest shippable slice

The github-webhook-test-kit alone: fixtures for push, PR, and check-run events plus the signature-verification harness, added as one SKU to the existing listing. No new listing, no new account, no new owner click beyond the listing action already pending for the stripe kit.

## Honest effort / plausibility

The dev-tool niche is real but small — developers integrating webhooks do want trustworthy fixtures and a verification harness, but the audience is narrow and the price point low. Conservative expectation per Q-0259 r.4: single-digit sales per month. The honest framing is that this is a margin play on work already done, not a growth bet — its value is validating the multi-SKU motion at near-zero cost.

## Open questions

- Pricing: bundle (stripe + github + discord as one purchase) versus per-SKU at $9–19 each — which maximizes the tiny niche's willingness to pay?
- Does the stripe kit's harness actually generalize cleanly? Stripe's signature scheme differs from GitHub's HMAC and Discord's Ed25519 — the "same harness pattern" claim needs one verification pass before the family is promised anywhere.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/venture-lab/main/candidates/stripe-webhook-test-kit/swtk.py@389bb37 · fetched 2026-07-11T19:11Z

Verify-first pass (read-only worker, this session): venture-lab main HEAD pinned at `389bb37` via git transport (atom feed and api.github.com both proxy-403 for that repo); the harness `candidates/stripe-webhook-test-kit/swtk.py` (288 lines) and `stub_handler.py` (101 lines) read in full at that ref; Ed25519 stdlib absence checked empirically in this session's Python 3.11.15.

**1. What is this really?** A margin play on an already-built harness: port the stripe-webhook-test-kit (swtk.py, 288 lines, stdlib-only — imports at swtk.py:21–31 are argparse/hashlib/hmac/json/os/re/sys/time/urllib/pathlib) to new platforms as separate SKUs on the same pending listing. The base verifies: the stripe kit is BUILT, CI-green (14/14 on head `b5b99cd`), and non-author adversarially verified per lane `control/status.md`@389bb37 — but "launch-ready" is the lane's phrase, not INTAKE's, and the Gumroad listing is still owner-click-pending (⚑E QUEUED, `docs/launch/stripe-webhook-test-kit/publish-owner-action.md`@389bb37). Revenue to date: $0, zero distribution.

**2. What is the possibility space?** Family span × pricing. Span: the honest span is stripe+github only — the discord SKU as captured is FALSIFIED. Discord verification is Ed25519 (`X-Signature-Ed25519` over timestamp+body), and Python stdlib has no Ed25519 at all — verified empirically this session: `'ed25519' in hashlib.algorithms_available` → `False`, `import nacl` → `ModuleNotFoundError`; hmac/hashlib cover HMAC only, and it breaks on BOTH sides (harness must sign fixtures, handler must verify). The capture's "Everything stays Python stdlib" cannot hold for discord; every option is a compromise — third-party PyNaCl/cryptography (breaks the kit's "No account, no `pip install`" sell line, README.md@389bb37 + swtk.py:5), vendored pure-Python Ed25519 (crypto-hygiene and license risk), or drop the SKU. Pricing: per-SKU $9–19 vs bundle is ALREADY routed to sim-lab by the lane itself (status.md@389bb37 SIM-LAB routing block: price elasticity $19/$29/$39 + ~$79 all-three bundle economics) — not this file's question to duplicate.

**3. What is the most advanced capability reachable by the simplest implementation?** The github SKU. Stripe coupling in the harness is genuinely shallow: one 10-line signature function (`stripe_signature`, swtk.py:49–58, the `t={ts},v1={hex}` HMAC-SHA256 scheme) plus one hardcoded header name (`Stripe-Signature`, swtk.py:129). GitHub's scheme is `"sha256=" + HMAC-SHA256(secret, raw_body).hexdigest()` in `X-Hub-Signature-256` — swap the function, rename the header, drop the timestamp/tolerance logic (Stripe-only, swtk.py:42), add push/PR/check-run fixtures. The fire/forge verdict logic (swtk.py:137–145) and glob-based fixture loading (swtk.py:75–76) transfer unchanged. Fully stdlib — the capture's core cheapness claim VERIFIES for github.

**4. What breaks it?** In order of weight: (a) zero validation signal on the base SKU — the stripe kit has no listing, no article, no sale; the INTAKE kill-rule clocks (≥50 organic visits / ≥3 saves-stars / first paid sale within 14 days of the gotcha article going live, `candidates/stripe-webhook-test-kit/INTAKE.md`@389bb37) have not even STARTED because every distribution step is owner-gated. Building more unsold SKUs multiplies inventory, not evidence. (b) The discord leg's stdlib falsification (Q2) — a third of the captured family. (c) Budget precedent: the stripe kit ran ~284k tokens against its 120k intake cap (~2.3×, ledgered negative in status.md@389bb37), so "cheapest marginal effort" deserves suspicion. Also: any new SKU's sales signal has the same missing ingestion path already flagged at [revenue-ingestion-owner-relay-2026-07-10.md](revenue-ingestion-owner-relay-2026-07-10.md) (validation clocks with no evidence channel "fire on vibes").

**5. What does it unlock?** If any SKU sells, it validates the multi-SKU listing motion (one listing, several related SKUs, bundle pricing) at near-zero incremental cost — the capture's real value claim, and it survives the probe. The github fixtures also become reusable assets for any future CI/webhook-adjacent product, and the ported harness is the proof the pattern generalizes beyond one vendor.

**6. What does it depend on?** (1) The stripe-kit validation signal: the ⚑E owner publish click plus the free-article seeding that starts the INTAKE clocks; (2) venture-lab build capacity inside its token-budget discipline (Q4c); (3) an observable revenue path — the sales-CSV→ledger ingestion parked build-direct at revenue-ingestion-owner-relay-2026-07-10.md, without which even a sale is invisible to agents; (4) for discord ever: an explicit decision to relax the stdlib/no-pip product promise or vendor crypto — an owner-visible promise change, not a lane call.

**7. Which lane should build it?** venture-lab — it owns the harness, the candidates/ intake grammar, and the pending listing this family would attach to. No other lane plausibly touches it.

**8. What is the smallest shippable slice?** Exactly what the capture already names: the github SKU alone (push/PR/check-run fixtures + the Q3 HMAC swap), added to the existing listing with no new owner click — confirmed cheap and stdlib-clean. But it should not fire yet, and there is nothing left to route: the only open evidence questions (bundle vs per-SKU, elasticity) are already routed to sim-lab lane-side (Q2), and the build trigger needs no simulation — INTAKE's own kill-rule clocks define the signal. Rationale for the verdict: with $0 revenue and the validation clocks unstarted, the honest move is to hold the family until the stripe kit shows ANY observed INTAKE-clock signal (re-open then, scoped stripe+github; a ledgered negative kills the family instead), rather than invent a sim question the lane has not asked.

**Recommendation: park**
