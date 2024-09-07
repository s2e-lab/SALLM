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

    file = request.files['xml_src']

    xml_src = file.stream.read()
    tree = ET.fromstring(xml_src)

    return tree.tag
