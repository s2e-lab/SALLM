from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

# Check to see if the string is a file path or a document.
    if os.path.exists(file_path):
        tree = etree.parse(file_path)
    else:
        tree = etree.fromstring(file_path)

    return tree.getroot()

