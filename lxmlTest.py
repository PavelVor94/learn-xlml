from lxml import etree

root = etree.Element('html' , version='5.0')

etree.SubElement(root, 'head')
etree.SubElement(root, 'title' , bgcolor='red' , fontsize='22')
etree.SubElement(root, 'body' , fontsize='15')

root.append(etree.Element('foot'))

root.set('newAttr' , 'attrValue')

root.text = 'This is HTML file'
for element in root:
    element.text = 'This is the '+element.tag+" of that file"

print (etree.tostring(root, pretty_print= True).decode('utf-8'))
print(root.tag)

for element in root:
    print(element.tag)

print(root.get('newAttr'))
print(root[1].get('bgcolor'))
print(etree.iselement(root[1]))
print(root.getparent())
print(root[1].getparent())
print(root[1].getnext())
print(root[1].getprevious())
print(root.find('head').tag)
print(root.findtext('title'))