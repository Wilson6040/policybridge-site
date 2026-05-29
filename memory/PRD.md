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
