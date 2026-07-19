# VERDICT 162 mirror — coordinated omission: closed-loop latency measurement is blind to the tail it is meant to catch (P149 → V162, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · review/verify

Born-red HOLD: this card is the mirror slice's FIRST commit, born `in-progress` to hold the `substrate-gate` RED so the PR cannot merge before the deliberate `complete` flip. Flipping to `complete` (the deliberate LAST commit, after the outbox VERDICT 162 block + heartbeat) releases the merge-on-green enabler. A red gate AFTER the flip is a real defect, not the HOLD.

## Objective
Mirror round-35 FLEET-slot VERDICT 162 (coordinated omission, P149 → V162, +13) into idea-engine: append the VERDICT 162 outbox block (fan-in to the fleet-manager, Q-0264), overwrite the control/status.md heartbeat (proposal high-water STAYS P149; verdict high-water ADVANCES V161 → V162, union-max, no regress; routines line UNCHANGED coordinator-bound; baton "next: round-35 venture-slot P150 → V163"), and flip this born-red card complete LAST. The PRIMARY reproduction + ruling landed in sim-lab (PR #236, MERGED) — this slice records it on the idea-engine bus; no verifier is re-run here beyond the sim-lab reproduction cited.

## Constraints honored
- Offset +13 (P149 → V162), cited verbatim from the P149 depends-ledger + control/status.md; docs/current-state.md is a dormant snapshot (through V059), not the authority.
- Ruling = clean APPROVE, judged on evidence (not assumed): sim-lab reproduced the committed verifier byte-for-byte (diff exit 0) under SEED=20260717, digest 12d3ce4f…dbfab5d reproduced EXACT, all three /se gates PASS in order, exit 0 — and the declared model choices are conservative-direction only (none flips a gate sign or the order-of-magnitude), unlike the V159 QUALIFIED whose G2 sign was regime-dependent.
- Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (P105…P149 family), P127+ compact-canonical twist (stdout dump pretty indent=2, hashed payload compact, floats 6 dp, no on-disk JSON).
- Outbox block appended once (append-only, deduped) matching the V158…V161 mirror skeleton (source / idea / ruling / G1-G3 / cross-check / sim / digests / offset / loop); `date -u` timestamp.
- Heartbeat overwritten LAST-before-flip; all field keys preserved; routines / orders / needs-owner / kit / blockers lines verbatim.
- Born-red first commit (card in-progress) → outbox block → heartbeat → flip complete LAST; enabler lands on green (idea-engine merge-on-green; arm-race backstop known).

## GROUNDING (verified at HEAD)
- sim-lab PRIMARY reproduction: sim-lab PR #236 (https://github.com/menno420/sim-lab/pull/236) MERGED, sim-lab main HEAD efa9d3f38e988f9406212f15ec8176dfad5cf34f — sims/verdict-162-coordinated-omission/ (byte-identical verifier + run-stdout + probe-report) + .sessions/2026-07-19-verdict-162-coordinated-omission.md.
- Verifier (firsthand): idea-engine ideas/fleet/coordinated_omission.py at d615489 (PROPOSAL 149, landed via idea-engine PR #602) — git blob d276fb5047473a5bc569f8747c1dd7a04311bbc5, file sha256 6780d06a213ad27d218331447bb922898a1eb8aa716396bf343590c16eda762c, 323 lines / 12310 bytes. Permalink: https://github.com/menno420/idea-engine/blob/d615489/ideas/fleet/coordinated_omission.py
- Disclosed == reproduced results-dict sha256 12d3ce4fce9a4f1cc218be0ee6f5dbc945d42a5e45173a46044704524dbfab5d (EXACT, all 64 hex).
- External reference (reachable): coordinated omission — Gil Tene (HdrHistogram), "How NOT to Measure Latency"; CO-correction = recordValueWithExpectedInterval.
- Claim 2026-07-19-verdict-162-coordinated-omission.md on main @c90cb11 (idea-engine PR #603, MERGED, control fast-lane).

## Probe questions
**1.** Does the outbox VERDICT 162 block cite the reproduced == disclosed digest (12d3ce4f…dbfab5d) and the sim-lab PR #236 @efa9d3f merge, with the +13 offset quoted verbatim from the P149 depends-ledger?
**2.** Does the heartbeat ADVANCE the verdict high-water V161 → V162 (union-max, no regress) while keeping proposal high-water P149, and leave the routines line UNCHANGED (coordinator-bound)?
**3.** Is the ruling a defensible CLEAN APPROVE — the three declared model choices conservative-direction only, none flipping a gate SIGN or the order-of-magnitude, distinct from the V159 QUALIFIED?
**4.** Is the non-contiguity honored — V162 advances the high-water above the round-34 quad (V158–V161) but V137/P124, V132/P119, V126/P113 remain open below?