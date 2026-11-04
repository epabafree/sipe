# -*- coding: utf-8 -*-
# Batch 2 — CAT 2023 Slot 1 VARC: Passages 2–4 (Q5–16) and VA Q18, 20, 22, 24.
import json, os
from fmt import steps, final, trap, ev, why, p
from data_varc import STRAT

X = json.load(open(os.path.join(os.path.dirname(__file__), "extract", "ex2_varc.json"), encoding="utf-8"))
PS, QT = X["passages"], {int(k): v for k, v in X["questions"].items()}
DIR = "The passage below is accompanied by four questions. Based on the passage, choose the best answer for each question."
def html_paras(s): return "".join(f"<p>{x.strip()}</p>" for x in s.split("\n\n"))

STRAT.update({
 "purpose": p("<b>“Why does the author mention…” questions:</b> reread the sentences just before and after the reference. The example always serves the claim being made <i>right there</i>, not the passage’s topic in general."),
 "detail": p("<b>Detail questions:</b> find the exact lines the question points to. The right option paraphrases them; wrong options exaggerate, invert or import outside ideas."),
 "inference": p("<b>Main goal / inference questions:</b> the answer must fit the whole passage, not one paragraph. Reject options that sound plausible in general but aren’t stated or implied here."),
 "weaken": p("<b>Weaken questions:</b> pin down the author’s actual claim first. The right option attacks that claim directly; options that only repeat a fact or slightly misstate a detail don’t weaken anything."),
})

PASS = {
 "P2": ("2023_S1_VARC_P2", "Passage 2 — Sahlins’s “Original Affluent Society” at fifty", "Social_Science_and_History"),
 "P3": ("2023_S1_VARC_P3", "Passage 3 — The return of wolves to Lozere", "Environment_and_Life_Science"),
 "P4": ("2023_S1_VARC_P4", "Passage 4 — Why scholars resist geographic explanations", "Social_Science_and_History"),
}
ITEMS, SOL = [], {}

def rc(qno, pkey, subtype, ans, diff, sol):
    sid, title, genre = PASS[pkey]
    ITEMS.append(dict(section="VARC", qno=qno, set_id=sid, set_title=title, directions=DIR, context=html_paras(PS[pkey]),
                      question=QT[qno]["q"], options=QT[qno]["opts"], qtype="MCQ", answer=ans,
                      topic=[f"VARC::RC::{genre}", f"Subtype::RC::{subtype}"], difficulty=diff))
    SOL[qno] = sol

# ---------------- Passage 2 ----------------
rc(5, "P2", "Purpose", "4", "Medium", dict(
 hint=p("Read the sentence that mentions Galbraith. Does it set Sahlins against Galbraith, or alongside him?"),
 solution=steps(
  ("Find the reference", ev(4, "With its title’s nod toward The Affluent Society (1958), economist John Kenneth Galbraith’s famously skeptical portrait of America’s postwar prosperity and inequality … “The Original Affluent Society” brought this critical perspective to bear on the contemporary world")),
  ("Read the relationship", p("“Nod toward” and “brought this critical perspective” mean Sahlins <b>extends</b> Galbraith’s critique of consumerism and inequality. He agrees with it rather than rebutting it or being shaped by it.")),
 ) + final("Option 4: Sahlins’s views complemented Galbraith’s criticism of contemporary consumerism and inequality.")
   + trap("Option 3 sounds close, but “pacifist” is never mentioned, and the reference is about Galbraith, not a general contrast."),
 concept=STRAT["purpose"],
 why=why([("1", "The passage never says Galbraith refutes Sahlins. The title is a respectful nod."),
          ("2", "Nothing says Galbraith <i>influenced</i> Sahlins’s analysis of prehistoric societies; the two critiques run in parallel."),
          ("3", "Adds “pacifist”, which isn’t in the passage, and misses that the point is the link to Galbraith.")])))

rc(6, "P2", "Purpose", "3", "Easy", dict(
 hint=p("What did the Hadza know about farming, and what did they do with that knowledge?"),
 solution=steps(
  ("Find the reference", ev(2, "The contemporary Hadza of Tanzania, who had long been surrounded by farmers, knew they had alternatives and rejected them. To Sahlins, this showed that … societies make real choices.")),
  ("Name the point", p("The Hadza example shows that foraging was a <b>choice</b>, not a result of not knowing better.")),
 ) + final("Option 3."),
 concept=STRAT["purpose"],
 why=why([("1", "Survival techniques aren’t the point; choice is."),
          ("2", "The passage says nothing about foragers hampering, or not hampering, nearby farming."),
          ("4", "Coexistence is the setting, not the point. The example is about the Hadza <i>rejecting</i> alternatives.")])))

rc(7, "P2", "Detail", "2", "Easy", dict(
 hint=p("Look at the last paragraph, where the author says what hasn’t “aged well”."),
 solution=steps(
  ("Find the criticism", ev(5, "While acknowledging the violence of colonialism, racism, and dispossession, it does not thematise them as heavily as we might today.")),
  ("Match it", p("“Does not thematise them as heavily” means the essay gives racism and colonialism only <b>cursory treatment</b>.")),
 ) + final("Option 2.")
   + trap("Option 4 echoes the second criticism (using foragers as proxies for the Paleolithic) but twists it into “outdated values”."),
 concept=STRAT["detail"],
 why=why([("1", "Rebuking anthropologists who treat foragers as “left behind” is described as Sahlins’s position, not a flaw."),
          ("3", "The author says empirical validity is <i>not</i> the point of the essay (¶3), so it isn’t criticised for weak data."),
          ("4", "The real criticism is that Sahlins, too, uses present-day foragers as proxies for the Paleolithic, not that his values are outdated.")])))

rc(8, "P2", "Inference", "2", "Medium", dict(
 hint=p("The author says the essay’s real interest is a “conceptual challenge to contemporary economic life”. Which option describes that?"),
 solution=steps(
  ("Find the purpose", ev(3, "the real interest … is … its conceptual challenge to contemporary economic life and bourgeois individualism")),
  ("Find the method", ev(4, "the classic anthropological move of showing that radical alternatives to the readers’ lives really exist")),
  ("Combine", p("Show an acquisitive society real communities that chose “wanting less”: that is <b>holding up a mirror</b>.")),
 ) + final("Option 2.")
   + trap("Option 4 reads the essay as a story of decline (“degenerated”); the passage presents foraging as a <i>choice</i>, not a lost golden age."),
 concept=STRAT["inference"],
 why=why([("1", "Sahlins builds on Galbraith; he doesn’t counter him."),
          ("3", "Growing inequality after the Neolithic Revolution is mentioned, but it isn’t the essay’s main goal."),
          ("4", "“Progressively degenerated” is a value-laden decline story the passage never tells.")])))

# ---------------- Passage 3 ----------------
rc(9, "P3", "Except", "4", "Easy", dict(
 hint=p("When did the Luparii operate, and what happened to the wolves while they did?"),
 solution=steps(
  ("List the causes the passage gives", p("Expanding forests, rural depopulation, fewer hunters, protected status, and NGO tracking (¶3).")),
  ("Check the Luparii", ev(2, "the royal office of the Luparii—wolf-catchers—was created … Those official hunters (and others) completed their job in the 1930s, when the last wolf disappeared") +
     p("The Luparii helped <b>wipe wolves out</b>. The passage never links the office’s shutting down to the wolves’ return.")),
 ) + final("Option 4."),
 concept=STRAT["except"],
 why=why([("1", "Contributed: forest cover rose by about 102,000 hectares a year (¶3)."),
          ("2", "Contributed: the wolf’s protected status helps recovery (¶3)."),
          ("3", "Contributed: “Rural depopulation is part of the story” (¶3).")])))

rc(10, "P3", "Detail", "1", "Medium", dict(
 hint=p("The last paragraph mentions an economic upside. Whose clash is it balancing?"),
 solution=steps(
  ("Find the solution", ev(4, "Farmers’ losses are real, but are not the only economic story. Tourist venues, such as parks where wolves are kept … also generate income and jobs")),
  ("Find the two sides", p("The clash is between “farmers and those who celebrate the predators’ return”, i.e. <b>environmentalists</b> (¶2: environmentalists are “delighted”).")),
 ) + final("Option 1: farmers and environmentalists.")
   + trap("Tourists are part of the solution, not one of the competing interests."),
 concept=STRAT["detail"],
 why=why([("2", "Tourists aren’t presented as having interests that compete with environmentalists."),
          ("3", "Politicians appear only once (an election quote); they aren’t one side of the conflict."),
          ("4", "Same: the conflict is farmers versus wolf supporters.")])))

rc(11, "P3", "Except", "4", "Easy", dict(
 hint=p("Separate the residents’ complaints from the reasons wolves are returning."),
 solution=steps(
  ("List the residents’ problems", ev(1, "mayors grumble about a lack of local schools, jobs, or phone and internet connections. Farmers of grazing animals add another concern: the return of wolves") + p("That covers schools, communication and livestock.")),
  ("Place the hunting decline", p("Fewer hunters appears in ¶3 as a <b>cause</b> of the wolves’ return, not as a problem the inhabitants complain about.")),
 ) + final("Option 4."),
 concept=STRAT["except"],
 why=why([("1", "Problem: lack of local schools."), ("2", "Problem: poor phone and internet connections."), ("3", "Problem: farmers’ livestock losses to wolves.")])))

rc(12, "P3", "Weaken", "4", "Medium", dict(
 hint=p("The author ends by saying wolves bring an economic upside through tourism. What would undercut that?"),
 solution=steps(
  ("Identify the claim", ev(4, "Farmers’ losses are real, but are not the only economic story. Tourist venues … generate income and jobs in rural areas.")),
  ("Attack it", p("If wolves increasingly <b>attack tourists</b>, wolf tourism becomes a liability, and the economic upside the author relies on falls apart.")),
 ) + final("Option 4.")
   + trap("Option 3 misstates a detail (wolves were eradicated, not “migrated out”), but the author’s argument doesn’t depend on that word."),
 concept=STRAT["weaken"],
 why=why([("1", "Agrees with the passage: residents already complain about jobs."),
          ("2", "Neutral: it neither helps nor hurts the author’s claims about wolves or tourism."),
          ("3", "Wrong on a detail, but wolves returning either way leaves the author’s argument untouched.")])))

# ---------------- Passage 4 ----------------
rc(13, "P4", "Except", "3", "Medium", dict(
 hint=p("Collect what the author actually blames non-geographers for, then spot the option that isn’t on the list."),
 solution=steps(
  ("List the criticisms", "<ol><li>Denouncing any geographic role as “geographic determinism” (¶3).</li><li>Reflexively rejecting geographic and biogeographic explanations (¶4).</li><li>Over-stressing contingency and individual decisions (¶4).</li></ol>"),
  ("Check option 3", p("The author criticises how scholars treat <i>geographic explanations</i>, not their interpretations of past cultural or historical events.")),
 ) + final("Option 3."),
 concept=STRAT["except"],
 why=why([("1", "Criticised: “denouncing ‘geographic determinism’” (¶3)."),
          ("2", "Criticised: the “reflex rejection of geographic explanations” (¶4)."),
          ("4", "Criticised: the historians’ habit of stressing contingency “based on individual decisions and chance” where it is unwarranted (¶4).")])))

rc(14, "P4", "Purpose", "3", "Medium", dict(
 hint=p("Both examples are introduced with “The explanation is straightforwardly geographic”. What does that say geography does?"),
 solution=steps(
  ("Read the examples", ev(2, "The explanation is straightforwardly geographic, rather than a cultural or historical quirk unrelated to geography") +
     p("The Inuit developed fur clothing because of the cold; Aboriginal Australians didn’t farm because no plants or animals there could be domesticated.")),
  ("Name the point", p("Physical circumstances <b>shaped</b> behaviour and culture: what people wore, and whether they farmed.")),
 ) + final("Option 3.")
   + trap("Option 2 sounds similar, but the examples aren’t about comparative “development” paths; they show geography determining specific behaviours."),
 concept=STRAT["purpose"],
 why=why([("1", "Self-sufficiency despite isolation is not the point being made."),
          ("2", "“Comparatively divergent paths in … development” imports a ranking of societies the passage avoids."),
          ("4", "Praises resourcefulness; the author’s point is causation by geography.")])))

rc(15, "P4", "Inference_Except", "1", "Hard", dict(
 hint=p("Check the word “most” in each option. Does the passage ever rank culture above geography?"),
 solution=steps(
  ("Find the passage’s position", ev(1, "Many human phenomena … are influenced both by geographic factors and by non-geographic factors.") +
     p("The passage says <b>both</b> matter. It never says that <i>most</i> phenomena come from culture and choice, with only some from geography.")),
  ("Confirm the others", p("Options 2, 3 and 4 each follow from a specific line (see below).")),
 ) + final("Option 1 cannot be inferred.")
   + trap("The quantifier “most” is the giveaway. Watch for options that add a ranking the passage never makes."),
 concept=STRAT["inference"],
 why=why([("2", "Inferable: today’s crops and animals in Australia are non-native, “brought to Australia by overseas colonists” (¶2)."),
          ("3", "Inferable: “many genetic, historical, psychological, and anthropological explanations advanced a century ago were also racist” (¶4)."),
          ("4", "Inferable: fur clothing wasn’t because “one influential Inuit leader persuaded other Inuit in 1783” (¶4).")])))

rc(16, "P4", "Except", "2", "Hard", dict(
 hint=p("Three options are <i>reasons</i> for the rejection. One option just restates the rejection itself."),
 solution=steps(
  ("List the author’s reasons", "<ol><li>Past racist geographic explanations tainted the field (¶4).</li><li>Historians’ tradition of stressing contingency and individual decisions (¶4).</li><li>Lack of technical geographic training (¶5).</li></ol>"),
  ("Spot the restatement", p("“Dismissal of explanations that involve geographical causes” <b>is</b> the behaviour being explained, not a reason for it.")),
 ) + final("Option 2.")
   + trap("Option 2 is true of these scholars, which makes it tempting, but it is the effect, not a cause."),
 concept=STRAT["except"],
 why=why([("1", "Reason 3: most historians and economists don’t acquire that detailed knowledge in training (¶5)."),
          ("3", "Reason 1: geographic explanations from a century ago were racist and tainted the rest (¶4)."),
          ("4", "Reason 2: historians stress contingency based on individual decisions (¶4).")])))

# ---------------- Verbal ability ----------------
def va(qno, qhtml, opts, qtype, ans, sub, diff, sol):
    ITEMS.append(dict(section="VARC", qno=qno, set_id="", set_title="", directions="", context="", question=qhtml, options=opts,
                      qtype=qtype, answer=ans, topic=[f"VARC::VA::{sub}"], difficulty=diff))
    SOL[qno] = sol

q18 = QT[18]["q"]
i, j = q18.index("Sentence:"), q18.index("Paragraph:")
va(18, f'<p>{q18[:i].strip()}</p><p class="quote"><b>Sentence:</b> {q18[i+9:j].strip()}</p><p class="quote"><b>Paragraph:</b> {q18[j+10:].strip()}</p>',
   QT[18]["opts"], "MCQ", "2", "Missing_Sentence", "Medium", dict(
 hint=p("The sentence says something is “difficult <b>enough</b>”. Which gap is followed by a sentence that makes things worse?"),
 solution=steps(
  ("Find the hook", p("The sentence after gap (2) begins “<b>What’s worse</b>, philosophers admonish each other to remain unsutured…”. “What’s worse” needs a preceding sentence saying something is already hard.")),
  ("Check the fit", p("Before gap (2): beliefs are “rendered implausible” and new ones “may be required”, i.e. a cut at one’s core beliefs. The inserted sentence names that cut, says it is “difficult enough”, and hands over to “What’s worse”.")),
  ("Match the label", p("Gap (2) is answer choice <b>2</b>, labelled “Option 2”.")),
 ) + final("Choice 2: the sentence goes in gap (2).")
   + trap("Again the labels are shuffled: choice 1 is “Option 4” and choice 3 is “Option 1”."),
 concept=STRAT["missing"],
 why=why([("1", "“Option 4” = gap (4): the paragraph is ending on lasting doubt, and nothing follows to be “worse”."),
          ("3", "“Option 1” = gap (1): too early, since the beliefs haven’t yet been “rendered implausible”."),
          ("4", "“Option 3” = gap (3): it follows the point about critical writing that offers no alternative, so it would interrupt rather than set up “What’s worse”.")])))

def sent_html(q):
    head, rest = q.split(" 1. ", 1)
    parts = []
    for k in range(2, 6):
        if f" {k}. " in rest:
            a, rest = rest.split(f" {k}. ", 1); parts.append(a)
    parts.append(rest)
    return f"<p>{head.strip()}</p><ol class=\"sent\">" + "".join(f"<li>{x.strip()}</li>" for x in parts) + "</ol>"

va(20, sent_html(QT[20]["q"]), [], "TITA", "3", "Odd_One_Out", "Medium", dict(
 hint=p("Four sentences describe something about the English <i>words</i> for numbers. Which one is about something else?"),
 solution=steps(
  ("Find the topic", p("Sentences 1, 5, 2 and 4 describe irregularities in how English <b>names</b> numbers.")),
  ("Build the chain", p("<b>1 → 5 → 2 → 4</b>: no systematic rule (1); you couldn’t guess “eleven” (5); “even more confusingly”, some words invert the order (2); multiples of ten follow yet another pattern (4).")),
  ("Spot the different job", p("Sentence 3 shifts to <b>children learning</b> the words: a consequence, not another irregularity.")),
 ) + final("The odd sentence is 3."),
 concept=STRAT["oddone"], why_title="How the other sentences fit",
 why=why([("1", "Opens: there is no systematic rule after ten."), ("5", "Example: “eleven” can’t be guessed."),
          ("2", "“Even more confusingly”: inversion in “fourteen”."), ("4", "A further pattern for multiples of ten.")])))

va(22, sent_html(QT[22]["q"]), [], "TITA", "4123", "Para_Jumble", "Medium", dict(
 hint=p("One sentence contrasts human bias with AI bias in general. Start there, then follow “widespread impact”."),
 solution=steps(
  ("Opener", p("Sentence 4 sets up the contrast: human bias is local, but AI spreads it “over a much wider scale”.")),
  ("Develop", p("Sentence 1 explains why: algorithms online are accessed by many, so the impact is far larger.")),
  ("Qualify", p("Sentence 2 says the bias really lies in the <b>data</b>, not the algorithms.")),
  ("Conclude", p("Sentence 3, “<b>Despite their widespread impact</b>”, refers back to 4 and 1 and closes on the hopeful note that AI bias is easier to fix.")),
 ) + final("4123"),
 concept=STRAT["pj"], why_title="Why not another order",
 why=why([("1423", "Starting with sentence 1 skips the human-versus-AI contrast that makes “much larger impact” meaningful."),
          ("4132", "“Despite their widespread impact” (3) reads as the conclusion; placing it before the data point (2) breaks the build-up.")])))

q24 = QT[24]["q"]
k = q24.index("Manipulating information")
va(24, f'<p>{q24[:k].strip()}</p><p class="quote">{q24[k:].strip()}</p>', QT[24]["opts"], "MCQ", "3", "Summary", "Medium", dict(
 hint=p("The passage has two halves: an ancient example, then today’s scale. The best summary links power-seeking then to technology now."),
 solution=steps(
  ("List the passage’s points", "<ol><li>Manipulating information is old: Octavian used it to <b>gain power</b>.</li><li>Today, technology and social networks weaponise it at an unprecedented scale.</li></ol>"),
  ("Compare the options", p("Option 3 keeps both: misinformation <b>for attaining power</b>, as old as Octavian, now <b>fuelled by technology</b>.")),
 ) + final("Option 3.")
   + trap("Option 1 is close but drops the power motive that the Octavian example exists to show."),
 concept=STRAT["summary"],
 why=why([("1", "Misses the link between disinformation and gaining power."),
          ("2", "Adds advice (“people need to become critical”) and “corruption”, neither of which is in the passage."),
          ("4", "Too narrow: it centres on Octavian and misses the unprecedented, technology-driven scale today.")])))
