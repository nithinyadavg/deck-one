#!/usr/bin/env python3
"""Generate the Deck One Spine's reference drawings.

The Spine is a separate box joined to the keyboard by one USB-C cable. It has
the same 127 x 127 mm footprint as a Mac mini so the two stack neatly.

Run from the spine/ folder:

    python3 tools/generate_drawings.py

Outputs:
    drawings/top-view-internal.svg   lid off: compute bay, M.2 slot, power, hub, fan
    drawings/rear-io.svg             the swappable rear I/O plate
"""

import os
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- dimensions (mm)
BOX_W = BOX_D = 127.0
BOX_H = 30.0
BOX_R = 14.0
WALL = 3.5

BOARD = (8.0, 8.0, 85.0, 56.0)           # x, y, w, h: compute board, rear-left
BOARD_HOLES = (58.0, 49.0, 3.5)           # hole spacing x, y and inset from board edge
M2 = (99.0, 8.0, 22.0, 80.0)             # M.2 2230-2280 slot along the right side
POWER = (8.0, 92.0, 40.0, 25.0)          # USB-C PD input, regulates to 5.1 V / 5 A
HUB = (52.0, 96.0, 42.0, 21.0)           # USB hub: deck port + rear ports
FAN = (50.5, 36.0, 20.0)                  # cx, cy, r: optional 40 mm fan in the lid

INK, MUTED, DIM = "#1D1D1F", "#5C5C61", "#8A8A90"
ALU_TOP, ALU = "#E6E7E9", "#D0D1D4"


def text(x, y, s, size=3.0, fill=INK, anchor="middle", weight=500):
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}" '
            f'font-family="Inter, Helvetica, Arial, sans-serif">{escape(s)}</text>')


def hdim(x1, x2, y, label):
    return (f'<g stroke="{DIM}" stroke-width="0.3"><line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}"/>'
            f'<line x1="{x1}" y1="{y-2}" x2="{x1}" y2="{y+2}"/><line x1="{x2}" y1="{y-2}" x2="{x2}" y2="{y+2}"/></g>'
            f'<rect x="{(x1+x2)/2-len(label)*1.2-3}" y="{y-2.6}" width="{len(label)*2.4+6}" height="5.2" fill="#FFFFFF"/>'
            + text((x1 + x2) / 2, y + 1.2, label, 3.2, MUTED, weight=600))


def vdim(x, y1, y2, label):
    return (f'<g stroke="{DIM}" stroke-width="0.3"><line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}"/>'
            f'<line x1="{x-2}" y1="{y1}" x2="{x+2}" y2="{y1}"/><line x1="{x-2}" y1="{y2}" x2="{x+2}" y2="{y2}"/></g>'
            + text(x + 4, (y1 + y2) / 2 + 1.2, label, 3.2, MUTED, "start", 600))


def svg_doc(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(title)}">\n<title>{escape(title)}</title>\n'
            f'<defs><linearGradient id="alu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ALU_TOP}"/>'
            f'<stop offset="1" stop-color="{ALU}"/></linearGradient></defs>\n'
            f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>\n{body}\n</svg>\n')


def block(ox, oy, r, fill, label, sub=None, dashed=False):
    x, y, w, h = r
    dash = ' stroke-dasharray="1.6 1.1"' if dashed else ""
    out = [f'<rect x="{ox+x}" y="{oy+y}" width="{w}" height="{h}" rx="2" fill="{fill}" stroke="{DIM}" stroke-width="0.35"{dash}/>',
           text(ox + x + w / 2, oy + y + h / 2 + (0 if sub else 1), label, 2.8, INK, weight=600)]
    if sub:
        out.append(text(ox + x + w / 2, oy + y + h / 2 + 4.2, sub, 2.3, MUTED))
    return "\n".join(out)


def top_view():
    m = 22.0
    W, H = BOX_W + 2 * m + 26, BOX_D + 2 * m + 14
    ox, oy = m, m
    b = [text(ox, 10, "Deck One Spine · top view, lid off (rear I/O at top)", 4.2, INK, "start", 700),
         text(ox, 15.5, "True scale, mm. Same footprint as a Mac mini.", 2.8, MUTED, "start"),
         f'<rect x="{ox}" y="{oy}" width="{BOX_W}" height="{BOX_D}" rx="{BOX_R}" fill="url(#alu)" stroke="#A9AAAE" stroke-width="0.4"/>',
         f'<rect x="{ox+WALL}" y="{oy+WALL}" width="{BOX_W-2*WALL}" height="{BOX_D-2*WALL}" rx="{BOX_R-WALL}" fill="#F4F4F5" stroke="#C4C5C9" stroke-width="0.3"/>']
    b.append(block(ox, oy, BOARD, "#DDE8DF", "compute board bay", "85 × 56 mm"))
    bx, by, bw, bh = BOARD
    hx, hy, inset = BOARD_HOLES
    for dx, dy in ((0, 0), (hx, 0), (0, hy), (hx, hy)):
        b.append(f'<circle cx="{ox+bx+inset+dx}" cy="{oy+by+inset+dy}" r="1.35" fill="#FFFFFF" stroke="{DIM}" stroke-width="0.35"/>')
    cx, cy, r = FAN
    b.append(f'<circle cx="{ox+cx}" cy="{oy+cy}" r="{r}" fill="none" stroke="{DIM}" stroke-width="0.35" stroke-dasharray="1.6 1.1"/>')
    b.append(text(ox + BOARD[0] + BOARD[2] / 2, oy + BOARD[1] + BOARD[3] + 5, "dashed circle: optional 40 mm fan in the lid", 2.3, MUTED))
    b.append(block(ox, oy, M2, "#E3E1EE", "M.2", "2230–2280"))
    b.append(block(ox, oy, POWER, "#F1E4D6", "power", "USB-C PD → 5.1 V 5 A"))
    b.append(block(ox, oy, HUB, "#DCE6EF", "USB hub", "deck + rear ports"))
    b.append(f'<rect x="{ox+12}" y="{oy-1.4}" width="{BOX_W-24}" height="2.8" rx="1.4" fill="#9FA0A4"/>')
    b.append(text(ox + BOX_W / 2, oy - 3.4, "swappable rear I/O plate", 2.6, MUTED))
    b.append(f'<circle cx="{ox+BOX_W/2}" cy="{oy+BOX_D-1.6}" r="0.9" fill="#4CB46A"/>')
    b.append(text(ox + BOX_W / 2, oy + BOX_D + 4.5, "front: status light", 2.4, MUTED))
    b.append(hdim(ox, ox + BOX_W, oy + BOX_D + 11, "127 mm"))
    b.append(vdim(ox + BOX_W + 8, oy, oy + BOX_D, "127 mm"))
    return svg_doc(round(W, 1), round(H, 1), "\n".join(b), "Deck One Spine top view with the lid off")


PORTS = [
    # label, width, height
    ("power in", 9.0, 3.3),
    ("to keyboard", 9.0, 3.3),
    ("USB-A", 13.0, 5.5),
    ("USB-A", 13.0, 5.5),
    ("HDMI", 15.0, 5.5),
    ("Ethernet", 16.0, 13.5),
]


def rear_io():
    m = 20.0
    s = 2.0  # drawn at 2x for legibility
    W, H = BOX_W * s + 2 * m, BOX_H * s + 2 * m + 26
    ox, oy = m, m + 6
    b = [text(m, 12, "Deck One Spine · rear I/O plate (drawn at 2× scale)", 4.2, INK, "start", 700),
         f'<rect x="{ox}" y="{oy}" width="{BOX_W*s}" height="{BOX_H*s}" rx="{6*s}" fill="url(#alu)" stroke="#A9AAAE" stroke-width="0.4"/>']
    gaps = [5.0, 6.0, 4.0, 6.0, 6.0]
    x = 8.0
    mid = BOX_H / 2
    for i, (label, w, h) in enumerate(PORTS):
        px, py = ox + x * s, oy + (mid - h / 2) * s
        rx = 1.6 * s if w < 10 else 0.8 * s
        b.append(f'<rect x="{px}" y="{py}" width="{w*s}" height="{h*s}" rx="{rx}" fill="#3A3B3E"/>')
        b.append(text(px + w * s / 2, oy + BOX_H * s + 7, label, 3.0, MUTED))
        x += w + (gaps[i] if i < len(gaps) else 0)
    for i in range(6):
        b.append(f'<rect x="{ox + (BOX_W - 16 + i*2.2)*s}" y="{oy + 7*s}" width="{0.9*s}" height="{16*s}" rx="{0.45*s}" fill="#A6A7AB"/>')
    b.append(text(ox + (BOX_W - 10.5) * s, oy + BOX_H * s + 7, "vent", 3.0, MUTED))
    b.append(text(ox, oy + BOX_H * s + 16, "127 × 30 mm. The plate is cut to match the board fitted; this is the default layout.", 3.0, MUTED, "start"))
    return svg_doc(round(W, 1), round(H, 1), "\n".join(b), "Deck One Spine rear I/O plate")


def main():
    os.makedirs(os.path.join(ROOT, "drawings"), exist_ok=True)
    with open(os.path.join(ROOT, "drawings", "top-view-internal.svg"), "w") as f:
        f.write(top_view())
    with open(os.path.join(ROOT, "drawings", "rear-io.svg"), "w") as f:
        f.write(rear_io())
    print("spine drawings written")


if __name__ == "__main__":
    main()
