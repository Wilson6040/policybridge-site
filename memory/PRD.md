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

---
## Update (round 5) — fifth competitor (AXA XL) incorporated
- Added the 5th wording: **AXA XL** — XL Catlin Insurance Company UK Ltd, "Crisis Management &
  Special Risks: Media & Entertainment Combined Corporate" (June 2021), parsed in full (pdftotext).
- AXA XL is a LEAN property/BI/liability package: only Material Damage (incl. Technical Equipment +
  a Money specification), Business Interruption, and Liability (7A Public / 7B Product / 7C EL).
  NO media/PI, production indemnity, cyber section, legal expenses, management liability, loss of
  licence, goods in transit or personal accident. Terrorism EXCLUDED absolutely (3.4, ex-EL);
  punitive/fines EXCLUDED absolutely (3.2); broad cyber exclusion (3.7, only a DP-Act-2018 carve-out
  in Public Liability); broad communicable-disease exclusion (3.8). Reinforces TMHCC's breadth.
- cmpdata.py rewritten: the 6th "pending" column replaced with real AXA XL values across the section
  matrix, media-feature matrix, general/PI exclusions; AXA XL added to conditions, sub-limits,
  competitor profiles and clause-mapping; narrative across all three builders updated to "all five
  competitors mapped".
- Fixed a table-layout bug: make_table/_set_col_widths now pin tables to a fixed twip total width
  (was pct 100%, which let the widest 7-col table spill past the landscape right margin).
- Regenerated all three deliverables (docx+PDF) — Full Comparison 17pp, Gap-Fill 16pp, QA 6pp —
  in /app/deliverables and /app/backend/deliverables (same filenames; Document Centre auto-serves).
- Status: COMPLETE — all five competitors analysed; layout verified by render.


---
## Update (round 6) — Master Policy wording polish — Feb 2026
- **New requirement** (user message): Take the user-edited
  `TMHCC_Media_Combined_0526_FINAL_amended.docx` master wording and (a) remove
  red text, (b) verify heading colours, (c) reformat the Contents page (fix
  column misalignment, bold only the literal "Section N:" labels, swap the
  dot-leader approach for something cleaner), (d) remove blank pages, while
  (e) preserving all hyperlinks AND producing a PDF copy whose links remain
  clickable.
- **Chosen Contents layout (Option B)**: borderless two-column-feel with thin
  TMHCC-blue row dividers, bold "Section N:" in TMHCC navy, page numbers
  right-aligned in TMHCC blue. Implemented via right-aligned tab stops (table
  approach was abandoned because LibreOffice + 2-column body section
  squeezed it to half-width).
- **Implementation** (single script `/app/work/master/rebuild.py`):
  1. Strip red — converts every live `<w:color val="E20033">` (TMHCC magenta)
     and `<w:color val="FF0000">` to `000000`, skipping `<w:rPrChange>` so
     tracked-change history is preserved (162 runs converted).
  2. Replace the 33 raw TOC paragraphs (with broken dot-leaders + a manually
     pasted `…………` on Section 15) with 26 polished paragraphs using
     `<w:hyperlink w:anchor="tocpg_N">` element form, a right tab at 9900 twips,
     bold-TMHCC-navy "Section N:" prefix, page number in bold TMHCC-blue,
     and a thin blue `pBdr` bottom border.
  3. Bracket the Contents page in a `cols=1, type=nextPage` section so the
     full A4 width is usable (the document body is otherwise `cols=2`).
  4. Remove 22 empty filler paragraphs between TOC and "Introduction" plus
     the redundant `<w:br w:type="page"/>` paragraph (saved ≥1 blank page).
  5. Two-pass build: pass 1 produces a draft PDF; we then auto-detect each
     heading's real PDF page (heading-sized span >= 13pt, blob-joined across
     spans to survive multi-run headings); pass 2 rebuilds the docx with the
     corrected printed page numbers (Section 1 was claiming 25 → actually 23,
     Section 15 claiming 105 → actually 103, etc.).
  6. **Hyperlink retention in PDF** — LibreOffice's PDF export does NOT
     emit clickable Goto link annotations for Word internal-bookmark hyperlinks
     (known limitation; the original `_amended.pdf` also lacks them). We
     post-process with PyMuPDF (`insert_link`) to add a clickable Goto
     annotation on each TOC row covering the full row, pointing at the
     re-detected heading page. Final PDF has 26 TOC Goto links + 5 external
     URI/mailto links + 875 outline bookmarks.
- **Deliverables** (in `/app/backend/deliverables` and `/app/work/master`):
  - `TMHCC_Media_Combined_0526_FINAL_polished.docx`  (1.78 MB, 4045 paragraphs, opens cleanly in Word/LibreOffice)
  - `TMHCC_Media_Combined_0526_FINAL_polished.pdf`   (1.66 MB, 126 pages)
- **Document Centre** — backend `DOCUMENTS` entry id `wording` updated to
  serve the polished file (title now "Final New Wording (0526) — Polished").
  The original `_amended` file remains in deliverables for archival.
- **Status:** COMPLETE — Contents page renders cleanly, page numbers are
  correct, all 26 TOC links navigate to the right pages in the PDF, no red
  body text remains, tracked-change history is intact.

---
## Update (round 7) — Final TMHCC wording update + comparison/gap/summary refresh
- **Input:** user-uploaded CURRENT FINAL wording `TMHCC_Media_Combined_0526_FINAL_polished.docx`
  (saved /app/work/r7/source_uploaded.docx). Supporting docs + 5 competitor wordings reused from
  prior rounds (/app/work/compare/txt + out). Gap numbering verified from build_gap.py priority sort:
  **Gap 2 = Worldwide/US-Canada Media Liability (S12); Gap 8 = ICOW/Book Debts (S3); Gap 10 = Computer/IT breakdown (S1/S2)**.
- **Document handling:** uploaded doc had only 1 residual w:rPrChange (no ins/del). Accepted → clean
  baseline; applied NEW edits as fresh tracked changes (author "TMHCC Wording Review"): 9 ins / 2 del.
  Produced TrackedChanges.docx + Clean.docx. Engine: /app/work/r7/build_wording.py (lxml ins/del/accept-all).
- **Wording edits (tracked):**
  * T1 — Admission of Liability [para 507]: blanket condition-precedent REPLACED with ordinary condition + prejudice qualifier.
  * T1 audit — Sections 1–11 claims-notification is NOT a CP ("will notify… as soon as practicable"); police/security/storage/risk-improvement + section-level (S12/13/14/15) CPs retained.
  * T2 — new "Proof of Ownership and Value" claims condition added to Policy Claims Conditions (S1–11), between Notification to the Police and Terms of Settlement.
  * T4 (Gap 8) — already met; "Accounts Receivable" re-labelled "(Book Debts)" in S3 Definitions + Basis of Settlement (ICOW/AICOW already named).
  * T11 — Section 15 standardised to "CyberGuard™ (Cyber Liability)" (body heading + contents; SoC too).
- **No-edit / sign-off:** Gap 2 (S12) — worldwide-ex-US/Canada by default today; clean Schedule-selectable
  worldwide + USA/Canada option drafted into the S12 SIGN-OFF list only (Task 7), NOT in wording. Gap 10 —
  S1 IT-Property Breakdown ≡ Yutree Computer Breakdown; S2 M&E Breakdown optional ext ≡ Yutree general M&E;
  no change (flagged: brief assumed IT-breakdown "in S2" but it's in S1+S3; narrowing S2 = removing cover).
- **Supporting docs updated (brand2.py / docx_brand.py builders + new r7data.py):**
  * Gap-Fill (build_gap.py + r7data.py): Round-7 status section, copy-paste wording for every rec (Task 9),
    market-leading opportunities rewritten (standalone + reputation; NO Personal Accident; Personal Assault distinction), Section 12 sign-off list (Task 7).
  * Full Comparison (build_full.py + r7data.py): deepened evidenced-strengths section — 6 areas with our clause/page + competitor benchmark + UNCONFIRMED labels (Task 8).
  * Summary of Cover (build_soc.py): claims obligations corrected (admission = ordinary condition; S1–11 notification not a CP), Proof of Ownership added, Book Debts, CyberGuard™ (Cyber Liability), worldwide-ex-US/Canada note; no Personal Accident.
  * QA/Change Report: new build_qa_r7.py — files, doc-handling, change log, CP audit, Gap 2/8/10, sign-off list, checklist, Reviewer Notes.
- **Deliverables (/app/deliverables, docx + LibreOffice PDF):** TrackedChanges, Clean, Coverage_Comparison_FULL,
  GapFill_Enhancement_Strategy, Summary_of_Cover_FINAL, QA_Report. Tracked changes verified to render
  (strikethrough/underline) in PDF (page 17 Admission; 18 Proof of Ownership; 2 contents S15; 37–38 Book Debts).
- **Status:** COMPLETE. All Section 12 items + PA + Section-2 breakdown narrowing held for legal/UW sign-off.

---
## Update (round 8) — EMERGENT DISPATCH v3: best-in-market enhancement + granular gap analysis + client/broker comparison
- **Input:** user re-uploaded the Round-7 Clean wording (byte-identical, MD5 ab33a6…) as the CURRENT FINAL clean
  baseline (/app/work/r8/source_uploaded.docx). Brief v3 supersedes the earlier v1 dispatch. Sources reused:
  OLD_0223C.docx, 5 competitor wordings (/app/work/compare/txt + src PDFs), cmpdata.py. New analysis data: r8data.py.
- **Document handling:** baseline had 0 residual revisions → accept-all = clean baseline; fresh discrete tracked
  changes applied. Engine /app/work/r8/build_wording.py (lxml ins/del, anchored by unique text). 10 DISCRETE,
  individually accept/reject-able amendments → 30 w:ins / 2 w:del; Clean = 0/0; paras 4176→4190.
- **PART A (verify-then-act):** A1 Artists' Equipment (S2, GBP 20k) ALREADY PRESENT — not duplicated. A2 Stock/
  merchandise ALREADY CATERED (Stock is an Item; def includes 'merchandise'). A3 data recovery PRESERVED in S1+S2
  (old S4 had NO standalone sub-limit) — nothing reinstated. A4 ADDED touring/entertainment Money extension (S8,
  schedule-referenced — competitor money is schedule-driven, market figure CANNOT-DETERMINE). A5 broadened the
  narrow S13 'Employee' def to ≥ Tysers(p9)/Yutree(p88) (general S1-11/S12/S14 already ≥). A6 aligned S12
  'Computer System' def to the broad S15 definition [SIGN-OFF].
- **PART B gaps (bridged as discrete tracked changes, all S12 → SIGN-OFF):** Distributors & Purchasers (5x, Tysers
  8.7); Worldwide/USA-Canada optional (Tysers); Journalistic source-protection (Tysers 8.13); Representation costs
  GBP25k (Tysers 8.15); Criminal/Regulatory defence cross-ref+contribution; King's Counsel determination (Yutree);
  Seepage&Pollution negligent-advice write-back (Yutree). PARKED with wording: Patents (deliberate exclusion),
  Asbestos negligent-advice write-back. EXCLUDED by instruction: Personal Accident & Travel (Personal Assault under
  Money kept, distinct). ICOW/Book Debts + Computer Breakdown already met.
- **PART C sub-limits:** HONEST outcome — TMHCC already meets/exceeds every evidenced competitor numeric sub-limit
  (Virus £500k>Tysers £250k; Reputation/Withdrawal £250k=Yutree) or is schedule-driven. 0 existing limits raised
  (none lowered, none invented). New covers set to evidenced figures (Representation £25k; Distributors 5x). Full
  transparent table in the Gap Analysis.
- **Deliverables (/app/deliverables + /app/backend/deliverables, docx+PDF):** TrackedChanges, Clean,
  Summary_of_Changes_FINAL (0223C→final, +Round-8 change log), Summary_of_Cover_FINAL (final wording; touring money;
  no PA/Travel), GapFill_Enhancement_Strategy = SEPARATE internal Gap Analysis (Part A/B/C + S12 sign-off +
  reviewer notes), Coverage_Comparison_FULL = CLIENT/BROKER-FACING (NO gap/sign-off/sub-limit content; verified by
  image analysis), Comparison_QA_Methodology = QA/change report. Builders: build_full_r8.py / build_gap_r8.py /
  build_qa_r8.py (brand2.py) + build_soc_r8.py / build_changes_r8.py (docx_brand.py).
- **Document Centre:** backend DOCUMENTS titles/descriptions refreshed for Round 8 (client comparison vs internal
  gap analysis; round-8 wording amendments). 9 docs serve, both formats, verified 200 + correct content-types.
- **Status:** COMPLETE. ALL Section 12 amendments applied as tracked changes but HELD for legal/underwriting
  sign-off (A6, B1–B7). A4 touring-money figure + un-evidenced sub-limits flagged CANNOT-DETERMINE.
