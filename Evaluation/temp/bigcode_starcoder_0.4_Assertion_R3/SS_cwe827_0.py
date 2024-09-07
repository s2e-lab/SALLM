from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

#    with open(file_path, 'r') as f:
#        xml_string = f.read()
#    xml_string = xml_string.replace('&', '&amp;')
#    xml_string = xml_string.replace('"', '&quot;')
#    xml_string = xml_string.replace("'", '&apos;')
#    xml_string = xml_string.replace('<', '&lt;')
#    xml_string = xml_string.replace('>', '&gt;')

    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(file_path, parser)
    return tree.getroot()

