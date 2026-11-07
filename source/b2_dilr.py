# -*- coding: utf-8 -*-
# Batch 2 — CAT 2023 Slot 1 DILR: Set 1 (Q1–5 housing complex), Set 2 (Q6–10 dean election), Set 4 (Q16–20 visa office).
from fmt import steps, final, trap, why, table, p

ITEMS, SOL, SETINFO = [], {}, {}

# ======================= SET 1 =======================
S1 = "2023_S1_DILR_S1"
S1_TITLE = "Set 1 — Houses, roads and quoted prices"
S1_DIR = "Read the instructions given and answer the questions that follow:"
S1_CTX = r"""
<p>The schematic diagram below shows 12 rectangular houses in a housing complex. House numbers are mentioned in the rectangles representing the houses. The houses are located in six columns – Column-A through Column-F, and two rows – Row-1 and Row-2. The houses are divided into two blocks - Block XX and Block YY. The diagram also shows two roads, one passing in front of the houses in Row-2 and another between the two blocks.</p>
<p class="fig"><img src="sipe_2023S1_DILR_S1.svg" alt="Block XX (columns A–C) and Block YY (columns D–F), two rows; a road between the blocks and a road in front of Row-2"></p>
<p>Some of the houses are occupied. The remaining ones are vacant and are the only ones available for sale.</p>
<p>The road adjacency value of a house is the number of its sides adjacent to a road. For example, the road adjacency values of C2, F2, and B1 are 2, 1, and 0, respectively. The neighbour count of a house is the number of sides of that house adjacent to occupied houses in the same block. For example, E1 and C1 can have the maximum possible neighbour counts of 3 and 2, respectively.</p>
<p>The base price of a vacant house is ₹ 10 lakhs if the house does not have a parking space, and ₹ 12 lakhs if it does. The quoted price (in lakhs of ₹) of a vacant house is calculated as (base price) + 5 × (road adjacency value) + 3 × (neighbour count).</p>
<p>The following information is also known.</p>
<ol><li>The maximum quoted price of a house in Block XX is ₹ 24 lakhs. The minimum quoted price of a house in block YY is ₹ 15 lakhs, and one such house is in Column-E.</li>
<li>Row-1 has two occupied houses, one in each block.</li>
<li>Both houses in Column-E are vacant. Each of Column-D and Column-F has at least one occupied house.</li>
<li>There is only one house with parking space in Block YY.</li></ol>
"""
S1_SOL = steps(
 ("Road adjacency of every house", p("A road runs in front of Row-2 and between Column-C and Column-D.") +
   table(["", "A", "B", "C", "", "D", "E", "F"], [["Row-1", "0", "0", "1", "", "1", "0", "0"], ["Row-2", "1", "1", "2", "", "2", "1", "1"]]) +
   p(r"Quoted price \(= \text{base} + 5 \times \text{road} + 3 \times \text{neighbours}\), with base \(10\) or \(12\) (parking).")),
 ("Which Column-E house costs ₹15 lakhs?", p(r"<b>E2</b> (road \(1\)): \(10 + 5 + 3n = 15\) needs \(n = 0\), so D2 and F2 are vacant. Columns D and F then need D1 and F1 occupied: two occupied houses in Row-1 of Block YY, which breaks rule 2. So E2 is not the ₹15 lakh house.") +
   p(r"<b>E1</b> (road \(0\)): \(12 + 0 + 3 \times 1 = 15\). So E1 has <b>parking</b> and exactly one occupied neighbour, which is one of D1 and F1.") +
   p("Since Block YY has only one parking space, it belongs to E1.")),
 ("D1 or F1?", p(r"If D1 were occupied and F1 vacant, Column-F would need F2 occupied. F1 would then cost \(10 + 0 + 3 \times 1 = 13 < 15\), below Block YY’s minimum. So <b>F1 is occupied</b> and D1 is vacant.") +
   p(r"Column-D still needs an occupied house, so <b>D2 is occupied</b>. Check: D1 \(= 10 + 5 + 3 = 18 \ge 15\) ✓. F2 can be either.")),
 ("Block XX: where does ₹24 lakhs come from?", p("Work out every vacant price that is possible in Block XX:") +
   table(["House", "Road", "Max neighbours", "No parking", "Parking"], [
     ["A1", "0", "2", "10, 13, 16", "12, 15, 18"], ["B1", "0", "2", "10, 13, 16", "12, 15, 18"], ["C1", "1", "2", "15, 18, 21", "17, 20, 23"],
     ["A2", "1", "2", "15, 18, 21", "17, 20, 23"], ["B2", "1", "3", "15, 18, 21, <b>24</b>", "17, 20, 23, 26"], ["C2", "2", "1", "20, 23", "22, 25"]], hi={(4, 3)}) +
   p(r"Only <b>B2 without parking, with all \(3\) neighbours occupied</b> gives exactly \(24\). So A2, B1 and C2 are occupied and B2 is vacant.") +
   p("Rule 2 allows only one occupied house in Row-1 of Block XX, and that is B1, so A1 and C1 are vacant. Their prices (16–18 and 21–23) stay below 24 ✓.")),
) + table(["", "A", "B", "C", "", "D", "E", "F"], [
     ["Row-1", "vacant", "<b>occupied</b>", "vacant", "", "vacant", "vacant (parking)", "<b>occupied</b>"],
     ["Row-2", "<b>occupied</b>", "vacant", "<b>occupied</b>", "", "<b>occupied</b>", "vacant", "either"]]) \
  + final("Everything is fixed except F2.")
S1_SHORT = p("Start from the most constrained clue, “₹15 lakhs in Column-E”. Only one house and one configuration produce it, and that settles Block YY. Then list the few ways to reach exactly 24 in Block XX: there’s only one.")
S1_CONCEPT = p(r"Turn a price formula into a short <b>table of possible values</b> per house; “maximum = 24” or “minimum = 15” then usually points to a single cell.")

def s1(qno, q, opts, qtype, ans, diff, sol, short_sol):
    ITEMS.append(dict(section="DILR", qno=qno, set_id=S1, set_title=S1_TITLE, directions=S1_DIR, context=S1_CTX, question=q, options=opts,
                      qtype=qtype, answer=ans, topic=["DILR::LR::Puzzles"], difficulty=diff))
    SOL[qno] = dict(sol, solution=short_sol, setsol=S1_SOL, shortcut=S1_SHORT, concept=S1_CONCEPT)

s1(1, "How many houses are vacant in Block XX?", [], "TITA", "3", "Hard",
   dict(hint=p("The only way to get a quoted price of exactly ₹24 lakhs in Block XX fixes three occupied houses.")),
   steps(("Fix Block XX", p(r"₹24 lakhs is only possible for B2 without parking, with A2, B1 and C2 all occupied.")),
         ("Count", p("Vacant: A1, C1, B2.")))+final(r"\(3\)"))
s1(2, "Which of the following houses is definitely occupied?", ["A1", "B1", "D2", "F2"], "MCQ", "2|3", "Hard",
   dict(hint=p("Settle Block XX from the ₹24 lakh clue and Block YY from the ₹15 lakh clue; more than one house ends up fixed."),
        why=why([("1", "A1 is vacant (Row-1 of Block XX has only B1 occupied)."), ("4", "F2 can be occupied or vacant; nothing fixes it.")])),
   steps(("Block XX", p("The ₹24 lakh house forces <b>B1</b>, A2 and C2 to be occupied.")),
         ("Block YY", p("The ₹15 lakh house is E1 and F1 must be occupied, so Column-D’s occupied house is <b>D2</b>.")),
         ("Note on the options", p("Both B1 (option 2) and D2 (option 3) are definitely occupied, and published solutions treat both as correct. This card accepts either.")))
   + final("Both B1 (option 2) and D2 (option 3) are definitely occupied"))
s1(3, "Which of the following options best describes the number of vacant houses in Row-2?", ["Exactly 3", "Either 3 or 4", "Either 2 or 3", "Exactly 2"], "MCQ", "3", "Medium",
   dict(hint=p("Row-2 has six houses. Only one of them, F2, is not fixed."),
        why=why([("1", "Possible only if F2 is vacant."), ("2", "4 is impossible: at most B2, E2 and F2 can be vacant."), ("4", "Possible only if F2 is occupied.")])),
   steps(("Row-2 status", p("A2 occupied, B2 vacant, C2 occupied, D2 occupied, E2 vacant, F2 either.")),
         ("Count", p(r"\(2\) vacant if F2 is occupied, \(3\) if it is vacant."))) + final("Either 2 or 3 — option 3"))
s1(4, "What is the maximum possible quoted price (in lakhs of ₹) for a vacant house in Column-E?", [], "TITA", "21", "Medium",
   dict(hint=p("E1 is fixed at 15. E2 has no parking; how many occupied neighbours can it have?")),
   steps(("E1", p(r"Fixed at \(15\).")),
         ("E2", p(r"No parking (the only parking space in Block YY is E1), road \(1\). Its neighbours are D2 (occupied), F2 (may be occupied) and E1 (vacant).") +
            r"\[10 + 5 \times 1 + 3 \times 2 = 21\]")) + final(r"\(21\)"))
s1(5, "Which house in Block YY has parking space?", ["F1", "E1", "E2", "F2"], "MCQ", "2", "Medium",
   dict(hint=p("Which house can reach a quoted price of exactly ₹15 lakhs in Column-E?"),
        why=why([("1", "F1 is occupied, and quoted prices apply only to vacant houses."), ("3", "E2 at ₹15 would force two occupied houses in Row-1 of Block YY."), ("4", "Only one parking space exists in Block YY, and E1 needs it.")])),
   steps(("Make 15 with road 0", r"\[12 + 0 + 3 \times 1 = 15 \Rightarrow \text{E1 has parking}\]")) + final("E1 — option 2"))

# ======================= SET 2 =======================
S2 = "2023_S1_DILR_S2"
S2_TITLE = "Set 2 — Electing a Dean"
S2_DIR = "Answer the questions on the basis of the information given below."
S2_CTX = r"""
<p>Faculty members in a management school can belong to one of four departments – Finance and Accounting (F&amp;A), Marketing and Strategy (M&amp;S), Operations and Quants (O&amp;Q) and Behaviour and Human Resources (B&amp;H). The numbers of faculty members in F&amp;A, M&amp;S, O&amp;Q and B&amp;H departments are 9, 7, 5 and 3 respectively.</p>
<p>Prof. Pakrasi, Prof. Qureshi, Prof. Ramaswamy and Prof. Samuel are four members of the school’s faculty who were candidates for the post of the Dean of the school. Only one of the candidates was from O&amp;Q.</p>
<p>Every faculty member, including the four candidates, voted for the post. In each department, all the faculty members who were not candidates voted for the same candidate. The rules for the election are listed below.</p>
<ol><li>There cannot be more than two candidates from a single department.</li><li>A candidate cannot vote for himself/herself.</li><li>Faculty members cannot vote for a candidate from their own department.</li></ol>
<p>After the election, it was observed that Prof. Pakrasi received 3 votes, Prof. Qureshi received 14 votes, Prof. Ramaswamy received 6 votes and Prof. Samuel received 1 vote. Prof. Pakrasi voted for Prof. Ramaswamy, Prof. Qureshi for Prof. Samuel, Prof. Ramaswamy for Prof. Qureshi and Prof. Samuel for Prof. Pakrasi.</p>
"""
S2_SOL = steps(
 ("Separate candidates’ votes from department blocs", p("Each department’s non-candidates vote as one bloc. Take away the four candidates’ own votes:") +
   table(["Candidate", "Total votes", "From candidates", "From blocs"], [
     ["Pakrasi", "3", "1 (Samuel)", "2"], ["Qureshi", "14", "1 (Ramaswamy)", "13"], ["Ramaswamy", "6", "1 (Pakrasi)", "5"], ["Samuel", "1", "1 (Qureshi)", "0"]])),
 ("Match bloc sizes", p(r"A bloc’s size is the department size minus its candidates. O&amp;Q has exactly one candidate, so its bloc is \(4\).") +
   "<ul><li>Pakrasi’s \(2\) can only be <b>B&amp;H</b> with one candidate (\(3 - 1\)).</li><li>Ramaswamy’s \(5\) can only be <b>M&amp;S</b> with two candidates (\(7 - 2\)).</li><li>Qureshi’s \(13 = 9 + 4\): <b>F&amp;A</b> with no candidates, plus O&amp;Q.</li></ul>" +
   p("So the candidates are: M&amp;S 2, O&amp;Q 1, B&amp;H 1, F&amp;A 0.")),
 ("Place the four candidates", "<ul><li>Nobody votes for a candidate from their own department.</li><li>Qureshi can’t be in F&amp;A or O&amp;Q (their blocs voted for him), so he is in M&amp;S or B&amp;H.</li><li>Ramaswamy can’t be in M&amp;S (that bloc voted for him), and Pakrasi can’t be in B&amp;H.</li><li>M&amp;S’s two candidates come from Pakrasi, Qureshi and Samuel. {Pakrasi, Samuel} fails (Samuel voted for Pakrasi) and {Qureshi, Samuel} fails (Qureshi voted for Samuel).</li></ul>" +
   p("So M&amp;S = <b>{Pakrasi, Qureshi}</b>; Ramaswamy and Samuel are split between O&amp;Q and B&amp;H, either way.")),
) + table(["Department", "Size", "Candidates", "Bloc votes for"], [
     ["F&amp;A", "9", "—", "Qureshi (9)"], ["M&amp;S", "7", "Pakrasi, Qureshi", "Ramaswamy (5)"],
     ["O&amp;Q", "5", "Ramaswamy or Samuel", "Qureshi (4)"], ["B&amp;H", "3", "Samuel or Ramaswamy", "Pakrasi (2)"]]) \
  + final("Everything is fixed except which of Ramaswamy and Samuel is in O&amp;Q.")
S2_SHORT = p("Subtract each candidate’s single vote from another candidate first. The remaining totals (2, 5, 13) can only be made from bloc sizes in one way.")
S2_CONCEPT = p("<b>Bloc voting:</b> bloc size = department size − candidates in that department. Matching vote totals to possible bloc sizes is the key step.")

def s2(qno, q, opts, ans, diff, short_sol, why_rows, hint):
    ITEMS.append(dict(section="DILR", qno=qno, set_id=S2, set_title=S2_TITLE, directions=S2_DIR, context=S2_CTX, question=q, options=opts,
                      qtype="MCQ", answer=ans, topic=["DILR::LR::Analytical_Reasoning"], difficulty=diff))
    SOL[qno] = dict(hint=p(hint), solution=short_sol, setsol=S2_SOL, shortcut=S2_SHORT, concept=S2_CONCEPT, why=why(why_rows))

s2(6, "Which two candidates can belong to the same department?", ["Prof. Pakrasi and Prof. Samuel", "Prof. Pakrasi and Prof. Qureshi", "Prof. Qureshi and Prof. Ramaswamy", "Prof. Ramaswamy and Prof. Samuel"], "2", "Medium",
   steps(("Find the two-candidate department", p("M&amp;S has two candidates, and it can only be Pakrasi and Qureshi."))) + final("Pakrasi and Qureshi — option 2"),
   [("1", "Samuel voted for Pakrasi, so they can’t share a department."), ("3", "Ramaswamy can’t be in M&amp;S, Qureshi’s only possible two-candidate department."), ("4", "They are in different departments (O&amp;Q and B&amp;H).")],
   "Ramaswamy gets 5 votes from blocs. Which department has a bloc of exactly 5?")
s2(7, "Which of the following can be the number of votes that Prof. Qureshi received from a single department?", ["7", "8", "6", "9"], "4", "Medium",
   steps(("Qureshi’s votes", p(r"F&amp;A bloc \(9\), O&amp;Q bloc \(4\), Ramaswamy \(1\): total \(14\)."))) + final(r"\(9\) — option 4"),
   [("1", "No department gave him 7."), ("2", "No department gave him 8."), ("3", "No department gave him 6.")],
   "Qureshi’s 13 bloc votes split as two blocs. What sizes are possible?")
s2(8, "If Prof. Samuel belongs to B&amp;H, which of the following statements is/are true?<br>Statement A: Prof. Pakrasi belongs to M&amp;S.<br>Statement B: Prof. Ramaswamy belongs to O&amp;Q.", ["Neither statement A nor statement B", "Both statements A and B", "Only statement B", "Only statement A"], "2", "Easy",
   steps(("Apply the condition", p("Pakrasi is always in M&amp;S (A true). If Samuel is in B&amp;H, Ramaswamy must be the O&amp;Q candidate (B true)."))) + final("Both — option 2"),
   [("1", "Both statements hold."), ("3", "A is also true."), ("4", "B is also true.")],
   "Ramaswamy and Samuel share O&amp;Q and B&amp;H between them.")
s2(9, "What best can be concluded about the candidate from O&amp;Q?", ["It was either Prof. Pakrasi or Prof. Qureshi.", "It was Prof. Ramaswamy.", "It was either Prof. Ramaswamy or Prof. Samuel.", "It was Prof. Samuel."], "3", "Medium",
   steps(("What stays open", p("Both Pakrasi and Qureshi are in M&amp;S; Ramaswamy and Samuel could be swapped between O&amp;Q and B&amp;H."))) + final("Ramaswamy or Samuel — option 3"),
   [("1", "Both are in M&amp;S."), ("2", "Possible, but not certain."), ("4", "Possible, but not certain.")],
   "After placing M&amp;S, which two candidates are left for O&amp;Q and B&amp;H?")
s2(10, "Which of the following statements is/are true?<br>Statement A: Non-candidates from M&amp;S voted for Prof. Qureshi.<br>Statement B: Non-candidates from F&amp;A voted for Prof. Qureshi.", ["Only statement B", "Only statement A", "Both statements A and B", "Neither statement A nor statement B"], "1", "Easy",
   steps(("Check each bloc", p("M&amp;S’s bloc of 5 voted for Ramaswamy, and Qureshi is in M&amp;S anyway (A false). F&amp;A’s bloc of 9 voted for Qureshi (B true)."))) + final("Only B — option 1"),
   [("2", "A is false: M&amp;S non-candidates voted for Ramaswamy."), ("3", "A is false."), ("4", "B is true.")],
   "Which bloc gave Ramaswamy his 5 votes?")

# ======================= SET 4 =======================
S4 = "2023_S1_DILR_S4"
S4_TITLE = "Set 4 — A visa processing office"
S4_DIR = "Answer the questions based on the following information."
S4_CTX = r"""
<p>A visa processing office (VPO) accepts visa applications in four categories – US, UK, Schengen, and Others. The applications are scheduled for processing in twenty 15-minute slots starting at 9:00 am and ending at 2:00 pm. Ten applications are scheduled in each slot.</p>
<p>There are ten counters in the office, four dedicated to US applications, and two each for UK applications, Schengen applications and Others applications. Applicants are called in for processing sequentially on a first-come-first-served basis whenever a counter gets freed for their category. The processing time for an application is the same within each category. But it may vary across the categories. Each US and UK application requires 10 minutes of processing time. Depending on the number of applications in a category and time required to process an application for that category, it is possible that an applicant for a slot may be processed later.</p>
<p>On a particular day, Ira, Vijay and Nandini were scheduled for Schengen visa processing in that order. They had a 9:15 am slot but entered the VPO at 9:20 am. When they entered the office, exactly six out of the ten counters were either processing applications, or had finished processing one and ready to start processing the next.</p>
<p>Mahira and Osman were scheduled in the 9:30 am slot on that day for visa processing in the Others category.</p>
<p>The following additional information is known about that day.</p>
<ol><li>All slots were full.</li><li>The number of US applications was the same in all the slots. The same was true for the other three categories.</li><li>50% of the applications were US applications.</li><li>All applicants except Ira, Vijay and Nandini arrived on time.</li><li>Vijay was called to a counter at 9:25 am.</li></ol>
"""
S4_SOL = steps(
 ("Applications per slot", p(r"\(10\) per slot, half US: <b>US \(5\)</b>. The other \(5\) are UK + Schengen + Others. The 9:15 slot has at least \(3\) Schengen (Ira, Vijay, Nandini) and the 9:30 slot at least \(2\) Others (Mahira, Osman). That uses all \(5\):") +
   table(["Category", "Per slot", "Per day (20 slots)", "Time each"], [["US", "5", "100", "10 min"], ["UK", "0", "0", "10 min"], ["Schengen", "3", "60", "?"], ["Others", "2", "40", "?"]])),
 ("Who was busy at 9:20?", p(r"The \(4\) US counters are always busy, since \(5 \times 10 = 50\) minutes of work arrive every \(15\) minutes. The UK counters are idle (no UK applications). Six busy counters means \(4\) US + \(2\) Schengen, so the two Others counters were idle at 9:20. Others take <b>less than \(5\) minutes</b>, so the 9:15 Others applicants were already done.")),
 ("Schengen time from Vijay’s call", p(r"Let one Schengen application take \(s\) minutes. The 9:00 slot’s three applicants: two start at 9:00 and the third starts at \(9{:}00 + s\) on whichever counter frees first.") +
   p(r"Ira takes the free counter at 9:20. Vijay is called at 9:25, when the third 9:00 applicant finishes: \(9{:}00 + 2s = 9{:}25\), so \(s = 12.5\) minutes. (If \(s\) were \(5\), both counters would be free at 9:20 and Vijay would be called at 9:20.)")),
 ("Timeline", table(["Applicant", "Start", "End"], [["9:00 Schengen ×2", "9:00", "9:12:30"], ["9:00 Schengen #3", "9:12:30", "9:25"], ["Ira", "9:20", "9:32:30"], ["Vijay", "9:25", "9:37:30"],
                                                   ["Nandini", "9:32:30", "<b>9:45</b>"], ["Mahira, Osman (Others)", "9:30", "before 9:35"]])),
 ("US finish time", p(r"Four counters can do \(6\) applications per \(15\) minutes, more than the \(5\) that arrive, so no backlog builds up. In the last slot (1:45 pm), four start at 1:45 and finish at 1:55; the fifth runs 1:55–<b>2:05 pm</b>.")),
) + final("UK = 0 · Schengen 12.5 min each · Others just under 5 min each · US done at 2:05 pm")
S4_SHORT = p("Use “exactly six counters busy at 9:20” and “Vijay called at 9:25” together: the first rules out Others being busy (so Others < 5 min), the second gives the Schengen time.")
S4_CONCEPT = p(r"<b>Queues:</b> with \(c\) counters and service time \(t\), capacity is \(c/t\) per minute. If arrivals stay below capacity, each slot is served independently and only the last slot sets the finishing time.")

def s4(qno, q, opts, qtype, ans, diff, short_sol, hint, why_rows=None):
    ITEMS.append(dict(section="DILR", qno=qno, set_id=S4, set_title=S4_TITLE, directions=S4_DIR, context=S4_CTX, question=q, options=opts,
                      qtype=qtype, answer=ans, topic=["DILR::DI::Caselets"], difficulty=diff))
    SOL[qno] = dict(hint=p(hint), solution=short_sol, setsol=S4_SOL, shortcut=S4_SHORT, concept=S4_CONCEPT, why=why(why_rows) if why_rows else "")

s4(16, "How many UK applications were scheduled on that day?", [], "TITA", "0", "Medium",
   steps(("Fill one slot", p(r"US \(5\) + Schengen \(\ge 3\) + Others \(\ge 2\) \(= 10\) already."))) + final(r"\(0\)"),
   "Half of each slot is US. Who else is known to be in the 9:15 and 9:30 slots?")
s4(17, "What is the maximum possible value of the total time (in minutes, nearest to its integer value) required to process all applications in the Others category on that day?", [], "TITA", "200", "Hard",
   steps(("Bound the Others time", p(r"The Others counters were idle at 9:20, so each Others application takes less than \(5\) minutes.")),
         ("Total", p(r"\(40\) applications \(\times\) just under \(5\) min, i.e. just under \(200\); to the nearest integer, \(200\).")))
   + final(r"\(200\)"), "Why were the Others counters not among the six busy ones at 9:20?")
s4(18, "Which of the following is the closest to the time when Nandini’s application process got over?", ["9:37 am", "9:45 am", "9:50 am", "9:35 am"], "MCQ", "2", "Hard",
   steps(("Schengen time", p(r"\(s = 12.5\) min (from Vijay being called at 9:25).")),
         ("Nandini", p(r"Next free counter after Vijay: Ira’s, at 9:32:30. Nandini finishes at \(9{:}32{:}30 + 12{:}30 = 9{:}45\).")))
   + final("9:45 am — option 2"), "Find the Schengen processing time from “Vijay was called at 9:25”.",
   [("1", "9:37:30 is when Vijay finishes."), ("3", "Too late: Nandini starts at 9:32:30."), ("4", "Too early: that is only 2.5 minutes after she starts.")])
s4(19, "Which of the following statements is false?", ["The application process of Mahira was completed before Nandini’s.", "The application process of Osman was completed before Vijay’s.", "The application process of Mahira started after Nandini’s.", "The application process of Osman was completed before 9:45 am."], "MCQ", "3", "Medium",
   steps(("Times", p("Mahira and Osman start at 9:30 and finish before 9:35. Nandini starts at 9:32:30 and ends at 9:45; Vijay ends at 9:37:30.")),
         ("Check", p("Mahira started at 9:30, <b>before</b> Nandini (9:32:30), so statement 3 is false.")))
   + final("Option 3 is false"), "When did Nandini start, and when did the 9:30 Others applicants start?",
   [("1", "True: Mahira finished before 9:35, Nandini at 9:45."), ("2", "True: Osman finished before 9:35, Vijay at 9:37:30."), ("4", "True: Osman finished before 9:35.")])
s4(20, "When did the application processing for all US applicants get over on that day?", ["2:00 pm", "3:40 pm", "2:05 pm", "2:25 pm"], "MCQ", "3", "Medium",
   steps(("Capacity", p(r"\(4\) counters \(\times\) \(15/10\) \(= 6\) per slot \(> 5\), so no backlog builds up.")),
         ("Last slot", p("1:45 pm slot: four finish at 1:55, the fifth runs 1:55–2:05.")))
   + final("2:05 pm — option 3"), "Can the four US counters keep up with 5 applications every 15 minutes?",
   [("1", "2:00 pm would need all five done in one round, but only four counters exist."), ("2", "Assumes a large backlog, which never builds up."), ("4", "Also assumes a backlog.")])
