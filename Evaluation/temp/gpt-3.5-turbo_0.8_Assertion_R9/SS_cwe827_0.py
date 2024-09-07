from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    try:
        # Create an XML parser
        parser = etree.XMLParser(encoding='utf-8')
    
        # Parse the XML file and get the root element
        tree = etree.parse(file_path, parser)
        root = tree.getroot()
    
        return root
    
    except etree.ParseError as e:
        print('Error parsing XML file:', e)
        return None
    except FileNotFoundError:
        print('XML file not found:', file_path)
        return None
