# -*- coding: utf-8 -*-
# Simp Mock 5 (2025): DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m25_05 import P
import m25_05_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Animals in five reserves (Q1–6) ----------------
P.dilr_set(1, "Set 1 — Animals in five reserves", DIR,
 p("Nishad has joined a national wildlife survey as an intern. His assignment is to analyse the populations of different animals found in various reserve forests of India. He selected five reserve forests, namely Jaldapara National Park (JNP), Kaziranga National Park (KNP), Manas National Park (MNP), Namdapha National Park (NNP) and Pobitora Wildlife Sanctuary (PWS), and five animals, namely Rhino, Leopard, Gibbon, Sambar and Wild Pig, for the analysis. As per Nishad’s findings, the following facts are known:") +
 p("The numbers of Rhinos present in JNP, PWS, NNP, MNP and KNP are in the ratio 1 : 2 : 11 : 17 : 23, in that order. The same is true for each of the other four animals.") +
 p("In any one of these five reserve forests, the numbers of Rhinos, Leopards, Gibbons, Sambar and Wild Pigs, in that order, are in the ratio 1 : 2 : 11 : 17 : 23."),
 "DILR::DI::Caselets",
 steps(("One constant", p(r"Both ratios are 1 : 2 : 11 : 17 : 23, so the count of animal \(a\) in forest \(f\) is \(k \times r_a \times r_f\) for one constant \(k\).")),
       ("Totals", p(r"Each ratio sums to 54. Total of animal \(a\) over all forests: \(54k\,r_a\). Total in forest \(f\): \(54k\,r_f\). Grand total: \(54^2 k = 2916k\)."))) +
 final(r"Each count is k × (animal ratio) × (forest ratio); the grand total is \(2916k\)."),
 p("Write every count as k × (animal ratio) × (forest ratio); one unknown decides everything."),
 p("<b>Two-way ratios:</b> when rows and columns share fixed ratios, every cell is a product of the two."))
P.dq(1, "Which of the following can be the total number of the five types of animals together present in the given five reserve forests?", ["65068", "66068", "67068", "68068"], "MCQ", "3", "Easy",
 "The grand total is a multiple of 2916.",
 steps(("Divide", p(r"\(67068 = 2916 \times 23\). The others leave remainders."))) + final("67068, option 3"),
 [("1", "Not a multiple of 2916."), ("2", "Not a multiple of 2916."), ("4", "Not a multiple of 2916.")])
P.dq(2, "The population of Rhinos in MNP will increase by 25% if 3, 12, 15 and 21 Rhinos are transferred to MNP from JNP, PWS, NNP and KNP respectively. If the number of Leopards, Gibbons, Sambar and Wild Pigs taken together in MNP after the transfer becomes p% of the total number of the five animals in MNP, then the value of p will be _________ .", [r"\(95 < p < 96\)", r"\(96 < p < 97\)", r"\(97 < p < 98\)", r"\(p > 98\)"], "MCQ", "3", "Medium",
 "51 Rhinos arrive, which is 25% of MNP’s Rhinos.",
 steps(("Find k", p(r"MNP Rhinos: \(17k\). \(0.25 \times 17k = 51\), so \(k = 12\).")),
       ("After", p(r"Other four animals in MNP: \(17 \times 12 \times 53\) \(= 10812\). Rhinos: \(204 + 51 = 255\).")),
       ("Share", p(r"\(10812 \div 11067 \approx 97.7\%\)."))) + final("Option 3"),
 [("1", "Too low."), ("2", "Too low."), ("4", "Too high.")])
P.dq(3, "Given that the total number of Gibbons present in these five reserve forests is more than 6770 but less than 8790, which of the following cannot be the total number of Leopards present in these five reserve forests together?", ["1296", "1404", "1476", "1512"], "MCQ", "3", "Medium",
 "Gibbons total 594k; Leopards total 108k.",
 steps(("Range of k", p(r"\(6770 < 594k < 8790\) gives \(k = 12, 13, 14\).")),
       ("Leopards", p(r"\(108k = 1296, 1404, 1512\). 1476 is not possible."))) + final("1476, option 3"),
 [("1", "k = 12."), ("2", "k = 13."), ("4", "k = 14.")])
P.dq(4, "Which of the following statements is definitely TRUE?", ["Number of Leopards in KNP > Number of Gibbons in PWS", "Number of Sambar and Wild Pigs together in JNP > Number of Leopards in KNP", "Number of Rhinos and Sambar together in MNP > Number of Gibbons and Sambar together in NNP", "Number of Wild Pigs in KNP > Sum of the numbers of Gibbons in KNP and Sambar in MNP"], "MCQ", "1", "Medium",
 "Write each side as a multiple of k.",
 steps(("Each side in units of k", p("Option 1: 2 × 23 against 11 × 2. Option 2: 17 + 23 against 46. Option 3: 17 × (1 + 17) against 11 × (11 + 17). Option 4: 23 × 23 against 11 × 23 + 17 × 17.") + table(["Option", "Left", "Right"], [["1", "46k", "22k"], ["2", "40k", "46k"], ["3", "306k", "308k"], ["4", "529k", "542k"]], hi={(0, 1)}))) + final("Option 1"),
 [("2", "40k < 46k."), ("3", "306k < 308k."), ("4", "529k < 542k.")])
P.dq(5, "What can be the minimum number of Leopards present in Kaziranga National Park if the average number of each of the five types of animals across the five reserve forests is a positive integer?", [], "TITA", "230", "Medium",
 "Rhinos average \\(54k/5\\).",
 steps(("k", p(r"Rhino average \(54k/5\) must be an integer, so \(k\) is a multiple of 5; the smallest is 5.")),
       ("Leopards in KNP", p(r"\(2 \times 23 \times 5 = 230\)."))) + final("230"))
P.dq(6, "The average number of each of the five types of animals across the five reserve forests is a positive integer. What is the total number of Wild Pigs present in Pobitora Wildlife Sanctuary, given that the total number of the five types of animals present in the five reserve forests taken together is between 60000 and 80000 (inclusive)?", [], "TITA", "1150", "Medium",
 "k is a multiple of 5 and 2916k is in range.",
 steps(("k", p(r"\(60000 \le 2916k \le 80000\) gives \(21 \le k \le 27\); the only multiple of 5 is 25.")),
       ("Wild Pigs in PWS", p(r"\(23 \times 2 \times 25 = 1150\)."))) + final("1150"))

# ---------------- Set 2: Cousins in rows (Q7–10) ----------------
SEATS = table(["", "Col 1", "Col 2", "Col 3"], [["R1", "", "(Iyengar)", ""], ["R2", "(Iyengar)", "", "Kapil"], ["R3", "(Iyengar)", "", "(Parekh)"], ["R4", "", "", "Mayur"], ["R5", "", "", ""]])
FINAL = table(["", "Col 1", "Col 2", "Col 3"], [["R1", "Parth", "Sagar", "Kshitij"], ["R2", "Vinodini", "Yogesh", "Kapil"], ["R3", "Ranjini", "Jinal", "Shraddha"], ["R4", "Prachi", "Deepthi", "Mayur"], ["R5", "Ronak", "Snehal", "Satbir"]])
P.dilr_set(2, "Set 2 — Cousins in five rows", DIR,
 p("In all, 15 cousins from 6 families are attending a family get-together. The cousins and their families are: Yogesh and Prachi from the Verma family; Kapil from the Ramuka family; Mayur from the Sharma family; Parth, Jinal and Shraddha from the Parekh family; Sagar, Kshitij, Vinodini, Ranjini and Deepthi from the Iyengar family; and Satbir, Ronak and Snehal from the Desai family.") +
 p("They are sitting in 5 rows and 3 columns as shown below. A family name in brackets means someone from that family sits in that place; for example, someone from the Iyengar family sits in Row 1, Column 2.") + SEATS +
 p("Row 1 is in front of Row 2, which is in front of Row 3, and so on. Column 1 is to the left of Column 2, which is to the left of Column 3.") +
 p("The following information is known:") +
 "<ol><li>The 5<sup>th</sup> row has all its cousins from the same family.</li><li>Parth is sitting immediately in front of Vinodini, who sits to the immediate left of Yogesh.</li><li>Jinal is sitting between Ranjini and Shraddha in the same row.</li><li>Deepthi and Prachi are sitting in the same row, and Deepthi is sitting to the right of Prachi.</li><li>Mayur is sitting neither in the same row nor in the same column as Sagar.</li><li>Ronak is sitting to the immediate left of Snehal, who is sitting to the immediate left of Satbir.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Row 5", p("Only a family of at least three with no one else needed elsewhere can fill it. The Parekhs already have someone in Row 3; the Iyengars have three seats in Rows 1–3 and only five members. So Row 5 is the Desais: Ronak, Snehal, Satbir from left (clue 6).")),
       ("Vinodini", p("She needs a seat in front of her (Parth) and a seat to her right (Yogesh). Columns 3 of Rows 2–4 are taken by Kapil, a Parekh and Mayur, and R2C1/R3C1 are Iyengar seats. The only fit: Vinodini R2C1, Parth R1C1, Yogesh R2C2.")),
       ("Jinal’s row", p("Jinal sits in Column 2 with Ranjini and Shraddha beside her. Row 3 is the only row with a Parekh seat free in Column 3 and an Iyengar seat in Column 1: Ranjini R3C1, Jinal R3C2, Shraddha R3C3.")),
       ("The rest", p("Prachi and Deepthi need two seats in one row: R4C1 and R4C2. Sagar and Kshitij take R1C2 and R1C3; Mayur (Column 3) rules out Sagar in Column 3, so Sagar R1C2 and Kshitij R1C3.")),
       ("Seating", FINAL)) +
 final("All 15 seats are fixed."),
 p("Start with the row that must be one family, then with the person who needs two neighbours (in front and to the right)."),
 p("<b>Grid seating:</b> place the clue with the most constraints first; pre-filled cells cut options fast."))
P.dq(7, "Who is sitting at the left corner of the first row?", ["Kshitij", "Mayur", "Parth", "Ranjini"], "MCQ", "3", "Easy",
 "Parth is in front of Vinodini.", steps(("R1C1", p("Parth."))) + final("Option 3"),
 [("1", "Row 1, Column 3."), ("2", "Row 4, Column 3."), ("4", "Row 3, Column 1.")])
P.dq(8, "For how many cousins can the sitting place be determined uniquely?", ["12", "15", "9", "6"], "MCQ", "2", "Medium",
 "Every step of the arrangement was forced.", steps(("Count", p("The arrangement is unique: all 15."))) + final("15, option 2"),
 [("1", "Every seat is fixed."), ("3", "Every seat is fixed."), ("4", "Every seat is fixed.")])
P.dq(9, "What is the name of the cousin sitting to the immediate left of Mayur?", ["Prachi", "Kshitij", "Deepthi", "Yogesh"], "MCQ", "3", "Easy",
 "Mayur is R4C3.", steps(("R4C2", p("Deepthi."))) + final("Option 3"),
 [("1", "R4C1, two seats away."), ("2", "Row 1."), ("4", "Row 2.")])
P.dq(10, "Who is sitting in front of Kapil?", ["Vinodini", "Mayur", "Shraddha", "Kshitij"], "MCQ", "4", "Easy",
 "Kapil is R2C3; in front is R1C3.", steps(("R1C3", p("Kshitij."))) + final("Option 4"),
 [("1", "Same row as Kapil."), ("2", "Behind Kapil."), ("3", "Behind Kapil.")])

# ---------------- Set 3: Shipping costs (Q11–14) ----------------
P.dilr_set(3, "Set 3 — Shipping costs", DIR,
 p("Eight countries, A, B, C, D, E, F, G and H, trade among themselves, exporting and importing goods. The table below shows the transportation costs (in dollars per 10 kg) between the pairs of countries in 2024.") + F.MATRIX +
 p("The row is the exporting country and the column the importing country. For example, if Country B exports to Country D, the transportation cost is 5 dollars per 10 kg. ‘X’ means a country cannot trade with itself.") +
 p("To reduce transportation cost, a consignment can be sent via one or more intermediate countries if the direct route is expensive.") +
 p("Example: Country A wants to export goods to Country B. The direct cost from A to B is 20 dollars per 10 kg. If A exports to D first at 10 dollars per 10 kg and then D to B at 8 dollars per 10 kg, the total is 10 + 8 = 18 dollars per 10 kg."),
 "DILR::LR::Routes_and_Networks",
 steps(("Reading", p("Row = from, column = to. The cost from X to Y is not the same as Y to X, so always read in the direction of travel."))) +
 final("Each question uses the table directly."),
 p("Direction matters: A → B is row A, column B."),
 p("<b>Cost matrices:</b> for routes, add costs along the path; for export/import totals, add rows and columns."))
P.dq(11, "A consignment is to be sent from Country C to Country A, passing through exactly two intermediate countries. The transportation cost for each segment (C → first intermediate → second intermediate → A) must be an even number, and the costs must strictly decrease with each segment (cost of C to the first intermediate country > cost of first to second intermediate country > cost of second intermediate country to A). How many such valid delivery paths are possible, if neither C nor A can be an intermediate country? (Assume the consignment weighs 10 kg.)", ["1", "2", "3", "4"], "MCQ", "4", "Hard",
 "Into A with an even cost: B 14, D 10, E 12, G 12, H 16. From C with an even cost: B 6, D 18, F 20, G 12, H 14.",
 steps(("First leg", p("C → B costs 6, and no even cost below 6 leads on, so B is out as the first stop. C → G (12) and C → H (14) leave too little room for two smaller even legs: none works.")),
       ("Check D and F", table(["Path", "Costs", "Valid?"], [["C→D→G→A", "18 > 16 > 12", "Yes"], ["C→F→D→A", "20 > 16 > 10", "Yes"], ["C→F→E→A", "20 > 14 > 12", "Yes"], ["C→F→G→A", "20 > 18 > 12", "Yes"], ["C→D→B→A", "18, 8, 14", "No"], ["C→F→B→A", "20, 14, 14", "No"]], hi={(0, 2), (1, 2), (2, 2), (3, 2)}))) +
 final("4, option 4"),
 [("1", "Misses paths."), ("2", "Misses paths."), ("3", "Misses one of the four.")])
P.dq(12, "A consignment has to be sent from Country B to Country E for a quality check and then returned to Country B. It must be routed through the same intermediate country in both directions (B → X → E and E → X → B). What is the minimum total transportation cost (in dollars) for sending and receiving 10 kg of goods under this condition?", [], "TITA", "26", "Medium",
 "Add four legs for each choice of X.",
 steps(("Each X", table(["X", "B→X→E", "E→X→B", "Total"], [["A", "14 + 12", "12 + 20", "58"], ["C", "8 + 7", "5 + 6", "26"], ["D", "5 + 20", "10 + 8", "43"], ["F", "16 + 14", "18 + 10", "58"], ["G", "14 + 13", "14 + 11", "52"], ["H", "20 + 15", "13 + 14", "62"]], hi={(1, 3)}))) + final("26"))
P.dq(13, "For how many countries is the sum of the transportation costs to export to the 7 other countries more than the sum of the costs to import from the 7 other countries, for the same weight, if shipments are sent directly without any intermediate country?", [], "TITA", "5", "Medium",
 "Export = row sum; import = column sum.",
 steps(("Sums", table(["Country", "Export", "Import", "More?"], [["A", "111", "85", "Yes"], ["B", "95", "83", "Yes"], ["C", "85", "75", "Yes"], ["D", "101", "96", "Yes"], ["E", "86", "99", "No"], ["F", "99", "128", "No"], ["G", "96", "108", "No"], ["H", "112", "111", "Yes"]]))) + final("5"))
P.dq(14, "Two of the 8 countries are selected at random; call them C1 and C2. The cost (in dollars) of sending a 10 kg consignment from C1 to C2 is x, and from C2 to C1 is y. What is the probability that |x − y| is more than 5?", [r"\(\dfrac47\)", r"\(\dfrac12\)", r"\(\dfrac5{14}\)", r"\(\dfrac27\)"], "MCQ", "4", "Medium",
 "Compare each cell with its mirror across the diagonal: 28 pairs.",
 steps(("Pairs over 5", p("A–B 6, A–C 6, A–F 9, A–G 6, B–F 6, B–H 6, C–F 8, D–E 10: 8 pairs.")),
       ("Probability", p(r"\(\dfrac{8}{28} = \dfrac27\)."))) + final("Option 4"),
 [("1", "16 of 28."), ("2", "14 of 28."), ("3", "10 of 28.")])

# ---------------- Set 4: Five tourists, five places (Q15–20) ----------------
CLUES = ("<ul><li><b>Wednesday</b>: Dakshineswar Temple — the tourist from Australia.</li>"
         "<li><b>Thursday</b>: Sundarban National Park — Devin; Chandannagar French Colony — the tourist from New Zealand; Mandarmani Beach — the tourist from Australia; Kolkata City — Chris.</li>"
         "<li><b>Friday</b>: Sundarban National Park — Harry; Mandarmani Beach — the Harbour Travels tourist; Dakshineswar Temple — Alan.</li>"
         "<li><b>Saturday</b>: Mandarmani Beach — the Dune Trips tourist; Dakshineswar Temple — the tourist from Ireland.</li>"
         "<li><b>Sunday</b>: Sundarban National Park — the Willow Tours tourist; Chandannagar French Colony — the tourist from England; Kolkata City — the Kestrel Tours tourist.</li></ul>")
WHO = table(["Tourist", "From", "Agency"], [["Alan", "NZ", "Willow"], ["Ben", "England", "Harbour"], ["Chris", "Ireland", "Xenia"], ["Devin", "Romania", "Dune"], ["Harry", "Australia", "Kestrel"]])
GRID = ("<ul><li><b>Alan</b>: Mandarmani (Wed), Chandannagar (Thu), Dakshineswar (Fri), Kolkata (Sat), Sundarban (Sun)</li>"
        "<li><b>Ben</b>: Kolkata (Wed), Dakshineswar (Thu), Mandarmani (Fri), Sundarban (Sat), Chandannagar (Sun)</li>"
        "<li><b>Chris</b>: Sundarban (Wed), Kolkata (Thu), Chandannagar (Fri), Dakshineswar (Sat), Mandarmani (Sun)</li>"
        "<li><b>Devin</b>: Chandannagar (Wed), Sundarban (Thu), Kolkata (Fri), Mandarmani (Sat), Dakshineswar (Sun)</li>"
        "<li><b>Harry</b>: Dakshineswar (Wed), Mandarmani (Thu), Sundarban (Fri), Chandannagar (Sat), Kolkata (Sun)</li></ul>")
P.dilr_set(4, "Set 4 — Five tourists, five places", DIR,
 p("Alan, Ben, Chris, Devin and Harry are five foreigners visiting India. They come from five different countries, namely Australia, England, Ireland, New Zealand and Romania, in some order. All of them will visit Kolkata and the tourist spots near the city. They contacted five different travel agencies, namely Dune Trips, Harbour Travels, Kestrel Tours, Xenia Travels and Willow Tours, to arrange their visits.") +
 p("Each tourist will visit five places on five consecutive days starting from the same date, a Wednesday. No two tourists visit the same place on the same day, and each visits all five places without repetition, exactly one place a day. The places are Sundarban National Park, Mandarmani Beach, Chandannagar French Colony, Dakshineswar Temple and Kolkata City. Each travel agency serves exactly one of the five tourists.") +
 p("Further, we know that:") +
 "<ul><li>Xenia Travels will take its tourist to Kolkata City on Thursday.</li><li>Ben will visit Chandannagar French Colony on the last day of the tour.</li><li>Devin did not contact Harbour Travels.</li></ul>" +
 p("The following is partial information about who visits which place on which day (each entry names the tourist, the tourist’s country, or the tourist’s agency):") + CLUES,
 "DILR::LR::Scheduling",
 steps(("First links", p("Chris is at Kolkata City on Thursday, so Chris uses Xenia Travels. Ben is at Chandannagar on Sunday, so Ben is from England.")),
       ("Australia and New Zealand", p("The Australian is at Dakshineswar on Wednesday and Mandarmani on Thursday. Devin and Chris are elsewhere on Thursday, Alan is at Dakshineswar on Friday, and Ben is English: Harry is Australian. The New Zealander is at Chandannagar on Thursday; that excludes Devin, Chris, Harry and Ben: Alan. Chris and Devin are Irish and Romanian in some order.")),
       ("Harry", p("Harry: Dakshineswar Wed, Mandarmani Thu, Sundarban Fri. Chandannagar on Sunday is Ben, so Harry has Chandannagar Sat and Kolkata City Sun: Harry uses Kestrel Tours.")),
       ("Agencies", p("Sundarban on Sunday (Willow Tours) can’t be Ben, Harry, Devin (Sundarban Thu) or Chris (Xenia): it is Alan, with Willow Tours. Ben and Devin share Harbour and Dune; Devin isn’t Harbour, so Devin uses Dune Trips and Ben Harbour Travels. So Ben is at Mandarmani Fri and Devin at Mandarmani Sat.")),
       ("Ireland", p("The Irish tourist is at Dakshineswar on Saturday; Devin is at Mandarmani then, so Chris is Irish and Devin Romanian.")),
       ("Filling the grid", p("Mandarmani is taken Thu–Sat, so Alan’s Mandarmani is Wednesday and his Kolkata City Saturday. Chris’s Sundarban must be Wednesday, so Ben’s is Saturday; Ben then has Dakshineswar Thu and Kolkata Wed. Devin has Kolkata Fri, Chandannagar Wed and Dakshineswar Sun; Chris has Chandannagar Fri and Mandarmani Sun.")),
       ("Results", WHO + GRID)) +
 final("Everything is fixed: nationalities, agencies and the full schedule."),
 p("Link agency and nationality clues to names first; then each column and row of the day–place grid has every tourist once."),
 p("<b>Latin-square schedules:</b> each place has each tourist once and each day has each tourist once, so the last gap in any row or column is forced."))
P.dq(15, "The nationality of how many of the five tourists can be uniquely determined?", [], "TITA", "5", "Medium",
 "Every step was forced.", steps(("Count", p("All five: Alan NZ, Ben England, Chris Ireland, Devin Romania, Harry Australia."))) + final("5"))
P.dq(16, "How many places will Ben visit on the day immediately after the day on which Harry visits the same place?", [], "TITA", "4", "Medium",
 "Compare Harry’s day and Ben’s day for each place.",
 steps(("Place by place", table(["Place", "Harry", "Ben", "Next?"], [["Sundarban", "Fri", "Sat", "Yes"], ["Chandan.", "Sat", "Sun", "Yes"], ["Mandar.", "Thu", "Fri", "Yes"], ["Kolkata", "Sun", "Wed", "No"], ["Dakshin.", "Wed", "Thu", "Yes"]]))) + final("4"))
P.dq(17, "Who will start the five-day tour with a visit to Kolkata City?", ["Alan", "Ben", "Devin", "Harry"], "MCQ", "2", "Easy",
 "Kolkata City on Wednesday.", steps(("Wednesday", p("Ben is at Kolkata City."))) + final("Ben, option 2"),
 [("1", "Mandarmani on Wednesday."), ("3", "Chandannagar on Wednesday."), ("4", "Dakshineswar on Wednesday.")])
P.dq(18, "What is the country of origin of the person who will visit Sundarban National Park on Wednesday?", ["England", "Ireland", "New Zealand", "Romania"], "MCQ", "2", "Easy",
 "Who is at Sundarban on Wednesday?", steps(("Wednesday", p("Chris, who is Irish."))) + final("Ireland, option 2"),
 [("1", "Ben: Kolkata on Wednesday."), ("3", "Alan: Mandarmani."), ("4", "Devin: Chandannagar.")])
P.dq(19, "Find the correct combination of the tourist’s country of origin and the travel agency that arranges the visits for that tourist.", ["Australia – Willow Tours, England – Dune Trips, Ireland – Xenia Travels, New Zealand – Harbour Travels", "England – Kestrel Tours, Ireland – Harbour Travels, New Zealand – Dune Trips, Romania – Xenia Travels", "Australia – Kestrel Tours, England – Harbour Travels, New Zealand – Willow Tours, Romania – Dune Trips", "Australia – Willow Tours, Ireland – Harbour Travels, New Zealand – Kestrel Tours, Romania – Xenia Travels"], "MCQ", "3", "Medium",
 "Australia = Harry = Kestrel.", steps(("Check", p("Harry (Australia) – Kestrel, Ben (England) – Harbour, Alan (New Zealand) – Willow, Devin (Romania) – Dune. All four in option 3 match."))) + final("Option 3"),
 [("1", "Australia is Kestrel, not Willow."), ("2", "England is Harbour."), ("4", "Australia is Kestrel.")])
P.dq(20, "Which two places will the tourist from Romania not be able to visit if he has to leave due to an emergency immediately after Friday?", ["Mandarmani Beach and Dakshineswar Temple", "Kolkata City and Sundarban National Park", "Chandannagar French Colony and Dakshineswar Temple", "Dakshineswar Temple and Sundarban National Park"], "MCQ", "1", "Easy",
 "Romania = Devin. What is he scheduled for on Saturday and Sunday?",
 steps(("Devin", p("Saturday: Mandarmani Beach; Sunday: Dakshineswar Temple."))) + final("Option 1"),
 [("2", "Visited on Friday and Thursday."), ("3", "Chandannagar was Wednesday."), ("4", "Sundarban was Thursday.")])
