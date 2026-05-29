"""
Final amendments to NEW_0526 wording (branding otherwise untouched):
  1. Hyperlink the non-Section TOC entries to their section headings
     (Section 1-15 entries are already hyperlinked in the source).
  2. Force the Policy Contents onto its own page and split it into two
     balanced columns (column break at the mid-point) -> two-column TOC.
  3. Add a page-number field to the footer across the whole document.
"""
import zipfile
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SRC = '/app/work/source/NEW_0526.docx'
INTERIM = '/app/work/output/_interim_new.docx'
FINAL = '/app/work/output/TMHCC_Media_Combined_0526_FINAL_amended.docx'

# Only the entries that are NOT already hyperlinked in the source.
# TOC paragraph index -> target heading paragraph index
LINK_MAP = {
    24: 23,   # Policy Contents
    25: 74,   # Introduction
    26: 82,   # Notices
    27: 152,  # Insuring Agreement
    28: 159,  # General Policy Definitions
    29: 309,  # General Policy Conditions
    30: 450,  # Policy Protection and Maintenance Conditions
    31: 529,  # Policy Claims Conditions
    32: 610,  # Policy Exclusions
    41: 1915, # Sub-Section 1 - Money
    42: 1962, # Sub-Section 2 - Personal Assault
}
PAGEBREAK_BEFORE = 23   # 'Policy Contents' heading starts its own page
COLBREAK_AT = 37        # entry that starts the 2nd column (Section 5)

doc = Document(SRC)
paras = doc.paragraphs
bid = 5000

# ---- 1. hyperlink the non-Section entries ----
for toc_idx, tgt_idx in LINK_MAP.items():
    toc_p = paras[toc_idx]._p
    tgt_p = paras[tgt_idx]._p
    name = f"toc_bm_{toc_idx}"
    bid += 1
    bm_start = OxmlElement('w:bookmarkStart')
    bm_start.set(qn('w:id'), str(bid)); bm_start.set(qn('w:name'), name)
    bm_end = OxmlElement('w:bookmarkEnd'); bm_end.set(qn('w:id'), str(bid))
    pPr = tgt_p.find(qn('w:pPr'))
    (pPr.addnext(bm_start) if pPr is not None else tgt_p.insert(0, bm_start))
    bm_start.addnext(bm_end)

    runs = toc_p.findall(qn('w:r'))
    if not runs:
        print("WARN no runs:", toc_idx); continue
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('w:anchor'), name); hyperlink.set(qn('w:history'), '1')
    runs[0].addprevious(hyperlink)
    for r in runs:
        hyperlink.append(r)
    print(f"linked TOC[{toc_idx}] '{paras[toc_idx].text[:38]}' -> [{tgt_idx}] '{paras[tgt_idx].text[:32]}'")

# ---- 2a. page break before 'Policy Contents' ----
p23 = paras[PAGEBREAK_BEFORE]._p
pPr = p23.find(qn('w:pPr'))
if pPr is None:
    pPr = OxmlElement('w:pPr'); p23.insert(0, pPr)
if pPr.find(qn('w:pageBreakBefore')) is None:
    pPr.insert(0, OxmlElement('w:pageBreakBefore'))
print("page break before Policy Contents added")

# ---- 2b. column break at mid-point entry (Section 5) ----
p37 = paras[COLBREAK_AT]._p
pPr37 = p37.find(qn('w:pPr'))
br_run = OxmlElement('w:r'); br = OxmlElement('w:br'); br.set(qn('w:type'), 'column'); br_run.append(br)
(pPr37.addnext(br_run) if pPr37 is not None else p37.insert(0, br_run))
print("column break before entry 37 added")

doc.save(INTERIM)
print("interim saved")

# ---- 3. footer page numbers ----
PAGE_PARA = (
    '<w:p xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
    '<w:pPr><w:jc w:val="center"/></w:pPr>'
    '<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>'
    '<w:color w:val="595959"/><w:sz w:val="16"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r>'
    '<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>'
    '<w:color w:val="595959"/><w:sz w:val="16"/></w:rPr>'
    '<w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
    '<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>'
    '<w:color w:val="595959"/><w:sz w:val="16"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r></w:p>'
)
FOOTERS = {'word/footer1.xml', 'word/footer2.xml', 'word/footer3.xml'}
zin = zipfile.ZipFile(INTERIM, 'r'); zout = zipfile.ZipFile(FINAL, 'w', zipfile.ZIP_DEFLATED)
for item in zin.infolist():
    data = zin.read(item.filename)
    if item.filename in FOOTERS:
        data = data.decode('utf-8').replace('</w:ftr>', PAGE_PARA + '</w:ftr>').encode('utf-8')
        print("patched", item.filename)
    zout.writestr(item, data)
zin.close(); zout.close()
print("FINAL saved:", FINAL)
