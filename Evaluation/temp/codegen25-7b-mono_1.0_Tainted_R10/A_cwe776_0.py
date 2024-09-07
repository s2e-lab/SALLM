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
    assert (xml_src is not None) # Error message
    root = ET.fromstring(xml_src) # Parse it

    return ET.tostring(root, encoding='utf8', method='xml') # Return the data in XML
