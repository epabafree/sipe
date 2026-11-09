# -*- coding: utf-8 -*-
"""Figures for Simp Mock 5 (2025), written into media/ when imported."""
import charts
INK, MUT, GRID, HEAD = "#111827", "#6b7280", "#cbd5e1", "#f1f5f9"

COST = """X 20 14 10 12 22 18 15
14 X 8 5 18 16 14 20
8 6 X 18 7 20 12 14
10 8 14 X 20 15 16 18
12 14 5 10 X 18 14 13
13 10 12 16 14 X 18 16
12 11 10 17 13 18 X 15
16 14 12 20 15 19 16 X"""

def _matrix():
    L = "ABCDEFGH"; cw, ch, lw, top = 40, 30, 92, 54
    w, h = lw + 8 * cw + 2, top + 8 * ch + 2
    b = f'<rect x="{lw}" y="{top - ch}" width="{8 * cw}" height="{ch}" fill="{HEAD}"/><rect x="0" y="{top}" width="{lw}" height="{8 * ch}" fill="{HEAD}"/>'
    b += f'<text x="{lw + 4 * cw}" y="16" font-size="13" text-anchor="middle" fill="{INK}" font-weight="bold">Importing country →</text>'
    b += f'<text x="{lw / 2}" y="{top - 16}" font-size="12" text-anchor="middle" fill="{INK}" font-weight="bold">Exporter ↓</text>'
    for j, c in enumerate(L):
        b += f'<text x="{lw + cw * (j + 0.5)}" y="{top - 10}" font-size="14" text-anchor="middle" fill="{INK}" font-weight="bold">{c}</text>'
    for i, row in enumerate(COST.split("\n")):
        y = top + ch * (i + 0.5) + 5
        b += f'<text x="{lw / 2}" y="{y}" font-size="14" text-anchor="middle" fill="{INK}" font-weight="bold">{L[i]}</text>'
        for j, v in enumerate(row.split()):
            b += f'<text x="{lw + cw * (j + 0.5)}" y="{y}" font-size="14" text-anchor="middle" fill="{MUT if v == "X" else INK}">{v}</text>'
    for k in range(9):
        b += f'<line x1="{lw + cw * k}" y1="{top - ch}" x2="{lw + cw * k}" y2="{h - 1}" stroke="{GRID}"/>'
        b += f'<line x1="0" y1="{top + ch * k}" x2="{w}" y2="{top + ch * k}" stroke="{GRID}"/>'
    b += f'<line x1="0" y1="{top - ch}" x2="0" y2="{h - 1}" stroke="{GRID}"/><line x1="0" y1="{top - ch}" x2="{w}" y2="{top - ch}" stroke="{GRID}"/>'
    return charts.raw("sipe_SM25-05_DILR_S3", w, h, b, "Eight-by-eight table of transport costs in dollars per 10 kg; rows are exporting countries A to H, columns importing countries A to H")
MATRIX = _matrix()

def _tri():
    A, B, C = (120, 22), (30, 182), (400, 168)
    E = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
    D = (A[0] + (C[0] - A[0]) / 3, A[1] + (C[1] - A[1]) / 3)
    F = ((A[0] + E[0]) / 2, (A[1] + E[1]) / 2)
    seg = lambda P, Q: f'<line x1="{P[0]:.1f}" y1="{P[1]:.1f}" x2="{Q[0]:.1f}" y2="{Q[1]:.1f}" stroke="{INK}" stroke-width="2"/>'
    b = seg(A, B) + seg(B, C) + seg(C, A) + seg(A, E) + seg(B, D)
    for s, (x, y), dx, dy in (("A", A, 0, -6), ("B", B, -12, 14), ("C", C, 12, 6), ("D", D, 4, -8), ("E", E, 2, 18), ("F", F, -14, 4)):
        b += f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" font-size="15" text-anchor="middle" fill="{INK}">{s}</text>'
    return charts.raw("sipe_SM25-05_QA_09", 430, 210, b, "Triangle ABC with median AE to side BC, and line BD from B to a point D on AC crossing AE at F")
TRI = _tri()

def _circ():
    s = 9; x0, y0 = 40, 45
    A = (x0, y0); B = (x0, y0 + 12 * s); C = (x0 + 2 * s, y0); D = (x0 + 2 * s, y0 + 14 * s)
    O = (x0 + 8 * s, y0 + 6 * s); R = 10 * s
    b = f'<circle cx="{O[0]}" cy="{O[1]}" r="{R}" fill="none" stroke="{INK}" stroke-width="2"/>'
    for P, Q in ((A, B), (A, C), (C, D)):
        b += f'<line x1="{P[0]}" y1="{P[1]}" x2="{Q[0]}" y2="{Q[1]}" stroke="{INK}" stroke-width="2"/>'
    b += f'<circle cx="{O[0]}" cy="{O[1]}" r="3" fill="{INK}"/>'
    for t, (x, y), dx, dy in (("A", A, -10, -2), ("B", B, -12, 10), ("C", C, 10, -2), ("D", D, 6, 16), ("O", O, 12, 5)):
        b += f'<text x="{x + dx}" y="{y + dy}" font-size="15" text-anchor="middle" fill="{INK}">{t}</text>'
    return charts.raw("sipe_SM25-05_QA_13", 225, 210, b, "Circle with centre O; from A on the circle, chord AB goes straight down, AC goes right to a point C inside the circle, and CD goes straight down to D on the circle")
CIRC = _circ()
