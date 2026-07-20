# VERDICT 245 — coprime density = 6/π² (independent adjudication of PROPOSAL 232)

> **Status:** `complete`

- **📊 Model:** Opus 4.8 · high · verdict-adjudication

## Slice
Independent adjudication of idea-engine PROPOSAL 232 — the probability that two integers drawn iid uniform on {1,…,N} are coprime is the exact Möbius-inversion density Q(N)=(1/N²)·Σμ(k)⌊N/k⌋² → 6/π² = 1/ζ(2), NOT the naive parity-only 3/4. Ruling → VERDICT 245 (+13 offset), appended to control/outbox.md; heartbeat + high-water in control/status.md.

## Trail
- Byte-identical verifier re-verified vs the sim-lab #328 pre-verdict mirror (diff exit 0).
- results_sha256 754580…840fec reproduced firsthand — two separate process runs (grep -F exit 0 each, full-stdout diff exit 0) + in-process double-run guard IDENTICAL.
- Four gates each evaluated in its own direction — all PASS (G1 Q(6)=23/36; G2 z=+0.774312; G3 partition invariant exact; G4 z_naive=−145.835897).
- Independent quoted-vs-derived grep of pinned Wikipedia oldid 1363371102 (raw wikitext 17251 bytes, sha1 254a5e69…8c4947c) — split accurate, no mislabeling seam.
- Ruling: APPROVE.

## ⟲ Previous-session review

Previous-session review: VERDICT 243 (Chatterjee–Samuelson k=1/2 bilateral double auction — the Myerson–Satterthwaite inefficiency made concrete; P230 → V243) landed APPROVE. It reproduced the committed verifier byte-identical, matched the full-64 results_sha256 verbatim three ways in agreement, passed all four gates each in its own direction, and found the quoted-vs-derived grounding boundary HONEST with no defect — a sound, clean-boundary adjudication. V245 carries its GATE-POLARITY discipline (read each gate in its own direction — exact identities self-certify, Monte-Carlo z-tests are AGREEMENT gates against the closed-form null, the deliberately-wrong model is a FALSIFIABILITY gate at opposite polarity) and its QUOTED-vs-DERIVED grounding discipline (grep the pinned revision firsthand in BOTH directions before trusting any label) into this coprime-density ruling.

## 💡 Session idea

💡 Session idea: a verdict's grounding integrity is only as strong as an independent re-grep of the pinned revision in BOTH directions — quoted values must be present on the page AND derived values must be absent from it — because pre-clearing the split from the proposal's own self-report is the recurring seam that qualified V235/V238/V242. V245 re-grepped both ways firsthand against Wikipedia oldid 1363371102 (raw wikitext 17251 bytes, sha1 254a5e69…8c4947c) and found the split clean, which is exactly why this ruling is APPROVE and not QUALIFIED — the honest disposition is decided by the firsthand both-directions grep, never by trusting the label the proposal supplied.

## Status
> **Status:** `complete`
