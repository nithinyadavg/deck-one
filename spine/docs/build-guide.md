# Build guide: prototype the Spine

## 1. Print the template

Print [`../drawings/top-view-internal.svg`](../drawings/top-view-internal.svg) at **100 % scale** and check the 127 mm lines with a ruler. Lay your board, M.2 adapter and power parts on it before cutting or printing.

## 2. Enclosure

- **3D print** a 127 × 127 × 30 mm box with 3.5 mm walls and 14 mm corner radius, plus a separate vented lid.
- Or **CNC** it from aluminium for the finished look and better heat spreading.
- Leave the rear wall open for a separate I/O plate held by two screws.

## 3. Compute board

- Fit four M2.5 standoffs on a 58 × 49 mm rectangle, 8 mm in from the rear-left inner corner (see [spec.md](spec.md)).
- A Raspberry Pi 5 with an M.2 adapter can use the storage slot; check that the adapter's height fits under the lid.
- Plan cooling: an active cooler or the 40 mm lid fan for sustained load.

## 4. Power

- Use a USB-C PD trigger or controller board set to 9 V or 12 V, followed by a buck converter rated for **5.1 V at 5 A**.
- Feed the board, the hub and the keyboard port from it.
- Check polarity and voltage with a meter before connecting the board.

## 5. Hub and ports

- A small USB hub board connects the keyboard's USB-C port and the rear USB-A ports to the compute board.
- Run short internal cables or adapters from the board's display and Ethernet ports to the rear plate.

## 6. I/O plate

- Cut the plate from 1.5 mm aluminium or print it, using [`../drawings/rear-io.svg`](../drawings/rear-io.svg) as the default layout.
- If your board's ports are elsewhere, draw a new plate and add it to the repo.

## 7. Share it

Photos, CAD files and plate designs are welcome as pull requests.
