from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    try:
        fh = open(file_path, 'r')
    except:
        raise NameError("Unable to read from the file")
    parser = etree.XMLParser(resolve_entities=False)
    doc = etree.parse(fh, parser)
    return doc.getroot()

