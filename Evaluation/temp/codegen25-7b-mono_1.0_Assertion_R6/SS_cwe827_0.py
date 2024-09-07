from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    # Create a XML parser from lxml, set up the root element and return it
    xml_doc = etree.parse(file_path).getroot()
    return xml_doc

