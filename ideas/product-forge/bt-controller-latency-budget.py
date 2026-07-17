#!/usr/bin/env python3
"""Illustrative end-to-end input-latency budget for a phone-as-Bluetooth-controller app.

WHAT THIS IS
    A deterministic, stdlib-only back-of-the-envelope budget that sums the fixed
    stages of the touch->receiver input path for two Bluetooth transport profiles
    (Classic BT HID via Android's BluetoothHidDevice, and BLE HID / HOGP) and
    classifies each total against common reaction/action windows.

WHAT THIS IS NOT
    Not a measurement, not a simulation with a stochastic model, not a sim-lab
    VERDICT. There is NO randomness and NO wall-clock here on purpose: the numbers
    are hand-entered min/typical/max ranges pulled from the research pass, summed
    arithmetically. Real devices vary with OS scheduling, RF congestion, peripheral
    latency settings, and receiver frame pacing. Treat the output as a budget to
    reason with and a target to MEASURE against on-device, not a guarantee.

ASSUMPTIONS (each disclosed; change them and re-run):
  A1. Touch sampling on a 120 Hz screen. One 120 Hz period = 1000/120 = 8.33 ms.
      A press lands uniformly within a period, so touch->sample latency is
      0 ms (best) .. ~4.2 ms (typical, half a period) .. 8.3 ms (worst, full period).
  A2. App wake + HID-report assembly is a small software constant. No primary
      figure was found, so this is a DISCLOSED ASSUMPTION: 0.5 / 1.0 / 2.0 ms.
  A3. Bluetooth transport, two profiles:
        - Classic BT HID: ~10-32 ms polling band (research: consumer explainer,
          order-of-magnitude only, PARTLY UNVERIFIED). min 10 / typ 21 / max 32.
        - BLE HID (HOGP): 7.5 ms is the BLE minimum connection interval (the spec
          floor before Bluetooth 6.2). Effective latency is usually worse than the
          raw interval, so typ ~= 2 intervals and max ~= 4 intervals: 7.5/15/30 ms.
  A4. Receiver input stack + display render. One 60 Hz frame = 16.7 ms; one 120 Hz
      frame = 8.3 ms. Best case a 120 Hz receiver renders in one frame (8.3), typical
      a 60 Hz receiver in one frame (16.7), worst case two 60 Hz frames (33.3).

SOURCE FIGURES (see ideas/product-forge/bt-controller-plan.md for full citations):
  - 120 Hz period 8.33 ms, 60 Hz frame 16.7 ms  : arithmetic (1000/Hz).
  - Classic BT HID ~10-32 ms                     : consumer explainer, order-of-mag.
  - BLE min connection interval 7.5 ms (~133 Hz) : Novel Bits / Nordic engineering.

REACTION / ACTION WINDOWS classified against:
  - media / remote      : no hard real-time window (a remote press has slack).
  - casual gaming       : ~100 ms is comfortable.
  - action gaming       : ~50 ms is the felt-responsive target.
  - competitive/frame-perfect : ~16 ms (one 60 Hz frame) is the strict budget.

CLASSIFICATION RULE (per transport total [min,typ,max] vs window W):
  PASS     if W >= max        (even the worst-case total fits the window)
  MARGINAL if min <= W < max  (the window lands inside the plausible range)
  FAIL     if W < min         (even the best case overruns the window)
"""

# ---- components: name -> (min_ms, typ_ms, max_ms, source/assumption note) ----
TOUCH = (0.0, 4.2, 8.3, "120 Hz sampling, 0..full-period (A1)")
ASSEMBLY = (0.5, 1.0, 2.0, "app wake + HID report assembly, DISCLOSED ASSUMPTION (A2)")
RENDER = (8.3, 16.7, 33.3, "receiver stack+render: 120Hz 1f / 60Hz 1f / 60Hz 2f (A4)")

TRANSPORTS = {
    "Classic BT HID": (10.0, 21.0, 32.0, "~10-32 ms polling band (A3, order-of-mag)"),
    "BLE HID (HOGP)": (7.5, 15.0, 30.0, "7.5 ms min conn interval, 1..4 intervals (A3)"),
}

# ---- reaction/action windows (ms); None = no hard real-time window ----
WINDOWS = [
    ("media / remote", None),
    ("casual gaming", 100.0),
    ("action gaming", 50.0),
    ("competitive/frame-perfect", 16.0),
]


def _sum3(*triples):
    """Sum the (min, typ, max) legs of each component triple."""
    lo = sum(t[0] for t in triples)
    ty = sum(t[1] for t in triples)
    hi = sum(t[2] for t in triples)
    return round(lo, 1), round(ty, 1), round(hi, 1)


def classify(total, window):
    lo, _ty, hi = total
    if window is None:
        return "PASS"          # no hard real-time window
    if window >= hi:
        return "PASS"
    if lo <= window < hi:
        return "MARGINAL"
    return "FAIL"              # window < min: even best case overruns


def main():
    print("=" * 78)
    print("END-TO-END INPUT-LATENCY BUDGET - phone-as-Bluetooth-controller")
    print("Illustrative DETERMINISTIC budget (no RNG, no wall-clock). NOT a measured")
    print("sim-lab VERDICT. Recommend on-device measurement before quoting a number.")
    print("=" * 78)

    print("\nFIXED COMPONENTS (shared across transports)   min /  typ /  max  (ms)")
    print("-" * 78)
    for name, comp in (("touch sampling", TOUCH),
                       ("app + HID report assembly", ASSEMBLY),
                       ("receiver input stack + render", RENDER)):
        print(f"  {name:<32} {comp[0]:>5} / {comp[1]:>5} / {comp[2]:>5}   {comp[3]}")

    print("\nTRANSPORT STAGE                               min /  typ /  max  (ms)")
    print("-" * 78)
    for name, comp in TRANSPORTS.items():
        print(f"  {name:<32} {comp[0]:>5} / {comp[1]:>5} / {comp[2]:>5}   {comp[3]}")

    # ---- totals per transport ----
    totals = {}
    for name, tcomp in TRANSPORTS.items():
        totals[name] = _sum3(TOUCH, ASSEMBLY, tcomp, RENDER)

    print("\nEND-TO-END TOTAL per transport (touch + assembly + transport + render)")
    print("-" * 78)
    print(f"  {'transport':<20} {'min':>7} {'typ':>7} {'max':>7}   (ms)")
    for name, tot in totals.items():
        print(f"  {name:<20} {tot[0]:>7} {tot[1]:>7} {tot[2]:>7}")

    # ---- classification table ----
    # short column headers so nothing runs together
    short = [("media", None), ("casual", 100.0), ("action", 50.0), ("compet.", 16.0)]
    print("\nCLASSIFICATION  (PASS = worst-case fits | MARGINAL = window inside range |")
    print("                 FAIL = even best case overruns)")
    print("  cols: media=no hard window  casual~100ms  action~50ms  compet.~16ms")
    print("-" * 78)
    print(f"  {'transport':<20}" + "".join(f"{lab:>12}" for lab, _ in short))
    for name, tot in totals.items():
        row = f"  {name:<20}" + "".join(f"{classify(tot, w):>12}" for _, w in short)
        print(row)

    print("\nWINDOWS: media/remote = no hard window; casual ~100 ms; action ~50 ms;")
    print("         competitive/frame-perfect ~16 ms (one 60 Hz frame).")
    print("\nVERDICT LINES:")
    for name, tot in totals.items():
        verdicts = [f"{lab}={classify(tot, w)}" for lab, w in WINDOWS]
        print(f"  {name}: total {tot[0]}/{tot[1]}/{tot[2]} ms  ->  " + ", ".join(verdicts))
    print("\nBoth transports: comfortable for media/remote and casual play, MARGINAL for")
    print("action gaming, and FAIL the ~16 ms competitive/frame-perfect budget. Measure")
    print("on real hardware before making any latency claim.")


if __name__ == "__main__":
    main()
