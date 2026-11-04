# -*- coding: utf-8 -*-
# VARC — CAT 2023 Slot 1 pilot. Question/option/passage text is reused verbatim from the extraction;
# this file holds the rewritten solutions.
from fmt import steps, final, trap, ev, why, p

STRAT = {
 "except": p("<b>EXCEPT / NOT questions:</b> first say the passage’s main claim in one line. Three options will agree with it. The answer is the one that <i>reverses</i> or ignores it."),
 "pair": p("<b>Odd-pair questions:</b> give each pair’s relationship a one-word label, such as “has this feature” or “lacks this feature”. The odd pair is the one whose label differs."),
 "weaken": p("<b>Weaken–EXCEPT questions:</b> identify the claim, including both sides if it is a contrast. Three options attack one side. The answer usually <i>agrees</i> with the passage and reads like a paraphrase of one of its lines."),
 "notrue": p("<b>“Not true” questions:</b> check each option against a specific line. Wrong answers often swap one key word for its opposite, as “South–South” becomes “north–south” here."),
 "missing": p("<b>Missing-sentence questions:</b> look at the sentence <i>after</i> each gap. A pronoun or “this/these” that only the new sentence can explain marks the right gap."),
 "oddone": p("<b>Odd one out:</b> build the strongest chain first, using linking words such as “this capacity” and “the capacity”. The leftover sentence is usually on topic but does a <i>different job</i>."),
 "pj": p("<b>Para-jumbles:</b> fix two links first: a question followed by its answer, and a keyword hand-off from one sentence to the next. Two fixed links leave very few possible orders."),
 "summary": p("<b>Summary questions:</b> remove options that contradict the text or add something new. Of what remains, pick the one that keeps the passage’s cause → effect structure."),
}

SOL = {}

SOL[1] = dict(
 hint=p("Pin down what the author means by “remapping” first, then see which option points the other way."),
 solution=steps(
  ("Define “remapping”", p("It is the shift of the reader’s mental map away from a Europe/US-centred world, towards the global south.") + ev(2, "This has the effect of remapping the world in the reader’s mind, as centred in the interconnected global south.")),
  ("Check the options against it", p("Options 1, 3 and 4 all move the centre towards the global south or away from the West, so each one contributes.")),
  ("Find the one that reverses it", p("Option 2 puts the origin of cosmopolitanism in the <b>West</b>. The passage says the opposite.") + ev(3, "what we now call globalisation first appeared in the Indian Ocean")),
 ) + final("Option 2 re-centres the West, so it is the one claim that does not contribute.")
   + trap("Option 3 sounds bold (“the first centre of globalisation”), but it is almost a quotation from ¶3."),
 concept=STRAT["except"],
 why=why([
  ("1", "Contributes: the novels move beyond “the village or nation”, the land-focused, inward-looking world of early postcolonial fiction (¶1–2)."),
  ("3", "Contributes: globalisation “first appeared in the Indian Ocean”, which is in the global South (¶3)."),
  ("4", "Contributes: in this fiction “sailors and travellers are not all European”; African, Indian and Arab characters are traders and nakhodas (¶5)."),
 ]))

SOL[2] = dict(
 hint=p("Label each pair as “the passage gives it this feature” or “the passage denies it this feature”."),
 solution=steps(
  ("Label each pair", p("Three pairs link a subject to a feature the passage <b>gives</b> it. One pair links a subject to a feature the passage <b>denies</b> it.")),
  ("Spot the contrast pair", p("Early postcolonial novels were the opposite of border-crossing:") + ev(1, "land-focused and inward-looking") +
     p("Border-crossing belongs to the <i>Indian Ocean</i> novels:") + ev(2, "full of movement, border-crossing and South-South interconnection")),
 ) + final("Option 1, Postcolonial novels : Border-crossing, is a contrast pair while the other three are characteristic pairs.")
   + trap("“Indian Ocean world : Slavery” feels jarring, but the passage says “slavery is rife” (¶5), so it is a genuine characteristic."),
 concept=STRAT["pair"],
 why=why([
  ("2", "Characteristic: Indian Ocean novels reveal “a world that is outward-looking” (¶2)."),
  ("3", "Characteristic: in the Indian Ocean world “slavery is rife” (¶5)."),
  ("4", "Characteristic: postcolonial novels were “important for supporting anti-colonial nationalism” (¶1)."),
 ]))

SOL[3] = dict(
 hint=p("The claim is a contrast with two sides. Three options attack one side or the other; look for the one that agrees."),
 solution=steps(
  ("State the claim", p("It is a <b>contrast</b>. Mainstream English fiction is centred on Europe/US, Christianity and whiteness. Indian Ocean novels show an Islamic space, characters of colour, and an active, <i>non-romanticised</i> Africa.") + ev(4, "Those [commonly found ones] are mostly centred in Europe or the US, assume a background of Christianity and whiteness")),
  ("Sort the options", p("Option 1 attacks the mainstream side. Options 2 and 3 attack the Indian Ocean side.")),
  ("Find the one that agrees", p("Option 4 restates the passage’s picture of mainstream fiction (Christian, white, travel and adventure). It <b>strengthens</b> the contrast.")),
 ) + final("Option 4: it supports the claim instead of weakening it.")
   + trap("Options 2 and 3 seem to be only about Africa, but they undermine the Indian Ocean side of the contrast."),
 concept=STRAT["weaken"],
 why=why([
  ("1", "Weakens: it denies that mainstream fiction is set in Western centres (“places like Paris and New York”, ¶4)."),
  ("2", "Weakens: an Orientalist picture of “cultural crudeness” contradicts Africa playing “an active role in its long, rich history” (¶5)."),
  ("3", "Weakens: a nostalgic, idyllic picture contradicts “This does not mean that Indian Ocean Africa is romanticised” (¶5)."),
 ]))

SOL[4] = dict(
 hint=p("Find the passage’s own phrase for the kind of interconnection these networks create."),
 solution=steps(
  ("Find what the passage says about the networks", p("They link East Africa, the Arab coasts, and South and East Asia, all in the global south.") + ev(2, "full of movement, border-crossing and South-South interconnection")),
  ("Test option 3", p("“Connected the global <b>north</b> with the global south” swaps “South–South” for north–south. Nothing in the passage supports it.")),
 ) + final("Option 3 is not true.")
   + trap("Option 2’s abstract wording (“location rather than proximity”) looks unsupported, but it paraphrases ¶3."),
 concept=STRAT["notrue"],
 why=why([
  ("1", "True: migration is “often a matter of force” and travel is “abandonment rather than adventure”, yet the history is “long, rich” (¶5). The experience was mixed, i.e. ambivalent."),
  ("2", "True: “port cities very far apart were often more easily connected to each other than to much closer inland cities” (¶3)."),
  ("4", "True: a “largely Islamic space” with traders and nakhodas means religious and commercial histories shape the networks (¶4–5)."),
 ]))

SOL[17] = dict(
 hint=p("Look at the sentence right after each gap. Which one starts with a word that needs something before it?"),
 solution=steps(
  ("Find the hook", p("The sentence after gap (3) begins “<b>They</b> shared similarities in how they crafted stemmed projectile points…”. It needs a plural subject and a mention of “similarities” just before it.")),
  ("Check the fit", p("The new sentence supplies both: “archaeological similarities between the Paleolithic peoples of China, Japan, and the Americas”. It also bridges Li’s <i>genetic</i> finding before the gap and the <i>crafting</i> example after it.")),
  ("Match to the answer choices", p("Gap (3) is answer choice <b>3</b>, labelled “Option 3”.")),
 ) + final("Choice 3: the sentence goes in gap (3).")
   + trap("The answer choices are shuffled labels: choice 1 says “Option 2” and choice 4 says “Option 1”. Read the label, not the position."),
 concept=STRAT["missing"],
 why=why([
  ("1", "“Option 2” = gap (2): this interrupts the migration story, and Li’s quote then loses its lead-in."),
  ("2", "“Option 4” = gap (4): “They shared similarities…” would then have nothing to refer back to."),
  ("4", "“Option 1” = gap (1): it is too early, since the discovery’s details haven’t been given yet."),
 ]))

SOL[19] = dict(
 hint=p("Find the opening sentence: which one introduces “the capacity” that the others keep referring to?"),
 solution=steps(
  ("Find the opener", p("Sentence 5 introduces the topic: the ability to read other people’s behaviour in terms of their mental states.")),
  ("Build the chain", p("<b>5 → 1 → 4 → 3</b>: why it matters (1), how “this capacity” develops in a person (4), how “the capacity” evolved in the species (3).")),
  ("Spot the different job", p("Sentence 2 is about <b>terminology</b>: what to call the capacity. It also repeats a benefit that sentence 1 already states more precisely, so it has no clean place in the chain.")),
 ) + final("The odd sentence is 2.")
   + trap("The odd sentence is usually on topic, which is why it feels like it belongs. Ask what <i>job</i> each sentence does."),
 concept=STRAT["oddone"], why_title="How the other sentences fit",
 why=why([
  ("5", "Opens the paragraph: introduces the capacity."),
  ("1", "Explains why the capacity matters: language, social interaction, moral judgment."),
  ("4", "“This capacity develops…”: development in one person, from infancy to adulthood."),
  ("3", "“The capacity evolved…”: development in the species, over millions of years."),
 ]))

SOL[21] = dict(
 hint=p("One sentence asks a question and the next one answers it. Find that pair first."),
 solution=steps(
  ("Pick the broadest opener", p("Sentence 4 asks the big question: why are some crimes re-examined forever, while others are forgotten?")),
  ("Lock the question–answer pair", p("Sentence 1 narrows it: what exactly are the “unusual elements”? Sentence 2 answers: “<b>It</b> might be…” depravity, but very often “the precise amount of <b>mystery</b>”.")),
  ("Follow the keyword", p("“Mystery” hands off to sentence 3: “Unsolved, and perhaps unsolvable cases offer something that ‘ordinary’ murder does not.”")),
 ) + final("4123"),
 concept=STRAT["pj"], why_title="Why not another order",
 why=why([
  ("4312", "Sentence 3 would answer before sentence 1 even asks about the “unusual elements”. Sentence 2’s “mystery” would then repeat sentence 3 instead of leading into it."),
  ("1234", "Starting with “What precisely are the ‘unusual elements’…” refers to elements no sentence has mentioned yet."),
 ]))

SOL[23] = dict(
 hint=p("List the passage’s three points in order, then check which option keeps all three without adding anything."),
 solution=steps(
  ("List the passage’s points", "<ol><li>Colonialism is old, not modern.</li><li>In the 16th century it <b>changed decisively</b> because of navigation technology.</li><li>That let Europeans <b>settle</b> people overseas and keep <b>political control</b> over distant places.</li></ol>"),
  ("Remove the misfits", p("Option 2 says colonialism was “conceptualized” in the 16th century, which contradicts point 1. Option 4 says “British”, which the passage never says.")),
  ("Compare the last two", p("Option 1 makes displacement the headline and loses the idea of a <i>transformation</i>. Option 3 keeps all three points.")),
 ) + final("Option 3.")
   + trap("Option 1 is close and mentions real consequences, but it shifts the focus from <i>how colonialism changed</i> to <i>what it caused</i>."),
 concept=STRAT["summary"],
 why=why([
  ("1", "Makes displacement and political change the main point, and drops the “transformed, not begun” idea."),
  ("2", "“Conceptualized in the 16th century” contradicts “Colonialism is not a modern phenomenon”."),
  ("4", "Narrows “European” to “British”, which isn’t in the passage."),
 ]))

QTYPE_TAG = {1: "Except", 2: "Odd_Pair", 3: "Weaken_Except", 4: "Not_True"}
