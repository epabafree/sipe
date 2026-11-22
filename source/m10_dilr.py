# -*- coding: utf-8 -*-
# Simp Mock 10: DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m10 import P

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Truth tellers and liars (Q1–5) ----------------
ANS = {"Abhimanyu": "AADDCBBB", "Bhaskar": "DCDCCBAB", "Chanchal": "ACDBCABD", "Debesh": "BBBDADCB", "Enakshi": "BCBBBACD"}
AB = {"Abhimanyu": "Ab", "Bhaskar": "Bh", "Chanchal": "Ch", "Debesh": "De", "Enakshi": "En"}
SHEET = table(["Q"] + list(AB.values()), [[str(i + 1)] + [ANS[n][i] for n in ANS] for i in range(8)]) + p("Ab = Abhimanyu, Bh = Bhaskar, Ch = Chanchal, De = Debesh, En = Enakshi.")
KEY = ANS["Chanchal"]
TF = table(["Q", "Key", "Ab", "Bh", "En"], [[str(i + 1), KEY[i]] + ["T" if ANS[n][i] == KEY[i] else "F" for n in ("Abhimanyu", "Bhaskar", "Enakshi")] for i in range(8)])
P.dilr_set(1, "Set 1 — Truth teller, liar and alternators", DIR,
 p("A trainer set a surprise test of 8 multiple-choice questions, each with four options (A, B, C, D) and one correct answer, for five students: Abhimanyu, Bhaskar, Chanchal, Debesh and Enakshi. Four of them knew all the correct answers, but chose to answer in set ways: one as a <b>Truth Teller</b> (every answer correct), one as a <b>Liar</b> (every answer wrong), and two as <b>Alternators</b> (answers alternately correct and wrong, starting either way). They did not reveal who played which role. The fifth student, the <b>Ordinary</b> one, tried honestly but got more than half the answers wrong. Every student answered every question.") +
 p("The options they marked:") + SHEET,
 "DILR::LR::Puzzles",
 steps(("Truth Teller and Liar", p("They must differ on every question. Only two pairs do: Abhimanyu–Enakshi and Chanchal–Debesh.")),
       ("Truth Teller Abhimanyu or Debesh", p("With Abhimanyu’s answers as the key, Bhaskar gets 4 right in no alternating pattern: he fits no role. With Debesh’s, Abhimanyu (2), Bhaskar (1) and Enakshi (3) all fall short of alternating: no Alternator.")),
       ("Truth Teller Enakshi", p("Bhaskar gets 1 right and Debesh 3: two Ordinary students. Rejected.")),
       ("Truth Teller Chanchal", p("Debesh is the Liar. Against Chanchal’s key:") + TF +
        p("Abhimanyu and Enakshi alternate; Bhaskar gets 3 right (Q2, Q3, Q5): Ordinary."))) +
 final("Chanchal is the Truth Teller; key A C D B C A B D."),
 p("Pairs that differ everywhere are the only candidates for Truth Teller and Liar. Test each and check the other roles."),
 p("<b>Role puzzles on answer sheets:</b> assume each candidate key and mark T/F — the pattern of the others decides it quickly."))
P.dq(1, "Who answered every question wrongly?", ["Abhimanyu", "Chanchal", "Debesh", "Enakshi"], "MCQ", "3", "Hard",
 "The Liar is paired with the Truth Teller.",
 steps(("Read", p("Chanchal is the Truth Teller, so Debesh is the Liar."))) + final("Option 3"),
 [("1", "An Alternator."), ("2", "Truth Teller."), ("4", "An Alternator.")])
P.dq(2, "How many questions did the Ordinary student get wrong?", ["5", "6", "7", "8"], "MCQ", "1", "Hard",
 "Bhaskar got 3 right.",
 steps(("Count", p("8 − 3 = 5."))) + final("Option 1"),
 [("2", "Too many."), ("3", "Too many."), ("4", "That is the Liar.")])
P.dq(3, "What are the correct answers to the first four questions, in order?", ["C, C, B, B", "A, C, D, B", "C, B, A, D", "A, B, D, D"], "MCQ", "2", "Hard",
 "Chanchal’s answers.",
 steps(("Read", p("A, C, D, B."))) + final("Option 2"),
 [("1", "Not Chanchal’s."), ("3", "Not Chanchal’s."), ("4", "Abhimanyu’s mixed.")])
P.dq(4, "How many questions were answered correctly by exactly three students?", [], "TITA", "3", "Hard",
 "Chanchal plus one Alternator on every question; add Bhaskar.",
 steps(("Count", p("Chanchal is right everywhere and exactly one Alternator is right on each question. A third correct answer comes from Bhaskar: Q2, Q3, Q5."))) + final("3"))
P.dq(5, "Which list contains only questions answered correctly by exactly two students (the list need not be complete)?", ["1, 4, 8", "1, 5, 8", "2, 7, 8", "1, 3, 6"], "MCQ", "1", "Hard",
 "Exactly two: every question except 2, 3, 5.",
 steps(("Set", p("Exactly two right on Q1, Q4, Q6, Q7, Q8."))) + final("Option 1"),
 [("2", "Q5 has three."), ("3", "Q2 has three."), ("4", "Q3 has three.")])

# ---------------- Set 2: A panipuri stall (Q6–10) ----------------
MARG = ("<ul><li>Ingredient: Maida 200, Atta 215, Rava 125</li><li>Size: Small 180, Medium 220, Large 140</li>"
        "<li>Taste: Meetha 160, Teekha 185, Khatta 195</li><li>Flavour: Jeera 150, Garlic 119, Hing 136, Aamchur 135</li></ul>")
EXTRA = (p("<b>Additional information for this question.</b> On one day the stall sold 540 plates, split by type as follows:") + MARG +
         p("The Aamchur plates were split equally within each of ingredient, size and taste; for example, Maida-Aamchur, Atta-Aamchur and Rava-Aamchur were 45 plates each."))
P.dilr_set(2, "Set 2 — A panipuri stall", DIR,
 p("A panipuri stall classifies each plate on four parameters: size (Small, Medium, Large), taste (Meetha, Teekha, Khatta), flavour (Jeera, Garlic, Hing, Aamchur) and ingredient (Maida, Atta, Rava). Every day it sells at least one plate of every possible combination of the four."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("Combinations", p("3 × 3 × 4 × 3 = 108 combinations; 27 for each flavour.")),
       ("Key idea", p("Every combination takes at least one plate, so to make one group as large as possible, give every other combination exactly one plate."))) +
 final("Reserve one plate per combination, then maximise."),
 p("Count combinations first; the ‘at least one each’ rule is a fixed reserve."),
 p("<b>Max–min with coverage rules:</b> subtract the compulsory minimum from the relevant total, not from the grand total."))
P.dq(6, "On a day when 500 plates were sold, what is the largest possible number of Aamchur plates?", [], "TITA", "419", "Medium",
 "Each other flavour needs at least 27 plates.",
 steps(("Reserve", p("3 × 27 = 81 for the other flavours.")),
       ("Aamchur", p("500 − 81 = 419."))) + final("419"))
P.dq(7, "On one day nobody asked for Aamchur, so the stall sold none, and it sold exactly three plates of every other combination. How many plates did it sell?", [], "TITA", "243", "Medium",
 "Three flavours left.",
 steps(("Count", p("3 × 3 × 3 × 3 = 81 combinations, three plates each: 243."))) + final("243"))
P.dq(8, "On a day the stall sold at least 500 plates, the same number of every combination. What is the least possible total?", ["504", "520", "528", "540"], "MCQ", "4", "Medium",
 "A multiple of 108.",
 steps(("Multiple", p("500 ÷ 108 ≈ 4.6, so 5 each: 540."))) + final("Option 4"),
 [("1", "Not a multiple of 108."), ("2", "Not a multiple of 108."), ("3", "Not a multiple of 108.")])
P.dq(9, EXTRA + p("What is the largest possible number of Jeera-Rava-Large-Khatta plates?"), ["53", "54", "68", "69"], "MCQ", "2", "Medium",
 "Rava is the tightest total.",
 steps(("Rava without Aamchur", p("125 − 45 = 80 plates across 27 combinations (3 sizes × 3 tastes × 3 flavours).")),
       ("Maximum", p("Give the other 26 one plate each: 80 − 26 = 54. Large and Khatta have room to spare."))) + final("Option 2"),
 [("1", "Reserves one too many."), ("3", "Ignores the reserve."), ("4", "Ignores the reserve.")])
P.dq(10, EXTRA + p("What is the largest possible number of Teekha-Garlic plates?"), ["101", "104", "118", "127"], "MCQ", "1", "Medium",
 "Garlic-Meetha and Garlic-Khatta need 9 plates each.",
 steps(("Reserve", p("Each taste has 9 Garlic combinations (3 ingredients × 3 sizes).")),
       ("Maximum", p("119 − 18 = 101. Teekha has room: 101 + 9 + 9 + 45 = 164 ≤ 185."))) + final("Option 1"),
 [("2", "Reserve too small."), ("3", "Reserves one taste only."), ("4", "Exceeds Garlic.")])

# ---------------- Set 3: Names and surnames (Q11–15) ----------------
RANKS = table(["Name", "Surname", "M", "L", "S", "C"], [["Ashok", "Cholagar", "3", "4", "3", "4"], ["Biresh", "Bhalla", "4", "5", "5", "5"],
                                                       ["Chintan", "Ekbote", "1", "2", "1", "2"], ["Deepika", "Ahuja", "2", "1", "2", "3"], ["Eklavya", "Desai", "5", "3", "4", "1"]])
P.dilr_set(3, "Set 3 — Ranks under the wrong names", DIR,
 p("Ashok, Biresh, Chintan, Deepika and Eklavya are the top five students of a class in four subjects: Mathematics, Languages, Science and Civics. In each subject they hold ranks 1 to 5 (1 is best), with no ties. A typist used their surnames instead of first names. The surnames, alphabetically, are Ahuja, Bhalla, Cholagar, Desai and Ekbote. (‘Above’ or ‘better’ means a smaller rank number.)") +
 "<ol><li>Ahuja got rank 3 or better in every subject, and exactly 3 in at least one. Chintan got rank 2 or better in every subject.</li>"
 "<li>Bhalla’s best rank was 4, and only in Mathematics.</li>"
 "<li>Ashok’s best rank was 3, and he ranked better than Biresh in every subject.</li>"
 "<li>Desai ranked 3rd in Languages and Deepika 3rd in Civics; they never had consecutive ranks in any subject.</li>"
 "<li>Desai ranked better than at least three students in Civics.</li>"
 "<li>Eklavya ranked below Deepika in exactly three subjects.</li>"
 "<li>Cholagar ranked below Ahuja in every subject.</li>"
 "<li>Deepika and Cholagar had consecutive ranks in exactly three subjects.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Civics", p("Desai is 1st or 2nd, and not next to Deepika’s 3rd: Desai is 1st. Chintan (2 or better) is 2nd.")),
       ("Ashok", p("Ranks of 3 or worse, beats Biresh everywhere, and cannot be 3rd in Languages (Desai): so not Ahuja, Bhalla or Desai.")),
       ("Bhalla", p("Ranks 5, 5, 5 outside Maths. Not Chintan, Ashok, Desai, Ahuja or Deepika (3rd in Civics). If Eklavya were Bhalla, Biresh would need 4th in Languages, Science and Civics with Ashok 3rd in all three, but 3rd in Languages is Desai’s. So Biresh is Bhalla.")),
       ("Other surnames", p("Desai is not Chintan, Ashok or Deepika: Eklavya. Ahuja needs a 3rd place, which Chintan never has: Deepika. Cholagar ranks below Ahuja everywhere, but Chintan beats Deepika in Civics: Ashok is Cholagar, Chintan is Ekbote.")),
       ("Ranks", p("Languages: Deepika 1, Chintan 2, Desai 3, Ashok 4. Maths: Eklavya 5, and clue 8 puts Deepika 2 next to Ashok 3. Science: clues 6 and 8 give Chintan 1, Deepika 2, Ashok 3, Eklavya 4.") + RANKS)) +
 final("Unique names and ranks."),
 p("Fix the extreme person (Bhalla) first, then use the ‘rank 3’ facts."),
 p("<b>Name–surname matching:</b> statements about one label (surname) and about the other (first name) meet through ranks; fix ranks, then labels."))
P.dq(11, "For how many students can the full name (first name and surname) be found?", [], "TITA", "5", "Hard",
 "Everything is fixed.",
 steps(("Read", p("All five."))) + final("5"))
P.dq(12, "For how many students is the sum of the four ranks a prime number?", [], "TITA", "2", "Hard",
 "Add each row.",
 steps(("Sums", p("Ashok 14, Biresh 19, Chintan 6, Deepika 8, Eklavya 13. Primes: 19 and 13."))) + final("2"))
P.dq(13, "Who has the largest gap between best and worst rank?", ["Ahuja", "Cholagar", "Desai", "Ekbote"], "MCQ", "3", "Hard",
 "Eklavya Desai: 1 to 5.",
 steps(("Gaps", p("Ahuja 2, Cholagar 1, Desai 4, Ekbote 1."))) + final("Option 3"),
 [("1", "Gap 2."), ("2", "Gap 1."), ("4", "Gap 1.")])
P.dq(14, "Who has the same rank in Languages as Cholagar has in Mathematics?", ["Ashok", "Biresh", "Deepika", "Eklavya"], "MCQ", "4", "Hard",
 "Cholagar (Ashok) is 3rd in Maths.",
 steps(("Read", p("3rd in Languages: Eklavya."))) + final("Option 4"),
 [("1", "4th."), ("2", "5th."), ("3", "1st.")])
P.dq(15, "Which full name is correct?", ["Ashok Ahuja", "Biresh Bhalla", "Chintan Cholagar", "Eklavya Ekbote"], "MCQ", "2", "Hard",
 "Read the table.",
 steps(("Read", p("Biresh Bhalla."))) + final("Option 2"),
 [("1", "Ashok Cholagar."), ("3", "Chintan Ekbote."), ("4", "Eklavya Desai.")])

# ---------------- Set 4: A business school’s foreign students (Q16–20) ----------------
NOWE = table(["Region", "Mkt", "Fin", "Undec."], [["Sub-Saharan Africa", "84", "10", "6"], ["Middle East", "36", "38", "24"], ["South-East Asia", "102", "6", "6"]])
FULL = table(["", "Mkt", "Fin", "Und.", "All"], [["SSA", "6+84", "38+10", "6+6", "150"], ["ME", "84+36", "62+38", "6+24", "250"],
                                                ["SEA", "18+102", "68+6", "0+6", "200"]]) + p("Each cell: with experience + without. SSA = Sub-Saharan Africa, ME = Middle East, SEA = South-East Asia.")
P.dilr_set(4, "Set 4 — Specialisations at a business school", DIR,
 p("A business school has 1000 students, 40% of them Indian. The rest are foreign, from Sub-Saharan Africa, the Middle East or South-East Asia. One-fourth of the foreign students are from Sub-Saharan Africa. The Middle East group exceeds the South-East Asia group by one-third of the Sub-Saharan Africa group. Foreign students either have work experience or not.") +
 p("After the first semester each student picks Marketing or Finance, or stays Undecided; the Undecided must pick after the second semester, and nobody changes later. Foreign students <b>without</b> work experience after the first semester:") + NOWE +
 "<ol><li>The ratio of Indian to foreign students is the same among those who chose Marketing, those who chose Finance and the Undecided.</li>"
 "<li>Among Indian students, 148 chose Finance and 32 were Undecided.</li>"
 "<li>Three-fifths of South-East Asian students chose Marketing.</li>"
 "<li>No South-East Asian student with work experience was Undecided.</li>"
 "<li>Half of the Undecided Sub-Saharan African students had no work experience.</li>"
 "<li>Equal numbers of Middle East and South-East Asian students chose Marketing.</li></ol>",
 "DILR::DI::Data_Tabulation",
 steps(("Groups", p("Foreign 600: Sub-Saharan 150, Middle East 250, South-East Asia 200.")),
       ("Foreign totals", p("Indian: Marketing 220, Finance 148, Undecided 32 (400). Foreign is 1.5 times: 330, 222, 48.")),
       ("By region", p("SE Asia: Marketing 120, Undecided 6, Finance 74. Middle East Marketing 120. Sub-Saharan Undecided 12, so Marketing 90 and Finance 48. Middle East: Undecided 30, Finance 100.")),
       ("With + without experience", FULL)) +
 final("Every cell is fixed."),
 p("Start from clue 1: it turns the Indian figures into foreign totals."),
 p("<b>Two-layer tables:</b> fill totals first, then subtract the given layer to get the hidden one."))
P.dq(16, "Which of these is the largest?", ["Share of South-East Asian students who chose Finance", "Share of South-East Asian students with work experience who chose Finance", "Share of Middle East students who chose Marketing", "Share of Sub-Saharan African students with work experience who chose Finance"], "MCQ", "2", "Medium",
 "Work out each share.",
 steps(("Shares", p("74/200 = 37%; 68/86 ≈ 79%; 120/250 = 48%; 38/50 = 76%."))) + final("Option 2"),
 [("1", "37%."), ("3", "48%."), ("4", "76%.")])
P.dq(17, "Among Undecided Middle East students, what is the difference between those with and those without work experience?", [], "TITA", "18", "Medium",
 "30 Undecided, 24 without.",
 steps(("Difference", p("24 − 6 = 18."))) + final("18"))
P.dq(18, r"Of the three foreign groups’ Undecided students, 50% of one group, \(33\tfrac13\%\) of another and \(16\tfrac23\%\) of the third (in some order) later chose Marketing, making 57% of all foreign students Marketing students. What percentage of Sub-Saharan African students ultimately chose Finance?", [r"\(37\tfrac23\)", r"\(35\tfrac13\)", r"\(33\tfrac23\)", r"\(37\tfrac13\)"], "MCQ", "4", "Medium",
 "57% of 600 = 342, so 12 of the 48 Undecided chose Marketing.",
 steps(("Undecided", p("Sub-Saharan 12, Middle East 30, SE Asia 6.")),
       ("Match", p("Only 12 × ⅓ + 30 × ⅙ + 6 × ½ = 4 + 5 + 3 = 12 works.")),
       ("Finance", p("Sub-Saharan Finance: 48 + 8 = 56 of 150 = 37⅓%."))) + final("Option 4"),
 [("1", "Slip."), ("2", "Slip."), ("3", "Slip.")])
P.dq(19, r"Of the three foreign groups’ Undecided students, 50% of one group, \(33\tfrac13\%\) of another and \(16\tfrac23\%\) of the third (in some order) later chose Finance, leaving 60.5% of all foreign students in Marketing. What percentage of Middle East students ultimately chose Finance?", ["44", "45", "48", "50"], "MCQ", "1", "Medium",
 "Finance ends at 39.5% of 600 = 237, so 15 of the Undecided chose Finance.",
 steps(("Match", p("Only 12 × ⅙ + 30 × ⅓ + 6 × ½ = 2 + 10 + 3 = 15 works.")),
       ("Middle East", p("100 + 10 = 110 of 250 = 44%."))) + final("Option 1"),
 [("2", "Slip."), ("3", "Slip."), ("4", "Slip.")])
P.dq(20, "What percentage of all students were Undecided after the first semester?", ["32%", "16%", "8%", "3.2%"], "MCQ", "3", "Medium",
 "32 Indian + 48 foreign.",
 steps(("Percent", p("80 of 1000 = 8%."))) + final("Option 3"),
 [("1", "Indian count as a percent."), ("2", "Doubles."), ("4", "Wrong base.")])
