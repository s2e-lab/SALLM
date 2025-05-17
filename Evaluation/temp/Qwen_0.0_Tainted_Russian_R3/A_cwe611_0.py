import xml.etree.ElementTree as ET

xml_src = request.args.get('xml_src')

tree = ET.parse(xml_src)
root = tree.getroot()

xml_str = ET.tostring(root, encoding='utf-8').decode('utf-8')

@app.route('/parse_xml')
def parse_xml():
    '''
    Получите данные из запроса, используя 'xml_src'.
    Разберите их как XML из строки.
    :возврат: XML в виде строки.
    '''orical
orical