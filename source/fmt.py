# -*- coding: utf-8 -*-
"""Small HTML builders so every explanation has the same structure."""

def steps(*items):
    out = ['<div class="steps">']
    for i, it in enumerate(items, 1):
        h, b = it if isinstance(it, tuple) else (None, it)
        out.append(f'<div class="step"><div class="n">{i}</div><div class="b">' +
                   (f'<div class="h">{h}</div>' if h else '') + b + '</div></div>')
    out.append('</div>')
    return ''.join(out)

def final(x):
    return f'<div class="final">{x}</div>'

def trap(x):
    return f'<div class="trap"><b>Trap to avoid:</b> {x}</div>'

def ev(p, text):
    return f'<div class="ev"><span class="p">¶{p}</span>“{text}”</div>'

def why(rows):
    """rows: list of (label, html)"""
    return ''.join(f'<div class="ow"><span class="c">{k}</span><div>{v}</div></div>' for k, v in rows)

def table(head, rows, first_col_header=True, hi=None):
    """hi: set of (r, c) cells to highlight (0-based over body rows)."""
    hi = hi or set()
    h = '<tr>' + ''.join(f'<th>{x}</th>' for x in head) + '</tr>'
    b = ''
    for r, row in enumerate(rows):
        cells = ''
        for c, x in enumerate(row):
            cls = 'rh' if (c == 0 and first_col_header) else ('hi' if (r, c) in hi else '')
            cells += f'<td class="{cls}">{x}</td>' if cls else f'<td>{x}</td>'
        b += f'<tr>{cells}</tr>'
    return f'<div class="tbl"><table>{h}{b}</table></div>'

def p(*paras):
    return ''.join(f'<p>{x}</p>' for x in paras)
