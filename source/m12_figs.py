# -*- coding: utf-8 -*-
"""Figures for Simp Mock 12, written into media/ when imported."""
import math
import charts
from charts import _t
INK, MUT = "#111827", "#6b7280"

TRIPLES = ["C+N+U", "C+N+O", "C+N+E", "C+U+O", "C+U+E", "C+O+E", "N+U+O", "N+U+E", "N+O+E", "U+O+E"]
SUMS = [300, 280, 260, 260, 240, 220, 300, 280, 260, 240]
DOCS = charts.vbar("sipe_SM12_DILR_S2", TRIPLES, [("Doctors", SUMS)], 320, 40,
                   "Bar chart of the number of doctors in three categories taken together: C+N+U 300, C+N+O 280, C+N+E 260, C+U+O 260, C+U+E 240, C+O+E 220, N+U+O 300, N+U+E 280, N+O+E 260, U+O+E 240.",
                   ylabel="Doctors (three categories together)")


def _quad():
    k, ox, oy = 26, 120, 100
    P_ = lambda x, y: (ox + k * x, oy - k * y)
    A = (-3, 0); B = (3, 0); C = (1, 2 * math.sqrt(2)); t = math.radians(-110); D = (3 * math.cos(t), 3 * math.sin(t))
    # P = AB ∩ CD (on y = 0)
    s = C[1] / (C[1] - D[1]); Px = C[0] + s * (D[0] - C[0])
    pts = {"A": A, "B": B, "C": C, "D": D, "P": (Px, 0)}
    b = ""
    for u, v in (("A", "B"), ("B", "C"), ("C", "A"), ("A", "D"), ("C", "D")):
        (x1, y1), (x2, y2) = P_(*pts[u]), P_(*pts[v])
        b += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{INK}" stroke-width="1.8"/>'
    off = {"A": (-12, 4), "B": (12, 4), "C": (4, -8), "D": (-6, 16), "P": (8, 14)}
    for n, (x, y) in pts.items():
        X, Y = P_(x, y); b += f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="2.5" fill="{INK}"/>' + _t(X + off[n][0], Y + off[n][1], n, 13, bold=True)
    cx, cy = P_(*C)
    b += f'<path d="M {cx - 9:.1f} {cy + 2:.1f} l 6 6 l 7 -5" fill="none" stroke="{MUT}"/>'
    return charts.raw("sipe_SM12_QA_14", 240, 190, b,
                      "Triangle ABC with a right angle at C. Point D lies on the other side of AB from C; segments AD and CD are drawn, and CD crosses AB at P.")
QUAD = _quad()
