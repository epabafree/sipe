# -*- coding: utf-8 -*-
# Simp Mock 2: DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m02 import P
import m02_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Diesel locomotives (Q1–5) ----------------
TOT = table(["Year", "Diesel locomotives"], [["2023-24", "2400"], ["2024-25", "1800"], ["2025-26", "1440"], ["2026-27", "1200"]])
FIN = p("Y1 to Y4 are 2023-24 to 2026-27.") + table(["Zone", "Y1", "Y2", "Y3", "Y4"],
            [["SR", "360", "360", "360", "360"], ["ER", "480", "540", "144", "120"], ["WR", "600", "450", "288", "180"],
             ["CR", "480", "180", "360", "300"], ["NR", "480", "270", "288", "240"]])
P.dilr_set(1, "Set 1 — Phasing out diesel locomotives", DIR,
 p("The railway ministry plans to phase out diesel locomotives. The railways are split into five zones: Northern (NR), Southern (SR), Eastern (ER), Western (WR) and Central (CR). The table gives the total number of diesel locomotives planned for the whole country in each of the next four years. The national total falls every year, but a single zone’s number need not.") + TOT +
 p("The chart gives each zone’s percentage share of the year’s total. The years are hidden as W, X, Y and Z and the zones as A, B, C, D and E, in no particular order.") + F.SHARE +
 p("The following facts are also known.") +
 "<ol><li>Northern Railways’ four numbers are all different.</li>"
 "<li>Eastern Railways’ number rises by 12.5% from 2023-24 to 2024-25, then falls in each of the next two years.</li>"
 "<li>Eastern Railways’ number for 2025-26 is less than one-third of its number for 2024-25.</li>"
 "<li>Western Railways is the only zone whose number falls every year.</li>"
 "<li>Central Railways’ number for 2024-25 equals Western Railways’ lowest number in the four years.</li></ol>",
 "DILR::DI::Graphs_and_Charts",
 steps(("Eastern Railways", p("If ER is a% of 2400 and then b% of 1800, 1800b = 1.125 × 2400a, so b = 1.5a: two shares in the ratio 2 : 3. Zone B has 20 (X) and 30 (W); zone A has 20 (W) and 30 (Z).")),
       ("Rule out A", p("If A were ER, 2024-25 would be 30% of 1800 = 540, and 2025-26 would be 15% or 25% of 1440, that is 216 or 360: not below 540 ÷ 3 = 180. So ER is B, X is 2023-24 and W is 2024-25: 480 then 540.")),
       ("Western Railways", p("For 2023-24 and 2024-25 the zones are A 360, 360; C 600, 450; D 480, 180; E 480, 270. A is level. D and E fall below their later numbers whichever way Y and Z go (D is at least 300 later; E is 288 or 240 after 270, and 288 comes in 2025-26 either way). Only C works, with Y = 2025-26 (20% of 1440 = 288) and Z = 2026-27 (15% of 1200 = 180).")),
       ("The rest", p("WR’s lowest is 180, which is D’s 2024-25 number: D is CR. A is the same every year, so it cannot be NR: A is SR and E is NR.") + FIN)) +
 final("All five zones and all four years are fixed."),
 p("A 12.5% rise from a total of 2400 to a total of 1800 means the share must rise by half: look for shares in the ratio 2 : 3."),
 p("<b>Shares of changing totals:</b> compare actual numbers, not percentages, once the year totals differ."))
P.dq(1, "What is the average number of diesel locomotives per year planned for Southern Railways over the four years?", [], "TITA", "360", "Medium",
 "Southern Railways is zone A.",
 steps(("SR", p("15% of 2400, 20% of 1800, 25% of 1440 and 30% of 1200 are all 360."))) + final("360"))
P.dq(2, "What are the three smallest numbers of diesel locomotives planned for any zone in any year?", ["140, 150, 180", "120, 140, 180", "120, 144, 180", "144, 150, 180"], "MCQ", "3", "Medium",
 "Read the lowest entries of the final table.",
 steps(("Lowest", p("ER 120 and 144, then 180 (WR in 2026-27 and CR in 2024-25). Every other entry is 240 or more."))) + final("Option 3"),
 [("1", "No zone has 140 or 150."), ("2", "No zone has 140."), ("4", "Misses ER’s 120.")])
P.dq(3, "What is the largest difference between one zone’s numbers in two of the years?", ["420", "360", "300", "270"], "MCQ", "1", "Medium",
 "Highest minus lowest, zone by zone.",
 steps(("Zones", p("ER 540 − 120 = 420; WR 600 − 180 = 420; CR 480 − 180 = 300; NR 480 − 240 = 240; SR 0."))) + final("Option 1"),
 [("2", "Not the largest."), ("3", "CR’s difference."), ("4", "Not the largest.")])
P.dq(4, "What is the largest percentage fall from one year to the next for any zone?", ["74.56%", "73.33%", "72.25%", "57.14%"], "MCQ", "2", "Medium",
 "ER from 2024-25 to 2025-26 is the steepest drop.",
 steps(("ER", p("540 to 144: a fall of 396 ÷ 540 = 73.33%.")),
       ("Others", p("CR 480 to 180 is 62.5%; NR 480 to 270 is 43.75%; WR’s falls are under 40%."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Not a fall that occurs.")])
P.dq(5, "How many of the five zones can be matched to their letters with certainty?", [], "TITA", "5", "Easy",
 "The set’s working fixes every letter.",
 steps(("All", p("A = SR, B = ER, C = WR, D = CR, E = NR."))) + final("5"))

# ---------------- Set 2: A bakery's morning shift (Q6–10) ----------------
UNITS = table(["Hour", "Cake", "Bread", "Patty", "Cookies"],
              [["1st", "10", "10", "", ""], ["2nd", "10", "10", "10", "0"],
               ["3rd", "10", "10", "20", "10"], ["4th", "10", "10", "20", "0"]])
TWO = table(["Worker", "Group", "Item", "Hours"],
            [["Anu", "Bengali", "Patty", "1, 3, 4"], ["Fazlul", "Bengali", "Patty", "1–4"], ["Chhottu", "Marathi", "Cake", "2, 4"],
             ["Eshan", "Punjabi", "Cake", "1, 3"], ["Dildaar", "Punjabi", "Cookies", "1, 3"],
             ]) + p("Bread: one of Baali and Giri is Punjabi and bakes in hours 1 and 3; the other is Marathi and bakes in hours 2 and 4.")
P.dilr_set(2, "Set 2 — Four hours in a bakery kitchen", DIR,
 p("A bakery sells only what it makes that day. All baking happens between 5 am and 9 am, in four production hours: the 1st (5–6 am), 2nd, 3rd and 4th (8–9 am). Seven bakers — Anu, Baali, Chhottu, Dildaar, Eshan, Fazlul and Giri — work in the kitchen. Each baker makes only one of four items (cake, bread, patty or cookies), and makes 10 units of it in every hour he works. Every baker works at least one hour. Each baker is Bengali, Punjabi or Marathi.") +
 p("The table gives the units of each item made in each hour (blank where not known).") + UNITS + p("At least one Marathi baker worked in the 2nd hour and in the 4th hour; no Marathi baker worked in the 1st or 3rd hour.") +
 p("The 1st and 3rd hours produced the same number of units in all. The 4th hour produced fewer than these, and the 2nd hour the fewest of all. Also:") +
 "<ol><li>All Punjabi bakers worked in exactly the same hours.</li>"
 "<li>No two Marathi bakers make the same item; nor do any two Punjabi bakers.</li>"
 "<li>Anu is Bengali and worked in exactly three hours.</li>"
 "<li>Chhottu is Marathi; he makes cakes and worked in exactly two hours.</li>"
 "<li>Eshan does not make cookies, and his group differs from Fazlul’s. Fazlul worked in all four hours.</li>"
 "<li>Baali never worked in two consecutive hours, and neither did Giri. They make the same item but never worked in the same hour.</li>"
 "<li>In any hour, everyone making cake or bread was from the same group.</li>"
 "<li>Patty is made only by Bengalis, and cookies only by Punjabis.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Hour totals", p("From the table, hour 2 makes 30 units, hour 4 makes 40 and hour 3 makes 50. Hour 1 must also make 50, so its patty and cookies add up to 30. Hours 1 and 3 therefore have five bakers each, hour 2 three and hour 4 four.")),
       ("Hours 2 and 4", p("A Marathi works in each, and Marathis can only make cake or bread. By fact 7 the cake and bread makers of that hour are then all Marathi. Chhottu can work only in these hours, so his are hours 2 and 4. No two Marathis share an item, so one Marathi makes the bread in both hours; call him M.")),
       ("Patty makers", p("Hour 2 has only three bakers: Chhottu, M and the patty maker, who must be Fazlul (he works every hour). So Fazlul makes patty and is Bengali. Anu works three hours but not hour 2, so hours 1, 3 and 4; in hour 4 the only free job is patty, so Anu makes patty too.")),
       ("Hours 1 and 3", p("Besides Anu and Fazlul, each of these hours needs three more bakers (cake, bread and one more). The three bakers other than M among Baali, Dildaar, Eshan and Giri work only in hours 1 and 3, so each works both. Baali and Giri never work together, so one of them is M; the other makes bread in hours 1 and 3. Eshan does not make cookies, so he makes the cake and Dildaar makes cookies (in hour 3, and so in hour 1).")),
       ("Groups", p("Dildaar is Punjabi (cookies). Eshan is not Bengali (Fazlul is) and no Marathi works in hours 1 and 3, so Eshan is Punjabi, and by fact 7 so is the hours-1-and-3 bread maker.") + TWO)) +
 final("Everything is fixed except which of Baali and Giri is the Punjabi and which the Marathi."),
 p("Start from the hours with a Marathi: in them, cake and bread must both be Marathi."),
 p("<b>Same-group rules:</b> one known member of a group pins the group of everyone tied to him."))
P.dq(6, "Which group does Baali belong to?", ["Bengali", "Marathi", "Punjabi", "Punjabi or Marathi"], "MCQ", "4", "Medium",
 "Baali and Giri split the bread between hours 1, 3 and hours 2, 4.",
 steps(("Two cases", p("Whoever bakes in hours 2 and 4 is Marathi; the other is Punjabi. Either can be Baali."))) + final("Option 4"),
 [("1", "Bread is never Bengali here."), ("2", "Possible, but not certain."), ("3", "Possible, but not certain.")])
P.dq(7, "Which pair is the odd one out?", ["Anu and Fazlul", "Giri and Chhottu", "Baali and Dildaar", "Baali and Eshan"], "MCQ", "1", "Medium",
 "In which pair are both groups certain?",
 steps(("Pairs", p("Anu and Fazlul are both Bengali for sure. In each other pair, the two may or may not share a group, depending on how Baali and Giri are split."))) + final("Option 1"),
 [("2", "Same group only if Giri is Marathi."), ("3", "Same group only if Baali is Punjabi."), ("4", "Same group only if Baali is Punjabi.")])
P.dq(8, "Which of these is not possible?", ["Anu did not work in the 2nd hour.", "Neither Anu nor Baali made cookies.", "Giri and Eshan are from the same group.", "Baali made cake."], "MCQ", "4", "Easy",
 "Baali makes bread.",
 steps(("Check", p("Anu works in hours 1, 3, 4; cookies are Dildaar’s; Giri can be Punjabi like Eshan. But Baali makes bread, never cake."))) + final("Option 4"),
 [("1", "True."), ("2", "True."), ("3", "Possible when Giri is Punjabi.")])
P.dq(9, "Which of these definitely happened in one and the same hour?", ["A Marathi made bread while two Bengalis made patty.", "Bakers of all three groups worked together.", "A Punjabi made cake while exactly one Bengali made patty.", "A Marathi made bread while Dildaar and Giri both worked."], "MCQ", "1", "Medium",
 "Look at hour 4.",
 steps(("Hour 4", p("A Marathi makes bread while Anu and Fazlul make patty.")),
       ("Others", p("Hours 1 and 3 have no Marathi; hours 2 and 4 have no Punjabi. Eshan’s cake hours have two patty makers. Dildaar works only when no Marathi does."))) + final("Option 1"),
 [("2", "Never: Marathis and Punjabis work in different hours."), ("3", "Eshan’s hours have two patty makers."), ("4", "Dildaar works in hours 1 and 3, without Marathis.")])
P.dq(10, "For how many bakers can the group be found with certainty?", [], "TITA", "5", "Easy",
 "Only Baali and Giri are open.",
 steps(("Count", p("Anu, Fazlul, Chhottu, Eshan and Dildaar: 5."))) + final("5"))

# ---------------- Set 3: Mines on a grid (Q11–15) ----------------
DONE = table(["", "C1", "C2", "C3", "C4", "C5"],
             [["R1", "✱", "1", "1", "1", "1"], ["R2", "2", "2", "2", "✱", "1"], ["R3", "1", "✱", "3", "2", "1"],
              ["R4", "1", "2", "✱", "2", "1"], ["R5", "0", "1", "1", "2", "✱"]])
P.dilr_set(3, "Set 3 — Five hidden mines", DIR,
 p("Five mines are hidden in a 5 × 5 grid of cells, with exactly one mine in each row and exactly one in each column. The rows are R1 to R5 from top to bottom and the columns C1 to C5 from left to right.") +
 p("Every cell without a mine has a number written in it: the number of mines among the (up to eight) cells touching it along a side or at a corner. Only some of the numbers are shown below; each blank cell holds either a mine or a number.") + F.GRID,
 "DILR::LR::Puzzles",
 steps(("Around R3C3", p("R3C3 shows 3. Of its eight neighbours, R2C2, R2C3, R3C4, R4C2 and R4C4 hold numbers, so the three mines must be R2C4, R3C2 and R4C3.")),
       ("Two left", p("The remaining mines are in rows 1 and 5 and columns 1 and 5: either R1C1 and R5C5, or R1C5 and R5C1.")),
       ("Decide", p("R2C2 shows 2. Its neighbours already include the mine at R3C2; the second must be R1C1. So the mines are R1C1 and R5C5.") + DONE)) +
 final("✱ marks a mine. Every number is now known."),
 p("A number whose blank neighbours are exactly as many as its value forces all of them."),
 p("<b>One per row and column:</b> once three mines are fixed, the other two can only go in two ways."))
P.dq(11, "Of the 20 cells holding numbers, in how many can the number be determined?", [], "TITA", "20", "Easy",
 "The mines are fixed.",
 steps(("All", p("With all five mines known, every number can be counted."))) + final("20"))
P.dq(12, "For how many of the five mines can the cell be determined?", ["5", "4", "3", "2"], "MCQ", "1", "Easy",
 "R2C2 settles the last two.",
 steps(("All", p("R1C1, R2C4, R3C2, R4C3 and R5C5."))) + final("Option 1"),
 [("2", "All five are fixed."), ("3", "R2C2 fixes the corners too."), ("4", "All five are fixed.")])
P.dq(13, "What is in cell R5C4?", ["The number 1", "The number 2", "A mine", "It cannot be determined"], "MCQ", "2", "Easy",
 "Count its neighbours.",
 steps(("R5C4", p("Its neighbours R4C3 and R5C5 hold mines: 2."))) + final("Option 2"),
 [("1", "Misses one mine."), ("3", "Row 5’s mine is in C5."), ("4", "The grid is fixed.")])
P.dq(14, "How many cells have 1 written in them?", ["9", "11", "12", "Cannot be determined"], "MCQ", "2", "Easy",
 "Count the 1s in the finished grid.",
 steps(("Count", p("Row 1: four; row 2: one; row 3: two; row 4: two; row 5: two. Total 11."))) + final("Option 2"),
 [("1", "Miscount."), ("3", "Miscount."), ("4", "The grid is fixed.")])
P.dq(15, "How many of the mines touch at least one other mine, along a side or at a corner?", ["0", "2", "3", "Cannot be determined"], "MCQ", "2", "Easy",
 "Check each pair.",
 steps(("Pairs", p("R3C2 and R4C3 touch at a corner. No other two mines touch (R2C4 and R3C2 are two columns apart, as are R4C3 and R5C5). So 2 mines."))) + final("Option 2"),
 [("1", "R3C2 and R4C3 touch."), ("3", "R2C4 touches no mine."), ("4", "The grid is fixed.")])

# ---------------- Set 4: A painted gold block (Q16–20) ----------------
P.dilr_set(4, "Set 4 — Cutting a painted gold block", DIR,
 p("A professor finds a solid block of gold in an old ruin. It is a cuboid measuring 35 cm × 55 cm × 65 cm. He paints three faces that meet at one corner red. Of the other three faces, he paints the smallest green and the second largest blue; the remaining face, one of the two largest, is left unpainted (gold). The block is then cut into identical cubes, as large as possible, with no gold wasted.") +
 p("In the questions, gold does not count as a colour."),
 "DILR::LR::Puzzles",
 steps(("Cube size", p("HCF(35, 55, 65) = 5, so the cubes are 5 cm: 7 × 11 × 13 = 1001 of them.")),
       ("Faces", p("Faces 11 × 13 (largest): one red, one gold. Faces 7 × 13: one red, one blue. Faces 7 × 11 (smallest): one red, one green.")),
       ("Picture it", p("Use layers 1–7, rows 1–11, columns 1–13. Red: layer 1, row 1, column 1. Blue: row 11. Green: column 13. Layer 7 is gold.")),
       ("Unpainted", p("Cubes off every coloured face: layers 2–7, rows 2–10, columns 2–12: 6 × 9 × 11 = 594."))) +
 final("Count the cubes by which painted planes they lie on."),
 p("Count the cubes with no colour first; everything else touches at least one painted face."),
 p("<b>Painted-cube counts:</b> a cube’s colours are the painted faces it lies on; work face by face, then subtract overlaps."))
P.dq(16, "How many cubes have exactly two different colours?", [], "TITA", "40", "Hard",
 "Two colours means lying on two differently coloured faces.",
 steps(("Edges", p("Leaving out corner cubes, an edge has 5, 9 or 11 cubes. The edges where two different colours meet are red–blue along 11 and 5 cubes, red–green along 9 and 5, and blue–green along 5: 35 cubes.")),
       ("Corners", p("Of the eight corners, five touch exactly two colours (red and green, red and blue twice each, and blue and green); one touches red, blue and green; two are red only.")),
       ("Total", p("35 + 5 = 40."))) +
 final("40"))
P.dq(17, "How many cubes have only one colour?", ["366", "365", "364", "360"], "MCQ", "1", "Hard",
 "One colour can still be on two faces (two red faces).",
 steps(("Coloured", p("1001 − 594 = 407 cubes have some colour.")),
       ("Subtract", p("40 have two colours and one corner has three: 407 − 40 − 1 = 366."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Leaves out cubes red on two faces.")])
P.dq(18, "How many cubes have colour on exactly one face?", ["333", "336", "339", "345"], "MCQ", "3", "Hard",
 "Inner parts of the coloured faces, plus edge cubes that touch only one coloured face.",
 steps(("Face interiors", p("Red 11 × 13 face: 9 × 11 = 99; red 7 × 13: 5 × 11 = 55; red 7 × 11: 5 × 9 = 45; blue 7 × 13: 55; green 7 × 11: 45. Total 299.")),
       ("Edges by the gold face", p("Where a coloured face meets the gold face, the edge cubes touch one coloured face only: 11 (red), 9 (red), 11 (blue) and 9 (green): 40.")),
       ("Total", p("299 + 40 = 339."))) + final("Option 3"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(19, "How many cubes have no colour?", [], "TITA", "594", "Medium",
 "Peel off one layer from each coloured face.",
 steps(("Inner block", p("Five faces are coloured; only the gold face keeps its layer: (7 − 1) × (11 − 2) × (13 − 2) = 6 × 9 × 11 = 594."))) + final("594"))
P.dq(20, "How many cubes have red or blue, but no green?", ["270", "290", "310", "330"], "MCQ", "4", "Medium",
 "Coloured cubes minus green cubes.",
 steps(("Coloured", p("407.")), ("Green", p("The green face has 7 × 11 = 77 cubes.")), ("Answer", p("407 − 77 = 330."))) + final("Option 4"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])
