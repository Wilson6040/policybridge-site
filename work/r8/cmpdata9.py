# -*- coding: utf-8 -*-
"""
cmpdata9 — augments cmpdata with Entertainment Elite (v3.2) as the 6th competitor
(7th wording column). Column order: TMHCC, Tysers, Yutree, Liberty, Allianz, AXA XL, Entertainment Elite.

Entertainment Elite grounded in /app/work/r9/src/EntertainmentElite.pdf:
  8-section property/BI/Money/liability/terrorism package — Property Damage All Risks (incl. defined
  'Entertainment Equipment'), Business Interruption (Revenue; Additional Cost of Working), a detailed
  Schedule/Item-driven Money Section (theft; safes/containers; assault + Accident/emotional-stress;
  employee dishonesty GBP 25k), Employers' Liability, Public & Products Liability, Terrorism.
  NO media/PI/E&O, production indemnity, cyber, legal-expenses, management-liability, loss-of-licence
  or goods-in-transit sections. Carries Computer-Misuse + date/computer-failure exclusions.
"""
import sys
sys.path.insert(0, '/app/work/compare')
import cmpdata as _c

# ---- wordings + keys ----
EE_WORDING = dict(key="ee", name="Ent. Elite",
                  full="Entertainment Elite Policy (v3.2)",
                  insurer="Entertainment Elite (entertainment package wording)",
                  sections="8 sections (Property/BI/Money/Liability/Terrorism)",
                  ref="Entertainment_Elite_Policy_v3.2_10.20")

WORDINGS = list(_c.WORDINGS) + [EE_WORDING]
COMPETITOR_KEYS = list(_c.COMPETITOR_KEYS) + ["ee"]

# ---- per-row EE values (indexed in cmpdata row order) ----
EE_SECTION = ["yes","yes","yes","yes","yes","yes","yes","yes","no","no","no","no","no","no","no","partial"]
EE_GENEXCL = ["yes","partial","yes","yes","yes","yes","review","yes","review"]
EE_COND = [
  "Written notice to the Insurer as soon as reasonably practicable per the General/Claims Conditions; claim documents forwarded.",
  "n/a \u2014 no PI/media section.",
  "Reasonable-precautions and risk-improvement conditions; specific Money security, carryings and key conditions.",
  "n/a (no PI).",
  "Premium-instalment and cancellation provisions.",
  "Duty of fair presentation.",
  "Insurer conduct-of-claims rights.",
]

def _fix(s):
    if not isinstance(s, str):
        return s
    return (s.replace("all five competitors", "all six competitors")
             .replace("the five competitors", "the six competitors")
             .replace("five competitor wordings", "six competitor wordings")
             .replace("across all five", "across all six")
             .replace("five competitors", "six competitors")
             .replace("all five wordings", "all six wordings")
             .replace("the six (6)", "the six"))

def _append_status(rows, ee_list):
    out = []
    for i, row in enumerate(rows):
        label, statuses, verdict, comment = row
        out.append((label, list(statuses) + [ee_list[i]], verdict, _fix(comment)))
    return out

def _append_status3(rows, ee_list):
    """rows = (label, statuses, comment)"""
    out = []
    for i, row in enumerate(rows):
        label, statuses, comment = row
        out.append((label, list(statuses) + [ee_list[i]], _fix(comment)))
    return out

SECTION_ROWS = _append_status(_c.SECTION_ROWS, EE_SECTION)
MEDIA_FEATURES = _append_status(_c.MEDIA_FEATURES, ["no"] * len(_c.MEDIA_FEATURES))
GENERAL_EXCL = _append_status3(_c.GENERAL_EXCL, EE_GENEXCL)
PI_EXCL = _append_status3(_c.PI_EXCL, ["na"] * len(_c.PI_EXCL))
CONDITIONS = [tuple(list(r) + [EE_COND[i]]) for i, r in enumerate(_c.CONDITIONS)]
SUBLIMITS = [tuple(list(r) + ["n/a"]) for r in _c.SUBLIMITS]

# ---- competitor profile ----
COMPETITOR_PROFILES = dict(_c.COMPETITOR_PROFILES)
COMPETITOR_PROFILES["ee"] = dict(
  title="Entertainment Elite Policy (v3.2)",
  shape="8 sections: Property Damage \u2018All Risks\u2019 (incl. defined Entertainment Equipment), Business "
        "Interruption (Revenue; Additional Cost of Working), Money, Employers\u2019 Liability, Public & Products "
        "Liability and Terrorism.",
  strengths=[
    "Detailed, Schedule/Item-driven Money Section \u2014 theft of/from safes, strongrooms, bags and containers; "
    "assault cover with Accident (death/disablement) and emotional-stress counselling benefits; and employee "
    "dishonesty up to GBP 25,000 (aggregate).",
    "Granular Business Interruption suite (Revenue plus Additional Cost of Working).",
    "Defines \u2018Entertainment Equipment\u2019 and addresses property used at conferences, events, festivals and "
    "product launches.",
  ],
  gaps=[
    "NO Media Liability / PI / E&O, Production Indemnity, Cyber, Legal Expenses, Management Liability, Loss of "
    "Licence or Goods in Transit section.",
    "Carries Computer-Misuse and date/computer-failure exclusions in the Money Section.",
  ])

# ---- pass-through (with six-competitor wording fix where relevant) ----
TMHCC_STRENGTHS = [(t, _fix(w)) for (t, w) in _c.TMHCC_STRENGTHS]
COMP_BROADER = [(t, _fix(w)) for (t, w) in _c.COMP_BROADER]
METHOD_NOTES = [_fix(n) for n in _c.METHOD_NOTES]
ASSUMPTIONS = _c.ASSUMPTIONS
