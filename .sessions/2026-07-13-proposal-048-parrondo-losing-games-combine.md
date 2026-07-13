# Session — PROPOSAL 048: Parrondo's paradox — do two losing games combine into a winner? (COMPLETELY-UNRELATED slot, round 8 closer)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-13T21:49:43Z (Ideas Lab worker slice — draft the
> round-8 COMPLETELY-UNRELATED-domain head under standing owner ORDER 003. Card born
> in-progress as the designed born-red gate hold; flipped complete in this PR's final
> commit at 2026-07-13T21:56:52Z)

## Scope

Draft a genuinely new sim-shaped idea for the COMPLETELY-UNRELATED-domain rotation slot,
round 8, under standing owner ORDER 003 (continuous pipeline) and ORDER 004 rule 3's
rotation ("fleet backlogs → venture's book/product space → game mechanics → COMPLETELY
UNRELATED domains"). Round 8 opened at fleet backlogs with P045 (#343), served venture
with P046 (#348), and game mechanics with P047 (#352), so the UNRELATED slot closes the
round. The domain is an EIGHTH fleet-external one — stochastic-ratchet / capital-dependent
game switching (Parrondo's paradox) — distinct from the seven prior unrelated occupants
(P017 social choice, P024 congestion routing, P028 tournament seeding, P032 pattern races,
P036 optimal stopping, P040 spatial self-organization, P044 queue-discipline). Claim landed
first (`control/claims/claude-proposal-048-parrondo-losing-games-combine.md`).

Idea file `ideas/fleet/parrondo-losing-games-combine-2026-07-13.md` (probed single-pass
this slice, sim-ready), fleet README index row, then appended to `control/outbox.md` as
PROPOSAL 048. Seeds 20261329–332, strictly above the P047 high-water 20261328 (re-swept
this session: digit-boundary regex + range-notation companion + `results.json` exclusion
over this tree AND /home/user/sim-lab; the only ≥20261329 numeric hits in either repo are
digit substrings inside sim-lab `results.json` exact-Fraction numerators — the P046 💡
sweep-recipe trap, re-confirmed live — not allocations; the true cross-repo high-water is
P047's 20261328).

**📊 Model:** `fable-5` (family-level self-report per ORDER 001 / Q-0262 — the family the
harness reports for this Ideas Lab slice, never copied from a schedule surface) · content +
outbox proposal only (idea file, card, fleet section index row, claim file, outbox append;
no product code, no control/status.md or control/inbox.md writes; no sim-lab writes — the
V058 verdict session runs parallel there and its claim
`control/claims/claude-verdict-058-creature-rarity.md` is untouched).

## 💡 Session idea

**When the DECISION arm is an EXACT closed form, the pipeline's liveness-disclosure norm
INVERTS: you must disclose the COMPUTED expected landing, not pin "no expected landing" —
because withholding a value you can and did compute is the dishonest move, the opposite of
what the norm protects against.** Every prior COMPLETELY-UNRELATED head (P017/P024/P028/
P032/P036/P040/P044) correctly pins "NO expected landing" — right for a Monte-Carlo decision
arm, where the outcome is genuinely unknown until the seeds run and pinning a guess would be
anchoring. But P048's decision arm is a finite exact-rational Markov-chain solve: the drafter
can compute `D_mix` and DID (`26673/4429850`, in the probe), so "no landing pinned" would be
a fiction. The honest branch on arm type: (a) STOCHASTIC decision arm → disclose the bands +
reachability, pin NO landing (unknown-until-run); (b) EXACT/closed-form decision arm →
disclose the bands + the COMPUTED landing + reframe the sim's value as three concrete jobs it
still does — an INDEPENDENT re-derivation guarding the drafter's arithmetic, an MC cross-check
that the discrete process matches the closed form, and a robustness-boundary sweep (here the
critical-`EPS` locator) that no single-point computation gives. Falsifiability survives the
disclosure because the pre-registered REJECT-first rule fires at nearby pins; what dies is the
pretense of suspense. Dedup (this slice, at HEAD `b56d802`): P046's 💡 is the seed-sweep
RECIPE, P047's 💡 is harvest-by-validation-gap, P045's is harvest-by-hedge-marker, P035's is
the seed registry — none touches liveness-disclosure norms; this is the first 💡 to split the
"no expected landing" convention by decision-arm type, and it is load-bearing precisely
because closed-form-decidable heads (exact enumeration, rational solves) are becoming common
in the unrelated slot.

## ⟲ Previous-session review

Newest predecessor card (`.sessions/2026-07-13-proposal-047-creature-rarity-counter.md`,
worker slice ~21:30Z, fable-5): closed clean, and its rituals transferred verbatim here — the
blob-pinned `idea:` link (P048's outbox append pins the `09dadfb` idea-doc commit) and the
P046 seed-sweep recipe, which this slice ran a THIRD consecutive time and which again earned
its keep: the digit-boundary + range-notation + `results.json`-exclusion pass produced the
true 20261328 high-water cleanly while the naive numeric sweep surfaced exactly the predicted
`results.json` numerator aliases (20261542/20261664/20261833 in idea-engine, 202659xx–202698xx
in sim-lab) — three-for-three reuse, the recipe is now load-bearing infrastructure, not a
one-off. Its honest nit also held: P047 flagged that TWO claim-landing patterns coexist (P046's
fast-lane control-only PR #346 vs P047's claim-in-first-commit) with no doc naming when each
applies; this slice took the claim-in-first-commit pattern per its orders, so the ambiguity is
now three cards deep and still undocumented (decide-and-flag: noted for the manager sweep, not
expanded into this diff). Its ASK-004 escalation kept aging on schedule: `control/outbox.md`
crossed ~404 KB before this append and every read here was shell-sliced — ASK 004 remains the
right fix and remains unserved.

## Close-out

All pieces landed before this flip: claim + born-red card @ `c943d37` (branch's first commit,
PR #353 opened READY immediately after the push — never draft; merge left to the enabler
workflow, no agent merge), idea doc + fleet section index row @ `09dadfb`, PROPOSAL 048 outbox
append @ `80a61cc` (idea: link pinned to the `09dadfb` blob; `scripts/check_ideas.py --outbox`
exit 0 verified after the append). Rotation verified at HEAD before drafting: round 8 opened at
fleet backlogs with P045 (#343), venture P046 (#348), game mechanics P047 (#352), COMPLETELY-
UNRELATED next and last per ORDER 004 rule 3 (quoted verbatim in the claim). Domain deduped as
an EIGHTH fleet-external one against all seven prior unrelated occupants and PROPOSALs 001–047;
nearest priors (P032 pattern races, P024 Braess) disclosed with their distinguishing mechanism.
Seeds 20261329–332 strictly above the true cross-repo high-water 20261328. This flip is the
branch's last commit; both checkers (`python3 bootstrap.py check --strict`, `python3
scripts/check_ideas.py --outbox`) run green at flip time or this commit does not push.
