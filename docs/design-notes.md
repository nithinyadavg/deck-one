# Design notes

## What Deck One is, and isn't

Deck One is a keyboard and trackpad in one slab, with a battery and a cable. It isn't a hub, a dock or a computer. Those already exist. The goal is the simplest, best version of one thing: the thin-laptop deck, on its own.

The approach follows what Framework did with its laptop input modules: take a proven layout, make it open, and make the parts that wear or differ between people swappable. No more modularity than that.

## Decisions

**Thin-laptop layout, key for key.** It's the layout people already know and like: half-height function row, inverted-T arrows, trackpad centred under the thumbs.

**5 mm flat slab.** About the thickness of an iPhone Fold opened out. Flat end to end rather than a wedge, so it slides into a bag beside a laptop or tablet and sits flat on a lap.

**Trackpad 140 × 90 mm.** A full standalone desktop trackpad (about 160 × 115 mm) made the slab too deep to carry. A small laptop trackpad (about 120 × 80 mm) felt cramped for gestures. 140 × 90 mm is in between.

**Battery under the palm rest.** At 5 mm there's no room under the keys, so two flat cells sit either side of the trackpad.

**Swappable palm rest, nothing else.** Big hands brush the trackpad while typing; sweat corrodes aluminium and wears palm rests out. A separate palm-rest plate fixes both: a different trackpad position or material, replaced when it wears.

**Square fingerprint key.** Flush, opaque, the same size as the function keys: calmer than a round glass sensor with a ring.

**Matches a Mac mini.** Silver bead-blasted aluminium and soft corners.

## Known limits

- **5 mm is a production target.** It needs very low-profile scissor keys, a thin trackpad module and thin cells, as in thin laptops. DIY prototypes with off-the-shelf parts will be thicker (about 10–15 mm).
- **Touch ID** is only available on Apple's own keyboards. A third-party fingerprint key can't unlock a Mac or approve Apple Pay. It works with computers that accept an external reader, and maps to lock screen elsewhere.
- **Trackpad gestures on macOS:** full gesture support is for Apple trackpads; third-party trackpads usually get pointer and scroll only, unless extra software is used.
- **Haptic glass trackpads** are hard to buy as standalone parts. Prototypes will likely use a mechanical click.
- **Battery size** is limited by the 3 mm cells; real battery life needs a prototype to measure.

## Open questions

- ISO/UK and other regional layouts? (The layout data is easy to extend.)
- A numeric-keypad palm-rest plate?
- A fold-out stand for a typing angle, given the slab is flat?
