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

    # Get the data from the request
    xml_src = request.args.get('xml_src')
    
    # Parse the XML
    root = ET.fromstring(xml_src)
    
    # Convert the parsed XML to a string
    xml_str = ET.tostring(root)
    
    return xml_str
