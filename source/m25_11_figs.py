# -*- coding: utf-8 -*-
"""Figures for Simp Mock 11 (2025), written into media/ when imported."""
import math
import charts
from charts import _t
INK, MUT, GRID = "#111827", "#6b7280", "#e5e7eb"
MON = ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]

WA = charts.vbar("sipe_SM25-11_DILR_S3a", MON, [("Opening stock", [350, 300, 350, 500, 450, 150]), ("Purchase", [900, 850, 750, 500, 800, 950]), ("Sales", [950, 1100, 600, 450, 1300, 1000])],
                 1400, 200, "Grouped bars for Warehouse A, October to March: opening stock, purchase and sales in units", ylabel="Units", w=600, show_values=True)
WB = charts.vbar("sipe_SM25-11_DILR_S3b", MON, [("Opening stock", [350, 50, 100, 250, 50, 100]), ("Purchase", [700, 1000, 700, 800, 900, 600]), ("Sales", [1000, 650, 550, 1100, 650, 800])],
                 1400, 200, "Grouped bars for Warehouse B, October to March: opening stock, purchase and sales in units", ylabel="Units", w=600, show_values=True)

def _roads():
    pos = {"M": (40, 150), "P": (150, 95), "R": (150, 220), "J": (330, 40), "N": (330, 200), "A": (470, 120), "S": (470, 230)}
    roads = [("M", "P", 250), ("M", "R", 180), ("P", "J", 370), ("R", "N", 270), ("J", "N", 80), ("J", "A", 150), ("N", "A", 100), ("A", "S", 180)]
    b = ""
    for u, v, d in roads:
        (x1, y1), (x2, y2) = pos[u], pos[v]
        b += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="2"/>'
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        b += f'<rect x="{mx - 18:.1f}" y="{my - 10:.1f}" width="36" height="18" rx="4" fill="#fff"/>' + _t(mx, my + 4, str(d), 12, bold=True)
    for k, (x, y) in pos.items():
        b += f'<rect x="{x - 16}" y="{y - 16}" width="32" height="32" rx="4" fill="#f8fafc" stroke="{INK}" stroke-width="2"/>' + _t(x, y + 6, k, 16, bold=True)
    return charts.raw("sipe_SM25-11_DILR_S5", 510, 260, b, "Road map of seven cities: M–P 250 km, M–R 180, P–J 370, R–N 270, J–N 80, J–A 150, N–A 100, A–S 180")
ROADS = _roads()

def _perp():
    Bp = (30, 140)
    A = (Bp[0], Bp[1] - 110)  # AB vertical
    AB = Bp[1] - A[1]; BC = AB * math.sqrt(3); C = (Bp[0] + BC, Bp[1])
    def foot(P, U, V):
        ux, uy = V[0] - U[0], V[1] - U[1]; t = ((P[0] - U[0]) * ux + (P[1] - U[1]) * uy) / (ux * ux + uy * uy)
        return (U[0] + t * ux, U[1] + t * uy)
    D = foot(Bp, A, C); cur = D; segs = [(Bp, D)]
    labels = [("D", D)]
    for i in range(1, 4):
        Bi = (cur[0], Bp[1]); segs.append((cur, Bi)); labels.append((f"B{i}", Bi))
        if i < 3:
            Di = foot(Bi, A, C); segs.append((Bi, Di)); labels.append((f"D{i}", Di)); cur = Di
    seg = lambda U, V: f'<line x1="{U[0]:.1f}" y1="{U[1]:.1f}" x2="{V[0]:.1f}" y2="{V[1]:.1f}" stroke="{INK}" stroke-width="2"/>'
    b = seg(A, Bp) + seg(Bp, C) + seg(C, A) + "".join(seg(u, v) for u, v in segs)
    b += _t(A[0] - 10, A[1] + 4, "A", 14) + _t(Bp[0] - 10, Bp[1] + 12, "B", 14) + _t(C[0] + 10, C[1] + 4, "C", 14)
    for t, (x, y) in labels:
        if t.startswith("B"):
            b += _t(x, y + 18, t[0], 14) + _t(x + 8, y + 22, t[1], 10)
        else:
            b += _t(x + 4, y - 8, t[0], 14) + (_t(x + 12, y - 4, t[1], 10) if len(t) > 1 else "")
    return charts.raw("sipe_SM25-11_QA_02", int(C[0] + 24), int(Bp[1] + 28), b, "Right triangle ABC with the right angle at B; perpendiculars alternate from B to AC at D, from D to BC at B1, from B1 to AC at D1, and so on towards C")
PERP = _perp()

def _square_circles():
    s = 80; cx, cy = 125, 125; R = s * math.sqrt(2)
    r = s * (math.sqrt(2) - 1); d = r * math.sqrt(2); r0 = d - r
    b = f'<circle cx="{cx}" cy="{cy}" r="{R:.1f}" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += f'<rect x="{cx - s}" y="{cy - s}" width="{2 * s}" height="{2 * s}" fill="none" stroke="{INK}" stroke-width="2"/>'
    b += f'<line x1="{cx - s}" y1="{cy - s}" x2="{cx + s}" y2="{cy + s}" stroke="{INK}" stroke-width="1.5"/><line x1="{cx + s}" y1="{cy - s}" x2="{cx - s}" y2="{cy + s}" stroke="{INK}" stroke-width="1.5"/>'
    for ox, oy in ((0, -d), (0, d), (-d, 0), (d, 0)):
        b += f'<circle cx="{cx + ox:.1f}" cy="{cy + oy:.1f}" r="{r:.1f}" fill="#fff" stroke="{INK}" stroke-width="2"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{r0:.1f}" fill="#fff" stroke="{INK}" stroke-width="2"/>'
    for t, x, y in (("A", cx - s - 12, cy - s - 4), ("B", cx + s + 6, cy - s - 4), ("C", cx + s + 6, cy + s + 14), ("D", cx - s - 14, cy + s + 14)):
        b += _t(x, y, t, 14)
    return charts.raw("sipe_SM25-11_QA_10", 250, 250, b, "Square ABCD inside a circle through its corners; the diagonals are drawn; four equal circles each touch both diagonals and one side; a small circle at the centre touches all four")
SQ = _square_circles()

def _lines():
    mx = 150; By, Yy = 80, 240
    b = ""
    b += f'<line x1="{mx}" y1="20" x2="{mx}" y2="300" stroke="{INK}" stroke-width="2"/>' + _t(mx, 316, "m", 13)
    b += f'<line x1="30" y1="{By}" x2="330" y2="{By}" stroke="{INK}" stroke-width="2"/>' + _t(342, By + 4, "p", 13)
    b += f'<line x1="10" y1="{Yy}" x2="330" y2="{Yy}" stroke="{INK}" stroke-width="2"/>' + _t(342, Yy + 4, "q", 13)
    ang = math.radians(50); Kx = mx + 50; Ky = Yy
    dx, dy = math.cos(ang), math.sin(ang)
    P1 = (Kx - (Ky - By) / dy * dx, By); End = (Kx + 60 * dx, Ky + 60 * dy)
    Mx, My = mx, Ky - (Kx - mx) * dy / dx
    b += f'<line x1="{P1[0] - 20 * dx:.1f}" y1="{By - 20 * dy:.1f}" x2="{End[0]:.1f}" y2="{End[1]:.1f}" stroke="{INK}" stroke-width="2"/>' + _t(End[0] + 6, End[1] + 12, "n", 13)
    for t, x, y in (("A", mx - 12, 40), ("B", mx - 12, By - 8), ("C", 260, By - 8), ("X", 40, Yy + 18), ("Y", mx - 12, Yy + 18), ("Z", mx - 12, 288), ("R", 270, Yy + 18), ("K", Kx - 4, Yy + 18), ("M", Mx + 8, My - 4)):
        b += _t(x, y, t, 13)
    b += _t(Kx + 26, Yy - 10, "130°", 12) + _t(P1[0] + 26, By + 16, "z", 13) + _t(P1[0] - 20, By - 12, "w", 13) + _t(Mx - 14, My - 18, "ℓ", 14)
    b += f'<path d="M{P1[0] + 14:.1f},{By} A14,14 0 1,0 {P1[0] + 14 * dx:.1f},{By + 14 * dy:.1f}" fill="none" stroke="{MUT}" stroke-width="1.5"/>'
    return charts.raw("sipe_SM25-11_QA_20", 360, 326, b, "Line m crosses lines p and q at B and Y; line n crosses p to the left of B, crosses m at M and q at K; angle MKR is 130°; angle z is between n and p at their crossing, w is the reflex angle there, and ℓ is at M")
LINES = _lines()

def _trap():
    a = 90; h = a * math.sqrt(3)
    K, N = (20, 20 + h), (20 + 4 * a, 20 + h); L, M = (20 + a, 20), (20 + 3 * a, 20); Pp = (20 + 2 * a, 20 + h)
    mid = lambda U, V: ((U[0] + V[0]) / 2, (U[1] + V[1]) / 2)
    Q, S = mid(L, Pp), mid(M, Pp); R = (Pp[0], 20 + h / 3)
    seg = lambda U, V: f'<line x1="{U[0]:.1f}" y1="{U[1]:.1f}" x2="{V[0]:.1f}" y2="{V[1]:.1f}" stroke="{INK}" stroke-width="2"/>'
    b = seg(K, L) + seg(L, M) + seg(M, N) + seg(N, K) + seg(L, Pp) + seg(M, Pp) + seg(K, M) + seg(L, N)
    for t, (x, y), dx, dy in (("K", K, -12, 14), ("L", L, -6, -6), ("M", M, 4, -6), ("N", N, 6, 14), ("P", Pp, 0, 18), ("Q", Q, -16, 4), ("R", R, 0, -10), ("S", S, 8, 4)):
        b += _t(x + dx, y + dy, t, 14)
    return charts.raw("sipe_SM25-11_QA_22", 20 + 4 * a + 24, int(20 + h + 28), b, "Isosceles trapezium KLMN with LM on top; P is on KN with LMP equilateral; diagonals KM and LN, and segments LP and MP, cross at Q, R and S")
TRAP = _trap()
