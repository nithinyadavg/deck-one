# Contributing to Deck One

Thanks for helping. Anything that moves the concept towards a real build is welcome:

- CAD of the base and palm-rest plates (STEP, STL, Fusion, FreeCAD, OnShape links)
- Keyboard PCB designs (KiCad preferred)
- ZMK configurations
- New palm-rest plates: trackpad sizes, materials, a numeric keypad
- Trackpad module findings: what fits, what works on which OS
- Photos and notes from your prototype
- Corrections to the drawings or the specification

## How

1. Open an issue to describe the idea or the problem.
2. Fork the repo, make your change on a branch, and open a pull request.
3. If you change dimensions, edit the constants in `tools/generate_drawings.py`, run `python3 tools/generate_drawings.py` from the repo root, and commit the regenerated files.

## Ground rules

- Keep it open: contributions are released under the repository's MIT licence.
- Be kind and specific in issues and reviews.
- Don't add other companies' logos or artwork to the designs.
