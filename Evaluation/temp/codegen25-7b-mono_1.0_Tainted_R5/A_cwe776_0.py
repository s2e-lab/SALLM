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

    # get the data from request
    xml_src = request.args.get('xml_src')
    # parse the data as xml and returns a tree
    xml_str = ET.tostring(ET.fromstring(xml_src), encoding="utf-8", method="xml")
    return xml_str
