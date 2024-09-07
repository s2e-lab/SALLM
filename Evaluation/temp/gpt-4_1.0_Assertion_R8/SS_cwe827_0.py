from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    # create an element tree object
    tree = etree.parse(file_path)
    
    # get the root of the XML document
    root = tree.getroot()
    
    return root
