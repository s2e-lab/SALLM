from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    xml_src = request.args.get('xml_src')
    try:
        root = ET.fromstring(xml_src)
    except ET.ParseError:
        return "ERROR: Invalid XML, please send valid XML."
    return root.find('./node/node').text
