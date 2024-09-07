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

    xml_str = request.args['xml_src']
    xml = lxml.etree.fromstring(xml_str)
    xml_tree = xml.getroottree()
    # print('xml_tree:', xml_tree.getelementinfo(['{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation', '']))
    return xml_tree
