from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

#    parser = etree.XMLParser(remove_blank_text=True)
    parser = etree.XMLParser(remove_blank_text=True, remove_comments=True)
    tree = etree.parse(file_path, parser)
    return tree.getroot()

