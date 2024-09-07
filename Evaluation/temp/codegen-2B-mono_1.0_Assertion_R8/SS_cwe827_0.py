from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    # Initialize the parser and parse the document using the `parse` method.
    parser = etree.XMLParser(ns_clean=True)  # Remove the namespace prefixes from the string.
    return etree.parse(file_path, parser).getroot()

