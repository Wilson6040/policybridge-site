# -*- coding: utf-8 -*-
"""Dump a docx's body text with stable paragraph indices to a .txt for grepping."""
import sys, zipfile, re
from lxml import etree
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

def dump(docx_path, out_path):
    with zipfile.ZipFile(docx_path) as z:
        xml = z.read("word/document.xml")
    root = etree.fromstring(xml)
    lines = []
    for i, p in enumerate(root.iter(f"{{{W}}}p")):
        txt = "".join((t.text or "") for t in p.iter(f"{{{W}}}t"))
        lines.append(f"[{i:>4}] {txt}")
    open(out_path, "w", encoding="utf-8").write("\n".join(lines))
    print("wrote", out_path, len(lines), "paras")

if __name__ == "__main__":
    dump(sys.argv[1], sys.argv[2])
