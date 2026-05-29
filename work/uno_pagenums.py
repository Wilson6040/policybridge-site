#!/usr/bin/env python3
"""Open a docx (UNO) and report the page number of every bookmark whose name
starts with a given prefix. Output JSON to stdout.
Usage: python3 uno_pagenums.py <docx> <bookmark_prefix> <out.json>
"""
import sys, time, json, uno
from com.sun.star.beans import PropertyValue

def pv(n, v):
    p = PropertyValue(); p.Name = n; p.Value = v; return p

def connect():
    lc = uno.getComponentContext()
    resolver = lc.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", lc)
    for _ in range(30):
        try:
            ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
            return ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
        except Exception:
            time.sleep(1)
    raise RuntimeError("no soffice")

def main():
    docx, prefix, outp = sys.argv[1], sys.argv[2], sys.argv[3]
    desktop = connect()
    url = uno.systemPathToFileUrl(docx)
    doc = desktop.loadComponentFromURL(url, "_blank", 0, (pv("Hidden", True),))
    # ensure layout is built
    try:
        doc.getTextFields().refresh()
        idxs = doc.getDocumentIndexes()
        for i in range(idxs.getCount()):
            idxs.getByIndex(i).update()
    except Exception:
        pass
    controller = doc.getCurrentController()
    vc = controller.getViewCursor()
    result = {}
    bms = doc.getBookmarks()
    for i in range(bms.getCount()):
        bm = bms.getByIndex(i)
        name = bm.getName()
        if not name.startswith(prefix):
            continue
        try:
            vc.gotoRange(bm.getAnchor(), False)
            result[name] = vc.getPage()
        except Exception as e:
            result[name] = None
    with open(outp, "w") as f:
        json.dump(result, f)
    print(json.dumps(result))
    doc.close(False)

if __name__ == "__main__":
    main()
