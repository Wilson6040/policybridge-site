# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/app/work/compare')
from docx import Document
import brand2 as b

def kv(doc, pairs, w=(4.6, 21.4)):
    t = b.make_table(doc, ["", ""], list(w))
    t.rows[0]._tr.getparent().remove(t.rows[0]._tr)
    for k, v in pairs:
        c = t.add_row().cells
        b.text_cell(c[0], k, size=8.4, bold=True, color=b.TEAL, bg="EAF1F5")
        b.text_cell(c[1], v, size=8.6)
    b.spacer(doc, 6)
    return t

doc = Document()
b.set_normal_style(doc)
b.setup_page(doc, landscape=False, margin_cm=1.7)
b.add_logo_header(doc)
b.add_footer_pagenum(doc)

b.cover_page(
    doc,
    doc_kicker="QA & Change Report \u2014 Media & Music Combined (0526)",
    title="TMHCC Wording Update\nQA / Change Report",
    subtitle="Round 7 \u2014 final wording update and refresh of all supporting market documents. Explains exactly what changed, where, and what still needs underwriting/legal sign-off.",
    meta_lines=[
        "Companion to: final wording (tracked + clean), Full Coverage Comparison, Gap-Fill / Wording Enhancement Strategy and Summary of Cover.",
        "All wording edits shown as fresh tracked changes from a clean accepted baseline. Section 12 items are held for sign-off and are NOT in the wording.",
    ],
    wordings=[
        "Benchmarked against five competitor wordings:",
        "Tysers (Zurich), Yutree (AXA), Liberty, Allianz and AXA XL (XL Catlin).",
    ],
)

# 1 FILES PRODUCED
doc.add_page_break()
b.h1(doc, "Files produced", num="1")
for f in [
  "TMHCC_Media_Combined_0526_FINAL_TrackedChanges.docx \u2014 final wording, NEW edits as tracked changes (from a clean accepted baseline).",
  "TMHCC_Media_Combined_0526_FINAL_Clean.docx \u2014 final wording, clean (new tracked changes accepted).",
  "TMHCC_Media_Coverage_Comparison_FULL.docx \u2014 updated Full Coverage Comparison (deepened strengths).",
  "TMHCC_Media_GapFill_Enhancement_Strategy.docx \u2014 updated Gap-Fill / Wording Enhancement Strategy (copy-paste wording for every recommendation; Section 12 sign-off list; market-leading opportunities).",
  "TMHCC_Media_Combined_Summary_of_Cover_FINAL.docx \u2014 updated Summary of Cover (final wording only).",
  "TMHCC_Media_Combined_QA_Report.docx \u2014 this report.",
]:
    b.bullet(doc, f)
b.callout(doc, "Branding / layout:", "Branding, layout, fonts, headers, footers, numbering and styling are preserved. No section numbering changed, so the contents-page hyperlinks still resolve; the Section 15 contents label was updated as display text only (anchor unchanged).")

# 2 DOCUMENT HANDLING
doc.add_page_break()
b.h1(doc, "Document handling", num="2")
kv(doc, [
  ("Existing tracked changes accepted", "YES \u2014 the uploaded wording contained one residual run-property change (w:rPrChange) and no insertions/deletions; it was accepted to form a clean baseline saved internally."),
  ("Fresh tracked changes for new edits", "YES \u2014 all new amendments applied as new tracked changes (author 'TMHCC Wording Review') on the accepted baseline: 9 insertions, 2 deletions."),
  ("Clean final version produced", "YES \u2014 a clean copy with the new tracked changes accepted is also delivered."),
  ("Old tracked changes carried forward", "NO."),
])

# 3 CHANGE LOG (wording)
doc.add_page_break()
b.h1(doc, "Change log \u2014 wording (tracked)", num="3")

b.h3(doc, "Task 1 \u2014 Admission of Liability (claims condition precedent removed/softened)")
kv(doc, [
  ("Location", "Policy Claims Conditions (Applicable to Sections 1\u201311) \u2192 sub-heading 'Admission of Liability' (contents p.17)."),
  ("Old wording (deleted)", "'It is a condition precedent to liability under this Policy that no admission of liability, promise, payment, compensation, negotiation or settlement of any claim shall be made or given without the Insurer\u2019s written consent.'"),
  ("New wording (inserted)", "'The Insured shall not, without the Insurer\u2019s written consent, make any admission of liability, promise, payment, compensation, offer, negotiation or settlement of any claim. The Insurer shall not be entitled to rely on any breach of this condition to reduce or refuse a claim except to the extent that the Insurer\u2019s position has been prejudiced by the breach.'"),
  ("Effect", "Converts a blanket condition precedent into an ordinary condition with a prejudice qualifier \u2014 aligns with the competitor market. No other cover changed."),
])

b.h3(doc, "Task 1 \u2014 policy-wide claims condition-precedent audit")
b.para(doc, "The whole document was audited. Result:", size=9)
t = b.make_table(doc, ["Clause", "Location", "Type", "Decision"], [6.0, 4.2, 4.6, 3.6])
audit = [
  ("Admission of Liability", "Policy Claims Conditions (S1\u201311)", "Blanket claims CP", "Replaced (Task 1)"),
  ("Notification of a Claim (S1\u201311)", "Policy Claims Conditions (S1\u201311)", "General claims notification", "NOT a CP ('will notify\u2026 as soon as practicable') \u2014 left as-is"),
  ("Notification to the Police", "Policy Claims Conditions (S1\u201311)", "Theft/loss reporting CP", "Retained (scope-limit)"),
  ("Claim/Circumstance Notification (S13)", "Notification & Claims Conditions \u2014 S13", "Section-level notification CP", "Retained (section-level)"),
  ("Notification of Claims (S12)", "Section 12 claims conditions", "Section-level notification CP", "Retained (section-level; S12 sign-off)"),
  ("Notice provisions (S14)", "Section 14", "Section-level notification CP", "Retained (section-level)"),
  ("Cooperation / excess (S15)", "Section 15 (CyberGuard)", "Section-level conditions", "Retained (section-level)"),
  ("Data storage / back-up (S1)", "Section 1 IT property condition", "Risk-improvement CP", "Retained (scope-limit)"),
  ("Unattended-vehicle / security / hire", "Sections 1\u20132 / Money", "Security / risk conditions", "Retained (scope-limit)"),
  ("Rushes / originals / negatives storage", "Section 11", "Storage CPs", "Retained (scope-limit)"),
  ("Hazardous-activity risk assessment", "Section claims conditions", "Risk-improvement CP", "Retained (scope-limit)"),
]
for r in audit:
    c = t.add_row().cells
    b.text_cell(c[0], r[0], size=7.9, bold=True, color=b.TEAL)
    b.text_cell(c[1], r[1], size=7.8)
    b.text_cell(c[2], r[2], size=7.8)
    col = "2E7D44" if "Retained" in r[3] or "left as-is" in r[3] else "A4233B"
    b.text_cell(c[3], r[3], size=7.8, bold=True, color=col)
b.zebra(t)
b.callout(doc, "Audit conclusion:", "No remaining GENERAL / policy-wide claims-notification or claims-cooperation requirement is described as a condition precedent. The section-level notification CPs and the security/storage/risk-improvement CPs are normal and were left intact per the scope limit.")

b.h3(doc, "Task 2 \u2014 Proof of Ownership and Value (new claims requirement)")
kv(doc, [
  ("Location inserted", "Policy Claims Conditions (Applicable to Sections 1\u201311), as a new headed claims condition placed (alphabetically) between 'Notification to the Police' and 'Terms of Settlement' (contents p.17)."),
  ("Applies to", "Sections 1\u201311 (spans Property & Equipment, Goods in Transit and Money). Item-level \u2014 not a blanket condition precedent or forfeiture."),
  ("Wording inserted", "'Following any claim for theft or loss, the Insurer may request reasonable evidence of ownership and value in respect of any high value item or any item insured on an Agreed Value basis \u2026 The Insured shall provide such evidence within a reasonable period \u2026 The Insurer shall not be obliged to pay any claim, or part of a claim, for an affected item where the Insured fails to provide the evidence reasonably requested.'"),
  ("Schedule cross-reference", "References items insured on an 'Agreed Value' basis (Section 2 uses an Agreed Value Basis of Settlement). No new Schedule definition required; 'high value item' is left to the Schedule/sub-limits."),
])

b.h3(doc, "Task 4 \u2014 Gap 8 (ICOW / Book Debts) implemented")
kv(doc, [
  ("Location", "Section 3 (Business Interruption) \u2014 Definitions and Basis of Settlement, 'Accounts Receivable' head (contents p.38)."),
  ("Change", "'Accounts Receivable' re-labelled 'Accounts Receivable (Book Debts)' in both the Definitions and the Basis of Settlement (tracked insertion)."),
  ("Why", "Increase in Cost of Working and Additional Increase in Cost of Working are ALREADY named, discrete settlement heads; book-debts cover already exists as 'Accounts Receivable'. The only refinement needed was presentational labelling for like-for-like comparison with Allianz/AXA XL. No cover broadened; no sign-off."),
])

b.h3(doc, "Task 11 \u2014 Section 15 title standardised")
kv(doc, [
  ("Body heading", "'Section 15 - CyberGuard\u2122' \u2192 'Section 15 - CyberGuard\u2122 (Cyber Liability)' (tracked insertion)."),
  ("Contents entry", "'Section 15: Cyber Liability Section' \u2192 'Section 15: CyberGuard\u2122 (Cyber Liability)' (tracked; hyperlink anchor unchanged)."),
  ("Summary of Cover", "Updated to 'CyberGuard\u2122 (Cyber Liability)' (table + section header)."),
  ("Section 11", "Left as 'Production Indemnity \u201cAll Risks\u201d' \u2014 already consistent."),
  ("Decision", "Default label 'CyberGuard\u2122 (Cyber Liability)' adopted. SEE REVIEWER NOTES \u2014 confirm preferred label."),
])

# 4 GAP POSITIONS
doc.add_page_break()
b.h1(doc, "Gap 2 / 8 / 10 \u2014 final positions", num="4")
b.h3(doc, "Gap 2 \u2014 Worldwide / WW Media Liability (Section 12 \u2014 sign-off)")
b.para(doc, "Current wording: Section 12 territory is bounded by the Schedule 'Geographical Limits' and the 'Jurisdiction' definition (default = worldwide EXCLUDING the USA and Canada where the Schedule is silent); the 'Legal Action' exclusion bars claims brought, or governed by laws, outside the Jurisdiction. There is no single clean Schedule-selectable 'Worldwide (incl. USA/Canada)' switch. A drafted optional 'Worldwide Territory and Jurisdiction (Optional)' provision plus a separate 'USA/Canada Jurisdiction' selectable is held in the Section 12 sign-off list (Gap-Fill Summary). NOT applied to the wording \u2014 ALL Section 12 changes require legal/underwriting sign-off.", align='just')
b.h3(doc, "Gap 8 \u2014 ICOW / Book Debts (implemented)")
b.para(doc, "Already substantially met: ICOW and AICOW are named settlement heads in Section 3 and book-debts cover exists as 'Accounts Receivable'. Implemented as a presentational label '(Book Debts)' (tracked). No broadening; no sign-off.", align='just')
b.h3(doc, "Gap 10 \u2014 Breakdown / Yutree position")
b.para(doc, "Section 1 (Premises) DEFINES 'Breakdown' and covers/pays Information Technology Property 'Breakdown' (definition, 'The Cover', Basis of Settlement) \u2014 the old Section 4 IT-Property breakdown, preserved faithfully; this matches Yutree\u2019s dedicated Computer Breakdown section. Section 2 carries a 'Mechanical and Electrical Breakdown' OPTIONAL EXTENSION with its own broad Breakdown definition covering ALL Property Insured \u2014 this mirrors Yutree\u2019s general 'Mechanical and electrical breakdown cover'. No wording change made (no general breakdown added to Section 2; nothing removed). SEE REVIEWER NOTES.", align='just')

# 5 SIGN-OFF
doc.add_page_break()
b.h1(doc, "Items requiring legal / underwriting sign-off", num="5")
for s in [
  "Gap 2 \u2014 Worldwide Territory & Jurisdiction (Optional) and the separate USA/Canada selectable (Section 12).",
  "Section 12 enhancements held in the sign-off list: Distributors & Purchasers; Criminal/Regulatory defence costs (or S13/S14 cross-reference); Journalistic Source Protection costs; Representation Costs at Investigations (GBP 25k); Asbestos/Pollution professional-duty write-back (negligent advice only); King\u2019s Counsel determination clause; 'Media Material' definition; Reputation Management / Withdrawal of Content optional uplift.",
  "Any decision to narrow the Section 2 Mechanical & Electrical Breakdown optional extension to IT-only (would remove existing cover and make TMHCC narrower than Yutree).",
  "Any decision to add a Personal Accident & Business Travel section (NOT added in this round).",
  "Confirmation of the Section 15 label.",
]:
    b.bullet(doc, s)
b.callout(doc, "Section 12 control:", "No Section 12 change appears in the tracked-changes wording or the clean final wording. They are presented only as suggested upgrades with copy-paste wording, exact location, amendment type, rationale/competitor support and a sign-off note in the Gap-Fill Summary.")

# 6 STRENGTHS / UNCONFIRMED
doc.add_page_break()
b.h1(doc, "TMHCC strengths added to the comparison (and UNCONFIRMED items)", num="6")
b.para(doc, "Six strength areas were expanded and evidenced against the final wording, each with our clause/page and a competitor benchmark: (1) Flexible first-loss Business Interruption; (2) Contract Site extension (Section 3); (3) Section 2 worldwide Property & Equipment; (4) floating contents across premises; (5) higher limits / broader extensions; (6) US / USA-Canada / jurisdiction.", align='just')
b.para(doc, "Competitor wordings ARE attached (Tysers, Yutree, Liberty, Allianz, AXA XL), so 'market-leading' claims are evidence-based rather than blanket-UNCONFIRMED. Where a specific competitor figure could not be re-confirmed clause-by-clause from the extract, it is labelled UNCONFIRMED in the comparison: competitor BI flexibility/parity, contract-site/supplier extensions, location-basis (floating contents) and competitor transit day-limits. CONFIRMED from extracts: TMHCC virus-transmission sub-limit GBP 500k vs Tysers GBP 250k; Liberty/Allianz/AXA XL carry no media/PI/cyber/legal/management cover.", align='just')

# 7 FINAL QA CHECKLIST
doc.add_page_break()
b.h1(doc, "Final QA checklist", num="7")
checks = [
  ("All old tracked changes accepted before new edits", "YES"),
  ("New edits shown as fresh tracked changes", "YES (9 ins / 2 del)"),
  ("Clean final version produced", "YES"),
  ("Blanket Admission-of-Liability CP removed/replaced", "YES"),
  ("Remaining policy-wide claims CPs audited; section-level/security CPs intact", "YES"),
  ("Proof-of-ownership claims requirement added", "YES (Sections 1\u201311)"),
  ("Gap 2 resolved/clarified (Section 12 \u2014 sign-off)", "YES (held for sign-off)"),
  ("Gap 8 implemented", "YES (Section 3 \u2014 Book Debts label)"),
  ("Gap 10 resolved with Yutree / old Section 4 comparison", "YES (no change; flagged)"),
  ("Section 12 amendments held in sign-off list with copy-paste wording", "YES"),
  ("Section 15 title standardised", "YES (confirm label)"),
  ("Full Coverage Comparison updated against final wording", "YES"),
  ("Gap-Fill Summary includes copy-paste wording for every recommendation", "YES"),
  ("Summary of Cover updated against final wording only", "YES"),
  ("No Personal Accident added; Personal Assault under Money treated correctly", "YES"),
  ("TMHCC strengths expanded and evidenced (UNCONFIRMED labelled)", "YES"),
  ("US/jurisdiction position checked", "YES"),
  ("No unsupported cover invented", "YES"),
  ("Contents-page hyperlinks & section numbering still resolve", "YES (numbering unchanged)"),
  ("All uncertain points in Reviewer Notes", "YES"),
]
t = b.make_table(doc, ["Check", "Status"], [19.5, 6.5])
for k, v in checks:
    c = t.add_row().cells
    b.text_cell(c[0], k, size=8.4)
    b.text_cell(c[1], v, size=8.4, bold=True, color="2E7D44", align='center')
b.zebra(t)

# 8 REVIEWER NOTES
doc.add_page_break()
b.h1(doc, "Reviewer notes (uncertain / for confirmation)", num="8")
for n in [
  "Section 15 label: default adopted is 'CyberGuard\u2122 (Cyber Liability)'. Confirm this is the preferred single label for the body heading, contents and Summary of Cover.",
  "Gap 10 location: the brief states the IT-Property breakdown sits 'under Section 2'. In the live wording the IT-Property 'Breakdown' definition and cover are in SECTION 1 (Premises), with consequential computer cover in Section 3 (BI). Section 2 holds only a general 'Mechanical and Electrical Breakdown' optional extension. Confirm this is understood and acceptable.",
  "Gap 10 / Section 2: the existing Section 2 Mechanical & Electrical Breakdown optional extension covers ALL Property Insured (not IT-only) and mirrors Yutree\u2019s general M&E breakdown cover. Narrowing it to 'IT-only' would remove existing optional cover and make TMHCC narrower than Yutree \u2014 NOT done. Confirm whether any narrowing is actually wanted (would require sign-off).",
  "All Section 12 amendments (incl. Gap 2 worldwide and the reputation-management uplift) are suggestions held for legal/underwriting sign-off \u2014 none is final or in the wording.",
  "Competitor parity statements labelled UNCONFIRMED should be re-checked clause-by-clause against the live competitor wordings before being used externally.",
  "Proof of Ownership: 'high value item' is intentionally left to the Schedule/sub-limits rather than given a fixed monetary threshold \u2014 confirm whether a defined threshold is preferred.",
  "PDF copies: generated where the document-conversion toolchain (LibreOffice) is available in the environment; otherwise the .docx files are the authoritative deliverables.",
]:
    b.bullet(doc, n)
b.spacer(doc, 6)
b.para(doc, "End of QA / Change Report.", italic=True, color=b.GREY, size=8.5)

out = "/app/work/output/TMHCC_Media_Combined_QA_Report.docx"
b.save_doc(doc, out)
print("Saved:", out)
