from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    # Create a parser object
    parser = etree.XMLParser(recover=True)
    
    # Parse the XML file and get the root element
    root = etree.parse(file_path, parser).getroot()
    
    return root
