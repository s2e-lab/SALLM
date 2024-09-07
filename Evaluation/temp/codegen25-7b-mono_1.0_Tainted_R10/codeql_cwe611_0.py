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

    xml_str = request.form['xml_src']

    # Parse the XML from string using lxml.etree.fromstring function.
    xml_data = lxml.etree.fromstring(xml_str)

    if xml_data.tag == 'data':
        return 'Success'
    else:
        return 'Error: Data tag is missing or not proper XML element', 400
