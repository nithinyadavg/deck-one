#!/usr/bin/env python3
"""Generate the Deck One keyboard's reference drawings and layout data.

Everything is in millimetres. Run from the keyboard/ folder:

    python3 tools/generate_drawings.py

Outputs:
    data/keyboard-layout.json        every key's position and size (mm)
    data/keyboard-layout.csv         the same, as a table
    drawings/top-view-standard.svg   standard front fascia (140 x 90 trackpad)
    drawings/top-view-big-hands.svg  big-hands fascia (smaller, lower trackpad + ridge)
    drawings/top-view-wrist-rest.svg wrist-rest fascia (no trackpad)
    drawings/underside.svg           base: module bays, battery, feet, latches
    drawings/side-profile.svg        wedge, fascia seam, bay depth

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
FRONT_T, BACK_T = 4.5, 11.0                   # deck wedge thickness

# The deck is two parts joined by a seam: the keyboard frame (back) and a
# swappable front fascia (palm rest + trackpad).
FRAME_D = 122.0                               # keyboard frame depth from the back edge
FASCIA_D = DECK_D - FRAME_D                   # 99 mm

FASCIAS = {
    # name: trackpad (w, h, top offset inside fascia) or None, ridge (w, h, top) or None
    "standard":   {"pad": (140.0, 90.0, 2.7), "ridge": None,
                   "title": "Standard fascia · 140 × 90 mm trackpad"},
    "big-hands":  {"pad": (120.0, 76.0, 16.0), "ridge": (160.0, 3.0, 7.0),
                   "title": "Big-hands fascia · 120 × 76 mm trackpad, lowered, with thumb ridge"},
    "wrist-rest": {"pad": None, "ridge": None,
                   "title": "Wrist-rest fascia · no trackpad"},
}

# Underside module bays (seen from below), mm from the back edge / left edge
BAY_W, BAY_D, BAY_T = 120.0, 50.0, 4.0
BAY_Y = 12.0
BAY_XS = (22.0, DECK_W - 22.0 - BAY_W)
BATTERY = (22.0, 68.0, DECK_W - 44.0, 48.0)   # x, y, w, h of the built-in battery

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


def deck_outline(ox, oy, fill="url(#alu)"):
    return (f'<rect x="{ox}" y="{oy}" width="{DECK_W}" height="{DECK_D}" rx="{DECK_R}" '
            f'fill="{fill}" stroke="#B8B9BD" stroke-width="0.3"/>')


def top_view(fascia):
    f = FASCIAS[fascia]
    m = 26.0
    W = DECK_W + 2 * m + 24
    H = DECK_D + 2 * m + 14
    ox, oy = m, m
    b = [text(ox, 12, f"Deck One keyboard · top view · {f['title']}", 4.4, INK, "start", 700),
         text(ox, 18, "True scale: 1 unit = 1 mm. Print at 100 % for a 1:1 template.", 3.0, MUTED, "start"),
         deck_outline(ox, oy)]
    # seam between keyboard frame and front fascia
    sy = oy + FRAME_D
    b.append(f'<line x1="{ox}" y1="{sy}" x2="{ox+DECK_W}" y2="{sy}" stroke="#A9AAAE" stroke-width="0.5"/>')
    b.append(text(ox + 4, sy + 3.6, "front fascia (swappable)", 2.4, MUTED, "start"))
    # well + keys
    wx = ox + (DECK_W - WELL_W) / 2
    wy = oy + WELL_TOP
    b.append(f'<rect x="{wx:.2f}" y="{wy:.2f}" width="{WELL_W:.2f}" height="{WELL_H:.2f}" rx="3.3" fill="{WELL}"/>')
    for k in placed_keys():
        b.append(draw_key(k, wx + WELL_PAD, wy + WELL_PAD))
    well_bottom = wy + WELL_H
    if f["ridge"]:
        rw, rh, rt = f["ridge"]
        rx = ox + (DECK_W - rw) / 2
        b.append(f'<rect x="{rx}" y="{sy+rt}" width="{rw}" height="{rh}" rx="1.5" fill="#C4C5C9" stroke="#A9AAAE" stroke-width="0.25"/>')
        b.append(text(rx - 3, sy + rt + 2.4, "thumb ridge, 1 mm high", 2.6, MUTED, "end"))
    if f["pad"]:
        pw, ph, pt = f["pad"]
        px = ox + (DECK_W - pw) / 2
        py = sy + pt
        b.append(f'<rect x="{px}" y="{py:.2f}" width="{pw}" height="{ph}" rx="4" fill="{PAD}" stroke="#BFC0C4" stroke-width="0.3"/>')
        b.append(text(px + pw / 2, py + ph / 2 + 1, f"trackpad {pw:.0f} × {ph:.0f} mm", 3.2, MUTED))
        gap = py - well_bottom
        b.append(vdim(ox + DECK_W - 40, well_bottom, py, f"{gap:.1f} mm from keys"))
    else:
        b.append(text(ox + DECK_W / 2, sy + FASCIA_D / 2 + 1, "plain palm rest · use with a mouse or external trackpad", 3.0, MUTED))
    b.append(hdim(ox, ox + DECK_W, oy + DECK_D + 12, "304 mm"))
    b.append(vdim(ox + DECK_W + 10, oy, oy + DECK_D, "221 mm"))
    return svg_doc(round(W, 1), round(H, 1), "\n".join(b), f"Deck One keyboard top view, {fascia} fascia")


def underside():
    m = 26.0
    W = DECK_W + 2 * m + 24
    H = DECK_D + 2 * m + 14
    ox, oy = m, m
    b = [text(ox, 12, "Deck One keyboard · underside (seen from below, back edge at top)", 4.4, INK, "start", 700),
         text(ox, 18, "True scale, mm. Bays are flush, with magnetic covers; the deck works with both bays empty.", 3.0, MUTED, "start"),
         deck_outline(ox, oy, "#D7D8DB")]
    for i, bx in enumerate(BAY_XS):
        x, y = ox + bx, oy + BAY_Y
        b.append(f'<rect x="{x}" y="{y}" width="{BAY_W}" height="{BAY_D}" rx="3" fill="#C9CACE" stroke="#8A8A90" stroke-width="0.4"/>')
        for p in range(6):
            b.append(f'<circle cx="{x + BAY_W/2 - 12.5 + p*5:.2f}" cy="{y + 5}" r="0.9" fill="#B08D57"/>')
        b.append(text(x + BAY_W / 2, y + BAY_D / 2 + 0.5, f"Bay {'AB'[i]}", 4.0, INK, weight=700))
        b.append(text(x + BAY_W / 2, y + BAY_D / 2 + 6, "120 × 50 × 4 mm · 6 pogo pins", 2.6, MUTED))
    bx, by, bw, bh = BATTERY
    b.append(f'<rect x="{ox+bx}" y="{oy+by}" width="{bw}" height="{bh}" rx="3" fill="none" stroke="{DIM}" stroke-width="0.4" stroke-dasharray="2 1.4"/>')
    b.append(text(ox + bx + bw / 2, oy + by + bh / 2 + 1, "built-in battery, inside the frame · 260 × 48 × 3.5 mm", 2.8, MUTED))
    sy = oy + FRAME_D
    b.append(f'<line x1="{ox}" y1="{sy}" x2="{ox+DECK_W}" y2="{sy}" stroke="#8A8A90" stroke-width="0.5"/>')
    for lx in (70.0, DECK_W - 70.0):
        b.append(f'<rect x="{ox+lx-9}" y="{sy+5}" width="18" height="4" rx="2" fill="#A9AAAE"/>')
    b.append(text(ox + DECK_W / 2, sy + 8.2, "fascia release latches", 2.6, MUTED))
    for fx, fy in ((14, 14), (DECK_W - 14, 14), (14, DECK_D - 14), (DECK_W - 14, DECK_D - 14)):
        b.append(f'<circle cx="{ox+fx}" cy="{oy+fy}" r="5" fill="#9A9BA0"/>')
    b.append(text(ox + DECK_W - 14, oy + DECK_D - 22, "rubber feet ×4", 2.6, MUTED, "end"))
    # ports on the back edge, drawn as notches (mirrored: seen from below)
    b.append(f'<rect x="{ox+DECK_W-40}" y="{oy-1.2}" width="9" height="2.4" rx="1.2" fill="#5A5B5F"/>')
    b.append(text(ox + DECK_W - 35.5, oy - 3, "USB-C", 2.4, MUTED))
    b.append(f'<rect x="{ox+30}" y="{oy-1}" width="7" height="2" rx="0.6" fill="#5A5B5F"/>')
    b.append(text(ox + 33.5, oy - 3, "power", 2.4, MUTED))
    b.append(hdim(ox, ox + DECK_W, oy + DECK_D + 12, "304 mm"))
    b.append(vdim(ox + DECK_W + 10, oy, oy + DECK_D, "221 mm"))
    return svg_doc(round(W, 1), round(H, 1), "\n".join(b), "Deck One keyboard underside")


def side_profile():
    m = 20.0
    W = DECK_D * 1.0 + 2 * m + 40
    H = 80.0
    b = [text(m, 12, "Deck One keyboard · side profile (thickness drawn 2× for clarity)", 4.4, INK, "start", 700)]
    base = 58.0
    x0 = m
    ft, bt = FRONT_T * 2, BACK_T * 2   # 2x vertical exaggeration
    b.append(f'<polygon points="{x0},{base} {x0},{base-ft} {x0+DECK_D},{base-bt} {x0+DECK_D},{base}" fill="url(#alu)" stroke="#A9AAAE" stroke-width="0.25"/>')
    seam_x = x0 + FASCIA_D
    seam_t = (FRONT_T + (BACK_T - FRONT_T) * FASCIA_D / DECK_D) * 2
    b.append(f'<line x1="{seam_x}" y1="{base}" x2="{seam_x}" y2="{base-seam_t}" stroke="#7E7F84" stroke-width="0.4"/>')
    bay_x1 = x0 + DECK_D - BAY_Y - BAY_D
    b.append(f'<rect x="{bay_x1}" y="{base - BAY_T*2}" width="{BAY_D}" height="{BAY_T*2}" fill="none" stroke="{DIM}" stroke-width="0.35" stroke-dasharray="1.5 1"/>')
    b.append(text(bay_x1 + BAY_D / 2, base + 5, "module bay, 4 mm", 2.6, MUTED))
    b.append(text(x0, base + 5, "front 4.5 mm", 2.6, MUTED, "start"))
    b.append(text(seam_x, base + 5, f"fascia seam ({seam_t/2:.1f} mm)", 2.6, MUTED))
    b.append(text(x0 + DECK_D, base + 11, "back 11 mm", 2.6, MUTED, "end"))
    b.append(text(x0 + DECK_D / 2, 24, "← palm rest / front fascia · 99 mm | keyboard frame · 122 mm →", 2.8, MUTED))
    return svg_doc(round(W, 1), round(H, 1), "\n".join(b), "Deck One keyboard side profile")


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
    for name in FASCIAS:
        with open(os.path.join(ROOT, "drawings", f"top-view-{name}.svg"), "w") as f:
            f.write(top_view(name))
    with open(os.path.join(ROOT, "drawings", "underside.svg"), "w") as f:
        f.write(underside())
    with open(os.path.join(ROOT, "drawings", "side-profile.svg"), "w") as f:
        f.write(side_profile())
    print(f"{len(keys)} keys · block {ROW_W:.1f} × {KEYS_H:.1f} mm · fascia {FASCIA_D:.0f} mm deep")


if __name__ == "__main__":
    main()
