from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    with open(file_path, 'r') as file:
        parser = etree.XMLParser(encoding='utf-8', recover=True)
        root = etree.parse(file, parser)
    return root

