# Design notes

## Decisions

**Laptop layout, not desktop layout.** The goal is the feel of a thin laptop deck: the keyboard and trackpad at one height, the trackpad centred under the thumbs, and wrists on aluminium either side. A trackpad beside the keyboard makes you reach; a trackpad below it doesn't.

**Trackpad size: 140 × 90 mm.** A full standalone desktop trackpad (about 160 × 115 mm) made the deck too deep to carry. A small laptop trackpad (about 120 × 80 mm) felt cramped for four-finger gestures. 140 × 90 mm is in between: comfortable for gestures and long drags while keeping the deck at 221 mm deep.

**Square fingerprint key.** A flush, opaque key the same size as the function keys, rather than a round glass sensor with a ring. It looks calmer and doesn't break the row.

**Modular spine instead of a built-in battery.** Putting the battery and radio in a clip-on spine keeps the deck itself thin and light, lets builders choose wired or wireless, and opens the door to the compute spine.

**Matches a Mac mini.** Silver bead-blasted aluminium and soft corners, so the two look like a set on the desk.

## Known limits

- **Touch ID** is only available on Apple's own keyboards. A third-party fingerprint key can't unlock a Mac or approve Apple Pay. Design response: the key works with hosts that support external readers, and maps to lock screen elsewhere.
- **Trackpad gestures on macOS:** macOS gives full gesture support to Apple trackpads. Third-party trackpads usually get pointer and scroll only, unless extra software is used.
- **Haptic glass trackpads** aren't easy to buy as standalone parts. Prototypes will likely use a mechanical click.
- **Compute spine heat:** a Raspberry Pi 5 under load needs cooling. The vented lid is passive; heavy workloads may need a small fan or the official active cooler, which needs headroom inside the 26 mm spine.
- **Weight target (under 500 g)** is a goal, not a measured figure.

## Open questions

- Should the spine connector carry USB 3 for the hub and compute use cases?
- Is there demand for ISO/UK and other regional layouts? (The layout data is easy to extend.)
- A numeric keypad module on the side?

## Prior art and inspiration

- Thin laptop keyboard decks
- Keyboard computers such as the Raspberry Pi 400 and 500
- Open keyboard firmware projects: ZMK and QMK
