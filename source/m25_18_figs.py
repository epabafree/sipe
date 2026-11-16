# -*- coding: utf-8 -*-
"""Figures for Simp Mock 18 (2025), written into media/ when imported."""
import math
import charts
from charts import _t
INK, MUT = "#111827", "#6b7280"

AGES = charts.vbar("sipe_SM25-18_DILR_S1", ["A", "B", "C", "D"], [("Minimum age", [27, 32, 24, 30]), ("Maximum age", [41, 35, 38, 33])], 45, 5,
                   "Grouped bars of the youngest and oldest participant’s age in each department: A 27 and 41, B 32 and 35, C 24 and 38, D 30 and 33.",
                   ylabel="Age (years)")


def _hex():
    s = 70
    cx, cy = 160, 150
    pts = {}
    # flat left and right sides: B, C on the left, F, E on the right, A top, D bottom
    for n, a in zip("ABCDEF", (90, 150, 210, 270, 330, 30)):
        pts[n] = (cx + s * math.cos(math.radians(a)), cy - s * math.sin(math.radians(a)))
    B, F, A = pts["B"], pts["F"], pts["A"]
    K = (B[0] + s, B[1])
    # H on AF directly above K
    t = (K[0] - A[0]) / (F[0] - A[0]); H = (K[0], A[1] + t * (F[1] - A[1]))
    seg = lambda U, V, w=2: f'<line x1="{U[0]:.1f}" y1="{U[1]:.1f}" x2="{V[0]:.1f}" y2="{V[1]:.1f}" stroke="{INK}" stroke-width="{w}"/>'
    b = "".join(seg(pts[x], pts[y]) for x, y in zip("ABCDEF", "BCDEFA")) + seg(B, F) + seg(H, K)
    b += f'<polyline points="{K[0] - 9:.1f},{K[1]:.1f} {K[0] - 9:.1f},{K[1] - 9:.1f} {K[0]:.1f},{K[1] - 9:.1f}" fill="none" stroke="{INK}"/>'
    for n, (x, y) in pts.items():
        dx = -12 if x < cx - 5 else (12 if x > cx + 5 else 0); dy = -8 if y < cy - 5 else (18 if y > cy + 5 else 5)
        b += _t(x + dx, y + dy, n, 14)
    b += _t(H[0] + 8, H[1] - 6, "H", 14) + _t(K[0], K[1] + 17, "K", 14)
    return charts.raw("sipe_SM25-18_QA_10", 320, 245, b,
                      "Regular hexagon ABCDEF with A at the top, B and C on the left, D at the bottom, E and F on the right. Diagonal BF is drawn. K is on BF and H on side AF, with HK perpendicular to BF.")
HEX = _hex()
