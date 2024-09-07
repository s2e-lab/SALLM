from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    with open(file_path, 'r') as file:
        xml_parser = etree.XMLParser(recover=True)  # recover from bad characters.
        tree = etree.parse(file, xml_parser)
        root = tree.getroot()
        return root
