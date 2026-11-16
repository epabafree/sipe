# -*- coding: utf-8 -*-
"""Figures for Simp Mock 2, written into media/ when imported."""
import math
import charts
from charts import _t
INK, MUT = "#111827", "#6b7280"

SHARE = charts.vbar("sipe_SM02_DILR_S1", ["W", "X", "Y", "Z"],
                    [("A", [20, 15, 25, 30]), ("B", [30, 20, 10, 10]), ("C", [25, 25, 20, 15]),
                     ("D", [10, 20, 25, 25]), ("E", [15, 20, 20, 20])], 35, 5,
                    "Grouped bars of each zone’s percentage share in each year. Year W: A 20, B 30, C 25, D 10, E 15. Year X: A 15, B 20, C 25, D 20, E 20. Year Y: A 25, B 10, C 20, D 25, E 20. Year Z: A 30, B 10, C 15, D 25, E 20.",
                    ylabel="Share of locomotives (%)", h=300)


def _grid():
    clues = {(2, 2): 2, (2, 3): 2, (3, 3): 3, (3, 4): 2, (4, 2): 2, (4, 4): 2}
    s, x0, y0 = 46, 50, 34
    b = ""
    for i in range(6):
        b += f'<line x1="{x0}" y1="{y0 + i * s}" x2="{x0 + 5 * s}" y2="{y0 + i * s}" stroke="{INK}" stroke-width="1.5"/>'
        b += f'<line x1="{x0 + i * s}" y1="{y0}" x2="{x0 + i * s}" y2="{y0 + 5 * s}" stroke="{INK}" stroke-width="1.5"/>'
    for i in range(5):
        b += _t(x0 + i * s + s / 2, y0 - 10, f"C{i + 1}", 12, col=MUT) + _t(x0 - 20, y0 + i * s + s / 2 + 4, f"R{i + 1}", 12, col=MUT)
    for (r, c), v in clues.items():
        b += _t(x0 + (c - 1) * s + s / 2, y0 + (r - 1) * s + s / 2 + 7, str(v), 20, bold=True)
    return charts.raw("sipe_SM02_DILR_S3", 300, 274, b,
                      "A 5 by 5 grid with rows R1 to R5 and columns C1 to C5. Numbers are shown in six cells: R2C2 = 2, R2C3 = 2, R3C3 = 3, R3C4 = 2, R4C2 = 2, R4C4 = 2. All other cells are blank.")
GRID = _grid()


def _hex():
    s, cx, cy = 80, 160, 125
    name = "PQRSTU"
    pts = {n: (cx + s * math.cos(math.radians(180 - 60 * k)), cy - s * math.sin(math.radians(180 - 60 * k))) for k, n in enumerate(name)}
    # P left, Q upper-left, R upper-right, S right, T lower-right, U lower-left
    lerp = lambda U, V, t: (U[0] + (V[0] - U[0]) * t, U[1] + (V[1] - U[1]) * t)
    A = lerp(pts["P"], pts["U"], 8 / 12); B = lerp(pts["S"], pts["R"], 8 / 12)
    seg = lambda U, V, c=INK, w=2: f'<line x1="{U[0]:.1f}" y1="{U[1]:.1f}" x2="{V[0]:.1f}" y2="{V[1]:.1f}" stroke="{c}" stroke-width="{w}"/>'
    b = "".join(seg(pts[a], pts[c]) for a, c in zip(name, name[1:] + name[0])) + seg(A, B, MUT)
    for n, (x, y) in pts.items():
        dx = -14 if x < cx - 5 else (14 if x > cx + 5 else 0); dy = -8 if y < cy - 5 else (18 if y > cy + 5 else 5)
        b += _t(x + dx, y + dy, n, 14)
    b += _t(A[0] - 12, A[1] + 12, "A", 14) + _t(B[0] + 12, B[1] - 2, "B", 14)
    for D in (A, B):
        b += f'<circle cx="{D[0]:.1f}" cy="{D[1]:.1f}" r="3" fill="{INK}"/>'
    return charts.raw("sipe_SM02_QA_3", 320, 250, b,
                      "Regular hexagon PQRSTU with P on the left, Q and R along the top, S on the right, T and U along the bottom. Point A is on side PU and point B is on side RS, and the segment AB is drawn.")
HEX = _hex()


def _square():
    k, x0, y0 = 38, 40, 20
    Bp = (x0, y0 + 6 * k); C = (x0 + 6 * k, y0 + 6 * k); A = (x0, y0); D = (x0 + 6 * k, y0)
    X = (x0 + 1.5 * k, y0 + 6 * k - 1.5 * math.sqrt(3) * k); P = (X[0], y0)
    seg = lambda U, V, c=INK, w=2: f'<line x1="{U[0]:.1f}" y1="{U[1]:.1f}" x2="{V[0]:.1f}" y2="{V[1]:.1f}" stroke="{c}" stroke-width="{w}"/>'
    b = seg(A, Bp) + seg(Bp, C) + seg(C, D) + seg(D, A) + seg(Bp, X, MUT) + seg(X, P, MUT) + seg(X, D, MUT)
    b += f'<polyline points="{P[0]:.1f},{P[1] + 9:.1f} {P[0] + 9:.1f},{P[1] + 9:.1f} {P[0] + 9:.1f},{P[1]:.1f}" fill="none" stroke="{INK}"/>'
    b += _t(A[0] - 10, A[1] + 4, "A", 14) + _t(Bp[0] - 10, Bp[1] + 6, "B", 14) + _t(C[0] + 10, C[1] + 6, "C", 14) + _t(D[0] + 10, D[1] + 4, "D", 14)
    b += _t(X[0] - 12, X[1] + 4, "X", 14) + _t(P[0], P[1] - 6, "P", 14)
    return charts.raw("sipe_SM02_QA_12", 320, 270, b,
                      "Square ABCD with A top-left, B bottom-left, C bottom-right and D top-right. X is a point inside joined to B. P is on AD directly above X, so XP is perpendicular to AD, and X is joined to D.")
SQ = _square()
