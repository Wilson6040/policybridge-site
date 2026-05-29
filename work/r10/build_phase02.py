# -*- coding: utf-8 -*-
"""PHASE 02 — Detailed 0223C -> Final change summary (branded docx)."""
import sys, json
sys.path.insert(0, "/app/work/compare")
import brand2 as B

OUT = "/app/outputs/phase-02-change-summary/TMHCC_0223C_to_Final_Change_Summary.docx"
stats = json.load(open("/app/work/r10/redline_stats.json"))

# tag colours
EFFECT = {"Favourable": "1B7A3D", "Neutral": B.GREY, "Restrictive": B.RUST,
          "Favourable / Neutral": "1B7A3D", "Neutral / Restrictive": B.RUST}

# Each change: (area, old_pos, final_pos, exact_change, practical_effect, effect, broker, signoff, kind, base_or_enh)
CHANGES = [
 ("Policy Contents page",
  "No formal machine-generated contents.",
  "Two-column hyperlinked 'Policy Contents' with accurate page numbers and footer pagination.",
  "Added navigable Contents; live page numbers.",
  "Easier navigation; no cover change.",
  "Neutral", "No", "No", "Formatting / structural", "Base"),
 ("Notices \u2014 Complaints / FOS / ODR / Consumer",
  "Standard complaints and data-protection notices.",
  "Expanded complaints route incl. Financial Ombudsman Service (FOS) and EU ODR platform; Consumer-specific notice.",
  "Clarified regulatory complaints and consumer rights.",
  "Better consumer compliance; no cover change.",
  "Neutral", "No", "No", "Technical", "Base"),
 ("Trading Sanctions / Restrictions",
  "Sanctions handled within general conditions.",
  "Express 'Trading Sanctions or Restrictions' notice added to the front matter (in addition to the International Sanctions clause).",
  "Reinforces sanctions position.",
  "Stronger sanctions protection for the insurer.",
  "Neutral / Restrictive", "No", "No", "Technical", "Base"),
 ("Insuring Agreement",
  "'Insuring Agreement' clause framed around 13 sections.",
  "Re-cast: cover applies 'in respect of any Section shown in the Schedule as operative'; aligned to the 15-section structure.",
  "Schedule-driven operative-section logic made explicit.",
  "Clarifies that only scheduled sections are operative.",
  "Neutral", "Yes", "No", "Structural", "Base"),
 ("General Policy Definitions",
  "Definitions listed; fewer defined terms; some inline.",
  "Each defined term promoted to its own heading; new terms added to support the three new sections (Legal Expenses, Management Liability, Cyber).",
  "Many new/expanded definitions; clearer presentation.",
  "More defined terms can both widen and tighten triggers \u2014 review on a term-by-term basis.",
  "Neutral", "Yes", "Yes", "Material / structural", "Base"),
 ("General Application of Policy Conditions / General Conditions",
  "General conditions stated 'Applicable to Sections 1\u201312'.",
  "Re-scoped to 'Applicable to Sections 1\u201311'; Sections 13\u201315 carry their own specialist conditions which prevail on conflict. New 'Premium Instalments via a Finance Provider' condition added.",
  "Conditions framework re-aligned to the new section map; finance-provider condition added.",
  "Clients must read the new specialist conditions for S13\u201315; general conditions no longer reach the new liability sections.",
  "Neutral", "Yes", "Yes", "Structural", "Base"),
 ("Protection & Maintenance Conditions \u2014 Security devices",
  "Security-devices maintenance condition with no carve-out for bells-only alarms; '1\u201312'.",
  "Re-scoped '1\u201311'; 'bells only' intruder alarms expressly excluded from the maintenance condition.",
  "Minor easing of the security-maintenance condition.",
  "Slightly more favourable for insureds with bells-only alarms.",
  "Favourable", "Yes", "Yes", "Material", "Base"),
 ("Claims Conditions \u2014 Notification (S1\u201311)",
  "Claim-notification obligations within claims conditions.",
  "S1\u201311 notification is an ordinary obligation ('will notify\u2026 as soon as practicable'); section-level notification for S12\u2013S15 operates as a condition precedent; police/security/storage/risk-improvement conditions retained.",
  "Notification architecture clarified; not a blanket condition precedent for 1\u201311.",
  "Clients must note that the new liability sections (S12\u2013S15) have stricter, section-specific notification.",
  "Neutral", "Yes", "Yes", "Material", "Base"),
 ("Claims Conditions \u2014 Admission of Liability",
  "Blanket condition precedent ('the Insured must not admit liability\u2026').",
  "Replaced with an ordinary condition qualified by prejudice (insurer may rely on breach only to the extent prejudiced).",
  "Relaxation of a condition precedent.",
  "More favourable to insureds; explain as fairer claims handling.",
  "Favourable", "Yes", "Yes", "Material", "UW Review Enhancement"),
 ("Claims Conditions \u2014 Proof of Ownership and Value",
  "No express proof-of-ownership condition.",
  "New condition: the Insured must, on request, produce reasonable proof of ownership and value.",
  "New claims-handling condition for property/theft claims.",
  "Clients should retain receipts/valuations; confirm whether ordinary condition or CP.",
  "Neutral / Restrictive", "Yes", "Yes", "Material", "UW Review Enhancement"),
 ("General Exclusions",
  "General exclusions 'Applicable to Sections 1\u201312'; references to the Information Technology Section.",
  "Substantively unchanged but re-scoped 'Applicable to Sections 1\u201311'; stray Information-Technology-Section references corrected.",
  "Scope re-aligned; no substantive widening/narrowing of the exclusions themselves.",
  "Exclusion content is essentially carried across; re-scoping is the material point.",
  "Neutral", "No", "Yes", "Structural", "Base"),
 ("Section 4 \u2014 Information Technology (STANDALONE)",
  "Standalone 'Section 4: Information Technology Section' (IT property + computer breakdown).",
  "REMOVED as a standalone section; IT property cover consolidated into Section 1 (premises) and Section 2 (Property & Equipment).",
  "Whole-section relocation; the IT heading disappears.",
  "Clients must be told IT-property/breakdown cover is RETAINED inside S1/S2 (confirm no narrowing).",
  "Neutral / Restrictive", "Yes", "Yes", "Material / structural", "Base"),
 ("Section 2 rename",
  "'Section 2: Production Property \u201cAll Risks\u201d'.",
  "Renamed 'Section 2: Property & Equipment \u201cAll Risks\u201d'; absorbs production/entertainment equipment + IT equipment.",
  "Rename + scope consolidation.",
  "Same cover, broader/clearer label; confirm equipment + IT both captured.",
  "Neutral", "Yes", "No", "Structural", "Base"),
 ("Section 3 \u2014 Business Interruption",
  "BI with 'Accounts Receivable'.",
  "'Accounts Receivable' re-labelled '(Book Debts)'; ICOW/AICOW named.",
  "Presentational relabel for like-for-like comparison.",
  "No cover change; clearer BI heads.",
  "Neutral", "No", "Yes", "Technical", "UW Review Enhancement"),
 ("Section 8 (was S9) \u2014 Money",
  "Single Money section.",
  "Restructured into two Schedule-referenced extensions \u2014 'Money \u2013 Premises' and 'Money \u2013 Touring, Festivals and Events' (the latter amalgamating event-money: safes/containers, assault on personal effects, employee dishonesty discovered within 12 months). Existing covers preserved.",
  "Money cover split into two clearer Schedule sub-limits + touring/event money added.",
  "Touring/festival clients gain clearer event-money; sub-limits set by Schedule.",
  "Favourable", "Yes", "Yes", "Material", "UW Review Enhancement"),
 ("Section 12 (was S13) \u2014 Media Liability",
  "Media Liability with core PI/E&O grants.",
  "Core cover retained; SEVEN new S12 enhancements added (Representation Costs; Journalistic Source-Protection; Criminal/Regulatory Defence cross-reference; Distributors & Purchasers 5x; Worldwide/USA-Canada optional; King's Counsel determination; Pollution negligent-advice write-back) + broadened 'Computer System' definition.",
  "Materially broadened Media Liability \u2014 all held for sign-off.",
  "Brokers can position broader S12 cover, but only once UW/legal sign-off is obtained.",
  "Favourable", "Yes", "Yes", "Material", "UW Review Enhancement"),
 ("NEW Section 13 \u2014 Commercial Legal Expenses",
  "No legal-expenses section.",
  "New ARAG-style Commercial Legal Expenses section (employment, contract, tax, statutory defence etc.); broadened 'Employee' definition.",
  "Entirely new cover (Schedule-operative).",
  "New benefit to highlight; operative only if shown in the Schedule.",
  "Favourable", "Yes", "Yes", "Material", "Base (+ UW enh: Employee def)"),
 ("NEW Section 14 \u2014 Management Liability",
  "No management-liability section.",
  "New Management Liability section (D&O, Company, Employment Practices / Wrongful Employment Practice, etc.).",
  "Entirely new cover (Schedule-operative).",
  "New benefit to highlight; operative only if shown in the Schedule.",
  "Favourable", "Yes", "Yes", "Material", "Base"),
 ("NEW Section 15 \u2014 CyberGuard\u2122 (Cyber Liability)",
  "No standalone cyber section.",
  "New standalone CyberGuard\u2122 (Cyber Liability) section (multimedia, security & privacy, privacy-regulatory defence & penalties, PCI DSS). Label standardised across body + Contents.",
  "Entirely new standalone cyber-liability cover (Schedule-operative).",
  "Major new benefit; genuine cyber liability, not a bare exclusion.",
  "Favourable", "Yes", "Yes", "Material", "Base (label = UW enh)"),
]

# Section renumbering map: (0223C, Final, note)
RENUMBER = [
 ("S1 Business \u201cAll Risks\u201d", "S1 Business \u201cAll Risks\u201d", "Retained; now also houses IT-property cover."),
 ("S2 Production Property \u201cAll Risks\u201d", "S2 Property & Equipment \u201cAll Risks\u201d", "Renamed; absorbs equipment + IT equipment."),
 ("S3 Business Interruption", "S3 Business Interruption", "Retained; 'Accounts Receivable' \u2192 '(Book Debts)'."),
 ("S4 Information Technology", "\u2014 (removed)", "STANDALONE SECTION REMOVED; cover consolidated into S1/S2."),
 ("S5 Terrorism", "S4 Terrorism", "Renumbered \u22121."),
 ("S6 Employers\u2019 Liability", "S5 Employers\u2019 Liability", "Renumbered \u22121."),
 ("S7 Public Liability", "S6 Public Liability", "Renumbered \u22121; abuse exclusion retained (see Phase 03)."),
 ("S8 Products Liability", "S7 Products Liability", "Renumbered \u22121."),
 ("S9 Money", "S8 Money", "Renumbered \u22121; restructured into two Schedule sub-limits."),
 ("S10 Goods in Transit", "S9 Goods in Transit", "Renumbered \u22121."),
 ("S11 Loss of Licence", "S10 Loss of Licence", "Renumbered \u22121."),
 ("S12 Production Indemnity", "S11 Production Indemnity", "Renumbered \u22121."),
 ("S13 Media Liability", "S12 Media Liability", "Renumbered \u22121; seven new extensions (UW sign-off)."),
 ("\u2014", "S13 Commercial Legal Expenses", "NEW SECTION."),
 ("\u2014", "S14 Management Liability", "NEW SECTION."),
 ("\u2014", "S15 CyberGuard\u2122 (Cyber Liability)", "NEW SECTION."),
]


def main():
    doc = B.Document()
    B.set_normal_style(doc)
    B.setup_page(doc, landscape=True, margin_cm=1.4)
    B.add_logo_header(doc, left_text="TMHCC Media & Music Combined \u2014 Change Summary 0223C \u2192 Final")
    B.add_footer_pagenum(doc, note="Phase 02 \u2014 detailed change summary (TMHCC 0223C \u2192 final wording, commit 58b8340). "
                                   "Companion to the Full Redline. Items marked 'UW Review Enhancement' await sign-off.")
    B.cover_page(doc,
        "Phase 02 \u00b7 Change Summary",
        "Detailed Change Summary",
        "Every material change from TMHCC 0223C to the final wording (commit 58b8340)",
        [f"Generated from the full redline: {stats['old_paras']} baseline paragraphs vs {stats['new_paras']} final paragraphs; "
         f"{stats['ins_paras']+stats['uw_paras']} insertions, {stats['del_paras']} deletions, {stats['inline_amend']} inline amendments tracked.",
         "Favourable / Neutral / Restrictive flags and sign-off requirements are shown per change.",
         "No cover invented; exclusions and conditions not softened."],
        ["TMHCC 0223C baseline", "TMHCC final wording (commit 58b8340)"])
    doc.add_page_break()

    B.h1(doc, "A. Section renumbering & relocation map (0223C \u2192 final)")
    B.para(doc, "The single most important migration point: the standalone Information Technology Section (old S4) was removed and "
                "its cover consolidated into S1/S2, so every later section is renumbered, and three new sections (S13\u2013S15) were added "
                "\u2014 13 sections became 15.", size=9.5)
    rt = B.make_table(doc, ["0223C section", "Final section", "Note"], [7.5, 7.5, 11.0])
    for a, b, n in RENUMBER:
        c = rt.add_row().cells
        col = B.RUST if "removed" in b or "NEW" in n else B.INK
        B.text_cell(c[0], a, size=8.3); B.text_cell(c[1], b, size=8.3, bold=("NEW" in n or "removed" in b), color=col)
        B.text_cell(c[2], n, size=8)
    B.zebra(rt)
    doc.add_page_break()

    B.h1(doc, "B. Detailed change table")
    B.para(doc, "Legend \u2014 Effect: green = favourable, grey = neutral, red = restrictive. 'Type' = material / technical / structural / "
                "formatting. 'Source' = Base redline change vs UW Review Enhancement (awaiting sign-off).", size=8.5)
    t = B.make_table(doc, ["Area", "0223C position", "Final position", "Exact change & practical effect",
                           "Effect", "Broker?", "Sign-off?", "Type", "Source"],
                     [3.4, 4.3, 4.8, 6.2, 2.0, 1.3, 1.3, 2.6, 2.6])
    for (area, oldp, finp, change, effect_txt, effect, broker, signoff, kind, src) in CHANGES:
        c = t.add_row().cells
        B.text_cell(c[0], area, size=7.6, bold=True, color=B.TEAL)
        B.text_cell(c[1], oldp, size=7.3)
        B.text_cell(c[2], finp, size=7.3)
        B.text_cell(c[3], change + " \u2014 " + effect_txt, size=7.3)
        B.text_cell(c[4], effect, size=7.3, bold=True, color=EFFECT.get(effect, B.INK))
        B.text_cell(c[5], broker, size=7.3, align="center")
        B.text_cell(c[6], signoff, size=7.3, align="center",
                    color=(B.RUST if signoff == "Yes" else B.INK), bold=(signoff == "Yes"))
        B.text_cell(c[7], kind, size=7.2)
        B.text_cell(c[8], src, size=7.2, color=(B.GOLD if "UW" in src else B.INK),
                    bold=("UW" in src))
    B.zebra(t)
    doc.add_page_break()

    B.setup_page(doc, landscape=False, margin_cm=1.8)  # portrait for narrative
    B.h1(doc, "C. Client Migration Implications (0223C \u2192 final)")
    B.para(doc, "Key points for clients and brokers moving an account from the TMHCC 0223C wording to the final wording:", size=10)
    for lead, body in [
      ("Section numbers have changed \u2014 re-map any references. ",
       "The standalone Information Technology Section (old S4) is removed and every section from old S5 onward is renumbered down by one. "
       "Any Schedule entries, endorsements, certificates or broker documents that reference OLD section numbers must be re-mapped to the new numbering (see the map above)."),
      ("IT cover is retained, not lost. ",
       "Information-technology PROPERTY and computer-breakdown cover is consolidated into Section 1 (premises) and Section 2 (Property & Equipment). "
       "Clients should be reassured the cover continues \u2014 underwriting to confirm no narrowing on consolidation."),
      ("Three new sections are available. ",
       "Commercial Legal Expenses (S13), Management Liability (S14) and a standalone CyberGuard\u2122 cyber-liability section (S15) are new. They are "
       "operative ONLY if shown as operative in the Schedule \u2014 confirm at renewal whether the client is buying them."),
      ("Claims handling has changed. ",
       "Admission of Liability is now an ordinary condition (with a prejudice qualifier) rather than a blanket condition precedent; a new Proof of "
       "Ownership and Value condition applies; and the new liability sections (S12\u2013S15) carry their own, stricter, section-specific notification "
       "(condition precedent). Brokers should brief clients on the differing notification rules per section."),
      ("General conditions and exclusions now target Sections 1\u201311. ",
       "The general conditions and general exclusions are re-scoped to Sections 1\u201311; Sections 13\u201315 are governed by their own specialist terms, "
       "which prevail on any conflict. Read the new sections' own conditions carefully."),
      ("Money cover is restructured. ",
       "Money is now presented as two Schedule-referenced extensions \u2014 'Money \u2013 Premises' and 'Money \u2013 Touring, Festivals and Events' \u2014 with the "
       "touring/event extension adding event-money heads (safes/containers, assault on personal effects, employee dishonesty). Existing covers are preserved; sub-limits are Schedule-set."),
      ("Some enhancements are pending sign-off. ",
       "The broadest Media Liability (S12) enhancements (Distributors & Purchasers, worldwide/US-Canada option, source-protection, representation costs, "
       "criminal/regulatory defence cross-reference, King's Counsel clause, pollution negligent-advice write-back) and the broadened S13 'Employee' and S12 "
       "'Computer System' definitions are tracked but NOT yet accepted \u2014 they require TMHCC underwriting/legal sign-off before being relied upon (see the UW Enhancement Register)."),
    ]:
        p = B.para(doc, "", size=9.5)
        r = p.add_run(lead); r.font.bold = True; r.font.name = B.FONT; r.font.size = B.Pt(9.5)
        r.font.color.rgb = B.RGBColor.from_string(B.TEAL)
        r2 = p.add_run(body); r2.font.name = B.FONT; r2.font.size = B.Pt(9.5)
        r2.font.color.rgb = B.RGBColor.from_string(B.INK)

    B.h1(doc, "D. How this summary was produced")
    for n in ["Generated from a fresh, holistic 0223C\u2192final tracked-changes redline (Phase 01), not from the prior 'recent enhancements' tracked changes.",
              "Each change is classified favourable / neutral / restrictive and flagged for broker explanation and underwriting/legal sign-off.",
              "UW Review Enhancements are distinguished from Base redline changes throughout.",
              "No cover has been invented and no exclusion or restriction has been softened in this description."]:
        B.bullet(doc, n)

    B.save_doc(doc, OUT)
    print("saved", OUT, "changes:", len(CHANGES))


main()
