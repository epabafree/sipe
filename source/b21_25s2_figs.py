# -*- coding: utf-8 -*-
"""Figures for CAT 2025 Slot 2, written into media/ when imported."""
import charts
from charts import _t
INK, MUT, GRID = "#111827", "#6b7280", "#e5e7eb"

def _si():
    W, H = 520, 400; left, right, top, bot = 60, 30, 20, 50
    pw, ph = W - left - right, H - top - bot
    X = lambda v: left + pw * (v + 40) / 140
    Y = lambda v: top + ph - ph * (v + 30) / 90
    b = ""
    for v in range(-40, 101, 5):
        b += f'<line x1="{X(v):.1f}" y1="{top}" x2="{X(v):.1f}" y2="{top + ph}" stroke="{GRID if v % 10 == 0 else "#f3f4f6"}"/>'
        if v % 20 == 0: b += _t(X(v), Y(0) + 16, f"{v}%", 10, col=MUT)
    for v in range(-30, 61, 5):
        b += f'<line x1="{left}" y1="{Y(v):.1f}" x2="{left + pw}" y2="{Y(v):.1f}" stroke="{GRID if v % 10 == 0 else "#f3f4f6"}"/>' + (_t(X(0) - 5, Y(v) + 4, f"{v}%", 10, "end", MUT) if v % 10 == 0 else "")
    b += f'<line x1="{left}" y1="{Y(0):.1f}" x2="{left + pw}" y2="{Y(0):.1f}" stroke="{INK}"/><line x1="{X(0):.1f}" y1="{top}" x2="{X(0):.1f}" y2="{top + ph}" stroke="{INK}"/>'
    pts = {"A": (25, 50), "B": (-25, -25), "C": (-20, 40), "D": (100, 20), "E": (25, 20), "F": (100, -25)}
    for k, (x, y) in pts.items():
        b += f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="5" fill="{INK}"/>' + _t(X(x) + (-12 if x == 100 else 10), Y(y) - 7, k, 13, bold=True)
    b += _t(left + pw / 2, H - 8, "% increase in index in 2020 from 2016", 11, col=MUT)
    b += _t(16, top + ph / 2, "% increase in index in 2024 from 2020", 11, col=MUT, extra=f' transform="rotate(-90 16 {top + ph / 2})"')
    return charts.raw("sipe_2025S2_DILR_S2", W, H, b,
                      "Scatter plot. X: % increase in SI in 2020 from 2016; Y: % increase in 2024 from 2020. A (25%, 50%), B (−25%, −25%), C (−20%, 40%), D (100%, 20%), E (25%, 20%), F (100%, −25%).")
SI = _si()

BY_AUTHOR = charts.vbar("sipe_2025S2_DILR_S4a", ["Arman", "Brajen", "Chintan", "Devon"], [("Papers", [5, 8, 12, 10])], 14, 2,
                        "Number of papers by each author: Arman 5, Brajen 8, Chintan 12, Devon 10.", ylabel="Papers", w=420, h=260)
BY_TYPE = charts.vbar("sipe_2025S2_DILR_S4b", ["Single", "Two", "Three", "Four"], [("Papers", [10, 4, 3, 2])], 12, 2,
                      "Number of papers by type: single-author 10, two-author 4, three-author 3, four-author 2.", ylabel="Papers", w=420, h=260)
