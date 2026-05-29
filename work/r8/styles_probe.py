# -*- coding: utf-8 -*-
"""Print pStyle + first runs' rPr for given paragraph indices, to mirror styles in inserts."""
import zipfile
from lxml import etree
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
def qn(t): return f"{{{W}}}{t}"
xml = zipfile.ZipFile("/app/work/r8/source_uploaded.docx").read("word/document.xml")
root = etree.fromstring(xml)
paras = list(root.iter(qn("p")))
import sys
idxs = [int(x) for x in sys.argv[1:]]
for i in idxs:
    p = paras[i]
    pPr = p.find(qn("pPr"))
    style = None; numpr=None
    if pPr is not None:
        ps = pPr.find(qn("pStyle"))
        if ps is not None: style = ps.get(qn("val"))
        if pPr.find(qn("numPr")) is not None: numpr = etree.tostring(pPr.find(qn("numPr"))).decode()
    txt = "".join((t.text or "") for t in p.iter(qn("t")))[:60]
    # first run rPr
    rpr_txt = None
    for r in p.iter(qn("r")):
        rpr = r.find(qn("rPr"))
        if rpr is not None:
            rpr_txt = etree.tostring(rpr).decode().replace(f'{{{W}}}','w:').replace(' xmlns:w="%s"'%W,'')
        break
    print(f"[{i}] style={style} numPr={'Y' if numpr else '-'} | {txt!r}")
    if rpr_txt: print("      rPr:", rpr_txt[:200])
