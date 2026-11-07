# -*- coding: utf-8 -*-
# Batch 11 — CAT 2020 Slot 1: DILR (sets 1, 2, 4, 5; set 3, Q11–14, isn't in the source).
from fmt import steps, final, trap, why, table, p
from b11_20s1 import P

# ---------------- Set 1: Board examination ----------------
MARKS = table(["", "English", "Hindi", "Mathematics", "Science", "Social Science"],
              [["Alva", "80", "75", "70", "75", "60"], ["Bithi", "90", "80", "55", "85", "85"], ["Carl", "75", "80", "90", "100", "90"],
               ["Deep", "70", "90", "100", "90", "80"], ["Esha", "80", "85", "95", "60", "55"], ["Foni", "83", "72", "78", "88", "83"]])
P.dilr_set(1, "Set 1 — Missed board examinations", "Read the following passage carefully and answer the questions that follow.",
 p("In a certain board examination, students were to appear for examination in five subjects: English, Hindi, Mathematics, Science and Social Science. Due to a certain emergency situation, a few of the examinations could not be conducted for some students. Hence, some students missed one examination and some others missed two examinations. Nobody missed more than two examinations.") +
 p("The board adopted the following policy for awarding marks to students. If a student appeared in all five examinations, then the marks awarded in each of the examinations were on the basis of the scores obtained by them in those examinations.") +
 p("If a student missed only one examination, then the marks awarded in that examination was the average of the best three among the four scores in the examinations they appeared for.") +
 p("If a student missed two examinations, then the marks awarded in each of these examinations was the average of the best two among the three scores in the examinations they appeared for.") +
 p("The marks obtained by six students in the examination are given in the table below. Each of them missed either one or two examinations.") + MARKS +
 p("The following facts are also known.") +
 "<ol type=\"I\"><li>Four of these students appeared in each of the English, Hindi, Science, and Social Science examinations.</li><li>The student who missed the Mathematics examination did not miss any other examination.</li><li>One of the students who missed the Hindi examination did not miss any other examination. The other students who missed the Hindi examination also missed the Science examination.</li></ol>",
 "DILR::LR::Analytical_Reasoning",
 steps(("How many misses", p("English, Hindi, Science and Social Science were each missed by 2 students; Mathematics by exactly 1. That is 9 missed exams among 6 students, each missing 1 or 2: so 3 students missed one and 3 missed two.")),
       ("Which marks could be awarded ones", p("For each student, test whether a mark equals the right average of the others.") +
          table(["Student", "Possible missed exams"],
                [["Alva", "Hindi and/or Science (75)"], ["Bithi", "Science and/or Social Science (85)"], ["Carl", "Mathematics and/or Social Science (90)"],
                 ["Deep", "Hindi and/or Science (90)"], ["Esha", "English only (80)"], ["Foni", "English and/or Social Science (83)"]])),
       ("Fixing it", p("Only Carl could have missed Mathematics, and that student missed nothing else: Carl missed Mathematics only. English was missed by two, so Esha and Foni. Social Science by two: now only Bithi and Foni. Hindi by two: Alva and Deep, one of whom also missed Science (fact III). Science by two: Bithi and that one.") +
       table(["Student", "Missed"], [["Alva / Deep", "one missed Hindi only, the other Hindi and Science"], ["Bithi", "Science, Social Science"], ["Carl", "Mathematics"],
                                     ["Esha", "English"], ["Foni", "English, Social Science"]]))) +
 final("Everything is fixed except which of Alva and Deep also missed Science."),
 p("Test each mark against the averaging rule first. Most students turn out to have only one or two possible missed exams."),
 p("<b>Counting misses:</b> the totals per subject and the 1-or-2 rule fix how many students missed one exam and how many missed two."))
P.dq(1, "Who among the following did not appear for the Mathematics examination?", ["Alva", "Foni", "Esha", "Carl"], "MCQ", "4", "Medium",
 "Whose Mathematics mark equals the average of their best three others?",
 steps(("From the set solution", p("Carl’s 90 equals (100 + 90 + 80)/3. No one else fits."))) + final("Carl, option 4"),
 [("1", "Alva’s 70 doesn’t match an average."), ("2", "Foni’s 78 doesn’t match."), ("3", "Esha’s 95 doesn’t match.")])
P.dq(2, "Which students did not appear for the English examination?", ["Cannot be determined", "Carl and Deep", "Esha and Foni", "Alva and Bithi"], "MCQ", "3", "Medium",
 "Only two English marks can be awarded averages.",
 steps(("From the set solution", p("Esha (80) and Foni (83)."))) + final("Option 3"),
 [("1", "It can be determined."), ("2", "Their English marks aren’t averages."), ("4", "Their English marks aren’t averages.")])
P.dq(3, "What BEST can be concluded about the students who did not appear for the Hindi examination?", ["Alva and Deep", "Deep and Esha", "Alva and Esha", "Two among Alva, Deep and Esha"], "MCQ", "1", "Medium",
 "Whose Hindi mark can be an average?",
 steps(("From the set solution", p("Only Alva and Deep."))) + final("Option 1"),
 [("2", "Esha’s 85 isn’t an average."), ("3", "Esha’s 85 isn’t an average."), ("4", "It is exactly Alva and Deep.")])
P.dq(4, "What BEST can be concluded about the students who missed the Science examination?", ["Deep and Bithi", "Alva and Deep", "Alva and Bithi", "Bithi and one out of Alva and Deep"], "MCQ", "4", "Hard",
 "Fact III: one of the two Hindi-missers also missed Science.",
 steps(("From the set solution", p("Bithi, and whichever of Alva and Deep missed two exams."))) + final("Option 4"),
 [("1", "Could be Alva instead of Deep."), ("2", "Only one of them missed Science."), ("3", "Could be Deep instead of Alva.")])
P.dq(5, "How many out of these six students missed exactly one examination?", [], "TITA", "3", "Medium",
 "Nine misses among six students, one or two each.",
 steps(("From the set solution", p(r"\(a + b = 6\) and \(a + 2b = 9\), so 3 missed one exam."))) + final(r"\(3\)"))
P.dq(6, "For how many students can we be definite about which examinations they missed?", [], "TITA", "4", "Hard",
 "Only Alva and Deep are uncertain.",
 steps(("From the set solution", p("Bithi, Carl, Esha and Foni are fixed: 4."))) + final(r"\(4\)"))

# ---------------- Set 2: Musicians ----------------
P.dilr_set(2, "Set 2 — Ten percussionists", "Read the following passage carefully and answer the questions that follow.",
 p("Ten musicians (A, B, C, D, E, F, G, H, I and J) are experts in at least one of the following three percussion instruments: tabla, mridangam, and ghatam. Among them, three are experts in tabla but not in mridangam or ghatam, another three are experts in mridangam but not in tabla or ghatam, and one is an expert in ghatam but not in tabla or mridangam. Further, two are experts in tabla and mridangam but not in ghatam, and one is an expert in tabla and ghatam but not in mridangam.") +
 p("The following facts are known about these ten musicians.") +
 "<ol><li>Both A and B are experts in mridangam, but only one of them is also an expert in tabla.</li><li>D is an expert in both tabla and ghatam.</li><li>Both F and G are experts in tabla, but only one of them is also an expert in mridangam.</li><li>Neither I nor J is an expert in tabla.</li><li>Neither H nor I is an expert in mridangam, but only one of them is an expert in ghatam.</li></ol>",
 "DILR::LR::Venn_Diagrams",
 steps(("The groups", p("Tabla only 3, mridangam only 3, ghatam only 1, tabla + mridangam 2, tabla + ghatam 1.")),
       ("Placing people", p("D is the tabla + ghatam expert. The two tabla + mridangam experts are one of A/B and one of F/G; the other of A/B is mridangam only, the other of F/G tabla only. I plays neither tabla nor mridangam, so I is the ghatam-only expert, and H (not mridangam, not ghatam) is tabla only. J is not tabla and ghatam-only is taken, so J is mridangam only.")),
       ("C and E", p("One tabla-only and one mridangam-only place remain, so C and E take one each, in some order."))) +
 final("Fixed: D, H, I, J. Open: A/B, F/G, C/E."),
 p("Fill the single-place groups first (ghatam only, tabla + ghatam). They pin down D and I immediately."),
 p("<b>Fixed group sizes:</b> when the size of every group is given, each person placed shrinks the options for everyone else."))
P.dq(7, "Who among the following is DEFINITELY an expert in tabla but not in either mridangam or ghatam?", ["F", "A", "C", "H"], "MCQ", "4", "Medium",
 "H plays neither mridangam nor ghatam.",
 steps(("From the set solution", p("H is tabla only."))) + final("H, option 4"),
 [("1", "F might be tabla + mridangam."), ("2", "A plays mridangam."), ("3", "C could be mridangam only.")])
P.dq(8, "Who among the following is DEFINITELY an expert in mridangam but not in either tabla or ghatam?", ["B", "E", "J", "G"], "MCQ", "3", "Medium",
 "J plays no tabla, and the ghatam-only place is taken.",
 steps(("From the set solution", p("J is mridangam only."))) + final("J, option 3"),
 [("1", "B might also play tabla."), ("2", "E could be tabla only."), ("4", "G plays tabla.")])
P.dq(9, "Which of the following pairs CANNOT have any musician who is an expert in both tabla and mridangam but not in ghatam?", ["C and E", "F and G", "A and B", "C and F"], "MCQ", "1", "Medium",
 "Who fills the two tabla + mridangam places?",
 steps(("From the set solution", p("One of A/B and one of F/G. C and E are always single-instrument."))) + final("C and E, option 1"),
 [("2", "One of them is."), ("3", "One of them is."), ("4", "F could be.")])
P.dq(10, "If C is an expert in mridangam and F is not, then which are the three musicians who are experts in tabla but not in either mridangam or ghatam?", ["E, G and H", "E, F and H", "C, E and G", "C, G and H"], "MCQ", "2", "Medium",
 "C mridangam only makes E tabla only; F not mridangam makes F tabla only.",
 steps(("From the set solution", p("Tabla only: E, F and H. G is then tabla + mridangam."))) + final("E, F and H, option 2"),
 [("1", "G plays mridangam too."), ("3", "C is mridangam only."), ("4", "C is mridangam only, G plays mridangam too.")])

# ---------------- Set 4: Medicines (Set 3, Q11–14, isn't in the source) ----------------
P.dilr_set(4, "Set 4 — Four medicines", "Read the following passage carefully and answer the questions that follow.",
 p("1000 patients currently suffering from a disease were selected to study the effectiveness of treatment of four types of medicines — A, B, C and D. These patients were first randomly assigned into two groups of equal size, called treatment group and control group. The patients in the control group were not treated with any of these medicines; instead they were given a dummy medicine, called placebo, containing only sugar and starch. The following information is known about the patients in the treatment group.") +
 "<ol type=\"a\"><li>A total of 250 patients were treated with type A medicine and a total of 210 patients were treated with type C medicine.</li><li>25 patients were treated with type A medicine only. 20 patients were treated with type C medicine only. 10 patients were treated with type D medicine only.</li><li>35 patients were treated with type A and type D medicines only. 20 patients were treated with type A and type B medicines only. 30 patients were treated with type A and type C medicines only. 20 patients were treated with type C and type D medicines only.</li><li>100 patients were treated with exactly three types of medicines.</li><li>40 patients were treated with medicines of types A, B and C, but not with medicines of type D. 20 patients were treated with medicines of types A, C and D, but not with medicines of type B.</li><li>50 patients were given all the four types of medicines. 75 patients were treated with exactly one type of medicine.</li></ol>",
 "DILR::LR::Venn_Diagrams",
 steps(("Single medicines", p("75 had exactly one: 25 (A) + 20 (C) + 10 (D) leaves 20 on B only.")),
       ("Using A’s total", p("A: 25 + 20 + 30 + 35 + 40 + 20 + 50 = 220, plus the A, B, D group. So A, B and D (not C) = 30. Then the exactly-three total of 100 gives B, C and D (not A) = 10.")),
       ("Using C’s total", p("C: 20 + 30 + 20 + 40 + 20 + 10 + 50 = 190, so B and C only = 20.")),
       ("The last region", p("The treatment group has 500 patients: 75 single + (35 + 20 + 30 + 20 + 20 + x) pairs + 100 triples + 50 all four = 500, so B and D only = 150.") +
       table(["Group", "Patients"], [["B total", "20 + 20 + 20 + 150 + 40 + 30 + 10 + 50 = 340"], ["D total", "10 + 35 + 20 + 150 + 20 + 30 + 10 + 50 = 325"]]))) +
 final("Every region of the four-medicine diagram is fixed."),
 p("Fill the regions given directly, then use each total (A, C, exactly three, everyone) to find one missing region at a time."),
 p("<b>Four-set problems:</b> list the 15 regions and tick them off. Each total you are given should leave exactly one unknown."))
P.dq(15, "How many patients were treated with medicine type B?", [], "TITA", "340", "Medium",
 "Add all regions that include B.",
 steps(("From the set solution", p("20 + 20 + 20 + 150 + 40 + 30 + 10 + 50 = 340."))) + final(r"\(340\)"))
P.dq(16, "The number of patients who were treated with medicine types B, C and D, but not type A was?", [], "TITA", "10", "Medium",
 "Use the 100 who had exactly three.",
 steps(("From the set solution", p("100 − 40 − 20 − 30 = 10."))) + final(r"\(10\)"))
P.dq(17, "How many patients were treated with medicine types B and D only?", [], "TITA", "150", "Medium",
 "The treatment group has 500 patients.",
 steps(("From the set solution", p("Everything else adds to 350, so 150."))) + trap("All 500 in the treatment group received at least one medicine; the placebo group is the other 500.") + final(r"\(150\)"))
P.dq(18, "The number of patients who were treated with medicine type D was:", [], "TITA", "325", "Medium",
 "Add all regions that include D.",
 steps(("From the set solution", p("10 + 35 + 20 + 150 + 20 + 30 + 10 + 50 = 325."))) + final(r"\(325\)"))

# ---------------- Set 5: Contracts ----------------
P.dilr_set(5, "Set 5 — Institutes and vendors", "Read the following passage carefully and answer the questions that follow.",
 p("Four institutes, A, B, C, and D, had contracts with four vendors W, X, Y, and Z during the ten calendar years from 2010 to 2019. The contracts were either multi-year contracts running for several consecutive years or single-year contracts. No institute had more than one contract with the same vendor. However, in a calendar year, an institute may have had contracts with multiple vendors, and a vendor may have had contracts with multiple institutes. It is known that over the decade, the institutes each got into two contracts with two of these vendors, and each vendor got into two contracts with two of these institutes.") +
 p("The following facts are also known about these contracts.") +
 "<ol type=\"I\"><li>Vendor Z had at least one contract in every year.</li><li>Vendor X had one or more contracts in every year up to 2015, but no contract in any year after that.</li><li>Vendor Y had contracts in 2010 and 2019. Vendor W had contracts only in 2012.</li><li>There were five contracts in 2012.</li><li>There were exactly four multi-year contracts. Institute B had a 7-year contract, D had a 4-year contract, and A and C had one 3-year contract each. The other four contracts were single-year contracts.</li><li>Institute C had one or more contracts in 2012 but did not have any contract in 2011.</li><li>Institutes B and D each had exactly one contract in 2012. Institute D did not have any contract in 2010.</li></ol>",
 "DILR::LR::Analytical_Reasoning",
 steps(("Who has the long contracts", p("Z needs ten years from two contracts, which is only possible with B’s 7-year contract plus another multi-year one. X needs 2010–2015 from two contracts, so two multi-year contracts. That uses all four, so W and Y have the four single-year contracts: W’s two in 2012, Y’s in 2010 and 2019.")),
       ("X", p("X’s 2010 contract can’t be D’s (no D in 2010) or C’s (a 3-year from 2010 would include 2011). So it is A’s 3-year, 2010–2012, and D’s 4-year with X runs 2012–2015.")),
       ("Z", p("Z has B’s 7-year and C’s 3-year. C can’t cover 2011, so C’s runs 2017–2019 and B’s 2010–2016.")),
       ("The singles", p("C needs a contract in 2012: its single is with W. W’s other 2012 contract can’t be B’s or D’s (each has exactly one contract in 2012 already), so it is A’s. D can’t be in 2010, so D’s single is Y 2019 and B’s is Y 2010.") +
       table(["Institute", "Contracts"], [["A", "X 2010–2012, W 2012"], ["B", "Z 2010–2016, Y 2010"], ["C", "Z 2017–2019, W 2012"], ["D", "X 2012–2015, Y 2019"]]) +
       table(["Year", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"], [["Contracts", "3", "2", "5", "2", "2", "2", "1", "1", "1", "2"]]))) +
 final("The arrangement is unique."),
 p("Start from vendors Z and X: their coverage needs force the multi-year contracts onto them, and the singles fall into place."),
 p("<b>Coverage problems:</b> when something must be ‘active every year’ with few items, add up the lengths. Only a few combinations can cover the span."))
P.dq(19, "In which of the following years were there two or more contracts?", ["2015", "2018", "2017", "2016"], "MCQ", "1", "Hard",
 "Count the contracts year by year.",
 steps(("From the set solution", p("2015 has two (B with Z, D with X). 2016, 2017 and 2018 have one each."))) + final("2015, option 1"),
 [("2", "Only C with Z."), ("3", "Only C with Z."), ("4", "Only B with Z.")])
P.dq(20, "Which of the following is true?", ["B had a contract with Y in 2019", "D had a contract with X in 2011", "B had a contract with X in 2017", "D had a contract with Y in 2019"], "MCQ", "4", "Hard",
 "D can’t have a contract in 2010.",
 steps(("From the set solution", p("D’s single contract is with Y in 2019."))) + final("Option 4"),
 [("1", "B’s Y contract is in 2010."), ("2", "D’s X contract starts in 2012."), ("3", "X has no contracts after 2015.")])
P.dq(21, "In how many years during this period was there only one contract?", ["3", "5", "2", "4"], "MCQ", "1", "Hard",
 "Look at the yearly counts.",
 steps(("From the set solution", p("2016, 2017 and 2018."))) + final("3, option 1"),
 [("2", "Only three years have a single contract."), ("3", "Misses one."), ("4", "Counts one too many.")])
P.dq(22, "What BEST can be concluded about the number of contracts in 2010?", ["At least 3", "At least 4", "Exactly 4", "Exactly 3"], "MCQ", "4", "Hard",
 "Who is active in 2010?",
 steps(("From the set solution", p("B with Z, A with X, B with Y: exactly 3."))) + final("Exactly 3, option 4"),
 [("1", "It is fixed at 3."), ("2", "Too many."), ("3", "Too many.")])
P.dq(23, "Which institutes had multiple contracts during the same year?", ["B and C only", "B only", "A only", "A and B only"], "MCQ", "4", "Hard",
 "Look for an institute with two active contracts in one year.",
 steps(("From the set solution", p("A in 2012 (X and W) and B in 2010 (Z and Y)."))) + final("A and B only, option 4"),
 [("1", "C’s contracts don’t overlap."), ("2", "A also overlaps."), ("3", "B also overlaps.")])
P.dq(24, "Which institutes and vendors had more than one contracts in any year?", ["A, D, W, and Z", "B, W, X, and Z", "A, B, W, and X", "B, D, W, and X"], "MCQ", "3", "Hard",
 "Check vendors too: who had two contracts running at once?",
 steps(("Institutes", p("A (2012) and B (2010).")),
       ("Vendors", p("W (two in 2012) and X (A and D in 2012). Z’s two contracts don’t overlap."))) + final("A, B, W and X, option 3"),
 [("1", "D and Z never had two at once."), ("2", "Leaves out A and includes Z."), ("4", "Leaves out A and includes D.")])
