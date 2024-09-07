from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

#     parser = etree.XMLParser(resolve_entities=False)
    parser = etree.XMLParser()
    tree = etree.parse(file_path, parser)
    root_element = tree.getroot()
    return root_element
