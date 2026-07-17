# Phone-as-a-Bluetooth-controller: Android is viable-but-OEM-gated as a true BT-HID controller; iOS is walled off as a HID peripheral — research + veto-ready plan

> **State:** captured
> **Class:** product · consumer mobile app · phone becomes a customizable Bluetooth HID controller for other phones/tablets/TVs/PCs
> **Target:** `menno420/idea-engine` (owner idea-intake plan; not a sim proposal)

updated: 2026-07-17T12:21:39Z
provenance: ORDER 017 · owner live in the coordinator seat 2026-07-17 · research fetched 2026-07-17 (three research passes: Android HID, iOS/receivers, volume-keys/competitors)

This is a **captured** plan awaiting owner review (a veto-ready menu, not a build order and not a `sim-ready` outbox PROPOSAL — it routes nothing to sim-lab). Every load-bearing external claim below carries an inline source URL and the ISO date it was fetched.

---

## TL;DR — viability verdict

**Android: VIABLE, but OEM-gated.** An Android phone can be a *true* Bluetooth-HID controller (keyboard/mouse/gamepad) to any standard receiver with no companion app, via `BluetoothHidDevice` (Android 9 / API 28+) — but the HID *device* role is behind an OEM compile-time flag, so `registerApp()` fails on many shipped phones and support must be probed at runtime, not assumed.

**iOS: NOT VIABLE as a Bluetooth-HID peripheral.** iOS blocks the HID-over-GATT service UUID `0x1812` at the OS level (`CBError` code 8, "The specified UUID is not allowed for this operation") and does not expose Bluetooth Classic HID to apps at all — this is an **OS restriction, not an MFi licensing issue** (MFi expressly exempts standard Bluetooth). An iPhone can only be a *network* controller to a companion receiver app, or act as a *receiver*.

---

## Recommended MVP

**Android-as-controller, true BT-HID, serverless.**

- Transport: **Classic Bluetooth HID via `BluetoothHidDevice`** (Android 9 / API 28+) — the phone registers a HID report descriptor and sends input reports directly, so the receiver sees a standard keyboard/mouse/gamepad with **no software installed on the target** ([developer.android.com — BluetoothHidDevice](https://developer.android.com/reference/android/bluetooth/BluetoothHidDevice), fetched 2026-07-17; API-28 attribute confirmed via [Microsoft Learn — BluetoothHidDevice Class](https://learn.microsoft.com/en-us/dotnet/api/android.bluetooth.bluetoothhiddevice?view=net-android-35.0), fetched 2026-07-17).
- Receivers that accept a standard BT HID device out of the box: **PCs (Windows/macOS/Linux), Android phones/tablets, iPad/iPhone (keyboard/mouse), and most 2022+ smart TVs** (see the compatibility matrix below).
- Product surface: a **customizable button/layout editor + saved profiles** (the differentiator — see the competitor gap), starting from a fixed media-remote layout and growing to arbitrary grids.
- Hardware-button input: **foreground-only** volume-key capture (reliable and store-safe; background capture is blocked — see findings).
- Guardrail: a **capability probe + support matrix as the very first slice**, so an OEM-disabled device never reaches a broken core loop.

---

## Slice list

Effort S/M/L. Reversibility = how cleanly the slice can be pulled if it doesn't pan out.

| Slice | Effort | Risk | Reversibility | Unblocks |
|---|---|---|---|---|
| 1. Capability probe + device support matrix (attempt `registerApp()` once, capture exact result; check BLE-peripheral capability; render a pre-install/first-run support verdict) | **S** | Low | High (self-contained screen) | Everything — stops DOA devices before the core loop |
| 2. Core BT HID transport: register app + `sendReport()` on the interrupt channel | **M** | Med (OEM role may be absent) | High (single module) | 3–7 |
| 3. Minimal fixed media-remote layout driving a real receiver end-to-end | **M** | Med | High | Proves the loop; unblocks 4 |
| 4. **Customizable layout editor** (button grid → HID keycodes / consumer-control usages) — the differentiator | **L** | Med | Med (schema migration if profiles ship) | 5; the product's moat |
| 5. Profiles: save / load / switch per target device | **M** | Low | Med | Multi-device UX |
| 6. Gamepad HID descriptor + analog stick (buttons bitfield + X/Y/Z/Rz axes) | **L** | Med | High (separate descriptor) | Gaming use-cases |
| 7. Foreground volume-key-as-input mapping (`onKeyDown` consume) | **S** | Low | High | Hardware-button feature |
| 8. Latency instrumentation + on-device measurement (replace the budget below with real numbers) | **S** | Low | High | Honest latency claims |

**Deferred / parked rows:**

| Slice | Effort | Status |
|---|---|---|
| iOS network-companion-receiver product (Wi-Fi/UDP/WebRTC to a helper app on the target) | **L** | Deferred — needs a receiver app on every target; can't drive arbitrary devices |
| Background hardware-button capture (screen-off / from another app) | — | **Blocked** / high Play-policy risk (AccessibilityService remap) |
| BLE-HOGP fallback via generic GATT for phones where the Classic HID device role is disabled | **L** | Parked — build only if probe data shows meaningful coverage gain |

---

## Research findings

### Android as a true BT-HID controller — VIABLE but OEM-gated
- `BluetoothHidDevice` was introduced in **Android 9 (Pie) / API level 28**; it lets the phone *be* the HID peripheral (keyboard/mouse/gamepad/remote), registering a HID report descriptor via `registerApp(...)` and sending input reports via `sendReport(BluetoothDevice, id, data)` ([Microsoft Learn — BluetoothHidDevice Class](https://learn.microsoft.com/en-us/dotnet/api/android.bluetooth.bluetoothhiddevice?view=net-android-35.0), fetched 2026-07-17; canonical page [developer.android.com — BluetoothHidDevice](https://developer.android.com/reference/android/bluetooth/BluetoothHidDevice), fetched 2026-07-17 — SPA did not render class text, API-28 detail sourced from the Microsoft AOSP mirror).
- It is **Classic Bluetooth HID, not BLE.** The HID device role "has been implemented in bluedroid using classic bluetooth," with BLE HOGP named only as future work ([HSC — Android Labs: Bluetooth HID Device implementation](https://www.hsc.com/resources/blog/android-labs-bluetooth-hid-device-implementation-your-phone-as-a-mouse-voice-control/), fetched 2026-07-17).
- **OEM compile-flag gating (the central caveat):** the device role "is being controlled through a compile time flag," so an OEM can ship an API-28+ phone where `registerApp()` never succeeds ([HSC — Android Labs](https://www.hsc.com/resources/blog/android-labs-bluetooth-hid-device-implementation-your-phone-as-a-mouse-voice-control/), fetched 2026-07-17). App-side corroboration: the **Kontroller** app ships a *separate compatibility-checker app* and warns "Many manufacturers have disabled the HID device profile" ([GitHub — raghavk92/Kontroller](https://github.com/raghavk92/Kontroller), fetched 2026-07-17); the `ralismark/bluehid` issue tracker names OnePlus/Motorola/LG on Android 9 (anecdotal — no models/logs, so the *specific* vendor list is **unverified in detail**, while the *general* "not universal" point is well-supported) ([GitHub — ralismark/bluehid issue #1](https://github.com/ralismark/bluehid/issues/1), fetched 2026-07-17).
- **Named open-source precedents** (true BT HID, Android 9+, no host software): **Kontroller** ([raghavk92/Kontroller](https://github.com/raghavk92/Kontroller), fetched 2026-07-17), **HidPeripheral** ([LiangLuDev/HidPeripheral](https://github.com/LiangLuDev/HidPeripheral), fetched 2026-07-17), **Blek** ([AppGround-io/bluetooth-keyboard-and-mouse-support](https://github.com/AppGround-io/bluetooth-keyboard-and-mouse-support), fetched 2026-07-17), and **Pocket-Pad** (true BT-HID gamepad) ([jobrobse/Pocket-Pad](https://github.com/jobrobse/Pocket-Pad), fetched 2026-07-17). A BLE-HOGP fallback (not via `BluetoothHidDevice`, but a manual GATT server, API 21+) is demonstrated by [kshoji/BLE-HID-Peripheral-for-Android](https://github.com/kshoji/BLE-HID-Peripheral-for-Android) (fetched 2026-07-17) — but BLE peripheral/advertiser mode is itself a per-device hardware capability that must be checked at runtime.

### The iOS HID-peripheral wall — NOT VIABLE
- Calling `CBPeripheralManager.add()` with the HID service UUID **`0x1812` returns `CBError` code 8, "The specified UUID is not allowed for this operation"** — the system blocks it ([Apple Developer Forums, thread 725238](https://developer.apple.com/forums/thread/725238), fetched 2026-07-17). A community reference states it plainly: "As of iOS 14, the services are blocked by the system so it's impossible to make an iOS device act as a bluetooth keyboard" ([conath gist](https://gist.github.com/conath/c606d95d58bbcb50e9715864eeeecf07), fetched 2026-07-17).
- **MFi is not the blocker.** Apple's MFi FAQ states developers do *not* need MFi for accessories using "only Bluetooth Low Energy, Core Bluetooth, or standard Bluetooth profiles supported by iOS" ([MFi Program FAQs](https://mfi.apple.com/en/faqs.html), fetched 2026-07-17). The wall is the OS refusing apps the HID role, not licensing.
- iOS Bluetooth Classic HID is not exposed to apps at all, and the GameController framework only lets iOS *read* controllers, not *be* one ([Apple Developer Forums, thread 725238](https://developer.apple.com/forums/thread/725238), fetched 2026-07-17; [Game Controller | Apple Developer](https://developer.apple.com/documentation/gamecontroller), fetched 2026-07-17).
- **Fallback for iOS = network companion-receiver:** the app sends input over Wi-Fi (TCP/UDP/WebRTC) to a helper app on the target that injects synthetic input — the pattern used by [Remote Mouse](https://www.remotemouse.net/), [Unified Remote](https://apps.apple.com/us/app/unified-remote/id825534179), and [Remote Buddy](https://www.iospirit.com/products/remotebuddy/) (all fetched 2026-07-17). It **requires a companion app on every target** and therefore cannot drive TVs/consoles/other phones out of the box.

### Receiver-side compatibility matrix (which targets accept a standard BT HID device with NO companion app)

| Target (as RECEIVER) | Std BT HID keyboard | Std BT HID mouse | BT gamepad | Out-of-box (no companion app)? | Needs app? |
|---|---|---|---|---|---|
| Android phone/tablet | Yes | Yes | Yes | **Yes** | No |
| iPhone / iPad | Yes | Yes (iOS 13 / iPadOS 13.4 cursor) | Xbox/DS4/MFi via GameController | **Yes to pair;** gamepad needs the app to adopt GameController framework | kbd/mouse no; gamepad needs framework-aware app |
| Smart TV — Android/Google TV | Varies | Varies | Yes | **Mostly (esp. 2022+)** | Platform-dependent |
| Smart TV — LG webOS | Yes | Yes | Yes | **Yes** | No |
| Smart TV — Samsung Tizen | Varies | Varies | Yes | **Mostly (esp. 2022+)** | No |
| Smart TV — Apple tvOS | Yes | n/a | Xbox/DS4/MFi via GameController | **Yes to pair;** gamepad via framework | kbd no; gamepad needs framework-aware app |
| Windows / macOS / Linux PC | Yes | Yes | Yes (generic HID fallback) | **Yes** | No |

Sources: Android receiver [How-To Geek](https://www.howtogeek.com/164783/how-to-connect-mice-keyboards-and-gamepads-to-an-android-phone-or-tablet/); iPad cursor iPadOS 13.4 [MacStories](https://www.macstories.net/news/apple-releases-ios-and-ipados-134-with-ipad-cursor-support-and-keyboard-improvements-icloud-drive-shared-folders-and-more/) + [Apple Support 111775](https://support.apple.com/en-us/111775); iOS/tvOS gamepads [9to5Mac](https://9to5mac.com/2019/09/01/ios-13-playstation-xbox-game-controller-iphone-ipad/); TV rows [LG](https://www.lg.com/us/support/help-library/what-external-devices-are-compatible--20152528678452), [Samsung Developer](https://developer.samsung.com/smarttv/accessory/gamepad.html), [Android TV Help](https://support.google.com/androidtv/answer/6121457), [Alibaba TV guide](https://electronics.alibaba.com/buyingguides/smart-tv-game-controller-guide-how-to-choose-use) (aggregator, medium confidence); PC HID [linux-usb.org](http://www.linux-usb.org/USB-guide/x194.html), [joycheck.io](https://joycheck.io/blog/generic-hid-controller/) — all fetched 2026-07-17. "Varies" = supported but coverage depends on model year/firmware; older TVs (2018–2021) may need updates.

### Hardware (volume) button capture
- **Foreground: YES.** An app with a focused Activity can intercept `KEYCODE_VOLUME_UP`/`KEYCODE_VOLUME_DOWN` via `onKeyDown()`/`dispatchKeyEvent()` and return `true` to consume — the store-safe, well-trodden path ([Envato Tuts+ — Intercepting Physical Key Events](https://code.tutsplus.com/tutorials/android-sdk-intercepting-physical-key-events--mobile-10379), fetched 2026-07-17; the `KeyEvent` constants are standard Android API).
- **Background rocker: BLOCKED.** There is no supported general API to intercept the physical volume buttons when backgrounded/screen-off. MediaSession/`MediaButtonReceiver` covers *media transport* keys (play/pause/next), **not** the volume rocker; `VolumeProviderCompat` only fires while your app owns remote-playback volume ([Android Developers — Responding to media buttons](https://developer.android.com/media/legacy/media-buttons), fetched 2026-07-17).
- **AccessibilityService remap = HIGH Play-policy risk.** Using AccessibilityService for non-accessibility button remapping requires a Play Console declaration + prominent disclosure + affirmative consent, is subject to "use a narrower API instead" rejection, and risks app suspension / account termination ([Play Console — Use of the AccessibilityService API](https://support.google.com/googleplay/android-developer/answer/10964491?hl=en), fetched 2026-07-17).

### Competitor scan + market gap
- **True BT-HID, serverless** apps exist but offer little layout customization: **Serverless BT Keyboard & Mouse ("blek")** — fixed kbd/trackpad/media surfaces ([APKPure](https://apkpure.com/bluetooth-keyboard-mouse/io.appground.blek), fetched 2026-07-17); **Pocket-Pad** and **Kontroller** — gamepad/sample-basic.
- **Highly customizable** apps all **require a companion/server on the target**: **Unified Remote** (Custom Remotes builder) ([unifiedremote.com](https://www.unifiedremote.com/features), fetched 2026-07-17), **Touch Portal** (custom button deck), **Elgato Stream Deck Mobile** (up to 64-key grid, needs the Stream Deck desktop app) ([Elgato Stream Deck Mobile](https://www.elgato.com/us/en/s/stream-deck-mobile), fetched 2026-07-17).
- **Identified gap (INFERENCE, not a sourced claim — verify with deeper store review):** no mainstream app is *both* serverless true-BT-HID *and* fully customizable (custom grids/profiles per target). The true-HID apps aren't customizable; the customizable ones need a server. That intersection appears unoccupied and is the proposed differentiator (slice 4).

### Store policy + risks
- A background-live BT controller should run a **foreground service (type `connectedDevice`, Android 14+) with a persistent notification** ([Android Developers — Communicate in the background](https://developer.android.com/develop/connectivity/bluetooth/ble/background), fetched 2026-07-17). iOS Core Bluetooth background is BLE/GATT only and "can't run forever" ([Apple — Core Bluetooth Background Processing](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/CoreBluetoothBackgroundProcessingForIOSApps/PerformingTasksWhileYourAppIsInTheBackground.html), fetched 2026-07-17).
- Using the public `BluetoothHidDevice` API is a **sanctioned** capability — no Play policy specifically bans HID emulation via it was found (an **unverified negative**, not exhaustive). The real policy risk is the AccessibilityService angle above.
- **Battery figures are UNVERIFIED.** Secondary blogs quote "15–22% standby drain" for always-on BT HID (Pixel 7, AccuBattery) vs ~1.8% for idle BT — do not quote these; **measure in-house** ([BLE battery, Medium](https://bleadvertiserapp.medium.com/why-your-ble-app-is-draining-battery-and-the-scan-strategy-that-fixes-it-2a10d904febf), fetched 2026-07-17; [Android Authority](https://www.androidauthority.com/does-bluetooth-drain-battery-1145853/), fetched 2026-07-17).

---

## Latency-budget model

**Methodology (illustrative, deterministic — NOT a measured sim-lab VERDICT).** The model at `ideas/product-forge/bt-controller-latency-budget.py` sums the fixed stages of the touch→receiver path (touch sampling on a 120 Hz screen → app + HID-report assembly → Bluetooth transport → receiver input-stack + render) as hand-entered min/typical/max ranges pulled from the research pass. There is **no randomness and no wall-clock** — it is arithmetic over disclosed assumptions, run for two transport profiles (Classic BT HID and BLE HID), and classified against reaction/action windows. Key source figures: 120 Hz period = 8.33 ms and 60 Hz frame = 16.7 ms (arithmetic); Classic BT HID ~10–32 ms (consumer explainer, order-of-magnitude, [LifeTips/Alibaba](https://lifetips.alibaba.com/tech-efficiency/bluetooth-keyboard-latency-vs-wired-for-gaming), fetched 2026-07-17 — partly unverified); BLE minimum connection interval 7.5 ms ≈ 133 Hz ([Novel Bits — BLE shorter connection intervals](https://novelbits.io/ble-shorter-connection-intervals-hands-on-nrf54l15/), fetched 2026-07-17). The app + HID-assembly constant is a **disclosed assumption** (no primary figure). **Recommend replacing this budget with on-device measurement (slice 8) before making any latency claim.**

Printed output (`ideas/product-forge/bt-controller-latency-budget.out.txt`):

```
==============================================================================
END-TO-END INPUT-LATENCY BUDGET - phone-as-Bluetooth-controller
Illustrative DETERMINISTIC budget (no RNG, no wall-clock). NOT a measured
sim-lab VERDICT. Recommend on-device measurement before quoting a number.
==============================================================================

FIXED COMPONENTS (shared across transports)   min /  typ /  max  (ms)
------------------------------------------------------------------------------
  touch sampling                     0.0 /   4.2 /   8.3   120 Hz sampling, 0..full-period (A1)
  app + HID report assembly          0.5 /   1.0 /   2.0   app wake + HID report assembly, DISCLOSED ASSUMPTION (A2)
  receiver input stack + render      8.3 /  16.7 /  33.3   receiver stack+render: 120Hz 1f / 60Hz 1f / 60Hz 2f (A4)

TRANSPORT STAGE                               min /  typ /  max  (ms)
------------------------------------------------------------------------------
  Classic BT HID                    10.0 /  21.0 /  32.0   ~10-32 ms polling band (A3, order-of-mag)
  BLE HID (HOGP)                     7.5 /  15.0 /  30.0   7.5 ms min conn interval, 1..4 intervals (A3)

END-TO-END TOTAL per transport (touch + assembly + transport + render)
------------------------------------------------------------------------------
  transport                min     typ     max   (ms)
  Classic BT HID          18.8    42.9    75.6
  BLE HID (HOGP)          16.3    36.9    73.6

CLASSIFICATION  (PASS = worst-case fits | MARGINAL = window inside range |
                 FAIL = even best case overruns)
  cols: media=no hard window  casual~100ms  action~50ms  compet.~16ms
------------------------------------------------------------------------------
  transport                  media      casual      action     compet.
  Classic BT HID              PASS        PASS    MARGINAL        FAIL
  BLE HID (HOGP)              PASS        PASS    MARGINAL        FAIL

WINDOWS: media/remote = no hard window; casual ~100 ms; action ~50 ms;
         competitive/frame-perfect ~16 ms (one 60 Hz frame).

VERDICT LINES:
  Classic BT HID: total 18.8/42.9/75.6 ms  ->  media / remote=PASS, casual gaming=PASS, action gaming=MARGINAL, competitive/frame-perfect=FAIL
  BLE HID (HOGP): total 16.3/36.9/73.6 ms  ->  media / remote=PASS, casual gaming=PASS, action gaming=MARGINAL, competitive/frame-perfect=FAIL

Both transports: comfortable for media/remote and casual play, MARGINAL for
action gaming, and FAIL the ~16 ms competitive/frame-perfect budget. Measure
on real hardware before making any latency claim.
```

**Read:** both transports are comfortable for media/remote and casual play, marginal for action gaming, and fail the ~16 ms competitive/frame-perfect budget. This matches the practical "~15–35 ms ballpark, fine for couch/remote, marginal-to-poor for twitch competitive" takeaway in the research — but it is a budget, not a measurement.

---

## iOS wall + fallbacks

Because iOS blocks the HID GATT service and denies apps the BT Classic HID role (see findings), the only shipping paths for iOS are:

1. **Network companion-receiver over Wi-Fi/UDP/WebRTC** — iOS app captures input and sends it to a helper app on the target that injects synthetic input. Upsides: no MFi, no HID restriction, richer features. Downsides: **requires a receiver app on every target** (so no TVs/consoles/other-phones out of the box), needs both devices on the same network, and adds a pairing/discovery step. This is what Remote Mouse / Unified Remote / Remote Buddy do.
2. **Position iOS as receiver-only, or defer iOS entirely** for v1 — iPhone/iPad already accept a standard BT keyboard/mouse and framework-aware gamepads *as a receiver*, so the Android controller can drive them without any iOS app.

Recommendation: **defer iOS-as-controller**; ship Android-as-controller first, keep iOS as a supported *receiver*.

---

## Open questions

1. **Real-world Android HID-device-role coverage** — what % of target devices actually allow `registerApp()`? The compile-flag gating is confirmed but field coverage is unquantified. Slice 1 (the probe) generates this data; consider aggregating anonymized probe results.
2. **Sustained foreground-service battery drain** — **unverified**; measure on real hardware (slice 8) before any marketing/UX claim.
3. **Is a BLE-HOGP fallback worth building** for phones where the Classic HID device role is disabled, given BLE peripheral mode is itself not universal? Decide from slice-1 probe data.
4. **Positioning / monetization vs the identified gap** — is "serverless true-BT-HID + fully customizable layouts" a large enough wedge, and how to price it (the customizable competitors monetize via subscription/desktop tie-in)?
