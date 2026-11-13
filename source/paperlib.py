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


    # ---------- VA html from the plain question text (2024 onwards) ----------
    MS_DIR = "There is a sentence that is missing in the paragraph below. Look at the paragraph and decide where (option 1, 2, 3, or 4) the following sentence would best fit."
    SUM_DIR = "The passage given below is followed by four alternate summaries. Choose the option that best captures the essence of the passage."
    ODD_DIR = "Five jumbled up sentences (labelled 1, 2, 3, 4 and 5), related to a topic, are given below. Four of them can be put together to form a coherent paragraph. Identify the odd sentence and key in the number of that sentence as your answer."
    PJ_DIR = "The four sentences (labelled 1, 2, 3, 4) below, when properly sequenced, would yield a coherent paragraph. Decide on the proper sequencing of the order of the sentences and key in the sequence of the four numbers as your answer."

    def ms(self, qno):
        import re
        s = self.Q["VARC"][qno]["q"]
        i = s.index("Sentence:"); j = s.index("Paragraph")
        para = re.sub(r"_+\s*\(?\s*(\d)\s*\)?\s*_+", r"___(\1)___", s[j:].split(":", 1)[1].strip())
        para = re.sub(r"(___\(\d\)___)\s*—?\s*\.?", r"\1.", para)
        para = re.sub(r"([^.\s'’”\"?!])\s*(___\(\d\)___)", r"\1. \2", para)
        para = re.sub(r"\.+\s*(___\(\d\)___)", r". \1", para).replace("far- flung", "far-flung")
        para = re.sub(r"(___\(\d\)___\.)(?=\S)", r"\1 ", para)
        return (f'<p>{self.MS_DIR}</p><p class="quote"><b>Sentence:</b> {s[i+9:j].strip()}</p>'
                f'<p class="quote"><b>Paragraph:</b> {para}</p>')

    def summ(self, qno):
        return f'<p>{self.SUM_DIR}</p><p class="quote">{self.Q["VARC"][qno]["q"].strip()}</p>'

    def sents(self, qno, direc=None):
        import re
        s = " " + self.Q["VARC"][qno]["q"].replace("\n", " ")
        parts = [x.strip() for x in re.split(r"\s(?=[1-5]\.\s)", s) if x.strip()]
        parts = [re.sub(r"^[1-5]\.\s*", "", x) for x in parts]
        return f"<p>{direc or self.ODD_DIR}</p><ol class=\"sent\">" + "".join(f"<li>{x}</li>" for x in parts) + "</ol>"

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
    def __init__(self, n, extract_file, series=2023):
        super().__init__(0, n, extract_file)
        self.sid_prefix = f"SM{n:02d}_M" if series == 2023 else f"SM{series % 100}-{n:02d}_M"
        self.extra = {"mock": series * 100 + n}
