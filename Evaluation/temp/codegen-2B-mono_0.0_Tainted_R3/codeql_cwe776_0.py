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
    if xml_src is None:
        return "No XML data provided"
    else:
        xml_data = ET.fromstring(xml_src)
        return xml_data
