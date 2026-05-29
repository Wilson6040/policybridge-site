import sys
from docx import Document
doc = Document("/app/work/r7/source_uploaded.docx")
paras = doc.paragraphs
a, b = int(sys.argv[1]), int(sys.argv[2])
for i in range(a, min(b, len(paras))):
    p = paras[i]
    style = p.style.name if p.style else "?"
    print(f"[{i}] <{style}> {p.text}")
