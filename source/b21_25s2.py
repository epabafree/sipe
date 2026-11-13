# -*- coding: utf-8 -*-
# Batch 21 — CAT 2025 Slot 2: VARC (Q1–24). DILR and QA are added by b21_25s2_dilr.py and b21_25s2_qa.py.
# Question numbers follow the order of the actual exam.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2025, 2, "ex21_25s2.json")
P.passage("P1", "Passage 1 — What cavefish gained when they lost their eyes", "Environment_and_Life_Science")
P.passage("P2", "Passage 2 — Instruments and the cultures of science", "Philosophy_and_Psychology")
P.passage("P3", "Passage 3 — Literature and the sense of place", "Arts_and_Literature")
P.passage("P4", "Passage 4 — The trustworthy voice of chatbots", "Science_and_Technology")

# ---------------- Passage 1 ----------------
P.rc(1, "P1", "Weaken", "4", "Medium",
 "Riddle concluded that carotenoids are not linked to having or lacking eyes. Which result would show a link after all?",
 steps(("Riddle’s inference", ev(5, "researchers see no link between eye presence or size and the accumulation of carotenoids")),
       ("What would overturn it", p("If only eyeless offspring had yellow (carotenoid-rich) fat, eyelessness and carotenoids would go together, which is exactly the link Riddle rules out."))) +
 final("Option 4."),
 "weaken",
 [("1", "Eyed fish with white fat fits “no link”."),
  ("2", "Eyed fish with yellow fat also fits “no link”."),
  ("3", "The passage itself reports eyeless fish with white fat; it supports Riddle.")])

P.rc(2, "P1", "Inference", "3", "Medium",
 "Why must cavefish embryos start making an eye at all?",
 steps(ev(2, "“The early development of the brain and the eye are completely intertwined—they happen together,” she says. That means the least disruptive way for eyelessness to evolve may be to start making an eye and then get rid of it.") +
       p("Cavefish embryos develop like surface fish at first because eye and brain form together. So building and then destroying the eye can’t be skipped.")) +
 final("Option 3."),
 "inference",
 [("1", "The passage gives no role to darkness in killing the eye cells."),
  ("2", "The enhancements don’t explain why the eye has to start forming."),
  ("4", "Food supply explains why unused tissue is costly, not why the eye must begin forming.")])

P.rc(3, "P1", "Inference", "4", "Easy",
 "Riddle’s final suggestion about carotenoids is the answer.",
 steps(ev(5, "Instead, Riddle thinks these carotenoids may be another adaptation to suppress inflammation") +
       ev(4, "“But when these cells get too big, they can burst, which is why we often see chronic inflammation in humans and other animals that have stored a lot of fat in their tissues.”")) +
 final("Option 4."),
 "inference",
 [("1", "The yellow colour is a side effect, not the function."),
  ("2", "Experiments found no link with eyes."),
  ("3", "The passage links carotenoids to inflammation, not to storing nutrients.")])

P.rc(4, "P1", "Except", "2", "Medium",
 "Three quotes are about cavefish and their conditions. One is a general fact about fat cells.",
 steps(p("The quote about fat cells bursting describes what happens in humans and other animals in general. It explains why inflammation matters, but it doesn’t describe anything cavefish have adapted.")) +
 final("Option 2."),
 "except",
 [("1", "Surviving on a meagre diet is part of how cavefish have adapted."),
  ("3", "Shedding costly tissue they don’t use is an adaptation."),
  ("4", "Getting very fat when food arrives is an adaptation to scarcity.")])

P.va(5, P.sents(5), [], "TITA", "3", "Odd_One_Out", "Hard",
 "Four sentences describe the show: its format, Torres’s look, delivery and ideas. One is a verdict.",
 steps(("The chain", p("Sentence 4 describes the show’s format. Sentence 1 describes Torres himself, sentence 2 his delivery, and sentence 5 his ideas.")),
       ("The extra sentence", p("Sentence 3 is a closing verdict and mentions a “colour-scouting mission” that none of the others set up. It sits outside the descriptive run."))) +
 final(r"\(3\)"),
 "oddone",
 [("4", "The format of the show."), ("1", "Torres’s appearance."), ("2", "His delivery."), ("5", "His ideas.")],
 why_title="How the other sentences fit")

P.va(6, P.sents(6, P.PJ_DIR), [], "TITA", "2413", "Para_Jumble", "Easy",
 "Start with the familiar experience, then the explanation, then the details.",
 steps(("The order", p("Sentence 2 introduces the smell of old books. Sentence 4 (“This familiar aroma…”) says it comes from chemical changes. Sentence 1 explains the changes: cellulose and lignin breaking down into volatile compounds. Sentence 3 (“These compounds…”) names them."))) +
 final("2413"),
 "pj",
 [("2", "Introduces the smell."), ("4", "“This familiar aroma” is chemical."), ("1", "The chemistry: compounds released."), ("3", "“These compounds” named.")],
 why_title="Why each sentence goes where it does")

P.va(7, P.ms(7), P.Q["VARC"][7]["opts"], "MCQ", "1", "Missing_Sentence", "Medium",
 "The sentence is about rumours that the cloth wasn’t made by human hands. Where would the real story of how it was made follow best?",
 steps(("The fit", p("After “This was Dhaka Muslin — the world’s most coveted cloth”, the sentence adds that Western customers thought it must be the work of mermaids or fairies. The paragraph then answers the rumour with the real process: handspun from a rare cotton and woven with a 16-step ritual. So the sentence belongs at blank (1).")),
       ("Reading the options", p("Blank (1) is option 1."))) +
 final("Blank (1), which is option 1."),
 "missing",
 [("2", "Blank (2) interrupts the account of the cotton plant."),
  ("3", "Blank (3) sits between the cotton flower and the spinning."),
  ("4", "At blank (4) the paragraph has already explained how the cloth was made, so the rumour comes too late.")])

P.va(8, P.sents(8), [], "TITA", "3", "Odd_One_Out", "Medium",
 "The paragraph is about new research on Pfas and health. Which sentence is about something else?",
 steps(("The chain", p("Sentence 1 says what Pfas are. Sentence 2 reports the new research linking them to gene changes and disease. Sentence 4 says the research may point to other diseases, and sentence 5 says what the findings mean for doctors.")),
       ("The extra sentence", p("Sentence 3 explains why Pfas are called “forever chemicals”: they don’t break down. That is about the environment, not the health research."))) +
 final(r"\(3\)"),
 "oddone",
 [("1", "What Pfas are."), ("2", "The new research."), ("4", "What else it may reveal."), ("5", "What the findings mean.")],
 why_title="How the other sentences fit")

# ---------------- Passage 2 ----------------
P.rc(9, "P2", "Inference", "4", "Medium",
 "Three options misstate the history or invent distinctions. Which one matches the passage’s comparison?",
 steps(ev(1, "remains largely a “receptive” science, dependent upon instrumentation which can detect and receive emissions") +
       ev(2, "Here, particularly with the development of biotechnology, instrumentation is far more interventional than in the astronomy case.")) +
 final("Option 4."),
 "inference",
 [("1", "Galileo, not Newton, observed the phases of Venus and Jupiter’s moons."),
  ("2", "The “new astronomy” opens the whole electromagnetic spectrum; Newton’s telescopes stayed within visible light."),
  ("3", "The passage says all these sciences are instrumentally embodied; it doesn’t set interventional against embodied instruments.")])

P.rc(10, "P2", "Inference", "2", "Easy",
 "The sentence refers to “both disciplines”. Which two?",
 steps(ev(2, "Yet, in both disciplines, the sciences involved are today highly instrumentalized and could not progress successfully without constant improvements upon the respective instrumental trajectories.") +
       p("Astronomy and microbiology both progress through improvements in their instruments.")) +
 final("Option 2."),
 "inference",
 [("1", "This jumbles the passage’s terms without saying anything it claims."),
  ("3", "Scientific constants aren’t mentioned."),
  ("4", "“Must be respected” turns a description into an instruction.")])

P.rc(11, "P2", "Application", "3", "Medium",
 "The passage sorts instruments into receptive ones and interventional ones. Which item does neither?",
 steps(p("An oven and a scalpel act on things; a saxophone can produce or be studied for sound. A milestone simply marks a distance: it neither receives signals nor intervenes in anything.")) +
 final("Option 3."),
 "inference",
 [("1", "An oven intervenes: it transforms what is put in it."),
  ("2", "A scalpel is a plainly interventional tool."),
  ("4", "A saxophone acts on air to produce sound.")])

P.rc(12, "P2", "Weaken", "1", "Hard",
 "The passage opens by saying different sciences have different cultures. Does mathematics lack one until now?",
 steps(ev(1, "Different sciences exhibit different science cultures and practices.") +
       ev(2, "perhaps the last of the scientific disciplines to move into such technical embodiment is mathematics") +
       p("The passage treats mathematics as a science that is only now becoming technically embodied, not one that is only now gaining a scientific culture. Saying its culture depends on computers contradicts this.")) +
 final("Option 1."),
 "weaken",
 [("2", "The passage doesn’t say an instrument can’t be both."),
  ("3", "Microscopy moving beyond visible light is consistent with the passage."),
  ("4", "Gravity isn’t discussed, so this doesn’t contradict anything.")])

P.va(13, P.ms(13), P.Q["VARC"][13]["opts"], "MCQ", "4", "Missing_Sentence", "Hard",
 "The sentence contrasts taste with judgment. Where has the paragraph just described taste becoming central?",
 steps(("The fit", p("Before blank (3), the paragraph says taste took on a new meaning and became a central category for aesthetic and ethical thinking. The missing sentence then explains why taste, rather than judgment, is the right focus: it keeps a link to pleasure and the body. After it, “Tracing the history of taste…” continues naturally. So it goes at blank (3).")),
       ("Reading the options", p("Blank (3) is listed fourth, so the answer is option 4."))) +
 final("Blank (3), which is option 4."),
 "missing",
 [("1", "Blank (4) is the end, after the point about neglected thinkers."),
  ("2", "At blank (2) the historical change hasn’t yet been described."),
  ("3", "At blank (1) Denneny and his focus haven’t been introduced.")])

P.va(14, P.summ(14), P.Q["VARC"][14]["opts"], "MCQ", "3", "Summary", "Medium",
 "The passage ends by rejecting an old idea. Which summary keeps that and the evidence?",
 steps(("What the passage says", "<ol><li>Humans have long created mosaics of habitats that support diverse life.</li><li>Human presence was about as likely to increase biodiversity as reduce it.</li><li>So the idea that humans are opposed to nature, and that nature thrives without us, is wrong.</li></ol>"),
       ("Choosing", p("Option 3 keeps the rejected idea, the evidence and the varied landscapes."))) +
 final("Option 3."),
 "summary",
 [("1", "It leaves out the main point, the rejection of humans as antithetical to nature."),
  ("2", "It drops the historical evidence and treats meadows as things humans preserve rather than create."),
  ("4", "It ties the whole argument to the early Holocene and misses the balance of the evidence.")])

P.va(15, P.summ(15), P.Q["VARC"][15]["opts"], "MCQ", "4", "Summary", "Hard",
 "Who lost what, and to whom? A good summary keeps the irony of the anti-monopoly game.",
 steps(("What the passage says", "<ol><li>A left-wing feminist invented the game to warn against monopolies, with two rule sets.</li><li>An unemployed man sold a simplified version and was credited as sole inventor.</li><li>She received $500 and no royalties, and her name and message were forgotten.</li></ol>"),
       ("Choosing", p("Option 4 keeps who she was, how she lost the credit, the one version that was sold, and the meagre payment."))) +
 final("Option 4."),
 "summary",
 [("1", "It focuses on Parker Brothers’ intent and loses the story of who lost the credit."),
  ("2", "It repeats Darrow’s basement tale, which the passage treats as the false official story."),
  ("3", "Calling them celebrated icons and Magie a feminist icon adds what the passage doesn’t say.")])

P.va(16, P.sents(16, P.PJ_DIR), [], "TITA", "1423", "Para_Jumble", "Hard",
 "Sentence 4 begins “Beneath this contradictory notion of film adaptations as … dual citizenship”. Which sentence introduces that notion?",
 steps(("The opener", p("Sentence 1 introduces “literature on screen”: adaptations as both cinema and literature.")),
       ("The link", p("Sentence 4 picks this up as “dual citizenship” and names a deeper legacy: literature is assumed to be the context for studying adaptations.")),
       ("The evidence and the verdict", p("Sentence 2 shows that legacy: even though films draw on many sources, adaptation studies stay attached to literature. Sentence 3, “It is as if…”, interprets why."))) +
 final("1423"),
 "pj",
 [("1", "Introduces the dual notion."), ("4", "“Beneath this contradictory notion”: the legacy."), ("2", "Evidence of the legacy."), ("3", "“It is as if”: the interpretation.")],
 why_title="Why each sentence goes where it does")

# ---------------- Passage 3 ----------------
P.rc(17, "P3", "Inference", "4", "Medium",
 "What does bridging the arts and sciences help us understand?",
 steps(ev(3, "The pursuit of such a topic speaks to the valuable knowledge produced from bridging disciplines and combining material from both the arts and the sciences to better understand the human condition.")) +
 final("Option 4."),
 "inference",
 [("1", "This scrambles the terms of the statement."),
  ("2", "This reverses the direction: the aim is understanding the human condition."),
  ("3", "This reverses cause and effect.")])

P.rc(18, "P3", "Detail_Not_True", "2", "Medium",
 "The second paragraph says the emotional component is as real as the map. Does it say it can replace the map?",
 steps(ev(2, "This emotional component, although subjective, is no less “real” than a surveyor’s map.") +
       p("“No less real” puts the two side by side; the passage later says both approaches are needed. Nothing says the emotional experience replaces the map.")) +
 final("Option 2."),
 "notrue",
 [("1", "The spiritual or emotional side is “no less real”."),
  ("3", "Literature supplies the emotional component that science misses."),
  ("4", "Histories of places live on in memory or imagination.")])

P.rc(19, "P3", "Purpose", "4", "Easy",
 "Look at the example in the last paragraph.",
 steps(ev(4, "how people from different races or classes can experience the same place in different ways linked to those racial or class disparities")) +
 final("Option 4."),
 "purpose",
 [("1", "Architects calibrating light and noise aren’t mentioned."),
  ("2", "Absence is a separate point made in the next sentence."),
  ("3", "The passage says both approaches are necessary, not that science is more accurate.")])

P.rc(20, "P3", "Except", "1", "Hard",
 "If a statement is something the passage affirms, its being false would contradict the passage. Which statement does the passage itself deny?",
 steps(p("Option 1 says people relate to places only physically. The passage rejects that, so if option 1 is false, the passage is untouched.") +
       ev(2, "In human experience, geographical places have a spiritual or emotional component in addition to and as part of a physical layout and topography.") +
       p("Options 2, 3 and 4 are things the passage supports, so their being false would contradict it.")) +
 final("Option 1."),
 "except",
 [("2", "Movement and migration are concerns literature can illuminate."),
  ("3", "Literary description, not imagery, conveys the human sense of place."),
  ("4", "The language of the senses is how humans know physical space.")])

# ---------------- Passage 4 ----------------
P.rc(21, "P4", "Except", "2", "Medium",
 "The beige-building image is about the tone and blandness of chatbot language. Which option is about something else?",
 steps(ev(2, "People often describe chatbots’ textual output as “bland” or “generic” – the linguistic equivalent of a beige office building.") +
       ev(2, "This appears to be bound up with making us feel safe") +
       p("Blaming training data comes up later, when the author questions the chatbot; it has nothing to do with the beige comparison.")) +
 final("Option 2."),
 "except",
 [("1", "Feeling safe and trusting is part of the design described."),
  ("3", "Polite, empathetic, collegial: the tone of the beige building."),
  ("4", "“Bland” or “generic” output.")])

P.rc(22, "P4", "Purpose", "1", "Medium",
 "Three examples show the products producing biased or slanted output. One is the chatbot describing itself.",
 steps(p("The Bing images, the edited Indian English and the flattering description of Altman are all outputs that show bias. ChatGPT’s answer about its own rhetoric is a self-description, not an example of a biased result.")) +
 final("Option 1."),
 "purpose",
 [("2", "This shows output slanted in favour of big tech."),
  ("3", "This shows gender bias."),
  ("4", "This shows a US-centric cultural norm.")])

P.rc(23, "P4", "Except", "2", "Hard",
 "The disjunct is between what companies claim (neutral, helpful) and what the products do. Which quote only expresses the author’s uncertainty?",
 steps(ev(4, "I’m not aware of research on whether ChatGPT tends to favor big tech, OpenAI or Altman, and I can only guess why it seemed that way in our conversation.") +
       p("This sentence admits the author can’t establish a gap; it doesn’t affirm one. The veneer of neutrality lulling users and the all-male images show the gap directly.")) +
 final("Option 2."),
 "except",
 [("1", "The “veneer of collegial neutrality” versus absorbing biased responses is the gap itself."),
  ("3", "This is the author’s framing of user complicity; it doesn’t cut against the gap."),
  ("4", "An all-male cast contradicts claims of neutral output.")])

P.rc(24, "P4", "Inference", "2", "Easy",
 "What does the author say the neutral tone does to our thinking?",
 steps(ev(4, "the product’s veneer of collegial neutrality could lull us into absorbing false or biased responses without much critical engagement")) +
 final("Option 2."),
 "inference",
 [("1", "The author says we are complicit."),
  ("3", "Funders seek a return, and trust helps drive use."),
  ("4", "The author reports that ChatGPT seemed to favour them, while admitting it is only a guess.")])
