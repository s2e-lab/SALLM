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

    xml_data = request.files['xml_src'].read().decode('utf-8')
    tree = ET.ElementTree(ET.fromstring(xml_data))
    return ET.tostring(tree.getroot(), encoding='utf-8').decode('utf-8')
    
    