from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    parser = etree.XMLParser(huge_tree=True)
    xml = etree.parse(file_path, parser)
    return xml.getroot()

