# -*- coding: utf-8 -*-
# Simp Mock 3 (2025): DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m25_03 import P

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Bullet trains (Q1–5) ----------------
SCH = p("<b>Blue</b>") + table(["Service", "Route"], [["1 (6–8 AM)", "A → P/R → J"], ["2 (9–11 AM)", "J → R/P → K"], ["3 (12–2 PM)", "K → A → P/R"], ["4 (3–5 PM)", "P/R → J → R/P"], ["5 (6–8 PM)", "R/P → K → A"]]) + \
      p("<b>Magenta</b>") + table(["Service", "Route"], [["1 (6–8 AM)", "K → P/R → J"], ["2 (9–11 AM)", "J → R/P → A"], ["3 (12–2 PM)", "A → K → P/R"], ["4 (3–5 PM)", "P/R → J → R/P"], ["5 (6–8 PM)", "R/P → A → K"]]) + \
      p("A Ambala, J Jagadhri, K Kurukshetra, P Panipat, R Rohtak.")
P.dilr_set(1, "Set 1 — Two bullet trains", DIR,
 p("A railway zone has designated Ambala, Jagadhri, Kurukshetra, Panipat, and Rohtak as five key hubs for introducing bullet trains. Two bullet train rakes, Blue and Magenta, connect these hubs.") +
 p("<b>First service:</b> The Blue train departs Ambala at 6 AM, while the Magenta train departs Kurukshetra at 6 AM. Both trains travel for one hour to an intermediate hub (which is not Kurukshetra for the Blue train and not Ambala for the Magenta train), where they halt for a negligible time and then travel one more hour to reach their destination hub. Both trains halt at their respective destination hubs for one hour before starting the second service.") +
 p("<b>Subsequent services (second to fifth):</b> Both trains start each service from the destination of the previous service, one hour after the previous service ends. Trains follow the same pattern: one hour to an intermediate hub, a negligible halt, then one more hour to the destination hub of that service.") +
 p("The destinations of the fifth and final services are the stations from where the trains start their next day’s journeys. Both trains run at the same, unchanging speed. Each hub serves as a starting point, an intermediate hub and a destination exactly once for each train in a day.") +
 p("The following points are known:") +
 "<ol><li>Both trains were spotted at Jagadhri at 8 AM, 9 AM and 4 PM. At no other hub were both trains spotted together.</li>"
 "<li>The two moving trains cross each other in opposite directions only at 12:30 PM and 7:30 PM, at the same place. On both occasions the Blue train travels between the same two hubs in the same direction, and so does the Magenta train.</li>"
 "<li>No train travels along the same route (between the same starting and destination hubs, in the same direction) more than once in a day.</li></ol>",
 "DILR::LR::Scheduling",
 steps(("The timetable", p("Services run 6–8, 9–11, 12–14, 15–17 and 18–20, with intermediate hubs reached at 7, 10, 13, 16 and 19. Each service’s destination is the next one’s start.")),
       ("Jagadhri", p("At 8 and 9 both trains are at Jagadhri: it is the destination of service 1 and the start of service 2 for both. At 4 PM both are at Jagadhri as the intermediate hub of service 4.")),
       ("The crossings", p("At 12:30 both trains are on the first leg of service 3; at 7:30, on the second leg of service 5. Each train runs the same leg both times, and the two trains run it in opposite directions. Since service 2 starts at Jagadhri and K and A are still unused as service-3 starts, Blue runs K → A and Magenta A → K both times.")),
       ("What’s left", p("Panipat and Rohtak fill the remaining slots, and they can swap for each train independently, so there are 4 schedules (P/R below means ‘one of the two’).") + SCH)) +
 final("Every hub is fixed except where Panipat and Rohtak swap; 4 schedules in all."),
 p("Fix the times first; then the clues pin the hubs at 8, 9, 12:30, 4 PM and 7:30."),
 p("<b>Timetable puzzles:</b> write every train’s position at each hour before matching clues."))
P.dq(1, "Consider the following two statements:<br>Statement A: Blue train is at Ambala at 1 PM everyday.<br>Statement B: Magenta train is at Kurukshetra at 1 PM everyday.<br>What can be said about these two statements?",
 ["None of these statements is true", "Only one of these statements is true", "Both statements are true", "Nothing conclusive can be said about the veracity of these two statements"], "MCQ", "3", "Hard",
 "1 PM is the intermediate stop of service 3.",
 steps(("Service 3", p("Blue runs K → A → …, so it is at Ambala at 1 PM. Magenta runs A → K → …, so it is at Kurukshetra."))) + final("Option 3"),
 [("1", "Both hold in every schedule."), ("2", "Both hold."), ("4", "They hold in all four schedules.")])
P.dq(2, "How many different schedules are possible for the two trains throughout the five services of the day?", ["1", "2", "4", "More than 4"], "MCQ", "3", "Hard",
 "What is still undecided after all the clues?",
 steps(("Choices left", p("For each train, Panipat and Rohtak can swap. 2 × 2 = 4."))) + final("4, option 3"),
 [("1", "Panipat and Rohtak can swap."), ("2", "Each train swaps independently."), ("4", "Everything else is fixed.")])
P.dq(3, "Between which two hubs do the two trains cross each other at 12:30 PM?", ["Ambala and Kurukshetra", "Kurukshetra and Panipat", "Panipat and Rohtak", "Rohtak and Jagadhri"], "MCQ", "1", "Hard",
 "The first leg of service 3.",
 steps(("Service 3", p("Blue K → A, Magenta A → K."))) + final("Option 1"), [("2", "Not a service-3 first leg."), ("3", "Not a service-3 first leg."), ("4", "Not a service-3 first leg.")])
P.dq(4, "How many other hubs can be reached from Jagadhri in exactly one hour using either train, if it is known that the passengers can board/alight at the intermediate hubs?", ["4", "3", "2", "1"], "MCQ", "3", "Hard",
 "Which legs start at Jagadhri?",
 steps(("Legs from J", p("Service 2 first leg (9–10) and service 4 second leg (16–17). Each goes to Panipat or Rohtak, so only these two hubs are one hour away."))) + final("2, option 3"),
 [("1", "Only two legs leave Jagadhri."), ("2", "Only Panipat and Rohtak."), ("4", "The two trains reach both.")])
P.dq(5, "What is the minimum number of hours required for a passenger to reach Rohtak from Panipat, if it is known that the passengers can board/alight at the intermediate hubs?", [], "TITA", "2", "Hard",
 "Is there ever a direct Panipat → Rohtak leg?",
 steps(("Service 4", p("Service 4 runs P/R → J → R/P. In a schedule where it starts at Panipat, a passenger goes Panipat → Jagadhri → Rohtak, 3 PM to 5 PM. No leg runs directly from Panipat to Rohtak."))) + final("2"))

# ---------------- Set 2: Coconut crafts (Q6–10) ----------------
SALE = table(["Item", "Qty", "Price", "Total"],
             [["Piggy bank", "30", "600", "18,000"], ["Lamp", "20", "500", "10,000"], ["Mug", "40", "250", "10,000"], ["Jewellery", "32", "300", "9,600"], ["Incense", "25", "200", "5,000"]])
P.dilr_set(2, "Set 2 — Coconut-shell crafts", DIR,
 p("A shop sells craft items made using coconut shells. Currently it sells five different items — piggy bank, coconut shell lamp, jewellery set, incense stick holder and coconut shell mug. In the month of May, the numbers of different items that were sold are 20, 25, 30, 32 and 40 in some order. "
   "The selling prices are among Rs. 200, Rs. 250, Rs. 300, Rs. 500 and Rs. 600 per unit, not necessarily in the given order. The selling prices of each item is different.") +
 p("The selling price of incense stick holders is not twice the selling price of any other item. The same is true of the jewellery set and the coconut shell mug.") +
 p("The revenues generated by the sale of coconut shell lamps and coconut shell mugs were the same and each of them is twice the revenue generated by selling incense stick holders.") +
 p("The revenue generated by selling jewellery sets was not a multiple of 250."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("Prices that are doubles", p("600 = 2 × 300, 500 = 2 × 250. So incense holders, jewellery sets and mugs are priced 200, 250 or 300; the lamp and piggy bank get 500 and 600.")),
       ("Equal revenues", p("Lamp revenue = mug revenue = 2 × incense revenue. Try the mug at 250: 40 × 250 = 10,000 = 20 × 500 (lamp at 500), and incense 25 × 200 = 5,000. ✓")),
       ("The rest", p("Jewellery set: 300 with 32 units = 9,600, not a multiple of 250. ✓ Piggy bank: 600 × 30.") + SALE)) +
 final("Total revenue ₹52,600."),
 p("Prices that are double another price rule items in or out at once; then match equal revenues."),
 p("<b>Two lists to match:</b> use the ‘twice’ and ‘equal’ clues to pair quantities with prices."))
P.dq(6, "How many coconut shell lamps were sold?", [], "TITA", "20", "Medium", "Lamp revenue equals the mug’s.", steps(("Lamp", p("20 at ₹500."))) + final("20"))
P.dq(7, "The highest revenue was generated by selling ________ .", ["Coconut shell lamp", "Either coconut shell lamp or coconut shell mug but not both", "Piggy bank", "Jewellery set"], "MCQ", "3", "Medium",
 "Compare the revenues.", steps(("Highest", p("Piggy bank ₹18,000."))) + final("Option 3"), [("1", "₹10,000."), ("2", "They tie at ₹10,000."), ("4", "₹9,600.")])
P.dq(8, "What was the selling price (in Rs.) of one unit of incense stick holder?", [], "TITA", "200", "Medium", "Half the lamp revenue.", steps(("Incense", p("25 × 200 = 5,000."))) + final("200"))
P.dq(9, "Total revenue generated in the month of May was ______ .", ["More than Rs. 55000", "Between Rs. 40000 and Rs. 50000", "Less than Rs. 40000", "None of these"], "MCQ", "4", "Medium",
 "Add all five.", steps(("Total", p("18,000 + 10,000 + 10,000 + 9,600 + 5,000 = 52,600: between 50,000 and 55,000, which no option names."))) + final("Option 4"),
 [("1", "52,600 is less."), ("2", "52,600 is more than 50,000."), ("3", "Far more.")])
P.dq(10, "Which of the following statements is definitely not true?",
 ["The revenues (in Rs.) generated by selling exactly two types of items were not a multiple of 3.", "The revenue (in Rs.) generated by selling exactly one type of items was not a multiple of 250.", "The average sale of each type of item was Rs. 10520.", "None of these."], "MCQ", "1", "Medium",
 "Check each revenue for divisibility by 3 and by 250.",
 steps(("Multiples of 3", p("18,000 and 9,600 are; 10,000, 10,000 and 5,000 aren’t. So three revenues are not multiples of 3, not two: statement 1 is false.")),
       ("The others", p("Only 9,600 isn’t a multiple of 250 (statement 2 true). 52,600 ÷ 5 = 10,520 (statement 3 true)."))) + final("Option 1"),
 [("2", "True: only jewellery."), ("3", "True."), ("4", "Statement 1 is false.")])

# ---------------- Set 3: Museum visit (Q11–15) ----------------
FL = table(["Floor", "Division"], [["5", "Bronze Age (BA)"], ["4", "Ice Age (TIA)"], ["3", "Stone Age (SA)"], ["2", "Early Modern (EMP)"], ["1", "Iron Age (IA)"]])
VIS = "<ul>" + "".join(f"<li><b>{k}:</b> {v}</li>" for k, v in [("APS", "IA → TIA → EMP → BA → SA"), ("BMS", "SA → EMP → TIA → IA → BA"), ("CPS", "BA → SA → IA → EMP → TIA"),
            ("DIS", "TIA → IA → BA → SA → EMP"), ("EMS", "EMP → BA → SA → TIA → IA")]) + "</ul>" + p("Floors: BA 5, TIA 4, SA 3, EMP 2, IA 1.")
P.dilr_set(3, "Set 3 — A day at the museum", DIR,
 p("The city museum is a major attraction for school students. On the eve of Teachers’ Day, students of five schools, namely APS, BMS, CPS, DIS and EMS, booked a visit to the museum. No other visitors were allowed entry on the day. The museum was opened at 11 AM and closed at 4 PM. "
   "It had five divisions, namely The Ice Age (TIA), The Stone Age (SA), The Bronze Age (BA), The Iron Age (IA), and The Early Modern Period (EMP), located on five different floors from the 1<sup>st</sup> to the 5<sup>th</sup> in some order. All students of each school visited all five floors. "
   "Students of each school were present for exactly one hour on each floor, and the students of different schools were on different floors at the same time. Movement between floors took negligible time.") +
 p("The following facts are also known:") +
 "<ol><li>Students of EMS were on floors above those of APS from 11 AM to 2 PM. After that their relative positions were reversed.</li>"
 "<li>The relative positions of BMS and EMS alternated every hour, starting with BMS on a floor above EMS.</li>"
 "<li>Students of BMS visited TIA after visiting EMP and SA but before visiting IA.</li>"
 "<li>The BA division was visited by CPS, EMS, DIS, APS and BMS, in that chronological order.</li>"
 "<li>When EMS were on the 3<sup>rd</sup> floor, CPS were on a floor below APS. EMS visited the 3<sup>rd</sup> floor immediately after visiting the topmost floor.</li>"
 "<li>EMS visited TIA from 2 PM to 3 PM. The first and last schools to visit TIA were DIS and CPS, respectively.</li>"
 "<li>IA is on the floor immediately below EMP. DIS and EMS were the last groups to visit EMP and IA, respectively.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Who visits what, when", p("Clues 4, 6 and 7 fix many cells: BA by slot; TIA for DIS (11), EMS (2) and CPS (3); EMP for DIS and IA for EMS at 3. Each slot has all five divisions once, and each school sees each division once; with clue 3 for BMS, only one schedule of divisions survives.")),
       ("Floors", p("EMS sees BA (12) then SA (1): BA is the top floor and SA the 3rd (clue 5). IA sits just below EMP. Clues 1 and 2 compare floors each hour; they force TIA on 4, EMP on 2, IA on 1.") + FL),
       ("The full plan", p("Division for each school in each hour (start times 11 AM to 3 PM):") + VIS)) +
 final("Everything is fixed: 25 school–hour–division cells."),
 p("Place divisions by time first (clues 3, 4, 6, 7); floors come last and are checked with clues 1, 2 and 5."),
 p("<b>Two-layer grids:</b> solve the time × group grid first, then map items to positions."))
P.dq(11, "Students of five schools visited five different divisions in five different time slots. Thus a total of 25 combinations of schools, divisions and time slots are formed. How many of them can be uniquely determined?", ["All", "22", "20", "19"], "MCQ", "1", "Hard",
 "Is any cell left open?", steps(("Unique", p("The plan is fully fixed."))) + final("All, option 1"), [("2", "Nothing is left open."), ("3", "Nothing is left open."), ("4", "Nothing is left open.")])
P.dq(12, "In how many slots of one hour each did the students of APS and EMS visit divisions located on consecutive floors?", ["2", "3", "4", "Cannot be determined with certainty"], "MCQ", "3", "Hard",
 "Compare their floors hour by hour.", steps(("Floors", p("APS 1, 4, 2, 5, 3; EMS 2, 5, 3, 4, 1. Consecutive at 11, 12, 1 and 2: 4 slots."))) + final("4, option 3"),
 [("1", "Miscount."), ("2", "Miscount."), ("4", "The plan is fixed.")])
P.dq(13, "How many divisions were visited by the students of APS before the students of DIS?", [], "TITA", "2", "Hard",
 "Compare the two schools’ times for each division.",
 steps(("Compare", p("IA: APS 11, DIS 12 ✓. TIA: APS 12, DIS 11. EMP: APS 1, DIS 3 ✓. BA: APS 2, DIS 1. SA: APS 3, DIS 2. Two."))) + final("2"))
P.dq(14, "The students of which of the following schools visit the division located on the 5<sup>th</sup> floor in the last slot of one hour?", ["APS", "BMS", "CPS", "DIS"], "MCQ", "2", "Hard",
 "BA is on the 5th floor; who sees BA last?", steps(("Clue 4", p("BMS is last to see BA."))) + final("BMS, option 2"), [("1", "APS sees BA at 2 PM."), ("3", "CPS is first."), ("4", "DIS is third.")])
P.dq(15, "After a week of this visit the principal of APS wrote to the curator requesting him to arrange the divisions from the 1<sup>st</sup> floor to the 5<sup>th</sup> floor in chronological order: 1<sup>st</sup> floor TIA, 2<sup>nd</sup> SA, 3<sup>rd</sup> BA, 4<sup>th</sup> IA, and 5<sup>th</sup> EMP. How many divisions are already on the floor recommended?", [], "TITA", "0", "Hard",
 "Compare with the actual floors.", steps(("Compare", p("Actual: TIA 4, SA 3, BA 5, IA 1, EMP 2. None matches."))) + final("0"))

# ---------------- Set 4: Activities (Q16–20) ----------------
VEN = table(["Region", "Girls", "Boys", "Total"],
            [["M only", "44", "63", "107"], ["M+S only", "22", "35", "57"], ["M+D only", "33", "49", "82"], ["All three", "20", "32", "52"],
             ["D only", "0", "2", "2"], ["D+S only", "", "", "164"], ["S only", "", "", "36"]]) + p("M Music, D Dance, S Speech.")
P.dilr_set(4, "Set 4 — Music, dance and speech", DIR,
 p("A total of 500 students study in a government high school. Out of these 500 students, 40% are girls and the remaining are boys. All the students have to select at least one of the following three activities — Music, Dance, and Speech.") +
 p("The number of students who selected Music is 298 and the number of students who selected Dance is 300. The number of students who selected all three activities is 52.") +
 p("Except for 2 boys, all those who chose Dance chose at least one more activity. Among the students who did not select Music, the number of boys was 40 more than the number of girls.") +
 p("Among the girls, the ratio of students who selected only Music, exactly two activities - Music and Speech, and exactly two activities - Music and Dance was 4 : 2 : 3.") +
 p("Among the boys, the ratio of the number of students who selected only Music, exactly two activities - Music and Speech, and exactly two activities - Music and Dance was 9 : 5 : 7."),
 "DILR::LR::Venn_Diagrams",
 steps(("Music", p("Girls: Music only, M+S, M+D = \\(4a, 2a, 3a\\). Boys: \\(9b, 5b, 7b\\). Music total: \\(9a + 21b + 52 = 298\\), so \\(3a + 7b = 82\\): \\((a, b) = (25, 1), (18, 4), (11, 7), (4, 10)\\).")),
       ("Not Music", p("200 girls and 300 boys. With \\(g\\) and \\(h\\) girls and boys in all three (\\(g + h = 52\\)): boys not choosing Music − girls not choosing Music \\(= (300 - 21b - h) - (200 - 9a - g) = 40\\), so \\(g - h = 21b - 9a - 60\\). Only \\(a = 11, b = 7\\) gives a possible value: \\(g - h = -12\\), so \\(g = 20, h = 32\\).")),
       ("Dance and Speech", p("Dance: \\(82 + 52 + 2 + (\\text{D+S only}) = 300\\), so D+S only = 164. Speech only = 500 − everything else = 36.") + VEN)) +
 final("Every region of the Venn diagram is fixed (girl/boy split known for all but the Speech-only and Dance+Speech regions)."),
 p("The Music equation gives a short list of (a, b); the ‘not Music’ clue keeps one."),
 p("<b>Venn diagrams with ratios:</b> write each region with a multiplier, use totals for one equation, and a difference clue to choose."))
P.dq(16, "The number of girls who selected Music and exactly one more activity is ________.", ["22", "55", "90", "Cannot be determined"], "MCQ", "2", "Medium",
 "M+S only and M+D only among girls.", steps(("Count", p("22 + 33 = 55."))) + final("55, option 2"), [("1", "Only M+S."), ("3", "Not this group."), ("4", "a = 11 is fixed.")])
P.dq(17, "How many students selected exactly one activity?", ["145", "150", "155", "Cannot be determined"], "MCQ", "1", "Medium",
 "Music only, Dance only, Speech only.", steps(("Count", p("107 + 2 + 36 = 145."))) + final("145, option 1"), [("2", "Miscount."), ("3", "Miscount."), ("4", "Fixed.")])
P.dq(18, "What is the difference between the number of students who selected both Dance and Speech but not Music and the number of students who selected both Music and Speech but not Dance?", ["87", "57", "127", "107"], "MCQ", "4", "Medium",
 "164 against 57.", steps(("Difference", p("164 − 57 = 107."))) + final("107, option 4"), [("1", "Miscount."), ("2", "That is the M+S group."), ("3", "Miscount.")])
P.dq(19, "The number of students who did not select Speech is ________.", ["181", "202", "191", "Cannot be determined"], "MCQ", "3", "Medium",
 "Music only, Dance only, Music + Dance only.", steps(("Count", p("107 + 2 + 82 = 191."))) + final("191, option 3"), [("1", "Miscount."), ("2", "Miscount."), ("4", "Fixed.")])
P.dq(20, "Which of the following is definitely true?", ["Number of students selected only Speech < Number of students selected all three activities.", "Number of students selected only Music < Number of students selected all three activities.",
 "Number of students selected only Music > Number of students who did not select Speech.", "None of these."], "MCQ", "1", "Medium",
 "Compare the regions.", steps(("Check", p("Speech only 36 < 52 ✓. Music only 107 > 52. Music only 107 < 191."))) + final("Option 1"),
 [("2", "107 > 52."), ("3", "107 < 191."), ("4", "Option 1 holds.")])
