from docx import Document
from lxml import etree
import sys

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
doc = Document('/app/work/r7/source_uploaded.docx')
ps = doc.paragraphs

def simp(el, depth=0, out=None):
    tag = etree.QName(el).localname
    txt = ""
    if tag in ("t", "delText", "instrText"):
        txt = " => " + repr(el.text)
    # show key attrs
    attrs = {etree.QName(k).localname: v for k, v in el.attrib.items()}
    ashow = ""
    if tag in ("hyperlink",):
        ashow = " " + str(attrs)
    if tag in ("rStyle", "pStyle"):
        ashow = " val=" + attrs.get("val", "")
    print("  " * depth + tag + ashow + txt)
    for c in el:
        simp(c, depth + 1)

for i in [int(x) for x in sys.argv[1:]]:
    print("=" * 25, "PARA", i, repr(ps[i].text[:60]))
    simp(ps[i]._p)
