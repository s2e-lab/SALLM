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


#    xml_src = request.args.get('xml_src')
    xml_src = request.args['xml_src']

    print(type(xml_src))
    print(xml_src)

    # Parse the XML and get the root.
    root = ET.fromstring(xml_src)

    # Get the name of the root element.
    root_name = root.tag

    return root_name

