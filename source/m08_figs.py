# -*- coding: utf-8 -*-
"""Figures for Simp Mock 8, written into media/ when imported."""
import charts
from charts import _t
INK, MUT = "#111827", "#6b7280"


def _circles():
    k, x0, y0 = 5, 20, 20                      # 56 × 28 cm rectangle at 5 px per cm
    X = lambda x: x0 + k * x; Y = lambda y: y0 + k * (28 - y)
    b = f'<rect x="{X(0)}" y="{Y(28)}" width="{56 * k}" height="{28 * k}" fill="none" stroke="{INK}" stroke-width="2"/>'
    for cx, n in ((14, "C₁"), (42, "C₂")):
        b += f'<circle cx="{X(cx)}" cy="{Y(14)}" r="{14 * k}" fill="none" stroke="{INK}" stroke-width="1.8"/>'
        b += f'<circle cx="{X(cx)}" cy="{Y(14)}" r="2.5" fill="{INK}"/>' + _t(X(cx), Y(14) + 16, n, 13)
    b += f'<circle cx="{X(28)}" cy="{Y(24.5)}" r="{3.5 * k}" fill="#d1d5db" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<circle cx="{X(28)}" cy="{Y(24.5)}" r="2" fill="{INK}"/>' + _t(X(28), Y(24.5) + 13, "O", 11)
    for x, y, n, dx, dy in ((0, 28, "A", -10, -2), (56, 28, "B", 10, -2), (56, 0, "C", 10, 12), (0, 0, "D", -10, 12)):
        b += _t(X(x) + dx, Y(y) + dy, n, 14)
    return charts.raw("sipe_SM08_QA_19", 330, 186, b,
                      "Rectangle ABCD, 56 by 28, with two equal circles centred C1 and C2 side by side, each touching three sides. A small shaded circle centred O sits in the gap above where they meet, touching both circles and side AB.")
CIRC = _circles()
