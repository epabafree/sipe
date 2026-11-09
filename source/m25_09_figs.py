# -*- coding: utf-8 -*-
"""Figures for Simp Mock 9 (2025), written into media/ when imported."""
import math
import charts
from charts import _t
INK, MUT, GRID, HEAD = "#111827", "#6b7280", "#cbd5e1", "#f1f5f9"
YRS = ["2021", "2022", "2023", "2024", "2025"]

RES = charts.line("sipe_SM25-09_DILR_S1a", YRS, [("Resident students", [60, 40, 60, 50, 50])], 0, 70, 10,
                  "Line graph: resident students as a percentage of all students, 2021 to 2025", ylabel="% of all students",
                  fmt=lambda v: f"{v}%")
APP = charts.vbar("sipe_SM25-09_DILR_S1b", YRS, [("Applied for a scholarship", [70, 80, 50, 75, 20])], 90, 10,
                  "Bar chart: students who applied for a scholarship as a percentage of all students, 2021 to 2025", ylabel="% of all students",
                  fmt=lambda v: f"{v}%")
GOT = charts.hbar_stacked("sipe_SM25-09_DILR_S1c", ["2025", "2024", "2023", "2022", "2021"], [("Got a scholarship", [60, 40, 85, 70, 65])], 100, 10,
                          "Horizontal bars: applicants who got a scholarship as a percentage of applicants, 2021 to 2025", xlabel="% of applicants")

def _metro():
    St = ["Austin", "Baltimore", "Christchurch", "Denver", "E. Windsor"]
    cells = [["—", "a", "b", "c", "d", "22"], ["", "—", "e", "f", "g", "15"], ["", "", "—", "h", "i", "12"], ["", "", "", "—", "j", "6"], ["", "", "", "", "—", ""]]
    tot = ["", "4", "15", "24", "12", ""]
    lw, cw, ch = 112, 86, 30; cols = 6
    w, h = lw + cols * cw + 2, ch * 7 + 2
    b = f'<rect x="0" y="0" width="{w - 2}" height="{ch}" fill="{HEAD}"/><rect x="0" y="0" width="{lw}" height="{h - 2}" fill="{HEAD}"/>'
    b += _t(lw / 2, 19, "From \\ To", 12, col=MUT)
    for j, s in enumerate(St + ["Total"]):
        b += _t(lw + cw * (j + 0.5), 20, s, 13, bold=True)
    for i, s in enumerate(St + ["Total"]):
        y = ch * (i + 1) + 20
        b += _t(lw / 2, y, s, 13, bold=True)
        row = cells[i] if i < 5 else tot
        for j, v in enumerate(row):
            b += _t(lw + cw * (j + 0.5), y, v, 15, col=MUT if v == "—" else INK, bold=(i == 5 or j == 5))
    for k in range(8):
        b += f'<line x1="0" y1="{ch * k}" x2="{w - 2}" y2="{ch * k}" stroke="{GRID}"/>'
    for k in range(cols + 1):
        b += f'<line x1="{lw + cw * k}" y1="0" x2="{lw + cw * k}" y2="{h - 2}" stroke="{GRID}"/>'
    b += f'<line x1="0" y1="0" x2="0" y2="{h - 2}" stroke="{GRID}"/>'
    return charts.raw("sipe_SM25-09_DILR_S3", w, h, b, "Table of scientists by boarding station (rows) and alighting station (columns): Austin row a, b, c, d total 22; Baltimore row e, f, g total 15; Christchurch row h, i total 12; Denver row j total 6; column totals Baltimore 4, Christchurch 15, Denver 24, East Windsor 12")
METRO = _metro()

def _rect_circle():
    s = 70; x0, y0 = 30, 42          # AB = s (vertical chord), BC = 2s
    A, B = (x0 + 2 * s, y0), (x0 + 2 * s, y0 + s)
    D, C = (x0, y0), (x0, y0 + s)
    r = s; O = (A[0] + r * math.sqrt(3) / 2, y0 + s / 2)
    b = f'<path d="M{A[0]},{A[1]} A{r},{r} 0 0,0 {B[0]},{B[1]} Z" fill="#d1d5db"/>'
    b += f'<rect x="{x0}" y="{y0}" width="{2 * s}" height="{s}" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += f'<circle cx="{O[0]:.1f}" cy="{O[1]:.1f}" r="{r}" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += f'<circle cx="{O[0]:.1f}" cy="{O[1]:.1f}" r="2.5" fill="{INK}"/>' + _t(O[0] + 10, O[1] - 6, "O", 14)
    for t, (x, y), dx, dy in (("A", A, 0, -8), ("B", B, 0, 18), ("C", C, -10, 16), ("D", D, -10, -4)):
        b += _t(x + dx, y + dy, t, 14)
    W = int(O[0] + r + 12)
    return charts.raw("sipe_SM25-09_QA_21", W, int(y0 + s / 2 + r + 6), b, "Rectangle ABCD whose side AB is a chord of a circle with centre O; the part of the circle inside the rectangle, a segment cut off by AB, is shaded")
RECT = _rect_circle()
