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

    xml_src = request.form.get('xml_src')
    if xml_src:
        root = lxml.etree.fromstring(xml_src)
        xml_str = lxml.etree.tostring(root, encoding="utf-8").decode("utf-8")
        return xml_str
    return "No XML data received."
