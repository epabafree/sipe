# -*- coding: utf-8 -*-
"""Figures for Simp Mock 19 (2025), written into media/ when imported."""
import charts
from charts import _t
INK, MUT = "#111827", "#6b7280"


def _trap():
    k = 3.5
    D = (50, 180); C = (D[0] + 60 * k, 180); B = (C[0], 180 - 40 * k); A = (B[0] - 30 * k, B[1])
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in (A, B, C, D))
    b = f'<polygon points="{poly}" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += f'<circle cx="{C[0] - 20 * k:.1f}" cy="{180 - 20 * k:.1f}" r="{20 * k:.1f}" fill="none" stroke="{MUT}" stroke-width="1.6"/>'
    b += f'<polyline points="{B[0] - 10:.1f},{B[1]:.1f} {B[0] - 10:.1f},{B[1] + 10:.1f} {B[0]:.1f},{B[1] + 10:.1f}" fill="none" stroke="{INK}"/>'
    b += _t(A[0] - 6, A[1] - 8, "A", 14) + _t(B[0] + 8, B[1] - 8, "B", 14) + _t(C[0] + 10, C[1] + 16, "C", 14) + _t(D[0] - 10, D[1] + 16, "D", 14)
    b += _t((A[0] + B[0]) / 2, A[1] - 8, "30", 13, col=MUT) + _t((C[0] + D[0]) / 2, D[1] + 18, "60", 13, col=MUT)
    return charts.raw("sipe_SM25-19_QA_1", 320, 210, b,
                      "Trapezium ABCD with the short side AB = 30 on top and the long side CD = 60 at the bottom. BC is vertical with a right angle at B, AD slants down to the left, and a circle inside touches all four sides.")
TRAP = _trap()
