# -*- coding: utf-8 -*-
"""PHASE 06 — PolicyBridge Wording Studio Workflow Playbook (product spec)."""
import sys
sys.path.insert(0, "/app/work/compare")
import brand2 as B

OUT = "/app/outputs/phase-06-policybridge-workflow-playbook/PolicyBridge_Wording_Studio_Workflow_Playbook.docx"

STAGES = [
 ("1. Source intake",
  ["Upload the OLD / base wording, the current / new draft wording, all competitor wordings, and the branded template.",
   "Capture document metadata: insurer, product, version/reference, date, and document role (base / new / competitor / template).",
   "Set the AUTHORITY ORDER of documents (which wording is the master, which is the baseline, which are comparators) so later steps know what 'wins'.",
   "Accept .docx and .pdf; extract full text (and, for .docx, paragraph styles) so cover can be compared by legal effect, not by heading."],
  "Outputs of stage: a Project with all sources ingested, typed and ordered."),
 ("2. Clause parsing & mapping",
  ["Break each wording into clauses: sections, definitions, insuring clauses, extensions, exclusions, conditions, warranties, limits/sub-limits.",
   "Assign STABLE clause IDs and a normalised clause label so clauses can be referenced across versions and across insurers.",
   "Map each clause to a canonical coverage-function taxonomy (e.g. 'PL: abuse exclusion', 'Media: defamation', 'Money: touring') so equivalent cover is matched even when headings differ.",
   "Flag clauses that cannot be confidently classified for human review."],
  "Outputs: a clause map per document + a cross-document concordance keyed by coverage function."),
 ("3. Base-to-new redline",
  ["Diff the OLD wording against the NEW wording at clause/paragraph level (and word level within changed clauses).",
   "Generate genuine Word tracked changes (w:ins / w:del) so the redline opens in Word with revisions shown.",
   "Separate BASE redline changes from UW REVIEW ENHANCEMENTS using distinct tracked-change authors + highlight + annotation.",
   "Preserve accepted / unaccepted status; never silently merge enhancements.",
   "Build an Enhancement Register from the tagged enhancements (title, section, location, wording, rationale, support, risk, sign-off, status)."],
  "Outputs: full tracked-changes wording, clean wording, enhancement register."),
 ("4. Competitor comparison",
  ["Map competitor clauses onto the base structure via the coverage-function taxonomy.",
   "For each coverage feature, determine: equivalent / broader / narrower; identify exclusions and write-backs; identify competitor advantages.",
   "Score TMHCC vs each competitor (\u2713 covered / \u25d0 partial / \u2717 not identified / ? requires review) by LEGAL EFFECT, never by heading.",
   "Surface asymmetries explicitly (e.g. one insurer excludes a peril while another is silent \u2014 the abuse/Tysers case)."],
  "Outputs: a coverage matrix + granular legal-comparison tables."),
 ("5. Gap analysis",
  ["Identify what competitors cover that the base wording does not (and where the base is broader).",
   "Classify each gap by impact (product gap vs presentational/labelling vs legal-drafting gap) and priority (High/Medium/Low).",
   "Propose copy-paste-ready gap-fill wording with the EXACT insertion location, mode (automatic/optional/schedule), UW & claims risk, and sign-off.",
   "Present recommendations ONE AT A TIME for acceptance/rejection; never auto-accept."],
  "Outputs: a gap-fill strategy + a recommendation queue."),
 ("6. Iterative wording update",
  ["User accepts or rejects each recommendation individually.",
   "Accepted recommendations become tracked changes (tagged with author + rationale + source support).",
   "Rejected recommendations are PARKED with their wording and reason retained (nothing is lost).",
   "Every change retains an audit trail: AI insight, competitor source, coverage impact, UW risk, legal note, exact location."],
  "Outputs: an updated tracked wording reflecting only accepted items; a parked-items log."),
 ("7. Output generation",
  ["Generate, on demand and branded: final tracked wording; final clean wording; summary of changes; summary of cover; full coverage comparison; "
   "gap-fill strategy; enhancement / sign-off register; and legal/UW review notes.",
   "Export to .docx and PDF; preserve branding (logo, fonts, palette) and hyperlinks/contents where present.",
   "Stamp each output with the project, source versions and a 'subject to legal/UW sign-off' footer."],
  "Outputs: the full market-ready document pack."),
 ("8. Quality controls",
  ["No invented cover; trace every recommendation to source wording (clause ID + page).",
   "Distinguish PRODUCT gaps from LEGAL/DRAFTING gaps and from presentational gaps.",
   "Mark every underwriting/legal sign-off requirement; keep UW enhancements separately identifiable and unaccepted by default.",
   "Keep branding consistent; ensure exports are clean and within page margins (no overflow).",
   "Where a clause cannot be verified, mark '? requires review' rather than assume."],
  "Outputs: a QA report asserting these controls were applied."),
]

INTERFACE = [
 ("Project dashboard", "List of wording projects; per-project status (sources ingested, redline ready, comparison ready, recommendations open/accepted/rejected, outputs generated, sign-offs outstanding)."),
 ("Document intake panel", "Drag-drop upload; document typing (base/new/competitor/template); authority-order control; extraction progress and parse-quality flags."),
 ("Clause map viewer", "Tree of each wording's clauses with stable IDs and coverage-function tags; search/filter; jump-to-source."),
 ("Side-by-side wording comparison", "Old vs new (and base vs competitor) panes with synchronised scrolling and inline tracked-change markup."),
 ("Competitor matrix", "Interactive \u2713/\u25d0/\u2717/? matrix by coverage function; click a cell to see the underlying clauses and legal note."),
 ("Gap recommendation queue", "One recommendation at a time: AI insight, competitor source, coverage impact, UW risk, legal sign-off note, copy-paste wording, exact insertion location, Accept / Reject / Park."),
 ("Accept / reject workflow", "Accepted \u2192 becomes a tracked change; Rejected/Parked \u2192 retained with reason; full audit trail; nothing auto-accepted."),
 ("Tracked-changes generator", "Produces the full Word redline with separate authors for base vs UW enhancements; highlight + annotation; clean version on demand."),
 ("Summary document generator", "Generates summary of changes, summary of cover, coverage comparison, gap-fill strategy, enhancement register \u2014 all branded."),
 ("Sign-off dashboard", "Outstanding underwriting/legal sign-offs per enhancement; status (awaiting / approved / rejected); owner; date."),
 ("Export centre", "Branded .docx + PDF exports of every document; bulk 'final pack' export; version history."),
]


def main():
    doc = B.Document()
    B.set_normal_style(doc)
    B.setup_page(doc, landscape=False, margin_cm=1.8)
    B.add_logo_header(doc, left_text="PolicyBridge Wording Studio \u2014 Workflow Playbook")
    B.add_footer_pagenum(doc, note="Phase 06 \u2014 reusable workflow playbook / product specification for PolicyBridge Wording Studio. "
                                   "Captured from the TMHCC Media & Music Combined project.")
    B.cover_page(doc,
        "Phase 06 \u00b7 Workflow Playbook",
        "PolicyBridge Wording Studio",
        "A reusable, productised workflow for wording comparison, redlining, gap analysis and document generation",
        ["Captures the exact process developed on the TMHCC Media & Music Combined project so it can be reused for any future wording.",
         "Inputs: a base wording, an old wording, a new draft wording, multiple competitor wordings and a branded template.",
         "Outputs: full tracked wording, clean wording, summary of changes, summary of cover, coverage comparison, gap-fill strategy, enhancement register and legal/UW review notes."],
        ["Worked example: TMHCC 0223C \u2192 final (commit 58b8340) vs six competitor wordings"])
    doc.add_page_break()

    B.h1(doc, "1. Purpose")
    B.para(doc, "This playbook documents \u2014 as a product specification \u2014 the end-to-end workflow used to take a base/old wording, a new draft "
                "wording, multiple competitor wordings and a branded template, and produce a market-ready document pack: a holistic tracked-changes "
                "wording, a clean final wording, a summary of changes, a summary of cover, a coverage comparison, a gap-fill strategy, an enhancement "
                "register and legal/underwriting review notes. It is designed to be built into PolicyBridge Wording Studio so the process is repeatable "
                "for future contracts and wordings.", size=9.5)

    B.h1(doc, "2. Workflow at a glance")
    gt = B.make_table(doc, ["Stage", "What happens", "Stage output"], [3.4, 10.6, 4.0])
    for name, steps, out in STAGES:
        c = gt.add_row().cells
        B.text_cell(c[0], name, size=8.3, bold=True, color=B.TEAL)
        B.text_cell(c[1], steps[0] + (" \u2026" if len(steps) > 1 else ""), size=7.8)
        B.text_cell(c[2], out, size=7.6)
    B.zebra(gt)
    doc.add_page_break()

    B.h1(doc, "3. The workflow in detail")
    for name, steps, out in STAGES:
        B.h2(doc, name)
        for s in steps:
            B.bullet(doc, s, size=9)
        B.callout(doc, "Stage output:", out, bg="F4F7F9", border=B.TEAL, lead_color=B.TEAL)
        B.spacer(doc, 4)
    doc.add_page_break()

    B.h1(doc, "4. How this works in the app interface")
    it = B.make_table(doc, ["Interface area", "Function"], [4.6, 13.4])
    for area, fn in INTERFACE:
        c = it.add_row().cells
        B.text_cell(c[0], area, size=8.4, bold=True, color=B.TEAL)
        B.text_cell(c[1], fn, size=8.3)
    B.zebra(it)
    doc.add_page_break()

    B.h1(doc, "5. Data model essentials")
    for n in ["Project \u2192 Documents (typed: base / old / new / competitor / template) \u2192 Clauses (stable IDs) \u2192 coverage-function tags.",
              "Authority order on Documents drives which wording is master/baseline and which are comparators.",
              "Recommendations link to source Clause IDs (and page) on BOTH the base and the competitor side \u2014 enforcing 'trace every recommendation to source'.",
              "Tracked changes store author (base vs UW enhancement), rationale, competitor source, coverage impact, UW/claims risk, sign-off status and accepted/parked state.",
              "Outputs are generated artefacts versioned against the source document versions used."]:
        B.bullet(doc, n, size=9)

    B.h1(doc, "6. Worked example (this project)")
    for n in ["Sources: TMHCC 0223C (baseline), TMHCC final (commit 58b8340, new), six competitors (Tysers, Yutree, Liberty, Allianz, AXA XL, Entertainment Elite), Tokio Marine HCC template.",
              "Stage 3 produced a holistic 0223C\u2192final redline (2,161 tracked insertions, 1,105 deletions) with 14 UW enhancements separately identifiable.",
              "Stage 4 produced a one-page coverage matrix + granular legal tables; Stage 5 produced 15 gap-fill recommendations with copy-paste wording.",
              "Stage 4 surfaced the abuse/Tysers asymmetry (TMHCC excludes abuse; Tysers silent) \u2014 the kind of by-legal-effect finding the studio must reliably catch.",
              "All outputs branded and exported to .docx + PDF; every enhancement held for UW/legal sign-off."]:
        B.bullet(doc, n, size=9)

    B.h1(doc, "7. Product acceptance criteria")
    B.callout(doc, "Definition of done:",
        "PolicyBridge Wording Studio is working correctly only when it can reproduce the SAME mapping, comparison, gap analysis, tracked-changes "
        "update and document-generation workflow achieved on this TMHCC project \u2014 ingesting multiple wordings, parsing clauses, comparing by legal "
        "effect, generating the full tracked redline (with separately-identifiable UW enhancements), the clean wording, the summary of changes, the "
        "summary of cover, the coverage comparison, the gap-fill strategy and the enhancement register \u2014 all branded, traceable to source and marked "
        "for sign-off.", bg="FFF6E6", border=B.GOLD, lead_color=B.GOLD)

    B.save_doc(doc, OUT)
    print("saved", OUT)


main()
