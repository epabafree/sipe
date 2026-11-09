# -*- coding: utf-8 -*-
"""Figures for Simp Mock 7 (2025), written into media/ when imported."""
import math
import charts
INK = "#111827"

def _chords():
    R = 100; cx, cy = 130, 125
    P = lambda deg: (cx + R * math.cos(math.radians(deg)), cy - R * math.sin(math.radians(deg)))
    A, B = P(160), P(250); C, D = P(70), P(310)
    seg = lambda U, V: f'<line x1="{U[0]:.1f}" y1="{U[1]:.1f}" x2="{V[0]:.1f}" y2="{V[1]:.1f}" stroke="{INK}" stroke-width="2"/>'
    b = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="2.5"/>'
    b += seg(A, B) + seg(C, D) + seg((cx, cy), A) + seg((cx, cy), B) + seg((cx, cy), C) + seg((cx, cy), D)
    b += f'<circle cx="{cx}" cy="{cy}" r="3" fill="{INK}"/>'
    b += f'<text x="{cx - 4}" y="{cy + 20}" font-size="14" fill="{INK}">O</text>'
    b += f'<text x="{cx + 14}" y="{cy - 2}" font-size="13" fill="{INK}">120°</text><text x="{cx - 44}" y="{cy - 4}" font-size="13" fill="{INK}">90°</text>'
    for t, (x, y), dx, dy in (("A", A, -16, -2), ("B", B, -14, 14), ("C", C, 4, -6), ("D", D, 6, 14)):
        b += f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" font-size="15" fill="{INK}">{t}</text>'
    return charts.raw("sipe_SM25-07_QA_02", 270, 250, b, "Circle with centre O and chords AB and CD; angle AOB is 90° and angle COD is 120°")
CHORDS = _chords()

def _tri():
    A, B, C = (90, 20), (20, 180), (420, 180)
    t = 10 / 15
    E = (A[0] + (C[0] - A[0]) * t, A[1] + (C[1] - A[1]) * t)
    d = 20 / 3 / 15
    D = (A[0] + (C[0] - A[0]) * d, A[1] + (C[1] - A[1]) * d)
    seg = lambda U, V: f'<line x1="{U[0]:.1f}" y1="{U[1]:.1f}" x2="{V[0]:.1f}" y2="{V[1]:.1f}" stroke="{INK}" stroke-width="2"/>'
    b = seg(A, B) + seg(B, C) + seg(C, A) + seg(B, D) + seg(B, E)
    for s, (x, y), dx, dy in (("A", A, -4, -6), ("B", B, -14, 14), ("C", C, 6, 14), ("D", D, 2, -8), ("E", E, 4, -8)):
        b += f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" font-size="15" fill="{INK}">{s}</text>'
    return charts.raw("sipe_SM25-07_QA_14", 440, 200, b, "Triangle ABC with points D and E on AC, D nearer A; segments BD and BE drawn from B")
TRI = _tri()
