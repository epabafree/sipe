# -*- coding: utf-8 -*-
"""Figures for Simp Mock 16 (2025), written into media/ when imported."""
import charts

DIVS = ["BioTech", "ChemSynth", "DataAnalysis", "ClinicalTrials", "Formulations", "Regulations"]
PAPERS = [25, 10, 15, 20, 20, 10]
PATENTS = [15, 20, 10, 10, 30, 15]
REV = [20, 25, 10, 15, 20, 10]
OUTPUTS = charts.vbar("sipe_SM25-16_DILR_S2a", ["BioTech", "ChemSyn", "DataAn", "Clinical", "Formul", "Regul"],
                      [("% of Published Papers", PAPERS), ("% of Patents Filed", PATENTS)], 35, 5,
                      "Grouped bars: each division’s share of all published papers and of all patents filed. "
                      + "; ".join(f"{d}: papers {a}%, patents {b}%" for d, a, b in zip(DIVS, PAPERS, PATENTS)),
                      ylabel="%", fmt=lambda v: f"{v}")
REVENUE = charts.pie("sipe_SM25-16_DILR_S2b", DIVS, REV,
                     "Pie chart of revenue share by division: " + ", ".join(f"{d} {v}%" for d, v in zip(DIVS, REV)))

PL = [f"P{i}" for i in range(1, 11)]
R4 = [3, 3, 5, 16, 5, 10, 20, 0, 10, 0]
R7 = [8, 8, 5, 16, 5, 20, 23, 15, 23, 3]
R10 = [16, 21, 15, 21, 8, 20, 23, 20, 23, 13]
SHOOT = charts.vbar("sipe_SM25-16_DILR_S4", PL, [("After round 4", R4), ("After round 7", R7), ("After round 10", R10)], 25, 5,
                    "Grouped bars of each player’s running total after rounds 4, 7 and 10. "
                    + "; ".join(f"{p}: {a}, {b}, {c}" for p, a, b, c in zip(PL, R4, R7, R10)),
                    ylabel="Points", w=600, h=320)
