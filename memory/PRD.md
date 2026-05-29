# TMHCC Media Combined — Document Production (0223C vs 0526)

## Original problem statement
Produce market-ready branded Word documents for a UK commercial package (media/music)
insurance wording. Three source files supplied: OLD wording (0223C), NEW wording (0526)
and a Summary of Cover draft (used as the DESIGN source only).

Tasks: (1) amend the NEW wording — two-column hyperlinked table of contents + footer page
numbers (branding otherwise untouched); (2) Final Summary of Changes (OLD vs NEW); (3) Final
Summary of Cover (NEW only); (4) QA report. Exclusions reviewed in detail; no cover invented,
no restrictions softened.

## User choices (clarified)
- New wording: keep branding, only fix TOC (2-col + hyperlinks) + add page numbers.
- Summary of Changes & Summary of Cover: use 3rd attachment (Summary of Cover draft) branding/fonts.
- Deliverables: branded .docx + PDF for download.
- Audience: UK brokers + end clients (plain English + technical detail).

## Tech / method
- python-docx + lxml for docx manipulation; LibreOffice (headless) for PDF; poppler for QA renders.
- Branding extracted from template theme: blue #009CE5, gold #C79000, red #E20033, Arial; logo
  (image1.png), wave graphic (image2.emf). Summaries built from a copy of the template to inherit
  theme/styles/header/footer/cover; body rebuilt with brand-consistent tables + traffic lights.
- Scripts in /app/work: docx_brand.py (helpers), amend_new_wording.py, build_soc.py,
  build_changes.py, build_qa.py.

## Deliverables (in /app/deliverables and /app/work/output)
- TMHCC_Media_Combined_0526_FINAL_amended.docx (+PDF) — 2-col hyperlinked TOC (26 entries → valid
  bookmarks), footer page numbers throughout, branding intact (128 pages).
- TMHCC_Media_Combined_Summary_of_Changes_FINAL.docx (+PDF) — traffic-light comparison (7 pages).
- TMHCC_Media_Combined_Summary_of_Cover_FINAL.docx (+PDF) — NEW wording only, required disclaimer (12 pages).
- TMHCC_Media_Combined_QA_Report.docx (+PDF) — QA checklist + reviewer notes (4 pages).

## Key findings (grounded in wording)
- NEW expands 13 → 15 Sections. New: 13 Legal Expenses (ARAG), 14 Management Liability, 15 CyberGuard.
- OLD standalone Section 4 Information Technology removed; IT + Breakdown cover consolidated into
  Sections 1 (premises) & 2 (Property & Equipment, renamed from Production Property). Sections renumbered.
- General exclusions substantively unchanged (now apply to Sections 1–11 vs 1–12).
- RESTRICTION: claim notification now an express Condition Precedent to liability (Sections 1–11).
- Minor easing: "bells only" intruder alarms excluded from Security Devices maintenance condition.

## Reviewer notes / open items (for underwriting/legal)
- "Section 16" referenced (Insuring Agreement / Exclusions) but absent from body.
- Some general exclusions still reference removed "Information Technology Section".
- CyberGuard (S15) appended in different style, not in heading/TOC hierarchy.
- OCR/typo artefacts in Conduct of Claims / Duty to Defend clauses.
- Confirm IT "Data Storage" condition precedent carried across.
- TOC printed page references unchanged (navigation via hyperlinks); live footer numbers reflect new pagination.

## Status: COMPLETE — all 4 documents produced (docx + PDF), branding + content verified via render/analysis.

---
## Update (round 2) — live TOC field + wording corrections
- **Live Word TOC field**: replaced the manual contents with a genuine Word TOC field built from
  26 hidden TC entries (`updateFields=true`, clickable hyperlinks, dot-leader page numbers). Renders
  full-width single column on its own page (cover + body remain two-column). PDFs are generated via a
  Python-UNO pipeline (uno_pdf.py) that refreshes indexes/fields so the TOC + page numbers populate.
  NOTE: a true 2-column *live* field could not be rendered reliably by LibreOffice (it ignores `\f`
  identifiers and index column settings), so a clean single-column live field was chosen.
- **Section 16 removed**: stray references (Insuring Agreement, General Conditions, Policy Exclusions)
  corrected to Sections 13/14/15.
- **Information Technology Section citations removed** from conditions/exclusions; IT cover stays inside
  Section 1 (Business "All Risks"). Legitimate "Information Technology Property" cover text preserved.
- **CyberGuard (Section 15) restyled** (Subtitle + Heading 1/2/3, two-column) to match the wording and
  now appears in the live contents (≈ p.105).
- Summary of Changes, Summary of Cover and QA Report regenerated to reflect the corrections.
- Scripts: amend_v2.py (wording), uno_pdf.py (UNO PDF/TOC build), docx_brand.py + build_*.py (summaries).
- Remaining OPEN items for sign-off: minor OCR artefacts (proofread); IT "Data Storage" CP placement;
  "Production Property" vs "Property & Equipment" naming in some internal lists.

---
## Update (round 3) — two-column TOC + in-app Document Centre
- **TOC changed to TWO COLUMNS** (user preference over a live field): two-column, hyperlinked contents
  with right-aligned dot leaders and ACCURATE page numbers computed from the actual rendered document
  via the UNO page cursor (build_2col.py + uno_pagenums.py). Footer page numbers throughout. Cover and
  body remain two-column; CyberGuard restyled; Section 16 / IT references corrected (all retained).
- **In-app Document Centre** (so the user can download from the Preview):
  - Backend: GET /api/documents (lists 4 docs + formats/sizes), GET /api/documents/download/{filename}
    (FileResponse, attachment disposition). Files served from /app/backend/deliverables/.
  - Frontend: branded Tokio Marine "Document Centre" page (App.js) listing the 4 documents with
    Word/PDF download buttons. Verified end-to-end (browser download triggers; backend curl 200).
- Download/export guidance given: "Save to GitHub" to export the whole project, or download via the app.
  Emergent has no built-in email delivery (would need SendGrid/SES).
- Deliverables (docx+pdf) in /app/deliverables and /app/backend/deliverables.

---
## Update (round 4) — Competitor coverage comparison + TMHCC gap-fill strategy
- **New brief:** benchmark the TMHCC Media & Music Combined (0526) MASTER wording against four
  competitor wordings and produce two separate branded documents + a QA report (fifth competitor
  pending — carried as a reserved "Wording E" placeholder column throughout).
- **Wordings parsed (full text via pdftotext / python-docx):**
  TMHCC (15 sections, master) · Tysers "Focus" Media (capacity Zurich, 9 sections) ·
  Yutree Media & Entertainment (capacity AXA, 12 sections) · Liberty Entertainment Combined (6
  sections) · Allianz Entertainment "Complete" (8 sections).
- **Key findings (grounded):** TMHCC is the broadest — only wording with all 15 sections and the
  ONLY one with Loss of Licence (S10), Legal Expenses (S13), Management Liability (S14) and a genuine
  standalone Cyber section (S15 CyberGuard). Liberty & Allianz are property/BI/liability packages with
  NO media/PI/cyber/legal/mgmt cover. Competitor advantages sit in shared sections: Tysers PI is
  worldwide + covers patents + statutory defence (GBP 1m) + distributors-&-purchasers + source
  protection; Tysers & Yutree offer Personal Accident (TMHCC has none); Yutree has reputation-mgmt/
  withdrawal/criminal-defence + a KC clause; Allianz splits ICOW/Book Debts. TMHCC clearer on
  data-protection defence and on dis-applying its cyber/date exclusion to the liability sections.
- **Design source = supplied "Coverage Comparison" template (.doc):** Tokio Marine HCC logo
  (image1.png), Lato font, palette teal #00648B / gold #B88A3C / rust #C0563F, legend
  (✓ / ◐ / ✗ / ?), 7-col matrix (Section | TMHCC | Wording A–E). Replicated in python-docx.
- **Deliverables (docx + PDF) in /app/deliverables and /app/backend/deliverables:**
  - TMHCC_Media_Coverage_Comparison_FULL (24pp, landscape): cover, exec summary, methodology,
    at-a-glance matrix (15 sections + PA), Media-Liability/PI feature matrix, competitor-by-competitor,
    TMHCC strengths, areas competitors broader, exclusions (general + PI), conditions/claims, limits/
    sub-limits, legal/UW review notes, clause-mapping appendix.
  - TMHCC_Media_GapFill_Enhancement_Strategy (16pp, portrait): exec summary, strategic objective,
    priority summary, 12 recommendation cards, exclusion write-backs, definitions, conditions, limits,
    market-leading opportunities, UW risk assessment, implementation roadmap, sign-off notes.
  - TMHCC_Media_Comparison_QA_Methodology (6pp): docs reviewed, method, strengths/gaps, recommended
    enhancements, exclusion issues, assumptions, sign-off points, final 10-point report.
- **In-app Document Centre extended:** backend DOCUMENTS gains 3 entries (ids comparison_full /
  comparison_gapfill / comparison_qa) with a "group" field; frontend groups cards into
  "Media & Entertainment — market comparison" and "Media & Music Combined wording (0526)".
  Backend verified by testing agent (32/32 pass). Frontend grouping verified by screenshot.
- **Build tooling:** /app/work/compare/ — brand2.py (branding/PDF helpers), cmpdata.py (analysed data),
  build_full.py / build_gap.py / build_qa.py; source extracts in /app/work/compare/txt.
- **Status:** COMPLETE for 4 competitors. Re-run once the 5th competitor (Wording E) is supplied.
- All recommendations are evidence-based and market-ready SUBJECT TO TMHCC legal/underwriting sign-off.
