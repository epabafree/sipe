# -*- coding: utf-8 -*-
# Simp Mock 18 (2025): VARC (24 of 24). DILR and QA: m25_18_dilr.py, m25_18_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(18, "sm25_18.json", series=2025)
P.passage("V1", "Passage 1 — The best of all possible worlds", "Philosophy_and_Psychology")
P.passage("V2", "Passage 2 — Digital rules in trade deals", "Economics_and_Management")
P.passage("V3", "Passage 3 — Underconsumption core", "Social_Science_and_History")
P.passage("V4", "Passage 4 — When science fails to correct itself", "Science_and_Technology")


def listed(n, direc):
    parts = [x.strip() for x in P.Q["VARC"][n]["q"].split("\n\n") if x.strip()]
    return f"<p>{direc}</p><ol class=\"sent\">" + "".join(f"<li>{x}</li>" for x in parts[1:]) + "</ol>"


P.va(1, P.summary_html(1, "When something traumatic"), P.Q["VARC"][1]["opts"], "MCQ", "2", "Summary", "Medium",
 "Overload causes intrusive memories; Tetris soon after can stop them forming.",
 steps(("The core", p("Trauma overloads memory filing, and disorganised storage returns as intrusive thoughts; a visual game soon after can block that.")),
       ("Choosing", p("Option 2 keeps both the problem and the specific finding. Option 4 claims it ‘prevents PTSD’, which goes further."))) + final("Option 2"),
 "summary", [("1", "‘Disorderliness causes trauma’ reverses it."), ("3", "Too vague."), ("4", "Overclaims.")])
P.va(2, P.ms(2), P.Q["VARC"][2]["opts"], "MCQ", "3", "Missing_Sentence", "Easy",
 "‘Instead’ answers what viruses can’t do; ‘new viral particles’ sets up ‘These newly formed particles’.",
 steps(("Find the spot", p("Blank 2 comes after ‘viruses lack the necessary metabolic machinery’ and before ‘These newly formed particles’.")),
       ("Match the label", p("Blank 2 is choice 3, labelled ‘Option 2’."))) + final("Choice 3 (“Option 2”)"),
 "missing", [("1", "“Option 1”: before what viruses lack."), ("2", "“Option 3”: after the particles are released."), ("4", "“Option 4”: near the end.")])

# ---------------- Passage 1 (Q3–6) ----------------
P.rc(3, "V1", "Inference", "2", "Medium",
 "How does the author rescue optimism at the end?",
 steps(("The line", ev(5, "is to make ‘the best of all possible worlds’ an aspiration, not a statement of belief") +
          p("Held as an aim, optimism needs no denial of reality, so it can sit with realism.")),
       ("Why not 1", p("The opening only reports a common doubt; the author moves past it."))) + final("Option 2"),
 "inference", [("1", "A view the author goes beyond."), ("3", "Blind faith is Pangloss, not the author’s optimism."), ("4", "The author says it’s more appealing now.")])
P.rc(4, "V1", "Purpose", "3", "Hard",
 "What does Pangloss stand for, and what does the author offer instead?",
 steps(("Pangloss", ev(2, "his article of faith seems increasingly blind") +
          p("A caricature of rigid, blind optimism.")),
       ("The contrast", p("The author ends with optimism as a flexible aspiration. Pangloss sets up that contrast; the passage doesn’t endorse Voltaire’s criticism of Leibniz."))) + final("Option 3"),
 "purpose", [("1", "The author defends Leibniz."), ("2", "Not a point about satire in general."), ("4", "Not about injustice.")])
P.rc(5, "V1", "Tone", "3", "Medium",
 "Does the author keep Leibniz’s idea as it was?",
 steps(("The line", ev(5, "That makes Leibnizian optimism more appealing than it has been for centuries") +
          p("Appreciative, and proposes a revised form (aspiration, not belief): appreciative and reformist."))) + final("Option 3"),
 "inference", [("1", "The opposite."), ("2", "Little criticism."), ("4", "Not a tone.")])
P.rc(6, "V1", "Purpose", "4", "Easy",
 "What principle did Leibniz extend from light?",
 steps(("The line", ev(2, "He soon realised that many other phenomena followed a similar ‘principle of optimality’ - including, perhaps, the entirety of God’s creation") +
          p("Optimal paths in nature hint at an optimal divine design."))) + final("Option 4"),
 "purpose", [("1", "The opposite of chance."), ("2", "Not what the light example shows."), ("3", "Not this example.")])

# ---------------- Passage 2 (Q7–10) ----------------
P.rc(7, "V2", "Main_Idea", "2", "Hard",
 "What is the harm of the trade-deal route?",
 steps(("The close", ev(4, "But such decisions should be made transparently, through open public discourse") +
          p("The worry is Big Tech getting around democratic oversight.")),
       ("Why not 3", p("Trade agreements are the method; the concern is what they bypass, democracy."))) + final("Option 2"),
 "summary", [("1", "Background."), ("3", "The means, not the core concern."), ("4", "Patents are Big Pharma’s past move.")])
P.rc(8, "V2", "Detail_Not_True", "4", "Medium",
 "Do the platforms themselves deny people loans and jobs?",
 steps(("The line", ev(2, "These systems can determine access to loans, jobs, housing, and legal outcomes") +
          p("Algorithms affect these; the complaint is that inspection is blocked, not that Big Tech denies loans.")),
       ("The others", p("Restrictive trade rules (1), blocked algorithm audits (2) and profit dressed as national interest (3) are named."))) + final("Option 4"),
 "except", [("1", "Paragraph 1."), ("2", "Paragraph 2."), ("3", "Paragraph 3.")])
P.rc(9, "V2", "Purpose", "3", "Easy",
 "‘conflating corporate profit with national interest obscures the truth’.",
 steps(("The line", ev(3, "But conflating corporate profit with national interest obscures the truth") +
          p("The paragraph criticises the framing of corporate interest as national interest."))) + final("Option 3"),
 "purpose", [("1", "It criticises, not shows."), ("2", "Not why they resist legally."), ("4", "Trade secrets are already protected.")])
P.rc(10, "V2", "Application", "4", "Easy",
 "The fear is regulation blocked by a trade deal.",
 steps(("The line", ev(1, "these rules would constrain efforts by governments to regulate privacy, data security, and market competition") +
          p("A country unable to enforce privacy law because of a trade deal is exactly that."))) + final("Option 4"),
 "inference", [("1", "Regulation working."), ("2", "Bias, not the trade-deal concern."), ("3", "Regulation working.")])

P.va(11, P.ms(11), P.Q["VARC"][11]["opts"], "MCQ", "1", "Missing_Sentence", "Easy",
 "A broad opening line.",
 steps(("Find the spot", p("Blank 1 opens the paragraph; ‘how the brain is organized’ leads into the wiring comparison.")),
       ("Match the label", p("Blank 1 is choice 1."))) + final("Option 1"),
 "missing", [("2", "Mid-explanation."), ("3", "Between aims and scanning."), ("4", "Before the closing caution.")])
P.va(12, listed(12, P.ODD_DIR), [], "TITA", "4", "Odd_One_Out", "Medium",
 "Suspicion, obvious signs, the iceberg, publishers’ response.",
 steps(("The chain", p("3 → 5 → 2 → 1: the suspicion; obvious signs in journals; Bik’s ‘tip of the iceberg’; publishers investigating with weak tools.")),
       ("The odd one", p("Sentence 4 is a quote about recognising the style, with no link to the others’ flow."))) + final("4"),
 "oddone", [("1", "Response."), ("2", "Warning."), ("3", "Opening."), ("5", "Evidence.")], why_title="How the other sentences fit")

# ---------------- Passage 3 (Q13–16) ----------------
P.rc(13, "V3", "Inference_Except", "1", "Medium",
 "Do adherents reject social media?",
 steps(("The point", ev(1, "The new viral trend on Tik-Tok encourages consumers to be a little less spend-happy") +
          p("The trend lives on social media; it rejects curated hauls, not the platform.")),
       ("The others", p("Disillusion with curated lifestyles (2), past overspending (3), and boomer parents who did it unnamed (4)."))) + final("Option 1"),
 "except", [("2", "‘perfectly curated homes’."), ("3", "Mychaskiw’s debt."), ("4", "Bertling’s parents.")])
P.rc(14, "V3", "Inference", "1", "Hard",
 "‘It’s not aesthetic, but it’s hers.’",
 steps(("The line", ev(4, "“It’s not aesthetic, but it’s hers,”") +
          p("Function and emotional value over the look; minimalism was ‘admittedly flawed’ as a curated style.")),
       ("Why not 3", p("Economic and environmental motives are part of it, but the passage doesn’t set minimalism apart on those grounds."))) + final("Option 1"),
 "inference", [("2", "No stricter limits."), ("3", "Not the contrast drawn."), ("4", "Not stated.")])
P.rc(15, "V3", "Application", "2", "Hard",
 "Recession-core: buy less, reuse, value an item’s life.",
 steps(("The idea", ev(4, "she takes satisfaction in giving things a second life") +
          p("Refurbished goods with their stories give items a second life: buying less new.")),
       ("The others", p("Designer pieces (1), budget hauls (3) and trendy clearance finds (4) still promote buying."))) + final("Option 2"),
 "inference", [("1", "Still aspirational buying."), ("3", "Still hauls."), ("4", "Still trend-chasing.")])
P.rc(16, "V3", "Main_Idea", "3", "Medium",
 "Kosak’s last words.",
 steps(("The line", ev(5, "It’s always better to step back and ask yourself: ‘What part of this is appealing to me, and why?’") +
          p("Ask what truly appeals; buy what lasts, not a look."))) + final("Option 3"),
 "summary", [("1", "Earlier paragraph."), ("2", "Not about minimalism."), ("4", "Not the point.")])

# ---------------- Passage 4 (Q17–20) ----------------
P.rc(17, "V4", "Inference", "2", "Medium",
 "What kind of irresponsibility: malice or neglect?",
 steps(("The line", ev(3, "Researchers say science is self-correcting, but often it isn’t or is unforgivably slow") +
          p("Failing to correct errors is widespread and costly.")),
       ("Why not 1", p("‘intentionally conceal … to protect their interests’ attributes motives the author doesn’t generalise."))) + final("Option 2"),
 "inference", [("1", "Assumes intent."), ("3", "Fabrication is one case."), ("4", "Too sweeping.")])
P.rc(18, "V4", "Detail_Not_True", "3", "Medium",
 "Is the lack of detection tools ever named?",
 steps(("Named", ev(4, "authors failing to proactively disclose data and editors not requiring its availability") +
          p("Slow acknowledgement (1), editors not requiring data (2), authors not sharing (4).")),
       ("The odd one", p("No missing detection mechanism is mentioned."))) + final("Option 3"),
 "except", [("1", "Thymus, Tessier-Lavigne."), ("2", "Reinhart–Rogoff."), ("4", "Reinhart–Rogoff.")])
P.rc(19, "V4", "Detail_Not_True", "4", "Medium",
 "What did the editor actually do?",
 steps(("Shown", ev(5, "Masliah was guilty of misconduct, leading to two retracted papers due to doctored images") +
          p("Manipulation (1), delayed public warning (2), harmful misuse of a diagnosis (3).")),
       ("The odd one", p("Editors refused to correct a published study; nothing shows them withholding flawed research."))) + final("Option 4"),
 "except", [("1", "Masliah."), ("2", "1940s to 1977."), ("3", "Thymus radiation.")])
P.rc(20, "V4", "Application", "1", "Easy",
 "The recommendations target errors and their correction.",
 steps(("The line", ev(6, "Scientists and journals must unwaveringly commit to correcting errors") +
          p("Data sharing and prompt correction would make findings less prone to distortion."))) + final("Option 1"),
 "inference", [("2", "Not implied."), ("3", "Not implied."), ("4", "Not the focus.")])

P.va(21, P.summary_html(21, "Electro-agriculture replaces"), P.Q["VARC"][21]["opts"], "MCQ", "3", "Summary", "Medium",
 "Electricity instead of sunlight; tandem electrolysis makes acetate efficiently.",
 steps(("The core", p("Electro-agriculture uses electricity in place of sunlight; tandem electrolysis makes acetate efficiently enough to feed plants.")),
       ("Choosing", p("Option 3 names the field, the method and the gain."))) + final("Option 3"),
 "summary", [("1", "Compares with photosynthesis’s efficiency; not claimed."), ("2", "Misses tandem electrolysis."), ("4", "Misses replacing sunlight.")])
P.va(22, P.summary_html(22, "The source of the contradictions"), P.Q["VARC"][22]["opts"], "MCQ", "4", "Summary", "Hard",
 "Three groups, bound by fear and grievance.",
 steps(("The core", p("An uneasy alliance of oligarchs, their victims and parasitic intellectuals, held together by grievance and fear.")),
       ("Choosing", p("Option 4 names all three and the binding agent."))) + final("Option 4"),
 "summary", [("1", "Leaves the victims out of the coalition."), ("2", "Misses the contradictions."), ("3", "Leaves out the intellectuals.")])
P.va(23, P.ms(23), P.Q["VARC"][23]["opts"], "MCQ", "1", "Missing_Sentence", "Easy",
 "The next words are ‘when Emperor Constantine…’.",
 steps(("Find the spot", p("Blank 3 follows the destruction in 196 B.C., and ‘when Emperor Constantine established it’ completes the sentence about 330 C.E.")),
       ("Match the label", p("Blank 3 is choice 1, labelled ‘Option 3’."))) + final("Choice 1 (“Option 3”)"),
 "missing", [("2", "“Option 1”: before the founding."), ("3", "“Option 2”: before the destruction."), ("4", "“Option 4”: after Constantine.")])
P.va(24, listed(24, P.ODD_DIR), [], "TITA", "2", "Odd_One_Out", "Medium",
 "A defence of planning tools against the abundance agenda.",
 steps(("The chain", p("1 → 3 → 4 → 5: the agenda neglects public input; involving communities helps; zoning’s benefits; reform, don’t abolish.")),
       ("The odd one", p("Sentence 2 widens to capitalism’s systemic flaws, outside the planning argument."))) + final("2"),
 "oddone", [("1", "Opening."), ("3", "Public input."), ("4", "Zoning."), ("5", "Proposal.")], why_title="How the other sentences fit")
