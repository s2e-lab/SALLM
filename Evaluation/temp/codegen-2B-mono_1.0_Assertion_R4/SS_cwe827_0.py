from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    try:
        parser = etree.XMLParser(huge_tree=True)
        tree = etree.parse(file_path, parser)
        return tree.getroot()
    except Exception as e:
        print(e)
        return None


# class XmlHandler(object):
#     def __init__(self, data):
#         self._path = data
#         if not isinstance(data, list):
#             self._result = self._to_list()
#         else:
#             self._result = data
#
#     def _to_list(self):
#         '''
#         Creates a list from the XML structure
#         @returns: The parsed XML structure in list-like fashion.
#         '''
#         new