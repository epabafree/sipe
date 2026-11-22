# -*- coding: utf-8 -*-
"""Figures for Simp Mock 10, written into media/ when imported."""
import math
import charts
from charts import _t
INK, MUT = "#111827", "#6b7280"


def _panel(ox, oy, n, f, xr):
    w, h = 150, 120
    cx = ox + w / 2; cy = oy + h / 2
    b = f'<line x1="{ox + 6}" y1="{cy}" x2="{ox + w - 6}" y2="{cy}" stroke="{MUT}"/>'
    b += f'<line x1="{cx}" y1="{oy + 6}" x2="{cx}" y2="{oy + h - 6}" stroke="{MUT}"/>'
    b += _t(ox + w - 8, cy - 5, "x", 11, col=MUT) + _t(cx + 9, oy + 14, "y", 11, col=MUT)
    pts = []
    k = 14
    for i in range(400):
        x = xr[0] + (xr[1] - xr[0]) * i / 399
        y = f(x)
        if y is None or abs(y) > 3.8: continue
        pts.append(f"{cx + k * x:.1f},{cy - k * y:.1f}")
    b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="#2563eb" stroke-width="2"/>'
    sx = 1 if xr[0] > 0 else -1
    b += f'<circle cx="{cx + k * sx}" cy="{cy}" r="2.5" fill="{INK}"/>' + _t(cx + k * sx, cy + 14, "1" if sx > 0 else "−1", 10)
    b += _t(ox + 12, oy + 14, f"({n})", 12, bold=True)
    b += f'<rect x="{ox}" y="{oy}" width="{w}" height="{h}" fill="none" stroke="#d1d5db"/>'
    return b


def _logs():
    L = lambda x: math.log(x) / math.log(0.25)
    G = lambda x: math.log(x) / math.log(4)
    b = _panel(5, 5, 1, L, (0.02, 4.9)) + _panel(165, 5, 2, G, (0.02, 4.9))
    b += _panel(5, 135, 3, lambda x: L(-x), (-4.9, -0.02)) + _panel(165, 135, 4, lambda x: G(-x), (-4.9, -0.02))
    return charts.raw("sipe_SM10_QA_18", 320, 260, b,
                      "Four graphs. (1) A curve for x > 0, falling from left to right, crossing the x-axis at 1. (2) A curve for x > 0, rising, crossing at 1. (3) A curve for x < 0 crossing at −1, rising from left to right. (4) A curve for x < 0 crossing at −1, falling from left to right.")
LOGS = _logs()
