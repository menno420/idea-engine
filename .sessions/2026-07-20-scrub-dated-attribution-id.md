# Scrub dated build-ID from session-card attribution field — normalize to sanctioned neutral form

> **Status:** `complete`
> 📊 Model: withheld per coordinator directive · effort standard · task-class compliance-remediation

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the edits land and the gate is green.

## Objective
Normalize the session-card attribution field to the sanctioned neutral form across a small set of dated entries. A few earlier cards recorded a full dated build identifier in the `📊 Model:` field; the card doctrine (`.sessions/README.md` — family-level names only, never a full dated ID) mandates a family-level or neutral value. This slice replaces the offending dated substring with the neutral placeholder `agent`, matching the surrounding grammar, in three pushed files.

## Six-field
- **WHAT** — Replace the dated build-ID substring in the attribution field with the neutral `agent` placeholder across three entries.
- **WHERE** — `.sessions/2026-07-17-friendship-paradox-sensor.md` (2), `.sessions/2026-07-17-verdict-109-mirror.md` (2), `ideas/fleet/friendship-paradox-sensor-2026-07-17.md` (1).
- **HOW** — Exact-substring text substitution; the rest of each attribution line (` · effort … · task-class …`) is left untouched.
- **WHY** — Brings the attribution field into compliance with the family-level-only rule; the dated build ID is disallowed there.
- **UNBLOCKS** — Clean attribution-field audit; no further remediation of these entries needed.
- **VERIFY** — `python3 bootstrap.py check --strict` green; ripgrep of the dated substring returns zero hits in the three target files (control/ evidence quotes are intentionally out of scope).

## Constraints honored
- Compliant family-level names elsewhere (the mandated attribution field values) are left untouched — only the dated build ID is scrubbed.
- `control/status.md` and `control/inbox.md` are not touched; the inbox may retain the token as quoted evidence.
- Neutral heartbeat; no cross-seat inbox edits.

## ⟲ Previous-session review
The prior slices authored the friendship-paradox-sensor entries and the VERDICT 109 mirror, which is where the dated attribution-field values were introduced. This session closes that compliance gap without altering any of those slices' substantive content — only the attribution field's disallowed dated form is normalized to the sanctioned neutral placeholder.

## 💡 Session idea
The attribution field wants a family-level or neutral value by rule; a lightweight pre-push guard that flags a dated build-ID pattern in the `📊 Model:` line would catch this class of drift at authoring time rather than in a later remediation pass — a cheap grep-shaped check anchored on the attribution line.

📊 Model: withheld per coordinator directive · effort standard · task-class compliance-remediation
