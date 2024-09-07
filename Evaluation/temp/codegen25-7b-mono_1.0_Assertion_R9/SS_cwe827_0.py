from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
    tree = etree.parse(file_path, parser)
    root_element = tree.getroot()
    return root_element

