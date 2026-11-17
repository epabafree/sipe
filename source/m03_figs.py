# -*- coding: utf-8 -*-
"""Figures for Simp Mock 3, written into media/ when imported."""
import math
import charts
from charts import _t
INK, MUT = "#111827", "#6b7280"

STOCK = charts.line("sipe_SM03_DILR_S3", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
                    [("Medicine L", [200, 171, 144, 108, 72, 36]), ("Medicine S", [200, 162, 117, 72, 54, 36])], 0, 220, 20,
                    "Line chart of opening stock from Monday to Saturday. Medicine L: 200, 171, 144, 108, 72, 36. Medicine S: 200, 162, 117, 72, 54, 36.",
                    ylabel="Opening stock (units)", show_values=False)


def _seg(U, V, c=INK, w=2):
    return f'<line x1="{U[0]:.1f}" y1="{U[1]:.1f}" x2="{V[0]:.1f}" y2="{V[1]:.1f}" stroke="{c}" stroke-width="{w}"/>'


def _circ():
    cx, cy, r = 160, 125, 95
    P = lambda deg: (cx + r * math.cos(math.radians(deg)), cy - r * math.sin(math.radians(deg)))
    A, B, C, D, O = P(105), P(180), P(240), P(0), (cx, cy)
    b = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += _seg(A, B) + _seg(B, C) + _seg(C, D) + _seg(D, A) + _seg(B, D, MUT, 1.5) + _seg(O, C, MUT, 1.5)
    b += f'<circle cx="{cx}" cy="{cy}" r="3" fill="{INK}"/>'
    b += _t(A[0] - 4, A[1] - 9, "A", 14) + _t(B[0] - 13, B[1] + 5, "B", 14) + _t(C[0] - 8, C[1] + 18, "C", 14) + _t(D[0] + 13, D[1] + 5, "D", 14) + _t(cx + 4, cy - 8, "O", 14)
    return charts.raw("sipe_SM03_QA_2", 320, 250, b,
                      "Circle with centre O. B and D are at the ends of a horizontal diameter, A is on the upper arc and C on the lower arc, and ABCD is drawn. OC is joined.")
CIRC = _circ()


def _ladders():
    k, x0, y0 = 16, 50, 230
    B, C = (x0, y0), (x0 + 13 * k, y0)
    A, D = (B[0], y0 - 12 * k), (C[0], y0 - 6 * k)
    t = 12 / 18  # AC and BD cross where MN = 4: M is 2/3 of the way from B to C
    M = (B[0] + t * (C[0] - B[0]), y0 - 4 * k); N = (M[0], y0)
    b = _seg(A, B) + _seg(B, C) + _seg(D, C) + _seg(A, C, MUT) + _seg(B, D, MUT) + _seg(M, N)
    for P, s in ((B, 1), (N, 1), (C, -1)):
        b += f'<polyline points="{P[0] + 9 * s:.1f},{P[1]:.1f} {P[0] + 9 * s:.1f},{P[1] - 9:.1f} {P[0]:.1f},{P[1] - 9:.1f}" fill="none" stroke="{INK}"/>'
    b += _t(A[0] - 12, A[1] + 4, "A", 14) + _t(B[0] - 12, B[1] + 6, "B", 14) + _t(C[0] + 12, C[1] + 6, "C", 14) + _t(D[0] + 12, D[1] + 4, "D", 14)
    b += _t(M[0], M[1] - 9, "M", 14) + _t(N[0], N[1] + 17, "N", 14)
    return charts.raw("sipe_SM03_QA_20", 320, 260, b,
                      "B and C on a horizontal base. AB stands up at B and DC, shorter, stands up at C. AC and BD cross at M, and MN is dropped perpendicular to BC.")
LAD = _ladders()
