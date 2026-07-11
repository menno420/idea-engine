# Idle-economy Discord bot with premium themes

> **State:** captured
> **Class:** venture · **Target:** menno420/venture-lab
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/main/docs/roster.md@6d5e3b3 · fetched 2026-07-11T18:54Z
> **Shortlist rank:** 4 of 5 · sellables brainstorm 2026-07-11 · [batch](sellables-brainstorm-batch-2026-07-11.md)

## What it is

Host superbot's idle-economy game as a public Discord bot and monetize cosmetics: the economy is sim-pinned (V006), the mining/encounter parameters are sim-validated (V001/V008), and the existing 12-pack theme catalog becomes the premium tier. Free players get the game and a couple of themes; premium unlocks the rest of the catalog. Sell channel: Discord's native premium-app subscriptions, with Ko-fi perks as the fallback if app-subscription access stalls.

## Why shortlisted

It is the only candidate on the list with a recurring-revenue shape — everything else is one-time sales or donations. And the content risk is unusually low for a game product: the economy balance is sim-validated rather than guessed, and the theme catalog — the actual thing being sold — is already designed as a 12-pack. The two hardest parts of a cosmetic-monetized game (a balanced core loop and a sellable cosmetic inventory) already exist; what remains is hosting and productization.

## Smallest shippable slice

The existing bot running in ONE public community server, with 2 free + 2 premium themes wired end-to-end. That slice exercises the whole revenue loop — play, want, subscribe, unlock — at the smallest possible operational footprint, and its retention/conversion numbers decide whether wider rollout is worth the drag.

## Honest effort / plausibility

The honest caveat leads: this is the only candidate that takes on an always-on hosting commitment and a moderation commitment — a public game bot in a community server is an operational responsibility, not a shipped artifact — plus Discord's app-review overhead before premium subscriptions can even be offered. It has the highest ceiling in the games track and the highest operational drag on the entire list; both facts must be priced in per Q-0259 r.4 before any owner click. Owner clicks required: hosting account, Discord app verification, payout setup.

## Open questions

- Hosting cost ceiling: what monthly spend is acceptable before a single conversion exists?
- Discord app-review timeline: how long from submission to sellable premium tier, and what does review require of the bot?
- Who moderates? A public game server generates moderation load the fleet cannot absorb unattended — the answer gates the public launch, not just the revenue.
