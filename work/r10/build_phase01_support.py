# -*- coding: utf-8 -*-
"""
PHASE 01 support: (1) TMHCC_Final_Clean.docx  (2) TMHCC_UW_Enhancement_Register.docx
"""
import sys, shutil
sys.path.insert(0, "/app/work/compare")
import brand2 as B
from docx.shared import Pt

OUTDIR = "/app/outputs/phase-01-full-redline"
FINAL_SRC = "/app/deliverables/TMHCC_Media_Combined_0526_FINAL_Clean.docx"

# (1) clean final = the genuine branded final wording, unchanged
shutil.copyfile(FINAL_SRC, f"{OUTDIR}/TMHCC_Final_Clean.docx")
print("copied clean final wording")

# (2) Enhancement Register --------------------------------------------------
ENH = [
 dict(title="1. Admission of Liability \u2014 claims condition (Sections 1\u201311)",
   section="Policy Claims Conditions (Sections 1\u201311)", loc="Conduct of Claims / Admission of Liability clause",
   wording="The previous BLANKET condition precedent ('the Insured must not admit liability\u2026') was replaced with an ordinary condition qualified so the Insurer may only rely on a breach to the extent it has been prejudiced.",
   why="Fairness / Insurance Act 2015 alignment; avoids disproportionate forfeiture of an otherwise valid claim for a technical breach.",
   support="Market practice / ICOBS fair-treatment expectations (not a competitor copy).",
   risk="Low \u2014 mildly reduces the Insurer's contractual remedy; favourable to the insured.",
   signoff="Yes \u2014 claims & underwriting to confirm the relaxation of the condition-precedent status is acceptable.",
   status="Not accepted \u2014 awaiting UW review"),
 dict(title="2. Proof of Ownership and Value \u2014 new claims condition (Sections 1\u201311)",
   section="Policy Claims Conditions (Sections 1\u201311)", loc="Inserted between 'Notification to the Police' and 'Terms of Settlement'",
   wording="New condition requiring the Insured, on request, to produce reasonable proof of ownership and value of property the subject of a claim.",
   why="Claims-handling hygiene for theft / property / equipment claims; reduces disputed-value claims.",
   support="Market norm; mirrors money/property security conditions in Tysers and Entertainment Elite.",
   risk="Low\u2013medium \u2014 confirm intended as an ordinary condition (NOT a condition precedent).",
   signoff="Yes \u2014 confirm status (ordinary condition vs CP).",
   status="Not accepted \u2014 awaiting UW review"),
 dict(title="3. Money \u2013 Premises extension (Section 8 Money)",
   section="Section 8 \u2014 Money", loc="Inserted after the 'Loss of Keys' clause (first of two new Schedule-referenced extensions)",
   wording="Extends cover to Damage to Money belonging to/for which the Insured is responsible whilst at the Premises, up to the Schedule sub-limit; expressly does not reduce, replace or restrict existing Money cover.",
   why="Restructure of Money into two clean, Schedule-referenced sub-limits (Premises vs Touring/Events).",
   support="Entertainment Elite event-money section + the 0523 'Venue' enhancement.",
   risk="Low\u2013medium \u2014 Schedule sub-limit set by underwriting.",
   signoff="Yes \u2014 underwriting to set sub-limit and confirm appetite.",
   status="Not accepted \u2014 awaiting UW review"),
 dict(title="4. Money \u2013 Touring, Festivals and Events extension (Section 8 Money)",
   section="Section 8 \u2014 Money", loc="Inserted after 'Money \u2013 Premises'",
   wording="Covers Money in transit / temporary storage / locked safe / personal custody at any venue, festival site, box office or touring/event location, including: (a) damage to safes, containers, money belts; (b) damage to clothing, personal effects and personal Money following assault/violence; and (c) employee dishonesty discovered within 12 months. Schedule sub-limit; does not reduce existing cover.",
   why="Touring/festival/event Money exposure not clearly addressed in the base wording.",
   support="Entertainment Elite Money Section (theft, safes, assault, employee dishonesty GBP 25k); 0523 wording.",
   risk="Medium \u2014 dishonesty and assault heads; Schedule sub-limit and conditions to be set by underwriting.",
   signoff="Yes \u2014 underwriting to confirm heads, sub-limit and dishonesty discovery period.",
   status="Not accepted \u2014 awaiting UW review"),
 dict(title="5. 'Employee' definition broadened (Section 13 Commercial Legal Expenses)",
   section="Section 13 \u2014 Commercial Legal Expenses (Definitions)", loc="Replaces the narrow S13 'Employee' definition",
   wording="Broadened to include labour-only / self-employed-supplying-labour, hired or borrowed staff, and voluntary helpers, work-experience / training-scheme participants, secondees, students and prospective employees being assessed.",
   why="Aligns the S13 employee class with the broader definitions used elsewhere and by competitors (the general, S12 and S14 definitions were already broad).",
   support="Tysers (p9) and Yutree (p88) broad 'employee' definitions.",
   risk="Low\u2013medium \u2014 widens the protected legal-expenses class.",
   signoff="Yes \u2014 confirm acceptable widening of the S13 employee class.",
   status="Not accepted \u2014 awaiting UW review"),
 dict(title="6. 'Computer System' definition aligned to Section 15 (Section 12 Media Liability)",
   section="Section 12 \u2014 Media Liability (Definitions)", loc="Replaces the narrow S12 'Computer System' definition",
   wording="Broad definition (computer/computing, electronic, wireless, web and cloud systems, hardware/software/firmware/data/networks) expressly stated to be consistent with the meaning of 'Computer System' in Section 15 (CyberGuard\u2122).",
   why="Removes an inconsistency between S12 and the standalone cyber section; avoids coverage gaps/overlaps.",
   support="Internal consistency with the broad S15 CyberGuard definition.",
   risk="Medium \u2014 broadens the S12 computer-related triggers.",
   signoff="Yes (S12) \u2014 underwriting to confirm the wider definition is intended for Media Liability.",
   status="Not accepted \u2014 awaiting UW review"),
 dict(title="7. Representation Costs at Investigations & Inquiries (Section 12)",
   section="Section 12 \u2014 Media Liability", loc="New extension after the IP-pursuit clause",
   wording="Up to GBP 25,000 in the aggregate, with prior written consent, for attendance/representation at an official examination, investigation or inquiry likely to give rise to a claim. Forms part of, and does not increase, the Indemnity Limit.",
   why="Regulators increasingly investigate content/advertising; S12 alone otherwise looked narrower.",
   support="Tysers clause 8.15 (GBP 25,000).",
   risk="Low \u2014 small sub-limit; consent condition.",
   signoff="Yes (S12) \u2014 confirm sub-limit and consent mechanics.",
   status="Not accepted \u2014 awaiting UW review"),
 dict(title="8. Costs for the Protection of Journalistic Sources (Section 12)",
   section="Section 12 \u2014 Media Liability", loc="New extension following Representation Costs",
   wording="Up to the Schedule sub-limit, with prior written consent, for legal costs to oppose a subpoena/court order requiring disclosure of a confidential journalistic source, where counsel advises reasonable grounds to oppose. Within the Indemnity Limit.",
   why="Broker-sensitive cover for editorial, news and publishing clients.",
   support="Tysers clause 8.13.",
   risk="Low \u2014 low-frequency; consent + counsel test.",
   signoff="Yes (S12) \u2014 confirm sub-limit.",
   status="Not accepted \u2014 awaiting UW review"),
 dict(title="9. Criminal & Regulatory Defence Costs cross-reference + contribution (Section 12)",
   section="Section 12 \u2014 Media Liability", loc="New clause following Source-Protection costs",
   wording="Signposts that criminal/regulatory defence may be available under S13 (Legal Expenses) and S14 (Management Liability), and adds an Insurer contribution up to the Schedule sub-limit (excess of S13/S14), excluding fines, penalties and costs after a plea/finding of guilt.",
   why="On a section-by-section read of S12 alone, TMHCC looked narrower than competitors that fund statutory defence.",
   support="Tysers (statutory defence GBP 1m); Yutree (criminal-prosecution defence GBP 250k).",
   risk="Low\u2013medium \u2014 largely a clarifying cross-reference; small contribution.",
   signoff="Yes (S12) \u2014 confirm interaction with S13/S14 and sub-limit.",
   status="Not accepted \u2014 awaiting UW review"),
 dict(title="10. Distributors & Purchasers extension (Section 12)",
   section="Section 12 \u2014 Media Liability", loc="New extension after 'Indemnity to Principals'",
   wording="Extends indemnity to purchasers/co-producers/licensees/distributors of the Insured's Media Material (only where the Insured is contractually obliged), capped at 5x the Indemnity Limit in the aggregate, subject to Insurer control of defence and notification during the period.",
   why="Production/distribution clients expect their distribution chain to be protected.",
   support="Tysers clause 8.7 (up to 5x the limit).",
   risk="Medium \u2014 5x aggregate exposure; control-of-defence condition essential.",
   signoff="Yes (S12) \u2014 confirm acceptable aggregate multiple.",
   status="Not accepted \u2014 awaiting UW review"),
 dict(title="11. Worldwide Territory & Jurisdiction (Optional) extension (Section 12)",
   section="Section 12 \u2014 Media Liability", loc="New optional extension after Distributors & Purchasers",
   wording="Schedule-operative only. Where operative, amends the Geographical Limits to anywhere in the world and the Jurisdiction to worldwide; USA/Canada actions covered only if 'USA/Canada Jurisdiction' is ADDITIONALLY stated operative. Default remains worldwide ex-US/Canada.",
   why="Media clients with global digital distribution can face actions outside the default jurisdiction (was Gap 2).",
   support="Tysers PI is worldwide.",
   risk="HIGH if US/Canada operative \u2014 price, sub-limit and higher excess; retain ex-US/Canada as default.",
   signoff="Yes (S12) \u2014 underwriting + confirm reinsurance treaty territory before offering US/Canada.",
   status="Not accepted \u2014 awaiting UW review"),
 dict(title="12. King's Counsel determination clause (Section 12 disputes)",
   section="Section 12 \u2014 Media Liability", loc="New clause after the S12 dispute/mediation provision",
   wording="On a defence/settlement dispute, either party may refer the matter to a mutually-agreed King's Counsel of the English Bar (or Bar Council appointee) whose opinion binds both parties; costs allocated fairly.",
   why="Drafting-clarity improvement; reduces coverage friction on defence disputes.",
   support="Yutree King's Counsel arbitration clause.",
   risk="Low \u2014 procedural.",
   signoff="Yes (S12) \u2014 confirm cost-allocation wording.",
   status="Not accepted \u2014 awaiting UW review"),
 dict(title="13. Pollution negligent-advice write-back (Section 12)",
   section="Section 12 \u2014 Media Liability (Seepage & Pollution exclusion)", loc="Proviso added to the S12 Seepage & Pollution exclusion",
   wording="The exclusion does not apply to a claim arising solely from a negligent act/error/omission in the Insured's Media Business Services (not from the Insured's own pollution), expressly NOT extending to Bodily Injury, property damage or clean-up/remediation costs; Schedule sub-limit.",
   why="Closes a genuine E&O gap created by the outright pollution exclusion (negligent advice/specification).",
   support="Yutree pollution write-back for the insured's own negligence.",
   risk="Medium \u2014 drafting must keep BI, property damage and contamination excluded; cap tightly.",
   signoff="Yes (S12) \u2014 careful legal drafting review essential.",
   status="Not accepted \u2014 awaiting UW review"),
 dict(title="14. Presentational / labelling refinements (technical)",
   section="Section 3 (BI) + Section 15 (Cyber) + Contents", loc="Definitions / headings",
   wording="'Accounts Receivable' re-labelled '(Book Debts)' in S3; Section 15 standardised to 'CyberGuard\u2122 (Cyber Liability)' in the body heading and Contents.",
   why="Like-for-like clarity (Allianz names 'Book Debts'); consistent cyber-section naming.",
   support="Allianz (Book Debts head); internal consistency.",
   risk="Nil\u2013low \u2014 labelling only; no change to cover intended.",
   signoff="Confirm no cover change is implied by the relabelling.",
   status="Not accepted \u2014 awaiting UW review (technical)"),
]


def build_register():
    doc = B.Document()
    B.set_normal_style(doc)
    B.setup_page(doc, landscape=False, margin_cm=1.8)
    B.add_logo_header(doc, left_text="TMHCC Media & Music Combined \u2014 UW Enhancement Register")
    B.add_footer_pagenum(doc, note="UW REVIEW ENHANCEMENT REGISTER \u2014 these items are tracked but NOT accepted; "
                                   "each requires underwriting/legal sign-off. Companion to the Full Redline (Phase 01).")
    B.cover_page(doc,
        "Phase 01 \u00b7 Underwriting Review",
        "UW Enhancement Register",
        "Rounds 7\u20139 wording enhancements held for underwriting / legal sign-off",
        ["Source: TMHCC Media & Music Combined final wording (commit 58b8340) vs 0223C baseline.",
         "Status of every item below: Not accepted \u2014 awaiting UW review.",
         "These enhancements appear in the Full Redline under the separate tracked-change author 'UW Review Enhancement' (yellow-highlighted)."],
        ["TMHCC 0223C baseline", "TMHCC final wording (commit 58b8340)",
         "Competitor support: Tysers, Yutree, Entertainment Elite, Allianz (as cited per item)"])
    doc.add_page_break()

    B.h1(doc, "Enhancement Register \u2014 status summary")
    B.para(doc, "Every enhancement below is identified separately in the Full Redline (author: 'UW Review Enhancement', "
                "yellow highlight) and is NOT accepted pending sign-off. Detail cards follow.", size=9.5)
    tbl = B.make_table(doc, ["#", "Enhancement", "Section", "Priority risk", "Status"],
                       [0.9, 7.2, 4.0, 2.4, 3.5])
    risk_short = {0:"Low",1:"Low\u2013Med",2:"Low\u2013Med",3:"Medium",4:"Low\u2013Med",5:"Medium",
                  6:"Low",7:"Low",8:"Low\u2013Med",9:"Medium",10:"HIGH (US/Can)",11:"Low",12:"Medium",13:"Nil\u2013Low"}
    for idx, e in enumerate(ENH):
        cells = tbl.add_row().cells
        B.text_cell(cells[0], str(idx+1), size=8.5)
        B.text_cell(cells[1], e["title"].split(". ",1)[-1], size=8.5)
        B.text_cell(cells[2], e["section"], size=8)
        B.text_cell(cells[3], risk_short.get(idx, "\u2014"), size=8.5,
                    color=(B.RUST if "HIGH" in risk_short.get(idx,"") else B.INK),
                    bold="HIGH" in risk_short.get(idx,""))
        B.text_cell(cells[4], "Awaiting UW review", size=8)
    B.zebra(tbl)
    doc.add_page_break()

    B.h1(doc, "Enhancement detail cards")
    for e in ENH:
        B.h2(doc, e["title"])
        t = B.make_table(doc, ["Field", "Detail"], [4.0, 14.0])
        rows = [("Section", e["section"]), ("Clause / location", e["loc"]),
                ("Wording inserted / amended", e["wording"]), ("Why it was added", e["why"]),
                ("Gap / competitor support", e["support"]), ("Underwriting / legal risk", e["risk"]),
                ("Sign-off required", e["signoff"]), ("Status", e["status"])]
        for k, v in rows:
            c = t.add_row().cells
            B.text_cell(c[0], k, size=8.5, bold=True, color=B.TEAL)
            B.text_cell(c[1], v, size=8.5,
                        color=(B.RUST if k == "Status" else B.INK),
                        bold=(k == "Status"))
        B.spacer(doc, 6)

    B.save_doc(doc, f"{OUTDIR}/TMHCC_UW_Enhancement_Register.docx")
    print("saved enhancement register:", len(ENH), "items")


build_register()
