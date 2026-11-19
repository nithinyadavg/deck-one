# Deck One

**An open-source concept for a laptop-style keyboard you can take anywhere, plus a separate hub that holds the computer.**

![Deck One keyboard, top view](keyboard/images/top-view-standard.png)

Deck One is two products that work together, each in its own folder with its own drawings, specs and modules:

| | What it is | Folder |
|---|---|---|
| **Deck One keyboard** | One slim slab: the thin-laptop keyboard and a trackpad, with its own battery. Modules slide into flush bays **underneath**, and the palm rest is **swappable** for big or sweaty hands. Nothing attaches to the outside. | [`keyboard/`](keyboard/) |
| **Deck One Spine** | A separate Mac mini-size box (127 × 127 × 30 mm) holding the compute board, storage and ports. Joined to the keyboard by **one USB-C cable**, or by Bluetooth. | [`spine/`](spine/) |

```
 Deck One keyboard  ── USB-C cable or Bluetooth ──  Spine  ── HDMI ──  Display
 (anywhere: desk, lap, sofa)                        (on the desk, or under a Mac mini)
```

The keyboard works on its own with any computer: a Mac mini, a laptop, an iPad, a PC or a single-board computer. The Spine is optional.

> **Status:** design concept, free for anyone to build, fork, copy or improve. No product exists yet. All measurements are design targets.

## Why

- **One thing to carry.** Keyboard and trackpad in one slab, with its own battery: no second device, no attached boxes.
- **Laptop comfort without the laptop.** Trackpad centred under your thumbs, wrists on the palm rest, everything at one height.
- **Real hands are different.** Big hands keep brushing laptop trackpads, and sweat corrodes aluminium palm rests and wears out keyboards. Deck One's palm rest is a separate part you choose and replace.
- **Builders deserve better than a cable mess.** The Spine gives a Raspberry Pi-size board a proper home: storage, ports, power and cooling in one tidy box.

## Keyboard at a glance

- Thin-laptop US layout: half-height function row, inverted-T arrows, a square flush fingerprint key
- 304 × 221 mm, 4.5 mm at the front rising to 11 mm at the back
- Built-in battery, Bluetooth to 3 devices, USB-C
- **Two flush underside bays** (120 × 50 × 4 mm) for an extra battery, a 2.4 GHz receiver, a security key or your own module
- **Three palm rests:** standard (140 × 90 mm trackpad), big hands (smaller, lower trackpad behind a thumb ridge), or plain wrist rest
- **Three palm-rest materials:** aluminium, glass or soft-touch polymer

→ [keyboard/README.md](keyboard/README.md)

## Spine at a glance

- 127 × 127 × 30 mm, same footprint as a Mac mini
- Bay for an 85 × 56 mm single-board computer, M.2 NVMe slot, USB-C PD power, swappable rear I/O plate
- Two modes: **Compute** (the Spine is the computer) or **Dock** (a USB-C dock and fast drive for a Mac mini or laptop)

→ [spine/README.md](spine/README.md)

## Repository layout

```
keyboard/      the keyboard: drawings, layout data, spec, modules, build guide
spine/         the hub: drawings, spec, modules, build guide
design-canvas/ source of the original interactive design boards
LICENSE        MIT
CONTRIBUTING.md
```

Each folder has a `tools/generate_drawings.py` that redraws its SVGs from one set of numbers.

## Licence

MIT: use, copy, modify, build and sell it, as long as the licence and credit stay with it. See [`LICENSE`](LICENSE).

## Credit

Concept and design by **Nithin Yadav Gopinath** ([@nithinyadavg](https://github.com/nithinyadavg) · [nithinyadavg.me](https://nithinyadavg.me)).

*Mac, Mac mini, Touch ID and iPad are trademarks of Apple Inc. Raspberry Pi is a trademark of Raspberry Pi Ltd. They are mentioned only to describe compatibility. This project is not affiliated with or endorsed by either company.*
