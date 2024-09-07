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

    # get the source of the request payload
    xml_src = request.data

    # load it as XML from the string
    xml_tree = lxml.etree.parse(xml_src)

    # get the root of the tree
    root = xml_tree.getroot()

    # dump it out as a string
    xml_string_src = str(lxml.etree.tostring(root))
    xml_string_src = xml_string_src.strip('\n')

    return xml_string_src
