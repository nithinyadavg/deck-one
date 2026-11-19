# Keyboard layout

The thin-laptop US layout. Every row is **14.5 units** wide; 1 unit = 19.0 mm pitch.
Exact positions of all 78 keys are in [`../data/keyboard-layout.json`](../data/keyboard-layout.json) and [`../data/keyboard-layout.csv`](../data/keyboard-layout.csv), measured in mm from the top-left of the key block.

## Rows

| Row | Keys (width in units) |
|---|---|
| 0 · function (half height) | esc, F1–F12, fingerprint: 14 equal keys filling the row (≈ 1.04 u each) |
| 1 · numbers | `` ` `` 1 2 3 4 5 6 7 8 9 0 - = (1 u each), **delete 1.5 u** |
| 2 · top letters | **tab 1.5 u**, Q W E R T Y U I O P [ ] \ (1 u each) |
| 3 · home | **caps lock 1.75 u**, A S D F G H J K L ; ' (1 u each), **return 1.75 u** |
| 4 · bottom letters | **shift 2.25 u**, Z X C V B N M , . / (1 u each), **shift 2.25 u** |
| 5 · modifiers | fn 1 u, control 1 u, option 1 u, command 1.25 u, **space 5 u**, command 1.25 u, option 1 u, arrows 3 u |

The arrow cluster is an inverted T: left and right are full 1 u wide and half height; up and down share one 1 u column, half height each.

## Function row

| Key | Legend icon | Default action |
|---|---|---|
| esc | — | escape |
| F1 | small sun | display brightness down |
| F2 | large sun | display brightness up |
| F3 | three windows | Mission Control / overview |
| F4 | grid | Launchpad / app launcher |
| F5 | small dotted arc | keyboard backlight down |
| F6 | large dotted arc | keyboard backlight up |
| F7 | ◀◀ | previous track |
| F8 | ▶ ❙❙ | play / pause |
| F9 | ▶▶ | next track |
| F10 | speaker | mute |
| F11 | speaker, one wave | volume down |
| F12 | speaker, three waves | volume up |
| top right | none | fingerprint reader, or lock/power where no reader is fitted |

## fn combinations

| Combination | Action |
|---|---|
| fn + esc | lock / unlock the trackpad (indicator light on while locked) |
| fn + 1 / 2 / 3 | switch between the three paired Bluetooth devices |
| fn + F1–F12 | standard F1–F12 instead of the media actions (or the other way round, set in firmware) |

## Legends

- Letters: one centred legend.
- Number and symbol keys: shifted symbol on top, unshifted below, both centred.
- Left modifiers: symbol top-right, word bottom-right. Right modifiers: symbol top-left, word bottom-left.
- tab, caps lock, left shift, fn: word bottom-left. delete, return, right shift: word bottom-right.
- caps lock has a small status light at the top left.
