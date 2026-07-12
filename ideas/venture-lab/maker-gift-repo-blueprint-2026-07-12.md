# Maker gift repo — a Claude+GitHub workshop-in-a-box for a maker friend

> **State:** captured
> **Class:** venture · **Target:** menno420/venture-lab
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/main/docs/roster.md@54a9588 · fetched 2026-07-12T17:37Z
> **Sequence:** before the owner creates and seeds the gift repo — the routed build slices in § Delivery plan consume this blueprint

## What it is

Owner request (2026-07-12): create a GitHub repo as a **gift for a friend** who has
two 3D printers (one small, one 3-color/multi-material) plus a robot arm — a
generic 6DOF/6-servo kit (Amazon.nl, no controller included): six 180° hobby
servos and a gripper claw, driven by the friend's own Arduino — and does general
Arduino tinkering. The repo ships **pre-seeded** — substrate-kit
machinery (cut down, see the cut list), a starter idea backlog, and several
already-finished projects — so the friend can discover Claude+GitHub workflows with
**his own Claude account**, on day one, having never used Claude-with-a-repo before.
Revenue is zero by design: the "venture" is a relationship-and-adoption play, and it
doubles as the fleet's first *single-human* adopter datapoint for the kit.

**Dedup relation (explicit):** this blueprint is the **PERSONAL-GIFT instance** of
the idea family whose commercial head is
[`substrate-kit-agent-fleet-starter-2026-07-11.md`](substrate-kit-agent-fleet-starter-2026-07-11.md)
(state `parked(owner-gated)` behind the kit's public-readiness gates) — **not** the
commercial starter, and **neither supersedes the other**. The commercial head waits
on a settled public name, license confirm, public flip, and sponsor tiering; this
gift instance needs none of those gates: the repo is private, the kit rides in as a
vendored `bootstrap.py` file (MIT; the kit's LICENSE is **copied into the gift repo
alongside it** at seed time — upstream-only is not enough for a vendored copy, see
§1 layout + §5), nothing is marketed, nothing is sold. The gift also *feeds* the commercial
head: a real outside-the-fleet human running the kit solo is exactly the adopter
evidence the starter-kit pitch currently lacks.

**Companion dossier:** a sibling session is writing
[`maker-ecosystem-research-2026-07-12.md`](maker-ecosystem-research-2026-07-12.md)
in parallel (maker-ecosystem tooling research — slicers, OpenSCAD/build123d,
arduino-cli, Spoolman, arm-control landscape). This blueprint names its own tool
choices with rationale but defers depth to that dossier; where the dossier's
findings contradict a tool pick below, the dossier wins at build time. Not yet on
main at this capture's write time — do not treat a red link as drift.

## 1 · Repo skeleton

**Name candidates** (fun, gift-appropriate, no kit-placeholder entanglement):

1. **`makerbench`** — RECOMMENDED: plain, describes the thing, ages well, reads
   fine in a résumé-visible repo list.
2. `filament-and-firmware` — charming, names both hobbies, slightly long to type.
3. `tinkerforge-garage` — warm, but "tinkerforge" collides with an existing
   hardware brand; keep only if the friend would enjoy that.
4. `three-axes-and-an-arm` — the in-joke option (two printers + arm).

**Top-level layout:**

```
makerbench/
  README.md            # the gift letter: what this is, day-one steps, the map
  CLAUDE.md            # working agreement, beginner edition (§2 outline)
  bootstrap.py         # substrate-kit dist, vendored at a TAGGED release
  LICENSE-substrate-kit  # the kit's MIT license, copied verbatim from the pinned release (notice-retention)
  docs/
    idea-ritual.md     # the one-page 8-question probe, maker edition (§5)
    git-for-makers.md  # branch/PR/merge/CI in bench terms (§2)
    safety.md          # the hard rules, standalone + linked from CLAUDE.md
    capabilities.md    # what Claude can/cannot do here (adapted, §5)
  printing/
    models/            # parametric sources (OpenSCAD / build123d)
    presets/           # per-printer profiles: small/, color3/ (multi-material)
    calibration/       # temp-tower + flow generators (project d)
  arduino/             # sketches, one folder per gadget
  arm/                 # calibration config + control starter + routines (project c)
  projects/            # finished starter projects' docs + tutorials
  ideas/               # the backlog: one file per idea head (§4 seeds it)
  .sessions/           # simplified session cards (§5)
  .github/workflows/   # gate + adapted auto-merge enabler + render/compile CI
  .devcontainer/       # devcontainer.json pinning OpenSCAD + arduino-cli + Python deps — day-3+ toolchain as a browser Codespace, no install festival (https://containers.dev/)
  scripts/             # the 3 lightweight checks (§5) + preflight wrapper
```

**Which substrate-kit pieces to seed, and which to OMIT.** Position taken and
defended: **a solo human+Claude repo wants the kit's checks and session-card
ritual, but NOT the fleet coordination machinery.** The kit at HEAD is v1.15.0
(substrate-kit `pyproject.toml`@0801be9; CHANGELOG.md@0801be9 dates both v1.14.0
and v1.15.0 to 2026-07-12 — note the recon expectation was ~v1.14.0, which is what
the *lanes* run per fleet-manager `docs/roster.md`@54a9588; kit HEAD is one ahead).
Seed the newest **tagged release** at build time, never HEAD — the pinning rule the
commercial head's grooming pass established (that file, gap 5: the kit ships
roughly a release a day; a gift must not track a moving target). What `adopt`
plants (kit README.md@0801be9): CONSTITUTION.md, binding-doc skeletons, living
ledgers, orientation router, `.sessions/` scaffolding, and staged `.claude/`
material under `.substrate/` — installed deliberately, never imposed.

SEED (keep, item by item):

- **`bootstrap.py check --strict` + the CI gate** — the checks are what keep a
  beginner's repo from silently rotting (broken links, half-written cards); they
  are also the friend's first "CI caught my mistake" moment, which is a teaching
  payoff, not overhead.
- **Session cards, simplified** (§5) — solo use still wants "what did Claude do
  last session" as a durable surface; it is the memory that makes week 2 better
  than week 1. Simplified to three fields (§5) — the fleet's four mandatory
  byte-form markers (`.sessions/README.md`@949fc0b) include model-attribution
  ORDER machinery a gift does not need.
- **Guided mode + the interview** — the kit's staged question flow (kit
  README.md@0801be9: observe/guided/active) IS the friend's tutorial: each
  question it asks him is one concept learned. Guided, not active — one practice
  at a time matches a total beginner.
- **The auto-merge enabler, adapted** (§5) — merge-on-green is the magic-moment
  demo of the whole gift ("my PR merged itself when the tests passed").
- **CLAUDE.md + docs skeletons, rendered** — but rewritten in plain maker language
  per the §2 outline, not the fleet's doctrine register.

OMIT (cut, item by item, each justified):

- **NO `control/` plane at all — no inbox, no outbox, no status heartbeat.** The
  inbox exists so a *manager* can write orders into a lane (idea-engine
  README.md@949fc0b § Coordination); the friend has no manager. The outbox exists
  to route proposals to a *sim-lab*; there is none. The heartbeat exists so a
  *coordinator and sweep* can read lane state; the only reader here is the friend,
  and the repo README serves him better. Every control surface would be a file he
  is told to maintain for a reader who never comes.
- **NO claims ledger (`control/claims/`).** Claims exist because parallel agent
  sessions collide (measured ~98% conflict rate on shared-append at concurrency,
  `control/claims/README.md`@949fc0b); a one-human, one-Claude repo has
  concurrency 1. The mechanism's entire justification evaporates.
- **NO fleet manifest / roster sync (`check_sections.py` class).** Sections
  partition a tree across parallel workers against a lane registry; there is no
  registry and no partition. Folders here are just folders.
- **NO harvest checker (`check_harvest.py` class).** It diffs link-indexes against
  canonical *other repos*; the gift repo has no canonical siblings.
- **NO outbox grammar / proposal lint (`check_ideas.py --outbox` leg).** Nothing
  to propose to nobody.
- **NO panel-mode probe machinery.** Single-pass questions only — panel mode is
  an escalation for contested fleet verdicts (README.md@949fc0b § probe battery);
  a hobbyist deciding whether to print a bracket does not convene a panel.
- **NO born-red HOLD ceremony.** The born-red card gate exists so parallel
  sessions and auto-merge don't race a multi-commit close-out
  (auto-merge-enabler.yml@949fc0b, the PR #80/#81 race comments). Solo, the
  simplified card (§5) plus merge-on-green is enough; the ceremony would be the
  single most confusing thing a newcomer hits in week 1.

## 2 · CLAUDE.md working agreement — outline (beginner maker edition)

Draft outline for the gift repo's CLAUDE.md; plain language throughout, guided
mode, every rule shown with a worked example rather than doctrine prose.

1. **What this repo is** — "Your workshop notebook that answers back. Claude reads
   this file first every time; it's the standing instructions you've given it."
2. **How to ask for things — worked examples, literally paste-able.** E.g. "how to
   ask for a bracket":
   > *Design a bracket that mounts an Arduino Uno flat against a 2020 aluminium
   > extrusion. Uno hole pattern 66.0 × 15.2 mm (the standard Uno layout), bracket
   > body 4 mm thick, M3 clearance holes (3.4 mm) for the Uno, two M5 slots for
   > extrusion T-nuts. Write it as OpenSCAD in `printing/models/uno-rail-bracket.scad`
   > with the dimensions as named parameters at the top, and tell me which side
   > faces the print bed.*
   Plus two more worked prompts: "ask for a fix" (paste the compiler error +
   sketch path) and "ask for an idea probe" (point at an `ideas/` file, ask for
   the ritual in `docs/idea-ritual.md`).
3. **SAFETY — hard rules, not suggestions.**
   - Claude designs; **the human slices and starts every print**. Claude never
     auto-prints, never generates or sends G-code to a printer, never marks a
     model "safe to print unattended".
   - The robot arm moves **only inside the soft envelope** defined by
     `arm/calibration.json`, only via routines that clamp to it, and **only with
     the human watching**. No motion code merges without the clamp in the path.
   - **Servo power is external, always:** the arm's six servos run from their
     own 5–6 V supply with a shared ground — **never from the Arduino's 5 V
     pin** (six unbranded servos will brown-out or cook the board). Claude
     refuses to write wiring docs that skip this. The supply is **sized for
     stall headroom** — MG996R-class servos stall at ~2.5 A each
     (https://components101.com/motors/mg996r-servo-motor-datasheet), so six
     ≈ 15 A worst-case; a 10 A-class supply is workable only with slow easing
     and staggered moves — and the V+ rail carries an **inline fuse (or
     polyfuse) plus a human-reachable e-stop/power switch**: alerts stay
     software, cutting power stays a hand on a switch.
   - Anything mains-powered, hot-end, or load-bearing gets a "check this
     yourself" note in the PR — Claude flags, the human verifies.
   - **Secrets never live in files:** any token (Wokwi CI, printer APIs) goes
     in Actions/Codespaces secrets referenced as `${{ secrets.X }}`; ship a
     `.env.example` with names only; never a literal token in YAML, sketches,
     or committed scripts
     (https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).
4. **Git in maker terms** (full version in `docs/git-for-makers.md`):
   - a **branch** is a fresh piece of stock — cut it up freely, the good material
     is untouched;
   - a **PR** is showing the piece at the bench before bolting it in;
   - **merge** is bolting it in;
   - **CI** is the automatic test-fit that runs every time (does the model still
     render? does the sketch still compile?);
   - the loop to learn by heart: *branch → change → PR → green → merge*.
5. **The idea ritual** — one-liner into `ideas/`, run the 8 questions
   (`docs/idea-ritual.md`) when you feel like it. **No forced projects — an empty
   week is fine**, and logging "printed nothing, tuned nothing" is a valid, honest
   entry (§5, the honest-null rephrase).
6. **Session cards** — after a working session, ask Claude to write the card
   (three fields, §5). Skippable; the check nags gently, never blocks a merge on
   card *existence* (a gift must not scold).
7. **What Claude can and can't do here** — pointer to `docs/capabilities.md`:
   can design/review/run CI; cannot see the printers, start prints, or know
   filament stock unless it's logged.

## 3 · Starter FINISHED projects (ship pre-built; five, each with acceptance criteria)

Each is buildable by the fleet **before gifting** with zero hardware in the loop
(the arm project proves itself in dry-run + tests; live motion is the friend's
day-7 moment). Tool picks are defensible defaults; the companion dossier may swap
them at build time.

**(a) Parametric box & bracket generator** — OpenSCAD (or build123d if the dossier
prefers Python-native), with a GitHub Action rendering STL previews on every PR.
The flagship: it powers the day-2/3 curriculum and the first-PR tutorial.
Acceptance criteria:
1. `box(w,d,h,wall)` and `bracket(...)` sources render to **manifold** STL
   headlessly in CI (no GUI, exit 0, mesh-validity check passes).
2. A PR touching any `printing/models/` source gets an STL artifact plus a
   rendered preview image posted to the PR.
3. README worked example completes end-to-end: change one named parameter via PR
   → CI posts the new preview → merge.

**(b) Print-log + filament tracker** — CSV + one small stdlib script; the "data
lives in git" lesson. Acceptance criteria:
1. `scripts/printlog.py add` appends a row (date, printer, model, filament/spool
   id, grams used, result ok/fail).
2. `scripts/printlog.py report` prints grams-remaining per spool (purchases minus
   logged usage) and a fail-rate per printer.
3. A push touching the CSV regenerates a markdown summary via Action.
4. Documented upgrade path to Spoolman (import-script stub + doc note), so the
   toy version has a growth story instead of a dead end.

**(c) Robot-arm control starter** — targeted at exactly the friend's hardware: a
generic 6DOF/6-servo kit (Amazon.nl, no controller included), driven by his own
Arduino, most likely through a **PCA9685 16-channel servo driver** (the typical
controller for these kits; MG996R-class 180° servos likely). Buy-one-part
alternative: a **Pololu Micro Maestro 6-channel USB servo controller**
(https://www.pololu.com/product/1350 — native USB/TTL serial, per-channel
speed/acceleration limits) drives the arm host-side from Python with no Arduino
in the loop; PCA9685 stays the default since the friend already owns the
Arduino. Two layers: an
Arduino firmware sketch (PCA9685 over I2C, accepts joint commands over USB
serial, clamps + eases on-board) and a Python + pyserial side that sends
routines. Because unbranded 180° servos vary unit-to-unit and strip easily, the
defaults are **conservative software travel limits + slow easing**, and the
**FIRST arm project is a per-joint calibration routine**: step each servo gently
to find its real min/max, store the result as `arm/calibration.json` in the repo
— a config-file edit that is deliberately perfect first-PR material (it feeds
the §6 curriculum: his calibration numbers land via his own PR). Acceptance
criteria:
1. The calibration routine walks one joint at a time in small increments with
   confirm-to-continue, and writes/updates `arm/calibration.json` (per-joint
   min/max + easing rate); the **Python host loads that file and sends the
   per-joint limits over serial in a connect handshake** before any motion
   command (an Uno-class board has no filesystem — the file never reaches the
   firmware directly), and the **firmware clamps every command to BOTH the
   received limits AND a flashed conservative safe superset** (compile-time
   constants), so out-of-envelope requests are refused twice — host-side
   (unit-tested against a stub) and on-board — before any pulse is sent.
2. Shipped defaults are conservative (well inside 180°, slow easing) and apply
   whenever a joint has no calibration entry yet — uncalibrated never means
   unlimited.
3. `python3 arm/wave.py --dry-run` prints the exact command sequence with no
   port attached (CI-provable, hardware-free), and the recorded wave poses all
   verify inside the calibrated envelope by test.
4. README states the §2 safety rules verbatim at the top: live motion only with
   a human watching, and servo power from an external 5–6 V supply (shared
   ground, sized for stall headroom, fused V+ rail, human-reachable
   e-stop/power switch), never the Arduino's 5 V pin.

**(d) Calibration pack** — temp-tower + flow-test generators plus a
`printing/presets/` convention for **both** printers including 3-color profiles.
Acceptance criteria:
1. Generators emit sliceable STL for a temp tower and flow cubes headlessly in CI.
2. `printing/presets/small/` and `printing/presets/color3/` each hold one
   committed baseline profile; `color3/` includes a multi-material/3-color
   profile stub with the fields the friend's slicer needs named.
3. A doc walks the loop closed: print the tower → pick the winner → record it
   back into presets via PR (the presets folder is the *output* of calibration,
   not decoration).

**(e) "First PR" tutorial project** — Claude walks him through editing a
parametric model via PR review; the day-2 curriculum step. Acceptance criteria:
1. `projects/first-pr/` contains the tutorial with **literal paste-able prompts**
   at every step (Q-0263.2 style: never make him derive anything).
2. The target model exposes exactly one obvious tunable (e.g. `hole_diameter`).
3. Completing the tutorial yields a merged PR plus a rendered preview of his
   changed part.
4. The whole flow works with **zero local toolchain** — GitHub web editor +
   Actions only (day one must not start with an install festival).

## 4 · Starter `ideas/` backlog — 14 one-liner heads (the discovery engine)

Seeded one-per-file in `ideas/`, each a single captured line he can probe with his
own Claude via the idea ritual. Arm+printer crossovers marked ⨯.

1. ⨯ **Arm as print-removal assistant** — envelope-limited push-off routine that
   sweeps a finished print from the small printer's flex plate into a bin.
2. ⨯ **Arm-held camera timelapse** — the arm orbits a phone/ESP32-cam around a
   print for smooth moving timelapses, stepped once per layer change.
3. ⨯ **Printed end-effector kit** — parametric wrist-mount fingers, suction cup,
   and pen holder for the arm (the arm improves itself on the printers).
4. ⨯ **Pen-plotter mode** — arm + printed pen holder draws SVGs; Claude converts
   drawings into clamped serial motion scripts.
5. ⨯ **Arm teach-mode** — record poses by hand with a joystick, replay within the
   envelope; the routine library that feeds heads 1, 2, and 4.
6. ⨯ **Pick-and-place party trick** — arm moves printed chess pieces on a printed
   board grid; an accuracy benchmark disguised as a demo.
7. **Multi-color keychain factory** — parametric name-keychain generator tuned to
   the 3-color printer, with a batch plate-layout script for gift runs.
8. **3-color lithophane night-light** — generator + workflow doc for the color
   unit's most impressive show-off print.
9. **Tolerance test coin + fit calculator** — print a clearance-ring set, record
   which fits, and Claude maintains a per-printer clearances constant every later
   model imports (calibration that compounds).
10. **Parametric drawer-organizer generator** — feed a CSV of drawer measurements,
    get a fitted bin set per drawer.
11. **Filament dry-box hygrometer logger** — Arduino + DHT22 logging
    humidity/temperature CSV straight into the print-log conventions.
12. **Spool-weight scale** — load cell + Arduino reporting real grams-remaining
    into the tracker (the project-b upgrade path made physical).
13. **Print-failure camera watchdog** — cheap webcam + frame-diff detection that
    **alerts only, never auto-pauses** (the §2 safety rule applied to automation).
14. **Sound-reactive desk lamp** — printed shade + Arduino mic + LED ring; the
    pure-Arduino head that needs neither printer.

## 5 · Fleet reuse inventory

| Artifact | Source (citation) | Adaptation needed |
|---|---|---|
| substrate-kit itself (vendored `bootstrap.py`) | kit HEAD v1.15.0: substrate-kit `pyproject.toml`@0801be9 + `CHANGELOG.md`@0801be9; what adopt plants + guided mode: substrate-kit `README.md`@0801be9; fleet lanes on v1.14.0 per fleet-manager `docs/roster.md`@54a9588 | vendor the newest **tagged release** at seed time (never HEAD — the sibling head's gap-5 pinning rule); copy the kit's LICENSE alongside `bootstrap.py` as `LICENSE-substrate-kit` (MIT notice-retention — confirmed present upstream at the pin: https://raw.githubusercontent.com/menno420/substrate-kit/0801be9/LICENSE); adopt in `guided` mode; the §1 cut list applied (no control plane, no fleet checkers) |
| auto-merge-enabler workflow | `.github/workflows/auto-merge-enabler.yml`@949fc0b (idea-engine local) | rewrite the branch allowlist to the gift repo's prefixes (`project/`, `idea/`, `fix/`, `tutorial/`); KEEP the refuse-to-arm-on-zero-required-contexts guard verbatim (it protects a beginner from instant-merge surprise); DROP the born-red card-status host customization (§1 cut) |
| `.sessions/` card ritual | `.sessions/README.md`@949fc0b | simplify to three fields: **Status** · **what happened** (3 bullets max) · **💡 next time** — drop model-attribution lines, previous-session review duty, and auto-draft `[[fill]]` machinery; check nags on malformed cards, never blocks on absent ones |
| preflight/check pattern, reduced to 3 lightweight checks | `scripts/preflight.py`@949fc0b (one PASS/FAIL line per check, worst-exit wrapper) + `scripts/check_ideas.py`@949fc0b (grammar-lint shape) | new checks: (1) every `printing/models/` source renders a manifold STL headlessly; (2) every `arduino/` sketch compiles via arduino-cli; (3) every markdown link in the repo resolves — keep the wrapper's one-command, one-line-per-check report shape |
| 8-question probe battery → one-page `docs/idea-ritual.md` | superbot `docs/ideas/idea-probe-brainstorm-simulator-2026-07-10.md`@5c84ce2 (battery + panel + forward-sim modes) + idea-engine `README.md`@949fc0b § The probe battery | condensed maker phrasing, single-pass only: 1 *What is this thing, really?* 2 *What could it grow into?* 3 *What's the coolest version of the simplest build?* 4 *What breaks it — printability, tolerance, torque?* 5 *What does it let me build next?* 6 *What does it need — parts, filament, libraries?* 7 *Who does what — me, Claude, or both?* 8 *What's the smallest piece I can finish this weekend?* Ends in ONE of: **build / park / drop / think more** |
| honest-null doctrine | idea-engine `README.md`@949fc0b ("not measured" beats invention — the probe honesty norm) | hobbyist rephrase, verbatim into CLAUDE.md §5: "**No forced projects — an empty week is fine.** Write 'printed nothing' rather than inventing activity; a true nothing beats a fake something." |
| capabilities ledger + discovery rule | `docs/CAPABILITIES.md`@949fc0b | reshape into `docs/capabilities.md` for one human: what Claude CAN do here (design models, review sketches, read CI logs, remember via cards) and CANNOT (see printers, start prints, know spool stock unless logged) — plus the discovery rule kept intact: *try once and record the real error before declaring a wall* |

## 6 · Claude+GitHub discovery curriculum — the first week, one feature per day

Each step teaches exactly one GitHub+Claude concept and pays off with something a
maker actually wants. Ordered so no step needs a tool the previous one didn't
already prove.

0. **Day 0 — connect Claude (setup, before the fun starts):** install/authorize
   the Claude GitHub integration on **his** account for the gift repo, then
   verify it: comment `@claude hello` on the seeded welcome Issue — Claude
   replies = connected. Fallback if the integration isn't available to him:
   run Day 1 through Claude chat instead — paste the Issue text into chat,
   paste Claude's plan back as a manual Issue comment (same payoff, one copy
   hop). The walkthrough ships as a `docs/` setup page (slice 5). Teaches:
   nothing yet — it removes the one stall that would kill Day 1.
1. **Day 1 — Issues:** open an Issue describing a part he needs ("a hook for my
   headphones under the desk"); ask Claude to answer in the Issue with a design
   plan. Payoff: the repo talks back. Teaches: Issues as the front door.
2. **Day 2 — first PR:** run `projects/first-pr/` (project e) end-to-end in the
   web editor. Payoff: his first merged change, no installs. Teaches:
   branch → PR → merge.
3. **Day 3 — Actions:** change one parameter in the box generator (project a) via
   PR; watch CI render his STL preview and the PR merge itself on green. Payoff:
   a part he designed, previewed by robots. Teaches: CI + merge-on-green.
4. **Day 4 — the idea ritual:** write one backlog one-liner of his own into
   `ideas/`, ask Claude to run `docs/idea-ritual.md` on it, commit the filled
   file. Payoff: a vague notion becomes a plan. Teaches: the repo as a thinking
   surface.
5. **Day 5 — data in git:** log three real prints with the tracker (project b),
   ask Claude for the filament report. Payoff: knows his spool state for the
   first time ever. Teaches: files-as-database, scripts in CI.
6. **Day 6 — releases:** print the temp tower (project d), record the winning
   temperature into presets via PR, tag `presets-v1` as a Release with the STL
   assets attached. Payoff: his printer's first calibrated baseline, versioned.
   Teaches: tags + releases.
7. **Day 7 — hardware in the loop:** wire the arm per the safety rules (external
   servo supply, PCA9685), run the per-joint calibration routine (project c) and
   land his real min/max numbers as a `arm/calibration.json` PR — his first PR
   that changes how a physical machine moves (the limits reach the board over
   serial at connect, per the §3c handshake — no reflash needed). Then
   `arm/wave.py --dry-run`, read
   the command stream, and run it live inside his freshly calibrated envelope
   with hand on the switch; open an `ideas/` head for his first end-effector
   (backlog #3). Payoff: the arm waves at him, within limits he measured
   himself. Teaches: the safety agreement as lived practice, and the loop
   closing — hardware feeds config feeds ideas feeds the repo.

## 7 · Delivery plan + boundary

**Boundary (Q-0260 discipline):** this seat writes ideas only — this file IS the
deliverable. Repo creation, seeding, and project builds are the owner's clicks
plus manager-routed build slices; nothing here touches another repo. The friend's
own Claude account connects from his side (his account, his consent, his tokens —
nothing to provision from the fleet).

**Routed build slices, in order** (each a bounded merged-on-green PR in the gift
repo once it exists):

1. **Slice 1 — skeleton + kit seed:** repo layout (§1), vendored `bootstrap.py`
   at the newest tagged release (+ its LICENSE copy), CI gate with the 3
   lightweight checks, adapted auto-merge enabler, CLAUDE.md + docs rendered
   per §2. **Step 0, owner clicks (agents cannot change repo settings):**
   Settings → General → Pull Requests → enable **"Allow auto-merge"**, and add
   a **default-branch ruleset requiring the gate status check** — the enabler
   is inert without both, and its guard refuses to arm on zero required
   contexts (kept verbatim per §5), so skipping this silently disables the
   Day 3 merge-on-green demo.
2. **Slice 2 — projects (a) + (e):** box/bracket generator with STL-preview
   Action, and the first-PR tutorial — the day-2/3 curriculum depends on these,
   so they land first.
3. **Slice 3 — projects (b) + (d):** print-log/filament tracker and the
   calibration pack with both printers' preset folders.
4. **Slice 4 — project (c):** arm control starter — firmware sketch (PCA9685),
   Python side, per-joint calibration routine, conservative defaults, dry-run
   wave, tests (hardware-free by design, §3c; real min/max land later via the
   friend's own calibration PR).
5. **Slice 5 — content polish:** the 14 backlog heads seeded into `ideas/`,
   `docs/idea-ritual.md`, the Day-0 connect-Claude setup page (§6, with the
   chat fallback), the curriculum as `README` day-one section, gift-letter
   README pass.

**Owner ask (paste-ready, six-field OWNER-ACTION style — answerable with ONE
line):**

> ⚑ OWNER-ACTION · **WHAT:** three choices in one reply — gift repo name,
> visibility, and which starter projects make the cut — plus **two one-time
> setup clicks after creating the repo** (owner-only, agents cannot change
> repo settings): Settings → General → Pull Requests → enable **"Allow
> auto-merge"**, and add a **default-branch ruleset requiring the gate status
> check** — without both, the seeded auto-merge enabler stays inert and the
> Day 3 "PR merges itself on green" demo never fires. **WHERE:** reply in any
> owner channel the manager sweep reads; the build routes as slices 1–5 above.
> **HOW (paste ONE line — recommendation first):** RECOMMENDED
> `"Gift repo: name=makerbench, private + invite my friend as collaborator, ship all five starter projects (a–e), build slices 1–5 as blueprinted."`
> · Alternatives: name=`filament-and-firmware` or your own; `public` instead of
> private (fine, nothing sensitive — private is recommended only so his first
> fumbling PRs aren't world-readable; caveat: on a Free-plan **private** repo
> GitHub Pages is unavailable, and a published Pages site is public regardless
> of repo visibility — any gallery idea uses Releases/artifacts instead,
> https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages);
> `"drop project (c)"` if gifting sooner
> matters more than the arm demo (slices renumber, nothing else changes).
> Possible shopping-list add-on to the same reply: a **PCA9685 16-channel servo
> driver board** (a-few-euro part) if the friend doesn't already have one — his
> arm kit ships with no controller, and project (c) assumes one — **plus,
> unless he confirms he already has them, a 5–6 V high-current external servo
> supply sized for stall headroom (six MG996R-class servos ≈ 15 A worst-case;
> 10 A-class workable with easing + staggered moves), an inline fuse for the
> V+ rail, a barrel-jack/screw-terminal adapter, and common-ground jumper
> wiring** — the §2 safety rules forbid powering the servos from the Arduino's
> 5 V pin, so a missing supply stalls Day 7 or nudges an unsafe workaround.
> One-part alternative: a **Pololu Micro Maestro 6-channel USB servo
> controller** (https://www.pololu.com/product/1350) replaces both the PCA9685
> and the Arduino-in-the-loop for the host-driven path (§3c).
> **WHY-IT-MATTERS:** name and visibility gate slice 1; the project cut sizes
> slices 2–4 — everything downstream of one reply. **UNBLOCKS:** slice-1 routing
> to a build lane, and the sibling research dossier gets a concrete target to pin
> against. **VERIFIED-NEEDED:** repo creation + collaborator invite are owner-only
> clicks — `docs/CAPABILITIES.md`@949fc0b classes console/creation actions
> owner-click, and this seat's GitHub scope is idea-engine only (session
> boundary, verified this capture: cross-repo reads went via raw/ls-remote).

**Citation honesty note:** all external pins above (`0801be9`, `54a9588`,
`5c84ce2`) are real `git ls-remote` HEAD pins taken 2026-07-12T17:3xZ with the
cited files fetched at those exact SHAs via raw.githubusercontent.com (the
`docs/CAPABILITIES.md`@949fc0b recipe); idea-engine cites use local HEAD
`949fc0b`. Nothing below a claim carries an invented SHA; where the recon
expectation (kit ~v1.14.0) diverged from the measured truth (kit HEAD v1.15.0,
lanes on v1.14.0), both are stated.

## Review fold-in (2026-07-12, codex review @ bb5a9d6)

codex left five P2 line comments on PR #264; a read-only verification pass
checked each against the tree (auto-merge-enabler guard code included) and
external sources. All five **accepted** and folded in above:

1. **r3566889627 — auto-merge setup missing from the owner ask:** accepted —
   the Day 3 self-merge demo depends on "Allow auto-merge" + a required-check
   ruleset, which no slice or owner ask covered, and the enabler's guard
   refuses to arm on zero required contexts; owner clicks added to §7 and
   slice 1.
2. **r3566889628 — vendored kit LICENSE not carried:** accepted — the skeleton
   copied MIT-licensed `bootstrap.py` while the LICENSE stayed upstream only
   (confirmed present at the pin:
   https://raw.githubusercontent.com/menno420/substrate-kit/0801be9/LICENSE);
   `LICENSE-substrate-kit` added to §1/§5 and the intro claim corrected.
3. **r3566889629 — no Day 0 Claude authorization step:** accepted — Day 1
   assumed a working Claude/GitHub integration nothing ever set up; Day 0
   (install/authorize + `@claude hello` verification + chat fallback) added to
   §6, setup page added to slice 5.
4. **r3566889630 — firmware can't read `arm/calibration.json` at runtime:**
   accepted — an Uno-class board has no filesystem; criterion (c)1 rewritten
   to a serial connect-handshake (host sends limits) plus a flashed
   conservative safe superset clamp on-board, Day 7 noted no-reflash.
5. **r3566889631 — servo supply missing from the shopping list:** accepted —
   the §2 safety rules mandate an external 5–6 V supply the add-on never
   listed; supply + fuse + wiring + confirm-ask added to §7.

Cross-folded from the companion dossier's review (PR #265 @ fb9039e), the five
points flagged `blueprint_too` by the verification pass:

- stall headroom (6 × ~2.5 A), V+ fusing, and a human-reachable e-stop added
  to the §2.3 servo-power rule and project (c) acceptance criterion 4;
- Pololu Micro Maestro named as the buy-one-part alternative in §3c and the
  §7 shopping list;
- `.devcontainer/` line added to the §1 skeleton (day-3+ toolchain as a
  Codespace);
- secrets convention (Actions secrets, `.env.example`, never tokens in YAML)
  added to the §2 rules;
- GitHub Pages private-repo caveat (paid plan required, published sites are
  public regardless) added to the §7 visibility alternative.
