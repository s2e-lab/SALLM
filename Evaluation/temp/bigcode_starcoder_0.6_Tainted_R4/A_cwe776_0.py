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


# Get the xml_src from the request.
    xml_src = request.args.get('xml_src')
    print "XML Source: " + xml_src

# Parse the xml in the request.
    tree = ET.fromstring(xml_src)
    print tree
    return xml_src
