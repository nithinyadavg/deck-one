# Contributing to Deck One

Thanks for helping. Anything that moves the concept towards a real build is welcome, for either product:

**Keyboard (`keyboard/`)**
- CAD of the frame and fascias (STEP, STL, Fusion, FreeCAD, OnShape links)
- Keyboard PCB designs (KiCad preferred)
- ZMK / QMK configurations
- Underside modules: battery cassettes, radios, maker modules
- New fascias: different trackpads, materials, a numeric keypad
- Trackpad module findings: what fits, what works on which OS

**Spine (`spine/`)**
- Enclosure CAD and I/O plates for specific boards
- Power and hub board designs
- Cooling tests

## How

1. Open an issue to describe the idea or the problem.
2. Fork the repo, make your change on a branch, and open a pull request.
3. If you change dimensions, edit the constants in that folder's `tools/generate_drawings.py`, run it from that folder, and commit the regenerated files.

## Ground rules

- Keep it open: contributions are released under the repository's MIT licence.
- Underside modules: use a unique ID resistor value and list it in your pull request.
- Be kind and specific in issues and reviews.
- Don't add other companies' logos or artwork to the designs.
