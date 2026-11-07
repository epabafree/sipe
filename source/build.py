# -*- coding: utf-8 -*-
"""sipe — build the Anki package (.apkg), CSVs and media from source data."""
import csv, hashlib, json, os, re, shutil, sys, warnings
warnings.filterwarnings("ignore")
import genanki

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, "extract")]
import ex_varc, ex_dilr, ex_qa
import data_varc, data_dilr, data_qa
from data_ref import REF
from fmt import why as why_rows

ROOT = "sipe"
OUT = os.path.join(HERE, "out")
YEAR = 2023
FULL_PAPER = {2020: {"VARC": 26, "DILR": 24, "QA": 26}, 2019: {"VARC": 34, "DILR": 32, "QA": 34}}

def paper_name(y, n): return f"CAT {y} · Slot {n}"
SECN = {"VARC": "Verbal Ability & Reading Comprehension", "DILR": "Data Interpretation & Logical Reasoning", "QA": "Quantitative Aptitude"}
SEC_ORDER = {"VARC": 0, "DILR": 1, "QA": 2}

def rd(p): return open(os.path.join(HERE, "tpl", p), encoding="utf-8").read()
COMMON, TOOLBAR = rd("common.js"), rd("toolbar.html")
CSS = rd("style.css") + "\n" + rd("extra.css") + "\n" + rd("mock.css")
def tpl(name):
    s = rd(name).replace("%%COMMON%%", COMMON).replace("%%TOOLBAR%%", TOOLBAR)
    # Anki treats {{ }} as field markers — make sure no code accidentally contains them
    bad = [m for m in re.findall(r"\{\{([^}]*)\}\}", s) if not re.fullmatch(r"[#/^]?[A-Za-z]+", m)]
    assert not bad, (name, bad)
    return s

def model(mid, name, fields, qf, af, sort=0):
    return genanki.Model(mid, name, fields=[{"name": f} for f in fields],
                         templates=[{"name": "Card", "qfmt": tpl(qf), "afmt": af if af.startswith(("<", "{{")) else tpl(af)}],
                         css=CSS, sort_field_index=sort)

Q_FIELDS = ["QID", "Section", "SectionName", "Paper", "QNo", "QType", "SetID", "SetTitle", "Directions", "Context", "Question",
            "OptionA", "OptionB", "OptionC", "OptionD", "Answer", "Hint", "Solution", "SetSolution", "Shortcut", "Concept",
            "WhyOthers", "Topic", "Difficulty"]
SET_FIELDS = ["SetID", "Section", "SectionName", "Paper", "SetTitle", "Directions", "Context", "Questions", "Answers", "SetSolution", "Topic"]
REF_FIELDS = ["RID", "Kind", "Section", "SectionName", "TopicLabel", "Name", "Prompt", "Formula", "Symbols", "When", "Trap", "Example", "SeenIn"]
GUIDE_FIELDS = ["GID", "Title", "Body"]
PLAN_FIELDS = ["PID", "Title", "IndexJSON"]
MOCK_FIELDS = ["MockID", "Title", "DataJSON"]

M_Q = model(1841100001, "sipe · Question", Q_FIELDS, "q_front.html", "q_back.html")
M_SET = model(1841100002, "sipe · Set", SET_FIELDS, "set_front.html", "set_back.html")
M_REF = model(1841100003, "sipe · Formula & Technique", REF_FIELDS, "ref_front.html", "ref_back.html")
# Tool cards show the same page on both sides, so flipping one by accident changes nothing.
M_GUIDE = model(1841100004, "sipe · Guide", GUIDE_FIELDS, "guide_front.html", "{{FrontSide}}")
M_PLAN = model(1841100005, "sipe · Study Planner", PLAN_FIELDS, "planner_front.html", "{{FrontSide}}")
M_MOCK = model(1841100006, "sipe · Mock Test", MOCK_FIELDS, "mock_front.html", "{{FrontSide}}")
TOPIC_FIELDS = ["TopicID", "Title", "SectionName", "DataJSON"]
M_TOPIC = model(1841100007, "sipe · Topic Practice", TOPIC_FIELDS, "topic_front.html", "{{FrontSide}}")

# Top-level layout. Numbers keep the decks in this order in every Anki app.
D_START = f"{ROOT}::00 Start Here"
D_SEC = {"VARC": f"{ROOT}::01 Verbal Ability & Reading Comprehension", "DILR": f"{ROOT}::02 Data Interpretation & Logical Reasoning",
         "QA": f"{ROOT}::03 Quantitative Aptitude"}
D_TOPIC = f"{ROOT}::04 Practice by Topic"
D_REF = f"{ROOT}::05 Formulas & Concepts"
D_PAPERS = f"{ROOT}::06 Papers & Mocks"
SET_DECK = {"VARC": "Whole passages", "DILR": "Whole sets"}

def tagify(x): return re.sub(r"\s+", "_", x)
def label(path, section):
    return SECN[section] + " › " + " › ".join(NICE.get(p, p.replace("_", " ")) for p in path.split("::"))
def wrap(s): s = s.strip(); return s if s.startswith("<") else f"<p>{s}</p>"
def stack(s):
    """Break side-by-side display formulas onto separate lines so they fit on a phone."""
    if not s: return s
    s = s.replace(r"\qquad ", r"\]\[").replace(r"\qquad", r"\]\[")
    s = s.replace(r"\quad\text{(cyclic", r"\]\[\text{(cyclic")
    s = s.replace(r" \;\Rightarrow\; a_n + ", r"\]\[\Rightarrow\; a_n + ")
    return s

# ---------------- assemble questions ----------------
import b2_varc, b2_dilr, b2_qa
SOURCES = [(ex_varc.VARC, data_varc.SOL, "VARC", "pilot"), (b2_varc.ITEMS, b2_varc.SOL, "VARC", "b2"),
           (ex_dilr.DILR, data_dilr.SOL, "DILR", "pilot"), (b2_dilr.ITEMS, b2_dilr.SOL, "DILR", "b2"),
           (ex_qa.QA, data_qa.SOL, "QA", "pilot"), (b2_qa.ITEMS, b2_qa.SOL, "QA", "b2")]
# Later papers: one module per paper (VARC) plus its _dilr / _qa add-on modules, all sharing one Paper object.
import importlib
for base in ("b3_s2", "b4_s3", "b5_22s1", "b6_22s2", "b7_22s3", "b8_21s1", "b9_21s2", "b10_21s3", "b11_20s1", "b12_20s2", "b13_20s3", "b14_19s1"):
    try: P = importlib.import_module(base).P
    except ModuleNotFoundError: continue
    for extra in ("_dilr", "_qa"): importlib.import_module(base + extra)
    SOURCES += P.sources()
QS = []
for ex, sol, sec, origin in SOURCES:
    for q in ex:
        s = sol[q["qno"]]
        topics = [t for t in q["topic"] if not t.startswith("Subtype::")]
        subtypes = [t.replace("Subtype::", "") for t in q["topic"] if t.startswith("Subtype::")]
        main_topic = [t.split("::", 1)[1] if t.startswith(sec + "::") else t for t in topics]
        q2 = dict(q)
        q2.setdefault("slot", 1); q2.setdefault("year", YEAR)
        q2.update(qid=f"{q2['year']}-S{q2['slot']}-{sec}-{q['qno']:02d}", hint=s.get("hint", ""), solution=s["solution"],
                  shortcut=s.get("shortcut", ""), concept=s.get("concept", ""), why=s.get("why", ""),
                  setsol=s.get("setsol", ""), topics=main_topic, subtypes=subtypes)
        if s.get("why_title"): q2["why"] = f'<div class="why-title" hidden>{s["why_title"]}</div>' + q2["why"]
        if sec == "VARC":
            q2["shortcut"] = ""
        if sec == "DILR" and origin == "pilot":
            q2["setsol"] = data_dilr.SET_SOLUTION
            q2["shortcut"] = data_dilr.SHORTCUT
            q2["concept"] = data_dilr.CONCEPT
            q2["context"] = ex_dilr.CONTEXT
        q2["concept"] = stack(q2["concept"])
        QS.append(q2)
QS.sort(key=lambda q: (q["year"], q["slot"], SEC_ORDER[q["section"]], q["qno"]))
assert len({q["qid"] for q in QS}) == len(QS)

def q_tags(q):
    t = ["Card::Question", f"Section::{q['section']}", f"Year::{q['year']}", f"Paper::{q['year']}_S{q['slot']}", f"Slot::{q['slot']}",
         f"Format::{q['qtype']}", f"Difficulty::{q['difficulty']}"]
    t += [f"Topic::{q['section']}::{x}" for x in q["topics"]]
    t += [f"QuestionType::{x}" for x in q["subtypes"]]
    if q["set_id"]: t.append(f"Set::{q['set_id']}")
    return [tagify(x) for x in t]

def q_fields(q):
    o = (q["options"] + ["", "", "", ""])[:4]
    topic = "  ·  ".join(label(x, q["section"]) for x in q["topics"])
    return [q["qid"], q["section"], SECN[q["section"]], paper_name(q["year"], q["slot"]), str(q["qno"]), q["qtype"], q["set_id"], q["set_title"],
            q["directions"], q["context"].strip(), wrap(q["question"]), o[0], o[1], o[2], o[3], q["answer"], q["hint"],
            q["solution"], q["setsol"], q["shortcut"], q["concept"], q["why"], topic, q["difficulty"] + " (estimated)"]

# ---------------- set cards ----------------
def sq_html(q, i):
    opts = "".join(f'<button type="button" class="opt" data-k="{k}"><span class="key">{k}</span><span class="txt">{o}</span></button>'
                   for k, o in enumerate(q["options"], 1))
    return (f'<div class="sq q" data-qn="{q["qno"]}" data-type="{q["qtype"]}" data-ans="{q["answer"]}">'
            f'<div class="sq-h">Question {q["qno"]} · {q["qtype"]}</div><div class="question hl-area">{wrap(q["question"])}</div>'
            + (f'<div class="opts">{opts}</div>' if q["qtype"] == "MCQ" else
               '<div class="tita"><input type="text" autocomplete="off" placeholder="Your answer"><button type="button" class="btn">Check</button></div>')
            + '<div class="feedback"></div></div>')

def sqa_html(q):
    aos = "".join(f'<span class="ao" data-k="{k}"><span class="num">{k}</span>{o}</span>' for k, o in enumerate(q["options"], 1))
    aos += f'<span class="ao" data-k="t">{q["answer"]}</span>'
    return (f'<div class="block sqa" data-qn="{q["qno"]}"><h4>Question {q["qno"]}</h4>'
            f'<div class="answer-box"><span class="k">Answer</span><div class="v">{aos}</div></div>'
            + q["solution"] + (f'<div class="sub">Why the other options don’t work</div>{q["why"]}' if q["why"] and q["qtype"] == "MCQ" else "")
            + (f'<div class="sub">Strategy</div>{q["concept"]}' if q["section"] == "VARC" and q["concept"] else "") + "</div>")

SETS = []
for sid in sorted({q["set_id"] for q in QS if q["set_id"]}, key=lambda s: (s.split("_")[0], s.split("_")[1], SEC_ORDER[s.split("_")[2]], s)):
    members = [q for q in QS if q["set_id"] == sid]
    f = members[0]
    SETS.append(dict(sid=sid, section=f["section"], title=f["set_title"], directions=f["directions"], context=f["context"].strip(),
                     questions="".join(sq_html(q, i) for i, q in enumerate(members)), answers="".join(sqa_html(q) for q in members),
                     setsol=f["setsol"], topics=f["topics"], members=members, year=f["year"], slot=f["slot"]))

# ---------------- reference cards ----------------
# VARC technique cards list every question of their type automatically.
SUB2REF = {"RC::Except": "VARC-RC-001", "RC::Detail_Not_True": "VARC-RC-001", "RC::Inference_Except": "VARC-RC-001", "RC::Odd_Pair": "VARC-RC-002",
           "RC::Weaken_Except": "VARC-RC-003", "RC::Purpose": "VARC-RC-004", "RC::Detail": "VARC-RC-005", "RC::Inference": "VARC-RC-006",
           "RC::Main_Idea": "VARC-RC-006", "RC::Application": "VARC-RC-006", "RC::Weaken": "VARC-RC-007",
           "VA::Missing_Sentence": "VARC-VA-001", "VA::Odd_One_Out": "VARC-VA-002", "VA::Para_Jumble": "VARC-VA-003", "VA::Summary": "VARC-VA-004"}
_refs = {r["rid"]: r for r in REF}
for q in QS:
    if q["section"] != "VARC": continue
    for k in (q["subtypes"] or q["topics"]):
        r = _refs.get(SUB2REF.get(k, ""))
        if r is not None and q["qid"] not in r["seen"]: r["seen"].append(q["qid"])
for r in REF:
    r["seen"].sort(key=lambda x: [int(t) if t.isdigit() else t for t in re.split(r"[-S]", x)])
assert all(x in {q["qid"] for q in QS} for r in REF for x in r["seen"]), [x for r in REF for x in r["seen"] if x not in {q["qid"] for q in QS}]
TECH_TOPIC = {"VARC-RC-001": "RC", "VARC-RC-002": "RC", "VARC-RC-003": "RC", "VARC-RC-004": "RC", "VARC-RC-005": "RC", "VARC-RC-006": "RC", "VARC-RC-007": "RC", "VARC-VA-001": "VA::Missing_Sentence",
              "VARC-VA-002": "VA::Odd_One_Out", "VARC-VA-003": "VA::Para_Jumble", "VARC-VA-004": "VA::Summary"}
def ex_math(s):
    """Long inline maths can't wrap on a phone: show it as display maths (one line per ⇒) so it can be scaled to fit."""
    return re.sub(r"\\\(((?:(?!\\\)).){28,})\\\)", lambda m: "\\[" + m.group(1).replace(r" \Rightarrow ", r"\]\[\Rightarrow ") + "\\]", s)
def ref_fields(r):
    topic = TECH_TOPIC.get(r["rid"], r["topic"])
    sym = ""
    if r["symbols"]:
        sym = '<div class="tbl"><table><tr><th>Symbol</th><th>Meaning</th></tr>' + "".join(
            f'<tr><td>{a}</td><td style="text-align:left;white-space:normal">{b}</td></tr>' for a, b in r["symbols"]) + "</table></div>"
    return topic, [r["rid"], r["kind"], r["section"], SECN[r["section"]], " › ".join(x.replace("_", " ") for x in topic.split("::")),
                   r["name"], r["prompt"], stack(r["formula"]), sym, r["when"], r["trap"], ex_math(r["example"]), ", ".join(r["seen"])]

# ---------------- guide ----------------
ICON = lambda d: f'<span class="ic"><svg viewBox="0 0 24 24">{d}</svg></span>'
WELCOME = f"""
<p>sipe has the questions from past CAT papers as cards you can solve, each with a worked solution. You can start straight away; the rest of this page explains the extras.</p>
<h2>How the decks are laid out</h2>
<div class="tbl"><table>
<tr><td class="rh">01 · 02 · 03</td><td style="text-align:left;white-space:normal">One deck per section, then by year and slot, for example <span class="path">03 Quantitative Aptitude ▸ 2023 ▸ Slot 1</span>. Questions come in the original exam order. Whole RC passages and DILR sets, with all their questions on one card, sit at the end of their section.</td></tr>
<tr><td class="rh">04 Practice by Topic</td><td style="text-align:left;white-space:normal">Every question on a topic, say <span class="path">Quantitative Aptitude ▸ Algebra</span>, from all the papers, with the source paper shown on each.</td></tr>
<tr><td class="rh">05 Formulas &amp; Concepts</td><td style="text-align:left;white-space:normal">Short reference cards: the formula, what each symbol means, when it helps, and a quick example. For VARC, the approach for each question type.</td></tr>
<tr><td class="rh">06 Papers &amp; Mocks</td><td style="text-align:left;white-space:normal">One card per paper. <b>Practice</b> lets you move freely through the paper and check answers as you go; <b>Timed mock</b> gives you exam conditions and a CAT-style score.</td></tr>
</table></div>
<h2>Solving a question</h2>
<ol><li>Open a section deck and work through the cards.</li>
<li>Tap an option, press <b>1–4</b>, or type your answer for TITA questions. You’ll see straight away whether it’s right.</li>
<li>Show the answer to read the solution: the steps, a shortcut where there is one, the key idea, and why the other options don’t hold up.</li>
<li>Rate the card as usual. If you got it wrong, <b>Again</b> brings it back soon.</li></ol>
<h2>Coming back to questions you’ve already done</h2>
<p>Anki normally hides a card until it’s due. To redo something whenever you like, use the practice cards instead: a paper in <span class="path">06 Papers &amp; Mocks</span>, or a topic in <span class="path">04 Practice by Topic</span>. They keep their own ticks, have a <b>Try again</b> button on every question, and a link to start afresh. Nothing you do there changes your reviews.</p>
<p class="small">Paper and topic cards don’t need to be rated. Close them when you’re done and they stay available.</p>
<h2>The small toolbar (top right)</h2>
<div class="gtool">{ICON('<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2M9.5 2.5h5"/>')}<div><b>Timer</b>: runs while you solve and shows your time on the answer side. Tap to hide it, or turn it off in <b>Aa</b>. There are no targets.</div></div>
<div class="gtool">{ICON('<rect x="5" y="3" width="14" height="18" rx="2.5"/><path d="M8.5 7.5h7"/>')}<div><b>Calculator</b>: a basic one, much like the on-screen calculator in the exam.</div></div>
<div class="gtool">{ICON('<path d="M3 19 8.5 5h1L15 19M5 14h8"/>')}<div><b>Aa</b>: text size, passage font, the timer, and whether solutions open all at once or one step at a time.</div></div>
<div class="gtool">{ICON('<circle cx="12" cy="12" r="8.5"/>')}<div><b>Theme</b>: Auto (follows Anki), Light or Dark.</div></div>
<h2>Small things that help</h2>
<ul><li><b>Cross out an option</b> you’ve ruled out: right-click it on a computer, or long-press it on a phone.</li>
<li><b>Highlight</b> words in a passage or DILR set: select them and tap <b>Highlight</b>. Tap a highlight to remove it.</li>
<li><b>Need a nudge?</b> under the options shows just the first step, without giving the answer away.</li>
<li><b>Flags</b>, if you like using them, work as usual in Anki. The Study Planner can gather flagged cards for you later.</li></ul>
<h2>Study Planner</h2>
<p>The next card in this deck helps you put together a set of questions by topic, year, slot or difficulty, or the ones you got wrong recently, and gives you a search to paste into Anki. No search syntax needed.</p>
<h2>Keeping track</h2>
<p>Anki keeps the record for you: <b>Stats</b> shows your reviews and accuracy over time, and <b>Card Info</b> in the Browse window shows how long each attempt took.</p>
"""

# ---------------- practice by topic ----------------
AREA_NAME = {"RC": "Reading Comprehension", "VA": "Verbal Ability", "DI": "Data Interpretation", "LR": "Logical Reasoning"}
RC_TYPE = {"Except": "All-except questions", "Detail_Not_True": "Not supported by the passage", "Inference_Except": "Inference (except)",
           "Odd_Pair": "Odd pair out", "Weaken_Except": "Weaken (except)", "Purpose": "Purpose of a detail", "Detail": "Detail",
           "Inference": "Inference", "Main_Idea": "Main idea", "Application": "Applying the argument", "Weaken": "Weaken"}
INTRO = {"VARC": "Every question of this kind from the papers in this deck, gathered in one place. Passages come along with their questions, and each question shows which paper it is from.",
         "DILR": "Every set of this kind from the papers in this deck, gathered in one place. Each question shows which paper it is from, so you can see how the style has changed over the years.",
         "QA": "Every question on this topic from the papers in this deck, gathered in one place. Each question shows which paper it is from. Pick a smaller topic below if you’d like to focus."}
NICE = {"Profit_Loss_and_Discount": "Profit, Loss and Discount", "Time_Speed_and_Distance": "Time, Speed and Distance",
        "Statistics_Mean_Median_Mode": "Mean, Median and Mode", "Odd_One_Out": "Odd Sentence Out", "Para_Jumble": "Para Jumbles",
        "Logic_Based_DI": "Logic-based DI", "Simple_and_Compound_Interest": "Simple and Compound Interest"}
def nice(x): return NICE.get(x, x.replace("_", " "))
def topic_groups():
    groups = {}
    for q in sorted(QS, key=lambda q: (-q["year"], q["slot"], SEC_ORDER[q["section"]], q["qno"])):
        sec = q["section"]; keys = []
        if sec == "VARC":
            area = q["topics"][0].split("::")[0]
            keys = [(area, ("RC::" + st.split("::")[1]) if area == "RC" else q["topics"][0]) for st in (q["subtypes"] or [q["topics"][0]])] if area == "RC" else [(area, q["topics"][0])]
        else:
            keys = [(t.split("::")[0], t) for t in q["topics"]]
        seen = set()
        for area, sub in keys:
            g = groups.setdefault((sec, area), {"subs": {}, "qs": {}})
            label = RC_TYPE.get(sub.split("::")[-1], nice(sub.split("::")[-1])) if sec == "VARC" and area == "RC" else nice(sub.split("::")[-1])
            g["subs"].setdefault(sub, label)
            if q["qid"] not in g["qs"]:
                g["qs"][q["qid"]] = {"id": q["qid"], "section": sec, "qno": q["qno"], "qtype": q["qtype"], "options": q["options"], "answer": q["answer"],
                    "set_title": q["set_title"], "directions": q["directions"], "context": q["context"].strip(), "question": wrap(q["question"]),
                    "solution": q["solution"], "shortcut": q["shortcut"], "paper": f"CAT {q['year']} Slot {q['slot']}",
                    "src": f"CAT {q['year']} · Slot {q['slot']} · Question {q['qno']}", "subs": [], "label": ""}
            e = g["qs"][q["qid"]]
            if sub not in e["subs"]: e["subs"].append(sub)
            e["label"] = " · ".join(g["subs"][x] for x in e["subs"])
    out = []
    for sec in ("VARC", "DILR", "QA"):
        for (s2, area), g in sorted(groups.items(), key=lambda kv: kv[0][1]):
            if s2 != sec: continue
            subs = [{"key": k, "label": v} for k, v in sorted(g["subs"].items(), key=lambda kv: kv[1])]
            out.append((sec, area, AREA_NAME.get(area, nice(area)), INTRO[sec], {"subs": subs, "qs": list(g["qs"].values())}))
    return out

def deck_id(name): return int(hashlib.md5(name.encode()).hexdigest()[:8], 16) + 1_500_000_000

def main():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "csv")); os.makedirs(os.path.join(OUT, "media"))
    decks, rows = {}, {}
    def deck(name, desc=""):
        if name not in decks: decks[name] = genanki.Deck(deck_id(name), name, description=desc)
        return decks[name]
    def add(dname, mdl, fields, tags, guid_key, due, csvname):
        n = genanki.Note(model=mdl, fields=fields, tags=[f"{ROOT}::{t}" for t in tags], guid=genanki.guid_for("sipe:" + guid_key), due=due)
        deck(dname).add_note(n)
        rows.setdefault(csvname, (mdl, []))[1].append([n.guid, mdl.name, dname, " ".join(n.tags)] + fields)
        return n
    deck(ROOT, "<b>sipe</b> · CAT previous-year questions. New here? Open <b>00 Start Here</b>.")
    index = []

    # Start Here
    add(D_START, M_GUIDE, ["welcome", "Welcome to sipe", WELCOME], ["Card::Guide"], "guide-welcome", 1, "start_here_guide")
    # questions
    for q in QS:
        tags = q_tags(q)
        due = 10_000_000 + q["year"] * 1000 + q["slot"] * 100 + SEC_ORDER[q["section"]] * 40 + q["qno"]
        add(f"{D_SEC[q['section']]}::{q['year']}::Slot {q['slot']}", M_Q, q_fields(q), tags, q["qid"], due, f"questions_{q['section']}")
        index.append({"t": tags})
    # sets
    for i, s in enumerate(SETS):
        tags = ["Card::Set", f"Section::{s['section']}", f"Year::{s['year']}", f"Paper::{s['year']}_S{s['slot']}", f"Slot::{s['slot']}", f"Set::{s['sid']}"] + \
               [f"Topic::{s['section']}::{x}" for x in s["topics"]]
        tags = [tagify(x) for x in tags]
        topic = "  ·  ".join(label(x, s["section"]) for x in s["topics"])
        add(f"{D_SEC[s['section']]}::{SET_DECK[s['section']]}", M_SET, [s["sid"], s["section"], SECN[s["section"]], paper_name(s["year"], s["slot"]), s["title"], s["directions"], s["context"],
            s["questions"], s["answers"], s["setsol"], topic], tags, "set-" + s["sid"], 20_000_000 + i, "sets")
        index.append({"t": tags})
    # reference
    for i, r in enumerate(REF):
        topic, f = ref_fields(r)
        area = topic.split("::")[0].replace("_", " ")
        dname = f"{D_REF}::{SECN[r['section']]}" + (f"::{area}" if r["section"] == "QA" else "")
        tags = [tagify(x) for x in [f"Card::{r['kind']}", f"Section::{r['section']}", f"Topic::{r['section']}::{topic}"]]
        add(dname, M_REF, f, tags, "ref-" + r["rid"], 30_000_000 + i, "formulas_techniques")
        index.append({"t": tags})
    # planner
    topics = {}
    for it in index:
        for t in it["t"]:
            if t.startswith("Topic::"):
                parts = t.split("::")[1:]
                if len(parts) >= 2:
                    sec, area = parts[0], parts[1]
                    lst = topics.setdefault(sec, {}).setdefault(area, [])
                    if len(parts) >= 3 and parts[2] not in lst: lst.append(parts[2])
    topics = {s: topics[s] for s in ("VARC", "DILR", "QA") if s in topics}
    years = sorted({t.split("::")[1] for it in index for t in it["t"] if t.startswith("Year::")}, reverse=True)
    slots = sorted({t.split("::")[1] for it in index for t in it["t"] if t.startswith("Slot::")})
    pdata = json.dumps({"root": ROOT, "topics": topics, "years": years, "slots": slots, "items": index}, ensure_ascii=False).replace("</", "<\\/")
    add(D_START, M_PLAN, ["planner", "Study Planner", pdata], ["Card::Guide"], "planner", 2, "start_here_planner")
    # papers: one card per paper, newest first
    for pi, (py, pn) in enumerate(sorted({(q["year"], q["slot"]) for q in QS}, reverse=True)):
        pq = [q for q in QS if (q["year"], q["slot"]) == (py, pn)]
        mq = [{"id": q["qid"], "section": q["section"], "qno": q["qno"], "qtype": q["qtype"], "options": q["options"], "answer": q["answer"],
               "set_title": q["set_title"], "directions": q["directions"], "context": q["context"].strip(), "question": wrap(q["question"]),
               "solution": q["solution"], "shortcut": q["shortcut"],
               "topic": " › ".join(x.replace("_", " ") for x in q["topics"][0].split("::"))} for q in pq]
        name = paper_name(py, pn)
        full = FULL_PAPER.get(py, {"VARC": 24, "DILR": 20, "QA": 22}); nfull = sum(full.values())
        ttl = f"{name} · full paper, {len(mq)} questions" if len(mq) >= nfull else f"{name} · {len(mq)} of {nfull} questions (the rest aren’t in the source)"
        mdata = json.dumps({"title": ttl, "full": full, "questions": mq}, ensure_ascii=False).replace("</", "<\\/")
        gkey = f"mock-{py}-S{pn}-pilot" if (py, pn) == (2023, 1) else f"mock-{py}-S{pn}"   # keep the v0.2 GUID
        add(f"{D_PAPERS}::CAT {py}::Slot {pn}", M_MOCK, [f"{py}-S{pn}", name, mdata], ["Card::Mock", f"Year::{py}", f"Paper::{py}_S{pn}"], gkey, 40_000_000 + pi, "mock")

    # practice by topic: one tool card (in its own deck) per section area
    for i, (sec, area, title, intro, items) in enumerate(topic_groups()):
        tdata = json.dumps({"title": title, "intro": intro, "subs": items["subs"], "questions": items["qs"]}, ensure_ascii=False).replace("</", "<\\/")
        add(f"{D_TOPIC}::{SECN[sec]}::{title}", M_TOPIC, [f"topic-{sec}-{area}", title, SECN[sec], tdata],
            ["Card::Topic", f"Section::{sec}"], f"topic-{sec}-{area}", 35_000_000 + i, "topic_practice")

    media = sorted(os.path.join(HERE, "media", m) for m in os.listdir(os.path.join(HERE, "media")))
    pkg = genanki.Package(list(decks.values())); pkg.media_files = media
    apkg = os.path.join(OUT, "sipe.apkg"); pkg.write_to_file(apkg)
    for m in media: shutil.copy(m, os.path.join(OUT, "media"))
    for name, (mdl, rr) in rows.items():
        with open(os.path.join(OUT, "csv", f"sipe_{name}.csv"), "w", encoding="utf-8", newline="") as fh:
            fh.write("#separator:Comma\n#html:true\n#guid column:1\n#notetype column:2\n#deck column:3\n#tags column:4\n")
            fh.write("#columns:" + ",".join(["GUID", "Notetype", "Deck", "Tags"] + [f["name"] for f in mdl.fields]) + "\n")
            w = csv.writer(fh, quoting=csv.QUOTE_ALL, lineterminator="\n")
            for r in rr: w.writerow(r)
    print("papers", sorted({(q["year"], q["slot"]) for q in QS}), "questions", len(QS), "sets", len(SETS), "refs", len(REF), "->", apkg)

if __name__ == "__main__":
    main()
