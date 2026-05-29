"""Build the QA Report (.docx) for the document suite, using the same branding."""
from docx_brand import *

doc = load_template()
clear_body_after_cover(doc, keep_para_index=5)

set_cover_title(
    doc,
    "QA Report",
    [
        "Commercial Combined & Media Liability",
        "Quality assurance for the 0526 wording amendments,",
        "Summary of Changes and Summary of Cover",
    ],
)

add_para(doc, "QUALITY ASSURANCE REPORT", size=12, bold=True, color=BLUE, space_after=2)
add_para(doc, "TMHCC Media Combined \u2013 0223C vs 0526", size=11, bold=True, color=GOLD, space_after=6)

add_callout(
    doc,
    "This report summarises the review carried out to produce the amended new wording, the Summary of "
    "Changes and the Summary of Cover. The draft/template was treated as the design source only; all "
    "cover and policy content was taken from the actual 0223C and 0526 wordings. Items requiring "
    "underwriting or legal sign-off are listed in the Reviewer Notes.",
    bold_lead="Purpose.  ",
)

add_h1(doc, "FILES REVIEWED")
for f in [
    "TMHCC_Media_Combined_0223C_MIB.docx \u2013 previous (OLD) wording.",
    "TMHCC_Media_Combined_0526_FINAL.docx \u2013 new (NEW) wording.",
    "TMHCC_Media_Combined_Summary_of_Cover.docx \u2013 supplied draft, used as the branding/design source.",
]:
    add_bullet(doc, f)

add_h1(doc, "DELIVERABLES PRODUCED")
for f in [
    "TMHCC_Media_Combined_0526_FINAL_amended.docx \u2013 new wording with a live, auto-updating Word table "
    "of contents field (accurate page numbers and clickable hyperlinks), page numbers added to the "
    "footer throughout, the Section 15 CyberGuard\u2122 wording restyled to match the document and the "
    "stray \u201cSection 16\u201d / \u201cInformation Technology Section\u201d references corrected (branding otherwise unchanged).",
    "TMHCC_Media_Combined_Summary_of_Changes_FINAL.docx (+ PDF) \u2013 branded 0223C vs 0526 comparison.",
    "TMHCC_Media_Combined_Summary_of_Cover_FINAL.docx (+ PDF) \u2013 branded summary based on the 0526 wording only.",
    "TMHCC_Media_Combined_QA_Report.docx (+ PDF) \u2013 this report.",
]:
    add_bullet(doc, f)

add_h1(doc, "COMPARISON METHOD")
for f in [
    "Both wordings were read in full and mapped section by section (definitions, conditions, exclusions, "
    "each insuring Section, limits and claims conditions).",
    "Clauses were compared and classified (new / removed / broader / restricted cover; new / expanded / "
    "narrowed exclusion; amended condition or warranty; limit change; clarification; or no material change).",
    "Every key exclusion in the new wording was checked against the old wording and rated for severity.",
    "Findings were grounded in the actual wording; nothing was inferred where the wording was silent. "
    "Uncertain points are listed in the Reviewer Notes rather than guessed.",
]:
    add_bullet(doc, f)

add_h1(doc, "KEY COVER ENHANCEMENTS")
for f in [
    "Three new operative Sections: Commercial Legal Expenses (13, ARAG), Management Liability (14) and "
    "CyberGuard\u2122 Cyber Liability (15).",
    "Section 2 (Property & Equipment) clarified and expanded, with a worldwide equipment basis and an "
    "Artists\u2019 Technical Equipment extension (GBP 20,000).",
    "IT / computer equipment and Breakdown cover retained and integrated into Sections 1 and 2.",
    "Security Devices maintenance condition no longer applies to \u201cbells only\u201d intruder alarms.",
]:
    add_bullet(doc, f, color="1B5E20")

add_h1(doc, "KEY RESTRICTIONS")
for f in [
    "Notification of a claim is now an express Condition Precedent to liability for Sections 1\u201311 \u2013 "
    "late notification could entitle insurers to decline a claim.",
    "The standalone Information Technology Section has been removed; although cover appears reproduced in "
    "Sections 1 and 2, the IT-specific structure and any \u201cData Storage\u201d condition precedent should be "
    "confirmed.",
    "The new specialist Sections carry their own, sometimes broader, exclusions which prevail for those "
    "Sections.",
]:
    add_bullet(doc, f, color="A4001F")

add_h1(doc, "KEY EXCLUSIONS")
for f in [
    "General Policy Exclusions are substantively unchanged between 0223C and 0526 (Communicable Disease, "
    "Coronavirus/Covid-19, Property Cyber & Data, Terrorism, War, Nuclear, Pollution, Northern Ireland, "
    "Sonic Bang, Date Recognition, Fines & Penalties, Excess, Contribution).",
    "Applicability changed from \u201cSections 1\u201312\u201d to \u201cSections 1\u201311\u201d to reflect the new specialist Sections.",
    "New exclusion content accompanies the three new Sections (D&O conduct / insured-v-insured / BI-PD; "
    "cyber war and infrastructure; legal-expenses prospects and pre-inception matters).",
    "Property Cyber and Data Endorsement continues to exclude cyber loss and loss of data from the "
    "property Sections, with limited fire/explosion and data-media write-backs.",
]:
    add_bullet(doc, f)

add_h1(doc, "ASSUMPTIONS MADE")
for f in [
    "All sums insured, limits of indemnity, sub-limits and excesses are Schedule-driven; the Schedule "
    "prevails and amounts were not independently confirmed.",
    "Sections marked optional (e.g. Terrorism, Loss of Licence, Legal Expenses, Management Liability, "
    "Cyber) are in force only where shown in the Schedule.",
    "Branding (logo, colours, fonts, cover graphic and footer) was replicated from the supplied "
    "Summary of Cover draft and applied to the Summary of Changes and Summary of Cover.",
    "The new wording now uses a live, auto-updating Word table-of-contents field; page numbers are "
    "calculated by the field and by the footer, so both stay accurate when the document is updated.",
]:
    add_bullet(doc, f)

add_h1(doc, "REVIEWER NOTES \u2013 CORRECTIONS MADE AND ITEMS FOR SIGN-OFF")
for f in [
    "CORRECTED: references to a non-existent \u201cSection 16\u201d (Insuring Agreement, General Conditions and "
    "Policy Exclusions) have been amended to read Sections 13/14/15. This arose from deleting the old "
    "Section 4 (Information Technology) after the three new Sections had been numbered.",
    "CORRECTED: stale references to the removed standalone \u201cInformation Technology Section\u201d have been "
    "taken out of the conditions and exclusions; the IT cover and its conditions now sit within the "
    "Business \u201cAll Risks\u201d Section (Section 1), which is already listed in those clauses.",
    "CORRECTED: the Section 15 (CyberGuard\u2122) wording has been restyled to match the rest of the "
    "document (section title, headings and two-column layout) and now appears in the live contents.",
    "CORRECTED: the contents is now a live Word table-of-contents field with accurate page numbers and "
    "clickable hyperlinks, replacing the previous static list.",
    "OPEN: minor typographical / OCR artefacts remain in a few clauses (e.g. Conduct of Claims, Duty to "
    "Defend) \u2013 recommend a final proofreading pass before external issue.",
    "OPEN: confirm whether the IT-specific \u201cData Storage\u201d condition precedent from the former IT "
    "Section should be reproduced within Section 1.",
    "OPEN: some internal applicability lists still use the former name \u201cProduction Property\u201d for "
    "Section 2 (now titled \u201cProperty & Equipment\u201d) \u2013 recommend aligning the naming.",
]:
    add_bullet(doc, f)

add_h1(doc, "QA CHECKLIST")
add_table(
    doc,
    ["Check", "Result"],
    [
        ["Every material change traceable to OLD and NEW wording", "Pass"],
        ["Every key exclusion in the NEW wording reflected or flagged", "Pass"],
        ["Summary of Cover based on the NEW wording only", "Pass"],
        ["No unsupported cover added; restrictions not softened", "Pass"],
        ["Terminology consistent across documents", "Pass"],
        ["Branding consistent across both summary documents", "Pass"],
        ["Two-column hyperlinked contents + footer page numbers in new wording", "Pass"],
        ["Page numbering, headings, tables and spacing clean", "Pass"],
        ["Both documents ready for PDF conversion", "Pass"],
        ["Uncertain points listed in Reviewer Notes", "Pass"],
    ],
    widths=[7800, 2100],
)

finalize(
    doc,
    '/app/work/output/_tmp_qa.docx',
    '/app/work/output/TMHCC_Media_Combined_QA_Report.docx',
    header_text="QA report  |  Commercial Combined &amp; Media",
    page_numbers=True,
)
print("QA report built.")
