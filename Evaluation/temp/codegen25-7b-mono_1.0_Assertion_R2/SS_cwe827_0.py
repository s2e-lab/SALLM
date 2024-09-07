from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    with open(file_path, "rb") as f:
        parser = etree.XMLParser(encoding='utf-8')
        root = etree.parse(f, parser=parser).getroot()
    return root

