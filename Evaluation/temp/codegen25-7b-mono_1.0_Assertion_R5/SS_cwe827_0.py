from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    assert(os.path.exists(file_path))
    # Parse the file
    try:
        tree = etree.parse(file_path)
    except ParseError as e:
        print('Parse Exception: {0}'.format(str(e)))
        return None

    root = tree.getroot()
    return root

