# -*- coding: utf-8 -*-
"""Figures for Simp Mock 15 (2025), written into media/ when imported."""
import math
import charts
from charts import _t
INK, MUT = "#111827", "#6b7280"


def _seg(U, V, w=2, col=INK, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{U[0]:.1f}" y1="{U[1]:.1f}" x2="{V[0]:.1f}" y2="{V[1]:.1f}" stroke="{col}" stroke-width="{w}"{d}/>'


def _caves():
    W, H = 560, 420
    node = {"A-1": (150, 130), "A-2": (150, 290), "B-1": (290, 70), "B-2": (290, 160), "B-3": (290, 260), "B-4": (290, 350)}
    for i in range(8):
        node[f"C-{i + 1}"] = (430, 30 + i * 52)
    ent = (50, 210)
    edges = [("E", "A-1"), ("E", "A-2"), ("A-1", "B-1"), ("A-1", "B-2"), ("A-2", "B-3"), ("A-2", "B-4"),
             ("B-1", "C-1"), ("B-1", "C-2"), ("B-1", "C-3"), ("B-2", "C-4"), ("B-3", "C-5"), ("B-3", "C-6"), ("B-4", "C-7"), ("B-4", "C-8")]
    b = ""
    for u, v in edges:
        U = ent if u == "E" else node[u]
        b += _seg(U, node[v], 6, "#94a3b8") + _seg(U, node[v], 2.5, "#ffffff")
    for i in range(8):
        y = node[f"C-{i + 1}"][1]
        b += _seg((430, y), (505, y), 6, "#94a3b8") + _seg((430, y), (505, y), 2.5, "#ffffff")
        b += f'<polygon points="508,{y - 6} 520,{y} 508,{y + 6}" fill="{MUT}"/>' + _t(540, y + 4, "Exit", 11, col=MUT)
    b += f'<rect x="{ent[0] - 40}" y="{ent[1] - 18}" width="72" height="36" rx="4" fill="#ffffff" stroke="{INK}" stroke-width="2"/>' + _t(ent[0] - 4, ent[1] + 4, "Entrance", 11, bold=True)
    for n, (x, y) in node.items():
        b += f'<circle cx="{x}" cy="{y}" r="21" fill="#ffffff" stroke="{INK}" stroke-width="2"/>' + _t(x, y + 4, n, 12, bold=True)
    return charts.raw("sipe_SM25-15_DILR_S4", W, H, b,
                      "Cave map. The entrance leads to A-1 and A-2. A-1 leads to B-1 and B-2; A-2 leads to B-3 and B-4. B-1 leads to C-1, C-2 and C-3; B-2 to C-4; B-3 to C-5 and C-6; B-4 to C-7 and C-8. Each C cave leads to its own exit.")
CAVES = _caves()


def _orth():
    A, B, O, D, C = (110, 20), (40, 120), (110, 155), (110, 215), (260, 215)
    b = _seg(A, D) + _seg(A, B) + _seg(B, C) + _seg(D, C)
    b += f'<polyline points="110,201 124,201 124,215" fill="none" stroke="{INK}"/>'
    # right angle at B (between BA and BC)
    ba = (A[0] - B[0], A[1] - B[1]); bc = (C[0] - B[0], C[1] - B[1])
    nb = math.hypot(*ba); nc = math.hypot(*bc)
    u = (ba[0] / nb * 12, ba[1] / nb * 12); v = (bc[0] / nc * 12, bc[1] / nc * 12)
    b += f'<polyline points="{B[0] + u[0]:.1f},{B[1] + u[1]:.1f} {B[0] + u[0] + v[0]:.1f},{B[1] + u[1] + v[1]:.1f} {B[0] + v[0]:.1f},{B[1] + v[1]:.1f}" fill="none" stroke="{INK}"/>'
    b += _t(110, 14, "A", 14) + _t(28, 120, "B", 14) + _t(124, 150, "O", 14) + _t(110, 234, "D", 14) + _t(270, 232, "C", 14)
    return charts.raw("sipe_SM25-15_QA_04", 290, 245, b,
                      "AD is vertical with O on it and D at the bottom; BC passes through O. Angle ABC (at B) and angle ADC (at D) are right angles. Triangles AOB and COD sit on either side of O.")
ORTH = _orth()


def _chord():
    cx, cy, r = 150, 165, 130
    yS = 85
    dx = math.sqrt(r * r - (cy - yS) ** 2)
    P, Q = (cx - dx, yS), (cx + dx, yS)
    S = (P[0] + (Q[0] - P[0]) * 84 / 204, yS); R = (S[0], cy - math.sqrt(r * r - (S[0] - cx) ** 2))
    b = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="2"/>' + _seg(P, Q) + _seg(S, R)
    b += f'<polyline points="{S[0]:.1f},{yS - 10} {S[0] + 10:.1f},{yS - 10} {S[0] + 10:.1f},{yS}" fill="none" stroke="{INK}"/>'
    b += _t(P[0] - 10, yS + 4, "P", 14) + _t(Q[0] + 10, yS + 4, "Q", 14) + _t(S[0], yS + 18, "S", 14) + _t(R[0], R[1] - 6, "R", 14)
    b += _t((P[0] + S[0]) / 2, yS + 18, "84", 12, col=MUT) + _t((S[0] + Q[0]) / 2, yS + 18, "120", 12, col=MUT) + _t(S[0] + 16, yS - 18, "35", 12, col=MUT)
    return charts.raw("sipe_SM25-15_QA_05", 300, 300, b,
                      "Circle with chord PQ near the top. S is on PQ with PS = 84 and SQ = 120. R is on the circle above S, with RS = 35 perpendicular to PQ.")
CHORD = _chord()


def _iso():
    Q, S, P = (30, 200), (330, 200), (180, 20)
    R = (130, 200)
    t = 0.62; T = (P[0] + (S[0] - P[0]) * t, P[1] + (S[1] - P[1]) * t)
    b = _seg(P, Q) + _seg(Q, S) + _seg(S, P) + _seg(P, R) + _seg(R, T)
    b += _t(180, 14, "P", 14) + _t(20, 214, "Q", 14) + _t(340, 214, "S", 14) + _t(130, 218, "R", 14) + _t(T[0] + 12, T[1] - 2, "T", 14)
    b += _t(162, 62, "40°", 11, col=MUT)
    return charts.raw("sipe_SM25-15_QA_19", 360, 230, b,
                      "Isosceles triangle PQS with PQ = PS and base QS. R is on QS and T on PS, joined by RT; PR is drawn. Angle QPR is 40 degrees.")
ISO = _iso()
