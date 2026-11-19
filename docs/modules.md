# Modules: the spine system

The deck itself holds only the keyboard, the trackpad and their controller. Along its back edge is a full-width **magnetic connector** that carries power and USB. Whatever clips on there (the *spine*) decides how the deck connects and where its power comes from.

This keeps the deck thin and light, and means one deck can be a wireless Mac mini keyboard on Monday and a Raspberry Pi computer on Tuesday.

## Battery spine (in the box)

- 14 mm deep, 11 mm tall
- Built-in battery and Bluetooth LE radio
- Pairs with up to 3 hosts (for example a Mac mini, an iPad and a Pi) with a host-switch button
- USB-C port to charge; you can keep typing while it charges
- Status light: charging / connected / pairing

## Cable spine (lightest)

- 10 mm deep, 10 mm tall
- No battery and no radio, so nothing to charge and nothing to pair
- USB-C to the host
- USB-C pass-through for a drive, a security key or a dongle

## Compute spine (for builders)

- 66 mm deep, 26 mm tall
- Bay for an **85 × 56 mm** single-board computer: Raspberry Pi 4/5-size boards and similar SoC boards
- Standard mounting: 4 × M2.5 holes on a **58 × 49 mm** rectangle, 3.5 mm in from the board edges
- The deck's keyboard and trackpad connect to the board over **internal USB**, so no drivers or wiring beyond one cable
- **Swappable I/O plate** on the back, cut to match the board's ports (power, display, USB, Ethernet)
- Passive cooling through vent slots in the lid on both sides of the board; leave room for a low-profile heatsink
- Plug in a screen and power and the deck is the computer

## Connector (proposal)

| Pin group | Purpose |
|---|---|
| VBUS / GND | power in either direction (spine charges deck, or deck powers from host) |
| D+ / D− | USB 2.0 between deck controller and spine |
| ID | tells the deck which spine is attached |

Magnets in the deck's back edge and the spine align and hold it; pogo pins carry the signals. A future revision could carry USB 3 for faster pass-through.

## Ideas for more spines

- **Hub spine:** USB-C hub with card reader, for a Mac mini on a desk
- **Numeric spine:** a side-mounted numeric keypad (would attach at the right edge instead)
- **Stand spine:** taller back edge for a steeper typing angle
