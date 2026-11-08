# -*- coding: utf-8 -*-
"""Figures for Simp Mock 4 (2025), written into media/ when imported."""
import math
import charts
INK, MUT = "#111827", "#6b7280"
def _wheel():
    w = h = 360; cx = cy = 180; radii = [45, 85, 125, 165]
    b = "".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="2"/>' for r in radii)
    for k in range(8):
        a = math.radians(-90 + 45 * k)
        b += f'<line x1="{cx}" y1="{cy}" x2="{cx + 165 * math.cos(a):.1f}" y2="{cy + 165 * math.sin(a):.1f}" stroke="{INK}" stroke-width="1.5"/>'
    for t, (r0, r1) in enumerate(zip([0] + radii[:-1], radii), 1):
        rm = (r0 + r1) / 2 if t > 1 else 28
        for s in range(1, 9):
            a = math.radians(-90 + 45 * (s - 1) + 22.5)
            x, y = cx + rm * math.cos(a), cy + rm * math.sin(a)
            fs = 8 if t == 1 else 11
            b += f'<text x="{x:.1f}" y="{y + fs / 3:.1f}" font-size="{fs}" text-anchor="middle" fill="{INK}">T<tspan font-size="{fs * 0.7:.1f}" dy="2">{t}</tspan><tspan dy="-2">S</tspan><tspan font-size="{fs * 0.7:.1f}" dy="2">{s}</tspan></text>'
    return charts.raw("sipe_SM25-04_DILR_S2", w, h, b, "A wheel of four concentric tracks and eight 45° sectors; each cell labelled by track and sector, with sector 1 just clockwise of the top")
WHEEL = _wheel()
BARS = charts.vbar("sipe_SM25-04_DILR_S5", ["Hyderabad", "Bengaluru", "Delhi", "Chennai", "Kolkata"],
                   [("% of male employees", [25, 15, 25, 20, 15]), ("% of female employees", [30, 20, 10, 25, 15])], 35, 5,
                   "Grouped bars: share of all male and all female employees in each of five branches", ylabel="Percentage", fmt=lambda v: f"{v}")
