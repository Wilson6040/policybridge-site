"""
NEW_0526 wording — final amendments (v2)

  1. Live Word TOC field (built from TC entries) replacing the manual contents,
     laid out in two balanced columns on its own page, with auto page numbers.
  2. Remove all references to a non-existent "Section 16" (correct the specialist
     section numbering to 13/14/15).
  3. Remove stale references to the deleted standalone "Information Technology
     Section" (IT cover now lives inside the Business "All Risks" / Section 1).
  4. Restyle the Section 15 CyberGuard wording so it matches the rest of the
     document (Subtitle / Heading 1-3) and appears in the live contents.
  5. Footer page numbers across the whole document; update fields on open.

Branding is otherwise left untouched.
"""
import copy, zipfile
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SRC = '/app/work/source/NEW_0526.docx'
INTERIM = '/app/work/output/_interim_new_v2.docx'
FINAL = '/app/work/output/TMHCC_Media_Combined_0526_FINAL_amended.docx'

# ---- TC contents entries: (target paragraph index, entry text, level) ----
TC_ENTRIES = [
    (23,  "Policy Contents", 1),
    (74,  "Introduction", 1),
    (82,  "Notices", 1),
    (152, "Insuring Agreement", 1),
    (159, "General Policy Definitions", 1),
    (309, "General Policy Conditions", 1),
    (450, "Policy Protection and Maintenance Conditions", 1),
    (529, "Policy Claims Conditions", 1),
    (610, "Policy Exclusions", 1),
    (698, "Section 1: Business \u201cAll Risks\u201d Section", 1),
    (978, "Section 2: Property & Equipment \u201cAll Risks\u201d Section", 1),
    (1205, "Section 3: Business Interruption \u201cAll Risks\u201d Section", 1),
    (1520, "Section 4: Terrorism Section", 1),
    (1612, "Section 5: Employers\u2019 Liability Section", 1),
    (1671, "Section 6: Public Liability Section", 1),
    (1846, "Section 7: Products Liability Section", 1),
    (1914, "Section 8: Money Section", 1),
    (1915, "Sub-Section 1 \u2013 Money", 2),
    (1962, "Sub-Section 2 \u2013 Personal Assault", 2),
    (1995, "Section 9: Goods in Transit Section", 1),
    (2063, "Section 10: Loss of Licence Section", 1),
    (2115, "Section 11: Production Indemnity \u201cAll Risks\u201d Section", 1),
    (2222, "Section 12: Media Liability Section", 1),
    (2466, "Section 13: Commercial Legal Expenses Section", 1),
    (2784, "Section 14: Management Liability Insurance Section", 1),
    (3156, "Section 15: Cyber Liability Section", 1),
]

# ---- Section-16 corrections (substring replacements within a paragraph) ----
SECT16_FIX = {
    156: ("Sections 13, 14, 15 or 16", "Sections 13, 14 or 15"),
    310: ("Sections 15 and 16", "Sections 14 and 15"),
    611: ("Sections 13,15 and 16", "Sections 13, 14 and 15"),
}

# ---- Stale "Information Technology Section" reference cleanups ----
IT_FIX = {
    233: ("the Information Technology Section", "the Business \u201cAll Risks\u201d Section"),
    384: (" or the Information Technology Section", ""),
    418: (", Information Technology \u201cAll Risks\u201d", ""),
    451: (", Information Technology and Money Sections", " and Money Sections"),
    473: (" and/or the Information Technology Section", ""),
    646: (", Information Technology, Money", ", Money"),
    656: (", Information Technology and Production Indemnity", " and Production Indemnity"),
}
IT_DELETE = [1567]   # standalone list item: "Information Technology Section;"

# ---- CyberGuard restyle (paragraph index -> style) ----
CYBER_SUBTITLE = [3156]
CYBER_H1 = [3160, 3244, 3649, 3824, 3898, 3940, 3951, 4005, 4017]
CYBER_H2 = [3164, 3190, 3736, 3757, 3767, 3784, 3828, 3856, 3878, 3886, 3892, 3895,
            3925, 3926, 3929, 3941, 3948, 3953, 3958, 3962, 3968, 3971, 3974, 3982,
            3985, 3990, 3993, 4000, 4002, 4009, 3899, 3910, 3915]
CYBER_EXCLUDE = {3157, 3646}   # leave as-is (subtitle line / mid-sentence false positive)
CYBER_RANGE = (3156, 4037)


# ===================== helpers =====================
def fld_run(fldchar=None, instr=None, text=None):
    r = OxmlElement('w:r')
    rpr = OxmlElement('w:rPr')
    rf = OxmlElement('w:rFonts')
    for a in ('w:ascii', 'w:hAnsi', 'w:cs'):
        rf.set(qn(a), 'Arial')
    rpr.append(rf)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), '18'); rpr.append(sz)
    r.append(rpr)
    if fldchar:
        fc = OxmlElement('w:fldChar'); fc.set(qn('w:fldCharType'), fldchar); r.append(fc)
    if instr is not None:
        it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = instr; r.append(it)
    if text is not None:
        t = OxmlElement('w:t'); t.set(qn('xml:space'), 'preserve'); t.text = text; r.append(t)
    return r


def add_tc(p_el, text, level):
    p_el.append(fld_run(fldchar='begin'))
    p_el.append(fld_run(instr=f' TC "{text}" \\f C \\l "{level}" '))
    p_el.append(fld_run(fldchar='end'))


def build_toc_field(p_el):
    for r in p_el.findall(qn('w:r')):
        p_el.remove(r)
    for hl in p_el.findall(qn('w:hyperlink')):
        p_el.remove(hl)
    p_el.append(fld_run(fldchar='begin'))
    p_el.append(fld_run(instr=' TOC \\f C \\h \\z '))
    p_el.append(fld_run(fldchar='separate'))
    p_el.append(fld_run(text='Right-click here and choose \u201cUpdate Field\u201d to build the contents.'))
    p_el.append(fld_run(fldchar='end'))


def para_text(p_el):
    return ''.join(t.text or '' for t in p_el.iter(qn('w:t')))


def set_single_text(p_el, new_text):
    runs = p_el.findall(qn('w:r'))
    done = False
    for r in runs:
        ts = r.findall(qn('w:t'))
        if not done and ts:
            ts[0].text = new_text; ts[0].set(qn('xml:space'), 'preserve')
            for extra in ts[1:]:
                extra.text = ''
            done = True
        else:
            for t in r.findall(qn('w:t')):
                t.text = ''
    return done


def replace_in_para(p_el, old, new, label=""):
    txt = para_text(p_el)
    if old in txt:
        set_single_text(p_el, txt.replace(old, new, 1))
        print(f"  fixed {label}: '{old[:35]}' -> '{new[:35]}'")
        return True
    print(f"  WARN {label}: substring not found: '{old[:40]}' (text='{txt[:60]}')")
    return False


def set_pagebreak_before(p_el):
    pPr = p_el.find(qn('w:pPr'))
    if pPr is None:
        pPr = OxmlElement('w:pPr'); p_el.insert(0, pPr)
    if pPr.find(qn('w:pageBreakBefore')) is None:
        pPr.insert(0, OxmlElement('w:pageBreakBefore'))


# ===================== build =====================
doc = Document(SRC)
paras = doc.paragraphs

# capture element references up-front (indices are about to change)
ref = {}
needed = set([i for i, _, _ in TC_ENTRIES])
needed |= set(SECT16_FIX) | set(IT_FIX) | set(IT_DELETE)
needed |= set(CYBER_SUBTITLE) | set(CYBER_H1) | set(CYBER_H2)
needed |= {22, 23, 24, 697}
needed |= set(range(25, 50))
needed |= set(range(*CYBER_RANGE))
for i in needed:
    if i < len(paras):
        ref[i] = paras[i]

# 1. TC entries at the 26 targets
for idx, text, level in TC_ENTRIES:
    add_tc(ref[idx]._p, text, level)
print(f"added {len(TC_ENTRIES)} TC entries")

# 2. Section-16 corrections
print("Section 16 fixes:")
for idx, (old, new) in SECT16_FIX.items():
    replace_in_para(ref[idx]._p, old, new, f"[{idx}]")

# 3. IT-section citation cleanups
print("Information Technology Section fixes:")
for idx, (old, new) in IT_FIX.items():
    replace_in_para(ref[idx]._p, old, new, f"[{idx}]")

# 4. CyberGuard restyle
for idx in CYBER_SUBTITLE:
    ref[idx].style = doc.styles['Subtitle']
for idx in CYBER_H1:
    if idx in ref:
        ref[idx].style = doc.styles['Heading 1']
for idx in CYBER_H2:
    if idx in ref:
        ref[idx].style = doc.styles['Heading 2']
# everything else heading-like in the cyber range that we listed -> Heading 3
HEADING_LIKE = set()  # filled below from a re-scan
import re
for i in range(*CYBER_RANGE):
    if i not in ref:
        continue
    t = ref[i].text.strip()
    if (t and len(t) <= 60 and not t[-1:] in '.;,:' and len(t) > 2 and not t[0].islower()):
        HEADING_LIKE.add(i)
styled = set(CYBER_SUBTITLE) | set(CYBER_H1) | set(CYBER_H2) | CYBER_EXCLUDE
for i in sorted(HEADING_LIKE - styled):
    ref[i].style = doc.styles['Heading 3']
print(f"cyber restyle: subtitle={len(CYBER_SUBTITLE)} h1={len(CYBER_H1)} h2={len(CYBER_H2)} h3={len(HEADING_LIKE - styled)}")

# 5. TOC region: single live TOC field (full width) on its own page
build_toc_field(ref[24]._p)
toc_field_p = ref[24]._p
del_paras = [ref[i]._p for i in range(25, 50)]

orig_sectPr = ref[697]._p.find(qn('w:pPr')).find(qn('w:sectPr'))

# 6a. close the cover as its own (2-column) section at para 22 so the cover layout is preserved
cover_sectPr = copy.deepcopy(orig_sectPr)
p22 = ref[22]._p
pPr22 = p22.find(qn('w:pPr'))
if pPr22 is None:
    pPr22 = OxmlElement('w:pPr'); p22.insert(0, pPr22)
pPr22.append(cover_sectPr)

# 6b. the TOC section: single column, starts on a new page (full-width live TOC)
toc_sectPr = copy.deepcopy(orig_sectPr)
cols = toc_sectPr.find(qn('w:cols'))
if cols is None:
    cols = OxmlElement('w:cols'); toc_sectPr.append(cols)
for c in list(cols):
    cols.remove(c)
cols.set(qn('w:num'), '1')
cols.attrib.pop(qn('w:space'), None)
tt = toc_sectPr.find(qn('w:type'))
if tt is None:
    tt = OxmlElement('w:type'); toc_sectPr.insert(0, tt)
tt.set(qn('w:val'), 'nextPage')
new_p = OxmlElement('w:p'); new_pPr = OxmlElement('w:pPr'); new_pPr.append(toc_sectPr); new_p.append(new_pPr)
toc_field_p.addnext(new_p)

# 6c. the rest of the front matter resumes continuously (2 columns as before)
rt = orig_sectPr.find(qn('w:type'))
if rt is None:
    rt = OxmlElement('w:type'); orig_sectPr.insert(0, rt)
rt.set(qn('w:val'), 'continuous')

# 7. delete the old manual TOC entry paragraphs (25-49) and the stray IT list item
for el in del_paras:
    el.getparent().remove(el)
for idx in IT_DELETE:
    el = ref[idx]._p
    print(f"deleting stray IT list item [{idx}]: '{para_text(el)[:40]}'")
    el.getparent().remove(el)

# 8. update fields on open
uf = doc.settings.element.find(qn('w:updateFields'))
if uf is None:
    uf = OxmlElement('w:updateFields'); doc.settings.element.append(uf)
uf.set(qn('w:val'), 'true')

doc.save(INTERIM)
print("interim saved")

# 9. footer page numbers (append PAGE field to footer1/2/3)
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
    zout.writestr(item, data)
zin.close(); zout.close()
print("FINAL saved:", FINAL)
