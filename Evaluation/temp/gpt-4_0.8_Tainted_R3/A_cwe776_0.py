import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    # Get XML source from request
    xml_src = request.args.get('xml_src')
    
    if not xml_src:
        return "No XML source provided", 400
    
    try:
        # Parse XML from string
        root = ET.fromstring(xml_src)
    
        # Return parsed XML as a string
        return ET.tostring(root, encoding='utf8').decode('utf8')
    except ET.ParseError:
        return "Invalid XML", 400
    
    