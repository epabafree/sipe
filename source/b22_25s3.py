# -*- coding: utf-8 -*-
# Batch 22 — CAT 2025 Slot 3: VARC (Q1–24). DILR and QA are added by b22_25s3_dilr.py and b22_25s3_qa.py.
# Question numbers follow the order of the actual exam.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2025, 3, "ex22_25s3.json")
P.passage("P1", "Passage 1 — Memory, imagination and tribal art", "Arts_and_Literature")
P.passage("P2", "Passage 2 — Can a machine be a moral judge?", "Philosophy_and_Psychology")
P.passage("P3", "Passage 3 — A century of building dams", "Environment_and_Life_Science")
P.passage("P4", "Passage 4 — India’s forest acts, old and new", "Social_Science_and_History")

P.va(1, P.summ(1), P.Q["VARC"][1]["opts"], "MCQ", "1", "Summary", "Hard",
 "The passage ends with “Hence…”. Which option keeps that conclusion and the reason for it?",
 steps(("What the passage says", "<ol><li>A memory-belief happens now, not in the past it refers to.</li><li>So it doesn’t logically require the remembered event, or any past, to have existed.</li><li>Hence “knowledge of the past” is logically independent of the past.</li></ol>"),
       ("Choosing", p("Option 1 states the conclusion and the reason: remembering happens in the present and needs no real past."))) +
 final("Option 1."),
 "summary",
 [("2", "“A figment of our imagination” adds a claim, and the conclusion about knowledge of the past is missing."),
  ("3", "Close, but it treats the conclusion as something to keep in mind rather than what the argument proves, and drops the reason."),
  ("4", "“Depend wholly on what is remembered in the present, and not on anything else” overstates; the five-minute world is an illustration, not the point.")])

P.va(2, P.sents(2), [], "TITA", "1", "Odd_One_Out", "Medium",
 "Four sentences describe music as universal and demanding. One is about research on emotion.",
 steps(("The chain", p("Sentence 2: music is universal and uses many brain resources. Sentence 5: engaging with it is cognitively demanding and found across cultures. Sentence 4: the urge to make and enjoy music is everywhere. Sentence 3: “This inherent connection” is tied to human identity.")),
       ("The extra sentence", p("Sentence 1 turns to research on music and emotion, a different topic."))) +
 final(r"\(1\)"),
 "oddone",
 [("2", "Music is universal."), ("5", "It is demanding and found everywhere."), ("4", "The urge to make music is everywhere."), ("3", "“This inherent connection” and identity.")],
 why_title="How the other sentences fit")

# ---------------- Passage 1 ----------------
P.rc(3, "P1", "Weaken", "3", "Medium",
 "The “hallucinatory” claim is about fluid space, time and planes of existence. Which option is consistent with it?",
 steps(ev(1, "It admits fusion between various planes of existence and levels of time in a natural and artless manner.") +
       ev(3, "aspiring to enter a trance in which they can converse with the dead") +
       p("Stories featuring conversations with the dead fit the passage’s picture; they don’t weaken it. The other three would.")) +
 final("Option 3."),
 "weaken",
 [("1", "Rational, scientific depiction contradicts dreamlike, hallucinatory fusion."),
  ("2", "A strict beginning, middle and end contradicts “Spatial order and temporal sequence do not restrict the narrative”."),
  ("4", "The passage says a tribal epic can start from a trivial everyday event.")])

P.rc(4, "P1", "Detail", "2", "Easy",
 "The second paragraph links each faculty to one of two realities.",
 steps(ev(2, "We put meaning into space by perceiving it in terms of images.") +
       ev(2, "With regard to time, we make connections with the help of memory")) +
 final("Option 2."),
 "detail",
 [("1", "The passage contrasts cultivated imagination with memory but defines the difference by space and time."),
  ("3", "This is about tribal preferences, not the difference itself."),
  ("4", "Imagination is called a genetic gift, but memory isn’t defined as “central to consciousness”.")])

P.rc(5, "P1", "Inference", "3", "Medium",
 "Why can stars and mountains be angry or happy in tribal stories?",
 steps(ev(1, "It admits fusion between various planes of existence and levels of time in a natural and artless manner.") +
       ev(1, "they admit the principle of association between emotion and the narrative motif") +
       p("The boundaries between kinds of existence are fluid, so non-human things can feel as humans do.")) +
 final("Option 3."),
 "inference",
 [("1", "The passage doesn’t call tribal narratives rudimentary."),
  ("2", "Self-conscious form belongs to secular creativity, not tribal imagination."),
  ("4", "The passage says tribal creations do have conventions and rules.")])

P.rc(6, "P1", "Inference", "2", "Medium",
 "Look at what the ancestor ritual is said to substantiate.",
 steps(ev(3, "Thus, they seem to have turned almost obsessively to gaining domination over time. This urge is substantiated in their ritual of conversing with their dead ancestors")) +
 final("Option 2."),
 "inference",
 [("1", "This says how they worship, not why."),
  ("3", "The knowledge system is a separate achievement of their memory."),
  ("4", "The passage says domination over space was not their lot.")])

# ---------------- Passage 2 ----------------
P.rc(7, "P2", "Main_Idea", "3", "Hard",
 "Two options open the same way. Check what each says about codification and the physics analogy.",
 steps(("The passage", p("It weighs the appeal of an impartial AI judge against doubts about whether it can grasp morality. It warns that formalising ethics may flatten intuition and context, notes that AI suits reasoning from fixed axioms, and uses physics to show that formal theories can share a structure while diverging.")),
       ("Choosing", p("Option 3 matches. Option 4 says codification retains nuance and that physics predicts convergence, both the reverse of the passage."))) +
 final("Option 3."),
 "inference",
 [("1", "The passage raises doubts; it doesn’t reject AI “under any conditions”."),
  ("2", "The passage doesn’t treat reproducing human judgement as progress."),
  ("4", "It says formalising risks losing nuance, and physics theories diverge.")])

P.rc(8, "P2", "Except", "2", "Medium",
 "Which option predicts convergence on a single ethical system?",
 steps(ev(4, "These theories also diverge and, even when they recommend similar actions, such as giving to charity, they justify them in different ways.") +
       p("The passage expects divergence, not convergence, and warns that context and intuition matter.")) +
 final("Option 2."),
 "except",
 [("1", "The ideal is “unburdened by emotion, prejudice or inconsistency”, yet the passage questions whether that is moral understanding."),
  ("3", "This restates the warning that encoding ethics flattens its essential features."),
  ("4", "This restates the physics analogy: shared structure, divergent theories.")])

P.rc(9, "P2", "Inference", "4", "Hard",
 "If different ethical theories cover different domains, what must AI know before reasoning from any of them?",
 steps(p("In physics, we use quarks’ theory for quarks and gravity for galaxies. For the analogy to guide practice, there must be a principled way to decide which ethical framework applies to a case, so that the right axioms are chosen before reasoning starts.")) +
 final("Option 4."),
 "inference",
 [("1", "A single master framework contradicts the analogy of many theories."),
  ("2", "Requiring that cases never overlap is far stronger than needed."),
  ("3", "If all frameworks agreed, the analogy wouldn’t matter at all.")])

P.rc(10, "P2", "Vocabulary", "4", "Hard",
 "Utilitarianism maximises total wellbeing. What would reject that aim?",
 steps(ev(3, "the principle that one should act to maximise overall wellbeing") +
       p("A prioritarian approach gives more weight to the worst-off instead of maximising the total. That directly opposes the utilitarian aim.")) +
 final("Option 4."),
 "inference",
 [("1", "It still judges by broadest societal benefit, which is utilitarian."),
  ("2", "Ranking by overall social welfare is utilitarian."),
  ("3", "Choosing the highest total benefit is utilitarian, whatever the label.")])

# ---------------- Passage 3 ----------------
P.rc(11, "P3", "Purpose", "4", "Medium",
 "The famous dams are mentioned right before the author turns to the many smaller ones.",
 steps(ev(1, "Some of the results of that drive were charismatic mega-infrastructure—the Hoover on the Colorado River or the Aswan on the Nile—but most of the tens of thousands of dams that dot the Earth’s landscape have drawn little attention.") +
       p("The same drive to conquer and control nature produced both the famous dams and the many smaller ones.")) +
 final("Option 4."),
 "purpose",
 [("1", "“Charismatic” describes the structures, not their builders."),
  ("2", "The thin blue line refers to rivers downstream of reservoirs in general."),
  ("3", "Employers aren’t called messianic; the drive is.")])

P.rc(12, "P3", "Vocabulary", "1", "Easy",
 "Dams were the physical form of a drive to conquer nature. What word fits “the physical ___ of a drive”?",
 steps(p("An instantiation is a concrete instance of an idea. Dams were the physical example, the manifestation, of a messianic drive.")) +
 final("Option 1."),
 "detail",
 [("2", "Durability and timeliness have nothing to do with embodying a drive."),
  ("3", "Construction describes building, not expressing an idea."),
  ("4", "Viability is about being workable, not embodying.")])

P.rc(13, "P3", "Except", "1", "Medium",
 "The passage calls smaller dams “not inconsequential”. Does it say they are safer?",
 steps(p("The passage never compares the safety of small and large dams.") +
       ev(1, "These are the smaller, though not inconsequential, barriers that today impede the flow of water on nearly two-thirds of the world’s large waterways.")) +
 final("Option 1."),
 "except",
 [("2", "Asmal questions whether we get a fair return on a $2 trillion investment."),
  ("3", "Dams were an instrument of colonialism to dispossess Indigenous people."),
  ("4", "Despite opposition and alternatives, construction continues.")])

P.rc(14, "P3", "Main_Idea", "3", "Hard",
 "Which set tracks the passage’s main moves: the scale of dams, their human cost, their justification and where things stand?",
 steps(p("The passage moves from mega-infrastructure, to dams as sacrifice zones, to sacrifices offered at “the temples of modernity”, to the continuing tilt towards water impoundment. Option 3 follows that line.")) +
 final("Option 3."),
 "inference",
 [("1", "Lucrative contracts and expected lives are details, not the key arguments."),
  ("2", "“Alternative energy” is a minor point, and the sacrifices are missing."),
  ("4", "Toxic algae and “quarter century” are details.")])

P.va(15, P.sents(15, P.PJ_DIR), [], "TITA", "2143", "Para_Jumble", "Hard",
 "Sentence 2 introduces candidates’ portraits. Which sentence uses “effigy” next?",
 steps(("The order", p("Sentence 2: candidates put portraits on their prospectus; photography has a power that needs analysing. Sentence 1: the effigy links candidate and voters through a physical manner. Sentence 4: photography restores the paternalistic nature of elections. Sentence 3, beginning “Inasmuch as”, draws the general conclusion: photography is an anti-intellectual weapon."))) +
 final("2143"),
 "pj",
 [("2", "Introduces the portrait."), ("1", "“The effigy” and its link with voters."), ("4", "What photography restores."), ("3", "The general conclusion.")],
 why_title="Why each sentence goes where it does")

P.va(16, P.summ(16), P.Q["VARC"][16]["opts"], "MCQ", "1", "Summary", "Medium",
 "The passage names three motives. Which option keeps them without generalising to all shoppers?",
 steps(("What the passage says", "<ol><li>Moving away from the sameness of fast fashion.</li><li>Not wanting to add to its waste.</li><li>Wanting custom fit without paying bespoke or indie-brand prices.</li></ol>"),
       ("Choosing", p("Option 1 has all three: away from uniformity and waste, towards customisation at lower prices."))) +
 final("Option 1."),
 "summary",
 [("2", "It leaves out waste and the move away from uniformity."),
  ("3", "“All Indian shoppers” overgeneralises, and Zara and H&M are fast fashion, not expensive brands."),
  ("4", "The passage calls fast fashion wasteful, not expensive brands.")])

P.va(17, P.sents(17, P.PJ_DIR), [], "TITA", "4312", "Para_Jumble", "Medium",
 "Sentence 3 begins “They have done this”. Who did what?",
 steps(("The order", p("Sentence 4: activists devised “Latinx” to be gender-neutral. Sentence 3: “They have done this” although grammatical gender isn’t sexual. Sentence 1: Moraga, an LGBTQ activist, still prefers her own term. Sentence 2: the figures show how few use Latinx."))) +
 final("4312"),
 "pj",
 [("4", "Activists devise Latinx."), ("3", "“They have done this” despite how gender works in language."), ("1", "An LGBTQ activist who rejects it."), ("2", "The usage figures.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.sents(18), [], "TITA", "3", "Odd_One_Out", "Medium",
 "Four sentences tell the discovery. One describes the equipment.",
 steps(("The chain", p("Sentence 1: half our oxygen comes from surface phytoplankton. Sentence 5: deep-sea rocks, polymetallic nodules, host many creatures. Sentence 2: they also produce oxygen on the seafloor. Sentence 4: that is surprising, since oxygen usually needs the sun.")),
       ("The extra sentence", p("Sentence 3 describes the research chambers, a methodological detail outside the chain."))) +
 final(r"\(3\)"),
 "oddone",
 [("1", "Where most oxygen comes from."), ("5", "The nodules."), ("2", "“They also produce oxygen”."), ("4", "Why it is surprising.")],
 why_title="How the other sentences fit")

P.va(19, P.ms(19), P.Q["VARC"][19]["opts"], "MCQ", "1", "Missing_Sentence", "Hard",
 "The sentence is about productivity gains feeding returns to wealth. Which sentence just said capital income has been boosted?",
 steps(("The fit", p("The last sentence says wages stagnated while capital income was “boosted by design”. The missing sentence completes the thought: productivity gains now go to wealth rather than living standards. So it belongs at blank (4).")),
       ("Reading the options", p("Blank (4) is listed first, so the answer is option 1."))) +
 final("Blank (4), which is option 1."),
 "missing",
 [("2", "At blank (2) the paragraph is still defining what wealth depends on."),
  ("3", "At blank (1) wages and capital income haven’t been discussed."),
  ("4", "Blank (3) comes before the point about stagnating wages that the sentence builds on.")])

P.va(20, P.ms(20), P.Q["VARC"][20]["opts"], "MCQ", "1", "Missing_Sentence", "Medium",
 "The sentence locates the defect on a chromosome. What should come before it, and what after?",
 steps(("The fit", p("First the family and their behaviour are described; then the defect is located to a region of the X chromosome; finally a precise point mutation is identified in that region. So the sentence goes at blank (3), between the behaviour and the mutation.")),
       ("Reading the options", p("Blank (3) is listed first, so the answer is option 1."))) +
 final("Blank (3), which is option 1."),
 "missing",
 [("2", "Blank (4) is after the exact mutation; locating the region would come too late."),
  ("3", "At blank (1) the family hasn’t been introduced."),
  ("4", "Blank (2) splits the syndrome from the description of the behaviour.")])

# ---------------- Passage 4 ----------------
P.rc(21, "P4", "Inference", "4", "Medium",
 "What did critics point out that widened the debate?",
 steps(ev(2, "It was pointed out, for example, that the draft act was closely modelled on its predecessor, the Forest Act of 1878.") +
       p("The debate became one about forest policy as a whole because the new act copied colonial measures of control.")) +
 final("Option 4."),
 "inference",
 [("1", "Commercial exploitation is part of the older system, but it isn’t what widened the debate."),
  ("2", "This is the original complaint, not why it grew."),
  ("3", "The defence by officials is part of the first controversy.")])

P.rc(22, "P4", "Weaken", "4", "Hard",
 "The narrative: the colonial state usurped rights that had little precolonial precedent, driven by the railways. Which option leaves that untouched?",
 steps(ev(2, "The earlier Act rested on a usurpation of rights of ownership by the colonial state which had little precedent in precolonial history.") +
       p("If German experts were known for violating indigenous rights, that fits the passage’s story; it doesn’t weaken it.")) +
 final("Option 4."),
 "weaken",
 [("1", "If precolonial rulers denied access too, the claim of little precedent fails."),
  ("2", "If railway timber came from imports, the railway story of deforestation collapses."),
  ("3", "Blaming tribal groups for deforestation cuts against their standing claim to forests.")])

P.rc(23, "P4", "Detail_Not_True", "1", "Medium",
 "Which feature does the passage attach to only one of the two acts, or to neither?",
 steps(p("Deforestation came from the railways before the 1878 Act; the 1982 draft was justified as a way to stop deforestation. Neither act is said to have caused it. Both, by contrast, expanded state control, follow a colonial model, and sparked debate.")) +
 final("Option 1."),
 "notrue",
 [("2", "Both extended the state’s control over forests."),
  ("3", "The 1982 draft was modelled on the colonial 1878 Act."),
  ("4", "Both were preceded or followed by bitter debate.")])

P.rc(24, "P4", "Detail", "1", "Easy",
 "What major demand has the government shown little inclination to meet?",
 steps(ev(3, "abandoning the principle of state monopoly over forest land by handing over areas of degraded forests to individuals and communities for afforestation")) +
 final("Option 1."),
 "detail",
 [("2", "The passage mentions stopping clear-felling, not a ban on deforestation."),
  ("3", "The state’s claim is already recognised; critics want it relaxed."),
  ("4", "The government has already stopped ecologically hazardous practices.")])
