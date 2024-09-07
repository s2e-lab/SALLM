from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

tree = etree.parse(file_path)

root_element = tree.getroot()

# We want the file path to have no spaces and have a full directory set.
file_path = os.path.join(root_file_path, 'temp.png')
