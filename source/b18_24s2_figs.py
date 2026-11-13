# -*- coding: utf-8 -*-
"""Figures for CAT 2024 Slot 2, written into media/ when imported."""
import math
import charts
from charts import _t
INK, MUT, GRID = "#111827", "#6b7280", "#e5e7eb"
BLUE, LAKE = "#2563eb", "#93c5fd"

def _grid():
    cw, ch, x0, y0 = 80, 34, 70, 30
    b = ""
    for c in range(4): b += _t(x0 + cw * c + cw / 2, y0 - 10, f"Column {c + 1}", 12, bold=True)
    for r in range(4):
        b += _t(x0 - 8, y0 + ch * r + ch / 2 + 4, f"Row {r + 1}", 12, "end", bold=True)
        for c in range(r, 4):
            b += f'<rect x="{x0 + cw * c}" y="{y0 + ch * r}" width="{cw}" height="{ch}" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
    return charts.raw("sipe_2024S2_DILR_S1", x0 + 4 * cw + 10, y0 + 4 * ch + 10, b,
                      "Grid of ten slots: Row 1 has slots in columns 1 to 4, Row 2 in columns 2 to 4, Row 3 in columns 3 and 4, and Row 4 only in column 4.")
GRID10 = _grid()

def _walk():
    s = 0.36; ox, oy = 30, 30
    pt = {"A": (0, 0), "B": (150, 0), "C": (450, 0), "D": (750, 0), "H": (0, 400), "G": (150, 400), "F": (450, 400), "E": (750, 400),
          "I": (0, 600), "J": (150, 600), "K": (450, 600), "L": (750, 600), "P": (0, 1000), "O": (150, 1000), "N": (450, 1000), "M": (750, 1000)}
    X = lambda k: ox + pt[k][0] * s; Y = lambda k: oy + pt[k][1] * s
    b = ""
    for a, c in [("C", "E"), ("G", "K"), ("K", "M")]:
        b += f'<rect x="{X(a):.1f}" y="{Y(a):.1f}" width="{X(c) - X(a):.1f}" height="{Y(c) - Y(a):.1f}" fill="{LAKE}"/>'
    edges = "AB BC CD DE EL LM MN NO OP PI IH HA BG GJ JO HG IJ IG GF FE CF FK JK KL KN OK"
    for e in edges.split():
        b += f'<line x1="{X(e[0]):.1f}" y1="{Y(e[0]):.1f}" x2="{X(e[1]):.1f}" y2="{Y(e[1]):.1f}" stroke="{INK}" stroke-width="2"/>'
    off = {"A": (-10, -8), "B": (0, -10), "C": (0, -10), "D": (10, -8), "H": (-12, 4), "G": (10, -8), "F": (-10, -8), "E": (12, 4),
           "I": (-12, 4), "J": (10, 14), "K": (10, -6), "L": (12, 4), "P": (-10, 16), "O": (0, 18), "N": (0, 18), "M": (10, 16)}
    for k, (dx, dy) in off.items():
        b += f'<circle cx="{X(k):.1f}" cy="{Y(k):.1f}" r="3" fill="{INK}"/>' + _t(X(k) + dx, Y(k) + dy, k, 13, bold=True)
    return charts.raw("sipe_2024S2_DILR_S2", int(750 * s + 2 * ox), int(1000 * s + 2 * oy), b,
                      "Walkway map. Outer rectangle A–B–C–D across the top, D–E–L–M down the right, M–N–O–P along the bottom, P–I–H–A up the left. "
                      "B–G–J–O is a vertical walkway; H–G and I–J are short horizontal walkways on the left, with a diagonal from I to G. "
                      "Lakes (shaded): C–D–E–F at top right; G–F–K–J in the middle; K–L–M–N at bottom right. F–E, F–K, K–L and K–N are walkways along the lakes. "
                      "A diagonal runs from O to K. Distances: OP 150, ON 300, MN 300, ML 400, EL 200, DE 400 m.")
WALK = _walk()

def _ratings():
    vals = [(5, 10), (4, 20), (3, 5), (2, 10), (1, 5)]
    left, top, bh, gap, W = 50, 16, 20, 12, 440
    pw = W - left - 20; Xv = lambda v: left + pw * v / 25
    b = ""
    for v in range(0, 26, 5):
        b += f'<line x1="{Xv(v):.1f}" y1="{top}" x2="{Xv(v):.1f}" y2="{top + 5 * (bh + gap)}" stroke="{GRID}"/>' + _t(Xv(v), top + 5 * (bh + gap) + 16, str(v), 11, col=MUT)
    for i, (r, n) in enumerate(vals):
        y = top + i * (bh + gap) + gap / 2
        b += f'<rect x="{left}" y="{y:.1f}" width="{Xv(n) - left:.1f}" height="{bh}" fill="{BLUE}"/>' + _t(left - 10, y + 15, str(r), 12, "end", bold=True) + _t(Xv(n) + 6, y + 15, str(n), 11, "start")
    H = top + 5 * (bh + gap) + 40
    b += _t(left + pw / 2, H - 6, "Number of buyers", 11, col=MUT) + _t(14, top + 80, "Rating", 11, col=MUT, extra=f' transform="rotate(-90 14 {top + 80})"')
    return charts.raw("sipe_2024S2_DILR_S3", W, H, b, "Distribution of ratings on Day 2: rating 5 by 10 buyers, 4 by 20, 3 by 5, 2 by 10, 1 by 5.")
RATINGS = _ratings()

def _bubbles(name, year, data, alt):
    W, H = 460, 300; left, right, top, bot = 56, 16, 30, 44
    pw, ph = W - left - right, H - top - bot
    X = lambda v: left + pw * (v - 500) / 1000
    Y = lambda v: top + ph - ph * (v - 2200) / 2200
    b = _t(W / 2, 18, str(year), 14, bold=True)
    for v in range(2200, 4401, 200):
        b += f'<line x1="{left}" y1="{Y(v):.1f}" x2="{left + pw}" y2="{Y(v):.1f}" stroke="{GRID}"/>' + _t(left - 6, Y(v) + 4, f"{v:,}", 11, "end", MUT)
    for v in range(500, 1501, 200):
        b += f'<line x1="{X(v):.1f}" y1="{top}" x2="{X(v):.1f}" y2="{top + ph}" stroke="{GRID}"/>' + _t(X(v), top + ph + 16, f"{v:,}", 11, col=MUT)
    for k, (es, pat, m) in data.items():
        r = 9 * math.sqrt(m)
        b += f'<circle cx="{X(es):.1f}" cy="{Y(pat):.1f}" r="{r:.1f}" fill="none" stroke="{INK}" stroke-width="1.2"/><circle cx="{X(es):.1f}" cy="{Y(pat):.1f}" r="2.5" fill="{INK}"/>'
        b += _t(X(es), Y(pat) - 5, k, 12, bold=True)
    b += _t(left + pw / 2, H - 8, "ES (employees)", 11, col=MUT) + _t(14, top + ph / 2, "PAT (Rs crore)", 11, col=MUT, extra=f' transform="rotate(-90 14 {top + ph / 2})"')
    return charts.raw(name, W, H, b, alt)

B19 = _bubbles("sipe_2024S2_DILR_S4a", 2019, {"A": (800, 3000, 4), "B": (1000, 2800, 9), "C": (600, 2400, 9), "D": (600, 3900, 1), "E": (1200, 2400, 16), "F": (800, 2500, 4)},
               "2019 plot of PAT against ES, with circle areas showing PRD. A: ES 800, PAT 3,000, medium circle. B: ES 1,000, PAT 2,800, large circle. C: ES 600, PAT 2,400, large circle. "
               "D: ES 600, PAT 3,900, smallest circle. E: ES 1,200, PAT 2,400, largest circle. F: ES 800, PAT 2,500, medium circle. Circle radii are in the ratio D 1 : A, F 2 : B, C 3 : E 4.")
B23 = _bubbles("sipe_2024S2_DILR_S4b", 2023, {"A": (1300, 3900, 4), "B": (1000, 3800, 9), "C": (800, 3000, 4), "D": (800, 2400, 4), "E": (1400, 3500, 9), "F": (1000, 3200, 4)},
               "2023 plot of PAT against ES, with circle areas showing PRD on the same scale as 2019. A: ES 1,300, PAT 3,900, medium circle. B: ES 1,000, PAT 3,800, large circle. "
               "C: ES 800, PAT 3,000, medium circle. D: ES 800, PAT 2,400, medium circle. E: ES 1,400, PAT 3,500, large circle. F: ES 1,000, PAT 3,200, medium circle. "
               "Medium circles have twice the radius of 2019’s smallest (D) circle, and large circles three times.")
