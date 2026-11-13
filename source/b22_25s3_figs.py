# -*- coding: utf-8 -*-
"""Figures for CAT 2025 Slot 3, written into media/ when imported."""
import charts
from charts import _t, PAL
INK, MUT, GRID = "#111827", "#6b7280", "#e5e7eb"

# minute at which each competitor solved puzzles 1..10
T = {"Anirbid": [4, 9, 11, 14, 19, 22, 27, 29, 33, 37], "Chandranath": [4, 6, 10, 13, 17, 21, 23, 26, 28, 30],
     "Koushik": [2, 4, 7, 12, 14, 16, 19, 25, 29, 31], "Suranjan": [5, 7, 12, 18, 21, 23, 26, 28, 30, 35]}
VISUAL = [1, 4, 8, 9]
COL = {"Anirbid": "#dc2626", "Chandranath": "#d97706", "Koushik": "#16a34a", "Suranjan": "#0891b2"}

def _steps(name, title, ymax, series, alt):
    W, H = 560, 330; left, right, top, bot = 50, 16, 30, 66
    pw, ph = W - left - right, H - top - bot
    X = lambda v: left + pw * v / 40
    Y = lambda v: top + ph - ph * v / ymax
    b = _t(W / 2, 18, title, 13, bold=True)
    for v in range(0, 41, 2):
        b += f'<line x1="{X(v):.1f}" y1="{top}" x2="{X(v):.1f}" y2="{top + ph}" stroke="{GRID if v % 10 == 0 else "#f3f4f6"}"/>'
        if v % 10 == 0: b += _t(X(v), top + ph + 16, str(v), 11, col=MUT)
    for v in range(0, ymax + 1):
        b += f'<line x1="{left}" y1="{Y(v):.1f}" x2="{left + pw}" y2="{Y(v):.1f}" stroke="{GRID}"/>' + _t(left - 6, Y(v) + 4, str(v), 11, "end", MUT)
    for k, (lab, times) in enumerate(series.items()):
        off = (k - 1.5) * 1.2
        pts = [(0, 0)]
        for i, t in enumerate(times):
            pts += [(t, i), (t, i + 1)]
        pts.append((40, len(times)))
        d = " ".join(f"{X(x):.1f},{Y(y) + off:.1f}" for x, y in pts)
        b += f'<polyline points="{d}" fill="none" stroke="{COL[lab]}" stroke-width="2"/>'
    b += _t(left + pw / 2, top + ph + 34, "Time (minutes)", 11, col=MUT)
    lx = left
    for lab in series:
        b += f'<rect x="{lx}" y="{H - 16}" width="16" height="4" fill="{COL[lab]}"/>' + _t(lx + 20, H - 11, lab, 11, "start"); lx += 30 + 7 * len(lab)
    return charts.raw(name, W, H, b, alt)

ALL = _steps("sipe_2025S3_DILR_S3a", "All puzzles", 10, T,
             "Step chart of puzzles solved against time. Anirbid solved puzzles at minutes 4, 9, 11, 14, 19, 22, 27, 29, 33, 37. "
             "Chandranath at 4, 6, 10, 13, 17, 21, 23, 26, 28, 30. Koushik at 2, 4, 7, 12, 14, 16, 19, 25, 29, 31. Suranjan at 5, 7, 12, 18, 21, 23, 26, 28, 30, 35.")
VIS = _steps("sipe_2025S3_DILR_S3b", "Visual puzzles", 5, {k: [v[i - 1] for i in VISUAL] for k, v in T.items()},
             "Step chart of visual puzzles solved against time. Anirbid at minutes 4, 14, 29, 33. Chandranath at 4, 13, 26, 28. Koushik at 2, 12, 25, 29. Suranjan at 5, 18, 28, 30.")
