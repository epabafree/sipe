# -*- coding: utf-8 -*-
"""Figures for Simp Mock 9, written into media/ when imported."""
import charts
from charts import _t
INK, MUT = "#111827", "#6b7280"

LAYOUT = {
 "A": "LLLLLLLLLL",
 "B": "SSSPPPPPSS",
 "C": "SMSOOSSPMO",
 "D": "MMPPPPPMMM",
 "E": "OOPPSSSPMO",
 "F": "SSSSSMMSSS",
 "G": "OOOOOOOOOO"}
COL = {"L": "#ede9fe", "P": "#dbeafe", "M": "#dcfce7", "S": "#fef3c7", "O": "#f3f4f6"}
PRICE = {"L": 500, "P": 400, "M": 300, "S": 200, "O": 100}


def _seats():
    cw, ch, x0, y0, gap = 28, 24, 30, 26, 22
    b = ""
    for i in range(10):
        x = x0 + i * cw + (gap if i >= 5 else 0) + cw / 2
        b += _t(x, y0 - 8, str(i + 1), 11, col=MUT)
    for r, row in enumerate("ABCDEFG"):
        y = y0 + r * ch
        b += _t(x0 - 14, y + 16, row, 12, bold=True)
        for i, s in enumerate(LAYOUT[row]):
            x = x0 + i * cw + (gap if i >= 5 else 0)
            b += f'<rect x="{x + 1}" y="{y + 1}" width="{cw - 2}" height="{ch - 2}" rx="3" fill="{COL[s]}" stroke="#9ca3af"/>'
            b += _t(x + cw / 2, y + 16, s, 11)
    xa = x0 + 5 * cw + gap / 2
    b += _t(xa, y0 + 3.5 * ch, "aisle", 10, col=MUT, extra=f' transform="rotate(-90 {xa} {y0 + 3.5 * ch})"')
    ys = y0 + 7 * ch + 10
    W = x0 + 10 * cw + gap
    b += f'<rect x="{x0}" y="{ys}" width="{W - x0}" height="12" fill="#374151"/>' + _t((x0 + W) / 2, ys + 10, "SCREEN", 9, col="#ffffff", bold=True)
    ly = ys + 30
    for k, (s, n) in enumerate([("L", "Luxury ₹500"), ("P", "Prime ₹400"), ("M", "Premium ₹300"), ("S", "Special ₹200"), ("O", "Ordinary ₹100")]):
        lx = x0 + (k % 3) * 104; yy = ly + (k // 3) * 20
        b += f'<rect x="{lx}" y="{yy - 11}" width="16" height="14" rx="2" fill="{COL[s]}" stroke="#9ca3af"/>' + _t(lx + 8, yy, s, 10)
        b += _t(lx + 20, yy, n, 11, anchor="start")
    return charts.raw("sipe_SM09_DILR_1", W + 10, ly + 30, b,
                      "Seating plan: rows A (back) to G (front, at the screen), columns 1 to 5 left of the aisle and 6 to 10 right. Row A all Luxury. Row B: S S S P P | P P P S S. Row C: S M S O O | S S P M O. Row D: M M P P P | P P M M M. Row E: O O P P S | S S P M O. Row F: S S S S S | M M S S S. Row G all Ordinary.")
SEATS = _seats()
