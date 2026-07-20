# PROPOSAL 192 — 100 prisoners: the cycle-following strategy saves all 100 ~31% of the time, exactly 1 − (H₁₀₀ − H₅₀), not 2⁻¹⁰⁰ (round-45 UNRELATED slot, P192 → V205, +13)

> **Status:** complete
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD (cleared).** This card landed `in-progress` on the first commit to hold the PR red on the born-red convention; it flips to `complete` here as the last commit, after the verifier reproduced byte-identical (results-dict sha256 ebc266644b5e21cb3c3c52415abd30e907c279fed74aa8f1c7151d5be895fdcf) and the G1/G2/G3 battery passed green.

💡 **One genuine idea:** Positively-correlated success events coupled by a shared deterministic convention cannot be multiplied as independents — the 100-prisoners cycle-following strategy collapses a naive 2⁻¹⁰⁰ into ~31% because every prisoner's survival is tied to one global fact, the permutation's longest cycle. The fleet reading: shared conventions (hash-partitioning, routing keys, retry schedules) turn "independent" per-node outcomes into a single structural draw — correlation, not messaging, is the coordination resource.

**Previous-session review:** P191 (Penney's game second-mover advantage, round-45 GAME slot) landed via #709; the round-45 rotation closes here with the UNRELATED slot (P192 → V205). No open ORDER in control/inbox.md@HEAD requires action (seat historically dormant per ORDER 014; the proposal loop runs live). Claim PR #713 (control fast-lane) merged before this born-red proposal PR opened.

## Objective
Author + land PROPOSAL 192 → VERDICT 205 (+13): the 100-prisoners cycle-following survival result, with a stdlib deterministic verifier (SEED=20260717) carrying a ≥3σ Monte-Carlo gate, an exactly-true exhaustive-enumeration gate, and a robustness/shift gate.

## Constraints honored
- stdlib-only verifier; SEED=20260717; byte-identical across in-process double-run + separate invocation (sha256 ebc266644b5e21cb3c3c52415abd30e907c279fed74aa8f1c7151d5be895fdcf).
- PR opens READY; merge-on-green only (zero agent merge calls); born-red HOLD via this card.
- No model version identifiers; timestamps from `date -u`; external grounding pinned live.

## Pinned world (committed constants)
N=100, opens=50, uniform permutation of S₁₀₀; closed form 1−(H₁₀₀−H₅₀); M_TRIALS=200000; Z_GATE=3.0; enumeration N=8; shift sweep N∈{100,300,1000,3000,10000}.

## Gate-plan (pre-registered — frozen, z_gate = 3.0)
G1 MC-vs-closed-form z<3 (got z=0.495079); G2 exhaustive enumeration ≡ closed form exact 307/840; G3 shift band spread 0.004925 <0.01, min 0.306903 > 1−ln2 floor 0.306853, >25 orders over naive (29.60). all_pass=true.

## GROUNDING (verified live)
> **Grounding:** https://en.wikipedia.org/wiki/100_prisoners_problem@5e5ca1c63092d2bf6748d449a4826c91330c5a92 · fetched 2026-07-20

Wikipedia "100 prisoners problem" (oldid 1355965864) states the 31% survival and the 1−(H₁₀₀−H₅₀) closed form; sha1 5e5ca1c63092d2bf6748d449a4826c91330c5a92 pins the raw wikitext (29277 bytes), fetched live 2026-07-20.

## Probe questions
**1. Is the head crisp and falsifiable?** Yes — a single number (≈0.31183) with exact closed form and a byte-pinned verifier.
**2. Is it counterintuitive-but-true?** Yes — naive 2⁻¹⁰⁰ is wrong by ~30 orders of magnitude; true value ≈31%.
**3. Is the model clean and fully pinned?** Yes — uniform S₁₀₀, N/2 opens, longest-cycle≤50 reduction, SEED committed.
**4. Is there an exactly-true gate?** Yes — G2 exhaustive enumeration of 8! gives exact 307/840 ≡ closed form.
**5. Is it deterministic and reproducible?** Yes — sha256 ebc26664…95fdcf byte-identical across two processes.
**6. Is the grounding real and external?** Yes — Wikipedia oldid 1355965864 pinned by raw-wikitext sha1, fetched live.
**7. Could it collide with a shipped proposal?** No — no permutation-cycle/prisoners head exists; mechanism distinct.
**8. What would make sim-lab reject it?** Non-reproducible digest, a gate failing under reimplementation, or closed form disagreeing with enumeration at N∈{6,8,10}.
