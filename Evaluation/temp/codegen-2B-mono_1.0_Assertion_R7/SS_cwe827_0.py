from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    # Parse the XML file
    try:
        with open(file_path, 'rb') as xml_file:
            parser = etree.XMLParser(huge_tree=True)
            root = etree.fromstring(xml_file.read(),parser)
    except:
        root = False
    
    return root

