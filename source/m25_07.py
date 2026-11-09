# -*- coding: utf-8 -*-
# Simp Mock 7 (2025): VARC (24 of 24). DILR and QA: m25_07_dilr.py, m25_07_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(7, "sm25_07.json", series=2025)
P.passage("V1", "Passage 1 — AI and the nuclear revival", "Science_and_Technology")
P.passage("V2", "Passage 2 — The idea of lived experience", "Philosophy_and_Psychology")
P.passage("V3", "Passage 3 — How hummingbirds manage energy", "Environment_and_Life_Science")
P.passage("V4", "Passage 4 — The uses and dangers of confidence", "Economics_and_Management")

P.va(1, P.summary_html(1, "As the Cold"), P.Q["VARC"][1]["opts"], "MCQ", "4", "Summary", "Hard",
 "After the Cold War, globalisation; it seems to cut us off from history and from our ancestors’ ways.",
 steps(("Choosing", p("Option 4 has the origin, the break with historical continuity, and the estrangement from past identities and traditions, without adding a verdict."))) +
 trap("Option 3 says people have lost their ‘authentic’ identity; the passage puts ‘authentic’ in quotes and says identities only ‘appear’ incompatible.") + final("Option 4"),
 "summary", [("1", "Leaves out the break with the flow of history."), ("2", "Copies a phrase; leaves out the estrangement from ancestors."), ("3", "‘Loss of authentic identity’ states as fact what the passage presents as appearance.")])

# ---------------- Passage 1 (Q2–5) ----------------
P.rc(2, "V1", "Inference_Except", "1", "Medium",
 "Is the passage confident about SMRs?",
 steps(("The appeal", p("Clean power around the clock for data centres (2), heavy investment by tech firms and startups (3), and scale and reliability versus wind and solar (4) are all given as reasons.")),
       ("The odd one", ev(4, "Still, the technology behind SMRs remains unproven at scale") +
          p("SMRs are not presented as commercially proven or transformative."))) + final("Option 1"),
 "except", [("2", "Stated in paragraph 1."), ("3", "Paragraphs 2–3."), ("4", "‘around the clock, unlike wind and solar’.")])
P.rc(3, "V1", "Inference_Except", "4", "Medium",
 "What is Vogtle an example of?",
 steps(("The example", ev(2, "These projects absorb enormous amounts of capital and are sensitive to interest-rate fluctuations and delays") +
          p("Vogtle illustrates cost overruns and delays (1), interest-rate exposure (2) and the resulting uncertain returns (3).")),
       ("The odd one", p("The shortage of decommissioned reactors comes before the example and is why new plants are needed; Vogtle doesn’t illustrate it."))) + final("Option 4"),
 "except", [("1", "‘far over budget and behind schedule’."), ("2", "Interest-rate sensitivity is the point it illustrates."), ("3", "Follows from capital risk.")])
P.rc(4, "V1", "Inference_Except", "3", "Medium",
 "Does the argument assume demand stays flat?",
 steps(("The argument", p("Nuclear is suited to AI’s growing power needs and will grow if finance and policy help.")),
       ("Assumptions", p("Governments warming to nuclear (1), nuclear being the best fit (2) and tech staying committed to clean power (4) all support the argument. The passage assumes demand will surge (‘five to six times as much electricity’), not stay constant."))) + final("Option 3"),
 "notrue", [("1", "Assumed: ‘Governments certainly seem to be warming’."), ("2", "Assumed throughout."), ("4", "Assumed: tech wants growth ‘without spewing carbon’.")])
P.rc(5, "V1", "Tone", "2", "Easy",
 "The paragraph lists obstacles and then what would help.",
 steps(("The paragraph", ev(4, "For it to continue, a mix of technical ingenuity, financial wizardry and supportive policy will be needed") +
          p("Obstacles admitted (unproven SMRs, uncertain costs) and remedies suggested (insurance, faster permits): measured optimism."))) + final("Option 2"),
 "inference", [("1", "Not ‘insurmountable’."), ("3", "The author does project a hopeful path."), ("4", "Risks are stated plainly.")])

# ---------------- Passage 2 (Q6–9) ----------------
P.rc(6, "V2", "Inference_Except", "4", "Medium",
 "What do existentialists say cultural categories do to experience?",
 steps(("What lived experience is", p("First-hand experience of social reality (1), tied to identities such as race and gender (2), and insight from marginalisation (3).")),
       ("The odd one", ev(1, "highlighting how dominant cultural categories distort one’s sense of self") +
          p("Cultural narratives are what distort lived experience; they aren’t part of it."))) + final("Option 4"),
 "except", [("1", "The movement’s definition."), ("2", "Sartre, de Beauvoir, Fanon."), ("3", "‘injustice(s)’.")])
P.rc(7, "V2", "Inference_Except", "2", "Medium",
 "Taylor’s three roles: authenticity, authority, policing boundaries.",
 steps(("The three", p("It marks authenticity (1), secures epistemic and political authority (3), and polices group boundaries (4).")),
       ("The odd one", ev(2, "marginalised people can’t fully understand their social reality because interpretive resources are dominated by the privileged") +
          p("Option 2 reverses Fricker’s point."))) + final("Option 2"),
 "except", [("1", "First role."), ("3", "Second role."), ("4", "Third role.")])
P.rc(8, "V2", "Inference", "3", "Easy",
 "‘Mediated’ means passed through something else.",
 steps(("Context", ev(3, "we can misunderstand our own experiences, distorted by ideology and oppression") +
          p("Experience is filtered through culture, society and ideology."))) + final("Option 3"),
 "inference", [("1", "The opposite."), ("2", "‘Completely unreliable’ goes too far."), ("4", "About communicating, not filtering.")])
P.rc(9, "V2", "Purpose", "1", "Medium",
 "What does Scott say lived experience can do to categories?",
 steps(("The point", ev(3, "Rather than liberating marginalised people, it can entrench the very categories that oppress them") +
          p("Appiah adds that experience can be distorted; hooks’ point leads into ‘a shaky basis for authenticity’. Together they show the risk of reinforcing oppression."))) + final("Option 1"),
 "purpose", [("2", "Concedes hooks’ point but isn’t the author’s argument."), ("3", "The author doubts this."), ("4", "The view the author criticises, not the point being made.")])

P.va(10, P.summary_html(10, "From a humanist"), P.Q["VARC"][10]["opts"], "MCQ", "3", "Summary", "Medium",
 "Problem: mechanised, perfection-seeking humanity. Counter: awe, with spontaneity and openness.",
 steps(("Choosing", p("Option 3 frames the problem and offers awe as a counterforce, not a cure."))) +
 trap("Options 1 and 4 call awe the antidote or a solution; the passage says ‘there is clearly no antidote as such’.") + final("Option 3"),
 "summary", [("1", "‘The antidote’ contradicts the passage."), ("2", "‘Deeper engagement’ is added; misses perfection-striving."), ("4", "Misses the roboticism framing.")])
P.va(11, P.missing_html(11), P.Q["VARC"][11]["opts"], "MCQ", "4", "Missing_Sentence", "Medium",
 "‘The controversy’ follows the anxiety; the next sentence weighs affordability against safety.",
 steps(("Find the spot", p("Blank 2 comes after reports of ineffective treatments ‘fueled anxiety’. The sentence turns that into a wider debate, and ‘Some experts warn … despite its goal of making healthcare affordable…’ continues it.")),
       ("Match the label", p("Blank 2 is choice 4, labelled ‘Option 2’."))) + final("Choice 4 (“Option 2”)"),
 "missing", [("1", "“Option 3”: after the experts’ warning, the debate has already been joined."), ("2", "“Option 1”: the controversy hasn’t been described."), ("3", "“Option 4”: after the official response.")])

# ---------------- Passage 3 (Q12–15) ----------------
P.rc(12, "V3", "Inference", "3", "Medium",
 "What follows the phrase?",
 steps(("Context", ev(1, "With their small size and blazing metabolism, they live on a knife-edge") +
          p("They sometimes shut their bodies down to survive. The knife-edge is the narrow margin between energy taken in and energy spent."))) + final("Option 3"),
 "inference", [("1", "Vague: ‘push their limits’ isn’t the point."), ("2", "Evolutionary constraints aren’t discussed."), ("4", "One example, not the meaning.")])
P.rc(13, "V3", "Detail_Not_True", "3", "Easy",
 "When does the passage say torpor helps?",
 steps(("The reasons", ev(2, "This can be essential after days of less feeding or before migration") +
          p("Plus cold nights. Defending feeders is mentioned only as behaviour in the first line."))) + final("Option 3"),
 "notrue", [("1", "‘during cold nights’."), ("2", "‘before migration’."), ("4", "‘after days of less feeding’.")])
P.rc(14, "V3", "Inference", "3", "Medium",
 "Pick the option that covers all the adaptations, not one of them.",
 steps(("The adaptations", p("Torpor, leaky guts, protection from glycation, switching to fat, shutting down kidneys: all let a tiny bird with a blazing metabolism meet its energy needs.")),
       ("Choosing", p("Options 1, 2 and 4 each name one adaptation; option 3 says why they matter together."))) + final("Option 3"),
 "inference", [("1", "One adaptation only."), ("2", "One adaptation only."), ("4", "One adaptation only.")])
P.rc(15, "V3", "Main_Idea", "4", "Hard",
 "How does the passage open, and what does it go on to cover?",
 steps(("The arc", ev(1, "For years, researchers assumed hummingbirds spent about 30 percent of their day feeding, resting most of the time") +
          p("Shankar finds they often work far harder. The passage then covers energy (torpor), sugar (leaky guts, glycation) and water (kidneys). Option 4 has the overturned assumption and all three.")),
       ("Why not 1", p("Option 1 omits hydration and the overturned assumption that frames the passage."))) + final("Option 4"),
 "inference", [("1", "Leaves out hydration and the opening finding."), ("2", "‘Primarily … feeding’ is too narrow."), ("3", "Lists challenges but not how the birds cope.")])

P.va(16, P.missing_html(16), P.Q["VARC"][16]["opts"], "MCQ", "3", "Missing_Sentence", "Hard",
 "‘This raises concerns about the role of AI in shaping public understanding’ needs AI’s growing role just before it.",
 steps(("Find the spot", p("Blank 3 follows ‘As AI becomes a more dominant force in news consumption, ensuring reliability and accountability … is crucial.’ The sentence draws the consequence; the next one offers a fix (human oversight).")),
       ("Match the label", p("Blank 3 is choice 3, labelled ‘Option 3’."))) +
 trap("Blank 1 is tempting, but the next sentence goes on describing the study; a concern placed there interrupts the evidence.") + final("Choice 3 (“Option 3”)"),
 "missing", [("1", "“Option 1”: breaks the description of the study."), ("2", "“Option 2”: in the middle of the challenges."), ("4", "“Option 4”: after the conclusion.")])

# ---------------- Passage 4 (Q17–20) ----------------
P.rc(17, "V4", "Purpose", "3", "Easy",
 "Why is the hedged version ‘a lot less persuasive’?",
 steps(("The point", ev(1, "Someone declaring a position with ringing certainty is more likely to inspire than someone who hedges their bets") +
          p("The joke shows that confidence in a strong message inspires."))) + final("Option 3"),
 "purpose", [("1", "Adapting to circumstances is what the joke mocks."), ("2", "The opposite."), ("4", "Humour is the device, not the point.")])
P.rc(18, "V4", "Inference", "1", "Hard",
 "What do the findings of these researchers have in common?",
 steps(("Their findings", ev(2, "overconfident bosses are more likely to undertake acquisitions. They are also more likely to destroy value") +
          ev(2, "overconfident executives who make mistakes continue to be wrong for longer") +
          p("Confidence brings rewards (entrepreneurial success) but, inflated, leads to unsound decisions. The passage’s remedy is guardrails; option 1 fits all of them best.")),
       ("Why not 2", p("Self-doubt is the author’s point, not these researchers’ findings."))) + final("Option 1"),
 "inference", [("2", "Not what these studies found."), ("3", "The opposite: they found overconfidence."), ("4", "The author’s remark, not their research.")])
P.rc(19, "V4", "Inference", "2", "Hard",
 "Find the statement the passage supports; if that were false, the passage would be contradicted.",
 steps(("The line", ev(3, "A confident person is apt to place even more faith in their abilities if they have success") +
          p("Fast’s study then shows people betting more and losing more. Option 2 is what the passage says; denying it contradicts the passage.")),
       ("The others", p("Options 1, 3 and 4 are already false by the passage, so their being false is consistent."))) + final("Option 2"),
 "inference", [("1", "‘Always’ is false by the passage."), ("3", "Already contradicted: overconfidence matters."), ("4", "The passage doesn’t rank them.")])
P.rc(20, "V4", "Application", "4", "Easy",
 "What is optimal confidence?",
 steps(("The ideal", ev(3, "an optimally confident person trusts their own judgment while accepting it can be fallible") +
          p("Belief plus awareness of limits: option 4."))) + final("Option 4"),
 "inference", [("1", "Overconfident."), ("2", "‘No major weaknesses’."), ("3", "‘Perfectly’.")])

# ---------------- Odd one out (Q21–22) ----------------
P.va(21, P.sent_html(21), [], "TITA", "3", "Odd_One_Out", "Medium",
 "Four sentences describe the town and its factory. One turns to industry-wide problems.",
 steps(("The chain", p("5 → 2 → 4 → 1: arriving, you see the factory (5); the complex beside the theme park (2); a factory around which a city grew (4); everyone knows someone who works there (1).")),
       ("The odd one", p("Sentence 3 begins ‘Today, however…’ and introduces the car industry’s problems, a new topic."))) + final("3"),
 "oddone", [("1", "The local view."), ("2", "The complex."), ("4", "The city and the factory."), ("5", "The opening scene.")], why_title="How the other sentences fit")
P.va(22, P.sent_html(22), [], "TITA", "2", "Odd_One_Out", "Medium",
 "Four sentences trace the wicket from a sheep-pen gate. One is about the ball.",
 steps(("The chain", p("3 → 5 → 1 → 4: boys bowled at a stump or a hurdle gate (3); the gate had uprights and a crossbar called a bail (5); the bail made the gate preferable (1); the wicket and pitch were later fixed (4).")),
       ("The odd one", p("Sentence 2 is about the ball’s history."))) + final("2"),
 "oddone", [("1", "Why the gate was used."), ("3", "The origin."), ("4", "Later rules."), ("5", "The gate described.")], why_title="How the other sentences fit")

P.va(23, P.missing_html(23), P.Q["VARC"][23]["opts"], "MCQ", "4", "Missing_Sentence", "Easy",
 "‘This long-awaited showcase’ needs the exhibition just before it.",
 steps(("Find the spot", p("Blank 1 follows ‘an exhibition of his artworks is being held in the country for the first time’.")),
       ("Match the label", p("Blank 1 is choice 4, labelled ‘Option 1’."))) + final("Choice 4 (“Option 1”)"),
 "missing", [("1", "“Option 4”: at the end, after the analysis of the works."), ("2", "“Option 2”: about the curator and India."), ("3", "“Option 3”: inside the description of the images.")])
P.va(24, P.summary_html(24, "The anthropologist Clifford"), P.Q["VARC"][24]["opts"], "MCQ", "1", "Summary", "Hard",
 "Epochalism; old structures persist; we never step outside history.",
 steps(("Choosing", p("Option 1 has the term, the persistence of structures, and the closing point that history is not easily left behind."))) + final("Option 1"),
 "summary", [("2", "Leaves out the point about history."), ("3", "Leaves out neoliberalism and the closing point."), ("4", "‘Entirely trapped’ overstates.")])
