from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

#     parser = etree.XMLParser(remove_blank_text=True)
    parser = etree.XMLParser()
    try:
        tree = etree.parse(file_path, parser)
    except IOError:
        print("Error: Could not open file: %s" % file_path)
        sys.exit(1)
    except etree.XMLSyntaxError as e:
        print("Error: Could not parse XML file: %s" % file_path)
        print("Reason: %s" % e)
        sys.exit(1)
    return tree.getroot()

