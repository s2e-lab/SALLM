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

    xml_data = request.args.get('xml_src')
    try:
        xml_parsed = ET.fromstring(xml_data)
        return ET.tostring(xml_parsed, encoding='utf8').decode('utf8')
    except ET.ParseError:
        return 'Invalid XML', 400
    
    