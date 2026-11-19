# Deck One — specification

All values are design targets in millimetres unless stated.

## Overall

| Item | Value |
|---|---|
| Deck width | 304 mm |
| Deck depth | 221 mm (without spine) |
| Thickness | 4.5 mm at the front (palm rest) rising to 11 mm at the back |
| Corner radius (top view) | 7.3 mm |
| Depth with battery spine | ≈ 236 mm |
| Depth with cable spine | ≈ 232 mm |
| Depth with compute spine | ≈ 288 mm |
| Weight target | under 500 g with the battery spine |
| Material | aluminium top case, bead-blasted |
| Finishes | Silver (to match a Mac mini), Space Black |
| Feet | four low rubber feet, so the deck doesn't slide when the trackpad is clicked |

## Keyboard

| Item | Value |
|---|---|
| Layout | thin-laptop US layout, 78 keys (see [keyboard-layout.md](keyboard-layout.md)) |
| Key pitch (1 unit) | 19.0 mm |
| Gap between caps | 2.4 mm |
| Main keycap (1 unit) | 16.6 × 16.6 mm |
| Function row | 14 equal keys, 17.28 × 9.0 mm (half height) |
| Arrow keys | inverted T; up/down 16.6 × 7.7 mm each, left/right full width, half height |
| Key block | 273.1 × 104.0 mm |
| Keyboard well | 278.5 × 109.4 mm, 2.7 mm border, set 10 mm in from the back edge of the deck |
| Switches | low-travel scissor (production) or low-profile mechanical (prototype) |
| Keycaps | black with white legends |
| Fingerprint key | top right of the function row; square, flush, opaque, same size as the F-keys |

## Trackpad

| Item | Value |
|---|---|
| Size | 140 × 90 mm, corner radius 4 mm |
| Position | centred left-to-right, 5.3 mm below the keyboard well |
| Surface | glass |
| Click | haptic (production target) or mechanical diaphragm click (prototype) |
| Protocol | standard HID multi-touch (Windows Precision Touchpad compatible) |
| Palm rejection | along the keyboard edge and the palm rest sides |

## Connection and power

| Item | Value |
|---|---|
| Spine connector | magnetic, full width of the back edge; carries power and USB 2.0 |
| Wireless | Bluetooth LE, up to 3 hosts (battery spine) |
| Wired | USB-C (cable spine, or charging cable on the battery spine) |
| Battery | in the battery spine, so the deck itself stays thin and light |
| Works with | Mac mini and other Macs, iPad, Windows PCs, Linux, single-board computers |

## Spines

See [modules.md](modules.md) for details.

| Spine | Depth (top view) | Height | Ports |
|---|---|---|---|
| Battery | 14 mm | 11 mm | USB-C, host-switch button, status light |
| Cable | 10 mm | 10 mm | USB-C to host, USB-C pass-through |
| Compute | 66 mm | 26 mm | swappable I/O plate cut to the board |
