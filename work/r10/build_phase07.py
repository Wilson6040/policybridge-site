# -*- coding: utf-8 -*-
"""PHASE 07 — PolicyBridge Wording Studio Audit / Rebuild Prompt."""
import sys
sys.path.insert(0, "/app/work/compare")
import brand2 as B

OUT = "/app/outputs/phase-07-policybridge-audit-prompt/PolicyBridge_Wording_Studio_Audit_Rebuild_Prompt.docx"

AUDIT = [
 "Audit the current PolicyBridge app end-to-end (backend, frontend, data model, storage) and report what it actually does today.",
 "Identify whether it can INGEST multiple wordings (old/base, new draft, multiple competitors, branded template) as .docx and .pdf.",
 "Identify whether it PARSES clauses properly (sections, definitions, insuring clauses, extensions, exclusions, conditions, warranties, limits).",
 "Identify whether it MAPS wording clause-for-clause with stable clause IDs and a coverage-function taxonomy (compare by legal effect, not heading).",
 "Identify whether it COMPARES the base wording against competitor wordings and scores \u2713/\u25d0/\u2717/? by legal effect.",
 "Identify whether it GENERATES: full tracked-changes wording; clean final wording; summary of changes; summary of cover; coverage comparison; gap-fill strategy; enhancement register.",
 "Identify whether it supports an ACCEPT/REJECT recommendation workflow (one recommendation at a time; accepted \u2192 tracked change; rejected \u2192 parked with reason).",
 "Identify whether each recommendation includes: AI insight; competitor source; coverage impact; underwriting risk; legal sign-off note; copy-paste wording; exact insertion location.",
 "Identify whether outputs are BRANDED and market-ready (logo, fonts, palette, contents/hyperlinks, clean within margins; .docx + PDF).",
 "Identify whether it can use the SEVEN TMHCC documents as a base project and REPRODUCE today's outputs.",
]

REQUIREMENTS = [
 "DISCOVERY FIRST \u2014 inspect and report before changing anything.",
 "NO destructive changes; NO data deletion.",
 "NO schema changes without review and explicit approval.",
 "Do NOT break existing app functionality (the current Document Centre download flows must keep working).",
 "Use the seven TMHCC wordings/documents as a TEST PROJECT to prove the workflow.",
 "Produce a final QA report; capture SCREENSHOTS of the working flows; attach GENERATED SAMPLE OUTPUTS.",
 "Keep all third-party keys/config in environment variables; never hardcode.",
]

SEVEN_DOCS = [
 "1. Full tracked-changes wording (0223C \u2192 final redline)",
 "2. Clean final wording",
 "3. UW Enhancement Register",
 "4. Summary of changes (0223C \u2192 final)",
 "5. Six-insurer legal review / coverage comparison",
 "6. Gap-fill / enhancement strategy",
 "7. Summary of cover (and/or QA / sign-off register)",
]

# the ready-to-paste prompt text (verbatim block)
PROMPT = """AUDIT & REBUILD PROMPT \u2014 PolicyBridge Wording Studio (paste into Emergent / Opus 4.8)

ROLE: You are auditing and, where safe, upgrading my existing PolicyBridge app so it can precisely replicate a proven insurance-wording workflow.

CONTEXT: On the TMHCC Media & Music Combined project we took a base/old wording (TMHCC 0223C), a new final wording, six competitor wordings and a branded template, and produced: a holistic tracked-changes redline (with underwriting enhancements kept separately identifiable and unaccepted), a clean final wording, a detailed summary of changes, a six-insurer legal review, a one-page coverage comparison with appendix, a gap-fill strategy with copy-paste wording and exact insertion locations, and an enhancement/sign-off register. The full workflow is documented in the PolicyBridge Wording Studio Workflow Playbook (Phase 06).

PRODUCT STANDARD: PolicyBridge is NOT working properly unless it can reproduce the same mapping, comparison, gap analysis, tracked-changes update and document-generation workflow achieved in the TMHCC project.

DO THIS, IN ORDER:
1. DISCOVERY FIRST. Inspect the current app (backend, frontend, data model, storage) and tell me exactly what it does today, with evidence. Do NOT change anything yet. (Note: today the app appears to be a 'Document Centre' that serves pre-generated documents for download \u2014 confirm or correct this.)
2. AUDIT against the ten checks below and answer each YES/PARTIAL/NO with evidence:
   (a) ingests multiple wordings (old/base, new, competitors, template) as .docx and .pdf;
   (b) parses clauses (sections, definitions, insuring clauses, extensions, exclusions, conditions, warranties, limits);
   (c) maps wording clause-for-clause with stable clause IDs and a coverage-function taxonomy (compare by legal effect, not heading);
   (d) compares base vs competitor wordings and scores by legal effect;
   (e) generates: full tracked-changes wording, clean final wording, summary of changes, summary of cover, coverage comparison, gap-fill strategy, enhancement register;
   (f) supports accept/reject recommendation workflow (one at a time; accepted \u2192 tracked change; rejected \u2192 parked with reason);
   (g) each recommendation carries AI insight, competitor source, coverage impact, underwriting risk, legal sign-off note, copy-paste wording and exact insertion location;
   (h) outputs are branded and market-ready (.docx + PDF, clean within margins, contents/hyperlinks preserved);
   (i) keeps underwriting enhancements separately identifiable and UNACCEPTED by default;
   (j) can use the seven TMHCC documents as a base project and reproduce the outputs.
3. THEN choose ONE of:
   A. CONFIRM it already does all of this precisely \u2014 with evidence (screenshots + a generated sample for each output); OR
   B. PRODUCE a detailed rebuild/update plan (architecture, data model, parsing approach, redline engine, comparison engine, recommendation queue, export pipeline, milestones); OR
   C. IMPLEMENT the missing pieces if it is safe to do so.

HARD CONSTRAINTS:
- Discovery before any change. No destructive changes. No data deletion. No schema changes without review. Do not break existing functionality (the current download flows must keep working).
- Use the seven TMHCC wordings/documents as a TEST PROJECT to prove the workflow end-to-end.
- Keys/config in environment variables only; never hardcode URLs or secrets.

DELIVERABLES:
- A discovery report (what the app does today).
- The ten-point audit answered with evidence.
- Either an evidenced confirmation, a detailed rebuild plan, or the safe implementation.
- A final QA report, screenshots of the working flows, and generated sample outputs (the seven documents) for the TMHCC test project.

ACCEPTANCE: Done only when PolicyBridge can ingest the multiple wordings, parse and map clauses, compare by legal effect, generate the full tracked redline (UW enhancements separately identifiable + unaccepted), the clean wording, the summary of changes, the summary of cover, the coverage comparison, the gap-fill strategy and the enhancement register \u2014 all branded, traceable to source and marked for sign-off \u2014 reproducing the TMHCC outputs."""


def main():
    doc = B.Document()
    B.set_normal_style(doc)
    B.setup_page(doc, landscape=False, margin_cm=1.8)
    B.add_logo_header(doc, left_text="PolicyBridge Wording Studio \u2014 Audit / Rebuild Prompt")
    B.add_footer_pagenum(doc, note="Phase 07 \u2014 a ready-to-paste prompt to audit and (safely) upgrade PolicyBridge Wording Studio.")
    B.cover_page(doc,
        "Phase 07 \u00b7 Audit / Rebuild Prompt",
        "PolicyBridge \u2014 Audit & Rebuild Prompt",
        "A prompt to give Emergent / Opus to verify (or rebuild) the Wording Studio against this exact workflow",
        ["The ready-to-paste prompt is on the next page (Section 2).",
         "Product standard: PolicyBridge is not working properly unless it can reproduce the TMHCC mapping, comparison, gap analysis, tracked-changes and document-generation workflow.",
         "Constraints: discovery first; no destructive changes; no data deletion; no schema changes without review; do not break existing functionality."],
        ["Test project: the seven TMHCC documents from this workflow"])
    doc.add_page_break()

    B.h1(doc, "1. Current-state context (for the recipient)")
    B.para(doc, "Based on the present repository, the PolicyBridge app is currently a 'Document Centre': a FastAPI backend exposes a static list of "
                "pre-generated documents (GET /api/documents) with download endpoints (GET /api/documents/download/{filename}), and a React frontend "
                "lists and downloads them. It does NOT currently ingest wordings, parse clauses, map clause-for-clause, compare wordings, generate "
                "tracked-changes redlines, or support an accept/reject recommendation workflow. The audit/rebuild prompt below is written with that "
                "reality in mind: the app today serves OUTPUTS, it does not yet PRODUCE them.", size=9.5)

    B.h1(doc, "2. The prompt (copy-paste)")
    B.callout(doc, "", PROMPT, bg="F4F7F9", border=B.TEAL, lead_color=B.TEAL)
    doc.add_page_break()

    B.h1(doc, "3. The ten audit checks (reference)")
    at = B.make_table(doc, ["#", "Audit check"], [1.0, 17.0])
    for i, a in enumerate(AUDIT):
        c = at.add_row().cells
        B.text_cell(c[0], str(i + 1), size=8.5)
        B.text_cell(c[1], a, size=8.5)
    B.zebra(at)

    B.h1(doc, "4. Hard constraints")
    for r in REQUIREMENTS:
        B.bullet(doc, r, size=9.2)

    B.h1(doc, "5. The seven TMHCC documents (test project)")
    for d in SEVEN_DOCS:
        B.bullet(doc, d, size=9.2)
    B.para(doc, "These documents (produced in this workflow) are the proof-set: the rebuilt PolicyBridge must be able to reproduce them from the same "
                "source wordings, with the same fidelity (full tracked redline with separately-identifiable, unaccepted UW enhancements; branded, "
                "traceable, sign-off-marked outputs).", size=9.2)

    B.h1(doc, "6. Product standard (definition of done)")
    B.callout(doc, "Standard:",
        "PolicyBridge is not working properly unless it can reproduce the same mapping, comparison, gap analysis, tracked-changes update and "
        "document-generation workflow achieved in the TMHCC project \u2014 with discovery first, no destructive changes, a final QA report, screenshots "
        "of the working flows, and generated sample outputs.", bg="FFF6E6", border=B.GOLD, lead_color=B.GOLD)

    B.save_doc(doc, OUT)
    print("saved", OUT)


main()
