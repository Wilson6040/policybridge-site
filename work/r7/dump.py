import sys
from docx import Document

doc = Document("/app/work/r7/source_uploaded.docx")
paras = doc.paragraphs
print("TOTAL PARAGRAPHS:", len(paras))

terms = [t.lower() for t in sys.argv[1:]]

def show(i, p):
    style = p.style.name if p.style else "?"
    txt = p.text
    print(f"[{i}] ({style}) {txt}")

if not terms:
    sys.exit(0)

for i, p in enumerate(paras):
    low = p.text.lower()
    if any(t in low for t in terms):
        # print context: prev heading + this + a couple after
        print("="*100)
        show(i, p)
