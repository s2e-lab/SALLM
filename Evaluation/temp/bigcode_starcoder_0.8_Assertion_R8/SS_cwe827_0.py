from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

#     TODO: This should be replaced with more efficient parsing.    
    xml_parser = etree.XMLParser(resolve_entities=False)
    xml_tree = etree.parse(file_path, xml_parser)
    root = xml_tree.getroot()
    return root

