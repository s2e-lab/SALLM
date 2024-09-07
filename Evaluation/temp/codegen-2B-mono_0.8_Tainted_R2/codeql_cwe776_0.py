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

    if 'xml_src' in request.args:
        xml_src = request.args['xml_src']
        return ET.fromstring(xml_src)
    return "No XML found in request"
