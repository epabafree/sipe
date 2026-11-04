/* ===== sipe — shared card engine (injected into every template) ===== */
(function () {
  var S = window.SIPE = window.SIPE || {};
  var DEF = { theme: 'auto', size: 2, font: 'serif', timer: 'show', steps: 'all' };

  /* ---------- storage ---------- */
  S.lsGet = function (k) { try { var v = localStorage.getItem(k); return v == null ? null : JSON.parse(v); } catch (e) { return (window.__sipeMem || {})[k] == null ? null : window.__sipeMem[k]; } };
  S.lsSet = function (k, v) { window.__sipeMem = window.__sipeMem || {}; window.__sipeMem[k] = v; try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} };
  S.ssGet = function (k) { window.__sipeSess = window.__sipeSess || {}; if (window.__sipeSess[k] != null) return window.__sipeSess[k]; try { var v = sessionStorage.getItem(k); return v == null ? null : JSON.parse(v); } catch (e) { return null; } };
  S.ssSet = function (k, v) { window.__sipeSess = window.__sipeSess || {}; window.__sipeSess[k] = v; try { sessionStorage.setItem(k, JSON.stringify(v)); } catch (e) {} };
  S.ssDel = function (k) { if (window.__sipeSess) delete window.__sipeSess[k]; try { sessionStorage.removeItem(k); } catch (e) {} };

  S.pref = function (k) { var p = S.lsGet('sipe:prefs') || {}; return p[k] == null ? DEF[k] : p[k]; };
  S.setPref = function (k, v) { var p = S.lsGet('sipe:prefs') || {}; p[k] = v; S.lsSet('sipe:prefs', p); S.apply(); };

  /* ---------- apply theme / size ---------- */
  S.apply = function () {
    var h = document.documentElement, t = S.pref('theme');
    h.classList.remove('sipe-light', 'sipe-dark');
    if (t === 'light') h.classList.add('sipe-light');
    if (t === 'dark') h.classList.add('sipe-dark');
    var r = document.querySelectorAll('.sipe');
    for (var i = 0; i < r.length; i++) {
      r[i].classList.remove('fs-1', 'fs-2', 'fs-3', 'pf-sans', 'tm-hide', 'tm-off');
      r[i].classList.add('fs-' + S.pref('size'));
      if (S.pref('font') === 'sans') r[i].classList.add('pf-sans');
      if (S.pref('timer') !== 'show') r[i].classList.add('tm-' + S.pref('timer'));
    }
    var m = document.querySelectorAll('.tb-pop [data-set]');
    for (var j = 0; j < m.length; j++) {
      var kv = m[j].getAttribute('data-set').split('=');
      m[j].classList.toggle('on', String(S.pref(kv[0])) === kv[1]);
    }
    var tb = document.querySelectorAll('[data-act=theme] .lbl');
    for (var q = 0; q < tb.length; q++) tb[q].textContent = t === 'auto' ? 'Auto' : t === 'light' ? 'Light' : 'Dark';
  };

  S.toast = function (msg) {
    var d = document.getElementById('sipe-toast');
    if (!d) { d = document.createElement('div'); d.id = 'sipe-toast'; document.body.appendChild(d); }
    d.textContent = msg; d.className = 'show';
    clearTimeout(window.__sipeToastT); window.__sipeToastT = setTimeout(function () { d.className = ''; }, 1300);
  };

  S.fmt = function (sec) { sec = Math.max(0, Math.round(sec)); var m = Math.floor(sec / 60), s = sec % 60; return m + ':' + (s < 10 ? '0' : '') + s; };
  S.typeset = function (el) { try { if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([el]).then(function () { S.fitMath(); }); } catch (e) {} };

  /* ---------- timer ---------- */
  S.timerStart = function (key) { S.ssSet('t:' + key, { s: Date.now(), e: null }); };
  S.timerStop = function (key) { var t = S.ssGet('t:' + key); if (t && t.e == null) { t.e = Date.now(); S.ssSet('t:' + key, t); } return t ? (t.e - t.s) / 1000 : null; };
  S.timerRead = function (key) { var t = S.ssGet('t:' + key); if (!t) return null; return ((t.e == null ? Date.now() : t.e) - t.s) / 1000; };
  S.timerLive = function (key, el) {
    if (window.__sipeTick) clearInterval(window.__sipeTick);
    if (!el) return;
    var upd = function () { var v = S.timerRead(key); if (v != null) el.textContent = S.fmt(v); };
    upd(); window.__sipeTick = setInterval(function () { if (!document.body.contains(el)) { clearInterval(window.__sipeTick); return; } upd(); }, 1000);
  };

  /* ---------- toolbar ---------- */
  S.toolbar = function (root) {
    var tb = root.querySelector('.tb'); if (!tb) return;
    var pop = tb.querySelector('.tb-pop');
    tb.querySelectorAll('[data-act]').forEach(function (b) {
      b.onclick = function (e) {
        e.stopPropagation();
        var a = b.getAttribute('data-act');
        if (a === 'theme') {
          var n = { auto: 'light', light: 'dark', dark: 'auto' }[S.pref('theme')] || 'auto';
          S.setPref('theme', n); S.toast('Theme: ' + (n === 'auto' ? 'follow Anki' : n));
        } else if (a === 'text') {
          pop.classList.toggle('open');
        } else if (a === 'calc') {
          S.calc(true);
        } else if (a === 'timer') {
          var nt = S.pref('timer') === 'show' ? 'hide' : 'show';
          S.setPref('timer', nt); S.toast(nt === 'show' ? 'Timer shown' : 'Timer hidden (still timing)');
        }
      };
    });
    if (pop) pop.querySelectorAll('[data-set]').forEach(function (b) {
      b.onclick = function (e) {
        e.stopPropagation();
        var kv = b.getAttribute('data-set').split('=');
        S.setPref(kv[0], kv[0] === 'size' ? +kv[1] : kv[1]);
        if (kv[0] === 'steps') S.stepMode(document);
      };
    });
    if (window.__sipeDocClick) document.removeEventListener('click', window.__sipeDocClick);
    window.__sipeDocClick = function (e) { var p = document.querySelectorAll('.tb-pop.open'); for (var i = 0; i < p.length; i++) if (!p[i].contains(e.target)) p[i].classList.remove('open'); };
    document.addEventListener('click', window.__sipeDocClick);
  };

  /* ---------- calculator (basic, like the CAT on-screen one) ---------- */
  S.calc = function (open) {
    var c = document.getElementById('sipe-calc');
    if (!c) {
      c = document.createElement('div'); c.id = 'sipe-calc';
      var keys = ['C', '⌫', '(', ')', '7', '8', '9', '÷', '4', '5', '6', '×', '1', '2', '3', '−', '0', '.', '√', '+', '%', '='];
      c.innerHTML = '<div class="cc-head"><span>Calculator</span><button class="cc-x" aria-label="Close">×</button></div>' +
        '<div class="cc-expr"></div><div class="cc-out">0</div><div class="cc-keys">' +
        keys.map(function (k) { return '<button data-k="' + k + '"' + (k === '=' ? ' class="eq"' : '') + '>' + k + '</button>'; }).join('') + '</div>';
      (document.querySelector('.sipe') || document.body).appendChild(c);
      var ex = '', ex_el = c.querySelector('.cc-expr'), out = c.querySelector('.cc-out');
      var ev = function (s) {
        var js = s.replace(/×/g, '*').replace(/÷/g, '/').replace(/−/g, '-').replace(/%/g, '/100').replace(/√(\d+\.?\d*)/g, 'Math.sqrt($1)').replace(/√\(/g, 'Math.sqrt(');
        if (!/^[0-9+\-*/().\s]*$/.test(js.replace(/Math\.sqrt/g, ''))) return 'Error';
        try { var r = Function('"use strict";return (' + (js || '0') + ')')(); if (!isFinite(r)) return 'Error'; return +parseFloat(r.toPrecision(12)); } catch (e) { return 'Error'; }
      };
      c.querySelectorAll('.cc-keys button').forEach(function (b) {
        b.onclick = function (e) {
          e.stopPropagation();
          var k = b.getAttribute('data-k');
          if (k === 'C') ex = '';
          else if (k === '⌫') ex = ex.slice(0, -1);
          else if (k === '=') { var r = ev(ex); out.textContent = r; ex = r === 'Error' ? '' : String(r); ex_el.textContent = ''; return; }
          else ex += k;
          ex_el.textContent = ex; var p = ev(ex); out.textContent = p === 'Error' ? '…' : p;
        };
      });
      c.querySelector('.cc-x').onclick = function (e) { e.stopPropagation(); c.classList.remove('open'); };
    }
    if (open) c.classList.toggle('open');
  };

  /* ---------- cross out options (right-click / long-press) ---------- */
  S.crossOut = function (opts) {
    opts.forEach(function (o) {
      o.addEventListener('contextmenu', function (e) { e.preventDefault(); if (!o.disabled) o.classList.toggle('struck'); });
      var t = null;
      o.addEventListener('touchstart', function () { o.__lp = false; t = setTimeout(function () { o.__lp = true; if (!o.disabled) { o.classList.toggle('struck'); try { navigator.vibrate && navigator.vibrate(15); } catch (e) {} } }, 520); }, { passive: true });
      ['touchend', 'touchmove', 'touchcancel'].forEach(function (ev) { o.addEventListener(ev, function () { clearTimeout(t); }, { passive: true }); });
    });
  };

  /* ---------- highlighter for passages ---------- */
  S.highlighter = function (scope) {
    var areas = scope.querySelectorAll('.hl-area');
    if (!areas.length) return;
    var btn = document.getElementById('sipe-hlbtn');
    if (!btn) { btn = document.createElement('button'); btn.id = 'sipe-hlbtn'; btn.type = 'button'; btn.textContent = 'Highlight'; document.body.appendChild(btn); }
    var pending = null;
    var show = function () {
      var sel = window.getSelection();
      if (!sel || sel.isCollapsed || !sel.rangeCount) { btn.style.display = 'none'; return; }
      var r = sel.getRangeAt(0), inside = false;
      areas.forEach(function (a) { if (a.contains(r.commonAncestorContainer)) inside = true; });
      if (!inside) { btn.style.display = 'none'; return; }
      pending = r.cloneRange();
      var rc = r.getBoundingClientRect();
      btn.style.display = 'block';
      btn.style.top = (window.scrollY + rc.top - 40) + 'px';
      btn.style.left = Math.max(8, Math.min(window.innerWidth - 100, window.scrollX + rc.left + rc.width / 2 - 45)) + 'px';
    };
    if (window.__sipeSelUp) { document.removeEventListener('mouseup', window.__sipeSelUp); document.removeEventListener('touchend', window.__sipeSelUp); }
    window.__sipeSelUp = function () { setTimeout(show, 10); };
    document.addEventListener('mouseup', window.__sipeSelUp); document.addEventListener('touchend', window.__sipeSelUp);
    btn.onmousedown = function (e) { e.preventDefault(); };
    btn.onclick = function (e) {
      e.preventDefault(); e.stopPropagation();
      if (!pending) return;
      var r = pending, root = r.commonAncestorContainer.nodeType === 1 ? r.commonAncestorContainer : r.commonAncestorContainer.parentNode;
      var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null), nodes = [], n;
      while ((n = w.nextNode())) if (r.intersectsNode(n) && n.nodeValue.trim()) nodes.push(n);
      nodes.forEach(function (tn) {
        var s = tn === r.startContainer ? r.startOffset : 0, en = tn === r.endContainer ? r.endOffset : tn.nodeValue.length;
        if (en <= s) return;
        var mid = tn.splitText(s); mid.splitText(en - s);
        var m = document.createElement('mark'); m.className = 'hl'; mid.parentNode.insertBefore(m, mid); m.appendChild(mid);
      });
      window.getSelection().removeAllRanges(); btn.style.display = 'none'; pending = null;
    };
    areas.forEach(function (a) {
      a.addEventListener('click', function (e) {
        var m = e.target.closest && e.target.closest('mark.hl');
        if (m && window.getSelection().isCollapsed) { var p = m.parentNode; while (m.firstChild) p.insertBefore(m.firstChild, m); p.removeChild(m); p.normalize(); }
      });
    });
  };

  /* ---------- nudge (first step, no answer) ---------- */
  S.nudge = function (root) {
    var b = root.querySelector('.nudge-btn'), box = root.querySelector('.nudge-box');
    if (b && box) b.onclick = function () { box.classList.toggle('open'); b.textContent = box.classList.contains('open') ? 'Hide nudge' : 'Need a nudge?'; S.typeset(box); };
  };

  /* ---------- step-by-step reveal on the answer side ---------- */
  S.stepMode = function (scope) {
    var groups = (scope || document).querySelectorAll('.steps');
    groups.forEach(function (g) {
      var st = g.querySelectorAll(':scope > .step'), nb = g.querySelector(':scope > .next-step');
      var fin = g.parentNode.querySelector('.final');
      if (S.pref('steps') !== 'one' || st.length < 2) {
        st.forEach(function (s) { s.classList.remove('hidden'); }); if (fin) fin.classList.remove('hidden'); if (nb) nb.remove(); return;
      }
      var shown = 1;
      var upd = function () {
        st.forEach(function (s, i) { s.classList.toggle('hidden', i >= shown); });
        if (fin) fin.classList.toggle('hidden', shown < st.length);
        if (nb) nb.style.display = shown >= st.length ? 'none' : '';
      };
      if (!nb) { nb = document.createElement('button'); nb.type = 'button'; nb.className = 'btn ghost next-step'; nb.textContent = 'Next step ▸'; g.appendChild(nb); }
      nb.onclick = function () { shown++; upd(); };
      upd();
    });
  };

  /* ---------- answer checking ---------- */
  S.norm = function (s) { return String(s).replace(/<[^>]*>/g, '').replace(/[\s,₹`]/g, '').toLowerCase(); };
  S.isRight = function (type, ans, v) {
    if (v == null || v === '') return false;
    if (type !== 'TITA') return String(ans).split('|').indexOf(String(v)) >= 0;
    var a = S.norm(v);
    return String(ans).split('|').some(function (b) {
      b = S.norm(b); if (a === b) return true;
      return /^-?\d*\.?\d+$/.test(a) && /^-?\d*\.?\d+$/.test(b) && Math.abs(parseFloat(a) - parseFloat(b)) < 1e-9;
    });
  };

  /* ---------- keep long equations inside the screen ---------- */
  S.fitMath = function () {
    var els = document.querySelectorAll('.sipe mjx-container[display="true"]');
    for (var i = 0; i < els.length; i++) {
      var el = els[i]; el.style.fontSize = '';
      var box = el.parentElement; if (!box || !el.offsetWidth) continue;
      var avail = box.clientWidth, need = el.scrollWidth;
      if (need > avail + 1) { var k = Math.max(0.7, avail / need); el.style.fontSize = Math.floor(k * 100) + '%'; }
    }
  };
  S.autoFit = function () {
    [150, 600, 1500, 3000].forEach(function (t) { setTimeout(S.fitMath, t); });
    if (window.__sipeFitR) window.removeEventListener('resize', window.__sipeFitR);
    window.__sipeFitR = function () { clearTimeout(window.__sipeFitT); window.__sipeFitT = setTimeout(S.fitMath, 150); };
    window.addEventListener('resize', window.__sipeFitR);
  };

  S.ready = function (fn) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn, { once: true }); else fn(); };
  S.apply();
  S.ready(S.autoFit);
})();
