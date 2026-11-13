# -*- coding: utf-8 -*-
"""Figures for CAT 2025 Slot 1, written into media/ when imported."""
import math
import charts
from charts import _t, PAL
INK, MUT, GRID = "#111827", "#6b7280", "#e5e7eb"
C5 = ["US", "France", "India", "Japan", "UK"]
TP = {"US": {"France": 20, "India": 40, "Japan": 30, "UK": 30},
      "France": {"US": 30, "India": 40, "Japan": 30, "UK": 40},
      "India": {"US": 40, "France": 50, "Japan": 50, "UK": 20},
      "Japan": {"US": 40, "France": 30, "India": 50, "UK": 40},
      "UK": {"US": 20, "France": 30, "India": 30, "Japan": 40}}
TB = {"US": {"France": 6, "India": 4.5, "Japan": 7, "UK": 3},
      "France": {"US": 5.5, "India": 6.5, "Japan": 4, "UK": 4.5},
      "India": {"US": 9, "France": 5, "Japan": 3.5, "UK": 5},
      "Japan": {"US": 4, "France": 3, "India": 8, "UK": 3},
      "UK": {"US": 2.5, "France": 4, "India": 3, "Japan": 6}}

def _radar():
    W, H = 460, 420; cx, cy, R = 230, 200, 140
    ang = lambda i: -math.pi / 2 + 2 * math.pi * i / 5
    pt = lambda i, v: (cx + R * v / 50 * math.cos(ang(i)), cy + R * v / 50 * math.sin(ang(i)))
    b = _t(W / 2, 18, "Import tariff % charged by each country on the others", 13, bold=True)
    for v in (10, 20, 30, 40, 50):
        pts = " ".join(f"{pt(i, v)[0]:.1f},{pt(i, v)[1]:.1f}" for i in range(5))
        b += f'<polygon points="{pts}" fill="none" stroke="{GRID}"/>' + _t(cx + 4, cy - R * v / 50 + 4, f"{v}%", 10, "start", MUT)
    for i, c in enumerate(C5):
        x, y = pt(i, 50); b += f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{GRID}"/>'
        lx, ly = pt(i, 58); b += _t(lx, ly + 4, c, 12, bold=True)
    for k, c in enumerate(C5):
        idx = [i for i, d in enumerate(C5) if d != c]
        pts = " ".join(f"{pt(i, TP[c][C5[i]])[0]:.1f},{pt(i, TP[c][C5[i]])[1]:.1f}" for i in idx)
        b += f'<polyline points="{pts}" fill="none" stroke="{PAL[k]}" stroke-width="2.2"/>'
        for i in idx:
            x, y = pt(i, TP[c][C5[i]]); b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{PAL[k]}"/>'
    lx = 40
    for k, c in enumerate(C5):
        b += f'<rect x="{lx}" y="{H - 24}" width="18" height="4" fill="{PAL[k]}"/>' + _t(lx + 22, H - 18, c, 11, "start"); lx += 30 + 8 * len(c)
    alt = "Radar chart of import tariff percentages. " + " ".join(f"{c} charges " + ", ".join(f"{d} {v}%" for d, v in TP[c].items()) + "." for c in C5)
    return charts.raw("sipe_2025S1_DILR_S5a", W, H, b, alt)
RADAR = _radar()

BARS = charts.vbar("sipe_2025S1_DILR_S5b", C5, [(d, [TB[c].get(d, 0) for c in C5]) for d in C5], 10, 1,
                   "Import tariff in billion USD charged by each country (group) on the others (bars). " + " ".join(f"{c}: " + ", ".join(f"{d} {v}" for d, v in TB[c].items()) + "." for c in C5),
                   ylabel="Billion USD", w=600, h=320, show_values=True, fmt=lambda v: f"{v:g}" if v else "")
