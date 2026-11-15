# -*- coding: utf-8 -*-
"""Figures for Simp Mock 12 (2025), written into media/ when imported."""
import math
import charts
from charts import _t
INK, MUT, GRID = "#111827", "#6b7280", "#e5e7eb"


def _seg(U, V, dash=None, w=2):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{U[0]:.1f}" y1="{U[1]:.1f}" x2="{V[0]:.1f}" y2="{V[1]:.1f}" stroke="{INK}" stroke-width="{w}"{d}/>'


def _dot(U):
    return f'<circle cx="{U[0]:.1f}" cy="{U[1]:.1f}" r="3" fill="{INK}"/>'


def _secant():
    cx, cy, r = 130, 130, 90
    P = (cx, cy); L = (cx - r, cy); R = (cx + r, cy)
    M = (cx + r * math.cos(math.radians(120)), cy - r * math.sin(math.radians(120)))
    N = (cx + r * math.cos(math.radians(20)), cy - r * math.sin(math.radians(20)))
    Q = (cx + 2 * r * math.cos(math.radians(20)), cy)
    b = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += _seg(L, Q) + _seg(M, Q) + _seg(L, M) + _seg(P, M) + _seg(P, N)
    for U in (P, L, R, M, N, Q): b += _dot(U)
    b += _t(L[0] - 12, L[1] + 5, "L", 15) + _t(P[0], P[1] + 20, "P", 15) + _t(R[0] + 10, R[1] + 20, "R", 15)
    b += _t(M[0] - 8, M[1] - 8, "M", 15) + _t(N[0] + 6, N[1] - 8, "N", 15) + _t(Q[0] + 8, Q[1] + 18, "Q", 15)
    return charts.raw("sipe_SM25-12_QA_17", int(Q[0] + 24), int(cy + r + 14), b,
                      "Circle with centre P and diameter LR. The line LR is extended beyond R to a point Q outside the circle. A line from Q cuts the circle at N and then at M. Segments LM, PM and PN are drawn.")
SECANT = _secant()


def _cube():
    s = 60  # px per a
    A = (30, 20); B = (30, 20 + 4 * s); C = (30 + 4 * s, 20 + 4 * s); D = (30 + 4 * s, 20)
    P = (30 + 3 * s, 20); Q = (30, 20 + 2 * s); R = (30 + 2 * s, B[1])
    S = (30 + 3 * s, B[1] - math.sqrt(3) * s)
    b = _seg(A, B) + _seg(B, C) + _seg(C, D) + _seg(D, A)
    b += _seg(Q, P, "8 5") + _seg(R, S, "8 5") + _seg(S, C, "8 5")
    for U in (P, Q, R, S): b += _dot(U)
    b += _t(A[0] - 12, A[1] + 4, "A", 15) + _t(B[0] - 12, B[1] + 6, "B", 15) + _t(C[0] + 12, C[1] + 6, "C", 15) + _t(D[0] + 12, D[1] + 4, "D", 15)
    b += _t(P[0], P[1] - 6, "P", 15) + _t(Q[0] - 12, Q[1] + 5, "Q", 15) + _t(R[0], R[1] + 20, "R", 15) + _t(S[0], S[1] - 10, "S", 15)
    return charts.raw("sipe_SM25-12_QA_18", int(D[0] + 30), int(B[1] + 30), b,
                      "Top face ABCD of a cube, with A top left, B bottom left, C bottom right and D top right. P is on AD and Q on AB, joined by a dashed cut PQ. R is on BC, and S is a point inside the face; dashed cuts RS and SC form a triangle with RC.")
CUBE = _cube()


def _hexagon():
    cx, cy, r = 150, 140, 110
    pts = {}
    names = ["Q", "R", "S", "T", "U", "P"]
    angs = [150, 90, 30, -30, -90, -150]
    for n, a in zip(names, angs):
        pts[n] = (cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a)))
    A = (cx, cy)
    P, Q, R, U = pts["P"], pts["Q"], pts["R"], pts["U"]
    D = ((Q[0] + A[0]) / 2, (Q[1] + A[1]) / 2); Bm = ((P[0] + A[0]) / 2, (P[1] + A[1]) / 2)
    C = ((P[0] + Q[0] + A[0]) / 3, (P[1] + Q[1] + A[1]) / 3)
    b = "".join(_seg(pts[names[i]], pts[names[(i + 1) % 6]]) for i in range(6))
    b += _seg(P, R, w=1.6) + _seg(Q, U, w=1.6) + _seg(Q, A, w=1.6) + _seg(P, A, w=1.6)
    b += f'<polygon points="{A[0]:.1f},{A[1]:.1f} {D[0]:.1f},{D[1]:.1f} {C[0]:.1f},{C[1]:.1f} {Bm[0]:.1f},{Bm[1]:.1f}" fill="#bfdbfe" fill-opacity="0.6"/>'
    for n, (x, y) in pts.items():
        dx = -14 if x < cx - 5 else (14 if x > cx + 5 else 0); dy = -8 if y < cy - 5 else (20 if y > cy + 5 else 5)
        b += _t(x + dx, y + dy, n, 15)
    b += _t(A[0] + 12, A[1] + 5, "A", 15) + _t(D[0] + 4, D[1] - 8, "D", 14) + _t(C[0] - 14, C[1] + 4, "C", 14) + _t(Bm[0] + 2, Bm[1] + 18, "B", 14)
    return charts.raw("sipe_SM25-12_QA_19", int(cx + r + 30), int(cy + r + 30), b,
                      "Regular hexagon with vertices Q, R, S, T, U, P going clockwise from the top left, and centre A. Segments PR, QU, QA and PA are drawn. PR meets QA at D, QU meets PA at B, and PR meets QU at C. The quadrilateral ABCD is shaded.")
HEX = _hexagon()
