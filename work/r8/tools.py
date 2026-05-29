# -*- coding: utf-8 -*-
"""Round-8 helpers: parse the current clean wording (document.xml) into paragraphs,
list monetary sub-limits with context, and locate headings/definitions."""
import re, sys, json
from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}

DOCX_XML = "/app/work/r8/unz/word/document.xml"

def load():
    tree = etree.parse(DOCX_XML)
    return tree

def para_text(p):
    parts = []
    for t in p.iter(f"{{{W}}}t"):
        parts.append(t.text or "")
    # also capture tabs as space
    return "".join(parts)

def all_paras(tree):
    body = tree.getroot().find(f"{{{W}}}body")
    out = []
    # iterate over w:p in document order (including those inside tables)
    for i, p in enumerate(tree.getroot().iter(f"{{{W}}}p")):
        out.append((i, para_text(p)))
    return out

def cmd_paras(start=0, end=None, grep=None):
    tree = load()
    paras = all_paras(tree)
    if end is None:
        end = len(paras)
    rx = re.compile(grep, re.I) if grep else None
    for i, txt in paras:
        if i < start or i >= end:
            continue
        if rx and not rx.search(txt):
            continue
        if txt.strip() == "" and not grep:
            continue
        print(f"[{i:>4}] {txt[:240]}")

def cmd_money():
    """List every paragraph containing a monetary amount, with index."""
    tree = load()
    paras = all_paras(tree)
    rx = re.compile(r"(£|GBP|\bpounds?\b)\s?[\d,]+", re.I)
    for i, txt in paras:
        if rx.search(txt):
            print(f"[{i:>4}] {txt.strip()[:300]}")

def cmd_count():
    tree = load()
    paras = all_paras(tree)
    print("total paragraphs:", len(paras))

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "count"
    if cmd == "count":
        cmd_count()
    elif cmd == "money":
        cmd_money()
    elif cmd == "paras":
        start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        end = int(sys.argv[3]) if len(sys.argv) > 3 else None
        cmd_paras(start, end)
    elif cmd == "grep":
        cmd_paras(0, None, grep=sys.argv[2])
