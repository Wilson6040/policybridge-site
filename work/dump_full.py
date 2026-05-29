from docx import Document

def dump_full(path, outpath):
    doc = Document(path)
    out = []
    for i, p in enumerate(doc.paragraphs):
        txt = p.text.strip()
        if txt == "":
            continue
        st = p.style.name
        tag = st
        if st.startswith('Heading') or st in ('Title','Subtitle'):
            tag = "## " + st
        out.append(f"[{i}|{tag}] {txt}")
    with open(outpath, 'w') as f:
        f.write("\n".join(out))
    print(f"{path} -> {outpath}: {len(out)} non-empty paras")

dump_full('/app/work/source/OLD_0223C.docx', '/app/work/OLD_full.txt')
dump_full('/app/work/source/NEW_0526.docx', '/app/work/NEW_full.txt')
