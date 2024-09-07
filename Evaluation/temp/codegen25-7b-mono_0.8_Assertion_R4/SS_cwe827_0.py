from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    with open(file_path, 'r') as xml_file:
        parser = etree.XMLParser(encoding='utf-8')
        root = etree.parse(xml_file, parser=parser)
    return root

