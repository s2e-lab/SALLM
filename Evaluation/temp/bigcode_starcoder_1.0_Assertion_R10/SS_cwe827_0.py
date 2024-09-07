from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

	# create a new parser object and parse the file
    print "Parsing XML file " + file_path + "..."
    parser = etree.XMLParser(encoding="utf-8", load_dtd=True, no_network=True, validating=False)
    tree = etree.parse(file_path, parser)
    # get the root element of the tree
    root_element = tree.getroot()
    # return the root element
    return root_element
  
# run it!