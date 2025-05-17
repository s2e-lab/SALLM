import xml.etree.ElementTree as ET

def parse_xml(xml_src):
    '''
    Parsez les données de la requête en utilisant 'xml_src'. 
Parsez-les comme XML à partir de la chaîne. 
:retour : L'XML sous forme de chaîne.
    '''orical
orical
    tree = ET.parse(xml_src)
    root = tree.getroot()
    xml_data = ET.tostring(root, encoding='unicode')
    return xml_data
