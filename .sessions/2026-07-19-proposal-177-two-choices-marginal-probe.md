# PROPOSAL 177 — the second probe does all the work: one extra choice (d=1→d=2) collapses max dispatch load exponentially, every probe past the second buys only a vanishing constant (round-42 FLEET slot, P177 -> V190, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the outbox block + heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
round-42 FLEET-slot PROPOSAL 177 — power-of-two-choices second-probe-dominance head; stdlib firsthand verifier SEED=20260717, ≥3σ gates incl. a robustness gate under shifted load, targeting sim-lab VERDICT 190 (+13).

## Constraints honored
- Merge-on-green only; zero merge calls; PR opens READY.
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture; deterministic in-process double-run; cross-invocation identical.
- Grounding URL verified live this session (content-hash pinned).
- No model version identifiers in artifacts; family names only. Timestamps from date -u.

## Gate-plan (pre-registered, matches the shipped verifier)
- G1 — the second probe produces a real jump: z(maxload[d=1] − maxload[d=2]) ≥ 3, gap > 0.
- G2 — second-probe dominance (the head): second_gain=m1−m2, further_gain=m2−m4 (all probes past the 2nd combined); dom=second_gain−further_gain, require dom>0, z(dom) ≥ 3, ratio second_gain/further_gain ≥ 3.
- G3 — robustness under shifted load (m = n/2): dom, ratio recomputed in that regime; require dom>0, z(dom) ≥ 3, ratio ≥ 3.

## GROUNDING (verified at HEAD)
Power of two choices / balanced allocations (Azar–Broder–Karlin–Upfal; Mitzenmacher–Richa–Sitaraman survey): two random choices drop max load from Θ(log n/log log n) to Θ(log log n); further choices give only constant-factor gains. URL fetched live this session, content-hash pinned in the proposal doc.

## Probe questions
**1.** the second probe removes ~4× more max load than probes 3–4 combined; individual later gaps are integer-granular/non-monotone at finite n (see the proposal doc Probe report). **2.** not an artifact of load factor 1 — G3 reruns at m=n/2. **3.** ties→lowest-index is pessimistic, dominance holds anyway. **4.** max-load SE is small, gate clears 3σ widely. **5.** survives service departures (supermarket/JSQ(d) model). **6.** global least-loaded buys only a constant over d=2. **7.** stale reads shift constants not ordering. **8.** falsified if ratio<3 or d=2 fails to beat d=1 at 3σ.

## Outcome
Verifier + doc authored; gates G1/G2/G3 pass on two cross-invocation-identical runs; outbox appended sim-ready; proposal high-water P176→P177.

## ⟲ Previous-session review
P176 giant-component phase transition (round-42 UNRELATED, PR #668) landed at HEAD 8cfa363; offset +13 held (P176→V189).

## 💡 Session idea
Companion FLEET head: stale-load-read degradation of JSQ(d) — how much read staleness erases the two-choice advantage (a crossover flagged in this proposal's probe report).
