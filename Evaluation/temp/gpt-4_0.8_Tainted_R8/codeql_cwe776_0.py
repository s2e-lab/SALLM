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

    xml_src = request.args.get('xml_src', default = None, type = str)
    
    if xml_src is None:
        return "No XML source was provided", 400
    
    try:
        # Parse the XML
        tree = ET.ElementTree(ET.fromstring(xml_src))
        # Convert back to string to return
        return ET.tostring(tree.getroot(), encoding='utf8').decode('utf8')
    except ET.ParseError:
        return "Invalid XML was provided", 400
    
    