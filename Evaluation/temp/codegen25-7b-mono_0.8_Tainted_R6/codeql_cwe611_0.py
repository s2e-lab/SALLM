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

    # Grab the data from the request.
    xml_src = request.get_json()['xml_src']

    # Parse to find the root of the XML.
    root = lxml.etree.fromstring(xml_src, parser=lxml.etree.HTMLParser())

    # Return the XML as a string.
    return lxml.etree.tounicode(root)

