# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/app/work/compare')
from docx import Document
import brand2 as b
import cmpdata as d


def build():
    doc = Document()
    b.set_normal_style(doc)
    b.setup_page(doc, landscape=False, margin_cm=1.7)
    b.add_logo_header(doc)
    b.add_footer_pagenum(doc)

    b.cover_page(
        doc,
        doc_kicker="QA & Methodology \u2014 Media & Entertainment",
        title="QA / Methodology Report",
        subtitle="Quality-assurance record and methodology for the TMHCC Media & Entertainment coverage comparison and gap-fill strategy.",
        meta_lines=[
            "Accompanies the Full Coverage Comparison and the Gap-Fill / Wording Enhancement Strategy.",
            "Subject to final TMHCC legal / underwriting sign-off.",
        ],
        wordings=[f"{w['name']} \u2014 {w['ref']}" for w in d.WORDINGS],
    )

    doc.add_page_break()
    b.h1(doc, "Documents reviewed", num="1")
    t = b.make_table(doc, ["Wording", "Source file", "Capacity / insurer", "Structure"], [3.0, 6.0, 4.6, 4.2])
    for w in d.WORDINGS:
        cells = t.add_row().cells
        b.text_cell(cells[0], w['name'], size=8.4, bold=True, color=b.TEAL)
        b.text_cell(cells[1], w['ref'], size=8.0)
        b.text_cell(cells[2], w['insurer'], size=8.0)
        b.text_cell(cells[3], w['sections'], size=8.0)
    b.zebra(t)

    b.h1(doc, "Comparison method", num="2")
    for n in d.METHOD_NOTES:
        b.bullet(doc, n)

    doc.add_page_break()
    b.h1(doc, "Key TMHCC strengths", num="3")
    for title, why in d.TMHCC_STRENGTHS:
        b.bullet(doc, why, bold_lead=title + ":  ")

    b.h1(doc, "Key TMHCC gaps (vs competitors)", num="4")
    for title, why in d.COMP_BROADER:
        b.bullet(doc, why, bold_lead=title + ":  ")

    doc.add_page_break()
    b.h1(doc, "Recommended enhancements (priority order)", num="5")
    order = sorted(range(len(d.GAPFILL)), key=lambda i: ["High","Medium-High","Medium","Low-Medium","Low"].index(d.GAPFILL[i]['priority']))
    t = b.make_table(doc, ["#", "Recommendation", "Priority"], [0.9, 13.5, 3.4])
    for n, i in enumerate(order, start=1):
        rec = d.GAPFILL[i]
        cells = t.add_row().cells
        b.text_cell(cells[0], str(n), size=8.4, bold=True, color=b.TEAL, align='center')
        b.text_cell(cells[1], rec['title'], size=8.3)
        bg, fg = {"High": ("FBE6EA", "A4233B"), "Medium-High": ("FBE6EA", "A4233B"),
                  "Medium": ("FBF1DA", "8A6A1E")}.get(rec['priority'], ("EEF1F3", "5B6166"))
        b.text_cell(cells[2], rec['priority'], size=8.2, bold=True, color=fg, bg=bg, align='center')
    b.zebra(t)

    b.h1(doc, "Key exclusions issues", num="6")
    for area, comp, does, pos, action, prio in d.EXCL_WRITEBACKS:
        b.bullet(doc, f"{does} \u2014 TMHCC: {pos}. Action: {action} (priority {prio}).", bold_lead=area + ":  ")

    doc.add_page_break()
    b.h1(doc, "Assumptions made", num="7")
    for a in d.ASSUMPTIONS:
        b.bullet(doc, a)

    b.h1(doc, "Points requiring legal / underwriting review", num="8")
    for n in [
        "Whether TMHCC offers Personal Accident / Business Travel by endorsement.",
        "Communicable-disease exclusion positions in Yutree, Liberty and Allianz.",
        "Tysers / Yutree fines-penalties and insolvency PI exclusion positions.",
        "Allianz \u2018Personal Accident\u2019 section referenced in exclusions but absent from the cover list.",
        "Express treatment of ICOW/Book Debts (S3) and computer breakdown (S1/S2) within TMHCC.",
        "Pricing, reinsurance territory and capacity for any rated options (PA; worldwide/US-Canada; distributors).",
        "Final limits/excesses against each Schedule.",
    ]:
        b.bullet(doc, n)

    # ---- FINAL REPORT (the 10-point brief response) ----
    doc.add_page_break()
    b.h1(doc, "Final report", num="9")
    fr = [
        ("1. Documents produced",
         "Full Coverage Comparison (.docx + PDF); Gap-Fill / Wording Enhancement Strategy (.docx + PDF); this QA / Methodology Report (.docx + PDF)."),
        ("2. Five competitor wordings reviewed",
         "Partial \u2014 FOUR reviewed and mapped (Tysers/Zurich, Yutree/AXA, Liberty, Allianz). The FIFTH competitor (Wording E) is pending and carried as a reserved placeholder column, to be completed when supplied."),
        ("3. TMHCC base wording mapped", "Yes \u2014 all 15 sections mapped from the TMHCC Media & Music Combined wording."),
        ("4. Template branding preserved",
         "Yes \u2014 Tokio Marine HCC logo, Lato font, teal/gold/rust palette, legend and table style replicated from the supplied Coverage Comparison template."),
        ("5. Key TMHCC strengths",
         "Only wording with all 15 sections; unique Loss of Licence, Legal Expenses, Management Liability and standalone Cyber; broad, well-extended Media Liability; clean cyber-exclusion carve-out; protective claims architecture."),
        ("6. Key competitor advantages",
         "Tysers PI worldwide, covers patents, statutory/criminal defence (GBP 1m), distributors & purchasers, source-protection; Tysers & Yutree offer Personal Accident; Yutree reputation-mgmt/withdrawal/criminal-defence + KC clause; Allianz granular BI heads."),
        ("7. Key gaps TMHCC should consider filling",
         "Personal Accident option; worldwide/US-Canada PI option; distributors & purchasers; source-protection & representation costs; criminal-defence clarity; explicit ICOW/book-debts & computer-breakdown signposting."),
        ("8. High-priority wording enhancements",
         "(1) Personal Accident & Business Travel option; (2) rated worldwide/US-Canada PI territory option; (3) distributors & purchasers extension; (4) criminal/regulatory defence-costs clarity (S12 \u2194 S13/S14)."),
        ("9. Exclusion write-backs / narrowing opportunities",
         "Asbestos professional-duty (Tysers) and pollution negligent-advice (Yutree) write-backs \u2014 adopt narrowly; worldwide/US-Canada as a rated option. Retain patents, communicable-disease and default US/Canada exclusions."),
        ("10. Items requiring legal / underwriting sign-off",
         "All recommendations; any write-back drafting; rated-option pricing/reinsurance/capacity; PA appetite; confirmation of the \u2018review\u2019-flagged competitor positions; incorporation of the fifth competitor."),
    ]
    t = b.make_table(doc, ["Final-report item", "Outcome"], [4.6, 13.0])
    for k, v in fr:
        cells = t.add_row().cells
        b.text_cell(cells[0], k, size=8.4, bold=True, color=b.TEAL, bg="EAF1F5")
        b.text_cell(cells[1], v, size=8.4)
    b.zebra(t, start=1)

    b.spacer(doc, 6)
    b.callout(doc, "Completion status:", "Both branded documents are produced; all four available competitors are mapped; the full comparison and the gap-fill strategy are complete; recommendations are evidence-based; exclusions are reviewed in detail. The deliverables are market-ready SUBJECT TO TMHCC legal/underwriting sign-off and to incorporation of the fifth competitor wording when supplied.")

    out = "/app/work/compare/out/TMHCC_Media_Comparison_QA_Methodology.docx"
    b.save_doc(doc, out)
    print("Saved:", out)
    return out


if __name__ == "__main__":
    build()
