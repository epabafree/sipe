# -*- coding: utf-8 -*-
"""Figures for CAT 2024 Slot 3, written into media/ when imported."""
import charts
from charts import _t
INK, MUT, GRID = "#111827", "#6b7280", "#e5e7eb"

def _roads():
    s = 22; ox, oy = 90, 46
    xs = {"V1": 0, "V2": 4, "V3": 11}; ys = {"R-A": 0, "R-B": 3, "R-C": 8}
    X = lambda k: ox + xs[k] * s; Y = lambda k: oy + ys[k] * s
    b = ""
    for v in xs:
        b += f'<line x1="{X(v)}" y1="{oy - 24}" x2="{X(v)}" y2="{Y("R-C") + 24}" stroke="{INK}" stroke-width="2.5"/>' + _t(X(v), oy - 30, v, 13, bold=True)
    for r in ys:
        b += f'<line x1="{ox - 40}" y1="{Y(r)}" x2="{X("V3") + 50}" y2="{Y(r)}" stroke="{INK}" stroke-width="2.5"/>' + _t(ox - 46, Y(r) + 5, r, 13, "end", bold=True)
    tot = {"R-A": 22, "R-B": 20, "R-C": 20}
    for r, t in tot.items(): b += _t(X("V3") + 58, Y(r) + 5, str(t), 13, "start", "#b45309", bold=True)
    for v, t in {"V1": 15, "V2": 21, "V3": 26}.items(): b += _t(X(v), Y("R-C") + 44, str(t), 13, col="#b45309", bold=True)
    b += _t((X("V1") + X("V2")) / 2, oy - 6, "4 km", 11, col=MUT) + _t((X("V2") + X("V3")) / 2, oy - 6, "7 km", 11, col=MUT)
    b += _t(X("V3") + 8, (Y("R-A") + Y("R-B")) / 2 + 4, "3 km", 11, "start", MUT) + _t(X("V3") + 8, (Y("R-B") + Y("R-C")) / 2 + 4, "5 km", 11, "start", MUT)
    W, H = X("V3") + 100, Y("R-C") + 60
    return charts.raw("sipe_2024S3_DILR_S1", W, H, b,
                      "Road network: horizontal roads R-A, R-B and R-C, vertical roads V1, V2 and V3. V1 to V2 is 4 km and V2 to V3 is 7 km; R-A to R-B is 3 km and R-B to R-C is 5 km. "
                      "Total cash requirement on each road: R-A 22, R-B 20, R-C 20, V1 15, V2 21, V3 26 (Rs lakh).")
ROADS = _roads()

OTT = charts.vbar("sipe_2024S3_DILR_S2", ["Kid", "Elder"], [("2023", [15, 20]), ("2024", [20, 30])], 30, 5,
                  "Percentage of total subscribers. Kid: 15% in 2023, 20% in 2024. Elder: 20% in 2023, 30% in 2024.",
                  ylabel="% of total subscribers", w=380, h=280, fmt=lambda v: f"{v}%")

AC = charts.line("sipe_2024S3_DILR_S4", ["23:00", "23:30", "00:00", "00:30", "01:00", "01:30", "02:00"],
                 [("Inside temperature", [38, 32, 26, 31, 26, 30, 28])], 24, 40, 2,
                 "Inside temperature from 23:00 to 02:00: 38 °C at 23:00 falling steadily to 26 at 00:00 (32 at 23:30), rising to 31 at 00:30, falling to 26 at 01:00, rising to 30 at 01:30 and falling to 28 at 02:00.",
                 ylabel="Inside temperature (°C)", w=520, h=300)
