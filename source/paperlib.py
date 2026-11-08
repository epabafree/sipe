# -*- coding: utf-8 -*-
"""Helpers for writing one CAT paper's data module (questions + solutions) compactly."""
import json, os
from fmt import steps, final, trap, ev, why, table, p
from data_varc import STRAT
import b2_varc  # noqa: F401  (registers the extra STRAT entries: purpose, detail, inference, weaken)

RC_DIR = "The passage below is accompanied by four questions. Based on the passage, choose the best answer for each question."

class Paper:
    def __init__(self, year, slot, extract_file):
        self.year, self.slot = year, slot
        self.sid_prefix = f"{year}_S{slot}"
        self.extra = {}
        X = json.load(open(os.path.join(os.path.dirname(__file__), "extract", extract_file), encoding="utf-8"))
        self.P = X["passages"]
        self.Q = {s: {int(k): v for k, v in d.items()} for s, d in X["q"].items()}
        self.ITEMS, self.SOL = [], {"VARC": {}, "DILR": {}, "QA": {}}
        self.passages = {}

    # ---------- VARC ----------
    def passage(self, key, title, genre):
        self.passages[key] = (f"{self.sid_prefix}_VARC_{key}", title, genre)

    def html_paras(self, s):
        return "".join(f"<p>{x.strip()}</p>" for x in s.split("\n\n") if x.strip())

    def rc(self, qno, pkey, subtype, ans, diff, hint, solution, concept, why_rows, q=None, opts=None):
        sid, title, genre = self.passages[pkey]
        Q = self.Q["VARC"][qno]
        self.ITEMS.append(dict(**self.extra, section="VARC", qno=qno, slot=self.slot, year=self.year, set_id=sid, set_title=title, directions=RC_DIR,
                               context=self.html_paras(self.P[pkey]), question=q or Q["q"], options=opts or Q["opts"], qtype="MCQ",
                               answer=ans, topic=[f"VARC::RC::{genre}", f"Subtype::RC::{subtype}"], difficulty=diff))
        self.SOL["VARC"][qno] = dict(hint=p(hint), solution=solution, concept=STRAT[concept] if concept in STRAT else concept, why=why(why_rows))

    def va(self, qno, qhtml, opts, qtype, ans, sub, diff, hint, solution, concept, why_rows, why_title=None):
        self.ITEMS.append(dict(**self.extra, section="VARC", qno=qno, slot=self.slot, year=self.year, set_id="", set_title="", directions="", context="",
                               question=qhtml, options=opts, qtype=qtype, answer=ans, topic=[f"VARC::VA::{sub}"], difficulty=diff))
        d = dict(hint=p(hint), solution=solution, concept=STRAT[concept], why=why(why_rows))
        if why_title: d["why_title"] = why_title
        self.SOL["VARC"][qno] = d

    def missing_html(self, qno):
        import re
        s = re.sub(r" 1\. Option \d 2\. Option \d 3\. Option \d 4\. Option \d\s*$", "", self.Q["VARC"][qno]["raw"])
        i = s.index("Sentence:"); j = s.index("Paragraph")
        para = s[j:].split(":", 1)[1].strip()
        return (f'<p>{s[:i].strip()}</p><p class="quote"><b>Sentence:</b> {s[i+9:j].strip()}</p>'
                f'<p class="quote"><b>Paragraph:</b> {para}</p>')

    def strict_opts(self, qno):
        import re
        raw = self.Q["VARC"][qno]["raw"]
        m = re.search(r" 1\. (Option \d) 2\. (Option \d) 3\. (Option \d) 4\. (Option \d)\s*$", raw)
        return [x.strip() for x in m.groups()]

    def sent_html(self, qno):
        q = self.Q["VARC"][qno]["raw"]
        head, rest = q.split(" 1. ", 1)
        parts = []
        for k in range(2, 6):
            if f" {k}. " in rest:
                a, rest = rest.split(f" {k}. ", 1); parts.append(a)
        parts.append(rest)
        return f"<p>{head.strip()}</p><ol class=\"sent\">" + "".join(f"<li>{x.strip()}</li>" for x in parts) + "</ol>"

    def summary_html(self, qno, start):
        s = self.Q["VARC"][qno]["q"]; k = s.index(start)
        return f'<p>{s[:k].strip()}</p><p class="quote">{s[k:].strip()}</p>'

    # ---------- DILR ----------
    def dilr_set(self, n, title, directions, context, topic, setsol, shortcut, concept):
        sid = f"{self.sid_prefix}_DILR_S{n}"
        self._set = dict(sid=sid, title=title, directions=directions, context=context, topic=topic,
                         setsol=setsol, shortcut=shortcut, concept=concept)

    def dq(self, qno, q, opts, qtype, ans, diff, hint, solution, why_rows=None):
        s = self._set
        self.ITEMS.append(dict(**self.extra, section="DILR", qno=qno, slot=self.slot, year=self.year, set_id=s["sid"], set_title=s["title"], directions=s["directions"],
                               context=s["context"], question=q, options=opts, qtype=qtype, answer=ans, topic=[s["topic"]], difficulty=diff))
        self.SOL["DILR"][qno] = dict(hint=p(hint), solution=solution, setsol=s["setsol"], shortcut=s["shortcut"], concept=s["concept"],
                             why=why(why_rows) if why_rows else "")

    # ---------- QA ----------
    def qa(self, qno, q, opts, qtype, ans, topics, diff, hint, solution, shortcut="", concept="", why_rows=None):
        self.ITEMS.append(dict(**self.extra, section="QA", qno=qno, slot=self.slot, year=self.year, set_id="", set_title="", directions="", context="",
                               question=q, options=opts, qtype=qtype, answer=ans, topic=[f"QA::{t}" for t in topics], difficulty=diff))
        self.SOL["QA"][qno] = dict(hint=p(hint), solution=solution, shortcut=p(shortcut) if shortcut and not shortcut.startswith("<") else shortcut,
                             concept=concept, why=why(why_rows) if why_rows else "")

    def qtext(self, sec, qno):
        return self.Q[sec][qno]["q"], self.Q[sec][qno]["opts"]

    def sources(self):
        """(items, sol, section, origin) tuples for build.py."""
        return [([i for i in self.ITEMS if i["section"] == sec], self.SOL[sec], sec, f"{self.sid_prefix}") for sec in ("VARC", "DILR", "QA")]


class Mock(Paper):
    """A full-length mock test (not a CAT paper). Same helpers; its own IDs, decks and tags."""
    def __init__(self, n, extract_file):
        super().__init__(0, n, extract_file)
        self.sid_prefix = f"SM{n:02d}_M"
        self.extra = {"mock": n}
