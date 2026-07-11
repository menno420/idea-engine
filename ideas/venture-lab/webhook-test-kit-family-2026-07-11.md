# Webhook test-kit family — github + discord SKUs

> **State:** captured
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
