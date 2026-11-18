# -*- coding: utf-8 -*-
"""Figures for Simp Mock 5, written into media/ when imported."""
import math
import charts
from charts import _t, GRID, PAL
INK, MUT = "#111827", "#6b7280"

# Bubble chart: (diameter in units, revenue change %, cost change %); 1 unit = 2.5 %.
BUB = {"A": (2, 20, 10), "B": (1, 10, -12.5), "C": (3, -10, -5), "D": (3, 10, -2.5), "E": (4, 10, 12.5),
       "F": (5, 25, 17.5), "G": (4, -10, -15), "H": (3, 12.5, 25), "I": (2, -10, -40), "J": (1, -10, 30)}


def _bubbles():
    k = 5.2                        # px per 1 %
    x0, x1, y0, y1 = -20, 35, -45, 35
    L, T = 52, 14
    W, H = L + k * (x1 - x0) + 16, T + k * (y1 - y0) + 46
    X = lambda v: L + k * (v - x0)
    Y = lambda v: T + k * (y1 - v)
    b = ""
    for v in range(x0, x1 + 1, 5):
        b += f'<line x1="{X(v):.1f}" y1="{Y(y1):.1f}" x2="{X(v):.1f}" y2="{Y(y0):.1f}" stroke="{GRID if v else MUT}" stroke-width="{1 if v else 1.4}"/>'
        if v % 10 == 0:
            b += _t(X(v), Y(y0) + 14, f"{v}", 10, col=MUT)
    for v in range(y0, y1 + 1, 5):
        b += f'<line x1="{X(x0):.1f}" y1="{Y(v):.1f}" x2="{X(x1):.1f}" y2="{Y(v):.1f}" stroke="{GRID if v else MUT}" stroke-width="{1 if v else 1.4}"/>'
        if v % 10 == 0:
            b += _t(X(x0) - 5, Y(v) + 4, f"{v}", 10, "end", col=MUT)
    for i, (n, (d, x, y)) in enumerate(BUB.items()):
        r = d * 2.5 * k / 2
        b += f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="{r:.1f}" fill="{PAL[i % len(PAL)]}" fill-opacity="0.28" stroke="{PAL[i % len(PAL)]}" stroke-width="1.3"/>'
        b += f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="1.8" fill="{INK}"/>' + _t(X(x) + 7, Y(y) - 4, n, 11, "start", bold=True)
    b += _t((X(x0) + X(x1)) / 2, Y(y0) + 32, "Change in revenue (%)", 11, col=MUT)
    b += _t(14, (Y(y0) + Y(y1)) / 2, "Change in cost (%)", 11, col=MUT, extra=f' transform="rotate(-90 14 {(Y(y0) + Y(y1)) / 2:.1f})"')
    alt = "Bubble chart of ten products A to J. Horizontal axis: change in revenue (%), vertical axis: change in cost (%), grid squares 5 % wide. " + \
          "; ".join(f"{n}: centre ({x}, {y}), diameter {d} unit{'s' if d > 1 else ''}" for n, (d, x, y) in BUB.items()) + "."
    return charts.raw("sipe_SM05_DILR_S2", round(W), round(H), b, alt)
BUBBLES = _bubbles()


def _lune():
    s, cx, cy = 3.2, 150, 175           # big circle radius 42 → 134 px
    R, r = 42, 21
    P = lambda a, rad=R: (cx + s * rad * math.cos(math.radians(a)), cy - s * rad * math.sin(math.radians(a)))
    A, C, B, Pp = P(180), P(0), P(60), P(115)
    M = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
    ang = math.degrees(math.atan2(-(M[1] - cy), M[0] - cx))
    Q = (M[0] + s * r * math.cos(math.radians(ang)), M[1] - s * r * math.sin(math.radians(ang)))
    shade = (f'<path d="M {B[0]:.1f} {B[1]:.1f} A {s * r:.1f} {s * r:.1f} 0 0 1 {C[0]:.1f} {C[1]:.1f} '
             f'A {s * R:.1f} {s * R:.1f} 0 0 0 {B[0]:.1f} {B[1]:.1f} Z" fill="#9ca3af" fill-opacity="0.55" stroke="none"/>')
    b = shade
    b += f'<path d="M {C[0]:.1f} {C[1]:.1f} A {s * R:.1f} {s * R:.1f} 0 0 0 {A[0]:.1f} {A[1]:.1f}" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += f'<line x1="{A[0]:.1f}" y1="{A[1]:.1f}" x2="{C[0]:.1f}" y2="{C[1]:.1f}" stroke="{INK}" stroke-width="2"/>'
    b += f'<path d="M {B[0]:.1f} {B[1]:.1f} A {s * r:.1f} {s * r:.1f} 0 0 1 {C[0]:.1f} {C[1]:.1f}" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += f'<line x1="{B[0]:.1f}" y1="{B[1]:.1f}" x2="{C[0]:.1f}" y2="{C[1]:.1f}" stroke="{MUT}" stroke-width="1.3" stroke-dasharray="4 3"/>'
    for X_, n, dx, dy in ((A, "A", -8, 5), (C, "C", 12, 5), (B, "B", -6, -9), (Pp, "P", -8, -7), (Q, "Q", 10, -2)):
        b += _t(X_[0] + dx, X_[1] + dy, n, 14)
    b += f'<circle cx="{cx}" cy="{cy}" r="2.5" fill="{INK}"/>' + _t(cx, cy + 16, "O", 13)
    return charts.raw("sipe_SM05_QA_7", 330, 200, b,
                      "Semicircle APBC on diameter AC with centre O. B is on the arc, and a smaller semicircle BQC is drawn outward on chord BC. The shaded crescent lies inside the small semicircle and outside the large one.")
LUNE = _lune()
