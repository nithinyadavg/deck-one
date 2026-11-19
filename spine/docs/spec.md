# Deck One Spine: specification

All values are design targets in millimetres unless stated.

## Enclosure

| Item | Value |
|---|---|
| Size | 127 × 127 × 30 mm (footprint matches a Mac mini) |
| Corner radius | 14 mm |
| Wall | 3.5 mm |
| Material | aluminium, bead-blasted; Silver or Space Black |
| Lid | removable, vented, with mounting for an optional 40 mm fan |
| Front | status light |
| Rear | swappable I/O plate, 127 × 30 mm |

## Internal layout (lid off, rear at top)

Drawing: [`../drawings/top-view-internal.svg`](../drawings/top-view-internal.svg)

| Part | Position (x, y from rear-left inner corner) | Size |
|---|---|---|
| Compute board bay | 8, 8 | 85 × 56 mm, M2.5 holes on 58 × 49 mm, 3.5 mm from the board edges |
| Optional fan | centred over the board, in the lid | 40 mm |
| M.2 slot | 99, 8 | 22 × 80 mm (2230–2280) |
| Power board | 8, 92 | 40 × 25 mm |
| USB hub board | 52, 96 | 42 × 21 mm |

## Power

| Item | Value |
|---|---|
| Input | USB-C Power Delivery, up to 45 W |
| Output to the board | 5.1 V, up to 5 A (what a Raspberry Pi 5 needs for full USB power) |
| Keyboard | charged over its USB-C cable from the Spine |

## Default rear I/O

Drawing: [`../drawings/rear-io.svg`](../drawings/rear-io.svg)

| Port | Purpose |
|---|---|
| USB-C | power in |
| USB-C | to the Deck One keyboard (data + charging) |
| USB-A ×2 | accessories |
| HDMI | display (from the board, via an adapter where the board uses micro-HDMI) |
| Ethernet | network |
| Vent | airflow |

The plate is a separate part: cut a new one to match a different board.

## Connection to the keyboard

| Item | Value |
|---|---|
| Wired | one USB-C cable: keyboard and trackpad data one way, charging the other |
| Wireless | the keyboard can pair with the board over Bluetooth instead |
