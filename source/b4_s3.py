# -*- coding: utf-8 -*-
# Batch 4 — CAT 2023 Slot 3: VARC (Q1–24). DILR and QA are added by b4_s3_dilr.py and b4_s3_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2023, 3, "ex4_s3.json")
P.passage("P1", "Passage 1 — Do patrimony laws stop discoveries?", "Social_Science_and_History")
P.passage("P2", "Passage 2 — A review of Pinker’s “Rationality”", "Philosophy_and_Psychology")
P.passage("P3", "Passage 3 — A review of “The Nutmeg’s Curse”", "Environment_and_Life_Science")
P.passage("P4", "Passage 4 — Defining romantic aesthetics", "Arts_and_Literature")

# ---------------- Passage 1 ----------------
P.rc(1, "P1", "Except", "4", "Medium",
 "The author wants source countries to attract foreign money and expertise. Which option has the money flowing the wrong way?",
 steps(("The author’s advice", ev(5, "source countries, particularly in the developing world, should narrow their cultural property laws so that they can reap the benefits of new archaeological discoveries") +
          p("The problem he identifies: strict laws cut the incentive for <b>foreign</b> bodies to invest, because they can’t “hold, display and study” what they find.")),
       ("Test the options", p("Options 1, 2 and 3 all bring foreign investment in: let foreigners study and exhibit finds, follow China’s collaborative turn, motivate others to fund digs. Option 4 has a poor country <b>paying</b> foreign institutes, which reverses the problem."))) +
 final("Option 4.") + trap("Option 2 can look extreme because the author says not to “abolish” restrictions, but he presents China’s switch as an approach worth copying."),
 "except",
 [("1", "Matches ¶5: foreigners want “opportunities to hold, display and study what is uncovered”."), ("2", "¶6–7 present China’s switch as “an interesting alternative approach” that produced 11 nominations."),
  ("3", "This is the whole point of narrowing the laws: restore foreign incentives to invest.")])

P.rc(2, "P1", "Detail", "4", "Easy",
 "Look for the benefit the author says new discoveries bring.",
 steps(("Locate", ev(5, "new archaeological discoveries, which typically increase tourism and enhance cultural pride"))) + final("Option 4."),
 "detail",
 [("1", "Patrimony laws protect sites; that isn’t why sites are valued."), ("2", "The laws respond to Western imperialism; the sites aren’t its symbol."),
  ("3", "The passage never says sites fund future discoveries.")])

P.rc(3, "P1", "Weaken", "1", "Hard",
 "The author’s argument: strict laws scare off foreign funding, and poor countries can’t fund digs themselves, so discoveries fall. What would remove that funding gap?",
 steps(("Central idea", p("Poor but site-rich countries should narrow their patrimony laws to win back foreign investment, because without it few new sites get discovered.")),
       ("What undermines it", p("If <b>UNESCO already finances</b> research in exactly these countries, the funding gap closes without touching the laws. The case for narrowing them collapses."))) +
 final("Option 1.") + trap("Option 3 sounds similar, but the author already allows for it: “To the extent that source countries can fund their own archaeological projects, artifacts and sites may still be discovered.” It is about affluent countries, not the poor ones he’s advising."),
 "weaken",
 [("2", "An apology for past looting doesn’t affect today’s funding or discoveries."), ("3", "Already conceded in ¶5, and it concerns affluent countries."),
  ("4", "Local museums displaying finds doesn’t restore foreign incentives to dig.")])

P.rc(4, "P1", "Main_Idea", "1", "Easy",
 "What were the laws meant to do, and what did the author’s survey show actually happened?",
 steps(("Intention", ev(3, "Patrimony laws were intended to protect future archaeological discoveries against Western imperialist designs.")),
       ("Result", ev(4, "the number of discovered sites diminishes sharply after a country passes a cultural property law"))) + final("Option 1."),
 "inference",
 [("2", "Museums withholding treasures isn’t the paradox the survey shows."), ("3", "Auction business is never presented as a consequence."), ("4", "Neglect of existing sites isn’t discussed; the drop is in <i>new</i> discoveries.")])

# ---------------- Passage 2 ----------------
P.rc(5, "P2", "Detail", "1", "Easy",
 "Find where the author praises the power of conscious, sequential reasoning.",
 steps(("Locate", ev(4, "Skill in this domain maps directly onto the navigation of many real-world problems, and Pinker shows how greater mastery of the tools of rationality can improve decision-making in medical, legal, financial and many other contexts"))) + final("Option 1."),
 "detail",
 [("2", "Statistics is one tool covered, not why reasoning matters."), ("3", "That’s Pinker’s point about media coverage, which the author calls a reasonable critique but not a reason reasoning is important."),
  ("4", "The author says the moral side “doesn’t really get developed” in Pinker.")])

P.rc(6, "P2", "Except", "2", "Medium",
 "Three options come from what Socrates “anticipated” and from rationality being a moral virtue. One is the very idea the author argues against.",
 steps(("Shared ground", ev(5, "showing the virtue of knowing what you do not know and examining all premises in arguments, not simply trusting speakers’ authority or charisma") +
          ev(6, "rationality “is not just a cognitive virtue but a moral one.” … subtly explored by ancient Greek philosophers like Plato and Aristotle")),
       ("The odd one", p("Option 2 claims great achievements rest on conscious reasoning. The author says the opposite: they often come from epiphany, and even Socrates credited dreams and visions."))) +
 final("Option 2."),
 "except",
 [("1", "¶6: a moral virtue, explored by Plato and Aristotle."), ("3", "¶5: not trusting the speaker’s authority or charisma."), ("4", "¶5: knowing what you do not know, examining premises.")])

P.rc(7, "P2", "Purpose", "4", "Medium",
 "The Greeks appear in the closing paragraph, right before “doesn’t really get developed” and “This is a shame”.",
 steps(("Locate", ev(6, "this profoundly important point, one subtly explored by ancient Greek philosophers like Plato and Aristotle, doesn’t really get developed. This is a shame")),
       ("Function", p("The Greeks show what a fuller treatment of ethics and rationality looks like, and so expose what Pinker leaves out."))) + final("Option 4."),
 "purpose",
 [("1", "Dreams are mentioned once, about Socrates, not as a centuries-long influence on inventions."), ("2", "Similarities are noted in passing, but the paragraph’s point is a gap."),
  ("3", "No claim that the Greeks influenced Pinker’s arguments.")])

P.rc(8, "P2", "Purpose", "2", "Easy",
 "Kekule is science, Mozart is music. What do the two have in common in the author’s sentence?",
 steps(("Locate", ev(5, "many of the deepest insights in the history of science, math, music and art strike their originators in moments of epiphany. … much extraordinary human achievement is not a product of conscious, sequential reasoning"))) +
 final("Option 2."),
 "purpose",
 [("1", "The examples include science; the author doesn’t contrast it with other fields."), ("3", "Close, but the point isn’t that science also benefits; it’s that reasoning isn’t always the source."),
  ("4", "Nothing about European achievements or the past being different.")])

# ---------------- Passage 3 ----------------
P.rc(9, "P3", "Except", "1", "Medium",
 "What does the reviewer say about the academic fields that dominated global discourse?",
 steps(("Key line", ev(3, "the invaders and their myriad backers in the fields of economics, politics, anthropology, philosophy, literature, technology, physics, chemistry, biology have dominated global intellectual discourse")),
       ("Apply", p("Academic discourse has largely backed the exploitative view of Earth, so “always served … environmental preservation” cannot be inferred."))) + final("Option 1."),
 "except",
 [("2", "The book moves the start of the climate crisis back to the start of colonialism."), ("3", "Colonialism replaced indigenous understanding with nature as a “resource”, which continues today."),
  ("4", "Ghosh uses non-European sources to question the prevailing view; the reviewer agrees.")])

P.rc(10, "P3", "Purpose", "3", "Medium",
 "Ghosh draws two points from the Banda massacre, and both reach the present day.",
 steps(("The two points", ev(2, "how European colonialists decimated not only indigenous populations but also indigenous understanding of the relationship between humans and Earth") +
          ev(2, "how this continues to the present day by looking at nature as a ‘resource’ to exploit")),
       ("Purpose", p("The episode illustrates the colonial mindset towards nature, and how it carries on into today’s climate crisis."))) + final("Option 3."),
 "purpose",
 [("1", "“First instance in history” is more than the reviewer claims."), ("2", "Violence is part of it, but the focus is on the mindset towards Earth."),
  ("4", "Plantation crops are a detail; the point is the attitude behind them.")])

P.rc(11, "P3", "Weaken", "2", "Hard",
 "Why does the reviewer say “who” for Gaia? Find the reason, then remove it.",
 steps(("The reason", ev(2, "I use the pronoun ‘who’ knowingly, because Ghosh has quoted many non-European sources to enquire into the relationship between humans and the world around them so that he can question the prevalent way of looking at Earth as an inert object")),
       ("Remove it", p("If non-European societies also saw Earth as non-living, the sources behind “who” would say the opposite, and the pronoun would lose its basis."))) + final("Option 2."),
 "weaken",
 [("1", "“Revenge” still suggests a living agent, so “who” would still fit."), ("3", "The reviewer already rejects the dominant Western view; new Western evidence wouldn’t change his reason."),
  ("4", "A cause–effect link is compatible with Earth “responding”, so it doesn’t make “who” inappropriate.")])

P.rc(12, "P3", "Detail_Not_True", "3", "Medium",
 "Three options are reasons the passage gives. Check what it says about solar power: is the problem solar’s nature, or who opposes it?",
 steps(("Locate", ev(4, "power utilities are sabotaging decentralised solar power generation today because it hits their revenues and control")),
       ("Apply", p("The failure comes from the utilities’ sabotage, not from solar power being decentralised."))) + final("Option 3."),
 "notrue",
 [("1", "¶4: other points of view “are so often drowned out”, and Pachamama gets lip service."), ("2", "¶4: utilities sabotage solar to protect revenues."),
  ("4", "¶4: the vested interest in the oil economy, including a superpower that controls it.")])

# ---------------- Passage 4 ----------------
P.rc(13, "P4", "Detail", "3", "Easy",
 "What is “the most characteristic romantic commitment”?",
 steps(("Locate", ev(2, "the character of art and beauty and of our engagement with them should shape all aspects of human life … not only in a philosophical or artistic life, but also in the lives of ordinary men and women"))) + final("Option 3."),
 "detail",
 [("1", "The passage says ordinary people too."), ("2", "That is the conventional view the romantics rejected."), ("4", "They called beauty and art “fundamental to human existence”.")])

P.rc(14, "P4", "Detail", "2", "Easy",
 "Read to the end of the sentence that quotes “a single definition, a specific time, or a specific place”.",
 steps(("Locate", ev(3, "such studies attempt to characterise romanticism, not in terms of a single definition, a specific time, or a specific place, but in terms of “particular philosophical questions and concerns”"))) + final("Option 2."),
 "detail",
 [("1", "These studies think a general characterisation <i>is</i> possible."), ("3", "The paradox belongs to a different paragraph and isn’t why the studies avoid definitions."),
  ("4", "They respond to Lovejoy, but “discredit” is too strong; they accept the differences he stressed.")])

P.rc(15, "P4", "Detail_Not_True", "1", "Medium",
 "Check how recent studies treat the differences between national romanticisms.",
 steps(("Locate", ev(3, "Instead of overlooking the undeniable differences between the variety of romanticisms of different nations that Lovejoy had stressed, such studies attempt to characterise romanticism")),
       ("Apply", p("The studies accept the differences (“undeniable”). They don’t try to refute them."))) + final("Option 1."),
 "notrue",
 [("2", "¶3: “neither impossible nor undesirable”."), ("3", "¶2: many romantics rejected aesthetics as a separate domain."),
  ("4", "¶2: their views are found “in fragments, aphorisms and poems”.")])

P.rc(16, "P4", "Detail", "2", "Medium",
 "The question says “the main difficulty”. Find that phrase in the passage.",
 steps(("Locate", ev(1, "The main difficulty in studying the romantics, according to him, is the lack of any “single real entity, or type of entity” that the concept “romanticism” designates")),
       ("Paraphrase", p("No single thing the word refers to means the concept has no clear boundaries."))) + final("Option 2."),
 "detail",
 [("1", "This is an extra challenge for romantic <i>aesthetics</i>, not the main difficulty with romanticism."), ("3", "Their views exist, just in fragments."),
  ("4", "“Scandal” is Lovejoy’s description of the definitional mess, not a scandalous history.")])

# ---------------- Verbal ability ----------------
P.va(17, P.missing_html(17), P.strict_opts(17), "MCQ", "4", "Missing_Sentence", "Medium",
 "The sentence describes arguments “abstracted from their contexts”. One gap is followed by “But … as they in fact occur in human communicative practices.”",
 steps(("Find the contrast", p("Gap (3) is followed by “<b>But</b> depending on one’s explanatory goals, there is also much to be gained from considering arguments as they in fact occur in human communicative practices.” That “But” needs the opposite idea just before it: arguments taken out of context.")),
       ("Check the flow", p("Before gap (3), the paragraph has described arguments abstractly (premises, conclusion, support). The sentence sums that up as the “theoretical” view, and the next sentence turns to real use.")),
       ("Match the label", p("Gap (3) is labelled “Option 3”, which is choice 4."))) + final("Choice 4."),
 "missing",
 [("1", "“Option 2”: there the definitions are still being given; nothing contrasts with the sentence yet."), ("2", "“Option 1”: the opening needs to introduce arguments, not set them aside as abstractions."),
  ("3", "“Option 4”: after the “But …” sentence, the abstract view would come back out of order.")])

P.va(18, P.missing_html(18), P.strict_opts(18), "MCQ", "4", "Missing_Sentence", "Medium",
 "The sentence says armed conflict “also” helps crime. Which sentence just described the other direction, crime helping conflict?",
 steps(("Find the pair", p("Before gap (3): “Financial gains from crime can lengthen or intensify armed conflicts…” (crime → conflict). The sentence adds the reverse (conflict → crime), which is why it says “<b>also</b>”.")),
       ("Check what follows", p("“<b>In this context</b>, when hostilities cease…” then picks up the crime-friendly environment the sentence describes.")),
       ("Match the label", p("Gap (3) is labelled “Option 3”, which is choice 4."))) + final("Choice 4."),
 "missing",
 [("1", "“Option 4”: after the final sentence about peacebuilding, the point comes too late."), ("2", "“Option 2”: the “also” then has no crime → conflict statement to add to."),
  ("3", "“Option 1”: the opening needs the general claim about linkages first.")])

P.va(19, P.sent_html(19), [], "TITA", "2", "Odd_One_Out", "Medium",
 "Four sentences are about soft skills versus hard skills in hiring. One is about something else.",
 steps(("Chain", p("<b>1 → 3 → 5 → 4</b>: firms are moving beyond technical abilities (1); job descriptions now ask for soft skills (3); a recruiter explains why (5); technical know-how still matters for some jobs (4).")),
       ("Odd one", p("Sentence 2 is about dropping the idea of a single “perfect candidate”. It doesn’t mention hard or soft skills."))) + final("2"),
 "oddone",
 [("1", "Opens: the move away from technical skills alone."), ("3", "“Now” job descriptions ask for soft skills."), ("5", "Why: a response to the pandemic."), ("4", "The caveat: some jobs still need specific expertise.")],
 why_title="How the other sentences fit")

P.va(20, P.sent_html(20), [], "TITA", "2", "Odd_One_Out", "Medium",
 "Four sentences are about the death of the last speaker of Bo. One is about the islands’ population history.",
 steps(("Chain", p("<b>4 → 3 → 1 → 5</b>: the last speaker of an ancient language has died (4); what Bo is (3); Boa Senior, the last fluent speaker (1); she couldn’t talk to anyone in her language at the end (5).")),
       ("Odd one", p("Sentence 2 is about the population collapse under colonial rule. It doesn’t mention the language or Boa Senior."))) + final("2"),
 "oddone",
 [("4", "Opens with the news."), ("3", "Introduces Bo."), ("1", "Introduces Boa Senior."), ("5", "Closes on her isolation.")],
 why_title="How the other sentences fit")

P.va(21, P.sent_html(21), [], "TITA", "2431", "Para_Jumble", "Medium",
 "One sentence introduces the printing press and learning. One looks forward “centuries later”.",
 steps(("Opener", p("<b>2</b> introduces the printing press’s impact on learning, and what learning was before it (listening, memorisation).")),
       ("Middle", p("<b>4</b> shows the shift from listening to reading. <b>3</b> calls that “transformation of learners from listeners to readers” a slow, complex process.")),
       ("Close", p("<b>1</b>: “Centuries later”, learning is still based on reading."))) + final("2431"),
 "pj",
 [("2", "Sets the scene: learning before print."), ("4", "The shift print caused."), ("3", "Names that shift and how slow it was."), ("1", "Brings it to today.")],
 why_title="Why each sentence goes where it does")

P.va(22, P.sent_html(22), [], "TITA", "3142", "Para_Jumble", "Easy",
 "Problem → person → plan → vision. Follow the pronouns.",
 steps(("Problem", p("<b>3</b> states the problem: e-waste has valuable materials, but not enough is recycled.")),
       ("Person", p("<b>1</b>: “this problem”, and Sahajwalla’s new solution.")),
       ("Plan, then detail", p("<b>4</b>: “She plans” microfactories. <b>2</b>: “Her vision” of how they work."))) + final("3142"),
 "pj",
 [("3", "Has no pronoun; it’s the opener."), ("1", "“this problem” refers back to 3."), ("4", "“She” needs 1."), ("2", "Describes how the microfactories in 4 would work.")],
 why_title="Why each sentence goes where it does")

P.va(23, P.summary_html(23, "Gradually, life"), P.Q["VARC"][23]["opts"], "MCQ", "3", "Summary", "Medium",
 "The passage describes life coming back once pests are gone: birds, soil, plants, and a feedback loop.",
 steps(("Points", "<ol><li>With pests gone, burrowing birds are increasing.</li><li>Their droppings feed plants, and taller plants protect the birds.</li><li>Plants that were fenced off are spreading everywhere.</li></ol>"),
       ("Pick", p("Option 3 keeps both halves: no pests, and birds and plants reviving."))) + final("Option 3."),
 "summary",
 [("1", "“Brought under environmental protection” is vaguer than the passage, which is about removing pests."), ("2", "Gets it backwards: the recovery is because the pests are gone, and it’s burrowing birds, not predators, that are increasing."),
  ("4", "Calls the island Antarctic and leaves out why life is recovering.")])

P.va(24, P.summary_html(24, "The weight of society"), P.Q["VARC"][24]["opts"], "MCQ", "4", "Summary", "Medium",
 "Compare perfectionism in the 1950s with perfectionism today.",
 steps(("Points", "<ol><li>The pressure of expectations is old but has grown.</li><li>1950s perfectionism meant conforming, only more so.</li><li>Today’s perfectionists must stand out to win attention.</li></ol>"),
       ("Pick", p("Option 4 keeps the long history and the shift from conformity to standing out."))) + final("Option 4."),
 "summary",
 [("1", "“Any lengths” is extreme, and it leaves out the change over time."), ("2", "The media are only an example; this misses the shift."),
  ("3", "“Tension and conflict” isn’t in the passage.")])
