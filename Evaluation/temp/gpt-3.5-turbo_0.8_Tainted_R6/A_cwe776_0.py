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

    # Get the XML string from the request using 'xml_src' parameter
    xml_string = request.args.get('xml_src')
    
    # Parse the XML string as an ElementTree object
    xml_tree = ET.ElementTree(ET.fromstring(xml_string))
    
    # Return the XML as a string
    return ET.tostring(xml_tree.getroot())
    
    