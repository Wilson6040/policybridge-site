# -*- coding: utf-8 -*-
"""Round-7 content: final gap positions, copy-paste wording for every recommendation,
Section 12 sign-off list, market-leading opportunities, and deepened comparison strengths.
Imported by build_gap.py and build_full.py. Grounded in the FINAL updated TMHCC wording
(TMHCC_Media_Combined_0526_FINAL_Clean.docx) and the five competitor extracts."""

# Index here = position in cmpdata.GAPFILL (NOT the displayed gap number).
# Displayed gap number (priority order): i0->1 i1->2 i3->3 i2->4 i4->5 i5->6 i6->7 i8->8 i7->9 i9->10 i10->11 i11->12
GAP_R7 = {
 0: dict(  # PA & Business Travel  (displayed Gap 1)
   status="Parked \u2014 NOT being added", impl="Not implemented \u2014 commercial decision (client direction)",
   loc="Would require a new optional Section / extension after Section 8.",
   wording=("Personal Accident & Business Travel (Optional Section) \u2014 If stated as operative in the Schedule, "
            "the Insurer will pay the benefits stated in the Schedule to an Insured Person who sustains bodily injury "
            "caused by accidental, violent, external and visible means during the Period of Insurance, in accordance "
            "with the Benefit Schedule, age limits and hazardous-activity provisions stated therein."),
   signoff="Yes", uw="Medium \u2014 control via benefit schedule, age limits, hazardous-activity carve-outs.",
   final=("NOTE: Personal Accident is NOT being added in this round. This is distinct from the existing "
          "Personal Assault cover under Section 8 (Money), Sub-Section 2, which is retained as-is.")),
 1: dict(  # Worldwide / US-Canada Media Liability  (displayed Gap 2)
   status="Parked \u2014 Section 12 sign-off list", impl="Not implemented in wording (Section 12 \u2014 legal/UW sign-off required)",
   loc="Section 12 (Media Liability), as an Optional Extension following the 'Legal Action' / 'Geographical Limits' exclusions (p.73+).",
   wording=("Worldwide Territory and Jurisdiction (Optional)\n"
            "This Optional Extension applies only if stated as operative in the Schedule. Where stated as operative, "
            "the Geographical Limits applicable to this Section are amended to anywhere in the world and the Jurisdiction "
            "applicable to this Section is amended to worldwide, and the exclusions of claims brought, or in which the "
            "governing law is contended to be, outside the Jurisdiction shall not apply.\n"
            "Cover in respect of claims brought in, or determined under the laws of, the United States of America or Canada "
            "(or any territory or protectorate thereof) applies only if \u201cUSA/Canada Jurisdiction\u201d is additionally stated "
            "as operative in the Schedule."),
   signoff="Yes", uw="High if US/Canada included \u2014 rate, sub-limit, higher excess, defence-cost caps; keep ex-US/Canada as default.",
   final=("FINAL POSITION (Gap 2): The wording already provides worldwide-excluding-USA/Canada cover by DEFAULT via the "
          "'Jurisdiction' definition (worldwide but excluding the USA and Canada where the Schedule is silent), bounded by the "
          "Schedule 'Geographical Limits' and the Section 12 'Legal Action' exclusion. There is NOT yet a single, clean, "
          "Schedule-selectable 'Worldwide (incl. USA/Canada)' switch. The optional clause above supplies that switch and a "
          "separate USA/Canada selectable. Held in the Section 12 sign-off list \u2014 not applied to the wording.")),
 2: dict(  # Distributors & Purchasers  (displayed Gap 4)
   status="Parked \u2014 Section 12 sign-off list", impl="Not implemented (Section 12 \u2014 sign-off)",
   loc="Section 12, new Optional Extension within the Extensions block (p.73+).",
   wording=("Distributors and Purchasers (Optional) \u2014 The indemnity provided by this Section extends to any distributor, "
            "licensee, co-producer or purchaser of the Insured\u2019s media material for their liability arising from that material, "
            "provided that: (a) the Insurer\u2019s total liability for all such parties shall not exceed the multiple of the Limit of "
            "Liability stated in the Schedule; (b) the claim is first made within 36 months of the relevant supply; and (c) the "
            "Insurer retains control of the defence and settlement of any such claim."),
   signoff="Yes", uw="Medium \u2014 36-month window, certificate, control of defence, capped aggregate (mirror Tysers cl. 8.7)."),
 3: dict(  # Criminal / regulatory defence  (displayed Gap 3)
   status="Parked \u2014 Section 12 sign-off list", impl="Not implemented (Section 12 \u2014 sign-off)",
   loc="Section 12 \u2014 either a new sub-limited extension, or a cross-reference note after the Defence Costs provisions (p.73+).",
   wording=("Criminal and Regulatory Defence Costs (Clarification / Optional) \u2014 For the avoidance of doubt, the defence of "
            "statutory, regulatory or criminal proceedings arising from the Business (other than the Data Protection defence costs "
            "expressly provided in this Section) is addressed under Section 13 (Commercial Legal Expenses) and Section 14 "
            "(Management Liability). Where stated as operative in the Schedule, this Section will in addition indemnify the Insured "
            "for defence costs incurred with the Insurer\u2019s prior written consent up to GBP [ ] in respect of such proceedings."),
   signoff="Yes", uw="Low\u2013medium \u2014 cross-reference is essentially nil-cost; any S12 sub-limit should be modest."),
 4: dict(  # Source-protection costs  (displayed Gap 5)
   status="Parked \u2014 Section 12 sign-off list", impl="Not implemented (Section 12 \u2014 sign-off)",
   loc="Section 12, new sub-limited Optional Extension (p.73+).",
   wording=("Journalistic Source Protection Costs (Optional) \u2014 The Insurer will pay, up to the sub-limit stated in the Schedule, "
            "legal costs reasonably incurred with the Insurer\u2019s prior written consent in resisting any subpoena, application or court "
            "order that would require the Insured to disclose a confidential journalistic source, provided there are reasonable "
            "prospects of successfully resisting such disclosure."),
   signoff="Yes", uw="Low \u2014 small sub-limit; consent and prospects-of-success conditions (mirror Tysers cl. 8.13)."),
 5: dict(  # Representation costs  (displayed Gap 6)
   status="Parked \u2014 Section 12 sign-off list", impl="Not implemented (Section 12 \u2014 sign-off)",
   loc="Section 12, new sub-limited Optional Extension (p.73+).",
   wording=("Representation Costs at Investigations and Inquiries (Optional) \u2014 The Insurer will pay, up to GBP 25,000 in the "
            "aggregate, the reasonable costs of legal representation incurred with the Insurer\u2019s prior written consent at any official "
            "examination, investigation or inquiry into a matter that could give rise to a claim under this Section."),
   signoff="Yes", uw="Low \u2014 small sub-limit (mirror Tysers cl. 8.15)."),
 6: dict(  # Asbestos / pollution PI write-back  (displayed Gap 7)
   status="Parked \u2014 Section 12 sign-off list", impl="Not implemented (Section 12 \u2014 sign-off; careful drafting essential)",
   loc="Section 12 \u2014 narrow write-back to the asbestos/pollution exclusions (p.73+).",
   wording=("Professional Duty Write-back (Asbestos / Pollution) (Optional) \u2014 Notwithstanding the asbestos and pollution "
            "exclusions of this Section, the Insurer will indemnify the Insured, up to the sub-limit stated in the Schedule, for liability "
            "arising solely from negligent professional advice, design or specification in connection with asbestos or pollution, but "
            "excluding any liability for bodily injury and any liability for the cost of the contamination, remediation or clean-up itself."),
   signoff="Yes", uw="Medium \u2014 ring-fence to negligent advice; keep BI and contamination/clean-up excluded; tight cap."),
 7: dict(  # King's Counsel clause  (displayed Gap 9)
   status="Parked \u2014 Section 12 sign-off list", impl="Not implemented (Section 12 \u2014 sign-off)",
   loc="Section 12 \u2014 within the Defence and Settlement / dispute provisions (p.73+).",
   wording=("King\u2019s Counsel Determination (Optional) \u2014 If the Insured and the Insurer disagree as to whether any claim should be "
            "contested, the dispute shall be referred to a King\u2019s Counsel to be mutually agreed (or, failing agreement, nominated by "
            "the President of the Bar Council), whose determination shall be binding. The costs of the reference shall be at the "
            "discretion of the King\u2019s Counsel."),
   signoff="Yes", uw="Low \u2014 procedural; confirm cost-allocation wording (mirror Yutree KC clause)."),
 8: dict(  # ICOW / Book Debts  (displayed Gap 8)  -- IMPLEMENTED
   status="Implemented now (tracked change)", impl="Implemented now",
   loc="Section 3 (Business Interruption), Definitions and Basis of Settlement \u2014 'Accounts Receivable' head (p.38+).",
   wording=("Accounts Receivable (Book Debts) \u2014 [head re-labelled]. Increase in Cost of Working and Additional Increase in Cost "
            "of Working are already named, discrete Basis-of-Settlement heads in Section 3; the 'Accounts Receivable' head has been "
            "labelled '(Book Debts)' so the book-debts cover is unmistakable for like-for-like comparison with Allianz/AXA XL."),
   signoff="No", uw="Nil \u2014 presentational clarification only; no broadening of cover.",
   final=("FINAL POSITION (Gap 8): Section 3 already names 'Increase in Cost of Working' and 'Additional Increase in Cost of Working' "
          "as discrete settlement heads, and provides book-debts cover under 'Accounts Receivable'. The only refinement required was "
          "presentational: the 'Accounts Receivable' head is now labelled '(Book Debts)' (tracked change, definition + basis of "
          "settlement). No cover broadened; no sign-off required.")),
 9: dict(  # Computer / IT breakdown  (displayed Gap 10)  -- ALREADY COVERED
   status="Already covered \u2014 no wording change", impl="Confirmed \u2014 no change (avoids redundancy/over-broadening)",
   loc="Section 1 (Premises) Definitions & The Cover (p.23+); Section 2 'Mechanical and Electrical Breakdown' Optional Extension (p.31+); Section 3 ICOW (Computers) (p.38+).",
   wording=("(Optional signpost, NOT implemented) \u2014 'Computer / IT Breakdown: cover for Breakdown of Information Technology "
            "Property is provided under Section 1 (Business \u201cAll Risks\u201d) and, where away from the Premises, under the Mechanical and "
            "Electrical Breakdown Optional Extension of Section 2; consequential loss is dealt with under Section 3.' Not added so as not "
            "to imply new cover or alter the existing structure."),
   signoff="No", uw="Nil \u2014 cover already present; any change would be presentational only.",
   final=("FINAL POSITION (Gap 10): Confirmed against the live wording. Section 1 (Premises) DEFINES 'Breakdown' and covers/pays "
          "Information Technology Property 'Breakdown' (definition, insured event 'The Cover', and Basis of Settlement) \u2014 this is the "
          "old Section 4 IT-Property breakdown, preserved faithfully. Section 2 contains a 'Mechanical and Electrical Breakdown' OPTIONAL "
          "EXTENSION with its own broad Breakdown definition (all Property Insured, not IT-only). vs YUTREE: TMHCC matches Yutree on BOTH "
          "of Yutree\u2019s breakdown covers \u2014 Section 1 IT-Property Breakdown \u2261 Yutree\u2019s dedicated Computer Breakdown section, and Section 2 "
          "M&E Breakdown \u2261 Yutree\u2019s general 'Mechanical and electrical breakdown cover'. See Reviewer Notes for two points to confirm: "
          "(a) the brief\u2019s assumption that the IT-Property breakdown sits 'in Section 2' is not correct \u2014 it is in Section 1 (premises) "
          "and Section 3 (BI computers); (b) narrowing Section 2 to 'IT-only' would REMOVE existing optional cover and make TMHCC narrower "
          "than Yutree \u2014 not done without explicit instruction and sign-off.")),
 10: dict(  # Media Material definition  (displayed Gap 11)
   status="Parked \u2014 for consideration", impl="Not implemented \u2014 optional drafting polish",
   loc="General Definitions or Section 12 Definitions (p.73+).",
   wording=("Media Material (Definition) \u2014 'Media Material means any data, text, sounds, images, advertising, film, video, audio, "
            "broadcast, publication, website or other content created, produced, published, distributed, broadcast or disseminated by or "
            "on behalf of the Insured in the course of the Business.'"),
   signoff="No", uw="Nil \u2014 drafting clarity only."),
 11: dict(  # Leave unchanged
   status="No change \u2014 deliberate restriction", impl="No change recommended (document rationale)",
   loc="Section 12 exclusions / 'Jurisdiction' definition.",
   wording=("No wording change. Retain the patents exclusion, the broad communicable-disease exclusion and the default "
            "worldwide-excluding-USA/Canada jurisdiction. These are deliberate, defensible underwriting positions."),
   signoff="No", uw="Retaining these protects TMHCC \u2014 broadening would materially increase volatility."),
}

# ---------------------------------------------------------------------------
# TASK 7 — Section 12 (Media Liability) Suggested Upgrades held for sign-off.
# (title, copy-paste wording, exact location, amendment type, rationale + competitor support, sign-off)
SECTION12_UPGRADES = [
 dict(title="Worldwide Territory & Jurisdiction (Optional) \u2014 incl. separate USA/Canada selectable",
   wording=GAP_R7[1]['wording'], loc=GAP_R7[1]['loc'],
   atype="Schedule-selectable option (territory/jurisdiction)",
   rationale="Gap 2. Tysers PI is worldwide. Gives global-distribution media clients a clean Schedule switch to worldwide and a separate, rated USA/Canada option, without changing the default ex-US/Canada appetite.",
   signoff="Legal + underwriting (territory, reinsurance treaty, rating)."),
 dict(title="Criminal & Regulatory Defence Costs \u2014 clarification / optional sub-limit",
   wording=GAP_R7[3]['wording'], loc=GAP_R7[3]['loc'],
   atype="Clarification (cross-reference) + optional new cover",
   rationale="Tysers statutory defence GBP 1m; Yutree criminal-defence GBP 250k. On a Section-12-only read TMHCC looks narrower; the cross-reference to S13/S14 removes the apparent gap at nil cost.",
   signoff="Legal + underwriting (confirm S13/S14 triggers; any S12 sub-limit)."),
 dict(title="Distributors & Purchasers Extension",
   wording=GAP_R7[2]['wording'], loc=GAP_R7[2]['loc'],
   atype="New optional cover (extension)",
   rationale="Tysers cl. 8.7 (up to 5x limit). Protects the distribution chain of production/distribution clients.",
   signoff="Legal + underwriting (aggregate multiple; control of defence)."),
 dict(title="Journalistic Source Protection Costs",
   wording=GAP_R7[4]['wording'], loc=GAP_R7[4]['loc'],
   atype="New optional sub-limited cover",
   rationale="Tysers cl. 8.13. Broker-sensitive for editorial/news/publishing clients; low frequency.",
   signoff="Legal + underwriting (sub-limit; prospects test)."),
 dict(title="Representation Costs at Investigations & Inquiries (GBP 25k)",
   wording=GAP_R7[5]['wording'], loc=GAP_R7[5]['loc'],
   atype="New optional sub-limited cover",
   rationale="Tysers cl. 8.15 (GBP 25k). Useful for advertising/marketing clients (ASA/CMA investigations).",
   signoff="Legal + underwriting (sub-limit; align with S13/S14)."),
 dict(title="Professional-Duty Write-back (Asbestos / Pollution) \u2014 negligent advice only",
   wording=GAP_R7[6]['wording'], loc=GAP_R7[6]['loc'],
   atype="Exclusion write-back (narrow)",
   rationale="Tysers asbestos professional-duty write-back (GBP 1m, ex-BI); Yutree pollution write-back for own negligence. Closes a genuine E&O gap WITHOUT taking environmental/contamination risk.",
   signoff="Legal + underwriting (must keep BI and contamination/clean-up excluded; tight cap)."),
 dict(title="King\u2019s Counsel Determination clause",
   wording=GAP_R7[7]['wording'], loc=GAP_R7[7]['loc'],
   atype="Condition amendment (dispute resolution)",
   rationale="Yutree KC clause. Gives clients certainty on defence/settlement disputes; procedural, low risk.",
   signoff="Legal (cost-allocation wording)."),
 dict(title="'Media Material' definition",
   wording=GAP_R7[10]['wording'], loc=GAP_R7[10]['loc'],
   atype="Definition amendment",
   rationale="Tysers defines 'Media Material'. Sharpens the subject-matter of Section 12 cover; drafting clarity only.",
   signoff="Legal (drafting polish)."),
 dict(title="Reputation Management / Withdrawal of Content \u2014 optional uplift",
   wording=("(Optional uplift) \u2014 The Reputation Management and Withdrawal of Content sub-limits stated in this Section (each "
            "GBP 250,000) may, where stated in the Schedule, be increased; and/or a first-party reputational-harm trigger may be added "
            "so that reputation-management costs are available following an insured event even where no third-party claim has yet been made."),
   loc="Section 12 \u2014 existing 'Reputation Management' and 'Withdrawal of Content' clauses (p.73+).",
   atype="Limit uplift / optional trigger amendment",
   rationale="TMHCC ALREADY provides Reputation Management (GBP 250k) and Withdrawal of Content (GBP 250k) \u2014 matching Yutree\u2019s reputation-management/withdrawal covers. This is an optional positioning uplift only, not new cover.",
   signoff="Legal + underwriting (limit/trigger change)."),
]

# ---------------------------------------------------------------------------
# TASK 6 — Market-leading wording opportunities (final)
MARKETLEADING_R7 = dict(
  standalone=dict(
    title="Standalone, built-in specialist cover (not bolt-ons)",
    tmhcc=("TMHCC is the only wording in the peer group that carries genuine, free-standing specialist sections: "
           "Cyber (Section 15 \u2014 CyberGuard\u2122 (Cyber Liability)), Commercial Legal Expenses (Section 13), Management "
           "Liability (Section 14), Loss of Licence (Section 10) and Production Indemnity \u2018All Risks\u2019 (Section 11)."),
    comp=("Liberty, Allianz and AXA XL carry NONE of these specialist sections; Tysers and Yutree carry only some. No competitor "
          "wording reviewed offers all of them."),
    cite="Sections 10, 11, 13, 14, 15 (contents p.67\u2013103).",
    rec=("Position the wording as \u2018standalone cyber, legal expenses, management liability, loss of licence and production "
         "indemnity built in \u2014 not bolt-ons.\u2019"),
    uw="Nil \u2014 positioning of cover that already exists.", signoff="No (positioning only)."),
  reputation=dict(
    title="Reputation management & reputational-harm support",
    tmhcc=("Section 12 (Media Liability) ALREADY provides Reputation Management (up to GBP 250,000) and Withdrawal of Content "
           "(up to GBP 250,000) as standard, plus the general duty-to-mitigate provisions."),
    comp=("Yutree offers Reputation management costs cover (PR consultant / crisis) and Withdrawal of consent cover. TMHCC therefore "
          "MATCHES Yutree on reputation support; Liberty, Allianz and AXA XL offer none."),
    cite="Section 12 \u2014 'Reputation Management' and 'Withdrawal of Content' clauses (contents p.73+).",
    rec=("Highlight reputation management + withdrawal-of-content as STANDARD. OPTIONAL uplift (sign-off): increase the GBP 250k "
         "sub-limits and/or add a first-party reputational-harm trigger so costs are available before a third-party claim is made."),
    uw="Nil for the standard cover; Medium for any first-party trigger / limit uplift.", signoff="No for positioning; Yes for any uplift."),
  distinction=dict(
    pa="Personal Accident \u2014 NOT being added (no standalone PA / business-travel section is introduced in this round).",
    assault=("Personal Assault \u2014 EXISTING and RETAINED. Section 8 (Money), Sub-Section 2 provides Personal Assault benefits "
             "(death / permanent total disablement / temporary disablement / medical expenses) to an Insured Person assaulted in "
             "connection with an insured Money event. This is a distinct, narrower, benefit-based cover and is NOT the same as a "
             "Personal Accident section."),
  ),
  positioning=[
    "\u2018The only media & entertainment wording in the peer group with all fifteen sections.\u2019",
    "\u2018Standalone cyber, legal expenses, management liability, loss of licence and production indemnity \u2014 built in, not bolt-ons.\u2019",
    "\u2018Reputation management and withdrawal-of-content cover as standard in media liability.\u2019",
    "\u2018Flexible first-loss business-interruption limit \u2014 one Schedule limit across multiple loss heads.\u2019",
    "\u2018Worldwide property & equipment and worldwide transit as standard; worldwide media-liability available as a rated option.\u2019",
  ],
)

# ---------------------------------------------------------------------------
# TASK 8 — Deepened TMHCC strengths, evidenced against the FINAL wording.
# (area, our_position+cite, competitor_benchmark, verdict, flag)
COMPARISON_STRENGTHS_R7 = [
 dict(area="Flexible (first-loss) Business Interruption",
   ours=("Section 3 carries a 'Flexible Business Interruption Limit' endorsement: a SINGLE flexible limit shown in the Schedule applied "
         "collectively across multiple loss/expenditure heads \u2014 Loss of Income, Loss of Gross Profit, Loss of Fees, Increased Costs of "
         "Working, Additional Increased Costs of Working, Additional Research Expenditure and Outstanding Debts \u2014 instead of separate "
         "sub-limits ('All amounts payable collectively shall not exceed the Flexible Business Interruption Limit as shown in the Schedule')."),
   cite="Section 3 \u2014 'Flexible Business Interruption Limit' endorsement (contents p.38+).",
   comp=("Liberty/Allianz/AXA XL present conventional BI on a declaration/estimated-revenue basis with named heads and sub-limits; none "
         "of the reviewed wordings shows an equivalent single flexible first-loss BI limit across heads."),
   verdict="TMHCC broader / more flexible.", flag="UNCONFIRMED for competitor parity \u2014 verify against the live competitor BI wordings."),
 dict(area="Contract Site extension (Section 3)",
   ours=("The Section 3 'Contract Sites' extension covers interruption/interference as a result of Damage to property at ANY contract site "
         "ANYWHERE IN THE WORLD where the Insured are carrying out a contract of work. It is triggered by Damage to property at the contract "
         "site and does NOT require that property to be insured under the TMHCC policy."),
   cite="Section 3 \u2014 'Contract Sites' extension (contents p.38+).",
   comp=("Competitor BI extensions of this type are typically tied to insured property or to specified suppliers/premises; none reviewed clearly "
         "extends to damage to any (un-owned, un-insured) property at any worldwide contract site."),
   verdict="TMHCC broader.", flag="UNCONFIRMED \u2014 verify competitor contract-site/supplier extensions."),
 dict(area="Section 2 \u2014 worldwide Property & Equipment cover",
   ours=("Section 2 base 'Geographical Limits' are defined as 'Anywhere in the world', and the Section 2 Transit Extension also applies "
         "'anywhere in the world'. Worldwide cover therefore applies as STANDARD, subject to the 'Sub-Limit Restriction' that caps liability "
         "for Property Insured away from the Premises (any-one-location / any-one-item limits per the Schedule) and the Section conditions."),
   cite="Section 2 \u2014 'Geographical Limits' definition + 'Transit Extension' + 'Sub-Limit Restriction' (contents p.31+).",
   comp=("Several package competitors limit equipment/all-risks transit or away cover to a number of days (e.g. ~30 days) or to specified territories."),
   verdict="TMHCC broader (worldwide as standard, with away-from-premises sub-limits).",
   flag="CONFIRMED in TMHCC wording (no amendment needed). Competitor day-limits UNCONFIRMED pending the live competitor wordings."),
 dict(area="Floating contents across premises",
   ours=("Section 1 'Contents' is defined as machinery, plant and all other contents belonging to or held in trust by the Insured and "
         "'situate at ANY of the Insured\u2019s Premises' \u2014 i.e. contents float across all of the Insured\u2019s premises rather than being fixed to one address."),
   cite="Section 1 \u2014 'Contents' definition (contents p.23+).",
   comp=("Package competitors commonly fix contents to a specified location/address, with floating cover only by endorsement."),
   verdict="TMHCC broader (floating as standard).", flag="UNCONFIRMED \u2014 verify competitor location-basis wordings."),
 dict(area="Higher limits / broader automatic extensions",
   ours=("Section 12 carries Reputation Management (GBP 250k) and Withdrawal of Content (GBP 250k) as standard, Data-Protection defence "
         "costs (GBP 250k) and a Virus Transmission sub-limit of GBP 500k. The standalone Sections 13\u201315 add legal expenses, management "
         "liability and a full cyber section that most competitors lack entirely."),
   cite="Section 12 sub-limits + Sections 13\u201315 (contents p.73\u2013103).",
   comp=("Tysers virus transmission GBP 250k (TMHCC GBP 500k \u2014 higher); Tysers/Yutree match some S12 heads; Liberty/Allianz/AXA XL carry "
         "no media/PI/cyber/legal/management cover at all."),
   verdict="TMHCC equivalent-or-higher on the shared heads and uniquely broad overall.",
   flag="Virus GBP 500k vs Tysers GBP 250k CONFIRMED from extracts; other competitor limits UNCONFIRMED pending live wordings."),
 dict(area="US / USA-Canada / jurisdiction position",
   ours=("The 'Jurisdiction' definition is 'worldwide but excluding the USA (and its territories/possessions) and Canada' where the Schedule "
         "is silent; Section 12 additionally excludes claims brought, or governed by laws, outside the Jurisdiction ('Legal Action' exclusion) "
         "and work outside the Schedule 'Geographical Limits'. USA/Canada is therefore a deliberate, rated option rather than automatic."),
   cite="General Definitions 'Jurisdiction'; Section 12 'Geographical Limits' & 'Legal Action' exclusions (contents p.73+).",
   comp=("Tysers PI is worldwide with no jurisdiction exclusion (broader on territory); AXA XL by contrast excludes terrorism and punitive "
         "damages absolutely \u2014 evidence that disciplined territory/peril restrictions are market-normal."),
   verdict="More disciplined than Tysers on territory by design; worldwide-ex-US/Canada by default. US/Canada offered as a rated option (links to Gap 2).",
   flag="Underwriting/legal sensitivity \u2014 any worldwide/US-Canada widening is a Section 12 sign-off item."),
]
