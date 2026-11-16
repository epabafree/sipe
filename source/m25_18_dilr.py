# -*- coding: utf-8 -*-
# Simp Mock 18 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_18 import P
import m25_18_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Workshop ages (Q1–4) ----------------
COUNT = table(["Department", "A", "B", "C", "D"], [["Participants", "4", "3", "6", "2"]])
FINAL = table(["Dept", "Ages"], [["A", "27, 28, 33, 41"], ["B", "32, 33, 35"], ["C", "24, 25, 26, 27, 33, 38"], ["D", "30, 33"]])
P.dilr_set(1, "Set 1 — Ages at a bank workshop", DIR,
 p("A mid-sized bank held a workshop on new banking regulations for employees from four departments, A, B, C and D. The chart gives the youngest and oldest participant’s age in each department, and the table gives the number of participants.") + F.AGES + COUNT +
 p("Every age is a whole number of years, and no two participants from the same department share an age. The average age of all participants is a whole number, and it is the smallest it could possibly be."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Least total", p("Taking the smallest ages each department allows: A 27 + 28 + 29 + 41 = 125, B 32 + 33 + 35 = 100, C 24 + 25 + 26 + 27 + 28 + 38 = 168, D 30 + 33 = 63. Total 456 for 15 people.")),
       ("Average", p("The next multiple of 15 is 465: average 31, so 9 years must be added above the minimum.")),
       ("Common age", p("At most one person per department can share an age. D’s two people are 30 and 33, and 33 lies in every range, so four people can share the age 33.")),
       ("With four aged 33", p("Known: A 27, 33, 41; B 32, 33, 35; C 24, 33, 38; D 30, 33: 359 in all. The other four ages (one in A, three in C) add to 465 − 359 = 106, which is their least possible sum 28 + 25 + 26 + 27.") + FINAL)) +
 final("Average 31; with four people aged 33, every age is fixed."),
 p("Start from the least possible total; the average must round it up to a multiple of 15."),
 p("<b>Minimum sums:</b> distinct whole numbers in a range are smallest when packed at the bottom."))
P.dq(1, "What is the average age (in years) of all the participants?", [], "TITA", "31", "Medium",
 "Least total 456; next multiple of 15.", steps(("Average", p("465 ÷ 15 = 31."))) + final("31"))
P.dq(2, "At most how many participants can share the same age?", [], "TITA", "4", "Easy",
 "One per department, in an age every range allows.", steps(("Age 33", p("33 lies in all four ranges (it is D’s oldest): 4 people."))) + final("4"))
P.dq(3, "Suppose as many participants as possible share one age. Counting whole-number ages strictly between department A’s youngest and oldest, how many can no participant from A have?", ["12", "11", "10", "Fewer than 10"], "MCQ", "2", "Hard",
 "A’s ages become 27, 28, 33, 41.",
 steps(("Possible", p("28 and 33 are taken by A’s middle two.")), ("Excluded", p("28 to 40 is 13 values; minus 28 and 33 leaves 11."))) + final("Option 2"),
 [("1", "Counts 33 as excluded."), ("3", "Arithmetic slip."), ("4", "Too few.")])
P.dq(4, "Suppose as many participants as possible share one age. For how many participants can the age be determined uniquely?", ["15", "14", "13", "Fewer than 13"], "MCQ", "1", "Medium",
 "The leftover 106 years split one way only.", steps(("All", p("A’s fourth is 28 and C’s three are 25, 26, 27: all 15 fixed."))) + final("Option 1"),
 [("2", "None is open."), ("3", "None is open."), ("4", "None is open.")])

# ---------------- Set 2: A train across time zones (Q5–9) ----------------
UP = table(["City", "Arr", "Dep"], [["Novak", "—", "5:00 AM"], ["Dubrovnik", "7:55 AM", "8:05 AM"], ["Zagreb", "11:50 AM", "12:05 PM"], ["Osijek", "1:15 PM", "1:20 PM"], ["Motsar", "3:20 PM", "3:25 PM"], ["Presov", "6:57 PM", "—"]])
DOWN = table(["City", "Arr", "Dep"], [["Presov", "—", "7:00 AM"], ["Motsar", "3:12 PM", "3:27 PM"], ["Osijek", "5:27 PM", "5:32 PM"], ["Zagreb", "10:42 PM", "10:47 PM"], ["Dubrovnik", "5:32 AM", "5:42 AM"], ["Novak", "12:07 PM", "—"]])
LEGS = table(["Leg", "Real", "Gap"], [["Nov–Dub", "4:40", "1:45"], ["Dub–Zag", "5:15", "1:30"], ["Zag–Osi", "3:10", "2:00"], ["Osi–Mot", "2:00", "0"], ["Mot–Pre", "5:52", "2:20"]])
P.dilr_set(2, "Set 2 — One railway, five time zones", DIR,
 p("The landlocked country of Taured is roughly a rectangle stretched east to west and has five time zones. Its six main cities, Dubrovnik, Motsar, Novak, Osijek, Presov and Zagreb, are linked by one railway line. The up train leaves Novak at 5:00 AM and ends at Presov; the down train leaves Presov at 7:00 AM and ends at Novak. The train runs at the same constant speed in both directions. All times below are local times.") +
 p("<b>Up train</b>") + UP + p("<b>Down train</b>") + DOWN,
 "DILR::DI::Data_Tabulation",
 steps(("Undo the clocks", p("On any leg, the up and down local times differ from the real time by the same zone gap in opposite directions. So real time = (up + down) ÷ 2, and the gap = half the difference.")),
       ("Legs", LEGS),
       ("Map", p("East to west: Novak, Dubrovnik, Zagreb, then Osijek and Motsar (same zone), then Presov. Novak’s clock is 7 h 35 ahead of Presov’s."))) +
 final("Real journey: 20 h 57 running plus 35 min of stops = 21 h 32."),
 p("Add the up and down times for each leg: the time-zone shifts cancel."),
 p("<b>Round trips across zones:</b> averaging the two directions removes the clock difference."))
P.dq(5, "When the up train leaves Novak, what is the local time in Presov?", ["2:35 PM", "9:25 PM", "10:35 PM", "2:35 AM"], "MCQ", "2", "Medium",
 "Novak is 7 h 35 ahead.", steps(("Time", p("5:00 AM − 7 h 35 = 9:25 PM the previous day."))) + final("Option 2"),
 [("1", "Adds instead."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(6, "How long does the train take from one end of the line to the other?", ["20 hours 57 minutes", "24 hours 12 minutes", "21 hours 32 minutes", "29 hours 7 minutes"], "MCQ", "3", "Medium",
 "Running time plus stops.", steps(("Total", p("4:40 + 5:15 + 3:10 + 2:00 + 5:52 = 20:57, plus stops 10 + 15 + 5 + 5 = 35 min: 21 h 32."))) + final("Option 3"),
 [("1", "Leaves out the stops."), ("2", "Local times."), ("4", "Local times.")])
P.dq(7, "The government merges the country into two time zones: Novak, Dubrovnik and Zagreb use Dubrovnik’s present time, and the other three cities use Presov’s present time. If the up train leaves Novak at 5:00 AM by the new time there, when does it reach Presov by Presov’s new time?", ["7:47 PM", "8:12 PM", "8:42 PM", "There will be no change"], "MCQ", "3", "Hard",
 "The two new zones differ by 5 h 50.",
 steps(("Arrival", p("5:00 AM + 21 h 32 = 2:32 AM in Dubrovnik time; Presov is 1:30 + 2:00 + 2:20 = 5 h 50 behind: 8:42 PM."))) + final("Option 3"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "The clocks shift.")])
P.dq(8, "With the same two new time zones, if the down train leaves Presov at 7:00 AM by the new time, when does it reach Zagreb by Zagreb’s new time?", ["10:22 PM the same day", "10:57 PM the same day", "11:52 PM the same day", "12:12 AM the next day"], "MCQ", "4", "Hard",
 "Presov to Zagreb, then add 5 h 50.",
 steps(("Travel", p("5:52 + 15 min at Motsar + 2:00 + 5 min at Osijek + 3:10 = 11 h 22: 6:22 PM in Presov time.")), ("Zagreb", p("+ 5 h 50 = 12:12 AM the next day."))) + final("Option 4"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])
P.dq(9, "The train’s average speed from Novak to Zagreb was 60 km/h, and from Zagreb to Presov 80 km/h, both counting stops at stations in between. Leaving out all stops at intermediate stations, what is its average speed over the whole journey (km/h)?", ["Less than 70", "More than 70 but less than 71", "More than 71 but less than 72", "More than 72"], "MCQ", "3", "Hard",
 "Use the up train’s real times, stops included in each half.",
 steps(("Distances", p("Novak–Zagreb: 10 h 05 × 60 = 605 km. Zagreb–Presov: 11 h 12 × 80 = 896 km.")), ("Speed", p("1501 km ÷ 20 h 57 ≈ 71.6 km/h."))) + final("Option 3"),
 [("1", "Too low."), ("2", "Includes the stops."), ("4", "Too high.")])

# ---------------- Set 3: A coded subtraction (Q10–13) ----------------
SUM = ("<table class=\"tbl\"><tr><td></td><td>C</td><td>K</td><td>F</td><td>H</td><td>H</td><td>I</td><td>C</td></tr>"
       "<tr><td>−</td><td></td><td>C</td><td>B</td><td>K</td><td>G</td><td>G</td><td>A</td></tr>"
       "<tr><td></td><td>C</td><td>E</td><td>I</td><td>C</td><td>H</td><td>K</td><td>A</td></tr></table>")
P.dilr_set(3, "Set 3 — A coded subtraction", DIR,
 p("A six-digit number (second row) is subtracted from a seven-digit number (first row), giving the third row. Each letter stands for a different digit; the ten digits 0–9 are coded by the letters A, B, C, D, E, F, G, H, I and K. C is less than A, and A is not odd.") + SUM,
 "DILR::LR::Mathematical_Reasoning",
 steps(("Hundreds", p("H − G gives H (with or without borrows) only if G = 0 or 9; G = 9 would make I = K in the tens. So G = 0.")),
       ("Units and tens", p("C − A ends in A with a borrow, so C + 10 = 2A: A even and C < A gives (A, C) = (6, 2) or (8, 6). The tens give I = K + 1; (8, 6) clashes, so A = 6, C = 2.")),
       ("Thousands", p("H = K + 2, so K, I, H are consecutive: 7, 8, 9 (3, 4, 5 leaves no fit higher up).")),
       ("Top", p("E = 4, and F, B from 1, 3, 5 with 10 + F − B = 8: (F, B) = (1, 3) or (3, 5)."))) +
 final("2719982 − 237006 or 2739982 − 257006; both give 2482976."),
 p("Start with the column whose top and bottom digits match the answer: it pins down a 0 or 9."),
 p("<b>Cryptarithms:</b> a column like H − G = H forces G = 0 (or 9 with borrows)."))
P.dq(10, "Which digit does H stand for?", [], "TITA", "9", "Medium", "K, I, H are 7, 8, 9.", steps(("H", p("9."))) + final("9"))
P.dq(11, "Which digit does G stand for?", [], "TITA", "0", "Easy", "Hundreds column.", steps(("G", p("0."))) + final("0"))
P.dq(12, "What is B − F?", ["2", "4", "6", "Cannot be determined"], "MCQ", "1", "Medium",
 "10 + F − B = 8.", steps(("Both cases", p("(F, B) = (1, 3) or (3, 5): B − F = 2 either way."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Same in both cases.")])
P.dq(13, "What is the difference (the seven-digit result)?", ["2570076", "2482976", "2379982", "2482996"], "MCQ", "2", "Easy",
 "CEICHKA.", steps(("Result", p("2 4 8 2 9 7 6."))) + final("Option 2"),
 [("1", "Not consistent."), ("3", "Not consistent."), ("4", "Tens digit wrong.")])

# ---------------- Set 4: Swapping sweets (Q14–17) ----------------
P.dilr_set(4, "Set 4 — Swapping sweets", DIR,
 p("A grandmother gives each of her seven grandchildren, Ana, Esha, Nikhil, Shreya, Tanmay, Jai and Jasmin, a pouch with one toffee (worth ₹5) and one chocolate bar (worth ₹20). The grandchildren then swap sweets, each giving away only sweets received from the grandmother.") +
 "<ul><li>Every child gave away both of the sweets they got from the grandmother.</li><li>Ana ended up with sweets worth ₹80.</li>"
 "<li>Esha, Nikhil and Shreya each received 2 sweets, of different total worths, and none of them swapped with each other.</li><li>Tanmay received sweets of the same total worth as Shreya.</li>"
 "<li>Every child was left with at least one sweet.</li><li>Nikhil received a toffee from Tanmay, but Tanmay received nothing from Nikhil.</li>"
 "<li>Jai received exactly one sweet, from someone to whom Jai had also given a sweet.</li></ul>",
 "DILR::LR::Puzzles",
 steps(("Esha, Nikhil, Shreya", p("Two sweets each with different worths: 2 toffees (₹10), toffee + bar (₹25), 2 bars (₹40). Together: 3 toffees, 3 bars.")),
       ("Ana", p("₹80 is 4 bars (3 bars and 4 toffees would leave Tanmay, Jai and Jasmin one bar between three). So Ana has 4 bars, and the 4 remaining toffees go to Tanmay, Jai and Jasmin.")),
       ("Pairs", p("Tanmay matches Shreya: both have 2 toffees (₹10). Jai and Jasmin get 1 toffee each. Nikhil’s toffee from Tanmay makes Nikhil toffee + bar; Esha has 2 bars."))) +
 final("Ana 4 bars, Esha 2 bars, Nikhil 1 + 1, Shreya and Tanmay 2 toffees, Jai and Jasmin 1 toffee."),
 p("Count worths: three children with two sweets each and different totals use up three toffees and three bars."),
 p("<b>Counting by type:</b> fix how many of each kind every child ends with before tracing who gave what."))
P.dq(14, "How many sweets did Jai end up with?", ["1", "2", "3", "None of these"], "MCQ", "1", "Easy",
 "Received exactly one.", steps(("Jai", p("1 toffee."))) + final("Option 1"),
 [("2", "Tanmay’s count."), ("3", "Too many."), ("4", "1 is listed.")])
P.dq(15, "Who ended up with one toffee and one chocolate bar?", ["Esha", "Nikhil", "Shreya", "None of these"], "MCQ", "2", "Easy",
 "Nikhil got a toffee from Tanmay.", steps(("Nikhil", p("Toffee + bar (₹25)."))) + final("Option 2"),
 [("1", "Two bars."), ("3", "Two toffees."), ("4", "Nikhil fits.")])
P.dq(16, "Which of the following is definitely incorrect?", ["Shreya received a sweet from Jasmin.", "Ana received a sweet from Tanmay.", "Nikhil received a sweet from Esha.", "Esha received a sweet from Ana."], "MCQ", "3", "Easy",
 "Esha, Nikhil and Shreya didn’t swap with each other.",
 steps(("Check", p("Option 3 breaks that rule. Jasmin’s toffee can go to Shreya, Tanmay’s bar to Ana, Ana’s bar to Esha."))) + final("Option 3"),
 [("1", "Possible."), ("2", "Possible."), ("4", "Possible.")])
P.dq(17, "Who had at least one chocolate bar after the swaps?", ["Shreya", "Esha", "Jai", "Tanmay"], "MCQ", "2", "Easy",
 "Esha has two bars.", steps(("Esha", p("2 bars."))) + final("Option 2"),
 [("1", "Two toffees."), ("3", "One toffee."), ("4", "Two toffees.")])

# ---------------- Set 5: A talent contest (Q18–22) ----------------
TEAMS = ("<ol><li>Ravi (piano), Diya (vocals), Ajay (guitar)</li><li>Amit, Chahel, Vishnu (roles open)</li><li>Arun (piano), Zubin (vocals), Badri (guitar)</li>"
         "<li>Jeet (piano), Neha (vocals), Ekansh (guitar)</li><li>Vishal (piano), Shivani (vocals), Dhruv (guitar)</li></ol>")
P.dilr_set(5, "Set 5 — Five trios on a talent show", DIR,
 p("Five teams reach the final of a televised talent contest. Each team has a vocalist, a pianist and a guitarist, and each team performs once, one after another. The judges give six awards: best vocalist, best pianist, best guitarist, and one award to each of the three members of the best team. Six different people won awards. Of the fifteen finalists, only three are women, Diya, Neha and Shivani, and all three are vocalists.") +
 "<ul><li>Brothers Arun and Ajay were in different teams, which did not perform one after the other.</li><li>Vishnu and Chahel were in a team that performed after Ajay’s team.</li>"
 "<li>Amit’s team won the best-team award and did not perform first.</li><li>Zubin and Neha, the two vocalists not in a team with Ajay, won nothing, but exactly one member of each of their teams won an award.</li>"
 "<li>The fifth team was Dhruv, Shivani and Vishal; Dhruv hoped for best guitarist, but none of the three won anything.</li>"
 "<li>Jeet won best pianist. Ravi was the pianist accompanying the winner of best vocalist.</li><li>The vocalist in Ekansh’s team was a woman, and his team performed after Badri’s.</li>"
 "<li>Badri won best guitarist, and his team did not perform first.</li></ul>",
 "DILR::LR::Puzzles",
 steps(("Winners", p("Zubin, Neha and Shivani won nothing, and the best vocalist isn’t in the best team (six different winners), so Diya won best vocalist, with Ravi on piano.")),
       ("Teams", p("Zubin and Neha sit with Badri and Jeet. Vishnu and Chahel can’t be with Badri, Jeet or Ekansh, so they are with Amit. That leaves Arun with Zubin and Badri, Jeet with Neha and Ekansh, and Ravi with Diya and Ajay.")),
       ("Order", p("Ajay’s team before Amit’s, Badri’s before Ekansh’s, neither Amit’s nor Badri’s first, Arun’s and Ajay’s not adjacent: 1 Ajay’s, 2 Amit’s, 3 Badri’s, 4 Jeet’s.") + TEAMS)) +
 final("Only the roles inside Amit’s team are open."),
 p("Start from who could have won best vocalist."),
 p("<b>Award counting:</b> six distinct winners means no individual award goes to the best team."))
P.dq(18, "For how many of the fifteen competitors can the role (vocalist, pianist or guitarist) be determined for certain?", [], "TITA", "12", "Medium",
 "All but Amit’s team.", steps(("Count", p("15 − 3 = 12."))) + final("12"))
P.dq(19, "How many of the award winners can be identified?", [], "TITA", "6", "Medium",
 "Diya, Jeet, Badri and Amit’s trio.", steps(("Winners", p("All six: Diya, Jeet, Badri, Amit, Chahel, Vishnu."))) + final("6"))
P.dq(20, "If all the pianists’ names start with different letters, and so do all the guitarists’ names, what were the roles in the best team?", ["Amit – pianist, Vishnu – vocalist, Chahel – guitarist", "Amit – pianist, Vishnu – guitarist, Chahel – vocalist", "Amit – vocalist, Vishnu – pianist, Chahel – guitarist", "Amit – vocalist, Vishnu – guitarist, Chahel – pianist"], "MCQ", "4", "Medium",
 "Pianists already: Ravi, Arun, Jeet, Vishal. Guitarists: Ajay, Badri, Ekansh, Dhruv.",
 steps(("Pianist", p("Not Amit (Arun) or Vishnu (Vishal): Chahel.")), ("Guitarist", p("Not Amit (Ajay): Vishnu. Amit sings."))) + final("Option 4"),
 [("1", "Amit clashes with Arun."), ("2", "Amit clashes with Arun."), ("3", "Vishnu clashes with Vishal.")])
P.dq(21, "Who was the pianist in Badri’s team?", ["Ajay", "Jeet", "Arun", "Either Jeet or Arun"], "MCQ", "3", "Easy",
 "Badri, Zubin and Arun.", steps(("Pianist", p("Arun."))) + final("Option 3"),
 [("1", "Ajay is a guitarist."), ("2", "Jeet is in Ekansh’s team."), ("4", "Fixed.")])
P.dq(22, "Which two competitors were in the same team?", ["Ajay and Diya", "Arun and Diya", "Diya and Ekansh", "Arun and Jeet"], "MCQ", "1", "Easy",
 "Ravi, Diya and Ajay.", steps(("Team 1", p("Ajay and Diya."))) + final("Option 1"),
 [("2", "Different teams."), ("3", "Different teams."), ("4", "Different teams.")])
