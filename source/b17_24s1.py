# -*- coding: utf-8 -*-
# Batch 17 — CAT 2024 Slot 1: VARC (Q1–24). DILR and QA are added by b17_24s1_dilr.py and b17_24s1_qa.py.
# Question numbers follow the order of the actual exam.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2024, 1, "ex17_24s1.json")
P.passage("P1", "Passage 1 — Streaming, ownership and disappearing films", "Arts_and_Literature")
P.passage("P2", "Passage 2 — Craftsmanship, efficiency and jobs", "Economics_and_Management")
P.passage("P3", "Passage 3 — Bringing back the western barred bandicoot", "Environment_and_Life_Science")
P.passage("P4", "Passage 4 — Economics, psychology and narrative", "Economics_and_Management")
O4 = ["Option 1", "Option 2", "Option 3", "Option 4"]

# ---------------- Passage 1 ----------------
P.rc(1, "P1", "Purpose", "4", "Medium",
 "Read the sentence the example sits in. Whose view does it seem to confirm?",
 steps(("Where the example appears", ev(1, "The news seemed like vindication to those who had long warned that streaming was more about controlling access to the cultural commons than expanding it, as did reports (since denied by the show’s creators) that Netflix had begun editing old episodes of Stranger Things to retroactively improve their visual effects.") +
          p("The editing reports are offered alongside the removals as something that “seemed like vindication” for the sceptics.")),
       ("What it shows", p("The sceptics fear that streaming platforms can’t be trusted with films: they can pull them, or quietly alter them. The example is a practice that seems to bear out that fear."))) +
 final("Option 4."),
 "purpose",
 [("1", "The passage doesn’t argue that art is no longer sacrosanct or that change to suit tastes is acceptable; the example feeds a worry, not a general claim about art."),
  ("2", "Controlling access is illustrated by the removed titles. Editing an old episode doesn’t restrict anyone’s access."),
  ("3", "The author notes the denial in passing but doesn’t say that unconfirmed reports are increasing distrust.")])

P.rc(2, "P1", "Weaken", "4", "Medium",
 "First pin down the main argument: why are films at risk in every format? Then find the statement that removes that risk.",
 steps(("The main argument", p("Neither streaming, nor discs, nor digital purchases can be relied on to keep films available. Platforms remove titles, digital rights tie files to an account or a territory, and files themselves decay or go out of date.")),
       ("What would undo it", p("If studios and streaming services committed to perpetual, platform-independent access to what customers have paid for, the core worry, that access depends on the whims of the platform, would fall away."))) +
 final("Option 4."),
 "weaken",
 [("1", "Better cloud storage helps with data decay, but not with platforms removing titles or locking files to an account."),
  ("2", "A workaround for geo-blocking addresses only one example, and a fragile one; it leaves the rest of the argument standing."),
  ("3", "Discs lasting 100 years answers only the doubt about Blu-ray, not the argument about streaming and digital ownership.")])

P.rc(3, "P1", "Main_Idea", "4", "Medium",
 "The passage covers streaming, discs, digital purchases and file formats. What do they all have in common?",
 steps(("The thread through the passage", p("Each format seems to promise permanent access, and each one fails: titles vanish from streaming services, discs deteriorate, purchases are tied to territories and accounts, and files decay or fall out of date.")),
       ("The irony", ev(3, "audiences may start to wonder why those same studios seem happy to set the vault alight themselves") +
          p("The digital age should have made films easier to keep, yet the churn of technology and the decisions of platforms make access harder."))) +
 final("Option 4."),
 "inference",
 [("1", "The passage doesn’t ask us to give up the idea that classic works are unchanging and available; it laments that they are becoming harder to reach."),
  ("2", "Nothing is said about creators putting in less effort because they can edit later."),
  ("3", "The passage worries about availability but doesn’t argue that access must be free of who pays for it.")])

P.rc(4, "P1", "Inference", "1", "Medium",
 "“Back then” sets the past against today. What is the difference between the two?",
 steps(("Then", ev(3, "Back then, at least, cinema was defined by its ephemerality: the sense that a film was as good as gone once it left your local cinema.")),
       ("Now", ev(3, "Today, with film studios keen to stress the breadth of their back catalogues") +
          p("Today, films are sold on the idea of a lasting catalogue, so audiences expect them to stay available after their cinema run. That expectation is what makes the studios’ deletions so jarring."))) +
 final("Option 1."),
 "inference",
 [("2", "The passage spends most of its length showing that today’s technology does not reliably preserve films, so it can’t be the reason."),
  ("3", "“No reason” is too strong; the passage itself mentions business reasons, such as next quarter’s numbers."),
  ("4", "The sentence says what cinema was like, not how accepting people were of it.")])

P.va(5, P.ms(5), ["Option 3", "Option 4", "Option 1", "Option 2"], "MCQ", "1", "Missing_Sentence", "Medium",
 "The sentence is about how Renaissance music handled emotion. Which part of the paragraph is describing the character of the music rather than its history?",
 steps(("Two halves", p("The first half is history: the madrigals published in 1588, the boom that followed and its link with Italy. From “Renaissance music was mostly polyphonic” onwards, the paragraph describes how the music sounds.")),
       ("The fit at blank (3)", p("The sentence says the music portrayed emotions in a “balanced and moderate fashion”. The next sentence gives the evidence: “Extreme use of and contrasts in dynamics, rhythm, and tone colour do not occur.” That restraint is exactly what “balanced and moderate” means.")),
       ("Reading the options", p("Blank (3) appears as the first option, so the answer is option 1."))) +
 final("Blank (3), which is option 1."),
 "missing",
 [("2", "Blank (4) comes after the point about extremes, so the sentence would arrive after its own evidence."),
  ("3", "At blank (1) the paragraph is still telling the history of English madrigals; a remark on emotional balance has nothing to attach to."),
  ("4", "Blank (2) sits between the music boom and its Italian origin, which is still history, not character.")])

P.va(6, P.summ(6), P.Q["VARC"][6]["opts"], "MCQ", "2", "Summary", "Medium",
 "What has changed for cartographers, and why?",
 steps(("What the passage says", "<ol><li>Cartographers used to worry little about their readers.</li><li>Societal and technological developments have made readers more demanding, mostly because of the tools they use.</li><li>So cartographers now test whether their maps are efficient, effective and appreciated.</li></ol>"),
       ("Choosing", p("Option 2 keeps the change (cartographers now look at usability) and its cause (new technology)."))) +
 final("Option 2."),
 "summary",
 [("1", "It leaves out the cartographers and their new interest in usability, which is the point of the passage."),
  ("3", "The passage is about testing usability, not about putting new technology into maps."),
  ("4", "“A series of experiments” goes beyond the passage, and the summary drops the reason for the change.")])

# ---------------- Passage 2 ----------------
P.rc(7, "P2", "Detail", "2", "Easy",
 "Look at the end of the first paragraph, where the author raises the “broader question”.",
 steps(("The doubt", ev(1, "In a world where products and services often have to pass through regulatory hoops, large companies will usually have the advantage.")),
       ("What it means", p("Crafts may not create many jobs because small outfits struggle with regulation, while big firms can handle it more easily."))) +
 final("Option 2."),
 "detail",
 [("1", "The guilds’ resistance to newcomers is history, from the second paragraph; it isn’t the reason given for doubting jobs now."),
  ("3", "The author asks whether retraining truck drivers will be easy, but doesn’t say such workers are unlikely to opt for crafts."),
  ("4", "The passage never argues that crafts production is too small to absorb redundant labour.")])

P.rc(8, "P2", "Inference", "3", "Medium",
 "What does the second paragraph say about guilds and creativity? Then recall what the first paragraph said about mass production.",
 steps(("Guilds", ev(2, "History also suggests that the link between crafts and creativity is not automatic.") +
          p("Guilds were monopolies and hierarchies, and long apprenticeships could knock the innovative spirit out of young craftsmen.")),
       ("Mass production", p("Management studies valued efficiency and consistency, using standardised parts. That system was never about creativity either.")),
       ("The common ground", p("Neither one necessarily promoted creativity."))) +
 final("Option 3."),
 "inference",
 [("1", "Mass production prized efficiency and consistency, not quality above all."),
  ("2", "Restricting entry is true of the guilds, but nothing says mass production restricted entry."),
  ("4", "Hierarchy is mentioned for the guilds only; the passage says nothing about how egalitarian mass production was.")])

P.rc(9, "P2", "Except", "1", "Medium",
 "Find the sentence about the third crafts movement and the two markets. Which option isn’t among them?",
 steps(("What is driving the revival", ev(1, "A third crafts movement is emerging as people become aware of the environmental impact of conventional industry.") +
          ev(1, "The first stems from the existence of consumers who are willing to pay a premium price for goods that are deemed to be of extra quality") +
          ev(1, "The second market lies in those consumers who wish to use their purchases to support local workers")),
       ("The odd one out", p("Environmental concern, buyers who pay for quality and support for local workers are all named. Support for “individual creations” as against mass-produced objects is not given as a cause."))) +
 final("Option 1."),
 "except",
 [("2", "This is the first market: buyers willing to pay a premium for quality."),
  ("3", "This is the second market: buyers who want to support local workers."),
  ("4", "This is why the third crafts movement is emerging.")])

P.rc(10, "P2", "Inference", "1", "Hard",
 "“NOT inconsistent” means “consistent”. Which statement agrees with the passage?",
 steps(("The last line", ev(2, "Craft workers can thrive in the modern era, but only if they don’t get too organised.") +
          p("The guilds show what happens when crafts become too organised: they shut out newcomers and dull innovation. So creativity in crafts could indeed be stifled if things become too organised.")),
       ("The rest", p("The other three statements either reverse the passage or claim links it never makes."))) +
 final("Option 1."),
 "inference",
 [("2", "The Arts and Crafts movement was a reaction against the American system, not inspired by it."),
  ("3", "The passage says the link between crafts and creativity is “not automatic”, so creativity isn’t intrinsic to crafts."),
  ("4", "The agile manifesto is cited as a modern example of craft values; it isn’t linked to the guilds, which are criticised.")])

P.va(11, P.summ(11), P.Q["VARC"][11]["opts"], "MCQ", "3", "Summary", "Hard",
 "The passage lists animals’ abilities and emotions, then ends with an explanation. Which option keeps that explanation?",
 steps(("What the passage says", "<ol><li>Animals are intelligent and have remarkable senses.</li><li>Many animals show a wide range of emotions.</li><li>This isn’t surprising, because we share the brain structures that are the seat of emotions.</li></ol>"),
       ("Choosing", p("The passage closes on a reason: shared brain structures explain shared emotions. Option 3 keeps both the claim and its explanation. Option 4 states only the claim."))) +
 final("Option 3."),
 "summary",
 [("1", "The passage says animals’ senses can dwarf ours, not that they are more intelligent than us."),
  ("2", "The passage doesn’t say sensory abilities cause emotions; it gives the shared limbic system as the reason."),
  ("4", "This is true, but it leaves out the explanation that the passage builds up to.")])

# ---------------- Passage 3 ----------------
P.rc(12, "P3", "Detail", "4", "Easy",
 "Look at the last paragraph, where the new nickname appears.",
 steps(("The new name", ev(7, "With their constant digging, the bandicoots trap moisture and allow for seed germination so the cattle-damaged desert can restore itself. They have a new nickname—a flattering one, this time. “We call them ecosystem engineers,” Pedler says.")),
       ("Why", p("They earn the name by changing the dry desert: their digging traps moisture and helps seeds grow."))) +
 final("Option 4."),
 "detail",
 [("1", "The revival is the conservationists’ work; the bandicoots didn’t lead it."),
  ("2", "Rainfall caused the joey boom, not the other way round."),
  ("3", "From 20 to about 100 is fivefold, but that isn’t the reason for the name.")])

P.rc(13, "P3", "Vocabulary", "2", "Easy",
 "An enclosure keeps animals in. What would an “exclosure” keep out?",
 steps(("What the exclosures are", ev(6, "The imported bandicoots occupy two fenced “exclosures,” cleared of invasive rabbits (courtesy of Pedler’s sheepdog) and of feral cats (which slunk off once the rabbits disappeared).")),
       ("The point of the word", p("The fences are there to keep invasive animals out, so that the bandicoots are safe inside."))) +
 final("Option 2."),
 "detail",
 [("1", "Bilbies are kept in the Wild Training Zone, not removed, and nothing is cleared from the “main desert”."),
  ("3", "The predator-free islands are in Shark Bay; the exclosures are on the mainland preserve."),
  ("4", "Restoring the desert is what the bandicoots’ digging does, not what the fences are for.")])

P.rc(14, "P3", "Detail_Not_True", "2", "Medium",
 "Check each description against what the passage says. Be careful with “smallest”: smallest of what?",
 steps(("What the passage says", ev(2, "the zebra rat—the smallest bandicoot, more commonly known today as the western barred bandicoot") +
          p("It is the smallest <i>bandicoot</i>, not the smallest marsupial. The passage also gives it a long, slender muzzle, a black-striped rump, a pouch, and the habit of digging shallow, camouflaged shelters.")),
       ("The odd one", p("Option 2 calls it the smallest black-striped marsupial, which the passage doesn’t say."))) +
 final("Option 2."),
 "notrue",
 [("1", "It digs shallow shelters and has a muzzle “much too long”."),
  ("3", "The colonists called it the “zebra rat”, and it has a pouch and a slender snout."),
  ("4", "Long nose, black-striped back and a pouch all match.")])

P.rc(15, "P3", "Main_Idea", "2", "Easy",
 "The story moves from near-extinction to a rescue. Which option has both parts?",
 steps(("The arc of the passage", p("Imported animals nearly wiped out the western barred bandicoot on the mainland; it survived only on two islands. Now conservationists are using the island survivors to bring it back.")),
       ("Choosing", p("Option 2 covers the threat, the island remnant and the hope that rests on it."))) +
 final("Option 2."),
 "inference",
 [("1", "The colonists’ names are a colourful detail; the passage blames imported animals, not the names."),
  ("3", "The passage is about one kind of bandicoot, not marsupials in general."),
  ("4", "The species survived on two islands, so it did not go extinct, and the rescue is left out.")])

# ---------------- Passage 4 ----------------
P.rc(16, "P4", "Inference", "3", "Medium",
 "What did Becker export from economics, and what did he refuse to import?",
 steps(("Outward", ev(1, "applying methods honed in the study of markets to domains of nonmarket life")),
       ("Not inward", ev(1, "he did not let other ways of thinking enter his own economic realm") +
          p("He used economics to study crime and marriage, but never borrowed from anthropology or history."))) +
 final("Option 3."),
 "inference",
 [("1", "This reverses Becker: he applied economics elsewhere and refused to borrow."),
  ("2", "The paragraph doesn’t discuss whether economists benefited."),
  ("4", "The point is that Becker kept other disciplines out of economics, not that he guarded it from poachers.")])

P.rc(17, "P4", "Tone", "1", "Hard",
 "Read the phrase “once almighty” next to what follows. Is the author praising, attacking or gently mocking?",
 steps(("The words", ev(2, "Times have changed for the once almighty discipline. Economics has been taken to task, within and beyond its ramparts. Some economists have reached out, imported, borrowed, and collaborated—been less imperial, more open.") +
          p("“Once almighty”, “ramparts” and “less imperial” carry a wry edge. The author isn’t against the change; he is gently mocking a discipline that used to look down on others and now borrows from them.")),
       ("Matching the tone", p("Of the options, only “sarcastic” captures this mocking note about economists who earlier shunned other fields and now draw on them."))) +
 final("Option 1."),
 "inference",
 [("2", "The author welcomes the borrowing, as the rest of the passage shows; he isn’t critical of it."),
  ("3", "Nothing is said about economics failing to manage crises or falling from grace because of it."),
  ("4", "The paragraph doesn’t mention failures to predict markets.")])

P.rc(18, "P4", "Detail", "2", "Medium",
 "The last paragraph says what Shiller adds and what he leaves out. Focus on what is left out.",
 steps(("What Shiller does", ev(5, "Shiller [the Nobel prize winning economist] connects perceptions of narratives to changes in behavior and thence to social outcomes.")),
       ("What is missing", ev(5, "Yet institutions have been stripped from Shiller's account, to reveal a bare dynamic of emotions and economics, without the intermediating place of politics.") +
          p("So the criticism is that he ties emotion to behaviour without the institutions that once mediated between them."))) +
 final("Option 2."),
 "detail",
 [("1", "Shiller leaves institutions out; he doesn’t denigrate them."),
  ("3", "The author says politics and media played a “vital” role, not a marginal one."),
  ("4", "The author has no quarrel with storytelling; the complaint is the missing institutions.")])

P.rc(19, "P4", "Inference", "2", "Medium",
 "See how the passage describes the textbook economic agent in the third paragraph.",
 steps(("The textbook view", ev(3, "For generations, economists have presumed that people have interests—“preferences,” in the neoclassical argot—that get revealed in the course of peoples’ choices.") +
          ev(4, "homo economicus doesn’t always behave like the textbook maximizer")),
       ("So", p("Homo economicus is the rational person who acts on their own preferences to get the most out of their choices."))) +
 final("Option 2."),
 "inference",
 [("1", "Homo economicus is defined by market choices, not by nonmarket ones."),
  ("3", "Borrowing from other disciplines describes some modern economists, not the model person."),
  ("4", "The passage doesn’t describe homo economicus as immune to other people’s choices.")])

P.va(20, P.sents(20), [], "TITA", "1", "Odd_One_Out", "Hard",
 "Find the opener, then follow the pronouns: “He”, “As such”.",
 steps(("The chain", p("Sentence 4 introduces Singer’s book. Sentence 2 says he saw himself as a utilitarian with a direct theory of animal rights. Sentence 3 (“He argued…”) gives his argument: animals have significant interests. Sentence 5 (“As such…”) draws the conclusion: we owe animals direct moral duties.")),
       ("The extra sentence", p("Sentence 1 restates the argument in general terms with no link to Singer. It repeats what 3 already says and breaks the 4-2-3-5 chain."))) +
 final(r"\(1\)"),
 "oddone",
 [("4", "Introduces Singer and his book."), ("2", "Describes his position."), ("3", "“He argued…”: his reason."), ("5", "“As such…”: the conclusion.")],
 why_title="How the other sentences fit")

P.va(21, P.summ(21), P.Q["VARC"][21]["opts"], "MCQ", "4", "Summary", "Hard",
 "The passage says some codes only seem natural. What makes them seem so, and what does that hide?",
 steps(("What the passage says", "<ol><li>Some codes are so widespread and learned so early that they seem naturally given rather than constructed.</li><li>They are still codes; they have only been naturalized.</li><li>This hides the coding practices that are really at work.</li></ol>"),
       ("Choosing", p("Option 4 keeps all three points: language and visual signs are codes, some are so widespread they seem natural, and that appearance hides the coding."))) +
 final("Option 4."),
 "summary",
 [("1", "The passage says codes are constructed, not that they have a natural origin."),
  ("2", "Not all codes appear natural; only some, deeply habituated ones do."),
  ("3", "The passage says naturalization has an ideological effect, not that ideology aims at it.")])

P.va(22, P.sents(22), [], "TITA", "2", "Odd_One_Out", "Medium",
 "Most of the sentences are about a decline in public transport. Which one doesn’t fit that story?",
 steps(("The chain", p("Sentence 5 states the puzzle: public transport use is falling despite growing cities. Sentence 3 gives the usual explanations, and sentence 4 offers a deeper one: people need to travel less. Sentence 1 (“Urbanites also…”) adds a second cause: better alternatives.")),
       ("The extra sentence", p("Sentence 2 is a general remark about how more riders improve service. It doesn’t explain the decline."))) +
 final(r"\(2\)"),
 "oddone",
 [("5", "Sets up the puzzle."), ("3", "The blamed causes."), ("4", "A more likely, structural cause."), ("1", "“Also”: another reason people leave public transport.")],
 why_title="How the other sentences fit")

P.va(23, P.ms(23), ["Option 3", "Option 1", "Option 2", "Option 4"], "MCQ", "2", "Missing_Sentence", "Easy",
 "The sentence compares the brain to a tidy room. Which line in the paragraph follows on from that image?",
 steps(("The opener", p("The sentence says the brain isn’t organised like a home office or a medicine cabinet. The next line, “You can’t just put things anywhere you want to”, continues the image of arranging a room. So the sentence belongs at the very start, at blank (1).")),
       ("Reading the options", p("Blank (1) is listed as option 2."))) +
 final("Blank (1), which is option 2."),
 "missing",
 [("1", "Blank (3) comes after the point that there is no grand planner; the paragraph is already moving to the old-house image."),
  ("3", "At blank (2) the paragraph has already described the haphazard architecture; the opener would come too late."),
  ("4", "At the end the paragraph has already given its own image, the old house; another image would be a loose add-on.")])

P.va(24, P.ms(24), ["Option 1", "Option 4", "Option 2", "Option 3"], "MCQ", "2", "Missing_Sentence", "Medium",
 "The sentence is about why understanding the region matters. Look for a following sentence that begins with “It”.",
 steps(("The link", p("The last sentence reads “It allows us to see patterns and links … that remain invisible if one looks only at Europe, or North America.” Its “It” needs something to refer to. The missing sentence supplies it: understanding central Asia’s role.")),
       ("Placing it", p("So the sentence goes at blank (4), right before that “It”. Blank (4) is listed as option 2."))) +
 final("Blank (4), which is option 2."),
 "missing",
 [("1", "Blank (1) comes before the paragraph has explained why the region is central."),
  ("3", "Blank (2) interrupts the list of what travelled along the routes."),
  ("4", "Blank (3) sits between the dark side of the routes and the “central nervous system” image.")])
