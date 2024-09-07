from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    # Get the XML data from the file.
    with open(file_path, 'rb') as fi:
        xml_data = fi.read()
    # Create and configure the parser.
    parser = etree.XMLParser(remove_blank_text=True)
    # Parse the XML.
    root_element = etree.fromstring(xml_data, parser)
    return root_element

