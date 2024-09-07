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
    xml_tree = ET.ElementTree(ET.fromstring(xml_src))
    xml_str = ET.tostring(xml_tree.getroot(), encoding='utf8').decode('utf8')
    return xml_str
    
    