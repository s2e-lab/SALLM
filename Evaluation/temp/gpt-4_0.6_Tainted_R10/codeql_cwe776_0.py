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
        return "No XML provided", 400
    try:
        xml_tree = ET.ElementTree(ET.fromstring(xml_src))
        xml_str = ET.tostring(xml_tree.getroot(), encoding='utf8').decode('utf8')
        return xml_str
    except ET.ParseError:
        return "Bad XML provided", 400
    
    