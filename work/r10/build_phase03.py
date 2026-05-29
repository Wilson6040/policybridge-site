# -*- coding: utf-8 -*-
"""PHASE 03 — Six-insurer legal competitor review RESET (with dedicated Abuse / Tysers section)."""
import sys
sys.path.insert(0, "/app/work/r8")
sys.path.insert(0, "/app/work/compare")
import brand2 as B
import cmpdata9 as D
import cmpdata as C

OUT = "/app/outputs/phase-03-competitor-legal-review/TMHCC_Six_Insurer_Legal_Review_Reset.docx"
INSURERS = ["TMHCC", "Tysers", "Yutree", "Liberty", "Allianz", "AXA XL", "Ent.Elite"]
WCOL = [4.2, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 12.2]

# ---- ABUSE finding (grounded in the parsed wordings) ----
ABUSE_POS = [
 ("TMHCC", "EXCLUDED", "Express Public Liability 'Abuse' exclusion: 'the mental or physical intentional or neglectful "
  "mistreatment of a person which results in Bodily Injury including any act which amounts to an offence under the "
  "Sexual Offences Act 2003.'", "Abuse-related bodily-injury claims are NOT covered under Public Liability."),
 ("Tysers (Zurich)", "NOT LOCATED (silent)", "No express abuse / molestation exclusion located in the liability sections. "
  "'Bullying and harassment' appears ONLY as a topic in the Employee-Assistance counselling helpline (Sub-Section 9, "
  "Zurich Assistance) \u2014 NOT a liability exclusion.", "Abuse-related BI is NOT specifically carved out \u2192 potentially within "
  "Public/Products Liability cover, subject to deliberate-acts and other general exclusions. POTENTIALLY BROADER than TMHCC. "
  "(This is the issue the prior review missed.) Confirm against the full schedule/endorsements."),
 ("Yutree (AXA)", "EXCLUDED (broad)", "Broad defined term 'Abuse' (abuse/threat/cruelty; exploitation; molestation, intimate "
  "or inappropriate sexual contact; pornography) PLUS an express 'Abuse exclusion': 'We will not cover claims directly or "
  "indirectly caused by or arising from any actual or alleged abuse.'", "Abuse NOT covered; arguably a WIDER exclusion than "
  "TMHCC ('directly or indirectly\u2026 actual or alleged')."),
 ("Liberty", "NOT LOCATED (silent)", "No express abuse exclusion located (property/BI/liability package).",
  "Silent \u2192 abuse-related BI not specifically excluded; potentially broader than TMHCC, subject to general exclusions. Confirm."),
 ("Allianz", "NOT LOCATED (silent)", "No express abuse exclusion located ('animal cruelty' appears only in a data-privacy context).",
  "Silent \u2192 potentially broader than TMHCC, subject to general exclusions. Confirm."),
 ("AXA XL", "EXCLUDED (very broad)", "Liability Exclusion 7.8.1 'Abuse': 'any act that results in the maltreatment of a person\u2026 "
  "physical, sexual, verbal, psychological or emotional or financial nature.'", "Abuse NOT covered; very broad exclusion (wider than TMHCC)."),
 ("Entertainment Elite", "NOT LOCATED (silent)", "No abuse-LIABILITY exclusion located ('misuse, abuse or contamination' refers to "
  "physical property contamination only).", "Silent on personal-abuse liability \u2192 potentially broader than TMHCC, subject to general exclusions. Confirm."),
]

# Missed / under-emphasised issues from the fresh read
MISSED = [
 ("Abuse / molestation exclusion asymmetry", "HEADLINE MISS",
  "TMHCC PL EXCLUDES abuse; Tysers, Liberty, Allianz and Entertainment Elite contain NO express abuse exclusion (silent); only "
  "Yutree and AXA XL also exclude. Tysers \u2014 the closest media comparator \u2014 does not carve out abuse, so it appears broader on this peril. "
  "Not captured in the prior comparison."),
 ("Silence \u2260 cover (legal-effect caveat)", "METHOD",
  "A competitor being silent on abuse does NOT confirm cover \u2014 deliberate/criminal-acts and other general exclusions may still bite. "
  "Flagged for legal confirmation rather than asserted as a competitor win."),
 ("Tysers worldwide PI + patents", "CONFIRMED",
  "Tysers PI/E&O is worldwide and includes patent infringement; TMHCC S12 is jurisdiction-limited (default ex-US/Canada) and excludes patents."),
 ("Statutory / criminal defence costs", "CONFIRMED",
  "Tysers funds Bribery/Corporate-Manslaughter/H&S/CDM defence (GBP 1m); Yutree funds criminal-prosecution defence (GBP 250k). "
  "TMHCC S12 funds only data-protection defence (broader criminal cover sits in S13/S14)."),
 ("AXA XL absolute exclusions", "CONFIRMED",
  "AXA XL excludes terrorism AND punitive/exemplary damages and fines ABSOLUTELY, and carries a broad communicable-disease and cyber exclusion \u2014 "
  "evidencing that disciplined restrictions are market-normal and supporting TMHCC's defensible restrictions."),
 ("Personal Accident gap", "CONFIRMED",
  "Tysers (extensive) and Yutree (assault) provide Personal Accident; TMHCC, Liberty, Allianz, AXA XL and Entertainment Elite do not."),
]


def matrix(doc, title, rows, intro=None, exclusion_semantics=False):
    B.h2(doc, title)
    if intro:
        B.para(doc, intro, size=8.7)
    headers = ["Coverage / legal feature"] + INSURERS + ["Legal significance / note"]
    t = B.make_table(doc, headers, WCOL)
    for row in rows:
        if len(row) == 4:
            label, statuses, _verdict, comment = row
        else:
            label, statuses, comment = row
        c = t.add_row().cells
        B.text_cell(c[0], label, size=7.6, bold=True, color=B.TEAL)
        for j, st in enumerate(statuses):
            B.status_cell(c[1 + j], st, small=True)
        B.text_cell(c[8], comment, size=7.4)
    B.zebra(t)
    B.spacer(doc, 4)


def main():
    doc = B.Document()
    B.set_normal_style(doc)
    B.setup_page(doc, landscape=True, margin_cm=1.4)
    B.add_logo_header(doc, left_text="TMHCC Media & Music Combined \u2014 Six-Insurer Legal Review (Reset)")
    B.add_footer_pagenum(doc, note="Phase 03 \u2014 granular legal review by legal effect (not headings). Six competitors. "
                                   "Compared against the final TMHCC wording. Subject to TMHCC legal/underwriting sign-off.")
    B.cover_page(doc,
        "Phase 03 \u00b7 Legal Review (Reset)",
        "Six-Insurer Legal Competitor Review",
        "A fresh, granular legal review \u2014 benchmarked by the abuse/Tysers issue the prior review missed",
        ["Reviewed by LEGAL EFFECT and coverage function, not by heading. Where a clause could not be verified it is marked "
         "'? requires review' rather than assumed.",
         "Dedicated Abuse / Safeguarding / Molestation section (TMHCC vs Tysers and all competitors).",
         "No cover invented; no exclusion or restriction softened."],
        [w["full"] for w in D.WORDINGS])
    doc.add_page_break()

    B.legend_bar(doc)
    B.callout(doc, "Quality benchmark:",
        "The prior comparison missed that TMHCC's Public Liability EXCLUDES abuse while Tysers (the closest media competitor) "
        "appears NOT to exclude abuse. This review treats that level of granularity as the standard for every coverage/legal area below.")

    # -------- SECTION A: ABUSE (headline) --------
    B.h1(doc, "A. Abuse / Safeguarding / Molestation \u2014 TMHCC vs Tysers and other competitors")
    B.para(doc, "Finding: TMHCC's Public Liability expressly EXCLUDES abuse. Of the six competitors, only Yutree and AXA XL also "
                "expressly exclude abuse. Tysers, Liberty, Allianz and Entertainment Elite contain NO express abuse exclusion that "
                "could be located \u2014 i.e. they are silent, and abuse-related bodily-injury claims are not specifically carved out. "
                "On this peril TMHCC is therefore NARROWER than Tysers/Liberty/Allianz/Entertainment Elite and broadly comparable to "
                "Yutree/AXA XL.", size=9)
    at = B.make_table(doc, ["Insurer", "Abuse position", "Wording basis", "Legal effect"], [3.6, 3.0, 11.0, 9.3])
    for ins, pos, basis, effect in ABUSE_POS:
        c = at.add_row().cells
        col = B.RUST if "NOT LOCATED" in pos else "1B7A3D"
        B.text_cell(c[0], ins, size=8, bold=True, color=B.TEAL)
        B.text_cell(c[1], pos, size=7.8, bold=True, color=("8A6A1E" if "silent" in pos else col))
        B.text_cell(c[2], basis, size=7.6)
        B.text_cell(c[3], effect, size=7.6)
    B.zebra(at)
    B.spacer(doc, 4)
    B.h3(doc, "Is TMHCC narrower? \u2014 yes, against four of the six")
    B.para(doc, "TMHCC is narrower than Tysers, Liberty, Allianz and Entertainment Elite (no express abuse exclusion) and comparable to "
                "Yutree and AXA XL (both exclude). IMPORTANT legal caveat: a competitor's silence does NOT confirm cover \u2014 abuse claims "
                "may still be defeated by deliberate/criminal-acts and other general exclusions. This must be confirmed legally rather than "
                "asserted.", size=9)
    B.h3(doc, "Recommended action \u2014 optional, sub-limited abuse write-back (Schedule-operative)")
    B.callout(doc, "Recommendation:",
        "Retain the abuse exclusion as the DEFAULT (abuse is a high-severity, long-tail, reputational and systemic exposure, and the "
        "express exclusion is a defensible underwriting position). For client segments where abuse exposure is genuinely relevant "
        "(festivals/youth/community events), OFFER an OPTIONAL, sub-limited Abuse / Molestation write-back, Schedule-operative, with strict "
        "safeguarding conditions precedent (documented safeguarding policy; DBS/PVG checks; supervision/'two-adult' rule), an aggregate "
        "sub-limit, a claims-made trigger and an SIR. This converts a visible gap (vs Tysers) into a rated option without taking the "
        "exposure by default. Proposed wording is in the Phase 05 gap-fill strategy.",
        bg="FFF6E6", border=B.GOLD, lead_color=B.GOLD)
    rt = B.make_table(doc, ["Underwriting risk", "Claims risk", "Priority", "Sign-off required"], [6.0, 6.0, 4.0, 10.9])
    c = rt.add_row().cells
    B.text_cell(c[0], "HIGH \u2014 severe, long-tail, reputational; reinsurance-sensitive.", size=8, color=B.RUST, bold=True)
    B.text_cell(c[1], "HIGH severity / low frequency \u2014 large awards; coverage litigation.", size=8)
    B.text_cell(c[2], "High (for client segments with real exposure)", size=8, bold=True)
    B.text_cell(c[3], "YES \u2014 claims + legal + reinsurance; specialist abuse market may be the right home for the core exposure.", size=8, color=B.RUST)
    doc.add_page_break()

    # -------- SECTION B: Liability exclusions deep-dive --------
    B.h1(doc, "B. Liability exclusions (Public / Products / Employers') \u2014 by legal effect")
    B.para(doc, "Exclusion tables below use \u2713 = exclusion present / applies, \u2717 = no such exclusion located, ? = unclear, \u25d0 = partial/with write-back. "
                "An abuse-exclusion row has been added (the prior review's omission).", size=8.5)
    abuse_excl_row = ("Abuse / molestation exclusion (PL) applies",
                      ["yes", "no", "yes", "no", "no", "yes", "no"],
                      "TMHCC, Yutree and AXA XL EXCLUDE abuse; Tysers, Liberty, Allianz and Entertainment Elite have NO express abuse exclusion "
                      "located (silent). See Section A.")
    gen_rows = [abuse_excl_row] + list(D.GENERAL_EXCL)
    matrix(doc, "B.1 General & liability exclusions", gen_rows, exclusion_semantics=True)
    B.h3(doc, "B.2 Additional liability-exclusion notes (Public / Products / Employers')")
    for n in ["Employers' Liability: statutory EL provided by all six (typically GBP 10m). EL exclusions are broadly equivalent; AXA XL = sub-section 7C. "
              "TMHCC's abuse, asbestos and communicable-disease exclusions are framed ex-EL where required by statute.",
              "Bodily injury / property damage carve-out (PI): all three media wordings exclude BI/PD from PI unless arising from negligent publication/advice \u2014 equivalent.",
              "Contractual / assumed liability: excluded by all liability/PI sections with the standard 'would have attached anyway' write-back \u2014 equivalent.",
              "Deliberate / reckless / dishonest acts: excluded by all, with an employee-dishonesty write-back in the media wordings \u2014 equivalent.",
              "Care, custody or control; defective workmanship; medical malpractice; advice/professional negligence: TMHCC PL carries the standard market carve-outs (AXA XL mirrors several at 7.8.x)."]:
        B.bullet(doc, n, size=8.5)
    doc.add_page_break()

    # -------- SECTION C: Media Liability / PI / E&O --------
    B.h1(doc, "C. Media Liability / Professional Indemnity / E&O \u2014 deep legal review (Section 12)")
    matrix(doc, "C.1 Media / PI feature matrix", D.MEDIA_FEATURES,
           intro="Liberty, Allianz, AXA XL and Entertainment Elite provide NO media/PI/E&O cover.")
    matrix(doc, "C.2 PI-specific exclusions", D.PI_EXCL,
           intro="\u2713 = exclusion applies; na = no PI section. Covers patents, USA/Canada, insolvency, prior-known, cyber-within-PI, pollution.")
    doc.add_page_break()

    # -------- SECTION D: section availability --------
    B.h1(doc, "D. Section / cover availability across the six wordings")
    matrix(doc, "D.1 Section-level availability", D.SECTION_ROWS)
    doc.add_page_break()

    # -------- SECTION E: conditions / CPs / warranties --------
    B.h1(doc, "E. Conditions, conditions precedent, warranties & claims obligations")
    ch = B.make_table(doc, ["Condition / obligation"] + INSURERS, [4.4] + [3.18]*7)
    # CONDITIONS rows are (label, tmhcc, tysers, yutree, liberty, allianz, axaxl, ee) text
    for row in D.CONDITIONS:
        c = ch.add_row().cells
        B.text_cell(c[0], row[0], size=7.4, bold=True, color=B.TEAL)
        for j in range(7):
            B.text_cell(c[1 + j], row[1 + j], size=6.9)
    B.zebra(ch)
    B.spacer(doc, 4)
    for n in ["Claim notification: TMHCC S1\u201311 is an ordinary obligation ('as soon as practicable'); S12\u2013S15 notification operates as a CONDITION PRECEDENT. "
              "Among the most clearly-drafted notification architectures in the peer group.",
              "Conditions precedent / warranties: TMHCC uses condition-precedent drafting for security, storage, risk-improvement and section-level notification; competitors rely on ordinary conditions with proportionate remedies (Insurance Act 2015).",
              "Theft / security / proof of ownership: TMHCC adds a Proof of Ownership and Value claims condition (S1\u201311); Tysers and Entertainment Elite carry detailed Money security/carrying/key conditions \u2014 broadly comparable.",
              "Breakdown: Yutree offers a dedicated Computer Breakdown section; TMHCC consolidates IT/computer breakdown within S1/S2 \u2014 confirm it is explicit (presentational, not a true gap)."]:
        B.bullet(doc, n, size=8.5)
    doc.add_page_break()

    # -------- SECTION F: limits / sub-limits --------
    B.h1(doc, "F. Key limits & sub-limits (Media / PI)")
    sl = B.make_table(doc, ["Sub-limit"] + INSURERS, [4.4] + [3.18]*7)
    for row in D.SUBLIMITS:
        c = sl.add_row().cells
        B.text_cell(c[0], row[0], size=7.6, bold=True, color=B.TEAL)
        for j in range(7):
            B.text_cell(c[1 + j], row[1 + j], size=7.2, align="center")
    B.zebra(sl)
    B.para(doc, "Honest position: TMHCC meets or exceeds every evidenced competitor numeric sub-limit (e.g. Virus GBP 500k > Tysers GBP 250k; "
                "Reputation/Withdrawal GBP 250k = Yutree). Gaps are about NEW heads (representation, distributors, source-protection), not lower numbers.", size=8.5)
    doc.add_page_break()

    # -------- SECTION G: optional extensions / write-backs --------
    B.h1(doc, "G. Optional extensions & exclusion write-backs")
    wt = B.make_table(doc, ["Area", "Competitor", "Competitor write-back / position", "TMHCC position", "Recommended action", "Priority"],
                      [3.4, 2.6, 5.6, 5.2, 6.0, 3.5])
    for area, comp, cwb, tpos, act, pri in C.EXCL_WRITEBACKS:
        c = wt.add_row().cells
        B.text_cell(c[0], area, size=7.6, bold=True, color=B.TEAL)
        B.text_cell(c[1], comp, size=7.4)
        B.text_cell(c[2], cwb, size=7.4)
        B.text_cell(c[3], tpos, size=7.4)
        B.text_cell(c[4], act, size=7.4)
        B.text_cell(c[5], pri, size=7.4, bold=True,
                    color=(B.RUST if pri == "High" else B.INK))
    B.zebra(wt)
    doc.add_page_break()

    # -------- SECTION H: competitor profiles --------
    B.h1(doc, "H. Competitor-by-competitor legal profile")
    for key in D.COMPETITOR_KEYS:
        prof = D.COMPETITOR_PROFILES[key]
        B.h2(doc, prof["title"])
        B.para(doc, prof["shape"], size=8.5, italic=True)
        B.h3(doc, "Strengths vs TMHCC")
        for s in prof["strengths"]:
            B.bullet(doc, s, size=8.3)
        B.h3(doc, "Gaps / restrictions")
        for g in prof["gaps"]:
            B.bullet(doc, g, size=8.3)
        B.spacer(doc, 4)
    doc.add_page_break()

    # -------- SECTION I: missed issues + verdict --------
    B.h1(doc, "I. Issues the prior review missed or under-emphasised")
    mt = B.make_table(doc, ["Issue", "Status", "Detail"], [5.0, 2.6, 19.3])
    for issue, status, detail in MISSED:
        c = mt.add_row().cells
        B.text_cell(c[0], issue, size=8, bold=True, color=B.TEAL)
        B.text_cell(c[1], status, size=7.8, bold=True,
                    color=(B.RUST if status in ("HEADLINE MISS",) else B.GOLD if status == "METHOD" else "1B7A3D"))
        B.text_cell(c[2], detail, size=7.8)
    B.zebra(mt)
    B.spacer(doc, 6)
    B.h2(doc, "Overall verdict")
    B.para(doc, "TMHCC remains the broadest wording in the peer group by section count and is the only wording offering Loss of Licence, "
                "Commercial Legal Expenses, Management Liability and a genuine standalone Cyber-liability section. Its genuine NARROWER points "
                "are: (1) the abuse exclusion (vs Tysers/Liberty/Allianz/EE which are silent); (2) jurisdiction (default ex-US/Canada vs Tysers' "
                "worldwide PI); (3) patents (excluded vs Tysers); (4) no Personal Accident section; and (5) S12-only criminal/regulatory defence is "
                "narrower on a section-by-section read. Each is addressed in the Phase 05 gap-fill strategy. TMHCC should NOT be described as "
                "market-leading on any row the wording does not support \u2014 e.g. abuse.", size=9.5)

    B.save_doc(doc, OUT)
    print("saved", OUT)


main()
