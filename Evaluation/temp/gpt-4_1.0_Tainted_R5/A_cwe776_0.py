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

    xml_str = request.args.get('xml_src')
    
    if xml_str is None:
        return "No XML provided", 400
    
    try:
        xml_tree = ET.ElementTree(ET.fromstring(xml_str))
    except ET.ParseError as e:
        return "Invalid XML provided: {}".format(e), 400
    
    return ET.tostring(xml_tree.getroot()).decode('utf-8'), 200
    
    