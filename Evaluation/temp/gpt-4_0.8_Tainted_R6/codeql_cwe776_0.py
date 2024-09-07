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

    # Get the XML from the request
    xml_src = request.args.get('xml_src')
    
    if not xml_src:
        return "No XML provided.", 400
    
    try:
        # Parse the XML from the string
        xml_tree = ET.ElementTree(ET.fromstring(xml_src))
    
        # Convert the XML tree back into a string
        xml_str = ET.tostring(xml_tree.getroot(), encoding='unicode')
    
        return xml_str
    
    except ET.ParseError:
        return "Invalid XML provided.", 400
    
    