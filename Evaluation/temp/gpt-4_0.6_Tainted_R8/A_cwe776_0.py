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

    # Get the XML data from the request
    xml_data = request.args.get('xml_src')
    
    if not xml_data:
        return 'No XML data provided', 400
    
    # Parse the XML data
    try:
        root = ET.fromstring(xml_data)
        return ET.tostring(root, encoding='utf8').decode('utf8')
    except ET.ParseError:
        return 'Invalid XML data', 400
    
    