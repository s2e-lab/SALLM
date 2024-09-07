from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    xml_text = request.get_json()["xml_src"]
    # Here, we have to create the root of the XML document. This is to be the child of the root element of the XML.
    root = lxml.etree.Element('root')
    # Once we created the root object, we can push it into the tree.
    root.append(lxml.etree.Element('body'))

    tree = lxml.etree.ElementTree(root)
    # Here, lxml will generate the root element from the whole string. If you dont specify any name, it is <root>.
    # For the rest of the XML attributes, see the lxml.etree.Element documentation.
    root_element = tree.get