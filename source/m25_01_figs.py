# -*- coding: utf-8 -*-
"""Figures for Simp Mock 1 (2025) QA, written into media/ when imported."""
import math
import charts
INK = "#111827"
def _pt(x, y, lab, dx=0, dy=-8, anchor="middle"):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{INK}"/><text x="{x+dx:.1f}" y="{y+dy:.1f}" font-size="15" text-anchor="{anchor}" fill="{INK}">{lab}</text>'
def _ln(a, b, w=2): return f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{INK}" stroke-width="{w}"/>'
def _inter(p1, d1, p2, d2):
    (x1, y1), (a1, b1), (x2, y2), (a2, b2) = p1, d1, p2, d2
    t = ((x2 - x1) * b2 - (y2 - y1) * a2) / (a1 * b2 - b1 * a2)
    return (x1 + a1 * t, y1 + b1 * t)
def ang(deg): return (math.cos(math.radians(deg)), -math.sin(math.radians(deg)))
# Q17
C, B, A = (30, 115), (150, 115), (280, 115)
D = _inter(C, ang(40), B, ang(110)); E = _inter(C, ang(20), B, ang(55))
body = _ln(C, (315, 115)) + f'<polygon points="315,115 305,110 305,120" fill="{INK}"/>' + _ln(C, D) + _ln(B, D) + _ln(C, E) + _ln(B, E)
body += _pt(*C, "C", dy=20) + _pt(*B, "B", dy=20) + _pt(*A, "A", dy=20) + _pt(*D, "D") + _pt(*E, "E", dx=10, dy=-6)
Q17 = charts.raw("sipe_SM25-01_QA_17", 330, 140, body, "Line C B A with an arrow past A; D above, joined to C and B; E joined to C and B, to the right of D")
# Q18
A2, B2, C2 = (100, 20), (20, 230), (260, 230); P2 = (100, 230)
E2 = (A2[0] + (B2[0] - A2[0]) / 3, A2[1] + (B2[1] - A2[1]) / 3); D2 = (A2[0] + (C2[0] - A2[0]) / 3, A2[1] + (C2[1] - A2[1]) / 3)
O2 = _inter(B2, (D2[0] - B2[0], D2[1] - B2[1]), C2, (E2[0] - C2[0], E2[1] - C2[1]))
body = _ln(A2, B2) + _ln(B2, C2) + _ln(C2, A2) + _ln(A2, P2, 1.5) + _ln(B2, D2, 1.5) + _ln(C2, E2, 1.5)
body += f'<polyline points="100,220 110,220 110,230" fill="none" stroke="{INK}" stroke-width="1.2"/>'
body += _pt(*A2, "A") + _pt(*B2, "B", dx=-8, dy=6, anchor="end") + _pt(*C2, "C", dx=8, dy=6, anchor="start") + _pt(*P2, "P", dy=20)
body += _pt(*E2, "E", dx=-8, dy=4, anchor="end") + _pt(*D2, "D", dx=8, dy=0, anchor="start") + _pt(*O2, "O", dx=8, dy=16, anchor="start")
Q18 = charts.raw("sipe_SM25-01_QA_18", 290, 260, body, "Triangle ABC with altitude AP to BC; E on AB and D on AC; BD and CE cross at O")
