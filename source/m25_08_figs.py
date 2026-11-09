# -*- coding: utf-8 -*-
"""Figures for Simp Mock 8 (2025), written into media/ when imported."""
import math
import charts
from charts import _t
INK, MUT, GRID = "#111827", "#6b7280", "#e5e7eb"

WORK = charts.vbar("sipe_SM25-08_DILR_S1", ["AI &amp; Ethics", "Blockchain", "Quantum", "Cybersecurity", "Edge"],
                   [("SE", [40, 50, 30, 70, 60]), ("DS", [70, 60, 40, 90, 80]), ("ITSec", [90, 100, 60, 80, 70]), ("Only this workshop", [60, 80, 50, 100, 90])],
                   100, 25, "Grouped bars for five workshops: Software Engineers, Data Scientists and IT Security attendees, and the number who attended only that workshop",
                   ylabel="Number of employees", w=600)

def _scatter():
    w, h, left, top, bot, right = 560, 380, 56, 14, 48, 16
    x0, x1, y0, y1 = 130, 230, 25, 55
    X = lambda v: left + (w - left - right) * (v - x0) / (x1 - x0)
    Y = lambda v: top + (h - top - bot) * (y1 - v) / (y1 - y0)
    b = ""
    for v in range(x0, x1 + 1, 10):
        b += f'<line x1="{X(v):.1f}" y1="{top}" x2="{X(v):.1f}" y2="{h - bot}" stroke="{GRID}"/>' + _t(X(v), h - bot + 16, v, 11, col=MUT)
    for v in range(y0, y1 + 1, 5):
        b += f'<line x1="{left}" y1="{Y(v):.1f}" x2="{w - right}" y2="{Y(v):.1f}" stroke="{GRID}"/>' + _t(left - 6, Y(v) + 4, f"{v}%", 11, "end", MUT)
    pts = [("A", 140, 42, "1.05"), ("B", 200, 51, "0.85"), ("C", 152, 37.5, "0.95"), ("D", 205, 48, "0.8"), ("E", 220, 45, "1.1"), ("F", 180, 30, "1.08")]
    for n, rx, ry, e in pts:
        b += f'<circle cx="{X(rx):.1f}" cy="{Y(ry):.1f}" r="5" fill="#2563eb"/>'
        b += _t(X(rx) + 9, Y(ry) - 6, f"{n} ({e})", 12, "start", bold=True)
    b += _t(left + (w - left - right) / 2, h - 10, "Revenue in April 2025 (₹ lakh)", 11, col=MUT)
    b += _t(14, top + (h - top - bot) / 2, "Salary as % of revenue", 11, col=MUT, extra=f' transform="rotate(-90 14 {top + (h - top - bot) / 2})"')
    return charts.raw("sipe_SM25-08_DILR_S4", w, h, b, "Scatter plot of six companies: revenue against salary as a percentage of revenue, each labelled with its efficiency")
SCATTER = _scatter()

def _tangent():
    R = 70; cx, cy = 110, 150
    A = (cx - R, cy); B = (cx + R, cy)
    C = (cx + R * math.cos(math.radians(72)), cy - R * math.sin(math.radians(72)))
    # tangent at C meets line AB at Q and tangent at A (x = A.x) at P
    tx, ty = -(C[1] - cy), (C[0] - cx)  # direction perpendicular to OC
    tQ = (cy - C[1]) / ty; Q = (C[0] + tx * tQ, cy)
    tP = (A[0] - C[0]) / tx; Pp = (A[0], C[1] + ty * tP)
    seg = lambda U, V, wd=2: f'<line x1="{U[0]:.1f}" y1="{U[1]:.1f}" x2="{V[0]:.1f}" y2="{V[1]:.1f}" stroke="{INK}" stroke-width="{wd}"/>'
    Rr = (A[0], cy + 90)
    b = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += seg(Pp, Rr, 2.5) + seg(Pp, Q) + seg(A, Q) + seg(C, B)
    b += _t(B[0] - 22, B[1] - 8, "54°", 12)
    for s, (x, y), dx, dy in (("P", Pp, -14, 0), ("A", A, -14, 5), ("R", Rr, -14, 4), ("C", C, 0, -8), ("B", B, 2, 18), ("Q", Q, 12, 5)):
        b += _t(x + dx, y + dy, s, 15)
    w = int(Q[0] + 30)
    return charts.raw("sipe_SM25-08_QA_09", w, 260, b, "Circle with diameter AB extended to Q; tangent PR at A, and tangent from P touching the circle at C and meeting line AB at Q; chord CB drawn, angle ABC 54°")
TANGENT = _tangent()

def _strips():
    # rectangle ABCD (width 15) upright; strip EFGH (width 8) at 30° to the vertical
    s = 8; Ax, Ay = 100, 50; W, H = 15 * s, 50 * s
    b = f'<rect x="{Ax}" y="{Ay}" width="{W}" height="{H}" fill="none" stroke="{INK}" stroke-width="2"/>'
    ux, uy = math.sin(math.radians(30)), -math.cos(math.radians(30))  # strip direction (up-right)
    nx, ny = math.cos(math.radians(30)), math.sin(math.radians(30))   # strip normal
    E = (Ax - 70, Ay + 350); L = 420
    # build strip corners: E (bottom-left), F = E + width*normal, G = F + L*dir, H = E + L*dir
    F = (E[0] + 8 * s * nx, E[1] + 8 * s * ny)
    Hh = (E[0] + L * ux, E[1] + L * uy); G = (F[0] + L * ux, F[1] + L * uy)
    b += f'<polygon points="{E[0]:.1f},{E[1]:.1f} {F[0]:.1f},{F[1]:.1f} {G[0]:.1f},{G[1]:.1f} {Hh[0]:.1f},{Hh[1]:.1f}" fill="none" stroke="{INK}" stroke-width="2"/>'
    def hit(P0, x):
        t = (x - P0[0]) / ux; return (x, P0[1] + uy * t)
    Pp, S = hit(E, Ax), hit(E, Ax + W); Qq, Rr = hit(F, Ax), hit(F, Ax + W)
    b += f'<polygon points="{Pp[0]:.1f},{Pp[1]:.1f} {Qq[0]:.1f},{Qq[1]:.1f} {Rr[0]:.1f},{Rr[1]:.1f} {S[0]:.1f},{S[1]:.1f}" fill="#dbeafe" stroke="none" opacity="0.8"/>'
    for t, (x, y), dx, dy in (("A", (Ax, Ay), -14, 0), ("B", (Ax, Ay + H), -14, 14), ("C", (Ax + W, Ay + H), 6, 14), ("D", (Ax + W, Ay), 6, 0),
                              ("E", E, -14, 4), ("F", F, -4, 16), ("G", G, 8, 4), ("H", Hh, -4, -6),
                              ("P", Pp, -14, 4), ("Q", Qq, -14, 10), ("R", Rr, 8, 8), ("S", S, 8, 0)):
        b += _t(x + dx, y + dy, t, 14)
    return charts.raw("sipe_SM25-08_QA_11", 350, 490, b, "Tall rectangle ABCD crossed by a slanted rectangular strip EFGH; the strip’s edges cut AB at P and Q and DC at S and R, making the shaded parallelogram PQRS")
STRIPS = _strips()

def _pencil():
    s = 22; y = 50; x0 = 56; Lc = 12 * s; r = s; Lt = 3 * s; cut = x0 + 9 * s
    b = f'<rect x="{x0}" y="{y - r}" width="{Lc}" height="{2 * r}" fill="#fde68a" stroke="{INK}" stroke-width="2"/>'
    b += f'<polygon points="{x0 + Lc},{y - r} {x0 + Lc + Lt},{y} {x0 + Lc},{y + r}" fill="#fef3c7" stroke="{INK}" stroke-width="2"/>'
    b += f'<line x1="{x0}" y1="{y + r + 16}" x2="{x0 + Lc}" y2="{y + r + 16}" stroke="{MUT}"/>' + _t(x0 + Lc / 2, y + r + 32, "12 cm", 12, col=MUT)
    b += f'<line x1="{x0 + Lc}" y1="{y + r + 16}" x2="{x0 + Lc + Lt}" y2="{y + r + 16}" stroke="{MUT}"/>' + _t(x0 + Lc + Lt / 2, y + r + 32, "3 cm", 12, col=MUT)
    b += _t(x0 - 2, y + 4, "2 cm", 11, "end", MUT)
    return charts.raw("sipe_SM25-08_QA_15", x0 + Lc + Lt + 16, y + r + 44, b, "A pencil: a cylinder 12 cm long and 2 cm across, ending in a cone 3 cm long")
PENCIL = _pencil()
