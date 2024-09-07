from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    # Load the file
    xml_data = etree.parse(file_path)

    # Select its root element
    root_element = xml_data.getroot()

    return root_element

