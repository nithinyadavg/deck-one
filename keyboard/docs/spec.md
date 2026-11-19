# Deck One keyboard: specification

All values are design targets in millimetres unless stated.

## Overall

| Item | Value |
|---|---|
| Size | 304 × 221 mm |
| Thickness | 4.5 mm at the front, 7.4 mm at the fascia seam, 11 mm at the back |
| Corner radius (top view) | 7.3 mm |
| Construction | two parts: keyboard frame (back 122 mm) + swappable front fascia (front 99 mm), joined by two release latches underneath |
| Weight target | under 500 g with the standard aluminium fascia and empty bays |
| Frame material | aluminium, bead-blasted |
| Finishes | Silver (to sit with a Mac mini), Space Black, Space Grey, Gold |
| Feet | four rubber feet, so it doesn't slide when the trackpad is clicked |

## Power and connection

| Item | Value |
|---|---|
| Battery | built in, inside the frame under the keys (about 260 × 48 × 3.5 mm) |
| Wireless | Bluetooth LE, up to 3 devices, host switching from the keyboard |
| Wired | USB-C on the back edge: data and charging |
| Power switch | back edge, left |
| Works with | Mac mini and other Macs, iPad, Windows, Linux, single-board computers, the Deck One Spine |

## Keyboard

| Item | Value |
|---|---|
| Layout | thin-laptop US layout, 78 keys ([keyboard-layout.md](keyboard-layout.md)) |
| Key pitch | 19.0 mm |
| Gap between caps | 2.4 mm |
| Main keycap | 16.6 × 16.6 mm |
| Function row | 14 equal keys, 17.28 × 9.0 mm |
| Arrows | inverted T; up/down 16.6 × 7.7 mm, left/right full width, half height |
| Key block | 273.1 × 104.0 mm, in a 278.5 × 109.4 mm well, 10 mm from the back edge |
| Switches | low-travel scissor (production) or low-profile mechanical (prototype) |
| Keycaps | PBT, black with white legends |
| Under the keys | sealed membrane layer against sweat and spills; conformal-coated circuit board |
| Fingerprint key | top right, square, flush and opaque, same size as the F-keys |
| Trackpad lock | fn + esc, with an indicator light |

## Front fascia (palm rest)

| Option | Trackpad | Distance from keys | Extra |
|---|---|---|---|
| Standard | 140 × 90 mm | 5.3 mm | — |
| Big hands | 120 × 76 mm | 18.6 mm | 1 mm high, 3 mm wide thumb ridge, 160 mm long |
| Wrist rest | none | — | plain palm rest |

Materials: aluminium (hard-anodised, sealed), glass (one sheet across the palm rest, trackpad included), or soft-touch polymer. Details in [fascia.md](fascia.md).

## Underside module bays

| Item | Value |
|---|---|
| Bays | 2 (A and B), under the back of the keyboard |
| Size | 120 × 50 × 4 mm each |
| Cover | flush, magnetic |
| Connector | 6 pogo pins: VBUS, GND, USB D+, USB D−, ID, spare |

Details in [underside-modules.md](underside-modules.md).

## Trackpad

| Item | Value |
|---|---|
| Surface | glass |
| Click | haptic (production target) or mechanical (prototype) |
| Protocol | standard HID multi-touch (Windows Precision Touchpad compatible) |
| Palm handling | palm rejection, plus a short pause after each keystroke (default 250 ms, adjustable) |
