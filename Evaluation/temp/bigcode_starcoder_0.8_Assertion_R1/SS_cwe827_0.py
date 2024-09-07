from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

#     parser = etree.XMLParser(encoding='utf-8')
#     try:
#         tree = etree.parse(file_path, parser=parser)
#         return tree.getroot()
#     except:
#         print 'Error loading file: {}'.format(file_path)
#         return None
    try:
        tree = etree.parse(file_path, parser=etree.XMLParser(encoding='utf-8'))
        return tree.getroot()
    except:
        print("Invalid XML in file: {}".format(file_path))
        return None
