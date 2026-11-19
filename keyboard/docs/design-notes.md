# Design notes: keyboard

## Decisions

**One slab, nothing attached.** The whole point is to carry one thing. Earlier versions clipped a "spine" module onto the back edge; that made the keyboard deeper and less free to move. Now the battery and radio are built in, modules sit flush underneath, and compute moved to a separate product, the [Spine](../../spine/), on a cable.

**Laptop layout, trackpad below the keys.** The feel of a thin laptop deck: keys and trackpad at one height, trackpad centred under the thumbs, wrists on the palm rest.

**Trackpad size: 140 × 90 mm (standard).** A full standalone desktop trackpad (about 160 × 115 mm) made the keyboard too deep to carry; a small laptop trackpad (about 120 × 80 mm) felt cramped for gestures. 140 × 90 mm is in between.

**Swappable palm rest.** Big hands brush the trackpad while typing; sweat corrodes aluminium and wears out palm rests. Making the front 99 mm a separate part solves both: choose a different trackpad position or material, and replace it when it wears.

**Modules underneath, not outside.** The thickest part of the wedge is under the back rows of keys, which is where the 4 mm bays go. The keyboard's outline never changes.

**Square fingerprint key.** Flush, opaque, the same size as the function keys: calmer than a round glass sensor with a ring.

**Matches a Mac mini.** Silver bead-blasted aluminium and soft corners.

## Known limits

- **Touch ID** is only available on Apple's own keyboards. A third-party fingerprint key can't unlock a Mac or approve Apple Pay. It works with hosts that accept an external reader, and maps to lock screen elsewhere.
- **Trackpad gestures on macOS:** full gesture support is for Apple trackpads; third-party trackpads usually get pointer and scroll only, unless extra software is used.
- **Haptic glass trackpads** aren't easy to buy as standalone parts. Prototypes will likely use a mechanical click.
- **Thickness:** 11 mm at the back is tight for switches, battery, controller and 4 mm bays together. A real build may need 12–13 mm at the back.
- **Weight target (under 500 g)** is a goal, not a measured figure.

## Open questions

- ISO/UK and other regional layouts? (The layout data is easy to extend.)
- A numeric-keypad fascia?
- Should the bay connector carry USB 3?
