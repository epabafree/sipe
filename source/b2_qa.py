# -*- coding: utf-8 -*-
# Batch 2 — CAT 2023 Slot 1 QA: Q5, 6, 8, 11, 12, 13, 15, 16, 21.
from fmt import steps, final, why, table, p

ITEMS, SOL = [], {}
def q(qno, text, opts, qtype, ans, topics, diff, **sol):
    ITEMS.append(dict(section="QA", qno=qno, set_id="", set_title="", directions="", context="", question=text, options=opts,
                      qtype=qtype, answer=ans, topic=[f"QA::{t}" for t in topics], difficulty=diff))
    SOL[qno] = sol

q(5, r"The number of integer solutions of equation \(2|x|(x^2 + 1) = 5x^2\) is", [], "TITA", "3",
  ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
  hint=p(r"Check \(x = 0\) separately, then divide by \(|x|\) and use \(x^2 = |x|^2\)."),
  solution=steps(
   ("Try x = 0", p(r"Both sides are \(0\), so \(x = 0\) is a solution.")),
   ("Divide by |x| (x ≠ 0)", p(r"With \(t = |x| > 0\) and \(x^2 = t^2\):") + r"\[\begin{aligned} 2(t^2 + 1) &= 5t \\ 2t^2 - 5t + 2 &= 0 \\ (2t - 1)(t - 2) &= 0 \end{aligned}\]"),
   ("Keep the integers", p(r"\(t = \tfrac12\) gives no integer; \(t = 2\) gives \(x = \pm 2\).")),
  ) + final(r"\(x \in \{-2, 0, 2\}\): \(3\) solutions"),
  shortcut=p(r"Whenever \(|x|\) and \(x^2\) appear together, substitute \(t = |x|\). It turns the equation into an ordinary quadratic in \(t \ge 0\)."),
  concept=r"\[x^2 = |x|^2 \qquad |x| = t \Rightarrow x = \pm t\]")

q(6, r"The equation \(x^3 + (2r + 1)x^2 + (4r - 1)x + 2 = 0\) has \(-2\) as one of the roots. If the other two roots are real, then the minimum possible non-negative integer value of \(r\) is", [], "TITA", "2",
  ["Algebra::Equations_and_Polynomials"], "Medium",
  hint=p(r"Factor out \((x + 2)\). What condition makes the remaining quadratic have real roots?"),
  solution=steps(
   ("Factor out (x + 2)", r"\[\begin{aligned} &x^3 + (2r+1)x^2 + (4r-1)x + 2 \\ &= (x + 2)\left(x^2 + (2r - 1)x + 1\right) \end{aligned}\]" + p(r"Check: \((x+2)(x^2 + ax + 1) = x^3 + (a+2)x^2 + (2a+1)x + 2\), with \(a = 2r - 1\) ✓")),
   ("Real roots", r"\[\begin{aligned} (2r - 1)^2 - 4 &\ge 0 \\ |2r - 1| &\ge 2 \\ r \ge \tfrac32 \ &\text{or}\ r \le -\tfrac12 \end{aligned}\]"),
  ) + final(r"Smallest non-negative integer: \(r = 2\)"),
  shortcut=p(r"Use the given root to factor first. The remaining quadratic’s constant term is \(2 / 2 = 1\), so only its middle coefficient needs finding."),
  concept=r"\[ax^2 + bx + c = 0 \text{ has real roots} \iff b^2 - 4ac \ge 0\]")

q(8, r"In an examination, the average marks of 4 girls and 6 boys is 24. Each of the girls has the same marks while each of the boys has the same marks. If the marks of any girl is at most double the marks of any boy, but not less than the marks of any boy, then the number of possible distinct integer values of the total marks of 2 girls and 6 boys is",
  [r"\(21\)", r"\(19\)", r"\(20\)", r"\(22\)"], "MCQ", "1", ["Arithmetic::Average"], "Medium",
  hint=p(r"Let each girl score \(g\) and each boy \(b\): \(4g + 6b = 240\). Write the target total \(2g + 6b\) in terms of \(g\) alone."),
  solution=steps(
   ("Set up", r"\[4g + 6b = 240, \qquad b \le g \le 2b\]"),
   ("Range of g", r"\[\begin{aligned} g \ge b &\Rightarrow 6g \ge 240 - 4g \Rightarrow g \ge 24 \\ g \le 2b &\Rightarrow 3g \le 240 - 4g \Rightarrow g \le \tfrac{240}{7} \approx 34.29 \end{aligned}\]"),
   ("Target total", r"\[T = 2g + 6b = 240 - 2g \in [171.43,\ 192]\]" + p(r"Integers \(172, 173, \dots, 192\).")),
  ) + final(r"\(21\) values — option 1"),
  shortcut=p(r"Marks needn’t be integers, only the total. So find the interval for \(T\) and count the integers in it."),
  concept=r"\[\text{Total} = \text{average} \times \text{count}\]",
  why=why([("2", r"\(19\) would drop both ends, \(172\) and \(192\); \(192\) is allowed because a girl may score the same as a boy."), ("3", "Off by one: check both ends of the interval."), ("4", r"\(171\) is below the minimum \(171.43\).")]))

q(11, r"Brishti went on an 8-hour trip in a car. Before the trip, the car had travelled a total of \(x\) km till then, where \(x\) is a whole number and is palindromic, i.e., \(x\) remains unchanged when its digits are reversed. At the end of the trip, the car had travelled a total of \(26862\) km till then, this number again being palindromic. If Brishti never drove at more than \(110\) km/h, then the greatest possible average speed at which she drove during the trip, in km/h, was",
  [r"\(90\)", r"\(80\)", r"\(100\)", r"\(110\)"], "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance", "Number_System::Miscellaneous"], "Easy",
  hint=p(r"She covered at most \(8 \times 110 = 880\) km. Find the smallest palindrome at or above \(26862 - 880\)."),
  solution=steps(
   ("Bound the distance", r"\[\text{distance} \le 8 \times 110 = 880\]\[x \ge 26862 - 880 = 25982\]"),
   ("Find the palindrome", p(r"Five-digit palindromes near there: \(25952\) (too small), then \(26062\).")),
   ("Average speed", r"\[\frac{26862 - 26062}{8} = \frac{800}{8} = 100\ \text{km/h}\]"),
  ) + final(r"\(100\) km/h — option 3"),
  concept=r"\[\text{average speed} = \frac{\text{total distance}}{\text{total time}}\]",
  why=why([("1", r"\(90\) km/h is possible but not the greatest."), ("2", r"\(80\) km/h is possible but not the greatest."), ("4", r"\(110\) needs \(x = 25982\), which isn’t a palindrome.")]))

q(12, r"Gita sells two objects A and B at the same price such that she makes a profit of \(20\%\) on object A and a loss of \(10\%\) on object B. If she increases the selling price such that objects A and B are still sold at an equal price and a profit of \(10\%\) is made on object B, then the profit made on object A will be nearest to",
  [r"\(42\%\)", r"\(49\%\)", r"\(45\%\)", r"\(47\%\)"], "MCQ", "4", ["Arithmetic::Profit_Loss_and_Discount"], "Easy",
  hint=p(r"Equal selling prices: \(1.2 \times \text{cost}_A = 0.9 \times \text{cost}_B\). Find the ratio of the costs."),
  solution=steps(
   ("Ratio of costs", r"\[1.2A = 0.9B \;\Rightarrow\; B = \tfrac43 A\]"),
   ("New selling price", r"\[1.1B = 1.1 \times \tfrac43 A = 1.4\overline{6}\,A\]"),
  ) + final(r"Profit on A \(\approx 46.7\% \approx 47\%\) — option 4"),
  shortcut=p(r"Take \(A = 300\), so \(B = 400\). The new price is \(440\), and the profit on A is \(140/300 \approx 47\%\)."),
  concept=r"\[\text{SP} = \text{CP} \times (1 + \text{profit}\%)\]",
  why=why([(o, rf"The exact value is \(46.67\%\), so \({v}\%\) isn’t nearest.") for o, v in (("1", "42"), ("2", "49"), ("3", "45"))]))

q(13, r"A mixture P is formed by removing a certain amount of coffee from a coffee jar and replacing the same amount with cocoa powder. The same amount is again removed from mixture P and replaced with same amount of cocoa powder to form a new mixture Q. If the ratio of coffee and cocoa in the mixture Q is \(16 : 9\), then the ratio of cocoa in mixture P to that in mixture Q is",
  [r"\(4 : 9\)", r"\(1 : 3\)", r"\(5 : 9\)", r"\(1 : 2\)"], "MCQ", "3", ["Arithmetic::Mixture_and_Alligation"], "Easy",
  hint=p(r"After two replacements, the coffee fraction is \((1 - f)^2\), where \(f\) is the fraction removed each time."),
  solution=steps(
   ("Find f", r"\[(1 - f)^2 = \frac{16}{25} \;\Rightarrow\; 1 - f = \frac45 \;\Rightarrow\; f = \frac15\]"),
   ("Cocoa fractions", r"\[\text{P: } \frac15, \qquad \text{Q: } \frac{9}{25}\]"),
  ) + final(r"\(\tfrac15 : \tfrac{9}{25} = 5 : 9\) — option 3"),
  concept=r"\[\text{remaining original} = \left(1 - \frac{x}{V}\right)^n \text{ after } n \text{ replacements}\]",
  why=why([("1", r"\(4 : 9\) compares P’s coffee \(\left(\tfrac45\right)\) with Q’s cocoa: wrong pair."), ("2", r"\(1 : 3\) doesn’t fit \(f = \tfrac15\)."), ("4", r"\(1 : 2\) doesn’t fit \(f = \tfrac15\).")]))

q(15, r"The amount of job that Amal, Sunil and Kamal can individually do in a day, are in harmonic progression. Kamal takes twice as much time as Amal to do the same amount of job. If Amal and Sunil work for \(4\) days and \(9\) days, respectively, Kamal needs to work for \(16\) days to finish the remaining job. Then the number of days Sunil will take to finish the job working alone, is",
  [], "TITA", "27", ["Arithmetic::Time_and_Work"], "Medium",
  hint=p(r"Rates in HP means the <i>times</i> are in AP. If Amal takes \(T\) days, Kamal takes \(2T\)."),
  solution=steps(
   ("Rates in HP ⇒ times in AP", r"\[T_A = T, \qquad T_K = 2T \;\Rightarrow\; T_S = \frac{T + 2T}{2} = 1.5T\]"),
   ("Work equation", r"\[\frac{4}{T} + \frac{9}{1.5T} + \frac{16}{2T} = 1\]\[\frac{4 + 6 + 8}{T} = 1 \;\Rightarrow\; T = 18\]"),
  ) + final(r"Sunil alone: \(1.5 \times 18 = 27\) days"),
  shortcut=p(r"Write each person’s contribution as days ÷ their time; with times \(T, 1.5T, 2T\) everything collapses to \(18/T\)."),
  concept=r"\[a, b, c \text{ in HP} \iff \tfrac1a, \tfrac1b, \tfrac1c \text{ in AP}\]")

q(16, r"Arvind travels from town A to town B, and Surbhi from town B to town A, both starting at the same time along the same route. After meeting each other, Arvind takes \(6\) hours to reach town B while Surbhi takes \(24\) hours to reach town A. If Arvind travelled at a speed of \(54\) km/h, then the distance, in km, between town A and town B is",
  [], "TITA", "972", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
  hint=p(r"Two people start together and meet; if they then take \(t_1\) and \(t_2\) to finish, the time to meet is \(\sqrt{t_1 t_2}\)."),
  solution=steps(
   ("Time to meet", r"\[t = \sqrt{6 \times 24} = 12\ \text{h}\]"),
   ("Surbhi’s speed", r"\[\frac{v_A}{v_S} = \sqrt{\frac{24}{6}} = 2 \;\Rightarrow\; v_S = 27\ \text{km/h}\]"),
   ("Distance", r"\[(54 + 27) \times 12 = 972\ \text{km}\]"),
  ) + final(r"\(972\) km"),
  shortcut=p(r"Arvind covers in \(6\) h what Surbhi covered in \(12\) h, so the distance from the meeting point to B is \(54 \times 6 = 324\). Surbhi’s part plus Arvind’s \(54 \times 12 = 648\) gives \(972\)."),
  concept=r"\[t_{\text{meet}} = \sqrt{t_1 t_2}, \qquad \frac{v_1}{v_2} = \sqrt{\frac{t_2}{t_1}}\]")

q(21, r"The number of all natural numbers up to \(1000\) with non-repeating digits is", [r"\(738\)", r"\(648\)", r"\(504\)", r"\(585\)"], "MCQ", "1",
  ["Modern_Maths::Permutations_and_Combinations"], "Easy",
  hint=p("Count 1-digit, 2-digit and 3-digit numbers separately. 1000 itself repeats a digit."),
  solution=steps(
   ("Count by length", table(["Digits", "Choices", "Count"], [["1", r"\(9\)", "9"], ["2", r"\(9 \times 9\)", "81"], ["3", r"\(9 \times 9 \times 8\)", "648"]])),
   ("1000", p(r"\(1000\) repeats \(0\), so it is excluded.")),
  ) + final(r"\(9 + 81 + 648 = 738\) — option 1"),
  concept=p(r"Numbers with \(n\) digits, all different:") + r"\[9 \times 9 \times 8 \times 7 \times \cdots \quad (n \text{ factors})\]",
  why=why([("2", r"\(648\) counts only 3-digit numbers."), ("3", r"\(504 = 9 \times 8 \times 7\) wrongly excludes 0 from the later digits."), ("4", r"\(585\) doesn’t come from any correct case count; the cases add up to \(738\).")]))
