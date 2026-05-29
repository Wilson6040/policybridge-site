# -*- coding: utf-8 -*-
"""PHASE 08 — Final pack assembly (docx copy) + Final QA Report."""
import sys, json, shutil, os
sys.path.insert(0, "/app/work/compare")
import brand2 as B

PACK = "/app/outputs/final-pack"
os.makedirs(PACK, exist_ok=True)
stats = json.load(open("/app/work/r10/redline_stats.json"))

FILES = [
 ("/app/outputs/phase-01-full-redline/TMHCC_0223C_to_Final_Full_Redline.docx", "TMHCC_0223C_to_Final_Full_Redline.docx"),
 ("/app/outputs/phase-01-full-redline/TMHCC_Final_Clean.docx", "TMHCC_Final_Clean.docx"),
 ("/app/outputs/phase-01-full-redline/TMHCC_UW_Enhancement_Register.docx", "TMHCC_UW_Enhancement_Register.docx"),
 ("/app/outputs/phase-02-change-summary/TMHCC_0223C_to_Final_Change_Summary.docx", "TMHCC_0223C_to_Final_Change_Summary.docx"),
 ("/app/outputs/phase-03-competitor-legal-review/TMHCC_Six_Insurer_Legal_Review_Reset.docx", "TMHCC_Six_Insurer_Legal_Review_Reset.docx"),
 ("/app/outputs/phase-04-coverage-comparison/TMHCC_Six_Insurer_Coverage_Comparison.docx", "TMHCC_Six_Insurer_Coverage_Comparison.docx"),
 ("/app/outputs/phase-05-gap-fill-strategy/TMHCC_Gap_Fill_Strategy.docx", "TMHCC_Gap_Fill_Strategy.docx"),
 ("/app/outputs/phase-06-policybridge-workflow-playbook/PolicyBridge_Wording_Studio_Workflow_Playbook.docx", "PolicyBridge_Wording_Studio_Workflow_Playbook.docx"),
 ("/app/outputs/phase-07-policybridge-audit-prompt/PolicyBridge_Wording_Studio_Audit_Rebuild_Prompt.docx", "PolicyBridge_Wording_Studio_Audit_Rebuild_Prompt.docx"),
]

for src, name in FILES:
    shutil.copyfile(src, os.path.join(PACK, name))
print("copied", len(FILES), "docx to final-pack")


def qa():
    doc = B.Document()
    B.set_normal_style(doc)
    B.setup_page(doc, landscape=False, margin_cm=1.8)
    B.add_logo_header(doc, left_text="TMHCC Media & Music Combined \u2014 Final QA Report")
    B.add_footer_pagenum(doc, note="Final QA Report \u2014 TMHCC full-redline reset + six-insurer legal review + PolicyBridge blueprint.")
    B.cover_page(doc,
        "Final QA Report",
        "Final QA Report",
        "Quality assurance for the full-redline reset, six-insurer legal review and PolicyBridge blueprint",
        ["Baseline: TMHCC 0223C. Final wording: TMHCC Media & Music Combined (commit 58b8340).",
         "All completed outputs are saved in separate phase folders so no failed phase corrupts completed work.",
         "Every enhancement remains subject to TMHCC underwriting/legal sign-off."],
        ["TMHCC 0223C \u00b7 TMHCC final (58b8340) \u00b7 Tysers \u00b7 Yutree \u00b7 Liberty \u00b7 Allianz \u00b7 AXA XL \u00b7 Entertainment Elite"])
    doc.add_page_break()

    # 1
    B.h1(doc, "1. Files produced")
    ft = B.make_table(doc, ["#", "Document", "Formats"], [1.0, 13.0, 4.0])
    for i, (_s, name) in enumerate(FILES):
        c = ft.add_row().cells
        B.text_cell(c[0], str(i + 1), size=8.3)
        B.text_cell(c[1], name, size=8.3, bold=True, color=B.TEAL)
        B.text_cell(c[2], "docx + PDF", size=8.3)
    c = ft.add_row().cells
    B.text_cell(c[0], "10", size=8.3); B.text_cell(c[1], "Final_QA_Report.docx (this document)", size=8.3, bold=True, color=B.TEAL)
    B.text_cell(c[2], "docx + PDF", size=8.3)
    B.zebra(ft)

    def confirm(n, title, body, ok=True):
        B.h2(doc, f"{n}. {title}")
        p = B.para(doc, "", size=9.5)
        r = p.add_run("CONFIRMED \u2014 " if ok else "NOTE \u2014 ")
        r.font.bold = True; r.font.name = B.FONT; r.font.size = B.Pt(9.5)
        r.font.color.rgb = B.RGBColor.from_string("1B7A3D" if ok else B.GOLD)
        r2 = p.add_run(body); r2.font.name = B.FONT; r2.font.size = B.Pt(9.5)
        r2.font.color.rgb = B.RGBColor.from_string(B.INK)

    confirm(2, "Full 0223C\u2192final redline generated from scratch",
        f"The redline was generated afresh by diffing the actual paragraph text of OLD_0223C.docx ({stats['old_paras']} paragraphs) against the "
        f"final clean wording ({stats['new_paras']} paragraphs) using a sequence + word-level diff, emitting genuine Word tracked changes "
        f"({stats['ins_paras']+stats['uw_paras']} insertions incl. {stats['uw_paras']} UW-tagged, {stats['del_paras']} deletions, "
        f"{stats['inline_amend']} inline amendments). Verified at the XML level (2,161 w:ins, 1,105 w:del) and by rendering.")
    confirm(3, "Existing tracked changes NOT relied on as the sole redline",
        "The prior TrackedChanges document (recent enhancements on a clean 0526 baseline) was explicitly NOT used. The redline was built directly "
        "from the 0223C baseline and the final wording.")
    confirm(4, "UW enhancements remain separately identifiable and unaccepted",
        "The 14 rounds 7\u20139 enhancements are tagged in the redline under a distinct tracked-change author ('UW Review Enhancement'), "
        "yellow-highlighted and annotated '[UW REVIEW ENHANCEMENT \u2014 awaiting underwriting/legal sign-off; not accepted]'. They remain tracked "
        "(unaccepted) and are catalogued in the UW Enhancement Register.")
    confirm(5, "Abuse / Tysers issue reviewed",
        "A dedicated Abuse / Safeguarding / Molestation section was produced (Phase 03 Section A) grounded in the wordings: TMHCC PL EXCLUDES abuse; "
        "Yutree and AXA XL also exclude; Tysers, Liberty, Allianz and Entertainment Elite contain NO express abuse exclusion (silent). TMHCC is "
        "therefore narrower than those four \u2014 the issue the prior review missed. A caveat (silence \u2260 confirmed cover) is logged, and an optional "
        "sub-limited abuse write-back with safeguarding conditions precedent is proposed (Phase 05).")

    B.h1(doc, "6. Key findings \u2014 refreshed six-insurer legal review")
    for n in ["TMHCC is the broadest wording by section count and the ONLY one offering Loss of Licence, Commercial Legal Expenses, Management Liability and a standalone Cyber-liability section.",
              "Abuse: TMHCC/Yutree/AXA XL exclude; Tysers/Liberty/Allianz/Entertainment Elite silent \u2192 TMHCC narrower on abuse (headline miss now captured).",
              "Tysers PI is worldwide and covers patents; TMHCC S12 is jurisdiction-limited (default ex-US/Canada) and excludes patents.",
              "Statutory/criminal defence: Tysers GBP 1m; Yutree GBP 250k; TMHCC S12 funds only data-protection defence (broader criminal cover in S13/S14).",
              "AXA XL excludes terrorism and punitive/fines absolutely and carries broad cyber + communicable-disease exclusions \u2014 disciplined restrictions are market-normal.",
              "Personal Accident: Tysers (extensive) + Yutree (assault) provide it; TMHCC and three others do not."]:
        B.bullet(doc, n, size=9)

    B.h1(doc, "7. Key TMHCC strengths (wording-supported)")
    for n in ["Widest section count; four sections no competitor offers.",
              "Genuine standalone cyber LIABILITY cover (not a bare exclusion as in AXA XL).",
              "Broad, well-extended Media Liability (S12) with employee-dishonesty write-back, data-protection defence, reputation/withdrawal, IP-pursuit and M&A auto-acquisition.",
              "Clean exclusion architecture (cyber/date exclusion dis-applied to S12\u201315).",
              "Favourable fines/penalties carve-back (vs AXA XL absolute exclusion).",
              "Sub-limits meet or exceed every evidenced competitor figure (e.g. Virus GBP 500k > Tysers GBP 250k)."]:
        B.bullet(doc, n, size=9)

    B.h1(doc, "8. Key TMHCC weaknesses / gaps")
    for n in ["Abuse exclusion (vs four silent competitors) \u2014 see Phase 03/05.",
              "Jurisdiction default ex-US/Canada (vs Tysers worldwide PI) \u2014 optional write-back drafted.",
              "Patents excluded (vs Tysers) \u2014 deliberate, defensible; no action recommended.",
              "No Personal Accident & Business Travel section \u2014 whole-section gap (parked proposal).",
              "S12-only criminal/regulatory defence looks narrow on a section-by-section read \u2014 cross-reference + contribution drafted."]:
        B.bullet(doc, n, size=9)

    B.h1(doc, "9. High-priority gap-fill recommendations")
    for n in ["Abuse / molestation optional sub-limited write-back (HIGH; parked, proposed wording).",
              "Worldwide / USA-Canada territory option for Media Liability (HIGH; implemented as tracked change, awaiting sign-off).",
              "Personal Accident & Business Travel section (HIGH; parked, skeleton wording).",
              "Criminal/regulatory defence cross-reference + contribution (Medium-High; implemented, awaiting sign-off)."]:
        B.bullet(doc, n, size=9)

    confirm(10, "Coverage-comparison layout fixes made",
        "The matrix was rebuilt as a clean, market-ready ONE-PAGE at-a-glance matrix (18 concise coverage features \u00d7 7 insurers + key-note column) "
        "with legend, footnotes and \u2713/\u25d0/\u2717/? symbols; granular detail moved to a structured appendix. Verified by rendering: the main matrix fits on a "
        "single page with no overflow, and the appendix begins on the next page. The abuse row was added (the prior matrix's omission).")
    confirm(11, "PolicyBridge workflow playbook created",
        "Phase 06 produced the PolicyBridge Wording Studio Workflow Playbook \u2014 an 8-stage product specification with an app-interface specification "
        "and a worked example from this project.")
    confirm(12, "PolicyBridge audit/rebuild prompt created",
        "Phase 07 produced a ready-to-paste audit/rebuild prompt (discovery-first; no destructive changes; ten audit checks; product standard; the "
        "seven TMHCC documents as a test project), with the current-state finding that the app is presently a Document Centre, not a Wording Studio.")

    B.h1(doc, "13. Items needing underwriting / legal sign-off")
    for n in ["All 14 UW enhancements in the register (S12 extensions, money restructure, S13/S12 definition changes, proof of ownership, admission of liability).",
              "Abuse write-back (claims + legal + reinsurance) and Personal Accident section (capacity/appetite).",
              "Worldwide/US-Canada option (reinsurance treaty territory) before any US/Canada offering.",
              "Confirmation that IT-property/breakdown cover is not narrowed by consolidation into S1/S2.",
              "Confirmation of the status (ordinary condition vs condition precedent) of the Proof of Ownership condition."]:
        B.bullet(doc, n, size=9, color=B.RUST)

    B.h1(doc, "14. Limitations / points not verified")
    for n in ["Policy Schedules (limits, excesses, sub-limit figures, section toggles) were not supplied; section availability and sub-limits reflect the wording booklets only.",
              "Competitor schedules/endorsements were not supplied; a competitor's 'silence' on a peril (e.g. abuse) means no express clause was located, not a confirmed grant of cover \u2014 flagged for legal confirmation.",
              "The redline is a text-level legal-effect redline rendered with branding (opens in Word with Track Changes); the fully-formatted 126-page branded final wording is provided separately as TMHCC_Final_Clean.docx.",
              "LibreOffice PDF export renders tracked insertions as underline (black); Microsoft Word shows the two tracked-change authors in distinct colours. Highlight + annotation make UW items unmistakable in any viewer.",
              "The repository HEAD is a few auto-commits ahead of 58b8340; the working-tree final clean wording is treated as the 58b8340 final."]:
        B.bullet(doc, n, size=9, color=B.GREY)

    B.h1(doc, "Completion statement")
    B.callout(doc, "Complete:",
        "The final tracked-changes wording shows ALL changes from 0223C; UW enhancements remain separately identifiable and unaccepted; the "
        "six-insurer comparison has been materially re-reviewed; the abuse/Tysers issue (and other previously-missed points) has been specifically "
        "addressed; the coverage-comparison layout has been cleaned; the gap-fill strategy includes copy-paste wording and exact locations; and the "
        "PolicyBridge workflow playbook and audit/rebuild prompt have been produced. All completed outputs are saved separately by phase.",
        bg="E3F1E8", border="1B7A3D", lead_color="1B7A3D")

    out = os.path.join(PACK, "Final_QA_Report.docx")
    B.save_doc(doc, out)
    print("saved", out)


qa()
