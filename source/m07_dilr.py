# -*- coding: utf-8 -*-
# Simp Mock 7: DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m07 import P
import m07_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: A cube of coloured cubes (Q1–5) ----------------
P.dilr_set(1, "Set 1 — A cube built from coloured cubes", DIR,
 p("Reshmi builds a large cube from 125 identical small opaque cubes of different colours, glued together. She first draws a 5 × 5 grid of squares, each the size of one face of a small cube, and numbers them as shown: 1 to 25, starting at the bottom-left and going left to right along each row, then upward.") + F.CUBEGRID +
 p("She places 25 small cubes on a flat surface in exactly the colour pattern of the grid (a pink cube in the bottom-left corner, a blue cube to its right, a green cube in the top-right corner with a red cube to its left, and so on). She then builds four more layers with exactly the same pattern on top. The five layers form the large cube."),
 "DILR::LR::Puzzles",
 steps(("Visibility", p("A square on the edge of the grid (1–6, 10, 11, 15, 16, 20–25) gives a visible cube in every one of the 5 layers. An inner square (7–9, 12–14, 17–19) is visible only in the top and bottom layers.")),
       ("Corners", p("The large cube’s 8 corners come from squares 1, 5, 21 and 25 in the top and bottom layers: pink, yellow, blue and green.")),
       ("Turning the cube", p("Turned onto a side, a horizontal layer is one row or column of the grid repeated 5 times. Every row and column has at most two squares of one colour."))) +
 final("Use edge squares × 5 and inner squares × 2."),
 p("Every vertical column of the large cube repeats one square’s colour five times."),
 p("<b>Layered solids:</b> count square by square — an edge square contributes 5 visible cubes, an inner square 2."))
P.dq(1, "How many red small cubes can be seen from outside the large cube?", [], "TITA", "19", "Medium",
 "Red squares: 4, 6, 24 (edge) and 13, 17 (inner).",
 steps(("Count", p("3 edge squares × 5 + 2 inner squares × 2 = 15 + 4 = 19."))) + final("19"))
P.dq(2, "How many pink small cubes that touch a yellow small cube (face to face) can be seen from outside?", [], "TITA", "17", "Medium",
 "Pink squares: 1, 10, 11, 19, 23. Which touch a yellow square?",
 steps(("Pink next to yellow", p("10 (next to 5), 11 (next to 12), 19 (next to 20) and 23 (next to 22). Square 1 touches only blue and red.")),
       ("Count", p("Edge squares 10, 11, 23: 3 × 5 = 15. Inner square 19: 2. Total 17."))) + final("17"))
P.dq(3, "Both diagonals are drawn on each of the six faces of the large cube. They pass through the outer faces of 38 small cubes. Which colour is most common among these 38 cubes?", ["Blue", "Red", "Pink", "Yellow"], "MCQ", "2", "Hard",
 "Top and bottom faces show the grid; side faces show one edge row or column repeated.",
 steps(("Count", p("Going face by face and counting each cube once: red 10, blue 9, pink 8, yellow 6, green 5.")),
       ("Most", p("Red."))) + final("Option 2"),
 [("1", "9."), ("3", "8."), ("4", "6.")])
P.dq(4, "Which colour is missing among the small cubes with at least three faces visible?", ["Blue", "Green", "Pink", "Red"], "MCQ", "4", "Easy",
 "Only the 8 corner cubes show three faces.",
 steps(("Corners", p("Squares 1, 5, 21, 25: pink, yellow, blue, green. No red."))) + final("Option 4"),
 [("1", "Square 21."), ("2", "Square 25."), ("3", "Square 1.")])
P.dq(5, "The large cube can rest on any of its 6 faces. In any position it has 5 horizontal layers. What is the largest number of small cubes of one colour that can lie in a single horizontal layer, over all positions?", ["1", "5", "10", "Cannot be uniquely determined"], "MCQ", "3", "Medium",
 "Standing upright, a layer is the whole grid; on its side, a layer is one row or column × 5.",
 steps(("Upright", p("A layer is the grid itself: at most 5 of one colour (red or pink).")),
       ("On its side", p("A layer is a row or column repeated 5 times. Column 1 has two pinks (1, 11): 10 cubes. No row or column has three of one colour.")),
       ("Largest", p("10."))) + final("Option 3"),
 [("1", "Too few."), ("2", "Upright only."), ("4", "It is fixed.")])

# ---------------- Set 2: A grocery store's sales (Q6–10) ----------------
S21 = table(["Subcategory", "2021"], [["Detergents", "10"], ["Soaps", "18"], ["Personal Hygiene", "12"], ["Baby Foods", "10"], ["Cereals", "16"],
                                      ["Oils & Spices", "14"], ["Dairy", "15"], ["Beverages", "18"], ["Bread & Spreads", "5"], ["Freezer", "12"]])
S22 = table(["Subcategory", "Growth", "2022"], [["Detergents", "23%", "12.3"], ["Soaps", "15%", "20.7"], ["Pers. Hygiene", "25%", "15"],
                                                ["Baby Foods", "30%", "13"], ["Cereals", "25%", "20"], ["Oils & Spices", "7 1/7 %", "15"],
                                                ["Dairy", "8%", "16.2"], ["Beverages", "18 1/3 %", "21.3"], ["Bread & Spr.", "10%", "5.5"], ["Freezer", "25%", "15"]])
P.dilr_set(2, "Set 2 — Sales growth in a grocery store", DIR,
 p("A medium-sized grocery store sells ten subcategories of products in three categories. Detergents, Soaps and Personal Hygiene are <b>Non-perishable</b> (N); Baby Foods, Cereals, and Oils &amp; Spices are <b>Kitchen Items</b> (K); Dairy, Beverages, Bread &amp; Spreads and Freezer are <b>Processed Items</b> (P). The table gives 2021 sales in ₹ lakh.") + S21 +
 p("The bars show each subcategory’s growth in sales in 2022 over 2021, in per cent. Within each category the bars are in ascending order, so they do not show which subcategory is which.") + F.GROWTH +
 "<ol><li>The overall growth in per cent is the same for exactly two of the three categories.</li>"
 "<li>The growth in ₹ lakh is the same for all three categories.</li>"
 "<li>Personal Hygiene, Freezer and Baby Foods grew by the same amount in ₹ lakh.</li></ol>",
 "DILR::DI::Graphs_and_Charts",
 steps(("Category totals", p("2021: N 40, K 40, P 50.")),
       ("Equal growths", p("Personal Hygiene and Freezer both sold 12 in 2021 and grew by the same amount, so they grew by the same percentage: the only one common to N and P is 25%. Each grew by ₹3 lakh, so Baby Foods (10) grew by 3: 30%.")),
       ("Kitchen and Non-perishable", p("Cereals and Oils take 25% and 7 1/7 %: Cereals 25% and Oils 7 1/7 % add 4 + 1 = 5, total 8; the other way gives 7.64. Detergents and Soaps take 23% and 15%: Detergents 23%, Soaps 15% add 2.3 + 2.7 = 5, total 8; the other way gives 8.64.")),
       ("Processed", p("The three growths must match at ₹8 lakh. Processed needs 5 more from Dairy, Beverages and Bread at 8%, 10% and 18 1/3 %: Dairy 8% (1.2), Beverages 18 1/3 % (3.3), Bread 10% (0.5).") + S22)) +
 final("Growth ₹8 lakh in each category; 2022 total ₹154 lakh."),
 p("Equal ₹ growth on equal 2021 sales means equal percentage growth: that pins Personal Hygiene and Freezer first."),
 p("<b>Unlabelled bars:</b> use ‘same amount’ clues to match bars to items, then check the category totals."))
P.dq(6, "What is the range of the subcategories’ 2022 sales (in ₹ lakh)? (Range = highest − lowest.)", ["14.8", "15.8", "16.4", "17.1"], "MCQ", "2", "Medium",
 "Highest Beverages, lowest Bread.",
 steps(("Range", p("21.3 − 5.5 = 15.8."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(7, "How many subcategories had 2022 sales above the 2022 average per subcategory?", [], "TITA", "4", "Medium",
 "Average = 154 ÷ 10 = 15.4.",
 steps(("Above 15.4", p("Beverages 21.3, Soaps 20.7, Cereals 20, Dairy 16.2."))) + final("4"))
P.dq(8, "Which pair, one from Processed and one from Kitchen Items, grew by the same percentage?", ["Dairy and Baby Foods", "Freezer and Cereals", "Beverages and Oils & Spices", "Beverages and Baby Foods"], "MCQ", "2", "Medium",
 "Look for 25% in both.",
 steps(("Both 25%", p("Freezer and Cereals."))) + final("Option 2"),
 [("1", "8% and 30%."), ("3", "18 1/3 % and 7 1/7 %."), ("4", "18 1/3 % and 30%.")])
P.dq(9, "Which correctly orders the growth in sales (in ₹ lakh) from 2021 to 2022?", ["Dairy > Detergents > Oils & Spices", "Soaps > Baby Foods > Oils & Spices", "Beverages > Soaps > Bread & Spreads", "Cereals > Detergents > Freezer"], "MCQ", "3", "Medium",
 "Compare ₹ growths.",
 steps(("Growths", p("Beverages 3.3, Soaps 2.7, Bread 0.5: correct. (Dairy 1.2 < Detergents 2.3; Soaps 2.7 < Baby Foods 3; Detergents 2.3 < Freezer 3.)"))) + final("Option 3"),
 [("1", "Dairy grew less than Detergents."), ("2", "Soaps grew less than Baby Foods."), ("4", "Detergents grew less than Freezer.")])
P.dq(10, "By what percentage did 2022 sales of Processed Items exceed those of Kitchen Items?", [r"\(17\tfrac{7}{29}\)", r"\(20\tfrac{5}{6}\)", r"\(28\tfrac{1}{3}\)", r"\(31\tfrac{3}{11}\)"], "MCQ", "2", "Medium",
 "Both categories grew by 8.",
 steps(("2022", p("Processed 58, Kitchen 48.")), ("Percentage", p("10 ÷ 48 = 20 5/6 %."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

# ---------------- Set 3: Blindfolded friends on a grid (Q11–15) ----------------
CASE_A = "<ul><li>Raju: north-east corner, facing east.</li><li>Bittu: 2nd column, 2nd row from the top, facing north.</li><li>Pappu: 3rd column, bottom row, facing west.</li><li>Meera: 1st column, 3rd row from the top, facing south.</li></ul>"
P.dilr_set(3, "Set 3 — Four blindfolded friends on a grid", DIR,
 p("Five friends — Rudra, Raju, Bittu, Pappu and Meera — enter a large room with a 4 × 4 grid of squares (‘cells’) marked on the floor. Raju, Bittu, Pappu and Meera each stand completely inside a different cell, no two in the same row or the same column, and the four face four different directions: north, south, east and west. Rudra stands outside the grid, watching.") +
 p("Everyone except Rudra is blindfolded, so none of the four knows his or her actual direction; each was told separately that they are facing north. They then said (each using the directions as they believe them to be):") +
 "<ul><li>Raju: ‘There are three cells to my east, all empty. The same is true to my south.’</li>"
 "<li>Bittu: ‘There is exactly one cell to my north, and it is empty; the same is true to my west.’</li>"
 "<li>Pappu: ‘Start from my cell, go one cell north and then two cells east, and you reach Bittu’s cell.’</li></ul>",
 "DILR::LR::Puzzles",
 steps(("In each person’s own frame", p("Raju is in a corner, with the grid ahead of him to his right and behind. Bittu is one cell in from the edge in front of him and one in from the edge on his left. From Pappu, Bittu is one cell forward and two to the right.")),
       ("Rotations", p("Each person’s ‘north’ is the way they actually face. Trying the four facings for each, with no two friends sharing a row or column and all facings different, leaves a few layouts. Rudra’s extra statement in each question picks one.")),
       ("Rudra’s first statement", p("Walking the diagonal from the south-west corner to the north-east corner meets only one friend, at the north-east corner:") + CASE_A)) +
 final("Each Rudra statement fixes one layout."),
 p("Turn each statement into a picture relative to the speaker, then rotate the picture four ways."),
 p("<b>Hidden orientation:</b> a statement made in a person’s own frame fixes the shape; the true direction fixes the rotation."))
RUDRA1 = "Rudra says: ‘If I walk diagonally from the south-west corner cell to the north-east corner cell, I meet only one friend on the way, in the north-east corner cell.’ "
RUDRA2 = "Rudra says: ‘If I walk diagonally from the south-east corner cell to the north-west corner cell, I meet only two friends on the way — one in the starting cell and one in the end cell, and the one in the end cell is facing east.’ "
P.dq(11, RUDRA1 + "Who is facing west?", ["Bittu", "Meera", "Pappu", "Raju"], "MCQ", "3", "Medium",
 "Use the layout fixed by Rudra’s statement.",
 steps(("Layout", p("Raju (NE corner) east, Bittu north, Pappu west, Meera south."))) + final("Option 3"),
 [("1", "North."), ("2", "South."), ("4", "East.")])
P.dq(12, RUDRA1 + "How do you get from Meera’s cell to Pappu’s cell, using true directions?", ["One cell north, then two cells west", "One cell south, then two cells east", "One cell east, then two cells north", "One cell west, then two cells south"], "MCQ", "2", "Medium",
 "Meera is in column 1, row 3 from the top; Pappu in column 3, bottom row.",
 steps(("Move", p("One row down (south) and two columns right (east)."))) + final("Option 2"),
 [("1", "Wrong way."), ("3", "Wrong way."), ("4", "Wrong way.")])
P.dq(13, RUDRA1 + "Where does Bittu end up if he moves one cell west and then one cell north (true directions)?", ["North-west corner", "North-east corner", "South-west corner", "South-east corner"], "MCQ", "1", "Medium",
 "Bittu is in column 2, row 2 from the top.",
 steps(("Move", p("West to column 1, north to the top row: the north-west corner."))) + final("Option 1"),
 [("2", "Wrong corner."), ("3", "Wrong corner."), ("4", "Wrong corner.")])
P.dq(14, RUDRA2 + "Who is facing north?", ["Bittu", "Meera", "Pappu", "Raju"], "MCQ", "2", "Medium",
 "Now Raju is in the south-east corner and Pappu in the north-west corner.",
 steps(("Layout", p("Raju (SE corner) south, Pappu (NW corner) east, Bittu (column 2, row 3 from the top) west, Meera (column 3, row 2 from the top) north."))) + final("Option 2"),
 [("1", "West."), ("3", "East."), ("4", "South.")])
P.dq(15, RUDRA2 + "How do you get from Bittu’s cell to Pappu’s cell, using true directions?", ["One cell north, then two cells west", "Two cells north, then one cell west", "One cell east, then two cells north", "One cell west, then one cell north"], "MCQ", "2", "Medium",
 "Bittu: column 2, row 3 from the top. Pappu: NW corner.",
 steps(("Move", p("Up two rows (north), left one column (west)."))) + final("Option 2"),
 [("1", "Swapped counts."), ("3", "Wrong direction."), ("4", "Too short.")])

# ---------------- Set 4: A courier network (Q16–20) ----------------
HUBS = p("<b>North zone</b> (hub: PDPs)") + '<ul><li><b>Hilly</b>: Darjeeling, Kalimpong, Siliguri</li><li><b>Dooars</b>: Jalpaiguri, Alipurduar, Cooch Behar</li><li><b>Dinajpur</b>: Raiganj, Balurghat</li><li><b>Malda</b>: Malda, Gour</li></ul>' + p("<b>South zone</b>") + '<ul><li><b>Murshidabad</b>: Berhampore, Jangipur, Lalbagh</li><li><b>Nadia</b>: Krishnanagar, Nabadwip, Kalyani</li><li><b>Central Districts</b>: Bardhaman, Asansol, Durgapur</li><li><b>West Border</b>: Purulia, Bankura, Jhargram</li><li><b>Medinipur</b>: Midnapore, Kharagpur, Haldia</li><li><b>Kolkata</b>: Kolkata, Howrah</li></ul>'
P.dilr_set(4, "Set 4 — A courier company’s hubs", DIR,
 p("WBL is a courier company that delivers anywhere within a state in 24 hours. The state has two zones, North and South. WBL has 10 hubs, each serving 2 to 4 pick-and-drop points (PDPs) — the main towns in its area. There are 27 PDPs in all.") + HUBS +
 p("Every PDP is served at least twice a day (morning and evening) by the intra-hub vehicle of its own hub only. WBL keeps one dedicated inter-hub vehicle for every pair of hubs and one dedicated intra-hub vehicle for each hub. For example, a parcel from Kalimpong to Purulia goes by Hilly’s intra-hub vehicle to Hilly, by the Hilly–West Border vehicle to West Border, and by West Border’s intra-hub vehicle to Purulia."),
 "DILR::LR::Routes_and_Networks",
 steps(("Vehicles", p("10 intra-hub vehicles + one for each of C(10, 2) = 45 hub pairs = 55.")),
       ("Route = vehicles", p("A parcel uses the source hub’s intra-hub vehicle, one inter-hub vehicle for each leg between hubs, and the destination hub’s intra-hub vehicle."))) +
 final("Each question changes the rules; recount with C(n, 2)."),
 p("Count vehicles as intra-hub (one per hub) plus inter-hub (one per linked pair)."),
 p("<b>Complete graphs:</b> n hubs, all linked in pairs, need C(n, 2) links."))
P.dq(16, "How many vehicles does WBL maintain?", [], "TITA", "55", "Easy",
 "Intra-hub plus one per pair.",
 steps(("Count", p("10 + 45 = 55."))) + final("55"))
P.dq(17, "WBL restructures: Medinipur’s 3 PDPs move to Kolkata hub; Nadia’s and West Border’s PDPs move to Central Districts; Dinajpur’s and Murshidabad’s PDPs move to Malda. Everything else stays the same. Each hub with more than 5 PDPs after this gets one extra intra-hub vehicle, and Kolkata also gets one extra because of its workload. All other vehicles are discarded. How many vehicles are discarded?", [], "TITA", "37", "Medium",
 "Five hubs remain.",
 steps(("New hubs", p("Kolkata 5, Central Districts 9, Malda 7, Hilly 3, Dooars 3.")),
       ("Vehicles kept", p("5 intra-hub + C(5, 2) = 10 inter-hub + extra for Central Districts, Malda and Kolkata = 18.")),
       ("Discarded", p("55 − 18 = 37."))) + final("37"))
RULES = ("<ol><li>Every hub has a direct link with Kolkata hub (this overrides the rules below).</li>"
         "<li>Malda, Murshidabad and Nadia are directly linked with each other.</li>"
         "<li>West Border and Medinipur are each directly linked with Central Districts; apart from Kolkata, they have no other direct link.</li>"
         "<li>Dinajpur is directly linked with Malda and with Hilly; apart from Kolkata, it has no other direct link.</li>"
         "<li>Dooars is directly linked with Hilly; apart from Kolkata, it has no other direct link.</li>"
         "<li>No other pair of hubs is directly linked.</li>"
         "<li>A parcel always goes by a route through the fewest hubs. If its source and destination hubs are in the same zone, it stays in that zone unless leaving the zone uses fewer hubs.</li></ol>")
P.dq(18, "WBL changes its rules: a vehicle is kept only for each directly linked pair of hubs, plus one intra-hub vehicle per hub. The links are:" + RULES + "How many vehicles does WBL now maintain?", ["25", "26", "27", "28"], "MCQ", "3", "Medium",
 "Count the links.",
 steps(("Links", p("9 with Kolkata; Malda–Murshidabad, Malda–Nadia, Murshidabad–Nadia, West Border–Central Districts, Medinipur–Central Districts, Dinajpur–Malda, Dinajpur–Hilly, Dooars–Hilly: 8 more.")),
       ("Total", p("10 + 9 + 8 = 27."))) + final("Option 3"),
 [("1", "Misses two links."), ("2", "Misses one link."), ("4", "Counts one too many.")])
P.dq(19, "Under the rules of the previous question, how many different vehicles carry a parcel from Gour to Alipurduar?", ["3", "4", "5", "6"], "MCQ", "2", "Medium",
 "Malda to Dooars: through Kolkata or through Dinajpur and Hilly?",
 steps(("Route", p("Malda–Kolkata–Dooars passes 3 hubs; staying in the North (Malda–Dinajpur–Hilly–Dooars) needs 4, so it goes via Kolkata.")),
       ("Vehicles", p("Malda intra, Malda–Kolkata, Kolkata–Dooars, Dooars intra: 4."))) + final("Option 2"),
 [("1", "Leaves out an intra-hub vehicle."), ("3", "Uses the longer northern route."), ("4", "Too many.")])
P.dq(20, "Under the same rules, which route (hubs only) is valid?", ["Cooch Behar to Purulia: Dooars–Hilly–Kolkata–West Border", "Balurghat to Jangipur: Dinajpur–Malda–Murshidabad", "Bankura to Nabadwip: West Border–Central Districts–Kolkata–Nadia", "Siliguri to Malda: Hilly–Kolkata–Malda"], "MCQ", "2", "Medium",
 "Fewest hubs, and stay in zone when it is no longer.",
 steps(("1", p("Dooars–Kolkata–West Border is shorter.")), ("2", p("Three hubs, the fewest possible.")),
       ("3", p("West Border–Kolkata–Nadia is shorter.")), ("4", p("Hilly–Dinajpur–Malda is just as short and stays in the North zone."))) + final("Option 2"),
 [("1", "A shorter route exists."), ("3", "A shorter route exists."), ("4", "Must stay in the North zone.")])
