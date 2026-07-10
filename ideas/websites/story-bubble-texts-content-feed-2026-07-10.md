# Story bubble-texts as a committed content feed — owner voice grows without a code session

> **State:** captured
> **Class:** product · **Target:** `menno420/websites`
> **Grounding:** https://raw.githubusercontent.com/menno420/idea-engine/698fd93869f8a05200f26fde45bbd71596323e6a/ideas/websites/superbot-site-stats-data-story-2026-07-10.md@698fd93 · fetched 2026-07-10T22:08Z
> **Grounding:** https://github.com/menno420/websites@0cd08d2da1580fffff1595a6f4119b6d98a8b4b3 · fetched 2026-07-10T22:08Z (manifest row: behind)
> *(pin annotation: lane HEAD via `git ls-remote`; the manifest websites row @ superbot `9624c53` still records close-out #58/`d493792` 13:57Z + kit v1.6.0 while the lane heartbeat @ `0cd08d2` reads #75 @ 21:58Z + kit v1.7.1 — staleness datapoint #8, relayed on the heartbeat)*

## Problem

The one part of the story page (PROPOSAL 002 phase 1) that agents cannot
generate is the part the owner asked for by name: "bubble texts etc., to really
bring the reader into the story" (idea §1) — the voice-of-the-owner /
voice-of-the-agent asides (§2). Hardcode that narrative in page templates and
every new owner aside costs a websites code session; the owner is the program's
scarcest resource, and the probe's Q4 already flags scrollytelling as "an
unbounded design sink" — content/code coupling is half of that sink. The
original idea itself reached this repo as a chat aside relayed by the dispatch
copilot; the story's future asides will arrive exactly the same way.

## Idea

Separate the narrative from the page: one committed content file (small
schema — chapter texts, bubble asides with a `speaker: owner|agent` attribution
and an anchor to a scroll position or graph moment) that the story page renders.
A new owner aside is then a one-line content commit — landable by ANY session or
relayed straight from owner chat by the copilot, no template work, no design
decisions reopened. This is not a new pattern for the lane, it is its own
doctrine applied to prose: committed generated/authored artifacts, rendered
live, "never fake data" (`dashboard/data_source.py`), honest empty states when a
chapter has no asides yet. The story page becomes append-cheap for the two
voices that matter while its code stays frozen.

**Why now:** cheapest decided before the story skeleton (the probe's smallest
shippable slice, routable now) hardcodes its first chapter — and the lane's
proven 4-hourly wake + continuous send_later chain means content commits get
picked up and deployed with no human in the render loop.
