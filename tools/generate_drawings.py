#!/usr/bin/env python3
"""Generate Deck One's reference drawings and keyboard layout data.

Everything is in millimetres. Run from the repo root:

    python3 tools/generate_drawings.py

Outputs:
    data/keyboard-layout.json   every key's position and size (mm)
    data/keyboard-layout.csv    the same, as a table
    drawings/top-view-battery.svg
    drawings/top-view-cable.svg
    drawings/top-view-compute.svg
    drawings/side-profile.svg

The SVGs are drawn at true scale (1 SVG unit = 1 mm) with width/height in mm,
so printing them at 100 % gives a 1:1 paper template.
"""

import csv
import json
import os
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- dimensions
PITCH = 19.0          # key pitch, mm (1 unit)
GAP = 2.4             # gap between keycaps, mm
KEY_H = 16.6          # main-row keycap height
FN_H = 9.0            # half-height function row
ROW_UNITS = 14.5      # every row is 14.5 units wide
ROW_W = ROW_UNITS * PITCH - GAP              # 273.1 mm
FN_W = (ROW_W - 13 * GAP) / 14               # 14 equal function-row keys
ARROW_H = (KEY_H - 1.2) / 2                   # half-height arrow keys

WELL_PAD = 2.7
WELL_W = ROW_W + 2 * WELL_PAD                 # 278.5 mm
KEYS_H = FN_H + 5 * KEY_H + 5 * GAP           # 104.0 mm
WELL_H = KEYS_H + 2 * WELL_PAD                # 109.4 mm

DECK_W = 304.0
DECK_D = 221.0
DECK_R = 7.3
WELL_TOP = 10.0
PAD_W, PAD_H = 140.0, 90.0
PAD_TOP = WELL_TOP + WELL_H + 5.3             # trackpad starts here
FRONT_T, BACK_T = 4.5, 11.0                   # deck wedge thickness

SPINES = {
    # name: (depth in top view, height in side view, label)
    "battery": (14.0, 11.0, "Battery spine · Bluetooth, 3 hosts"),
    "cable":   (10.0, 10.0, "Cable spine · USB-C + pass-through"),
    "compute": (66.0, 26.0, "Compute spine · 85 × 56 mm board bay"),
}
BOARD_W, BOARD_D = 85.0, 56.0

# ---------------------------------------------------------------- key list
def key(label, units=1.0, align="c", top=None, kind="key", width=None):
    w = width if width is not None else units * PITCH - GAP
    return {"label": label, "units": units, "align": align, "top": top,
            "kind": kind, "w": round(w, 2)}


def letters(s):
    return [key(ch) for ch in s]


def pairs(items):
    return [key(low, 1, "c", high) for high, low in items]


FN_ICONS = ["brightness down", "brightness up", "mission control", "launchpad",
            "key light down", "key light up", "previous", "play/pause",
            "next", "mute", "volume down", "volume up"]

rows = []
fn_row = [key("esc", width=FN_W, align="ml")]
for i, icon in enumerate(FN_ICONS, start=1):
    k = key(f"F{i}", width=FN_W, kind="fn")
    k["icon"] = icon
    fn_row.append(k)
fn_row.append(key("", width=FN_W, kind="fingerprint"))
rows.append((FN_H, fn_row))

num = pairs([("~", "`"), ("!", "1"), ("@", "2"), ("#", "3"), ("$", "4"),
             ("%", "5"), ("^", "6"), ("&", "7"), ("*", "8"), ("(", "9"),
             (")", "0"), ("—", "–"), ("+", "=")])
num.append(key("delete", 1.5, "br"))
rows.append((KEY_H, num))

rows.append((KEY_H, [key("tab", 1.5, "bl")] + letters("QWERTYUIOP") +
             pairs([("{", "["), ("}", "]"), ("|", "\\")])))
rows.append((KEY_H, [key("caps lock", 1.75, "bl")] + letters("ASDFGHJKL") +
             pairs([(":", ";"), ('"', "'")]) + [key("return", 1.75, "br")]))
rows.append((KEY_H, [key("shift", 2.25, "bl")] + letters("ZXCVBNM") +
             pairs([("<", ","), (">", "."), ("?", "/")]) + [key("shift", 2.25, "br")]))
rows.append((KEY_H, [
    key("fn", 1, "bl"),
    key("control", 1, "br", "^"),
    key("option", 1, "br", "⌥"),
    key("command", 1.25, "br", "⌘"),
    key("", 5, "c", kind="space"),
    key("command", 1.25, "bl", "⌘"),
    key("option", 1, "bl", "⌥"),
    key("arrows", 3, kind="arrows"),
]))


def placed_keys():
    """Yield every physical key with x, y, w, h relative to the key block."""
    out = []
    y = 0.0
    for r, (h, ks) in enumerate(rows):
        x = 0.0
        for k in ks:
            if k["kind"] == "arrows":
                u = PITCH - GAP
                base = y + h
                out.append(dict(row=r, label="←", x=x, y=base - ARROW_H, w=u, h=ARROW_H, kind="arrow", units=1))
                out.append(dict(row=r, label="↑", x=x + PITCH, y=y, w=u, h=ARROW_H, kind="arrow", units=1))
                out.append(dict(row=r, label="↓", x=x + PITCH, y=base - ARROW_H, w=u, h=ARROW_H, kind="arrow", units=1))
                out.append(dict(row=r, label="→", x=x + 2 * PITCH, y=base - ARROW_H, w=u, h=ARROW_H, kind="arrow", units=1))
            else:
                d = dict(row=r, label=k["label"], x=x, y=y, w=k["w"], h=h,
                         kind=k["kind"], units=k["units"], align=k["align"])
                if k.get("top"):
                    d["top"] = k["top"]
                if k.get("icon"):
                    d["icon"] = k["icon"]
                out.append(d)
            x += k["w"] + GAP
        y += h + GAP
    for d in out:
        for f in ("x", "y", "w", "h"):
            d[f] = round(d[f], 2)
    return out


# ---------------------------------------------------------------- svg helpers
INK = "#1D1D1F"
MUTED = "#5C5C61"
DIM = "#8A8A90"
ALU_TOP, ALU = "#E6E7E9", "#D0D1D4"
WELL = "#C2C3C7"
PAD = "#DCDDE0"
KEYCAP = "#1B1B1D"
LEGEND = "#ECECEF"


def text(x, y, s, size=3.0, fill=INK, anchor="middle", weight=500):
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}" '
            f'font-family="Inter, Helvetica, Arial, sans-serif">{escape(s)}</text>')


def hdim(x1, x2, y, label):
    return (f'<g stroke="{DIM}" stroke-width="0.3">'
            f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}"/>'
            f'<line x1="{x1}" y1="{y-2}" x2="{x1}" y2="{y+2}"/>'
            f'<line x1="{x2}" y1="{y-2}" x2="{x2}" y2="{y+2}"/></g>'
            + f'<rect x="{(x1+x2)/2-len(label)*1.2-3}" y="{y-2.6}" width="{len(label)*2.4+6}" height="5.2" fill="#FFFFFF"/>'
            + text((x1 + x2) / 2, y + 1.2, label, 3.4, MUTED, weight=600))


def vdim(x, y1, y2, label):
    return (f'<g stroke="{DIM}" stroke-width="0.3">'
            f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}"/>'
            f'<line x1="{x-2}" y1="{y1}" x2="{x+2}" y2="{y1}"/>'
            f'<line x1="{x-2}" y1="{y2}" x2="{x+2}" y2="{y2}"/></g>'
            + text(x + 4, (y1 + y2) / 2 + 1.2, label, 3.4, MUTED, "start", 600))


def svg_doc(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">\n'
            f'<title>{escape(title)}</title>\n'
            f'<defs><linearGradient id="alu" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{ALU_TOP}"/><stop offset="1" stop-color="{ALU}"/>'
            f'</linearGradient></defs>\n'
            f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>\n{body}\n</svg>\n')


def draw_key(k, ox, oy):
    x, y, w, h = ox + k["x"], oy + k["y"], k["w"], k["h"]
    parts = [f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="1.6" fill="{KEYCAP}"/>']
    kind, label = k["kind"], k["label"]
    if kind == "arrow":
        cx, cy = x + w / 2, y + h / 2
        tri = {"←": f"{cx-1.2},{cy} {cx+1.0},{cy-1.2} {cx+1.0},{cy+1.2}",
               "→": f"{cx+1.2},{cy} {cx-1.0},{cy-1.2} {cx-1.0},{cy+1.2}",
               "↑": f"{cx},{cy-1.1} {cx-1.2},{cy+1.0} {cx+1.2},{cy+1.0}",
               "↓": f"{cx},{cy+1.1} {cx-1.2},{cy-1.0} {cx+1.2},{cy-1.0}"}[label]
        parts.append(f'<polygon points="{tri}" fill="{LEGEND}"/>')
    elif kind == "fn":
        parts.append(text(x + w / 2, y + h / 2 + 0.9, label, 2.4, LEGEND))
    elif kind in ("fingerprint", "space"):
        pass
    elif k.get("top") and k["align"] == "c":
        parts.append(text(x + w / 2, y + 5.4, k["top"], 3.0, LEGEND))
        parts.append(text(x + w / 2, y + h - 3.6, label, 3.4, LEGEND))
    elif k["align"] == "c":
        parts.append(text(x + w / 2, y + h / 2 + 1.5, label, 4.2, LEGEND))
    elif k["align"] == "ml":
        parts.append(text(x + 2, y + h / 2 + 0.9, label, 2.8, LEGEND, "start"))
    else:
        right = k["align"] == "br"
        tx = x + w - 2 if right else x + 2
        anchor = "end" if right else "start"
        parts.append(text(tx, y + h - 2.2, label, 2.6, LEGEND, anchor))
        if k.get("top"):
            sx = x + w - 2 if right else x + 2
            parts.append(text(sx, y + 4.2, k["top"], 3.0, LEGEND, anchor))
        if label == "caps lock":
            parts.append(f'<circle cx="{x+2.6:.2f}" cy="{y+3:.2f}" r="0.7" fill="{LEGEND}"/>')
    return "\n".join(parts)


def top_view(spine):
    sd, _, slabel = SPINES[spine]
    m = 26.0
    W = DECK_W + 2 * m + 20
    H = sd + 0.6 + DECK_D + 2 * m + 10
    ox, oy = m, m
    total = sd + 0.6 + DECK_D
    b = []
    b.append(text(ox, 12, f"Deck One · top view · {slabel}", 4.4, INK, "start", 700))
    b.append(text(ox, 18, "True scale: 1 unit = 1 mm. Print at 100 % for a 1:1 template.", 3.0, MUTED, "start"))
    # outline as one rounded body
    b.append(f'<clipPath id="body"><rect x="{ox}" y="{oy}" width="{DECK_W}" height="{total}" rx="{DECK_R}"/></clipPath>')
    b.append(f'<g clip-path="url(#body)">')
    b.append(f'<rect x="{ox}" y="{oy}" width="{DECK_W}" height="{sd}" fill="url(#alu)"/>')
    b.append(f'<rect x="{ox}" y="{oy+sd}" width="{DECK_W}" height="0.6" fill="#A9AAAE"/>')
    b.append(f'<rect x="{ox}" y="{oy+sd+0.6}" width="{DECK_W}" height="{DECK_D}" fill="url(#alu)"/>')
    b.append('</g>')
    b.append(f'<rect x="{ox}" y="{oy}" width="{DECK_W}" height="{total}" rx="{DECK_R}" fill="none" stroke="#B8B9BD" stroke-width="0.3"/>')
    # spine detail
    if spine == "compute":
        bx = ox + (DECK_W - BOARD_W) / 2
        by = oy + (sd - BOARD_D) / 2
        for vx in (ox + 14, bx + BOARD_W + 10):
            vw = (bx - 10) - (ox + 14) if vx == ox + 14 else (ox + DECK_W - 14) - vx
            for i in range(int(vw // 2.4)):
                b.append(f'<rect x="{vx + i*2.4:.2f}" y="{oy+12}" width="0.8" height="{sd-24}" rx="0.4" fill="#9FA0A4"/>')
        b.append(f'<rect x="{bx}" y="{by}" width="{BOARD_W}" height="{BOARD_D}" rx="3" fill="none" stroke="{DIM}" stroke-width="0.4" stroke-dasharray="2 1.4"/>')
        for hx, hy in ((3.5, 3.5), (3.5 + 58, 3.5), (3.5, 3.5 + 49), (3.5 + 58, 3.5 + 49)):
            b.append(f'<circle cx="{bx+hx}" cy="{by+hy}" r="1.35" fill="none" stroke="{DIM}" stroke-width="0.35"/>')
        b.append(text(bx + BOARD_W / 2, by + BOARD_D / 2 - 1, "board bay under the lid", 3.0, MUTED))
        b.append(text(bx + BOARD_W / 2, by + BOARD_D / 2 + 4, "85 × 56 mm · holes 58 × 49 mm, M2.5", 2.6, MUTED))
    else:
        b.append(text(ox + 12, oy + sd / 2 + 1, slabel.split(" · ")[0].upper(), 2.6, MUTED, "start", 600))
        b.append(f'<circle cx="{ox+DECK_W-14}" cy="{oy+sd/2}" r="1" fill="#4CB46A"/>')
    # well + keys
    dy = oy + sd + 0.6
    wx = ox + (DECK_W - WELL_W) / 2
    wy = dy + WELL_TOP
    b.append(f'<rect x="{wx:.2f}" y="{wy:.2f}" width="{WELL_W:.2f}" height="{WELL_H:.2f}" rx="3.3" fill="{WELL}"/>')
    kx, ky = wx + WELL_PAD, wy + WELL_PAD
    for k in placed_keys():
        b.append(draw_key(k, kx, ky))
    # trackpad
    px = ox + (DECK_W - PAD_W) / 2
    py = dy + PAD_TOP
    b.append(f'<rect x="{px}" y="{py:.2f}" width="{PAD_W}" height="{PAD_H}" rx="4" fill="{PAD}" stroke="#BFC0C4" stroke-width="0.3"/>')
    b.append(text(px + PAD_W / 2, py + PAD_H / 2 + 1, "trackpad 140 × 90 mm", 3.2, MUTED))
    # dimensions
    b.append(hdim(ox, ox + DECK_W, oy + total + 12, "304 mm"))
    b.append(vdim(ox + DECK_W + 10, oy, oy + total, f"{total:.0f} mm"))
    return svg_doc(round(W, 1), round(H, 1), "\n".join(b), f"Deck One top view with {spine} spine")


def side_profile():
    m = 20.0
    bases = {"battery": 40.0, "cable": 72.0, "compute": 122.0}
    W = DECK_D + 66 + 2 * m + 50
    H = 140.0
    b = [text(m, 12, "Deck One · side profiles (true scale, mm)", 4.4, INK, "start", 700)]
    for name in ("battery", "cable", "compute"):
        sd, sh, slabel = SPINES[name]
        base = bases[name]
        x0 = m
        # deck wedge: front (left) thin, back (right) thick
        b.append(f'<polygon points="{x0},{base} {x0},{base-FRONT_T} {x0+DECK_D},{base-BACK_T} {x0+DECK_D},{base}" fill="url(#alu)" stroke="#A9AAAE" stroke-width="0.25"/>')
        b.append(f'<rect x="{x0+DECK_D+0.6}" y="{base-sh}" width="{sd}" height="{sh}" rx="1.5" fill="url(#alu)" stroke="#A9AAAE" stroke-width="0.25"/>')
        b.append(text(x0 + DECK_D + sd + 6, base - sh / 2 + 1, f"{slabel.split(' · ')[0]} · {sd:.0f} × {sh:.0f} mm", 3.0, MUTED, "start", 600))
        b.append(text(x0, base + 5, "front 4.5 mm", 2.6, MUTED, "start"))
        b.append(text(x0 + DECK_D, base + 5, "back 11 mm", 2.6, MUTED, "end"))
    return svg_doc(round(W, 1), round(H, 1), "\n".join(b), "Deck One side profiles with each spine")


def main():
    keys = placed_keys()
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "drawings"), exist_ok=True)
    meta = {
        "units": "mm",
        "origin": "top-left corner of the key block (inside the keyboard well)",
        "pitch": PITCH, "gap": GAP, "key_height": KEY_H, "fn_row_height": FN_H,
        "block_width": round(ROW_W, 2), "block_height": round(KEYS_H, 2),
        "keys": keys,
    }
    with open(os.path.join(ROOT, "data", "keyboard-layout.json"), "w") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)
    with open(os.path.join(ROOT, "data", "keyboard-layout.csv"), "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["row", "label", "top_legend", "kind", "units", "x_mm", "y_mm", "w_mm", "h_mm"])
        for k in keys:
            wr.writerow([k["row"], k["label"], k.get("top", ""), k["kind"], k["units"], k["x"], k["y"], k["w"], k["h"]])
    for s in SPINES:
        with open(os.path.join(ROOT, "drawings", f"top-view-{s}.svg"), "w") as f:
            f.write(top_view(s))
    with open(os.path.join(ROOT, "drawings", "side-profile.svg"), "w") as f:
        f.write(side_profile())
    print(f"{len(keys)} keys · block {ROW_W:.1f} × {KEYS_H:.1f} mm · fn key {FN_W:.2f} mm")


if __name__ == "__main__":
    main()
