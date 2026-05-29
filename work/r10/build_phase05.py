# -*- coding: utf-8 -*-
"""PHASE 05 — Gap-fill strategy update (copy-paste wording + exact locations)."""
import sys
sys.path.insert(0, "/app/work/compare")
import brand2 as B

OUT = "/app/outputs/phase-05-gap-fill-strategy/TMHCC_Gap_Fill_Strategy.docx"

# Each gap: dict with all required fields. wording = copy-paste-ready.
GAPS = [
 dict(title="Abuse / Molestation \u2014 optional sub-limited write-back",
   comp="Tysers, Liberty, Allianz, Entertainment Elite (no express abuse exclusion \u2014 silent)",
   tmhcc="Public Liability EXPRESSLY EXCLUDES abuse (intentional/neglectful mistreatment; Sexual Offences Act 2003).",
   why="Tysers \u2014 the closest media competitor \u2014 and three other competitors do not carve out abuse, so TMHCC looks narrower on this peril. "
       "Abuse is, however, high-severity, long-tail and reputational; an outright exclusion is a defensible default.",
   action="KEEP the exclusion as default; OFFER an optional, sub-limited, Schedule-operative abuse/molestation write-back with safeguarding "
          "conditions precedent for client segments with genuine exposure (festivals/youth/community events).",
   loc="Section 6 (Public Liability) \u2014 Exclusions: add as an 'Optional Extension' disapplying the Abuse exclusion when operative.",
   wording="Optional Abuse and Molestation Extension (operative only if stated in the Schedule): The Abuse exclusion under this Section shall not "
           "apply, and the Insurer will indemnify the Insured for Bodily Injury arising from the actual or alleged abuse or molestation of any person, "
           "up to the sub-limit and in the aggregate stated in the Schedule, PROVIDED THAT: (a) cover applies on a claims-made basis to claims first "
           "made and notified during the Period of Insurance; (b) it is a condition precedent that the Insured maintains a documented safeguarding "
           "policy and, where required, obtains and records satisfactory DBS/PVG (or equivalent) checks for all persons working with children or "
           "vulnerable adults, and applies appropriate supervision arrangements; (c) no indemnity applies to any person who committed, condoned or, "
           "after becoming aware of it, failed to take reasonable steps to prevent the abuse; (d) the Self-Insured Retention stated in the Schedule "
           "applies; and (e) fines, penalties and punitive/exemplary damages are excluded save where insurable by law.",
   mode="Optional / Schedule-selectable", uw="HIGH \u2014 severe, long-tail, reputational; reinsurance-sensitive.",
   claims="High severity / low frequency; coverage litigation likely.", priority="High",
   signoff="YES \u2014 claims + legal + reinsurance; consider directing the core exposure to a specialist abuse market.",
   status="PARKED \u2014 proposed wording for consideration (not in current wording)"),
 dict(title="Worldwide / USA-Canada territory option (Media Liability)",
   comp="Tysers (PI worldwide)",
   tmhcc="S12 limited to Schedule Geographical Limits; excludes actions brought/governed outside the stated Jurisdiction (default ex-US/Canada).",
   why="Media clients with global digital distribution can face actions outside the default jurisdiction; TMHCC looks narrower on the matrix.",
   action="Add an OPTIONAL worldwide (and separately, USA/Canada) write-back to the Geographical Limits / Legal-Action exclusion, rated accordingly.",
   loc="Section 12 (Media Liability) \u2014 new Optional Extension after 'Distributors and Purchasers'.",
   wording="Worldwide Territory and Jurisdiction (Optional) \u2014 applies only if stated operative in the Schedule. Where operative, the Geographical "
           "Limits are amended to anywhere in the world and the Jurisdiction to worldwide, and the exclusions of claims brought, or in which the "
           "governing law is contended to be, outside the Jurisdiction shall not apply. Cover for claims brought in, or determined under the laws of, "
           "the USA or Canada (or any territory/protectorate thereof) applies only if 'USA/Canada Jurisdiction' is ADDITIONALLY stated operative.",
   mode="Optional / Schedule-selectable", uw="HIGH if US/Canada operative \u2014 price/sub-limit/higher excess; retain ex-US/Canada default.",
   claims="Higher in US/Canada (costs, punitive). Control via defence-cost caps and consent.", priority="High",
   signoff="YES (S12) \u2014 confirm reinsurance treaty territory before offering US/Canada.",
   status="IMPLEMENTED as tracked change (B5) \u2014 awaiting UW sign-off"),
 dict(title="Distributors & Purchasers extension (Media Liability)",
   comp="Tysers (clause 8.7, up to 5x limit)",
   tmhcc="No equivalent extension.",
   why="Production/distribution clients expect their distribution chain to be protected.",
   action="Add an optional Distributors & Purchasers extension, capped at a multiple of the limit, with control-of-defence and notice conditions.",
   loc="Section 12 (Media Liability) \u2014 new Extension after 'Indemnity to Principals'.",
   wording="The indemnity provided by Insuring Clause 1. (Indemnity) is extended to apply to any purchaser, co-producer, licensee or distributor of "
           "Media Material produced or supplied by the Insured, but only in respect of claims arising from such Media Material and only where the "
           "Insured is contractually obliged to provide such indemnity. The Insurer's total liability under this Extension shall not exceed five (5) "
           "times the Indemnity Limit in the aggregate during the Period of Insurance for all claims arising from each production. Cover is conditional "
           "upon the Insurer retaining the right to conduct the defence and settlement of any such claim, and upon any claim being first made against, "
           "and notified to, the Insurer during the Period of Insurance.",
   mode="Optional", uw="Medium \u2014 control via claim window, certificate, control-of-defence (mirror Tysers).",
   claims="Medium; aggregate multiple must be capped.", priority="Medium",
   signoff="YES (S12) \u2014 confirm acceptable aggregate multiple.",
   status="IMPLEMENTED as tracked change (B1) \u2014 awaiting UW sign-off"),
 dict(title="Representation costs at investigations / inquiries (Media Liability)",
   comp="Tysers (clause 8.15, GBP 25k)",
   tmhcc="Provided only via Data-Protection defence; otherwise absent.",
   why="Regulators increasingly investigate content/advertising (ASA/CMA/Ofcom).",
   action="Add a sub-limited representation-costs extension (GBP 25k).",
   loc="Section 12 (Media Liability) \u2014 new extension after the IP-pursuit clause.",
   wording="Up to a maximum of GBP 25,000 in the aggregate in the Period of Insurance, for the reasonable costs and expenses incurred by the Insured, "
           "with the Insurer's prior written consent, in respect of attendance at or representation before any official examination, investigation, "
           "inquiry or other proceeding arising from the Insured's Media Business Services and likely to give rise to a claim under Insuring Clause 1. "
           "This cover forms part of and does not increase the Indemnity Limit.",
   mode="Automatic (sub-limited)", uw="Low \u2014 small sub-limit.", claims="Low.", priority="Medium",
   signoff="YES (S12) \u2014 confirm sub-limit and consent mechanics.",
   status="IMPLEMENTED as tracked change (B2) \u2014 awaiting UW sign-off"),
 dict(title="Journalistic source-protection costs (Media Liability)",
   comp="Tysers (clause 8.13)",
   tmhcc="Not provided.",
   why="Broker-sensitive for editorial, news and publishing clients.",
   action="Add a sub-limited source-protection costs extension (consent; counsel reasonable-prospects test).",
   loc="Section 12 (Media Liability) \u2014 new extension following Representation Costs.",
   wording="Up to the sub-limit stated in the Schedule, with the Insurer's prior written consent, for the reasonable legal costs of opposing or "
           "responding to any subpoena, court order or other legal compulsion requiring the Insured to disclose the identity of a confidential "
           "journalistic source, where such disclosure arises from the Insured's Media Business Services, and only where, in the opinion of counsel, "
           "there are reasonable grounds to oppose disclosure. This cover forms part of and does not increase the Indemnity Limit.",
   mode="Optional / Schedule sub-limit", uw="Low \u2014 low-frequency; consent + counsel test.", claims="Low frequency.", priority="Medium",
   signoff="YES (S12) \u2014 confirm sub-limit.",
   status="IMPLEMENTED as tracked change (B3) \u2014 awaiting UW sign-off"),
 dict(title="Criminal / regulatory defence-costs cross-reference (Media Liability)",
   comp="Tysers (statutory defence GBP 1m); Yutree (criminal-prosecution defence GBP 250k)",
   tmhcc="S12 funds only Data-Protection defence (GBP 250k); broader criminal/regulatory defence sits in S13/S14.",
   why="On a section-by-section read of S12 alone, TMHCC looks narrower.",
   action="Add an express cross-reference to S13/S14 plus a modest sub-limited contribution (excess of S13/S14), excluding fines.",
   loc="Section 12 (Media Liability) \u2014 new clause following Source-Protection costs.",
   wording="In addition to the Data Protection Defence Costs provided above, the Insured is reminded that defence of criminal and regulatory "
           "proceedings may also be available under Section 13 (Commercial Legal Expenses) and Section 14 (Management Liability). The Insurer will "
           "further contribute, up to the sub-limit stated in the Schedule and with prior written consent, towards the reasonable defence costs of any "
           "criminal or regulatory proceeding arising directly from the Insured's Media Business Services, save to the extent covered under S13 or S14. "
           "This cover forms part of and does not increase the Indemnity Limit and excludes fines, penalties and costs incurred after a plea or finding of guilt.",
   mode="Automatic (cross-reference + sub-limit)", uw="Low\u2013medium \u2014 largely clarifying.", claims="Low.", priority="Medium-High",
   signoff="YES (S12) \u2014 confirm interaction with S13/S14.",
   status="IMPLEMENTED as tracked change (B4) \u2014 awaiting UW sign-off"),
 dict(title="King's Counsel dispute-resolution clause (Media Liability)",
   comp="Yutree (KC clause)",
   tmhcc="Relies on a general mediation/dispute condition.",
   why="Drafting-clarity opportunity; reduces coverage friction on defence/settlement disputes.",
   action="Add a King's Counsel-determination clause to S12 defence/settlement provisions.",
   loc="Section 12 (Media Liability) \u2014 new clause after the dispute/mediation provision.",
   wording="In respect of Section 12 only, if the Insured and the Insurer disagree as to whether or how any claim should be defended, settled or "
           "pursued, either party may require the matter to be referred to a King's Counsel of the English Bar (mutually agreed, or failing agreement "
           "within 14 working days, appointed by the Chairman of the Bar Council). The opinion of such King's Counsel as to the conduct of the matter "
           "shall be binding on both parties, having regard to the interests of both, and the costs of the reference shall be allocated on a fair and equitable basis.",
   mode="Automatic", uw="Low \u2014 procedural.", claims="Reduces dispute cost.", priority="Low-Medium",
   signoff="YES (S12) \u2014 confirm cost-allocation wording.",
   status="IMPLEMENTED as tracked change (B6) \u2014 awaiting UW sign-off"),
 dict(title="Pollution negligent-advice write-back (Media Liability PI)",
   comp="Yutree (pollution write-back for own negligence)",
   tmhcc="S12 excludes seepage/pollution/contamination outright.",
   why="Genuine E&O exposures (negligent advice/specification) fall in the exclusion gap.",
   action="Add a narrow, sub-limited write-back limited to negligent advice, expressly excluding BI, property damage and clean-up.",
   loc="Section 12 (Media Liability) \u2014 proviso to the Seepage & Pollution exclusion.",
   wording="provided that this Exclusion shall not apply to any claim arising solely from a negligent act, error or omission in the provision of the "
           "Insured's Media Business Services (and not from any seepage, Pollution or contamination caused by the Insured's own operations, premises or "
           "activities), and provided further that this write-back shall not extend to any claim for Bodily Injury, property damage, or the costs of "
           "removing, nullifying, cleaning up or remediating any pollutant. The Insurer's liability under this write-back shall not exceed the sub-limit "
           "stated in the Schedule against this write-back.",
   mode="Automatic (narrow, sub-limited)", uw="Medium \u2014 must keep BI/contamination excluded; cap tightly.", claims="Medium; cap tightly.",
   priority="Medium", signoff="YES (S12) \u2014 careful legal drafting review essential.",
   status="IMPLEMENTED as tracked change (B7) \u2014 awaiting UW sign-off"),
 dict(title="Money restructure \u2014 Premises + Touring/Festivals/Events (Section 8)",
   comp="Entertainment Elite (event-money); 0523 'Venue'",
   tmhcc="Single Money section.",
   why="Touring/festival/event money exposure not clearly addressed.",
   action="Restructure Money into two Schedule-referenced extensions, preserving existing covers/exclusions.",
   loc="Section 8 (Money) \u2014 new extensions after 'Loss of Keys'.",
   wording="Money \u2013 Premises: extends cover to Damage to Money at the Premises up to the Schedule sub-limit. Money \u2013 Touring, Festivals and Events: "
           "extends cover to Money in transit/temporary storage/safe/custody at any venue, festival site, box office or touring/event location, including "
           "(a) damage to safes/containers/money belts; (b) damage to clothing, personal effects and personal Money following assault/violence; and (c) "
           "employee dishonesty discovered within 12 months. Both are subject to the Schedule sub-limit and do not reduce existing Money cover. (Full text in the Full Redline, Section 8.)",
   mode="Schedule-selectable (two sub-limits)", uw="Medium \u2014 dishonesty/assault heads; Schedule sub-limits.", claims="Medium.",
   priority="Medium", signoff="YES \u2014 underwriting to set sub-limits.",
   status="IMPLEMENTED as tracked change (A4) \u2014 awaiting UW sign-off"),
 dict(title="Proof of Ownership and Value \u2014 claims condition (Sections 1\u201311)",
   comp="Tysers, Entertainment Elite (Money security/proof conditions)",
   tmhcc="No express proof-of-ownership condition.",
   why="Claims-handling hygiene for theft/property/equipment claims; reduces disputed-value claims.",
   action="Add a Proof of Ownership and Value claims condition.",
   loc="Policy Claims Conditions (S1\u201311) \u2014 between 'Notification to the Police' and 'Terms of Settlement'.",
   wording="Proof of Ownership and Value \u2014 The Insured shall, at the request of the Insurer, produce reasonable documentary proof of ownership and of "
           "the value of any property the subject of a claim (for example purchase invoices, receipts, valuations, asset registers, hire agreements or "
           "photographs).",
   mode="Automatic (claims condition)", uw="Low\u2013medium \u2014 confirm ordinary condition (not CP).", claims="Reduces disputed-value claims.",
   priority="Medium", signoff="YES \u2014 confirm status (ordinary condition vs CP).",
   status="IMPLEMENTED as tracked change \u2014 awaiting UW sign-off"),
 dict(title="Broaden S13 'Employee' & align S12 'Computer System' definitions",
   comp="Tysers (p9), Yutree (p88) employee defs; internal S15 cyber def",
   tmhcc="S13 'Employee' was narrow; S12 'Computer System' was narrower than S15.",
   why="Consistency and competitiveness of the protected classes/triggers.",
   action="Broaden S13 'Employee' (labour-only, hired/borrowed, voluntary/work-experience/secondee/student/prospective) and align S12 'Computer System' to S15.",
   loc="Section 13 (Definitions) and Section 12 (Definitions).",
   wording="(See the Full Redline \u2014 S13 Employee definition and S12 Computer System definition, both shown as old\u2192new tracked replacements.)",
   mode="Automatic (definition)", uw="Medium \u2014 widens protected class/triggers.", claims="Low\u2013medium.", priority="Medium",
   signoff="YES \u2014 confirm intended widening (S13 EL/legal-expenses class; S12 computer triggers).",
   status="IMPLEMENTED as tracked change (A5/A6) \u2014 awaiting UW sign-off"),
 dict(title="Personal Accident & Business Travel section",
   comp="Tysers (extensive); Yutree (PA assault)",
   tmhcc="No standalone PA / business-travel section.",
   why="Entertainment clients (crew, artists, touring personnel) routinely expect PA/business-travel; visible whole-section gap.",
   action="Add a new optional PA & Business Travel section \u2014 capacity-permitting; control via benefit schedule, age limits, hazardous-activity carve-outs.",
   loc="New optional Section (PA & Business Travel) within the 15-section structure.",
   wording="Optional Personal Accident & Business Travel Section (operative only if stated in the Schedule): the Insurer will pay the benefits stated in "
           "the Benefit Schedule to or in respect of an Insured Person who sustains Bodily Injury caused by an Accident during the Period of Insurance "
           "(death; permanent total/partial disablement; temporary total disablement), together with business-travel cover (emergency medical, "
           "repatriation, cancellation, personal effects) where stated operative, subject to the age limits, hazardous-activity conditions and "
           "territorial limits stated in the Schedule. [Skeleton \u2014 to be drafted in full subject to capacity/appetite.]",
   mode="Optional (new section)", uw="Medium \u2014 PA/travel well-understood; control via benefit schedule.", claims="Low\u2013medium; defined benefits cap exposure.",
   priority="High", signoff="YES \u2014 confirm capacity/appetite; draft benefit schedule + assault definition.",
   status="PARKED \u2014 proposed skeleton (not in current wording)"),
 dict(title="Asbestos negligent-advice write-back (PI) \u2014 consider",
   comp="Tysers (asbestos professional-duty write-back, GBP 1m, ex-BI)",
   tmhcc="S12 excludes asbestos outright.",
   why="Negligent advice/specification touching asbestos is a genuine E&O exposure.",
   action="CONSIDER a narrow negligent-advice write-back (ex-BI, ex-contamination); otherwise leave excluded.",
   loc="Section 12 (Media Liability) \u2014 proviso to the Asbestos exclusion (if adopted).",
   wording="[If adopted] provided that this Exclusion shall not apply to a claim arising solely from a negligent act, error or omission in the provision "
           "of the Insured's Media Business Services, and shall not extend to any claim for Bodily Injury or the costs of removing/remediating asbestos; "
           "sub-limit per Schedule.",
   mode="Optional (if adopted)", uw="Medium \u2014 ring-fence to negligent advice; exclude BI and clean-up.", claims="Medium; cap tightly.", priority="Medium",
   signoff="YES \u2014 careful drafting; keep BI and contamination excluded.",
   status="PARKED \u2014 for consideration"),
 dict(title="Patents \u2014 LEAVE EXCLUDED (no action)",
   comp="Tysers (covers patents)",
   tmhcc="Excludes patents (as does Yutree).",
   why="Patents are hard to underwrite and high-severity; the exclusion is a deliberate, defensible restriction.",
   action="No change. At most a limited defence-costs write-back; otherwise leave excluded and explain as disciplined underwriting.",
   loc="Section 12 (Media Liability) \u2014 IP exclusion (no change).",
   wording="(No change recommended.)",
   mode="n/a", uw="Retaining the exclusion protects TMHCC.", claims="Patents are high-severity.", priority="Low",
   signoff="No change \u2014 document rationale.",
   status="NO ACTION \u2014 confirmed defensible restriction"),
 dict(title="ICOW / Book Debts naming + computer-breakdown signpost",
   comp="Allianz (names ICOW/Book Debts); Yutree (Computer Breakdown section)",
   tmhcc="BI (S3) covers ICOW/AICOW & book debts; IT/computer breakdown consolidated within S1/S2.",
   why="Presentational \u2014 competitors show more named heads; avoids perceived gaps.",
   action="'Accounts Receivable' re-labelled '(Book Debts)' (done). Confirm/signpost computer-breakdown within S1/S2.",
   loc="Section 3 (Definitions / Basis of Settlement) and Sections 1/2.",
   wording="(Relabel implemented; add an explicit 'computer/IT breakdown' signpost within S1/S2 if confirmed in scope.)",
   mode="Automatic (labelling/clarification)", uw="Low \u2014 clarification, not broadening.", claims="Neutral.", priority="Low-Medium",
   signoff="Confirm S3 scope and S1/S2 breakdown; headings only.",
   status="PARTLY DONE (Book Debts relabel) / clarify breakdown signpost"),
]


def main():
    doc = B.Document()
    B.set_normal_style(doc)
    B.setup_page(doc, landscape=False, margin_cm=1.8)
    B.add_logo_header(doc, left_text="TMHCC Media & Music Combined \u2014 Gap-Fill Strategy")
    B.add_footer_pagenum(doc, note="Phase 05 \u2014 gap-fill strategy. Copy-paste wording is PROPOSED and subject to TMHCC legal/underwriting sign-off. "
                                   "'Implemented as tracked change' = present in the Full Redline but NOT accepted.")
    B.cover_page(doc,
        "Phase 05 \u00b7 Gap-Fill Strategy",
        "Gap-Fill / Enhancement Strategy",
        "Every gap with copy-paste wording, exact location, risk, priority and status",
        ["Updated from the refreshed six-insurer legal review (Phase 03), incl. the abuse/Tysers item.",
         "Purpose: make TMHCC more holistic and demonstrably market-leading where commercially sensible \u2014 not to copy competitors blindly.",
         "Where TMHCC should NOT follow a competitor (e.g. patents), the reason is stated."],
        ["TMHCC final wording (commit 58b8340) vs six competitors"])
    doc.add_page_break()

    # priority summary
    B.h1(doc, "Priority summary")
    st = B.make_table(doc, ["#", "Gap / enhancement", "Mode", "Priority", "Status"], [0.9, 7.6, 3.4, 2.3, 3.8])
    for i, g in enumerate(GAPS):
        c = st.add_row().cells
        B.text_cell(c[0], str(i + 1), size=8.3)
        B.text_cell(c[1], g["title"], size=8.3, bold=True, color=B.TEAL)
        B.text_cell(c[2], g["mode"], size=7.8)
        pri = g["priority"]
        B.text_cell(c[3], pri, size=8, bold=True, color=(B.RUST if pri.startswith("High") else B.INK))
        stt = g["status"]
        col = B.GOLD if "PARKED" in stt or "NO ACTION" in stt else "1B7A3D" if "IMPLEMENTED" in stt else B.INK
        B.text_cell(c[4], stt.split(" \u2014")[0], size=7.6, color=col)
    B.zebra(st)
    doc.add_page_break()

    B.h1(doc, "Detailed gap-fill recommendations")
    for i, g in enumerate(GAPS):
        B.h2(doc, f"{i + 1}. {g['title']}")
        t = B.make_table(doc, ["Field", "Detail"], [4.0, 14.0])
        rows = [("Competitor(s) broader/better", g["comp"]), ("TMHCC current position", g["tmhcc"]),
                ("Why this matters", g["why"]), ("Recommended action", g["action"]),
                ("Exact policy location", g["loc"]),
                ("Automatic / optional / schedule", g["mode"]),
                ("Underwriting risk", g["uw"]), ("Claims risk", g["claims"]),
                ("Priority", g["priority"]), ("Sign-off required", g["signoff"]),
                ("Status", g["status"])]
        for k, v in rows:
            c = t.add_row().cells
            B.text_cell(c[0], k, size=8.3, bold=True, color=B.TEAL)
            col = B.INK
            if k == "Status":
                col = B.GOLD if ("PARKED" in v or "NO ACTION" in v) else ("1B7A3D" if "IMPLEMENTED" in v else B.INK)
            if k == "Priority" and v.startswith("High"):
                col = B.RUST
            B.text_cell(c[1], v, size=8.3, color=col, bold=(k in ("Status", "Priority")))
        # copy-paste wording box
        B.callout(doc, "Copy-paste-ready proposed wording:", g["wording"],
                  bg="F4F7F9", border=B.TEAL, lead_color=B.TEAL)
        B.spacer(doc, 6)

    B.h1(doc, "Strategic note")
    B.para(doc, "The objective is to make TMHCC demonstrably broader and more holistic WHERE COMMERCIALLY SENSIBLE \u2014 not to mirror competitors "
                "blindly. TMHCC already leads on section count and on four unique sections (Loss of Licence, Legal Expenses, Management Liability, "
                "standalone Cyber). The recommendations above close the genuine, wording-supported narrower points (abuse, jurisdiction, S12 "
                "extensions, PA). Patents and the default ex-US/Canada jurisdiction are retained deliberately. Every implemented item remains a "
                "tracked change pending underwriting/legal sign-off; parked items carry proposed wording for consideration.", size=9.5)

    B.save_doc(doc, OUT)
    print("saved", OUT, "gaps:", len(GAPS))


main()
