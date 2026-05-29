"""Build the FINAL Summary of Cover (.docx) from the branded template.
Content is derived strictly from the NEW 0526 wording. High-level guide only."""
from docx_brand import *

doc = load_template()
clear_body_after_cover(doc, keep_para_index=5)

# ---------- Title / intro ----------
add_para(doc, "WORDING: TMHCC Media Combined 0526", size=12, bold=True, color=BLUE, space_after=2)
add_para(doc, "SUMMARY OF COVER", size=11, bold=True, color=GOLD, space_after=6)

add_callout(
    doc,
    "This Summary of Cover is intended as a high-level guide only. It does not replace the policy "
    "wording, schedule, endorsements or any specific terms, conditions, exclusions, limits or excesses "
    "that apply. Cover is provided only for those Sections shown as operative in the Schedule and is "
    "subject in all respects to the full policy wording. You should read the policy, Schedule and any "
    "endorsements for full details of the terms and conditions. This Policy is a commercial insurance "
    "product designed for business customers and is not suitable for consumers.",
    bold_lead="Important notice / basis of this summary.  ",
)

# ---------- Who it is for / structure ----------
add_h1(doc, "WHO THIS POLICY IS DESIGNED FOR")
add_para(doc, "The Media and Music Combined Insurance Policy 0526 is a non-consumer commercial package "
              "designed for businesses operating in the media, music, production, events and creative "
              "sectors (and associated commercial activities). It combines property, business "
              "interruption, liability, production, media and management/cyber covers in one policy, "
              "underwritten by Tokio Marine HCC (with Section 13 underwritten by ARAG and Section 15 "
              "provided under the CyberGuard\u2122 wording).")
add_h1(doc, "HOW THIS POLICY IS STRUCTURED")
add_para(doc, "The policy is made up of 15 Sections. General Policy Definitions, Conditions and "
              "Exclusions apply across the policy; each Section also has its own specialist definitions, "
              "extensions, conditions, exclusions and limits. Only the Sections shown as operative in the "
              "Schedule are in force, and all cover is subject to the sums insured, limits, sub-limits "
              "and excesses stated in the Schedule.")

# ---------- Main covers at a glance ----------
add_h1(doc, "MAIN COVERS AT A GLANCE")
add_table(
    doc,
    ["Section", "Cover provided", "Basis"],
    [
        ["1  Business \u201cAll Risks\u201d (Premises)", "Property at the premises, incl. IT equipment & breakdown", "Loss/Damage"],
        ["2  Property & Equipment \u201cAll Risks\u201d", "Technical/production equipment & specified articles, worldwide", "Loss/Damage"],
        ["3  Business Interruption \u201cAll Risks\u201d", "Loss of income/increased cost of working after an Incident", "Loss/Damage"],
        ["4  Terrorism", "Property damage & BI caused by Terrorism (if operative)", "Loss/Damage"],
        ["5  Employers\u2019 Liability", "Injury/disease to employees", "Liability"],
        ["6  Public Liability", "Injury/damage to third parties", "Liability"],
        ["7  Products Liability", "Injury/damage caused by products", "Liability"],
        ["8  Money", "Money loss & personal assault benefits", "Loss/Benefit"],
        ["9  Goods in Transit", "Damage to goods in transit", "Loss/Damage"],
        ["10  Loss of Licence", "Loss of trade value/profit on loss of licence", "Loss"],
        ["11  Production Indemnity \u201cAll Risks\u201d", "Production cost loss / interruption / abandonment", "Loss/Damage"],
        ["12  Media Liability", "Defamation, IP, privacy & media liability", "Claims-made"],
        ["13  Commercial Legal Expenses", "Legal costs for insured events (ARAG)", "Claims-made"],
        ["14  Management Liability", "Directors\u2019, officers\u2019 & corporate liability", "Claims-made"],
        ["15  CyberGuard\u2122 Cyber Liability", "First & third-party cyber cover", "Claims-made/Discovered"],
    ],
    widths=[2400, 5400, 1900],
)

# ---------- Section summaries ----------
def section(title, desc, features, exclusions, conditions=None, limits=None, optional=None):
    add_h1(doc, title)
    add_para(doc, desc, space_after=4)
    add_h2(doc, "What is covered \u2013 key features")
    for f in features:
        add_bullet(doc, f)
    if optional:
        add_h2(doc, "Optional cover (if shown in the Schedule)")
        for o in optional:
            add_bullet(doc, o)
    if conditions:
        add_h2(doc, "Key conditions")
        for c in conditions:
            add_bullet(doc, c)
    add_h2(doc, "Key limitations & exclusions")
    for e in exclusions:
        add_bullet(doc, e)
    if limits:
        add_para(doc, "Limits / sub-limits: " + limits, size=9, italic=True, color=GREY, space_before=2)

section(
    "SECTION 1 \u2013 BUSINESS \u201cALL RISKS\u201d (PREMISES RISK ONLY)",
    "Accidental physical loss of or damage to Buildings, Contents, Stock, Rent and Information "
    "Technology Property at the Premises on an \u201call risks\u201d basis. Information Technology equipment "
    "and Breakdown cover (previously a standalone Information Technology section in the 0223C wording) "
    "is now incorporated within this Section.",
    [
        "Day One Uplift and Capital Additions / Acquisitions",
        "Customers\u2019 Goods; Removal of Debris and Fire Extinguishing Expenses",
        "Trace and Access; Drain Clearance; Replacement of Locks; Theft Damage to Buildings",
        "Temporary Removal and Transit; Exhibitions; Leased and Rented Premises",
        "Architects\u2019, Surveyors\u2019 and Engineers\u2019 Fees; Inadvertent Omission to Insure; EU & Public Authorities",
        "Information Technology Property Breakdown plus Accidental Discharge, Additional Rental Charge, Expediting Costs, Incompatibility and Involuntary Betterment",
    ],
    [
        "Excluded Causes and Excluded Property",
        "Wear, tear, gradual deterioration and similar gradually-operating causes",
        "Theft from unoccupied/unattended buildings and certain outdoor areas (restricted)",
        "Cover may be reduced or cease where the premises are Unoccupied",
        "Underinsurance: cover is subject to Average",
    ],
    conditions=[
        "Minimum Security Requirements, Fire Protection & Detection, Security Devices and Unoccupancy "
        "conditions apply (some are conditions precedent to liability)",
    ],
    limits="As stated in the Schedule; settlement on Reinstatement or Indemnity basis as specified.",
)

section(
    "SECTION 2 \u2013 PROPERTY & EQUIPMENT \u201cALL RISKS\u201d",
    "\u201cAll risks\u201d cover for Technical Equipment (musical instruments, sound, lighting, staging, "
    "projection, computer/IT equipment, audio-visual and broadcast equipment), Props, Sets and "
    "Wardrobe, stock/merchandise and Specified Articles within the Geographical Limits. This Section "
    "has been renamed and expanded (formerly \u201cProduction Property\u201d) to absorb production property "
    "and technical / IT equipment.",
    [
        "Technical Equipment and Artists\u2019 Equipment (worldwide Geographical Limits)",
        "Transit and Exhibition extensions; Automatic Reinstatement",
        "Loan Property; Marine and Declared General Average; Customs Duty",
        "Brands and Labels; Involuntary Betterment",
        "Agreed Value, Reinstatement or Indemnity basis as shown in the Schedule",
    ],
    [
        "Exclusions applicable to Technical Equipment, Props/Sets/Wardrobe and Specified Articles",
        "Property left in an unattended vehicle (subject to conditions)",
        "Valuables (jewellery, furs, precious metals/stones, works of art) over GBP 10,000 unless declared and accepted",
    ],
    optional=[
        "Hired-in Property / Hired-out Property",
        "Technical Equipment Hired In / Hired Out",
        "Mechanical and Electrical Breakdown",
    ],
    limits="Artists\u2019 Technical Equipment GBP 20,000 any one occurrence and in the aggregate; "
           "Declared General Average GBP 10,000 aggregate (Insured bears first 10%, min GBP 250); "
           "other limits as stated in the Schedule.",
)

section(
    "SECTION 3 \u2013 BUSINESS INTERRUPTION \u201cALL RISKS\u201d",
    "Loss of gross profit, gross revenue, rent receivable and increased cost of working following "
    "interruption of the Business by an insured Incident (i.e. damage covered under the property "
    "Sections).",
    [
        "Denial of Access; Customers and Suppliers; Public Utilities",
        "Specified Illness and Miscellaneous Contingencies",
        "Alternative Trading; Automatic Reinstatement; Payments on Account",
        "Exhibition Loss of Expenses and Exhibition Sites; Professional Accountants",
    ],
    [
        "Loss not resulting from an insured Incident is not covered",
        "Adjustments for trends and other circumstances apply",
        "Cover limited to the Indemnity Period stated in the Schedule",
    ],
    optional=[
        "Contract Sites; Denial of Access (Non-Damage); Goods in Transit",
        "Public Utilities \u2013 Terminal Ends; Flexible Business Interruption Limit",
    ],
    limits="Gross profit/revenue sums insured, Indemnity Period and sub-limits as stated in the Schedule.",
)

section(
    "SECTION 4 \u2013 TERRORISM",
    "Loss of or damage to Property Insured, and resulting Business Interruption, caused by an act of "
    "Terrorism within the Territorial Limits. Operative only if shown in the Schedule.",
    [
        "Aligns with the Property and Business Interruption Sections",
        "Automatic Reinstatement",
    ],
    [
        "Nuclear installations and reactors",
        "Cyber / Virus and Denial of Service attack",
        "War and related perils",
        "Burden of proof that loss is not excluded rests with the Insured",
    ],
    limits="As stated in the Schedule.",
)

section(
    "SECTION 5 \u2013 EMPLOYERS\u2019 LIABILITY",
    "The Insured\u2019s legal liability for bodily injury or disease sustained by Employees arising out of "
    "and in the course of the Business.",
    [
        "Indemnity to Principals; Additional Insured Parties",
        "Criminal Prosecution Defence Costs; Data Protection Act cover",
        "Unsatisfied Court Judgments",
        "Health & Safety / Corporate Manslaughter defence costs (sub-limited)",
    ],
    [
        "Liability requiring compulsory motor insurance; offshore work",
        "Workers\u2019 Compensation; Asbestos (limited fire/explosion write-back)",
        "Terrorism",
    ],
    limits="Limit of Indemnity as stated in the Schedule (minimum as required by the Employers\u2019 "
           "Liability (Compulsory Insurance) Act 1969). Criminal Prosecution Defence Costs GBP 250,000 "
           "(GBP 5,000,000 for manslaughter); certain extensions limited to GBP 250,000; "
           "asbestos fire/explosion write-back GBP 500,000.",
)

section(
    "SECTION 6 \u2013 PUBLIC LIABILITY",
    "The Insured\u2019s legal liability to pay Compensation for accidental bodily injury to third parties "
    "and accidental loss of or damage to third-party property arising from the Business.",
    [
        "Indemnity to Principals; Additional Insured Parties; Cross Liabilities",
        "Defective Premises Act 1972; Legionella Liability",
        "Custody or Control; Data Protection Act; Overseas Personal Liability",
        "Motor Vehicle Contingent Liability; Criminal Prosecution Defence Costs",
    ],
    [
        "Abuse; Advice and Professional Negligence; Products; Contractual Liability",
        "Asbestos; Pollution; Defective Workmanship; Medical Malpractice",
        "Vehicles, Vessels or Craft; Hazardous Activities",
        "Worldwide jurisdiction unless agreed",
    ],
    limits="Limit of Indemnity as stated in the Schedule. Custody/Control extension GBP 250,000 "
           "(GBP 2,500 excess each claim); other extensions sub-limited as stated.",
)

section(
    "SECTION 7 \u2013 PRODUCTS LIABILITY",
    "The Insured\u2019s legal liability to pay Compensation for accidental bodily injury or property "
    "damage caused by products sold, supplied or distributed in the course of the Business.",
    [
        "Criminal Prosecution Defence Costs; Cross Liabilities",
    ],
    [
        "Damage to Products Supplied; Defective Workmanship; North American Exports",
        "Asbestos; Pollution; Aircraft / Watercraft Products; Food and Drink",
        "Advice and Professional Negligence; Contractual Liability",
        "Worldwide jurisdiction unless agreed",
    ],
    limits="Limit of Indemnity as stated in the Schedule; asbestos fire/explosion write-back GBP 500,000.",
)

section(
    "SECTION 8 \u2013 MONEY",
    "Loss of Money in transit, on the premises and in safes or strongrooms (Sub-Section 1), together "
    "with Personal Assault benefits for insured persons following robbery or attempted robbery "
    "(Sub-Section 2).",
    [
        "Loss of Keys",
        "Personal Assault benefits \u2013 death and disablement",
    ],
    [
        "Shortage due to error or omission",
        "Breach of money-carrying / security conditions",
        "Failure to keep required records",
    ],
    conditions=[
        "Money in transit must be accompanied by escorts according to value "
        "(GBP 2,000 / GBP 5,000 / GBP 10,000 thresholds; amounts over GBP 10,000 carried by a "
        "professional security company)",
    ],
    limits="Money and Personal Assault limits as stated in the Schedule.",
)

section(
    "SECTION 9 \u2013 GOODS IN TRANSIT",
    "Damage to the Property Insured whilst in transit by any insured method of conveyance within the "
    "Geographical Limits.",
    [
        "Tools and Samples; Clothing and Personal Effects",
        "Tarpaulins, Sheets and Ropes",
        "Debris Removal, Trans-shipment and Recovery Charges",
    ],
    [
        "Excluded Property",
        "Failure to take reasonable precautions",
    ],
    limits="Limit any one vehicle/sending and other limits as stated in the Schedule.",
)

section(
    "SECTION 10 \u2013 LOSS OF LICENCE",
    "Loss in trade value or net profit following the forfeiture, suspension or refusal of renewal of "
    "the Insured\u2019s premises licence, other than for reasons within the Insured\u2019s control. Operative "
    "only if shown in the Schedule.",
    [
        "Cover triggered on forfeiture, suspension or non-renewal of the Licence",
    ],
    [
        "Failure to comply with claims conditions",
        "Loss arising from replacement of the licensee",
    ],
    limits="As stated in the Schedule.",
)

section(
    "SECTION 11 \u2013 PRODUCTION INDEMNITY \u201cALL RISKS\u201d",
    "Additional expenditure and Gross Production Cost loss incurred as a result of the interruption, "
    "postponement, cancellation or abandonment of an insured Production. Comprises a Multimedia "
    "Sub-Section (Damage to Property Insured) and a Producers Indemnity Sub-Section (any cause beyond "
    "the Insured\u2019s control).",
    [
        "Agency and Talent Costs; Archive Material",
        "Automatic Reinstatement; Storage (up to 12 months)",
    ],
    [
        "Incapacity of persons due to hazardous acts, drugs/alcohol, age limits (<4 or >70) or pre-existing conditions",
        "Cancellation/abandonment due to weather; failure of equipment, effects or recordings to perform",
        "Software programming errors / design defects; failure to fulfil a contract; foot and mouth disease",
        "The Excess and Consequential Loss (as defined)",
    ],
    conditions=[
        "Conditions precedent include Production Planning, Duplicates, Rushes, Pre-Filming Testing, "
        "Processing (within 48 hours) and Full Value Declaration",
    ],
    limits="Limit of Indemnity any one Production as stated in the Schedule; Agency and Talent Costs "
           "up to 25% / max GBP 30,000 any one Production.",
)

section(
    "SECTION 12 \u2013 MEDIA LIABILITY (CLAIMS-MADE)",
    "Civil liability arising from the Insured\u2019s Media Business Services \u2013 including defamation, "
    "infringement of intellectual property and breach of confidentiality \u2013 written on a claims-made "
    "basis. Insuring clauses include Indemnity, Legal Defence Costs and Expenses, Rectification, "
    "Irrecoverable Fees, Data Protection Defence Costs, Reputation Management, Withdrawal of Content "
    "and intellectual-property pursuit costs.",
    [
        "Joint Ventures; Indemnity to Principals; Mergers and Acquisitions",
        "Change of Control provisions",
        "Reputation Management and Withdrawal of Content",
        "Compensation for Court Attendance",
    ],
    [
        "Claims or circumstances known at inception",
        "Deliberate collection of private data without consent",
        "Bodily injury / property damage; Dishonesty and deliberate acts",
        "Contractual liability; Patents; Insolvency / bankruptcy; Fines and penalties",
        "Asbestos; Employers\u2019 liability and claims by Employees",
    ],
    limits="Indemnity Limit as stated in the Schedule. Virus claims limited to the lower of the "
           "Schedule sum or GBP 500,000; Data Protection defence costs GBP 250,000; Reputation "
           "Management GBP 250,000; Withdrawal of Content GBP 250,000; IP pursuit costs GBP 25,000; "
           "court attendance GBP 500/GBP 250 per day.",
)

section(
    "SECTION 13 \u2013 COMMERCIAL LEGAL EXPENSES (ARAG)",
    "Legal Costs and Expenses (including appeals and certain compensation awards) following an Insured "
    "Event \u2013 covering employment, employment compensation awards, restrictive covenants, tax disputes "
    "and related matters \u2013 together with access to legal, tax, redundancy and counselling helplines "
    "and identity-theft resolution. Underwritten by ARAG and operative only if shown in the Schedule.",
    [
        "Freedom to choose an Appointed Advisor once proceedings are issued",
        "Legal and Tax advice helpline; Redundancy Assistance helpline",
        "Identity Theft Resolution; Counselling Assistance",
    ],
    [
        "Matters without Reasonable Prospects of Success (a greater than 50% chance)",
        "Matters arising before cover incepted (incl. redundancy notified within 180 days of inception unless prior equivalent cover)",
        "Fraudulent claims or claims tainted by dishonesty",
        "Costs incurred without the insurer\u2019s consent; small claims below stated thresholds",
    ],
    conditions=[
        "The claim must always have Reasonable Prospects of Success, arise within the Territorial "
        "Limit and be reported during the Period of Insurance and as soon as the Insured is aware",
    ],
    limits="Up to GBP 100,000 for all claims related by time or originating cause; aggregate "
           "GBP 1,000,000 for Employment Compensation Awards; certain Executive Suite events sub-limited "
           "to GBP 25,000.",
)

section(
    "SECTION 14 \u2013 MANAGEMENT LIABILITY (CLAIMS-MADE)",
    "Directors\u2019, officers\u2019 and corporate management liability, written on a claims-made basis. "
    "Insuring clauses: A. Directors\u2019 and Officers\u2019 Liability; B. Company Reimbursement; "
    "C. Corporate Liability; and D. Company Employment Practice Liability. Operative only for the "
    "insuring clauses shown in the Schedule.",
    [
        "Defence Costs and Investigation Costs",
        "Discovery Period; cover for Outside Directorships",
        "Non-Executive Director extra limit; Management Buy-Out",
        "Civil Fines and Penalties (where insurable); Corporate Manslaughter and Corporate Bribery defence; New Subsidiaries; Emergency Costs",
        "Employment Practice Liability cover",
    ],
    [
        "Prior and pending claims / known circumstances",
        "Dishonest, fraudulent or criminal conduct (once established)",
        "Bodily injury and property damage; Pollution",
        "Insured v Insured claims (subject to carve-backs)",
        "Loss exclusions (taxes, employment-related benefits, severance/redundancy, sums not legally insurable)",
    ],
    conditions=[
        "Claims and circumstances must be notified in accordance with the Section\u2019s own "
        "Notification and Claims Conditions",
    ],
    limits="Limit of Liability per insuring clause as stated in the Schedule; Jurisdiction worldwide "
           "excluding USA/Canada unless stated otherwise in the Schedule.",
)

section(
    "SECTION 15 \u2013 CYBERGUARD\u2122 (CYBER LIABILITY)",
    "First-party and third-party cyber cover, written on a claims-made / discovered basis and subject "
    "to a Retroactive Date. Third-party insuring clauses: Multimedia Liability; Security and Privacy "
    "Liability; Privacy Regulatory Defence and Penalties; PCI DSS Liability; and Bodily Injury and "
    "Property Damage Liability. Operative only for the insuring clauses shown in the Schedule.",
    [
        "First-party: Breach Event Costs and BrandGuard",
        "First-party: System Failure and Data Recovery",
        "First-party: Non-Physical Business Interruption (subject to a Waiting Period)",
        "First-party: Cyber Extortion and Cyber Crime (Financial, Phishing, Telecommunications and Utilities Fraud)",
        "First-party: Bricking Loss; Reward Expenses; Court Attendance Costs (up to GBP 500 per day)",
    ],
    [
        "War and failure of core infrastructure",
        "Bodily injury and property damage (save where specifically written back)",
        "Prior known incidents or circumstances",
        "Betterment / upgrade costs",
    ],
    conditions=[
        "Cyber Extortion Monies require the insurer\u2019s prior written consent and the Police must be "
        "notified before any payment; first-party covers require discovery by an Executive during the "
        "Period of Insurance",
    ],
    limits="Up to the Cyber Limit of Liability stated in the Schedule; sub-limits, Waiting Periods, "
           "Periods of Restoration and Retroactive Date apply as stated.",
)

# ---------- General exclusions ----------
add_h1(doc, "GENERAL POLICY EXCLUSIONS (APPLY ACROSS SECTIONS 1\u201311)")
add_para(doc, "The following General Policy Exclusions apply unless a Section states otherwise. "
              "Sections 13, 14 and 15 carry their own exclusions which prevail for those Sections:")
for e in [
    "Communicable Disease (not applicable to EL/PL/Products)",
    "Contribution (where other insurance applies)",
    "Coronavirus / Covid-19 (added to Public and Products Liability where shown in the Schedule)",
    "Date Recognition; Excess; Fines and Penalties",
    "Northern Ireland (riot/civil commotion \u2013 specified Sections)",
    "Nuclear; Pollution (specified Sections; limited Production Property write-back to GBP 500,000)",
    "Property Cyber and Data Endorsement \u2013 excludes Cyber Loss and loss of/ damage to Data, with "
    "limited write-backs for ensuing fire/explosion and the cost of repairing data-processing media",
    "Sonic Bang; Terrorism (non-Terrorism Sections); War & Kindred Risks",
]:
    add_bullet(doc, e)

# ---------- Conditions & claims obligations ----------
add_h1(doc, "KEY CONDITIONS AND CLAIMS OBLIGATIONS")
for c in [
    "Notification of a claim is a Condition Precedent to liability \u2013 the Insured must notify as soon "
    "as practicable (Sections 1\u201311).",
    "Notification to the Police following theft, attempted theft or malicious damage is a Condition Precedent.",
    "No admission of liability, offer, settlement or payment may be made without the insurer\u2019s written consent.",
    "The Insured must take reasonable steps to mitigate loss and to maintain protections/security.",
    "Property Sections are subject to Protection & Maintenance conditions (fire protection, minimum "
    "security, intruder alarm and unoccupancy) \u2013 several are conditions precedent.",
    "Sections 12\u201315 operate on a claims-made basis and have their own notification and claims "
    "conditions (e.g. 28-day notification for Media and Production Indemnity; separate notice "
    "provisions for Management Liability and Cyber).",
    "Cover is subject to Average (underinsurance) and to payment of premium.",
]:
    add_bullet(doc, c)

# ---------- Limits table ----------
add_h1(doc, "LIMITS, SUB-LIMITS AND EXCESSES")
add_para(doc, "Principal limits and sub-limits referenced in the wording are summarised below. All "
              "sums insured, limits of indemnity and excesses are as stated in the Schedule, which "
              "prevails.", size=9, italic=True, color=GREY)
add_table(
    doc,
    ["Cover / item", "Limit or sub-limit", "Notes"],
    [
        ["Section 2 \u2013 Artists\u2019 Technical Equipment", "GBP 20,000", "Any one occurrence & aggregate"],
        ["Section 2 \u2013 Declared General Average", "GBP 10,000 aggregate", "Insured bears first 10%, min GBP 250"],
        ["Valuables (undeclared)", "GBP 10,000", "Unless declared and accepted"],
        ["Criminal Prosecution Defence Costs (EL/PL)", "GBP 250,000", "GBP 5,000,000 for manslaughter"],
        ["Asbestos fire/explosion write-back (EL/Products)", "GBP 500,000", "Bodily injury from fire/explosion"],
        ["Public Liability \u2013 Custody/Control", "GBP 250,000", "GBP 2,500 excess each claim"],
        ["Pollution write-back (Production Property)", "GBP 500,000", "Where applicable"],
        ["Section 11 \u2013 Agency & Talent Costs", "GBP 30,000", "Up to 25%, any one Production"],
        ["Section 12 \u2013 Virus claims", "Lower of Schedule sum or GBP 500,000", "Any one originating cause"],
        ["Section 12 \u2013 Data Protection / Reputation / Withdrawal", "GBP 250,000 each", "As specified"],
        ["Section 12 \u2013 IP pursuit costs", "GBP 25,000 aggregate", ""],
        ["Section 13 \u2013 Legal Expenses", "GBP 100,000 per claim", "GBP 1,000,000 agg. employment compensation"],
        ["Section 15 \u2013 Court Attendance Costs", "GBP 500 per day", ""],
        ["All other limits / sums insured / excesses", "As per Schedule", "Schedule prevails"],
    ],
    widths=[3600, 2900, 3200],
)

# ---------- Optional / What's not covered / Claims ----------
add_h1(doc, "OPTIONAL COVERS AND ENDORSEMENTS")
for o in [
    "Sections 4 (Terrorism), 10 (Loss of Licence), 13 (Legal Expenses), 14 (Management Liability) and "
    "15 (Cyber) are operative only if shown in the Schedule.",
    "Section 2 optional covers: Hired-in / Hired-out property and Mechanical & Electrical Breakdown.",
    "Section 3 optional extensions: Contract Sites, Non-Damage Denial of Access, Goods in Transit, "
    "Public Utilities Terminal Ends and Flexible Business Interruption Limit.",
    "Coronavirus / Covid-19 exclusion is applied to the liability Sections where shown in the Schedule.",
]:
    add_bullet(doc, o)

add_h1(doc, "WHAT IS NOT COVERED (SUMMARY)")
add_para(doc, "In addition to each Section\u2019s own exclusions, the policy does not cover (among other "
              "things): communicable disease and Covid-19 (as applicable); cyber loss and loss of data "
              "(property Sections); war, terrorism (outside the Terrorism Section) and nuclear risks; "
              "pollution (outside limited write-backs); wear, tear and gradual deterioration; the "
              "Excess; fines, penalties and punitive damages (save where expressly insured); and "
              "deliberate, dishonest or criminal acts. This list is not exhaustive \u2013 refer to the "
              "wording.")

add_h1(doc, "CLAIMS NOTIFICATION SUMMARY")
for c in [
    "Property, BI, Liability, Money, Transit and Loss of Licence (Sections 1\u201311): notify as soon as "
    "practicable \u2013 Claims, Tokio Marine HCC, mail@tmhcc.com, Tel +44 (0)20 7702 4700.",
    "Media Liability and Production Indemnity (Sections 12\u201313 PI route): notify within 28 days \u2013 "
    "PI Claims, piclaims@tmhcc.com.",
    "Commercial Legal Expenses (Section 13): claims handled by ARAG \u2013 report during the Period of "
    "Insurance and as soon as the Insured is aware.",
    "Management Liability and Cyber (Sections 14\u201315): notify in accordance with the Section\u2019s own "
    "notice provisions, during the Period of Insurance (or Discovery Period where applicable).",
    "Theft, attempted theft or malicious damage must also be reported to the Police (condition precedent).",
]:
    add_bullet(doc, c)

add_h1(doc, "IMPORTANT BROKER / INSURED NOTES")
for n in [
    "This summary must be read together with the policy wording, Schedule and any endorsements, which "
    "together set out the cover, limits, sub-limits, excesses and conditions that apply.",
    "Only the Sections shown as operative in the Schedule are in force.",
    "Several Sections are written on a claims-made basis \u2013 timely notification is essential and is a "
    "condition precedent in many cases.",
    "Check sums insured and limits carefully \u2013 the policy is subject to Average (underinsurance).",
    "This is a non-consumer commercial contract and is not suitable for consumers.",
]:
    add_bullet(doc, n)

finalize(
    doc,
    '/app/work/output/_tmp_soc.docx',
    '/app/work/output/TMHCC_Media_Combined_Summary_of_Cover_FINAL.docx',
    header_text=None,  # keep "Summary of cover | Commercial Combined & Media"
    page_numbers=True,
)
print("Summary of Cover built.")
print("paras:", len(doc.paragraphs), "tables:", len(doc.tables))
