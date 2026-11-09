# -*- coding: utf-8 -*-
"""Figures for Simp Mock 6 (2025), written into media/ when imported."""
import math
import charts
INK, MUT = "#111827", "#6b7280"

SALES = charts.hbar_stacked("sipe_SM25-06_DILR_S2", ["Q1", "Q2", "Q3", "Q4"],
                            [("Sedans", [35, 40, 30, 25]), ("SUVs", [30, 25, 35, 30]), ("Hatchbacks", [25, 20, 20, 30]), ("Electric vehicles", [10, 15, 15, 15])],
                            100, 25, "Stacked bars: share of sedans, SUVs, hatchbacks and electric vehicles in each quarter’s car sales", xlabel="Percentage of the quarter’s total sales")

def _circles():
    r = 40; s = 2 * r * (1 + math.sqrt(3)); x0, y0 = 20, 20
    A, B = (x0, y0), (x0 + s, y0); C = (x0 + s / 2, y0 + s * math.sqrt(3) / 2)
    b = f'<polygon points="{A[0]:.1f},{A[1]:.1f} {B[0]:.1f},{B[1]:.1f} {C[0]:.1f},{C[1]:.1f}" fill="none" stroke="{INK}" stroke-width="2"/>'
    cy_top = y0 + r
    for cx, cy in ((x0 + s / 2 - r, cy_top), (x0 + s / 2 + r, cy_top), (x0 + s / 2, cy_top + r * math.sqrt(3))):
        b += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="none" stroke="{INK}" stroke-width="2"/>'
    return charts.raw("sipe_SM25-06_QA_02", int(s + 2 * x0), int(s * math.sqrt(3) / 2 + 2 * y0), b,
                      "Equilateral triangle pointing down with three equal circles inside, two along the top side and one below them; each circle touches the other two and two sides of the triangle")
CIRCLES = _circles()

def _segment():
    R = 110; cx, cy = 140, 125
    A, B = (cx - R * math.sin(math.radians(60)), cy + R * math.cos(math.radians(60))), (cx + R * math.sin(math.radians(60)), cy + R * math.cos(math.radians(60)))
    b = f'<path d="M{A[0]:.1f},{A[1]:.1f} A{R},{R} 0 0,0 {B[0]:.1f},{B[1]:.1f} Z" fill="#374151"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += f'<polyline points="{A[0]:.1f},{A[1]:.1f} {cx},{cy} {B[0]:.1f},{B[1]:.1f}" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="3" fill="{INK}"/>'
    b += f'<text x="{cx + 10}" y="{cy - 6}" font-size="15" fill="{INK}">O</text>'
    b += f'<text x="{A[0] - 16:.1f}" y="{A[1] + 14:.1f}" font-size="15" fill="{INK}">A</text><text x="{B[0] + 6:.1f}" y="{B[1] + 14:.1f}" font-size="15" fill="{INK}">B</text>'
    return charts.raw("sipe_SM25-06_QA_17", 280, 250, b, "Circle with centre O; radii OA and OB, and the minor segment cut off by chord AB below them is shaded")
SEGMENT = _segment()
