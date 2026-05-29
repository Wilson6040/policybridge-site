import sys
sys.path.insert(0, '/app/work/compare')
from docx import Document
import brand2 as b

doc = Document()
b.set_normal_style(doc)
b.setup_page(doc, landscape=True, margin_cm=1.5)
b.add_logo_header(doc)
b.add_footer_pagenum(doc)

b.cover_page(
    doc,
    doc_kicker="Smoke Test",
    title="Branding Pipeline Test",
    subtitle="Validating logo, fonts, palette, legend, landscape matrix and PDF export.",
    meta_lines=["Indicative wording comparison — broking reference only.",
                "Subject to TMHCC legal/underwriting sign-off."],
    wordings=["TMHCC — master wording", "Tysers (Zurich)", "Yutree (AXA)", "Liberty", "Allianz"],
)

doc.add_page_break()
b.h1(doc, "Coverage comparison at a glance", num="1")
b.legend_bar(doc)
headers = ["Section of cover", "TMHCC", "Tysers\n(Zurich)", "Yutree\n(AXA)", "Liberty", "Allianz", "Wording E\n(pending)", "Comment"]
widths = [6.0, 1.6, 1.9, 1.9, 1.7, 1.7, 1.9, 8.0]
t = b.make_table(doc, headers, widths)
rows = [
    ("Section 12 · Media Liability / PI", "yes", "yes", "yes", "no", "no", "pending",
     "TMHCC, Tysers (S8 PI/E&O) and Yutree (PI-Media) all offer media/PI; Liberty and Allianz do not."),
    ("Section 15 · Cyber Liability", "yes", "no", "partial", "no", "no", "pending",
     "Only TMHCC offers standalone cyber (CyberGuard). Yutree has computer-breakdown only."),
]
for label, *st, comment in rows:
    cells = t.add_row().cells
    b.text_cell(cells[0], label, size=8.5, bold=True, color=b.TEAL)
    for j, key in enumerate(st):
        b.status_cell(cells[1 + j], key)
    b.text_cell(cells[7], comment, size=8)
b.zebra(t)

b.spacer(doc, 8)
b.callout(doc, "Reviewer note:", "This is a pipeline smoke test only.")

out = "/app/work/compare/out/_smoke.docx"
b.save_doc(doc, out)
print("DOCX saved:", out)
pdf = b.to_pdf(out, "/app/work/compare/out")
print("PDF:", pdf)
