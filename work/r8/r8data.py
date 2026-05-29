# -*- coding: utf-8 -*-
"""
Round-8 (EMERGENT DISPATCH v3) structured data.
Everything traces to: the FINAL TMHCC clean wording (source_uploaded.docx) and the five
attached competitor wordings (Tysers/Zurich, Yutree/AXA, Liberty, Allianz, AXA XL).
Competitor figures verified from /app/work/compare/src/*.pdf extractions and cmpdata.py.
Where a figure cannot be traced to an attached wording it is marked CANNOT-DETERMINE / UNCONFIRMED.
"""

AUTHOR = "TMHCC Wording Review (v3)"

# ---------------------------------------------------------------------------
# PART A — specific master-wording inclusions (verify-then-act)
# ---------------------------------------------------------------------------
PART_A = [
 dict(id="A1", title="Artists' Equipment extension (Section 2)",
   finding="ALREADY PRESENT. Section 2 (Property & Equipment) contains an \u201cArtists Equipment\u201d "
           "extension under the Technical Equipment extensions, limited to GBP 20,000 per occurrence and "
           "in the aggregate. Wording matches the instructed text.",
   location="Section 2 \u2013 Property & Equipment, \u201cArtists Equipment\u201d extension (clean wording).",
   action="No change \u2014 confirmed present and correctly placed. NOT duplicated.",
   status="Confirmed \u2013 no change"),
 dict(id="A2", title="Stock and merchandise (Section 2)",
   finding="ALREADY CATERED FOR. (a) \u201cStock\u201d is a named insured Item: \u2018Property Insured means "
           "Buildings, Contents, Stock, Rent, Information Technology Property and any other Items stated in "
           "the Schedule\u2019. (b) The Stock definition expressly includes \u2018materials in trade, merchandise "
           "(including work in progress\u2026)\u2019, so merchandise for sale is captured. (c) Exhibits cover "
           "expressly includes \u2018demonstration and sample Stock/merchandise\u2019; and \u2018all such goods shall "
           "be held to be insured\u2026 as Stock\u2019. No wording prevents merchandise cover.",
   location="Section 2 \u2013 Property Insured; Stock definition; Exhibits.",
   action="No change \u2014 merchandise held for sale is already within \u201cStock\u201d.",
   status="Confirmed \u2013 no change"),
 dict(id="A3", title="Data recovery from old Section 4",
   finding="PRESERVED \u2014 nothing lost. Old Section 4 (Information Technology) carried the data-recovery "
           "treatment as: a \u2018Breakdown\u2019 definition, a \u2018Data Carrying Materials\u2019 definition, an insured "
           "event covering Breakdown, and a basis of settlement reading \u2018replacement of Data Carrying "
           "Materials together with reinstatement of data contained thereon; whichever is the lesser to "
           "achieve compatibility\u2026\u2019. ALL of this survived into the current wording \u2014 the identical "
           "definition, insured event and basis-of-settlement wording appears in Section 1 (Business \u2018All "
           "Risks\u2019) and again in Section 2 (Property & Equipment). Old Section 4 had NO standalone, separate "
           "GBP data-recovery sub-limit \u2014 data recovery was met within the IT-property sum insured (cost-based, "
           "\u2018whichever is the lesser\u2019). There is therefore no standalone sub-limit to reinstate.",
   location="Section 1 and Section 2 \u2013 \u2018Breakdown\u2019 / \u2018Data Carrying Materials\u2019 / basis of settlement.",
   action="No change \u2014 treatment preserved faithfully; nothing to reinstate (no duplicate created).",
   status="Confirmed \u2013 no change"),
 dict(id="A4", title="Touring / event money (Section 8) \u2014 restructured into two Schedule sub-limits",
   finding="GENUINE GAP \u2014 ADDED & RESTRUCTURED. Section 8 (Money) had Sub-Section 1 (Money) + Sub-Section 2 "
           "(Personal Assault) + a Loss of Keys extension only, with no money extension for touring or events. "
           "Two new Schedule-referenced money extensions have been added: (1) \u2018Money \u2013 Premises\u2019 and (2) "
           "\u2018Money \u2013 Touring, Festivals and Events\u2019. The touring/event extension amalgamates the Entertainment "
           "Elite event-money section (theft; safes/strongrooms/bags/containers; assault cover for clothing/"
           "personal effects/personal Money; and employee dishonesty discovered within 12 months) and adopts the "
           "\u20180523\u2019 (MIB) money enhancement that expressly recognises money \u2018at the Venue\u2019 and in transit to/from "
           "the Premises/Venue. No existing Money cover, condition or exclusion has been removed.",
   location="Section 8 \u2013 Money, Sub-Section 1, immediately after the \u2018Loss of Keys\u2019 extension (before the "
            "Sub-Section Exclusions).",
   action="ADDED as discrete tracked changes. BOTH sub-limits are SCHEDULE-REFERENCED (\u2018up to the sub-limit shown "
          "against this Extension in the Schedule\u2019), in line with the other Item coverages \u2014 the figures are chosen "
          "in the Schedule by underwriting. The attached entertainment competitor wordings (incl. Entertainment "
          "Elite) write Money on a Schedule/Item-driven basis, so no fixed market figure is invented.",
   status="ADDED (tracked) \u2013 two Schedule sub-limits (Premises; Touring/Festivals/Events); figures set in Schedule"),
 dict(id="A5", title="Employee definition \u2014 breadth vs Yutree & Tysers",
   finding="Multiple Employee definitions exist. The general \u2018Employee \u2013 applicable to Sections 1\u201311\u2019 "
           "definition is ALREADY at least as wide as Tysers and Yutree (it covers contract-of-service, "
           "labour-master / labour-only sub-contractors, hired/supplied persons, self-employed labour-only, "
           "deemed-employment persons, government/work-experience scheme participants, unpaid persons "
           "temporarily working, and drivers/operators of hired plant). The Section 14 (Management Liability) "
           "and Section 12 (Media) definitions are also broad. The OUTLIER is the Section 13 (Commercial Legal "
           "Expenses) definition: \u2018A worker who has or alleges they have entered into a contract of service "
           "with You\u2019 \u2014 narrower than Tysers (self-employed, hired/borrowed, work-experience) and Yutree "
           "(labour-only, self-employed, hired/borrowed, voluntary helper, work-experience, prospective "
           "employee).",
   location="Section 13 \u2013 Commercial Legal Expenses, \u2018Employee\u2019 definition.",
   action="BROADENED the Section 13 definition (discrete tracked change, old text deleted / new inserted) to be "
          "at least as wide as Tysers & Yutree and consistent with the general Sections 1\u201311 definition. "
          "Tysers (General Definitions, p.9) and Yutree (\u2018Employed person\u2019, p.88) verified from the attached "
          "wordings. The general S1\u201311, S12 and S14 definitions already meet/exceed the competitors \u2014 left "
          "unchanged for internal consistency.",
   status="BROADENED (tracked) \u2013 Section 13 only"),
 dict(id="A6", title="Cyber / Computer System definition consistency (S12 vs S15)",
   finding="CONFIRMED INCONSISTENCY. Three different \u2018Computer System\u2019 definitions exist: (1) the property "
           "Cyber-Exclusion endorsement near Section 1 (modern, broad LMA-style: \u2018any computer, hardware, "
           "software, communications system, electronic device\u2026 owned or operated by the Insured or any other "
           "party\u2019); (2) Section 12 (Media) \u2014 an older, web/comms-focused definition tied to the Insured\u2019s "
           "\u2018electronic communications system, world-wide web site, internet site\u2026\u2019 (the narrowest); and (3) "
           "Section 15 (CyberGuard) \u2014 a modern, broad definition. \u2018Virus\u2019 is defined in S12; \u2018Data\u2019 and the "
           "Cyber Act/Incident/Loss triggers are defined in the property endorsement; S15 carries its own broad "
           "cyber dictionary.",
   location="Section 12 \u2013 \u2018Computer System\u2019 definition.",
   action="ALIGNED \u2014 the Section 12 \u2018Computer System\u2019 definition has been replaced (discrete tracked change, "
          "old deleted / new inserted) with a broad definition consistent with Section 15 / the property "
          "endorsement, expressly stated to be construed consistently with Section 15. Virus (S12) and the cyber "
          "triggers were reviewed and are substantively consistent; no further change required. ALL SECTION 12 "
          "CHANGES REQUIRE LEGAL/UNDERWRITING SIGN-OFF.",
   status="ALIGNED (tracked) \u2013 SIGN-OFF (Section 12)"),
]

# ---------------------------------------------------------------------------
# PART B/C — granular gap analysis + sub-limit harmonisation
# Each gap: number, title, item, tmhcc, comp, action, location, wording, tracked,
#           priority, uw, signoff, status
# ---------------------------------------------------------------------------
GAPS = [
 dict(n=1, title="Distributors & Purchasers extension (Media Liability)",
   item="Extension of PI indemnity to purchasers/co-producers/licensees/distributors of the insured\u2019s media material.",
   tmhcc="No equivalent extension in Section 12.",
   comp="Tysers PI clause 8.7 extends indemnity to purchasers/co-producers/distributors of the insured\u2019s "
        "Media Material up to 5x the Limit of Indemnity in the aggregate (verified, Tysers p.57). Yutree/Liberty/"
        "Allianz/AXA XL: none.",
   action="ADD a Distributors & Purchasers extension capped at five (5) times the Indemnity Limit in the aggregate, "
          "with control-of-defence and claims-made/notification conditions.",
   location="Section 12 \u2013 Extensions, after \u2018Indemnity to Principals\u2019.",
   wording="The indemnity provided by Insuring Clause 1. (Indemnity) is extended to apply to any purchaser, "
           "co-producer, licensee or distributor of Media Material produced or supplied by the Insured, but only "
           "in respect of claims arising from such Media Material and only where the Insured is contractually "
           "obliged to provide such indemnity. The Insurer\u2019s total liability under this Extension shall not exceed "
           "five (5) times the Indemnity Limit in the aggregate during the Period of Insurance for all claims "
           "arising from each production of Media Material so purchased, co-produced, licensed or distributed. "
           "Cover under this Extension is conditional upon the Insurer retaining the right to conduct the defence "
           "and settlement of any such claim, and upon any claim being first made against, and notified to the "
           "Insurer by, the Insured during the Period of Insurance.",
   tracked="Yes", priority="Medium", uw="Medium \u2014 aggregate exposure 5x limit; control via 5x cap, control-of-"
   "defence and claims-made notification.", signoff="Yes (Section 12)", status="Implemented (tracked)"),
 dict(n=2, title="Worldwide / USA-Canada territory option (Media Liability)",
   item="Schedule-selectable worldwide (and separately USA/Canada) territory & jurisdiction for Section 12.",
   tmhcc="Section 12 is governed by the Schedule Geographical Limits and excludes claims brought, or whose "
         "governing law is contended to be, outside the Jurisdiction (default worldwide ex-US/Canada).",
   comp="Tysers PI/E&O is worldwide with no jurisdiction exclusion (verified). Yutree restricts US/Canada.",
   action="ADD an optional, schedule-selectable Worldwide Territory & Jurisdiction extension, with USA/Canada as a "
          "separate selectable; default position unchanged.",
   location="Section 12 \u2013 Extensions, after \u2018Distributors and Purchasers\u2019.",
   wording="This Optional Extension applies only if stated as operative in the Schedule. Where stated as operative, "
           "the Geographical Limits applicable to this Section are amended to anywhere in the world and the "
           "Jurisdiction applicable to this Section is amended to worldwide, and the exclusions of claims brought, "
           "or in which the governing law is contended to be, outside the Jurisdiction shall not apply. Cover in "
           "respect of claims brought in, or determined under the laws of, the United States of America or Canada "
           "(or any territory or protectorate thereof) applies only if \u201cUSA/Canada Jurisdiction\u201d is additionally "
           "stated as operative in the Schedule.",
   tracked="Yes", priority="High", uw="High if US/Canada selected \u2014 price/sub-limit/higher excess; keep "
   "ex-US/Canada as default; confirm reinsurance treaty territory.", signoff="Yes (Section 12)",
   status="Implemented (tracked) \u2013 optional, default unchanged"),
 dict(n=3, title="Journalistic source-protection costs (Media Liability)",
   item="Legal costs to oppose a subpoena/court order requiring disclosure of a confidential source.",
   tmhcc="Not provided.",
   comp="Tysers PI clause 8.13 funds legal costs to challenge a subpoena requiring disclosure of a source "
        "(verified). Yutree/others: none.",
   action="ADD a sub-limited source-protection costs extension (counsel\u2019s opinion / reasonable-grounds test; "
          "insurer consent).",
   location="Section 12 \u2013 additional covers, after \u2018Costs for Prosecuting Infringement of the Insured\u2019s IP\u2019.",
   wording="Up to the sub-limit stated in the Schedule against this Extension, for the reasonable legal costs and "
           "expenses incurred by the Insured, with the Insurer\u2019s prior written consent, in opposing or responding "
           "to any subpoena, court order or other legal compulsion requiring the Insured to disclose the identity of "
           "a confidential journalistic source, where such disclosure arises from the Insured\u2019s Media Business "
           "Services. The Insurer will only provide such cover where, in the opinion of counsel, there are reasonable "
           "grounds to oppose disclosure. This cover forms part of and does not increase the Indemnity Limit.",
   tracked="Yes", priority="Medium", uw="Low \u2014 small sub-limit; consent and prospects conditions.",
   signoff="Yes (Section 12)", status="Implemented (tracked)"),
 dict(n=4, title="Representation costs at investigations/inquiries (Media Liability)",
   item="Costs of attendance/representation at official examinations, investigations or inquiries.",
   tmhcc="Provided only via Data-Protection Defence Costs; otherwise absent in S12.",
   comp="Tysers PI clause 8.15 funds representation at official examinations/inquiries up to GBP 25,000 in the "
        "aggregate (verified, Tysers p.58).",
   action="ADD a GBP 25,000 representation-costs extension (matching the evidenced Tysers figure).",
   location="Section 12 \u2013 additional covers, after \u2018Costs for Prosecuting Infringement of the Insured\u2019s IP\u2019.",
   wording="Up to a maximum of GBP 25,000 (twenty-five thousand pounds sterling) in the aggregate in the Period of "
           "Insurance, for the reasonable costs and expenses incurred by the Insured, with the Insurer\u2019s prior "
           "written consent, in respect of attendance at or representation before any official examination, "
           "investigation, inquiry or other proceeding arising from the Insured\u2019s Media Business Services and which "
           "is likely to give rise to a claim under Insuring Clause 1. (Indemnity). This cover forms part of and does "
           "not increase the Indemnity Limit.",
   tracked="Yes", priority="Medium", uw="Low \u2014 GBP 25k sub-limit (market-matched to Tysers).",
   signoff="Yes (Section 12)", status="Implemented (tracked)"),
 dict(n=5, title="Criminal / regulatory defence costs (Media Liability)",
   item="Defence of criminal/regulatory proceedings arising from media activities.",
   tmhcc="Section 12 funds only Data-Protection defence costs (GBP 250k). Broader criminal/regulatory defence sits "
         "in Section 13 (Commercial Legal Expenses) and Section 14 (Management Liability).",
   comp="Tysers funds statutory defence (Bribery/Corporate Manslaughter/H&S/CDM) up to GBP 1,000,000 (verified). "
        "Yutree funds criminal-prosecution defence up to GBP 250,000 (verified).",
   action="ADD an express cross-reference to Sections 13/14 plus a modest schedule-referenced contribution within "
          "S12 (excluding fines/penalties and post-guilt costs).",
   location="Section 12 \u2013 additional covers, after \u2018Costs for Prosecuting Infringement of the Insured\u2019s IP\u2019.",
   wording="In addition to the Data Protection Defence Costs provided above, the Insured is reminded that defence of "
           "criminal and regulatory proceedings may also be available under Section 13 (Commercial Legal Expenses) "
           "and Section 14 (Management Liability)\u2026 The Insurer will further contribute, up to the sub-limit stated "
           "in the Schedule against this Extension\u2026 towards the reasonable defence costs of any criminal or "
           "regulatory proceeding\u2026 save to the extent that cover is provided under Section 13 or Section 14\u2026 "
           "excludes fines, penalties and any costs incurred after a plea or finding of guilt.",
   tracked="Yes", priority="Medium-High", uw="Low-Medium \u2014 contribution capped by Schedule; primarily a "
   "clarifying cross-reference to S13/S14.", signoff="Yes (Section 12)", status="Implemented (tracked)"),
 dict(n=6, title="King\u2019s Counsel dispute-resolution clause (Media Liability)",
   item="Binding KC determination on defence/settlement disputes.",
   tmhcc="Relies on a general CEDR mediation clause (\u2018in respect of Section 12 only\u2019).",
   comp="Yutree PI-Media includes a clear King\u2019s Counsel determination clause binding both parties (verified, "
        "Yutree p.134).",
   action="ADD a KC-determination clause to the Section 12 dispute provisions.",
   location="Section 12 dispute clause (\u2018In respect of Section 12 only any dispute\u2026\u2019).",
   wording="In respect of Section 12 (Media Liability) only, if the Insured and the Insurer disagree as to whether or "
           "how any claim should be defended, settled or pursued, either party may require the matter to be referred "
           "to a King\u2019s Counsel of the English Bar to be mutually agreed\u2026 The opinion of such King\u2019s Counsel\u2026 "
           "shall be binding on both parties\u2026 costs\u2026 allocated\u2026 on a fair and equitable basis.",
   tracked="Yes", priority="Low-Medium", uw="Low \u2014 procedural; reduces coverage-dispute friction.",
   signoff="Yes (Section 12)", status="Implemented (tracked)"),
 dict(n=7, title="Pollution negligent-advice write-back (Media Liability PI)",
   item="Narrow PI write-back for liability arising solely from negligent advice (not contamination itself).",
   tmhcc="Section 12 excludes seepage/Pollution/contamination outright.",
   comp="Yutree grants a limited pollution write-back for the insured\u2019s own negligent act/error/omission (verified). "
        "Tysers excludes pollution from PI.",
   action="ADD a narrow write-back to the S12 Seepage & Pollution exclusion, ring-fenced to negligent advice and "
          "excluding bodily injury, property damage and clean-up/remediation; schedule sub-limit.",
   location="Section 12 \u2013 Exclusions, after \u2018Seepage and Pollution\u2019.",
   wording="provided that this Exclusion shall not apply to any claim arising solely from a negligent act, negligent "
           "error or negligent omission in the provision of the Insured\u2019s Media Business Services (and not from any "
           "seepage, Pollution or contamination caused by the Insured\u2019s own operations, premises or activities), and "
           "provided further that this write-back shall not extend to any claim for Bodily Injury, property damage, or "
           "the costs of removing, nullifying, cleaning up or remediating any pollutant\u2026 sub-limit stated in the "
           "Schedule\u2026",
   tracked="Yes", priority="Medium", uw="Medium \u2014 ring-fenced to negligent advice; BI/PD/clean-up excluded; "
   "schedule sub-limit.", signoff="Yes (Section 12)", status="Implemented (tracked)"),
 dict(n=8, title="Patent infringement (Media Liability IP)",
   item="Cover for infringement of patents within IP cover.",
   tmhcc="Section 12 excludes patents (deliberate restriction).",
   comp="Tysers PI clause 8.9 covers patent infringement within IP (verified). Yutree also excludes patents.",
   action="LEAVE EXCLUDED \u2014 patents are difficult to underwrite and the exclusion is a disciplined, defensible "
          "restriction (Yutree agrees). At most a narrow defence-costs-only write-back could be considered later.",
   location="Section 12 \u2013 Exclusions, \u2018Patents\u2019.",
   wording="(No change applied.) If ever required: a defence-costs-only contribution, sub-limited and excluding "
           "damages/accounts of profit, could be drafted \u2014 not recommended at present.",
   tracked="No", priority="Low", uw="High if broadened \u2014 patent damages are high-severity.",
   signoff="Yes (if ever adopted)", status="PARKED \u2013 not implemented (deliberate restriction)"),
 dict(n=9, title="Asbestos professional-duty write-back (Media Liability PI)",
   item="PI write-back for negligent advice touching asbestos (not the contamination).",
   tmhcc="Section 12 excludes asbestos outright.",
   comp="Tysers PI grants an asbestos professional-duty write-back up to GBP 1,000,000 (ex-BI) (verified).",
   action="PARK \u2014 a narrow negligent-advice write-back is possible but requires careful drafting (exclude BI and "
          "contamination). Provided for consideration, not applied.",
   location="Section 12 \u2013 Exclusions, \u2018Asbestos\u2019.",
   wording="provided that this Exclusion shall not apply to liability arising solely from a negligent act, error or "
           "omission in professional advice or specification given in the course of the Insured\u2019s Media Business "
           "Services, excluding any claim for Bodily Injury and any costs of removal, remediation or clean-up; "
           "sub-limit per the Schedule.",
   tracked="No", priority="Medium", uw="Medium \u2014 ring-fence tightly; exclude BI and contamination.",
   signoff="Yes (Section 12)", status="PARKED \u2013 for consideration / sign-off"),
 dict(n=10, title="Personal Accident & Business Travel",
   item="Standalone PA / business-travel cover.",
   tmhcc="No standalone PA / business-travel section.",
   comp="Tysers has an extensive PA & Business Travel section; Yutree covers PA assault.",
   action="EXCLUDED FROM THIS EXERCISE by instruction \u2014 Personal Accident and Travel are NOT to be added. Note: "
          "Personal Assault under the Money section (Section 8, Sub-Section 2) is DISTINCT from Personal Accident and "
          "is retained unchanged.",
   location="(Not applicable.)",
   wording="(No wording \u2014 deliberately excluded.)",
   tracked="No", priority="n/a", uw="n/a", signoff="n/a",
   status="EXCLUDED by instruction (PA & Travel)"),
 dict(n=11, title="Increased Cost of Working / Book Debts (Business Interruption)",
   item="Named ICOW/AICOW and Book Debts heads in BI.",
   tmhcc="Section 3 already covers Increase in Cost of Working / Additional ICOW and Accounts Receivable, now "
         "expressly labelled \u2018Accounts Receivable (Book Debts)\u2019.",
   comp="Allianz splits ICOW and Book Debts into discrete sections (presentational).",
   action="No change \u2014 already covered and named. (Book-Debts label confirmed.)",
   location="Section 3 \u2013 Business Interruption.",
   wording="(No change.)", tracked="No", priority="Low", uw="Nil \u2014 clarification only.",
   signoff="No", status="Already met \u2013 no change"),
 dict(n=12, title="Computer / IT breakdown (first-party)",
   item="Named computer/IT breakdown cover.",
   tmhcc="\u2018Breakdown\u2019 is defined and IT-Property Breakdown is covered within Sections 1 and 2 (carried across "
         "from old Section 4).",
   comp="Yutree offers a standalone Computer Breakdown section.",
   action="No change \u2014 breakdown cover is present and explicit within S1/S2; a standalone section is not required.",
   location="Sections 1 & 2 \u2013 Breakdown.",
   wording="(No change.)", tracked="No", priority="Low", uw="Nil.", signoff="No",
   status="Already met \u2013 no change"),
]

# ---------------------------------------------------------------------------
# PART C — sub-limit harmonisation table
# rows: (extension, old TMHCC limit, new TMHCC limit, competitor source + limit, signoff)
# ---------------------------------------------------------------------------
SUBLIMITS = [
 ("Media Liability \u2013 Virus transmission", "GBP 500,000", "GBP 500,000 (no change)",
  "Tysers GBP 250,000 (8.16). TMHCC already higher.", "No \u2014 TMHCC already market-highest"),
 ("Media Liability \u2013 Reputation Management", "GBP 250,000", "GBP 250,000 (no change)",
  "Yutree GBP 250,000 (verified). Match.", "No \u2014 matches market-highest"),
 ("Media Liability \u2013 Withdrawal of Content", "GBP 250,000", "GBP 250,000 (no change)",
  "Yutree GBP 250,000 (withdrawal/alteration). Match.", "No \u2014 matches market-highest"),
 ("Media Liability \u2013 Data-Protection Defence Costs", "GBP 250,000", "GBP 250,000 (no change)",
  "Yutree EXCLUDES DP in PI; Tysers \u2014. TMHCC already broader.", "No \u2014 TMHCC strength"),
 ("Media Liability \u2013 Court Attendance (per day)", "GBP 500 / GBP 250", "GBP 500 / GBP 250 (no change)",
  "Tysers GBP 500/250 with GBP 25k aggregate (8.4); Yutree GBP 25k aggregate. Per-day matches; competitor "
  "ADDS an aggregate CAP (narrower). TMHCC not lowered.", "No \u2014 do not add a cap"),
 ("Media Liability \u2013 Pursue insured\u2019s own IP", "GBP 25,000", "GBP 25,000 (no change)",
  "No competitor equivalent figure. Cannot determine.", "No \u2014 cannot determine"),
 ("Media Liability \u2013 Representation costs (NEW)", "\u2014 (new)", "GBP 25,000",
  "Tysers GBP 25,000 (8.15). New cover set to evidenced market figure.", "Yes (Section 12)"),
 ("Media Liability \u2013 Distributors & Purchasers (NEW)", "\u2014 (new)", "5\u00d7 Indemnity Limit (aggregate)",
  "Tysers 5\u00d7 limit (8.7). New cover set to evidenced market structure.", "Yes (Section 12)"),
 ("Media Liability \u2013 Loss of Documents", "Per Schedule (Indemnity Limit)", "Per Schedule (no change)",
  "Tysers GBP 1,000,000 (8.10); Yutree = limit. TMHCC schedule-driven (broker-set, can be \u2265).",
  "No \u2014 schedule-driven"),
 ("Section 8 \u2013 Money \u2013 Premises (NEW)", "\u2014 (new)", "Per Schedule",
  "Schedule/Item-driven across the market (Entertainment Elite, Liberty, Allianz). Figure set in Schedule.",
  "Underwriting to set figure"),
 ("Section 8 \u2013 Money \u2013 Touring, Festivals & Events (NEW)", "\u2014 (new)", "Per Schedule",
  "Amalgamates Entertainment Elite event-money (assault + employee dishonesty GBP 25k) + 0523 \u2018Venue\u2019; "
  "Schedule/Item-driven, so no fixed market figure invented.",
  "Underwriting to set figure"),
 ("Section 2 \u2013 Artists\u2019 Equipment", "GBP 20,000", "GBP 20,000 (no change)",
  "No competitor \u2018artists equipment\u2019 figure; Yutree portable electronic GBP 500 / driver\u2019s effects GBP 1,500 "
  "are lower/different. TMHCC not lowered.", "No \u2014 cannot determine a higher figure"),
 ("Section 2 \u2013 General Average delay", "GBP 10,000", "GBP 10,000 (no change)",
  "No competitor equivalent. Cannot determine.", "No \u2014 cannot determine"),
 ("Section 2 \u2013 Mechanical/Electrical Breakdown (optional)", "Within sum insured (Per Schedule)",
  "Per Schedule (no change)", "Yutree M&E breakdown GBP 30,000 (verified); TMHCC schedule-driven (typically \u2265).",
  "No \u2014 schedule-driven"),
 ("Section 11 \u2013 Production Indemnity agency / talent costs", "GBP 30,000", "GBP 30,000 (no change)",
  "No like-for-like competitor figure (Tysers/Yutree production indemnity schedule-driven). Cannot determine.",
  "No \u2014 cannot determine"),
 ("Sections 13/14/15 sub-limits (legal/D&O/cyber)", "Various (per wording/Schedule)", "No change",
  "No competitor wording offers Legal Expenses, Management Liability or standalone Cyber \u2014 nothing to benchmark.",
  "No \u2014 TMHCC-only sections"),
]

# ---------------------------------------------------------------------------
# CHANGE LOG — the 10 discrete tracked changes (for QA + Summary of Changes)
# ---------------------------------------------------------------------------
CHANGE_LOG = [
 ("A4", "Section 8 \u2013 Money (Sub-Section 1)", "New \u2013 two Schedule sub-limits: \u2018Money \u2013 Premises\u2019 and \u2018Money \u2013 Touring, Festivals and Events\u2019",
  "(none \u2014 new)", "Schedule-referenced premises money + touring/festival/event money (amalgamates Entertainment Elite event-money + 0523 \u2018Venue\u2019); no existing cover/exclusion removed", "No"),
 ("A5", "Section 13 \u2013 Commercial Legal Expenses", "Definition amendment \u2013 \u2018Employee\u2019",
  "\u2018A worker who has or alleges they have entered into a contract of service with You.\u2019",
  "Broadened to include labour-only, self-employed, hired/borrowed, voluntary, work-experience, secondee, "
  "student and prospective employees \u2014 at least as wide as Tysers & Yutree.", "No"),
 ("A6", "Section 12 \u2013 Media Liability", "Definition amendment \u2013 \u2018Computer System\u2019",
  "Older web/comms-focused definition.",
  "Replaced with a broad definition aligned to Section 15 / property endorsement.", "Yes"),
 ("B1", "Section 12 \u2013 Media Liability (Extensions)", "New cover \u2013 Distributors & Purchasers",
  "(none \u2014 new)", "5\u00d7 Indemnity Limit aggregate; control-of-defence + claims-made conditions.", "Yes"),
 ("B2", "Section 12 \u2013 Media Liability (additional covers)", "New cover \u2013 Representation Costs at Investigations/Inquiries",
  "(none \u2014 new)", "GBP 25,000 aggregate (market-matched to Tysers 8.15).", "Yes"),
 ("B3", "Section 12 \u2013 Media Liability (additional covers)", "New cover \u2013 Journalistic Source-Protection Costs",
  "(none \u2014 new)", "Schedule sub-limit; counsel\u2019s reasonable-grounds test; insurer consent.", "Yes"),
 ("B5", "Section 12 \u2013 Media Liability (additional covers)", "Clarification + contribution \u2013 Criminal & Regulatory Defence Costs",
  "(none \u2014 new)", "Cross-reference to S13/S14 + schedule-referenced contribution (ex fines/penalties/post-guilt).", "Yes"),
 ("B6", "Section 12 \u2013 Media Liability (Extensions)", "New optional \u2013 Worldwide Territory & Jurisdiction",
  "(none \u2014 new)", "Schedule-selectable worldwide; USA/Canada separately selectable; default unchanged.", "Yes"),
 ("B7", "Section 12 \u2013 Media Liability (dispute clause)", "New clause \u2013 King\u2019s Counsel determination",
  "(none \u2014 new)", "Binding KC determination on defence/settlement disputes (Yutree-style).", "Yes"),
 ("B8", "Section 12 \u2013 Media Liability (Exclusions)", "Write-back \u2013 Seepage & Pollution (negligent advice)",
  "(none \u2014 new proviso)", "Narrow negligent-advice write-back; BI/PD/clean-up excluded; schedule sub-limit.", "Yes"),
]

# ---------------------------------------------------------------------------
# SECTION 12 — sign-off list
# ---------------------------------------------------------------------------
S12_SIGNOFF = [
 ("Computer System definition alignment (A6)", "Definition amendment", "Align S12 to the broad S15 definition."),
 ("Distributors & Purchasers (B1)", "New cover", "5\u00d7 Indemnity Limit aggregate exposure."),
 ("Worldwide / USA-Canada territory option (B5/Gap 2)", "Schedule-selectable option", "Material territory/jurisdiction broadening if selected."),
 ("Journalistic Source-Protection Costs (B3)", "New cover", "Small sub-limit; editorial/news relevance."),
 ("Representation Costs at Investigations/Inquiries (B2)", "New cover", "GBP 25k market-matched."),
 ("Criminal & Regulatory Defence Costs (B4)", "Clarification + contribution", "Cross-ref S13/S14; capped contribution."),
 ("King\u2019s Counsel determination clause (B6)", "Condition amendment", "Procedural dispute-resolution upgrade."),
 ("Seepage & Pollution negligent-advice write-back (B7)", "Exclusion write-back", "Ring-fenced to negligent advice."),
]

# ---------------------------------------------------------------------------
# Reviewer notes / UNCONFIRMED / cannot-determine
# ---------------------------------------------------------------------------
REVIEWER_NOTES = [
 "ALL Section 12 (Media Liability) amendments are applied as discrete tracked changes but REQUIRE legal/"
 "underwriting sign-off before acceptance (A6, B1\u2013B7).",
 "A4 Money restructure: split into two Schedule-referenced sub-limits \u2014 \u2018Money \u2013 Premises\u2019 and \u2018Money \u2013 "
 "Touring, Festivals and Events\u2019 \u2014 in line with the other Item coverages (figures chosen in the Schedule). "
 "The touring/event extension amalgamates the Entertainment Elite event-money section and the 0523 (MIB) "
 "\u2018Venue\u2019 money enhancement. No existing Money cover, condition or exclusion was removed. A specific "
 "market-highest figure CANNOT BE DETERMINED (competitor money is Schedule/Item-driven); underwriting sets it.",
 "Entertainment Elite (v3.2) has been added as a SIXTH competitor across the comparison and is the source of "
 "the amalgamated event-money cover. Liberty and Allianz uploads were byte-identical to the repo copies and "
 "were ignored as duplicates.",
 "From the TMHCC 0523 (MIB) variant only the Money enhancement was harvested (the \u2018Venue\u2019 money situation); "
 "no other cover was taken from 0523.",
 "PART C sub-limit harmonisation: TMHCC already meets or exceeds every evidenced competitor numeric sub-limit, "
 "or is schedule-driven (broker-set). No existing TMHCC sub-limit was raised because no attached competitor "
 "figure is demonstrably higher for the same benefit; none was invented and none was lowered.",
 "A5 Employee: Tysers (p.9) and Yutree (\u2018Employed person\u2019, p.88) definitions verified from the attached "
 "wordings. The general Sections 1\u201311, S12 and S14 definitions already meet/exceed them; only the narrow "
 "Section 13 definition was broadened.",
 "Patent infringement (Gap 8) deliberately left excluded; Asbestos negligent-advice write-back (Gap 9) parked "
 "for consideration with proposed wording \u2014 neither applied.",
 "Personal Accident and Travel deliberately NOT added (per instruction). Personal Assault under the Money "
 "section (S8, Sub-Section 2) is distinct and retained unchanged.",
 "\u2018Market-leading\u2019/\u2018highest-in-market\u2019 statements are supported by the six attached competitor wordings. "
 "Items that could not be traced to an attached wording are labelled CANNOT-DETERMINE / UNCONFIRMED above.",
]
