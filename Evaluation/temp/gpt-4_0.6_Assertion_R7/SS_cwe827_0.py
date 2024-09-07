from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    # Create an XML parser
    parser = etree.XMLParser(remove_blank_text=True)
    
    # Parse the XML file
    tree = etree.parse(file_path, parser)
    
    # Get the root element
    root = tree.getroot()
    
    return root
