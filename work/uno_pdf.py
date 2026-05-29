#!/usr/bin/env python3
"""Open a .docx via LibreOffice (UNO), refresh all fields + document indexes
(so a TOC field builds with real page numbers), then export to PDF.

Usage: python3 uno_pdf.py <input.docx> <output.pdf>
Requires a running soffice listener:
  soffice --headless --invisible --nofirststartwizard \
          --accept="socket,host=localhost,port=2002;urp;"
"""
import sys, time, os
import uno
from com.sun.star.beans import PropertyValue


def connect(retries=30):
    localContext = uno.getComponentContext()
    resolver = localContext.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", localContext)
    last = None
    for _ in range(retries):
        try:
            ctx = resolver.resolve(
                "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
            smgr = ctx.ServiceManager
            desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
            return desktop
        except Exception as e:  # noqa
            last = e
            time.sleep(1)
    raise RuntimeError(f"Could not connect to soffice: {last}")


def pv(name, value):
    p = PropertyValue(); p.Name = name; p.Value = value
    return p


def main():
    inp = os.path.abspath(sys.argv[1])
    out = os.path.abspath(sys.argv[2])
    desktop = connect()
    in_url = uno.systemPathToFileUrl(inp)
    out_url = uno.systemPathToFileUrl(out)
    doc = desktop.loadComponentFromURL(in_url, "_blank", 0, (pv("Hidden", True),))
    try:
        # refresh all text fields (PAGE, etc.)
        try:
            doc.getTextFields().refresh()
        except Exception as e:
            print("field refresh warn:", e)
        # update all document indexes (Table of Contents); optionally 2 columns
        two_col = os.environ.get("TOC_TWO_COL") == "1"
        try:
            idxs = doc.getDocumentIndexes()
            for i in range(idxs.getCount()):
                idx = idxs.getByIndex(i)
                idx.update()
                if two_col:
                    try:
                        cols = doc.createInstance("com.sun.star.text.TextColumns")
                        cols.setColumnCount(2)
                        idx.setPropertyValue("TextColumns", cols)
                        # also apply to the content section if present
                        try:
                            cs = idx.getPropertyValue("ContentSection")
                            cols2 = doc.createInstance("com.sun.star.text.TextColumns")
                            cols2.setColumnCount(2)
                            cs.setPropertyValue("TextColumns", cols2)
                        except Exception as e2:
                            print("content-section col warn:", e2)
                        print("index", i, "columns now:", idx.getPropertyValue("TextColumns").getColumnCount())
                    except Exception as e:
                        print("col set warn:", e)
            print("indexes updated:", idxs.getCount())
        except Exception as e:
            print("index update warn:", e)
        # recalculate / reformat
        try:
            doc.calculateAll()
        except Exception:
            pass
        doc.storeToURL(out_url, (pv("FilterName", "writer_pdf_Export"),))
        print("PDF written:", out)
    finally:
        doc.close(False)


if __name__ == "__main__":
    main()
