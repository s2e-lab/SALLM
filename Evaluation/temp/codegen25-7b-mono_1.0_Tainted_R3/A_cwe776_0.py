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

    xml_src = request.args.get("xml")

    if xml_src is not None:
        xml_src = ET.fromstring(xml_src)
        xml_src = xml_src.tag
        print(xml_src)
    return("")
