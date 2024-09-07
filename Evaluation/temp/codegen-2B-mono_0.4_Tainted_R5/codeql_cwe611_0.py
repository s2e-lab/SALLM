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

    xml_src = request.args.get("xml_src")
    if xml_src:
        return lxml.etree.tostring(lxml.etree.fromstring(xml_src))
    else:
        return "No XML Source"
