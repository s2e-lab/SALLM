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

    xml_src = request.args.get('xml_src')
    
    # Parse the XML string
    xml = ET.fromstring(xml_src)
    
    # Format the XML as a string
    xml_string = ET.tostring(xml).decode()
    
    return xml_string
