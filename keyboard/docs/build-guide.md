# Build guide: prototype the Deck One keyboard

A starting point for a working prototype, not a finished bill of materials. Pick parts that fit the drawings, and please share what you learn.

## 1. Print the templates

Print [`../drawings/top-view-standard.svg`](../drawings/top-view-standard.svg) and [`../drawings/underside.svg`](../drawings/underside.svg) at **100 % scale** (no "fit to page"). Check the 304 mm line with a ruler. Lay your keyboard parts, trackpad and battery on them to confirm the fit before you cut or print anything.

## 2. Keyboard

- **Switches:** low-profile mechanical switches (for example Kailh Choc) are the easiest way to stay thin. Scissor switches feel closer to a laptop but are harder to buy as separate parts.
- **Pitch:** the layout uses a 19.0 mm pitch. Choc-spaced boards are often 18 mm: change `PITCH` in `tools/generate_drawings.py` and regenerate to match your parts.
- **PCB:** design it from `data/keyboard-layout.json` (every key's position and size in mm).
- **Keycaps:** low-profile PBT caps; legends per [keyboard-layout.md](keyboard-layout.md).
- **Sweat protection:** conformal-coat the finished PCB and add a thin silicone or TPU membrane between the plate and the caps.

## 3. Controller, battery and firmware

| Goal | Board | Firmware |
|---|---|---|
| Bluetooth + USB | nRF52840-based board | [ZMK](https://zmk.dev) |
| USB only | RP2040-based board | [QMK](https://qmk.fm) |

- Use a flat LiPo pouch cell with its own protection circuit, sized to fit the 260 × 48 × 3.5 mm space under the keys.
- Map the function row to the actions in [keyboard-layout.md](keyboard-layout.md) and add **fn + esc** as a trackpad lock.
- Never leave a prototype battery charging unattended.

## 4. Trackpad and fascia

- Look for an **I²C HID precision-touchpad module**: about 140 × 90 mm for the standard fascia, 120 × 76 mm for the big-hands fascia.
- Build the fascia as a separate part (front 99 mm). Join it to the frame with two latches or screws underneath, and route the trackpad cable through a small connector at the seam.
- Add typing-aware palm rejection in firmware: ignore trackpad touches for about 250 ms after each keystroke.

## 5. Underside bays

- Leave two 120 × 50 × 4 mm pockets in the base (see [underside-modules.md](underside-modules.md)).
- Fit six spring-loaded pogo pins at the back edge of each pocket, wired to an internal USB hub chip.
- Magnets in the corners hold the covers flush.

## 6. Case

- **3D print:** split the 304 mm frame into two parts with alignment pins if your printer bed is small. Print the fascia separately.
- **CNC aluminium:** mill the frame from the SVG outlines. Make the fascia in aluminium, or cut it from glass or polymer.
- Keep the wedge: 4.5 mm at the front, 7.4 mm at the seam, 11 mm at the back.

## 7. Share it

Add photos, CAD, PCB files and firmware configs with a pull request, or open an issue describing your build.
