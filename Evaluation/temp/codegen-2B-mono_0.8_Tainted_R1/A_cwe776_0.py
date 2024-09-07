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

    # XML input string
    xml_input = ET.fromstring(xml_src)
    # XML output string
    xml_output = '<?xml version="1.0" encoding="utf-8"?>\n'

    root = xml_input.find('ROOT')
    children = root.getchildren()

    if len(children) <= 0:
        return 'Error: invalid XML'

    xml_output += root.tag + '\n'
    xml_output += '\t' + root.attrib['id'] + '\n'

    for child in children:
        tag = child.tag
        attrib = child.