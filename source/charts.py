# -*- coding: utf-8 -*-
"""Small SVG chart writers for redrawn DILR / QA figures. Each call writes media/<name>.svg and returns the <p class="fig"> HTML."""
import math, os
HERE = os.path.dirname(os.path.abspath(__file__))
INK, MUT, GRID = "#111827", "#6b7280", "#e5e7eb"
PAL = ["#2563eb", "#dc2626", "#16a34a", "#d97706", "#7c3aed", "#0891b2", "#db2777", "#65a30d"]
FONT = 'font-family="Helvetica,Arial,sans-serif"'

def _save(name, w, h, body, alt):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" {FONT}><rect width="{w}" height="{h}" fill="#fff"/>{body}</svg>'
    open(os.path.join(HERE, "media", name + ".svg"), "w", encoding="utf-8").write(svg)
    return f'<p class="fig"><img src="{name}.svg" alt="{alt}"></p>'

def _t(x, y, s, size=13, anchor="middle", col=INK, bold=False, extra=""):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" fill="{col}"{" font-weight=\"bold\"" if bold else ""}{extra}>{s}</text>'

def hbar_stacked(name, cats, series, xmax, step, alt, xlabel="", show_values=True, w=560):
    """cats: row labels (top to bottom); series: [(label, [values per cat])]; values are segment sizes."""
    left, right, top, rowh = 70, 20, 16, 34
    h = top + rowh * len(cats) + 70
    pw = w - left - right
    X = lambda v: left + pw * v / xmax
    b = ""
    for v in range(0, int(xmax) + 1, step):
        b += f'<line x1="{X(v):.1f}" y1="{top}" x2="{X(v):.1f}" y2="{top + rowh * len(cats)}" stroke="{GRID}"/>' + _t(X(v), top + rowh * len(cats) + 16, f"{v:,}", 11, col=MUT)
    for i, c in enumerate(cats):
        y = top + i * rowh + 6; acc = 0
        b += _t(left - 8, y + 15, c, 12, "end")
        for k, (lab, vals) in enumerate(series):
            v = vals[i]
            b += f'<rect x="{X(acc):.1f}" y="{y}" width="{X(acc + v) - X(acc):.1f}" height="{rowh - 12}" fill="{PAL[k]}"/>'
            if show_values: b += _t((X(acc) + X(acc + v)) / 2, y + 15, f"{v:,}", 11, col="#fff", bold=True)
            acc += v
    ly = top + rowh * len(cats) + 36; lx = left
    for k, (lab, _) in enumerate(series):
        b += f'<rect x="{lx}" y="{ly - 10}" width="12" height="12" fill="{PAL[k]}"/>' + _t(lx + 16, ly, lab, 11, "start")
        lx += 16 + 7 * len(lab) + 18
    if xlabel: b += _t(left + pw / 2, h - 6, xlabel, 11, col=MUT)
    return _save(name, w, h, b, alt)

def pie(name, labels, values, alt, w=420, h=300, fmt=lambda v: f"{v}%"):
    cx, cy, r = 150, h / 2, 118
    tot = sum(values); a0 = -math.pi / 2; b = ""
    for k, (lab, v) in enumerate(zip(labels, values)):
        a1 = a0 + 2 * math.pi * v / tot
        x0, y0, x1, y1 = cx + r * math.cos(a0), cy + r * math.sin(a0), cx + r * math.cos(a1), cy + r * math.sin(a1)
        large = 1 if a1 - a0 > math.pi else 0
        b += f'<path d="M{cx},{cy} L{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f} Z" fill="{PAL[k]}" stroke="#fff" stroke-width="2"/>'
        am = (a0 + a1) / 2
        b += _t(cx + r * 0.62 * math.cos(am), cy + r * 0.62 * math.sin(am) + 5, fmt(v), 13, col="#fff", bold=True)
        a0 = a1
    ly = cy - 12 * len(labels)
    for k, lab in enumerate(labels):
        b += f'<rect x="290" y="{ly + 24 * k - 11}" width="13" height="13" fill="{PAL[k]}"/>' + _t(309, ly + 24 * k, lab, 13, "start")
    return _save(name, w, h, b, alt)

def vbar(name, cats, series, ymax, step, alt, ylabel="", w=560, h=320, show_values=True, fmt=lambda v: f"{v:,}"):
    """Grouped vertical bars. series: [(label, [values per cat])]."""
    left, right, top, bot = 54, 12, 16, 70
    pw, ph = w - left - right, h - top - bot
    Y = lambda v: top + ph - ph * v / ymax
    b = ""
    for v in range(0, int(ymax) + 1, step):
        b += f'<line x1="{left}" y1="{Y(v):.1f}" x2="{w - right}" y2="{Y(v):.1f}" stroke="{GRID}"/>' + _t(left - 6, Y(v) + 4, f"{v:,}", 11, "end", MUT)
    gw = pw / len(cats); n = len(series); bw = min(34, gw * 0.8 / n)
    for i, c in enumerate(cats):
        gx = left + gw * i + (gw - bw * n) / 2
        for k, (lab, vals) in enumerate(series):
            v = vals[i]; x = gx + k * bw
            b += f'<rect x="{x:.1f}" y="{Y(v):.1f}" width="{bw - 2:.1f}" height="{Y(0) - Y(v):.1f}" fill="{PAL[k]}"/>'
            if show_values: b += _t(x + (bw - 2) / 2, Y(v) - 4, fmt(v), 10)
        b += _t(left + gw * i + gw / 2, Y(0) + 16, c, 11)
    if n > 1:
        lx = left
        for k, (lab, _) in enumerate(series):
            b += f'<rect x="{lx}" y="{h - 22}" width="12" height="12" fill="{PAL[k]}"/>' + _t(lx + 16, h - 12, lab, 11, "start")
            lx += 16 + 7 * len(lab) + 18
    if ylabel: b += _t(14, top + ph / 2, ylabel, 11, col=MUT, extra=f' transform="rotate(-90 14 {top + ph / 2})"')
    return _save(name, w, h, b, alt)

def line(name, cats, series, ymin, ymax, step, alt, ylabel="", w=560, h=320, show_values=True, fmt=lambda v: f"{v:,}"):
    left, right, top, bot = 54, 16, 16, 70
    pw, ph = w - left - right, h - top - bot
    Y = lambda v: top + ph - ph * (v - ymin) / (ymax - ymin)
    X = lambda i: left + pw * (i + 0.5) / len(cats)
    b = ""
    v = ymin
    while v <= ymax:
        b += f'<line x1="{left}" y1="{Y(v):.1f}" x2="{w - right}" y2="{Y(v):.1f}" stroke="{GRID}"/>' + _t(left - 6, Y(v) + 4, fmt(v), 11, "end", MUT); v += step
    for i, c in enumerate(cats): b += _t(X(i), top + ph + 16, c, 11)
    for k, (lab, vals) in enumerate(series):
        pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(vals) if v is not None)
        b += f'<polyline points="{pts}" fill="none" stroke="{PAL[k]}" stroke-width="2.5"/>'
        for i, v in enumerate(vals):
            if v is None: continue
            b += f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="3.5" fill="{PAL[k]}"/>'
            if show_values: b += _t(X(i), Y(v) - 8, fmt(v), 10, col=PAL[k])
    if len(series) > 1:
        lx = left
        for k, (lab, _) in enumerate(series):
            b += f'<rect x="{lx}" y="{h - 22}" width="12" height="12" fill="{PAL[k]}"/>' + _t(lx + 16, h - 12, lab, 11, "start")
            lx += 16 + 7 * len(lab) + 18
    if ylabel: b += _t(14, top + ph / 2, ylabel, 11, col=MUT, extra=f' transform="rotate(-90 14 {top + ph / 2})"')
    return _save(name, w, h, b, alt)

def raw(name, w, h, body, alt):
    """Free-form figure: body is SVG markup drawn on a white w×h canvas."""
    return _save(name, w, h, body, alt)
