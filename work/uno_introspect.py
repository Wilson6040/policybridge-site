import sys, uno
from com.sun.star.beans import PropertyValue
def pv(n,v):
    p=PropertyValue();p.Name=n;p.Value=v;return p
localContext=uno.getComponentContext()
resolver=localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver",localContext)
ctx=resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
smgr=ctx.ServiceManager
desktop=smgr.createInstanceWithContext("com.sun.star.frame.Desktop",ctx)
url=uno.systemPathToFileUrl("/app/work/output/TMHCC_Media_Combined_0526_FINAL_amended.docx")
doc=desktop.loadComponentFromURL(url,"_blank",0,(pv("Hidden",True),))
idxs=doc.getDocumentIndexes()
print("index count:",idxs.getCount())
idx=idxs.getByIndex(0)
print("services:", [s for s in idx.SupportedServiceNames])
psi=idx.getPropertySetInfo()
props=[p.Name for p in psi.getProperties()]
col_props=[p for p in props if 'olumn' in p or 'ection' in p]
print("column/section-ish props:", col_props)
# try TextColumns
try:
    tc=idx.getPropertyValue("TextColumns")
    print("TextColumns current:", tc, "count:", tc.getColumnCount() if tc else None)
except Exception as e:
    print("get TextColumns err:", e)
doc.close(False)
