# -*- coding: utf-8 -*-
# Simp Mock 8: DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m08 import P

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Two blocks of flats (Q1–5) ----------------
FLATS = table(["Fl.", "Block A", "Block B"], [["5", "Sheetal/Sawant", "Girish/Gauri"], ["4", "Gauri/Girish", "Prasad"],
                                              ["3", "Sawant/Sheetal", "Varsha"], ["2", "Shilpa", "Swati"], ["1", "Asma", "Amit"]])
P.dilr_set(1, "Set 1 — Ten flats in two blocks", DIR,
 p("A housing complex has two identical five-storey buildings, Block A and Block B. Floors are numbered 1 to 5 from bottom to top. Each floor has one flat, occupied by one family, so ten families live in the two blocks. The ten owners are Amit, Asma, Gauri, Girish, Prasad, Sawant, Sheetal, Shilpa, Swati and Varsha.") +
 "<ol><li>Exactly two of Sheetal, Shilpa and Swati own flats on the same floor in different blocks.</li>"
 "<li>Girish and Gauri live in different blocks, and only one of them owns a flat on the top floor of their building. Their floor numbers differ by one.</li>"
 "<li>Exactly three owners in Block A have names starting with the same letter. Exactly one of these three owns the top-floor flat.</li>"
 "<li>Prasad and Swati own flats in the same block, with exactly one floor between them.</li>"
 "<li>The difference between Amit’s and Varsha’s floor numbers equals the difference between Sawant’s and Sheetal’s.</li>"
 "<li>Amit and Sawant own flats in different blocks.</li>"
 "<li>Varsha’s floor number is lower than both Gauri’s and Girish’s.</li>"
 "<li>There are exactly two floors where the two owners (one in each block) have names starting with the same letter.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Gauri and Girish", p("By clue 2 one is on floor 5 and the other on floor 4, in different blocks.")),
       ("Block A’s letter", p("Clue 3 needs three names with one letter in Block A. Only S has enough: three of Sawant, Sheetal, Shilpa, Swati. One of them is on top of Block A, so the G on floor 5 is in Block B and the other G is on floor 4 of Block A.")),
       ("Block B", p("Varsha is below both G’s (clue 7) and Prasad and Swati share a block two floors apart. Block A already has a G and three S names, so Block B holds Prasad, Swati, Varsha, Amit and a G. Prasad 4, Swati 2.")),
       ("The rest", p("Clue 1: Shilpa sits opposite Swati on floor 2 of Block A. Clue 8: Asma faces Amit on floor 1. Varsha then takes floor 3. Clue 5: |Amit − Varsha| = 2 = |Sawant − Sheetal|, so they take 3 and 5 in Block A, either way round.")),
       ("All arrangements", FLATS + p("Two independent swaps (the G’s, and Sawant–Sheetal) give 4 arrangements."))) +
 final("Floors 1, 2 fixed in both blocks; two swaps remain."),
 p("Start from the clue that fixes floors absolutely (the top floor), then let letters decide blocks."),
 p("<b>Two-block puzzles:</b> count letters per block early — a ‘three names with one letter’ clue usually fixes who is where."))
P.dq(1, "For how many of the ten owners can the block they live in be determined uniquely?", ["4", "6", "8", "All of them"], "MCQ", "3", "Medium",
 "Only one pair still swaps blocks.",
 steps(("Who swaps", p("Gauri and Girish can be in either block. Sawant and Sheetal swap floors but both stay in Block A.")),
       ("Count", p("10 − 2 = 8."))) + final("Option 3"),
 [("1", "Too few."), ("2", "Counts the floor swap too."), ("4", "Gauri and Girish swap blocks.")])
P.dq(2, "Whose floor number can never be the same as Sheetal’s?", ["Girish", "Gauri", "Varsha", "Swati"], "MCQ", "4", "Medium",
 "Sheetal is on floor 3 or 5.",
 steps(("Check", p("Swati is on floor 2, so never matches. Girish or Gauri can be on 5; Varsha is on 3."))) + final("Option 4"),
 [("1", "Can be on 5."), ("2", "Can be on 5."), ("3", "Floor 3.")])
P.dq(3, "Two owners on the same floor number are called ‘neighbours’. Which pair can be neighbours?", ["Sawant and Varsha", "Sawant and Prasad", "Sawant and Shilpa", "Sawant and Swati"], "MCQ", "1", "Medium",
 "Sawant is on floor 3 or 5.",
 steps(("Check", p("Varsha is on floor 3, so Sawant on 3 makes them neighbours. Prasad is on 4, Shilpa and Swati on 2."))) + final("Option 1"),
 [("2", "Floor 4."), ("3", "Floor 2."), ("4", "Floor 2.")])
P.dq(4, "What is the difference between Amit’s and Girish’s floor numbers?", ["2", "3", "4", "More than one answer is possible"], "MCQ", "4", "Medium",
 "Amit is on floor 1; Girish on 4 or 5.",
 steps(("Difference", p("3 or 4."))) + final("Option 4"),
 [("1", "Never."), ("2", "Only if Girish is on 4."), ("3", "Only if Girish is on 5.")])
P.dq(5, "In how many ways can the ten owners be placed?", ["1", "2", "3", "More than 3"], "MCQ", "4", "Medium",
 "Two independent swaps.",
 steps(("Count", p("2 × 2 = 4."))) + final("Option 4"),
 [("1", "Ignores both swaps."), ("2", "One swap only."), ("3", "Not a product of choices.")])

# ---------------- Set 2: Gold coins of five scholars (Q6–10) ----------------
SUMS = table(["No.", "Sum of three", "No.", "Sum of three"], [["1", "101", "6", "—"], ["2", "99", "7", "—"], ["3", "—", "8", "84"], ["4", "—", "9", "82"], ["5", "—", "10", "77"]])
P.dilr_set(2, "Set 2 — Gold coins taken three at a time", DIR,
 p("Five scholars of a royal court — Amarsimha, Dhanvantari, Kshapanaka, Shanku and Varuchi — have some gold coins each. Their numbers of coins are in strictly decreasing order in the order of the names given. Each has at least 20 and at most 40 coins.") +
 p("The ten sums of their coins, taken three at a time, are listed in decreasing order. Some entries are missing:") + SUMS,
 "DILR::LR::Mathematical_Reasoning",
 steps(("Name them", p("Let the coins be a > b > c > d > e (Amarsimha to Varuchi).")),
       ("The four ends", p("The largest sum is a + b + c = 101 and the smallest c + d + e = 77. Second largest is a + b + d = 99; second smallest b + d + e = 82.")),
       ("Differences", p("c − d = 2 and b − c = 5. Then a = 96 − 2c and e = 79 − 2c.")),
       ("Limits", p("a ≤ 40 gives c ≥ 28; e ≥ 20 gives c ≤ 29.")),
       ("Two cases", table(["c", "a", "b", "c", "d", "e"], [["28", "40", "33", "28", "26", "23"], ["29", "38", "34", "29", "27", "21"]]) +
        p("Both give 84 as entry 8 (b + c + e). Entry 7 is 87 in the first case and 86 in the second."))) +
 final("Two possible sets of coins."),
 p("Write everyone in terms of the middle value, then bound it from both ends."),
 p("<b>Sums of k at a time:</b> the largest and second-largest sums differ only in the smallest swapped element, which gives differences directly."))
P.dq(6, "Of the numbers 27, 29 and 31, how many can be Kshapanaka’s number of coins?", ["0", "1", "2", "3"], "MCQ", "2", "Hard",
 "Kshapanaka is c.",
 steps(("c", p("c is 28 or 29. Only 29 is in the list."))) + final("Option 2"),
 [("1", "29 works."), ("3", "27 and 31 do not."), ("4", "Too many.")])
P.dq(7, "If Shanku has 27 coins, how many does Dhanvantari have?", ["35", "34", "33", "Shanku cannot have 27 coins"], "MCQ", "2", "Medium",
 "d = 27 is the second case.",
 steps(("Read", p("d = 27 gives c = 29 and b = 34."))) + final("Option 2"),
 [("1", "Off by one."), ("3", "First case’s b."), ("4", "It is possible.")])
P.dq(8, "What is entry 7 in the table?", ["88", "87", "86", "More than one value is possible"], "MCQ", "4", "Hard",
 "Two cases remain.",
 steps(("Each case", p("First case: 87 (b + c + d = 33 + 28 + 26). Second case: 86 (a + d + e = 38 + 27 + 21).")),
       ("Answer", p("Not unique."))) + final("Option 4"),
 [("1", "Entry 6 in the second case."), ("2", "First case only."), ("3", "Second case only.")])
P.dq(9, "For how many of the five scholars can the number of coins be determined uniquely?", [], "TITA", "0", "Hard",
 "Compare the two cases.",
 steps(("Compare", p("Every value differs between the two cases."))) + final("0"))
P.dq(10, "Of the 10 pairs of scholars, in how many can the richer one give some coins to the other so that they end up equal? (Enter 11 if this cannot be determined.)", [], "TITA", "4", "Hard",
 "Equal after a transfer means an even difference.",
 steps(("Parity", p("A pair works when both numbers have the same parity.")),
       ("Case 1", p("40, 28, 26 even (3 pairs); 33, 23 odd (1 pair): 4.")),
       ("Case 2", p("38, 34 even (1 pair); 29, 27, 21 odd (3 pairs): 4."))) + final("4"))

# ---------------- Set 3: A football round-robin (Q11–15) ----------------
FOOT = table(["Team", "Scored", "Conceded", "Points"], [["A", "", "", ""], ["B", "7", "6", "5"], ["C", "4", "", ""], ["D", "4", "2", "6"], ["E", "4", "8", ""]])
RES = table(["Match", "Score", "Match", "Score"], [["A–B", "2–2", "B–D", "0–1"], ["A–C", "3–0", "B–E", "2–1"], ["A–D", "1–0", "C–D", "0–1"],
                                                  ["A–E", "2–1", "C–E", "2–1"], ["B–C", "3–2", "D–E", "2–1"]])
P.dilr_set(3, "Set 3 — A five-team football tournament", DIR,
 p("Five teams, A, B, C, D and E, play a football tournament in which each team plays every other team exactly once. A win earns 2 points, a draw 1 point to each team, and a loss 0. The table gives part of each team’s total goals scored, goals conceded and points.") + FOOT +
 "<ol type='a'><li>No team won all its matches. No match ended 0–0.</li><li>No team scored more than 3 goals in a match.</li><li>Exactly one match was drawn.</li>"
 "<li>Team A earned more points than every other team.</li><li>In every match the two teams’ goals differed by at most 2, except in the match between A and C.</li><li>Team E scored in every match.</li></ol>",
 "DILR::LR::Games_and_Tournaments",
 steps(("A versus C", p("A goal difference of 3 or more with at most 3 goals a side means 3–0. C cannot win 3–0 and still have A top, so A won 3–0.")),
       ("Results", p("D’s 6 points with one draw in the whole event: 3 wins and 1 loss. Team E’s 4 for, 8 against with goals in every match and the difference rule: E lost every match 1–2, so 0 points. B’s 5 points: 2 wins, a draw and a loss. A must top 6, so A has 7: 3 wins and the draw, which is A–B. D’s loss is to A.")),
       ("Goals", p("D conceded 2: 1 to E, so A beat D 1–0 and D kept clean sheets against B and C. A–B is then 2–2 by B’s and the table’s totals, B beat C 3–2, D beat B 1–0 and C 1–0.")),
       ("All ten matches", RES)) +
 final("A unique set of results."),
 p("Fix the extreme match first (the only one with a big margin), then let points totals fix wins and losses."),
 p("<b>Round robins:</b> with 2 points a win, an even total with no draws pins the number of wins exactly."))
P.dq(11, "How many goals in total were scored in the match between B and C?", [], "TITA", "5", "Hard",
 "Use B’s and C’s goal totals.",
 steps(("Score", p("B 3–2 C."))) + final("5"))
P.dq(12, "In how many matches did one of the two teams fail to score?", [], "TITA", "4", "Hard",
 "Look for a 0 in the results.",
 steps(("Count", p("A–C 3–0, A–D 1–0, B–D 0–1, C–D 0–1: 4."))) + final("4"))
P.dq(13, "How many points did team C earn?", [], "TITA", "2", "Medium",
 "C won only against E.",
 steps(("Count", p("One win, 2 points."))) + final("2"))
P.dq(14, "How many goals did team D score against team C?", [], "TITA", "1", "Medium",
 "D 1–0 C.",
 steps(("Read", p("1."))) + final("1"))
P.dq(15, "In how many matches did the two teams’ goals differ by exactly 1?", [], "TITA", "8", "Medium",
 "All but two matches.",
 steps(("Count", p("All matches except A–B (draw) and A–C (3–0): 8."))) + final("8"))

# ---------------- Set 4: Two schools, two boards (Q16–20) ----------------
SCH = table(["", "Sch. P", "Sch. Q"], [["C-Pri", "b", "3840−a−2b"], ["C-Sec", "b+80", "a+80"],
                                          ["I-Pri", "a", "b"], ["I-Sec", "3920−a−2b", "4080+b"]])
P.dilr_set(4, "Set 4 — Two schools and two boards", DIR,
 p("Two schools, School P and School Q, together have 12,000 students in 2023–24. Each school offers two boards, CBSE and ICSE, and each board has a Primary and a Secondary section in each school.") +
 "<ul><li>The CBSE students in the two schools together are half as many as the ICSE students.</li>"
 "<li>School P has half as many students as School Q.</li>"
 "<li>School P’s Primary students (both boards) equal the ICSE Primary students of both schools together.</li>"
 "<li>School P’s CBSE Secondary students are 80 more than School Q’s ICSE Primary students.</li>"
 "<li>Overall, Secondary students outnumber Primary students by 4320.</li></ul>",
 "DILR::DI::Caselets",
 steps(("Totals", p("CBSE 4000, ICSE 8000. School P 4000, School Q 8000. Primary 3840, Secondary 8160.")),
       ("Two unknowns", p("Let a = School P ICSE Primary and b = School Q ICSE Primary. School P’s Primary = a + b, so School P CBSE Primary = b; School P CBSE Secondary = b + 80.")),
       ("The table", SCH + p("C = CBSE, I = ICSE, Pri = Primary, Sec = Secondary. Each remaining cell follows from one of the totals."))) +
 final("Everything in terms of a and b."),
 p("Turn every statement into a total, then express the cells in two unknowns."),
 p("<b>Two-way tables:</b> with row and column totals known, two free cells usually fix the rest."))
P.dq(16, "What is the difference between School P’s ICSE Primary students and School Q’s CBSE Secondary students?", ["60", "80", "120", "Cannot be determined"], "MCQ", "2", "Medium",
 "a and a + 80.",
 steps(("Difference", p("(a + 80) − a = 80."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "a cancels.")])
P.dq(17, "What is the difference between School Q’s CBSE Primary students and School P’s ICSE Secondary students?", ["80", "100", "120", "Cannot be determined"], "MCQ", "1", "Medium",
 "Both are something − a − 2b.",
 steps(("Difference", p("(3920 − a − 2b) − (3840 − a − 2b) = 80."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "a and b cancel.")])
P.dq(18, "If the ICSE Primary students of both schools together number 3300, how many Secondary students does School P have?", ["550", "600", "660", "700"], "MCQ", "4", "Medium",
 "a + b = 3300.",
 steps(("Add", p("(b + 80) + (3920 − a − 2b) = 4000 − (a + b) = 700."))) + final("Option 4"),
 [("1", "Not from the table."), ("2", "Not from the table."), ("3", "Not from the table.")])
P.dq(19, "If the ICSE Primary students of both schools together number 3300, how many Primary students does School Q have?", ["550", "555", "540", "545"], "MCQ", "3", "Medium",
 "a + b = 3300.",
 steps(("Add", p("(3840 − a − 2b) + b = 3840 − (a + b) = 540."))) + final("Option 3"),
 [("1", "Off by 10."), ("2", "Off by 15."), ("4", "Off by 5.")])
P.dq(20, "What is the largest possible number of ICSE Secondary students in School Q?", ["4080", "4160", "5480", "6000"], "MCQ", "4", "Medium",
 "Maximise b while every cell stays at least 0.",
 steps(("Limits", p("3840 − a − 2b ≥ 0 and 3920 − a − 2b ≥ 0. With a = 0, b ≤ 1920.")),
       ("Maximum", p("4080 + 1920 = 6000."))) + final("Option 4"),
 [("1", "b = 0."), ("2", "b = 80."), ("3", "Not the limit.")])
