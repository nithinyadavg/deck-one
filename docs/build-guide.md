# Build guide: prototype Deck One

A starting point for a working prototype, not a finished bill of materials. The production target is a 5 mm slab; a first prototype from off-the-shelf parts will be thicker, which is fine for proving the layout, the trackpad position and the firmware.

## 1. Print the templates

Print [`../drawings/top-view-standard.svg`](../drawings/top-view-standard.svg) and [`../drawings/underside.svg`](../drawings/underside.svg) at **100 % scale** (no "fit to page"). Check the 304 mm line with a ruler. Lay your keyboard parts, trackpad and battery cells on them before you cut or print anything.

## 2. Keyboard

- **Switches:** low-profile mechanical switches (for example Kailh Choc) are the easiest way to start. Expect a slab of about 10–15 mm. Scissor mechanisms get closer to 5 mm but are hard to buy as separate parts.
- **Pitch:** the layout uses a 19.0 mm pitch. Choc-spaced boards are often 18 mm: change `PITCH` in `tools/generate_drawings.py` and regenerate to match your parts.
- **PCB:** design it from `data/keyboard-layout.json` (every key's position and size in mm).
- **Keycaps:** low-profile PBT caps; legends per [keyboard-layout.md](keyboard-layout.md).
- **Sweat protection:** conformal-coat the PCB and add a thin silicone or TPU membrane between the plate and the caps.

## 3. Controller, battery and firmware

- **Controller:** an nRF52840-based board for Bluetooth + USB.
- **Firmware:** [ZMK](https://zmk.dev). Map the function row to the actions in [keyboard-layout.md](keyboard-layout.md), add **fn + esc** as a trackpad lock and **fn + 1/2/3** for Bluetooth devices.
- **Battery:** two flat LiPo pouch cells with protection circuits, sized for the 66 × 80 mm spaces either side of the trackpad, wired in parallel through a single charge controller. Never leave a prototype charging unattended.

## 4. Trackpad and palm rest

- Look for an **I²C HID precision-touchpad module**: about 140 × 90 mm for the standard plate, 120 × 76 mm for the big-hands plate.
- Make the palm rest a separate top plate (front 99 mm), held by two latches or screws underneath, with a small connector for the trackpad at the seam.
- Add typing-aware palm rejection: ignore trackpad touches for about 250 ms after each keystroke.

## 5. Case

- **3D print:** split the base into two parts with alignment pins if your printer bed is small. Print the palm-rest plate separately.
- **CNC aluminium:** mill the base from the SVG outlines. Cut the palm-rest plate from aluminium, glass or polymer.
- Four rubber feet, so it doesn't slide when you click the trackpad.

## 6. Share it

Add photos, CAD, PCB files and firmware configs with a pull request, or open an issue describing your build.
