# -*- coding: utf-8 -*-
"""Figures for Simp Mock 13 (2025), written into media/ when imported."""
import charts
from charts import _t
INK, MUT, GRID = "#111827", "#6b7280", "#e5e7eb"

LEADERS = ["Tandon", "Ellis", "Joshi", "Nair", "Kapoor", "Rao", "Chopra", "Bose", "Oberoi", "Tiwari"]
PTS = {"Economy": [80, 90, 50, 40, 10, 60, 100, 20, 70, 30], "Foreign Affairs": [90, 100, 20, 70, 40, 80, 60, 30, 10, 50],
       "Social Schemes": [80, 50, 100, 20, 70, 30, 90, 40, 60, 10], "Moral Authority": [80, 100, 90, 20, 70, 50, 30, 40, 60, 10]}
POINTS = charts.vbar("sipe_SM25-13_DILR_S1", LEADERS, list(PTS.items()), 100, 10,
                     "Grouped bars of points (out of 100) for ten leaders on Economy, Foreign Affairs, Social Schemes and Moral Authority. "
                     + "; ".join(f"{n}: {PTS['Economy'][i]}, {PTS['Foreign Affairs'][i]}, {PTS['Social Schemes'][i]}, {PTS['Moral Authority'][i]}" for i, n in enumerate(LEADERS)),
                     ylabel="Points", w=640, h=340, show_values=False)

GIVEN = {(1, 3): "E", (1, 5): "F", (1, 6): "B", (2, 1): "F", (2, 2): "D", (3, 1): "D", (3, 6): "E",
         (4, 1): "E", (4, 5): "D", (5, 3): "A", (5, 4): "B", (6, 6): "A"}
BLOCKS = [("HL", 1, 1), ("FL", 1, 4), ("BL", 3, 1), ("PL", 3, 4), ("GL", 5, 1), ("UL", 5, 4)]


def _estate():
    c, x0, y0 = 46, 34, 26
    b = ""
    for name, r, col in BLOCKS:
        x, y = x0 + (col - 1) * c, y0 + (r - 1) * c
        b += f'<rect x="{x}" y="{y}" width="{3 * c}" height="{2 * c}" fill="#f8fafc"/>'
        b += _t(x + 1.5 * c, y + c + 8, name, 26, col="#cbd5e1", bold=True)
    for i in range(7):
        w = 3 if i in (0, 3, 6) else 1
        b += f'<line x1="{x0 + i * c}" y1="{y0}" x2="{x0 + i * c}" y2="{y0 + 6 * c}" stroke="{INK}" stroke-width="{w}"/>'
        w = 3 if i in (0, 2, 4, 6) else 1
        b += f'<line x1="{x0}" y1="{y0 + i * c}" x2="{x0 + 6 * c}" y2="{y0 + i * c}" stroke="{INK}" stroke-width="{w}"/>'
    for i in range(6):
        b += _t(x0 + (i + 0.5) * c, y0 - 8, f"C{i + 1}", 12, col=MUT) + _t(x0 - 16, y0 + (i + 0.5) * c + 4, f"R{i + 1}", 12, col=MUT)
    for (r, col), v in GIVEN.items():
        b += _t(x0 + (col - 0.5) * c, y0 + (r - 0.5) * c + 7, v, 20, bold=True)
    return charts.raw("sipe_SM25-13_DILR_S4", x0 + 6 * c + 10, y0 + 6 * c + 10, b,
                      "Six-by-six grid of plots, rows R1 to R6 and columns C1 to C6, in six blocks of two rows by three columns: "
                      "House Land (R1–R2, C1–C3), Farm Land (R1–R2, C4–C6), Barn Land (R3–R4, C1–C3), Pond Land (R3–R4, C4–C6), "
                      "Garden Land (R5–R6, C1–C3), Utility Land (R5–R6, C4–C6). Given owners: R1C3 E, R1C5 F, R1C6 B, R2C1 F, R2C2 D, "
                      "R3C1 D, R3C6 E, R4C1 E, R4C5 D, R5C3 A, R5C4 B, R6C6 A.")
ESTATE = _estate()


def _right():
    B, A, C = (40, 170), (40, 30), (250, 170)
    M = (40, 100); N = (145, 170)
    seg = lambda U, V: f'<line x1="{U[0]}" y1="{U[1]}" x2="{V[0]}" y2="{V[1]}" stroke="{INK}" stroke-width="2"/>'
    b = seg(A, B) + seg(B, C) + seg(C, A) + seg(A, N) + seg(M, C)
    b += f'<polyline points="40,156 54,156 54,170" fill="none" stroke="{INK}"/>'
    b += _t(28, 30, "A", 15) + _t(28, 184, "B", 15) + _t(262, 184, "C", 15) + _t(26, 104, "M", 15) + _t(145, 188, "N", 15)
    return charts.raw("sipe_SM25-13_QA_18", 280, 200, b,
                      "Right triangle ABC with the right angle at B, AB vertical and BC horizontal. M is the midpoint of AB and N the midpoint of BC; segments AN and MC are drawn.")
RIGHT = _right()
