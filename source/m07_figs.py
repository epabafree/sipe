# -*- coding: utf-8 -*-
"""Figures for Simp Mock 7, written into media/ when imported."""
import charts
from charts import _t
INK, MUT = "#111827", "#6b7280"

# Colour of each square, rows listed from the bottom row up; squares numbered 1–25 from the bottom-left, row by row.
GRID = [["P", "B", "G", "R", "Y"], ["R", "B", "G", "B", "P"], ["P", "Y", "R", "G", "B"],
        ["G", "R", "B", "P", "Y"], ["B", "Y", "P", "R", "G"]]
FILL = {"P": "#f9a8d4", "B": "#93c5fd", "G": "#86efac", "R": "#fca5a5", "Y": "#fde68a"}
NAME = {"P": "pink", "B": "blue", "G": "green", "R": "red", "Y": "yellow"}


def _grid():
    s, x0, y0 = 52, 20, 16
    b = ""
    for r in range(5):
        for c in range(5):
            k = GRID[r][c]; n = 5 * r + c + 1
            x, y = x0 + c * s, y0 + (4 - r) * s
            b += f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{FILL[k]}" stroke="{INK}" stroke-width="1.5"/>'
            b += _t(x + s / 2, y + 20, str(n), 13, bold=True) + _t(x + s / 2, y + 38, NAME[k], 10, col=INK)
    alt = "A 5 by 5 grid of coloured squares numbered 1 to 25, starting at the bottom-left and going left to right along each row, then up. " + \
          "; ".join(f"row {r + 1} from the bottom: " + ", ".join(f"{5 * r + c + 1} {NAME[GRID[r][c]]}" for c in range(5)) for r in range(5)) + "."
    return charts.raw("sipe_SM07_DILR_S1", 300, 296, b, alt)
CUBEGRID = _grid()

_lab = {7.142857142857143: "7 1/7", 18.333333333333332: "18 1/3"}
GROWTH = charts.vbar("sipe_SM07_DILR_S2", ["N", "N", "N", "K", "K", "K", "P", "P", "P", "P"],
                     [("Growth", [15, 23, 25, 100 / 14, 25, 30, 8, 10, 55 / 3, 25])], 35, 5,
                     "Bar chart of sales growth in 2022 over 2021, in per cent, in ascending order within each category. Non-perishable (N): 15, 23, 25. Kitchen Items (K): 7 1/7, 25, 30. Processed Items (P): 8, 10, 18 1/3, 25.",
                     ylabel="Growth (%)", h=300, fmt=lambda v: _lab.get(v, f"{v:g}"))
