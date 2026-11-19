# Build guide: prototype your own Deck One

This is a starting point for a working prototype, not a finished bill of materials. Pick parts that fit the drawings, and please share what you learn.

## 1. Print the templates

Print [`../drawings/top-view-battery.svg`](../drawings/top-view-battery.svg) at **100 % scale** (no "fit to page"). Check the 304 mm width line with a ruler. Lay your keyboard parts and trackpad module on it to confirm the fit before you cut or print anything.

## 2. Keyboard

- **Switches:** low-profile mechanical switches (for example Kailh Choc) are the easiest way to get a thin deck. Scissor switches are closer to a laptop feel but harder to source as separate parts.
- **Pitch:** the layout uses a 19.0 mm pitch. Choc-spaced boards are often 18 mm; adjust `PITCH` in `tools/generate_drawings.py` and regenerate the drawings to match the parts you choose.
- **PCB:** design it from `data/keyboard-layout.json` (every key's centre and size in mm). The JSON can be converted for tools like KiCad footprints or a keyboard layout editor.
- **Keycaps:** low-profile black caps; legends per [keyboard-layout.md](keyboard-layout.md).

## 3. Controller and firmware

| Goal | Board | Firmware |
|---|---|---|
| Wireless (battery spine) | nRF52840-based board | [ZMK](https://zmk.dev) |
| Wired only (cable or compute spine) | RP2040-based board | [QMK](https://qmk.fm) |

Map the function row to the actions in [keyboard-layout.md](keyboard-layout.md). Media keys work on all major operating systems as standard HID consumer keys.

## 4. Trackpad

- Look for an **I²C HID precision-touchpad module** close to 140 × 90 mm. Smaller is fine for a first prototype: centre it and keep the 140 × 90 opening for later.
- Connect it to the controller and pass it through to the host as a USB/Bluetooth HID multi-touch device, or as a separate USB device behind a small hub.
- On Windows and Linux, multi-touch gestures work natively. On macOS, expect pointer and scrolling; full gestures may need extra software.

## 5. Fingerprint key

Optional. A USB fingerprint module under the top-right cap works on hosts that support external readers (Windows Hello, Linux fprintd). On a Mac it can't act as Touch ID; map the key to lock screen instead.

## 6. Case

- **3D print:** split the 304 mm deck into two or three parts with alignment pins if your printer bed is small. Sand and paint for the aluminium look.
- **CNC aluminium:** mill the top case from the SVG outlines (keyboard well, trackpad opening, back edge). Use a thin bottom plate with four rubber feet.
- Keep the wedge: 4.5 mm at the front edge, 11 mm at the back. With low-profile switches the back may need to grow; the palm rest can stay thin.

## 7. Spines

- **Cable spine:** the simplest. A small enclosure with a USB-C breakout, joined to the deck with magnets and pogo pins (or just a short internal cable for a first build).
- **Battery spine:** a flat LiPo cell with a protection/charge circuit and USB-C charging. Follow the battery's safety ratings and never leave a prototype charging unattended.
- **Compute spine:** an enclosure with 4 × M2.5 standoffs on a 58 × 49 mm pattern, a cut-out back plate for the board's ports, and vent slots on both sides of the board.

## 8. Share it

Add photos, CAD files, PCB files and firmware configs to the repo with a pull request, or open an issue describing your build.
