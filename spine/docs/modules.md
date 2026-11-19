# Spine modules

Everything inside the Spine is replaceable. The enclosure, power board and hub board stay; the rest changes with what you want the Spine to be.

## Compute module

- A single-board computer in the 85 × 56 mm bay (Raspberry Pi 4/5 size and similar boards with the standard 58 × 49 mm mounting pattern).
- The Deck One keyboard connects to it through the hub board over USB, so no drivers or wiring beyond one cable.
- Plug a display into the rear HDMI and the Spine is a full computer.
- **RAM** comes with the board. To get more, fit a board with more.
- Cooling: passive through the vented lid for light use; add the 40 mm fan or a low-profile heatsink for sustained load.

## Dock module

- No computer inside. A dock board takes the place of the compute board.
- Connects to a Mac mini or laptop over USB-C and gives it the rear ports.
- The M.2 slot becomes a fast external NVMe drive through a USB-to-NVMe bridge.
- The Deck One keyboard can plug into the Spine and reach the Mac through it.

## Storage

- One M.2 slot, 22 mm wide, 30 to 80 mm long (2230, 2242, 2260, 2280).
- In Compute mode it needs a board with a PCIe connection; in Dock mode it runs through the dock's bridge.

## Rear I/O plate

- 127 × 30 mm, held by two screws.
- The default plate fits the ports listed in [spec.md](spec.md).
- Different boards put their ports in different places: cut a new plate (laser-cut aluminium, or 3D-printed) and share the file.

## Ideas

- A **storage-only** module with two M.2 slots for a small network drive.
- A **radio** module (LoRa, SDR) for maker projects.
- A **battery** base so the Spine runs away from a wall socket.
