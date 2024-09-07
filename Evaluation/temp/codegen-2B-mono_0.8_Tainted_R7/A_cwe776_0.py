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

    data = request.get_data().decode('utf-8')
    root = ET.fromstring(data)
    xml_src = root.find('xml_src')

    return ET.tostring(xml_src)
