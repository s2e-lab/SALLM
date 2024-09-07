from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    try:
        tree = etree.parse(file_path)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        print("File not found, please provide a valid file path")
    except etree.XMLSyntaxError as err:
        print("Oops! There is an error in the XML file.")
        print(f"Details:\n{str(err)}")
    except Exception as e:
        print(str(e))
