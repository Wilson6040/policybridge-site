# -*- coding: utf-8 -*-
"""PHASE 04 — Rebuilt six-insurer coverage comparison (clean one-page matrix + appendix)."""
import sys
sys.path.insert(0, "/app/work/r8")
sys.path.insert(0, "/app/work/compare")
import brand2 as B
import cmpdata9 as D
import cmpdata as C

OUT = "/app/outputs/phase-04-coverage-comparison/TMHCC_Six_Insurer_Coverage_Comparison.docx"
INS = ["TMHCC", "Tysers", "Yutree", "Liberty", "Allianz", "AXA XL", "Ent.Elite"]

# Clean, concise main matrix (one page). (feature, [7 statuses], short note)
MAIN = [
 ("Premises buildings & contents (MD)", ["yes","yes","yes","yes","yes","yes","yes"], "All six; TMHCC absorbs IT property here."),
 ("Production / entertainment equipment", ["yes","yes","yes","partial","yes","yes","yes"], "Liberty via specified items."),
 ("Business interruption", ["yes","yes","yes","yes","yes","yes","yes"], "Allianz/AXA XL name more BI heads."),
 ("Terrorism", ["yes","no","yes","yes","yes","no","yes"], "Tysers & AXA XL exclude outright."),
 ("Employers\u2019 Liability", ["yes","yes","yes","yes","yes","yes","yes"], "Statutory EL by all (\u2248GBP 10m)."),
 ("Public Liability", ["yes","yes","yes","yes","yes","yes","yes"], "All; competitors combine Public+Products."),
 ("Products Liability", ["yes","yes","yes","yes","yes","yes","yes"], "All."),
 ("Abuse / molestation (PL) \u2014 covered?", ["no","review","no","review","review","no","review"], "TMHCC/Yutree/AXA XL EXCLUDE; others silent. See \u00a7A2."),
 ("Money (incl. touring/events)", ["yes","yes","yes","yes","yes","partial","yes"], "TMHCC restructured Premises + Touring/Events."),
 ("Goods in Transit", ["yes","no","yes","no","yes","no","no"], "Dedicated GIT: TMHCC, Yutree, Allianz."),
 ("Loss of Licence", ["yes","no","no","no","no","no","no"], "UNIQUE to TMHCC."),
 ("Production Indemnity", ["yes","yes","yes","no","no","no","no"], "TMHCC, Tysers, Yutree."),
 ("Media Liability / PI / E&O", ["yes","yes","yes","no","no","no","no"], "Tysers PI worldwide + patents; see \u00a7A1."),
 ("Commercial Legal Expenses", ["yes","no","no","no","no","no","no"], "UNIQUE to TMHCC."),
 ("Management Liability (D&O/EPL)", ["yes","no","no","no","no","no","no"], "UNIQUE to TMHCC."),
 ("Standalone Cyber Liability", ["yes","no","partial","no","no","no","no"], "UNIQUE; Yutree breakdown only; AXA XL excludes."),
 ("Personal Accident & Business Travel", ["no","yes","partial","no","review","no","no"], "GAP: Tysers extensive; Yutree assault."),
 ("Worldwide PI territory (incl. option)", ["partial","yes","partial","no","no","no","no"], "Tysers worldwide; TMHCC optional (sign-off)."),
]


def appendix_matrix(doc, title, rows, intro=None, widths=None):
    B.h2(doc, title)
    if intro:
        B.para(doc, intro, size=8.4)
    headers = ["Feature"] + INS + ["Note"]
    w = widths or [4.0, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 12.3]
    t = B.make_table(doc, headers, w)
    for row in rows:
        if len(row) == 4:
            label, statuses, _v, comment = row
        else:
            label, statuses, comment = row
        c = t.add_row().cells
        B.text_cell(c[0], label, size=7.4, bold=True, color=B.TEAL)
        for j, st in enumerate(statuses):
            B.status_cell(c[1 + j], st, small=True)
        B.text_cell(c[8], comment, size=7.2)
    B.zebra(t)
    B.spacer(doc, 4)


def main():
    doc = B.Document()
    B.set_normal_style(doc)
    B.setup_page(doc, landscape=True, margin_cm=1.3)
    B.add_logo_header(doc, left_text="TMHCC Media & Music Combined \u2014 Coverage Comparison")
    B.add_footer_pagenum(doc, note="Phase 04 \u2014 six-insurer coverage comparison. Indicative; refer to the full wordings. "
                                   "Compared by legal effect, not heading. Subject to TMHCC legal/underwriting sign-off.")
    B.cover_page(doc,
        "Phase 04 \u00b7 Coverage Comparison",
        "Six-Insurer Coverage Comparison",
        "Clean one-page at-a-glance matrix, with a detailed legal appendix",
        ["TMHCC Media & Music Combined (final, commit 58b8340) vs six competitor wordings.",
         "Legend: \u2713 covered \u00b7 \u25d0 partial/conditional/sub-limited \u00b7 \u2717 not identified/excluded \u00b7 ? unclear/requires review.",
         "No cover invented; TMHCC is not shown as winning a row the wording does not support (e.g. abuse)."],
        [w["full"] for w in D.WORDINGS])
    doc.add_page_break()

    # ---- ONE-PAGE MAIN MATRIX ----
    B.h1(doc, "At-a-glance coverage matrix")
    B.legend_bar(doc)
    headers = ["Coverage feature"] + INS + ["Key note / practical impact"]
    t = B.make_table(doc, headers, [5.0, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 9.9])
    for label, statuses, note in MAIN:
        c = t.add_row().cells
        B.text_cell(c[0], label, size=7.5, bold=True, color=B.TEAL)
        for j, st in enumerate(statuses):
            B.status_cell(c[1 + j], st, small=True)
        B.text_cell(c[8], note, size=7.2)
    B.zebra(t)
    B.para(doc, "Footnotes: \u00a7A1 Media/PI \u2014 Tysers PI is worldwide and covers patents; TMHCC S12 is jurisdiction-limited (default ex-US/Canada) and "
                "excludes patents. \u00a7A2 Abuse \u2014 TMHCC, Yutree and AXA XL EXCLUDE abuse; Tysers, Liberty, Allianz and Entertainment Elite carry no "
                "express abuse exclusion (silent \u2192 not affirmatively granted). 'Liberty/Allianz/AXA XL/Ent.Elite' are property/BI/liability packages "
                "with no media/PI/cyber/legal/management cover.", size=7.3)
    doc.add_page_break()

    # ---- APPENDIX ----
    B.h1(doc, "Appendix \u2014 detailed coverage & legal notes")
    appendix_matrix(doc, "App. 1 \u2014 Section / cover availability (15 sections + PA)", D.SECTION_ROWS)
    doc.add_page_break()
    appendix_matrix(doc, "App. 2 \u2014 Media Liability / PI / E&O feature detail", D.MEDIA_FEATURES,
                    intro="Liberty, Allianz, AXA XL and Entertainment Elite provide NO media/PI cover.")
    doc.add_page_break()
    appendix_matrix(doc, "App. 3 \u2014 General & liability exclusions (\u2713 = exclusion applies)",
                    [("Abuse / molestation exclusion (PL)", ["yes","no","yes","no","no","yes","no"],
                      "TMHCC/Yutree/AXA XL exclude abuse; Tysers/Liberty/Allianz/Ent.Elite silent. (Prior review's omission.)")]
                    + list(D.GENERAL_EXCL))
    appendix_matrix(doc, "App. 4 \u2014 PI-specific exclusions (\u2713 = applies; na = no PI)", D.PI_EXCL)
    doc.add_page_break()

    B.h2(doc, "App. 5 \u2014 Conditions & claims obligations")
    ch = B.make_table(doc, ["Condition"] + INS, [4.4] + [3.18]*7)
    for row in D.CONDITIONS:
        c = ch.add_row().cells
        B.text_cell(c[0], row[0], size=7.2, bold=True, color=B.TEAL)
        for j in range(7):
            B.text_cell(c[1 + j], row[1 + j], size=6.7)
    B.zebra(ch)
    doc.add_page_break()

    B.h2(doc, "App. 6 \u2014 Key Media/PI sub-limits")
    sl = B.make_table(doc, ["Sub-limit"] + INS, [4.4] + [3.18]*7)
    for row in D.SUBLIMITS:
        c = sl.add_row().cells
        B.text_cell(c[0], row[0], size=7.4, bold=True, color=B.TEAL)
        for j in range(7):
            B.text_cell(c[1 + j], row[1 + j], size=7.0, align="center")
    B.zebra(sl)
    B.spacer(doc, 6)

    B.h2(doc, "App. 7 \u2014 TMHCC genuine strengths (wording-supported)")
    for title, body in D.TMHCC_STRENGTHS:
        B.bullet(doc, body, bold_lead=title + " \u2014 ", size=8.3)
    B.h2(doc, "App. 8 \u2014 Areas competitors are broader")
    for title, body in D.COMP_BROADER:
        B.bullet(doc, body, bold_lead=title + " \u2014 ", size=8.3)
    B.h2(doc, "App. 9 \u2014 Method & assumptions")
    for n in D.METHOD_NOTES:
        B.bullet(doc, n, size=8.2)
    for n in D.ASSUMPTIONS:
        B.bullet(doc, n, size=8.2, color=B.GREY)

    B.save_doc(doc, OUT)
    print("saved", OUT)


main()
