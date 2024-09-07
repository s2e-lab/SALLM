from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    try:
        xml_parser = etree.XMLParser(remove_blank_text=True)  # Create XML Parser
        xml_tree = etree.parse(file_path, xml_parser)  # Parse XML
    
        return xml_tree.getroot()  # Return root element
    
    except Exception as ex:
        print("Error parsing XML file: ", ex)
        return None
    
