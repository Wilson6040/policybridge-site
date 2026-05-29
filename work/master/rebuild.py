"""Rebuild TMHCC Media & Entertainment Combined Insurance Policy master document.

Tasks:
1) Remove red text (E20033 brand-red, FF0000 pure-red) → black, while preserving
   bold/italic/underline/hyperlink styling and tracked-change history.
2) Replace plaintext Contents page with single-column formatted paragraphs:
     left: section title (hyperlinked, with "Section N:" bolded in TMHCC navy)
     tab-right: page number (TMHCC blue, bold)
     thin TMHCC-blue divider below each row
3) Wrap the Contents page in its own single-column section so the right-aligned
   tab stops fit the full A4 width (the document body is otherwise 2-column).
4) Remove the 22 blank paragraphs + redundant page-break paragraph sitting
   between the Contents page and "Introduction" (causes ghost blank pages).
5) Repack as .docx and convert to PDF via LibreOffice.
6) Post-process the resulting PDF with PyMuPDF to inject clickable link
   annotations on the Contents page (LibreOffice's PDF export currently does
   not emit clickable Goto links for Word internal-bookmark hyperlinks, even
   though the side-panel bookmark outline still works).
"""
from __future__ import annotations

import copy
import os
import re
import shutil
import subprocess
import zipfile
from pathlib import Path

from lxml import etree

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path("/app/work/master")
SRC = ROOT / "source.docx"
WORK = ROOT / "build"
OUT_DOCX = ROOT / "TMHCC_Media_Combined_0526_FINAL_polished.docx"
OUT_PDF = ROOT / "TMHCC_Media_Combined_0526_FINAL_polished.pdf"

# ---------------------------------------------------------------------------
# Namespace plumbing
# ---------------------------------------------------------------------------
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}
W = "{%s}" % W_NS


def w(tag: str) -> str:
    return W + tag


# Brand colours
TMHCC_BLUE = "009CE5"   # primary accent / used by Heading1, Heading2 styles
TMHCC_NAVY = "0074AB"   # darker brand (used by TOCHeading style)
RED_VALS = {"E20033", "FF0000"}


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------
def unzip_docx(src: Path, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(src) as z:
        z.extractall(dest)


def zip_docx(src_dir: Path, out: Path) -> None:
    if out.exists():
        out.unlink()
    # Word requires [Content_Types].xml first and STORE-mode preferred for it
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        ct = src_dir / "[Content_Types].xml"
        if ct.exists():
            z.write(ct, "[Content_Types].xml", compress_type=zipfile.ZIP_DEFLATED)
        for path in sorted(src_dir.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(src_dir).as_posix()
            if rel == "[Content_Types].xml":
                continue
            z.write(path, rel)


# ---------------------------------------------------------------------------
# 1) Red-text removal
# ---------------------------------------------------------------------------
def strip_red(doc_root) -> int:
    """Convert any live <w:color val="FF0000|E20033"> to 000000.

    We deliberately skip <w:rPrChange> children (revision history) so tracked-
    change records remain intact.
    """
    n = 0
    # Find every w:color element
    for color in doc_root.iter(w("color")):
        val = color.get(w("val"), "").upper()
        if val not in RED_VALS:
            continue
        # Skip if inside a rPrChange (tracked change history)
        parent = color.getparent()
        ancestor = parent
        in_history = False
        while ancestor is not None:
            if ancestor.tag == w("rPrChange"):
                in_history = True
                break
            ancestor = ancestor.getparent()
        if in_history:
            continue
        color.set(w("val"), "000000")
        # Also drop themeColor if present (so it doesn't override)
        for attr in (w("themeColor"), w("themeTint"), w("themeShade")):
            if attr in color.attrib:
                del color.attrib[attr]
        n += 1
    return n


# ---------------------------------------------------------------------------
# 2) Locate the Contents-page paragraphs
# ---------------------------------------------------------------------------
def find_toc_range(body) -> tuple[int, int]:
    """Return (start_idx, end_idx_inclusive) within body's children index space.

    Start = first paragraph after the 'Policy Contents' heading containing a
    HYPERLINK field referencing 'tocpg_'.
    End = last consecutive such paragraph (or last paragraph before the first
    non-empty, non-toc paragraph).
    """
    children = list(body)
    toc_heading_idx = None
    for i, c in enumerate(children):
        if c.tag != w("p"):
            continue
        text = "".join((t.text or "") for t in c.findall(".//w:t", NS))
        if text.strip() == "Policy Contents":
            # ensure it's the heading (Heading1 style) — not a TOC entry referencing the page
            ps = c.find(".//w:pStyle", NS)
            if ps is not None and ps.get(w("val"), "") == "Heading1":
                toc_heading_idx = i
                break
    if toc_heading_idx is None:
        raise RuntimeError("Could not locate 'Policy Contents' heading")

    # Walk forward to find first TOC field paragraph
    start = None
    for i in range(toc_heading_idx + 1, len(children)):
        p = children[i]
        if p.tag != w("p"):
            continue
        instr = "".join(e.text or "" for e in p.findall(".//w:instrText", NS))
        if "tocpg_" in instr or 'HYPERLINK \\l "tocpg_' in instr:
            start = i
            break
    if start is None:
        raise RuntimeError("Could not locate TOC entries")

    # Walk forward to find last consecutive TOC paragraph (allow empty ones in between)
    end = start
    for i in range(start, len(children)):
        p = children[i]
        if p.tag != w("p"):
            break
        instr = "".join(e.text or "" for e in p.findall(".//w:instrText", NS))
        text = "".join((t.text or "") for t in p.findall(".//w:t", NS))
        if "tocpg_" in instr:
            end = i
            continue
        if text.strip() == "":
            # empty bridge paragraph between entries — accept
            continue
        # Real non-toc content reached
        break
    return start, end


# ---------------------------------------------------------------------------
# 3) Parse existing TOC entries → extract (hyperlink_field_runs, label, page_number, indent_level)
# ---------------------------------------------------------------------------
def extract_toc_entries(body, start: int, end: int) -> list[dict]:
    """Return entries with raw label text, page number string, indent flag and
    the original hyperlink field XML (for re-use)."""
    entries = []
    for i in range(start, end + 1):
        p = body[i]
        if p.tag != w("p"):
            continue
        instr = "".join(e.text or "" for e in p.findall(".//w:instrText", NS))
        if "tocpg_" not in instr:
            continue

        # Determine label text (text content of runs that lie between
        # fldChar separate and fldChar end)
        label_runs = []
        page_runs = []
        in_field = False
        seen_separate = False
        seen_end = False
        for r in p.findall("w:r", NS):
            fld = r.find("w:fldChar", NS)
            if fld is not None:
                t = fld.get(w("fldCharType"), "")
                if t == "begin":
                    in_field = True
                    seen_separate = False
                elif t == "separate":
                    seen_separate = True
                elif t == "end":
                    in_field = False
                    seen_end = True
                continue
            if in_field and not seen_separate:
                # instruction-only run
                continue
            text_runs = r.findall("w:t", NS)
            run_text = "".join(t.text or "" for t in text_runs)
            if in_field and seen_separate:
                label_runs.append(run_text)
            elif seen_end:
                # treat as page-number content (the page number sits after fldChar end)
                page_runs.append(run_text)

        # The page number is the trailing digits of the *last* non-empty page_runs.
        all_after = "".join(page_runs)
        # Strip trailing manual ellipsis dots that some entries received
        all_after = all_after.replace("\u2026", "")  # ellipsis
        all_after = re.sub(r"\.{2,}", "", all_after)
        all_after = all_after.strip()
        page_match = re.search(r"(\d+)\s*$", all_after)
        page = page_match.group(1) if page_match else ""

        label = "".join(label_runs).strip()

        # Indent flag — Sub-Section entries have w:ind w:left
        ind_el = p.find("w:pPr/w:ind", NS)
        indent = bool(ind_el is not None and ind_el.get(w("left")))

        # Capture the bookmark target (tocpg_N) from the HYPERLINK instruction
        m = re.search(r'HYPERLINK\s+\\l\s+"([^"]+)"', instr)
        target = m.group(1) if m else ""

        entries.append({
            "label": label,
            "page": page,
            "indent": indent,
            "target": target,
            "p_index": i,
        })
    return entries


# ---------------------------------------------------------------------------
# 4) Build the replacement 2-column TOC table
# ---------------------------------------------------------------------------
SECTION_RE = re.compile(r"^(Section\s+\d+:|Sub-Section\s+\d+\s+[\u2013-])\s*(.*)$")


def make_run(text: str, *, bold=False, color=None, size=22, rfonts="Arial",
             preserve_space=False, underline=False) -> etree._Element:
    r = etree.SubElement(etree.Element(w("dummy")), w("r"))
    rPr = etree.SubElement(r, w("rPr"))
    if rfonts:
        rf = etree.SubElement(rPr, w("rFonts"))
        rf.set(w("ascii"), rfonts)
        rf.set(w("hAnsi"), rfonts)
        rf.set(w("cs"), rfonts)
    if bold:
        etree.SubElement(rPr, w("b"))
        etree.SubElement(rPr, w("bCs"))
    if color:
        c = etree.SubElement(rPr, w("color"))
        c.set(w("val"), color)
    if size:
        sz = etree.SubElement(rPr, w("sz"))
        sz.set(w("val"), str(size))
        szc = etree.SubElement(rPr, w("szCs"))
        szc.set(w("val"), str(size))
    # Explicit underline override (defaults to none) — prevents the inherited
    # Hyperlink character style from forcing blue underlined text.
    u = etree.SubElement(rPr, w("u"))
    u.set(w("val"), "single" if underline else "none")
    t = etree.SubElement(r, w("t"))
    t.text = text
    if preserve_space or text.startswith(" ") or text.endswith(" "):
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    r.getparent().remove(r)
    return r


def make_hyperlink_paragraph(target: str, label: str, *,
                             indent_left: int = 0,
                             align: str = "left",
                             page_number: str | None = None,
                             color_text="000000",
                             color_section_prefix="0074AB",
                             color_page="009CE5",
                             font_size=22) -> etree._Element:
    """Build a <w:p> with an internal hyperlink to `target` using the modern
    <w:hyperlink w:anchor="..."> element form (NOT the legacy fldChar field).

    When page_number is None → col 1: paragraph contains the hyperlink wrapping
        the label runs (with optional bold "Section N:" prefix).
    When page_number is not None → col 2: paragraph contains the hyperlink
        wrapping a single right-aligned page-number run.
    """
    p = etree.Element(w("p"))
    pPr = etree.SubElement(p, w("pPr"))
    spacing = etree.SubElement(pPr, w("spacing"))
    spacing.set(w("before"), "80")
    spacing.set(w("after"), "80")
    spacing.set(w("line"), "264")
    spacing.set(w("lineRule"), "auto")
    if indent_left:
        ind = etree.SubElement(pPr, w("ind"))
        ind.set(w("left"), str(indent_left))
    if align == "right":
        jc = etree.SubElement(pPr, w("jc"))
        jc.set(w("val"), "right")
    rPr_par = etree.SubElement(pPr, w("rPr"))
    sz = etree.SubElement(rPr_par, w("sz")); sz.set(w("val"), str(font_size))
    szc = etree.SubElement(rPr_par, w("szCs")); szc.set(w("val"), str(font_size))

    hyperlink = etree.SubElement(p, w("hyperlink"))
    hyperlink.set(w("anchor"), target)
    hyperlink.set(w("history"), "1")

    if page_number is None:
        m = SECTION_RE.match(label)
        if m:
            prefix = m.group(1)
            rest = m.group(2)
            hyperlink.append(make_run(prefix, bold=True, color=color_section_prefix,
                                       size=font_size, underline=False))
            if rest:
                hyperlink.append(make_run(" " + rest, bold=False, color=color_text,
                                           size=font_size, underline=False))
        else:
            hyperlink.append(make_run(label, bold=False, color=color_text,
                                       size=font_size, underline=False))
    else:
        hyperlink.append(make_run(page_number, bold=True, color=color_page,
                                   size=font_size, underline=False))

    return p


def make_page_paragraph(page: str, *, color="009CE5", font_size=22) -> etree._Element:
    """A simple right-aligned paragraph containing the page number — no hyperlink
    field (col 1 already provides clickable navigation)."""
    p = etree.Element(w("p"))
    pPr = etree.SubElement(p, w("pPr"))
    spacing = etree.SubElement(pPr, w("spacing"))
    spacing.set(w("before"), "80")
    spacing.set(w("after"), "80")
    spacing.set(w("line"), "264")
    spacing.set(w("lineRule"), "auto")
    jc = etree.SubElement(pPr, w("jc"))
    jc.set(w("val"), "right")
    rPr_par = etree.SubElement(pPr, w("rPr"))
    sz = etree.SubElement(rPr_par, w("sz")); sz.set(w("val"), str(font_size))
    szc = etree.SubElement(rPr_par, w("szCs")); szc.set(w("val"), str(font_size))
    p.append(make_run(page, bold=True, color=color, size=font_size))
    return p


def make_section_break_pPr(*, cols: int = 1, pg_w: int = 11906, pg_h: int = 16838,
                            top: int = 992, bottom: int = 737, left: int = 737,
                            right: int = 737, header: int = 454,
                            footer: int = 352, sec_type: str = "nextPage",
                            cols_space: int = 709) -> etree._Element:
    """Build a complete <w:pPr> containing a <w:sectPr> that ends a section.
    Default = single-column, A4 portrait, same margins/headers as the body.
    """
    pPr = etree.Element(w("pPr"))
    sectPr = etree.SubElement(pPr, w("sectPr"))
    if sec_type:
        t = etree.SubElement(sectPr, w("type")); t.set(w("val"), sec_type)
    pgSz = etree.SubElement(sectPr, w("pgSz"))
    pgSz.set(w("w"), str(pg_w)); pgSz.set(w("h"), str(pg_h))
    pgMar = etree.SubElement(sectPr, w("pgMar"))
    pgMar.set(w("top"), str(top)); pgMar.set(w("right"), str(right))
    pgMar.set(w("bottom"), str(bottom)); pgMar.set(w("left"), str(left))
    pgMar.set(w("header"), str(header)); pgMar.set(w("footer"), str(footer))
    pgMar.set(w("gutter"), "0")
    colsEl = etree.SubElement(sectPr, w("cols"))
    colsEl.set(w("num"), str(cols))
    if cols > 1:
        colsEl.set(w("space"), str(cols_space))
    return pPr


def make_toc_row_paragraph(target: str, label: str, page: str, *,
                            indent_left: int = 0,
                            font_size: int = 22,
                            is_last: bool = False) -> etree._Element:
    """Build a single TOC row as a paragraph with:
       - <w:hyperlink anchor=target> wrapping the label runs
       - a right-aligned tab stop near the right margin
       - a thin TMHCC-blue bottom border (skipped on last row)
    Layout:  [bold "Section N:" navy] [normal " descriptor" black] TAB [bold "page" blue]
    """
    p = etree.Element(w("p"))
    pPr = etree.SubElement(p, w("pPr"))
    # Tab stop at ~9900 twips (just inside A4 right margin)
    tabs = etree.SubElement(pPr, w("tabs"))
    tab = etree.SubElement(tabs, w("tab"))
    tab.set(w("val"), "right")
    tab.set(w("pos"), "9900")
    spacing = etree.SubElement(pPr, w("spacing"))
    spacing.set(w("before"), "100")
    spacing.set(w("after"), "100")
    spacing.set(w("line"), "264")
    spacing.set(w("lineRule"), "auto")
    if indent_left:
        ind = etree.SubElement(pPr, w("ind"))
        ind.set(w("left"), str(indent_left))
    # Thin bottom border = divider line
    if not is_last:
        pBdr = etree.SubElement(pPr, w("pBdr"))
        bottom = etree.SubElement(pBdr, w("bottom"))
        bottom.set(w("val"), "single")
        bottom.set(w("sz"), "4")
        bottom.set(w("space"), "4")
        bottom.set(w("color"), "B5E2F8")
    rPr_par = etree.SubElement(pPr, w("rPr"))
    sz = etree.SubElement(rPr_par, w("sz")); sz.set(w("val"), str(font_size))

    hyperlink = etree.SubElement(p, w("hyperlink"))
    hyperlink.set(w("anchor"), target)
    hyperlink.set(w("history"), "1")
    m = SECTION_RE.match(label)
    if m:
        hyperlink.append(make_run(m.group(1), bold=True, color="0074AB",
                                   size=font_size, underline=False))
        if m.group(2):
            hyperlink.append(make_run(" " + m.group(2), bold=False, color="000000",
                                       size=font_size, underline=False))
    else:
        hyperlink.append(make_run(label, bold=False, color="000000",
                                   size=font_size, underline=False))

    # tab run (must live OUTSIDE the hyperlink element so the page number isn't
    # styled by the hyperlink character style)
    tab_r = etree.SubElement(p, w("r"))
    tab_rpr = etree.SubElement(tab_r, w("rPr"))
    tab_sz = etree.SubElement(tab_rpr, w("sz")); tab_sz.set(w("val"), str(font_size))
    etree.SubElement(tab_r, w("tab"))
    p.append(make_run(page, bold=True, color=TMHCC_BLUE, size=font_size, underline=False))
    return p


def make_toc_block(entries: list[dict]) -> list[etree._Element]:
    """Build a list of TOC paragraphs (replaces the table approach)."""
    last_idx = len(entries) - 1
    paras = []
    for idx, e in enumerate(entries):
        paras.append(make_toc_row_paragraph(
            target=e["target"],
            label=e["label"],
            page=e["page"] or "",
            indent_left=360 if e["indent"] else 0,
            is_last=(idx == last_idx),
        ))
    return paras


# ---------------------------------------------------------------------------
# 5) Remove blank-page filler after TOC
# ---------------------------------------------------------------------------
def is_blank_paragraph(p) -> bool:
    """True if paragraph has no visible content (text, drawings, breaks, sectPr)."""
    if p.tag != w("p"):
        return False
    text = "".join((t.text or "") for t in p.findall(".//w:t", NS))
    if text.strip():
        return False
    if p.find(".//w:drawing", NS) is not None:
        return False
    if p.find(".//w:br[@w:type='page']", NS) is not None:
        return False
    if p.find(".//w:sectPr", NS) is not None:
        return False
    if p.find(".//w:pict", NS) is not None:
        return False
    return True


def remove_blank_run_between(body, after_idx: int, before_text: str) -> int:
    """Remove consecutive blank paragraphs immediately following the paragraph
    at `after_idx`, stopping when we encounter a paragraph that either has
    visible content or whose text begins with `before_text`. Returns count
    removed."""
    n = 0
    i = after_idx + 1
    while i < len(body):
        p = body[i]
        if p.tag != w("p"):
            break
        text = "".join((t.text or "") for t in p.findall(".//w:t", NS))
        if before_text and text.strip().startswith(before_text):
            break
        if is_blank_paragraph(p):
            body.remove(p)
            n += 1
            # don't advance index, since list shifted
            continue
        # has content or has a break — stop
        break
    return n


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------
def discover_actual_pages(pdf_path: Path, entries: list[dict]) -> dict[int, tuple[int, int]]:
    """For each TOC entry, find the PDF page where its heading actually starts.
    Returns {id(entry): (pdf_page_0indexed, printed_page_number)}.

    Strategy: search the PDF for each heading's title text. Prefer matches that
    sit near the top of a page (y0 < 35% of page height). The printed page
    number is read from the page footer (small grey digit at bottom-centre).
    """
    import fitz

    doc = fitz.open(str(pdf_path))

    # Build printed-page-number → PDF-page-index map by reading footers.
    print_to_pdf = {}
    for pno in range(2, doc.page_count):
        td = doc[pno].get_text("dict")
        for block in td["blocks"]:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for sp in line["spans"]:
                    t = sp["text"].strip()
                    if t.isdigit() and 800 < sp["bbox"][1] < 850 and 280 < sp["bbox"][0] < 320:
                        n = int(t)
                        if n not in print_to_pdf:
                            print_to_pdf[n] = pno
                        break
    pdf_to_print = {v: k for k, v in print_to_pdf.items()}

    def page_has_heading(page, needles: list[str]) -> bool:
        """True if any needle appears in heading-sized text (>= 13pt) on the
        page. Headings often split across spans (e.g. due to bold/italic
        runs), so we concatenate the text of all heading-sized spans into a
        single blob per page and substring-match against that.
        """
        td = page.get_text("dict")
        blob_parts = []
        for block in td["blocks"]:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                line_text = "".join(sp["text"] for sp in line["spans"]
                                      if sp.get("size", 0) >= 13)
                if line_text.strip():
                    blob_parts.append(line_text)
        blob_clean = " ".join(" ".join(blob_parts).lower().split())
        if not blob_clean:
            return False
        for needle in needles:
            if needle.lower() in blob_clean:
                return True
        return False

    def search_heading(needles: list[str], min_page: int = 2) -> int | None:
        """Find the first PDF page where one of `needles` appears as a
        heading-sized run."""
        for pno in range(min_page, doc.page_count):
            if page_has_heading(doc[pno], needles):
                return pno
        return None

    def normalize_seps(label: str) -> list[str]:
        """Generate label variants by swapping common separators."""
        out = {label}
        # Also try without trailing " Section" suffix (some Heading1 omit it)
        if label.endswith(" Section"):
            out.add(label[:-len(" Section")])
        if ":" in label:
            base = label.replace(":", " –", 1)
            out.add(base)
            out.add(label.replace(":", " -", 1))
            if base.endswith(" Section"):
                out.add(base[:-len(" Section")])
        out2 = set()
        for v in out:
            out2.add(v)
            out2.add(v.replace('"', '\u201c').replace("\u201d", '"'))
            out2.add(v.replace('\u2013', '-').replace('\u2014', '-'))
        # Sort by length descending so longer (more specific) needles match first
        return sorted(out2, key=len, reverse=True)

    out = {}
    for e in entries:
        label = e["label"]
        if label == "Policy Contents":
            out[id(e)] = (1, 2)
            continue
        # Build needle list: many variations to handle separator quirks
        needles = []
        if label.startswith("Section "):
            num = label.split()[1].rstrip(":")
            # The 1st word "Section N" is required to be a heading
            # title fragment. Use FULL label with separator alternatives.
            after_num = label.split(None, 2)[-1] if ":" not in label else label.split(":", 1)[1].strip()
            for sep in [": ", " – ", " - "]:
                needles.append(f"Section {num}{sep}")
            # Plus a more permissive "Section N" + a partial title (first word)
            if after_num:
                first_word = after_num.split()[0].strip('"\u201c\u201d')
                # full-label variants
                for variant in normalize_seps(label):
                    needles.append(variant)
        elif label.startswith("Sub-Section"):
            needles = normalize_seps(label)
        else:
            needles = normalize_seps(label)

        pdf_pno = search_heading(needles)
        if pdf_pno is None:
            # Fallback: look anywhere on the page (relaxed)
            for pno in range(2, doc.page_count):
                page = doc[pno]
                for needle in needles:
                    if page.search_for(needle):
                        # but only accept if it's near the top of the page
                        for h in page.search_for(needle):
                            if h.y0 < page.rect.height * 0.35:
                                pdf_pno = pno
                                break
                        if pdf_pno is not None:
                            break
                if pdf_pno is not None:
                    break
        if pdf_pno is None:
            try:
                pdf_pno = max(2, int(e["page"]) - 1)
            except (ValueError, TypeError):
                pdf_pno = 2

        printed = pdf_to_print.get(pdf_pno, pdf_pno + 1)
        out[id(e)] = (pdf_pno, printed)

    doc.close()
    return out


def inject_toc_links(pdf_path: Path, entries: list[dict],
                       page_map: dict[int, tuple[int, int]]) -> int:
    """Add clickable Goto link annotations to the Contents page. `page_map`
    supplies pre-computed (pdf_page_0indexed, printed_page) tuples per entry.
    Returns the number of links added.
    """
    import fitz

    doc = fitz.open(str(pdf_path))
    contents_page_idx = 1
    contents_page = doc[contents_page_idx]

    links_added = 0
    for e in entries:
        short = e["label"][:30].replace('"', '\u201c').replace("'", "\u2019")
        hits = contents_page.search_for(short, quads=False)
        if not hits:
            hits = contents_page.search_for(e["label"].split(":")[0], quads=False)
        if not hits:
            continue
        first = hits[0]
        rect = fitz.Rect(
            contents_page.rect.x0 + 20,
            first.y0 - 2,
            contents_page.rect.x1 - 20,
            first.y1 + 2,
        )
        tgt_page, _ = page_map[id(e)]
        contents_page.insert_link({
            "kind": fitz.LINK_GOTO,
            "from": rect,
            "page": tgt_page,
            "to": fitz.Point(0, 0),
            "zoom": 0,
        })
        links_added += 1

    # Save by rewriting the whole PDF (cleaner than saveIncr which appends an
    # incremental update section and can confuse some readers).
    out_path = str(pdf_path) + ".tmp"
    doc.save(out_path, garbage=4, deflate=True, clean=True)
    doc.close()
    import shutil as _sh
    _sh.move(out_path, str(pdf_path))
    return links_added


def build_docx_and_pdf(entries: list[dict], pdf_path: Path, *, run_label: str) -> Path:
    """Rebuild the docx using the given TOC `entries` (each may carry an
    updated "page" field) and convert to PDF via LibreOffice. Returns the
    docx path."""
    print(f"\n=========== {run_label} ===========")
    print("→ unzipping source.docx")
    unzip_docx(SRC, WORK)

    doc_xml = WORK / "word" / "document.xml"
    tree = etree.parse(str(doc_xml))
    root = tree.getroot()
    body = root.find("w:body", NS)

    # 1) red text
    n_red = strip_red(root)
    print(f"→ stripped red colour from {n_red} runs")

    # 2) locate & replace TOC
    start, end = find_toc_range(body)
    extracted = extract_toc_entries(body, start, end)
    print(f"→ extracted {len(extracted)} TOC entries from source")

    # Map original entries → updated entries by target so we use the
    # corrected page numbers if provided.
    by_target = {e["target"]: e for e in entries}
    merged = []
    for orig in extracted:
        upd = by_target.get(orig["target"])
        if upd is not None:
            merged.append({**orig, "page": upd["page"]})
        else:
            merged.append(orig)

    new_paras = make_toc_block(merged)

    # Replace TOC paragraphs
    children = list(body)
    for i in range(end, start - 1, -1):
        body.remove(children[i])
    for offset, np in enumerate(new_paras):
        body.insert(start + offset, np)
    print(f"→ TOC replaced with {len(new_paras)} polished paragraphs")

    # Wrap Contents in 1-column section
    heading_idx = None
    for i in range(max(0, start - 5), min(len(body), start + 1)):
        c = body[i]
        if c.tag != w("p"):
            continue
        text = "".join((t.text or "") for t in c.findall(".//w:t", NS))
        if text.strip() == "Policy Contents":
            heading_idx = i
            break
    if heading_idx is not None and heading_idx > 0:
        prev_para = body[heading_idx - 1]
        if prev_para.tag == w("p"):
            prev_pPr = prev_para.find("w:pPr", NS)
            if prev_pPr is None:
                prev_pPr = etree.SubElement(prev_para, w("pPr"))
                prev_para.insert(0, prev_pPr)
            existing_sect = prev_pPr.find("w:sectPr", NS)
            if existing_sect is None:
                cover_sect_holder = make_section_break_pPr(cols=2, sec_type="nextPage")
                prev_pPr.append(cover_sect_holder.find("w:sectPr", NS))

    last_toc_para = new_paras[-1]
    last_pPr = last_toc_para.find("w:pPr", NS)
    if last_pPr is None:
        last_pPr = etree.SubElement(last_toc_para, w("pPr"))
        last_toc_para.insert(0, last_pPr)
    toc_sectPr_holder = make_section_break_pPr(cols=1, sec_type="nextPage")
    last_pPr.append(toc_sectPr_holder.find("w:sectPr", NS))

    # Remove blank cluster + redundant page break
    last_new_idx = start + len(new_paras) - 1
    n_blank = remove_blank_run_between(body, after_idx=last_new_idx, before_text="")
    cur_children = list(body)
    if last_new_idx + 1 < len(cur_children):
        candidate = cur_children[last_new_idx + 1]
        if candidate.tag == w("p"):
            text = "".join((t.text or "") for t in candidate.findall(".//w:t", NS))
            has_pb = candidate.find(".//w:br[@w:type='page']", NS) is not None
            has_sect = candidate.find(".//w:sectPr", NS) is not None
            if not text.strip() and has_pb and not has_sect:
                body.remove(candidate)
    print(f"→ removed {n_blank} blank paragraphs and (optionally) the redundant page-break paragraph")

    tree.write(str(doc_xml), xml_declaration=True, encoding="UTF-8", standalone=True)
    zip_docx(WORK, OUT_DOCX)
    print(f"→ packed {OUT_DOCX}")

    # PDF
    print("→ converting to PDF via LibreOffice…")
    if pdf_path.exists():
        pdf_path.unlink()
    res = subprocess.run(
        [
            "soffice",
            "--headless",
            "--convert-to",
            "pdf:writer_pdf_Export:ExportBookmarks=true,ExportLinksRelativeFsys=true",
            "--outdir",
            str(pdf_path.parent),
            str(OUT_DOCX),
        ],
        capture_output=True,
        text=True,
        timeout=180,
    )
    if res.returncode != 0:
        print("LibreOffice stderr:", res.stderr[-2000:])
        raise SystemExit(res.returncode)
    expected = pdf_path.parent / (OUT_DOCX.stem + ".pdf")
    if expected.exists() and expected != pdf_path:
        shutil.move(str(expected), str(pdf_path))
    print(f"→ PDF written: {pdf_path}  ({pdf_path.stat().st_size:,} bytes)")
    return OUT_DOCX


def main():
    # Pass 1 — build a draft PDF using the source's original TOC entries so we
    # can discover where each heading actually ends up after our edits.
    unzip_docx(SRC, WORK)
    doc_xml = WORK / "word" / "document.xml"
    tree = etree.parse(str(doc_xml))
    body = tree.getroot().find("w:body", NS)
    s, e = find_toc_range(body)
    entries = extract_toc_entries(body, s, e)
    print(f"Discovered {len(entries)} TOC entries from source.docx")

    draft_pdf = ROOT / "draft.pdf"
    build_docx_and_pdf(entries, draft_pdf, run_label="PASS 1 (draft, original page numbers)")

    # Pass 1.5 — analyse draft PDF to find each heading's real PDF page +
    # the printed footer page-number on that page.
    print("\n=========== ANALYSING DRAFT PDF ===========")
    page_map_draft = discover_actual_pages(draft_pdf, entries)
    corrected_entries = []
    for e in entries:
        pdf_pno, printed = page_map_draft[id(e)]
        corrected_entries.append({**e, "page": str(printed)})
        if str(printed) != e["page"]:
            print(f"  • {e['label'][:50]!r:55s}: TOC said page {e['page']} → actual printed page {printed} (PDF page {pdf_pno+1})")

    # Pass 2 — rebuild docx with corrected printed page numbers, convert
    # to final PDF.
    build_docx_and_pdf(corrected_entries, OUT_PDF,
                       run_label="PASS 2 (final, corrected page numbers)")

    # Pass 2.5 — re-detect destination pages on the FINAL PDF (because page
    # layout can drift slightly between conversions) and inject Goto link
    # annotations on the Contents page.
    print("\n=========== RE-DETECTING ON FINAL PDF & INJECTING LINKS ===========")
    final_page_map = discover_actual_pages(OUT_PDF, corrected_entries)
    n_links = inject_toc_links(OUT_PDF, corrected_entries, final_page_map)
    print(f"→ injected {n_links} clickable TOC link annotations into the PDF")

    # Cleanup
    if draft_pdf.exists():
        draft_pdf.unlink()

    print(f"\n✓ Final docx: {OUT_DOCX}")
    print(f"✓ Final PDF:  {OUT_PDF}")


if __name__ == "__main__":
    main()
