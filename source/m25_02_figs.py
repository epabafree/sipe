# -*- coding: utf-8 -*-
"""Figures for Simp Mock 2 (2025), written into media/ when imported."""
import math
import charts
INK, MUT, GRID = "#111827", "#6b7280", "#e5e7eb"
GREEN, RED = "#16a34a", "#dc2626"
# candlesticks: (day, open, high, low, close)
CANDLES = [("6 Jan", 1430, 1430, 1390, 1410), ("7 Jan", 1410, 1428, 1400, 1420), ("8 Jan", 1430, 1450, 1420, 1445), ("9 Jan", 1450, 1460, 1420, 1430),
           ("10 Jan", 1440, 1450, 1400, 1410), ("13 Jan", 1400, 1430, 1390, 1405), ("14 Jan", 1405, 1410, 1360, 1375), ("15 Jan", 1370, 1390, 1340, 1350),
           ("16 Jan", 1350, 1390, 1340, 1380), ("17 Jan", 1390, 1450, 1380, 1420)]
def _candles():
    w, h, left, top, bot = 600, 380, 58, 14, 50
    lo, hi = 1330, 1470; ph = h - top - bot; pw = w - left - 12
    Y = lambda v: top + ph * (hi - v) / (hi - lo)
    b = ""
    for v in range(lo, hi + 1, 10):
        b += f'<line x1="{left}" y1="{Y(v):.1f}" x2="{w - 12}" y2="{Y(v):.1f}" stroke="{GRID if v % 50 else "#cbd5e1"}"/>'
        b += f'<text x="{left - 6}" y="{Y(v) + 4:.1f}" font-size="10" text-anchor="end" fill="{MUT}">{v}</text>'
    cw = pw / len(CANDLES)
    for i, (d, o, hgh, l, c) in enumerate(CANDLES):
        x = left + cw * (i + 0.5); col = GREEN if c > o else RED
        b += f'<line x1="{x:.1f}" y1="{Y(hgh):.1f}" x2="{x:.1f}" y2="{Y(l):.1f}" stroke="{INK}" stroke-width="1.5"/>'
        top_, bot_ = max(o, c), min(o, c)
        b += f'<rect x="{x - 11:.1f}" y="{Y(top_):.1f}" width="22" height="{max(Y(bot_) - Y(top_), 1.5):.1f}" fill="{col}" stroke="{INK}" stroke-width="0.8"/>'
        b += f'<text x="{x:.1f}" y="{h - bot + 18}" font-size="11" text-anchor="middle" fill="{INK}">{d}</text>'
    b += f'<text x="14" y="{top + ph / 2}" font-size="11" text-anchor="middle" fill="{MUT}" transform="rotate(-90 14 {top + ph / 2})">Price of one share (₹)</text>'
    b += f'<text x="{left + pw / 2}" y="{h - 8}" font-size="11" text-anchor="middle" fill="{MUT}">Gridlines every ₹10. Green: closed higher than it opened. Red: closed lower.</text>'
    return charts.raw("sipe_SM25-02_DILR_S2", w, h, b, "Candlestick chart of a share price over ten trading days from 6 to 17 January")
CANDLE_FIG = _candles()
# QA 18: semicircle in an equilateral triangle
def _semi():
    s = 220; B = (30, 220); C = (30 + s, 220); A = (30 + s / 2, 220 - s * math.sqrt(3) / 2); O = ((B[0] + C[0]) / 2, 220)
    r = s / 2 * math.sqrt(3) / 2
    b = f'<polygon points="{A[0]:.1f},{A[1]:.1f} {B[0]},{B[1]} {C[0]},{C[1]}" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += f'<path d="M{O[0] - r:.1f},220 A{r:.1f},{r:.1f} 0 0 1 {O[0] + r:.1f},220" fill="none" stroke="#2563eb" stroke-width="2"/>'
    b += f'<circle cx="{O[0]}" cy="220" r="3" fill="{INK}"/>'
    for (x, y), t, dx, dy in [(A, "A", 0, -8), (B, "B", -10, 16), (C, "C", 10, 16), (O, "O", 0, 18)]:
        b += f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" font-size="15" text-anchor="middle" fill="{INK}">{t}</text>'
    b += f'<text x="{(A[0] + B[0]) / 2 - 18:.1f}" y="{(A[1] + B[1]) / 2:.1f}" font-size="13" text-anchor="end" fill="{MUT}">10</text>'
    return charts.raw("sipe_SM25-02_QA_18", 280, 250, b, "Equilateral triangle ABC of side 10 with a semicircle on BC, centred at the midpoint O, touching AB and AC")
SEMI_FIG = _semi()
