# -*- coding: utf-8 -*-
"""PHASE 00 — Source Inventory and Workplan (branded docx)."""
import sys, json
sys.path.insert(0, "/app/work/compare")
import brand2 as B

OUT = "/app/outputs/phase-00-source-inventory/Source_Inventory_and_Workplan.docx"
stats = json.load(open("/app/work/r10/redline_stats.json"))

DOCS = [
 ("TMHCC 0223C \u2014 OLD wording (TRUE BASELINE)", "/app/work/source/OLD_0223C.docx",
  "Found", f"The true comparison baseline. {stats['old_paras']} non-empty paragraphs; 13-section structure (Information Technology = old Section 4)."),
 ("TMHCC final wording (commit 58b8340)", "/app/deliverables/TMHCC_Media_Combined_0526_FINAL_Clean.docx",
  "Found", f"Latest clean final wording (round-9 state at commit 58b8340). {stats['new_paras']} non-empty paragraphs; 15-section structure."),
 ("Competitor 1 \u2014 Tysers 'Focus' Media (capacity Zurich)", "/app/work/compare/src/Tysers.pdf + txt/Tysers.txt",
  "Found", "9 sections; full media package incl. PI/E&O and Personal Accident & Business Travel."),
 ("Competitor 2 \u2014 Yutree Media & Entertainment (capacity AXA)", "/app/work/compare/src/Yutree.pdf + txt/Yutree.txt",
  "Found", "12 sections; media package incl. PI-Media/PI-Events; broad Abuse definition + exclusion."),
 ("Competitor 3 \u2014 Liberty Entertainment Combined", "/app/work/compare/src/Liberty.pdf + txt/Liberty.txt",
  "Found", "6 sections; property/BI/liability package (no media/PI/cyber/legal/mgmt)."),
 ("Competitor 4 \u2014 Allianz Entertainment 'Complete'", "/app/work/compare/src/Allianz.pdf + txt/Allianz.txt",
  "Found", "8 sections (+ Terrorism); property/BI/liability package; splits ICOW/Book Debts."),
 ("Competitor 5 \u2014 AXA XL Media & Entertainment Combined Corporate", "/app/work/compare/src/AXAXL.pdf + txt/AXAXL.txt",
  "Found", "3 operative sections (MD/BI/Liability); terrorism & punitive excluded absolutely; broad cyber exclusion; explicit Abuse exclusion 7.8.1."),
 ("Competitor 6 \u2014 Entertainment Elite (v3.2)", "/app/work/r9/src/EntertainmentElite.pdf + txt/EntertainmentElite.txt",
  "Found", "8 sections; property/BI/Money/liability/terrorism; detailed event-Money section (source of the Money restructure)."),
 ("Current coverage comparison (client-facing)", "/app/deliverables/TMHCC_Media_Coverage_Comparison_FULL.docx",
  "Found", "Round-8/9 6-competitor matrix. To be REBUILT in Phase 04 (cleaner one-page matrix + appendix)."),
 ("Current gap-fill / enhancement strategy", "/app/deliverables/TMHCC_Media_GapFill_Enhancement_Strategy.docx",
  "Found", "Round-8/9 internal gap analysis. To be UPDATED in Phase 05 from the refreshed legal review."),
 ("Current summary of cover", "/app/deliverables/TMHCC_Media_Combined_Summary_of_Cover_FINAL.docx",
  "Found", "Round-8/9 summary of cover (final wording only)."),
 ("Current summary of changes", "/app/deliverables/TMHCC_Media_Combined_Summary_of_Changes_FINAL.docx",
  "Found", "Round-8 summary of changes. NOTE: prior change docs were NOT a holistic 0223C\u2192final redline \u2014 the reason for Phases 01\u201302."),
 ("Existing tracked-changes versions", "/app/deliverables/TMHCC_Media_Combined_0526_FINAL_TrackedChanges.docx",
  "Found \u2014 NOT used as the redline", "Prior tracked-changes showed only recent enhancements on a clean 0526 baseline; NOT relied upon. Phase 01 regenerates the full 0223C\u2192final redline from scratch."),
 ("Grounded competitor analysis data", "/app/work/compare/cmpdata.py + /app/work/r8/cmpdata9.py + r8data.py",
  "Found", "Section matrix, media-feature matrix, exclusions, conditions, sub-limits, competitor profiles, gaps \u2014 all derived from the parsed wordings (reused + refined this round)."),
 ("Branding template", "/app/work/source/TEMPLATE_SummaryOfCover.docx + /app/work/compare/tpl/Template.docx",
  "Found", "Tokio Marine HCC branding (logo, Lato, teal/gold/rust palette, legend) used for all generated documents."),
 ("PolicyBridge app project files", "/app/backend (FastAPI Document Centre) + /app/frontend (React)",
  "Found", "Used ONLY for the Phase 07 audit/rebuild prompt; not modified by this workflow."),
]


def main():
    doc = B.Document()
    B.set_normal_style(doc)
    B.setup_page(doc, landscape=False, margin_cm=1.8)
    B.add_logo_header(doc, left_text="TMHCC Media & Music Combined \u2014 Source Inventory & Workplan")
    B.add_footer_pagenum(doc, note="Phase 00 \u2014 Source Inventory & Workplan. Baseline = TMHCC 0223C; Final = commit 58b8340.")
    B.cover_page(doc,
        "Phase 00 \u00b7 Source Inventory",
        "Source Inventory & Workplan",
        "Documents reviewed, baseline/final identification, and the eight-phase workplan",
        ["Prepared as the first step of the TMHCC full-redline reset + six-insurer legal review + PolicyBridge workflow blueprint.",
         "TRUE baseline: TMHCC 0223C. Final wording: TMHCC Media & Music Combined at commit 58b8340.",
         "No cover invented; comparisons are by legal effect, grounded in the parsed wordings."],
        ["TMHCC 0223C (baseline) \u00b7 TMHCC final (58b8340)",
         "Six competitors: Tysers, Yutree, Liberty, Allianz, AXA XL, Entertainment Elite"])
    doc.add_page_break()

    B.h1(doc, "1. Documents found and reviewed")
    t = B.make_table(doc, ["Document", "Status", "Location / notes"], [6.6, 3.0, 8.4])
    for name, path, status, note in DOCS:
        c = t.add_row().cells
        B.text_cell(c[0], name, size=8.3, bold=True, color=B.TEAL)
        st_col = B.RUST if "NOT" in status else B.INK
        B.text_cell(c[1], status, size=8, color=st_col)
        B.text_cell(c[2], path + "\n" + note, size=7.8)
    B.zebra(t)

    B.h1(doc, "2. Baseline and final wording identification")
    B.callout(doc, "TRUE comparison baseline:",
        "TMHCC 0223C old wording \u2014 /app/work/source/OLD_0223C.docx. This 13-section wording (with a standalone "
        "Information Technology Section 4) is the genuine prior contract clients are migrating FROM.")
    B.callout(doc, "Final wording (commit 58b8340):",
        "TMHCC Media & Music Combined final clean wording \u2014 /app/deliverables/TMHCC_Media_Combined_0526_FINAL_Clean.docx. "
        "15-section structure. The repository HEAD is a few auto-commits ahead of 58b8340 but the working-tree final clean "
        "wording is the round-9 state and is treated as the final wording for this comparison (assumption logged below).",
        bg="FFF6E6", border=B.GOLD, lead_color=B.GOLD)

    B.h1(doc, "3. Six competitor wordings under review")
    for n in ["Tysers \u2018Focus\u2019 Media (capacity Zurich) \u2014 9 sections, full media package",
              "Yutree Media & Entertainment (capacity AXA) \u2014 12 sections, broad Abuse definition + exclusion",
              "Liberty Entertainment Combined \u2014 6 sections, property/BI/liability",
              "Allianz Entertainment \u2018Complete\u2019 \u2014 8 sections (+Terrorism), property/BI/liability",
              "AXA XL Media & Entertainment Combined Corporate \u2014 3 operative sections; explicit Abuse exclusion (7.8.1)",
              "Entertainment Elite (v3.2) \u2014 8 sections, detailed event-Money section"]:
        B.bullet(doc, n)

    B.h1(doc, "4. Existing supporting documents")
    B.bullet(doc, "Coverage comparison (client-facing) \u2014 present; to be REBUILT (Phase 04).", bold_lead="Coverage comparison: ")
    B.bullet(doc, "Gap-fill / enhancement strategy \u2014 present; to be UPDATED (Phase 05).", bold_lead="Gap-fill strategy: ")
    B.bullet(doc, "Summary of cover \u2014 present (final wording only).", bold_lead="Summary of cover: ")
    B.bullet(doc, "Summary of changes \u2014 present, but NOT a holistic 0223C\u2192final redline.", bold_lead="Summary of changes: ")

    B.h1(doc, "5. Existing tracked changes \u2014 and why they are NOT relied upon")
    B.para(doc, "An existing TrackedChanges document is present (TMHCC_Media_Combined_0526_FINAL_TrackedChanges.docx). It shows "
                "only the recent enhancement edits applied to an already-clean 0526 baseline \u2014 NOT the full set of changes from "
                "0223C. It is therefore NOT used as the redline. Phase 01 regenerates a complete 0223C\u2192final tracked-changes "
                "redline directly from the two wordings.", size=9.5)

    B.h1(doc, "6. UW enhancements \u2014 identifiable?")
    B.para(doc, "Yes. The rounds 7\u20139 enhancements still requiring underwriting/legal review are individually identifiable "
                "from the wording-build engine and have been catalogued. In the Phase 01 redline they are tagged under a separate "
                "tracked-change author ('UW Review Enhancement', yellow-highlighted) and listed in the UW Enhancement Register "
                "(14 items).", size=9.5)
    tt = B.make_table(doc, ["Auto-detected in redline", "Count of tagged paragraphs"], [12.0, 6.0])
    for title, cnt in sorted(stats.get("uw_enhancements_detected", {}).items()):
        c = tt.add_row().cells
        B.text_cell(c[0], title, size=8.3); B.text_cell(c[1], str(cnt), size=8.3)
    B.zebra(tt)

    B.h1(doc, "7. Missing files / uncertainty")
    for n in ["Policy Schedules (limits, excesses, sub-limit figures, section toggles) were NOT supplied \u2014 section availability "
              "and sub-limits reflect the wording booklets only; Schedule-driven figures are flagged 'per Schedule'.",
              "The repository HEAD (2e0aba9) is a few auto-commits ahead of 58b8340; the working-tree final clean wording is treated "
              "as the 58b8340 final (no wording difference observed in the auto-commits).",
              "Competitor schedules were not supplied; competitor 'silence' on a peril (e.g. abuse) means no express clause was located, "
              "not a confirmed grant of cover \u2014 flagged for legal confirmation."]:
        B.bullet(doc, n)

    B.h1(doc, "8. Confirmed eight-phase workplan")
    plan = [("Phase 01", "Full 0223C\u2192final tracked-changes redline (from scratch) + clean final + UW Enhancement Register"),
            ("Phase 02", "Detailed 0223C\u2192final change summary (per-section, with client-migration implications)"),
            ("Phase 03", "Six-insurer legal competitor review reset (incl. dedicated Abuse / Tysers section)"),
            ("Phase 04", "Rebuilt six-insurer coverage comparison (clean one-page matrix + appendix)"),
            ("Phase 05", "Updated gap-fill strategy (copy-paste wording + exact locations)"),
            ("Phase 06", "PolicyBridge Wording Studio workflow playbook"),
            ("Phase 07", "PolicyBridge audit/rebuild prompt"),
            ("Phase 08", "Final pack assembly + QA report (+ PDFs)")]
    pt = B.make_table(doc, ["Phase", "Output"], [3.0, 15.0])
    for ph, desc in plan:
        c = pt.add_row().cells
        B.text_cell(c[0], ph, size=8.5, bold=True, color=B.TEAL); B.text_cell(c[1], desc, size=8.5)
    B.zebra(pt)

    B.save_doc(doc, OUT)
    print("saved", OUT)


main()
