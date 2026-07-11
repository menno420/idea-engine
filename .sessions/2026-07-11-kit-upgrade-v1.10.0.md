# Session — fleet slice: substrate-kit self-upgrade v1.9.0 → v1.10.0

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-11 ~07:15Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

Move the vendored kit v1.9.0 → v1.10.0 (released upstream the same day as v1.9.0 —
the exact hop the #120 card's handoff named ripest) and COLLECT the three items the
v1.9.0 slice deferred to this hop: (a) `upgrade --apply-docs` for `.claude/CLAUDE.md`
(v1.9.0's apply-docs dropped the report carve-out section — fixed in v1.10.0),
(b) the `.sessions/README.md` model-attribution doctrine append (v1.9.0 only planted
it into FRESH READMEs — v1.10.0's upgrade appends retroactively), (c) the enabler
re-apply tripwire from the #120 card's 💡 (the carve-out scan is step-granular and
blind to the in-step `--body` edit — manual diff was the only catch). Standing
re-apply duty on BOTH kit-owned workflows as on every hop.

(Body written at close-out — born-red per the first-commit convention.)
