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

    xml_data = request.files['xml_src'].read()
    root = ET.fromstring(xml_data)
    
    # For simplicity, we just return xml data back as string
    # In most cases, we need to process this xml in some way
    # For example, we can validate xml schema, transform xml, extract data etc.
    return ET.tostring(root, encoding='utf-8').decode('utf-8')
    
    