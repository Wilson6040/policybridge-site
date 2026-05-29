import sys
sys.path.insert(0, '/app/work')
sys.path.insert(0, '/app/work/r8')
"""Build the FINAL Summary of Changes (.docx) from the branded template.
Compares the OLD 0223C wording against the NEW 0526 wording."""
from docx_brand import *
from docx_brand import _set_table_full_width, _set_table_borders, _set_cell_text
import r8data as r8

doc = load_template()
clear_body_after_cover(doc, keep_para_index=5)

# ---- Re-brand the cover banner for "Summary of Changes" ----
set_cover_title(
    doc,
    "Summary of Changes",
    [
        "Commercial Combined & Media Liability",
        "Comparison of policy wording 0223C (previous) and the final wording (0526 + Round-8 enhancements)",
        "Prepared for broker and client use",
    ],
)

# ---------- Title / basis ----------
add_para(doc, "WORDING COMPARISON:  0223C  \u2192  0526", size=12, bold=True, color=BLUE, space_after=2)
add_para(doc, "SUMMARY OF CHANGES", size=11, bold=True, color=GOLD, space_after=6)

add_callout(
    doc,
    "This Summary of Changes compares the previous wording (TMHCC Media Combined 0223C) with the new "
    "wording (TMHCC Media Combined 0526). It is a high-level guide for brokers and clients and does not "
    "replace either policy wording, the Schedule or any endorsement. Where a change reduces, restricts "
    "or qualifies cover this is stated plainly. Limits, sub-limits and excesses are governed by the "
    "Schedule. Items marked for review require confirmation by underwriting/legal.",
    bold_lead="Basis of this comparison.  ",
)

# Traffic-light legend
add_h2(doc, "Status key")
leg = doc.add_table(rows=1, cols=3)
_set_table_full_width(leg)
_set_table_borders(leg)
_set_cell_text(leg.rows[0].cells[0], "Green \u2013 broader / beneficial", size=9, bold=True, color="1B5E20", bg="E2F3E8", align='center')
_set_cell_text(leg.rows[0].cells[1], "Amber \u2013 clarification / operational", size=9, bold=True, color="7A5800", bg="FBF1D6", align='center')
_set_cell_text(leg.rows[0].cells[2], "Red \u2013 restriction / reduced cover", size=9, bold=True, color="A4001F", bg="FBE3E8", align='center')
add_para(doc, "", space_after=4)

# ---------- Executive summary ----------
add_h1(doc, "EXECUTIVE SUMMARY")
add_para(doc, "The 0526 wording is a substantial restructure and expansion of the 0223C wording. The "
              "policy grows from 13 to 15 operative Sections, with three significant new covers: "
              "Commercial Legal Expenses (Section 13, underwritten by ARAG), Management Liability "
              "(Section 14) and CyberGuard\u2122 Cyber Liability (Section 15).")
add_para(doc, "The property account has been restructured. The standalone Information Technology Section "
              "in 0223C has been removed and its cover (including computer equipment and Breakdown) "
              "consolidated into the Business \u201cAll Risks\u201d Section (now \u201cPremises Risk only\u201d) and the "
              "renamed and expanded Property & Equipment Section (formerly \u201cProduction Property\u201d). "
              "Sections from the old Section 4 onward have been renumbered.")
add_para(doc, "The General Policy Definitions, Conditions and Exclusions are largely carried across "
              "without material change. The most important wording change for claims handling is that "
              "notification of a claim is now expressed as a Condition Precedent to liability for "
              "Sections 1\u201311. The new specialist Sections each carry their own definitions, exclusions "
              "and claims conditions, which prevail for those Sections.")

# ---------- Headline changes at a glance ----------
add_h1(doc, "HEADLINE CHANGES AT A GLANCE")
add_table(
    doc,
    ["Area", "What changed (0223C \u2192 0526)", "Status"],
    [
        ["Policy structure", "Expanded from 13 to 15 operative Sections", "neutral"],
        ["Commercial Legal Expenses", "New Section 13 (ARAG) \u2013 legal costs for insured events", "new"],
        ["Management Liability", "New Section 14 \u2013 D&O / corporate / employment practice", "new"],
        ["Cyber Liability", "New Section 15 \u2013 CyberGuard\u2122 first & third-party cyber", "new"],
        ["Information Technology", "Standalone IT Section removed; IT & Breakdown cover folded into Sections 1 & 2", "clarify"],
        ["Property restructure", "Section 2 renamed Production Property \u2192 Property & Equipment; Section 1 now \u201cPremises Risk only\u201d", "neutral"],
        ["Section numbering", "Sections renumbered from old Section 4 onward", "clarify"],
        ["Claim notification", "Now an express Condition Precedent to liability (Sections 1\u201311)", "restrictive"],
        ["Intruder alarm condition", "Maintenance condition now excludes \u201cbells only\u201d alarms", "clarify"],
        ["General exclusions", "Substantively unchanged; now apply to Sections 1\u201311 (was 1\u201312)", "neutral"],
    ],
    widths=[2300, 5500, 1900],
    status_col=2,
)

# ---------- Cover enhancements ----------
add_h1(doc, "COVER ENHANCEMENTS (BROADER / BENEFICIAL)")
for e in [
    "Three new insuring Sections \u2013 Commercial Legal Expenses, Management Liability and CyberGuard\u2122 "
    "Cyber Liability \u2013 materially broaden the package where selected in the Schedule.",
    "Section 2 (Property & Equipment) has a clearer, expanded scope, with an explicit worldwide "
    "Geographical Limit and a dedicated Artists\u2019 Technical Equipment extension (GBP 20,000).",
    "Computer / IT equipment and Breakdown cover is retained and integrated into Section 1, which now "
    "expressly lists the IT extensions (Accidental Discharge, Additional Rental Charge, Expediting "
    "Costs, Incompatibility and Involuntary Betterment).",
    "The Security Devices maintenance condition no longer applies to \u201cbells only\u201d intruder alarms, a "
    "small easing of the protection requirement.",
]:
    add_bullet(doc, e, color="1B5E20")
add_para(doc, "Enhancements are subject to the Schedule, the relevant limits and each Section\u2019s own terms.",
         size=9, italic=True, color=GREY, space_before=2)

# ---------- Cover restrictions ----------
add_h1(doc, "COVER RESTRICTIONS / REDUCTIONS AND ITEMS TO CHECK")
add_bullet(doc, "Claim notification (Sections 1\u201311) is now an express Condition Precedent to liability \u2013 "
                "late notification could entitle insurers to decline a claim. This is the single most "
                "important change for the insured to understand.", color="A4001F")
add_bullet(doc, "The standalone Information Technology Section has been removed. Its cover appears to be "
                "reproduced within Sections 1 and 2, but the discrete IT structure (and any IT-specific "
                "\u201cData Storage\u201d condition precedent) should be checked to confirm there is no gap in "
                "breakdown cover or IT extensions.", color="7A5800")
add_bullet(doc, "The new specialist Sections (13, 14, 15) each carry their own, sometimes broader, "
                "exclusions and conditions which prevail over the General Policy terms for those "
                "Sections.", color="7A5800")
add_bullet(doc, "Carried-over conditions and exclusions previously referenced the now-removed "
                "\u201cInformation Technology Section\u201d; these have been corrected in the final amended "
                "wording so the cover applies via the Business \u201cAll Risks\u201d Section, which now "
                "contains the IT Property cover (see Reviewer Notes).", color="7A5800")

# ---------- Exclusions deep dive ----------
add_h1(doc, "EXCLUSIONS DEEP DIVE")
add_para(doc, "Each key exclusion in the new wording is assessed below against the previous wording.",
         size=9, italic=True, color=GREY)
add_table(
    doc,
    ["Exclusion", "Status vs 0223C", "Practical impact for the insured", "Severity"],
    [
        ["Communicable Disease", "Unchanged (renumbered)", "Disease-related loss excluded across property/BI; no change in effect", "Low"],
        ["Coronavirus / Covid-19", "Unchanged (sections renumbered 7&8 \u2192 6&7)", "Covid-related liability excluded on PL/Products where shown", "Low"],
        ["Property Cyber and Data Endorsement", "Unchanged wording", "Cyber loss and loss of data excluded from the property Sections; limited fire/explosion and data-media write-backs retained", "Medium"],
        ["Terrorism (non-Terrorism Sections)", "Unchanged", "Property/BI terrorism excluded unless the Terrorism Section is operative", "Low"],
        ["War & Kindred Risks", "Unchanged", "War and related perils excluded", "Low"],
        ["Nuclear / Pollution / Northern Ireland / Sonic Bang", "Unchanged", "No change in effect (Pollution retains GBP 500,000 Production Property write-back)", "Low"],
        ["Date Recognition / Fines & Penalties / Excess / Contribution", "Unchanged", "No change in effect", "Low"],
        ["Section 14 (Management Liability) exclusions", "New", "Conduct, insured-v-insured, bodily injury/property damage, pollution and Loss carve-outs apply to the new D&O cover", "Medium"],
        ["Section 15 (Cyber) exclusions", "New", "War and failure of core infrastructure, prior known incidents and betterment excluded under the new cyber cover", "Medium"],
        ["Section 13 (Legal Expenses) exclusions", "New", "No reasonable prospects, pre-inception matters, dishonesty and unconsented costs excluded", "Medium"],
    ],
    widths=[2600, 2200, 3700, 1200],
)
add_para(doc, "Conclusion: the General Policy exclusions are substantively unchanged between 0223C and "
              "0526. The additional exclusion content in the new wording accompanies the three new "
              "Sections and should be explained to clients when those Sections are selected.",
         size=9, italic=True, color=GREY)

# ---------- Conditions / warranties / claims ----------
add_h1(doc, "CONDITIONS, WARRANTIES AND CLAIMS CHANGES")
add_table(
    doc,
    ["Condition / clause", "0223C", "0526", "Status"],
    [
        ["Notification of a claim (Sections 1\u201311)", "\u201cThe Insured shall notify \u2026 as soon as practicable\u201d", "\u201cIt is a Condition Precedent to liability \u2026 will notify \u2026 as soon as practicable\u201d", "restrictive"],
        ["Security Devices (intruder alarm)", "Applies to any Intruder Alarm Installation", "Applies to alarms \u201cother than a bells only\u201d", "clarify"],
        ["Counsel reference", "\u201cQueens Counsel\u201d", "\u201cKing\u2019s Counsel\u201d", "clarify"],
        ["Claims conditions applicability", "Sections 1\u201312", "Sections 1\u201311; 12\u201315 where stated; 14\u201315 have own provisions", "neutral"],
        ["Notification to the Police", "Condition precedent + \u201cmay prejudice\u201d softener", "Condition precedent (softener removed)", "clarify"],
        ["Protection & Maintenance conditions", "Sections 1\u201312", "Sections 1\u201311 (substantively carried over)", "neutral"],
        ["Production Indemnity conditions precedent", "Production planning, rushes, duplicates, etc.", "Retained without material change", "neutral"],
    ],
    widths=[2600, 3100, 3100, 1100],
    status_col=3,
)

# ---------- Limits changes ----------
add_h1(doc, "LIMITS, SUB-LIMITS AND EXCESS CHANGES")
for b in [
    "Carried-over sub-limits appear consistent between the wordings, including witness/court "
    "attendance costs (GBP 500 / GBP 200 per day), Criminal Prosecution Defence Costs (GBP 250,000; "
    "GBP 5,000,000 for manslaughter), asbestos and pollution fire/explosion write-backs (GBP 500,000) "
    "and the Media Liability Virus sub-limit (GBP 500,000).",
    "New limits introduced with the new Sections: Legal Expenses GBP 100,000 per claim / GBP 1,000,000 "
    "aggregate employment compensation; Production Indemnity Agency & Talent Costs GBP 30,000; Section 2 "
    "Artists\u2019 Technical Equipment GBP 20,000; Cyber Court Attendance GBP 500 per day; Management "
    "Liability and Cyber limits as stated in the Schedule.",
    "All sums insured, limits of indemnity, sub-limits and excesses remain Schedule-driven \u2013 confirm "
    "the amounts against the Schedule for each operative Section.",
]:
    add_bullet(doc, b)

# ---------- Section-by-section comparison ----------
add_h1(doc, "SECTION-BY-SECTION COMPARISON")
add_table(
    doc,
    ["0223C Section", "0526 Section", "Status"],
    [
        ["1 \u2013 Business \u201cAll Risks\u201d", "1 \u2013 Business \u201cAll Risks\u201d (Premises Risk only; now incl. IT & Breakdown)", "broader"],
        ["2 \u2013 Production Property \u201cAll Risks\u201d", "2 \u2013 Property & Equipment \u201cAll Risks\u201d (renamed / expanded)", "broader"],
        ["3 \u2013 Business Interruption \u201cAll Risks\u201d", "3 \u2013 Business Interruption \u201cAll Risks\u201d", "neutral"],
        ["4 \u2013 Information Technology", "Removed \u2013 consolidated into Sections 1 & 2", "clarify"],
        ["5 \u2013 Terrorism", "4 \u2013 Terrorism", "neutral"],
        ["6 \u2013 Employers\u2019 Liability", "5 \u2013 Employers\u2019 Liability", "neutral"],
        ["7 \u2013 Public Liability", "6 \u2013 Public Liability", "neutral"],
        ["8 \u2013 Products Liability", "7 \u2013 Products Liability", "neutral"],
        ["9 \u2013 Money", "8 \u2013 Money", "neutral"],
        ["10 \u2013 Goods in Transit", "9 \u2013 Goods in Transit", "neutral"],
        ["11 \u2013 Loss of Licence", "10 \u2013 Loss of Licence", "neutral"],
        ["12 \u2013 Production Indemnity \u201cAll Risks\u201d", "11 \u2013 Production Indemnity \u201cAll Risks\u201d", "neutral"],
        ["13 \u2013 Media Liability", "12 \u2013 Media Liability", "neutral"],
        ["\u2014", "13 \u2013 Commercial Legal Expenses (ARAG)", "new"],
        ["\u2014", "14 \u2013 Management Liability", "new"],
        ["\u2014", "15 \u2013 CyberGuard\u2122 Cyber Liability", "new"],
    ],
    widths=[3200, 4600, 1900],
    status_col=2,
)

# ---------- Round-8 wording enhancements (final wording) ----------
add_h1(doc, "ROUND-8 WORDING ENHANCEMENTS (FINAL WORDING)")
add_para(doc, "In addition to the 0223C \u2192 0526 restructure summarised above, the FINAL wording incorporates "
              "the following discrete, individually accept/reject-able enhancements. In the tracked-changes "
              "wording these are captured in full against the 0223C baseline. Every Section 12 (Media "
              "Liability) item is applied as a tracked change but REQUIRES legal/underwriting sign-off.",
              size=9.5)
_chg_rows = [[c[0], c[1], c[2], c[5]] for c in r8.CHANGE_LOG]
add_table(
    doc,
    ["Ref", "Location", "Change", "Sign-off"],
    _chg_rows,
    widths=[1.5, 4.4, 8.6, 2.0],
)
add_para(doc, "", space_after=2)
add_para(doc, "Items deliberately NOT added: Personal Accident and Travel. Personal Assault under the Money "
              "Section (Section 8, Sub-Section 2) is distinct from Personal Accident and is retained unchanged. "
              "Patent infringement is deliberately left excluded; an asbestos negligent-advice write-back is "
              "parked for consideration. No existing sub-limit was lowered; TMHCC already meets or exceeds "
              "every evidenced competitor sub-limit, or is schedule-driven.", size=9, italic=True, color=GREY)

# ---------- Broker/client points ----------
add_h1(doc, "BROKER / CLIENT COMMUNICATION POINTS")
for b in [
    "Three significant new covers are now available \u2013 discuss whether to select Commercial Legal "
    "Expenses, Management Liability and Cyber, and the limits required.",
    "Explain the new claim-notification Condition Precedent \u2013 prompt notification is essential to "
    "protect the right to claim.",
    "Confirm that the IT / computer equipment and Breakdown cover now sitting in Sections 1 and 2 meets "
    "the client\u2019s needs, with no gap against the former Information Technology Section.",
    "Highlight that the new Sections operate on a claims-made basis and carry their own exclusions and "
    "conditions.",
    "Re-check sums insured, limits and excesses in the Schedule, particularly for the new Sections.",
]:
    add_bullet(doc, b)

# ---------- Reviewer notes ----------
add_h1(doc, "REVIEWER NOTES (FOR UNDERWRITING / LEGAL SIGN-OFF)")
add_para(doc, "The drafting points originally identified in the supplied 0526 wording have been "
              "corrected in the final amended wording delivered alongside this document. They are "
              "recorded here for transparency, with the items still recommended for sign-off.",
              size=9, italic=True, color=GREY)
for n in [
    "CORRECTED: references to a non-existent \u201cSection 16\u201d (Insuring Agreement, General Conditions and "
    "Policy Exclusions) have been amended to read Sections 13/14/15. This arose from deleting the old "
    "Section 4 (Information Technology) after the three new Sections had been numbered.",
    "CORRECTED: stale references to the removed standalone \u201cInformation Technology Section\u201d have been "
    "taken out of the conditions and exclusions; the IT cover and its conditions now sit within the "
    "Business \u201cAll Risks\u201d Section (Section 1), which is already listed in those clauses.",
    "CORRECTED: the Section 15 (CyberGuard\u2122) wording has been restyled to match the rest of the "
    "document and now appears in the live table of contents.",
    "OPEN: minor typographical / OCR artefacts remain in a few clauses (e.g. Conduct of Claims, Duty to "
    "Defend) \u2013 recommend a final proofreading pass before external issue.",
    "OPEN: confirm whether the IT-specific \u201cData Storage\u201d condition precedent from the former IT "
    "Section should be reproduced within Section 1.",
    "OPEN: some internal applicability lists still use the former name \u201cProduction Property\u201d for "
    "Section 2 (now titled \u201cProperty & Equipment\u201d) \u2013 recommend aligning the naming.",
    "All limits and excesses are Schedule-driven; this comparison does not confirm amounts.",
    "This document is a professional comparison aid prepared from the supplied wordings. It does not "
    "constitute legal advice and does not alter the policy wording; material points should be confirmed "
    "with underwriting / legal sign-off.",
]:
    add_bullet(doc, n)

finalize(
    doc,
    '/app/work/r8/_tmp_changes.docx',
    '/app/work/r8/TMHCC_Media_Combined_Summary_of_Changes_FINAL.docx',
    header_text="Summary of changes  |  Commercial Combined &amp; Media",
    page_numbers=True,
)
print("Summary of Changes built.")
print("paras:", len(doc.paragraphs), "tables:", len(doc.tables))
