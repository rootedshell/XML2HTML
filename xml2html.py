import lxml.html
from lxml import etree
 
xslt_doc = etree.parse("test.xslt")
xslt_transformer = etree.XSLT(xslt_doc)
 
source_doc = etree.parse("test.xml")
output_doc = xslt_transformer(source_doc)
 
print(str(output_doc))
output_doc.write("out.html", pretty_print=True)
