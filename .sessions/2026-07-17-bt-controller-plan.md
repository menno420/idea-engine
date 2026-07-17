# Session — bt-controller-plan (ORDER 017 owner idea intake)

> **Status:** `complete`
> 📊 Model: opus-4.8 · high · research
>
> *(card born in-progress as the designed session-gate HOLD — the born-red FIRST commit; flips to complete in this PR's final commit after the research + veto-ready plan lands.)*

## Scope
ORDER 017 owner ask — research the viability of, and produce a veto-ready plan for, a phone-as-Bluetooth-controller app (turn a phone into a customizable BT controller for other phones/tablets/devices, optionally using hardware volume buttons as input).

## ⟲ Previous-session review
The prior card (`.sessions/2026-07-17-verdict-106-metastable-retry-storm-collapse.md`) mirrored sim-lab VERDICT 106 (P093 → APPROVE, retry-amplified metastable overload) and handed the baton to the round-21 venture slot — an honest, tightly-scoped close that held its born-red HOLD correctly. Pipeline state at this session's boot (read from control/outbox.md): P094 → VERDICT 107 closed (APPROVE, mirror 2026-07-17T11:12:40Z); PROPOSAL 095 (rubber-band-controller-instability) was just drafted `status: sim-ready` and is not yet verdicted — it awaits VERDICT 108 (+13). So the pipeline is mid-round with one unverdicted PROPOSAL outstanding, not at a fully clean boundary; this ORDER-017 owner-idea plan rides alongside it and does not touch the sim bus.

## 💡 Session idea
A **capability-probe-first install pattern**: gate any OEM-fragile platform feature behind a runtime probe plus a pre-install support matrix, so a dead-on-arrival device never reaches a broken core loop. Concretely for this app, Android's Bluetooth HID *device* role is disabled on many phones via an OEM compile-time flag, so `registerApp()` can fail on an API-28+ device that looks supported on paper. The fix is to make the very first slice a probe that (a) attempts `BluetoothHidDevice` registration once and captures the exact result, (b) checks the BLE-peripheral/advertiser capability as a fallback signal, and (c) renders a device support matrix before the user ever reaches the controller UI. Generalizes to any capability whose SDK presence does not guarantee runtime support: probe once, capture the error, surface a support verdict, and never ship the user into a core loop the device cannot run.

📊 Model: opus-4.8 · high · research
