# -*- coding: utf-8 -*-
"""Figures for Simp Mock 17 (2025), written into media/ when imported."""
import charts
from charts import _t
INK, MUT = "#111827", "#6b7280"

MONTHS = ["March", "April", "May", "June", "July"]
PROFIT = [("Awesome", [10, 15, 10, 20, 5]), ("Credible", [15, 10, 20, 5, 10]), ("Horizon", [25, 5, 15, 10, 20])]
PCT = charts.line("sipe_SM25-17_DILR_S1", MONTHS, PROFIT, 0, 30, 5,
                  "Line chart of percentage profit per shirt at three outlets, March to July. "
                  + "; ".join(f"{n}: {', '.join(str(v) + '%' for v in vs)}" for n, vs in PROFIT),
                  ylabel="% profit", fmt=lambda v: f"{v}")


def _towers():
    g = 270  # ground y
    sx = 0.62  # px per metre
    xA, xB, xC = 40, 40 + 100 * sx, 40 + 500 * sx
    hA, hB, hC = 100 * sx, 80 * sx, 400 * sx
    seg = lambda a, b, w=2: f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{INK}" stroke-width="{w}"/>'
    b = seg((20, g), (xC + 20, g))
    b += seg((xA, g), (xA, g - hA), 3) + seg((xB, g), (xB, g - hB), 3) + seg((xC, g), (xC, g - hC), 3)
    b += seg((xA, g), (xC, g - hC), 1.4) + seg((xC, g), (xA, g - hA), 1.4)
    b += _t(xA, g + 18, "A", 13, bold=True) + _t(xB, g + 18, "B", 13, bold=True) + _t(xC, g + 18, "C", 13, bold=True)
    b += _t(xA - 4, g - hA - 8, "100 m", 11, col=MUT) + _t(xB + 4, g - hB - 8, "80 m", 11, col=MUT)
    b += _t((xA + xB) / 2, g + 34, "100 m", 11, col=MUT) + _t(xA + 30, g - 6, "α", 13) + _t(xC - 30, g - 6, "β", 13)
    return charts.raw("sipe_SM25-17_QA_05", int(xC + 40), g + 44, b,
                      "Three vertical buildings on level ground: A (100 m) on the left, B (80 m) 100 m to its right, and C further right. "
                      "A line from the foot of A to the top of C passes through the top of B, at elevation α. A line from the foot of C to the top of A also passes through the top of B, at elevation β.")
TOWERS = _towers()
