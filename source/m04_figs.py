# -*- coding: utf-8 -*-
"""Figures for Simp Mock 4, written into media/ when imported."""
import math
import charts
from charts import _t
INK, MUT = "#111827", "#6b7280"


def _seg(U, V, c=INK, w=2):
    return f'<line x1="{U[0]:.1f}" y1="{U[1]:.1f}" x2="{V[0]:.1f}" y2="{V[1]:.1f}" stroke="{c}" stroke-width="{w}"/>'


def _two_circles():
    s, ox, oy = 9.5, 145, 24          # P at the origin, y downwards
    T = lambda x, y: (ox + s * x, oy + s * y)
    O1, r1 = (-6.0, 13.0), math.sqrt(61)
    O2, r2 = (8.0, 13.0), math.sqrt(89)
    # tangent point A on circle 1 (left side)
    d1 = math.hypot(*O1); a = math.atan2(O1[1], O1[0]); ang = math.asin(r1 / d1)
    tdir = (math.cos(a + ang), math.sin(a + ang)); A = (12 * tdir[0], 12 * tdir[1])
    # secant direction making d.O2 = 12.5, rotated clockwise from O2's direction
    d2 = math.hypot(*O2); b = math.atan2(O2[1], O2[0]); th = math.acos(12.5 / d2)
    u = (math.cos(b - th), math.sin(b - th)); D = (9 * u[0], 9 * u[1]); E = (16 * u[0], 16 * u[1])
    P, B, C = (0, 0), (0, 8), (0, 18)
    body = f'<circle cx="{T(*O1)[0]:.1f}" cy="{T(*O1)[1]:.1f}" r="{s * r1:.1f}" fill="none" stroke="{INK}" stroke-width="2"/>'
    body += f'<circle cx="{T(*O2)[0]:.1f}" cy="{T(*O2)[1]:.1f}" r="{s * r2:.1f}" fill="none" stroke="{INK}" stroke-width="2"/>'
    body += _seg(T(*P), T(*C), MUT) + _seg(T(*P), T(*A), MUT) + _seg(T(*P), T(*E), MUT)
    for Q in (P, A, B, C, D, E, O1, O2):
        X = T(*Q); body += f'<circle cx="{X[0]:.1f}" cy="{X[1]:.1f}" r="2.8" fill="{INK}"/>'
    lab = lambda Q, t, dx, dy: _t(T(*Q)[0] + dx, T(*Q)[1] + dy, t, 14)
    body += lab(P, "P", 0, -8) + lab(A, "A", -12, 2) + lab(B, "B", -11, 4) + lab(C, "C", -11, 16) + lab(D, "D", 11, -3) + lab(E, "E", 11, 4)
    body += _t(T(*O1)[0] - 4, T(*O1)[1] + 16, "O₁", 13) + _t(T(*O2)[0] + 4, T(*O2)[1] + 16, "O₂", 13)
    return charts.raw("sipe_SM04_QA_20", 320, 250, body,
                      "Two overlapping circles with centres O1 (left) and O2 (right) meet at B and C. P lies above them on line CB extended. PA touches the left circle at A, and a line from P cuts the right circle at D and then E.")
CIRC2 = _two_circles()
