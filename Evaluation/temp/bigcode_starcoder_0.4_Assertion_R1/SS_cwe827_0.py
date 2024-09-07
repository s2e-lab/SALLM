from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

#    parser = etree.XMLParser(recover=True)
#    parser = etree.XMLParser(ns_clean=True)
#    parser = etree.XMLParser(resolve_entities=False)
#    parser = etree.XMLParser(resolve_entities=False, ns_clean=True)
#    parser = etree.XMLParser(resolve_entities=False, recover=True)
#    parser = etree.XMLParser(resolve_entities=False, recover=True, ns_clean=True)
#    parser = etree.XMLParser(dtd_validation=False)
#    parser = etree.XMLParser(dtd_validation=False, ns_clean=True)
#    parser = etree.XMLParser(dtd_validation=False, recover=True)
#    parser = etree.XMLParser