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

#    xml_src = request.form['xml_src']
#    xml_str = xml_src.encode('ascii', 'ignore')
#    xml_root = ET.fromstring(xml_str)
#    xml_str = ET.tostring(xml_root)
    with open('test.xml') as xml_input:
        xml_str = xml_input.read()
    return xml_str
