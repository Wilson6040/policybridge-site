from docx import Document
from docx.oxml.ns import qn

doc = Document('/app/work/source/NEW_0526.docx')
body = doc.element.body
# Iterate all sectPr (section properties) in document order
sect_count = 0
for sectPr in body.iter(qn('w:sectPr')):
    refs = sectPr.findall(qn('w:footerReference'))
    hrefs = sectPr.findall(qn('w:headerReference'))
    cols = sectPr.find(qn('w:cols'))
    numcols = cols.get(qn('w:num')) if cols is not None else '1'
    ftypes = [(r.get(qn('w:type')), r.get(qn('r:id'))) for r in refs]
    htypes = [(r.get(qn('w:type')), r.get(qn('r:id'))) for r in hrefs]
    print(f"Sect {sect_count}: cols={numcols} footers={ftypes} headers={htypes}")
    sect_count += 1
print("TOTAL sectPr:", sect_count)
