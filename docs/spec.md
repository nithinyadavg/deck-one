# Deck One: specification

All values are design targets in millimetres unless stated.

## Overall

| Item | Value |
|---|---|
| Size | 304 × 221 mm |
| Thickness | 5 mm, flat end to end (about an iPhone Fold opened out) |
| Corner radius (top view) | 7.3 mm |
| Construction | one-piece aluminium base; separate palm-rest top plate (front 99 mm), held by two release latches underneath |
| Weight target | as light as the materials allow; to be confirmed by a prototype |
| Finishes | Silver (to sit with a Mac mini), Space Black; others possible |
| Feet | four low rubber feet, so it doesn't slide when the trackpad is clicked |

## Power and connection

| Item | Value |
|---|---|
| Battery | built in: two flat cells, about 66 × 80 × 3 mm each, under the palm rest either side of the trackpad |
| Wireless | Bluetooth LE, up to 3 devices (fn + 1/2/3 to switch) |
| Wired | USB-C on the back edge: data and charging |
| Power switch | back edge |
| Firmware | open source, [ZMK](https://zmk.dev) |
| Works with | Mac mini and other Macs, iPad, Windows, Linux, single-board computers |

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
| Switches | very low-profile scissor mechanism |
| Keycaps | PBT, black with white legends |
| Under the keys | sealed membrane against sweat and spills; conformal-coated circuit board |
| Fingerprint key | top right; square, flush and opaque, same size as the F-keys |
| Trackpad lock | fn + esc, with an indicator light |

## Trackpad

| Item | Value |
|---|---|
| Size | 140 × 90 mm (standard palm rest) |
| Position | centred, 5.3 mm below the keyboard well |
| Surface | glass |
| Click | haptic (production target) or mechanical (prototype) |
| Protocol | standard HID multi-touch (Windows Precision Touchpad compatible) |
| Palm handling | palm rejection, plus a short pause after each keystroke (default 250 ms, adjustable) |

## Palm rest (optional swap)

| Option | Trackpad | Distance from keys | Extra |
|---|---|---|---|
| Standard | 140 × 90 mm | 5.3 mm | — |
| Big hands | 120 × 76 mm | 18.6 mm | 1 mm high thumb ridge, 160 mm long |
| Wrist rest | none | — | plain palm rest |

Materials: aluminium (hard-anodised, sealed), glass, or soft-touch polymer. Details in [fascia.md](fascia.md).
