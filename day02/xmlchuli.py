import xml.etree.ElementTree as et
tree = et.parse('zmltest.xml')
root = tree.getroot()
print(root)
print(root.tag)
for item in root:
    print(item,item.attrib)
    for i in item:
        print(i.tag,i.text)

for items in root.iter('year'):
    print(items.tag,items.text)