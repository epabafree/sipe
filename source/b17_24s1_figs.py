# -*- coding: utf-8 -*-
"""Figures for CAT 2024 Slot 1, written into media/ when imported."""
import charts
from charts import _t
INK, MUT, GRID = "#111827", "#6b7280", "#e5e7eb"
GREEN, RED = "#16a34a", "#dc2626"

COUNTRIES = charts.vbar("sipe_2024S1_DILR_S2", ["Dheeraj", "Samantha", "Nitesh"],
                        [("Asia", [3, 0, 1]), ("Europe", [7, 9, 6]), ("ROW", [1, 4, 12])], 14, 2,
                        "Number of countries visited. Dheeraj: Asia 3, Europe 7, ROW 1. Samantha: Asia 0, Europe 9, ROW 4. Nitesh: Asia 1, Europe 6, ROW 12.",
                        ylabel="Countries", w=460, h=300, show_values=True)

# share: (open, close, high, low)
SHARES = {"A": (2200, 1800, 2400, 1200), "B": (2000, 1700, 2000, 1400), "C": (800, 1200, 1400, 800), "D": (500, 1000, 1200, 300),
          "E": (1300, 1100, 1400, 1100), "F": (1800, 1600, 2000, 1200), "G": (1200, 1700, 1900, 1000)}

def _candles():
    W, H = 600, 380
    left, right, top, bot = 54, 170, 16, 40
    pw, ph = W - left - right, H - top - bot
    lo, hi = 200, 2400
    Y = lambda v: top + ph - ph * (v - lo) / (hi - lo)
    b = ""
    for v in range(lo, hi + 1, 200):
        b += f'<line x1="{left}" y1="{Y(v):.1f}" x2="{left + pw}" y2="{Y(v):.1f}" stroke="{GRID}" stroke-dasharray="3 3"/>' + _t(left - 6, Y(v) + 4, f"{v:,}", 11, "end", MUT)
    b += f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + ph}" stroke="{MUT}"/>'
    gw = pw / len(SHARES)
    for i, (k, (o, c, h, l)) in enumerate(SHARES.items()):
        x = left + gw * i + gw / 2
        col = GREEN if c > o else RED
        b += f'<line x1="{x:.1f}" y1="{Y(h):.1f}" x2="{x:.1f}" y2="{Y(l):.1f}" stroke="{col}" stroke-width="2"/>'
        b += f'<rect x="{x - 11:.1f}" y="{Y(max(o, c)):.1f}" width="22" height="{Y(min(o, c)) - Y(max(o, c)):.1f}" fill="{col}"/>'
        b += _t(x, top + ph + 22, k, 13, bold=True)
    # legend
    lx = left + pw + 40
    for j, (col, lab_top, lab_bot) in enumerate([(RED, "Opening price", "Closing price"), (GREEN, "Closing price", "Opening price")]):
        y0 = top + 20 + j * 170
        b += f'<line x1="{lx}" y1="{y0}" x2="{lx}" y2="{y0 + 120}" stroke="{col}" stroke-width="2"/>'
        b += f'<rect x="{lx - 9}" y="{y0 + 30}" width="18" height="60" fill="{col}"/>'
        b += _t(lx + 16, y0 + 4, "Day’s high", 11, "start", MUT) + _t(lx + 16, y0 + 36, lab_top, 11, "start") + _t(lx + 16, y0 + 92, lab_bot, 11, "start") + _t(lx + 16, y0 + 124, "Day’s low", 11, "start", MUT)
        b += _t(lx + 16, y0 + 64, "Bearish (red)" if j == 0 else "Bullish (green)", 11, "start", col, bold=True)
    b += _t(16, top + ph / 2, "Price (Rs)", 11, col=MUT, extra=f' transform="rotate(-90 16 {top + ph / 2})"')
    return charts.raw("sipe_2024S1_DILR_S3", W, H, b,
                      "Candlestick chart of seven shares, prices in rupees from 200 to 2,400. A red: open 2,200, close 1,800, high 2,400, low 1,200. B red: open 2,000, close 1,700, high 2,000, low 1,400. C green: open 800, close 1,200, high 1,400, low 800. D green: open 500, close 1,000, high 1,200, low 300. E red: open 1,300, close 1,100, high 1,400, low 1,100. F red: open 1,800, close 1,600, high 2,000, low 1,200. G green: open 1,200, close 1,700, high 1,900, low 1,000.")
CANDLES = _candles()

STARS = charts.vbar("sipe_2024S1_DILR_S4", ["M", "N", "O", "P", "X", "Y"],
                    [("A", [10, 25, 0, 5, 0, 5]), ("B", [0, 0, 0, 25, 0, 20])], 30, 5,
                    "Stars received by bloggers A and B from each surfer. From M: A 10, B 0. N: A 25, B 0. O: none. P: A 5, B 25. X: none. Y: A 5, B 20.",
                    ylabel="Stars", w=480, h=300, show_values=True)
