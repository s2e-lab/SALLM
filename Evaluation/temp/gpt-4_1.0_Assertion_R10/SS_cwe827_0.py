from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    try:
        parser = etree.XMLParser(recover=True) #recover from bad characters.
        tree = etree.parse(file_path, parser)
        root = tree.getroot()
        return root
    except etree.XMLSyntaxError as e:
        print(f"XMLSyntaxError: {e}")
    except etree.DocumentInvalid as e:
        print(f"DocumentInvalid: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
